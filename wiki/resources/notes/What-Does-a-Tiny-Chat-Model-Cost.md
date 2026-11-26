---
title: What Does a Tiny Chat Model Cost?
aliases:
  - Cost of a tiny chat model
type: question
status: mature
created: 2026-11-23
updated: 2026-11-26
reading_time: 2
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/training
  - question
---

# What Does a Tiny Chat Model Cost?

## Answer

About **\$48** for a model that beats GPT-2, by the nanochat README's own arithmetic: an 8×H100 node at about \$3 per GPU-hour is about \$24 an hour, and the run takes about 2 hours. The README adds that a spot instance can bring the total closer to \$15.[^readme]

## Working

$$\text{cost} = \text{GPUs} \times \text{price per GPU-hour} \times \text{hours} = 8 \times 3 \times 2 = 48$$

| Run | Hours on 8×H100 | At \$24 an hour |
| --- | --- | --- |
| Leaderboard row 1 | 3.04 | about \$73 |
| Leaderboard row 6 | 1.65 | about \$40 |

The rows come from the [[Time-to-GPT-2-Leaderboard]]; the dollar column is my multiplication, not the README's.

## For comparison

The README puts the cost of training GPT-2 in 2019 at about \$43,000.

> [!note] What this does not include
> Experiments that failed, data preparation, and your own time.

[^readme]: [nanochat README at commit 92d63d4](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md).
