# Cold-FDE v1: Classification Advice (provisional, for the consultant's decision)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Advisory only. Every label below is provisional and is yours to accept or
reject. Line references are to the frozen v1 files as read on 2026-11-22
(`rules.md:L10` = rules.md, line 10). Check each against the source.

---

## 1. The criteria

Criteria 3 and 5 are sound as written. I'd change the other four before
classifying. Change 5 matters most.

| # | Your criterion | Proposed change | Questions it moves |
|---|---|---|---|
| 1 | "v1 does not answer it, even indirectly" | **"v1 does not answer it unambiguously."** If two competent engineers could build different behaviour from the same text, count it as a gap even though v1 touches the topic. "Indirectly" otherwise lets a vague sentence close a real question | Q2, Q19, Q46 move toward real gap |
| 2 | Already flagged as open, so not a new finding | **Count these separately as ALREADY KNOWN.** Leave them out of the real-gap count, but report them next to it. Two exceptions: (a) a known item with **no interim behaviour** is a real gap; (b) a question that exposes a part the dependency doesn't cover is "known, widen the dependency" | Q41 (deductible basis), Q18 (observed holidays) |
| 4 | Changes the route, decision, rule_applied, a trigger or an output field | **Widen it to "changes any behaviour v1 requires".** That includes system actions the stories require (send, block, notify, record, prepare), not only agent output fields. v1 makes the agent send letters, send reminders and prepare filing packages | Q28, Q35, Q37, Q44 move to real gap |
| 5 | The business must answer it | **"The business or the spec owner must answer it."** Internal inconsistencies in v1 (an input no rule uses, a step with no triggering event) are spec defects. An engineer would be guessing your intent, so they should count | Q12, Q42, Q44 |
| + | (none) | **Fix the unit of count before classifying.** Many of the 56 questions are the same gap asked several ways. Decide now whether the metric counts questions or distinct gaps. Deciding after you see the numbers looks like gaming. My suggestion: report both, and set the target on distinct gaps | Changes the headline, not the labels |
| + | (none) | **Add a severity tag** to each real gap: *blocks routing* or *does not block routing*. It sets the v2 order and gives you an honest one-line story | Ordering only |

**Is the binary enough?** No. Use six labels: REAL GAP, AMBIGUOUS (lean real
or lean noise), DUPLICATE, ALREADY KNOWN, OUT OF SCOPE, and NOISE, split
into *answered by v1* and *engineering choice*. Only REAL GAP counts toward
the metric. The other labels make the split you report auditable.

---

## 2. Question by question

Confidence: **H** = high, **M** = medium, **L** = low. **⚖** = reasonable
people could disagree. **⇄** = the engineer and v1 disagree about what v1
says, so check the source yourself.

### Inputs and data availability

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q1 | **REAL GAP** (blocks routing) | rules.md:L251 says `shipment_record` may be null ("if held"). RB1 (L196) says nothing about null | H | Null could mean RB1 fails, is skipped, or passes: three builds. This is EG1 territory (unverifiable evidence). Cluster B |
| Q2 | **AMBIGUOUS, lean real** ⚖ | rules.md:L83–85 says "received" with no quality bar. RB2 and RB5 judge content later (L197, L200) | M | One reading: received = present, and quality is judged by the rubric (a blurry photo fails RB2 and goes to R14). That's defensible but not stated. Cluster B |
| Q3 | **DUPLICATE of Q2** | rules.md:L89 | H | Same "what counts as received" question, for photos |
| Q4 | NOISE (answered) ⇄ | rules.md:L241: `claim_type` is a supplied input | H | The agent doesn't classify the claim type. The engineer missed the input schema |
| Q5 | NOISE (answered) | README.md:L45 (calendar dates, no roll); rules.md:L246 (supplied dates) | M | Where the delivery date comes from is upstream data, out of scope (README.md:L114) |
| Q6 | NOISE (answered) | rules.md:L94–97, L252: any claim with the same `shipment_ref`; the list is supplied | M ⚖ | The literal reading flags same-ref, different-goods claims, which fails safe to sign-off. Whether that's too strict is a v2 refinement, not a gap |
| Q7 | **REAL GAP** (blocks routing) ⇄ | rules.md:L99–102 and RB3 (L198) compare against the invoice value "for the claimed goods", but the input carries one `invoice_amount` (L250). EC16 (edge-cases.md:L189) | H | Tax, freight and line-item allocation are business policy. The input schema also contradicts the rule: one invoice total versus the value of the claimed goods. Cluster C |
| Q8 | NOISE (answered) | README.md:L44 | M | One currency by convention. Foreign invoices are an edge you could add in v2 |

