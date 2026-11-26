---
title: "Mixtral of Experts"
aliases:
  - Mixtral
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
  - llm/progress
authors: "Albert Q. Jiang et al."
arxiv: "2401.04088v1"
license: CC BY 4.0
url: https://arxiv.org/abs/2401.04088v1
pdf: wiki/assets/Mixtral-of-Experts-2401.04088v1.pdf
pages: 13
---

# Mixtral of Experts

**PDF:** [Open the PDF](/wiki/assets/Mixtral-of-Experts-2401.04088v1.pdf) (13 pages) · Albert Q. Jiang et al. · [arXiv:2401.04088v1](https://arxiv.org/abs/2401.04088v1) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

A sparse mixture-of-experts model: every layer has 8 feedforward blocks, and a small router sends each token to 2 of them. Each token therefore draws on a large pool of parameters while only a fraction of them run for it, which keeps inference cost close to that of a much smaller dense model. The weights were released openly.

## How it connects

- The MLP half of a [[Transformer-Block]] is what gets split into experts.
- It is the reading for the not-yet-written Mixture of Experts note in the [learning path](/wiki/resources/notes/Learning-Path-LLMs.md#stage-3-after-pretraining).
- [DeepSeek-Coder-V2](/wiki/resources/notes/Source-DeepSeek-Coder-V2.md) is another mixture-of-experts model.

## License

The paper is by its authors, redistributed unchanged under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
