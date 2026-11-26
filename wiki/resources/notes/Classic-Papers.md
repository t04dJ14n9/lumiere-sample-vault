---
title: Classic Papers
aliases:
  - Papers linked only
type: concept
status: developing
created: 2026-11-26
updated: 2026-11-26
reading_time: 2
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - source
  - llm/foundations
---

# Classic Papers

Papers this vault relies on but does not include: arXiv's default license or a restrictive Creative Commons license does not let us pass the PDF on, so each is a link with one line on why it matters. The papers that *are* in the vault are CC BY 4.0, listed in the [Sources and Reading Map](/wiki/resources/mocs/Sources-and-Reading-Map.md).

| Paper | arXiv | Why it matters here |
| --- | --- | --- |
| Attention Is All You Need | [1706.03762](https://arxiv.org/abs/1706.03762) | the transformer, see [[Transformer-Block]] |
| Scaling Laws for Neural Language Models | [2001.08361](https://arxiv.org/abs/2001.08361) | loss as a power law of compute, and $C \approx 6ND$ |
| Training Compute-Optimal LLMs (Chinchilla) | [2203.15556](https://arxiv.org/abs/2203.15556) | about 20 tokens per parameter, see [[Scaling-Laws-and-Compute]] |
| RoFormer (RoPE), CC BY-NC-ND | [2104.09864](https://arxiv.org/abs/2104.09864) | rotary position embeddings, which [YaRN](/wiki/resources/notes/Source-YaRN.md) extends |
| DeepSeekMath (GRPO) | [2402.03300](https://arxiv.org/abs/2402.03300) | the GRPO method in [[Reasoning-Models-and-RL]] |
| DeepSeek-V2 (MLA) | [2405.04434](https://arxiv.org/abs/2405.04434) | multi-head latent attention, a smaller [[KV-Cache]] |
| DeepSeek-V3 | [2412.19437](https://arxiv.org/abs/2412.19437) | a large open mixture-of-experts model that reports its full training cost |
| DeepSeek-R1 | [2501.12948](https://arxiv.org/abs/2501.12948) | reasoning learned through RL, examined by [Dr. GRPO](/wiki/resources/notes/Source-Dr-GRPO.md) |
| Training LMs to Follow Instructions (InstructGPT) | [2203.02155](https://arxiv.org/abs/2203.02155) | SFT then RL from human feedback, simplified by [DPO](/wiki/resources/notes/Source-DPO.md) |
