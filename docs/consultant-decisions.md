# Consultant decisions log

> Northline Freight is a fictional client. All people and data are synthetic.

Where the consultant overruled, corrected, or chose against Claude, and why.
Claude drafts entries; the consultant confirms the wording.

| Date | Day / step | Claude proposed | Consultant decided | Why |
|---|---|---|---|---|
| 2026-10-16 | Day 1 / workflow | Claude makes the commits; one branch per session with a PR at the end | One branch per session. The consultant does all git work in GitHub Desktop. Claude only drafts commit and PR text. Claude's commit on `main` was reversed and the changes moved to `day1/discovery`. | I prefer to own the version control. Keeps me honest and accountable about reviewing all the changes made by Claude throughout the session. |
| 2026-10-17 | Day 1 / SOW | Turn governance meetings that have no session in the plan into written steps, or reframe them as the consultant's rulings pending sponsor ratification | Kept the daily sponsor summary. Removed the Day 1 COO playback and the Day 3 COO/CFO readout. Accepted all other SOW fixes. | A short engagement benefits from daily visibility and clarity for the client; a longer one would use weekly summaries. The Day 3 CFO defence already covers the readout. |
| 2026-10-17 | Day 1 / data request | Keep the event log optional, with fallback fields in the claims table for H2 | Event log made required; fallback fields removed | A required event log reduces guessing on our end. |

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
