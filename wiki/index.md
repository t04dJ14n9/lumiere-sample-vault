---
title: Start here
aliases:
  - Home
  - Index
type: meta
status: evergreen
created: 2026-10-20
updated: 2026-11-22
tags:
  - meta
  - index
---

# Start here

Welcome. This is a small, made-up knowledge vault about **distributed systems**, written to show what [Lumiere](https://marketplace.visualstudio.com/items?itemName=t04dJ14n9.lumiere) can do with Obsidian-style notes in VS Code. Everything in it is synthetic and free to reuse (CC0).

You are looking at it in Live Preview. **Click into any line** and the Markdown behind it appears around the caret, then hides again when you leave. Use **Toggle Live Preview/Source Mode** in the Command Palette (F1) to see the plain text.

## A five-minute tour

1. **Follow a link.** Ctrl-click (Cmd-click on a Mac) a link to open it in a new tab. This vault uses Markdown links in note bodies, like [Distributed Systems Fundamentals](/wiki/resources/notes/Distributed-Systems-Fundamentals.md), and wikilinks in places, like [[Quorum-Reads-and-Writes|quorums]]. Both resolve the same way.
2. **Jump to a heading or a block.** [[Quorum-Reads-and-Writes#Choosing R and W]] goes to a section, and [[Lamport-Clocks#^happens-before]] goes to one paragraph by its block id.
3. **Embed a note.** The section under [An embedded note](#an-embedded-note) is not copied, it is the "short version" of the [CAP theorem](/wiki/resources/notes/CAP-Theorem.md), shown in place with `![[CAP-Theorem#The short version]]`.
4. **Open a PDF at a page.** [Page 2 of the lecture notes](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=2) opens in Lumiere's PDF reader. The [source note](/wiki/resources/notes/Source-Replication-and-Quorums-Lecture-Notes.md) also draws that page inline.
5. **Read the properties.** Open any note: the frontmatter at the top is a typed editor, with dates, a checkbox, numbers, tags and links as chips.
6. **Look around.** Open **Go to Heading…** (outline), **Quick Switcher**, **Search Vault…**, and **Open Vault Graph** from the Command Palette. The Explorer has **Markdown Outline**, **Tags**, **Backlinks** and **Outgoing Links** sections.

> [!tip] Where is everything?
> The files are in the Explorer under `wiki/`. If you would rather not look at folders, the [[Distributed-Systems-Map]] is a hub that links to all of it.

## An embedded note

![[CAP-Theorem#The short version]]

## What each note shows

| Feature | Look at |
| --- | --- |
| Wikilinks, aliases, heading and block links, embeds of a section or a block | [[Replication-Strategies]], [[Logical-Clocks-Compared]], this page |
| Callouts, many types, some folded | [[Distributed-Systems-Fundamentals]], [[CAP-Theorem]], [[Playbook-Debugging-Replica-Divergence]] |
| Inline and display math | [[Quorum-Reads-and-Writes]], [[Lamport-Clocks]], [[Failure-Detection]], [[Gossip-Protocols]] |
| Tables, edited as a grid | [[Replication-Strategies]], [[Two-Phase-Commit]], [[How-Many-Replicas-Do-I-Need]] |
| Code blocks with highlighting | [[Consistent-Hashing]] (Python), [[Raft-Leader-Election]] (Go), [[Failure-Detection]] (TypeScript), [[Playbook-Debugging-Replica-Divergence]] (shell) |
| Mermaid diagrams | [[Replication-Strategies]], [[Raft-Leader-Election]], [[Raft-Log-Replication]], [[Two-Phase-Commit]], and clickable nodes in [[Distributed-Systems-Map]] |
| Images, SVG and PNG | [[Quorum-Reads-and-Writes]], [[Consistent-Hashing]], [Toy KV progress](/wiki/projects/Toy-Replicated-KV/progress.md) |
| PDF reader, page links, an inline page | [[Source-Replication-and-Quorums-Lecture-Notes]] |
| A local HTML file as a card | [[Consistent-Hashing]] |
| Bases (a live table of notes) | [[Distributed-Systems-Map]], [Distributed Systems Study](/wiki/areas/Distributed-Systems-Study.md) |
| A live search in a `query` block | [Consensus and Replication Map](/wiki/resources/mocs/Consensus-and-Replication-Map.md) |
| Task lists | [Learning path](/wiki/resources/notes/Learning-Path-Distributed-Systems.md), [Toy KV overview](/wiki/projects/Toy-Replicated-KV/overview.md) |
| Footnotes | [[CAP-Theorem]], [[Gossip-Protocols]], [[Failure-Detection]] |
| Highlights, comments, strikethrough | [[Distributed-Systems-Glossary]], [[Sandbox-Try-Lumiere-Here]] |
| A dimmed link to a note that does not exist yet | [Learning path](/wiki/resources/notes/Learning-Path-Distributed-Systems.md#stage-3-consensus) |

## How the vault is laid out

The layout follows [claude-obsidian](https://github.com/t04dJ14n9/claude-obsidian): projects and areas for action, maps of content and flat notes for knowledge.

| Folder | What it holds |
| --- | --- |
| `wiki/projects/Toy-Replicated-KV/` | A project: [overview](/wiki/projects/Toy-Replicated-KV/overview.md), [progress](/wiki/projects/Toy-Replicated-KV/progress.md), [decisions](/wiki/projects/Toy-Replicated-KV/decisions.md), [discoveries](/wiki/projects/Toy-Replicated-KV/discoveries.md) |
| `wiki/areas/` | An ongoing responsibility: [Distributed Systems Study](/wiki/areas/Distributed-Systems-Study.md) |
| `wiki/resources/mocs/` | Maps of content, the entry points |
| `wiki/resources/notes/` | The notes themselves, flat: concepts, a source, a question, a comparison, a playbook |
| `wiki/resources/bases/` | `.base` files that list notes by their properties |
| `wiki/archives/` | Finished work: [Heartbeat simulator spike](/wiki/archives/Heartbeat-Simulator-Spike.md) |
| `wiki/daily/` | Daily notes: [today](/wiki/daily/2026-11-22.md) and [yesterday](/wiki/daily/2026-11-21.md) |
| `wiki/assets/` | The images, the PDF and the HTML file |

Also in `wiki/`: [Recent context](/wiki/hot.md), a cache of what I was doing, and the [Operation log](/wiki/log.md).

## Try it yourself

- [ ] Open the [sandbox](/wiki/resources/notes/Sandbox-Try-Lumiere-Here.md) and break something.
- [ ] Tick this box by clicking it.
- [ ] Type `[[` in the sandbox and pick a note.
- [ ] Open [Consistent Hashing](/wiki/resources/notes/Consistent-Hashing.md) and click **Open** on the HTML card.

> [!info] Lumiere is not affiliated with Obsidian
> The vault is plain Markdown and also opens in Obsidian, where `.base` files and most of the syntax here work too.
