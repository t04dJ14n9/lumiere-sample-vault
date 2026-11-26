# Sample vault

A synthetic knowledge vault about large language models, centered on nanochat, laid out the way the
[claude-obsidian](https://github.com/t04dJ14n9/claude-obsidian) plugin lays out
a vault, and written to show [Lumiere](https://marketplace.visualstudio.com/items?itemName=t04dJ14n9.lumiere).

- Start at `wiki/index.md`. Notes live flat in `wiki/resources/notes/`, maps of
  content in `wiki/resources/mocs/`, projects in `wiki/projects/`.
- Links in note bodies are vault-root-relative Markdown links
  (`[Title](/wiki/resources/notes/Title.md)`), with wikilinks in a few places on
  purpose. Properties keep quoted wikilinks.
- The SVG, PNG and HTML under `wiki/assets/` come from `tools/make_assets.py`; the PDFs are real
  papers from `tools/annotate_papers.py`.
- All content is original and CC0. Do not add third-party text or images; summarize sources in your own
  words and link them (pin GitHub links to a commit).
- The one documented exception: CC BY 4.0 arXiv papers in `wiki/assets/`, added only through
  `tools/annotate_papers.py` (pinned version and SHA-256) and listed in `wiki/assets/ATTRIBUTION.md`.
  A paper under any other license is linked in `wiki/resources/notes/Classic-Papers.md`, never included.
