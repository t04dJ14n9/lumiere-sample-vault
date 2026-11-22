---
title: "Learning Path: Distributed Systems"
aliases:
  - Study plan
type: concept
status: developing
created: 2026-10-20
updated: 2026-11-21
reading_time: 3
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Distributed-Systems-Map|Distributed Systems Map]]"
tags:
  - ds/foundations
  - learning-path
---

# Learning Path: Distributed Systems

The order I am working through the topics, with each box ticked when I can explain the note without looking at it. Click a checkbox to tick it.

## Stage 1: Foundations

- [x] [Distributed Systems Fundamentals](/wiki/resources/notes/Distributed-Systems-Fundamentals.md)
- [x] [CAP Theorem](/wiki/resources/notes/CAP-Theorem.md)
- [x] [Lamport Clocks](/wiki/resources/notes/Lamport-Clocks.md)
- [ ] [Vector Clocks](/wiki/resources/notes/Vector-Clocks.md)
- [ ] [Failure Detection](/wiki/resources/notes/Failure-Detection.md)

## Stage 2: Replication

- [x] [Quorum Reads and Writes](/wiki/resources/notes/Quorum-Reads-and-Writes.md)
- [ ] [Replication Strategies](/wiki/resources/notes/Replication-Strategies.md)
- [ ] [Consistent Hashing](/wiki/resources/notes/Consistent-Hashing.md)
- [ ] [CRDTs and Convergence](/wiki/resources/notes/CRDTs-and-Convergence.md)

## Stage 3: Consensus

- [ ] [Raft Leader Election](/wiki/resources/notes/Raft-Leader-Election.md)
    - [ ] Draw the state machine from memory
    - [ ] Explain why timeouts are random
- [ ] [Raft Log Replication](/wiki/resources/notes/Raft-Log-Replication.md)
- [ ] [Two-Phase Commit](/wiki/resources/notes/Two-Phase-Commit.md)
- [ ] [[Paxos-Notes|Paxos]] (not written yet, the link is dimmed)

## Stage 4: Build something

- [ ] Finish the [toy replicated store](/wiki/projects/Toy-Replicated-KV/overview.md)

> [!tip] A dimmed link
> `Paxos-Notes` does not exist yet, so Lumiere draws its link dimmed with a dotted underline. Click it and choose to create the note, and it stops being dimmed.
