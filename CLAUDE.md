# CLAUDE.md — process-to-agent

## What this project is

A 3-day simulated consulting engagement, run with Claude Code. A fictional
logistics client wants an AI agent to handle freight claims. I act as the AI
lead consultant and technical product owner. My job is to:

1. Run discovery and decide what should be automated, redesigned, or eliminated.
2. Define the agent's decision logic and human sign-off boundaries.
3. Write requirements an engineer can build from without clarification.
4. Prototype the agent, test it on two models, and measure quality and cost.
5. Build and defend a business case.
6. Document which components are reusable platform pieces and which are one-offs.

Everything is synthetic. The client, people and data are fictional. This is a
portfolio project showing AI-assisted delivery, and it says so plainly.

## The client

**Northline Freight** is a fictional mid-size third-party logistics (3PL)
company. Its ask: "Build us an AI agent that handles freight damage and
shortage claims." The engagement runs two-in-a-box: I own the what and why,
and Claude plays the forward-deployed engineer (FDE) who owns the how.

### Stakeholders (played by Claude via `/interview`)

| Persona | Session | Role in the story |
|---|---|---|
| COO (sponsor) | Day 1 | Wants the agent; believes claims are slow because staff are slow |
| Claims and dispatch lead | Day 1 | Owns the day-to-day; knows the workarounds and edge cases |
| CFO | Day 3 | Challenger; tests the ROI model and model-cost assumptions |

IT is not a persona. IT's role is a data release: a synthetic 6-month claims
dataset (~400 claims), released to `data/released/` only after I submit a
written data request.

## Roles

**I own every judgment call.** Claude does production work and logs it.

| I own | Claude does |
|---|---|
| SOW with stakeholder map, interview guide, data request | Repo scaffold, world-building and seal (via subagent) |
| Interviews, field notes | Persona play, data release |
| Contradiction rulings, the "eliminate, don't automate" call | Cited synthesis, data-vs-claims check, swimlane drafts |
| Future-state process, decision logic, scope table | Critique of my logic; flags gaps |
| User stories, acceptance criteria, edge cases, eval expected outcomes | Claims-agent Skill built from my requirements |
| Spike design: which models, which metrics, the pass bar | Eval harness, two-model run, decision trace, sign-off queue view |
| Model recommendation, platform ADR | Cost and latency tables |
| ROI structure, baselines, assumptions | Python ROI model -> .xlsx, sensitivity, payback |
| Exec memo, CFO defence | Cold-FDE subagent, CFO persona, README draft |

When Claude reaches a decision that belongs to me, it stops and asks. It
does not decide on my behalf and record that as my decision.

## Ground rules (non-negotiable)

1. **Sealed world.**
   - `sealed/` holds persona briefs, ground truth (planted findings), and the
     full dataset. It is gitignored until the Day 3 reveal.
   - On Day 1 its contents are hashed into `SEAL.sha256`, which is committed.
   - A subagent writes the sealed world, so the main session never authors
     the ground truth.
   - The main session may read persona briefs only while running `/interview`
     in character, and the dataset only to produce the release.
   - Claude never reads `sealed/ground-truth.md` before the reveal.
   - Claude never hints at, summarizes, or steers me toward sealed contents.
   - Personas answer only what they are asked, in character, and do not
     volunteer findings.
2. **No invented numbers.** Every figure comes from a transcript, the released
   dataset, a spike run, or an assumption I set and label. If a number is
   missing, Claude asks for it.
3. **Cite everything.** Findings cite a transcript line (`T1:L41`) or a
   dataset query in `analysis/`. Uncited claims get flagged, not written.
4. **Calculations in code.** No arithmetic in prose. ROI, data checks and
   spike metrics run in Python and are reproducible.
5. **Synthetic, stated plainly.** README and every client-facing deliverable
   carry a one-line note that the client and data are fictional.
6. **Two logs, updated at the end of every session.**
   - `docs/ai-assisted-delivery.md`: what Claude did, which model, which files.
   - `docs/consultant-decisions.md`: where I overruled, corrected, or chose
     against Claude, and why. Claude drafts entries; I confirm the wording.
7. **Requirements freeze.** Requirements v1 is frozen before the cold-FDE test.
   It is not edited during the test. Revisions go to v2, and both are kept.
