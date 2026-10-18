# Future-State Inputs: What the Swimlane Must Reflect

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Checklist for the consultant's future-state swimlane, drawn from the Day 1
rulings in `docs/consultant-decisions.md` ("Discovery rulings"). The swimlane
is not drawn yet. Items marked **⚠** depend on something still open (see
Open dependencies).

## Lanes

- [ ] Customer
- [ ] Claims agent (new)
- [ ] Claims team: sign-off and escalation queue (C5)
- [ ] Account manager: expedite requests only, no approve or pay (C4, E4) **⚠ D5**
- [ ] Finance: pre-approval above $10k only (C2, E1, E2) **⚠ D1, D2, D4**; payments (E3)
- [ ] Carrier
- [ ] Cargo insurer

## Intake and documents

- [ ] Intake requests every required document up front, using a structured checklist and a deadline (E5)
- [ ] Automated reminders replace manual email chasing (E5)
- [ ] Written fallback rule for deciding on incomplete documents replaces "judgment" (E5; T2:L34). **Requirement to be specified** by the consultant in requirements v1
- [ ] Temperature/reefer claims escalate to a person at intake, never queued (C5; T2:L44, T2:L58)
- [ ] Account-manager expedite requests enter at intake and route to a person, never auto-approved (C4, E4) **⚠ D5**

## Decision routing (C5)

- [ ] **Autonomous:** approvals at or below $10k with complete documents and no special flags **⚠ D3, D6**
- [ ] **Human sign-off:** all denials; claims above $10k and at or below the deductible **⚠ D1, D3**
- [ ] **Always escalate:** claims above the deductible; temperature/reefer claims; expedite requests **⚠ D1**
- [ ] Every path ends in exactly one route (SOW deliverable #2) **⚠ D6** (C5 open points leave some claims unrouted)

## After the decision

- [ ] Finance pre-approval only for claims above $10k (C2, E1) **⚠ D2, D3**
- [ ] No pre-approval for denial letters (E2) **⚠ D2**
- [ ] Payment on approval or a more frequent run, shown as a **finance recommendation**, not an agent step (E3) **⚠ D2**
- [ ] Insurer notified within 30 days and consent obtained before settlement, for claims above the deductible (C5; T2:L16) **⚠ D1**
- [ ] Clean-POD shortages are not filed with the carrier; rule marked **UNTESTED** (E6; Q10) **⚠ D7**
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
| D6 | Rule on C5 open points: partial approvals ≤ $10k, approvals ≤ $10k with incomplete documents, and which special flags apply | Consultant | C5 | Before the future-state swimlane |
| D7 | POD-exception field to test the clean-POD rule | Follow-up data request | E6 | Release 2 |
| D8 | Late-notice discrepancy: "two other" late notices (T2:L16) vs one in Q12 | CFO | C6 | Day 3 |
