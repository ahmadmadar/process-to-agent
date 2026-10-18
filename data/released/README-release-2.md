# IT Data Release 2: Follow-up

**From:** IT Manager, Northline Freight
**To:** AI Lead Consultant
**Re:** Data Request 2 (`engagement/01-discovery/data-request-2.md`), §2–§4

> Fictional engagement for portfolio purposes. All data is synthetic.

This release answers the IT sections of the request (§2–§4). §5 is for the
claims and dispatch lead and §6 is for finance, so IT has not answered them.

## What is included

| File | Contents | Rows |
|---|---|---|
| `claims_r2_fields.csv` | §2 fields the system holds, one row per claim; joins to release 1 `claims.csv` on `claim_id` | 363 |
| `loss_summary.csv` | §3 loss-claim summary figures (no claim-level records) | 12 |
| `dq_document_fields.csv` | §4 Q1: document flags against the docs-complete date | 16 |
| `dq_am_preapproval.csv` | §4 Q3: finance review on account-manager decisions | 3 |
| `eval_sample.csv` | §4 Q4: 30-claim sample with all held fields | 30 |
| `build_release_2.py` | Script that produced the files above from the same extract as release 1 | — |

Same period, claims and keys as release 1 (2026-03-01 to 2026-08-31; damage
and shortage claims; joinable on `claim_id`).

## §2 Claims table fields

### Supplied

| Requested field | Source and note |
|---|---|
| `pod_exception` | The system's POD-exception flag, `Y` or `N`. No blanks for damage and shortage claims. |
| `reefer_flag` | Derived from the shipment's equipment mode (`Reefer` → `Y`), the fallback named in the request. |
| `key_account` | Derived from the customer tier the system holds (`key` → `Y`, `standard` → `N`). |
| `shipment_ref` | The carrier PRO number, replaced with a pseudonymous `SHP-` reference. The same PRO number always maps to the same reference. |
| `prior_payment_same_shipment` | Derived from `shipment_ref`, as the request allows: `Y` if an earlier claim on the same shipment was paid, with that claim's ID in `prior_payment_claim_id`. The check runs across all claim types in the extract, loss included. |
| `recovery_outcome` (refreshed) | **No change.** The extract is the same one used for release 1, so pending claims are still pending. The date each pending claim was filed is `recovery_filed_at` in release 1. |

### Not held

| Requested field | Answer to the fallback |
|---|---|
| `carrier_not_filed_reason` | Not held. The system has no free-text notes field. |
| `sent_to_preapproval_date` | Not held. The system records only the date of the finance review result (release 1 event log, `finance_review`). No email-sent date is held. |
| `insurer_consent_date` | Not held. The system records the insurer notification date and status only (release 1 event log, `insurer_notified`). Correspondence dates, if any, sit with finance. |
| `temp_download_requested_date` | Not held. Referred to the claims lead (§5). |
| `cold_chain_customer` | Not held. The system holds no contract terms, and IT does not hold the customer contracts. Referred to the claims lead or finance. |
| `invoice_amount` | Not held. The system records whether an invoice was received (release 1 `docs_missing`), not its value. |
| `denial_reversed` | Not held. Referred to the claims lead (§5). |
| `partial_basis` | Not held beyond the reason code already in release 1 `denial_reason`. No free-text decision notes are held. The amount deducted can be derived from `amount_claimed` and `amount_paid` in release 1. |
| `am_payment_request` | Not held. No record of account-manager requests exists in the system. |

## §3 Loss claims

Summary figures only, in `loss_summary.csv`: count by month received, count
of closed claims, median days from received to closed for closed claims, and
total claimed, paid and recovered. Amounts are plain numbers; the system does
not record currency (same as release 1).

## §4 Data quality questions

1. **Document fields.** The document flags (`photos_received`,
   `invoice_received`, `bol_received`, `temp_log_obtained`) and
   `docs_complete_date` are separate fields. The system does not check that
   they agree. `dq_document_fields.csv` counts each flag value against
   whether a completion date is set. The flags carry no date and show status
   at extract (release 1 note). IT cannot say which field the team treats as
   authoritative; the claims lead can.
2. **Withdrawn claims.** No. The system's status values are `closed` and three
   `open - …` states; none means withdrawn. No close notes are held.
3. **Account-manager payments and pre-approval.** See `dq_am_preapproval.csv`.
   It counts account-manager decisions with and without a finance review date
   in the system.
4. **Eval sample.** `eval_sample.csv` has 30 damage and shortage claims with
   all the fields IT holds, including each document flag. Limits:
   - **No per-document received dates.** The system stores one completion
     date per claim.
   - **No delivery-receipt document flag.** The POD exception flag is the only
     delivery-receipt field.
   - **Sampling:** at least 4 claims from each requested stratum (damage,
     shortage, reefer, key account, denied, partial), the rest random from
     all damage and shortage claims, with a fixed seed so it can be
     reproduced. Strata overlap, so one claim can count in several.

## Data quality

Blank counts in `claims_r2_fields.csv` (from `build_release_2.py`): 0 in
every field except `prior_payment_claim_id`, which is blank where
`prior_payment_same_shipment` is `N`.
