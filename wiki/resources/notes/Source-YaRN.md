---
title: "YaRN"
aliases:
  - YaRN
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
  - llm/inference
authors: "Bowen Peng et al."
arxiv: "2309.00071v3"
license: CC BY 4.0
url: https://arxiv.org/abs/2309.00071v3
pdf: wiki/assets/YaRN-2309.00071v3-annotated.pdf
pages: 20
---

# YaRN

**PDF:** [Open the annotated PDF](/wiki/assets/YaRN-2309.00071v3-annotated.pdf) (20 pages) · Bowen Peng et al. · [arXiv:2309.00071v3](https://arxiv.org/abs/2309.00071v3) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What it says

Models that encode positions with rotary embeddings (RoPE) break down on texts longer than they were trained on. YaRN stretches a trained model's context by rescaling the rotation speeds of RoPE's dimensions unevenly, so fast-turning dimensions keep their local detail while slow ones are interpolated. The paper reports needing far fewer tokens and training steps than earlier extension methods.

## How it connects

- RoPE is how a [[Transformer-Block]] can see the distance between tokens; this paper explains it well on its page 3.
- Longer contexts make the [[KV-Cache]] the main memory cost.
- The RoPE paper itself is in [[Classic-Papers]], linked only.

## What the annotations point at

- [p. 1](/wiki/assets/YaRN-2309.00071v3-annotated.pdf#page=1): what RoPE is and the problem the paper solves.
- [p. 3](/wiki/assets/YaRN-2309.00071v3-annotated.pdf#page=3): why RoPE depends only on relative distance, and what a dimension's wavelength means, with a margin box and a note.

![[YaRN-2309.00071v3-annotated.pdf#page=3&height=560]]

## License

The paper is by its authors, redistributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with annotations added by this vault; see [ATTRIBUTION](/wiki/assets/ATTRIBUTION.md).
