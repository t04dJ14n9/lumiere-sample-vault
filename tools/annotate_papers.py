"""Download CC BY 4.0 arXiv papers into wiki/assets/, four of them annotated.

    pip install pymupdf
    python3 tools/annotate_papers.py [--from DIR]

With --from, read <arxiv-id>.pdf files already downloaded to DIR instead of
fetching them (still checked against the pinned SHA-256).

Each paper is pinned to an arXiv version and its SHA-256, so the annotations
land on the same text every time. The papers belong to their authors and are
redistributed under CC BY 4.0 (see wiki/assets/ATTRIBUTION.md); the only change
is the annotations added here, whose notes are this repository's own (CC0).
"""

import hashlib
import sys
import time
import urllib.request
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "wiki" / "assets"
AUTHOR = "Lumiere sample vault"
YELLOW = (1.0, 0.92, 0.45)
BLUE = (0.25, 0.47, 0.85)

PAPERS = [
    {
        "arxiv": "2406.11794v4",
        "sha256": "af8fc884ccd601f8c6fbbba8f8e381de652fce1233949c0c64f64b4ab4b0f5b2",
        "out": "DCLM-2406.11794v4-annotated.pdf",
        "marks": [
            (
                1,
                "highlight",
                "a standardized corpus of 240T tokens extracted from Common",
                None,
            ),
            (
                1,
                "note",
                "Common",
                (
                    "DCLM-Pool: the raw web text that every entry filters. "
                    "nanochat's leaderboard is scored with this paper's CORE metric."
                ),
            ),
            (
                2,
                "highlight",
                "Improving training sets leads to better models that are cheaper to train.",
                None,
            ),
            (3, "underline", "models as small as 400M parameters", None),
            (
                3,
                "note",
                "400M parameters",
                (
                    "Small runs still rank datasets correctly. "
                    "The same bet as iterating on a small nanochat model before a big run."
                ),
            ),
            (6, "highlight", "we propose the CORE centered accuracy", None),
            (
                6,
                "freetext",
                "CORE centered accuracy",
                (
                    "CORE = the score nanochat's "
                    "Time-to-GPT-2 leaderboard reports (GPT-2: 0.2565)."
                ),
            ),
        ],
    },
    {
        "arxiv": "2502.02737v1",
        "sha256": "a95fbda201d21cd25c89e949636373d36c288bd2d287e3cabd208e2041ea36d3",
        "out": "SmolLM2-2502.02737v1-annotated.pdf",
        "marks": [
            (1, "highlight", "we overtrain SmolLM2 on ~11 trillion", None),
            (
                1,
                "note",
                "11 trillion",
                (
                    "11T tokens / 1.7B parameters is about 6,500 tokens "
                    "per parameter, far past the ~20 that is compute optimal. Overtraining buys a "
                    "cheaper model to run."
                ),
            ),
            (1, "underline", "Stack-Edu, and SmolTalk)", None),
            (
                1,
                "note",
                "SmolTalk)",
                (
                    "SmolTalk is the chat data nanochat's SFT task file "
                    "(tasks/smoltalk.py) loads."
                ),
            ),
            (2, "highlight", "around 1e23 FLOPs, or $250,000", None),
            (
                2,
                "freetext",
                "1e23 FLOPs",
                (
                    "Scale check: the nanochat speedrun is a 4e19 "
                    "FLOPs model, about 2,500 times less compute."
                ),
            ),
            (3, "underline", "DCLM (Li et al., 2024c)", None),
            (
                3,
                "note",
                "DCLM (Li et al., 2024c)",
                (
                    "DCLM is the other paper in this vault: "
                    "DCLM-2406.11794v4-annotated.pdf."
                ),
            ),
        ],
    },
    {
        "arxiv": "2503.20783v2",
        "sha256": "98243d51297f011fb5baad8a70a972d061ffbef618f1d7cfc10deea37c5887d0",
        "out": "Dr-GRPO-2503.20783v2-annotated.pdf",
        "marks": [
            (
                1,
                "highlight",
                "we identify an optimization bias in Group Relative Policy Optimization",
                None,
            ),
            (
                1,
                "note",
                "we identify an optimization bias",
                (
                    "GRPO is the RL method of the "
                    "DeepSeekMath paper. The bias found here: the way its loss is averaged lets "
                    "wrong answers grow longer and longer."
                ),
            ),
            (1, "underline", "DeepSeek-V3-Base already exhibit", None),
            (
                1,
                "note",
                "DeepSeek-V3-Base already exhibit",
                (
                    "The famous 'aha moment' shows up "
                    "in the base model already, before any RL."
                ),
            ),
            (
                2,
                "highlight",
                "Right (Dr. GRPO), which leads to better token efficiency",
                None,
            ),
            (
                4,
                "underline",
                "if a base policy cannot even sample a single trajectory that leads to the correct",
                None,
            ),
            (
                4,
                "freetext",
                "if a base policy cannot even sample",
                (
                    "No correct sample, no "
                    "reward, nothing to learn. RL can only sharpen what the model can already do "
                    "sometimes."
                ),
            ),
        ],
    },
    {
        "arxiv": "2309.00071v3",
        "sha256": "e7c0268a796138460c6ba2f67a7cba5bd922c401aea94c1fcd09c4b76b883c85",
        "out": "YaRN-2309.00071v3-annotated.pdf",
        "marks": [
            (
                1,
                "highlight",
                "Rotary Position Embeddings (RoPE) have been shown to effectively encode",
                None,
            ),
            (
                1,
                "note",
                "Rotary Position Embeddings (RoPE)",
                (
                    "RoPE (the RoFormer paper) rotates "
                    "queries and keys by an angle that grows with position."
                ),
            ),
            (
                1,
                "underline",
                "fail to generalize past the sequence length they were trained on",
                None,
            ),
            (3, "highlight", "only depends on the relative distance", None),
            (
                3,
                "freetext",
                "only depends on the relative distance",
                (
                    "The point of RoPE: "
                    "attention sees how far apart two tokens are, not where they are."
                ),
            ),
            (
                3,
                "underline",
                "The wavelength describes the length of tokens needed",
                None,
            ),
            (
                3,
                "note",
                "The wavelength describes",
                (
                    "Each dimension turns at its own speed. "
                    "Context extension methods like YaRN rescale these speeds."
                ),
            ),
        ],
    },
]

