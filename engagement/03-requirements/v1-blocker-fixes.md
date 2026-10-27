# Requirements v1: Blocker Fixes (proposed, for consultant approval)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Claude's recommended rulings on the six findings that block the v1 freeze. Nothing
here is applied. On approval: each ruling goes into `docs/consultant-decisions.md`,
and the edits below are applied exactly as written. Line numbers refer to the files
as they were drafted.

## Proposed rulings

| ID | Finding | Recommended ruling | Rejected option |
|---|---|---|---|
| **G19** | 5. Where the tree re-runs from | Every re-evaluation (documents arrive, new information) re-runs the tree **from step 0**. A step-1 trigger found in late documents (a temperature allegation, an amount above the deductible) must be caught. | Re-run from step 3. That misses step-1 triggers that appear in later documents |
| **G20** | 3. Does an answered expedite request still count? | An expedite request is a **persistent** step-1 trigger. Once made, R3 fires on every later evaluation, whether or not the request has been answered. Answering it closes the SLA clock only. | R3 fires only while the request is open. Then `rule_applied` and `triggers` change when someone answers, although the claim stays escalated (G10b) |
| **G21** | 4. Expedite request after an autonomous decision | Refines G10a: new information after an autonomous decision sends the claim to sign-off, **unless the re-run fires a step-1 trigger, which escalates it**. The higher tier wins, consistent with G2 and up-only re-routing. EC25 → escalate (R3). | Sign-off. That puts the expedite request below its own always-escalate rule (R3, E4) |
| **G22** | 6. Loss claim with a temperature allegation | A loss claim still escalates at step 0 (`rule_applied` = R16) with no decision. The **step-1 triggers are still evaluated** and listed in `triggers` and the fact pack, for clocks and queue only, with no change to the route. If R1 is among them, the claim is handled as a reefer/temperature escalation: picked up on the day of receipt, with the 72-hour download clock. | Skip step 1 for loss claims. That loses the 72-hour window on a reefer loss (T2:L44; G7d) |
| **EV4** | 1. K01 changes a sample case | K01 uses a constructed customer ID, `C-K01`, which no released claim uses. The eval cold-chain list is `["C-K01"]` and nothing else. No sample customer is on the eval list, so no sample expectation changes. | Keep C010. NLC-26-0016 (customer C010) would then have to escalate under R2, which changes a sample expectation |
| **EV5** | 2. K06's input breaks the hindsight rule | K06 shares `shipment_ref` SHP-0001 with NLC-26-0001, which is **open, not paid**, at both K06 snapshots (it was received 2026-03-01 and paid 2026-04-09). No prior-payment input. R7 still fires under the "paid or open" definition. | Keep `prior_payment_same_shipment` = Y. That shows a payment made after the snapshot |

**Rationale (common):** each fix applies an existing ruling consistently (G2 precedence,
G10a/G10b up-only, G7d reefer timing, the hindsight rule in EV1). None adds a new
number. All six are needed before the freeze because each one changes an expected outcome or makes
a rule read two ways.

**Citations:** T2:L44; G2, G7d, G10a, G10b, G1, R3, E4, EV1, EV3; Q21 not needed.

## Edits on approval

### G19: re-run from step 0

| File:line | Old | New |
|---|---|---|
| `v1/stories.md:49` | When the last required document arrives, the agent re-runs the tree from step 3. | When the last required document arrives, the agent re-runs the tree from step 0. |
| `v1/edge-cases.md:21` | Documents complete. Re-run from step 3 | Documents complete. Re-run the tree from step 0 |
| `v1/rules.md:175` | Re-run the tree. The claim may move up a tier, never down | Re-run the tree from step 0. The claim may move up a tier, never down |

### G20: expedite request persists

