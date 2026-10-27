# Scoring

> Northline Freight is a fictional client. All people and data are synthetic.

Completed on Day 3, after the seal reveal. Results are reported honestly, misses included.

## Seal verification

Method: SHA-256 of every file under `sealed/`, sorted by path, one line per file
(`shasum -a 256` format), committed as `SEAL.sha256` on Day 1. On Day 3, rerun
the same command and diff against the committed file.

Result: _pending_

## Success metrics

| Metric | Target | Result |
|---|---|---|
| Cold-FDE real-gap questions on v2 | 0 (v1 count reported too) | _pending_ |
| Planted findings discovered | ≥ 4 of 5–6 | _pending_ |
| Eval pass rate, recommended model | ≥ 85% | _pending_ |
| Escalation correctness | 100% of must-escalate claims | _pending_ |
| Cost per claim and latency | Reported for both models | _pending_ |
| ROI structural revisions after CFO defence | 0 | _pending_ |
| Unsupported numbers in deliverables | 0 | _pending_ |

## Planted findings

| # | Category | Found / partial / missed | Evidence (transcript line or analysis query) |
|---|---|---|---|

## Miss review

Process misses logged as they occur:

- **D5 close (T3:L29–L30):** The close restated "owns every payout" but not "cannot approve". Restate both verbs at the close next time. Mitigated by the COO's written confirmation (D5h).

Full review: _pending_ (Day 3)
