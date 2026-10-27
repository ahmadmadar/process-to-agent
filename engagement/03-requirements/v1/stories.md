# User Stories and Acceptance Criteria

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Rules referenced here are defined in `rules.md`. Each acceptance criterion is
testable from the agent output and the decision trace.

## Intake

**US-01. Escalate out-of-scope and high-risk claims at intake.**
As the claims lead, I want claims that the agent must not decide sent to me
the moment they arrive, so no clock runs out in a queue.

- Given a loss claim, the agent returns `route` = `escalate`, `rule_applied` = `R16`, `decision` = null. It runs no step after step 1. Step-1 triggers are still evaluated for `triggers` and the fact pack; `rule_applied` stays `R16`.
- Given `reefer_flag` = Y or a temperature allegation, the agent returns `escalate`, `R1` in `triggers`, and a fact pack whose `clocks` says the download must be requested today.
- Given a cold-chain customer, an expedite request, or a claimed amount above the deductible, the agent returns `escalate` with R2, R3 or R4 in `triggers`.
- When several step-1 triggers fire, all appear in `triggers`, and `rule_applied` is the first in table order.
- Escalated claims never carry a decision or an amount.

**US-02. Request every document up front.**
As a claims specialist, I want the customer asked for the full checklist on
day 0, so I stop chasing documents by email.

- On receipt of a non-escalated claim, the agent sends the checklist for the claim type with the fallback date, and records day 0 in `reminders_sent`.
- The checklist matches the claim type table in `rules.md` (photos optional for shortages).

**US-03. Flag possible duplicates at intake.**
As a claims specialist, I want to see a likely duplicate before I chase its documents.

- If another claim with the same `shipment_ref` is paid or open, `hold.duplicate_flag` = true.
- The flag does not change the route while the claim is held. After documents are complete, the claim goes to sign-off with `rule_applied` = `R7`.

## Documents and hold

**US-04. Hold claims with incomplete documents.**
As a claims specialist, I want claims without full documents held and visible,
not decided.

- While documents are incomplete and the fallback date has not passed, `status` = `held`, `route` = null, `decision` = null, `rule_applied` = `R5`.
- The hold applies at every amount.
- `hold.missing_items` lists only items not yet received.

**US-05. Remind automatically.**
- Reminders go out on days 3, 7 and 11 after receipt, listing only missing items. Each date is added to `hold.reminders_sent`.
- The day-11 reminder states the fallback date.
- No reminder is sent after documents are complete or the claim leaves the hold.

**US-06. Release at completion or the fallback date.**
- When the last required document arrives, the agent re-runs the tree from step 0.
- If documents are still incomplete at 23:59 ET on the fallback date, the claim goes to sign-off with `rule_applied` = `R6`, and the agent drafts a decision on the documents held.
- The agent never forms an autonomous decision on incomplete documents.

## Routing

**US-07. Send flagged claims to a person.**
- A possible duplicate, invoice mismatch or claim outside the filing window goes to sign-off with R7, R8 or R9.
- Every flag that fired is listed in `triggers`.

**US-08. Send every denial and partial to a person.**
- Any `deny` goes to sign-off (R10), at any amount, key accounts included.
- Any `partial` at or below $10,000 goes to sign-off (R11); above $10,000, R13.

**US-09. Score confidence two ways.**
- On every claim that reaches step 4, the agent returns `rubric_score`, `rubric_items` (RB1–RB6) and `self_reported_confidence`.
- If `rubric_score` < `RUBRIC_SCORE_THRESHOLD` or `self_reported_confidence` < `SELF_REPORTED_CONFIDENCE_THRESHOLD`, the route is `sign_off` with `rule_applied` = `R14`.

## Autonomous tier

**US-10. Approve routine claims without waiting.**
As a customer, I want a straightforward, fully documented claim paid without
waiting for review steps.

