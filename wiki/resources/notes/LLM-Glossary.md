---
title: LLM Glossary
aliases:
  - Glossary
type: concept
status: evergreen
created: 2026-11-20
updated: 2026-11-26
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/foundations
  - glossary
---

# LLM Glossary

Short definitions, with a link to the note that says more. The ==highlighted== terms are the ones I kept getting wrong. %%Add a term every time a note uses one I had to look up.%%

- **Base model**: A model after pretraining only: it continues text, it does not answer. See [[LLM-Training-Pipeline]].
- **Bits per byte (bpb)**: Loss measured per byte of text rather than per token, so tokenizers can be compared. nanochat reports `val_bpb`.
- **CORE**: The DCLM evaluation score nanochat uses to decide "GPT-2 grade". See [[Time-to-GPT-2-Leaderboard]].
- **==Compute optimal==**: The split of a fixed budget between model size and data that gives the lowest loss. See [[Scaling-Laws-and-Compute]].
- **FLOPs**: Floating-point operations, the unit of training compute. Not to be confused with FLOP/s, a speed.
- **GRPO**: Group relative policy optimization: RL that scores each sampled answer against its siblings. See [[Reasoning-Models-and-RL]].
- **==KV cache==**: Saved attention keys and values that make generation fast. See [[KV-Cache]].
- **MFU**: Model FLOPs utilization: the share of the hardware's peak that training actually uses.
- **SFT**: Supervised finetuning on example conversations. See [[SFT-vs-RL]].
- **Token**: ~~A word.~~ A piece of text from the tokenizer's vocabulary, often part of a word. See [[BPE-Tokenization]].
