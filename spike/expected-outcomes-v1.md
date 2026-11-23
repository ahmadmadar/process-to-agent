# Expected Outcomes for Requirements v1 (approved 2026-10-27)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Written from `engagement/03-requirements/v1/` before any run (EV1–EV3). Kept
outside `v1/`, so the cold-FDE never sees it. Sample and constructed cases are
reported separately and never combined into one headline (EV3).

## Scoring conventions

- **Route** is scored on every snapshot. **Status** is scored on every snapshot (`held` / `routed`).
- **Decision** is scored only where the rules determine it: `null` on hold and escalate, and `approve` on autonomous-eligible cases. On `sign_off` the decision is the agent's draft and is **not scored**; route and `rule_applied` are.
- **`autonomous*`**: the rules allow the autonomous tier, but the confidence gates are not yet calibrated. Scored as correct if `route` = `autonomous`, or if `route` = `sign_off` with `rule_applied` = `R14` (a gate failed). R14 cases are counted and reported separately as "gate-held".
- **Info gap**: the snapshot lacks the evidence that drove the historical outcome (salvage, shipment record, filing-window rule). These cases are scored on the rules, and also reported as a separate group, because an `approve` here would pay what the historical team reduced or denied.
- **Sample assumptions (EV6):** no sample case has a cold-chain customer, a temperature allegation in its claim text, or an expedite request. None of these is held in the released data (release 2 §2). The eval cold-chain list is `["C-K01"]` only (EV4).
- **Invoice amount** is not held by IT. For sample cases, each snapshot sets `invoice_amount` = `amount_claimed`, labelled an assumption in the case file.
- **Decision-point moment** (EV2): the historical completion date if every checklist flag for the claim type is received and completion is on or before day 14; otherwise the day-14 fallback.

## Sample cases (30 claims, 60 snapshots)

