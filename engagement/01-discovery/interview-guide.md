# Interview Guide: Claims Process Discovery (v1)

**Engagement:** Claims-to-Agent Discovery Sprint (see SOW)
**Interviews:** COO (sponsor) first, then Claims and dispatch lead (process owner), so the second interview can test what the first one claimed. Interview D is the Day 2 COO ratification session. The CFO section is for Day 3.
**Length:** about 25 minutes each, including the opening

> Fictional engagement for portfolio purposes. All stakeholders are synthetic.

---

## How to use this guide

- **Open first, probe second.** Start each section with the open question. Use probes only if the answer doesn't cover them. Never state a hypothesis to the interviewee.
- **Ask for specifics.** Ask about "the last claim you handled", not "usually". Ask "how do you know?" for any number.
- **Must-ask** prompts are marked ★. If time runs short, skip unmarked prompts first.
- **Comparable prompts** are marked ⇄. Ask them of both personas in exactly the same words, at the same point in the interview (straight after the opening), so the answers can be compared.
- **Double-barrelled prompts** (S1, S2): if only the first half is answered, prompt for the second.
- **Capture claims and evidence separately.** In the field notes, record what was said (with its transcript line) apart from what can be checked against data.

### Tags

Each prompt carries a tag, used when citing in synthesis.

| Tag | Links to |
|---|---|
| H1–H5 | Hypotheses in the data request (below) |
| BC | Business-case baselines |
| Scope | Scope table and scope boundaries |
| Acceptance | Agent acceptance criteria |
| Edge cases | Edge cases for requirements |
| Data quality | Gaps and reliability of the data release |

### Hypotheses (from the data request; never read aloud)

| ID | Hypothesis |
|---|---|
| H1 | Delay comes mainly from waiting and handoffs, not hands-on work |
| H2 | At least one approval or review step rarely changes the outcome |
| H3 | Claims rules are applied inconsistently |
| H4 | Decision ownership is unclear between operations and finance |
| H5 | The biggest cost is in write-offs and missed carrier recoveries, not labour |
| BC | Business-case baselines |

---

## Opening (1 min, both)

- Purpose: understand how claims work today before deciding what, if anything, to automate.
- Recording: "I'll be keeping a transcript. Is that OK?"
- Confidentiality: notes stay within the engagement; deliverables cite interviewees by role, never by name.
- "There are no wrong answers. I'm interested in how it actually works, not how it's supposed to."

## Shared questions (4 min, both, straight after the opening)

| # | Prompt | Tag |
|---|---|---|
| S1 ★⇄ | What does "slow" or "costly" mean to you when it comes to claims? How would you know it had improved? | BC |
| S2 ★⇄ | Who has the final say on a claim decision today? And who *should*? | H4 |
| S3 ★⇄ | What should an agent never decide on its own? | Scope |

---

## Interview A: COO (sponsor), 25 min

Opening (1 min) and shared questions S1–S3 (4 min) first.

### A1. Problem and baselines (6 min)

| # | Prompt | Tag |
|---|---|---|
| A1.1 | What made this a priority now? | BC |
| A1.2 | How do you hear about claims today: reports, complaints, escalations? | H1, BC |
| A1.3 ★ | Which numbers do you look at to judge how claims are going? How do you know they're right? | BC |
| A1.4 | From receipt to close, how long does a typical claim take? How much of that is someone actually working on it? | H1, BC |
| A1.5 | *Probe:* Where do you think the time goes? | H1 |

### A2. Rules, ownership and decisions (5 min)

| # | Prompt | Tag |
|---|---|---|
| A2.1 ★ | What rules do you understand the team applies when deciding a claim? How do you know? | H3 |
| A2.2 | How are write-offs decided, and who owns that decision? | H4, H5 |
| A2.3 | *Probe:* Tell me about the last time people disagreed on a claim decision. Who was involved, and how was it settled? | H4 |

### A3. The agent (6 min)

| # | Prompt | Tag |
|---|---|---|
| A3.1 | What would you want it to handle first, and why? | BC |
| A3.2 | What would make you lose confidence in it? | Acceptance |

### A4. Close (3 min)

