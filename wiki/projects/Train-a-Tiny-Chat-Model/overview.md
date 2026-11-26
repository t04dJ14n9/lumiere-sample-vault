---
title: Train a Tiny Chat Model
type: entity
methodology_role: project
status: active
project_status: ongoing
priority: 1
outcome: A small chat model trained end to end with nanochat on one GPU, and notes on every stage
deadline: 2026-12-20
created: 2026-11-21
updated: 2026-11-26
area: "[[wiki/areas/LLM-Study|LLM Study]]"
para: project
tags:
  - project
  - llm/training
---

# Train a Tiny Chat Model

A project is a time-bound effort with an outcome. Everything stable lives here; the records that grow while the work runs are separate files: [progress](/wiki/projects/Train-a-Tiny-Chat-Model/progress.md), [decisions](/wiki/projects/Train-a-Tiny-Chat-Model/decisions.md) and [discoveries](/wiki/projects/Train-a-Tiny-Chat-Model/discoveries.md).

## Goal

Run every stage of [[nanochat]] myself, on one rented GPU, small enough to finish in an evening, and be able to explain each stage afterwards. Done means: a model I can chat with, and a note per stage in the [learning path](/wiki/resources/notes/Learning-Path-LLMs.md).

## Status

Pretraining works; finetuning is next. All numbers in this project are synthetic, made up for the sample vault.

## What's left

- [x] Train a tokenizer
- [x] Pretrain a small model (depth 12)
- [ ] SFT on conversations
- [ ] Try the RL stage
- [ ] Chat with it and write down what it gets wrong

## Plan

Start at depth 12, the README's suggestion for quick experiments, and only grow once each stage runs. See [D-001](/wiki/projects/Train-a-Tiny-Chat-Model/decisions.md#d-001-start-at-depth-12).

## Related

- [LLM Training Pipeline](/wiki/resources/notes/LLM-Training-Pipeline.md)
- [What does a tiny chat model cost?](/wiki/resources/notes/What-Does-a-Tiny-Chat-Model-Cost.md)
