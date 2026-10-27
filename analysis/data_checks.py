"""Data-vs-claims checks on IT data releases 1 and 2.

Northline Freight is a fictional client. All data is synthetic.

Tests the numbers and rules stated in T1 (COO) and T2 (claims lead) against
data/released/. Every figure in the synthesis cites a query ID (Q1, Q2, ...)
in the generated analysis/results.md.

Run from the repo root: python analysis/data_checks.py
"""

import csv
import statistics
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RELEASE = Path("data/released")
OUT = Path("analysis/results.md")

# From data/released/README.md: loss claims excluded from release 1 by scope.
LOSS_EXCLUDED = 49

# Assumption, labelled: T2:L16 gives the insurance deductible as "twenty-five,
# I think?" (unconfirmed; CFO to confirm). Used only as a band edge.
DEDUCTIBLE_ASSUMED = 25_000
APPROVAL_LINE = 10_000  # T2:L14, T2:L62
COO_AUTONOMY_LINE = 50_000  # T1:L12
INSURER_NOTICE_DAYS = 30  # T2:L16


def d(s):
    return date.fromisoformat(s) if s else None


def num(s):
    return float(s) if s else 0.0


def days(a, b):
    return (b - a).days if a and b else None


def pct(n, total):
    return f"{100 * n / total:.0f}%" if total else "n/a"


def med(xs):
    return f"{statistics.median(xs):.0f}" if xs else "n/a"


def p90(xs):
    if len(xs) < 2:
        return "n/a"
    return f"{statistics.quantiles(xs, n=10, method='inclusive')[8]:.0f}"


def money(x):
    return f"${x:,.0f}"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def load():
    claims = list(csv.DictReader(open(RELEASE / "claims.csv")))
    events = defaultdict(dict)
    for e in csv.DictReader(open(RELEASE / "event_log.csv")):
        events[e["claim_id"]][e["step"]] = e
    for c in claims:
        for f in ("received_at", "closed_at", "paid_at", "delivered_at",
                  "docs_completed_at", "recovery_filed_at"):
            c[f] = d(c[f])
        for f in ("amount_claimed", "amount_paid", "amount_recovered"):
            c[f] = num(c[f])
        ev = events[c["claim_id"]]
        c["decision_at"] = d(ev.get("decision", {}).get("completed_at"))
        c["finance_at"] = d(ev.get("finance_review", {}).get("completed_at"))
        c["finance_result"] = ev.get("finance_review", {}).get("action", "")
        c["insurer_at"] = d(ev.get("insurer_notified", {}).get("completed_at"))
        c["insurer_status"] = ev.get("insurer_notified", {}).get("action", "")
    return claims


def q_volume(claims):
    by_month = Counter(c["received_at"].strftime("%Y-%m") for c in claims)
    months = len(by_month)
    per_month = len(claims) / months
    per_month_all = (len(claims) + LOSS_EXCLUDED) / months
    rows = [(m, n) for m, n in sorted(by_month.items())]
    return ("Q1. Claim volume (T1:L18, T2:L50)", [
        table(["Month received", "Claims (damage + shortage)"], rows),
        table(["Measure", "Value"], [
            ("Months in release", months),
            ("Damage + shortage per month (mean)", f"{per_month:.0f}"),
            ("Including excluded loss claims, per month (mean)", f"{per_month_all:.0f}"),
            ("Including loss, annualised", f"{per_month_all * 12:.0f}"),
        ]),
    ])


def q_mix(claims):
    n_all = len(claims) + LOSS_EXCLUDED
    mix = Counter(c["claim_type"] for c in claims)
    rows = [(t, n, pct(n, n_all)) for t, n in sorted(mix.items())]
    rows.append(("loss (excluded; count from IT README)", LOSS_EXCLUDED, pct(LOSS_EXCLUDED, n_all)))
    return ("Q2. Claim type mix (T2:L50)", [table(["Type", "Claims", "Share of all"], rows)])


def q_cycle(claims):
    closed = [days(c["received_at"], c["closed_at"]) for c in claims if c["closed_at"]]
    over_30 = sum(1 for x in closed if x > 30)
    return ("Q3. Cycle time, received to closed (T1:L8, T1:L22, T2:L12, T2:L66)", [
        table(["Measure", "Days"], [
            ("Closed claims", len(closed)),
            ("Median", med(closed)),
            ("p90", p90(closed)),
            ("Mean", f"{statistics.mean(closed):.0f}"),
            ("Closed claims over 30 days", f"{over_30} ({pct(over_30, len(closed))})"),
        ]),
    ])


