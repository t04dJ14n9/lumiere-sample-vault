#!/usr/bin/env python3
"""Regenerate the sample vault's images, HTML page and PDFs.

Everything under wiki/assets/ is drawn by this script, so there is nothing
third-party in the vault. The SVGs, the HTML page and the PDFs need only
Python 3. The PNG is rasterized from an SVG with `rsvg-convert` when that tool
is installed.

The PDFs carry standard PDF annotations (a highlight, an underline, a sticky
note and a text box), each with its own appearance stream, so they open
already annotated in any PDF reader.

    python3 tools/make_assets.py
"""

import shutil
import subprocess
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "wiki" / "assets"

INK = "#1f2933"
MUTED = "#616e7c"
BLUE = "#2f6fdb"
ORANGE = "#e07a1f"
GREEN = "#2f9e6f"
PANEL = "#f7f9fb"
RULE = "#cbd2d9"

FONT = 'font-family="Helvetica, Arial, sans-serif"'


# ---------------------------------------------------------------------------
# SVG
# ---------------------------------------------------------------------------


def svg(width, height, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="{title}">\n'
        f"<title>{title}</title>\n"
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="14" '
        f'fill="{PANEL}" stroke="{RULE}"/>\n{body}</svg>\n'
    )


def text(x, y, s, size=14, fill=INK, anchor="start", weight="normal"):
    return (
        f'<text x="{x}" y="{y}" {FONT} font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>\n'
    )


def training_pipeline():
    """The stages nanochat's scripts cover, left to right."""
    stages = [
        ("Tokenizer", "tok_train", BLUE),
        ("Pretraining", "base_train", BLUE),
        ("SFT", "chat_sft", GREEN),
        ("RL", "chat_rl", GREEN),
        ("Eval", "chat_eval", ORANGE),
        ("Chat", "chat_cli", ORANGE),
    ]
    parts = [text(400, 36, "From raw text to a model you can talk to", 18, INK, "middle", "bold")]
    for i, (name, script, color) in enumerate(stages):
        x = 24 + i * 128
        parts.append(
            f'<rect x="{x}" y="70" width="108" height="64" rx="10" fill="{color}" fill-opacity="0.9"/>\n'
        )
        parts.append(text(x + 54, 98, name, 15, "#ffffff", "middle", "bold"))
        parts.append(text(x + 54, 120, script, 11, "#ffffff", "middle"))
        if i < len(stages) - 1:
            parts.append(
                f'<path d="M {x + 110} 102 L {x + 126} 102" stroke="{INK}" stroke-width="2" '
                f'marker-end="url(#arrow)"/>\n'
            )
    parts.append(text(140, 168, "base model", 12, BLUE, "middle"))
    parts.append(text(396, 168, "chat model", 12, GREEN, "middle"))
    parts.append(text(652, 168, "measure and use it", 12, ORANGE, "middle"))
    marker = (
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>\n'
    )
    return svg(800, 196, marker + "".join(parts), "nanochat training pipeline: tokenizer, pretraining, SFT, RL, eval, chat")


def loss_curve():
    """A synthetic validation curve with one spike, for the playbook and the project."""
    left, right, top, bottom = 70, 610, 60, 280
    steps = 60
    values = []
    for i in range(steps + 1):
        v = 1.20 * (0.62 + 0.38 * (1 - i / steps) ** 2.2)
        if 31 <= i <= 34:
            v += [0.0, 0.16, 0.09, 0.03][i - 31]
        values.append(v)
    lo, hi = 0.70, 1.25

    def xy(i, v):
        x = left + (right - left) * i / steps
        y = bottom - (bottom - top) * (v - lo) / (hi - lo)
        return x, y

    parts = [text(340, 34, "Validation bits per byte by step (synthetic)", 17, INK, "middle", "bold")]
    for tick in (0.8, 0.9, 1.0, 1.1, 1.2):
        _, y = xy(0, tick)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="{RULE}"/>\n')
        parts.append(text(left - 10, f"{y + 4:.1f}", f"{tick:.1f}", 12, MUTED, "end"))
    points = " ".join(f"{x:.1f},{y:.1f}" for x, y in (xy(i, v) for i, v in enumerate(values)))
    parts.append(f'<polyline points="{points}" fill="none" stroke="{BLUE}" stroke-width="3"/>\n')
    sx, sy = xy(32, values[32])
    parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="9" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>\n')
    parts.append(text(sx + 14, sy - 10, "spike at step 3,200", 13, ORANGE, "start", "bold"))
    for i in (0, 20, 40, 60):
        x, _ = xy(i, lo)
        parts.append(text(x, bottom + 22, f"{i * 100:,}", 12, MUTED, "middle"))
    parts.append(text(340, bottom + 46, "step", 12, MUTED, "middle"))
    return svg(680, 350, "".join(parts), "Line chart of validation bits per byte falling over 6,000 steps, with a spike near step 3,200")


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

