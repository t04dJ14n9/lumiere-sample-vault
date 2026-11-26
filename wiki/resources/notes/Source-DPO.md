---
title: "Direct Preference Optimization (DPO)"
aliases:
  - DPO
type: source
status: seed
created: 2026-11-26
updated: 2026-11-26
reading_time: 5
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - source
  - llm/post-training
authors: "Rafael Rafailov et al."
arxiv: "2305.18290v3"
license: CC BY 4.0
url: https://arxiv.org/abs/2305.18290v3
pdf: wiki/assets/DPO-2305.18290v3.pdf
pages: 27
---

# Direct Preference Optimization (DPO)

**PDF:** [Open the PDF](/wiki/assets/DPO-2305.18290v3.pdf) (27 pages) · Rafael Rafailov et al. · [arXiv:2305.18290v3](https://arxiv.org/abs/2305.18290v3) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

Learning from human preferences usually means fitting a reward model and then running RL against it. DPO shows that the same objective can be optimized directly on pairs of preferred and rejected answers with a simple classification-style loss, without a separate reward model and without sampling from the model during training.

## How it connects

- It is the middle ground in [[SFT-vs-RL]]: it learns from comparisons like RL, but trains like SFT.
- The RL-from-human-feedback recipe it simplifies is InstructGPT's, in [[Classic-Papers]].
- [[Reasoning-Models-and-RL]] covers the other branch: rewards a program can check.

## License

The paper is by its authors, redistributed unchanged under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