def q_stages(claims):
    stages = [
        ("Received → docs complete", "received_at", "docs_completed_at"),
        ("Docs complete → decision", "docs_completed_at", "decision_at"),
        ("Decision → finance pre-approval", "decision_at", "finance_at"),
        ("Finance pre-approval → paid", "finance_at", "paid_at"),
        ("Paid → closed", "paid_at", "closed_at"),
        ("Decision → paid", "decision_at", "paid_at"),
    ]
    rows = []
    for label, a, b in stages:
        xs = [days(c[a], c[b]) for c in claims if c[a] and c[b]]
        rows.append((label, len(xs), med(xs), p90(xs)))
    return ("Q4. Elapsed days by stage (H1; T1:L26, T2:L18, T2:L26)", [
        table(["Stage", "Claims with both dates", "Median days", "p90 days"], rows),
        "Elapsed time only. The event log has one date per step, so waiting "
        "and working time within a stage cannot be separated (README, Event log).",
    ])


def q_finance(claims):
    reviewed = [c for c in claims if c["finance_at"]]
    results = Counter(c["finance_result"] for c in reviewed)
    by_outcome = Counter(c["outcome"] for c in reviewed)
    adjusted = [c for c in reviewed if c["finance_result"] != "approved_as_submitted"]
    rows_adj = [(c["claim_id"], money(c["amount_claimed"]), c["outcome"], c["finance_result"]) for c in adjusted]
    lag = [days(c["decision_at"], c["finance_at"]) for c in reviewed if c["decision_at"]]
    return ("Q5. Finance pre-approval (H2; T1:L26, T2:L18, T2:L26, T2:L56, T2:L60)", [
        table(["Measure", "Value"], [
            ("Claims with a finance pre-approval step", f"{len(reviewed)} of {len(claims)}"),
            *[(f"Result: {k}", f"{v} ({pct(v, len(reviewed))})") for k, v in results.most_common()],
            *[(f"Reviewed, decision {k}", v) for k, v in by_outcome.most_common()],
            ("Decision → pre-approval, median days", med(lag)),
            ("Decision → pre-approval, p90 days", p90(lag)),
        ]),
        "Claims where the pre-approval result was not `approved_as_submitted`:",
        table(["Claim", "Amount claimed", "Decision", "Pre-approval result"], rows_adj),
    ])


def q_weekday(claims):
    wd = Counter(c["paid_at"].strftime("%A") for c in claims if c["paid_at"])
    return ("Q6. Payment day of week (T2:L18, T2:L26)", [
        table(["Day", "Payments"], wd.most_common()),
    ])


def q_size(claims):
    amts = [c["amount_claimed"] for c in claims]
    bands = [
        (f"Over {money(APPROVAL_LINE)} (approval line, T2:L14)", APPROVAL_LINE),
        (f"Over {money(DEDUCTIBLE_ASSUMED)} (assumed deductible, T2:L16)", DEDUCTIBLE_ASSUMED),
        (f"Over {money(COO_AUTONOMY_LINE)} (COO autonomy line, T1:L12)", COO_AUTONOMY_LINE),
    ]
    rows = [("Median amount claimed", money(statistics.median(amts))),
            ("p90 amount claimed", money(statistics.quantiles(amts, n=10, method="inclusive")[8])),
            ("Largest amount claimed", money(max(amts)))]
    rows += [(label, f"{sum(1 for a in amts if a > edge)} ({pct(sum(1 for a in amts if a > edge), len(amts))})")
             for label, edge in bands]
    between = sum(1 for a in amts if DEDUCTIBLE_ASSUMED < a <= COO_AUTONOMY_LINE)
    rows.append((f"Over {money(DEDUCTIBLE_ASSUMED)} and at or under {money(COO_AUTONOMY_LINE)}", between))
    under_coo = sum(1 for a in amts if a <= COO_AUTONOMY_LINE)
    rows.append((f"At or under {money(COO_AUTONOMY_LINE)}", f"{under_coo} ({pct(under_coo, len(amts))})"))
    return ("Q7. Claim size (T1:L18, T1:L34, T2:L48)", [table(["Measure", "Value"], rows)])


