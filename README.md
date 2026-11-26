# Lumiere sample vault

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/t04dJ14n9/lumiere-sample-vault?quickstart=1)

A small, made-up knowledge vault about **large language models**, built around
[nanochat](https://github.com/karpathy/nanochat) and recent LLM progress, for trying
[Lumiere](https://marketplace.visualstudio.com/items?itemName=t04dJ14n9.lumiere), the VS Code
extension that edits Markdown the way Obsidian's Live Preview does and reads PDFs.

Click the badge. GitHub starts a Codespace with VS Code in your browser, installs Lumiere, and
opens [`wiki/index.md`](wiki/index.md), a short tour of what Lumiere renders. Nothing to install.
Your edits stay in your own Codespace.

## What is inside

About 30 notes, written for this repository, all linked to each other.

| Path | Holds |
| --- | --- |
| `wiki/index.md` | "Start here": a tour and an index of which note shows which feature |
| `wiki/resources/notes/` | 16 notes: concepts, a repository card, two sources with PDFs, a question, a comparison, a playbook, a glossary |
| `wiki/resources/mocs/` | Three maps of content, with a live search and clickable Mermaid nodes |
| `wiki/resources/bases/` | Two `.base` files, embedded as live tables |
| `wiki/projects/Train-a-Tiny-Chat-Model/` | A project with overview, progress, decisions and discoveries |
| `wiki/areas/`, `wiki/archives/`, `wiki/daily/` | An area, a finished spike and two daily notes |
| `wiki/assets/` | An SVG and a PNG, two annotated PDFs (3 pages and 1 page) and a local HTML page |

What you can see in Lumiere: Live Preview, wikilinks (with aliases, headings and block ids) and
Markdown links, note and section embeds, images, PDFs with highlights, underlines and sticky notes,
an inline PDF page, a local HTML file as a card, Obsidian Bases, callouts (including folded ones),
math, tables, task lists, footnotes, tags, frontmatter Properties, code blocks and Mermaid diagrams.

The notes summarize their sources in their own words and link to them: the
[nanochat README](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md)
pinned to one commit, and a few papers on arXiv. Nothing from them is copied.

## Open it locally

1. Install [VS Code](https://code.visualstudio.com/) and clone this repository.
2. Open the folder. VS Code offers the recommended extension, [Lumiere](https://marketplace.visualstudio.com/items?itemName=t04dJ14n9.lumiere)
   (`t04dj14n9.lumiere`): install it.
3. `.vscode/settings.json` makes `*.md` open in Lumiere. Elsewhere, run **Use Lumiere for
   Markdown in This Workspace** from the Command Palette.
4. Open `wiki/index.md`.

The same folder opens as a vault in [Obsidian](https://obsidian.md). Lumiere is not affiliated
with Obsidian.

## Notes

- Lumiere runs in a desktop-style VS Code, including the one in a Codespace. It does not run in
  `vscode.dev` or the `.` editor on github.com.
- If the Codespace opens without Lumiere, install it from the Extensions view (search for
  "Lumiere") and reopen `wiki/index.md` with **Open With... > Lumiere**.
- Images, the PDFs (with their annotations) and the HTML file are drawn by `tools/make_assets.py`;
  run it with Python 3 to regenerate them. Everything here is original.

## License

[CC0 1.0](LICENSE): do what you like with it.
