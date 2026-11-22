---
title: Distributed Systems Fundamentals
aliases:
  - Distributed systems 101
  - DS fundamentals
type: concept
status: mature
created: 2026-10-20
updated: 2026-11-18
reading_time: 6
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Distributed-Systems-Map|Distributed Systems Map]]"
tags:
  - ds/foundations
  - note
---

# Distributed Systems Fundamentals

A distributed system is a set of machines that cooperate over a network so that they look like one system. The cooperation is the easy part. What matters is what happens when a machine or the network misbehaves.

> [!abstract] In short
> Machines fail on their own, networks fail between machines, and clocks disagree. Everything else in this vault, from [[Quorum-Reads-and-Writes|quorums]] to [[Raft-Leader-Election|leader election]], is a response to those three facts.

## Why it is hard

A call over a network can go wrong in three ways: the request is lost, the request is late, or the reply is lost. From the caller's side all three look the same, a silence. ^three-failures

That single fact explains most of the rest:

1. You cannot tell a crashed machine from a slow one, so every failure detector is a guess ([[Failure-Detection]]).
2. You cannot safely retry a request unless repeating it is harmless ([[Idempotency-and-Retries|idempotency]]).
3. You cannot trust a wall clock to order events on two machines ([[Lamport-Clocks|logical clocks]]).

> [!warning] Partial failure
> A single machine either works or it does not. A distributed system is *partly* broken most of the time: some nodes are up, some are slow, some can only be reached from one side of a [network partition](/wiki/resources/notes/CAP-Theorem.md).

## What a system promises

Every design picks how much it promises about the order and visibility of writes. Three common levels, strongest first:

| Promise | What a reader sees | Typical cost |
| --- | --- | --- |
| Linearizable | The latest write, as if there were one copy | A round trip to a quorum or leader |
| Causal | Every write that could have influenced it | Metadata carried with each request |
| Eventual | *Some* past value, converging if writes stop | Almost nothing, until a conflict |

## The toolbox

| Problem | Where it is covered |
| --- | --- |
| Which copy is right? | [[Quorum-Reads-and-Writes]], [Replication strategies](/wiki/resources/notes/Replication-Strategies.md) |
| Who is in charge? | [[Raft-Leader-Election]], [Raft log replication](/wiki/resources/notes/Raft-Log-Replication.md) |
| What happened first? | [[Lamport-Clocks]], [[Vector-Clocks]] |
| Is that node dead? | [[Failure-Detection]], [Gossip protocols](/wiki/resources/notes/Gossip-Protocols.md) |
| Where does this key live? | [[Consistent-Hashing]] |
| Can two nodes agree to commit? | [Two-phase commit](/wiki/resources/notes/Two-Phase-Commit.md) |

> [!tip]- How to read this vault
> Start with this note, then follow the [learning path](/wiki/resources/notes/Learning-Path-Distributed-Systems.md). Unfamiliar word? Look it up in the [[Distributed-Systems-Glossary#Quorum|glossary]]. The [[Distributed-Systems-Map]] shows how the notes connect.

> [!example]- Try it: the three failures in code
> The three silences are indistinguishable to this caller, which is the point.
>
> ```python
> import socket
>
> def ask(host: str, port: int, payload: bytes, timeout: float = 1.0):
>     try:
>         with socket.create_connection((host, port), timeout=timeout) as s:
>             s.sendall(payload)
>             return s.recv(4096)
>     except TimeoutError:
>         # Lost request, late request or lost reply: we cannot tell which.
>         return None
> ```
