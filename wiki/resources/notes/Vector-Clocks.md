---
title: Vector Clocks
aliases:
  - Version vectors
type: concept
status: developing
created: 2026-10-29
updated: 2026-11-12
reading_time: 6
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Time-and-Ordering-Map|Time and Ordering Map]]"
tags:
  - ds/time
  - note
---

# Vector Clocks

A [Lamport clock](/wiki/resources/notes/Lamport-Clocks.md) cannot say two events are concurrent. A vector clock can, by keeping one counter per process.

## How it works

With $n$ processes, each keeps a vector $V = [v_1, \dots, v_n]$. Process $i$ increments only $v_i$ on its own events, attaches $V$ to messages, and on receipt takes the element-wise maximum before incrementing its own entry.

Compare two vectors $V$ and $W$:

- $V \le W$ when $v_k \le w_k$ for every $k$. Then $V$ happened before $W$ or is equal.
- If neither $V \le W$ nor $W \le V$, the events are **concurrent**.

## Code

```python
def compare(v: dict[str, int], w: dict[str, int]) -> str:
    keys = v.keys() | w.keys()
    le = all(v.get(k, 0) <= w.get(k, 0) for k in keys)
    ge = all(v.get(k, 0) >= w.get(k, 0) for k in keys)
    if le and ge:
        return "equal"
    if le:
        return "before"
    if ge:
        return "after"
    return "concurrent"


print(compare({"a": 2, "b": 1}, {"a": 1, "b": 3}))  # concurrent
```

## Where you meet them

- Leaderless stores attach a version vector to each value, so that two replicas holding different versions can tell "one is newer" from "these conflict".
- A conflict is returned to the application, or merged by a [CRDT](/wiki/resources/notes/CRDTs-and-Convergence.md).

> [!info] The cost
> The vector grows with the number of writers. Systems cap it, or replace process ids with the replicas that coordinate writes, and accept a small chance of treating ordered events as concurrent.

## Related

- Side by side with Lamport clocks: [Logical clocks compared](/wiki/resources/notes/Logical-Clocks-Compared.md)
