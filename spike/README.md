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

## Snapshot construction

`spike/build_eval_set.py` writes `spike/eval_set.jsonl`: 78 snapshots (39
cases × 2). Expected outcomes are parsed from `expected-outcomes-v1.md`, and
each derived moment is checked against the date written there.

| Item | Convention |
|---|---|
| Intake | Event `received`, 09:00 ET on the receipt date. No documents yet |
| Decision point, documents complete | Event `documents_updated`, 12:00 ET on the completion date. Every checklist item, POD included, received on that date (EV2) |
| Decision point, fallback | Event `fallback_check`, 23:59 ET on day 14. Items flagged received are listed without a date; the POD is missing (no completion date by day 14) |
| Decision point, reefer sample cases | Same as intake (G10b), as written in the expected outcomes |
| `current_state` at the decision point | The state the intake evaluation produced: held, or escalated |
| Constructed cases | Every checklist item received on the base claim's completion date. K02's expedite request is in the decision-point snapshot |
| `invoice_amount` | `amount_claimed` (E-d), except K04 |
| `other_claims_same_shipment` | Derived from release 1 by `shipment_ref`, with each claim's status as known at the snapshot |
| Not held in the release | `claim_text` (except K09), `shipment_record`, and the content of photos, BOL and POD. Sent as null |

The clock times (09:00, 12:00) are a harness convention; the release holds dates only.

## Harness

| File | Does |
|---|---|
| `.claude/skills/claims-agent/SKILL.md` | The agent prompt, built from v1. `run_eval.py` loads it directly |
| `run_eval.py` | Runs one model over the eval set; scores each snapshot; appends traces to `traces/<model>.jsonl`; writes `runs/<run_id>__<model>.json` |
| `report.py` | Writes `metrics.md` and `queues/<model>.md` (sign-off queue view) from the latest run per model |

Output is constrained to a JSON schema (structured outputs). Scoring is
deterministic, and there is no LLM-as-judge. Route, status and `rule_applied` are scored on every
snapshot, and the decision only where the rules determine it. Triggers are reported but not scored.

## Cost

Before any run, the estimated cost is stated for 2 snapshots × all cases × 2
models (EV1). `run_eval.py --estimate` counts input tokens through the API
(free) and prices output at a stated assumption.
