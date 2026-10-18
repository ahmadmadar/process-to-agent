"""Build IT data release 2 from the full claims extract.

Northline Freight is a fictional client. All data is synthetic.

Cuts the release to the IT sections (§2–§4) of
engagement/01-discovery/data-request-2.md. Fields the system does not hold
are left out and listed in README-release-2.md.
Run from the repo root: python data/released/build_release_2.py
"""

import csv
import random
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from statistics import median

SOURCE = Path("sealed/data/claims_full.csv")
OUT = Path("data/released")
IN_SCOPE_TYPES = {"damage", "shortage"}
DOC_FLAGS = {
    "photos": "photos_received",
    "invoice": "invoice_received",
    "bol": "bol_received",
    "temp_log": "temp_log_obtained",
}
SAMPLE_SIZE = 30
SAMPLE_SEED = 2
SAMPLE_MIN_PER_STRATUM = 4

# §2 fields the system holds. Everything else in §2 is "not held" (README).
FIELDS_R2 = [
    "claim_id", "pod_exception", "reefer_flag", "key_account",
    "shipment_ref", "prior_payment_same_shipment", "prior_payment_claim_id",
]
SAMPLE_FIELDS = [
    "claim_id", "claim_type", "customer_id", "carrier_id",
    "amount_claimed", "amount_paid", "outcome", "denial_reason",
    "decided_by_role", "delivered_at", "received_at", "docs_completed_at",
    "photos_received", "invoice_received", "bol_received", "temp_log_obtained",
    "pod_exception", "reefer_flag", "key_account", "shipment_ref",
    "recovery_filed", "recovery_outcome",
]


def d(s):
    return date.fromisoformat(s) if s else None


def num(s):
    return float(s) if s else 0.0


def shipment_refs(source):
    # Pseudonymise the carrier PRO number; keeps claims on one shipment linkable.
    refs = {}
    for r in sorted(source, key=lambda r: r["claim_id"]):
        refs.setdefault(r["pro_number"], f"SHP-{len(refs) + 1:04d}")
    return refs


def prior_payments(source):
    # Earliest earlier paid claim on the same shipment, across all claim types.
    by_pro = defaultdict(list)
    for r in source:
        by_pro[r["pro_number"]].append(r)
    prior = {}
    for group in by_pro.values():
        group.sort(key=lambda r: (r["claim_received_date"], r["claim_id"]))
        paid_before = None
        for r in group:
            prior[r["claim_id"]] = paid_before
            if paid_before is None and num(r["paid_amount"]) > 0:
                paid_before = r["claim_id"]
    return prior


def r2_row(r, refs, prior):
    p = prior[r["claim_id"]]
    return {
        "claim_id": r["claim_id"],
        "pod_exception": r["pod_exception_noted"],
        "reefer_flag": "Y" if r["mode"] == "Reefer" else "N",
        "key_account": "Y" if r["customer_tier"] == "key" else "N",
        "shipment_ref": refs[r["pro_number"]],
        "prior_payment_same_shipment": "Y" if p else "N",
        "prior_payment_claim_id": p or "",
    }


def loss_summary(source):
    loss = [r for r in source if r["claim_type"] == "loss"]
    by_month = Counter(r["claim_received_date"][:7] for r in loss)
    closed_days = [
        (d(r["close_date"]) - d(r["claim_received_date"])).days
        for r in loss if r["close_date"]
    ]
    rows = [{"measure": f"count received {m}", "value": n} for m, n in sorted(by_month.items())]
    rows += [
        {"measure": "count total", "value": len(loss)},
        {"measure": "closed claims", "value": len(closed_days)},
        {"measure": "median days received to closed (closed claims)", "value": median(closed_days)},
        {"measure": "total claimed", "value": round(sum(num(r["claimed_value"]) for r in loss), 2)},
        {"measure": "total paid", "value": round(sum(num(r["paid_amount"]) for r in loss), 2)},
        {"measure": "total recovered", "value": round(sum(num(r["carrier_recovered_amount"]) for r in loss), 2)},
    ]
    return rows