BPE_DEMO = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Byte pair encoding, one merge at a time</title>
<style>
  body { font: 15px/1.5 system-ui, sans-serif; margin: 24px; color: #1f2933; background: #f7f9fb; }
  textarea { width: 100%; height: 4em; font: 14px ui-monospace, monospace; }
  button { font: inherit; padding: 4px 12px; margin: 8px 8px 8px 0; }
  .tok { display: inline-block; margin: 2px; padding: 1px 5px; border-radius: 4px; background: #dbe7fb;
         font: 14px ui-monospace, monospace; white-space: pre; }
  ol { font: 13px ui-monospace, monospace; }
</style>
</head>
<body>
<h1>Byte pair encoding, one merge at a time</h1>
<p>Type some text, then press <b>Merge</b>. Each press finds the most frequent adjacent pair of
tokens and fuses it into a new token, which is all BPE training does. Written for the Lumiere sample
vault (CC0).</p>
<textarea id="input">low lower lowest newer newest wider widest</textarea>
<div><button id="merge">Merge</button><button id="reset">Reset</button>
<span id="count"></span></div>
<div id="tokens"></div>
<h2>Merges so far</h2>
<ol id="merges"></ol>
<script>
let tokens = [];
const merges = [];
function reset() {
  tokens = Array.from(document.getElementById("input").value);
  merges.length = 0;
  render();
}
function bestPair() {
  const counts = new Map();
  for (let i = 0; i + 1 < tokens.length; i++) {
    const key = tokens[i] + "\\u0000" + tokens[i + 1];
    counts.set(key, (counts.get(key) || 0) + 1);
  }
  let best = null, n = 1;
  for (const [key, c] of counts) if (c > n) { best = key; n = c; }
  return best && { pair: best.split("\\u0000"), n };
}
function merge() {
  const found = bestPair();
  if (!found) return;
  const [a, b] = found.pair;
  const out = [];
  for (let i = 0; i < tokens.length; i++) {
    if (i + 1 < tokens.length && tokens[i] === a && tokens[i + 1] === b) { out.push(a + b); i++; }
    else out.push(tokens[i]);
  }
  tokens = out;
  merges.push(`"${a}" + "${b}" -> "${a + b}" (seen ${found.n} times)`);
  render();
}
function render() {
  const box = document.getElementById("tokens");
  box.replaceChildren(...tokens.map(t => {
    const s = document.createElement("span");
    s.className = "tok";
    s.textContent = t === " " ? "\\u2423" : t;
    return s;
  }));
  document.getElementById("merges").replaceChildren(...merges.map(m => {
    const li = document.createElement("li");
    li.textContent = m;
    return li;
  }));
  document.getElementById("count").textContent = `${tokens.length} tokens`;
}
document.getElementById("merge").onclick = merge;
document.getElementById("reset").onclick = reset;
reset();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# A small PDF writer: A4 pages of Helvetica text and vector drawing, with
# bookmarks and annotations. Pure Python, no dependencies.
# ---------------------------------------------------------------------------

PAGE_W, PAGE_H = 595, 842
AUTHOR = "Lumiere sample vault"
STAMP = "D:20261126000000Z"


def pdf_escape(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def rgb(hex_color):
    return tuple(int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5))


def text_width(s, size):
    """A close-enough Helvetica width, for wrapping and placing highlights."""
    narrow = set("iljtfrI.,:;'!|() ")
    wide = set("mwMW@%")
    units = sum(0.28 if c in narrow else 0.85 if c in wide else 0.56 for c in s)
    return units * size


class Page:
    def __init__(self):
        self.ops = []
        self.annots = []

    def color(self, hex_color, stroke=False):
        r, g, b = rgb(hex_color)
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} {'RG' if stroke else 'rg'}")

    def text(self, x, y, s, font="F1", size=11, fill=INK):
        self.color(fill)
        self.ops.append(f"BT /{font} {size} Tf {x} {PAGE_H - y} Td ({pdf_escape(s)}) Tj ET")
        return (x, y, text_width(s, size), size)

    def paragraph(self, x, y, s, width=470, font="F1", size=11, leading=15, fill=INK):
        """Draw wrapped text; return the next y and the box of each line."""
        line, lines = "", []
        for word in s.split():
            candidate = f"{line} {word}".strip()
            if text_width(candidate, size) > width and line:
                lines.append(line)
                line = word
            else:
                line = candidate
        lines.append(line)
        boxes = [self.text(x, y + i * leading, ln, font, size, fill) for i, ln in enumerate(lines)]
        return y + len(lines) * leading, boxes

    def rect(self, x, y, w, h, fill=None, stroke=None, width=1):
        if fill:
            self.color(fill)
        if stroke:
            self.color(stroke, stroke=True)
        paint = "B" if fill and stroke else "f" if fill else "S"
        self.ops.append(f"{width} w {x} {PAGE_H - y - h} {w} {h} re {paint}")

    def line(self, x1, y1, x2, y2, stroke=RULE, width=1):
        self.color(stroke, stroke=True)
        self.ops.append(f"{width} w {x1} {PAGE_H - y1} m {x2} {PAGE_H - y2} l S")

    # Annotations. Text boxes are (x, top-based baseline y, width, size).

    def highlight(self, box, note):
        self.annots.append(("Highlight", box, note))

    def underline(self, box, note):
        self.annots.append(("Underline", box, note))

    def sticky(self, x, y, note):
        self.annots.append(("Text", (x, y, 18, 18), note))

    def textbox(self, x, y, w, h, note):
        self.annots.append(("FreeText", (x, y, w, h), note))

    def stream(self):
        return "\n".join(self.ops).encode("latin-1")


