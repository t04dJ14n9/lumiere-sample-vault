---
title: Quorum Reads and Writes
aliases:
  - Quorums
  - Quorum replication
type: concept
status: mature
created: 2026-10-22
updated: 2026-11-20
reading_time: 8
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Consensus-and-Replication-Map|Consensus and Replication Map]]"
tags:
  - ds/replication
  - ds/consensus
  - note
source: "[[wiki/resources/notes/Source-Replication-and-Quorums-Lecture-Notes|Replication and Quorums lecture notes]]"
---

# Quorum Reads and Writes

A quorum is a group of replicas big enough that any two such groups share at least one member. Because they overlap, a read quorum cannot miss a write that a write quorum has acknowledged.

![[quorum-overlap.svg|560]]

## The rule

Take $N$ replicas. A write must be acknowledged by $W$ of them and a read must be answered by $R$ of them. Reads see the latest acknowledged write when

$$R + W > N$$

and two conflicting writes cannot both succeed on disjoint groups when $W > N/2$. Each quorum tolerates a different number of failures:

$$\text{write failures tolerated} = N - W \qquad \text{read failures tolerated} = N - R$$

The [lecture notes, page 2](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=2) draw the same figure and tabulate common choices.

## Choosing R and W

| N | W | R | Writes survive | Reads survive | Shape |
| ---: | ---: | ---: | :---: | :---: | --- |
| 3 | 2 | 2 | 1 | 1 | Majority, the smallest useful cluster |
| 5 | 3 | 3 | 2 | 2 | Majority, a common production size |
| 5 | 5 | 1 | 0 | 4 | Fast reads, fragile writes |
| 5 | 1 | 5 | 4 | 0 | Fast writes, fragile reads |

> [!important] Majority quorums
> With $W = R = \lfloor N/2 \rfloor + 1$ both rules hold at once, and a cluster of $N = 2f + 1$ replicas keeps working through $f$ failures. That is why clusters have odd sizes: a sixth replica adds cost and no extra tolerance.

> [!question]- Does $R + W > N$ give linearizability?
> Not on its own. It guarantees that a read quorum *contains* the latest acknowledged write, but a concurrent or half-finished write can still be seen by one reader and missed by the next. Real systems add read repair, versioning or a leader to close that gap ([[Replication-Strategies]]).

## A tiny simulation

```python
import random

def quorum_read(replicas: list[dict], r: int):
    """Ask r random replicas and keep the answer with the highest version."""
    answers = random.sample(replicas, r)
    return max(answers, key=lambda a: a["version"])

replicas = [{"version": 1}, {"version": 1}, {"version": 2}, {"version": 2}, {"version": 2}]
print(quorum_read(replicas, r=3))  # any 3 of 5 include one that holds version 2
```

## Related

- Counting replicas: [[How-Many-Replicas-Do-I-Need]]
- Where quorums sit in the larger picture: [[Distributed-Systems-Fundamentals#What a system promises]]
- Used by the toy store: [D-002](/wiki/projects/Toy-Replicated-KV/decisions.md#d-002-majority-quorums-for-reads-and-writes)
