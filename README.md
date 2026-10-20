# process-to-agent

> **Synthetic project.** Northline Freight, its people and its data are fictional. This is a portfolio project showing AI-assisted consulting delivery, and it says so plainly.

A three-day simulated consulting engagement, run end to end with Claude Code.
A fictional logistics client asks for "an AI agent that handles freight damage
and shortage claims." The engagement tests whether that is the right answer,
redesigns the process first, and only then specifies, prototypes and costs an
agent.

The consultant (repo owner) owns every judgment call. Claude does production
work and plays the client's stakeholders, the IT data team and the
forward-deployed engineer. Both sides of that split are logged.

## Headline results

Reported on Day 3, misses included. Targets are fixed in advance.

| Metric | Target | Result |
|---|---|---|
| Planted findings discovered | ≥ 4 of 5–6 | Pending seal reveal (Day 3) |
| Cold-FDE real-gap questions on requirements v2 | 0 (v1 count reported too) | Pending (Day 2) |
| Eval pass rate, recommended model | ≥ 85% | Pending (Day 2) |
| Escalation correctness | 100% of must-escalate claims | Pending (Day 2) |
| Cost per claim and latency | Reported for both models | Pending (Day 2) |
| ROI structural revisions after CFO defence | 0 | Pending (Day 3) |
| Unsupported numbers in deliverables | 0 | Pending (Day 3) |

Scoring method and results: [`docs/scoring.md`](docs/scoring.md).

## How it works

### The setup

- **Client:** Northline Freight, a fictional mid-size third-party logistics
  (3PL) company.
- **Ask:** an AI agent for damage and shortage claims.
- **Delivery model:** two-in-a-box. The consultant owns the *what* and *why*;
  Claude, as forward-deployed engineer, owns the *how*.
- **Stakeholders:** COO (sponsor) and claims lead, interviewed on Day 1; CFO,
  as challenger in the Day 3 business-case defence. All are played by Claude
  through the `/interview` skill.
- **Data:** a synthetic 6-month claims dataset, released by "IT" only against
  a written data request, and cut to the fields actually requested.

### The sealed world

The test is whether discovery finds what is really there, so the answers are
hidden before the engagement starts.

1. On Day 1 a **subagent** wrote the persona briefs, the full dataset and a
   ground-truth file of planted findings into `sealed/`. The main session
   never authored them.
2. `sealed/` is gitignored. Its SHA-256 hashes are committed in
   [`SEAL.sha256`](SEAL.sha256) (tag `seal-day1`), so any later change is
   detectable.
3. The main session reads a persona brief only while playing that persona,
   and the full dataset only to cut a data release. It never reads the ground
   truth before the Day 3 reveal.
4. On Day 3, `sealed/` is un-ignored, the hashes are re-verified, and findings
   are scored as found, partial or missed.

The planted findings cover five categories: waste to eliminate, an ownership
conflict, a stated rule the data contradicts, a hidden edge case known to one
person, and a feasibility trap (something the client wants automated that
should stay with a human).

### Ground rules

- **No invented numbers.** Every figure comes from a transcript, the released
  data, a spike run, or a labelled assumption.
- **Cite everything.** Findings cite a transcript line (`T2:L56`) or a query in
  `analysis/` (`Q5`).
- **Calculations in code.** Data checks, spike metrics and the ROI model run in
  Python and are reproducible.
- **Requirements freeze.** v1 is frozen before the cold-engineer handoff test;
  revisions go to v2, and both are kept.
- **Spend control.** The prototype eval runs on its own API key with a capped
  budget; each run logs tokens and cost.
- **Two logs:** [`docs/ai-assisted-delivery.md`](docs/ai-assisted-delivery.md)
  (what Claude did, which model, which files) and
  [`docs/consultant-decisions.md`](docs/consultant-decisions.md) (every ruling,
  and every place the consultant overruled Claude).

Full rules: [`CLAUDE.md`](CLAUDE.md).

### The three days

| Day | Theme | Consultant | Claude |
|---|---|---|---|
| 1 | Discovery and redesign | SOW, data request, interview guide, interviews, field notes, contradiction rulings, "eliminate, don't automate" calls, future-state process, decision logic, scope table | Scaffold, sealed world (subagent), `/interview` skill, persona play, data release, critique, cited synthesis, data-vs-claims check, current-state swimlane |
| 2 | Requirements and spike | Requirements v1, expected outcomes for ~20 eval claims, spike design, model recommendation | `claims-agent` Skill built from v1, eval harness, two-model run, decision traces, sign-off queue view, cold-engineer handoff test |
| 3 | Business case and ship | ROI structure and assumptions, CFO defence, platform ADR, exec memo | ROI model in Python → `.xlsx`, CFO persona, seal reveal and scoring, README |

## Current status

**Day 2 in progress.** Branch `day2/requirements`. The redesign is complete
and tested; requirements v1 and the spike have not started. Next: COO
ratification session, then requirements v1.

### Day 1 deliverables