| # | Prompt | Tag |
|---|---|---|
| A4.1 ★ | What should I have asked that I didn't? | — |
| A4.2 | Who else should I talk to? | — |

---

## Interview B: Claims and dispatch lead (process owner), 25 min

Opening (1 min) and shared questions S1–S3 (4 min) first.

### B1. Role and process walkthrough (7 min)

| # | Prompt | Tag |
|---|---|---|
| B1.1 ★ | Walk me through the last claim you handled, from the moment it arrived to the moment it closed. | H1, H2 |
| B1.2 | *Probe at each step:* Who does it? Which system or tool? What decision is made, and on what rule? | H3, H4 |
| B1.3 ★ | Which of those steps aren't recorded in the system? | H1 |
| B1.4 | Which roles handle claims, and how does a claim get assigned to someone? | H4 |

### B2. Waiting, documents and rework (3 min)

| # | Prompt | Tag |
|---|---|---|
| B2.1 ★ | Where does a claim wait, and who is it waiting for? | H1 |
| B2.2 | When do documents usually arrive relative to the claim? What happens when something is missing? | H1, H3 |
| B2.3 | *Probe, per step:* Why does this step exist? What would happen if it were skipped? When was it last overturned? | H2 |

### B3. Rules and exceptions (4 min)

| # | Prompt | Tag |
|---|---|---|
| B3.1 ★ | Is there a written claims policy or approval-authority matrix? Can we have copies? | H3 |
| B3.2 | Tell me about the last time you didn't follow the written rule. Why? | H3 |
| B3.3 | How is escalation decided, and where is it recorded? | H2, H4 |
| B3.4 | Is shipment value checked when assessing a claim? Where does it come from? | H3 |
| B3.5 | Tell me about a claim nobody wanted to touch. What made it hard? | Edge cases |
| B3.6 | What does a new team member usually get wrong in their first month? | Edge cases |
| B3.7 | What's the rarest kind of claim you've handled in the last six months? How did you handle it? | Edge cases |
| B3.8 | Are loss claims handled differently from damage and shortage claims? Is that the right boundary? | Scope |

### B4. Follow-ups from T1 (4 min)

Added after the COO interview (see field notes, T1 follow-ups). Ask in
neutral words: never quote the COO or his figures, so the claims lead's
answers stay independent and can be compared. Document timing (`T1:L26`) is
already covered by B2.2.

| # | Prompt | Source | Tag |
|---|---|---|---|
| B4.1 | Does anyone outside the claims team approve or pay claims? How is that recorded, and does your team see it? | `T1:L10` | H4 |
| B4.2 | *If a check before payment came up in B1:* What does it look at? When did it last change or stop a payment? | `T1:L26` | H2 |
| B4.3 | Which claims need a person's judgment, and why? | `T1:L12`, `T1:L34` | Scope |
| B4.4 | How are denials decided and written? When was a denial last reversed? | `T1:L36` | H3, Acceptance |
| B4.5 | Who approves large claims? Is there a value threshold? | `T1:L12` | H4, Scope |
| B4.6 | How do you decide whether to pursue the carrier for recovery? How much do you recover, and how is that measured? | `T1:L18` | H5 |

### B5. Data and record-keeping (if time allows)

| # | Prompt | Tag |
|---|---|---|
| B5.1 | From receipt to close, how long does a typical claim take? How much of that is someone actually working on it, by role? How do you know? | H1, BC |
| B5.2 | How are write-offs decided, by whom, and where are they recorded? | H4, H5 |
| B5.3 | Is a claim ever withdrawn? How is that recorded? | Data quality |
| B5.4 | Any process, system or coding changes in the last 6 months? | Data quality |
| B5.5 | Are any claims handled outside the system, for example by email or spreadsheet? | H1, Data quality |

### B6. Close (2 min)

| # | Prompt | Tag |
|---|---|---|
| B6.1 ★ | What should I have asked that I didn't? | — |
| B6.2 | If you could change one thing about the process tomorrow, what would it be? | H2 |

---

## Interview C: CFO (Day 3, business-case defence), draft only

Finalize after the spike and the ROI draft. The session is a defence: the CFO
challenges the business case and we answer. The prompts below open the
session; the challenge log records the rest.

### Opening prompts

