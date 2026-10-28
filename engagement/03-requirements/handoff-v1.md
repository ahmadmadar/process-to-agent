# Cold-FDE Handoff Test: Requirements v1

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

**Run:** 2026-10-27, against tag `requirements-v1` · **Model:** Sonnet (fresh subagent) ·
**Access:** Read only, limited to the five files in `engagement/03-requirements/v1/`.

**Prompt (CLAUDE.md):** "You are the engineer building this agent. List every question
you would need the business to answer before you could build it without guessing."
Format instructions added: group by area, number Q1…, give Ref and "Why it blocks",
business questions only, end with a total.

The subagent's output follows unedited. The consultant classifies each question as a
real gap or noise; Claude has not pre-classified them.

---

## Inputs and data availability

**Q1.** What is the format and source of `shipment_record` (items and quantities shipped), and what should the agent do when it is null? Does a null record automatically fail RB1 (which blocks autonomous)?
Ref: rules.md, Agent input (`shipment_record`), RB1
Why it blocks: I would have to guess whether a missing shipment record means RB1 fails, is skipped, or counts as pass.

**Q2.** How is "documents received" decided: does the presence of a document of the right type count, or must its content be legible/valid (e.g. a blurry photo, an unsigned BOL, a POD for a different shipment)? Who or what judges that?
Ref: rules.md, "Documents complete (step 2)"; Agent input `documents`
Why it blocks: I would have to guess the bar for "received", which controls hold vs. release and therefore every downstream route.

**Q3.** For a damage claim, how many photos or what quality counts as "Photos" being received? Does one photo satisfy the checklist item?
Ref: rules.md, Documents complete table (Damage row); RB2
Why it blocks: I would have to guess the minimum that ends the hold.

**Q4.** How does the agent determine `claim_type` and a "temperature allegation" when the claim text is the only source: is `claim_type` always supplied by intake, or must the agent classify the claim from text (e.g. damage vs. loss vs. shortage)? If a customer calls a missing shipment "short", who decides loss vs. shortage?
Ref: rules.md, Agent input (`claim_type`), Step 0
Why it blocks: Step 0 sends loss claims to escalate with no decision, so I would have to guess the boundary between shortage and loss.

**Q5.** What is the exact definition of the delivery date and receipt date used for the filing window and fallback date (delivery per POD vs. carrier scan; receipt date as the date the claim arrives vs. the date the claim is complete)? Does receipt after 23:59 or on a non-business day roll to the next day?
Ref: rules.md, Outside the filing window; Fallback date; Agent input
Why it blocks: A one-day difference changes R9 and the fallback date, so I would have to guess the date convention.

**Q6.** What counts as the "same `shipment_ref`" for duplicate matching (exact string match, normalised case/whitespace, multiple refs per shipment, partial-shipment claims by different consignees)? Is a claim with the same shipment_ref but different goods still a duplicate?
Ref: rules.md, Possible duplicate; Agent input `other_claims_same_shipment`
Why it blocks: I would have to guess match strictness; false positives push claims to sign-off and false negatives risk duplicate payments.

**Q7.** How does the agent identify the "invoice amount for the claimed goods" when an invoice covers multiple line items and the claim covers some of them (which line items, including freight, tax, discounts)? Which amount is compared to the cent?
Ref: rules.md, Invoice mismatch; RB3; edge-cases EC16
Why it blocks: I would have to guess how to derive the invoice value of just the claimed goods and whether tax/freight are included.

**Q8.** What currency and rounding rules apply to `amount_claimed` and `amount`? The README says no currency is recorded, but what if invoices arrive in another currency?
Ref: README, Conventions; rules.md Invoice mismatch
Why it blocks: Thresholds ($10,000/$25,000) and the to-the-cent comparison depend on one currency; I would have to guess what to do with foreign-currency invoices.

## Routing rules and precedence

**Q9.** Does the claimed amount for threshold purposes include multiple claims on the same shipment/customer (aggregation), or is every claim evaluated in isolation? Can a customer split a $40,000 loss into several claims under $10,000 or $25,000?
Ref: rules.md, Glossary (claimed amount), R4, R15
Why it blocks: I would have to guess whether split-claim avoidance of the deductible or autonomous line must be detected.

