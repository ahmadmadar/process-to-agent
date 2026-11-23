# Edge Cases

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Each case states the expected handling under `rules.md`.

## Multiple triggers

| # | Case | Handling |
|---|---|---|
| EC1 | Reefer claim above the deductible, from a cold-chain customer | Escalate. `triggers` = R1, R2, R4. `rule_applied` = R1. Fact pack shows both the reefer clock and the insurer dates. Claims lead |
| EC2 | Expedite request on a claim above the deductible | Escalate. `triggers` = R3, R4. Claims lead decides (another trigger fired). Payment gated on insurer consent |
| EC3 | Duplicate flag and invoice mismatch on the same claim | Sign-off. Both in `triggers`; `rule_applied` = R7 |
| EC4 | $9,000 key-account partial | Sign-off (R11). Specialists' queue, worked first |
| EC5 | Loss claim with a temperature allegation | Escalate at step 0 (R16). `triggers` = R16, R1. Handled as a reefer/temperature escalation: picked up on the day of receipt, fact pack shows the 72-hour download clock |

## Documents and timing

| # | Case | Handling |
|---|---|---|
| EC6 | Last document arrives on the fallback date before 23:59 ET | Documents complete. Re-run the tree from step 0 |
| EC7 | Documents arrive after the claim went to sign-off at the fallback date | Stays with the person (G10a), who sees the documents. No return to the agent |
| EC8 | Shortage without photos | Complete if invoice, BOL and delivery receipt/POD are received |
| EC9 | Reefer claim with no temperature download | Escalated at intake anyway. Fact pack shows the download as missing and the clock |
| EC10 | Temperature allegation on a non-reefer shipment | Escalate (R1). `reefer_flag` = N does not prevent it |
| EC11 | Ambiguous temperature wording ("product looked off") | Treated as an allegation. Escalate |
| EC12 | Claim received with every document already attached | No hold. Run steps 3–6 at once |

## Amounts and thresholds

| # | Case | Handling |
|---|---|---|
| EC13 | Claimed amount exactly $10,000.00 | At or below the line: eligible for autonomous |
| EC14 | Claimed amount exactly $25,000.00 | Not above the deductible: no R4. Above $10,000: sign-off (R13) |
| EC15 | Claimed $12,000, agent proposes paying $8,000 | Partial. Sign-off (R13), claims lead. Finance pre-approval applies (claimed amount > $10,000) |
| EC16 | Only part of the shipment is claimed, so the claimed amount is below the invoice total | Not a mismatch (R8). RB3 compares the claimed amount with the invoice value of the claimed goods only |
| EC17 | Invoice amount unreadable | Invoice mismatch (R8). Sign-off |
| EC18 | Delivery date missing | Filing window cannot be checked: treat as outside the window (R9). Sign-off |

## Expedite requests

| # | Case | Handling |
|---|---|---|
| EC19 | Request at 15:30 on a Monday | Answer due 12:00 Tuesday |
| EC20 | Request on Saturday, or on a company holiday | Answer due 12:00 the next business day |
| EC21 | Request on a held claim with no one working it | Escalate. Claims lead assigns or answers |
| EC22 | Request on a claim already approved | Answer may include the payment date |
| EC23 | Request on an undecided claim, account manager asks "can you confirm we're paying?" | Answer gives status, next step and expected date only. No payment commitment |
| EC24 | Second expedite request on the same claim | Recorded separately with its own due time. Route unchanged |
| EC25 | Expedite request after an autonomous decision | Escalate (R3): the re-run fires a step-1 trigger, which outranks sign-off. Answered under the SLA |

## Re-routing, withdrawals and duplicates

| # | Case | Handling |
|---|---|---|
| EC26 | Duplicate flag at intake; the earlier claim is later denied and closed | The flag stays; routing at step 3 re-checks: only paid or open claims count. If neither, no R7 |
| EC27 | Customer withdraws a held claim | `withdrawn`, reminders stop, leaves the list |
| EC28 | Customer withdraws after an autonomous payment | Sign-off |
| EC29 | Escalated reefer claim turns out to be ordinary damage | Stays with the person (G10b) |
| EC30 | Paid clean-POD shortage | Carrier filing package prepared like any other paid claim |