| # | Prompt | Tag |
|---|---|---|
| C1 ★⇄ | What does "slow" or "costly" mean to you when it comes to claims? How would you know it had improved? | BC |
| C2 ★⇄ | Who has the final say on a claim decision today? And who *should*? | H4 |
| C3 | What evidence would you need to trust the savings estimate? | BC |
| C4 | How are write-offs and carrier recoveries reported today? | H5 |
| C5 | What is the loaded cost of an hour of claims handling, and how is it calculated? | BC |

### Challenge log (SOW deliverable #5)

| # | CFO challenge | Our answer | Evidence cited | Structural change to ROI model? (Y/N) |
|---|---|---|---|---|
| | | | | |

---

## Interview D: COO ratification of C4 and E4 (Day 2)

Short session before the requirements v1 freeze (D5 handling ruling). The
sponsor ratifies or rejects C4 and E4, as SOW §8 requires. The ask was put in
`sponsor-summary-day2.md`. Transcript: `transcripts/T3-coo.md`.

**Length:** 25 minutes, hard stop (D5d). If the session does not converge,
log "not ratified" and proceed under D5a.

### Inputs (briefing; never read aloud)

**The decision**

- **C4:** the claims team owns all claim payouts. Account managers can request expedited handling but cannot approve or pay.
- **E4:** the account-manager early-payment path is eliminated. It is replaced by an expedite request, which always routes to a person and is never auto-approved (scope table R3).

**What the COO has said**

| Line | Said |
|---|---|
| T1:L10 | Account managers "can approve for their key accounts… that's how it should be"; "I want the AM to fix it today, not wait for claims" |
| T1:L8 | Improvement means claims close "in days, not weeks" and key accounts stop raising it |
| T1:L14 | Two key accounts raised claims speed in business reviews; Hollisbrook is "about 9 percent of revenue" |
| T1:L36 | Red line: a key account wrongly denied by the agent, or the agent not being faster |
| T1:L32 | Recalls no disagreements: "It doesn't reach me as a fight" |

**What the claims lead has said**

| Line | Said |
|---|---|
| T2:L14 | Account managers pay early, before photos or a delivery receipt; "I've got nothing to file"; payouts should be the claims team's decision |
| T2:L54 | "We usually find out after the money's gone" |
| T2:L78 | Stopping account managers paying before paperwork "would help recoveries more than anything" |

**Evidence** (backup: shown in full only if challenged, D5c)

| Query | Finding |
|---|---|
| Q8 | Account managers decided 35 claims at or below $10k and 2 above |
| Q11 | Account managers: 37 claims; 22 (61%) paid before documents were complete; 38% filed with the carrier; recovered ÷ paid 3%; median 20 days from receipt to payment |
| Q11 | Claims team: 324 claims; 0 (0%) paid before documents were complete; 66% filed; recovered ÷ paid 29%; median 28 days from receipt to payment |
| Q12 | NLC-26-0169, $60,296, decided by an account manager, paid before insurer notice; notified 41 days after receipt; cover declined. The only claim paid before notice |
| C6 | The conflict does not reach the sponsor (T1:L32), although the claims lead calls the declined claim "still a sore point" (T2:L16) |

**What account managers keep or gain**

- An expedite request goes straight to a person and never waits on the agent (E4; R3).
- Key-account claims are worked first in the sign-off and escalation queues (G6).
- The account manager is notified of the outcome when the claim is decided, with no approval or payment rights (G6).
- Every denial goes to a person, which covers the COO's red line (C5; G6).

**Fallback positions already rejected**

| Ruling | Rejected option |
|---|---|
| C4 (a) | Keep account-manager authority for key accounts |
| C4 (b) | Allow account-manager payouts up to a limit |
| C4 (c) | Reclassify account-manager payments as goodwill outside the claims process |
| E4 (a) | Keep the path with a spending limit |
| E4 (b) | Keep the path but require documents before payment |

**What a rejection or conditional ratification reopens**

