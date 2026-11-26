---
title: Transformer Block
aliases:
  - Transformer
  - Attention
type: concept
status: mature
created: 2026-11-21
updated: 2026-11-25
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Training-and-Inference-Map|Training and Inference Map]]"
tags:
  - llm/foundations
---

# Transformer Block

A GPT is a stack of identical blocks. Each block lets every token look at the tokens before it (attention), then thinks about what it saw on its own (an MLP). The design comes from [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

## Attention in one line

For queries $Q$, keys $K$ and values $V$, with key size $d_k$:

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right)V$$

The mask $M$ is $-\infty$ above the diagonal, so a token cannot see the future. Dividing by $\sqrt{d_k}$ keeps the scores from growing with the key size. ^attention

## One block

$$
\begin{aligned}
h &= x + \mathrm{Attention}(\mathrm{Norm}(x)) \\
y &= h + \mathrm{MLP}(\mathrm{Norm}(h))
\end{aligned}
$$

The additions are residual connections: each block only *adds* to a running stream, which is what lets dozens of blocks train together.

## Sizes

| Symbol | Meaning |
| --- | --- |
| $L$ | number of blocks, nanochat's `--depth` |
| $d$ | width of the residual stream |
| $h$ | number of attention heads |

In nanochat the depth decides the rest ([[nanochat#^one-dial]]).

## Next

- At inference the keys and values of past tokens are reused: [[KV-Cache]].
- Counting the multiply-adds of a block gives the $6ND$ rule in [[Scaling-Laws-and-Compute]].
