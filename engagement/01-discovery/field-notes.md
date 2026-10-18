# Field Notes: Claims Process Discovery

> Fictional engagement for portfolio purposes. All stakeholders are synthetic.

Cite every point to a transcript line (e.g. `T1:L18`). Keep what was said
separate from what can be checked against data.

---

## T1: COO (sponsor)

### Top 3 surprises

1. **There are two approval paths.** Account managers approve claims for their own key accounts, outside the claims team, and the COO endorses this as a commercial decision (`T1:L10`). Rules may differ by customer, and the claims team may not see every decision.
2. **The sponsor wants wide autonomy for the agent.** He wants it to approve, pay and send denials on its own for everything under $50k (`T1:L12`, `T1:L34`), even though he says most claims are a few thousand dollars (`T1:L18`). That threshold covers almost everything. His own red line is a wrongful denial to a key account (`T1:L36`), and autonomous denials make that more likely.
3. **The delay may be waiting, not work.** The COO believes most of the month is hands-on work (`T1:L24`). But his own description is paperwork arriving "in dribs and drabs" and the file "sitting on someone's desk" (`T1:L26`). He also calls the finance pre-payment check "a sensible control" without saying what it catches (`T1:L26`).

Also notable: part of the motivation is a CEO-driven AI quick win (`T1:L14`), and his anticipated next question is speed to go-live (`T1:L38`). There's pressure to automate before redesigning.

### Stated numbers to verify

| Number as stated | Transcript line | How to verify |
|---|---|---|
| Claims take "a month, sometimes more" to close | `T1:L8`, `T1:L18`, `T1:L22` | `received_at` → `closed_at` in released data; median and p90 |
| "Whole days on a single file" of hands-on effort | `T1:L8`, `T1:L24` | Claims lead interview; handling-time estimates (data request §6) |
| ~70 claims/month, "800-plus a year" | `T1:L18` | Count of claims by month in released data (note: loss claims excluded from scope) |
| "Most of them are a few thousand dollars, every so often a big one" | `T1:L18`, `T1:L34` | Distribution of `amount_claimed`; share of claims over $50k |
| ~70% recovered from carriers | `T1:L18` | `amount_recovered` vs paid amounts; confirm with CFO what the 70% is a percentage of |
| Finance check takes "a day or two at most" | `T1:L26` | Event log, if the finance step is recorded (current log has no start dates; see follow-up) |
| Key account is ~9% of revenue | `T1:L14` | CFO (not in claims data) |
| Two key accounts raised claims speed in QBRs | `T1:L8`, `T1:L14` | Account managers / COO; not in claims data |
| $50k as the human-review threshold | `T1:L12` | Not data; a policy proposal to test against the claims distribution and the approval-authority matrix |

The COO says his numbers come from what he has "seen come through" and he does not stand behind them exactly (`T1:L20`). Treat all of them as unverified.

### Contradictions

- **Time spent working vs waiting:** "most of it" is someone working (`T1:L24`) vs the file "sitting on someone's desk" waiting for paperwork (`T1:L26`).
- **Who decides:** "it's her team's call" (`T1:L10`) vs account managers approving for key accounts in the same answer (`T1:L10`).
- **Agent autonomy vs his red line:** autonomous denials under $50k (`T1:L12`, `T1:L34`) vs "a key account getting a denial they shouldn't have… that's the end of it" (`T1:L36`).
- **Visible conflict vs structure:** "nothing specific comes to mind" for disagreements (`T1:L32`), yet two approval paths and finance-owned write-offs (`T1:L10`, `T1:L30`) suggest conflicts may happen below his level. This is not a direct contradiction; flag it to test with the claims lead.

### Hypotheses

| ID | Gained / lost / no change | Evidence (transcript line) |
|---|---|---|
| H1 | Gained (weak; COO perception only) | Paperwork arriving piecemeal, file "sitting on someone's desk" (`T1:L26`), despite his framing of it as work (`T1:L24`) |
| H2 | No change; candidate identified | Finance check before payment, described as "a sensible control" with no stated catch rate (`T1:L26`). Test with the claims lead and data |
| H3 | Gained (weak) | Account managers approve for key accounts (`T1:L10`); COO can't describe the detailed rules (`T1:L28`) |
| H4 | Gained | Two approval paths (`T1:L10`); write-offs sit with finance and he'd "have to check" how (`T1:L30`); no known dispute process (`T1:L32`) |
| H5 | No change (COO view contradicts it, unverified) | Recovery "basically fine" at ~70% (`T1:L18`); write-off process unknown to him (`T1:L30`) |

### Follow-ups

**Questions for the claims lead:**

- How do account-manager approvals work? How often, under what rules, where are they recorded, and does the claims team see them? (`T1:L10`)
- What does the finance check before payment look at? How often does it change or stop a payment? (`T1:L26`)
- When do documents arrive, and what does chasing them involve? (`T1:L26`)
- What makes a claim "weird"? This is the COO's intended human scope (`T1:L12`, `T1:L34`).
- How are denials decided and written? How often is a denial reversed? (`T1:L36`)
- Are carrier recoveries pursued on every eligible claim? What does "70%" refer to? (`T1:L18`)
- How often does a claim exceed $50k, and who approves those today? (`T1:L12`)