| Artifact | Dependency on C4/E4 |
|---|---|
| Scope table R3; decision tree step 1 and T3 | Expedite request → always escalate |
| Future-state swimlane, account-manager lane | "Submits expedite request only; cannot approve or pay" |
| G6 | Notice carries no approval or payment rights |
| G9b | Rationale cites account-manager payments outside the claims process (Q11); the gate would have to cover account-manager payments if C4 falls |
| G10a | An expedite request is new information that re-runs the tree |
| Requirements v1 | Frozen on the outcome (D5 handling ruling) |

### D1. Recap and ask (3 min)

| # | Prompt | Tag |
|---|---|---|
| D1.1 ★ | On Day 1 you said account managers should be able to fix a key account's problem the same day. Today I'm asking for one decision: the claims team owns every claim payout, and account managers no longer approve or pay. Instead they send an expedite request, which goes straight to a person on the claims team. | H4 |

### D2. Evidence (7 min, speed gap first)

Headline figures only (D5c). State the speed gap before the COO can raise it
(D5b).

| # | Prompt | Tag |
|---|---|---|
| D2.1 ★ | First, the case for the current way: account managers pay faster. The median is 20 days from receipt to payment, against 28 for the claims team (Q11). | BC |
| D2.2 ★ | The speed comes from paying before the documents are in: 61% of account-manager payments, against none for the claims team (Q11). | H4, H5 |
| D2.3 ★ | Without the documents, the money is rarely recovered from the carrier: 3% of what account managers paid, against 29% for the claims team (Q11). | H5, BC |
| D2.4 ★ | One claim shows the insurance risk. A $60,296 claim was paid by an account manager before the insurer was told, and the insurer declined cover (Q12). It is one claim, not a rate. | H4 |
| D2.5 | The redesign goes after the claims team's delay: finance pre-approval goes (subject to the CFO's agreement), so does the Thursday payment batch, and documents are requested up front (E1, E2, E3, E5). We'll measure how close it gets to 20 days; I'm not promising it. | BC |
| D2.6 | *Probe:* How does that compare with what you'd heard? | H4 |

### D3. What account managers keep or gain (3 min)

| # | Prompt | Tag |
|---|---|---|
| D3.1 ★ | Account managers keep a fast lane. An expedite request goes straight to a person and never waits on the agent. Key-account claims are worked first, and the account manager is told the outcome as soon as the claim is decided. Every denial still goes to a person. | Scope |

### D4. Objections and conditions (10 min)

Classify any condition against D5a as it is stated. Do not negotiate payment
authority; record it.

| # | Prompt | Tag |
|---|---|---|
| D4.1 ★ | What concerns do you have about this? | H4 |
| D4.2 ★ | What would need to be true for you to agree? | Acceptance |
| D4.3 | *Probe, if a condition is given:* Is that about how fast expedite requests are handled, or how account managers are kept informed? Or about account managers being able to pay? | Acceptance |
| D4.4 | *Probe, if a speed condition is given:* What response time would you hold the claims team to on an expedite request? | Acceptance |
| D4.5 | *Probe, if the answer is "not yet":* What would you need to see, and from whom? | — |

### D5. Close (2 min)

| # | Prompt | Tag |
|---|---|---|
| D5.1 ★ | To confirm in one sentence: the claims team owns every claim payout, account managers cannot approve or pay, and they send expedite requests instead [plus any condition stated in D4]. Is that your decision? | H4 |

### Outcome (record after the session, per D5a)

| COO answer | Ratified? | Next step |
|---|---|---|
| Yes | Yes | Requirements v1 |
| Yes, with a service or communication condition | Yes | The condition becomes an expedite service-level requirement in v1 |
| Yes, with any payment authority for account managers | No | A new ruling amending C4/E4 before v1 |
| No, deferred, or no convergence by the hard stop | No | v1 with C4 flagged as an open dependency |

**Recorded outcome:** · **Condition (verbatim, with transcript line):** · **Classification:**

---

## After each interview (10 min)

- [ ] Save the transcript to `transcripts/T<n>-<persona>.md`
- [ ] Field notes: top 3 surprises, stated numbers (to verify), contradictions, follow-ups
- [ ] Mark which hypotheses gained or lost support, citing transcript lines
- [ ] Add new questions for the next interview
- [ ] Don't open `data/released/` until both interviews are done
- [ ] Log decisions in `docs/consultant-decisions.md`
