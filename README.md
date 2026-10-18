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

**Day 1, redesign step.** Branch `day1/discovery`.

### Done

- [x] Repo scaffold, sealed world and seal (`SEAL.sha256`, tag `seal-day1`)
- [x] `/interview` skill (closes on "end interview" in plain text)
- [x] [SOW](engagement/01-discovery/sow.md), with stakeholder map, baselines and acceptance criteria
- [x] [Data request](engagement/01-discovery/data-request.md), with hypotheses H1–H5 mapped to fields; one follow-up request allowed
- [x] [IT data release 1](data/released/README.md): damage and shortage claims plus an event log, with a cover note on what could not be supplied
- [x] [Interview guide](engagement/01-discovery/interview-guide.md), with shared comparable questions and T1 follow-ups
- [x] Interviews: [T1, COO](engagement/01-discovery/transcripts/T1-coo.md) and [T2, claims lead](engagement/01-discovery/transcripts/T2-claims-lead.md)
- [x] [Field notes](engagement/01-discovery/field-notes.md)
- [x] [Data-vs-claims checks](analysis/data_checks.py) → [results](analysis/results.md) (Q1–Q14)
- [x] [Discovery synthesis](engagement/01-discovery/synthesis.md): findings F1–F8, an 18-claim data check, contradictions, data gaps
- [x] Draft [current-state swimlane](engagement/02-redesign/current-state-swimlane.md)
- [x] Consultant rulings C1–C6 (contradictions) and E1–E6 (eliminate or redesign), logged in [`consultant-decisions.md`](docs/consultant-decisions.md)
- [x] [Future-state inputs](engagement/02-redesign/future-state-inputs.md): checklist and open dependencies D1–D8

### Open before Day 1 closes

- [ ] Rule on the three C5 open points (partial approvals ≤ $10k, approvals ≤ $10k with incomplete documents, which special flags apply)
- [ ] Rule on loss-claim scope (SOW §3)
- [ ] Correct the current-state swimlane
- [ ] Write the follow-up data request (`data-request-2.md`); Claude cuts release 2
- [ ] Future-state swimlane, decision tree with confidence thresholds and escalation triggers, three-tier scope table

### Carried to Day 3 (CFO)

Deductible amount, removal of finance pre-approval at or below $10k, the
recovery-rate definition, the late-notice discrepancy, and any challenge to
the provisional $10k thresholds. COO ratification of payout ownership is due
before requirements v1 is frozen. See D1–D8 in
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
```

The data checks use only the standard library. `requirements.txt` pins the
packages the Day 2 spike and Day 3 ROI model will need.

## Suggestions

Ideas Claude raised while drafting this README. None is adopted unless the
consultant says so.

1. **Commit the citation checker.** Citations were checked during the session
   with one-off scripts: every `T<n>:L<line>` resolves to an interviewee line,
   and every `Q<n>` exists in the results. A small committed
   `analysis/check_citations.py` would make the "cite everything" and "0
   unsupported numbers" metrics reproducible for anyone reviewing the repo.
2. **Render-check the Mermaid swimlanes.** The current-state diagram has not
   been rendered. GitHub's preview or `mmdc` would catch syntax errors before
   the future-state version builds on it.
3. **One `make check` target.** Seal verification, data checks and the
   citation check in one command, so a reviewer can confirm the repo's state
   in one step.
4. **State the main session's exposure plainly.** The sealed-world design
   limits what the main session saw, but it did read each persona brief while
   playing that persona, and the full dataset's columns and field values when
   cutting the release. The delivery log records this. Repeating it in the Day
   3 miss review would make the scoring more credible.
5. **Time-box the remaining Day 1 rulings.** The future-state swimlane, decision
   tree and scope table all depend on the C5 open points and the loss-claim
   ruling. Settling those first unblocks everything else on the list.
6. **Plan for the eval set's size.** About 20 claims gives a directional
   result (SOW deliverable #4). Choosing the eval claims to cover every C5
   tier and every escalation trigger matters more than adding claims.

## License

[MIT](LICENSE).
