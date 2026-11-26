---
title: "Learning Path: LLMs"
aliases:
  - Learning path
type: concept
methodology_role: learning-path
status: developing
created: 2026-11-20
updated: 2026-11-26
reading_time: 2
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/foundations
  - learning-path
---

# Learning Path: LLMs

Read in order; tick a box when you could explain the note without looking.

## Stage 1: what the model is

- [x] [Transformer Block](/wiki/resources/notes/Transformer-Block.md)
- [x] [BPE Tokenization](/wiki/resources/notes/BPE-Tokenization.md)
- [ ] [LLM Glossary](/wiki/resources/notes/LLM-Glossary.md), skimmed

## Stage 2: how it is trained

- [x] [LLM Training Pipeline](/wiki/resources/notes/LLM-Training-Pipeline.md)
- [ ] [Scaling Laws and Compute](/wiki/resources/notes/Scaling-Laws-and-Compute.md)
- [ ] [nanochat](/wiki/resources/notes/nanochat.md), then run its CPU example
- [ ] Read the annotations in [DCLM](/wiki/resources/notes/Source-DCLM.md) and [SmolLM2](/wiki/resources/notes/Source-SmolLM2.md)

## Stage 3: after pretraining

- [ ] [SFT vs RL](/wiki/resources/notes/SFT-vs-RL.md)
- [ ] [Reasoning Models and RL](/wiki/resources/notes/Reasoning-Models-and-RL.md), then [Dr. GRPO](/wiki/resources/notes/Source-Dr-GRPO.md)
- [ ] [DPO](/wiki/resources/notes/Source-DPO.md), preference tuning without RL
- [ ] [Mixture of Experts](/wiki/resources/notes/Mixture-of-Experts.md), not written yet, so the link is dimmed; read [Mixtral](/wiki/resources/notes/Source-Mixtral.md) for now

## Stage 4: serving

- [ ] [KV Cache](/wiki/resources/notes/KV-Cache.md)
- [ ] [YaRN](/wiki/resources/notes/Source-YaRN.md), for longer contexts
- [ ] The [project](/wiki/projects/Train-a-Tiny-Chat-Model/overview.md): train one and talk to it