def text_quad(box):
    """PDF rectangle (bottom-left based) covering a line of text."""
    x, y, w, size = box
    base = PAGE_H - y
    return x - 1, base - size * 0.28, x + w + 1, base + size * 0.92


class PdfWriter:
    def __init__(self):
        self.objs = []

    def add(self, body):
        self.objs.append(body if isinstance(body, bytes) else body.encode("latin-1"))
        return len(self.objs)

    def set(self, ref, body):
        self.objs[ref - 1] = body.encode("latin-1")

    def stream(self, header, data):
        head = f"<< {header} /Length {len(data)} >>\nstream\n".encode("latin-1")
        return self.add(head + data + b"\nendstream")

    def form(self, bbox, ops, resources=""):
        x1, y1, x2, y2 = bbox
        return self.stream(
            f"/Type /XObject /Subtype /Form /BBox [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}] /Resources << {resources} >>",
            ops.encode("latin-1"),
        )

    def bytes(self, catalog, info):
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for i, body in enumerate(self.objs, 1):
            offsets.append(len(out))
            out += b"%d 0 obj\n" % i + body + b"\nendobj\n"
        xref = len(out)
        out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(self.objs) + 1)
        for off in offsets:
            out += b"%010d 00000 n \n" % off
        out += (
            f"trailer\n<< /Size {len(self.objs) + 1} /Root {catalog} 0 R /Info {info} 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n"
        ).encode("latin-1")
        return bytes(out)


def wrap(note, width, size):
    lines, line = [], ""
    for word in note.split():
        candidate = f"{line} {word}".strip()
        if text_width(candidate, size) > width and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    return lines


def markup(pdf, kind, box, common):
    """A highlight or underline over one line of text."""
    x1, y1, x2, y2 = text_quad(box)
    quad = f"{x1:.2f} {y2:.2f} {x2:.2f} {y2:.2f} {x1:.2f} {y1:.2f} {x2:.2f} {y1:.2f}"
    if kind == "Highlight":
        color = "1 0.86 0.25"
        ops = f"/GS gs {color} rg {x1:.2f} {y1:.2f} {x2 - x1:.2f} {y2 - y1:.2f} re f"
        res = "/ExtGState << /GS << /Type /ExtGState /BM /Multiply /ca 0.55 >> >>"
    else:
        color = "0.18 0.44 0.86"
        ops = f"{color} RG 1.2 w {x1:.2f} {y1 + 1:.2f} m {x2:.2f} {y1 + 1:.2f} l S"
        res = ""
    ap = pdf.form((x1, y1, x2, y2), ops, res)
    return pdf.add(
        f"<< {common} /Rect [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}] /QuadPoints [{quad}] "
        f"/C [{color}] /AP << /N {ap} 0 R >> >>"
    )


