# Sponsor Summary: Day 2, Agent Design and Requirements

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

**To:** COO (sponsor) · **From:** AI lead consultant · **Day:** 2 (2026-10-19)

## Bottom line

1. **The agent's rulebook is complete and tested.** Every claim combination
   we tested lands in exactly one route: handled by the agent, signed off by a
   person, or escalated (`coverage-test.md`).
2. **The data overturned one of the team's rules, and it means money.**
   Carriers do pay shortage claims with a clean delivery receipt: of those
   filed and answered, the carrier accepted 8 of 12 (Q18). Most of these
   claims were never filed (Q18). We now file them (E6a).
3. **We need your decision on account-manager payments (C4, E4) before the
   requirements are frozen.**

## Decision needed from you

**C4 and E4: the claims team owns every claim payout.**

- **What changes:** account managers no longer approve or pay claims for key
  accounts. They submit an expedite request instead. Every expedite request
  goes straight to a person on the claims team, never to the agent.
- **What account managers gain:** their key-account claims are worked first,
  and they are told the outcome as soon as the claim is decided (G6).
- **Why:** account-manager claims are paid before documents are complete far
  more often, filed with carriers less often, and recover far less (Q11). The
  one claim that lost insurance cover was an account-manager payment made
  before the insurer was told (Q12).
- **What you said:** you want account managers to fix key-account problems
  the same day (T1:L10). The expedite route and the priority keep that speed
  without the payment risk.

We would like to take this with you in a short session before the
requirements are frozen.

## Decisions made today

| Ruling | Decision |
|---|---|
| G1 | Loss claims are always passed to a person; the agent does not decide them |
| G2 | When a claim meets more than one rule, the most cautious route wins |
| G3a–b | Claims waiting for documents are held in a visible list, at any amount |
| P2 | If documents are still missing after 14 days, a person takes the claim. 92% of claims that completed did so within 14 days (Q19) |
| G4 | The $10k line and the deductible are measured on the amount claimed |
| G5 | Any claim on a refrigerated load, or alleging a temperature problem, goes to a person the same day |
| G6 | Key-account claims are worked first, and the account manager is told the outcome |
| G7a–e | At sign-off, the agent drafts the decision and the letter and a person approves or changes it. Escalated claims get a fact pack and no agent decision. Specialists take claims up to $10k; the claims lead takes larger claims and escalations, with the senior specialist as backup |
| G8a–b | On a claim it approves, the agent sends the letter and the payment instruction; a specialist files with the carrier. During the pilot, a person reviews every decision the agent makes on its own |
| G9b | No payment above the deductible until the insurer's consent is recorded |
| G10a–b | New information can move a claim to a more cautious route, never a less cautious one |
| G11 | The agent acts alone only when two separate confidence checks both pass |
| G12 | Withdrawn claims get their own status, so they can be counted |
| G13 | Possible duplicate payments are flagged as soon as a claim arrives |
| E6a | Clean-POD shortage claims are filed with carriers (reverses E6) |

## Open questions

| # | Question | Owner |
|---|---|---|
| D5 | Ratify C4 and E4 (above) | You, before the requirements freeze |
| D1–D4, D8 | Carried from Day 1: deductible, pre-approval removal, $10k thresholds, recovery figure, late-notice count | CFO, Day 3 |
| D9 | When the insurer's 30-day notice period starts (the data cannot tell, Q17) | CFO, Day 3 |

## Next

Your decision on C4 and E4, then the requirements freeze, an independent
engineering review of the requirements, and the two-model test on sample
claims.
