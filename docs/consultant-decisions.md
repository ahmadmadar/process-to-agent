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
| `CONFIDENCE_THRESHOLD` | C5c; autonomous tier (C5) | Unset; provisional value to be calibrated in the Day 2 eval | Day 2 |
| `FALLBACK_DEADLINE_DAYS` | C5b, E5 | Unset | Requirements v1 |

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