def doc_field_check(in_scope):
    # Data quality question 1: document flags vs docs-complete date.
    rows = []
    for label, col in DOC_FLAGS.items():
        c = Counter(
            (r[col], "date set" if r["docs_complete_date"] else "no date")
            for r in in_scope
        )
        for (flag, has_date), n in sorted(c.items()):
            rows.append({"document": label, "flag": flag, "docs_complete_date": has_date, "claims": n})
    return rows


def am_preapproval_check(in_scope):
    # Data quality question 3: do account-manager decisions get a finance review?
    am = [r for r in in_scope if r["approved_by_role"] == "account_manager"]
    reviewed = sum(1 for r in am if r["finance_review_date"])
    return [
        {"measure": "account-manager decisions", "value": len(am)},
        {"measure": "with a finance review date", "value": reviewed},
        {"measure": "without a finance review date", "value": len(am) - reviewed},
    ]


def eval_sample(in_scope, r2):
    # Stratified sample: at least SAMPLE_MIN_PER_STRATUM from each requested stratum.
    rng = random.Random(SAMPLE_SEED)
    strata = {
        "damage": lambda r: r["claim_type"] == "damage",
        "shortage": lambda r: r["claim_type"] == "shortage",
        "reefer": lambda r: r["mode"] == "Reefer",
        "key_account": lambda r: r["customer_tier"] == "key",
        "denied": lambda r: r["decision"] == "denied",
        "partial": lambda r: r["decision"] == "partially_approved",
    }
    pool = sorted(in_scope, key=lambda r: r["claim_id"])
    chosen = {}
    for test in strata.values():
        have = sum(1 for r in chosen.values() if test(r))
        candidates = [r for r in pool if test(r) and r["claim_id"] not in chosen]
        for r in rng.sample(candidates, max(0, SAMPLE_MIN_PER_STRATUM - have)):
            chosen[r["claim_id"]] = r
    rest = [r for r in pool if r["claim_id"] not in chosen]
    for r in rng.sample(rest, SAMPLE_SIZE - len(chosen)):
        chosen[r["claim_id"]] = r
    rows = []
    for cid in sorted(chosen):
        r = chosen[cid]
        rows.append({
            "claim_id": cid,
            "claim_type": r["claim_type"],
            "customer_id": r["customer_id"],
            "carrier_id": r["carrier_code"],
            "amount_claimed": r["claimed_value"],
            "amount_paid": r["paid_amount"],
            "outcome": r["decision"] or "open",
            "denial_reason": r["decision_reason"] if r["decision"] in {"denied", "partially_approved"} else "",
            "decided_by_role": r["approved_by_role"],
            "delivered_at": r["delivery_date"],
            "received_at": r["claim_received_date"],
            "docs_completed_at": r["docs_complete_date"],
            **{col: r[col] for col in DOC_FLAGS.values()},
            **{k: r2[cid][k] for k in ("pod_exception", "reefer_flag", "key_account", "shipment_ref")},
            "recovery_filed": r["carrier_claim_filed"],
            "recovery_outcome": r["carrier_response"],
        })
    return rows, {name: sum(1 for x in chosen.values() if t(x)) for name, t in strata.items()}


def write(path, rows, fields=None):
    fields = fields or list(rows[0])
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    source = list(csv.DictReader(open(SOURCE)))
    in_scope = [r for r in source if r["claim_type"] in IN_SCOPE_TYPES]
    refs = shipment_refs(source)
    prior = prior_payments(source)
    r2 = {r["claim_id"]: r2_row(r, refs, prior) for r in in_scope}

    write(OUT / "claims_r2_fields.csv", list(r2.values()), FIELDS_R2)
    write(OUT / "loss_summary.csv", loss_summary(source))
    write(OUT / "dq_document_fields.csv", doc_field_check(in_scope))
    write(OUT / "dq_am_preapproval.csv", am_preapproval_check(in_scope))
    sample, strata_counts = eval_sample(in_scope, r2)
    write(OUT / "eval_sample.csv", sample, SAMPLE_FIELDS)

    print(f"claims in release 2 field file: {len(r2)}")
    print(f"eval sample: {len(sample)} claims; strata coverage {strata_counts}")
    print("blank counts, claims_r2_fields.csv:")
    for f in FIELDS_R2:
        print(f"  {f}: {sum(1 for c in r2.values() if not c[f])}")


if __name__ == "__main__":
    main()
