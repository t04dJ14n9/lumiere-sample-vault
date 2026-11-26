---
title: Start here
aliases:
  - Home
  - Index
type: meta
status: evergreen
created: 2026-11-20
updated: 2026-11-26
tags:
  - meta
  - index
---

# Start here

Welcome. This is a small, made-up knowledge vault about **large language models**, built around [nanochat](/wiki/resources/notes/nanochat.md), a small repository that trains a chat model end to end, and a few notes on recent progress. It exists to show what [Lumiere](https://marketplace.visualstudio.com/items?itemName=t04dJ14n9.lumiere) does with Obsidian-style notes and PDFs in VS Code. Everything in it is written for this vault and free to reuse (CC0).

You are looking at it in Live Preview. **Click into any line** and the Markdown behind it appears around the caret, then hides again when you leave. Use **Toggle Live Preview/Source Mode** in the Command Palette (F1) to see the plain text.

## A five-minute tour

1. **Follow a link.** Ctrl-click (Cmd-click on a Mac) a link to open it in a new tab. Note bodies use Markdown links, like [LLM Training Pipeline](/wiki/resources/notes/LLM-Training-Pipeline.md), and wikilinks in places, like [[Scaling-Laws-and-Compute|scaling laws]]. Both resolve the same way.
2. **Jump to a heading or a block.** [[Transformer-Block#Attention in one line]] goes to a section, and [[nanochat#^one-dial]] goes to one paragraph by its block id.
3. **Embed a note.** The section under [An embedded note](#an-embedded-note) is not copied, it is the "short version" of the [pipeline note](/wiki/resources/notes/LLM-Training-Pipeline.md), shown in place with `![[LLM-Training-Pipeline#The short version]]`.
4. **Open a PDF at a page.** [Page 2 of the study notes](/wiki/assets/nanochat-Study-Notes.pdf#page=2) opens in Lumiere's PDF reader, already annotated: a highlight, an underline and a margin note. The [source note](/wiki/resources/notes/Source-nanochat-Study-Notes.md) also draws that page inline.
5. **Read the properties.** Open any note: the frontmatter at the top is a typed editor, with dates, a checkbox, numbers, tags and links as chips.
6. **Look around.** Open **Go to Heading…** (outline), **Quick Switcher**, **Search Vault…**, and **Open Vault Graph** from the Command Palette. The Explorer has **Markdown Outline**, **Tags**, **Backlinks** and **Outgoing Links** sections.

> [!tip] Where is everything?
> The files are in the Explorer under `wiki/`. If you would rather not look at folders, the [[LLM-Map]] is a hub that links to all of it.

## An embedded note

![[LLM-Training-Pipeline#The short version]]

## What each note shows

| Feature | Look at |
| --- | --- |
| Wikilinks, aliases, heading and block links, embeds of a section | [[LLM-Training-Pipeline]], [[Transformer-Block]], this page |
| Callouts, many types, some folded | [[Playbook-Debugging-a-Loss-Spike]], [[Reasoning-Models-and-RL]], [[nanochat]] |
| Inline and display math | [[Transformer-Block]], [[Scaling-Laws-and-Compute]], [[Reasoning-Models-and-RL]], [[KV-Cache]] |
| Tables, edited as a grid | [[Time-to-GPT-2-Leaderboard]], [[SFT-vs-RL]], [[What-Does-a-Tiny-Chat-Model-Cost]] |
| Code blocks with highlighting | [[BPE-Tokenization]] (Python), [[KV-Cache]] (TypeScript), [[Playbook-Debugging-a-Loss-Spike]] and [[nanochat]] (shell) |
| Mermaid diagrams | [[LLM-Training-Pipeline]], and clickable nodes in [[LLM-Map]] |
| Images, SVG and PNG | [[LLM-Training-Pipeline]], [[Playbook-Debugging-a-Loss-Spike]], [project progress](/wiki/projects/Train-a-Tiny-Chat-Model/progress.md) |
| PDF reader, page links, an inline page, annotations | [[Source-nanochat-Study-Notes]], [[Source-Scaling-Laws-Cheat-Sheet]] |
| A local HTML file as a card | [[BPE-Tokenization]] |
| Bases (a live table of notes) | [[LLM-Map]], [LLM Study](/wiki/areas/LLM-Study.md) |
| A live search in a `query` block | [Training and Inference Map](/wiki/resources/mocs/Training-and-Inference-Map.md) |
| Task lists | [Learning path](/wiki/resources/notes/Learning-Path-LLMs.md), [project overview](/wiki/projects/Train-a-Tiny-Chat-Model/overview.md) |
| Footnotes | [[Scaling-Laws-and-Compute]], [[Reasoning-Models-and-RL]], [[What-Does-a-Tiny-Chat-Model-Cost]] |
| Highlights, comments, strikethrough | [[LLM-Glossary]], [[Sandbox-Try-Lumiere-Here]] |
| A dimmed link to a note that does not exist yet | [Learning path](/wiki/resources/notes/Learning-Path-LLMs.md#stage-3-after-pretraining) |

## How the vault is laid out

The layout follows [claude-obsidian](https://github.com/t04dJ14n9/claude-obsidian): projects and areas for action, maps of content and flat notes for knowledge.

| Folder | What it holds |
| --- | --- |
| `wiki/projects/Train-a-Tiny-Chat-Model/` | A project: [overview](/wiki/projects/Train-a-Tiny-Chat-Model/overview.md), [progress](/wiki/projects/Train-a-Tiny-Chat-Model/progress.md), [decisions](/wiki/projects/Train-a-Tiny-Chat-Model/decisions.md), [discoveries](/wiki/projects/Train-a-Tiny-Chat-Model/discoveries.md) |
| `wiki/areas/` | An ongoing responsibility: [LLM Study](/wiki/areas/LLM-Study.md) |
| `wiki/resources/mocs/` | Maps of content, the entry points |
| `wiki/resources/notes/` | The notes themselves, flat: concepts, a repository card, two sources, a question, a comparison, a playbook |
| `wiki/resources/bases/` | `.base` files that list notes by their properties |
| `wiki/archives/` | Finished work: [Char-level GPT spike](/wiki/archives/Char-Level-GPT-Spike.md) |
| `wiki/daily/` | Daily notes: [today](/wiki/daily/2026-11-26.md) and [yesterday](/wiki/daily/2026-11-25.md) |
| `wiki/assets/` | The images, the two PDFs and the HTML file |

Also in `wiki/`: [Recent context](/wiki/hot.md), a cache of what I was doing, and the [Operation log](/wiki/log.md).

## Try it yourself

- [ ] Open the [sandbox](/wiki/resources/notes/Sandbox-Try-Lumiere-Here.md) and break something.
- [ ] Tick this box by clicking it.
- [ ] Type `[[` in the sandbox and pick a note.
- [ ] Open [BPE Tokenization](/wiki/resources/notes/BPE-Tokenization.md) and click **Open** on the HTML card.
- [ ] Open the [cheat sheet PDF](/wiki/assets/Scaling-Laws-Cheat-Sheet.pdf) and highlight a line of your own.

> [!info] Lumiere is not affiliated with Obsidian
> The vault is plain Markdown and also opens in Obsidian, where `.base` files and most of the syntax here work too.
