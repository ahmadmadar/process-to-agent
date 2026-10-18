# Statement of Work: Claims Automation Discovery and Requirements

**Client:** Northline Freight
**Engagement:** Claims-to-Agent Discovery Sprint
**Duration:** 3 working days
**Delivery model:** Two-in-a-box (AI lead consultant + forward-deployed engineer)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

---

## 1. Background

Northline Freight handles freight damage and shortage claims. Our current
understanding, to be confirmed in discovery, is that it settles claims with
customers and pursues recovery from carriers. Leadership believes claims take
too long to resolve and cost too much to process, and has asked for an AI
agent to handle them.

Discovery will establish whether the underlying problem is speed, cost,
consistency, or something else. An AI agent is one possible answer. This
engagement tests whether it is the right one, and for which parts of the
process.

## 2. Objective

Decide whether, where and how an AI agent should handle damage and shortage
claims. Where an agent is the right answer, define it precisely enough for an
engineer to build without further business clarification. Back the
recommendation with a business case the CFO can validate.

**One possible outcome is a recommendation not to automate some or all of
the current process.** Steps that add no value will be recommended for
elimination, not automation.

### Baseline measures

The business case measures change against these baselines, established from
the client's claims data. Where the data cannot support a baseline, it is
recorded as a labelled assumption.

- Claim cycle time, from receipt to closure
- Handling effort per claim
- Claim outcomes, including recovery from carriers
- Rework and exception rates

## 3. Scope

### In scope
- Current-state discovery of the damage and shortage claims process, from claim receipt to closure
- Analysis of a 6-month claims dataset provided by the client
- Future-state process redesign, including steps recommended for elimination
- AI agent decision logic and scope boundaries: what it handles on its own, what requires human sign-off, and what is always escalated
- Agent requirements: user stories, acceptance criteria, edge cases
- Prototype agent and evaluation on a test set of claims, comparing two models on quality, cost and latency
- Business case with conservative, base and optimistic scenarios
- Platform recommendation: which components are reusable and which are claims-specific, including data-residency and sovereign deployment considerations

### Out of scope
- Production build, deployment or system integration
- Claim types other than damage and shortage
- Changes to carrier contracts or customer terms
- Organizational design or staffing decisions. The business case quantifies capacity released but makes no headcount or role recommendations.
- Legal review of claims liability. Scope boundaries that involve liability or compliance exposure default to human sign-off or escalation, pending the client's legal review.

## 4. Approach

| Day | Phase | Activities | Outputs |
|---|---|---|---|
| 1 | Discovery and redesign | Stakeholder interviews (COO, claims lead), data request, current-state mapping, resolution of conflicting accounts, future-state redesign | Interview transcripts, current- and future-state process maps, decision logic, scope table |
| 2 | Requirements and prototype | Requirements authoring, prototype build, evaluation on two models, engineering handoff review | Requirements v1 and v2, prototype, eval results, model recommendation |
| 3 | Business case and readout | ROI modelling, CFO review, platform recommendation, executive summary | ROI model, CFO Q&A log, platform decision record, executive memo |

### Roles

- **AI lead consultant:** owns what is built and why: discovery, process redesign, decision logic, requirements, model recommendation and business case.
- **Forward-deployed engineer:** owns how it is built: prototype, evaluation harness, cost and latency measurement, ROI model build.
- **Client:** provides stakeholder time for interviews and the CFO review, and releases data against the written data request.

## 5. Stakeholders

| Stakeholder | Role in engagement | Interest | Influence | What they need from us |
|---|---|---|---|---|
| COO | Executive sponsor | Faster claims resolution; a visible AI initiative | High | A clear recommendation and a credible path to results |
| Claims and dispatch lead | Process owner | Workable process; fewer exceptions and rework | Medium | A redesign that reflects how the work is actually done |
| CFO | Economic buyer and approver | Lower cost, fewer write-offs, defensible investment | High | A business case built on validated assumptions |
| IT manager | Data provider | Minimal disruption; data handled appropriately | Low–medium | A clear, bounded data request |
| Claims handlers | Affected; not interviewed | Workable sign-off queue; clear escalation rules | Low | A process they can operate |
| Customers and carriers | Affected; not interviewed | Timely, consistent claim decisions | Low | Decisions that are fair and explainable |

**Decision-maker for sign-off:** COO, with CFO approval of the business case.

**Limitation:** claims handlers, customers and carriers are not interviewed in
this engagement. Their perspective is represented only through the claims lead
and the claims data.

## 6. Deliverables and acceptance criteria

| # | Deliverable | Accepted when |
|---|---|---|
| 1 | Current- and future-state process maps | Current state is cited to interview transcripts and claims data; conflicting accounts are resolved with documented rationale; any eliminated steps have documented rationale |
| 2 | Agent decision logic and scope table | Every claim path ends in exactly one route: autonomous, human sign-off or escalate |
| 3 | Agent requirements (v1 and v2) | An engineering review of v2 raises zero unresolved business questions, as classified by the AI lead consultant |
| 4 | Prototype and evaluation results | The pass bar is set before the evaluation runs; results are reported for both models, with pass rate, escalation correctness, cost per claim and latency. The test set is about 20 claims, so results are directional, not statistically significant |
| 5 | Business case and ROI model | Every input is sourced or labelled as an assumption; every CFO challenge is logged and answered |
| 6 | Platform decision record | Reusable and claims-specific components are explicitly separated |
| 7 | Executive memo | One page, with a clear recommendation and pilot proposal |

## 7. Assumptions

- The client provides 6 months of claims data in CSV format, with personally identifiable information (PII) removed.
- Stakeholders are available for interviews of about 25 minutes each.
- The CFO is available to review the business case on Day 3.
- Claims data reflects actual practice closely enough to test stated rules and volumes.
- Process facts that stakeholders and data cannot confirm are recorded as labelled assumptions.

## 8. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Data incomplete or inconsistent | Weak baselines and ROI | Flag quality issues early; use labelled assumptions with sensitivity ranges |
| Stakeholders disagree on process ownership or rules | Requirements stall | The AI lead consultant resolves conflicts with documented rationale and reports them in the daily summary for sponsor ratification |
| The agent turns out to be the wrong answer for part of the process | Reduced automation scope | Treated as a valid outcome; recommendation states what to eliminate or keep with people |
| Requirements ambiguity reaches engineering | Rework mid-build | Engineering handoff review before requirements are final |

## 9. Data handling

- Data is released by IT against a written data request, limited to fields that serve a stated hypothesis or business case input.
- Data is held in the project repository, and deleted or returned at engagement close.
- API credentials are stored outside version control, and model usage runs under a capped budget.

## 10. Governance

- **Daily:** end-of-day summary to the sponsor (decisions made, conflicts resolved, open questions)
- **Change control:** scope changes are agreed with the sponsor before work proceeds
