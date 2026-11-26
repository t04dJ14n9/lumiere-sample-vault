---
title: Train a Tiny Chat Model progress
type: session
methodology_role: project-log
status: active
created: 2026-11-21
updated: 2026-11-26
area: "[[wiki/areas/LLM-Study|LLM Study]]"
para: project
tags:
  - project
  - llm/training
---

# Progress

Newest first. Numbers are synthetic.

## 2026-11-26

P-003 · Pretraining finished. Validation bits per byte ended near 0.75, with one spike on the way:

![Validation curve with a spike near step 3,200](/wiki/assets/loss-curve.png)

Worked through it with the [loss spike playbook](/wiki/resources/notes/Playbook-Debugging-a-Loss-Spike.md); see the [discovery](/wiki/projects/Train-a-Tiny-Chat-Model/discoveries.md#a-spike-from-one-bad-shard).

## 2026-11-25

P-002 · Started pretraining at depth 12 on one GPU. Throughput looked low; checked the dtype table in the README and confirmed bf16 was on.

## 2026-11-21

P-001 · Trained the tokenizer and read its compression rate with `scripts/tok_eval.py`. Wrote [[BPE-Tokenization]] the same evening.
