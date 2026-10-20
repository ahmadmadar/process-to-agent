# Future-State Inputs: What the Swimlane Must Reflect

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Checklist for the consultant's future-state swimlane, drawn from the Day 1
rulings in `docs/consultant-decisions.md` ("Discovery rulings" and "Redesign
rulings"). The swimlane is not drawn yet. Items marked **⚠** depend on
something still open (see Open dependencies D1–D8 and Open parameters P1–P2).

## Lanes

- [ ] Customer
- [ ] Claims agent (new)
- [ ] Claims team: sign-off and escalation queue (C5)
- [ ] Account manager: expedite requests only, no approve or pay (C4, E4) **⚠ D5**
- [ ] Finance: pre-approval above $10k only (C2, E1, E2) **⚠ D1, D2, D4**; payments (E3)
- [ ] Carrier
- [ ] Cargo insurer

## Claim types (S1)

- [ ] Redesigned steps apply to the shared process, so loss claims go through them too (S1; T2:L50). No loss-specific steps are designed
- [ ] Mark where the agent pilot excludes loss claims; loss is the phase-2 candidate (S1)

## Intake and documents

- [ ] Intake requests every required document up front, using a structured checklist and a deadline (E5)
- [ ] Automated reminders replace manual email chasing (E5)
- [ ] Written fallback rule replaces "judgment" (E5; T2:L34): the agent holds the claim and sends reminders; at `FALLBACK_DEADLINE_DAYS` it routes to human sign-off (C5b) **⚠ P2**
- [ ] Temperature/reefer claims escalate to a person at intake, never queued (C5; T2:L44, T2:L58)
- [ ] Account-manager expedite requests enter at intake and route to a person, never auto-approved (C4, E4) **⚠ D5**

## Decision routing (C5)

- [ ] **Autonomous:** approvals at or below $10k with complete documents, no special flags and confidence ≥ `CONFIDENCE_THRESHOLD` (C5, C5b, C5c) **⚠ D3, P1**
- [ ] **Human sign-off:** all denials; partials at or below $10k (C5a); claims above $10k and at or below the deductible; incomplete documents at `FALLBACK_DEADLINE_DAYS` (C5b); key-account denials or partials, possible duplicates, invoice mismatches, out-of-window claims, low confidence (C5c) **⚠ D1, D3, P1, P2**
- [ ] **Always escalate:** claims above the deductible; temperature/reefer claims; expedite requests; cold-chain contract customers (C5c) **⚠ D1**
- [ ] Insurer 30-day notice clock shown as an urgency alert on escalated claims, not a routing flag (C5c)
- [ ] Every path ends in exactly one route (SOW deliverable #2); check against C5a–c

## After the decision

- [ ] Finance pre-approval only for claims above $10k (C2, E1) **⚠ D2, D3**
- [ ] No pre-approval for denial letters (E2) **⚠ D2**
- [ ] Payment on approval or a more frequent run, shown as a **finance recommendation**, not an agent step (E3) **⚠ D2**
- [ ] Insurer notified within 30 days and consent obtained before settlement, for claims above the deductible (C5; T2:L16) **⚠ D1**
- [x] ~~Clean-POD shortages are not filed with the carrier (E6)~~ Reversed by E6a: clean-POD shortages are filed (Q18)
- [ ] Carrier filing for all other paid claims with evidence (E5, E6)

## Removed from the current state

Show these as removed, with the ruling ID:

- [ ] Finance pre-approval at or below $10k (E1)
- [ ] Finance pre-approval of denials (E2)
- [ ] Weekly Thursday payment batch (E3)
- [ ] Account-manager early-payment path (E4)
- [ ] Unstructured email chasing (E5, redesigned)

## Measures carried into the business case

- [ ] Recovery baseline: recovered ÷ paid across all paid claims, with the accepted-claims rate alongside (C3; Q9) **⚠ D4**
- [ ] Hands-on effort (~3 hours per claim) as a labelled assumption (C1; T2:L66)

## Open dependencies

| # | Dependency | Owner | Affects | When |
|---|---|---|---|---|
| D1 | Confirm the deductible amount (assumed ~$25k, T2:L16) | CFO | C5 tiers, insurer step | Day 3 |
| D2 | Agree removal of pre-approval at or below $10k and for denials, and the payment-run change | CFO (control owner) | C2, E1, E2, E3 | Day 3 |
| D3 | CFO challenge on the $10k thresholds; revisions logged as new decisions | CFO | C2, C5, E1 | Day 3 |
| D4 | Confirm the recovery definition and the source of the COO's ~70% (T1:L18) | CFO | C3 | Day 3 |
| D5 | Ratify claims-team ownership of payouts and the expedite path (SOW §8) | COO (sponsor) | C4, E4 | Before requirements v1 is frozen |
| D6 | ~~Rule on C5 open points~~ **Resolved 2026-10-18:** see C5a (partials), C5b (incomplete documents), C5c (special flags) | Consultant | C5 | Done |
| D7 | ~~POD-exception field to test the clean-POD rule~~ **Resolved:** release 2; tested in Q18; E6 reversed by E6a | Follow-up data request | E6, E6a | Done |
| D8 | Late-notice discrepancy: "two other" late notices (T2:L16) vs one in Q12 | CFO | C6 | Day 3 |
| D9 | Confirm when the insurer's 30-day notice period starts (policy wording; Q17) | CFO | G9a | Day 3 |

## Open parameters

Consultant-owned and unset (see "Consultant-owned parameters" in
`docs/consultant-decisions.md`).

| # | Parameter | Affects | When |
|---|---|---|---|
| P1 | `CONFIDENCE_THRESHOLD`: two thresholds under G11 (rubric score, self-reported confidence); calibrated in the Day 2 eval | Autonomous tier (C5), C5c, G11 | Day 2 |
| P2 | `FALLBACK_DEADLINE_DAYS` | C5b, E5 | Requirements v1 |
