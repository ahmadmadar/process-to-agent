# Spike Results

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

## Run configuration (EV8)

| Item | Setting |
|---|---|
| Models | `claude-sonnet-5-5`, `claude-haiku-5-5`. Opus 5.5 only if Sonnet fails |
| Effort | `medium`, pinned on both models (EV8) |
| Agent prompt | `.claude/skills/claims-agent/SKILL.md`, built from requirements v1 |
| Eval set | `spike/eval_set.jsonl`, 78 snapshots (39 cases × 2) |
| Expected outcomes | `spike/expected-outcomes-v1.md` |
| Refusal fallback | Off (EV11) |

## Metrics

See `spike/metrics.md`, generated from the full runs.

## Consultant recommendation

Inputs, from `spike/metrics.md` (latest full run per model, effort `medium`). Groups are not combined (EV3). The headline excludes gate-held (R14) snapshots (EV9). The autonomous tier is untested on released data.

| | `claude-sonnet-5-5` | `claude-haiku-5-5` |
|---|---|---|
| Run | `20261027T215046-e80258` | `20261027T215318-0bee8a` |
| Headline pass: sample / info gap / constructed | 33/33 · 8/8 · 18/18 | 33/33 · 8/8 · 18/18 |
| Must-escalate routed to escalate: sample / constructed | 10/10 · 9/9 | 10/10 · 9/9 |
| Escalated when not expected | 0 | 0 |
| Failures | None | 1 `wrong_rule`: `NLC-26-0053/decision_point`, `deny` via R10 (carried to v2 as EG1) |
| Schema / v1 output-rule violations | 0 | 1: `NLC-26-0052/decision_point` |
| Refusals | 0 | 0 |
| Cost per claim (2 snapshots) | $0.02407 | $0.00233 |
| Latency p50 / p95 | 5.3s / 12.4s | 7.9s / 14.1s |

Recommendation: *(to be written by the consultant)*
