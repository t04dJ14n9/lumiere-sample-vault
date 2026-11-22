---
title: Lamport Clocks
aliases:
  - Lamport timestamps
  - Logical clock
type: concept
status: mature
created: 2026-10-27
updated: 2026-11-12
reading_time: 5
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Time-and-Ordering-Map|Time and Ordering Map]]"
tags:
  - ds/time
  - note
---

# Lamport Clocks

Wall clocks on different machines drift, so "10:00:01 here" and "10:00:00 there" say nothing about order. A Lamport clock is a counter that gives up on real time and keeps only the order that messages force.

## The rules

Each process keeps a counter $C$.

1. Before any local event, $C \leftarrow C + 1$.
2. When sending a message, attach the current $C$.
3. When receiving a message stamped $t$, set $C \leftarrow \max(C, t) + 1$.

The *happens-before* relation $a \to b$ means $a$ could have influenced $b$: it came earlier on the same process, or $a$ sent a message that $b$ received, or the two are linked through a chain of those. ^happens-before

The clock respects it in one direction only:

$$a \to b \;\Longrightarrow\; C(a) < C(b) \qquad\text{but}\qquad C(a) < C(b) \;\not\Longrightarrow\; a \to b$$

> [!warning] One direction only
> A smaller timestamp does **not** prove that one event caused the other. Two unrelated events can be stamped in either order. To detect that two events are concurrent you need [[Vector-Clocks]].

## In code

```python
class LamportClock:
    def __init__(self) -> None:
        self.time = 0

    def tick(self) -> int:
        """A local event."""
        self.time += 1
        return self.time

    def send(self) -> int:
        """Stamp an outgoing message."""
        return self.tick()

    def receive(self, stamp: int) -> int:
        """Merge the stamp of an incoming message."""
        self.time = max(self.time, stamp) + 1
        return self.time


a, b = LamportClock(), LamportClock()
t = a.send()        # a: 1
b.receive(t)        # b: max(0, 1) + 1 = 2
```

## Breaking ties

To get a *total* order, order by `(timestamp, process_id)`. The order is arbitrary between concurrent events, but every process computes the same one. That is enough for a replicated log or a mutual-exclusion queue.

## Related

- How it compares with the alternatives: [[Logical-Clocks-Compared]]
- Part of the [[Time-and-Ordering-Map|ordering map]]