8. **Spike spend control.** The spike uses its own API key, stored as
   `SPIKE_ANTHROPIC_API_KEY` in `.env` at the repo root and loaded by
   `spike/run_eval.py` via `python-dotenv`. It is never exported to the
   shell, never committed, and never named `ANTHROPIC_API_KEY` (so Claude
   Code doesn't pick it up and bill sessions to it). The key lives in a
   dedicated Console workspace with a monthly spend limit. Each eval run
   logs token usage and cost, and before any run Claude states the
   estimated cost.
9. **Models.** Opus for world-building and Day 1 synthesis; Sonnet otherwise.
   The spike compares two models I choose.
10. **No real organizations.** No real company, client, or employer names
    anywhere in the repo.

## 3-day plan

### Day 1: Discovery and redesign
- Claude:
  - Scaffold the repo.
  - Spawn a subagent to build the sealed world and write `SEAL.sha256`.
  - Create the `/interview` skill.
  - Critique my interview guide.
- Me:
  - SOW with stakeholder map and data request.
  - Interview guide.
  - Two live interviews (COO, claims lead), about 25 minutes each.
  - Field notes.
- Claude: cited synthesis, data-vs-claims check, current-state swimlane draft.
- Me:
  - Contradiction rulings.
  - The "eliminate, don't automate" call.
  - Future-state swimlane.
  - Decision tree with confidence thresholds and escalation triggers.
  - Scope table with three tiers: autonomous / human sign-off / always escalate.

### Day 2: Requirements and spike
- Me:
  - Requirements v1: user stories, acceptance criteria, edge cases.
  - Expected outcomes for about 20 eval claims.
- Claude:
  - Claims-agent Skill built from v1.
  - `spike/run_eval.py`.
  - Decision trace (JSONL) and sign-off queue view.
- Run the eval on two models: pass rate, cost per claim, latency.
- Freeze v1, run the cold-FDE test, then revise to v2.

### Day 3: Business case and ship
- Me: ROI structure and assumptions.
- Claude: Python model -> `.xlsx`, with three scenarios that use spike costs, plus payback and sensitivity.
- CFO interview as the defence; log every challenge and answer.
- Me:
  - Platform ADR: reusable vs claims-specific components, and data-residency / sovereign deployment considerations.
  - One-page exec memo with a pilot recommendation.
- Seal reveal and scoring, then a miss review.
- Claude drafts the README. Publish.

## Sealed world specification (for the world-building subagent)

Plant 5–6 findings across these categories. Each needs evidence hidden in
persona briefs and/or the dataset.

- **Waste to eliminate:** a step that adds no value and should be removed,
  not automated.
- **Ownership conflict:** two stakeholders disagree on who owns a decision.
- **Claim vs. data:** a rule someone states confidently that the dataset
  contradicts.
- **Hidden edge case:** known to only one persona, revealed only if asked well.
- **Feasibility trap:** something the client wants the agent to own that
  should stay with a human (judgment, liability, or compliance exposure).

Files:
- `sealed/personas/<role>.md` — background, knowledge, beliefs, blind spots,
  what they reveal only under good questioning.
- `sealed/ground-truth.md` — each finding, its evidence, and what counts as
  found vs. partial.
- `sealed/data/claims_full.csv` — full synthetic dataset.

The released dataset is a subset or cut of the full one, chosen to match the
data request I actually write.

## Skills

### `/interview <persona>`
- Claude reads only that persona's brief and answers in character, in plain
  conversational language.
- Claude does not break character to coach me.
- Claude saves the transcript with numbered lines to
  `engagement/01-discovery/transcripts/T<n>-<persona>.md`.
- The interview ends when I type `end interview` in plain text. (`/end` does not work: Claude Code reads a leading slash as a command.)

### `claims-agent`
- The prototype agent, built only from the current requirements version.
- For each claim, it outputs a structured decision:
  - `decision`
  - `rule_applied`
  - `confidence`
  - `route` (`autonomous` | `sign_off` | `escalate`)
  - `rationale`
- It never decides outside its scope table. Anything outside scope goes to
  `escalate`.

## Spike: eval harness

- `spike/eval_set.jsonl`: about 20 claims, each with my expected `decision`
  and `route`. Must-escalate cases are included.
- `spike/run_eval.py`:
  - Runs the claims-agent prompt against each model.
  - Records pass/fail per claim, input/output tokens, cost, and latency.
  - Writes a trace line per decision to `spike/traces/<model>.jsonl`.
- `spike/results.md` reports:
  - Pass rate, escalation correctness, cost per claim, and p50/p95 latency for each model.
  - My recommendation, written by me.
- `run_eval.py` loads the agent prompt directly from
  `.claude/skills/claims-agent/SKILL.md`, so the Skill and the spike never drift.  
- Scoring is deterministic: compare structured fields. No LLM-as-judge unless
  I approve it.

## Cold-FDE handoff test

- Spawn a fresh subagent (Sonnet) that can read only
  `engagement/03-requirements/v1/`.
- Prompt: "You are the engineer building this agent. List every question you
  would need the business to answer before you could build it without
  guessing."
- Save its output to `engagement/03-requirements/handoff-v1.md`.
- I classify each question as a real gap or noise. Only real gaps count.
- Revise to v2, rerun the test, and save `handoff-v2.md`.

## Success metrics (reported honestly, misses included)

| Metric | Target |
|---|---|
| Cold-FDE real-gap questions on v2 | 0 (v1 count reported too) |
| Planted findings discovered | ≥ 4 of 5–6 |
| Eval pass rate, recommended model | ≥ 85% |
| Escalation correctness | 100% of must-escalate claims routed correctly |
| Cost per claim and latency | Reported for both models |
| ROI structural revisions after CFO defence | 0 |
| Unsupported numbers in deliverables | 0 |

## Repo structure

```
process-to-agent/
├── CLAUDE.md
├── README.md                # headline numbers on the first screen
├── LICENSE                  # MIT
├── .gitignore               # sealed/, .env
├── .env                     # gitignored — SPIKE_ANTHROPIC_API_KEY
├── .env.example             # committed — variable name only, no value
├── requirements.txt         # pinned; includes anthropic, python-dotenv
├── SEAL.sha256              # committed Day 1; hash of sealed/
├── sealed/                  # gitignored until reveal
│   ├── personas/            # one brief per persona
│   ├── ground-truth.md      # planted findings; unread until reveal
│   └── data/claims_full.csv
├── .claude/skills/
│   ├── interview/           # /interview <persona>; type "end interview" to close
│   └── claims-agent/        # SKILL.md is the single source of the agent prompt
├── engagement/
│   ├── 01-discovery/        # SOW, guide, transcripts/, field notes
│   ├── 02-redesign/         # swimlanes, decision logic, scope table
│   ├── 03-requirements/     # v1/, v2/, handoff-v1.md, handoff-v2.md
│   ├── 04-business-case/    # model.py, roi.xlsx, CFO Q&A
│   └── 05-readout/          # exec memo, platform ADR
├── spike/
│   ├── eval_set.jsonl       # ~20 claims + expected decision and route
│   ├── run_eval.py          # loads prompt from claims-agent/SKILL.md
│   ├── traces/              # <model>.jsonl, one line per decision
│   └── results.md           # metrics + my recommendation
├── analysis/                # data-vs-claims queries
├── data/released/           # IT data release (subset of sealed data)
└── docs/
    ├── ai-assisted-delivery.md
    ├── consultant-decisions.md
    └── scoring.md
```

## Conventions

- Deliverables are Markdown. Diagrams use Mermaid swimlanes or flowcharts.
- Writing is consulting-grade: lead with the conclusion, short sections, no
  filler.
- Python 3.11+. Dependencies go in `requirements.txt`, with pinned versions.
- **Git is the consultant's.** Claude never commits, branches, pushes or tags.
  The consultant does all git work in GitHub Desktop.
- One branch per session, named `day<n>/<theme>` (e.g. `day1/discovery`),
  created by the consultant. One PR per session into `main`.
- At the end of each work block, Claude provides a commit summary and
  description. Summaries use conventional-commit types:
  `<type>: <what changed>`, where type is `feat`, `fix`, `docs`, `chore`,
  `refactor` or `test`. The day is carried by the branch name. At the end of each session,
  Claude provides the PR title and description.
- Suggested tags (applied by the consultant): `seal-day1` on the commit that
  adds `SEAL.sha256`; `requirements-v1` when v1 is frozen (before the
  cold-FDE test); `requirements-v2` after the v2 revision; `seal-reveal` on
  the Day 3 commit that un-ignores `sealed/`.
- Whenever a drafted commit must be tagged, Claude says so next to that
  commit, with the tag name.
- At the start of each session, Claude reads this file, both logs, and the
  latest outputs. Then it states which day and step we're on before doing
  anything.