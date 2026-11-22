#!/usr/bin/env python3
"""Regenerate the sample vault's images and PDF.

Everything under wiki/assets/ is drawn by this script, so there is nothing
third-party in the vault. The SVGs and the PDF need only Python 3. The PNG is
rasterized from an SVG with `rsvg-convert` when that tool is installed.

    python3 tools/make_assets.py
"""

import math
import shutil
import subprocess
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "wiki" / "assets"

INK = "#1f2933"
MUTED = "#616e7c"
WRITE = "#2f6fdb"
READ = "#e07a1f"
BOTH = "#2f9e6f"
PANEL = "#f7f9fb"
RULE = "#cbd2d9"

FONT = "font-family=\"Helvetica, Arial, sans-serif\""


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


def quorum_overlap():
    """Five replicas, a write quorum of three and a read quorum of three."""
    parts = [text(320, 36, "N = 5 replicas, W = 3, R = 3", 18, INK, "middle", "bold")]
    writes = {0, 1, 2}
    reads = {2, 3, 4}
    for i in range(5):
        cx = 80 + i * 120
        cy = 130
        in_w, in_r = i in writes, i in reads
        fill = BOTH if (in_w and in_r) else WRITE if in_w else READ if in_r else "#ffffff"
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="34" fill="{fill}" fill-opacity="0.9" '
            f'stroke="{INK}" stroke-width="1.5"/>\n'
        )
        parts.append(text(cx, cy + 6, f"R{i + 1}", 18, "#ffffff", "middle", "bold"))
    # Brackets under the replicas that belong to each quorum.
    parts.append(f'<path d="M 46 184 H 354" stroke="{WRITE}" stroke-width="4" stroke-linecap="round"/>\n')
    parts.append(text(200, 208, "write quorum (acknowledged by 3)", 13, WRITE, "middle", "bold"))
    parts.append(f'<path d="M 286 196 H 594" stroke="{READ}" stroke-width="4" stroke-linecap="round"/>\n')
    parts.append(text(440, 220, "read quorum (answered by 3)", 13, READ, "middle", "bold"))
    parts.append(text(320, 250, "R3 is in both sets, so every read sees the latest write.", 13, MUTED, "middle"))
    return svg(640, 268, "".join(parts), "Quorum overlap: five replicas with a write quorum and a read quorum sharing one replica")


def hash_ring():
    """A hash ring with four nodes and six keys."""
    cx, cy, r = 190, 190, 120
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{RULE}" stroke-width="10"/>\n',
        text(cx, cy - 4, "hash ring", 16, INK, "middle", "bold"),
        text(cx, cy + 16, "0 to 2^32", 13, MUTED, "middle"),
    ]
    nodes = [("A", 20), ("B", 105), ("C", 200), ("D", 290)]
    keys = [("k1", 50), ("k2", 80), ("k3", 140), ("k4", 175), ("k5", 235), ("k6", 330)]

    def pos(deg, radius):
        a = math.radians(deg - 90)
        return cx + radius * math.cos(a), cy + radius * math.sin(a)

    for name, deg in nodes:
        x, y = pos(deg, r)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="{WRITE}" stroke="#ffffff" stroke-width="3"/>\n')
        parts.append(text(f"{x:.1f}", f"{y + 5:.1f}", name, 15, "#ffffff", "middle", "bold"))
    for name, deg in keys:
        x, y = pos(deg, r)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{READ}" stroke="#ffffff" stroke-width="2"/>\n')
        lx, ly = pos(deg, r + 30)
        parts.append(text(f"{lx:.1f}", f"{ly + 4:.1f}", name, 11, MUTED, "middle"))
    parts.append(text(400, 90, "Each key belongs to the first node", 14, INK))
    parts.append(text(400, 110, "met going clockwise from it.", 14, INK))
    parts.append(text(400, 150, "Adding node E takes keys from", 14, MUTED))
    parts.append(text(400, 170, "one neighbour only, about K / N", 14, MUTED))
    parts.append(text(400, 190, "of all K keys.", 14, MUTED))
    parts.append(f'<circle cx="408" cy="236" r="6" fill="{WRITE}"/>\n')
    parts.append(text(422, 241, "node", 13, MUTED))
    parts.append(f'<circle cx="478" cy="236" r="6" fill="{READ}"/>\n')
    parts.append(text(492, 241, "key", 13, MUTED))
    return svg(640, 380, "".join(parts), "Consistent hashing ring with four nodes A to D and six keys")


