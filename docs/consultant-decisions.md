# Consultant decisions log

> Northline Freight is a fictional client. All people and data are synthetic.

Where the consultant overruled, corrected, or chose against Claude, and why.
Claude drafts entries; the consultant confirms the wording.

| Date | Day / step | Claude proposed | Consultant decided | Why |
|---|---|---|---|---|
| 2026-10-16 | Day 1 / workflow | Claude makes the commits; one branch per session with a PR at the end | One branch per session. The consultant does all git work in GitHub Desktop. Claude only drafts commit and PR text. Claude's commit on `main` was reversed and the changes moved to `day1/discovery`. | I prefer to own the version control. Keeps me honest and accountable about reviewing all the changes made by Claude throughout the session. |
| 2026-10-17 | Day 1 / SOW | Turn governance meetings that have no session in the plan into written steps, or reframe them as the consultant's rulings pending sponsor ratification | Kept the daily sponsor summary. Removed the Day 1 COO playback and the Day 3 COO/CFO readout. Accepted all other SOW fixes. | A short engagement benefits from daily visibility and clarity for the client; a longer one would use weekly summaries. The Day 3 CFO defence already covers the readout. |
| 2026-10-17 | Day 1 / data request | Keep the event log optional, with fallback fields in the claims table for H2 | Event log made required; fallback fields removed | A required event log reduces guessing on our end. |
| 2026-10-18 | Day 1 / current-state swimlane | 25 corrections to the current-state draft, including #11 (dotted "sometimes filed" edge from the AM path to carrier filing, from Q11 data only) and #14 (annotate the three cold-chain contract customers as paid almost regardless, T2:L44) | Approved and applied 1–10, 12, 13 and 15–25. Rejected #11 and #14. | #11 has no transcript support and would draw a data pattern as a process step. #14 is not on the consultant's correction list; cold-chain terms are carried into the future state through C5c. |
| 2026-10-18 | Day 1 / documentation | README carried a "Suggestions" section of Claude's ideas; deliverables carried "Claude's draft" labels | Deleted the README suggestions. Accepted documents read as regular documents, with no draft labels. Claude's suggestions are raised with the consultant first, or worded from the consultant's point of view. The coverage probes and the options in `open-gaps.md` are kept. | The consultant owns every deliverable. Unrequested additions and draft labels blur who decided what. |

---

## Discovery rulings (Day 1)

Rulings on the six contradictions (synthesis §4) and the "eliminate, don't
automate" candidates. The decision in each entry is the consultant's, recorded
as given. Rejected options and rationale were drafted by Claude from the
synthesis evidence and confirmed by the consultant without edits on 2026-10-18.

Revisions are logged as new entries with a new ID that references the
original. Originals are not edited.

**Provisional thresholds:** the $10k pre-approval threshold (C2, E1) and the
$10k autonomy threshold (C5) are aligned with the existing specialist approval
line (T2:L14, T2:L62; Q8). They were chosen on discovery evidence and are open
to revision if the CFO challenges them on Day 3.

### C1. Where the time goes

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Evidence ruling
- **Decision:** Waiting dominates elapsed time. The work/wait split inside stages is unquantified. Hands-on effort (~3 hours per claim) is carried into the business case as a labelled assumption.
- **Rejected options:** (a) Accept the COO's view that most of the time is hands-on work. (b) Treat the ~3-hour estimate as a measured baseline.
- **Rationale:** The longest measured stage sits after the decision, and the elapsed time from complete documents to a decision is short (Q4). The COO's view rests on perception, not stage data (T1:L24). The claims lead places the delay in waiting on customers and finance (T2:L26). The ~3-hour figure is an untimed estimate ("nobody times it", T2:L66), so it can only be an assumption.
- **Citations:** T1:L24, T2:L12, T2:L26, T2:L66; Q3, Q4, Q6

### C2. Finance pre-approval

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** PROVISIONAL threshold; conditional on CFO agreement on Day 3 (control owner not yet interviewed)
- **Decision:** Keep finance pre-approval only for claims above $10k. Remove it at or below $10k, and for all denials.
- **Rejected options:** (a) Keep pre-approval for every claim, as today. (b) Remove pre-approval entirely. (c) Keep it for all claims but add a turnaround target.
- **Rationale:** Nearly every reviewed claim is approved as submitted, and the only outcome changes were on large claims (Q5), matching the claims lead's account (T2:L56). It is the longest elapsed stage (Q4), not "a day or two" (T1:L26). Keeping it above $10k preserves the fraud control where it has acted (T2:L56). Denials carry no payment, so the fraud rationale does not apply (see E2).
- **Citations:** T1:L26, T2:L18, T2:L56, T2:L60; Q4, Q5
- **Dependencies:** CFO agreement; CFO challenge on the $10k threshold

### C3. Recovery rate

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Evidence ruling
- **Decision:** Both stated figures are correct on different denominators. The business-case baseline is recovered ÷ paid across all paid claims. The accepted-claims rate is reported alongside it.
- **Rejected options:** (a) Use the COO's ~70% as the baseline. (b) Use the accepted-claims rate as the baseline. (c) Rule one stakeholder's figure wrong.
- **Rationale:** The all-paid-claims rate matches the claims lead's figure, and the accepted-claims rate matches the COO's (Q9). The all-paid-claims rate is the one that reflects money actually lost, including claims never filed. Reporting both avoids a definitional dispute with the COO. Pending carrier responses (Q9) mean the baseline will move as they resolve.
- **Citations:** T1:L18, T1:L20, T2:L12, T2:L64; Q9
- **Dependencies:** CFO to confirm the source of the COO's figure

### C4. Payout ownership

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** Requires sponsor (COO) ratification, per SOW §8
- **Decision:** The claims team owns all claim payouts. Account managers can request expedited handling but cannot approve or pay.
- **Rejected options:** (a) Keep account-manager authority for key accounts, as the COO prefers (T1:L10). (b) Allow account-manager payouts up to a limit. (c) Reclassify account-manager payments as goodwill outside the claims process.
- **Rationale:** Account managers decide claims on both sides of the $10k line (Q8). Their claims are paid before documents are complete far more often, filed with carriers less often, and recover far less (Q11). The one account-manager payment over the assumed deductible was paid before insurer notice, and cover was declined (Q12). The expedite request keeps the commercial need the COO describes (T1:L10) without the recovery and insurance cost.
- **Presentation to the sponsor:** This is the decision the COO needs to make. Evidence: Q8, Q11, Q12.
- **Citations:** T1:L10, T2:L14, T2:L54, T2:L78; Q8, Q11, Q12
- **Dependencies:** COO ratification

### C5. Agent autonomy

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** PROVISIONAL $10k threshold; deductible (~$25k) is an assumption until the CFO confirms it
- **Decision:** Tiered scope.
  - **Autonomous:** approvals at or below $10k with complete documents and no special flags.
  - **Human sign-off:** all denials; claims above $10k and at or below the deductible.
  - **Always escalate:** claims above the deductible (insurer notice and consent, T2:L16); temperature/reefer claims at intake (72-hour window, T2:L44); expedite requests from account managers.
- **Overrides:** the COO's proposal to auto-approve, pay and deny everything under $50k (T1:L12, T1:L34).
- **Rejected options:** (a) The COO's $50k autonomy line. (b) Autonomy up to the deductible. (c) No autonomy; the agent drafts only.
- **Rationale:** The $50k line includes claims above the assumed deductible (Q7), where the insurer must be notified and must consent before settlement (T2:L16). Paying first lost cover in the one case found (Q12; F5). Autonomous denials conflict with the COO's own red line, a wrongful denial to a key account (T1:L36), and the claims lead's view (T2:L16, T2:L58). Temperature claims cannot wait in a queue (T2:L44, T2:L58). $10k matches the line the claims team already works to (T2:L14; Q8).
- **Open points (not yet ruled; raised 2026-10-18):** (1) Tier for partial approvals at or below $10k. (2) Tier for approvals at or below $10k with incomplete documents. (3) Which "special flags" apply beyond temperature and expedite requests.
- **Citations:** T1:L12, T1:L34, T1:L36, T2:L16, T2:L44, T2:L58; Q7, Q8, Q12
- **Dependencies:** CFO confirmation of the deductible; CFO challenge on the $10k threshold

### C6. Disagreements

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Evidence ruling
- **Decision:** Conflict over claim decisions exists but is not visible to the sponsor.
- **Rejected options:** (a) Take the COO's account that there are no disagreements. (b) Frame the gap as the sponsor being misinformed.
- **Rationale:** The COO recalls no disagreements (T1:L32). The claims lead describes a declined insurer claim that is "still a sore point" (T2:L16), and the data shows that case (Q12). The difference reflects what reaches the sponsor, not a dispute over facts.
- **Open question for the CFO:** the claims lead describes "two other" late notices (T2:L16); Q12 shows one.
- **Citations:** T1:L32, T2:L16; Q12

### E1. Finance pre-approval at or below $10k

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** PROVISIONAL threshold; conditional on CFO agreement (see C2)
- **Decision:** ELIMINATE.
- **Rejected options:** (a) Automate the pre-approval check. (b) Keep it with a turnaround target.
- **Rationale:** No outcome change below $10k in the data (Q5). Automating a step that changes nothing would preserve the delay (Q4) at lower cost, not remove it.
- **Citations:** T2:L56; Q4, Q5
- **Dependencies:** CFO agreement; CFO challenge on the $10k threshold

### E2. Finance pre-approval of denial letters

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** Conditional on CFO agreement (see C2)
- **Decision:** ELIMINATE. No payment is made, so the fraud rationale does not apply.
- **Rejected options:** (a) Keep finance review of denials. (b) Move denial review to the claims lead.
- **Rationale:** Denials go through pre-approval today (T2:L60; Q5), but the step exists to stop fraudulent payment (T2:L56). Denials still go to human sign-off under C5.
- **Citations:** T2:L56, T2:L60; Q5
- **Dependencies:** CFO agreement

### E3. Weekly Thursday payment batch

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling — **RECOMMENDATION to finance, not an agent requirement**
- **Decision:** ELIMINATE. Move to pay-on-approval or a more frequent run.
- **Rejected options:** (a) Keep the weekly run. (b) Make payment timing an agent requirement.
- **Rationale:** Every payment falls on a Thursday (Q6), adding a wait after pre-approval (Q4). The payment run is owned by finance (T2:L18), so the change is finance's to make.
- **Citations:** T2:L18, T2:L26; Q4, Q6
- **Dependencies:** CFO / finance agreement