def q_approval(claims):
    def band(a):
        return f"≤ {money(APPROVAL_LINE)}" if a <= APPROVAL_LINE else f"> {money(APPROVAL_LINE)}"
    grid = Counter((band(c["amount_claimed"]), c["decided_by_role"] or "(blank)") for c in claims)
    roles = sorted({r for _, r in grid})
    rows = [(b, *[grid[(b, r)] for r in roles]) for b in (f"≤ {money(APPROVAL_LINE)}", f"> {money(APPROVAL_LINE)}")]
    return ("Q8. Who decides, by amount (T1:L10, T2:L14, T2:L62)", [
        table(["Amount claimed", *roles], rows),
    ])


def recovery_rows(group):
    paid = [c for c in group if c["amount_paid"] > 0]
    filed = [c for c in paid if c["recovery_filed"] == "Y"]
    answered = [c for c in filed if c["recovery_outcome"] in ("paid", "partial", "denied")]
    accepted = [c for c in filed if c["recovery_outcome"] in ("paid", "partial")]

    def ratio(cs):
        p = sum(c["amount_paid"] for c in cs)
        return pct(sum(c["amount_recovered"] for c in cs), p) if p else "n/a"

    return [
        ("Claims with a payout", len(paid)),
        ("Filed with the carrier", f"{len(filed)} ({pct(len(filed), len(paid))})"),
        ("Recovered ÷ paid, all paid claims", ratio(paid)),
        ("Recovered ÷ paid, filed claims", ratio(filed)),
        ("Recovered ÷ paid, filed claims with a carrier answer", ratio(answered)),
        ("Recovered ÷ paid, claims the carrier accepted (paid or partial)", ratio(accepted)),
    ]


def q_recovery(claims):
    responses = Counter(c["recovery_outcome"] for c in claims)
    return ("Q9. Carrier recovery, by denominator (H5; T1:L18, T2:L12, T2:L64)", [
        table(["Measure", "Value"], recovery_rows(claims)),
        table(["Carrier response", "Claims"], responses.most_common()),
        "The rate depends on the denominator. Neither interviewee stated one (T1:L20, T2:L64).",
    ])


def q_recovery_by_type(claims):
    out = []
    for t in sorted({c["claim_type"] for c in claims}):
        group = [c for c in claims if c["claim_type"] == t]
        out.append(f"**{t}**")
        out.append(table(["Measure", "Value"], recovery_rows(group)))
        resp = Counter(c["recovery_outcome"] for c in group)
        out.append(table(["Carrier response", "Claims"], resp.most_common()))
    out.append("Release 1 has no POD-exception field, so the clean-POD shortage "
               "rule (T2:L20, T2:L64) cannot be tested here. It is tested in Q18 (release 2).")
    return ("Q10. Carrier recovery by claim type (H5; T2:L20, T2:L64)", out)


def q_am(claims):
    def stats(group):
        paid = [c for c in group if c["paid_at"]]
        before_docs = sum(1 for c in paid if not c["docs_completed_at"] or c["paid_at"] < c["docs_completed_at"])
        to_paid = [days(c["received_at"], c["paid_at"]) for c in paid]
        return [len(group), len(paid), f"{before_docs} ({pct(before_docs, len(paid))})", med(to_paid)] + \
            [v for _, v in recovery_rows(group)[1:4]]
    am = [c for c in claims if c["decided_by_role"] == "account_manager"]
    team = [c for c in claims if c["decided_by_role"] in ("claims_specialist", "claims_lead")]
    headers = ["Decided by", "Claims", "Paid", "Paid before docs complete",
               "Median days received → paid", "Filed with carrier", "Recovered ÷ paid (all paid)",
               "Recovered ÷ paid (filed)"]
    return ("Q11. Account-manager decisions vs claims team (H4, H5; T1:L10, T2:L14, T2:L52, T2:L54)", [
        table(headers, [["account_manager", *stats(am)], ["claims team", *stats(team)]]),
    ])