**Q10.** What is the autonomous-tier amount in the case of a `partial` on an escalated or sign-off claim: how should the agent compute `amount` (the proposed payout) for partial and approve decisions? What rules reduce an approval (salvage, depreciation, limits of liability, per-pound caps, contract terms)? Where do those figures come from?
Ref: rules.md, Agent output (`amount`); RB4; edge-cases EC15
Why it blocks: The requirements say the agent proposes a payout but give no valuation or limit-of-liability rules, so I would have to invent them.

**Q11.** What are the business criteria for `approve`, `partial` and `deny`? What makes a claim deniable beyond the filing window (e.g. no evidence, carrier-caused vs. customer-caused, excluded goods, contract exclusions, missing POD exception)? Is a clean POD a reason to deny or reduce a shortage claim?
Ref: rules.md, Step 4 and Step 5; edge-cases EC30
Why it blocks: Step 4 says the agent "forms a decision" but no decision criteria are given, so I would have to guess the adjudication logic.

**Q12.** What does a POD exception (`pod_exception` = true) do in the rules? It is an input, but no rule or rubric item uses it.
Ref: rules.md, Agent input (`pod_exception`); Glossary (clean POD)
Why it blocks: I would have to guess whether it affects the decision, RB5, RB4, or routing.

**Q13.** When R6 sends a claim to sign-off at the fallback date with incomplete documents, may the agent's draft recommend approve? Does it route to the $10,000 specialist/lead split on claimed amount? And what happens when an incomplete-document claim at the fallback date also has a step-3 flag or a step-1 trigger?
Ref: rules.md, Step 2 fallback; US-06
Why it blocks: Precedence for combined cases is implied but not stated for the draft's allowed decisions, so I would have to guess.

**Q14.** What `rule_applied` and `triggers` values should be output when a claim reaches step 4 and ends in sign-off because of both a denial and a failed gate (R10 vs. R14), or a partial above $10,000 (R11 vs. R13), or deny with amount > $10,000 (R10 vs. R13)? "First row that fired" at step 3 is stated, but not for steps 5-6.
Ref: rules.md, Precedence; Rule table steps 5-6; Agent output (`rule_applied`)
Why it blocks: Eval scoring and the trace depend on one deterministic `rule_applied`, and I would have to guess the ordering across steps 5-6.

**Q15.** Do step-3 flags (R7-R9) appear in `triggers` on a claim that is held (R5) when documents are incomplete? US-03 says the duplicate check runs at intake and sets `duplicate_flag`, but what about invoice mismatch and filing window while held (the invoice may not have arrived)?
Ref: rules.md, Precedence and Possible duplicate; US-03; Agent output (`triggers`)
Why it blocks: I would have to guess whether step-3 checks run during a hold.

**Q16.** Does the intake evaluation for a held claim output `rule_applied` = R5 only, or can the escalation triggers at step 1 be evaluated on later `documents_updated` events (e.g. a document reveals a temperature allegation)? Is a temperature allegation found in a document, not the claim text, in scope for step 1 re-evaluation?
Ref: rules.md, Temperature allegation definition; Re-routing table
Why it blocks: I would have to guess whether the agent must read all documents (including photos) for temperature allegations on every evaluation.

## Cold-chain list, expedite, and time

**Q17.** What are the customer IDs for Copperwick Foods, Asterholm Medical Supply and Pinehallow Gourmet, and how does the list get updated (who, how, effective from when for in-flight claims)? Until D12 is resolved, what should the agent do in test and eval?
Ref: README, D12; rules.md, Cold-chain list
Why it blocks: R2 cannot be evaluated or tested without the IDs, and the pilot is stated as not going live without them.

**Q18.** What is the list of company holidays (A4 assumes US federal holidays; D11 is open), and does it include observed days (e.g. a Saturday holiday observed on Friday)? Should the agent be supplied with a holiday calendar?
Ref: README, A3/A4/D11; rules.md, EXPEDITE_RESPONSE_SLA
Why it blocks: Due times for expedite answers depend on exact business days.

**Q19.** What exactly counts as an "answer" that closes the expedite SLA clock, and who has authority to record it? Does an answer need to contain all three elements (status, next step, expected date), and is "expected date where known" enforced by the system or by the person?
Ref: rules.md, Expedite requests table; US-15, US-16
Why it blocks: I would have to guess the validation the system applies before recording an answer as given.

