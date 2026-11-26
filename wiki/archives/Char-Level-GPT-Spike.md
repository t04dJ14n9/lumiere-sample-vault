---
title: Char-Level GPT Spike
type: entity
methodology_role: project
status: archived
project_status: completed
priority: 3
outcome: A character-level GPT on a small text, to see attention work before using a tokenizer
deadline: 2026-11-19
created: 2026-11-15
updated: 2026-11-19
area: "[[wiki/areas/LLM-Study|LLM Study]]"
para: archive
tags:
  - project
  - llm/foundations
---

# Char-Level GPT Spike

A finished project, kept for its lessons. Archived projects keep their links working.

## Outcome

Trained a tiny character-level model on one book of public-domain text. It learned spelling and line breaks, then words, then nothing more. Done.

## Retrospective

- Characters are an easy start but waste context: the same text needs many more steps than with a tokenizer. That is why the [project](/wiki/projects/Train-a-Tiny-Chat-Model/overview.md) starts with [[BPE-Tokenization]].
- Writing the attention mask by hand made [[Transformer-Block#Attention in one line]] stick.
