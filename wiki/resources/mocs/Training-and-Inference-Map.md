---
title: Training and Inference Map
type: meta
methodology_role: moc
status: developing
created: 2026-11-21
updated: 2026-11-26
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
tags:
  - moc
  - llm/training
---

# Training and Inference Map

How a model is built, stage by stage, and then served.

## Building it

1. [BPE Tokenization](/wiki/resources/notes/BPE-Tokenization.md)
2. [Transformer Block](/wiki/resources/notes/Transformer-Block.md)
3. [LLM Training Pipeline](/wiki/resources/notes/LLM-Training-Pipeline.md)
4. [Scaling Laws and Compute](/wiki/resources/notes/Scaling-Laws-and-Compute.md)
5. [SFT vs RL](/wiki/resources/notes/SFT-vs-RL.md), and [DPO](/wiki/resources/notes/Source-DPO.md) between them
6. Data: [DCLM](/wiki/resources/notes/Source-DCLM.md) and [SmolLM2](/wiki/resources/notes/Source-SmolLM2.md)

## Serving it

- [KV Cache](/wiki/resources/notes/KV-Cache.md)
- [YaRN](/wiki/resources/notes/Source-YaRN.md): longer contexts than training

## When it goes wrong

- [Playbook: debugging a loss spike](/wiki/resources/notes/Playbook-Debugging-a-Loss-Spike.md)

## Everything tagged `llm/training`

The block below is a live search, written as a fenced `query` block. It lists matching notes and updates as the vault changes.

```query
tag:#llm/training
```

## Adjacent maps

- [LLM Map](/wiki/resources/mocs/LLM-Map.md)
- [Sources and Reading Map](/wiki/resources/mocs/Sources-and-Reading-Map.md)
