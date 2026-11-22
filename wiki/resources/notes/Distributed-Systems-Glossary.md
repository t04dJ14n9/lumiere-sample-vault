---
title: Distributed Systems Glossary
aliases:
  - Glossary
type: concept
status: developing
created: 2026-10-21
updated: 2026-11-19
reading_time: 4
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Distributed-Systems-Map|Distributed Systems Map]]"
tags:
  - ds/foundations
  - glossary
---

# Distributed Systems Glossary

Short definitions, one heading each, so other notes can link straight to a term, as in `[[Distributed-Systems-Glossary#Quorum]]`. Highlighted words are the ones to remember.

## Terms

### Availability

Every request to a node that is up gets an answer, even if it is out of date. One of the words in the [CAP theorem](/wiki/resources/notes/CAP-Theorem.md).

### Commit index

The highest log position the leader knows is stored on a ==majority==. Entries up to it are safe to apply. See [Raft log replication](/wiki/resources/notes/Raft-Log-Replication.md).

### Election timeout

How long a follower waits without hearing from a leader before it starts an election. Randomized so that elections rarely tie. See [Raft leader election](/wiki/resources/notes/Raft-Leader-Election.md).

### Idempotent

An operation that has the same effect done once or many times, which makes ==retrying== it safe. See [Idempotency and retries](/wiki/resources/notes/Idempotency-and-Retries.md).

### Leader

The one node that orders writes for a replica group. Also called primary or master in older writing.

### Linearizability

Operations appear to happen at a single instant between their start and end, in an order every client agrees on. The "C" in CAP.

### Partition

A failure that splits the nodes into groups that cannot reach each other, though every node may still be running.

### Quorum

A group of replicas large enough that any two groups ==overlap==. With $N$ replicas, any $\lfloor N/2 \rfloor + 1$ is a majority quorum. See [[Quorum-Reads-and-Writes]].

### Replica

One copy of a piece of data, on one node.

### Term

Raft's numbered epoch. At most one leader per term; a higher term always wins.

### Vector clock

A list of counters, one per process, that can tell "happened before" from "concurrent". See [[Vector-Clocks]].

### Write-ahead log

A file where a change is recorded *before* it is applied, so that a crash can be replayed. Raft's log is also a write-ahead log.

## Not defined here

Terms with no note yet are left unlinked on purpose: `Byzantine fault`, `TrueTime` and `Paxos`. Only Paxos is on the [learning path](/wiki/resources/notes/Learning-Path-Distributed-Systems.md) so far.

%% Idea: turn this into a single glossary per topic once it passes thirty terms. %%