def lag_chart():
    """Synthetic replication lag, one bar per test run (made up for the vault)."""
    runs = [("run 1", 42), ("run 2", 38), ("run 3", 61), ("run 4", 35), ("run 5", 29), ("run 6", 33)]
    left, bottom, top, step = 70, 280, 70, 80
    scale = (bottom - top) / 70
    parts = [text(320, 34, "Follower lag by test run (ms, synthetic)", 17, INK, "middle", "bold")]
    for tick in range(0, 71, 10):
        y = bottom - tick * scale
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="600" y2="{y:.1f}" stroke="{RULE}" stroke-width="1"/>\n')
        parts.append(text(left - 10, f"{y + 4:.1f}", tick, 12, MUTED, "end"))
    for i, (name, value) in enumerate(runs):
        x = left + 20 + i * step
        h = value * scale
        fill = READ if value > 50 else WRITE
        parts.append(f'<rect x="{x}" y="{bottom - h:.1f}" width="44" height="{h:.1f}" rx="3" fill="{fill}"/>\n')
        parts.append(text(x + 22, f"{bottom - h - 6:.1f}", value, 12, INK, "middle", "bold"))
        parts.append(text(x + 22, bottom + 20, name, 12, MUTED, "middle"))
    parts.append(text(320, 332, "Run 3 shows the spike described in the discoveries log.", 12, MUTED, "middle"))
    return svg(640, 350, "".join(parts), "Bar chart of follower replication lag for six test runs, run 3 is the highest")


# ---------------------------------------------------------------------------
# A small PDF writer: three A4 pages of Helvetica text and vector drawing,
# with bookmarks. Pure Python, no dependencies.
# ---------------------------------------------------------------------------

PAGE_W, PAGE_H = 595, 842


def pdf_escape(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class Page:
    def __init__(self):
        self.ops = []

    def color(self, hex_color, stroke=False):
        r, g, b = (int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5))
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} {'RG' if stroke else 'rg'}")

    def text(self, x, y, s, font="F1", size=11, fill="#1f2933"):
        self.color(fill)
        self.ops.append(f"BT /{font} {size} Tf {x} {PAGE_H - y} Td ({pdf_escape(s)}) Tj ET")

    def paragraph(self, x, y, s, width=470, font="F1", size=11, leading=15, fill="#1f2933"):
        per_line = max(20, int(width / (size * 0.50)))
        line, lines = "", []
        for word in s.split():
            if len(line) + len(word) + 1 > per_line:
                lines.append(line)
                line = word
            else:
                line = f"{line} {word}".strip()
        lines.append(line)
        for i, ln in enumerate(lines):
            self.text(x, y + i * leading, ln, font, size, fill)
        return y + len(lines) * leading

    def rect(self, x, y, w, h, fill=None, stroke=None, width=1):
        if fill:
            self.color(fill)
        if stroke:
            self.color(stroke, stroke=True)
        self.ops.append(f"{width} w {x} {PAGE_H - y - h} {w} {h} re " + ("B" if fill and stroke else "f" if fill else "S"))

    def line(self, x1, y1, x2, y2, stroke="#cbd2d9", width=1):
        self.color(stroke, stroke=True)
        self.ops.append(f"{width} w {x1} {PAGE_H - y1} m {x2} {PAGE_H - y2} l S")

    def stream(self):
        return "\n".join(self.ops).encode("latin-1")


def frame(page, n, total):
    page.line(60, 52, 535, 52)
    page.text(60, 44, "Replication and Quorums: lecture notes", "F4", 9, "#616e7c")
    page.text(472, 44, "Sample vault, CC0", "F4", 9, "#616e7c")
    page.text(278, 800, f"Page {n} of {total}", "F1", 9, "#616e7c")


