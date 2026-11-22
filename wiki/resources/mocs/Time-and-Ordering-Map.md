---
title: Time and Ordering Map
type: meta
methodology_role: moc
status: developing
created: 2026-10-27
updated: 2026-11-16
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
tags:
  - moc
  - ds/time
---

# Time and Ordering Map

What happened first, and who can know it.

## Why this map exists

Two machines cannot read one clock. Everything here is a way to get an agreed order, or to notice that no order exists, without one.

## Core notes

- [[Lamport-Clocks]]: one counter, one agreed order
- [[Vector-Clocks]]: tell "before" from "concurrent"
- [[Logical-Clocks-Compared]]: when to use which
- [[CRDTs-and-Convergence]]: avoid needing an order at all

## The definition everything rests on

The same block, embedded from the Lamport note by its block id:

![[Lamport-Clocks#^happens-before]]

## Tagged `ds/time`

```query
tag:#ds/time
```

## Adjacent maps

- [Consensus and Replication Map](/wiki/resources/mocs/Consensus-and-Replication-Map.md)
- [Distributed Systems Map](/wiki/resources/mocs/Distributed-Systems-Map.md)
