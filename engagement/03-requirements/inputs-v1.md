# Requirements v1: Traceability Index

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

A working aid, kept outside `v1/`. It lists every ruling, parameter and open
dependency that requirements v1 has to cover, grouped by requirement area.
Rulings are in `docs/consultant-decisions.md`, and the design is in
`engagement/02-redesign/`.

**Self-containment.** The cold-FDE reads only `v1/`. Each item has to be
stated in v1 in full. Ruling IDs can be kept for traceability, but they are
not enough on their own.

**Status key:** **Live** = in force · **Superseded** = replaced, shown so
that v1 does not reintroduce it · **Open** = a dependency v1 must flag ·
**Out of v1** = governance or business case, not a requirement.

## 1. Scope and claim types

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| S1 | Pilot covers damage and shortage claims; loss claims are out of the agent pilot (phase-2 candidate). Redesigned process steps still apply to loss | Live | T2:L50 |
| G1 | Loss claim is always escalated at step 0; the agent forms no decision | Live | T2:L50; S1 |
| C5 | Three tiers: autonomous, human sign-off, always escalate | Live | T1:L36, T2:L16, T2:L58 |
| G2 | Precedence: escalate > hold > sign-off > autonomous; decision-tree order governs | Live | C5, G3a |
| C4 | Claims team owns all payouts; account managers cannot approve or pay | Live (ratified, D5 closed) | T1:L10, T2:L14; Q11, Q12; T3:L30, W1:L2 |

## 2. Intake

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| E5 | Structured document checklist requested up front with a deadline; automated reminders replace email chasing | Live | T2:L28, T2:L30, T2:L34 |
| G5 | Temperature/reefer escalation fires on either `reefer_flag` = Y or a customer temperature allegation, at intake | Live | T2:L44, T2:L58; Q16 |
| C5c | Cold-chain contract customer always escalates. Customers named at T2:L44; v1 must say how the agent identifies them | Live | T2:L44 |
| G13 | Duplicate check runs at intake and raises a flag visible on the "awaiting documents" list; routing on it stays at step 3 | Live | T2:L68 |
| E4 | Account-manager early-payment path eliminated; replaced by expedite request routed to a person, never the agent | Live (ratified) | T1:L10, T2:L14, T2:L54 |

