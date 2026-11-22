---
title: CRDTs and Convergence
aliases:
  - CRDT
  - Conflict-free replicated data types
type: concept
status: seed
created: 2026-11-11
updated: 2026-11-16
reading_time: 5
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Time-and-Ordering-Map|Time and Ordering Map]]"
tags:
  - ds/consistency
  - note
---

# CRDTs and Convergence

If every replica applies the same set of updates in *any* order and ends in the same state, conflicts cannot happen. A conflict-free replicated data type (CRDT) is built so that this is true by construction.

## The three laws

Replica states form a join-semilattice if the merge $\sqcup$ is

| Law | Statement | Why it matters |
| --- | --- | --- |
| Commutative | $a \sqcup b = b \sqcup a$ | Order of arrival does not matter |
| Associative | $(a \sqcup b) \sqcup c = a \sqcup (b \sqcup c)$ | Grouping does not matter |
| Idempotent | $a \sqcup a = a$ | A duplicated message is harmless |

## The simplest example: a grow-only counter

Each replica increments only its own slot. The value is the sum of all slots, and merge takes the maximum of each slot.

```python
class GCounter:
    def __init__(self, replica: str):
        self.replica = replica
        self.slots: dict[str, int] = {}

    def increment(self, by: int = 1) -> None:
        self.slots[self.replica] = self.slots.get(self.replica, 0) + by

    def value(self) -> int:
        return sum(self.slots.values())

    def merge(self, other: "GCounter") -> None:
        for r, n in other.slots.items():
            self.slots[r] = max(self.slots.get(r, 0), n)
```

> [!example]- Two replicas, any order
>
> ```text
> a: {a: 2}            b: {b: 1}
> a merges b -> {a: 2, b: 1}   value 3
> b merges a -> {a: 2, b: 1}   value 3
> a merges b again -> unchanged
> ```

> [!warning] Not everything is a CRDT
> A counter that can also decrement, a set with deletions, a text document: each needs a careful design. And some rules, such as "the balance must never go below zero", cannot be kept without coordination at all.

## Related

- The comparison that detects conflicts instead: [Vector clocks](/wiki/resources/notes/Vector-Clocks.md)
