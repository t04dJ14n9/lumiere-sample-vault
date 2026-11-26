---
title: SFT vs RL
aliases:
  - Finetuning compared with RL
type: comparison
status: developing
created: 2026-11-24
updated: 2026-11-26
reading_time: 2
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Training-and-Inference-Map|Training and Inference Map]]"
tags:
  - llm/post-training
---

# SFT vs RL

Both start from a pretrained base model and both are small next to pretraining. They differ in what they learn from.

| | Supervised finetuning | Reinforcement learning |
| --- | --- | --- |
| Learns from | example answers | a reward on its own answers |
| Needs | good demonstrations | a checker or a judge |
| Good at | format, tone, turn-taking | getting checkable answers right |
| Can go wrong by | copying the demos' mistakes | gaming a weak reward |
| In nanochat | `scripts/chat_sft.py` | `scripts/chat_rl.py` |

## A third option

[DPO](/wiki/resources/notes/Source-DPO.md) learns from pairs of preferred and rejected answers like RL, but trains like SFT, with no reward model and no sampling.

## Rule of thumb

Use SFT to teach *what an answer looks like*, then RL to teach *which answers are right* where a program can tell. See the [pipeline](/wiki/resources/notes/LLM-Training-Pipeline.md#where-the-compute-goes) for where both sit and [[Reasoning-Models-and-RL]] for what RL changed.
