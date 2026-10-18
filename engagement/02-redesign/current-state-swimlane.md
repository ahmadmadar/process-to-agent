# Current-State Swimlane: Damage and Shortage Claims (draft)

> Fictional engagement for portfolio purposes. The client, stakeholders and data are synthetic.

Claude's draft from T1, T2 and release 1, for the consultant to correct. Each
step cites its source. Elapsed times are in `analysis/results.md` (Q4–Q6,
Q12); none are written here.

```mermaid
flowchart LR
    subgraph CUS["Customer"]
        C1["Reports claim by email<br/>(T2:L18)"]
        C2["Sends documents piecemeal<br/>(T2:L18, T2:L28)"]
    end

    subgraph AM["Account manager (key accounts)"]
        A1["Pays key customer early,<br/>often before docs complete<br/>(T1:L10, T2:L14; Q11)"]
    end

    subgraph CT["Claims team: specialists ≤ $10k, lead > $10k"]
        T1["Log in tracker workbook<br/>(T2:L18, T2:L20)"]
        T2["Send document list;<br/>chase by email and phone<br/>(T2:L18, T2:L30)"]
        T3{"Temperature claim?<br/>(T2:L44)"}
        T4["Lead phones reefer carrier<br/>same day for download<br/>(T2:L44)"]
        T5["Review and decide:<br/>approve, partial or deny<br/>(T2:L20; Q14)"]
        T6{"Over deductible?<br/>(T2:L16, assumed $25k)"}
        T7{"File with carrier?<br/>Not if clean-POD shortage<br/>or no evidence<br/>(T2:L20, T2:L64)"}
        T8["Write letter<br/>(T2:L60)"]
        T9["Close in tracker<br/>(T2:L18)"]
    end

    subgraph FIN["Finance: AP analyst"]
        F1["Pre-approval of every claim,<br/>incl. denials<br/>(T2:L18, T2:L60; Q5)"]
        F2["Weekly payment run,<br/>Thursdays<br/>(T2:L18; Q6)"]
    end

    subgraph CAR["Carrier"]
        R1["Respond: paid, partial,<br/>denied or pending<br/>(Q9)"]
    end

    subgraph INS["Cargo insurer"]
        I1["Notified within 30 days;<br/>consent before settlement<br/>(T2:L16; Q12)"]
    end

    C1 --> T1 --> T2 --> C2 --> T3
    T3 -- yes --> T4 --> T5
    T3 -- no --> T5
    T5 --> T6
    T6 -- yes --> I1 --> T7
    T6 -- no --> T7
    T7 -- file --> R1
    T7 --> T8 --> F1 --> F2 --> T9
    C1 -. key account .-> A1 -. logged after the fact<br/>(T2:L54) .-> T9
```

## Notes and open points

- **Order of steps after the decision** follows the claims lead's walkthrough
  (T2:L18): file with carrier, then pre-approval, then the payment run. The
  carrier step may run in parallel with pre-approval; not confirmed.
- **Insurer step position** is inferred from T2:L16 and T2:L48. Whether
  notification happens before or after the decision is not stated.
- **Account-manager path** bypasses review, pre-approval timing and carrier
  filing as described (T2:L14, T2:L54). Whether it goes through finance
  pre-approval is not stated.
- **Not recorded in the tracker:** document chasing (T2:L22), reefer calls
  (T2:L74), and AM payments until after the fact (T2:L54, T2:L74).
- **Escalation** is by value plus informal "walk over and ask" (T2:L40); not
  drawn as a separate step.
- **Loss claims** run through the same process (T2:L50) and are out of scope
  pending the consultant's ruling.
