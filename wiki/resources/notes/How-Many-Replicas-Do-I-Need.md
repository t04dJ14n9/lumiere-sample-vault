---
title: How Many Replicas Do I Need?
aliases:
  - Replica count question
type: question
status: mature
created: 2026-10-30
updated: 2026-11-04
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Consensus-and-Replication-Map|Consensus and Replication Map]]"
tags:
  - ds/replication
  - question
---

# How Many Replicas Do I Need?

> [!question] The question
> I want a cluster that keeps accepting reads and writes while **two** machines are down. How many replicas must I run with a majority quorum?

## Answer

Five.

With $N$ replicas a majority quorum is $\lfloor N/2 \rfloor + 1$, which leaves $N - (\lfloor N/2 \rfloor + 1)$ replicas free to fail. Solving for $f$ failures gives

$$N = 2f + 1 \quad\Longrightarrow\quad f = 2 \;\Rightarrow\; N = 5$$

| Replicas ($N$) | Majority | Failures tolerated |
| ---: | ---: | ---: |
| 1 | 1 | 0 |
| 2 | 2 | 0 |
| 3 | 2 | 1 |
| 4 | 3 | 1 |
| 5 | 3 | 2 |
| 6 | 4 | 2 |
| 7 | 4 | 3 |

> [!note] Even numbers buy nothing
> Four replicas tolerate one failure, exactly like three, and six tolerate two, exactly like five. The extra replica only adds cost and a way for a partition to split evenly, leaving no majority on either side.

> [!success] What I did with it
> The [toy store](/wiki/projects/Toy-Replicated-KV/overview.md) runs five replicas in its tests. The reasoning is recorded in [D-002](/wiki/projects/Toy-Replicated-KV/decisions.md#d-002-majority-quorums-for-reads-and-writes).

## Follow-ups

- [x] Check the table against the [lecture notes](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=2)
- [ ] What changes when replicas are in different zones and one zone can fail as a whole?

See [[Quorum-Reads-and-Writes]] for why the arithmetic works.