**Fields for the follow-up data request:**

- Approver role on each decision (claims team vs account manager), since `assigned_role` was withheld
- Key-account flag or customer tier
- Finance-check step: start and completion timestamps, and outcome (passed, changed, rejected)
- Document receipt timestamps per document type
- Denial reversals or appeals
- Carrier-recovery eligibility flag, so the recovery rate has a defined denominator
- Write-off records (from finance)

---

## T2: Claims and dispatch lead (process owner)

### Top 3 surprises

1. **Insurer constraints rule out the COO's autonomy threshold.** Any claim over the cargo-insurance deductible (believed to be ~$25k, unconfirmed) must be reported to the insurer within 30 days, and the insurer must agree before settlement. Pay first and the insurer can walk away (`T2:L16`, `T2:L48`, `T2:L62`). This already happened: a key-account claim was paid early by an account manager, the insurer was told late, and cover was declined. Two other large claims had late notice because the file sat in the queue, and the insurer reserved its rights (`T2:L16`). The COO's proposal to auto-pay up to $50k (`T1:L12`) would breach this.
2. **The finance pre-approval looks like the step to eliminate, at least below a threshold.** Every claim goes through it: any amount, any outcome, including denial letters (`T2:L18`, `T2:L60`). It sits "a week, maybe more", then waits for a weekly Thursday payment run (`T2:L26`). In the claims lead's experience it has changed the outcome only a handful of times, always on large claims (`T2:L56`). It was introduced after a single fraud case (`T2:L56`).
3. **Temperature (reefer) claims carry a hidden, time-critical edge case.** The evidence is the reefer unit's temperature download, which carriers keep for only ~72 hours after delivery. It must be requested by phone the same day the customer calls, or the carrier claim is lost (`T2:L44`). Three customers have cold-chain contract terms that make Northline liable regardless of the carrier, so those claims are paid almost regardless (`T2:L44`). None of this is written down; new staff learn it by getting it wrong (`T2:L46`).

Also notable:
- There is no written claims policy. Approval levels exist only in an old email (`T2:L14`, `T2:L36`).
- Undocumented rule: clean-POD shortages are never filed with the carrier, because carriers always deny them (`T2:L20`, `T2:L64`).
- Account-manager early payments, made before evidence is collected, kill carrier recovery (`T2:L14`, `T2:L30`, `T2:L64`).
- The claims lead sees routine work (intake, chasing, a first draft of the decision) as reasonable to automate (`T2:L58`).

### Stated numbers to verify

