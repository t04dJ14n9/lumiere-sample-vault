---
title: Toy KV Decisions
type: session
methodology_role: decision-log
status: active
created: 2026-10-27
updated: 2026-11-19
para: project
project: "[[wiki/projects/Toy-Replicated-KV/overview|Toy Replicated KV Store]]"
tags:
  - project
  - decision
---

# Toy KV Decisions

One entry per decision, each a `###` heading with its id, so it can be linked as `decisions.md#d-002-majority-quorums-for-reads-and-writes`. A decision is never edited after the fact: if I change my mind, a new entry supersedes the old one.

## Decisions

### D-001 Use Raft for replication

2026-10-27 · active

**Context.** I need one agreed order of writes across five nodes.

**Decision.** Implement Raft, not Paxos. The reason is readability: Raft splits the problem into [election](/wiki/resources/notes/Raft-Leader-Election.md) and [log replication](/wiki/resources/notes/Raft-Log-Replication.md), and each can be tested alone.

**Consequences.** One leader is a throughput ceiling. Acceptable for a toy.

### D-002 Majority quorums for reads and writes

2026-11-04 · active

**Context.** The [quorum rules](/wiki/resources/notes/Quorum-Reads-and-Writes.md) allow other splits of $R$ and $W$.

**Decision.** $W = R = 3$ of $N = 5$. It tolerates two failures for both reads and writes, which is the goal in the [overview](/wiki/projects/Toy-Replicated-KV/overview.md#goal).

**Alternatives.** $W = 5$, $R = 1$ gives fast reads and no tolerance for write failures. Rejected: the point is to survive failures.

### D-003 Hash sharding with virtual nodes

2026-11-10 · proposed

**Context.** One Raft group holds all keys, so adding nodes does not add capacity.

**Decision.** Shard keys over several groups with [consistent hashing](/wiki/resources/notes/Consistent-Hashing.md), 64 virtual nodes each. Not started: it waits for snapshots.

### D-004 Client-supplied request ids

2026-11-19 · active

**Context.** A client that times out cannot tell whether its write happened ([the three failures](/wiki/resources/notes/Distributed-Systems-Fundamentals.md#why-it-is-hard)).

**Decision.** Every write carries a client-generated id, and the leader remembers recent ids and their results. A retry returns the first answer instead of writing twice. See [Idempotency and retries](/wiki/resources/notes/Idempotency-and-Retries.md).

**Consequences.** The leader's memory of ids must itself be replicated, or a new leader forgets them.
