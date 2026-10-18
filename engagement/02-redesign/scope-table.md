# Scope Table: Claims Agent

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Rows match `coverage_test.py` (R1–R16), and the coverage results are in
`coverage-test.md`. Open gaps are listed in `open-gaps.md`.

Thresholds: $10k provisional (D3); deductible assumed $25k (D1).
Parameters: `CONFIDENCE_THRESHOLD` (P1), `FALLBACK_DEADLINE_DAYS` (P2), both unset.

| # | Condition | Tier | Rationale | Citation | Ruling |
|---|---|---|---|---|---|
| R1 | Temperature/reefer claim | Always escalate | Temperature download kept ~72h and must be requested the same day; cannot sit in a queue | T2:L44, T2:L58 | C5 |
| R2 | Cold-chain contract customer | Always escalate | Contract liability regardless of carrier; a liability question, not an agent decision | T2:L44 | C5c |
| R3 | Account-manager expedite request | Always escalate | Commercial urgency goes to an accountable person; never auto-approved | T1:L10, T2:L14, T2:L54 | C5, C4, E4 |
| R4 | Amount above the deductible | Always escalate | Insurer notice within 30 days and consent before settlement; paying first lost cover once | T2:L16, T2:L48; Q12 | C5 |
| R5 | Documents incomplete, before `FALLBACK_DEADLINE_DAYS` | Hold at intake (no tier yet); automated reminders | The agent never decides on incomplete documents | T2:L30, T2:L34; Q13 | C5b, E5 |
| R6 | Documents incomplete at `FALLBACK_DEADLINE_DAYS` | Human sign-off | Replaces unwritten "judgment" with a fixed point that goes to a person | T2:L34; Q11 | C5b |
| R7 | Possible duplicate: same shipment or claim already paid | Human sign-off | Duplicate payments have happened; one was written off | T2:L68 | C5c |
| R8 | Claimed amount does not match the invoice | Human sign-off | The invoice is the value the team works from | T2:L42 | C5c |
| R9 | Outside the customer filing window | Human sign-off | Filing-window denials occur in the data | Q14 | C5c |
| R10 | Denial, any amount | Human sign-off | A wrongful denial to a key account is the COO's red line; the claims lead wants a person on every denial | T1:L36, T2:L16, T2:L58 | C5 |
| R11 | Partial at or below $10k | Human sign-off | A partial is a partial denial; salvage or depreciation amounts are judgment calls | T1:L36; Q14 | C5a |
| R12 | Key-account customer, denial or partial | Human sign-off | COO red line on wrongful key-account denials | T1:L10, T1:L36 | C5c |
| R13 | Amount above $10k, at or below the deductible | Human sign-off | Matches the existing specialist/lead approval line | T2:L14, T2:L62; Q8 | C5 |
| R14 | Agent confidence below `CONFIDENCE_THRESHOLD` | Human sign-off | A low-confidence decision should not go out unreviewed | — (consultant parameter, P1) | C5c |
| R15 | Approval at or below $10k, documents complete, no flags (R1–R3, R7–R9), confidence ≥ `CONFIDENCE_THRESHOLD` | Autonomous | Routine, documented, low-value approvals; key-account approvals may stay autonomous | T2:L14, T2:L58; Q8 | C5, C5b, C5c |
| R16 | Loss claim | **Not ruled** (agent pilot excludes; see `open-gaps.md` G1) | Different evidence; not in release 1; phase-2 candidate | T2:L50 | S1 |

## Actions and alerts (not tiers)

| Condition | Action | Citation | Ruling |
|---|---|---|---|
| Paid shortage claim with a clean POD | Do not file with the carrier. **UNTESTED** | T2:L20, T2:L64; Q10 | E6 |
| Escalated claim above the deductible | Urgency alert: insurer 30-day notice clock; consent before settlement | T2:L16, T2:L48 | C5c |
| Approval above $10k after sign-off | Finance pre-approval | T2:L56; Q5 | C2, E1 |
| Denial after sign-off | No finance pre-approval | T2:L56, T2:L60; Q5 | E2 |