def q_insurer(claims):
    notified = [c for c in claims if c["insurer_at"]]
    status = Counter(c["insurer_status"] for c in notified)
    lag = [days(c["received_at"], c["insurer_at"]) for c in notified]
    late = sum(1 for x in lag if x > INSURER_NOTICE_DAYS)
    paid_first = sum(1 for c in notified if c["paid_at"] and c["paid_at"] < c["insurer_at"])
    over_ded = [c for c in claims if c["amount_claimed"] > DEDUCTIBLE_ASSUMED]
    over_ded_no_notice = sum(1 for c in over_ded if not c["insurer_at"])
    rows = [(c["claim_id"], money(c["amount_claimed"]), c["decided_by_role"],
             days(c["received_at"], c["insurer_at"]), c["paid_at"] < c["insurer_at"] if c["paid_at"] else "not paid",
             c["insurer_status"]) for c in sorted(notified, key=lambda c: c["received_at"])]
    return ("Q12. Insurer notification (T2:L16, T2:L48, T2:L62)", [
        table(["Measure", "Value"], [
            ("Claims with an insurer-notified step", len(notified)),
            *[(f"Insurer status: {k}", v) for k, v in status.most_common()],
            ("Smallest amount claimed among notified", money(min(c["amount_claimed"] for c in notified))),
            (f"Notified more than {INSURER_NOTICE_DAYS} days after receipt", late),
            ("Paid before the insurer was notified", paid_first),
            (f"Claims over {money(DEDUCTIBLE_ASSUMED)} (assumed deductible)", len(over_ded)),
            (f"…of which no insurer-notified step", over_ded_no_notice),
        ]),
        table(["Claim", "Amount claimed", "Decided by", "Days received → notified", "Paid before notice", "Insurer status"], rows),
    ])


def q_docs(claims):
    missing = Counter(doc for c in claims for doc in c["docs_missing"].split(";") if doc)
    never = [c for c in claims if not c["docs_completed_at"]]
    lag = [days(c["received_at"], c["docs_completed_at"]) for c in claims if c["docs_completed_at"]]
    same_day = sum(1 for x in lag if x == 0)
    return ("Q13. Documents (H1, H3; T1:L26, T2:L18, T2:L28, T2:L30)", [
        table(["Measure", "Value"], [
            ("Claims with docs complete", len(lag)),
            ("Docs complete on day of receipt", f"{same_day} ({pct(same_day, len(lag))})"),
            ("Received → docs complete, median days", med(lag)),
            ("Received → docs complete, p90 days", p90(lag)),
            ("Claims never docs complete", len(never)),
        ]),
        table(["Document missing (as of extract)", "Claims"], missing.most_common()),
        table(["Outcome, claims never docs complete", "Decided by", "Claims"],
              [(o, r, n) for (o, r), n in Counter((c["outcome"], c["decided_by_role"]) for c in never).most_common()]),
    ])


def q_outcomes(claims):
    out = Counter(c["outcome"] for c in claims)
    reasons = Counter(c["denial_reason"] for c in claims if c["denial_reason"])
    still_open = sum(1 for c in claims if not c["closed_at"])
    return ("Q14. Outcomes and denial reasons (H3; T2:L60, T2:L70)", [
        table(["Outcome", "Claims"], out.most_common()),
        table(["Denial / partial reason", "Claims"], reasons.most_common()),
        f"Claims with no `closed_at` (still open): {still_open}.",
    ])


def load_r2(claims):
    r2 = {r["claim_id"]: r for r in csv.DictReader(open(RELEASE / "claims_r2_fields.csv"))}
    sample = {r["claim_id"]: r for r in csv.DictReader(open(RELEASE / "eval_sample.csv"))}
    for c in claims:
        c.update({k: v for k, v in r2.get(c["claim_id"], {}).items() if k != "claim_id"})
        c["temp_log_required"] = (sample[c["claim_id"]]["temp_log_obtained"] != "N/A"
                                  if c["claim_id"] in sample else None)


def q_threshold_basis(claims):
    lines = [(APPROVAL_LINE, "$10k approval line"), (DEDUCTIBLE_ASSUMED, "assumed deductible")]
    paid = [c for c in claims if c["outcome"] in ("approved", "partially_approved")]
    rows, detail = [], []
    for line, name in lines:
        cross = [c for c in paid if c["amount_claimed"] > line >= c["amount_paid"]]
        rows.append((f"{name} ({money(line)})", sum(c["amount_claimed"] > line for c in claims), len(cross)))
        detail += [(c["claim_id"], name, money(c["amount_claimed"]), money(c["amount_paid"]), c["outcome"])
                   for c in cross]
    return ("Q15. Threshold basis: claimed vs paid amount (G4; T2:L14, T2:L16, T2:L62)", [
        table(["Threshold", "Claims with claimed amount above it", "Paid claims claimed above, paid at or below"], rows),
        table(["Claim", "Threshold crossed", "Claimed", "Paid", "Outcome"], detail),
    ])


