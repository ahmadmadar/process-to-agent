# Interview Guide: Claims Process Discovery (v1)

**Engagement:** Claims-to-Agent Discovery Sprint (see SOW)
**Interviews:** COO (sponsor) first, then Claims and dispatch lead (process owner), so the second interview can test what the first one claimed. The CFO section is for Day 3.
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

### B1. Role and process walkthrough (8 min)

| # | Prompt | Tag |
|---|---|---|
| B1.1 ★ | Walk me through the last claim you handled, from the moment it arrived to the moment it closed. | H1, H2 |
| B1.2 | *Probe at each step:* Who does it? Which system or tool? What decision is made, and on what rule? | H3, H4 |
| B1.3 ★ | Which of those steps aren't recorded in the system? | H1 |
| B1.4 | Who performs each step other than the final decision? | H4 |
| B1.5 | Which roles handle claims, and how does a claim get assigned to someone? | H4 |

### B2. Waiting, documents and rework (4 min)

| # | Prompt | Tag |
|---|---|---|
| B2.1 ★ | Where does a claim wait, and who is it waiting for? | H1 |
| B2.2 | When do documents usually arrive relative to the claim? What happens when something is missing? | H1, H3 |
| B2.3 | *Probe, per step:* Why does this step exist? What would happen if it were skipped? When was it last overturned? | H2 |

### B3. Rules and exceptions (6 min)

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

### B4. Data and record-keeping (if time allows)

| # | Prompt | Tag |
|---|---|---|
| B4.1 | From receipt to close, how long does a typical claim take? How much of that is someone actually working on it, by role? How do you know? | H1, BC |
| B4.2 | How are write-offs decided, by whom, and where are they recorded? | H4, H5 |
| B4.3 | How do you decide whether to pursue the carrier for recovery? | H5 |
| B4.4 | Is a claim ever withdrawn? How is that recorded? | Data quality |
| B4.5 | Any process, system or coding changes in the last 6 months? | Data quality |
| B4.6 | Are any claims handled outside the system, for example by email or spreadsheet? | H1, Data quality |

### B5. Close (2 min)

| # | Prompt | Tag |
|---|---|---|
| B5.1 ★ | What should I have asked that I didn't? | — |
| B5.2 | If you could change one thing about the process tomorrow, what would it be? | H2 |

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

## After each interview (10 min)

- [ ] Save the transcript to `transcripts/T<n>-<persona>.md`
- [ ] Field notes: top 3 surprises, stated numbers (to verify), contradictions, follow-ups
- [ ] Mark which hypotheses gained or lost support, citing transcript lines
- [ ] Add new questions for the next interview
- [ ] Don't open `data/released/` until both interviews are done
- [ ] Log decisions in `docs/consultant-decisions.md`
