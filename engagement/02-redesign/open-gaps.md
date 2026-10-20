# Future-State Design: Open Gaps

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Open gaps in `future-state-swimlane.md`, `decision-tree.md` and
`scope-table.md`, with the coverage results in `coverage-test.md`. Each open gap
needs a consultant ruling; the options listed are not recommendations.

## Coverage result

After rulings G1, G2, G3a and G3b (2026-10-19), all 10 combinations and
all 5 probes resolve to one tier, and the scope table and the decision tree
agree (`coverage-test.md`). G4 and G5 are resolved; G6–G12 remain open.

## Gaps that broke the coverage test (resolved)

| # | Gap | Evidence | Ruling |
|---|---|---|---|
| G1 | **Loss claims have no tier.** S1 excludes them from the agent, but no step in the tree catches them. A $6k loss approval passes every check and reaches autonomous. | Coverage #7; S1 | **Resolved, G1:** step 0, loss → always escalate. |
| G2 | **No precedence rule in the scope table.** A $9k reefer key-account denial matches escalate (R1) and sign-off (R10, R12). C5 itself overlaps: "all denials → sign-off" and "above the deductible → escalate" both match a $30k denial. The tree's step order implies the highest tier wins, but no ruling says so. | Probes P1, P2; C5 | **Resolved, G2:** highest tier wins; escalate > hold > sign-off > autonomous. |
| G3 | **Hold is a state, not a tier.** A $12k claim waiting for documents matches R13 (sign-off) in the table but is held in the tree. Also, C5b is worded for approvals at or below $10k; the tree applies the hold to every claim. | Probe P3; C5b | **Resolved, G3a:** hold is a state, not a route, in a visible "awaiting documents" list. **G3b:** the hold applies at every amount. |

## Definitions the rulings leave open

| # | Gap | Why it matters | Citation |
|---|---|---|---|
| G4 | **Resolved, G4: claimed amount for both thresholds (Q15).** Which amount meets the thresholds: the claimed amount, or the proposed payout? Step 1 runs before any decision, so it can only use the claimed amount. Step 6 runs after, so it could use either. | Decides the route for a $12k claim partially approved at $9k, or a $26k claim proposed at $20k | C5; T2:L16 |
| G5 | **Resolved, G5: reefer equipment or a temperature allegation (Q16).** Definition of the temperature/reefer trigger: a temperature-excursion claim, or any claim on reefer equipment? Release 2 `reefer_flag` is equipment mode. Under the equipment definition, a crushed pallet on a reefer load escalates. | Escalation volume and the eval inputs | C5; T2:L44; release 2 |
| G6 | **The key-account flag never changes a tier.** Key-account denials and partials are already sign-off under R10, R11 and R13 (coverage #1 matches two rows in the same tier). | It is redundant as a routing rule. Decide whether it does anything else (priority, notifying the account manager) or is dropped from routing. | C5c |
| G7 | **What each tier means in operation.** Sign-off: does the agent draft and a person approves or edits? Escalate: does the agent draft anything? Who owns each queue? Does the specialist/lead split at $10k carry over? Is there a response time? | Requirements v1 cannot specify the queues without this | C5; T2:L14, T2:L44 |
| G8 | **What autonomous covers.** Approve only, or also the payment instruction, the customer letter and the carrier filing? The swimlane draws the letter and filing with the team (no change ruled). | C4 gives payout ownership to the claims team; the agent acting for them needs a stated limit | C4, C5 |
| G9 | **Insurer clock start and consent gate.** "Within 30 days" of what: receipt, delivery or loss? Q12 measures from receipt. The swimlane shows the insurer step but no gate on the payment edge. | Escalation SLA and payment control | T2:L16, T2:L48; Q12 |
| G10 | **Re-routing on new information.** An expedite request after routing; documents that arrive after the deadline; a reefer claim after the download is secured: does it return to the agent? | Without a rule, claims stall or are routed twice | C5, E4, C5b |
| G11 | **The confidence score.** How it is produced (model self-report or a rubric) and how P1 is calibrated. | Step 6 depends on it | C5c; P1 |
| G12 | **Withdrawn and open claims** have no route. | Edge case for requirements | T2:L70 |

## Data dependencies for the Day 2 eval

| # | Rule | Status in the released data |
|---|---|---|
| D-a | Clean-POD (E6) | `pod_exception` is now in release 2. **E6 can be tested before requirements v1 is frozen.** Until then the autonomous tier applies an untested rule. |
| D-b | Invoice mismatch (C5c) | `invoice_amount` is not held (release 2). The check depends on the agent reading the invoice document; eval inputs will be labelled assumptions. |
| D-c | Filing window (C5c) | The rule is unknown; it is asked of the claims lead in data request 2 §5, which is unanswered. |
| D-d | Cold-chain customer (C5c) | Not held (release 2). T2:L44 names the customers, but the release uses anonymised IDs. |
| D-e | Duplicate (C5c) | `shipment_ref` is in release 2; no claim in the period has a prior payment on the same shipment. Eval cases for this rule must be constructed and labelled. |

## Smaller points

- **Rule-check order:** duplicates are checked only after documents are
  complete (step 3 follows step 2), so a duplicate waits through the hold.
  Consider checking duplicates at intake.
- **Loss claims outside the agent** still need the insurer and reefer rules
  applied by people. The swimlane shows the team handling them through
  redesigned steps but doesn't repeat those triggers.
- **D5 (COO ratification of C4 and E4)** is still open. The account-manager
  lane assumes it.
