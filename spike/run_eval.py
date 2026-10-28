"""Spike eval harness: run the claims-agent prompt on one model and score it.

- The agent prompt is loaded from .claude/skills/claims-agent/SKILL.md, so the
  Skill and the spike never drift.
- Cases come from spike/eval_set.jsonl (built by spike/build_eval_set.py).
- Scoring is deterministic: structured fields compared with the consultant's
  expected outcomes. No LLM-as-judge.
- One trace line per decision is appended to spike/traces/<model>.jsonl (NF-01
  to NF-04). A run summary goes to spike/runs/<run_id>__<model>.json.
- The API key is read from .env as SPIKE_ANTHROPIC_API_KEY and passed to the
  client directly. It is never put in the environment (ground rule 8).

Usage:
  .venv/bin/python spike/run_eval.py --model claude-sonnet-5-5 --estimate --assume-output-tokens N
  .venv/bin/python spike/run_eval.py --model claude-sonnet-5-5 --ids K04/decision_point
  .venv/bin/python spike/run_eval.py --model claude-sonnet-5-5
"""
import argparse
import json
import sys
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parent.parent
SPIKE = ROOT / "spike"
SKILL = ROOT / ".claude" / "skills" / "claims-agent" / "SKILL.md"

# USD per million tokens. Source: claude-api reference (Anthropic first-party
# rates, cached 2026-10-06). Cache writes are 1.25x input (5-minute TTL).
# Haiku 5.5's cache-read rate is not listed there; the documented ~0.1x of
# input is used and labelled.
PRICES = {
    "claude-opus-5-5":   {"input": 4.00,  "output": 20.00, "cache_read": 0.20},
    "claude-sonnet-5-5": {"input": 2.00,  "output": 10.00, "cache_read": 0.20},
    "claude-haiku-5-5":  {"input": 0.10,  "output": 0.50,  "cache_read": 0.01},  # 0.1x input, assumption
    "claude-fable-5-1":  {"input": 10.00, "output": 50.00, "cache_read": 0.25},
}
CACHE_WRITE_MULTIPLIER = 1.25

STEP4_FIELDS = ("rubric_score", "rubric_items", "self_reported_confidence")


# ---------------------------------------------------------------- prompt and schema
def load_prompt():
    parts = SKILL.read_text().split("\n---\n")
    assert len(parts) == 3, "SKILL.md: frontmatter, header, then the prompt after a --- line"
    return parts[2].strip()


def nullable(schema):
    return {"anyOf": [schema, {"type": "null"}]}


def obj(props, required=None):
    return {"type": "object", "properties": props,
            "required": required or list(props), "additionalProperties": False}


RULES = [f"R{i}" for i in range(1, 17)] + ["G12"]
STR = {"type": "string"}
PASS_FAIL = {"type": "string", "enum": ["pass", "fail"]}

OUTPUT_SCHEMA = obj({
    "claim_id": STR,
    "status": {"type": "string", "enum": ["held", "routed", "withdrawn"]},
    "route": nullable({"type": "string", "enum": ["autonomous", "sign_off", "escalate"]}),
    "decision": nullable({"type": "string", "enum": ["approve", "partial", "deny"]}),
    "amount": nullable({"type": "number"}),
    "rule_applied": {"type": "string", "enum": RULES},
    "triggers": {"type": "array", "items": {"type": "string", "enum": RULES}},
    "rubric_score": nullable({"type": "number"}),
    "rubric_items": nullable(obj({f"RB{i}": PASS_FAIL for i in range(1, 7)})),
    "self_reported_confidence": nullable({"type": "number"}),
    "rationale": STR,
    "hold": nullable(obj({
        "hold_reason": {"type": "string", "enum": ["awaiting_documents"]},
        "missing_items": {"type": "array", "items": STR},
        "reminders_sent": {"type": "array", "items": STR},
        "fallback_date": STR,
        "duplicate_flag": {"type": "boolean"},
    })),
    "fact_pack": nullable(obj({
        "triggers": {"type": "array", "items": {"type": "string", "enum": RULES}},
        "checklist_status": {"type": "array", "items": obj({
            "item": STR, "status": {"type": "string", "enum": ["received", "missing"]}})},
        "clocks": obj({
            "reefer": nullable(STR),
            "insurer": nullable(obj({"delivery_date": nullable(STR), "receipt_date": STR})),
        }),
        "expedite": nullable(obj({"requester": STR, "request_time": STR, "answer_due": STR})),
        "queue": {"type": "string", "enum": ["claims_lead", "specialist"]},
        "key_account": {"type": "boolean"},
    })),
    "steps": {"type": "array", "items": obj({"step": STR, "result": STR})},
    "checks": {"type": "array", "items": obj({"check": STR, "fired": {"type": "boolean"}})},
})


