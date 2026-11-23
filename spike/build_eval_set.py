"""Build spike/eval_set.jsonl: one line per snapshot (EV1), 2 per case.

Inputs come from data/released/ and the constructed-case settings (EV3a,
EV4, EV5). Expected outcomes are parsed from spike/expected-outcomes-v1.md,
the consultant's file, so they are never retyped. The derived snapshot moment
is checked against the moment the consultant wrote for every case.

Run: .venv/bin/python spike/build_eval_set.py
"""
import csv
import json
import re
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
REL = ROOT / "data" / "released"
SPIKE = ROOT / "spike"
ET = ZoneInfo("America/New_York")

FALLBACK_DEADLINE_DAYS = 14
EVAL_COLD_CHAIN_LIST = ["C-K01"]  # EV4

# Snapshot times. The release holds dates only; these clock times are a
# harness convention (spike/README.md, "Snapshot construction").
INTAKE_AT = time(9, 0)
DOCS_UPDATED_AT = time(12, 0)
FALLBACK_AT = time(23, 59)  # v1 rules.md, fallback date

claims = {r["claim_id"]: r for r in csv.DictReader(open(REL / "claims.csv"))}
r2 = {r["claim_id"]: r for r in csv.DictReader(open(REL / "claims_r2_fields.csv"))}
sample = list(csv.DictReader(open(REL / "eval_sample.csv")))


def d(s):
    return date.fromisoformat(s[:10]) if s else None


def ts(day, t):
    return datetime.combine(day, t, ET).isoformat()


# ---------------------------------------------------------------- expected
def parse_expected():
    """Return {case: [intake_row, decision_row]} from the consultant's tables."""
    rows = {}
    last_case = None
    for line in (SPIKE / "expected-outcomes-v1.md").read_text().splitlines():
        if not line.startswith("| ") or line.startswith("| Case") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        case = cells[0] or last_case
        last_case = case
        if case.startswith("NLC-"):
            _, _, _, snap, status, route, decision, rule, trig, notes = cells
        elif re.fullmatch(r"K\d\d", case):
            _, _, snap, status, route, decision, rule, trig, notes = cells
        else:
            continue
        rows.setdefault(case, []).append(dict(
            snapshot=snap, status=status, route=route, decision=decision,
            rule=rule, triggers=trig, notes=notes))
    assert all(len(v) == 2 for v in rows.values()), "every case needs 2 snapshots"
    return rows


def expected_record(row):
    """Turn one table row into scoring fields (conventions: expected-outcomes-v1.md)."""
    route = row["route"]
    autonomous_star = route == "autonomous*"
    rules = [r.strip().rstrip("*") for r in row["rule"].split(" or ")]
    if autonomous_star:
        rules = ["R15", "R14"]
    decision = row["decision"]
    return {
        "status": row["status"],
        "route": None if route == "null" else route.rstrip("*"),
        "autonomous_star": autonomous_star,
        # Decision is scored only where the rules determine it.
        "decision_scored": decision != "not scored",
        "decision": None if decision in ("null", "not scored") else decision,
        "rule_applied": rules,
        "triggers": [] if row["triggers"] == "—" else [t.strip() for t in row["triggers"].split(",")],
        "notes": row["notes"],
    }


EXPECTED = parse_expected()
INFO_GAP = {c for c, rs in EXPECTED.items() if any("info gap" in r["notes"] for r in rs)}


# ---------------------------------------------------------------- inputs
def other_claims(shipment_ref, own_ids, at):
    """Other claims on the shipment, with status as known at `at` (hindsight rule)."""
    out = []
    for cid, x in r2.items():
        if x["shipment_ref"] != shipment_ref or cid in own_ids or cid not in claims:
            continue
        c = claims[cid]
        if d(c["received_at"]) > at:
            continue
        if c["paid_at"] and d(c["paid_at"]) <= at:
            status = "paid"
        elif c["closed_at"] and d(c["closed_at"]) <= at:
            status = "closed_unpaid"
        else:
            status = "open"
        out.append({"claim_id": cid, "status": status})
    return out


def document(item, received, amount_claimed):
    """One received checklist item. The release holds no document content
    except what EV-rulings set: invoice_amount = amount_claimed (E-d)."""
    content = None
    if item == "invoice":
        content = {"invoice_amount": amount_claimed}
    return {"item": item, "received_date": received.isoformat() if received else None, "content": content}