### Routing rules and precedence

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q9 | NOISE (answered indirectly) ⇄ | Glossary README.md:L53 (thresholds per claim); rules.md:L94–97 (duplicate) | M | Split claims on the same shipment see each other as open, so R7 sends them to sign-off. Worth telling the engineer in v2 so they see it |
| Q10 | **REAL GAP** (blocks routing) | rules.md:L269 says `amount` is the proposed payout. No valuation or liability rules | H | The autonomous amount can be derived (approve, RB3 pass, RB4 pass → amount claimed). Partial and draft amounts can't. Cluster A |
| Q11 | **REAL GAP** (blocks routing) | rules.md:L56 says the agent "forms a decision" with no adjudication criteria. Denial reasons appear only through R9 | H | **The central gap.** v1 defines when the agent may decide, but not how to choose approve, partial or deny. Cluster A |
| Q12 | **REAL GAP** (spec defect) ⇄ | rules.md:L248: `pod_exception` is an input, and no rule or rubric item uses it | H | The engineer is right. Either give it a rule or remove it. Cluster A |
| Q13 | NOISE (answered) | US-06 (stories.md:L50: any draft decision); rules.md:L137 (queue split on claimed amount); L10 (precedence) | M | Minor ambiguity: are step-3 flags evaluated when R6 fires? That folds into Q15 |
| Q14 | NOISE (answered) ⇄ | rules.md:L10 ("first step that matches decides"); L57–60 (partial above $10,000 → R13 explicitly) | H | Deny plus a failed gate → R10 (step 5 comes before step 6). The engineer missed L10 and L58 |
| Q15 | NOISE (answered) | Decision tree rules.md:L24–29 (a held claim stops at step 2); US-03 (duplicate at intake) | M | Step 3 isn't reached during a hold, so nothing fires. Optional v2 clarity line |
| Q16 | NOISE (answered) ⇄ | rules.md:L65–66 ("in the claim or its documents"); L176 (re-run from step 0) | H | Yes: re-read the documents on every evaluation. The modality question is Q56 |

### Cold-chain list, expedite and time

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q17 | **ALREADY KNOWN** (D12) | README.md:L107; rules.md:L71–76; input `cold_chain_list` (L253) | H | For eval, the list is supplied per evaluation, so the engineer can build and test |
| Q18 | **ALREADY KNOWN** (D11, A4) | README.md:L91, L106 | H | Widen D11 to cover observed-day rules (a Saturday holiday observed on Friday). Supplying the calendar is engineering |
| Q19 | **AMBIGUOUS, lean real** ⚖ | rules.md:L80–81 ("answering closes the SLA clock") and L155; US-15 | M | "Answer" is never defined as an event. Does an answer missing the next step still close the clock? That decides whether a miss notice fires. Cluster D |
| Q20 | **REAL GAP** (does not block routing) | rules.md:L155; US-15 (stories.md:L113) | M ⚖ | Two parts v1 doesn't settle: (a) does an autonomous approval count as "approved by the claims team"? (b) may a payment date be promised while finance pre-approval is pending? Insurer consent is covered by L155. Cluster D |
| Q21 | NOISE (answered) ⇄ | rules.md:L255 (`current_state` holds the assigned person); L151–152 | M | "Working the claim" = the assigned person. No backup is the design choice, and the lead covers |
| Q22 | NOISE (answered by definition) | rules.md:L78 (expedite = a request from an account manager) | M | Verifying the requester's identity is integration. Other requesters aren't R3 by definition |
| Q23 | NOISE (answered) ⇄ | rules.md:L228 (no reminders once the claim leaves the hold); NF-10 (release reason includes "escalated") | H | Escalation ends the hold. The consequence the engineer found is real, but it's Q28 |

