---
title: Logical Clocks Compared
type: comparison
status: developing
created: 2026-11-02
updated: 2026-11-12
reading_time: 3
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Time-and-Ordering-Map|Time and Ordering Map]]"
tags:
  - ds/time
  - comparison
---

# Logical Clocks Compared

Two ways to order events without trusting wall clocks.

## The definition both build on

![[Lamport-Clocks#^happens-before]]

## Comparison

| | [Lamport clock](/wiki/resources/notes/Lamport-Clocks.md) | [Vector clock](/wiki/resources/notes/Vector-Clocks.md) |
| --- | --- | --- |
| State per process | One integer | One integer per process |
| Message overhead | One integer | A vector that grows with the group |
| If $a \to b$ | $C(a) < C(b)$ | $V(a) < V(b)$ |
| If $C(a) < C(b)$ | Tells you nothing | Tells you $a \to b$ |
| Detects concurrency | No | Yes |
| Total order | With a process-id tie break | Only partial, by nature |
| Use it for | Ordering a log or a lock queue | Spotting conflicting writes |

> [!success] Rule of thumb
> Need one agreed order and do not care how concurrent events are ranked? Use a Lamport clock. Need to *notice* that two writes conflict? Use a vector clock.

> [!quote] Worth remembering
> Time is not what a clock says, it is what a message can prove.
