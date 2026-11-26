---
title: "DataComp-LM (DCLM)"
aliases:
  - DCLM
type: source
status: developing
created: 2026-11-26
updated: 2026-11-26
reading_time: 10
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - source
  - llm/training
authors: "Jeffrey Li et al."
arxiv: "2406.11794v4"
license: CC BY 4.0
url: https://arxiv.org/abs/2406.11794v4
pdf: wiki/assets/DCLM-2406.11794v4-annotated.pdf
pages: 89
---

# DataComp-LM (DCLM)

**PDF:** [Open the annotated PDF](/wiki/assets/DCLM-2406.11794v4-annotated.pdf) (89 pages) · Jeffrey Li et al. · [arXiv:2406.11794v4](https://arxiv.org/abs/2406.11794v4) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

DCLM turns "which training data is best?" into a benchmark: the training code and the evaluations are fixed, and entrants change only the data, drawn from one shared pool of Common Crawl text. Its baseline experiments find that filtering with a model is what most improves a training set. It also defines the CORE score, an average over many tasks that small models can already be measured on.

## How it connects

- CORE is the score [[nanochat]]'s [[Time-to-GPT-2-Leaderboard]] uses, with GPT-2 at 0.2565.
- The leaderboard's biggest speedup in our snapshot was a change of dataset, which is this paper's whole argument.
- [SmolLM2](/wiki/resources/notes/Source-SmolLM2.md) builds on DCLM data.

## What the annotations point at

- [p. 1](/wiki/assets/DCLM-2406.11794v4-annotated.pdf#page=1): the size of the shared pool, with a note on why it matters here.
- [p. 2](/wiki/assets/DCLM-2406.11794v4-annotated.pdf#page=2): the claim that better data gives better and cheaper models.
- [p. 3](/wiki/assets/DCLM-2406.11794v4-annotated.pdf#page=3): small models already rank datasets correctly.
- [p. 6](/wiki/assets/DCLM-2406.11794v4-annotated.pdf#page=6): where CORE is defined, with a margin box linking it to nanochat.

![[DCLM-2406.11794v4-annotated.pdf#page=6&height=560]]

## License

The paper is by its authors, redistributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with annotations added by this vault; see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
