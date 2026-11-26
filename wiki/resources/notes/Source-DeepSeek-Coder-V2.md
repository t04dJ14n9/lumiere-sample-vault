---
title: "DeepSeek-Coder-V2"
aliases:
  - DeepSeek-Coder-V2
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
authors: "Qihao Zhu et al."
arxiv: "2406.11931v1"
license: CC BY 4.0
url: https://arxiv.org/abs/2406.11931v1
pdf: wiki/assets/DeepSeek-Coder-V2-2406.11931v1.pdf
pages: 19
---

# DeepSeek-Coder-V2

**PDF:** [Open the PDF](/wiki/assets/DeepSeek-Coder-V2-2406.11931v1.pdf) (19 pages) · Qihao Zhu et al. (DeepSeek-AI) · [arXiv:2406.11931v1](https://arxiv.org/abs/2406.11931v1) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

An open mixture-of-experts model for code, made by continuing the pretraining of an intermediate DeepSeek-V2 checkpoint on several trillion more tokens, mostly code and math. The continued training widens the set of programming languages and lengthens the context window, and the paper reports code results close to the best closed models of its time.

## How it connects

- Continued pretraining is a fourth option beside the stages in [[LLM-Training-Pipeline]]: start from someone else's base model and keep going on narrower data.
- [[nanochat]] has a small code task of its own and a tool that runs Python.
- [Mixtral](/wiki/resources/notes/Source-Mixtral.md) explains the mixture-of-experts layer.

## License

The paper is by its authors, redistributed unchanged under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
