# Data Request 2: Follow-up (final)

**To:** IT manager (§2–§4), claims and dispatch lead (§5), finance (§6), Northline Freight
**From:** AI lead consultant
**Re:** Claims-to-Agent Discovery Sprint, follow-up to Data Request 1
**Needed by:** start of Day 2

> Fictional engagement for portfolio purposes. All data is synthetic.

---

## 1. Purpose and ground rules

This is the single follow-up request allowed under Data Request 1. Every
item below traces to an interview line, a consultant ruling (C, E, S IDs in
the decisions log) or an open dependency (D IDs).

- **Same period and keys as release 1:** the same 6 months, joinable on `claim_id`.
- **If a field isn't held,** say so, and give the fallback named for that field. A clear "not held" is a useful answer.
- **No personally identifiable information (PII).** Use anonymized IDs only. Do not send handler names or IDs.
- **Not requested:** shipment value (IT confirmed it isn't held), handler identities, and anything not cited below.

## 2. Claims table: additional fields (IT)

One row per `claim_id`, added to the release 1 claims table.

| Field | Description | Why (citation) | If not held |
|---|---|---|---|
| `pod_exception` | Whether an exception was noted on the proof of delivery (Y/N) | Tests the clean-POD rule. E6 stays UNTESTED without it (E6, D7; T2:L20). **Highest priority** | Say whether POD images are stored, and where |
| `carrier_not_filed_reason` | Why no carrier claim was filed (clean POD, no evidence, below threshold, other) | Separates rule-based from evidence-based non-filing (E6, F3; T2:L64) | Free-text notes for claims with no carrier filing |
| `sent_to_preapproval_date` | Date the claim was sent to finance pre-approval | Splits decision → pre-approval into queue time vs review time (E1, C2; Q4) | Email-sent date, if the claims tracker or finance records it |
| `insurer_consent_date` | Date the insurer agreed to settlement, for claims over the deductible | Tests consent-before-settlement (C5; T2:L16) | Insurer correspondence dates, if held by finance |
| `reefer_flag` | Temperature-controlled (reefer) shipment (Y/N) | Sizes the temperature edge case (C5, F7; T2:L44) | Equipment type from the shipment record |
| `temp_download_requested_date` | Date the reefer temperature download was requested from the carrier | Tests the 72-hour window (C5; T2:L44) | Say "not held"; the claims lead is asked in §5 |
| `cold_chain_customer` | Customer has cold-chain liability terms in their contract (Y/N) | Cold-chain flag (C5c; T2:L44) | List of customer IDs with these terms |
| `key_account` | Customer is a key account, or customer tier | Key-account flag and account-manager analysis (C4, C5c; T1:L10, T1:L36) | List of key-account customer IDs |
| `invoice_amount` | Invoice value submitted with the claim, separate from `amount_claimed` | Invoice-mismatch flag (C5c; T2:L42) | Say whether invoice values are captured anywhere |
| `shipment_ref` | Shipment or BOL reference for the claim | Duplicate detection; claims on the same shipment must be linkable (C5c; T2:L68) | Any shared shipment key in the tracker |
| `prior_payment_same_shipment` | Any earlier claim payment against the same shipment (Y/N, with `claim_id`) | Duplicate flag (C5c; T2:L68) | Derivable from `shipment_ref` if supplied |
| `denial_reversed` | Denial later reversed or paid on appeal (Y/N, with date) | Denial risk for human sign-off (C5, C5a; T1:L36, T2:L60) | Say "not held"; the claims lead is asked in §5 |
| `partial_basis` | For partial approvals: how the amount was reduced (salvage, depreciation, invoice cap, other) and the amount deducted | Tests whether partials are mechanical (C5a; Q14) | Free-text decision notes for partial approvals |
| `am_payment_request` | Any record of an account manager asking for a claim to be paid (Y/N, with date) | Sizes the expedite-request volume (E4, C4; T2:L14, T2:L54) | Say "not held"; this will be estimated |
| `recovery_outcome` (refreshed) | Current carrier response for claims pending in release 1 | Stabilizes the recovery baseline (C3, D4; Q9) | Note which claims are still pending, and since when |

## 3. Loss claims: summary only (IT)

The agent pilot excludes loss claims, but the process redesign covers them
(S1; T2:L50). Please provide summary figures only, not claim-level records:

- Count by month
- Median days from received to closed
- Total claimed, paid and recovered

## 4. Data quality questions (IT)

1. **Document fields:** `docs_missing` lists more claims missing photos than there are claims without a docs-complete date (Q13). What does each field mean, and which is reliable?
2. **Withdrawn claims:** there is no withdrawn code (T2:L70). Can withdrawn claims be identified another way, e.g. from a close note?
3. **Account-manager payments and pre-approval:** do claims paid by account managers pass through finance pre-approval? A pre-approval event on these claims would answer it. This is open in the current-state map (T2:L14, T2:L52).
4. **Eval sample:** please provide full anonymized records for a sample of about 30 claims, with all fields above plus a document checklist (photos, invoice, BOL, delivery receipt: received Y/N and date). The sample should include damage, shortage, reefer, key-account, denied and partial claims. If this isn't possible, say so: the eval set will then be built from release 2 fields plus labelled assumptions.

## 5. Claims lead (process and policy)

| Item | Why (citation) |
|---|---|
| The approval-levels email | Documents the $10k line (C2, C5; T2:L14, T2:L36) |
| Customer filing-window rule: a standard window, or windows that vary by customer contract | Filing-window flag (C5c; Q14). Not mentioned in interviews |
| Packaging rule used in denials or partials | Denial reason in data, unexplained (Q14) |
| Whether temperature download requests are logged anywhere | Fallback for `temp_download_requested_date` (T2:L44) |
| Any known denial reversals in the period | Fallback for `denial_reversed` (T2:L60) |
| The two other late insurer notices mentioned (T2:L16): which claims | Data shows one (Q12; C6) |

## 6. Finance (business-case inputs; can be held for the Day 3 CFO interview)

| Item | Why (citation) |
|---|---|
| Cargo insurance deductible, notice period and consent terms | Always-escalate threshold; currently an assumption (C5, D1; T2:L16) |
| Write-offs in the period, including the duplicate payments | Cost baseline (H5; T2:L68) |
| Loaded hourly cost by role (claims specialist, claims lead, AP analyst) | Labour cost; hands-on time stays a labelled assumption (C1; T2:L66) |
| Customer penalties, credits or service-level breaches related to claims | Cost of delay (BC; T1:L8, T1:L14) |
| What finance pre-approval checks, and how often it changes a claim | Control owner's view (C2, E1; T2:L54, T2:L56) |
| Source and definition of the ~70% recovery figure | Recovery definition (C3, D4; T1:L18) |
| Currency of all amounts | Confirms units for the model |

## 7. Handling

- Used only for this engagement; stored in the project repository.
- Anonymized IDs only; no PII.
- Questions go to the AI lead consultant.