---
title: Scaling Laws and Compute
aliases:
  - Scaling laws
  - 6ND
type: concept
status: mature
created: 2026-11-21
updated: 2026-11-26
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Training-and-Inference-Map|Training and Inference Map]]"
tags:
  - llm/training
  - llm/progress
---

# Scaling Laws and Compute

## Two rules

**Compute.** Training a model of $N$ parameters on $D$ tokens costs about

$$C \approx 6ND$$

floating-point operations: about $2ND$ for the forward pass and $4ND$ for the backward pass.[^kaplan]

**Balance.** For a fixed compute budget, the Chinchilla paper found that parameters and tokens should grow together; a common reading of it is **about 20 tokens per parameter**.[^chinchilla] Training a bigger model on less data, or a smaller one for longer, wastes compute if the only goal is the loss at the end of training.

## Worked numbers

| $N$ | $D = 20N$ | $C = 6ND$ |
| --- | --- | --- |
| 100 M | 2 B | $1.2 \times 10^{18}$ |
| 1 B | 20 B | $1.2 \times 10^{20}$ |
| 7 B | 140 B | $5.9 \times 10^{21}$ |

The rows are arithmetic, not measurements. The same table is on the [cheat sheet PDF](/wiki/assets/Scaling-Laws-Cheat-Sheet.pdf), with annotations.

## In nanochat

nanochat derives every hyperparameter from the depth so each size comes out compute optimal ([[nanochat#^one-dial]]). Its README describes its speedrun model as a $4 \times 10^{19}$ FLOPs capability model.

> [!warning]- Why "compute optimal" is not "best to deploy"
> A model that will answer millions of requests is often trained on far more than 20 tokens per parameter: inference costs about $2N$ per token, so a smaller, longer-trained model can be cheaper overall.

[^kaplan]: [Kaplan et al., Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), 2020.
[^chinchilla]: [Hoffmann et al., Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), 2022.
