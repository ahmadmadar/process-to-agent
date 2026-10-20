"""Coverage test for the future-state decision tree and scope table drafts.

Northline Freight is a fictional client. All data is synthetic.

Checks that each claim combination lands in exactly one tier. Two checks run:
- Scope table: every row whose condition matches, resolved by the precedence
  rule (G2): escalate > hold > human sign-off > autonomous. No matching row,
  or an unruled row, is a gap.
- Decision tree: the consultant's step order (decision-tree.md), first match wins.
The two must agree. Hold is a state, not a route (G3a).

Thresholds are provisional: $10k (C2, C5; D3) and the deductible, assumed
$25k until the CFO confirms it (D1). Amounts are claimed amounts (G4). Confidence is a yes/no against
CONFIDENCE_THRESHOLD, which is unset (P1).
Run from the repo root: python engagement/02-redesign/coverage_test.py
"""

from pathlib import Path

TEN_K = 10_000
DEDUCTIBLE = 25_000  # assumption, D1
OUT = Path("engagement/02-redesign/coverage-test.md")

ESC, SIGN, AUTO, HOLD, NONE = "always escalate", "human sign-off", "autonomous", "hold (state, no route)", "NOT RULED"
PRECEDENCE = [ESC, HOLD, SIGN, AUTO]  # G2: highest wins


def claim(label, amount, decision="approve", **flags):
    c = {
        "label": label, "amount": amount, "decision": decision, "type": "damage",
        "docs_complete": True, "at_deadline": False, "reefer": False,
        "temp_allegation": False, "cold_chain": False, "expedite": False, "key_account": False,
        "duplicate": False, "invoice_mismatch": False, "outside_window": False,
        "confidence_ok": True, "clean_pod": False,
    }
    c.update(flags)
    return c


# (row id, condition, tier, ruling, predicate). Mirrors scope-table.md.
ROWS = [
    ("R1", "Reefer equipment or temperature allegation", ESC, "C5, G5", lambda c: c["reefer"] or c["temp_allegation"]),
    ("R2", "Cold-chain contract customer", ESC, "C5c", lambda c: c["cold_chain"]),
    ("R3", "Account-manager expedite request", ESC, "C5, E4", lambda c: c["expedite"]),
    ("R4", "Amount above the deductible", ESC, "C5", lambda c: c["amount"] > DEDUCTIBLE),
    ("R5", "Documents incomplete, before deadline", HOLD, "C5b, G3a, G3b", lambda c: not c["docs_complete"] and not c["at_deadline"]),
    ("R6", "Documents incomplete at deadline", SIGN, "C5b", lambda c: not c["docs_complete"] and c["at_deadline"]),
    ("R7", "Possible duplicate", SIGN, "C5c", lambda c: c["duplicate"]),
    ("R8", "Amount does not match invoice", SIGN, "C5c", lambda c: c["invoice_mismatch"]),
    ("R9", "Outside customer filing window", SIGN, "C5c", lambda c: c["outside_window"]),
    ("R10", "Denial, any amount", SIGN, "C5", lambda c: c["decision"] == "deny"),
    ("R11", "Partial at or below $10k", SIGN, "C5a", lambda c: c["decision"] == "partial" and c["amount"] <= TEN_K),
    ("R13", "Amount above $10k, at or below deductible", SIGN, "C5", lambda c: TEN_K < c["amount"] <= DEDUCTIBLE),
    ("R14", "Confidence below threshold", SIGN, "C5c", lambda c: not c["confidence_ok"]),
    ("R15", "Approval at or below $10k, docs complete, no flags, confidence at or above threshold", AUTO, "C5, C5b, C5c",
     lambda c: c["type"] != "loss" and c["decision"] == "approve" and c["amount"] <= TEN_K and c["docs_complete"] and c["confidence_ok"]
     and not any(c[f] for f in ("reefer", "temp_allegation", "cold_chain", "expedite", "duplicate", "invoice_mismatch", "outside_window"))),
    ("R16", "Loss claim (agent pilot excludes)", ESC, "S1, G1", lambda c: c["type"] == "loss"),
]


def scope_table(c):
    hits = [(rid, tier) for rid, _, tier, _, test in ROWS if test(c)]
    tiers = sorted({t for _, t in hits}, key=lambda t: PRECEDENCE.index(t) if t in PRECEDENCE else -1)
    return hits, tiers


def resolve(tiers):
    # G2: highest tier wins. An unruled row, or no row, cannot be resolved.
    if not tiers or NONE in tiers:
        return None
    return tiers[0]