| Case | Type | Claimed | Snapshot | Status | Route | Decision | Rule applied | Triggers | Notes |
|---|---|---|---|---|---|---|---|---|---|
| NLC-26-0016 | damage | 1,613.68 | Intake | held | null | null | R5 | — |  |
| NLC-26-0016 | damage | 1,613.68 | Complete (2026-03-16, day 8) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0020 | damage | 481.00 | Intake | held | null | null | R5 | — |  |
| NLC-26-0020 | damage | 481.00 | Complete (2026-03-13, day 4) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0022 | damage | 1,552.83 | Intake | held | null | null | R5 | — |  |
| NLC-26-0022 | damage | 1,552.83 | Complete (2026-03-17, day 7) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0028 | damage | 1,562.18 | Intake | held | null | null | R5 | — |  |
| NLC-26-0028 | damage | 1,562.18 | Day 14 fallback (2026-03-25; never completed) | routed | sign_off | not scored | R6 | — |  |
| NLC-26-0052 | shortage | 6,565.08 | Intake | held | null | null | R5 | — |  |
| NLC-26-0052 | shortage | 6,565.08 | Complete (2026-03-25, day 3) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0053 | shortage | 4,404.26 | Intake | held | null | null | R5 | — |  |
| NLC-26-0053 | shortage | 4,404.26 | Complete (2026-03-30, day 8) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0125 | damage | 1,144.49 | Intake | routed | escalate | null | R1 | R1 |  |
| NLC-26-0125 | damage | 1,144.49 | Decision point (= intake; G10b) | routed | escalate | null | R1 | R1 | No handback |
| NLC-26-0139 | damage | 7,992.60 | Intake | held | null | null | R5 | — |  |
| NLC-26-0139 | damage | 7,992.60 | Complete (2026-05-07, day 10) | routed | autonomous* | approve | R15* | — | info gap: Historically denied: outside filing window. Not outside under A5 (13 days) |
| NLC-26-0141 | damage | 1,173.42 | Intake | held | null | null | R5 | — |  |
| NLC-26-0141 | damage | 1,173.42 | Complete (2026-04-29, day 2) | routed | autonomous* | approve | R15* | — | info gap: Historically partial (salvage/depreciation). No salvage input in the snapshot; RB4 should fail if the documents show it |
| NLC-26-0163 | shortage | 1,955.89 | Intake | routed | escalate | null | R1 | R1 |  |
| NLC-26-0163 | shortage | 1,955.89 | Decision point (= intake; G10b) | routed | escalate | null | R1 | R1 | No handback |
| NLC-26-0164 | shortage | 1,500.81 | Intake | held | null | null | R5 | — |  |
| NLC-26-0164 | shortage | 1,500.81 | Complete (2026-05-16, day 10) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0170 | shortage | 1,947.06 | Intake | held | null | null | R5 | — |  |
| NLC-26-0170 | shortage | 1,947.06 | Complete (2026-05-10, day 2) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0224 | damage | 450.00 | Intake | routed | escalate | null | R1 | R1 |  |
| NLC-26-0224 | damage | 450.00 | Decision point (= intake; G10b) | routed | escalate | null | R1 | R1 | No handback |
| NLC-26-0226 | shortage | 4,688.72 | Intake | held | null | null | R5 | — |  |
| NLC-26-0226 | shortage | 4,688.72 | Complete (2026-06-14, day 6) | routed | autonomous* | approve | R15* | — | info gap: Historically partial (salvage/depreciation). No salvage input; see RB4 |
| NLC-26-0231 | shortage | 10,339.85 | Intake | held | null | null | R5 | — |  |
| NLC-26-0231 | shortage | 10,339.85 | Complete (2026-06-19, day 10) | routed | sign_off | not scored | R13 or R10 | — | Historically partial. Route is sign-off whatever the decision: R10 if the draft is a denial (step 5), R13 otherwise (EV7) |
| NLC-26-0245 | damage | 1,392.41 | Intake | held | null | null | R5 | — |  |
| NLC-26-0245 | damage | 1,392.41 | Complete (2026-06-27, day 8) | routed | autonomous* | approve | R15* | — | info gap: Historically partial (salvage/depreciation). No salvage input; see RB4 |
| NLC-26-0246 | shortage | 3,463.74 | Intake | held | null | null | R5 | — |  |
| NLC-26-0246 | shortage | 3,463.74 | Complete (2026-07-03, day 14) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0275 | damage | 2,294.96 | Intake | held | null | null | R5 | — |  |
| NLC-26-0275 | damage | 2,294.96 | Complete (2026-07-06, day 1) | routed | autonomous* | approve | R15* | — | info gap: Historically denied: outside filing window. Not outside under A5 (13 days) |
| NLC-26-0305 | damage | 2,716.90 | Intake | held | null | null | R5 | — |  |
| NLC-26-0305 | damage | 2,716.90 | Complete (2026-07-19, day 2) | routed | autonomous* | approve | R15* | — | info gap: Historically partial (salvage/depreciation). No salvage input; see RB4 |
| NLC-26-0310 | damage | 2,360.07 | Intake | held | null | null | R5 | — |  |
| NLC-26-0310 | damage | 2,360.07 | Day 14 fallback (2026-08-02; completed day 16) | routed | sign_off | not scored | R6 | — |  |
| NLC-26-0313 | shortage | 4,484.84 | Intake | held | null | null | R5 | — |  |
| NLC-26-0313 | shortage | 4,484.84 | Complete (2026-07-30, day 11) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0335 | damage | 1,566.36 | Intake | held | null | null | R5 | — |  |
| NLC-26-0335 | damage | 1,566.36 | Complete (2026-08-06, day 11) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0357 | shortage | 1,762.66 | Intake | held | null | null | R5 | — |  |
| NLC-26-0357 | shortage | 1,762.66 | Day 14 fallback (2026-08-21; never completed) | routed | sign_off | not scored | R6 | — |  |
| NLC-26-0359 | damage | 316.10 | Intake | held | null | null | R5 | — |  |
| NLC-26-0359 | damage | 316.10 | Complete (2026-08-12, day 5) | routed | autonomous* | approve | R15* | — | info gap: Historically partial (salvage/depreciation). No salvage input; see RB4 |
| NLC-26-0374 | damage | 752.03 | Intake | held | null | null | R5 | — |  |
| NLC-26-0374 | damage | 752.03 | Day 14 fallback (2026-08-26; never completed) | routed | sign_off | not scored | R6 | — |  |
| NLC-26-0380 | damage | 1,650.00 | Intake | held | null | null | R5 | — |  |
| NLC-26-0380 | damage | 1,650.00 | Complete (2026-08-19, day 3) | routed | autonomous* | approve | R15* | — |  |
| NLC-26-0382 | damage | 1,486.74 | Intake | routed | escalate | null | R1 | R1 |  |
| NLC-26-0382 | damage | 1,486.74 | Decision point (= intake; G10b) | routed | escalate | null | R1 | R1 | No handback |
| NLC-26-0392 | shortage | 819.92 | Intake | held | null | null | R5 | — |  |
| NLC-26-0392 | shortage | 819.92 | Complete (2026-08-29, day 6) | routed | autonomous* | approve | R15* | — | info gap: Historically denied: not on shipment record. Snapshot has no shipment-record contents; RB1 should catch it if the documents show it |
| NLC-26-0407 | damage | 1,813.89 | Intake | routed | escalate | null | R1 | R1 |  |
| NLC-26-0407 | damage | 1,813.89 | Decision point (= intake; G10b) | routed | escalate | null | R1 | R1 | No handback |
| NLC-26-0412 | damage | 666.61 | Intake | held | null | null | R5 | — |  |
| NLC-26-0412 | damage | 666.61 | Day 14 fallback (2026-09-14; never completed) | routed | sign_off | not scored | R6 | — |  |

