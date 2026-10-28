# Gaps Carried to Requirements v2

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Gaps in requirements v1 found after the freeze. v1 is not edited (ground
rule 7); each gap is ruled on by the consultant and resolved in v2. Sources:
the spike eval (`EG` IDs) and the cold-FDE handoff test (added once the
consultant has classified `handoff-v1.md`).

## From the spike eval

| ID | Gap | Evidence | Status |
|---|---|---|---|
| EG1 | v1 does not say what the step-4 draft decision should be when the evidence cannot be verified. With no shipment record and no BOL or POD content, RB1, RB2 and RB5 fail. One model drafted a denial (sign-off by R10); every other draft on the same inputs was an approval sent to sign-off by a failed gate (R14). Both reach a person, but through different rules, with a different draft in front of the specialist | Haiku 5.5, run `20261027T215318-0bee8a`, `NLC-26-0053/decision_point`: `deny`, R10, rubric 0.50. Sonnet 5.5 drafted `approve` with R14 on all 19 autonomous* snapshots; Haiku 5.5 on 18 of 19 (`spike/metrics.md`) | Open: ruling needed (consultant) |

**Where v1 is silent (EG1).** `rules.md` step 4 says the agent forms a
decision, and step 5 sends a denial to R10. The rubric (RB1–RB6) and gate 1
say when the autonomous tier is blocked, but not whether a failed rubric item
is grounds for a denial draft or only for sign-off. `G7a` requires a draft on
sign-off claims without saying how unverifiable evidence affects it.
