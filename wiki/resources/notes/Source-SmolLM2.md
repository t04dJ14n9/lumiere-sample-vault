---
title: "SmolLM2"
aliases:
  - SmolLM2
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
  - llm/training
authors: "Loubna Ben Allal et al."
arxiv: "2502.02737v1"
license: CC BY 4.0
url: https://arxiv.org/abs/2502.02737v1
pdf: wiki/assets/SmolLM2-2502.02737v1-annotated.pdf
pages: 24
---

# SmolLM2

**PDF:** [Open the annotated PDF](/wiki/assets/SmolLM2-2502.02737v1-annotated.pdf) (24 pages) · Loubna Ben Allal et al. · [arXiv:2502.02737v1](https://arxiv.org/abs/2502.02737v1) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

A 1.7B-parameter model trained on about 11 trillion tokens, far more than compute-optimal training would use, in several stages that mix web text with math, code and instruction data. Where existing data was too small or too noisy, the authors built their own: FineMath, Stack-Edu and SmolTalk. The paper is mostly about data choices, not architecture.

## How it connects

- It is the opposite end of [[Scaling-Laws-and-Compute]]: overtraining a small model to make it cheap to run.
- SmolTalk is the conversation data that [[nanochat]]'s SFT task file loads.
- It cites [DCLM](/wiki/resources/notes/Source-DCLM.md) for its web data.

## What the annotations point at

- [p. 1](/wiki/assets/SmolLM2-2502.02737v1-annotated.pdf#page=1): the 11T-token budget (a note works out the tokens per parameter) and the three new datasets.
- [p. 2](/wiki/assets/SmolLM2-2502.02737v1-annotated.pdf#page=2): the training compute and cost, with a margin box comparing it to nanochat's speedrun.
- [p. 3](/wiki/assets/SmolLM2-2502.02737v1-annotated.pdf#page=3): the citation of DCLM.

![[SmolLM2-2502.02737v1-annotated.pdf#page=1&height=560]]

## License

The paper is by its authors, redistributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with annotations added by this vault; see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