def build_pdf(path):
    p1, p2, p3 = Page(), Page(), Page()

    # Page 1: title and overview.
    frame(p1, 1, 3)
    p1.text(60, 120, "Replication and Quorums", "F2", 26)
    p1.text(60, 146, "Lecture notes for the Lumiere sample vault", "F4", 13, "#616e7c")
    p1.line(60, 160, 535, 160, "#2f6fdb", 2)
    p1.text(60, 200, "Contents", "F2", 13)
    for i, entry in enumerate(["1  Overview .......................................... page 1",
                               "2  Quorums ........................................... page 2",
                               "3  Failure scenarios ................................. page 3"]):
        p1.text(72, 222 + i * 18, entry, "F3", 10)
    y = p1.paragraph(60, 310, "These notes are synthetic: they were written for the sample vault and drawn "
                     "by tools/make_assets.py. They exist so that a note can link to a page of a PDF "
                     "and embed that page, as a note about a real paper would.")
    p1.text(60, y + 24, "1  Overview", "F2", 16, "#2f6fdb")
    y = p1.paragraph(60, y + 48, "A replicated system keeps several copies of the same data so that it "
                     "survives the loss of a machine and serves reads from nearby. The price is that "
                     "the copies can disagree. Almost every design decision in this area is a way of "
                     "deciding how much disagreement to allow, for how long, and who may see it.")
    y = p1.paragraph(60, y + 12, "Three ideas carry most of the weight. A leader decides the order of "
                     "writes, so that every copy applies them in the same sequence. A quorum is a "
                     "group of copies large enough that any two groups overlap, so that news cannot "
                     "be missed by everyone. A clock, even a logical one, lets two machines agree "
                     "which of two events came first, or admit that neither did.")
    y = p1.paragraph(60, y + 12, "Page 2 turns the second idea into arithmetic. Page 3 walks through "
                     "four ways the arithmetic is tested by real failures.")

    # Page 2: quorums.
    frame(p2, 2, 3)
    p2.text(60, 100, "2  Quorums", "F2", 16, "#2f6fdb")
    y = p2.paragraph(60, 124, "Let N be the number of replicas, W the number that must acknowledge a "
                     "write, and R the number that must answer a read. The two rules to remember are:")
    p2.rect(60, y + 6, 475, 50, fill="#f7f9fb", stroke="#cbd2d9")
    p2.text(80, y + 28, "R + W > N     reads and writes overlap in at least one replica", "F3", 10)
    p2.text(80, y + 46, "W > N / 2     two writes cannot both succeed on disjoint groups", "F3", 10)
    y = p2.paragraph(60, y + 80, "With a majority quorum, W = R = floor(N / 2) + 1, so a cluster of "
                     "N = 2f + 1 replicas keeps working while f of them are down. The table shows "
                     "common choices.")
    top = y + 10
    cols = [60, 120, 180, 240, 350]
    heads = ["N", "W", "R", "Failures", "Note"]
    p2.rect(60, top, 475, 22, fill="#e4ebf2")
    for x, h in zip(cols, heads):
        p2.text(x + 8, top + 15, h, "F2", 10)
    rows = [("3", "2", "2", "1", "smallest useful cluster"),
            ("5", "3", "3", "2", "common production size"),
            ("5", "5", "1", "0 writes", "fast reads, fragile writes"),
            ("7", "4", "4", "3", "survives a rack and a node")]
    for i, row in enumerate(rows):
        ry = top + 22 + i * 22
        p2.line(60, ry + 22, 535, ry + 22)
        for x, cell in zip(cols, row):
            p2.text(x + 8, ry + 15, cell, "F1", 10)
    fy = top + 22 + len(rows) * 22 + 40
    p2.text(60, fy, "Figure 1. N = 5, W = 3, R = 3. R3 is in both quorums.", "F4", 10, "#616e7c")
    for i in range(5):
        x = 70 + i * 90
        in_w, in_r = i < 3, i > 1
        fill = "#2f9e6f" if (in_w and in_r) else "#2f6fdb" if in_w else "#e07a1f"
        p2.rect(x, fy + 14, 60, 60, fill=fill, stroke="#1f2933")
        p2.text(x + 19, fy + 50, f"R{i + 1}", "F2", 13, "#ffffff")
    p2.text(70, fy + 96, "blue: write quorum", "F1", 9, "#2f6fdb")
    p2.text(210, fy + 96, "orange: read quorum", "F1", 9, "#e07a1f")
    p2.text(350, fy + 96, "green: in both", "F1", 9, "#2f9e6f")

    # Page 3: failures.
    frame(p3, 3, 3)
    p3.text(60, 100, "3  Failure scenarios", "F2", 16, "#2f6fdb")
    y = 124
    scenarios = [
        ("A replica crashes.", "With N = 5 and W = R = 3, two replicas can be down and both reads and writes still find a quorum."),
        ("A replica is slow.", "A slow replica counts as down for latency: the request waits for the fastest W or R answers, not for all N."),
        ("The network splits 3 and 2.", "The side with three replicas can keep going. The side with two cannot reach any quorum and must refuse requests."),
        ("A write reaches only two replicas.", "It did not reach W = 3, so the client was never told it succeeded. Later reads may or may not see it, and repair must settle which."),
    ]
    for i, (head, body) in enumerate(scenarios, 1):
        p3.text(60, y, f"{i}.  {head}", "F2", 11)
        y = p3.paragraph(78, y + 17, body, width=450) + 14
    p3.rect(60, y + 6, 475, 58, fill="#fff4e5", stroke="#e07a1f")
    p3.paragraph(74, y + 28, "Summary. Quorums trade availability for agreement: the larger the quorum, "
                 "the fewer failures a request survives and the stronger the guarantee it gets.",
                 width=450, font="F4", size=10)

    # Assemble objects.
    objs = []

    def add(body):
        objs.append(body if isinstance(body, bytes) else body.encode("latin-1"))
        return len(objs)

    catalog = add("")  # 1, filled in once the outline id is known
    pages_root = add("")  # 2
    fonts = {
        "F1": add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"),
        "F2": add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"),
        "F3": add("<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>"),
        "F4": add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"),
    }
    font_res = " ".join(f"/{k} {v} 0 R" for k, v in fonts.items())
    page_ids = []
    for page in (p1, p2, p3):
        data = page.stream()
        content = add(b"<< /Length %d >>\nstream\n" % len(data) + data + b"\nendstream")
        page_ids.append(
            add(f"<< /Type /Page /Parent {pages_root} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
                f"/Resources << /Font << {font_res} >> >> /Contents {content} 0 R >>")
        )
    titles = ["1 Overview", "2 Quorums", "3 Failure scenarios"]
    outline_root = add("")
    item_ids = [add("") for _ in titles]
    for i, (item, title) in enumerate(zip(item_ids, titles)):
        prev = f"/Prev {item_ids[i - 1]} 0 R " if i else ""
        nxt = f"/Next {item_ids[i + 1]} 0 R " if i < len(titles) - 1 else ""
        objs[item - 1] = (
            f"<< /Title ({title}) /Parent {outline_root} 0 R {prev}{nxt}"
            f"/Dest [{page_ids[i]} 0 R /XYZ 0 {PAGE_H} 0] >>"
        ).encode("latin-1")
    objs[outline_root - 1] = (
        f"<< /Type /Outlines /First {item_ids[0]} 0 R /Last {item_ids[-1]} 0 R /Count {len(titles)} >>"
    ).encode("latin-1")
    info = add("<< /Title (Replication and Quorums: lecture notes) /Author (Lumiere sample vault) "
               "/Subject (Synthetic lecture notes, CC0) /Producer (tools/make_assets.py) "
               "/CreationDate (D:20261122000000Z) >>")
    kids = " ".join(f"{i} 0 R" for i in page_ids)
    objs[pages_root - 1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode("latin-1")
    objs[catalog - 1] = (
        f"<< /Type /Catalog /Pages {pages_root} 0 R /Outlines {outline_root} 0 R /PageMode /UseOutlines >>"
    ).encode("latin-1")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for i, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % i + body + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    for off in offsets:
        out += b"%010d 00000 n \n" % off
    out += (f"trailer\n<< /Size {len(objs) + 1} /Root {catalog} 0 R /Info {info} 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n").encode("latin-1")
    path.write_bytes(bytes(out))


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "quorum-overlap.svg").write_text(quorum_overlap())
    (ASSETS / "hash-ring.svg").write_text(hash_ring())
    lag_svg = ASSETS / "replication-lag.svg"
    lag_svg.write_text(lag_chart())
    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", "1280", str(lag_svg), "-o", str(ASSETS / "replication-lag.png")],
            check=True,
        )
        lag_svg.unlink()
    else:
        print("rsvg-convert not found: replication-lag.png was not regenerated")
    build_pdf(ASSETS / "Replication-and-Quorums-Lecture-Notes.pdf")


if __name__ == "__main__":
    main()
