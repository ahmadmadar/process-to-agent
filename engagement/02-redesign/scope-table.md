# Scope Table: Claims Agent

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Rows match `coverage_test.py` (R1–R16), and the coverage results are in
`coverage-test.md`. Open gaps are listed in `open-gaps.md`.

Thresholds: $10k provisional (D3); deductible assumed $25k (D1). Both are measured on the claimed amount (G4).
Parameters: `CONFIDENCE_THRESHOLD` (P1; two thresholds under G11, rubric and self-report), `FALLBACK_DEADLINE_DAYS` (P2), all unset.

**Precedence (G2).** Rows are not mutually exclusive. When a claim matches
more than one row, the highest wins: always escalate > hold > human sign-off >
autonomous. This follows the decision-tree order.

**Hold is a state, not a route (G3a).** A held claim has no route. It sits in
the "awaiting documents" list until its documents are complete or
`FALLBACK_DEADLINE_DAYS` is reached. The hold applies at every amount (G3b).

| # | Condition | Tier | Rationale | Citation | Ruling |
|---|---|---|---|---|---|
| R1 | Temperature/reefer claim: reefer equipment (`reefer_flag` = Y) or a temperature-excursion allegation | Always escalate | Temperature download kept ~72h and must be requested the same day; cannot sit in a queue | T2:L44, T2:L58; Q16 | C5, G5 |
| R2 | Cold-chain contract customer | Always escalate | Contract liability regardless of carrier; a liability question, not an agent decision | T2:L44 | C5c |
| R3 | Account-manager expedite request | Always escalate | Commercial urgency goes to an accountable person; never auto-approved | T1:L10, T2:L14, T2:L54 | C5, C4, E4 |
| R4 | Claimed amount above the deductible | Always escalate | Insurer notice within 30 days and consent before settlement; paying first lost cover once | T2:L16, T2:L48; Q12 | C5 |
| R5 | Documents incomplete, before `FALLBACK_DEADLINE_DAYS`, any amount | Hold (state, no route): "awaiting documents" list; automated reminders | The agent never decides on incomplete documents; at intake, the decision is not yet known | T2:L30, T2:L34; Q11, Q13 | C5b, E5, G3a, G3b |
| R6 | Documents incomplete at `FALLBACK_DEADLINE_DAYS` | Human sign-off | Replaces unwritten "judgment" with a fixed point that goes to a person | T2:L34; Q11 | C5b |
| R7 | Possible duplicate: same shipment or claim already paid | Human sign-off | Duplicate payments have happened; one was written off | T2:L68 | C5c |
| R8 | Claimed amount does not match the invoice | Human sign-off | The invoice is the value the team works from | T2:L42 | C5c |
| R9 | Outside the customer filing window | Human sign-off | Filing-window denials occur in the data | Q14 | C5c |
| R10 | Denial, any amount | Human sign-off | A wrongful denial to a key account is the COO's red line; the claims lead wants a person on every denial | T1:L36, T2:L16, T2:L58 | C5 |
| R11 | Partial at or below $10k | Human sign-off | A partial is a partial denial; salvage or depreciation amounts are judgment calls | T1:L36; Q14 | C5a |
| R12 | *Removed from routing (G6).* Key-account denials and partials reach sign-off through R10, R11 and R13 | — | Never decided a route; replaced by priority and account-manager notice (see Actions) | T1:L10, T1:L36 | C5c, G6 |
| R13 | Claimed amount above $10k, at or below the deductible | Human sign-off | Matches the existing specialist/lead approval line | T2:L14, T2:L62; Q8 | C5 |
| R14 | Agent confidence fails either gate: rubric score or self-reported confidence below its threshold | Human sign-off | A low-confidence decision should not go out unreviewed; doubt from either signal sends it to a person | — (consultant parameters, P1) | C5c, G11 |
| R15 | Damage or shortage approval, claimed amount at or below $10k, documents complete, no flags (R1–R3, R7–R9), confidence ≥ `CONFIDENCE_THRESHOLD` | Autonomous | Routine, documented, low-value approvals; key-account approvals may stay autonomous | T2:L14, T2:L58; Q8 | C5, C5b, C5c |
| R16 | Loss claim | Always escalate | Outside the agent pilot; different evidence; not in release 1; phase-2 candidate | T2:L50 | S1, G1 |

## Actions and alerts (not tiers)

| Condition | Action | Citation | Ruling |
|---|---|---|---|
| Paid shortage claim with a clean POD | Do not file with the carrier. **UNTESTED** | T2:L20, T2:L64; Q10 | E6 |
| Escalated claim above the deductible | Urgency alert: insurer 30-day notice. Shows delivery and receipt dates, no countdown, until the CFO confirms the start (G9a) | T2:L16, T2:L48; Q17 | C5c, G9a |
| Claim above the deductible, before payment | Hard gate: no payment instruction until insurer consent is recorded on the claim | T2:L16; Q12 | G9b |
| Approval above $10k after sign-off | Finance pre-approval | T2:L56; Q5 | C2, E1 |
| Denial after sign-off | No finance pre-approval | T2:L56, T2:L60; Q5 | E2 |
| Key-account claim in the sign-off or escalation queue | Worked first in that queue | T1:L10 | G6 |
| Key-account claim decided | Account manager notified of the outcome; no approval or payment rights | T1:L10; C4 | G6 |

## Re-routing and withdrawals

| Event | Effect | Ruling |
|---|---|---|
| New information before a decision (expedite request, late documents, new flag) | Re-run the decision tree; the claim can move up a tier, never down | G10a |
| New information on a claim already with a person | Stays with that person, who sees the new information | G10a |
| New information after an autonomous decision | Human sign-off | G10a |
| Escalated claim found to be simple | No handback; a person finishes it | G10b |
| Customer withdraws, nothing paid | Status `withdrawn`, date and reason recorded; leaves any hold or queue, no route | G12 |
| Customer withdraws, payment already made | Human sign-off | G12 |

## Operations by tier

| Tier | Agent produces | Who works it | Response time | Ruling |
|---|---|---|---|---|
| Autonomous | Decision, customer letter and payment instruction (no pre-approval, E1). Carrier filing package prepared, or "do not file" for clean-POD shortages (E6) | Specialist submits the carrier filing. Pilot: a person reviews every autonomous decision after it is made | — | C5, G8a, G8b |
| Human sign-off | Full draft: decision, amount, rule applied, rationale, customer letter. The person approves, edits or overrides; every edit or override is logged with a reason | Specialists: claimed amount ≤ $10k. Claims lead: > $10k | No target in v1; measured in the pilot | G7a, G7c, G7d |
| Always escalate | Fact pack: trigger(s), document checklist status, running clocks (72h reefer; insurer 30-day dates, G9a). No decision, no amount | Claims lead; the senior specialist as backup | Reefer/temperature: same day as receipt. Others: no target in v1 | G7b, G7c, G7d |
| Hold (state, no route) | Automated reminders; at `FALLBACK_DEADLINE_DAYS`, routes to sign-off | Claims specialists own the "awaiting documents" list | — | G3a, G7e, E5 |