### E4. Account-manager early-payment path

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** Requires sponsor (COO) ratification (see C4)
- **Decision:** ELIMINATE. Replaced by an expedite request that account managers submit to the claims team. The claims team decides and pays. Expedite requests route to a person and are never auto-approved.
- **Rejected options:** (a) Keep the path with a spending limit. (b) Keep the path but require documents before payment.
- **Rationale:** See C4. Expedite requests go to a person so the commercial urgency is handled by someone accountable, without bypassing evidence collection (Q11) or insurer notice (Q12).
- **Citations:** T1:L10, T2:L14, T2:L54; Q8, Q11, Q12
- **Dependencies:** COO ratification

### E5. Document chasing

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Decision:** REDESIGN, not eliminate. Intake requests everything up front with a structured checklist and a deadline; reminders are automated. A written fallback rule for deciding on incomplete documents replaces "judgment" (T2:L34).
- **Requirement to be specified:** the fallback rule's parameters are to be defined by the consultant in requirements v1.
- **Rejected options:** (a) Eliminate chasing. (b) Automate today's email chasing as is.
- **Rationale:** The step cannot be skipped, because the evidence is needed to decide and to file with the carrier (T2:L34, T2:L30). Documents arrive piecemeal (T2:L28; Q13), and the stopping point is unwritten judgment (T2:L34).
- **Citations:** T2:L18, T2:L28, T2:L30, T2:L34, T2:L46; Q4, Q13

### E6. Filing clean-POD shortages with carriers

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Status:** **UNTESTED** until a POD-exception field exists (Q10)
- **Decision:** ELIMINATE. Endorse current practice and codify it as a rule.
- **Rejected options:** (a) File all shortages. (b) Leave the practice uncodified until it is tested.
- **Rationale:** The claims lead states that carriers deny clean-POD shortages every time (T2:L20, T2:L64). Release 1 cannot test this: there is no POD-exception field, and filed shortage claims in Q10 cannot be split by POD status.
- **Citations:** T2:L20, T2:L64; Q10
- **Dependencies:** POD-exception field in the follow-up data request

---

## Redesign rulings (Day 1): C5 open points and loss-claim scope

These rulings settle the three open points in C5 (dependency D6) and the
loss-claim scope question in SOW §3. Each decision is the consultant's,
recorded as given. Rejected options and rationale were drafted by Claude and
confirmed by the consultant without edits on 2026-10-18. C5 itself is not edited; these
entries refine it.

Two clarifications were agreed before logging (2026-10-18):
- **S1** is recorded as a clarification, reworded so it does not widen SOW §3.
- **C5a** cites the release-1 reason for partials (salvage or depreciation,
  Q14) instead of packaging and filing window, which are denial reasons in Q14.

### C5a. Partial approvals at or below $10k

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Refines:** C5, open point 1
- **Decision:** Human sign-off.
- **Rejected options:** (a) Autonomous, treating partials like approvals at or below $10k. (b) Autonomous when the reduction follows a fixed salvage or depreciation formula, otherwise sign-off.
- **Rationale:** A partial is a partial denial. Sending it to a person matches "all denials to human sign-off" (C5) and the COO's red line, a wrongful denial to a key account (T1:L36). Every partial in release 1 is a salvage or depreciation reduction (Q14), and the size of that reduction is a judgment call. Revisit after the Day 2 eval if partials turn out to be mostly mechanical.
- **Citations:** T1:L36; Q14
- **Dependencies:** Day 2 eval result on partials

### C5b. Approvals at or below $10k with incomplete documents

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Refines:** C5, open point 2; specifies the fallback in E5
- **Decision:** The agent never decides on incomplete documents. It holds the claim at intake and sends automated reminders (E5). At the fallback deadline (`FALLBACK_DEADLINE_DAYS`, set in requirements v1), the claim routes to human sign-off. "Documents complete" is a precondition for the autonomous tier.
- **Rejected options:** (a) The agent decides on the documents it has at the deadline. (b) The agent approves low-value claims without full documents to save time. (c) The claim is closed automatically at the deadline.
- **Rationale:** Deciding or paying before documents are complete is the account-manager failure pattern: those claims are paid before documents are complete far more often and recover far less (Q11). Without photos or a delivery receipt there is nothing to file with the carrier (T2:L30). Today the stopping point is unwritten judgment (T2:L34); a fixed deadline that routes to a person replaces it without letting the agent guess.
- **Citations:** T2:L30, T2:L34; Q11, Q13
- **Dependencies:** `FALLBACK_DEADLINE_DAYS` set in requirements v1

### C5c. Special flags

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling
- **Refines:** C5, open point 3
- **Decision:** In addition to temperature/reefer claims and expedite requests (C5, always escalate), these flags apply:

  | Flag | Route | Citation |
  |---|---|---|
  | Cold-chain contract customer | Always escalate | T2:L44 |
  | Key-account customer | Human sign-off for any denial or partial; a straight approval may stay autonomous | T1:L10, T1:L36 |
  | Possible duplicate: same shipment or claim already paid | Human sign-off | T2:L68 |
  | Claimed amount does not match the invoice | Human sign-off | T2:L42 |
  | Outside the customer filing window | Human sign-off | Q14 |
  | Agent confidence below `CONFIDENCE_THRESHOLD` | Human sign-off | Consultant parameter |

  Not special flags:
  - **Amount above the deductible.** It is already an always-escalate trigger under C5.
  - **The insurer's 30-day notice clock.** It is an urgency alert on escalated claims, not a routing flag (T2:L16, T2:L48).
- **Rejected options:** (a) No flags beyond C5; rely on the confidence score alone. (b) Route every key-account claim to sign-off, including straight approvals. (c) Treat the 30-day insurer clock as a routing flag.
- **Rationale:** Each flag marks a known failure or liability exposure. Cold-chain customers are paid "almost no matter what" under contract terms, so the claim is about liability and recovery, not a decision the agent should own (T2:L44). Key accounts carry the COO's red line on wrongful denials (T1:L36), but a correct approval does not create that risk, so approvals can stay autonomous. Duplicate payments have happened and one was written off (T2:L68). The claimed amount is checked against the invoice today (T2:L42). Filing-window denials occur in the data (Q14). A low-confidence decision should not go out unreviewed.
- **Citations:** T1:L10, T1:L36, T2:L16, T2:L42, T2:L44, T2:L48, T2:L68; Q14
- **Dependencies:** `CONFIDENCE_THRESHOLD` calibrated in the Day 2 eval

### S1. Loss-claim scope

- **Date / step:** 2026-10-18, Day 1 / redesign
- **Type:** Design ruling. **Clarification of SOW §3, not a scope change.**
- **Decision:** Split scope.
  - **Process redesign:** loss claims go through the same team and process as damage and shortage claims (T2:L50). The redesigned steps (E1–E5) change that shared process, so they also apply to loss claims as a side effect. No loss-specific steps or evidence rules are designed.
  - **Agent pilot:** excludes loss claims. Their evidence differs (nothing delivered to photograph, T2:L50), and they are not in release 1. Loss claims are the phase-2 expansion candidate.
  - The SOW text is unchanged. Damage and shortage remain the designed scope.
- **Rejected options:** (a) Design loss-specific redesign steps now. (b) Include loss claims in the agent pilot. (c) Draw the redesign as damage and shortage only, ignoring that the process is shared.
- **Rationale:** The claims lead describes one process for all claim types (T2:L50). Drawing a future state that applies only to damage and shortage would misstate how the team works, and the redesigned steps affect every claim that passes through them. The agent needs claim-type-specific evidence rules, and release 1 has no loss claims to test against, so loss claims wait for phase 2.
- **Citations:** T2:L50; SOW §3; release 1 cover note (`data/released/README.md`)

### Consultant-owned parameters

Set by the consultant. Claude does not set or change them.

| Parameter | Used in | Status | Set when |
|---|---|---|---|
| `CONFIDENCE_THRESHOLD` → `RUBRIC_SCORE_THRESHOLD`, `SELF_REPORTED_CONFIDENCE_THRESHOLD` (G11, G17) | C5c; autonomous tier (C5) | Unset; provisional values to be calibrated in the Day 2 eval | Day 2 |
| `FALLBACK_DEADLINE_DAYS` | C5b, E5 | **14 days** (set 2026-10-19; see P2 below) | Requirements v1 |
| `EXPEDITE_RESPONSE_SLA` | D5 outcome, D5g | **Business days; before 14:00 → end of that day; at or after 14:00 → 12:00 next business day** (Eastern Time; company holidays excluded, US federal as provisional default (P3a); provisional assumption, set 2026-10-27; see P3 below; awaits claims-lead capacity D10 and COO written confirmation) | Requirements v1 |

---

## Redesign rulings (Day 2): coverage-test gaps G1–G3

These rulings close gaps G1–G3 in `engagement/02-redesign/open-gaps.md`,
which broke the coverage test. Each decision is the consultant's, recorded as
given on 2026-10-19. Rejected options and rationale were drafted by Claude
and confirmed by the consultant without edits on 2026-10-19. The position of
hold in the G2 precedence order was proposed by Claude and confirmed by the
consultant. C5b and S1 are not edited; G1 and G3b refine them.

