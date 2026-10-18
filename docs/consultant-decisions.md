# Consultant decisions log

> Northline Freight is a fictional client. All people and data are synthetic.

Where the consultant overruled, corrected, or chose against Claude, and why.
Claude drafts entries; the consultant confirms the wording.

| Date | Day / step | Claude proposed | Consultant decided | Why |
|---|---|---|---|---|
| 2026-10-16 | Day 1 / workflow | Claude makes the commits; one branch per session with a PR at the end | One branch per session. The consultant does all git work in GitHub Desktop. Claude only drafts commit and PR text. Claude's commit on `main` was reversed and the changes moved to `day1/discovery`. | I prefer to own the version control. Keeps me honest and accountable about reviewing all the changes made by Claude throughout the session. |
| 2026-10-17 | Day 1 / SOW | Turn governance meetings that have no session in the plan into written steps, or reframe them as the consultant's rulings pending sponsor ratification | Kept the daily sponsor summary. Removed the Day 1 COO playback and the Day 3 COO/CFO readout. Accepted all other SOW fixes. | A short engagement benefits from daily visibility and clarity for the client; a longer one would use weekly summaries. The Day 3 CFO defence already covers the readout. |
| 2026-10-17 | Day 1 / data request | Keep the event log optional, with fallback fields in the claims table for H2 | Event log made required; fallback fields removed | A required event log reduces guessing on our end. |