def q_reefer(claims):
    reefer = [c for c in claims if c.get("reefer_flag") == "Y"]
    temp_missing = lambda c: "temp_log" in c["docs_missing"].split(";")
    sampled = [c for c in claims if c["temp_log_required"] is not None]
    return ("Q16. Reefer equipment vs temperature claims (G5; T2:L44, T2:L58)", [
        table(["Measure", "Value"], [
            ("Claims on reefer equipment (`reefer_flag` = Y)", f"{len(reefer)} of {len(claims)}"),
            ("…damage", sum(c["claim_type"] == "damage" for c in reefer)),
            ("…shortage", sum(c["claim_type"] == "shortage" for c in reefer)),
            ("Reefer claims with a temperature log missing (required, not obtained)", sum(map(temp_missing, reefer))),
            ("Non-reefer claims with a temperature log missing", sum(temp_missing(c) for c in claims if c not in reefer)),
        ]),
        "Eval sample only (`temp_log_obtained` is N/A where no temperature log is required):",
        table(["`reefer_flag`", "Temperature log required", "Claims"],
              [(r, "yes" if t else "no", n) for (r, t), n in sorted(Counter(
                  (c.get("reefer_flag"), c["temp_log_required"]) for c in sampled).items())]),
    ])


def q_insurer_clock(claims):
    notified = [c for c in claims if c["insurer_at"]]
    rows = []
    for c in sorted(notified, key=lambda c: c["claim_id"]):
        from_receipt = days(c["received_at"], c["insurer_at"])
        from_delivery = days(c["delivered_at"], c["insurer_at"])
        rows.append((c["claim_id"], from_delivery, from_receipt,
                     "Y" if from_delivery > INSURER_NOTICE_DAYS else "N",
                     "Y" if from_receipt > INSURER_NOTICE_DAYS else "N", c["insurer_status"]))
    over = lambda i: [r for r in rows if r[i] == "Y"]
    return ("Q17. Insurer 30-day clock: from delivery vs from receipt (G9; T2:L16, T2:L48)", [
        table(["Measure", "From delivery", "From receipt"], [
            ("Notified more than 30 days after", len(over(3)), len(over(4))),
            ("…of which insurer consented to settle", sum(r[5] == "consent_to_settle" for r in over(3)),
             sum(r[5] == "consent_to_settle" for r in over(4))),
        ]),
        table(["Claim", "Days delivery → notified", "Days receipt → notified", "> 30 from delivery",
               "> 30 from receipt", "Insurer status"], rows),
    ])


def q_clean_pod(claims):
    responses = ["paid", "partial", "denied", "pending", "not_filed"]
    rows, resp_rows = [], []
    for t in ("shortage", "damage"):
        for pod, label in (("N", "clean POD"), ("Y", "POD exception")):
            g = [c for c in claims if c["claim_type"] == t and c.get("pod_exception") == pod]
            paid = [c for c in g if c["amount_paid"] > 0]
            filed = [c for c in paid if c["recovery_filed"] == "Y"]
            answered = [c for c in filed if c["recovery_outcome"] in ("paid", "partial", "denied")]
            accepted = [c for c in answered if c["recovery_outcome"] in ("paid", "partial")]
            rec = sum(c["amount_recovered"] for c in filed)
            rows.append((t, label, len(g), len(paid), len(filed), len(answered), len(accepted),
                         money(rec), pct(rec, sum(c["amount_paid"] for c in filed))))
            r = Counter(c["recovery_outcome"] for c in paid)
            resp_rows.append((t, label, *(r.get(x, 0) for x in responses)))
    return ("Q18. Clean-POD rule: carrier response by POD status (E6; T2:L20, T2:L64)", [
        table(["Type", "POD", "Claims", "Paid", "Filed", "Carrier answered", "Carrier accepted (paid or partial)",
               "Recovered (filed)", "Recovered ÷ paid (filed)"], rows),
        table(["Type", "POD", *responses], resp_rows),
        "`pod_exception` from release 2: `N` is a clean POD. Paid claims only in the response table.",
    ])


def q_docs_deadline(claims):
    lag = [days(c["received_at"], c["docs_completed_at"]) for c in claims if c["docs_completed_at"]]
    never = sum(1 for c in claims if not c["docs_completed_at"])
    rows = [(f"Within {n} days", sum(1 for x in lag if x <= n), pct(sum(1 for x in lag if x <= n), len(lag)))
            for n in (7, 10, 14, 21, 30, 45)]
    rows.append(("Longest, days", max(lag), ""))
    return ("Q19. Days from receipt to documents complete (FALLBACK_DEADLINE_DAYS; C5b, E5; T2:L28, T2:L34)", [
        table(["Documents complete", "Claims", "Share of claims that completed"], rows),
        f"Claims that completed: {len(lag)}. Claims never complete: {never} (Q13).",
    ])