### G1. Loss claims reaching the agent

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** S1
- **Decision:** Step 0 in the decision tree: a loss claim is always escalated. The agent forms no decision on it.
- **Rejected options:** (a) A filter before the agent sends loss claims to the claims team, so the agent never sees them. (b) The filter plus an agent-side escalation as a backstop.
- **Rationale:** S1 excludes loss claims from the agent pilot, but no step caught them, so a $6k loss approval reached the autonomous tier (coverage #7). Escalation matches the rule that anything outside the agent's scope goes to escalate (CLAUDE.md, claims-agent). It also keeps the control inside the agent, where the eval can test it, instead of relying on an intake step outside the spike.
- **Citations:** T2:L50; S1; coverage test #7
- **Consequences:** Loss claims add volume to the escalation queue. The eval set includes at least one loss claim as a must-escalate case.

### G2. Claims that match more than one tier

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Decision:** The highest tier wins, and the decision-tree order governs: escalate > hold (G3a) > human sign-off > autonomous. The scope table's rows are not mutually exclusive; they are read in this precedence order.
- **Rejected options:** (a) Rewrite the scope-table rows to be mutually exclusive.
- **Rationale:** C5 itself overlaps: "all denials → sign-off" and "above the deductible → escalate" both match a $30k denial (P2). A single precedence rule settles every overlap, including P1 (a $9k reefer key-account denial), and keeps the table readable. Exclusive rows would have to be rechecked against every other row each time a row is added.
- **Citations:** C5, C5c; coverage probes P1, P2

### G3a. Documents hold is a state, not a route

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5b
- **Decision:** While documents are incomplete and `FALLBACK_DEADLINE_DAYS` has not been reached, the agent returns no route. The claim sits in a visible "awaiting documents" list and automated reminders go out (E5). The route stays limited to three values (`autonomous`, `sign_off`, `escalate`); the hold is carried in a separate status field, to be specified in requirements v1.
- **Rejected options:** (a) Add `hold` as a fourth route. (b) Put held claims in the sign-off queue, tagged "awaiting documents".
- **Rationale:** A held claim has no decision yet, so giving it a route would record a routing outcome that has not happened. Keeping three routes holds to the claims-agent output spec (CLAUDE.md). Putting held claims in the sign-off queue would mix waiting work with work that is ready to decide.
- **Citations:** T2:L30, T2:L34; Q13; C5b, E5; coverage probe P3
- **Dependencies:** Status field and "awaiting documents" list specified in requirements v1. Who owns the list is open (`open-gaps.md` G7).

### G3b. Documents hold applies at every amount

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5b
- **Decision:** The documents hold applies to every claim that is not escalated at step 0 or step 1, at any amount. C5b's wording, "approvals at or below $10k", is replaced for routing purposes by "any non-escalated claim".
- **Rejected options:** (a) Hold claims at or below $10k only; claims above $10k go straight to sign-off with the documents they have.
- **Rationale:** The hold happens at intake, before the agent forms a decision, so whether a claim will be an approval is not yet known. Sending larger claims to sign-off with incomplete documents would bring manual chasing back for those claims (E5). Deciding on incomplete documents is the failure pattern C5b exists to prevent (Q11).
- **Citations:** T2:L30, T2:L34; Q11, Q13; C5b, E5; coverage probe P3

---

## Redesign rulings (Day 2): definitions G4–G5

These rulings close definition gaps G4 and G5 in
`engagement/02-redesign/open-gaps.md`. Each decision is the consultant's,
recorded as given on 2026-10-19. Rejected options and rationale were drafted
by Claude and confirmed by the consultant without edits on 2026-10-19. C5 is
not edited; these entries define its terms.

### G4. Threshold basis: claimed amount

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Definition ruling
- **Refines:** C5 ($10k line and deductible)
- **Decision:** Both thresholds, the $10k line and the deductible, are measured on the claimed amount.
- **Rejected options:** (a) Claimed amount at step 1 (deductible), proposed payout at step 6 ($10k line). (b) The higher of the claimed amount and the proposed payout.
- **Rationale:** The deductible check runs at step 1, before the agent forms a decision, so only the claimed amount is known there. The claims lead states the insurer rule as "any claim over the deductible" (T2:L16). At the $10k line, the basis changes no route in the released data, because every claim paid below its claimed amount is a partial and partials go to sign-off (C5a; Q15). One definition for both thresholds keeps the requirements unambiguous. The one paid claim claimed above the assumed deductible and paid below it escalates under this ruling (Q15).
- **Citations:** T2:L14, T2:L16, T2:L62; Q15; C5, C5a

### G5. Temperature/reefer trigger: either signal

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Definition ruling
- **Refines:** C5 (temperature/reefer escalation)
- **Decision:** The temperature/reefer escalation fires on either signal: the shipment ran on reefer equipment (`reefer_flag` = Y), or the customer alleges a temperature excursion. Either one escalates at intake.
- **Rejected options:** (a) Temperature allegation only, on any equipment. (b) Reefer equipment only.
- **Rationale:** The temperature download is kept about 72 hours and must be requested the same day (T2:L44, T2:L58), so a missed trigger cannot be recovered. The equipment flag is deterministic and held in the data (release 2). The allegation matches the claims lead's own definition (T2:L44) and catches a temperature claim if the equipment flag is wrong or missing. In the released data, temperature logs are required only on reefer claims (Q16), so the equipment flag drives the volume: 48 of 363 claims, including damage and shortage claims with no temperature allegation.
- **Citations:** T2:L44, T2:L58; Q16; release 2 (`reefer_flag`)
- **Consequences:** Higher escalation volume than an allegation-only trigger (Q16). Non-temperature claims on reefer equipment, such as a crushed pallet, also escalate. The eval inputs carry both `reefer_flag` and a temperature-allegation field.

---

## Redesign rulings (Day 2): key accounts and tier operations G6–G7

These rulings close gaps G6 and G7 in `engagement/02-redesign/open-gaps.md`.
Each decision is the consultant's, recorded as given on 2026-10-19.
Rejected options and rationale were drafted by Claude and confirmed by the
consultant without edits on 2026-10-19. C5 and C5c are not edited; these
entries refine them.

### G6. Key-account flag: priority and account-manager notice, not routing

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5c (key-account flag)
- **Decision:** The key-account flag is removed from routing (scope-table R12). It becomes two actions: (1) key-account claims are worked first within the sign-off and escalation queues; (2) the account manager is notified of the outcome when the claim is decided. The notice carries no approval or payment rights (C4).
- **Rejected options:** (a) Keep R12 as a guard row in case C5a is revisited. (b) Guard row plus priority and notice. (c) Drop the flag entirely, keeping it only as a trace attribute.
- **Rationale:** Every key-account denial or partial already reaches sign-off through the denial and partial rules (C5, C5a), so R12 never decided a route (coverage #1). Priority and notice answer the COO's concern that key-account problems are fixed quickly (T1:L10) and keep the account manager informed, without bringing back account-manager authority (C4, E4). The red line, a wrongful key-account denial (T1:L36), stays covered because every denial goes to a person.
- **Citations:** T1:L10, T1:L36; C4, C5, C5a, C5c, E4; coverage test #1
- **Consequences:** If C5a is revisited after the Day 2 eval and partials become autonomous, key-account partials would no longer reach a person. Any C5a revision must address key accounts explicitly.

### G7a. Human sign-off: full draft to approve

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5 (human sign-off tier)
- **Decision:** For every sign-off claim, the agent drafts the decision, amount, rule applied, rationale and customer letter. The person approves, edits or overrides. Every edit or override is logged with a reason.
- **Rejected options:** (a) Decision draft without the letter; the person writes the letter. (b) Summary only, with no proposed decision.
- **Rationale:** The claims lead sees the agent helping with "a first draft of the decision" (T2:L58). Letters are part of the team's hands-on time today (T2:L60, T2:L66). Logged overrides give the data needed to calibrate `CONFIDENCE_THRESHOLD` (P1) and to revisit C5a.
- **Citations:** T2:L58, T2:L60, T2:L66; C5, C5a; P1

### G7b. Always escalate: fact pack, no decision

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5 (always-escalate tier)
- **Decision:** For every escalated claim, the agent produces a fact pack: the trigger(s) that fired, the document checklist status, and any running clock (the 72-hour reefer window, the insurer 30-day notice). It proposes no decision and no amount.
- **Rejected options:** (a) Fact pack plus an advisory draft decision. (b) Alert only, with no pack.
- **Rationale:** Escalated claims are the ones ruled outside the agent's scope: loss, temperature/reefer, cold-chain, expedite requests and claims above the deductible (C5, C5c, G1). An advisory draft would have the agent deciding them in practice. The clocks are the reason these claims cannot wait (T2:L16, T2:L44, T2:L58), so the pack leads with them.
- **Citations:** T2:L16, T2:L44, T2:L48, T2:L58; C5, C5c, G1

### G7c. Queue ownership: the $10k split, with an escalation backup

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5 (queue ownership)
- **Decision:** Specialists work sign-off claims with a claimed amount at or below $10k (G4). The claims lead works sign-off claims above $10k and all escalations. The senior specialist covers escalations when the lead is unavailable.
- **Rejected options:** (a) The $10k split with no backup. (b) A single pool; anyone works any item.
- **Rationale:** The split is the authority line the team already works to (T2:L14, T2:L24, T2:L62), and C2 and C5 are aligned to it. The lead also handles reefer calls personally (T2:L44) and splits time between claims and dispatch (T2:L24), so without a backup the 72-hour reefer window depends on one person's availability.
- **Citations:** T2:L14, T2:L24, T2:L44, T2:L62; C2, C5, G4
- **Backup role:** named by the consultant on 2026-10-19 as **senior specialist**. The team has no senior specialist title today (T2:L24), so requirements v1 defines the role as a designation within the existing specialist team.

### G7d. Response time: reefer same day only

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Decision:** Reefer and temperature escalations (G5) are picked up on the day the claim is received. No other queue has a response-time target in v1. Wait times in the other queues are measured in the pilot and targets are set from that data.
- **Rejected options:** (a) Set targets for every queue now, as labelled assumptions. (b) No targets in v1, including reefer.
- **Rationale:** The only time limit in the evidence is the reefer download, which must be requested the same day (T2:L44, T2:L58). There is no source for other targets, and there are no recorded escalations today (T2:L40), so any other number would be invented.
- **Citations:** T2:L40, T2:L44, T2:L58; G5

### G7e. Owner of the "awaiting documents" list

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** G3a
- **Decision:** Claims specialists own the "awaiting documents" list. The agent sends the reminders (E5). At `FALLBACK_DEADLINE_DAYS`, a held claim routes to sign-off under the G7c split.
- **Rejected options:** (a) The claims lead owns it. (b) No human owner; the agent runs reminders and the deadline alone.
- **Rationale:** Specialists handle intake and chasing today (T2:L20, T2:L24). A human owner can see claims stuck in hold. Giving the list to the lead would add to a role already split with dispatch (T2:L24).
- **Citations:** T2:L20, T2:L24; E5, G3a, G7c

---

## Redesign rulings (Day 2): autonomous scope and insurer controls G8–G9

These rulings close gaps G8 and G9 in `engagement/02-redesign/open-gaps.md`.
Each decision is the consultant's, recorded as given on 2026-10-19.
Rejected options and rationale were drafted by Claude and confirmed by the
consultant without edits on 2026-10-19. C4, C5 and E6 are not edited; these
entries refine them.

### G8a. What the agent does on an autonomous approval

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C4, C5 (autonomous tier)
- **Decision:** On an autonomous approval, the agent sends the customer letter and issues the payment instruction to finance, with no pre-approval (E1). It prepares the carrier filing package, and a claims specialist submits it. For a shortage with a clean POD, the agent marks the claim "do not file" (E6) instead of preparing a package, and the specialist confirms.
- **Superseded in part (G16, 2026-10-27):** the clean-POD "do not file" clause above is superseded by E6a. Clean-POD shortages are filed like any other paid claim with evidence.
- **Rejected options:** (a) Full straight-through: the agent also submits the carrier filing. (b) The agent drafts the letter and payment instruction, and a specialist releases both.
- **Rationale:** The claims team owns payouts (C4). An autonomous approval is the team's decision made by its agent within the scope table, so the letter and payment follow from it, and no pre-approval applies at or below $10k (E1). Carrier filing is where recovery is won or lost (Q11), and the clean-POD rule the agent would apply is untested (E6). A person submitting the filing keeps that exposure with the team.
- **Citations:** T2:L18, T2:L20, T2:L64; Q10, Q11; C4, C5, E1, E6

### G8b. Control on autonomous decisions during the pilot

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Decision:** During the pilot, a person reviews every autonomous decision after it is made. Review moves to a sample once the agent has proved itself.
- **Rejected options:** (a) A sample audit from the start. (b) No control beyond the trace log.
- **Rationale:** The autonomous tier pays customers without a person in the loop. Until pilot data shows its error rate, every decision is checked after the fact. This does not slow the customer, because the review follows the payment.
- **Citations:** C5, G7a
- **Open (consultant):** who performs the review; the criterion for moving to a sample; the sample rate after that.

### G9a. Insurer 30-day clock start: unset until the CFO confirms

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Status:** PROVISIONAL until the CFO confirms the policy wording (Day 3)
- **Decision:** The start of the insurer's 30-day notice period is not set. Until the CFO confirms it, the urgency alert on escalated claims above the deductible shows the delivery date and the receipt date, with no countdown.
- **Rejected options:** (a) Count from the delivery date, falling back to the receipt date. (b) Count from the receipt date.
- **Rationale:** "Within 30 days" (T2:L16, T2:L48) does not say of what. The released data cannot tell the two dates apart: the same two notices are late on either basis, and those are the only two where the insurer did not consent (Q17). A countdown on the wrong basis would show the wrong time left.
- **Citations:** T2:L16, T2:L48; Q12, Q17; C5c, G7b
- **Dependencies:** CFO to confirm when the notice period starts (Day 3).

### G9b. Insurer consent: hard gate on payment

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5 (claims above the deductible)
- **Decision:** No payment instruction can be issued on a claim whose claimed amount is above the deductible (G4) until insurer consent is recorded on the claim.
- **Rejected options:** (a) Consent as a checklist item in the escalation fact pack.
- **Rationale:** The insurer must agree before settlement, or it can walk away (T2:L16). The one claim paid before notice lost cover (Q12; NLC-26-0169). That payment came from outside the claims team's process (Q11), so a control that relies on a person ticking a box in the claims queue would not have stopped it.
- **Citations:** T2:L16, T2:L48; Q11, Q12; C4, C5, G4
- **Open (consultant):** who records consent on the claim.

---

## Redesign rulings (Day 2): re-routing, confidence and withdrawals G10–G12

These rulings close gaps G10–G12 in `engagement/02-redesign/open-gaps.md`.
Each decision is the consultant's, recorded as given on 2026-10-19.
Rejected options and rationale were drafted by Claude and confirmed by the
consultant without edits on 2026-10-19. C5c is not edited; G11 refines it.

### G10a. Re-routing on new information: up only

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5, C5b, E4
- **Decision:** New information (an expedite request, late documents, a new flag) re-runs the decision tree. The claim can move up a tier but never down (autonomous → sign-off → escalate). A claim already with a person stays with that person, who sees the new information. New information after an autonomous decision sends the claim to sign-off.
- **Rejected options:** (a) Re-run the full tree freely until a decision, so a claim can move up or down. (b) Freeze the route at first routing and attach new information for whoever holds the claim.
- **Rationale:** Without a rule, claims stall or are routed twice (open-gaps G10). Moving only up means no claim leaves a person's hands on the strength of later information. An expedite request on a claim already under way still reaches a person (E4).
- **Citations:** C5, C5b, E4, G2

### G10b. No handback from escalation

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Decision:** A person finishes every escalated claim. It is never released back to the sign-off path or to the agent's tree.
- **Rejected options:** (a) Handback to sign-off, where the agent drafts and a specialist approves. (b) Handback to the agent's tree with the trigger cleared.
- **Rationale:** Consistent with G10a: claims move only up. Escalated claims are the ones ruled outside the agent's scope (C5, C5c, G1, G7b).
- **Citations:** C5, C5c, G1, G7b, G10a; Q16
- **Consequences:** The lead and the senior specialist carry routine work on escalated claims that turn out to be simple, such as non-temperature damage on reefer loads (G5; Q16). Escalation-queue load is measured in the pilot.

### G11. Confidence: two gates

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Refines:** C5c (confidence flag)
- **Decision:** Confidence is produced two ways: a rubric score from a fixed checklist, and the model's self-reported confidence. Each has its own threshold, and both must pass for the autonomous tier. If either fails, the claim goes to human sign-off. `CONFIDENCE_THRESHOLD` (P1) becomes two parameters.
- **Rejected options:** (a) Rubric only. (b) Self-report only. (c) Self-consistency: agreement across repeated runs.
- **Rationale:** The confidence score gates whether a decision goes out with no person in the loop. Requiring both signals to pass means doubt from either one sends the claim to a person. The two are on different scales, so each gets its own threshold rather than being combined. The rubric is explainable in the trace; the self-report is tested in the eval for whether it separates right from wrong decisions. Self-consistency was rejected for cost: it runs the model more than once per claim.
- **Citations:** C5, C5c; P1; G7a, G8b
- **Open (consultant):** the rubric checklist (requirements v1); both threshold values (calibrated in the Day 2 eval).

### G12. Withdrawn claims: new status

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling
- **Decision:** A customer withdrawal sets a new status, `withdrawn`, with the withdrawal date and reason recorded. The claim leaves any hold or queue with no route. If any payment has already been made, the claim goes to human sign-off instead.
- **Rejected options:** (a) Every withdrawal goes to a person to confirm and close. (b) Withdrawals stay manual and outside the pilot.
- **Rationale:** Withdrawals happen "now and then" with no code, so they are closed with at most a note (T2:L70), and the system has no withdrawn status (release 2 cover note §2). A status makes them countable. A paid claim cannot simply be closed, so it goes to a person. Open claims without a decision are already covered by the hold state (G3a; Q14).
- **Citations:** T2:L70; Q14; release 2 cover note §2; G3a

---

## Redesign revision (Day 2): clean-POD filing E6a

Recorded as given on 2026-10-19. Rejected options and rationale were
drafted by Claude and confirmed by the consultant without edits on
2026-10-19. E6 is not edited; E6a supersedes it.

### E6a. File clean-POD shortages with the carrier

- **Date / step:** 2026-10-19, Day 2 / redesign
- **Type:** Design ruling. **Revision of E6.**
- **Supersedes:** E6, and the "do not file" marking in G8a
- **Decision:** REVERSE E6. Clean-POD shortages are filed with the carrier like any other paid claim that has evidence. A clean POD is not a bar to filing. On the autonomous route the agent prepares the filing package and a specialist submits it (G8a).
- **Rejected options:** (a) File clean-POD shortages only above an amount set by the consultant. (b) The agent prepares the package with a lower-recovery note and the specialist decides whether to file. (c) Keep E6 and raise Q18 with the CFO on Day 3.
- **Rationale:** E6 was ruled UNTESTED on the claims lead's account that carriers deny clean-POD shortages "every single time" (T2:L20, T2:L64). Release 2's `pod_exception` field tests it: of the clean-POD shortages filed and answered by the carrier, most were accepted, and filed clean-POD shortages recovered money (Q18). Recovery is lower than on POD-exception shortages, but not zero. Most paid clean-POD shortages were never filed (Q18), so the current practice gives up recoverable money.
- **Caveats:** Small sample, with some carrier responses still pending (Q18). The filed clean-POD shortages may have been selected because they had other evidence, so they may not represent the unfiled ones.
- **Citations:** T2:L20, T2:L64; Q10, Q18; E6, G8a
- **Consequences:** Step 7 of the decision tree no longer branches on POD status. The business case can count recovery on clean-POD shortages, using Q18 as the basis.

---

## Pre-freeze rulings (Day 2): fallback deadline, duplicate check, D5

Recorded as given on 2026-10-19. Rejected options and rationale were
drafted by Claude and confirmed by the consultant without edits on
2026-10-19.

### P2. `FALLBACK_DEADLINE_DAYS` = 14

- **Date / step:** 2026-10-19, Day 2 / pre-freeze
- **Type:** Parameter ruling
- **Sets:** P2 (C5b, E5, G3a, G7e)
- **Decision:** `FALLBACK_DEADLINE_DAYS` is 14 calendar days from receipt. A claim whose documents are still incomplete on day 14 routes to human sign-off.
- **Rejected options:** (a) 21 days. (b) 30 days.
- **Rationale:** 92% of the claims whose documents were completed had completed them within 14 days (Q19). Claims whose documents never complete reach a person after two weeks rather than waiting indefinitely (Q13). The cost is that some slow claims whose documents would have arrived go to sign-off with documents still due. Under G10a, they stay with that person, who sees the documents when they arrive.
- **Citations:** T2:L28, T2:L34; Q13, Q19; C5b, E5, G10a

### G13. Duplicate check: flag at intake, route at step 3

- **Date / step:** 2026-10-19, Day 2 / pre-freeze
- **Type:** Design ruling
- **Resolves:** "Rule-check order" in `open-gaps.md`
- **Refines:** C5c (duplicate flag)
- **Decision:** The duplicate check runs at intake and raises a flag on the claim, visible to the specialists who own the "awaiting documents" list (G7e). Routing on the flag stays at step 3, after documents are complete, so G2 (hold > sign-off) is unchanged.
- **Rejected options:** (a) Route a possible duplicate to sign-off at intake, as an exception to G2. (b) Keep the check at step 3 only.
- **Rationale:** Duplicate payments have happened and one was written off (T2:L68). Flagging at intake lets a specialist see a likely duplicate before documents are chased, without making an exception to the precedence rule.
- **Citations:** T2:L68; release 2 (`shipment_ref`, `prior_payment_same_shipment`); C5c, G2, G7e

### D5 handling: sponsor summary and COO ratification session

- **Date / step:** 2026-10-19, Day 2 / pre-freeze
- **Type:** Governance ruling
- **Resolves:** how dependency D5 (COO ratification of C4, E4) is met before the v1 freeze
- **Decision:** C4 and E4 are reported to the sponsor in a Day 2 summary, following the route in SOW §8 and §10. A short `/interview` session with the COO then ratifies or rejects them. Requirements v1 is frozen on the outcome.
- **Rejected options:** (a) Report in the Day 2 summary and freeze v1 with C4/E4 marked pending. (b) Freeze v1 with C4/E4 pending and take ratification into Day 3.
- **Rationale:** SOW §8 makes the sponsor summary the route for ratifying conflict rulings. A live session tests the ruling against the sponsor's stated preference for account-manager authority (T1:L10) before engineering builds on it. Freezing on a pending ruling would risk a v2 change driven by governance rather than by the cold-FDE test.
- **Citations:** T1:L10; SOW §8, §10; C4, E4

---

## Ratification rulings (Day 2): COO session on C4/E4, D5a–D5d

These rulings set the terms of the D5 ratification session (Interview D in
`engagement/01-discovery/interview-guide.md`) before it runs. Decisions,
rejected options and rationale are the consultant's, recorded as given on
2026-10-26. The consultant gave them as R1–R4; they are logged as D5a–D5d
because scope-table rows use R1–R16. The D5 revision note in D5a was drafted
by Claude and confirmed by the consultant without edits on 2026-10-26. D5
handling is not edited; D5a revises it.

### D5a. What counts as ratified

- **Date / step:** 2026-10-26, Day 2 / pre-freeze
- **Type:** Design ruling
- **Refines:** D5 handling. **Revises** its rejected options (a) and (b) for the "not ratified" outcome
- **Decision:** A conditional yes counts only if the condition can be written as a requirement without changing the core of C4/E4: the claims team owns all payouts and account managers cannot pay.
  - **Yes** → ratified; proceed to requirements v1.
  - **Yes with a service or communication condition** (for example, same-day handling of key-account expedite requests) → ratified; the condition becomes an expedite service-level requirement in v1.
  - **Yes with any payment authority returned to account managers** → not ratified; write a new ruling amending C4/E4 before v1.
  - **No, or deferred** → not ratified; write v1 with C4 flagged as an open dependency.
- **Rejected options:** (a) Count any conditional yes. (b) Require an unconditional yes.
- **Rationale:** Fixing the rule before the session prevents rationalizing a weak yes afterwards. The test is whether the requirements keep a single payout path.
- **Revision of D5 handling:** D5 rejected freezing v1 with C4/E4 pending, to avoid a v2 change driven by governance rather than by the cold-FDE test. For "no" or "deferred", and for a session that does not converge (D5d), v1 now proceeds with C4 open and that risk is accepted.
- **Citations:** SOW §8; C4, E4; D5 handling

### D5b. Payment speed raised by the consultant

- **Date / step:** 2026-10-26, Day 2 / pre-freeze
- **Type:** Design ruling
- **Decision:** The consultant raises the payment-speed gap (account managers a median of 20 days from receipt to payment, the claims team 28; Q11) early in the session, with its cause.
- **Rejected options:** (a) Leave it for the COO to raise. (b) Omit it.
- **Rationale:** It is the COO's strongest counterargument, and hiding it damages credibility. The speed comes from paying before documents are complete (61% vs 0%; Q11), the same behaviour behind lower filing and recovery (Q11) and the declined insurer claim (Q12). The redesign targets the claims team's delay (E1, E2, E3, E5), and E4 expedite requests give key accounts a fast lane. The redesign is not promised to reach 20 days; that is a target to measure.
- **Citations:** T1:L10; Q11, Q12; E1, E2, E3, E4, E5

### D5c. Data shown: headline figures only

- **Date / step:** 2026-10-26, Day 2 / pre-freeze
- **Type:** Design ruling
- **Decision:** Show headline figures only: paid before documents complete, recovered ÷ paid, and median days to payment (Q11), plus the single insurer case (Q12) presented as one claim, not a rate. The full Q8, Q11 and Q12 tables are backup, shown only if challenged.
- **Rejected options:** (a) Present the full tables.
- **Rationale:** The sponsor is making one decision, and full tables invite a debate about method instead.
- **Citations:** Q8, Q11, Q12

### D5d. Timebox: 25 minutes with a hard stop

- **Date / step:** 2026-10-26, Day 2 / pre-freeze
- **Type:** Design ruling
- **Decision:** 25-minute session: 3 min recap and ask; 7 min evidence, speed gap first (D5b); 3 min what account managers keep or gain; 10 min objections and conditions; 2 min close with an explicit one-sentence restatement and confirmation. Hard stop: if the session does not converge, log "not ratified" and proceed under D5a.
- **Rejected options:** (a) An open-ended session.
- **Rationale:** Matches the discovery interviews; a single executive decision should not need more.
- **Citations:** interview guide (Interviews A and B, 25 min); D5a

---

## Ratification outcome (Day 2): D5, D5e–D5h, P3

The consultant's rulings on the outcome of the COO ratification session
(T3), recorded as given on 2026-10-27. The consultant referred to D5a by its
original ID, R1. One conflict was raised before logging: P3's 14:00 cut-off
promises less than the "same day" in T3:L30. The consultant resolved it by
putting P3 in the sponsor follow-up note for the COO's written confirmation.
The rejected options for D5e, P3, D5f, D5g and D5h, the D5h rationale and
this note were drafted by Claude and confirmed by the consultant without
edits on 2026-10-27. On the same day the consultant set P3's "local time" to
headquarters time (Eastern), asked for D5e to be included in the follow-up
note, and chose a written note to the claims lead for D10.

### D5 outcome. Ratified with a service condition

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Governance outcome
- **Resolves:** D5 (COO ratification of C4, E4)
- **Classification:** **Ratified with a service condition**, under D5a branch 2 ("Yes with a service or communication condition"). C4 and E4 stand unchanged.
- **Conditional on:** D5e (what counts as an answer) and D5h ("approve" is covered), and on the COO confirming in writing, in the sponsor follow-up note, both the restated decision and P3.
- **The COO's condition, verbatim (T3:L30):** "Yes. The claims team owns every payout, AMs don't pay, and every expedite request gets an answer the same day, with Priya on the hook for it. If that same-day answer isn't happening, I want to hear about it, because that's the part I'm agreeing to."
- **The consultant's interpretation:** the condition is about service and accountability: a same-day answer to every expedite request, a named owner, and the sponsor being told about misses. It returns no approval or payment authority to account managers, so the single payout path that D5a tests for holds. The COO rejected a fallback payment right for account managers (T3:L26–L28).
- **Citations:** T3:L20–L30; C4, E4, D5a

### D5e. What counts as an expedite "answer"

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Design ruling
- **Refines:** D5 outcome (the T3:L30 condition)
- **Decision:** The same-day answer to an expedite request is limited to the current status, the next step, and the expected date where known. A payment commitment is allowed only if the claims team has already approved the claim (for example, "approved, payment going out [date]"). There is no commitment to pay before the claim is decided, before documents are complete, or before the insurer has consented where that is required.
- **Rejected options:** (a) Allow an answer such as "we're paying, it's in hand" before a decision (T3:L22).
- **Rationale:** "We're paying, it's in hand" before a decision obliges the claims team to pay. That is the account-manager bypass at one remove, and under D5a it would make the outcome "not ratified". Reporting a decision already made gives the account manager something concrete for the customer without returning payment authority.
- **Citations:** T3:L22; T2:L16; G9b, D5a

### P3. `EXPEDITE_RESPONSE_SLA` (provisional)

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Parameter ruling (consultant-owned, provisional)
- **Sets:** the expedite service-level requirement in D5a branch 2
- **Decision:** Measured in business days, not calendar days. A request received before 14:00 local time is answered by the end of that business day. "Local time" means headquarters time: Eastern Time. Public holidays are not business days (consultant, 2026-10-27). A request received at or after 14:00 is answered by 12:00 the next business day.
- **Assumption:** No data supports these values. They are labelled an assumption. The headquarters location is also an assumption: Northline Freight is fictional, and it is assumed to be headquartered in the Eastern time zone.
- **Open dependency:** the claims lead must confirm capacity (D10). The claims lead splits time roughly 60/40 between claims and dispatch (T2:L24) and was not party to this commitment. Route: a written note to the claims lead (`engagement/00-governance/claims-lead-capacity-d10.md`).
- **Sponsor confirmation:** The cut-off promises less than "the same day" in T3:L30. P3 goes in the sponsor follow-up note for the COO's written confirmation (see the conflict note above).
- **Rejected options:** (a) Calendar days. (b) No cut-off.
- **Rationale:** The team works business hours, and nobody has discussed weekend cover. A cut-off makes the promise achievable, and a missed promise erodes trust faster than a slightly weaker one.
- **Citations:** T3:L30; T2:L24; D5a

### D5f. Expedite miss reporting: recorded in v1, reported through governance

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Design ruling
- **Refines:** D5 outcome (T3:L30, "I want to hear about it")
- **Decision:** Split.
  - **v1 requirement:** for every expedite request, the system records the request time, the answer time, the answer content and the outcome.
  - **Governance item (not v1):** the miss report, its cadence and the COO's review of it.
- **Rejected options:** (a) Put the miss report in v1.
- **Rationale:** Requirements define what the system captures, not how management reviews it.
- **Citations:** T3:L30

### D5g. COO as arbiter, not an escalation route

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Design ruling
- **Refines:** D5 outcome (T3:L28, "the AM rings me")
- **Decision:** Logged as a sponsor commitment, not a v1 escalation path. The COO arbitrates disputes between the claims team and account managers, with no approval or payment authority.
  - **v1 requirement:** if `EXPEDITE_RESPONSE_SLA` is missed, the system automatically notifies the claims lead and the requesting account manager.
  - Misses reach the COO through the report (D5f), not as a live route.
- **Rejected options:** (a) A v1 escalation path from the account manager to the COO.
- **Rationale:** Routing escalations to the COO puts the bypass back one level higher and undoes C4.
- **Citations:** T3:L28; C4, D5f, P3

### D5h. "Cannot approve" treated as covered

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Interpretation
- **Refines:** D5 outcome (T3:L29–L30)
- **Decision:** "Cannot approve" is treated as covered for v1. Interpreted: payout ownership includes the approval decision (T3:L29–30). The sponsor follow-up note restates "Account managers cannot approve or pay claims; they may submit expedite requests" for the COO's written confirmation. The session is not re-run.
- **Rejected options:** (a) Re-run the session.
- **Rationale:** At the close the consultant restated "owns every payout" (T3:L29), and the COO confirmed "AMs don't pay" (T3:L30). Neither said "approve". The written confirmation closes that gap without another session. The miss is recorded in the miss review (`docs/scoring.md`).
- **Citations:** T3:L29–L30; C4

---

## Written replies (Day 2): D5 closed, G7f, D5i, P3a

The consultant's rulings on the written replies W1 (COO) and W2 (claims
lead), recorded as given on 2026-10-27. In the consultant's text, "R1" means
D5a and "D5 point 2" means D5e. Two conflicts with G7c were raised before
logging, and the consultant resolved both:

- **Decision authority:** a specialist decides an expedite claim only when the expedite request is its only escalation trigger.
- **Backup:** the "no formal backup" instruction applies only to expedite answers.

Claude reworded G7f's rejected option (b), added the T3:L25 note to G7f, and
drafted the rationales for D5 closed, D5i and P3a, the clause in G7f on why
the T2:L14 line can apply, and D11's "before go-live" timing. The consultant
confirmed all of it without edits on 2026-10-27.

### D5 closed

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Governance outcome
- **Closes:** D5 (the conditions in "D5 outcome")
- **Decision:** D5 is closed. The COO's written confirmation covers all three points in the sponsor follow-up note, including "cannot approve or pay" (W1:L2–L4), which settles D5h. The outcome stays in D5a branch 2. Requirements v1 is frozen on C4 and E4 as ratified.
- **The 14:00 caveat (W1:L3):** a preference, not a reversal, and it does not touch payout authority. It is handled as governance (D5i).
- **Rejected options:** (a) Treat the caveat as a condition that reopens P3.
- **Rationale:** Each point the ratification depended on (D5e, D5h, P3) is now confirmed in writing by the sponsor. The caveat asks that the after-14:00 path not become routine, which is a monitoring point, not a change to the decision.
- **Citations:** W1:L2–L4; D5 outcome, D5a, D5e, D5h, P3

### G7f. Expedite requests: the specialist on the claim answers, the lead owns it

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Design ruling
- **Resolves:** D10 (claims-lead capacity)
- **Refines:** G7c, for expedite requests only
- **Decision:**
  - **Ownership:** the claims lead owns every expedite escalation and the on-time answer under `EXPEDITE_RESPONSE_SLA`.
  - **Who answers:** the specialist already working the claim gives the answer (G10a). If no one is working the claim, the claims lead assigns it or answers.
  - **Who decides, when the expedite request is the claim's only escalation trigger:** the T2:L14 line applies. Specialists decide claims at or below $10k, and the claims lead decides above $10k. This is an explicit exception to G7c ("all escalations" go to the lead).
  - **When any other escalation trigger has fired** (loss, temperature or reefer, cold-chain, above the deductible): G7c applies unchanged, and the claims lead works the claim.
  - **Answer content:** every answer is bound by D5e: status, next step and expected date only, and a payment commitment only on a claim that is already approved.
  - **Routing:** the expedite request still always routes to a person, never the agent (C5, R3).
  - **Backup:** no formal backup is named for expedite answers. G7c's senior-specialist backup still applies to every other escalation.
- **Open capacity risk:** dispatch-day coverage (W2:L2). On days the claims lead is tied up with dispatch and no one is working the claim, the answer depends on the lead. This is monitored through the miss report (D5f), with no target.
- **Note:** at T3:L25 the COO was told the owner is the claims lead, with the senior specialist as backup. G7f keeps the claims lead as owner. For expedite answers, it replaces the named backup with the specialist working the claim.
- **Rejected options:**
  - (a) Reject the condition. That would bottleneck on dispatch days (W2:L2).
  - (b) Specialists answer and the lead decides, as G7c applies today. It keeps decisions at or below $10k on expedite-only claims with the lead, away from the approval line the team works to (T2:L14), and it keeps the bottleneck.
- **Rationale:** The specialist working the claim knows the file best (W2:L3), and G10a already keeps a claim with the person who has it. When the expedite request is the only trigger, the claim carries no risk that makes the escalation tier necessary. The trigger is commercial urgency, so the T2:L14 line can apply. Every other escalation trigger keeps the claim with the lead.
- **Citations:** W2:L2–L4; T2:L14, T2:L24; T3:L25; C5, R3, G7c, G10a, D5e, D5f, P3

### D5i. Miss report: after-14:00 share

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Governance ruling
- **Refines:** D5f (governance item)
- **Decision:** The governance miss report adds one metric: the share of expedite answers given under the after-14:00 path. This is monitoring only, with no target. It needs no new requirement, because D5f already records request and answer times.
- **Rejected options:** (a) Set a target. (b) Add a v1 requirement.
- **Rationale:** It answers the COO's caveat (W1:L3) with evidence rather than a promise. No target is set because there is no baseline data on when requests arrive.
- **Citations:** W1:L3; D5f, P3

### P3a. Holiday calendar

- **Date / step:** 2026-10-27, Day 2 / pre-freeze
- **Type:** Parameter ruling (refines P3)
- **Decision:** For `EXPEDITE_RESPONSE_SLA`, the holidays that are not business days are the client's observed company holidays. US federal holidays are the provisional default.
- **Assumption:** The calendar is labelled an assumption, alongside the Eastern Time assumption, because the client's location was never stated in discovery.
- **Open dependency:** the COO confirms the company holiday list (D11). No further round with the claims lead is needed, because the holiday rule was accepted at W2:L4.
- **Rejected options:** (a) Leave "public holidays" undefined.
- **Rationale:** The SLA cannot be measured without a defined calendar. The company's own holidays are what the team actually observes, and the federal list is a stated placeholder until they are confirmed.
- **Citations:** W1:L3, W2:L4; P3

---

## Pre-v1 rulings (Day 2): design-doc alignment, document checklist, eval design

Rulings given on 2026-10-27, before requirements v1 is written. Each
decision is the consultant's, recorded as given. Before logging, Claude
raised three conflicts and the consultant resolved them:

- **1.1:** align the always-escalate row by trigger, rather than removing the backup outright.
- **4:** the loss case tests escalation under G1, not a "rejected" outcome.
- **3b:** a rule for setting each sample case's decision moment from the released data.

The rejected options for G14, G15, G16, G18, E5a, EV1 and EV2, and the
rationale for G16, G18, EV1 and EV2, were drafted by Claude and confirmed by
the consultant without edits on 2026-10-27. The same day the consultant
approved the G17 schema, approved the constructed cases K01–K08, added K09
(EV3a), and asked for the future-state swimlane to be aligned to G14.

**Principle (applies to G14–G18):** contradictions between the rulings and
the design docs are ruled on here, and the design docs are updated to
match. Requirements v1 cites rulings and does not resolve contradictions
inline. **Rejected:** resolving them inline in v1, which would put the
reasoning in the wrong place and leave the repo contradicting itself.

### G14. Always-escalate operations aligned by trigger

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Design-doc alignment
- **Aligns:** `scope-table.md` "Operations by tier", always-escalate row, with G7c, G7d, G7f, P3
- **Decision:** The row is split by trigger:
  - **Expedite request:** the specialist working the claim answers; if no one is, the claims lead assigns it or answers. The claims lead owns the on-time answer. No named backup. Response time: `EXPEDITE_RESPONSE_SLA` (G7f, P3).
  - **Reefer/temperature:** the claims lead, with the senior specialist as backup. Picked up the same day as receipt (G7c, G7d).
  - **Other escalations** (loss, cold-chain, above the deductible): the claims lead, with the senior specialist as backup. No response-time target in v1 (G7c, G7d).
- **Rejected options:** (a) Remove the senior-specialist backup from every escalation. That would revise G7c and G7f and reopen 72-hour reefer coverage (T2:L44).
- **Rationale:** G7f changed ownership and timing for expedite requests only, and kept G7c's backup for every other escalation. The row has to show both.
- **Citations:** T2:L44; G7c, G7d, G7f, P3

### G15. Expedite rulings carried into the design docs

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Design-doc alignment
- **Decision:** `decision-tree.md` and `scope-table.md` carry G7f, D5e, D5f, D5g and P3/P3a. No routing change: expedite requests still always escalate (R3, T3).
- **Rejected options:** (a) Leave them in the decisions log only.
- **Rationale:** The scope table and the decision tree are the design references that v1 cites, so they must not contradict the log.
- **Citations:** G7f, D5e, D5f, D5g, P3, P3a

### G16. G8a clean-POD clause superseded by E6a

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Supersession record
- **Decision:** G8a's clause "For a shortage with a clean POD, the agent marks the claim 'do not file' (E6) instead of preparing a package, and the specialist confirms" is superseded by E6a. The clause is marked superseded in G8a and is not deleted. The rest of G8a stands.
- **Rejected options:** (a) Delete the clause. (b) Leave G8a unmarked.
- **Rationale:** The log keeps originals. A visible marker stops v1 or the agent from reintroducing a reversed rule.
- **Citations:** G8a, E6, E6a; Q18

### G17. Agent output carries one field per G11 gate

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Design ruling (schema)
- **Decision:** G11 governs. The single `confidence` field in the agent output is replaced by one field per G11 gate, named to match G11. The output schema in `CLAUDE.md` and `.claude/skills/claims-agent/SKILL.md` is updated accordingly. **Status:** approved by the consultant on 2026-10-27 and applied to `CLAUDE.md`. `SKILL.md` does not exist yet; it is built from v1 with this schema.
- **Schema:** `decision` (`approve` | `partial` | `deny` | null), `rule_applied` (rule-table step or scope-table row), `rubric_score` (0–1; G11 gate 1, fixed checklist), `self_reported_confidence` (0–1; G11 gate 2), `route` (`autonomous` | `sign_off` | `escalate` | null), `rationale`. On a hold, `route` is null and the hold status field (G18) is defined in v1. On escalate, `decision` is null, with no amount (G7b). P1 becomes `RUBRIC_SCORE_THRESHOLD` and `SELF_REPORTED_CONFIDENCE_THRESHOLD`.
- **Rejected options:** (a) Keep one combined `confidence` field (G11 rejected combining the two signals).
- **Rationale:** G11 requires each signal to pass its own threshold. A single field cannot show which gate failed.
- **Citations:** G11, P1

### G18. Hold status field: defined in v1

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Scope record
- **Decision:** This is not an inconsistency: G3a deferred the hold status field to v1. v1 will define it as the hold reason, the reminders sent, and the fallback date. It is not defined in the design docs.
- **Rejected options:** (a) Define it in the design docs first.
- **Rationale:** G3a placed the definition in v1. Defining it twice would create a second source.
- **Citations:** G3a, E5, P2

### E5a. "Documents complete": required checklist by claim type

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Design ruling
- **Refines:** E5 (structured checklist), C5b (documents complete as a precondition)
- **Decision:**

  | Claim type | Required |
  |---|---|
  | Damage | Photos, invoice, BOL, delivery receipt/POD |
  | Shortage | Invoice, BOL, delivery receipt/POD; photos optional |
  | Reefer/temperature | The damage or shortage list, plus the temperature download (T2:L44) |
  | Loss | Out of the agent pilot (S1) |

  The agent applies this checklist, not a historical completion date. The historical date reflects past practice, not this rule.
- **"Photos optional for shortage":** the consultant's ruling, based on observed practice (for example, NLC-26-0052). Of the shortage claims with a completion date, 68 of 104 (65%) have photos missing, against 5 of 196 (3%) for damage (Q20). **Data-quality caveat:** IT has no answer on which field is authoritative. The document flags show status at extract, not at receipt, and IT does not check that they agree with the completion date (release 2 §4 Q1; Q13). The observed practice is therefore indicative only.
- **Rejected options:** (a) Use the historical completion date as "documents complete". (b) Require photos for shortages.
- **Rationale:** The claims lead's own list for a damage claim is photos, invoice, bill of lading and delivery receipt (T2:L18). For a shortage, photos of missing goods show little, and the team already treats shortage files as complete without them (Q20). Temperature claims cannot be judged from photos, and the download is the evidence (T2:L44).
- **Citations:** T2:L18, T2:L44; Q13, Q20; release 2 §4 Q1; E5, C5b, S1

### EV1. Eval decision moments: two snapshots, hindsight rule

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Eval design ruling
- **Decision:** Every eval case is evaluated at two moments:
  - **(a) Intake.** The expected outcome is the hold (state, no route; G3a) or escalate. The reefer rule is tested here (T2:L58).
  - **(b) Decision point.** The document-completion moment under the E5a checklist (see EV2). If documents never complete, the snapshot is taken at `FALLBACK_DEADLINE_DAYS`, where the expected route is human sign-off (C5b), unless a higher tier applies (G2).
  - **Hindsight rule:** each snapshot contains only what was knowable at that moment. No outcome, payment date or recovery, and no documents received later. This rule is stated in the eval README.
  - **Cost:** before any run, Claude states the estimated cost for 2 snapshots × all cases × 2 models.
- **Rejected options:** (a) A single snapshot at the decision point, which would leave the intake rules (hold, reefer) untested. (b) Snapshots built from the full historical record.
- **Rationale:** The routing rules fire at two different moments. Testing both is the only way to check the hold and the intake escalations. Hindsight would leak the outcome into the input.
- **Citations:** T2:L58; G2, G3a, C5b, P2, E5a

### EV2. Setting the decision point for sample cases

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Eval design ruling
- **Refines:** EV1(b)
- **Decision:** A sample case's decision point is its historical completion date, but only if every E5a checklist item for its claim type is flagged as received. The delivery receipt/POD is treated as received when that date is set, because no flag exists for it. Otherwise the documents never complete, and the decision-point snapshot is taken at `FALLBACK_DEADLINE_DAYS` (day 14). Each case records which rule set its moment.
- **Rejected options:** (a) Exclude claims whose flags and completion date disagree. (b) Set each case's moment by hand.
- **Rationale:** The release has no per-document dates and no delivery-receipt flag (release 2 §4 Q4), and the flags and the date can disagree (Q20). A fixed, recorded rule keeps the snapshots reproducible and keeps the full sample.
- **Citations:** Q20; release 2 §4 Q1, Q4; E5a, P2

### EV3. Must-escalate coverage: constructed cases

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Eval design ruling
- **Decision:** A small set of consultant-built synthetic cases is added to the eval set, each labelled `constructed` in a `source` field, with one or two cases per check:
  - **Always escalate:** cold-chain customer, expedite request, above the deductible.
  - **Human sign-off:** invoice mismatch, outside the filing window, possible duplicate.
  - **Routing boundary:** one claim between $10k and the deductible.
  - **Out of scope:** one loss claim. Expected: escalate at step 0, with no decision (G1, S1).
  - **Expected outcomes:** the consultant writes them from requirements v1, before any run. Claude prepares the case inputs only, with the expected-outcome fields blank.
  - **Reporting:** results are reported in two groups, sample and constructed, and never combined into one headline. The report states that constructed cases test rule coverage, not real-world frequency.
- **Rejected options:** (a) Accept the gap: with only reefer testable, the 100% escalation-correctness target cannot be verified.
- **Rationale:** The released sample contains no cold-chain, expedite, above-deductible, loss, duplicate, invoice or filing-window inputs (`analysis/eval-sample-triggers.md`).
- **Citations:** G1, S1; `analysis/eval-sample-triggers.md`

### EV3a. Constructed cases K01–K09

- **Date / step:** 2026-10-27, Day 2 / pre-v1
- **Type:** Eval design ruling
- **Refines:** EV3
- **Decision:** The constructed cases are K01–K08 as proposed, plus K09: a temperature allegation without a reefer flag, which tests G5's second signal. Each case starts from a clean claim in release 1, outside the sample (approved, documents complete, not reefer, not decided by an account manager), and changes one input, so amounts come from the data. Case inputs are in `spike/constructed-cases.md`. The consultant sets the inputs marked as theirs and writes every expected outcome from v1.
- **Rejected options:** (a) Leave G5's allegation signal untested; the sample tests `reefer_flag` only. (b) Invent amounts for constructed cases.
- **Rationale:** One change per base claim isolates the rule under test. Basing cases on released claims keeps every amount sourced (ground rule 2).
- **Citations:** G5; EV3; `analysis/eval-sample-triggers.md`
- **Wording:** rejected options and rationale drafted by Claude and confirmed by the consultant without edits on 2026-10-27.

---

## v1 freeze blockers (Day 2): G19–G23, EV4–EV7

Claude's review of requirements v1 found six blockers and three optional
fixes. Claude drafted recommended rulings with exact edits
(`engagement/03-requirements/v1-blocker-fixes.md`). The consultant approved
all nine without edits on 2026-10-27, and they were applied to v1, the
expected outcomes and the constructed cases.

### G19. Re-evaluation re-runs the tree from step 0

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Design ruling
- **Refines:** G10a
- **Decision:** Every re-evaluation (documents arrive, new information) re-runs the decision tree from step 0.
- **Rejected options:** (a) Re-run from step 3.
- **Rationale:** A step-1 trigger can first appear in late documents, such as a temperature allegation or an amount above the deductible. Re-running from step 3 would miss it.
- **Citations:** G2, G10a; v1 `stories.md` US-06, `edge-cases.md` EC6

### G20. An expedite request is a persistent trigger

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Design ruling
- **Refines:** R3, E4
- **Decision:** Once made, an expedite request is a step-1 trigger on every later evaluation, whether or not it has been answered. Answering it closes the SLA clock only.
- **Rejected options:** (a) R3 fires only while the request is open.
- **Rationale:** The claim stays escalated anyway (G10b). A trigger that disappears when the request is answered would change `rule_applied` and `triggers` without any change in risk.
- **Citations:** G10b, P3; K02

### G21. Step-1 trigger after an autonomous decision escalates

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Design ruling
- **Refines:** G10a
- **Decision:** New information after an autonomous decision sends the claim to sign-off, unless the re-run fires a step-1 trigger, in which case the claim escalates. An expedite request after an autonomous decision escalates (R3).
- **Rejected options:** (a) Always sign-off after an autonomous decision.
- **Rationale:** The higher tier wins (G2), and re-routing goes only up (G10a). Sign-off would put an expedite request below its own always-escalate rule (R3, E4).
- **Citations:** G2, G10a, R3, E4; v1 `edge-cases.md` EC25

### G22. Loss claims: step-1 triggers evaluated for the fact pack

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Design ruling
- **Refines:** G1, G7d
- **Decision:** A loss claim still escalates at step 0 (`rule_applied` = R16) with no decision. Step-1 triggers are still evaluated and listed in `triggers` and the fact pack, without changing the route. If R1 is among them, the claim is handled as a reefer/temperature escalation: picked up on the day of receipt, with the 72-hour download clock.
- **Rejected options:** (a) Skip step 1 for loss claims.
- **Rationale:** Skipping step 1 would lose the 72-hour download window on a reefer loss claim.
- **Citations:** T2:L44; G1, G7d; v1 `edge-cases.md` EC5

### G23. Agent input schema in v1

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Design ruling
- **Decision:** `rules.md` gains an "Agent input" table listing what the agent receives at each evaluation, limited to what is known at the evaluation time. It includes the claim fields, `claim_text`, the documents with their content and dates, `shipment_record`, other claims on the same shipment, the cold-chain list, expedite requests, the current state, payment and withdrawal.
- **Rejected options:** (a) Leave the inputs implicit.
- **Rationale:** Without it, an engineer cannot build the agent without guessing, and RB1, R7, R2 and R3 have no stated data source.
- **Citations:** G13, G18, EV1; release 2 §2

### EV4. K01 uses a constructed customer ID

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Eval design ruling
- **Refines:** EV3a
- **Decision:** K01 uses customer `C-K01`, which no released claim uses. The eval cold-chain list is `["C-K01"]` only.
- **Rejected options:** (a) Keep C010.
- **Rationale:** Sample case NLC-26-0016 is also customer C010, so keeping it would force a sample case to escalate under R2.
- **Citations:** EV3a; `spike/constructed-cases.md`

### EV5. K06: the earlier claim is open, not paid

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Eval design ruling
- **Refines:** EV3a
- **Decision:** K06 shares `shipment_ref` SHP-0001 with NLC-26-0001, which is open, not paid, at both K06 snapshots. There is no prior-payment input. R7 fires under the "paid or open" duplicate definition.
- **Rejected options:** (a) Keep `prior_payment_same_shipment` = Y.
- **Rationale:** NLC-26-0001 was paid on 2026-04-09, after both K06 snapshots, so a prior-payment input would break the hindsight rule (EV1).
- **Citations:** EV1, EV3a

### EV6. Sample eval assumptions labelled

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Eval design ruling
- **Decision:** The expected outcomes state that no sample case has a cold-chain customer, a temperature allegation or an expedite request, and that the eval cold-chain list is `["C-K01"]`.
- **Rejected options:** (a) Leave the assumption implicit.
- **Rationale:** None of these inputs is held in the released data (release 2 §2), so the sample expectations rest on an assumption that must be visible.
- **Citations:** release 2 §2; EV4

### EV7. R10 or R13 accepted where the draft decision sets the row

- **Date / step:** 2026-10-27, Day 2 / v1 freeze
- **Type:** Eval design ruling
- **Decision:** For NLC-26-0231 and K07 (claimed amount above $10,000), `rule_applied` is scored as correct if it is R13, or R10 when the agent drafts a denial.
- **Rejected options:** (a) Expect R13 only.
- **Rationale:** Step 5 sends a denial to R10 before step 6 is reached. The route (sign-off) is the same either way.
- **Citations:** v1 `rules.md` rule table

---

## v1 values (Day 2): V1–V24, E-a to E-d

Values Claude proposed while drafting requirements v1 with the consultant
(`engagement/03-requirements/v1-draft-notes.md`). The consultant approved
all of them on 2026-10-27, with two corrections from Claude's review:

- **V2:** the comparison figure is 16–19 days for the same customers (20 across all other claims), from Q21, not "19–20".
- **V22:** the basis cites W2:L2, and v1 `README.md` no longer says the team has no such title.

IDs are kept as given. Where the table says "Unset", that is the option
rejected: leaving the value open and letting the engineer choose.

| ID | Decision (as stated in v1) | Rejected | Rationale | Citations |
|---|---|---|---|---|
| V1 | Hold status field: `hold_reason`, `missing_items`, `reminders_sent`, `fallback_date`, `duplicate_flag` | G18's three fields only | Reminders need the missing items, and G13's intake flag needs a field | G3a, G13, G18 |
| V2 | `FILING_WINDOW_DAYS` = 270 calendar days, delivery to receipt, all customers (assumption A5). Raised as D13 | Derive a window from the denials | No single threshold reproduces the 12 historical denials on any date basis (Q21). The window may vary by contract or was applied inconsistently | Q14, Q21 |
| V3 | K02 request time 2026-03-11 15:30 ET, while the claim is held | — | Tests up-only re-routing (G10a) and the after-14:00 SLA path | G10a, P3 |
| V4 | K04 invoice amount 3,406.70 (80% of claimed) | — | An unambiguous mismatch | R8 |
| V5 | K05 `delivered_at` = 2025-05-31 (276 days to receipt) | Move the receipt date | Keeps the released document dates | A5 |
| V6 | K09 allegation wording as in the expected outcomes | — | States an excursion without the word "reefer" | G5 |
| V7 | Rubric checklist RB1–RB6 | Unset | G11 left the checklist to v1 | G11 |
| V8 | `RUBRIC_SCORE_THRESHOLD` = 1.00 for the pilot | A partial-pass threshold | An all-pass checklist gate is clearest | G11, P1 |
| V9 | `SELF_REPORTED_CONFIDENCE_THRESHOLD` = 0.80, provisional; recalibrated from the eval | Unset | A starting value is needed to run the eval | G11, P1 |
| V10 | Reminders on days 3, 7 and 11; the day-11 reminder states the fallback date | Unset | E5 automates reminders but set no cadence | E5, P2 |
| V11 | "End of business day" = 17:00 ET | Unset | P3 named no time | P3 |
| V12 | Expedite request on a non-business day: due 12:00 the next business day | Unset | P3 covers business days only | P3, P3a |
| V13 | Fallback check at 23:59 ET on the fallback date | Unset | P2 said "day 14" without a time | P2 |
| V14 | Invoice mismatch: claimed amount above the invoice value, to the cent, or invoice unreadable | Any difference | A claim may cover part of a shipment | C5c |
| V15 | Possible duplicate: same `shipment_ref`, other claim paid or open | Paid only | An open claim on the same shipment can still be paid twice | C5c, G13; T2:L68 |
| V16 | Temperature allegation: any excursion statement; if unsure, treat it as one | Literal keywords only | The cautious reading protects the 72-hour window | G5; T2:L44 |
| V17 | Cold-chain identification: a list of customer IDs kept by the claims lead; no go-live with an empty list (D12) | Infer from customer names | IT holds no contract terms | C5c; T2:L44; release 2 §2 |
| V18 | Missing delivery date: treated as outside the filing window (R9) | Treat as inside | The cautious reading sends the claim to a person | R9 |
| V19 | Carrier filing on incomplete documents: no package; the person may file manually | Package anyway | "With evidence" needs documents | G8a, E6a |
| V20 | Autonomous reviewer: a specialist designated by the claims lead | Unset | G8b left the reviewer open | G8b |
| V21 | Insurer consent recorded by the claims lead | Unset | G9b left it open; the claims lead works claims above the deductible | G9b, G7c |
| V22 | Senior specialist: a designation within the specialist team, named by the claims lead | Unset | G7c names the role without defining it | G7c; W2:L2 |
| V23 | Output fields beyond G17: `claim_id`, `status`, `amount`, `triggers`, `rubric_items`, `hold`, `fact_pack` | G17's six fields only | Six fields cannot carry the hold, the fact pack or which rubric item failed | G17, G18, G7b |
| V24 | New dependency IDs: D12 (cold-chain list), D13 (filing-window rule) | — | Not in the index | V2, V17 |
| E-a | `autonomous*` scoring: autonomous, or sign-off via R14, both count; R14 reported as "gate-held" | Score autonomous only | The confidence thresholds are uncalibrated | G11, P1 |
| E-b | The decision is not scored on sign-off | Score the draft decision | The draft is not a routing outcome | G7a |
| E-c | 8 "info gap" sample cases reported separately | Fold into the headline | Their snapshots lack the evidence behind the historical outcome | EV1 |
| E-d | `invoice_amount` = `amount_claimed` for sample snapshots, labelled an assumption | Leave blank | IT holds no invoice values; otherwise R8 fires on every sample case | release 2 §2 |

---

## Spike design (Day 2): EV8–EV13

Rulings given on 2026-10-27, after the claims-agent Skill and harness were
built and before any model run. Each decision is the consultant's, recorded
as given. **Wording:** the rejected options and rationale marked *(drafted)*
were drafted by Claude and await the consultant's confirmation.

### EV8. Spike models: Sonnet 5.5 against Haiku 5.5, effort pinned

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Spike design ruling
- **Decision:** The spike compares `claude-sonnet-5-5` with `claude-haiku-5-5`. Opus 5.5 is used only if Sonnet fails. Effort is pinned explicitly to the same level on both models, not left at each model's default, and is recorded in `spike/results.md`. The price table in `spike/run_eval.py` cites its source.
- **Level:** `medium` on both models (consultant, 2026-10-27).
- **Rejected options:** *(drafted)* (a) Opus 5.5 against Sonnet 5.5. (b) Each model at its default effort.
- **Rationale:** Routing is mostly rule application, so the question is whether the cheaper model routes correctly. Unpinned effort would compare two models at two different thinking budgets.
- **Citations:** ground rule 9; `spike/run_eval.py` (`PRICES`)

### EV9. Unheld fields sent as null; headline is routing on escalate, hold and sign-off

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Eval design ruling
- **Refines:** E-a, EV6
- **Decision:**
  - `claim_text` (except K09), `shipment_record` and the content of photos, BOL and POD are sent as null.
  - Gate-held (R14) cases are reported as their own line and excluded from the headline pass rate. The headline is routing correctness on escalate, hold and sign-off snapshots.
  - The report states plainly that the autonomous tier is untested on released data, because document content is not held.
  - Any escalation caused by a null `claim_text` under "if unsure, treat it as an allegation" is logged as a v2 gap (v1 does not say what missing claim text means), not as a harness bug.
- **Rejected options:** *(drafted)* (a) Fill the unheld fields with text built from the held fields. (b) Keep autonomous* snapshots in the headline.
- **Rationale:** *(drafted)* Null tests v1 as written and invents no claim content. With no document content, the rubric cannot pass, so autonomous* results measure missing data rather than routing.
- **Citations:** release 2 §2; E-a, EV6; v1 `rules.md` (temperature allegation)

### EV10. Harness snapshot conventions accepted

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Eval design ruling
- **Decision:** Accepted as built: intake at 09:00 ET and the documents check at 12:00 ET; `current_state` at the decision point carried from the intake result; fallback snapshots list flagged items without a date and the POD as missing. `spike/README.md` carries a caveat: the flags show status at extract, so a fallback snapshot may show a document as received that arrived after day 14. No expected outcome changes, because the POD is missing and the claim routes to R6 either way.
- **Rejected options:** *(drafted)* (a) Fallback snapshots with no documents listed. (b) `current_state` reset to new at every snapshot.
- **Rationale:** *(drafted)* The release holds dates only and no per-document dates (release 2 §4 Q4). Fixed, recorded conventions keep the snapshots reproducible.
- **Citations:** EV1, EV2; release 2 §4 Q1, Q4; `spike/README.md`

### EV11. No refusal fallback; refusals are their own failure category

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Spike design ruling
- **Decision:** The server-side refusal fallback stays off. A refusal counts as a failure, reported as its own category, separate from a wrong route.
- **Rejected options:** *(drafted)* (a) Enable the fallback to another model.
- **Rationale:** *(drafted)* A fallback would answer some snapshots with a different model and mix two models into one model's results.
- **Citations:** EV8

### EV12. Smoke test before the full run

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Spike design ruling
- **Decision:** Before the full run, a smoke test on both models with three snapshots: K04/decision_point, NLC-26-0016/decision_point and K09/intake. Every output is validated against the v1 output schema. Measured input, cached and output tokens are reported per call. The full-run estimate is made from the measured numbers (snapshots × models × measured cost). The hard spend limit on the key stays. The full run waits for the consultant's approval.
- **Rejected options:** *(drafted)* (a) Estimate from an assumed output size. (b) Go straight to the full run.
- **Rationale:** *(drafted)* Output size, including thinking tokens, is unknown until measured. Three snapshots cover sign-off, autonomous* and escalate paths at small cost.
- **Citations:** ground rule 8; EV1; NF-16

### EV13. Expected outcomes marked approved and committed before any run

- **Date / step:** 2026-10-27, Day 2 / spike design
- **Type:** Process ruling
- **Decision:** The "(draft for consultant review)" label on `spike/expected-outcomes-v1.md` is removed only after V1–V24 and E-a to E-d are logged in this file, and replaced with "approved [date]". The approved file is committed before any run, the smoke test included.
- **Rejected options:** *(drafted)* (a) Remove the label at once.
- **Rationale:** *(drafted)* EV1 requires expected outcomes written before any run. A committed, approved file shows they were not changed after seeing results.
- **Citations:** EV1
