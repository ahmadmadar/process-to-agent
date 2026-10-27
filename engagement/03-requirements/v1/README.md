# Claims Agent Requirements v1

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

## Purpose and scope

These requirements define an AI agent that routes and, within strict limits,
decides freight damage and shortage claims for Northline Freight, a
third-party logistics (3PL) company. They are written so an engineer can
build the agent from this folder alone. Every rule is stated here in full;
bracketed IDs (for example `C5`, `G11`) point to the consultant's decisions
log for traceability only.

**What the agent does**

- Checks every new claim against escalation triggers and sends those claims straight to a person.
- Holds claims whose documents are incomplete, sends reminders, and releases them when documents are complete or the fallback deadline is reached.
- Runs rule checks, forms a decision (approve, partial, deny) with two confidence signals, and routes the claim to one of three tiers.
- Acts on its own only for routine, fully documented approvals at or below $10,000 that pass both confidence gates.

**In scope (the pilot)**

- Damage and shortage claims (`S1`).
- The decision tree, scope table, tier operations, expedite requests, hold, re-routing and withdrawals defined in this folder.

**Out of scope for the agent**

- Loss claims. The agent always escalates them and forms no decision (`S1`, `G1`). They are a phase-2 candidate.
- Anything listed under "Out of scope" below.

## How to read these requirements

| File | Contains |
|---|---|
| `README.md` | Scope, glossary, roles, assumptions, open dependencies |
| `rules.md` | Precedence, decision tree, rule table, scope table, confidence gates, parameters, agent input and output schemas |
| `stories.md` | User stories with acceptance criteria |
| `edge-cases.md` | Edge cases and how each is handled |
| `non-functional.md` | Trace, records, service levels, cost, data handling |

Conventions:

- **Must** marks a requirement. Everything else is explanation.
- Amounts are plain numbers in the client's currency. The system does not record a currency.
- All times are Eastern Time (ET). Dates are calendar dates unless a rule says business days.
- Where `rules.md` and another file differ, `rules.md` governs.

## Glossary

| Term | Meaning |
|---|---|
| Claim | A customer's request for payment for goods damaged or short on delivery |
| Claimed amount | The amount the customer claims. **All amount thresholds are measured on the claimed amount**, not the amount paid (`G4`) |
| Deductible | The cargo insurance deductible. Assumed to be $25,000 (see Assumptions) |
| Route | Where a claim goes: `autonomous`, `sign_off` or `escalate`. Exactly three values |
| Tier | Same as route. Autonomous = the agent decides and acts. Human sign-off = the agent drafts and a person approves, edits or overrides. Always escalate = a person handles the claim from a fact pack, with no agent decision |
| Hold | A **state, not a route**. A claim waiting for documents has no route (`G3a`) |
| Documents complete | Every item on the required checklist for the claim type has been received (`E5a`; see `rules.md`) |
| "Awaiting documents" list | The list of held claims, visible to specialists |
| Fact pack | What the agent produces for an escalated claim: triggers fired, document checklist status, running clocks. No decision and no amount (`G7b`) |
| Expedite request | A request from an account manager to speed up a claim. It always escalates to a person (`E4`) |
| POD | Proof of delivery (delivery receipt). A **clean POD** has no exception noted |
| BOL | Bill of lading |
| Reefer | A temperature-controlled shipment (`reefer_flag` = Y) |
| Cold-chain customer | A customer whose contract makes Northline liable for any temperature excursion, regardless of the carrier |
| Key account | A customer with tier `key`. **Not a routing input** (`G6`) |
| Carrier filing | Northline's claim against the carrier to recover what it paid the customer |
| Business day | Monday to Friday, excluding company holidays (see Assumptions) |

## Roles

| Role | Responsibilities |
|---|---|
| Claims specialist | Works sign-off claims with a claimed amount at or below $10,000. Owns the "awaiting documents" list. Submits carrier filings. Answers expedite requests on claims they are already working |
| Senior specialist | A designation within the specialist team, named by the claims lead, who describes one specialist as "the senior one" (W2:L2). Covers escalations, other than expedite answers, when the claims lead is unavailable |
| Claims lead | Works sign-off claims above $10,000 and all escalations, except expedite-only decisions at or below $10,000. Owns every expedite escalation and its on-time answer. Records insurer consent on claims above the deductible |
| Account manager | May submit an expedite request. Receives outcome notices on key-account claims and SLA-miss notices on their own requests. **Cannot approve or pay any claim** (`C4`, `E4`) |
| Finance (AP analyst) | Pre-approves payments only on approvals with a claimed amount above $10,000. Issues payments |
| Autonomous reviewer | During the pilot, a claims specialist designated by the claims lead reviews every autonomous decision after it is made (`G8b`) |
| Agent | Applies `rules.md`. Never decides outside the scope table |

## Assumptions

Labelled assumptions, used until confirmed:

| # | Assumption | Used in | Confirm with |
|---|---|---|---|
| A1 | Deductible is $25,000 on the claimed amount | R4, insurer gate | CFO (D1) |
| A2 | $10,000 line on the claimed amount | R13, R15, finance pre-approval, queues | CFO (D3) |
| A3 | Headquarters time zone is Eastern Time | SLA, all timestamps | COO |
| A4 | Company holidays are US federal holidays | SLA business days | COO (D11) |
| A5 | Customer filing window is 270 calendar days from delivery date to receipt date, for every customer | R9 | Claims lead (D13) |
| A6 | Finance pre-approval is removed at or below $10,000 and for denials | Payment | CFO (D2) |

## Open dependencies

The agent can be built and piloted with these open. Each has a stated
interim behaviour.

| ID | Dependency | Owner | Interim behaviour in v1 |
|---|---|---|---|
| D1 | Deductible amount | CFO | Use A1 |
| D2 | Removal of pre-approval at or below $10,000 and for denials; payment-run change | CFO | Use A6 |
| D3 | $10,000 thresholds | CFO | Use A2 |
| D9 | When the insurer's 30-day notice period starts | CFO | Insurer alert shows delivery and receipt dates, no countdown |
| D11 | Company holiday list | COO, before go-live | Use A4 |
| D12 | Customer IDs for the cold-chain customers | Claims lead, before go-live | Pilot does not go live until the list is populated (see `rules.md`, cold-chain list) |
| D13 | Customer filing-window rule, and whether windows vary by contract | Claims lead | Use A5 |
| P1 | Confidence thresholds | Consultant, from the eval | See `rules.md`, Parameters |
| Risk | Expedite answers on days the claims lead is on dispatch | Claims lead | Monitored through the expedite record; no target |

## Out of scope

- Production build, deployment and integration with the claims tracker, email or finance systems.
- Loss-claim decisions (always escalated).
- The governance miss report, its cadence and the COO's review of it. v1 only records the data it needs.
- The finance payment-run change (a recommendation to finance, not an agent step).
- Recovery baselines and business-case figures.
- Rules for when autonomous review moves from every decision to a sample.
