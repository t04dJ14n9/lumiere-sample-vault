---
title: Distributed Systems Study
type: concept
methodology_role: area
status: active
created: 2026-10-20
updated: 2026-11-22
review_cadence: weekly
para: area
tags:
  - area
---

# Distributed Systems Study

An area is an ongoing responsibility, not a goal with an end date. It states what is in scope and what good looks like, and lists the projects and reference material that serve it.

## Scope

Understanding how systems of several machines stay correct and available: replication, consensus, ordering, failure handling. Out of scope: operating a production cluster, and anything about a specific vendor's product.

## Standards

What good looks like:

- Every note explains one idea and links to the notes it builds on.
- Every claim traces to a source note or to something I built and measured.
- Notes rated `mature` have been recalled from memory at least once.

Routine:

- [x] Add to the [learning path](/wiki/resources/notes/Learning-Path-Distributed-Systems.md) when a topic comes up twice
- [ ] Review `developing` notes weekly and promote or fold them
- [ ] Re-read the [glossary](/wiki/resources/notes/Distributed-Systems-Glossary.md) before starting a new topic

## Active projects in this area

Projects live in `wiki/projects/` and set `area` in their properties. This table is a Base that finds them, so nothing here is maintained by hand:

![[Projects.base]]

## Reference material

- [Distributed Systems Map](/wiki/resources/mocs/Distributed-Systems-Map.md)
- [Consensus and Replication Map](/wiki/resources/mocs/Consensus-and-Replication-Map.md)
- [Time and Ordering Map](/wiki/resources/mocs/Time-and-Ordering-Map.md)
- [Sources and Reading Map](/wiki/resources/mocs/Sources-and-Reading-Map.md)

Finished work is kept in [archives](/wiki/archives/Heartbeat-Simulator-Spike.md).

## Review cadence

Weekly, on Sunday: look at the open tasks above, the `developing` notes, and the [project's progress](/wiki/projects/Toy-Replicated-KV/progress.md).
