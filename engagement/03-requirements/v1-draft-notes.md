# Requirements v1: Draft Notes (for consultant review, not part of v1)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Claude drafted `v1/` and `spike/expected-outcomes-v1.md` for the
consultant's review. Every value below was **proposed by Claude**. The consultant approved all of
them (V1–V24, E-a to E-d) on 2026-10-27, with corrections to V2 and V22; see
"v1 values" in `docs/consultant-decisions.md`.

## Values the consultant asked to set

| # | Item | Proposed | Where | Basis |
|---|---|---|---|---|
| V1 | G18 hold status field | `hold_reason`, `missing_items`, `reminders_sent`, `fallback_date`, `duplicate_flag` | rules.md, Agent output | G18 named three fields; `missing_items` and `duplicate_flag` added so reminders and G13 have somewhere to live |
| V2 | `FILING_WINDOW_DAYS` | 270 calendar days, delivery to receipt, all customers (A5) | rules.md | No source. **Finding:** no single window reproduces the 12 historical filing-window denials. They have delivery-to-receipt gaps of 0–14 days, while approved or partial claims for the same customers run up to 16–19 days (20 across all other claims; Q21). The window is either measured from another date, varies by contract, or was applied inconsistently (H3). Raised as D13 |
| V3 | K02 request time | 2026-03-11 15:30 ET, while held | expected outcomes | Tests G10a and the after-14:00 path |
| V4 | K04 invoice amount | 3,406.70 | expected outcomes | 80% of claimed; unambiguous mismatch |
| V5 | K05 inputs | `delivered_at` = 2025-05-31 (276 days) | expected outcomes | Moves delivery, not receipt, so document dates stay as released |
| V6 | K09 wording | See expected outcomes | expected outcomes | States a temperature excursion without the word "reefer" |

## Other values v1 needed (the cold FDE would ask)

| # | Item | Proposed | Why it was needed |
|---|---|---|---|
| V7 | G11 rubric checklist | RB1–RB6 | G11 left the checklist to v1 |
| V8 | `RUBRIC_SCORE_THRESHOLD` | 1.00 (all items pass) | P1 unset; a checklist gate is clearest as all-pass |
| V9 | `SELF_REPORTED_CONFIDENCE_THRESHOLD` | 0.80, provisional | P1 unset; recalibrated from the eval |
| V10 | Reminder schedule | Days 3, 7, 11; day-11 states the fallback date | E5 automates reminders but set no cadence |
| V11 | "End of business day" | 17:00 ET | P3 says "end of that business day" with no time |
| V12 | Expedite request on a non-business day | Due 12:00 the next business day | P3 covers business days only |
| V13 | Fallback check time | 23:59 ET on the fallback date | P2 says "day 14" without a time |
| V14 | Invoice mismatch definition | Claimed > invoice value, to the cent, or unreadable invoice | C5c named the flag only |
| V15 | Duplicate definition | Same `shipment_ref`, other claim paid or open | C5c/G13 named the flag only |
| V16 | Temperature allegation definition | Any temperature-excursion statement; unsure → treat as allegation | G5 named the signal only |
| V17 | Cold-chain identification | Claims-lead-maintained list of customer IDs; no go-live with an empty list (D12) | Index asked how the agent identifies them |
| V18 | Missing delivery date | Treat as outside the window (R9) | Needed for R9 |
| V19 | Carrier filing on incomplete documents | No package; the person may file manually | "Every paid claim with evidence" needed a definition |
| V20 | Autonomous reviewer (G8b) | A specialist designated by the claims lead | G8b left the reviewer open |
| V21 | Who records insurer consent (G9b) | Claims lead | G9b left it open |
| V22 | Senior specialist (G7c) | Designation within the specialist team, named by the claims lead | G7c names the role without defining it; the claims lead calls one specialist "the senior one" (W2:L2) |
| V23 | Output fields beyond G17 | `claim_id`, `status`, `amount`, `triggers`, `rubric_items`, `hold`, `fact_pack` | G17's six fields can't carry the hold, the fact pack or which rubric item failed |
| V24 | New dependency IDs | D12 (cold-chain list), D13 (filing-window rule) | Not in the index |

## Eval design choices (spike/expected-outcomes-v1.md)

| # | Choice | Why |
|---|---|---|
| E-a | `autonomous*` scoring: autonomous, or sign-off via R14, both count; R14 reported as "gate-held" | Thresholds are uncalibrated |
| E-b | Decision not scored on sign-off | The draft decision isn't a routing outcome |
| E-c | 8 "info gap" sample cases reported separately | Their snapshots lack the evidence behind the historical partial or denial; an `approve` here would overpay |
| E-d | `invoice_amount` = `amount_claimed` for sample snapshots, labelled an assumption | IT doesn't hold invoice values; otherwise R8 fires on every sample case |
