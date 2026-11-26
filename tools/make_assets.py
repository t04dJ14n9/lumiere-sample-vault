#!/usr/bin/env python3
"""Regenerate the sample vault's images and HTML page.

The SVG, the PNG and the HTML page under wiki/assets/ are drawn by this
script and are this repository's own (CC0). The SVG and the HTML page need
only Python 3. The PNG is rasterized from an SVG with `rsvg-convert` when that
tool is installed. The PDFs are real papers and come from
tools/annotate_papers.py instead.

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
    parts = [
        text(
            400,
            36,
            "From raw text to a model you can talk to",
            18,
            INK,
            "middle",
            "bold",
        )
    ]
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
    return svg(
        800,
        196,
        marker + "".join(parts),
        "nanochat training pipeline: tokenizer, pretraining, SFT, RL, eval, chat",
    )


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

    parts = [
        text(
            340,
            34,
            "Validation bits per byte by step (synthetic)",
            17,
            INK,
            "middle",
            "bold",
        )
    ]
    for tick in (0.8, 0.9, 1.0, 1.1, 1.2):
        _, y = xy(0, tick)
        parts.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="{RULE}"/>\n'
        )
        parts.append(text(left - 10, f"{y + 4:.1f}", f"{tick:.1f}", 12, MUTED, "end"))
    points = " ".join(
        f"{x:.1f},{y:.1f}" for x, y in (xy(i, v) for i, v in enumerate(values))
    )
    parts.append(
        f'<polyline points="{points}" fill="none" stroke="{BLUE}" stroke-width="3"/>\n'
    )
    sx, sy = xy(32, values[32])
    parts.append(
        f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="9" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>\n'
    )
    parts.append(
        text(sx + 14, sy - 10, "spike at step 3,200", 13, ORANGE, "start", "bold")
    )
    for i in (0, 20, 40, 60):
        x, _ = xy(i, lo)
        parts.append(text(x, bottom + 22, f"{i * 100:,}", 12, MUTED, "middle"))
    parts.append(text(340, bottom + 46, "step", 12, MUTED, "middle"))
    return svg(
        680,
        350,
        "".join(parts),
        "Line chart of validation bits per byte falling over 6,000 steps, with a spike near step 3,200",
    )


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


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "training-pipeline.svg").write_text(training_pipeline())
    (ASSETS / "bpe-merge-demo.html").write_text(BPE_DEMO)
    curve_svg = ASSETS / "loss-curve.svg"
    curve_svg.write_text(loss_curve())
    if shutil.which("rsvg-convert"):
        subprocess.run(
            [
                "rsvg-convert",
                "-w",
                "1360",
                str(curve_svg),
                "-o",
                str(ASSETS / "loss-curve.png"),
            ],
            check=True,
        )
        curve_svg.unlink()
    else:
        print("rsvg-convert not found: loss-curve.png was not regenerated")


if __name__ == "__main__":
    main()
