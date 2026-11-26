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

About 35 notes, written for this repository, all linked to each other, and seven real papers.

| Path | Holds |
| --- | --- |
| `wiki/index.md` | "Start here": a tour and an index of which note shows which feature |
| `wiki/resources/notes/` | 22 notes: concepts, a repository card, seven paper sources, a list of classic papers, a question, a comparison, a playbook, a glossary |
| `wiki/resources/mocs/` | Three maps of content, with a live search and clickable Mermaid nodes |
| `wiki/resources/bases/` | Two `.base` files, embedded as live tables |
| `wiki/projects/Train-a-Tiny-Chat-Model/` | A project with overview, progress, decisions and discoveries |
| `wiki/areas/`, `wiki/archives/`, `wiki/daily/` | An area, a finished spike and two daily notes |
| `wiki/assets/` | An SVG, a PNG, a local HTML page, and seven CC BY 4.0 arXiv papers, four of them annotated ([ATTRIBUTION.md](wiki/assets/ATTRIBUTION.md)) |

What you can see in Lumiere: Live Preview, wikilinks (with aliases, headings and block ids) and
Markdown links, note and section embeds, images, real papers with highlights, underlines and sticky notes,
an inline PDF page, a local HTML file as a card, Obsidian Bases, callouts (including folded ones),
math, tables, task lists, footnotes, tags, frontmatter Properties, code blocks and Mermaid diagrams.

The notes summarize their sources in their own words: the
[nanochat README](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md)
pinned to one commit, the seven papers in `wiki/assets/`, and classic papers whose licenses only let us
link them.

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
- The SVG, the PNG and the HTML file are drawn by `tools/make_assets.py` (Python 3). The papers come from
  `tools/annotate_papers.py`, which downloads each pinned arXiv version, checks its SHA-256 and adds the
  annotations (needs `pymupdf`).

## License

The repository's own content is [CC0 1.0](LICENSE): do what you like with it. The exception is the
seven papers in `wiki/assets/`, which belong to their authors and keep their
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licenses; see
[wiki/assets/ATTRIBUTION.md](wiki/assets/ATTRIBUTION.md). The annotations added to four of them are CC0.