| File:line | Old | New |
|---|---|---|
| `v1/rules.md:50` | An expedite request is open on the claim | An expedite request has been made on the claim |
| `v1/rules.md:78–80` | …recorded on the claim with the requester and the request time. It stays open until it is answered. | …recorded on the claim with the requester and the request time. Once made, it is a step-1 trigger on every later evaluation, whether or not it has been answered. Answering it closes the SLA clock only. |
| `v1/stories.md:16` | an open expedite request | an expedite request |

### G21: expedite after an autonomous decision

| File:line | Old | New |
|---|---|---|
| `v1/rules.md:177` | New information after an autonomous decision \| Human sign-off | New information after an autonomous decision \| Human sign-off, or escalate if the re-run fires a step-1 trigger |
| `v1/stories.md:143` | New information after an autonomous decision sends the claim to sign-off. | New information after an autonomous decision sends the claim to sign-off, or to escalate if the re-run fires a step-1 trigger. |
| `v1/edge-cases.md:50` | Sign-off (G10a), and the request is answered under the SLA | Escalate (R3): the re-run fires a step-1 trigger, which outranks sign-off. Answered under the SLA |

### G22: step-1 triggers on loss claims

| File:line | Old | New |
|---|---|---|
| `v1/rules.md:47` | Escalate (R16). No decision | Escalate (R16). No decision. Step-1 triggers are still evaluated and listed in `triggers` and the fact pack; they do not change the route |
| `v1/rules.md:138` | Escalate: reefer/temperature | Escalate: reefer/temperature (R1 among the triggers, loss claims included) |
| `v1/stories.md:14` | It does not run steps 1–6. | It runs no step after step 1. Step-1 triggers are still evaluated for `triggers` and the fact pack; `rule_applied` stays `R16`. |
| `v1/edge-cases.md:15` | Escalate at step 0 (R16). Step 1 is not run, but the fact pack notes the allegation | Escalate at step 0 (R16). `triggers` = R16, R1. Handled as a reefer/temperature escalation: picked up on the day of receipt, fact pack shows the 72-hour download clock |
| `spike/expected-outcomes-v1.md:112` | Steps 1–6 not run | Step-1 triggers evaluated; none fire. Steps 2–6 not run |

### EV4: K01 customer

| File | Old | New |
|---|---|---|
| `spike/constructed_cases.py` (K01 row) | `cold_chain_customer` = Y | `customer_id` = C-K01 (constructed; the only ID on the eval cold-chain list) |
| `spike/expected-outcomes-v1.md:98` | Fact pack; claims lead queue | Fact pack; claims lead queue. Customer `C-K01`; eval cold-chain list = `["C-K01"]` (EV4) |

The script is regenerated afterwards, so `constructed-cases.md` matches.

### EV5: K06 input

| File | Old | New |
|---|---|---|
| `spike/constructed_cases.py` (K06 row) | `prior_payment_same_shipment` = Y; `shipment_ref` and `prior_payment_claim_id` from NLC-26-0001 | `shipment_ref` = SHP-0001, shared with NLC-26-0001, open (not paid) at both snapshots; no prior payment (EV5) |
| `spike/constructed_cases.py` (footer) | K06 shares `shipment_ref` … (paid …) | K06 shares `shipment_ref` SHP-0001 with NLC-26-0001 (received 2026-03-01; paid 2026-04-09, after both K06 snapshots) |
| `spike/expected-outcomes-v1.md:108` | `hold.duplicate_flag` = true | `hold.duplicate_flag` = true. NLC-26-0001 is open, not paid, at this snapshot (EV5) |

## Not blocking, but quick to fold in (optional)

- **E-e** (finding 9): label the sample eval assumptions. No sample case has a cold-chain customer, a temperature allegation or an expedite request (none is held, release 2 §2). One line in `expected-outcomes-v1.md` conventions.
- **Finding 20:** NLC-26-0231 and K07 should accept `rule_applied` R10 *or* R13, because a drafted deny gives R10.
- **Finding 7:** an input schema table in `rules.md`. The cold FDE will ask for it.