def base_input(c, x, claim_id, claim_type, customer_id, amount, delivered, received):
    return {
        "claim_id": claim_id,
        "claim_type": claim_type,
        "customer_id": customer_id,
        "key_account": x["key_account"] == "Y",
        "shipment_ref": x["shipment_ref"],
        "amount_claimed": amount,
        "delivered_at": delivered.isoformat() if delivered else None,
        "received_at": received.isoformat(),
        "reefer_flag": x["reefer_flag"] == "Y",
        "pod_exception": x["pod_exception"] == "Y",
        "claim_text": None,
        "shipment_record": None,
        "cold_chain_list": EVAL_COLD_CHAIN_LIST,
        "expedite_requests": [],
        "paid": False,
        "withdrawal": None,
    }


def snapshot(inp, when, event, docs, other, state):
    s = dict(inp)
    s["evaluation_time"] = when
    s["event"] = event
    s["documents"] = docs
    s["other_claims_same_shipment"] = other
    s["current_state"] = state
    order = ["evaluation_time", "event", "claim_id", "claim_type", "customer_id", "key_account",
             "shipment_ref", "amount_claimed", "delivered_at", "received_at", "reefer_flag",
             "pod_exception", "claim_text", "documents", "shipment_record",
             "other_claims_same_shipment", "cold_chain_list", "expedite_requests",
             "current_state", "paid", "withdrawal"]
    return {k: s[k] for k in order}


NEW = {"status": None, "route": None, "assigned": None, "autonomous_decision_made": False}
HELD = {"status": "held", "route": None, "assigned": "awaiting_documents_list", "autonomous_decision_made": False}


def escalated(queue):
    return {"status": "routed", "route": "escalate", "assigned": queue, "autonomous_decision_made": False}


def state_after_intake(exp_intake, queue="claims_lead"):
    """The decision-point snapshot starts from the state the intake evaluation produced."""
    return escalated(queue) if exp_intake["route"] == "escalate" else HELD


def moment_label(snap):
    m = re.search(r"\d{4}-\d{2}-\d{2}", snap)
    return d(m.group(0)) if m else None


# ---------------------------------------------------------------- sample cases
def sample_cases():
    for s in sample:
        cid = s["claim_id"]
        c, x = claims[cid], r2[cid]
        exp = EXPECTED[cid]
        e0, e1 = expected_record(exp[0]), expected_record(exp[1])
        received, completed = d(s["received_at"]), d(s["docs_completed_at"])
        amount = float(s["amount_claimed"])
        inp = base_input(c, x, cid, s["claim_type"], s["customer_id"], amount, d(s["delivered_at"]), received)
        assumptions = ["invoice_amount = amount_claimed (E-d)",
                       "no cold-chain customer, temperature allegation or expedite request (EV6)",
                       "claim_text, shipment_record and photo/BOL/POD content not held in the release"]

        intake = snapshot(inp, ts(received, INTAKE_AT), "received", [],
                          other_claims(x["shipment_ref"], {cid}, received), NEW)

        flagged = [i for i, f in (("photos", s["photos_received"]), ("invoice", s["invoice_received"]),
                                  ("bol", s["bol_received"]), ("temperature_download", s["temp_log_obtained"]))
                   if f == "Y"]
        required = {"damage": ["photos", "invoice", "bol"], "shortage": ["invoice", "bol"]}[s["claim_type"]]
        fallback = received + timedelta(days=FALLBACK_DEADLINE_DAYS)

        if e0["route"] == "escalate":
            # Reefer: the decision point is the intake (G10b), as written in the expected outcomes.
            dp, rule = intake, "decision point = intake (G10b)"
        elif completed and all(i in flagged for i in required) and completed <= fallback:
            # EV2: completion date used; every item (POD included) received on it.
            docs = [document(i, completed, amount) for i in flagged] + [document("delivery_receipt_pod", completed, amount)]
            dp = snapshot(inp, ts(completed, DOCS_UPDATED_AT), "documents_updated", docs,
                          other_claims(x["shipment_ref"], {cid}, completed), state_after_intake(e0))
            rule = "EV2: completion date, every checklist flag received"
        else:
            # EV2: never completes by day 14. Flagged items listed without a date;
            # the POD counts as received only when the completion date is set and reached.
            docs = [document(i, None, amount) for i in flagged]
            dp = snapshot(inp, ts(fallback, FALLBACK_AT), "fallback_check", docs,
                          other_claims(x["shipment_ref"], {cid}, fallback), state_after_intake(e0))
            rule = "EV2: day-14 fallback"

        label = moment_label(exp[1]["snapshot"])
        got = d(dp["evaluation_time"])
        assert label is None or label == got, (cid, label, got)
        if "fallback" in exp[1]["snapshot"].lower():
            assert dp["event"] == "fallback_check", cid

        group = "info_gap" if cid in INFO_GAP else "sample"
        yield from emit(cid, "sample", group, [(intake, e0, "intake"), (dp, e1, rule)], assumptions)