| Number as stated | Transcript line | How to verify |
|---|---|---|
| ~4 weeks from customer call to close | `T2:L12`, `T2:L66` | `received_at` → `closed_at` in released data; median and p90 |
| ~3 hours of hands-on work per claim | `T2:L26`, `T2:L66` | Estimate only ("nobody times it"); triangulate with team capacity and volume; confirm loaded cost with the CFO |
| ~⅓ of payouts recovered from carriers | `T2:L12`, `T2:L64` | `amount_recovered` / `amount_paid`; also against filed claims only. "Sense of it rather than a report" (`T2:L64`) |
| $10k approval line (specialists below, lead above) | `T2:L14`, `T2:L62` | The approval-levels email (`T2:L36`); handler vs `amount_claimed` in data |
| Insurance deductible ~$25k ("I think?") | `T2:L16` | CFO; insurance policy document |
| 30-day insurer notice; consent required before settlement | `T2:L16`, `T2:L48` | Insurance policy document (CFO) |
| ~72-hour reefer download window | `T2:L44` | Carrier terms; not in claims data |
| Finance pre-approval sits "a week, maybe more"; payment run weekly (Thursdays) | `T2:L18`, `T2:L26` | Decision date → paid date in released data; day-of-week of payments |
| Pre-approval changed something "on one hand" in "four years"; started 2019 | `T2:L56` | Finance records (CFO); dates conflict internally (see Contradictions) |
| Typical claim "a couple of thousand"; "a dozen or so" per half-year over $25k | `T2:L48` | Distribution of `amount_claimed`; count over $25k |
| Mix ~60% damage, ~30% shortage, ~10% loss | `T2:L50` | `claim_type` counts (loss is excluded from the release; check IT's exclusion count) |
| 3 specialists + lead; lead ~60% claims / 40% dispatch | `T2:L24` | Capacity input for business case; confirm with COO |
| Two duplicate payments last year, ~$9,400 combined; one written off | `T2:L68` | Finance write-off records (CFO) |
| Three customers with cold-chain liability terms | `T2:L44` | Contracts (COO / account managers) |

### Contradictions

**Within this interview:**

- **Pre-approval timeline:** it "started in 2019" but "in four years" it has rarely changed anything (`T2:L56`). 2019 to now is about seven years. Either the claims lead's tenure is ~4 years, or one figure is off. Clarify.
- **Escalation:** described as "mostly by value", but specialists also informally walk over and ask (`T2:L40`). Neither is recorded as an escalation, so escalation volume cannot be measured from data.

**Against T1:**

- **Carrier recovery:** COO says ~70%, "basically fine" (`T1:L18`) vs claims lead ~⅓, "less than it should be" (`T2:L12`, `T2:L64`). This is the largest gap so far; data can settle it.
- **Where the time goes:** COO says most of the month is hands-on work, "whole days on a single file" (`T1:L8`, `T1:L24`) vs the claims lead's ~3 hours of work, with the rest waiting on documents and finance (`T2:L12`, `T2:L26`, `T2:L66`).
- **Finance check:** COO says "a day or two at most… a sensible control" (`T1:L26`) vs claims lead "a week, maybe more", rarely changing anything (`T2:L26`, `T2:L56`).
- **Account-manager payments:** COO says "that's how it should be" (`T1:L10`) vs the claims lead, who says they kill recoveries and have cost insurance cover; her one change would be to stop them (`T2:L14`, `T2:L16`, `T2:L78`). This is an ownership dispute the sponsor will need to rule on.
- **Agent autonomy:** COO wants auto-approve, pay and deny under $50k (`T1:L12`, `T1:L34`) vs the claims lead, for whom denials, insurer-touching claims and temperature claims always go to a person (`T2:L16`, `T2:L58`). The insurer-consent rule above the deductible makes the $50k line unworkable as stated.
- **Disagreements:** COO says none come to mind (`T1:L32`) vs a specific, unresolved account-manager/insurer case that "is still a sore point" with the CFO (`T2:L16`).

### Hypotheses

| ID | Gained / lost / no change | Evidence (transcript line) |
|---|---|---|
| H1 | Gained (strong) | ~3 hours of work in ~4 weeks (`T2:L26`, `T2:L66`); waits on customer documents and finance pre-approval plus the weekly payment run (`T2:L18`, `T2:L26`); chasing lives in inboxes, not the tracker (`T2:L22`) |
| H2 | Gained | Finance pre-approves every claim and letter, any amount (`T2:L18`, `T2:L60`); rarely changes anything, only on big ones (`T2:L56`); content of the check unknown to the claims team (`T2:L54`). Needs data and the CFO to confirm |
| H3 | Gained | No written policy; rules learned on the job (`T2:L36`, `T2:L46`); missing-document fallback is "judgment" (`T2:L34`); account managers pay key customers outside the rules (`T2:L14`, `T2:L38`) |
| H4 | Gained (strong) | Account managers pay outside the process, and the team finds out afterwards (`T2:L14`, `T2:L52`, `T2:L54`); write-offs owned by finance and opaque to the claims team (`T2:L68`); claims lead claims payout ownership (`T2:L14`, `T2:L78`) |
| H5 | Gained | Recovery ~⅓, "less than it should be" (`T2:L12`, `T2:L64`); recoveries lost to early payments without evidence (`T2:L14`, `T2:L64`), late insurer notice (`T2:L16`) and missed reefer windows (`T2:L44`); labour comparatively small at ~3 hours per claim (`T2:L66`) |

### Follow-ups

**Questions for the CFO (Day 3):**

- Deductible amount, notice period and consent terms in the cargo insurance policy (`T2:L16`, `T2:L76`)
- What the AP pre-approval checks, how often it changes or stops a payment, and its turnaround (`T2:L54`, `T2:L56`)
- How recovery is measured, if at all, and what the COO's 70% refers to (`T1:L18`, `T2:L64`)
- How write-offs are decided and recorded, including the duplicate-payment case (`T2:L68`)
- The declined insurer claim: amount, and whether it was written off (`T2:L16`)

**Fields for the follow-up data request:**

- Paid-by role and payment date, so early account-manager payments can be compared with the docs-complete date (`T2:L14`, `T2:L54`)
- Carrier claim filed (Y/N), filed date, and reason not filed (e.g., clean POD, no evidence) (`T2:L20`, `T2:L64`)
- Insurer notice date, consent date and insurer outcome, for claims over the deductible (`T2:L16`, `T2:L48`)
- Pre-approval sent and returned dates, and whether anything changed (`T2:L18`, `T2:L56`)
- Temperature/reefer flag, download-requested date, and cold-chain customer flag (`T2:L44`)
- Withdrawn indicator or closing note (`T2:L70`)
- Denial reversals (`T2:L60`)
- Documents: copy of the approval-levels email (`T2:L36`); insurance policy terms (CFO)

**Scope decision needed:** loss claims (~10%) run through the same team and process (`T2:L50`). Rule on whether to keep them out of scope (SOW §3), and log the ruling in `docs/consultant-decisions.md`.