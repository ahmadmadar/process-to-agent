# Future-State Swimlane: Claims Process with Agent

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Every element cites a ruling in `docs/consultant-decisions.md` or a source.
Routing detail is in `decision-tree.md` and `scope-table.md`. Open gaps are
listed in `open-gaps.md`.

The redesign applies to all claim types, because loss claims share the
process (S1; T2:L50). The agent pilot handles damage and shortage only; the
agent escalates loss claims at step 0, and the claims team handles them
through the same redesigned steps (S1, G1).

```mermaid
flowchart LR
    subgraph CUS["Customer"]
        C1["Reports claim<br/>damage, shortage or loss<br/>(T2:L18, T2:L50; S1)"]
        C2["Submits documents<br/>against checklist and deadline<br/>(E5)"]
        C3["Receives decision letter;<br/>paid if approved or partial<br/>(T2:L18)"]
    end

    subgraph AM["Account manager"]
        A1["Submits expedite request only;<br/>cannot approve or pay<br/>(C4, E4)"]
        A2["Notified of key-account<br/>outcomes (G6)"]
        A3["Receives expedite answer:<br/>status, next step, date;<br/>payment only if approved (D5e)"]
    end

    subgraph AG["Claims agent (new; pilot: damage and shortage)"]
        G0{"Loss claim?<br/>(S1, G1)"}
        G1{"Hard escalation?<br/>reefer equipment or temp allegation ·<br/>cold-chain · expedite ·<br/>claimed > deductible<br/>(C5, C5c, E4, G4, G5)"}
        G2["Send structured checklist<br/>with deadline (E5);<br/>duplicate flag raised (G13)"]
        G3{"Documents complete?<br/>(C5b, E5)"}
        G4["Hold: 'awaiting documents'<br/>list (state, no route), owned<br/>by specialists; automated<br/>reminders (E5, G3a, G3b, G7e)"]
        G5{"FALLBACK_DEADLINE_DAYS<br/>(14 days) reached? (C5b; P2)"}
        G6{"Rule checks: duplicate ·<br/>invoice mismatch ·<br/>filing window (C5c)"}
        G7["Form decision; rubric +<br/>self-reported confidence<br/>(C5c, G11; P1)"]
        G8{"Approval ≤ $10k and<br/>both confidence gates pass?<br/>(C5, C5a, C5c, G11)"}
        G9["Approve autonomously: letter +<br/>payment instruction; filing<br/>package prepared (C5, G8a)<br/>pilot: every decision reviewed after (G8b)"]
        G10["Urgency alert: insurer 30-day<br/>notice; dates, no countdown<br/>until CFO (C5c, G9a)"]
    end

    subgraph CT["Claims team: sign-off and escalation queue (C4, C5)"]
        T1["Human sign-off: approve, edit<br/>or override the agent's full draft;<br/>reason logged (G7a)<br/>specialists ≤ $10k, lead > $10k (G7c)<br/>key accounts first (G6)"]
        T2["Escalation (reefer, loss, cold-chain,<br/>> deductible): lead (backup:<br/>senior specialist) works<br/>the agent's fact pack (G7b, G7c, G14)<br/>reefer: same day (G7d)"]
        T6["Expedite: specialist on the claim<br/>answers, else lead assigns or answers;<br/>lead owns the answer, no named backup;<br/>within EXPEDITE_RESPONSE_SLA<br/>(G7f, G14, P3); request and answer<br/>recorded (D5f); miss → notice to<br/>lead and AM (D5g)"]
        T3["Lead phones reefer carrier<br/>dispatcher same day<br/>(C5; T2:L44)"]
        T4["Notify insurer within 30 days;<br/>record consent: payment gated<br/>until recorded (C5, G9b; T2:L16)"]
        T5["Loss claims: handled by team<br/>through redesigned steps<br/>(S1, G1; agent pilot excludes)"]
        T8["File with carrier with evidence,<br/>clean-POD shortages included<br/>(E5, E6a; T2:L18; Q18)"]
    end

    subgraph RD["Reefer carrier dispatcher"]
        D1["Provides temperature download<br/>(~72h window; T2:L44)"]
    end

    subgraph AP["Finance: AP analyst"]
        F1["Pre-approval above $10k only<br/>(C2, E1); none for denials (E2)"]
    end

    subgraph PR["Finance payment run"]
        P1["RECOMMENDATION to finance:<br/>pay on approval or<br/>more frequent run (E3)"]
    end

    subgraph CAR["Carrier"]
        R1["Respond to filing<br/>(Q9)"]
    end

    subgraph INS["Cargo insurer"]
        I1["Consents before settlement<br/>(T2:L16)"]
    end

    subgraph REM["Removed from the current state"]
        X1["Pre-approval ≤ $10k (E1)"]
        X2["Pre-approval of denials (E2)"]
        X3["Weekly Thursday batch (E3, recommendation)"]
        X4["AM early-payment path (E4)"]
        X5["Unstructured email chasing (E5, redesigned)"]
    end

    C1 --> G0
    G0 -- "yes: always escalate (G1)" --> T2 -. loss .-> T5
    G0 -- no --> G1
    A1 --> G1
    G1 -- yes --> T2
    G1 -- "yes: expedite" --> T6
    T6 --> A3
    T6 --> T8
    G1 -. "> deductible" .-> G10 -.-> T4
    T2 -. reefer .-> T3 -. same day .-> D1
    G1 -- no --> G2 --> C2 --> G3
    G3 -- no --> G4 --> G5
    G5 -- no --> C2
    G5 -- yes --> T1
    G3 -- yes --> G6
    G6 -- flagged --> T1
    G6 -- clean --> G7 --> G8
    G8 -- yes --> G9
    G8 -- "no (denial, partial, > $10k, low confidence)" --> T1
    T4 --> I1
    G9 --> T8
    T1 --> T8
    T2 --> T8
    T8 --> R1
    T1 -- "approval > $10k" --> F1 --> P1
    T2 -- "approval > $10k" --> F1
    G9 -- "approval ≤ $10k: no pre-approval (E1)" --> P1
    T1 -- "denial: no pre-approval (E2)" --> C3
    P1 --> C3
    T1 -. "key account" .-> A2
    T2 -. "key account" .-> A2
```

## Notes

- **Every E ruling is visible:** E1 to E4 as changes and in the "Removed"
  lane, E5 at intake. E6 was reversed by E6a (Q18): clean-POD shortages are
  filed with the carrier.
- **E3 is a recommendation to finance**, not an agent step (E3).
- **Account managers** only submit expedite requests, which always escalate
  (C4, E4; ratified, D5 closed). The answer comes within
  `EXPEDITE_RESPONSE_SLA` from the specialist on the claim or the lead
  (G7f, G14, P3), and may promise payment only on an approved claim (D5e).
- **Insurer consent** is a hard gate: no payment instruction on a claim above
  the deductible until consent is recorded (G9b). The 30-day clock start is
  unset until the CFO confirms it (G9a).
- **On the autonomous route** the agent sends the letter and the payment
  instruction, and prepares the carrier filing for a specialist to submit
  (G8a). During the pilot, every autonomous decision is reviewed after it is
  made (G8b).
- **Re-routing:** new information moves a claim up a tier, never down;
  escalated claims are never handed back (G10a, G10b). Withdrawals take a
  `withdrawn` status, or go to sign-off if a payment was made (G12).