### Confidence

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q24 | NOISE (engineering choice) ⚖ | RB3 "to the cent" (L198); RB5 "agree" (L200) | L | The strict reading is derivable and fails safe at threshold 1.00 (any doubt → R14). Units of measure are model judgement. Could become a gap if you want tolerances |
| Q25 | NOISE (answered / engineering) | README.md:L109 (P1 owned by the consultant); rules.md:L210 | H | Prompt wording is engineering. The consultant changes thresholds |
| Q26 | NOISE (engineering choice) | rules.md:L190–191 (formula given) | H | The formula defines the score. Where it's computed is the engineer's call (code is safer) |

### Documents, hold and reminders

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q27 | NOISE (out of scope / engineering) | README.md:L114 (no email integration); US-02 (the customer is the recipient; minimum content given) | M | Channel is integration. Template wording doesn't change behaviour. Contrast with Q35, where the letters carry decisions |
| Q28 | **REAL GAP** (does not block routing) | US-02 (stories.md:L24, "non-escalated" only); fact pack `checklist_status` (rules.md:L299) | H | Escalated claims with missing documents: nobody is told to request them. The reefer download is covered by the clock; other documents aren't. Cluster E |
| Q29 | NOISE (answered) ⇄ | README.md:L45 (calendar unless a rule says business days) | H | Calendar days; send on weekends |
| Q30 | NOISE (answered by absence) ⚖ | rules.md:L107–109 (fixed date); EC7 | M | No extension exists. Relief is that the claim goes to a person (EC7). Could become a v2 business question if you want extensions |
| Q31 | NOISE (engineering choice) | rules.md:L108 (23:59 ET) | H | 23:59 exists on DST days (the switch is at 02:00). The scheduler is engineering |

### Sign-off, queues and people

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q32 | **AMBIGUOUS, lean real** (does not block routing) ⚖ | README.md:L75 (senior specialist); US-13 | M | Who the people are is configuration. Backup when both the lead and the senior specialist are out, on a same-day reefer claim, isn't covered. The README risk row covers expedite only. Cluster L |
| Q33 | **AMBIGUOUS, lean real** ⚖ | README.md:L75 ("when the claims lead is unavailable") | L | Unavailability triggers backup routing but is never defined. Could be ops configuration rather than a business rule. Cluster L |
| Q34 | NOISE (engineering choice) | rules.md:L143–144 | M | Only the first sort key is business-owned. Reefer has its own same-day rule anyway |
| Q35 | **REAL GAP** (does not block routing) | rules.md:L136 (autonomous sends the customer letter); US-10 | H | Autonomous letters reach customers with no person in the loop and no approved content. Denials are person-edited, but approvals aren't. Cluster F |
| Q36 | NOISE (engineering / governance) | NF-05, NF-06 ("reason"); README.md:L116 (miss report out of scope) | M | Free-text reason meets v1. Reason codes are a reporting want |
| Q37 | **REAL GAP** (does not block routing) | US-11 (stories.md:L77–79) records disagreement only | H | A disagreement after payment has no consequence: reopen, recover, sign-off? Cluster G |

