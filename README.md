# process-to-agent

A simulated consulting engagement, run end to end with Claude Code: a fictional logistics company asks for an AI claims agent, and the consultant diagnoses, plans, builds and tests it.

> **Synthetic project.** Northline Freight, its people and its data are fictional. This is a portfolio project showing AI-assisted consulting delivery, and it says so plainly.

## What it does

A fictional third-party logistics (3PL) company, Northline Freight, asks for "an AI agent that handles freight damage and shortage claims." The engagement runs as **diagnose → plan → build → test**: discovery and process redesign first, then requirements, then a prototype agent tested on two models. The consultant (repo owner) owns every judgment call. Claude does production work and plays the stakeholders, IT and the forward-deployed engineer. Both sides of that split are logged.

## How it was built

- **Claude Code** as the working environment. Which model did what is in the [delivery log](docs/ai-assisted-delivery.md).
- **Claude-played stakeholder interviews**, through the [`/interview` skill](.claude/skills/interview/SKILL.md): [COO](engagement/01-discovery/transcripts/T1-coo.md), [claims lead](engagement/01-discovery/transcripts/T2-claims-lead.md) and a [COO ratification session](engagement/01-discovery/transcripts/T3-coo.md). The answers were sealed in advance ([SEAL.sha256](SEAL.sha256)).
- **Data-vs-claims checks in Python**: [`analysis/data_checks.py`](analysis/data_checks.py), results in [`analysis/results.md`](analysis/results.md).
- **Rulings logged**: every consultant decision, with rejected options, in [`docs/consultant-decisions.md`](docs/consultant-decisions.md). What Claude did is in [`docs/ai-assisted-delivery.md`](docs/ai-assisted-delivery.md).
- **Requirements v1, frozen** (tag `requirements-v1`): [`engagement/03-requirements/v1/`](engagement/03-requirements/v1/).
- **Cold-FDE handoff test**: a fresh subagent that can read only v1 lists what it would need to ask the business: [`handoff-v1.md`](engagement/03-requirements/handoff-v1.md).
- **`claims-agent` Skill**, built only from v1: [`.claude/skills/claims-agent/SKILL.md`](.claude/skills/claims-agent/SKILL.md).
- **Python eval harness on two models**: [`spike/run_eval.py`](spike/run_eval.py), with deterministic scoring and no LLM judge. Design in [`spike/README.md`](spike/README.md), expected outcomes written by the consultant before any run in [`spike/expected-outcomes-v1.md`](spike/expected-outcomes-v1.md).

## Headline numbers

Sonnet 5.5 and Haiku 5.5, effort `medium`, 78 snapshots each (39 cases × 2). Source: [`spike/metrics.md`](spike/metrics.md), generated from the full runs. Sample and constructed cases are never combined into one figure (EV3).

