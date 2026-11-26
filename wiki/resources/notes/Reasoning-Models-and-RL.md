---
title: Reasoning Models and RL
aliases:
  - Reasoning models
  - RL with verifiable rewards
type: concept
status: developing
created: 2026-11-24
updated: 2026-11-26
reading_time: 3
reviewed: false
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/post-training
  - llm/progress
---

# Reasoning Models and RL

A major shift in LLMs since chat models is spending more compute at answer time: models that write out a long chain of reasoning before answering, trained with reinforcement learning on problems whose answers can be **checked by a program**.

## Timeline

| When | What | Link |
| --- | --- | --- |
| 2024-02 | GRPO, an RL method without a value network, on math | [DeepSeekMath](https://arxiv.org/abs/2402.03300) |
| 2024-09 | OpenAI's o1, a model trained to reason before answering | [Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) |
| 2025-01 | DeepSeek-R1, reasoning learned mostly from rule-based rewards | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |

## Verifiable rewards

A reward that code computes, such as "is the final number right" or "do the tests pass", cannot be flattered and costs nothing per sample. The model samples several answers to the same problem; GRPO scores each one against the group:

$$A_i = \frac{r_i - \operatorname{mean}(r_1, \dots, r_G)}{\operatorname{std}(r_1, \dots, r_G)}$$

Answers better than their siblings are made more likely, worse ones less.[^grpo]

> [!warning] A known bias
> [Dr. GRPO](/wiki/resources/notes/Source-Dr-GRPO.md) shows that dividing by the group's spread and by answer length biases training toward longer answers, especially wrong ones, and drops both. Its PDF is in this vault, annotated.

> [!tip] In nanochat
> The README lists an RL script, `scripts/chat_rl.py`, and a GSM8K task of grade-school math problems, a natural fit for a checker.

> [!warning]- Limits
> Verifiable rewards only cover tasks with a checker. Writing, judgment and open questions still rely on human or model preferences.

Compared with finetuning: [[SFT-vs-RL]].

[^grpo]: The group-relative advantage is from [DeepSeekMath](https://arxiv.org/abs/2402.03300), section 4.