- [x] Repo scaffold, sealed world and seal (`SEAL.sha256`, tag `seal-day1`)
- [x] `/interview` skill (closes on "end interview" in plain text)
- [x] [SOW](engagement/01-discovery/sow.md), with stakeholder map, baselines and acceptance criteria
- [x] [Data request 1](engagement/01-discovery/data-request.md), with hypotheses H1–H5 mapped to fields
- [x] [IT data release 1](data/released/README.md): damage and shortage claims plus an event log
- [x] [Interview guide](engagement/01-discovery/interview-guide.md), with shared comparable questions and T1 follow-ups
- [x] Interviews: [T1, COO](engagement/01-discovery/transcripts/T1-coo.md) and [T2, claims lead](engagement/01-discovery/transcripts/T2-claims-lead.md)
- [x] [Field notes](engagement/01-discovery/field-notes.md)
- [x] [Data-vs-claims checks](analysis/data_checks.py) → [results](analysis/results.md) (Q1–Q14)
- [x] [Discovery synthesis](engagement/01-discovery/synthesis.md): findings F1–F8, contradictions, data gaps
- [x] [Current-state swimlane](engagement/02-redesign/current-state-swimlane.md)
- [x] Rulings C1–C6, E1–E6, C5a–c and S1, logged in [`consultant-decisions.md`](docs/consultant-decisions.md)
- [x] [Data request 2](engagement/01-discovery/data-request-2.md) and [IT data release 2](data/released/README-release-2.md)
- [x] [Future-state swimlane](engagement/02-redesign/future-state-swimlane.md), [decision tree](engagement/02-redesign/decision-tree.md) and [scope table](engagement/02-redesign/scope-table.md)
- [x] [Coverage test](engagement/02-redesign/coverage-test.md): at Day 1 close, 9 of 10 combinations landed in one tier; the loss claim landed in none

### Day 2 progress

- [x] Rulings G1–G13 close every open gap in [`open-gaps.md`](engagement/02-redesign/open-gaps.md): loss claims, tier precedence, the documents hold, threshold basis, the reefer trigger, key accounts, tier operations, autonomous actions, insurer controls, re-routing, confidence gates, withdrawals and the duplicate check
- [x] [Coverage test](engagement/02-redesign/coverage-test.md): 0 gaps across 10 combinations and 7 probes
- [x] Data checks Q15–Q19: threshold basis, reefer vs temperature claims, insurer clock start, clean-POD recovery, document completion times
- [x] **Clean-POD rule reversed (E6a).** The stated rule that carriers deny clean-POD shortages every time is contradicted by release 2 (Q18)
- [x] `FALLBACK_DEADLINE_DAYS` set to 14 days (Q19)
- [x] Sponsor summaries: [Day 1](engagement/00-governance/sponsor-summary-day1.md) (issued a day late) and [Day 2](engagement/00-governance/sponsor-summary-day2.md)
- [ ] COO ratification of payout ownership and the expedite path (D5), via `/interview coo`, before the v1 freeze
- [ ] Data request 2 §5 (claims lead), still unanswered: approval email, filing-window rule, packaging rule, reefer logging, denial reversals, late notices
- [ ] Requirements v1 and eval set; freeze (tag `requirements-v1`)
- [ ] Cold-FDE handoff test on v1
- [ ] `claims-agent` Skill, eval harness, two-model run, confidence-threshold calibration
- [ ] Requirements v2 and second handoff test (tag `requirements-v2`)

### Carried to Day 3 (CFO)

Deductible amount, removal of finance pre-approval at or below $10k, the
recovery-rate definition, the late-notice discrepancy, any challenge to the
provisional $10k thresholds, when the insurer's 30-day notice period starts,
and data request 2 §6 (finance inputs). See D1–D9 in
[`future-state-inputs.md`](engagement/02-redesign/future-state-inputs.md).

## Repository map

```
process-to-agent/
├── CLAUDE.md                 # engagement rules and plan (read first)
├── SEAL.sha256               # hashes of sealed/, committed Day 1
├── sealed/                   # gitignored until the Day 3 reveal
├── .claude/skills/
│   ├── interview/            # /interview <persona>; "end interview" to close
│   └── claims-agent/         # Day 2: single source of the agent prompt
├── engagement/
│   ├── 00-governance/        # daily sponsor summaries
│   ├── 01-discovery/         # SOW, data request, guide, transcripts, field notes, synthesis
│   ├── 02-redesign/          # swimlanes, future-state inputs, decision logic, scope table
│   ├── 03-requirements/      # Day 2: v1/, v2/, handoff tests
│   ├── 04-business-case/     # Day 3: ROI model, CFO Q&A
│   └── 05-readout/           # Day 3: exec memo, platform ADR
├── spike/                    # Day 2: eval set, harness, traces, results
├── analysis/                 # data-vs-claims queries and generated results
├── data/released/            # IT data releases and cover notes
└── docs/                     # delivery log, decisions log, scoring
```

## Reproduce

Python 3.11+.

```bash
# Verify the seal (works once sealed/ is present locally)
shasum -a 256 -c SEAL.sha256

# Re-run the data-vs-claims checks; regenerates analysis/results.md
python analysis/data_checks.py

# Rebuild data release 1 from the sealed extract (needs sealed/; after the reveal for anyone but the owner)
python data/released/build_release.py

# Rebuild data release 2 (same conditions as release 1)
python data/released/build_release_2.py

# Re-run the future-state coverage test; regenerates engagement/02-redesign/coverage-test.md
python engagement/02-redesign/coverage_test.py
```

The data checks use only the standard library. `requirements.txt` pins the
packages the Day 2 spike and Day 3 ROI model will need.

## License

[MIT](LICENSE).
