---
title: nanochat Study Notes
aliases:
  - Study notes PDF
type: source
status: mature
created: 2026-11-22
updated: 2026-11-26
reading_time: 8
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - llm/training
  - source
pdf: wiki/assets/nanochat-Study-Notes.pdf
pages: 3
---

# nanochat Study Notes

**PDF:** [Open the PDF](/wiki/assets/nanochat-Study-Notes.pdf) (3 pages)

A short set of reading notes on [[nanochat]], written for this vault and drawn by `tools/make_assets.py`. It stands in for a paper so you can try Lumiere's PDF reader: the links below open it at a page, the embed shows a page inline, and the PDF already carries **annotations**.

## Key points

1. **The pipeline.** One codebase covers tokenizer, pretraining, finetuning, evaluation and chat; one dial, the depth, sets the size. ([p. 1](/wiki/assets/nanochat-Study-Notes.pdf#page=1))
2. **What it costs.** $C = 6ND$, and the README's figures for a GPT-2 grade run. ([p. 2](/wiki/assets/nanochat-Study-Notes.pdf#page=2)) Worked through in [[What-Does-a-Tiny-Chat-Model-Cost]].
3. **After pretraining.** SFT teaches the shape of a chat; RL on checkable tasks rewards right answers. ([p. 3](/wiki/assets/nanochat-Study-Notes.pdf#page=3))

## Page 2, inline

![[nanochat-Study-Notes.pdf#page=2&height=520]]

## The annotations in it

Every page has a highlight, an underline and a sticky note or a margin box. They are standard PDF annotations, so they show in Lumiere's reader and its annotation panel, and in any other PDF reader. Add your own: select text, right-click, **Highlight**. Lumiere keeps yours beside the PDF, under `.lumiere/pdf-annotations/`, and changes the file only if you run **Save Annotations into This PDF**.

## Provenance

Written for this vault and released under CC0. Every number in it comes from the [nanochat README at commit 92d63d4](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md).[^why] Page links also work in a wikilink: [[nanochat-Study-Notes.pdf#page=3|page 3 as a wikilink]].

[^why]: Pinned to a commit because the README changes as the leaderboard moves.