### Payment, insurer and carrier filing

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q38 | OUT OF SCOPE | README.md:L114 (finance integration) | M | Payload and payee data are integration. The minimum (claim ID, amount) is derivable |
| Q39 | **AMBIGUOUS, lean noise** ⚖ | rules.md:L164; US-18 | L | Pre-approval applies only to claims above $10,000, which are always person-handled. The agent never waits on it. Reject or amend is a finance process. Could be read as a system gap |
| Q40 | **REAL GAP** (does not block routing) | rules.md:L166 (consent gates payment only); R4 rationale (L118) | M ⚖ | Insurer declines, partial consent, and whether a denial above the deductible needs notice or consent are business questions. The work is person-handled, which is why it's ⚖. Cluster H |
| Q41 | **ALREADY KNOWN** (D1; widen) | README.md:L88, L102 | M ⚖ | D1 covers the amount, not the basis (per claim vs aggregate). A1's "on the claimed amount" gives an interim per-claim build. Widen D1 to "amount and basis" |
| Q42 | **REAL GAP** (spec defect) ⇄ | rules.md:L61, L168 (package required); input schema L236–257 has **no carrier field** | H | v1 requires a package with no contents and no carrier identity in the input. Cluster I |
| Q43 | NOISE (answered) | rules.md:L168 ("every such claim"; partially paid = paid) | M | Tracking carrier deadlines would be a new requirement, not a gap |
| Q44 | **REAL GAP** (spec defect) ⇄ | rules.md:L239 (`event` enum has no payment event); L256 (`paid` exists); L61 (step 7 depends on paid) | H | Step 7 has no triggering event. "Paid" is undefined: instruction issued or payment confirmed? Cluster I/J |

### Re-routing, withdrawals and events

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q45 | NOISE (answered) ⇄ | rules.md:L176–177; EC26 (edge-cases.md:L209) | M | No contradiction. EC26 applies while the claim is held (no route yet, so nothing moves down). A claim already with a person stays (L177) |
| Q46 | **AMBIGUOUS, lean real** ⚖ | rules.md:L177 ("sees the new information"); NF-01 (every evaluation is traced) | M | A trace is required. Whether the agent re-drafts or only annotates isn't stated, and two builds would differ. Cluster M |
| Q47 | **REAL GAP** (does not block routing) | rules.md:L181; US-22; EC28 | H | Withdrawal after payment goes to sign-off, but no decision value fits (approve, partial or deny). Cluster G |
| Q48 | NOISE (answered) | rules.md:L180 ("leaves any hold or queue") | M | Withdrawal overrides escalation. Whether the SLA clock stops is a minor sub-point (fold into Q19) |
| Q49 | **DUPLICATE of Q37** | rules.md:L178 | H | Same post-payment reversal gap. Cluster G |

### Outputs, notifications, non-functional