def tree(c):
    # The consultant's step order, decision-tree.md. Step 7 is an action, not a route.
    if c["type"] == "loss":
        return ESC, "0"
    if c["reefer"] or c["temp_allegation"] or c["cold_chain"] or c["expedite"] or c["amount"] > DEDUCTIBLE:
        return ESC, "1"
    if not c["docs_complete"]:
        return (SIGN, "2") if c["at_deadline"] else (HOLD, "2")
    if c["duplicate"] or c["invoice_mismatch"] or c["outside_window"]:
        return SIGN, "3"
    if c["decision"] in {"deny", "partial"}:
        return SIGN, "5"
    if c["decision"] == "approve" and c["amount"] <= TEN_K and c["confidence_ok"]:
        return AUTO, "6"
    return SIGN, "6"


def actions(c):
    out = []
    if c["clean_pod"] and c["type"] == "shortage":
        out.append("do not file with carrier (E6, UNTESTED)")
    if c["amount"] > DEDUCTIBLE:
        out.append("insurer 30-day clock alert")
    return "; ".join(out)


CASES = [
    claim("1. $9k partial, key account", 9_000, "partial", key_account=True),
    claim("2. $3k reefer claim", 3_000, reefer=True),
    claim("3. $12k, incomplete documents (at deadline)", 12_000, docs_complete=False, at_deadline=True),
    claim("4. $8k approval, duplicate flag", 8_000, duplicate=True),
    claim("5. $26k damage claim", 26_000),
    claim("6. $4k clean-POD shortage", 4_000, type="shortage", clean_pod=True),
    claim("7. $6k loss claim", 6_000, type="loss"),
    claim("8. $2k claim, expedite request", 2_000, expedite=True),
    claim("9. $7k approval, confidence below threshold", 7_000, confidence_ok=False),
    claim("10. $5k straight approval, all checks clean", 5_000),
]
PROBES = [
    claim("P1. $9k denial, reefer, key account", 9_000, "deny", reefer=True, key_account=True),
    claim("P2. $30k denial", 30_000, "deny"),
    claim("P3. $12k, incomplete documents (before deadline)", 12_000, docs_complete=False),
    claim("P4. $10,000 exactly, clean approval", 10_000),
    claim("P5. $25,000 exactly, clean approval", 25_000),
    claim("P6. $4k damage, temperature allegation, no reefer flag", 4_000, temp_allegation=True),
    claim("P7. $33k claimed, agent would partial at $18k (as NLC-26-0061, Q15)", 33_000, "partial"),
]


def table(cases):
    lines = [
        "| Combination | Scope-table rows matched | Tiers matched | Resolved (G2) | Decision tree (step) | Actions | Result |",
        "|---|---|---|---|---|---|---|",
    ]
    gaps = []
    for c in cases:
        hits, tiers = scope_table(c)
        t_tier, step = tree(c)
        resolved = resolve(tiers)
        if resolved is None:
            result = "GAP: no ruled tier"
        elif resolved != t_tier:
            result = "GAP: table and tree disagree"
        elif len(tiers) > 1:
            result = "OK: precedence (G2)"
        else:
            result = "OK: one tier"
        if result.startswith("GAP"):
            gaps.append(c["label"])
        lines.append(
            f"| {c['label']} | {', '.join(r for r, _ in hits) or 'none'} | {'; '.join(tiers) or 'none'} "
            f"| {resolved or '—'} | {t_tier} ({step}) | {actions(c) or '—'} | {result} |"
        )
    return lines, gaps


def main():
    case_lines, case_gaps = table(CASES)
    probe_lines, probe_gaps = table(PROBES)
    md = [
        "# Coverage Test: Decision Tree and Scope Table",
        "",
        "> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.",
        "",
        "Generated by `coverage_test.py`. Do not edit by hand.",
        "",
        "Each combination is checked two ways: against every scope-table row that",
        "matches, resolved by the precedence rule (G2: escalate > hold > human",
        "sign-off > autonomous), and through the decision tree in the consultant's",
        "step order (first match wins). The two must agree. Hold is a state, not a",
        "route (G3a). Thresholds: $10k (provisional, D3); deductible",
        "assumed $25k (D1). Unless stated, a combination is a damage claim, the",
        "agent's decision is approve, documents are complete, no flags are set and",
        "confidence is at or above `CONFIDENCE_THRESHOLD`.",
        "",
        "## Consultant's 10 combinations",
        "",
        *case_lines,
        "",
        f"Gaps: {len(case_gaps)} of {len(CASES)}" + (f" ({', '.join(case_gaps)})" if case_gaps else ""),
        "",
        "## Additional probes",
        "",
        *probe_lines,
        "",
        f"Gaps: {len(probe_gaps)} of {len(PROBES)}" + (f" ({', '.join(probe_gaps)})" if probe_gaps else ""),
        "",
    ]
    OUT.write_text("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
