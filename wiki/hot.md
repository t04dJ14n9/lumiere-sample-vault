---
title: Hot Cache
type: meta
status: developing
created: 2026-10-20
updated: 2026-11-22
tags:
  - meta
  - hot-cache
---

# Recent Context

A short cache of where things stand, read first when resuming work.

Navigation: [Start here](/wiki/index.md) · [Operation log](/wiki/log.md) · [Distributed Systems Map](/wiki/resources/mocs/Distributed-Systems-Map.md)

## Last Updated

2026-11-22. Added the client-request-id decision and the step-down task to the [toy store](/wiki/projects/Toy-Replicated-KV/overview.md).

## Key Recent Facts

- A leader cut off from its majority keeps accepting writes until a heartbeat fails ([discovery](/wiki/projects/Toy-Replicated-KV/discoveries.md#an-old-leader-keeps-writing)).
- Majority quorums, $W = R = 3$ of $N = 5$, are the chosen setup ([D-002](/wiki/projects/Toy-Replicated-KV/decisions.md#d-002-majority-quorums-for-reads-and-writes)).

## Recent Changes

- New note: [Playbook: debugging replica divergence](/wiki/resources/notes/Playbook-Debugging-Replica-Divergence.md).
- New note: [Idempotency and Retries](/wiki/resources/notes/Idempotency-and-Retries.md).

## Active Threads

- [ ] Leader step-down when it cannot reach a majority
- [ ] Write the Paxos note
- [ ] Review the `developing` notes on Sunday