| Q | Provisional | v1 support | Conf | Note |
|---|---|---|---|---|
| Q50 | **DUPLICATE of Q10** | rules.md:L269 (deny → null is answered) | H | Approve amount is derivable for autonomous; draft amounts aren't. Cluster A |
| Q51 | **AMBIGUOUS, lean noise** ⚖ | US-23; rules.md:L170 | L | The customer → account manager mapping is upstream data. "Decided" reasonably means a final decision recorded. Denial-notice content could be argued as business |
| Q52 | NOISE (answered by absence) | US-02, US-10, US-12 | M | v1 lists the communications. More (acknowledgements) would be a scope addition |
| Q53 | OUT OF SCOPE | README.md:L114 (deployment); NF-17 | M ⚖ | Retention and access are compliance and deployment concerns. A compliance owner might call this real. Note: Q53 appears twice in the paste; it's one question |
| Q54 | OUT OF SCOPE | README.md:L114 | H | Belongs in the platform ADR (data residency) |
| Q55 | **REAL GAP** (blocks routing) | NF-14, NF-15; rules.md:L6 ("outside scope → escalate" doesn't cover failures) | H | The fail-safe route when the model call fails or times out is a business call (escalate by default?), and NF-14's same-day reefer promise depends on it. Sizing is out of scope. Cluster K |
| Q56 | **AMBIGUOUS, lean noise** ⚖ | RB2 (L197) implies image judgement; input `documents` content (L250) | L | Image reading is implied by RB2. Format is integration. Document language is a business fact that v1 doesn't state |

---

## 3. Clusters (distinct gaps)

| Cluster | Gap | Questions | Severity |
|---|---|---|---|
| A | Adjudication criteria and payout valuation (how to choose approve, partial or deny; partial amounts; `pod_exception`) | Q10, Q11, Q12, Q50 | Blocks routing |
| B | Missing or unverifiable evidence (null shipment record; what "received" means) → **EG1** | Q1, Q2, Q3 | Blocks routing |
| C | Invoice value of the claimed goods (line items, tax, freight; one input field) | Q7 | Blocks routing |
| D | Expedite answer mechanics (what is an answer; what counts as approved) | Q19, Q20 | No |
| E | Escalated claims with missing documents: who requests them | Q28 | No |
| F | Customer letter content and approval | Q35 | No |
| G | Reversal after an autonomous payment (reviewer disagrees, new information, withdrawal) | Q37, Q47, Q49 | No |
| H | Insurer declines, partial consent, denial above the deductible | Q40 | No |
| I/J | Carrier filing package: contents, carrier identity, the "paid" event | Q42, Q44 | No |
| K | Fail-safe route on model failure | Q55 | Blocks routing |
| L | Backup when the lead and the senior specialist are unavailable *(lean real)* | Q32, Q33 | No |
| M | Re-draft or annotate on a person-owned claim *(lean real)* | Q46 | No |

That's **10 firm distinct gaps plus 2–3 lean-real**, from 56 questions.
Four clusters block routing: A, B, C and K.

---

## 4. Where the engineer and v1 disagree (check the source)

**The engineer missed what v1 says** (these support NOISE):
- Q4 (`claim_type` is an input, rules.md:L241)
- Q9 (R7 catches split claims)
- Q14 (precedence L10; R13 for a partial above $10,000 at L58)
- Q16 (re-run from step 0 at L176; documents included at L65)
- Q21 (assigned person at L255)
- Q23 (reminders stop at L228)
- Q29 (calendar convention at README.md:L45)
- Q45 (no up-only contradiction with EC26)

**The engineer found real internal defects in v1** (these support REAL GAP):
- Q7 (one `invoice_amount` versus the value of the claimed goods)
- Q12 (`pod_exception` unused)
- Q42 (no carrier field in the input)
- Q44 (no payment event)

---

## 5. Counts and least-sure list

| Label | Count | Questions |
|---|---|---|
| REAL GAP | 14 | 1, 7, 10, 11, 12, 20, 28, 35, 37, 40, 42, 44, 47, 55 |
| AMBIGUOUS, lean real | 5 | 2, 19, 32, 33, 46 |
| AMBIGUOUS, lean noise | 3 | 39, 51, 56 |
| DUPLICATE | 3 | 3 (→2), 49 (→37), 50 (→10) |
| ALREADY KNOWN | 3 | 17, 18, 41 |
| OUT OF SCOPE | 3 | 38, 53, 54 |
| NOISE, answered by v1 | 18 | 4, 5, 6, 8, 9, 13, 14, 15, 16, 21, 22, 23, 29, 30, 43, 45, 48, 52 |
| NOISE, engineering choice | 7 | 24, 25, 26, 27, 31, 34, 36 |
| **Total** | **56** | |

**Real-gap range**, depending on your calls on the ambiguous items:
**14–19 questions**, or **10–13 distinct gaps**.

**Least sure, decide these first:** Q2, Q19, Q20, Q24, Q30, Q32, Q33, Q39,
Q40, Q41, Q46, Q51, Q53, Q56.

**The one to settle before anything else:** Q11, cluster A. If you rule
that adjudication criteria are deliberately left to the model and the
rubric, then Q10, Q11 and Q50 become a design choice, not a gap. You'd need
to say so explicitly in v2. Q12 stays a spec defect either way.
