# IT Data Release 1: Claims Process Data

**From:** IT Manager, Northline Freight
**To:** AI Lead Consultant
**Re:** Data request, Claims Automation Discovery Sprint (`engagement/01-discovery/data-request.md`)

> Fictional engagement for portfolio purposes. All data is synthetic.

## What is included

| File | Contents | Rows |
|---|---|---|
| `claims.csv` | One row per claim | 363 |
| `event_log.csv` | One row per recorded step | 2,338 |
| `build_release.py` | Script that produced both files from the claims system extract | — |

- **Period:** claims received 2026-03-01 to 2026-08-31 (6 complete months).
- **Claim types:** damage and shortage only, as requested. 49 claims of type `loss` were excluded under §3 scope.
- **Records:** all in-scope claims received in the period, including open and denied.

## How the request was met

### Supplied, with notes

| Requested field | Note |
|---|---|
| `carrier_id` | The system's internal carrier code. Carrier names withheld. |
| `outcome` | The decision as recorded: `approved`, `partially_approved`, `denied`. `open` where no decision is recorded. The system has no `withdrawn` code. Claims with a decision but a blank `closed_at` are still open. |
| `denial_reason` | Supplied for denied and partially approved claims only, as requested. |
| `decided_by_role` | The role recorded as approving the decision. |
| `recovery_outcome` | Carrier response as recorded: `paid`, `partial`, `denied`, `pending`, `not_filed`. |
| `docs_complete_at_receipt` | **Replaced by `docs_completed_at`.** The system stores the date documentation was completed, not a flag at receipt. Compare it to `received_at` to derive the flag. Blank where documentation was never completed. |
| `docs_missing` | Derived from the system's document flags (`photos`, `invoice`, `bol`, `temp_log`), semicolon-separated. The flags carry no date, so they show status as of this extract, not at receipt. A temperature log counts only where one is required. |
| All `_at` fields | The system records dates, not timestamps. |
| Amounts | The system stores amounts as plain numbers; currency is not recorded. |

### Not supplied

| Requested field | Reason |
|---|---|
| `shipment_value` | Not held. The system records the claimed value only. |
| `assigned_role` | The system records the handler by name, not by role. Withheld under the PII rule (staff by role only). |
| `escalated` | No field records escalation. |
| `write_off_amount` | No field records write-offs. |

### Event log

The system has no event log table. This file was built from the step dates
held on each claim record, so:

- each step has one date, supplied as `completed_at`. `started_at` is blank throughout;
- `actor_role` is supplied for the decision step only. Other steps do not record who performed them;
- `action` is supplied where the system records a result (decision, finance review, carrier response, insurer status);
- a step appears only if its date is recorded.

Steps: `intake`, `document_check`, `decision`, `finance_review`, `payment`,
`carrier_recovery_filed`, `carrier_recovery_response`, `insurer_notified`, `close`.

### Policy documents and business-case inputs

IT does not hold the written claims policy, the approval authority matrix,
handling times, hourly costs, or penalty and credit records. Please request
these from the claims lead and finance.

## Data quality

Blank counts per field (from `build_release.py`):

| `claims.csv` field | Blank | `claims.csv` field | Blank |
|---|---|---|---|
| `claim_id` | 0 | `outcome` | 0 |
| `claim_type` | 0 | `denial_reason` | 242 |
| `customer_id` | 0 | `decided_by_role` | 2 |
| `carrier_id` | 0 | `docs_completed_at` | 63 |
| `amount_claimed` | 0 | `docs_missing` | 225 |
| `amount_paid` | 2 | `delivered_at` | 0 |
| `amount_recovered` | 2 | `received_at` | 0 |
| `recovery_filed` | 2 | `closed_at` | 9 |
| `recovery_filed_at` | 183 | `paid_at` | 81 |
| `recovery_outcome` | 2 | | |

| `event_log.csv` field | Blank |
|---|---|
| `claim_id`, `step`, `completed_at` | 0 |
| `actor_role` | 1,977 |
| `started_at` | 2,338 |
| `action` | 1,479 |

Many blanks are expected: for example, `denial_reason` is blank for approved
claims and `docs_missing` is blank where nothing is missing.

IT cannot speak to process or coding changes during the period, or to claims
handled outside the system. Please ask the claims lead.
