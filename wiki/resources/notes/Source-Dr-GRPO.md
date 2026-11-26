---
title: "Understanding R1-Zero-Like Training (Dr. GRPO)"
aliases:
  - Dr. GRPO
type: source
status: developing
created: 2026-11-26
updated: 2026-11-26
reading_time: 8
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - source
  - llm/post-training
authors: "Zichen Liu et al."
arxiv: "2503.20783v2"
license: CC BY 4.0
url: https://arxiv.org/abs/2503.20783v2
pdf: wiki/assets/Dr-GRPO-2503.20783v2-annotated.pdf
pages: 20
---

# Understanding R1-Zero-Like Training (Dr. GRPO)

**PDF:** [Open the annotated PDF](/wiki/assets/Dr-GRPO-2503.20783v2-annotated.pdf) (20 pages) · Zichen Liu et al., COLM 2025 · [arXiv:2503.20783v2](https://arxiv.org/abs/2503.20783v2) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

A close look at RL on base models in the style of DeepSeek-R1-Zero. It finds that base models already show some of the reasoning behaviour credited to RL, and that GRPO's way of normalizing its loss biases training toward longer answers, especially wrong ones. The fix, Dr. GRPO, removes that bias and spends fewer tokens for the same accuracy.

## How it connects

- It corrects the GRPO formula in [[Reasoning-Models-and-RL]]: the division by the group's spread and by answer length is what it drops.
- Its point that RL cannot reward what the model never samples fits the [[SFT-vs-RL]] rule of thumb: SFT first.

## What the annotations point at

- [p. 1](/wiki/assets/Dr-GRPO-2503.20783v2-annotated.pdf#page=1): the bias it finds in GRPO, and the base model that already reasons, each with a note.
- [p. 2](/wiki/assets/Dr-GRPO-2503.20783v2-annotated.pdf#page=2): the proposed fix and its token efficiency.
- [p. 4](/wiki/assets/Dr-GRPO-2503.20783v2-annotated.pdf#page=4): why RL needs at least one correct sample, with a margin box.

![[Dr-GRPO-2503.20783v2-annotated.pdf#page=1&height=560]]

## License

The paper is by its authors, redistributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with annotations added by this vault; see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
