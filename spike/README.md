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
Conventions accepted by the consultant (EV10).

**Caveat on fallback snapshots.** The document flags show status at extract,
not at day 14 (release 2 §4 Q1). A fallback snapshot may therefore show a
document as received that arrived after day 14 (for example NLC-26-0310,
completed on day 16). This changes no expected outcome: the POD is missing in
every fallback snapshot, so the claim routes to R6 either way.

## Harness

| File | Does |
|---|---|
| `.claude/skills/claims-agent/SKILL.md` | The agent prompt, built from v1. `run_eval.py` loads it directly |
| `run_eval.py` | Runs one model over the eval set; scores each snapshot; appends traces to `traces/<model>.jsonl`; writes `runs/<run_id>__<model>.json` |
| `report.py` | Writes `metrics.md` and `queues/<model>.md` (sign-off queue view) from the latest run per model |

Output is constrained to a JSON schema (structured outputs). Scoring is
deterministic, and there is no LLM-as-judge. Route, status and `rule_applied` are scored on every
snapshot, and the decision only where the rules determine it. Triggers are reported but not scored.
Every output is also checked against the v1 output schema and its field rules (for example, route
null on a hold, fact pack required on escalate); violations are reported, not scored.

## Models and reporting

- **Models:** Sonnet 5.5 against Haiku 5.5, at the same pinned effort level (EV8). Opus 5.5 only if Sonnet fails.
- **Headline:** routing correctness on escalate, hold and sign-off snapshots. Autonomous* snapshots
  are reported on their own line, with gate-held (R14) cases counted separately (EV9).
- **The autonomous tier is untested on released data:** document content and shipment records are
  not held, so the rubric cannot pass on sample cases.
- **v2 gaps:** an escalation caused by a null `claim_text` under "if unsure, treat it as an
  allegation" is logged as a v2 gap, not a harness bug (EV9).
- **Refusals:** no server-side fallback to another model. A refusal is a failure, reported as its
  own category (EV11).

## Cost

Before any run, the estimated cost is stated for 2 snapshots × all cases × 2
models (EV1). A smoke test (`run_eval.py --smoke`, three snapshots per model)
measures tokens per call, and the full-run estimate is made from those
measurements (EV12). The API key's workspace keeps its hard monthly spend limit.
