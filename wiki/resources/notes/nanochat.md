---
title: nanochat
aliases:
  - nanochat repository
type: entity
methodology_role: repository
status: developing
created: 2026-11-20
updated: 2026-11-26
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/training
  - repository
repository_url: https://github.com/karpathy/nanochat
---

# nanochat

> [!info] Repository card
> **Repository:** [karpathy/nanochat](https://github.com/karpathy/nanochat), MIT license.
> **Read at:** commit `92d63d4`, whose [README](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) this card summarizes.

## What it is

A small, readable harness that takes a language model through every stage: tokenizer, pretraining, finetuning, evaluation and a chat interface, on one GPU node. The [pipeline note](/wiki/resources/notes/LLM-Training-Pipeline.md) walks through the stages.

## The one dial

The README says the code is configured around a single setting, `--depth`, the number of transformer layers. Width, heads, learning rates and training length are derived from it so each size is compute optimal. That is the [scaling-law](/wiki/resources/notes/Scaling-Laws-and-Compute.md) idea turned into one flag. ^one-dial

## Running it

The README's whole pipeline is one script for an 8×H100 node, then a chat in the terminal:

```bash
bash runs/speedrun.sh
python -m scripts.chat_cli
```

A smaller example for CPU or Apple Silicon lives in `runs/runcpu.sh`, and the README is candid that it will not give strong results.

## Where to look in the code

| File | Holds |
| --- | --- |
| `nanochat/gpt.py` | the transformer, see [[Transformer-Block]] |
| `nanochat/tokenizer.py` | the BPE tokenizer, see [[BPE-Tokenization]] |
| `nanochat/engine.py` | inference with a [[KV-Cache]] |
| `nanochat/optim.py` | AdamW and Muon |
| `scripts/chat_rl.py` | reinforcement learning, see [[Reasoning-Models-and-RL]] |

## Why it matters here

It is the backbone of this vault: the [project](/wiki/projects/Train-a-Tiny-Chat-Model/overview.md), the [leaderboard note](/wiki/resources/notes/Time-to-GPT-2-Leaderboard.md) and the [cost question](/wiki/resources/notes/What-Does-a-Tiny-Chat-Model-Cost.md) all start from it.
