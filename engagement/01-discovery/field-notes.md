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

1.
2.
3.

### Stated numbers to verify

| Number as stated | Transcript line | How to verify |
|---|---|---|
| | | |

### Contradictions

Within this interview, and against T1.

-

### Hypotheses

| ID | Gained / lost / no change | Evidence (transcript line) |
|---|---|---|
| H1 | | |
| H2 | | |
| H3 | | |
| H4 | | |
| H5 | | |

### Follow-ups

**Fields for the follow-up data request:**

-