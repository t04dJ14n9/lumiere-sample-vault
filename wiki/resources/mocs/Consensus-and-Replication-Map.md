---
title: Consensus and Replication Map
type: meta
methodology_role: moc
status: developing
created: 2026-10-24
updated: 2026-11-20
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
tags:
  - moc
  - ds/consensus
  - ds/replication
---

# Consensus and Replication Map

How several machines keep one copy of the truth.

## Why this map exists

Replication is the question "how do we keep copies in step?", and consensus is its strongest answer: "make the copies agree on one sequence, even through failures". Following the links below goes from the cheap answer (quorums) to the expensive one (a replicated log).

## Core notes

1. [Quorum Reads and Writes](/wiki/resources/notes/Quorum-Reads-and-Writes.md)
2. [Replication Strategies](/wiki/resources/notes/Replication-Strategies.md)
3. [Raft Leader Election](/wiki/resources/notes/Raft-Leader-Election.md)
4. [Raft Log Replication](/wiki/resources/notes/Raft-Log-Replication.md)
5. [Two-Phase Commit](/wiki/resources/notes/Two-Phase-Commit.md)
6. [Gossip Protocols](/wiki/resources/notes/Gossip-Protocols.md)
7. [Failure Detection](/wiki/resources/notes/Failure-Detection.md)

## Practical notes

- [How many replicas do I need?](/wiki/resources/notes/How-Many-Replicas-Do-I-Need.md), a question with a worked answer
- [Playbook: debugging replica divergence](/wiki/resources/notes/Playbook-Debugging-Replica-Divergence.md)

## Everything tagged `ds/consensus`

The block below is a live search, written as a fenced `query` block. It lists matching notes and updates as the vault changes.

```query
tag:#ds/consensus
```

## Adjacent maps

- [Time and Ordering Map](/wiki/resources/mocs/Time-and-Ordering-Map.md)
- [Distributed Systems Map](/wiki/resources/mocs/Distributed-Systems-Map.md)

## Frontier

- What does Paxos add to, or take away from, what Raft gives?
- Which of these notes can I turn into a runnable test in the [toy store](/wiki/projects/Toy-Replicated-KV/overview.md)?
