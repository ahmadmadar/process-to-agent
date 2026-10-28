"""Spike eval harness: run the claims-agent prompt on one model and score it.

- The agent prompt is loaded from .claude/skills/claims-agent/SKILL.md, so the
  Skill and the spike never drift.
- Cases come from spike/eval_set.jsonl (built by spike/build_eval_set.py).
- Scoring is deterministic: structured fields compared with the consultant's
  expected outcomes. No LLM-as-judge.
- Every output is validated against the v1 output schema and its rules.
- One trace line per decision is appended to spike/traces/<model>.jsonl (NF-01
  to NF-04). A run summary goes to spike/runs/<run_id>__<model>.json.
- The API key is read from .env as SPIKE_ANTHROPIC_API_KEY and passed to the
  client directly. It is never put in the environment (ground rule 8).
- Effort is pinned explicitly and is the same on both models (EV8).

Usage:
  .venv/bin/python spike/run_eval.py --model claude-sonnet-5-5 --effort LEVEL --smoke
  .venv/bin/python spike/run_eval.py --model claude-sonnet-5-5 --effort LEVEL
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

# USD per million tokens, Anthropic first-party API, global routing, 5-minute
# cache TTL. Source: https://platform.claude.com/docs/en/about-claude/pricing
# ("Model pricing" table), fetched 2026-10-27. Haiku 5.5 rates are for prompts
# up to 100,000 tokens; every eval prompt is far below that.
PRICES = {
    "claude-sonnet-5-5": {"input": 2.00, "cache_write": 2.50, "cache_read": 0.10, "output": 10.00},
    "claude-haiku-5-5":  {"input": 0.10, "cache_write": 0.125, "cache_read": 0.01, "output": 0.50},
    "claude-opus-5-5":   {"input": 4.00, "cache_write": 5.00, "cache_read": 0.20, "output": 20.00},  # only if Sonnet fails (EV8)
}

SMOKE_IDS = ["K04/decision_point", "NLC-26-0016/decision_point", "K09/intake"]  # EV12


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

# v1 rules.md, "Agent output", plus `steps` and `checks` for the trace (NF-02).
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


# ---------------------------------------------------------------- validation
TYPES = {"string": str, "number": (int, float), "boolean": bool, "object": dict, "array": list, "null": type(None)}


def schema_errors(value, schema, path="$"):
    if "anyOf" in schema:
        return [] if any(not schema_errors(value, s, path) for s in schema["anyOf"]) else [f"{path}: no anyOf branch matches"]
    t = schema["type"]
    if not isinstance(value, TYPES[t]) or (t == "number" and isinstance(value, bool)):
        return [f"{path}: expected {t}"]
    if "enum" in schema and value not in schema["enum"]:
        return [f"{path}: {value!r} not in enum"]
    errs = []
    if t == "object":
        errs += [f"{path}.{k}: missing" for k in schema["required"] if k not in value]
        errs += [f"{path}.{k}: not allowed" for k in value if k not in schema["properties"]]
        for k, s in schema["properties"].items():
            if k in value:
                errs += schema_errors(value[k], s, f"{path}.{k}")
    if t == "array":
        for i, item in enumerate(value):
            errs += schema_errors(item, schema["items"], f"{path}[{i}]")
    return errs


def v1_rule_errors(o):
    """Field rules from v1 rules.md, "Agent output" and "Confidence gates"."""
    e = []
    status, route, decision = o["status"], o["route"], o["decision"]
    if status in ("held", "withdrawn") and route is not None:
        e.append("route must be null when status is held or withdrawn")
    if status == "routed" and route is None:
        e.append("route must be set when status is routed")
    if (route == "escalate" or status in ("held", "withdrawn")) and decision is not None:
        e.append("decision must be null on escalate, held and withdrawn")
    if (decision is None or decision == "deny") and o["amount"] is not None:
        e.append("amount must be null when decision is null or deny")
    if status == "held" and o["rule_applied"] != "R5":
        e.append("rule_applied must be R5 on a hold")
    if status == "withdrawn" and o["rule_applied"] != "G12":
        e.append("rule_applied must be G12 on a withdrawal")
    if (status == "held") != (o["hold"] is not None):
        e.append("hold is required when held, otherwise null")
    if (route == "escalate") != (o["fact_pack"] is not None):
        e.append("fact_pack is required on escalate, otherwise null")
    step4 = [o[k] is None for k in ("rubric_score", "rubric_items", "self_reported_confidence")]
    if any(step4) and not all(step4):
        e.append("rubric_score, rubric_items and self_reported_confidence are all set or all null")
    if o["rubric_items"] is not None and o["rubric_score"] is not None:
        passed = sum(v == "pass" for v in o["rubric_items"].values())
        if o["rubric_score"] != round(passed / 6, 2):
            e.append(f"rubric_score {o['rubric_score']} != {passed}/6 rounded")
    for k in ("rubric_score", "self_reported_confidence"):
        if o[k] is not None and not 0 <= o[k] <= 1:
            e.append(f"{k} outside 0-1")
    if route == "autonomous" and (o["rule_applied"] != "R15" or decision != "approve"):
        e.append("autonomous requires R15 and approve")
    return e


def validate(out):
    errs = schema_errors(out, OUTPUT_SCHEMA)
    return errs if errs else v1_rule_errors(out)


# ---------------------------------------------------------------- scoring
def score(out, exp, inp, stop_reason, error):
    """Deterministic comparison with the expected outcome (expected-outcomes-v1.md, EV9, EV11)."""
    if stop_reason == "refusal":
        return {"pass": False, "category": "refusal", "fields": {}, "gate_held": False,
                "triggers_match": False, "v2_gap": None}
    if out is None:
        return {"pass": False, "category": "error", "fields": {}, "gate_held": False,
                "triggers_match": False, "v2_gap": None}
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
    passed = all(f.values())
    # EV9: an escalation on a null claim_text under "if unsure, treat it as an
    # allegation" is a v2 gap (v1 does not say what missing claim text means).
    v2_gap = None
    if (route == "escalate" and exp["route"] != "escalate" and "R1" in (out.get("triggers") or [])
            and inp["claim_text"] is None and not inp["reefer_flag"]):
        v2_gap = "null claim_text treated as a temperature allegation"
    return {
        "pass": passed,
        "category": "pass" if passed else ("wrong_route" if not f["route"] else "wrong_field"),
        "fields": f,
        "gate_held": exp["autonomous_star"] and route == "sign_off" and rule == "R14",
        "triggers_match": sorted(out.get("triggers") or []) == sorted(exp["triggers"]),
        "v2_gap": v2_gap,
    }


# ---------------------------------------------------------------- model call
def cost_usd(model, usage):
    p = PRICES[model]
    return (usage["input_tokens"] * p["input"]
            + usage["cache_creation_input_tokens"] * p["cache_write"]
            + usage["cache_read_input_tokens"] * p["cache_read"]
            + usage["output_tokens"] * p["output"]) / 1_000_000


def call(client, model, effort, system, case):
    # No server-side refusal fallback: a fallback would mix models in one model's results (EV11).
    kwargs = dict(
        model=model,
        max_tokens=16000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_message(case["input"])}],
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
    )
    started = time.perf_counter()
    error, out, resp = None, None, None
    try:
        resp = client.messages.create(**kwargs)
    except anthropic.APIStatusError as e:
        error = f"{type(e).__name__} {e.status_code}: {e.message}"
    except anthropic.APIConnectionError as e:
        error = f"{type(e).__name__}: {e}"
    latency = time.perf_counter() - started

    usage = {k: 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")}
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


def trace_record(run_id, kind, model, effort, case, out, usage, latency, stop_reason, request_id, error):
    """NF-02: inputs seen, steps reached, checks evaluated, full output, model, tokens, latency, cost."""
    inp = case["input"]
    return {
        "run_id": run_id,
        "kind": kind,
        "eval_id": case["id"],
        "group": case["group"],
        "claim_id": inp["claim_id"],
        "evaluation_time": inp["evaluation_time"],
        "event": inp["event"],
        "inputs": inp,
        "steps": (out or {}).get("steps"),
        "checks": (out or {}).get("checks"),
        "output": {k: v for k, v in (out or {}).items() if k not in ("steps", "checks")} or None,
        "schema_violations": validate(out) if out is not None else None,
        "model": model,
        "effort": effort,
        "usage": usage,
        "latency_s": round(latency, 3),
        "cost_usd": round(cost_usd(model, usage), 6),
        "stop_reason": stop_reason,
        "request_id": request_id,
        "error": error,
        "expected": case["expected"],
        "score": score(out, case["expected"], inp, stop_reason, error),
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------- metrics
def nearest_rank(values, pct):
    if not values:
        return None
    v = sorted(values)
    return v[max(0, -(-len(v) * pct // 100) - 1)]


def metrics(traces):
    """Groups are reported separately and never combined (EV3, E-c). The headline
    is routing on escalate, hold and sign-off; autonomous* is its own line (EV9)."""
    groups = {}
    for g in ("sample", "info_gap", "constructed"):
        ts = [t for t in traces if t["group"] == g]
        if not ts:
            continue
        head = [t for t in ts if not t["expected"]["autonomous_star"]]
        star = [t for t in ts if t["expected"]["autonomous_star"]]
        esc = [t for t in ts if t["expected"]["route"] == "escalate"]
        route_of = lambda t: (t["output"] or {}).get("route")
        groups[g] = {
            "headline_snapshots": len(head),
            "headline_passed": sum(t["score"]["pass"] for t in head),
            "must_escalate": len(esc),
            "escalated_correctly": sum(route_of(t) == "escalate" for t in esc),
            "escalated_when_not_expected": sum(route_of(t) == "escalate" and t["expected"]["route"] != "escalate" for t in ts),
            "autonomous_star": len(star),
            "autonomous": sum(route_of(t) == "autonomous" and t["score"]["pass"] for t in star),
            "gate_held": sum(t["score"]["gate_held"] for t in star),
            "autonomous_star_other": sum(not t["score"]["pass"] for t in star),
            "categories": {c: sum(t["score"]["category"] == c for t in ts)
                           for c in ("pass", "wrong_route", "wrong_field", "refusal", "error")},
            "schema_violations": sum(bool(t["schema_violations"]) for t in ts),
            "v2_gaps": sum(bool(t["score"]["v2_gap"]) for t in ts),
            "triggers_match": sum(t["score"]["triggers_match"] for t in ts),
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


def full_run_estimate(model, traces, n_snapshots):
    """Full-run cost from measured smoke tokens: the system prompt is written to the
    cache once and read on every other call; per-call input and output are the
    measured means (EV12)."""
    p = PRICES[model]
    traces = [t for t in traces if not t["error"]]
    if not traces:
        return None
    prefix = max(t["usage"]["cache_creation_input_tokens"] + t["usage"]["cache_read_input_tokens"] for t in traces)
    mean_in = sum(t["usage"]["input_tokens"] for t in traces) / len(traces)
    mean_out = sum(t["usage"]["output_tokens"] for t in traces) / len(traces)
    cost = (prefix * p["cache_write"] + (n_snapshots - 1) * prefix * p["cache_read"]
            + n_snapshots * (mean_in * p["input"] + mean_out * p["output"])) / 1_000_000
    return {"snapshots": n_snapshots, "calls_measured": len(traces), "cached_prefix_tokens": prefix, "mean_input_tokens": round(mean_in),
            "mean_output_tokens": round(mean_out), "estimated_cost_usd": round(cost, 4)}


# ---------------------------------------------------------------- main
def make_client():
    key = dotenv_values(ROOT / ".env").get("SPIKE_ANTHROPIC_API_KEY")
    if not key:
        sys.exit("SPIKE_ANTHROPIC_API_KEY is not set in .env")
    return anthropic.Anthropic(api_key=key, max_retries=4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=sorted(PRICES))
    ap.add_argument("--effort", required=True, choices=["low", "medium", "high", "xhigh", "max"],
                    help="pinned explicitly, same level on both models (EV8)")
    ap.add_argument("--smoke", action="store_true", help=f"run only {SMOKE_IDS} and estimate the full run")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    all_cases = [json.loads(l) for l in open(SPIKE / "eval_set.jsonl")]
    cases = [c for c in all_cases if c["id"] in SMOKE_IDS] if args.smoke else all_cases
    if args.smoke:
        cases.sort(key=lambda c: SMOKE_IDS.index(c["id"]))
        assert len(cases) == len(SMOKE_IDS)
    system = load_prompt()
    client = make_client()
    kind = "smoke" if args.smoke else "full"
    run_id = datetime.now().strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6]

    def one(case):
        out, usage, latency, stop, rid, err = call(client, args.model, args.effort, system, case)
        return trace_record(run_id, kind, args.model, args.effort, case, out, usage, latency, stop, rid, err)

    # Warm the prompt cache with the first case, then run the rest in parallel.
    traces = [one(cases[0])]
    with ThreadPoolExecutor(max_workers=1 if args.smoke else args.workers) as pool:
        traces += list(pool.map(one, cases[1:]))

    (SPIKE / "traces").mkdir(exist_ok=True)
    with open(SPIKE / "traces" / f"{args.model}.jsonl", "a") as f:  # append-only (NF-04)
        for t in traces:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    summary = {"run_id": run_id, "kind": kind, "model": args.model, "effort": args.effort,
               "eval_ids": [c["id"] for c in cases], "metrics": metrics(traces),
               "results": {t["eval_id"]: {"pass": t["score"]["pass"], "category": t["score"]["category"],
                                          "fields": t["score"]["fields"], "v2_gap": t["score"]["v2_gap"],
                                          "schema_violations": t["schema_violations"], "error": t["error"]}
                           for t in traces}}
    if args.smoke:
        summary["full_run_estimate"] = full_run_estimate(args.model, traces, len(all_cases))
    (SPIKE / "runs").mkdir(exist_ok=True)
    (SPIKE / "runs" / f"{run_id}__{args.model}.json").write_text(json.dumps(summary, indent=2))

    print(f"run {run_id} ({kind}) {args.model} effort={args.effort}")
    print("eval_id | category | schema/v1 violations | input | cache write | cache read | output | cost | latency")
    for t in traces:
        u = t["usage"]
        print(f"{t['eval_id']} | {t['score']['category']} | {len(t['schema_violations'] or [])} | "
              f"{u['input_tokens']} | {u['cache_creation_input_tokens']} | {u['cache_read_input_tokens']} | "
              f"{u['output_tokens']} | ${t['cost_usd']:.5f} | {t['latency_s']:.1f}s"
              + (f" | {t['error']}" if t["error"] else ""))
        for v in t["schema_violations"] or []:
            print(f"    violation: {v}")
    if args.smoke:
        print("full-run estimate:", json.dumps(summary["full_run_estimate"]))
    else:
        print(json.dumps(summary["metrics"], indent=2))


if __name__ == "__main__":
    main()