def annotation(pdf, kind, box, note, font_ref):
    """One annotation object with its normal appearance stream."""
    common = (
        f"/Type /Annot /Subtype /{kind} /F 4 /T ({AUTHOR}) /M ({STAMP}) "
        f"/NM (sample-{len(pdf.objs) + 1}) /Contents ({pdf_escape(note)})"
    )
    if kind in ("Highlight", "Underline"):
        return markup(pdf, kind, box, common)
    x, y, w, h = box
    x1, y1, x2, y2 = x, PAGE_H - y - h, x + w, PAGE_H - y
    rect = f"/Rect [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}]"
    if kind == "Text":
        ops = (
            f"1 0.86 0.25 rg 0.55 0.42 0.05 RG 1 w {x1 + 0.5:.2f} {y1 + 0.5:.2f} {w - 1} {h - 1} re B "
            f"{x1 + 4:.2f} {y1 + 12:.2f} m {x2 - 4:.2f} {y1 + 12:.2f} l "
            f"{x1 + 4:.2f} {y1 + 8:.2f} m {x2 - 4:.2f} {y1 + 8:.2f} l "
            f"{x1 + 4:.2f} {y1 + 4:.2f} m {x2 - 7:.2f} {y1 + 4:.2f} l S"
        )
        ap = pdf.form((x1, y1, x2, y2), ops)
        return pdf.add(f"<< {common} {rect} /Name /Comment /Open false /C [1 0.86 0.25] /AP << /N {ap} 0 R >> >>")
    body = " ".join(
        f"BT /Helv 9 Tf {x1 + 6:.2f} {y2 - 14 - i * 11:.2f} Td ({pdf_escape(ln)}) Tj ET"
        for i, ln in enumerate(wrap(note, w - 12, 9))
    )
    ops = (
        f"1 0.97 0.88 rg 0.88 0.48 0.12 RG 1 w {x1 + 0.5:.2f} {y1 + 0.5:.2f} {w - 1} {h - 1} re B "
        f"0.12 0.16 0.2 rg {body}"
    )
    ap = pdf.form((x1, y1, x2, y2), ops, f"/Font << /Helv {font_ref} 0 R >>")
    return pdf.add(
        f"<< {common} {rect} /DA (0.12 0.16 0.2 rg /Helv 9 Tf) /C [0.88 0.48 0.12] /AP << /N {ap} 0 R >> >>"
    )