def user_message(inp):
    return "Evaluate this claim.\n\n```json\n" + json.dumps(inp, indent=2, ensure_ascii=False) + "\n```"


# ---------------------------------------------------------------- scoring
def score(out, exp):
    """Deterministic comparison with the expected outcome (expected-outcomes-v1.md conventions)."""
    if out is None:
        return {"pass": False, "fields": {}, "gate_held": False, "triggers_match": False}
    route, rule = out.get("route"), out.get("rule_applied")
    f = {"status": out.get("status") == exp["status"]}
    if exp["autonomous_star"]:
        # E-a: autonomous (R15, approve) or sign-off via a failed gate (R14) both count.
        auto = route == "autonomous" and rule == "R15"
        held = route == "sign_off" and rule == "R14"
        f["route"] = auto or held
        f["rule_applied"] = auto or held
        if auto:
            f["decision"] = out.get("decision") == "approve"
    else:
        f["route"] = route == exp["route"]
        f["rule_applied"] = rule in exp["rule_applied"]
        if exp["decision_scored"]:
            f["decision"] = out.get("decision") == exp["decision"]
    return {
        "pass": all(f.values()),
        "fields": f,
        "gate_held": exp["autonomous_star"] and route == "sign_off" and rule == "R14",
        "triggers_match": sorted(out.get("triggers") or []) == sorted(exp["triggers"]),
    }


# ---------------------------------------------------------------- model call
def cost_usd(model, usage):
    p = PRICES[model]
    return (usage["input_tokens"] * p["input"]
            + usage["cache_creation_input_tokens"] * p["input"] * CACHE_WRITE_MULTIPLIER
            + usage["cache_read_input_tokens"] * p["cache_read"]
            + usage["output_tokens"] * p["output"]) / 1_000_000


def call(client, model, effort, system, case):
    kwargs = dict(
        model=model,
        max_tokens=16000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_message(case["input"])}],
        output_config={"format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
    )
    if effort:
        kwargs["output_config"]["effort"] = effort
    started = time.perf_counter()
    error, out, resp = None, None, None
    try:
        resp = client.messages.create(**kwargs)
    except anthropic.APIStatusError as e:
        error = f"{type(e).__name__} {e.status_code}: {e.message}"
    except anthropic.APIConnectionError as e:
        error = f"{type(e).__name__}: {e}"
    latency = time.perf_counter() - started

    usage = {k: 0 for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}
    stop_reason, request_id = None, None
    if resp is not None:
        stop_reason, request_id = resp.stop_reason, resp._request_id
        for k in usage:
            usage[k] = getattr(resp.usage, k, 0) or 0
        if stop_reason == "end_turn":
            text = next((b.text for b in resp.content if b.type == "text"), None)
            try:
                out = json.loads(text)
            except (TypeError, json.JSONDecodeError) as e:
                error = f"unparseable output: {e}"
        else:
            error = f"stop_reason {stop_reason}"
    return out, usage, latency, stop_reason, request_id, error


