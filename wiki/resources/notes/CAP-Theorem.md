---
title: CAP Theorem
aliases:
  - CAP
type: concept
status: mature
created: 2026-10-23
updated: 2026-11-14
reading_time: 5
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Distributed-Systems-Map|Distributed Systems Map]]"
tags:
  - ds/foundations
  - ds/consistency
  - note
---

# CAP Theorem

## The short version

When the network splits a system in two, each half must choose. It can **refuse** some requests to stay consistent, or it can **answer** from what it has and risk being stale. It cannot do both while the split lasts.

## The three words

- **Consistency** here means linearizability: every read sees the latest completed write.[^c]
- **Availability** means every request to a node that is up gets an answer.
- **Partition tolerance** means the system keeps working when messages between nodes are lost.

Partitions are not optional: networks drop packets whether you plan for it or not. So the real choice is only what to give up *during* a partition.

> [!danger] The common misreading
> "Pick two of three" suggests that a system can be CA. A system that cannot survive a partition is not a distributed system you can run on a real network, it is a single machine with extra steps.

## When there is no partition

Most of the time the network is fine, and a second trade-off applies: lower latency versus stronger consistency. Waiting for a quorum costs a round trip, answering locally does not. This is the idea behind PACELC.[^pacelc]

## Examples

| System behaviour during a partition | Choice |
| --- | --- |
| The minority side refuses writes | Consistency |
| Both sides accept writes and merge later | Availability |
| A leader steps down when it loses its majority ([Raft](/wiki/resources/notes/Raft-Leader-Election.md)) | Consistency |
| A shopping cart accepts adds on any replica | Availability |

> [!tip]- A question to ask of any database
> "What happens to a write if the node I talk to cannot reach the others?" The answer tells you which side it chose.

[^c]: The formal statement uses atomic (linearizable) registers. Weaker meanings of "consistent" in everyday speech, such as "the data is not corrupt", are not what the theorem is about.
[^pacelc]: Partition: choose Availability or Consistency; Else: choose Latency or Consistency. The name is the sentence, abbreviated.