**Q20.** How does the system know a claim's decision "has already been approved by the claims team" to permit a payment commitment in an expedite answer? Is it any sign-off approval by a person, or an autonomous approval, and does finance pre-approval or insurer consent also have to be done?
Ref: rules.md, "What the answer may say"; US-15; EC22
Why it blocks: The block logic for payment commitments depends on which state flags qualify, and I would have to guess them.

**Q21.** Who is "the specialist already working the claim" and how does the system know (assignment field, last touch, queue ownership)? What if the specialist is on leave when an expedite arrives?
Ref: rules.md, Expedite requests (Who answers); US-14
Why it blocks: Assignment logic needs a definition of "working", and no backup is named for expedite answers.

**Q22.** What happens to an expedite request made by someone who is not an account manager (customer, sales, executive), and how does the system verify the requester is an account manager and for which customers?
Ref: rules.md, Expedite request definition; README Roles
Why it blocks: I would have to guess whether other requesters trigger R3 or are ignored.

**Q23.** After an expedite escalation, what is the claim's lifecycle: does a claim that is held and later escalated by an expedite request keep its hold reminders running? Do reminders continue, and does the fallback release still fire (to sign-off) for an escalated claim?
Ref: rules.md, Expedite request; NF-10; US-14; EC21
Why it blocks: Hold and escalate interact (escalated claims are "never handed back"), and I would have to guess whether the hold clock keeps running.

## Confidence

**Q24.** How should RB3 and RB5 treat rounding, units of measure, and quantity-versus-value differences (e.g. 10 cases vs. 10 pallets)? What tolerance, if any, applies to "agree" on dates, quantities and references?
Ref: rules.md, Gate 1 RB3, RB5
Why it blocks: I would have to guess what "consistent" means, and with a threshold of 1.00 any ambiguity decides autonomous vs. sign-off.

**Q25.** How should the model produce `self_reported_confidence` (prompt wording, scale anchors, one number overall or per claim), and is the 0.80 threshold to be changed automatically by the eval or only by the consultant? Who approves a changed threshold, and is it versioned in the trace?
Ref: rules.md, Gate 2 and Thresholds; README P1
Why it blocks: I would have to guess whether the threshold is configuration, who may change it, and how changes are recorded.

**Q26.** Is `rubric_score` computed by the agent or by deterministic code from the items? If the model's reported score disagrees with the item results, which wins?
Ref: rules.md, Gate 1; Agent output
Why it blocks: I would have to guess where the arithmetic lives and how to resolve an inconsistency.

## Documents, hold and reminders

**Q27.** Through what channel are the day-0 checklist request and reminders sent (email, portal), to whom (customer contact on the claim), and using what template/wording? Who approves the customer-facing text?
Ref: rules.md, Parameters (checklist request); US-02, US-05
Why it blocks: I would have to guess the recipient, channel and content of customer communications.

**Q28.** Is the day-0 checklist request sent for claims that escalate at intake (the US-02 wording says "non-escalated")? Do escalated claims get document requests at all, and from whom?
Ref: US-02; rules.md, Parameters; fact pack `checklist_status`
Why it blocks: The fact pack reports missing documents, but nobody is said to request them, so I would have to guess.

**Q29.** Are reminder days 3, 7, 11 and the fallback (14) calendar days counted from the receipt date regardless of weekends and holidays? What if a reminder day falls on a non-business day: send anyway or shift?
Ref: rules.md, REMINDER_DAYS; FALLBACK_DEADLINE_DAYS
Why it blocks: I would have to guess whether reminders follow calendar or business days.

**Q30.** If a customer asks for an extension or says documents are coming (a human-entered note), can the hold or fallback date be extended? Who may extend, and does the agent honour it?
Ref: rules.md, Fallback date; "Documents complete" ("not any completion date entered by a person")
Why it blocks: I would have to guess whether any override of the fixed 14-day deadline exists.

**Q31.** On a claim re-run via `fallback_check`, what if documents are complete at 23:59 but a new flag appears at the same instant? Is the 23:59 check driven by a scheduler the business provides, and what timezone and daylight-saving handling applies (e.g. 23:59 ET on a DST switch day)?
Ref: rules.md, Fallback date; Agent input `event`
Why it blocks: I would have to guess scheduler ownership and DST behaviour for deadline checks.

