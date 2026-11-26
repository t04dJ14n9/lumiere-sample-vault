---
title: "Sandbox: Try Lumiere Here"
aliases:
  - Sandbox
type: concept
status: seed
created: 2026-11-22
updated: 2026-11-26
reading_time: 2
reviewed: false
para: resource
mocs:
  - "[[wiki/resources/mocs/LLM-Map|LLM Map]]"
tags:
  - sandbox
---

# Sandbox: Try Lumiere Here

A note to break. Edit anything: VS Code keeps undo and save, and in a Codespace your changes stay in your own copy.

## Things to try

- [ ] Click into this line: the syntax of **bold**, *italic*, `code` and [a link](/wiki/index.md) appears around the caret and hides again when you leave.
- [ ] Type `[[` and pick a note from the suggestions. Type `[[#` for headings of this note and `[[^` for blocks.
- [ ] Select a word and press Ctrl+B (Cmd+B on a Mac) to bold it, Ctrl+I for italics.
- [ ] Tick this task by clicking its box.
- [ ] Hover a link with Ctrl (Cmd on a Mac) held to preview the note it points to.
- [ ] Open the Command Palette (F1) and run **Insert Callout**, **Insert Table** or **Insert Math Block**.
- [ ] Run **Go to Heading…** to jump around this note.
- [ ] Run **Toggle Live Preview/Source Mode** to see the plain Markdown.

## A little of everything

Text can be ==highlighted==, ~~struck through~~, written with `inline code`, or hidden in a %%comment that shows only while you edit%%.

> [!note] Callouts are blockquotes with a type
> Change `note` to `warning`, `tip`, `bug`, `quote`, `success` or any word you like.

Inline math such as $\mathrm{softmax}(z)_i = e^{z_i} / \sum_j e^{z_j}$ sits in a sentence. A display formula gets its own line:

$$C \approx 6ND$$

| Try | Then |
| --- | --- |
| Click a cell | Edit it in place |
| Drag a column grip | Move the column |
| Right-click a cell | Sort, align, insert |

A footnote[^one], a tag #sandbox, a nested list:

- Parent
    - Child
        - Grandchild

[^one]: Footnotes appear as small numbers in the text and as a numbered line down here.

## An agent-friendly detail

Select a passage in any note and run **Copy link to this**. It puts the passage and an `@path#lines` link on the clipboard, so an AI agent can be pointed to the exact lines.
