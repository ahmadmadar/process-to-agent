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
    end

    subgraph AG["Claims agent (new; pilot: damage and shortage)"]
        G0{"Loss claim?<br/>(S1, G1)"}
        G1{"Hard escalation?<br/>reefer equipment or temp allegation ·<br/>cold-chain · expedite ·<br/>claimed > deductible<br/>(C5, C5c, E4, G4, G5)"}
        G2["Send structured checklist<br/>with deadline (E5)"]
        G3{"Documents complete?<br/>(C5b, E5)"}
        G4["Hold: 'awaiting documents'<br/>list (state, no route), owned<br/>by specialists; automated<br/>reminders (E5, G3a, G3b, G7e)"]
        G5{"FALLBACK_DEADLINE_DAYS<br/>reached? (C5b; P2)"}
        G6{"Rule checks: duplicate ·<br/>invoice mismatch ·<br/>filing window (C5c)"}
        G7["Form decision<br/>and confidence (C5c; P1)"]
        G8{"Approval ≤ $10k and<br/>confidence ≥ threshold?<br/>(C5, C5a, C5c)"}
        G9["Approve autonomously<br/>(C5)"]
        G10["Urgency alert: insurer<br/>30-day clock (C5c; T2:L16)"]
    end

    subgraph CT["Claims team: sign-off and escalation queue (C4, C5)"]
        T1["Human sign-off: approve, edit<br/>or override the agent's full draft;<br/>reason logged (G7a)<br/>specialists ≤ $10k, lead > $10k (G7c)<br/>key accounts first (G6)"]
        T2["Escalation: lead (backup:<br/>senior specialist) works<br/>the agent's fact pack (G7b, G7c)<br/>reefer: same day (G7d)"]
        T3["Lead phones reefer carrier<br/>dispatcher same day<br/>(C5; T2:L44)"]
        T4["Notify insurer within 30 days;<br/>consent before settling<br/>(C5; T2:L16, T2:L48)"]
        T5["Loss claims: handled by team<br/>through redesigned steps<br/>(S1, G1; agent pilot excludes)"]
        T6{"Shortage with clean POD?<br/>(E6, UNTESTED)"}
        T7["Do not file<br/>(E6; T2:L20, T2:L64)"]
        T8["File with carrier with evidence<br/>(E5, E6; T2:L18)"]
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
    G9 --> T6
    T1 --> T6
    T2 --> T6
    T6 -- yes --> T7
    T6 -- no --> T8 --> R1
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
  lane, E5 at intake, E6 at carrier filing (marked UNTESTED).
- **E3 is a recommendation to finance**, not an agent step (E3).
- **Account managers** only submit expedite requests, which always escalate
  (C4, E4). C4 and E4 still need the COO's ratification (D5).
- **Insurer consent** must be obtained before payment on claims above the
  deductible. The diagram shows the insurer step but not a gate on the
  payment edge; see `open-gaps.md` G9.
- **Carrier filing, letters and payment instructions** are drawn with the
  claims team, as today, except for the autonomous route. Which of these the
  agent performs is not ruled; see `open-gaps.md` G8.
