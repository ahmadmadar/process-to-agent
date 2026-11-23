# Cold-FDE Handoff: Classification of the v1 Questions

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Classification of the 56 questions in [`handoff-v1.md`](handoff-v1.md), under rulings CF1–CF5 in `docs/consultant-decisions.md`. Line references are to the frozen v1 files (tag `requirements-v1`, `rules.md:L10` = `rules.md`, line 10), checked against the files. v1 is not edited; real gaps are resolved in v2.

## Criteria (CF1)

A question is a **REAL GAP** only if all of these hold:

1. v1 does not answer it unambiguously. If two competent engineers could build different behaviour from the text, it counts as a gap.
2. It is not already recorded as an assumption or open dependency with interim behaviour.
3. It is in scope.
4. Without an answer, any behaviour v1 requires would change: agent output, or a required system action (send, block, notify, record, prepare).
5. The business or the spec owner must answer it. Internal v1 defects count.

Labels: REAL GAP, AMBIGUOUS (lean real or lean noise), DUPLICATE, ALREADY KNOWN, OUT OF SCOPE, NOISE (answered by v1, or engineering choice). Each real gap carries a severity: blocks routing, or does not. Ambiguous items take their lean (CF3): lean real counts as REAL GAP, lean noise counts as NOISE. The unit of count is fixed in CF2: both real-gap questions and distinct gaps are reported, and the v2 target of 0 is set on distinct gaps.

## Classification