| Metric | Sonnet 5.5 | Haiku 5.5 | Caveat |
|---|---|---|---|
| Routing pass rate (headline) | Sample 33/33 · info gap 8/8 · constructed 18/18 | Sample 33/33 · info gap 8/8 · constructed 18/18 | Headline is routing on escalate, hold and sign-off snapshots. **Gate-held (R14) cases are excluded** (EV9). It includes intake snapshots (all passed, both models) as well as decision-point snapshots; the split is in [`metrics.md`](spike/metrics.md#what-the-headline-contains) |
| Must-escalate routed to escalate | 10/10 sample · 9/9 constructed | 10/10 sample · 9/9 constructed | 19/19 for both. 0 escalations when not expected |
| Cost per claim (2 snapshots) | $0.02407 | $0.00233 | Prices from `PRICES` in `spike/run_eval.py`. Whole run: $0.9386 and $0.0909 |
| Latency p50 / p95 | 5.3s / 12.4s | 7.9s / 14.1s | Per evaluation |
| Failures | None | 1 `wrong_rule`: `NLC-26-0053`, draft `deny` through R10 instead of the R14 gate | Right tier, wrong scope-table row; still a fail (E-a). Carried to v2 as gap EG1 ([`v2-gaps.md`](engagement/03-requirements/v2-gaps.md)) |
| Output-rule violations | 0 | 1: `NLC-26-0052`, rubric score 0.33 does not match 3/6 rounded | Reported, not scored |
| Autonomous tier | Untested on released data | Untested on released data | The release holds no document content (photos, BOL, POD) and no shipment record, so the rubric cannot pass on sample cases. Reported on their own line: 19 autonomous* snapshots on Sonnet, all gate-held; Haiku 18 gate-held and 1 other |
| Info-gap cases | 8 reported separately | 8 reported separately | Their snapshots lack the evidence behind the historical outcome (salvage, shipment record, filing-window rule). An `approve` there would pay what the historical team reduced or denied (E-c) |
| Cold-FDE on v1 | 56 questions | | Real-gap count pending: the consultant has not classified them. v2 and the rerun are not done |
| Model recommendation | Pending (consultant) | | Not written yet |

Targets and scoring method: [`docs/scoring.md`](docs/scoring.md).

## What broke and what changed

- **A stated rule was reversed by the data.** The claims lead said carriers deny clean-POD shortages; release 2 showed they often pay (Q18). Ruling E6 became E6a: file them. [E6a](docs/consultant-decisions.md#e6a-file-clean-pod-shortages-with-the-carrier) · [Q18](analysis/results.md)
- **No single filing window fits the history.** Twelve filing-window denials cannot be separated from other claims on any date basis (Q21), so the 270-day window in v1 is an assumption raised as D13. [V2](docs/consultant-decisions.md#v1-values-day-2-v1v24-e-a-to-e-d) · [Q21](analysis/results.md)
- **The design docs contradicted the rulings before v1.** Aligned by G14–G18, so v1 cites rulings and does not resolve contradictions inline. [G14–G18](docs/consultant-decisions.md#pre-v1-rulings-day-2-design-doc-alignment-document-checklist-eval-design)
- **The `/end` interview trigger collided with Claude Code slash commands.** The skill now closes on "end interview" in plain text. [Delivery log, 2026-10-17](docs/ai-assisted-delivery.md) · [skill](.claude/skills/interview/SKILL.md)
- **The spike key is kept out of Claude Code's reach.** It is named `SPIKE_ANTHROPIC_API_KEY`, never `ANTHROPIC_API_KEY`, so sessions cannot bill to it. [`CLAUDE.md` rule 8](CLAUDE.md) · [`.env.example`](.env.example)
- **The ratification close missed "cannot approve".** It restated "owns every payout" but not the second verb. Mitigated by the COO's written confirmation. [D5h](docs/consultant-decisions.md#d5h-cannot-approve-treated-as-covered) · [miss review](docs/scoring.md)

## Status

| | |
|---|---|
| **Done** | Day 1 discovery and redesign. Requirements v1 (frozen). Cold-FDE test on v1. Claims-agent Skill. Two-model eval run |
| **Not done** | Requirements v2 and the cold-FDE rerun. Business case, CFO defence, platform ADR, exec memo |
| **Sealed** | Hashed on Day 1 in commit `edb23fe` (tag `seal-day1`), [`SEAL.sha256`](SEAL.sha256). Not opened. The reveal and scoring come after the business case |
| **Open for the consultant** | Classify the 56 cold-FDE questions as real gap or noise. Rule on EG1. Write the model recommendation. Confirm the drafted rationale on EV8–EV14 |

Branch `day2/requirements`. Planted findings, v2 gap count and ROI results are pending.

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
| 2 | Requirements and spike | Requirements v1, expected outcomes for the eval cases (39 cases, 78 snapshots), spike design, model recommendation | `claims-agent` Skill built from v1, eval harness, two-model run, decision traces, sign-off queue view, cold-engineer handoff test |
| 3 | Business case and ship | ROI structure and assumptions, CFO defence, platform ADR, exec memo | ROI model in Python → `.xlsx`, CFO persona, seal reveal and scoring, README |

## Current status

**Day 2, after the spike run and before v2.** Branch `day2/requirements`. The
redesign and requirements v1 are done and frozen, the claims-agent Skill is
built, and both models have been run. Next: classify the cold-FDE questions,
rule on EG1, write the model recommendation, then v2. The top of this README
has the numbers and the full done and not-done list.

### Day 1 deliverables

- [x] Repo scaffold, sealed world and seal (`SEAL.sha256`, tag `seal-day1`)
- [x] `/interview` skill (closes on "end interview" in plain text)
- [x] [SOW](engagement/01-discovery/sow.md), with stakeholder map, baselines and acceptance criteria
- [x] [Data request 1](engagement/01-discovery/data-request.md), with hypotheses H1–H5 mapped to fields
- [x] [IT data release 1](data/released/README.md): damage and shortage claims plus an event log
- [x] [Interview guide](engagement/01-discovery/interview-guide.md), with shared comparable questions and T1 follow-ups
- [x] Interviews: [T1, COO](engagement/01-discovery/transcripts/T1-coo.md) and [T2, claims lead](engagement/01-discovery/transcripts/T2-claims-lead.md)
- [x] [Field notes](engagement/01-discovery/field-notes.md)
- [x] [Data-vs-claims checks](analysis/data_checks.py) → [results](analysis/results.md) (Q1–Q14 on Day 1; extended to Q21 on Day 2)
- [x] [Discovery synthesis](engagement/01-discovery/synthesis.md): findings F1–F8, contradictions, data gaps
- [x] [Current-state swimlane](engagement/02-redesign/current-state-swimlane.md)
- [x] Rulings C1–C6, E1–E6, C5a–c and S1, logged in [`consultant-decisions.md`](docs/consultant-decisions.md)
- [x] [Data request 2](engagement/01-discovery/data-request-2.md) and [IT data release 2](data/released/README-release-2.md)
- [x] [Future-state swimlane](engagement/02-redesign/future-state-swimlane.md), [decision tree](engagement/02-redesign/decision-tree.md) and [scope table](engagement/02-redesign/scope-table.md)
- [x] [Coverage test](engagement/02-redesign/coverage-test.md): at Day 1 close, 9 of 10 combinations landed in one tier; the loss claim landed in none

### Day 2 progress

- [x] Rulings G1–G13 close every open gap in [`open-gaps.md`](engagement/02-redesign/open-gaps.md): loss claims, tier precedence, the documents hold, threshold basis, the reefer trigger, key accounts, tier operations, autonomous actions, insurer controls, re-routing, confidence gates, withdrawals and the duplicate check
- [x] [Coverage test](engagement/02-redesign/coverage-test.md): 0 gaps across 10 combinations and 7 probes
- [x] Data checks Q15–Q21: threshold basis, reefer vs temperature claims, insurer clock start, clean-POD recovery, document completion times, documents missing on complete claims, filing-window denials
- [x] **Clean-POD rule reversed (E6a).** The stated rule that carriers deny clean-POD shortages every time is contradicted by release 2 (Q18)
- [x] `FALLBACK_DEADLINE_DAYS` set to 14 days (Q19)
- [x] Sponsor summaries: [Day 1](engagement/00-governance/sponsor-summary-day1.md) (issued a day late) and [Day 2](engagement/00-governance/sponsor-summary-day2.md)
- [x] COO ratification of payout ownership and the expedite path (D5): [T3](engagement/01-discovery/transcripts/T3-coo.md) and written replies, in [`engagement/00-governance/`](engagement/00-governance/)
- [ ] Data request 2 §5 (claims lead), still unanswered: approval email, filing-window rule (D13), packaging rule, reefer logging, denial reversals, late notices
- [x] [Requirements v1](engagement/03-requirements/v1/) and eval set; frozen (tag `requirements-v1`)
- [x] [Cold-FDE handoff test on v1](engagement/03-requirements/handoff-v1.md): 56 questions
- [ ] Classify the 56 questions as real gap or noise (consultant)
- [x] `claims-agent` Skill, eval harness and two-model run: [`spike/metrics.md`](spike/metrics.md)
- [ ] Rule on EG1, write the model recommendation ([`spike/results.md`](spike/results.md)), confirm the drafted rationale on EV8–EV14
- [ ] Confidence-threshold calibration (inputs in [`spike/metrics.md`](spike/metrics.md))
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
│   └── claims-agent/         # single source of the agent prompt
├── engagement/
│   ├── 00-governance/        # sponsor summaries and follow-up notes
│   ├── 01-discovery/         # SOW, data request, guide, transcripts, field notes, synthesis
│   ├── 02-redesign/          # swimlanes, future-state inputs, decision logic, scope table
│   ├── 03-requirements/      # v1/ (frozen), v2/ (empty), handoff-v1.md, v2-gaps.md
│   ├── 04-business-case/     # Day 3: ROI model, CFO Q&A
│   └── 05-readout/           # Day 3: exec memo, platform ADR
├── spike/                    # eval set, harness, traces, queues, metrics, results
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

# Rebuild the eval set (78 snapshots) from the released data and the expected outcomes
python spike/build_eval_set.py

# Regenerate spike/metrics.md and the sign-off queue views from the stored runs (no API calls)
python spike/report.py

# Run the eval on one model. Calls the API and spends money: needs SPIKE_ANTHROPIC_API_KEY in .env
python spike/run_eval.py --model claude-sonnet-5-5 --effort medium --smoke   # 3 snapshots first
python spike/run_eval.py --model claude-sonnet-5-5 --effort medium
```

The data checks use only the standard library. The spike needs the packages in
`requirements.txt`, and the Day 3 ROI model will use them too.

## License

[MIT](LICENSE).