# Redistributed unchanged, for completeness.
PLAIN = [
    (
        "2406.11931v1",
        "de4e77c86e6320ff0974aac3825133540fa7ddc31da79e0d8a353dc6264549a3",
        "DeepSeek-Coder-V2-2406.11931v1.pdf",
    ),
    (
        "2401.04088v1",
        "f8bbf0e9d979b7a8ce7be65119266545a229a85b57e077d8bd048e458bb642da",
        "Mixtral-of-Experts-2401.04088v1.pdf",
    ),
    (
        "2305.18290v3",
        "92cb3a2b71362acda98a789b03d88688fd33cf5fcf13f81d2b1de30ee7d3b67a",
        "DPO-2305.18290v3.pdf",
    ),
]


def fetch(arxiv: str, sha256: str, local: Path | None) -> bytes:
    if local is not None:
        data = (local / f"{arxiv}.pdf").read_bytes()
    else:
        time.sleep(3)  # arXiv asks automated clients to pace their requests
        url = f"https://arxiv.org/pdf/{arxiv}"
        request = urllib.request.Request(
            url, headers={"User-Agent": "lumiere-sample-vault"}
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != sha256:
        sys.exit(f"{arxiv}: SHA-256 {digest} is not the pinned {sha256}")
    return data


def find(page: pymupdf.Page, text: str) -> list[pymupdf.Quad]:
    quads = page.search_for(text, quads=True)
    if not quads:
        sys.exit(f"page {page.number + 1}: text not found: {text!r}")
    return quads


def text_area(page: pymupdf.Page) -> pymupdf.Rect:
    """The body text's bounding box, ignoring narrow blocks such as the arXiv stamp."""
    area = pymupdf.Rect()
    for x0, y0, x1, y1, *_ in page.get_text("blocks"):
        if x1 - x0 > 100:
            area |= pymupdf.Rect(x0, y0, x1, y1)
    return area


def note_point(page: pymupdf.Page, anchor: pymupdf.Rect) -> pymupdf.Point:
    """A sticky note's icon in the margin beside the anchor's column, off the text."""
    area = text_area(page)
    if anchor.x0 < page.rect.width / 2:
        return pymupdf.Point(max(2, area.x0 - 22), anchor.y0)
    return pymupdf.Point(min(page.rect.width - 22, area.x1 + 4), anchor.y0)


def box_rect(page: pymupdf.Page, anchor: pymupdf.Rect) -> pymupdf.Rect:
    """A text box in the right margin when it is wide enough, else under the text."""
    area = text_area(page)
    margin = page.rect.width - area.x1
    if margin >= 80:
        left = area.x1 + 6
        return pymupdf.Rect(left, anchor.y0, page.rect.width - 6, anchor.y0 + 96)
    top = min(area.y1 + 6, page.rect.height - 60)
    return pymupdf.Rect(area.x0, top, area.x0 + 260, top + 34)


def mark(page: pymupdf.Page, kind: str, text: str, note: str | None) -> None:
    quads = find(page, text)
    if kind == "highlight":
        annot = page.add_highlight_annot(quads)
        annot.set_colors(stroke=YELLOW)
    elif kind == "underline":
        annot = page.add_underline_annot(quads)
        annot.set_colors(stroke=BLUE)
    elif kind == "note":
        annot = page.add_text_annot(note_point(page, quads[-1].rect), note)
    else:
        annot = page.add_freetext_annot(
            box_rect(page, quads[0].rect),
            note,
            fontsize=7,
            text_color=(0.15, 0.15, 0.2),
            fill_color=(1.0, 0.97, 0.88),
        )
        annot.set_border(width=1)
    annot.set_info(title=AUTHOR, content=note or "")
    annot.update()


def main() -> None:
    local = (
        Path(sys.argv[2]) if len(sys.argv) == 3 and sys.argv[1] == "--from" else None
    )
    for paper in PAPERS:
        doc = pymupdf.open(
            stream=fetch(paper["arxiv"], paper["sha256"], local), filetype="pdf"
        )
        for page_number, kind, text, note in paper["marks"]:
            mark(doc[page_number - 1], kind, text, note)
        out = ASSETS / paper["out"]
        doc.save(out, garbage=3, deflate=True)
        print(
            f"{out.relative_to(ROOT)}: {len(paper['marks'])} annotations, {out.stat().st_size} bytes"
        )
    for arxiv, sha256, name in PLAIN:
        out = ASSETS / name
        out.write_bytes(fetch(arxiv, sha256, local))
        print(f"{out.relative_to(ROOT)}: unchanged, {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