def q_docs_by_type(claims):
    rows = []
    for ctype in ("damage", "shortage"):
        group = [c for c in claims if c["claim_type"] == ctype]
        done = [c for c in group if c["docs_completed_at"]]
        notdone = [c for c in group if not c["docs_completed_at"]]
        for doc in ("photos", "invoice", "bol", "temp_log"):
            n = sum(1 for c in done if doc in c["docs_missing"].split(";"))
            rows.append((ctype, doc, n, len(done), pct(n, len(done))))
        clean = sum(1 for c in notdone if not c["docs_missing"])
        rows.append((ctype, "(none missing, but no completion date)", clean, len(notdone), pct(clean, len(notdone))))
    return ("Q20. Documents missing on claims marked complete, by claim type (E5 checklist; T2:L18)", [
        table(["Type", "Document missing (as of extract)", "Claims", "Of", "Share"], rows),
        "\"Of\" is claims with a completion date, except the last row per type, where it is claims without one. "
        "`docs_missing` shows flag status at extract, not at receipt, and IT does not check that the flags agree with "
        "the completion date (release 1 README; release 2 §4 Q1). There is no delivery-receipt document flag (release 2 §4 Q4).",
    ])


def q_filing_window(claims):
    fw = "outside customer filing window"
    denied = [c for c in claims if c["denial_reason"] == fw]
    others = [c for c in claims if c["denial_reason"] != fw]
    bases = [("Delivery → receipt", "delivered_at", "received_at"),
             ("Delivery → documents complete", "delivered_at", "docs_completed_at"),
             ("Receipt → documents complete", "received_at", "docs_completed_at")]
    rows = []
    for label, a, b in bases:
        dg = [days(c[a], c[b]) for c in denied if c[a] and c[b]]
        og = [days(c[a], c[b]) for c in others if c[a] and c[b]]
        separable = bool(dg) and min(dg) > max(og)
        rows.append((label, len(dg), f"{min(dg)}–{max(dg)}", len(og), f"{min(og)}–{max(og)}",
                     "Yes" if separable else "No"))
    cust = sorted({c["customer_id"] for c in denied})
    crow = []
    for cid in cust:
        dg = [days(c["delivered_at"], c["received_at"]) for c in denied if c["customer_id"] == cid]
        ok = [days(c["delivered_at"], c["received_at"]) for c in others
              if c["customer_id"] == cid and c["outcome"] in ("approved", "partially_approved")]
        crow.append((cid, len(dg), ", ".join(str(x) for x in sorted(dg)), len(ok), max(ok) if ok else "—"))
    return ("Q21. Filing-window denials: is there a single day threshold? (R9; Q14)", [
        f"Claims denied as \"{fw}\": {len(denied)}.",
        table(["Basis (calendar days)", "Denied: claims", "Denied: range", "All other claims", "Others: range",
               "One threshold separates them?"], rows),
        table(["Customer", "Filing-window denials", "Their delivery → receipt days",
               "Approved or partial claims", "Longest delivery → receipt, approved or partial"], crow),
        "\"Separates\" means every denied claim's gap is longer than every other claim's gap on that basis. "
        "Dates are as released; the system holds no contract terms (release 2 §2, `cold_chain_customer`).",
    ])


def main():
    claims = load()
    load_r2(claims)
    sections = [q(claims) for q in (q_volume, q_mix, q_cycle, q_stages, q_finance, q_weekday,
                                    q_size, q_approval, q_recovery, q_recovery_by_type, q_am,
                                    q_insurer, q_docs, q_outcomes, q_threshold_basis, q_reefer, q_insurer_clock, q_clean_pod, q_docs_deadline, q_docs_by_type, q_filing_window)]
    parts = [
        "# Data-vs-claims results (releases 1 and 2)",
        "> Fictional engagement for portfolio purposes. All data is synthetic.",
        "Generated by `analysis/data_checks.py` from `data/released/`. Do not edit by hand.",
        f"Claims in release: {len(claims)} (damage and shortage, received 2026-03-01 to 2026-08-31).",
        "Labelled assumption: the insurance deductible is taken as "
        f"{money(DEDUCTIBLE_ASSUMED)} from T2:L16 (\"I think?\"), pending CFO confirmation.",
    ]
    for title, body in sections:
        parts.append(f"## {title}")
        parts.extend(body)
    OUT.write_text("\n\n".join(parts) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
