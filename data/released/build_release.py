"""Build IT data release 1 from the full claims extract.

Northline Freight is a fictional client. All data is synthetic.

Cuts the release to the fields in engagement/01-discovery/data-request.md.
Fields the system does not hold are left out and listed in README.md.
Run from the repo root: python data/released/build_release.py
"""

import csv
from collections import Counter
from pathlib import Path

SOURCE = Path("sealed/data/claims_full.csv")
OUT = Path("data/released")
IN_SCOPE_TYPES = {"damage", "shortage"}
DOC_FLAGS = {
    "photos": "photos_received",
    "invoice": "invoice_received",
    "bol": "bol_received",
    "temp_log": "temp_log_obtained",
}

CLAIM_FIELDS = [
    "claim_id", "claim_type", "customer_id", "carrier_id",
    "amount_claimed", "amount_paid", "amount_recovered",
    "recovery_filed", "recovery_filed_at", "recovery_outcome",
    "outcome", "denial_reason", "decided_by_role",
    "docs_completed_at", "docs_missing",
    "delivered_at", "received_at", "closed_at", "paid_at",
]
EVENT_FIELDS = ["claim_id", "step", "actor_role", "started_at", "completed_at", "action"]


def claim_row(r):
    outcome = r["decision"] or "open"
    return {
        "claim_id": r["claim_id"],
        "claim_type": r["claim_type"],
        "customer_id": r["customer_id"],
        "carrier_id": r["carrier_code"],
        "amount_claimed": r["claimed_value"],
        "amount_paid": r["paid_amount"],
        "amount_recovered": r["carrier_recovered_amount"],
        "recovery_filed": r["carrier_claim_filed"],
        "recovery_filed_at": r["carrier_claim_filed_date"],
        "recovery_outcome": r["carrier_response"],
        "outcome": outcome,
        "denial_reason": r["decision_reason"] if outcome in {"denied", "partially_approved"} else "",
        "decided_by_role": r["approved_by_role"],
        "docs_completed_at": r["docs_complete_date"],
        "docs_missing": ";".join(k for k, col in DOC_FLAGS.items() if r[col] == "N"),
        "delivered_at": r["delivery_date"],
        "received_at": r["claim_received_date"],
        "closed_at": r["close_date"],
        "paid_at": r["payment_date"],
    }


def event_rows(r):
    # (step, date column, actor_role, action) — one recorded date per step.
    steps = [
        ("intake", "claim_received_date", "", ""),
        ("document_check", "docs_complete_date", "", ""),
        ("decision", "decision_date", r["approved_by_role"], r["decision"]),
        ("finance_review", "finance_review_date", "", r["finance_review_result"]),
        ("payment", "payment_date", "", ""),
        ("carrier_recovery_filed", "carrier_claim_filed_date", "", ""),
        ("carrier_recovery_response", "carrier_response_date", "", r["carrier_response"]),
        ("insurer_notified", "insurer_notified_date", "", r["insurer_status"]),
        ("close", "close_date", "", ""),
    ]
    for step, col, actor, action in steps:
        if r[col]:
            yield {
                "claim_id": r["claim_id"], "step": step, "actor_role": actor,
                "started_at": "", "completed_at": r[col], "action": action,
            }


def write(path, fields, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    source = list(csv.DictReader(open(SOURCE)))
    in_scope = [r for r in source if r["claim_type"] in IN_SCOPE_TYPES]
    claims = [claim_row(r) for r in in_scope]
    events = [e for r in in_scope for e in event_rows(r)]
    write(OUT / "claims.csv", CLAIM_FIELDS, claims)
    write(OUT / "event_log.csv", EVENT_FIELDS, events)

    received = sorted(c["received_at"] for c in claims)
    print(f"source rows: {len(source)}")
    print(f"excluded by claim type: {dict(Counter(r['claim_type'] for r in source if r['claim_type'] not in IN_SCOPE_TYPES))}")
    print(f"claims released: {len(claims)}")
    print(f"event rows released: {len(events)}")
    print(f"received_at range: {received[0]} to {received[-1]}")
    print("blank counts, claims.csv:")
    for f in CLAIM_FIELDS:
        print(f"  {f}: {sum(1 for c in claims if not c[f])}")
    print("blank counts, event_log.csv:")
    for f in EVENT_FIELDS:
        print(f"  {f}: {sum(1 for e in events if not e[f])}")


if __name__ == "__main__":
    main()
