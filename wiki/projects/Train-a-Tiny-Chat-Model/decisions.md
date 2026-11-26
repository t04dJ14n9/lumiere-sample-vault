---
title: Train a Tiny Chat Model decisions
type: session
methodology_role: decision-log
status: active
created: 2026-11-21
updated: 2026-11-25
area: "[[wiki/areas/LLM-Study|LLM Study]]"
para: project
tags:
  - project
  - decision
---

# Decisions

## D-002 Skip RL until SFT works

D-002 · 2026-11-25 · active · me

RL needs a model that already answers in the right format; doing it first would only teach the reward to fail. See [[SFT-vs-RL]].

## D-001 Start at depth 12

D-001 · 2026-11-21 · active · me

The README calls a 12-layer model its favourite scale for quick experiments. Small enough for one GPU, big enough to see real loss curves. Grow only once every stage runs.