# ---------------------------------------------------------------- constructed cases
K02_REQUEST = datetime(2026, 3, 11, 15, 30, tzinfo=ET)  # expected-outcomes-v1.md, K02
K04_INVOICE = 3406.70
K05_DELIVERED = date(2025, 5, 31)
K09_TEXT = ("The pallets arrived warm. Our receiving team measured the product at 14°C against "
            "the required 2–8°C, and we believe it went out of range in transit.")

CONSTRUCTED = [  # (case, base claim) as in spike/constructed_cases.py
    ("K01", "NLC-26-0001"), ("K02", "NLC-26-0021"), ("K03", "NLC-26-0123"),
    ("K04", "NLC-26-0003"), ("K05", "NLC-26-0006"), ("K06", "NLC-26-0013"),
    ("K07", "NLC-26-0023"), ("K08", "NLC-26-0054"), ("K09", "NLC-26-0014"),
]


def constructed_cases():
    for k, base in CONSTRUCTED:
        c, x = claims[base], r2[base]
        assert not c["docs_missing"], base
        exp = EXPECTED[k]
        e0, e1 = expected_record(exp[0]), expected_record(exp[1])
        received, completed = d(c["received_at"]), d(c["docs_completed_at"])
        amount = float(c["amount_claimed"])
        ctype = "loss" if k == "K08" else c["claim_type"]
        customer = "C-K01" if k == "K01" else c["customer_id"]
        delivered = K05_DELIVERED if k == "K05" else d(c["delivered_at"])
        inp = base_input(c, x, k, ctype, customer, amount, delivered, received)
        own = {base}
        if k == "K06":
            inp["shipment_ref"] = r2["NLC-26-0001"]["shipment_ref"]  # EV5
        if k == "K09":
            inp["claim_text"] = K09_TEXT
        assumptions = [f"constructed from {base} (EV3a)", "claim_text, shipment_record and photo/BOL/POD content not held"]

        items = ["photos", "invoice", "bol", "delivery_receipt_pod"]
        docs = [document(i, completed, amount) for i in items]
        if k == "K04":
            next(dd for dd in docs if dd["item"] == "invoice")["content"] = {"invoice_amount": K04_INVOICE}
        else:
            assumptions.append("invoice_amount = amount_claimed (E-d)")

        intake = snapshot(inp, ts(received, INTAKE_AT), "received", [],
                          other_claims(inp["shipment_ref"], own, received), NEW)

        dp_inp = dict(inp)
        if k == "K02":
            dp_inp["expedite_requests"] = [{"requester": "account_manager", "request_time": K02_REQUEST.isoformat()}]
        queue = "specialist" if e0["triggers"] == ["R3"] else "claims_lead"
        dp = snapshot(dp_inp, ts(completed, DOCS_UPDATED_AT), "documents_updated", docs,
                      other_claims(inp["shipment_ref"], own, completed), state_after_intake(e0, queue))

        label = moment_label(exp[1]["snapshot"])
        assert label == completed, (k, label, completed)
        if k == "K06":
            assert intake["other_claims_same_shipment"] == [{"claim_id": "NLC-26-0001", "status": "open"}]
            assert dp["other_claims_same_shipment"] == [{"claim_id": "NLC-26-0001", "status": "open"}]

        yield from emit(k, "constructed", "constructed",
                        [(intake, e0, "intake"), (dp, e1, "base claim completion date (EV3a)")], assumptions)


def emit(case, source, group, snaps, assumptions):
    for (inp, exp, rule), name in zip(snaps, ("intake", "decision_point")):
        yield {
            "id": f"{case}/{name}",
            "case": case,
            "source": source,
            "group": group,
            "snapshot": name,
            "moment_rule": rule,
            "assumptions": assumptions,
            "input": inp,
            "expected": exp,
        }


def main():
    records = list(sample_cases()) + list(constructed_cases())
    assert len(records) == 2 * (len(sample) + len(CONSTRUCTED))
    assert {r["case"] for r in records} == set(EXPECTED), "every expected case has inputs"
    with open(SPIKE / "eval_set.jsonl", "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    by = {}
    for r in records:
        by[r["group"]] = by.get(r["group"], 0) + 1
    print(f"wrote {len(records)} snapshots: " + ", ".join(f"{g} {n}" for g, n in sorted(by.items())))


if __name__ == "__main__":
    main()