## Sign-off, queues and people

**Q32.** Who are the specific people or queues behind "specialists' queue", "claims lead", "senior specialist" and "autonomous reviewer", and how is the senior specialist designation recorded in the system? What is the backup when both the claims lead and the senior specialist are unavailable on a reefer day-of-receipt claim?
Ref: README, Roles; US-13
Why it blocks: Assignment and backup logic needs named roles or identifiers, and the day-of-receipt service level has no fallback beyond the senior specialist.

**Q33.** What defines "unavailable" for the claims lead (leave, dispatch duty, off-shift) and who sets it?
Ref: README, Roles (Senior specialist); Risk row
Why it blocks: Backup routing triggers on unavailability, and I would have to guess the signal.

**Q34.** How do queue ordering rules combine: key-account first, then by what (age, amount, expedite due time, reefer clock)?
Ref: rules.md, key-account queue priority; US-12
Why it blocks: Only the first sort key is given, so I would have to guess the rest.

**Q35.** What is the content, tone and approval standard of the customer letter (approval, partial, denial), and is a denial letter or partial letter drafted by the agent allowed to state reasons or legal/contract references? Any mandatory wording?
Ref: rules.md, Operations by tier; US-10, US-12; After the decision (denial)
Why it blocks: Letters go to customers (autonomously for approvals) and I have no approved content or legal wording.

**Q36.** What must a reason for an override or an autonomous-review disagreement contain (free text, coded list)? Is there a list of reason codes the business wants for reporting?
Ref: US-11, US-12; NF-05, NF-06
Why it blocks: I would have to guess the data structure, and the miss-report data needs are said to be recorded but not specified.

**Q37.** What happens when the autonomous reviewer disagrees with a decision after payment has been issued? Is there a recall, clawback, or reopen step, and does the claim move to sign-off?
Ref: US-11; README Roles (Autonomous reviewer); rules.md "New information after an autonomous decision"
Why it blocks: Disagreement has no stated consequence, so I would have to guess whether it triggers any workflow.

## Payment, insurer, carrier filing

**Q38.** How does the agent send the payment instruction (to what finance system or queue, with which fields: payee, bank reference, amount, claim ID)? Who is the payee and where do payee details come from?
Ref: rules.md, Operations by tier; US-10, US-18
Why it blocks: The payment instruction content and destination are unspecified, and integration is out of scope, so I need the expected payload.

**Q39.** For approvals above $10,000, how does the agent know finance pre-approval has been granted before issuing the payment instruction, and what happens if finance rejects or edits the amount?
Ref: rules.md, After the decision; US-18
Why it blocks: The pre-approval outcome flow (reject, amend, timeout) is not described.

**Q40.** For a claim above the deductible, which claims-lead action ends the escalation (insurer consent recorded)? What happens if the insurer declines or consents only to a different amount, and is a denial above the deductible also subject to the consent gate?
Ref: rules.md, After the decision (Claimed amount > deductible); US-19; NF-08
Why it blocks: The consent gate is defined only for payment instructions, so I would have to guess what to do for denials and partial consent.

**Q41.** Is the deductible per claim, per shipment, per customer, or aggregate over a period? A1 says $25,000 on the claimed amount; does it erode as claims are paid?
Ref: README, Glossary (Deductible), A1, D1
Why it blocks: R4 compares each claim to a fixed figure; if the real deductible is aggregate, the rule is wrong.

**Q42.** What is the content and format of the carrier filing package, and which carrier is the target? How does the agent identify the carrier and its filing rules (the filing window and documents differ by carrier)?
Ref: rules.md, Step 7; US-10, US-20
Why it blocks: Carrier identity is not in the agent input, and no package contents are specified, so I would have to invent them.

**Q43.** The carrier filing package is prepared for every paid claim with documents complete: is it also prepared for claims paid after a person sign-off with a partial payout, and does a filing deadline for carriers exist that the agent should track?
Ref: rules.md, Step 7 and After the decision; US-20
Why it blocks: Partial payments and carrier time limits are not covered, and I would have to guess.

**Q44.** Who triggers step 7 and when: the `paid` field changes, or the payment instruction is issued? What event signals "claim paid" to the agent, as no `paid` event appears in the `event` enum?
Ref: rules.md, Agent input (`event`, `paid`); Step 7
Why it blocks: The event list has no payment event, so I would have to guess how step 7 is triggered.

