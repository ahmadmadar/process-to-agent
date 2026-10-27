# Non-Functional Requirements

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

## Decision trace and audit

- **NF-01.** Every evaluation of a claim writes one trace record (JSON Lines). A claim evaluated several times (intake, documents complete, new information) has one record per evaluation.
- **NF-02.** Each trace record contains: `claim_id`; evaluation timestamp (ET, ISO 8601 with offset); the event that triggered the evaluation; the inputs the agent saw; each tree step reached with its result; every trigger and flag evaluated, fired or not; the full agent output (`rules.md`, Agent output); model name; input and output tokens; latency; cost.
- **NF-03.** The inputs in a trace are only what was known at that moment. No later document, outcome or payment appears in it.
- **NF-04.** Trace records are append-only. A correction is a new record that references the one it corrects.

## Records

- **NF-05.** Every sign-off edit or override is stored with the person, the time, the field changed, the old and new values, and the reason.
- **NF-06.** Every autonomous review is stored with the reviewer, the time, agree or disagree, and the reason on disagree.
- **NF-07.** Every expedite request is stored with the requester, request time, answer due time, answer time, answer content, who answered, and outcome.
- **NF-08.** Insurer consent is stored with the date and the person who recorded it.
- **NF-09.** Withdrawals are stored with date and reason.
- **NF-10.** Hold history is stored: the day-0 request, each reminder date, and the release reason (complete, fallback, withdrawn, escalated).

## Service levels

- **NF-11.** Reefer/temperature escalations are picked up on the day of receipt.
- **NF-12.** Expedite answers meet `EXPEDITE_RESPONSE_SLA`. Misses trigger the automatic notice (US-17).
- **NF-13.** No other response-time target applies in v1. Queue wait times are measured in the pilot.
- **NF-14.** The intake evaluation (steps 0–2) runs when the claim is received, so reefer and temperature claims reach the claims lead on the day of receipt.

## Cost and latency

- **NF-15.** No cost or latency target in v1. Both are measured per evaluation and reported per model in the eval.
- **NF-16.** Every model call logs token usage and cost. Before any batch run, the estimated cost is stated.

## Data handling

- **NF-17.** No personally identifiable information is sent to the model beyond what is on the claim and its documents. Staff are referred to by role, not name, in outputs.
- **NF-18.** API keys are held outside version control.
- **NF-19.** All data in this engagement is synthetic.
