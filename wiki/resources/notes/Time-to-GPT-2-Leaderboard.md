---
title: Time-to-GPT-2 Leaderboard
aliases:
  - GPT-2 speedrun
type: concept
status: developing
created: 2026-11-23
updated: 2026-11-26
reading_time: 2
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - llm/progress
  - llm/training
---

# Time-to-GPT-2 Leaderboard

[[nanochat]] keeps a leaderboard for one number: the wall-clock time to train a model that beats GPT-2's CORE score (0.256525) on one 8×H100 node. CORE is the evaluation score from the DCLM paper. It is a compact way to watch progress in pretraining.

## The rows, as the README lists them

| # | Hours | CORE | Change | Date |
| --- | --- | --- | --- | --- |
| 0 | 168 | 0.2565 | the original GPT-2 | 2019 |
| 1 | 3.04 | 0.2585 | d24 baseline | 2026-01-29 |
| 2 | 2.91 | 0.2578 | d26, fp8 | 2026-02-02 |
| 3 | 2.76 | 0.2602 | total batch of 1M tokens | 2026-02-05 |
| 4 | 2.02 | 0.2571 | NVIDIA ClimbMix data | 2026-03-04 |
| 5 | 1.80 | 0.2690 | autoresearch, round 1 | 2026-03-09 |
| 6 | 1.65 | 0.2626 | autoresearch, round 2 | 2026-03-14 |

Source: the [README at commit 92d63d4](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md#time-to-gpt-2-leaderboard), which says the leaderboard focuses on pretraining because it takes most of the compute.

## What the rows say

- Precision, batch size and **data** each moved the time; the biggest single jump in this list is the dataset change.
- Rows 5 and 6 came from *autoresearch*, changes found by an automated search rather than by hand.
- Times fall from about 3 hours to about 1.65 hours in under two months.

> [!note] Check before quoting
> The leaderboard moves. Treat this table as a snapshot of the README at one commit.

Cost at these speeds: [[What-Does-a-Tiny-Chat-Model-Cost]].
