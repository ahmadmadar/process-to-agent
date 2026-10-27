# Spike: Claims-Agent Evaluation

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

How the eval cases are built, snapshotted and reported. Rulings: EV1–EV3 in
`docs/consultant-decisions.md`.

## Cases

| Group | Source | Label (`source` field) |
|---|---|---|
| Sample | `data/released/eval_sample.csv` (IT release 2) | `sample` |
| Constructed | Built by the consultant to cover checks that the sample cannot test (EV3) | `constructed` |

Expected outcomes are written by the consultant from requirements v1 before
any run.

## Two snapshots per case (EV1)

1. **Intake.** The claim as received. The expected outcome is the hold (a
   state with no route) or escalate.
2. **Decision point.** The moment documents are complete under the E5a
   checklist, or `FALLBACK_DEADLINE_DAYS` (day 14) if they never complete.

**How the decision point is set for sample cases (EV2):** the historical
completion date is used only if every E5a checklist item for the claim type
is flagged as received. The delivery receipt/POD is treated as received when
the date is set, because no flag exists for it. Otherwise the snapshot is
taken at day 14. Each case records which rule set its moment.

## Hindsight rule

Each snapshot contains only what was knowable at that moment. It never
includes the outcome, the amount paid, the payment date, the recovery, or any
document received after the snapshot.

## Reporting (EV3)

Results are reported in two groups, sample and constructed, and are never
combined into one headline figure. Constructed cases test rule coverage, not
real-world frequency.

## Cost

Before any run, the estimated cost is stated for 2 snapshots × all cases × 2
models (EV1).