def trace_record(run_id, model, effort, case, out, usage, latency, stop_reason, request_id, error, result):
    """NF-02: inputs seen, steps reached, checks evaluated, full output, model, tokens, latency, cost."""
    inp = case["input"]
    return {
        "run_id": run_id,
        "eval_id": case["id"],
        "group": case["group"],
        "claim_id": inp["claim_id"],
        "evaluation_time": inp["evaluation_time"],
        "event": inp["event"],
        "inputs": inp,
        "steps": (out or {}).get("steps"),
        "checks": (out or {}).get("checks"),
        "output": {k: v for k, v in (out or {}).items() if k not in ("steps", "checks")} or None,
        "model": model,
        "effort": effort,
        "usage": usage,
        "latency_s": round(latency, 3),
        "cost_usd": round(cost_usd(model, usage), 6),
        "stop_reason": stop_reason,
        "request_id": request_id,
        "error": error,
        "expected": case["expected"],
        "score": result,
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------- metrics
def nearest_rank(values, pct):
    if not values:
        return None
    v = sorted(values)
    return v[max(0, -(-len(v) * pct // 100) - 1)]


def metrics(traces):
    """Groups are reported separately and never combined (EV3, E-c)."""
    groups = {}
    for g in ("sample", "info_gap", "constructed"):
        ts = [t for t in traces if t["group"] == g]
        if not ts:
            continue
        esc = [t for t in ts if t["expected"]["route"] == "escalate"]
        star = [t for t in ts if t["expected"]["autonomous_star"]]
        groups[g] = {
            "snapshots": len(ts),
            "passed": sum(t["score"]["pass"] for t in ts),
            "pass_rate": round(sum(t["score"]["pass"] for t in ts) / len(ts), 4),
            "must_escalate": len(esc),
            "escalated_correctly": sum((t["output"] or {}).get("route") == "escalate" for t in esc),
            "escalated_when_not_expected": sum(
                (t["output"] or {}).get("route") == "escalate" and t["expected"]["route"] != "escalate" for t in ts),
            "autonomous_star": len(star),
            "autonomous": sum((t["output"] or {}).get("route") == "autonomous" for t in star),
            "gate_held": sum(t["score"]["gate_held"] for t in star),
            "triggers_match": sum(t["score"]["triggers_match"] for t in ts),
            "errors": sum(bool(t["error"]) for t in ts),
        }
    per_claim = {}
    for t in traces:
        per_claim[t["claim_id"]] = per_claim.get(t["claim_id"], 0) + t["cost_usd"]
    lat = [t["latency_s"] for t in traces if not t["error"]]
    return {
        "groups": groups,
        "evaluations": len(traces),
        "cost_total_usd": round(sum(t["cost_usd"] for t in traces), 4),
        "cost_per_evaluation_usd": round(sum(t["cost_usd"] for t in traces) / len(traces), 6),
        "cost_per_claim_usd": round(sum(per_claim.values()) / len(per_claim), 6),
        "latency_p50_s": nearest_rank(lat, 50),
        "latency_p95_s": nearest_rank(lat, 95),
        "tokens": {k: sum(t["usage"][k] for t in traces) for k in traces[0]["usage"]},
    }


# ---------------------------------------------------------------- main
def make_client():
    key = dotenv_values(ROOT / ".env").get("SPIKE_ANTHROPIC_API_KEY")
    if not key:
        sys.exit("SPIKE_ANTHROPIC_API_KEY is not set in .env")
    return anthropic.Anthropic(api_key=key, max_retries=4)


def estimate(client, model, system, cases, assumed_output):
    """Input tokens counted by the API (free); output tokens are the stated assumption."""
    total_in = 0
    for c in cases:
        n = client.messages.count_tokens(
            model=model, system=system,
            messages=[{"role": "user", "content": user_message(c["input"])}]).input_tokens
        total_in += n
    p = PRICES[model]
    in_cost = total_in * p["input"] / 1_000_000
    out_cost = len(cases) * assumed_output * p["output"] / 1_000_000
    print(f"{model}: {len(cases)} evaluations, {total_in:,} input tokens counted "
          f"(no caching assumed; excludes output-schema overhead)")
    print(f"  input  ${in_cost:.4f}")
    print(f"  output ${out_cost:.4f}  at an assumed {assumed_output:,} output tokens per evaluation")
    print(f"  total  ${in_cost + out_cost:.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=sorted(PRICES))
    ap.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"],
                    help="omit to use the model's default effort")
    ap.add_argument("--ids", nargs="*", help="run only these eval ids (e.g. K04/decision_point)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--estimate", action="store_true", help="count input tokens and estimate cost; no model run")
    ap.add_argument("--assume-output-tokens", type=int, help="required with --estimate")
    args = ap.parse_args()

    cases = [json.loads(l) for l in open(SPIKE / "eval_set.jsonl")]
    if args.ids:
        cases = [c for c in cases if c["id"] in set(args.ids)]
        missing = set(args.ids) - {c["id"] for c in cases}
        if missing:
            sys.exit(f"unknown ids: {sorted(missing)}")
    system = load_prompt()
    client = make_client()

    if args.estimate:
        if args.assume_output_tokens is None:
            sys.exit("--estimate needs --assume-output-tokens (a stated assumption, not a default)")
        return estimate(client, args.model, system, cases, args.assume_output_tokens)

    run_id = datetime.now().strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6]

    def one(case):
        out, usage, latency, stop, rid, err = call(client, args.model, args.effort, system, case)
        result = score(out, case["expected"])
        return trace_record(run_id, args.model, args.effort, case, out, usage, latency, stop, rid, err, result)

    # Warm the prompt cache with the first case, then run the rest in parallel.
    traces = [one(cases[0])]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        traces += list(pool.map(one, cases[1:]))

    (SPIKE / "traces").mkdir(exist_ok=True)
    with open(SPIKE / "traces" / f"{args.model}.jsonl", "a") as f:  # append-only (NF-04)
        for t in traces:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    summary = {"run_id": run_id, "model": args.model, "effort": args.effort,
               "eval_ids": [c["id"] for c in cases], "metrics": metrics(traces),
               "results": {t["eval_id"]: {"pass": t["score"]["pass"], "fields": t["score"]["fields"],
                                          "error": t["error"]} for t in traces}}
    (SPIKE / "runs").mkdir(exist_ok=True)
    (SPIKE / "runs" / f"{run_id}__{args.model}.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary["metrics"], indent=2))
    fails = [t["eval_id"] for t in traces if not t["score"]["pass"]]
    print(f"run {run_id}: {len(traces) - len(fails)}/{len(traces)} passed" + (f"; failed: {fails}" if fails else ""))


if __name__ == "__main__":
    main()