**Sample summary:** 5 reefer (escalate at both snapshots); 5 day-14 fallbacks
(sign-off, R6); 1 above $10,000 (sign-off, R13); 19 autonomous-eligible, of
which 8 are info-gap cases.

## Constructed cases (K01–K09)

Consultant-set inputs:

- **K02 request time:** 2026-03-11 (Wednesday) 15:30 ET, while the claim is held. Tests an upward re-route (G10a) and the after-14:00 SLA path.
- **K04 invoice amount:** 3,406.70 (80% of the claimed 4,258.38, rounded to the cent).
- **K05:** `FILING_WINDOW_DAYS` = 270 (A5). `delivered_at` set to 2025-05-31; receipt date unchanged at 2026-03-03 (276 days). The delivery date is moved instead of the receipt date, so the document dates stay as released.
- **K09 allegation wording:** "The pallets arrived warm. Our receiving team measured the product at 14°C against the required 2–8°C, and we believe it went out of range in transit." (`reefer_flag` stays N.)

| Case | Tests | Snapshot | Status | Route | Decision | Rule applied | Triggers | Also check |
|---|---|---|---|---|---|---|---|---|
| K01 | Cold-chain customer | Intake | routed | escalate | null | R2 | R2 | Fact pack; claims lead queue. Customer `C-K01`; eval cold-chain list = `["C-K01"]` (EV4) |
| K01 | | Decision point (2026-03-05) | routed | escalate | null | R2 | R2 | No handback |
| K02 | Expedite, only trigger | Intake (2026-03-09) | held | null | null | R5 | — | Request not yet made |
| K02 | | Decision point (2026-03-13) | routed | escalate | null | R3 | R3 | Answer due 12:00 Thu 2026-03-12; queue `specialist` (≤ $10,000, only trigger) |
| K03 | Above the deductible | Intake | routed | escalate | null | R4 | R4 | Insurer alert with delivery and receipt dates, no countdown; payment gated on consent |
| K03 | | Decision point (2026-04-25) | routed | escalate | null | R4 | R4 | No handback |
| K04 | Invoice mismatch | Intake | held | null | null | R5 | — | |
| K04 | | Decision point (2026-03-04) | routed | sign_off | not scored | R8 | R8 | Specialists' queue |
| K05 | Outside filing window | Intake | held | null | null | R5 | — | |
| K05 | | Decision point (2026-03-07) | routed | sign_off | not scored | R9 | R9 | |
| K06 | Possible duplicate | Intake | held | null | null | R5 | — | `hold.duplicate_flag` = true. NLC-26-0001 is open, not paid, at this snapshot (EV5) |
| K06 | | Decision point (2026-03-17) | routed | sign_off | not scored | R7 | R7 | |
| K07 | Between $10,000 and the deductible | Intake | held | null | null | R5 | — | |
| K07 | | Decision point (2026-03-11) | routed | sign_off | not scored | R13 or R10 | — | Claims lead queue; finance pre-approval if approved. R10 if the draft is a denial (EV7) |
| K08 | Loss claim | Intake | routed | escalate | null | R16 | R16 | Step-1 triggers evaluated; none fire. Steps 2–6 not run |
| K08 | | Decision point (2026-03-23) | routed | escalate | null | R16 | R16 | |
| K09 | Temperature allegation, no reefer flag | Intake | routed | escalate | null | R1 | R1 | Fact pack clock: download must be requested today |
| K09 | | Decision point (2026-03-09) | routed | escalate | null | R1 | R1 | |