- The route is `autonomous` only when: damage or shortage; claimed amount ≤ $10,000; documents complete; no step-1 trigger; no step-3 flag; `decision` = `approve`; both gates pass.
- On an autonomous approval, the agent sends the customer letter and the payment instruction to finance, with no finance pre-approval.
- The agent prepares the carrier filing package. A specialist submits it.

**US-11. Review every autonomous decision during the pilot.**
- Every autonomous decision appears in the autonomous reviewer's list after it is made.
- The reviewer records agree or disagree, with a reason on disagree. The result is stored with the claim.

## Human sign-off tier

**US-12. Approve from a full draft.**
As a specialist or the claims lead, I want a full draft to approve, so I am
editing, not writing from scratch.

- For every sign-off claim, the agent provides decision, amount, rule applied, rationale and customer letter.
- The person approves, edits or overrides. Every edit or override is logged with a reason.
- Claims with a claimed amount ≤ $10,000 go to the specialists' queue; above $10,000 to the claims lead.
- Key-account claims appear first in each queue.

## Always-escalate tier

**US-13. Work escalations from a fact pack.**
- Every escalated claim has a fact pack: triggers, checklist status, clocks.
- Reefer/temperature escalations are picked up on the day of receipt. The claims lead works them, with the senior specialist as backup.
- Loss, cold-chain and above-deductible escalations go to the claims lead, with the senior specialist as backup.
- An escalated claim is never handed back to the agent or the sign-off path.

## Expedite requests

**US-14. Answer every expedite request on time.**
As an account manager, I want a reliable answer to an expedite request, so I
can tell the customer something concrete.

- An expedite request always escalates the claim (R3), whatever its state, including a held claim.
- If a specialist is already working the claim, that specialist is assigned the answer. Otherwise the claims lead is assigned.
- The answer due time follows `EXPEDITE_RESPONSE_SLA` and is shown in the fact pack.
- If the expedite request is the only trigger, the claim stays with the specialist queue when the claimed amount is ≤ $10,000, and goes to the claims lead above that. If any other trigger fired, it goes to the claims lead.

**US-15. Keep expedite answers within limits.**
- The answer contains status, next step, and expected date where known.
- A payment commitment is allowed only if the claim's decision has already been approved by the claims team. The system blocks a payment commitment otherwise.

**US-16. Record expedite requests.**
- For every expedite request, the system records request time, answer time, answer content and outcome.

**US-17. Notify on an SLA miss.**
- If no answer is recorded by the due time, the system notifies the claims lead and the requesting account manager automatically.

## Payment, insurer and carrier filing

**US-18. Apply finance pre-approval only above $10,000.**
- Approvals and partials with a claimed amount ≤ $10,000 go to payment without pre-approval.
- Above $10,000, they go to finance pre-approval first.
- Denials never go to pre-approval.

**US-19. Gate payment on insurer consent.**
As the CFO, I want no claim above the deductible paid before the insurer agrees.

- For a claimed amount above the deductible, the system refuses to issue a payment instruction until insurer consent is recorded on the claim by the claims lead.
- The fact pack shows the delivery date and receipt date for the insurer notice, with no countdown.

**US-20. File every paid claim with the carrier.**
- For every paid claim with documents complete, the agent prepares a carrier filing package, including clean-POD shortages.
- A specialist submits it.

## Re-routing and withdrawals

**US-21. Re-route on new information, upward only.**
- New information before a decision re-runs the tree. The new route is never lower than the current one.
- A claim already with a person stays with that person, who is shown the new information.
- New information after an autonomous decision sends the claim to sign-off, or to escalate if the re-run fires a step-1 trigger.

**US-22. Record withdrawals.**
- If nothing has been paid, `status` = `withdrawn`, `route` = null, with withdrawal date and reason. The claim leaves any hold or queue.
- If a payment has been made, the claim goes to sign-off.

## Notifications

**US-23. Tell account managers the outcome.**
- When a key-account claim is decided, the account manager is notified of the outcome.
- The notice gives no approval or payment rights.
