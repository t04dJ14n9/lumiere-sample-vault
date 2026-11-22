---
title: Heartbeat Simulator Spike
type: entity
methodology_role: project
status: archived
project_status: completed
priority: 3
outcome: Learn how fast a heartbeat detector reacts to a lost message
deadline: 2026-10-26
created: 2026-10-21
updated: 2026-10-26
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
para: archive
tags:
  - project
  - archive
  - ds/membership
---

# Heartbeat Simulator Spike

An afternoon's experiment, finished before the main project began, so it is archived rather than active. It lives in `wiki/archives/` because archived material is no longer part of the working set but is still worth finding.

## Outcome

A 40-line simulation of [heartbeat failure detection](/wiki/resources/notes/Failure-Detection.md). With a 1 s interval and a 3 s timeout, one lost heartbeat in a hundred caused a false alarm about every 90 seconds across ten nodes, which is far too often. Requiring three missed heartbeats in a row dropped the rate to almost none, at the cost of slower detection.

## What I kept

- The lesson went into [Failure Detection](/wiki/resources/notes/Failure-Detection.md): a timeout is a trade-off, not a number to look up.
- The code was thrown away.

## Why it was archived

Completed, and nothing in it needs to change. To revive it, set `para` back to `project` and `project_status` to `ongoing`.