## 3. Routing: decision tree and scope table

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| Steps 0–7 | The decision tree in full: rule table, escalation triggers T1–T5, sign-off triggers H1–H9 | Live | `decision-tree.md` |
| R1–R16 | Scope table rows in full, with R12 shown as removed | Live | `scope-table.md` |
| G4 | $10k line and deductible are measured on the claimed amount | Live | Q15 |
| C5a | Partial at or below $10k → sign-off (partials above $10k reach sign-off through R13) | Live | T1:L36; Q14 |
| C5b | Agent never decides on incomplete documents; "documents complete" is a precondition for autonomous | Live | T2:L34 |
| G3a | Hold is a state, not a route. Route stays `autonomous` / `sign_off` / `escalate`; **the hold is carried in a separate status field, to be specified in v1** | Live — v1 must define the field | T2:L30 |
| G3b | Hold applies at every amount, to any non-escalated claim (replaces C5b's "≤$10k" wording for routing) | Live | C5b |
| C5c | Sign-off flags: possible duplicate, invoice mismatch, outside filing window, low confidence | Live | T2:L42, T2:L68; Q14 |
| G11 | Two confidence gates (rubric score from a fixed checklist; self-reported confidence), each with its own threshold; both must pass for autonomous | Live — v1 must define the rubric | P1 |
| G10a | New information re-runs the tree; claims move up only; a claim with a person stays with that person; after an autonomous decision → sign-off | Live | — |
| G10b | No handback from escalation | Live | — |
| G12 | Withdrawal: status `withdrawn` with date and reason, no route; if a payment was made → sign-off | Live | — |
| G6 | Key-account flag is not a routing input (R12/H8 removed) | Live | T1:L10, T1:L36 |

## 4. Operations by tier

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| G8a | Autonomous approval: agent sends customer letter and issues payment instruction (no pre-approval); prepares carrier filing package; specialist submits | Live, **except** its clean-POD "do not file" clause | E1 |
| E6a | Clean-POD shortages are filed like any other paid claim with evidence | Live; reverses E6 and the G8a clause | T2:L20, T2:L64; Q10, Q18 |
| E6 | "Do not file clean-POD shortages" | **Superseded** by E6a | Q18 |
| G8b | Pilot: a person reviews every autonomous decision after it is made; moves to a sample later | Live | — |
| G7a | Sign-off: agent drafts decision, amount, rule applied, rationale, letter; person approves/edits/overrides; every edit or override logged with reason | Live | — |
| G7b | Escalate: fact pack (triggers, document checklist status, running clocks); no decision, no amount | Live | T2:L16, T2:L44, T2:L58 |
| G7c | Queues: specialists sign-off ≤$10k; lead sign-off >$10k and all escalations; senior specialist backs up escalations | Live, refined by G7f for expedite requests | T2:L14, T2:L24, T2:L44 |
| G7d | Reefer/temperature escalations picked up the day received; no other response-time target in v1 | Live; expedite answers now have P3 (see §5) | T2:L44 |
| G7e | Specialists own the "awaiting documents" list; agent sends reminders; at fallback → sign-off under the G7c split | Live | — |
| G6 | Key-account claims worked first in sign-off and escalation queues; AM notified of outcome when decided, no rights | Live | T1:L10 |

## 5. Expedite requests

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| R3 / T3 | Expedite request always escalates to a person; never the agent | Live | T1:L10, T2:L14, T2:L54 |
| G7f | Lead owns every expedite escalation and the on-time answer. Specialist working the claim answers; else lead assigns or answers. Expedite-only trigger: specialists decide ≤$10k, lead >$10k (exception to G7c). Any other trigger → lead. No named backup for expedite answers | Live | W2:L2–L4; T2:L14 |
| D5e | Answer limited to status, next step, expected date; payment commitment only on a claim already approved; none before decision, complete documents, or insurer consent | Live | T3:L22; T2:L16; G9b |
| P3 / P3a | `EXPEDITE_RESPONSE_SLA` (see §8) | Live (provisional) | T3:L30; W1:L3, W2:L4 |
| D5f | Record request time, answer time, answer content, outcome for every expedite request | Live (v1 requirement) | T3:L30 |
| D5g | SLA miss → automatic notice to the claims lead and the requesting AM. No route to the COO | Live (v1 requirement) | T3:L28 |
| D5f / D5i | Miss report, cadence, COO review, after-14:00 share | **Out of v1** (governance) | W1:L3 |

## 6. After the decision: finance, payment, insurer, carrier

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| C2 / E1 | Finance pre-approval only above $10k; removed at or below | Live; CFO to agree (D2, D3) | T2:L56; Q5 |
| E2 | No finance pre-approval for denials | Live; CFO to agree (D2) | T2:L56, T2:L60; Q5 |
| E3 | Thursday batch removed; pay on approval or a more frequent run — a finance recommendation, not an agent step | Live; CFO to agree (D2) | T2:L18; Q6 |
| C5 | Claims above the deductible: insurer notified within 30 days, consent before settlement | Live | T2:L16 |
| G9a | Insurer alert on escalated claims above the deductible shows delivery and receipt dates, no countdown | Live; start date open (D9) | Q17 |
| G9b | No payment instruction above the deductible until insurer consent is recorded | Live | T2:L16; Q12 |
| Step 7 | Carrier filing for every paid claim with evidence | Live | E5, E6a |

## 7. Agent output and records

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| CLAUDE.md | Structured output per claim: `decision`, `rule_applied`, `confidence`, `route`, `rationale`; out-of-scope → `escalate` | Live | Project spec |
| G3a | Separate status field for the hold (values to be specified) | Live — to define | — |
| G11 | Confidence carries two values (rubric, self-report), not one | Live — reconcile with the single `confidence` field | P1 |
| G12 | `withdrawn` status, date, reason | Live | — |
| G7a | Edit/override log with reason | Live | — |
| D5f | Expedite request record | Live | — |

## 8. Parameters and assumptions

| ID | Value | Status | Sources |
|---|---|---|---|
| $10k line | $10,000 on claimed amount | Provisional (D3) | T2:L14, T2:L62; Q8 |
| Deductible | Assumed $25,000 on claimed amount | Assumption (D1) | T2:L16 |
| P1 `CONFIDENCE_THRESHOLD` | Two thresholds (rubric, self-report) | **Unset**; calibrated in the Day 2 eval | G11 |
| P2 `FALLBACK_DEADLINE_DAYS` | 14 calendar days from receipt | Set | Q19 |
| P3 `EXPEDITE_RESPONSE_SLA` | Business days, Eastern Time; before 14:00 → end of that business day; at or after 14:00 → 12:00 next business day | Provisional assumption | T3:L30; W1:L3 |
| P3a holidays | Client's company holidays; US federal holidays as provisional default | Assumption (D11) | W1:L3, W2:L4 |
| HQ time zone | Eastern Time | Assumption (location never stated in discovery) | P3 |

## 9. Open dependencies v1 must flag

| # | Dependency | Owner | Affects |
|---|---|---|---|
| D1 | Deductible amount | CFO, Day 3 | R4, G9a–b |
| D2 | Removal of pre-approval ≤$10k and for denials; payment-run change | CFO, Day 3 | C2, E1–E3 |
| D3 | $10k thresholds | CFO, Day 3 | C2, C5, E1 |
| D4 | Recovery definition; source of the COO's ~70% | CFO, Day 3 | Business case (out of v1) |
| D8 | Late-notice count discrepancy | CFO, Day 3 | Out of v1 |
| D9 | Insurer 30-day start | CFO, Day 3 | G9a |
| D11 | Company holiday list | COO, before go-live | P3a |
| Risk | Dispatch-day expedite coverage (W2:L2), monitored via miss report | Claims lead | G7f |

## 10. Out of v1 (do not write as requirements)

C1 (time split, business case), C3 (recovery baseline, business case), C6
(visibility of conflict), D5 handling and D5a–D5d (session terms), D5 outcome
and D5 closed (governance record), D5h (settled by W1:L2), D5i (governance
metric), D5g's COO arbitration (sponsor commitment).

## Inconsistencies in the design docs (resolved 2026-10-27)

Ruled on before v1 (G14–G18), and the design docs updated to match:

1. Always-escalate operations row: split by trigger (G14).
2. G7f, D5e, D5f, D5g and P3 carried into `decision-tree.md` and `scope-table.md` (G15).
3. G8a clean-POD clause marked superseded by E6a (G16).
4. Output schema: one field per G11 gate (G17); approved and applied to `CLAUDE.md`.
5. Hold status field: v1 defines it as hold reason, reminders sent and fallback date (G18).

## Added 2026-10-27

| ID | What v1 must state | Status | Sources |
|---|---|---|---|
| E5a | Documents-complete checklist by claim type: damage (photos, invoice, BOL, delivery receipt/POD); shortage (invoice, BOL, delivery receipt/POD; photos optional); reefer/temperature (that list plus the temperature download); loss out of pilot. The agent applies the checklist, not a historical date | Live; "photos optional" carries the Q20 data-quality caveat | T2:L18, T2:L44; Q20 |
| G18 | Hold status field: hold reason, reminders sent, fallback date | Live — v1 defines | G3a |
| G17 | Output fields: `decision`, `rule_applied`, `rubric_score`, `self_reported_confidence`, `route`, `rationale`; null conventions for hold and escalate; P1 → `RUBRIC_SCORE_THRESHOLD`, `SELF_REPORTED_CONFIDENCE_THRESHOLD` | Live (approved) | G11 |
| EV1–EV3 | Eval design (two snapshots, hindsight rule, constructed cases) | Live — eval, not v1 requirements | `spike/README.md` |
