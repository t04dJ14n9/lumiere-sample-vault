---
title: Replication and Quorums Lecture Notes
aliases:
  - Quorums lecture notes
  - Lecture notes PDF
type: source
status: mature
created: 2026-10-22
updated: 2026-11-04
reading_time: 10
reviewed: true
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Sources-and-Reading-Map|Sources and Reading Map]]"
tags:
  - ds/replication
  - source
pdf: wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf
pages: 3
---

# Replication and Quorums Lecture Notes

**PDF:** [Open the PDF](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf) (3 pages)

A short, synthetic set of lecture notes, written for this sample vault and drawn by `tools/make_assets.py`. It stands in for a real paper so you can try Lumiere's PDF features: the links below open the reader at a page, and the embed shows one page inline.

## Key points

1. **Why replicate.** To survive a lost machine and to read from nearby, at the price of copies that can disagree. ([p. 1](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=1))
2. **The quorum rules.** $R + W > N$ and $W > N/2$, with a table of common choices and a figure of the overlap. ([p. 2](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=2)) Used in [[Quorum-Reads-and-Writes]].
3. **Four failure scenarios.** A crashed replica, a slow one, a 3 and 2 split, and a write that reached too few replicas. ([p. 3](/wiki/assets/Replication-and-Quorums-Lecture-Notes.pdf#page=3))

## Page 2, inline

The embed below draws page 2 of the PDF inside this note. Use its page buttons to turn pages, or **Open** to read it in Lumiere's PDF reader, which has an outline, zoom, search and annotation tools.

![[Replication-and-Quorums-Lecture-Notes.pdf#page=2&height=520]]

## How I used it

- The table on page 2 is where [How many replicas do I need?](/wiki/resources/notes/How-Many-Replicas-Do-I-Need.md) comes from.[^check]
- The failure scenarios became test cases for the toy store ([progress](/wiki/projects/Toy-Replicated-KV/progress.md)).

## Provenance

Written for this vault, released under CC0 with the rest of it. Page links in this note use `#page=N`, which also works in a wikilink such as [[Replication-and-Quorums-Lecture-Notes.pdf#page=3|page 3 as a wikilink]].

[^check]: I checked each row against the arithmetic in the [quorum note](/wiki/resources/notes/Quorum-Reads-and-Writes.md) rather than trusting the table.