def write_pdf(path, pages, titles, title, subject):
    pdf = PdfWriter()
    catalog = pdf.add("")
    pages_root = pdf.add("")
    fonts = {
        "F1": pdf.add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"),
        "F2": pdf.add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"),
        "F3": pdf.add("<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>"),
        "F4": pdf.add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"),
    }
    font_res = " ".join(f"/{k} {v} 0 R" for k, v in fonts.items())
    page_ids = []
    for page in pages:
        content = pdf.stream("", page.stream())
        annots = [annotation(pdf, kind, box, note, fonts["F1"]) for kind, box, note in page.annots]
        annot_list = f"/Annots [{' '.join(f'{a} 0 R' for a in annots)}] " if annots else ""
        page_ids.append(
            pdf.add(
                f"<< /Type /Page /Parent {pages_root} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
                f"/Resources << /Font << {font_res} >> >> /Contents {content} 0 R {annot_list}>>"
            )
        )
    outline_root = pdf.add("")
    items = [pdf.add("") for _ in titles]
    for i, (item, entry) in enumerate(zip(items, titles)):
        prev = f"/Prev {items[i - 1]} 0 R " if i else ""
        nxt = f"/Next {items[i + 1]} 0 R " if i < len(titles) - 1 else ""
        pdf.set(
            item,
            f"<< /Title ({entry}) /Parent {outline_root} 0 R {prev}{nxt}/Dest [{page_ids[i]} 0 R /XYZ 0 {PAGE_H} 0] >>",
        )
    pdf.set(outline_root, f"<< /Type /Outlines /First {items[0]} 0 R /Last {items[-1]} 0 R /Count {len(titles)} >>")
    info = pdf.add(
        f"<< /Title ({pdf_escape(title)}) /Author ({AUTHOR}) /Subject ({pdf_escape(subject)}) "
        f"/Producer (tools/make_assets.py) /CreationDate ({STAMP}) >>"
    )
    kids = " ".join(f"{i} 0 R" for i in page_ids)
    pdf.set(pages_root, f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>")
    pdf.set(
        catalog,
        f"<< /Type /Catalog /Pages {pages_root} 0 R /Outlines {outline_root} 0 R /PageMode /UseOutlines >>",
    )
    path.write_bytes(pdf.bytes(catalog, info))


def frame(page, n, total, title):
    page.line(60, 52, 535, 52)
    page.text(60, 44, title, "F4", 9, MUTED)
    page.text(472, 44, "Sample vault, CC0", "F4", 9, MUTED)
    page.text(278, 800, f"Page {n} of {total}", "F1", 9, MUTED)


def table(page, top, cols, heads, rows):
    page.rect(60, top, 475, 22, fill="#e4ebf2")
    for x, h in zip(cols, heads):
        page.text(x + 8, top + 15, h, "F2", 10)
    for i, row in enumerate(rows):
        ry = top + 22 + i * 22
        page.line(60, ry + 22, 535, ry + 22)
        for x, cell in zip(cols, row):
            page.text(x + 8, ry + 15, cell, "F1", 10)
    return top + 22 + len(rows) * 22


def notes_page_one(p, title):
    frame(p, 1, 3, title)
    p.text(60, 120, "nanochat Study Notes", "F2", 26)
    p.text(60, 146, "Reading notes on a small, complete LLM training harness", "F4", 13, MUTED)
    p.line(60, 160, 535, 160, BLUE, 2)
    p.text(60, 200, "Contents", "F2", 13)
    for i, entry in enumerate(["1  The pipeline ....................................... page 1",
                               "2  What it costs ...................................... page 2",
                               "3  After pretraining .................................. page 3"]):
        p.text(72, 222 + i * 18, entry, "F3", 10)
    y, _ = p.paragraph(60, 310, "These notes are synthetic: written for the sample vault and drawn by "
                       "tools/make_assets.py. They summarize, in our own words, what the nanochat README "
                       "describes. Read the repository itself for the details.", font="F4", size=10, fill=MUTED)
    p.text(60, y + 24, "1  The pipeline", "F2", 16, BLUE)
    y, boxes = p.paragraph(60, y + 48, "nanochat covers every stage of building a chat model in one small "
                           "codebase: training a tokenizer, pretraining a base model, finetuning it into a "
                           "chat model, evaluating it, and talking to it from a command line.")
    p.highlight(boxes[0], "The point of the repo: one codebase, every stage, small enough to read.")
    y, boxes = p.paragraph(60, y + 12, "One number sets the size of the model: the depth, the number of "
                           "transformer layers. Width, heads, learning rates and the training horizon are "
                           "derived from it so that each size comes out compute optimal.")
    p.underline(boxes[0], "A single dial: --depth.")
    p.sticky(540, y - 30, "Compare with the scaling-laws cheat sheet: compute optimal means tokens grow with parameters.")
    stages = ["tokenizer", "pretrain", "SFT", "RL", "eval", "chat"]
    for i, stage in enumerate(stages):
        x = 60 + i * 80
        p.rect(x, y + 30, 70, 36, fill=BLUE if i < 2 else GREEN if i < 4 else ORANGE)
        p.text(x + 8, y + 53, stage, "F2", 11, "#ffffff")
    p.text(60, y + 90, "Figure 1. The six stages, as the repository's scripts are named.", "F4", 10, MUTED)


def notes_page_two(p, title):
    frame(p, 2, 3, title)
    p.text(60, 100, "2  What it costs", "F2", 16, BLUE)
    y, boxes = p.paragraph(60, 124, "Training compute is usually estimated as C = 6 N D floating-point "
                           "operations, for N parameters and D training tokens. Cost then follows from GPU "
                           "hours and an hourly price.")
    p.highlight(boxes[0], "The 6ND rule of thumb; see the scaling-laws cheat sheet.")
    end = table(p, y + 16, [60, 250, 400], ["Quantity", "Value", "Note"], [
        ("Node", "8 x H100", "one machine"),
        ("Price assumed", "about $3 per GPU-hour", "so about $24 an hour"),
        ("Time to GPT-2", "about 2 hours", "so about $48"),
        ("GPT-2 in 2019", "about $43,000", "for comparison"),
    ])
    y, boxes = p.paragraph(60, end + 30, "The README reports these figures for its GPT-2 grade run, measured "
                           "by the DCLM CORE score. Spot instances bring the total down further.")
    p.underline(boxes[0], "All four numbers come from the README; nothing here was measured by us.")
    p.textbox(330, end + 90, 205, 62, "Margin note: the leaderboard keeps lowering the time. Check the README "
              "for the current row before quoting a number.")


def notes_page_three(p, title):
    frame(p, 3, 3, title)
    p.text(60, 100, "3  After pretraining", "F2", 16, BLUE)
    y, boxes = p.paragraph(60, 124, "A base model only continues text. Supervised finetuning (SFT) on "
                           "conversations teaches it the shape of a chat: whose turn it is, and when to stop.")
    p.highlight(boxes[-1], "SFT teaches format more than knowledge.")
    y, boxes = p.paragraph(60, y + 12, "Reinforcement learning then rewards answers that a program can check, "
                           "such as a final number in a math word problem. The model samples several answers, "
                           "and the better ones are made more likely.")
    p.underline(boxes[0], "Verifiable rewards: the checker is code, not a person.")
    p.sticky(540, y - 24, "The README lists an RL script (chat_rl.py) and a GSM8K task; see the reasoning note in the vault.")
    p.rect(60, y + 16, 475, 58, fill="#fff4e5", stroke=ORANGE)
    p.paragraph(74, y + 38, "Summary. Pretraining buys knowledge, SFT buys manners, and RL on checkable "
                "tasks buys reliability on those tasks.", width=450, font="F4", size=10)


def study_notes(path):
    title = "nanochat study notes"
    pages = [Page(), Page(), Page()]
    notes_page_one(pages[0], title)
    notes_page_two(pages[1], title)
    notes_page_three(pages[2], title)
    write_pdf(path, pages, ["1 The pipeline", "2 What it costs", "3 After pretraining"],
              "nanochat study notes", "Synthetic reading notes, CC0")


def cheat_sheet(path):
    p = Page()
    frame(p, 1, 1, "Scaling laws cheat sheet")
    p.text(60, 112, "Scaling Laws Cheat Sheet", "F2", 24)
    p.line(60, 126, 535, 126, BLUE, 2)
    y, boxes = p.paragraph(60, 160, "Training compute: C = 6 N D, for N parameters and D tokens. Two of the "
                           "six come from the forward pass and four from the backward pass.")
    p.highlight(boxes[0], "Memorize this one.")
    y, boxes = p.paragraph(60, y + 12, "Compute-optimal training, as the Chinchilla paper found, grows "
                           "parameters and tokens together; a common rule of thumb is about 20 tokens per "
                           "parameter.")
    p.underline(boxes[-1], "A rule of thumb, not a law; it shifts with data and architecture.")
    end = table(p, y + 20, [60, 220, 380], ["Parameters N", "Tokens D (20 N)", "Compute 6 N D"], [
        ("100 M", "2 B", "1.2e18 FLOPs"),
        ("500 M", "10 B", "3.0e19 FLOPs"),
        ("1 B", "20 B", "1.2e20 FLOPs"),
        ("7 B", "140 B", "5.9e21 FLOPs"),
    ])
    p.text(60, end + 22, "Rows are arithmetic from the two rules above, not measurements.", "F4", 10, MUTED)
    p.sticky(540, end - 40, "Check: 6 x 1e9 x 20e9 = 1.2e20. The table is just the formula.")
    p.textbox(60, end + 50, 300, 50, "Inference costs about 2 N FLOPs per generated token, which is why a small "
              "model that is good enough is worth so much.")
    write_pdf(path, [p], ["Scaling laws cheat sheet"], "Scaling laws cheat sheet", "Synthetic reference card, CC0")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "training-pipeline.svg").write_text(training_pipeline())
    (ASSETS / "bpe-merge-demo.html").write_text(BPE_DEMO)
    curve_svg = ASSETS / "loss-curve.svg"
    curve_svg.write_text(loss_curve())
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "1360", str(curve_svg), "-o", str(ASSETS / "loss-curve.png")], check=True)
        curve_svg.unlink()
    else:
        print("rsvg-convert not found: loss-curve.png was not regenerated")
    study_notes(ASSETS / "nanochat-Study-Notes.pdf")
    cheat_sheet(ASSETS / "Scaling-Laws-Cheat-Sheet.pdf")


if __name__ == "__main__":
    main()
