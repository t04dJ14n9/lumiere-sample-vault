---
title: Train a Tiny Chat Model discoveries
type: session
methodology_role: project-log
status: active
created: 2026-11-25
updated: 2026-11-26
area: "[[wiki/areas/LLM-Study|LLM Study]]"
para: project
tags:
  - project
  - llm/training
---

# Discoveries

## A spike from one bad shard

S-002 · 2026-11-26

The spike at step 3,200 lined up with one data shard full of repeated lines. Skipping the shard and resuming from the checkpoint gave a smooth curve. Added the check to the [playbook](/wiki/resources/notes/Playbook-Debugging-a-Loss-Spike.md).

## Bits per byte, not loss

S-001 · 2026-11-25

Loss per token changes when the tokenizer changes, so two runs with different vocabularies cannot be compared by loss. Bits per byte can. See the [[LLM-Glossary|glossary]].