## Re-routing, withdrawals and events

**Q45.** The "may move up a tier, never down" rule: how are tiers ranked relative to hold (hold is a state with no route)? Can a claim in sign-off with a person return to hold if a document is later found invalid? And what if new information would, on a clean re-run, lower the tier (e.g. an expedite request answered, a duplicate's earlier claim denied)?
Ref: rules.md, Re-routing; EC26; US-21
Why it blocks: EC26 says the duplicate flag re-checks at step 3 but "never down" appears to contradict removal of R7, so I would have to guess which governs.

**Q46.** For new information on a claim already with a person, does the agent still produce a new evaluation and trace record, and does it overwrite the draft, or only notify the person?
Ref: rules.md, Re-routing; US-21; NF-01
Why it blocks: Whether to re-run and re-draft on a person-owned claim is unspecified.

**Q47.** Customer withdraws after payment: sign-off for what purpose (recovery of the payment, closing the record)? What should the agent draft as the decision and amount?
Ref: rules.md, Re-routing (withdrawals); US-22; EC28
Why it blocks: A withdrawal after payment has no decision type among approve/partial/deny, so I would have to guess the draft content.

**Q48.** What happens on a withdrawal when an expedite request is open, or the claim is escalated (already with the claims lead)? Does `withdrawn` override escalate, and does the SLA clock stop?
Ref: rules.md, Re-routing; US-17
Why it blocks: Withdrawal precedence over escalation is only specified for held and unpaid claims.

**Q49.** After an autonomous decision (payment instruction issued), what is the exact step when new information arrives: is the payment instruction recalled, and who handles it?
Ref: rules.md, Re-routing (new info after autonomous); US-21
Why it blocks: The route changes but the already-sent payment instruction's fate is not stated.

## Outputs and notifications

**Q50.** Which amount does `amount` hold for `approve`: always the full claimed amount, or the claimed amount less any deductible/limit? Is `amount` null for sign-off drafts of `deny` and for R6 drafts with insufficient documents?
Ref: rules.md, Agent output (`amount`)
Why it blocks: Rules say amount is the proposed payout, but payout rules are not defined (see Q10).

**Q51.** What triggers the account manager notification for key-account claims: which account manager (per customer mapping), and what is "decided" (agent autonomous decision, sign-off approval, denial, or any final outcome)? What information may the notice include for a denial?
Ref: US-23; rules.md, After the decision
Why it blocks: Notification mapping and trigger point are unspecified.

**Q52.** What outcome notifications, if any, go to non-key-account customers beyond the letter, and does the customer receive any notice when a claim is escalated or held?
Ref: US-02, US-10, US-12
Why it blocks: Only certain communications are specified; I would have to guess the rest.

## Non-functional and data handling

**Q53.** What retention period, access control and audit-log review policy apply to trace records, edits/overrides, and PII within them? NF-03 requires inputs in the trace, but NF-17 limits PII sent to the model.
Ref: NF-01 to NF-04, NF-17
Why it blocks: Retention and access are business/compliance decisions I cannot assume.

**Q54.** What data-residency, hosting and model-provider restrictions apply to claim data (region, vendor approvals)?
Ref: NF-17, NF-18, README Out of scope (deployment)
Why it blocks: Which model endpoints and regions I may call depends on this and is not stated.

**Q55.** What volumes should the agent be sized for (claims per day, peak, evaluations per claim, concurrency), and what is the acceptable behaviour when the model call fails or times out? NF-15 says no latency or cost targets, but what is the failure mode for intake, given NF-14 requires reefer claims reach the lead on the day of receipt?
Ref: NF-14, NF-15
Why it blocks: I would have to guess the degraded-mode routing (e.g. escalate by default) when the model is unavailable.

**Q56.** In what language(s) will claim text and documents arrive, and are photos/attachments in scope for the agent to read (image analysis for RB2) or only text/metadata? How are documents supplied to the agent (as extracted text, images, or file links)?
Ref: rules.md, Agent input `documents`; RB2
Why it blocks: RB2 needs the agent to judge photos, and I would have to guess the document format and modality.

Total questions: 56

---

## Classification (consultant)

| Q | Real gap / noise | Note |
|---|---|---|
| | | |