| Q | Label | Severity | Cluster | v1 citation | Note |
|---|---|---|---|---|---|
| Q1 | REAL GAP | Blocks routing | B | rules.md:L251 says `shipment_record` may be null ("if held"). RB1 (L196) says nothing about null | Null could mean RB1 fails, is skipped, or passes: three builds. This is EG1 territory (unverifiable evidence). Cluster B |
| Q2 | AMBIGUOUS, lean real | Blocks routing | B | rules.md:L83–85 says "received" with no quality bar. RB2 and RB5 judge content later (L197, L200) | One reading: received = present, and quality is judged by the rubric (a blurry photo fails RB2 and goes to R14). That's defensible but not stated. Cluster B |
| Q3 | DUPLICATE of Q2 | — | B | rules.md:L89 | Same "what counts as received" question, for photos |
| Q4 | NOISE, answered by v1 | — | — | rules.md:L241: `claim_type` is a supplied input | The agent doesn't classify the claim type. The engineer missed the input schema |
| Q5 | NOISE, answered by v1 | — | — | README.md:L45 (calendar dates, no roll); rules.md:L246 (supplied dates) | Where the delivery date comes from is upstream data, out of scope (README.md:L114) |
| Q6 | NOISE, answered by v1 | — | — | rules.md:L94–97, L252: any claim with the same `shipment_ref`; the list is supplied | The literal reading flags same-ref, different-goods claims, which fails safe to sign-off. Whether that's too strict is a v2 refinement, not a gap |
| Q7 | REAL GAP | Blocks routing | C | rules.md:L99–102 and RB3 (L198) compare against the invoice value "for the claimed goods", but the input carries one `invoice_amount` (L250). EC16 (edge-cases.md:L36) | Tax, freight and line-item allocation are business policy. The input schema also contradicts the rule: one invoice total versus the value of the claimed goods. Cluster C |
| Q8 | NOISE, answered by v1 | — | — | README.md:L44 | One currency by convention. Foreign invoices are an edge you could add in v2 |
| Q9 | NOISE, answered by v1 | — | — | Glossary README.md:L53 (thresholds per claim); rules.md:L94–97 (duplicate) | Split claims on the same shipment see each other as open, so R7 sends them to sign-off. Worth telling the engineer in v2 so they see it |
| Q10 | REAL GAP | Blocks routing | A | rules.md:L269 says `amount` is the proposed payout. No valuation or liability rules | The autonomous amount can be derived (approve, RB3 pass, RB4 pass → amount claimed). Partial and draft amounts can't. Cluster A |
| Q11 | REAL GAP | Blocks routing | A | rules.md:L56 says the agent "forms a decision" with no adjudication criteria. Denial reasons appear only through R9 | The central gap. v1 defines when the agent may decide, but not how to choose approve, partial or deny. Cluster A |
| Q12 | REAL GAP | Blocks routing | A | rules.md:L248: `pod_exception` is an input, and no rule or rubric item uses it | The engineer is right. Either give it a rule or remove it. Cluster A |
| Q13 | NOISE, answered by v1 | — | — | US-06 (stories.md:L50: any draft decision); rules.md:L137 (queue split on claimed amount); L10 (precedence) | Minor ambiguity: are step-3 flags evaluated when R6 fires? That folds into Q15 |
| Q14 | NOISE, answered by v1 | — | — | rules.md:L10 ("first step that matches decides"); L57–60 (partial above $10,000 → R13 explicitly) | Deny plus a failed gate → R10 (step 5 comes before step 6). The engineer missed L10 and L58 |
| Q15 | NOISE, answered by v1 | — | — | Decision tree rules.md:L24–29 (a held claim stops at step 2); US-03 (duplicate at intake) | Step 3 isn't reached during a hold, so nothing fires. Optional v2 clarity line |
| Q16 | NOISE, answered by v1 | — | — | rules.md:L65–66 ("in the claim or its documents"); L176 (re-run from step 0) | Yes: re-read the documents on every evaluation. The modality question is Q56 |
| Q17 | ALREADY KNOWN | — | — | README.md:L107; rules.md:L71–76; input `cold_chain_list` (L253) | For eval, the list is supplied per evaluation, so the engineer can build and test |
| Q18 | ALREADY KNOWN | — | — | README.md:L91, L106 | Widen D11 to cover observed-day rules (a Saturday holiday observed on Friday). Supplying the calendar is engineering |
| Q19 | AMBIGUOUS, lean real | Does not block routing | D | rules.md:L80–81 ("answering closes the SLA clock") and L155; US-15 | "Answer" is never defined as an event. Does an answer missing the next step still close the clock? That decides whether a miss notice fires. Cluster D |
| Q20 | REAL GAP | Does not block routing | D | rules.md:L155; US-15 (stories.md:L113) | Two parts v1 doesn't settle: (a) does an autonomous approval count as "approved by the claims team"? (b) may a payment date be promised while finance pre-approval is pending? Insurer consent is covered by L155. Cluster D |
| Q21 | NOISE, answered by v1 | — | — | rules.md:L255 (`current_state` holds the assigned person); L151–152 | "Working the claim" = the assigned person. No backup is the design choice, and the lead covers |
| Q22 | NOISE, answered by v1 | — | — | rules.md:L78 (expedite = a request from an account manager) | Verifying the requester's identity is integration. Other requesters aren't R3 by definition |
| Q23 | NOISE, answered by v1 | — | — | rules.md:L228 (no reminders once the claim leaves the hold); NF-10 (release reason includes "escalated") | Escalation ends the hold. The consequence the engineer found is real, but it's Q28 |
| Q24 | NOISE, engineering choice | — | — | RB3 "to the cent" (L198); RB5 "agree" (L200) | The strict reading is derivable and fails safe at threshold 1.00 (any doubt → R14). Units of measure are model judgement. Could become a gap if you want tolerances |
| Q25 | NOISE, engineering choice | — | — | README.md:L109 (P1 owned by the consultant); rules.md:L210 | Prompt wording is engineering. The consultant changes thresholds |
| Q26 | NOISE, engineering choice | — | — | rules.md:L190–191 (formula given) | The formula defines the score. Where it's computed is the engineer's call (code is safer) |
| Q27 | NOISE, engineering choice | — | — | README.md:L114 (no email integration); US-02 (the customer is the recipient; minimum content given) | Channel is integration. Template wording doesn't change behaviour. Contrast with Q35, where the letters carry decisions |
| Q28 | REAL GAP | Does not block routing | E | US-02 (stories.md:L24, "non-escalated" only); fact pack `checklist_status` (rules.md:L299) | Escalated claims with missing documents: nobody is told to request them. The reefer download is covered by the clock; other documents aren't. Cluster E |
| Q29 | NOISE, answered by v1 | — | — | README.md:L45 (calendar unless a rule says business days) | Calendar days; send on weekends |
| Q30 | NOISE, answered by v1 | — | — | rules.md:L107–109 (fixed date); EC7 | No extension exists. Relief is that the claim goes to a person (EC7). Could become a v2 business question if you want extensions |
| Q31 | NOISE, engineering choice | — | — | rules.md:L108 (23:59 ET) | 23:59 exists on DST days (the switch is at 02:00). The scheduler is engineering |
| Q32 | AMBIGUOUS, lean real | Does not block routing | L | README.md:L75 (senior specialist); US-13 | Who the people are is configuration. Backup when both the lead and the senior specialist are out, on a same-day reefer claim, isn't covered. The README risk row covers expedite only. Cluster L |
| Q33 | AMBIGUOUS, lean real | Does not block routing | L | README.md:L75 ("when the claims lead is unavailable") | Unavailability triggers backup routing but is never defined. Could be ops configuration rather than a business rule. Cluster L |
| Q34 | NOISE, engineering choice | — | — | rules.md:L143–144 | Only the first sort key is business-owned. Reefer has its own same-day rule anyway |
| Q35 | REAL GAP | Does not block routing | F | rules.md:L136 (autonomous sends the customer letter); US-10 | Autonomous letters reach customers with no person in the loop and no approved content. Denials are person-edited, but approvals aren't. Cluster F |
| Q36 | NOISE, engineering choice | — | — | NF-05, NF-06 ("reason"); README.md:L116 (miss report out of scope) | Free-text reason meets v1. Reason codes are a reporting want |
| Q37 | REAL GAP | Does not block routing | G | US-11 (stories.md:L77–79) records disagreement only | A disagreement after payment has no consequence: reopen, recover, sign-off? Cluster G |
| Q38 | OUT OF SCOPE | — | — | README.md:L114 (finance integration) | Payload and payee data are integration. The minimum (claim ID, amount) is derivable |
| Q39 | AMBIGUOUS, lean noise | — | — | rules.md:L164; US-18 | Pre-approval applies only to claims above $10,000, which are always person-handled. The agent never waits on it. Reject or amend is a finance process. Could be read as a system gap |
| Q40 | REAL GAP | Does not block routing | H | rules.md:L166 (consent gates payment only); R4 rationale (L118) | Insurer declines, partial consent, and whether a denial above the deductible needs notice or consent are business questions. The work is person-handled, which is why it's . Cluster H |
| Q41 | ALREADY KNOWN | — | — | README.md:L88, L102 | D1 covers the amount, not the basis (per claim vs aggregate). A1's "on the claimed amount" gives an interim per-claim build. Widen D1 to "amount and basis" |
| Q42 | REAL GAP | Does not block routing | I/J | rules.md:L61, L168 (package required); input schema L236–257 has no carrier field | v1 requires a package with no contents and no carrier identity in the input. Cluster I |
| Q43 | NOISE, answered by v1 | — | — | rules.md:L168 ("every such claim"; partially paid = paid) | Tracking carrier deadlines would be a new requirement, not a gap |
| Q44 | REAL GAP | Does not block routing | I/J | rules.md:L239 (`event` enum has no payment event); L256 (`paid` exists); L61 (step 7 depends on paid) | Step 7 has no triggering event. "Paid" is undefined: instruction issued or payment confirmed? Cluster I/J |
| Q45 | NOISE, answered by v1 | — | — | rules.md:L176–177; EC26 (edge-cases.md:L56) | No contradiction. EC26 applies while the claim is held (no route yet, so nothing moves down). A claim already with a person stays (L177) |
| Q46 | AMBIGUOUS, lean real | Does not block routing | M | rules.md:L177 ("sees the new information"); NF-01 (every evaluation is traced) | A trace is required. Whether the agent re-drafts or only annotates isn't stated, and two builds would differ. Cluster M |
| Q47 | REAL GAP | Does not block routing | G | rules.md:L181; US-22; EC28 | Withdrawal after payment goes to sign-off, but no decision value fits (approve, partial or deny). Cluster G |
| Q48 | NOISE, answered by v1 | — | — | rules.md:L180 ("leaves any hold or queue") | Withdrawal overrides escalation. Whether the SLA clock stops is a minor sub-point (fold into Q19) |
| Q49 | DUPLICATE of Q37 | — | G | rules.md:L178 | Same post-payment reversal gap. Cluster G |
| Q50 | DUPLICATE of Q10 | — | A | rules.md:L269 (deny → null is answered) | Approve amount is derivable for autonomous; draft amounts aren't. Cluster A |
| Q51 | AMBIGUOUS, lean noise | — | — | US-23; rules.md:L170 | The customer → account manager mapping is upstream data. "Decided" reasonably means a final decision recorded. Denial-notice content could be argued as business |
| Q52 | NOISE, answered by v1 | — | — | US-02, US-10, US-12 | v1 lists the communications. More (acknowledgements) would be a scope addition |
| Q53 | OUT OF SCOPE | — | — | README.md:L114 (deployment); NF-17 | Retention and access are compliance and deployment concerns. A compliance owner might call this real. |
| Q54 | OUT OF SCOPE | — | — | README.md:L114 | Belongs in the platform ADR (data residency) |
| Q55 | REAL GAP | Blocks routing | K | NF-14, NF-15; rules.md:L6 ("outside scope → escalate" doesn't cover failures) | The fail-safe route when the model call fails or times out is a business call (escalate by default?), and NF-14's same-day reefer promise depends on it. Sizing is out of scope. Cluster K |
| Q56 | AMBIGUOUS, lean noise | — | — | RB2 (L197) implies image judgement; input `documents` content (L250) | Image reading is implied by RB2. Format is integration. Document language is a business fact that v1 doesn't state |

## Clusters (distinct gaps)

| Cluster | Gap | Questions | Severity |
|---|---|---|---|
| A | Adjudication criteria and payout valuation (how to choose approve, partial or deny; partial amounts; `pod_exception`) | Q10, Q11, Q12, Q50 | Blocks routing |
| B | Missing or unverifiable evidence (null shipment record; what "received" means) → EG1 | Q1, Q2, Q3 | Blocks routing |
| C | Invoice value of the claimed goods (line items, tax, freight; one input field) | Q7 | Blocks routing |
| D | Expedite answer mechanics (what is an answer; what counts as approved) | Q19, Q20 | Does not block routing |
| E | Escalated claims with missing documents: who requests them | Q28 | Does not block routing |
| F | Customer letter content and approval | Q35 | Does not block routing |
| G | Reversal after an autonomous payment (reviewer disagrees, new information, withdrawal) | Q37, Q47, Q49 | Does not block routing |
| H | Insurer declines, partial consent, denial above the deductible | Q40 | Does not block routing |
| I/J | Carrier filing package: contents, carrier identity, the "paid" event | Q42, Q44 | Does not block routing |
| K | Fail-safe route on model failure | Q55 | Blocks routing |
| L | Backup when the lead and the senior specialist are unavailable *(lean real)* | Q32, Q33 | Does not block routing |
| M | Re-draft or annotate on a person-owned claim *(lean real)* | Q46 | Does not block routing |

Cluster B is where spike gap EG1 (`engagement/03-requirements/v2-gaps.md`) falls: a null shipment record and what "received" means.

## Where the engineer and v1 disagree

**The engineer missed what v1 says** (these support NOISE):

- Q4: `claim_type` is an input (`rules.md:L241`)
- Q9: R7 catches split claims
- Q14: precedence at `rules.md:L10`; R13 for a partial above $10,000 at L58
- Q16: re-run from step 0 at `rules.md:L176`; documents included at L65
- Q21: assigned person at `rules.md:L255`
- Q23: reminders stop at `rules.md:L228`
- Q29: calendar convention at `README.md:L45`
- Q45: no up-only contradiction with EC26

**The engineer found real internal defects in v1** (these support REAL GAP):

- Q7: one `invoice_amount` versus the value of the claimed goods
- Q12: `pod_exception` is an input that no rule uses
- Q42: no carrier field in the input
- Q44: no payment event

## Counts

<!-- COUNTS -->
| Measure | Count |
|---|---|
| Questions | 56 |
| **Real-gap questions** | **19** (14 firm, 5 lean real) |
| **Distinct gaps** (clusters, I/J once) | **12** |
| Distinct gaps that block routing | 4 (A, B, C, K) |
| Already known | 3 |
| Out of scope | 3 |
| Duplicates | 3 |
| Noise, including lean noise | 28 (18 answered by v1, 7 engineering choice, 3 lean noise) |
<!-- /COUNTS -->
