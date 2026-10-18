# Data Request: Claims Process Data

**To:** IT Manager, Northline Freight
**From:** AI Lead Consultant
**Re:** Claims Automation Discovery Sprint (see SOW §3, §9)
**Requested by:** Day 1, before post-interview synthesis

> Fictional engagement for portfolio purposes. All data is synthetic.

---

## 1. Purpose

We need claims data to test what stakeholders tell us against what actually
happens, and to set baselines for the business case. We are asking only for
fields that serve a stated hypothesis or a business-case input.

## 2. Working hypotheses

These are things to test, not conclusions. Each requested field maps to at
least one of them.

| ID | Hypothesis |
|---|---|
| H1 | Claims are slow mainly because of waiting and handoffs between steps, not because of the time spent working on them |
| H2 | At least one approval or review step rarely changes the outcome and may add no value |
| H3 | Claims rules (eligibility, documentation, payout thresholds) are applied inconsistently |
| H4 | Ownership of claim decisions is unclear between operations and finance |
| H5 | The largest cost is in write-offs and missed carrier recoveries, not handling labour |
| BC | Business-case baselines: volume, cycle time, handling effort, payout and recovery amounts |

**Event log required:** H1 and H2 cannot be tested from the claims table
alone, because it shows total cycle time but not where claims wait or whether
a review step changed the outcome. The event log (§5) is therefore required.

## 3. Scope

- **Claim types:** freight damage and shortage claims only
- **Period:** the most recent 6 complete months
- **Records:** all claims received in the period, including those still open, denied or withdrawn
- **Format:** CSV, one row per claim, plus one event log (see §5)
- **Personally identifiable information (PII):** removed. Use internal IDs for customers and carriers. Staff are identified by role only, not by name or ID.
- **Currency:** state the currency used for all amount fields.

## 4. Requested fields: claims table (one row per claim)

| Field | Description | Serves |
|---|---|---|
| `claim_id` | Unique claim identifier | All |
| `claim_type` | Damage or shortage | H3, BC |
| `customer_id` | Anonymized customer identifier | H3 |
| `carrier_id` | Anonymized carrier identifier | H5 |
| `shipment_value` | Declared value of the shipment | H3, H5 |
| `amount_claimed` | Amount the customer claimed | H3, H5, BC |
| `amount_paid` | Amount paid to the customer | H3, H5, BC |
| `amount_recovered` | Amount recovered from the carrier, if any | H5, BC |
| `recovery_filed` | Whether a recovery claim was filed with the carrier (Y/N) | H5 |
| `recovery_filed_at` | Timestamp the recovery claim was filed, if filed | H5 |
| `recovery_outcome` | Recovered in full, recovered in part, denied by carrier, pending, or not filed | H5 |
| `outcome` | Approved, partially approved, denied, withdrawn or open | H2, H3, BC |
| `denial_reason` | Reason code, if denied or partially approved | H3 |
| `decided_by_role` | Role that made the final outcome decision | H4 |
| `docs_complete_at_receipt` | Whether required documentation was complete when the claim was received (Y/N) | H1, H3 |
| `docs_missing` | Which documents were missing, if any | H1, H3 |
| `delivered_at` | Date the shipment was delivered | H3 |
| `received_at` | Timestamp the claim was received | H1, BC |
| `closed_at` | Timestamp the claim was closed. Blank for open claims | H1, BC |
| `paid_at` | Timestamp the customer was paid, if paid | H1, BC |
| `assigned_role` | Role that owned the claim (e.g., claims clerk, dispatch, finance) | H4 |
| `escalated` | Whether the claim was escalated beyond standard handling (Y/N) | H2, H4 |
| `write_off_amount` | Amount written off, if any | H5, BC |

## 5. Requested fields: event log (required, one row per step)

This is the most valuable thing you can send. It shows where claims wait and
which steps change outcomes.

| Field | Description | Serves |
|---|---|---|
| `claim_id` | Links to the claims table | All |
| `step` | Step name (e.g., intake, document check, review, approval, payment, carrier recovery) | H1, H2 |
| `actor_role` | Role that performed the step | H4 |
| `started_at` | Timestamp the step started | H1 |
| `completed_at` | Timestamp the step completed | H1 |
| `action` | What happened (approved, rejected, returned, requested info, overridden) | H2, H3 |

If some steps are not recorded in the claims system, include whatever is
tracked elsewhere (email, spreadsheets, a separate tool) and flag it. If an
event log cannot be supplied at all, tell us before the deadline so the
affected hypotheses can be rescoped.

## 6. Policy documents

These are needed to test H3. Rules cannot be shown to be applied
inconsistently without the rules themselves.

- The written claims policy: eligibility, required documentation, filing windows and payout thresholds
- The approval authority matrix: which roles can approve which claims, and up to what amount

## 7. Business-case inputs (if available)

These may not live in the claims system. Approximate figures are fine if
labelled as such.

- Average handling time per claim, by role (or how it is estimated)
- Loaded hourly cost by role
- Any claims-related penalties, customer credits or service-level breaches in the period

## 8. Data quality notes requested

Please flag:
- Fields that are often blank, entered manually or known to be unreliable
- Any change in process, system or coding during the 6-month period
- Claims handled outside the system (email, spreadsheets)

## 9. Handling

- Data is used only for this engagement and stored in the project repository.
- No PII is to be included; anonymized IDs for customers and carriers, roles only for staff.
- Data is deleted or returned at engagement close.
- Questions about this request go to the AI Lead Consultant.
