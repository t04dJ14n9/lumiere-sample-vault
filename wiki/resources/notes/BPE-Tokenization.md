---
title: BPE Tokenization
aliases:
  - Byte pair encoding
  - BPE
type: concept
status: mature
created: 2026-11-21
updated: 2026-11-24
reading_time: 3
reviewed: true
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Training-and-Inference-Map|Training and Inference Map]]"
tags:
  - llm/foundations
  - llm/training
---

# BPE Tokenization

A model reads integers, not letters. Byte pair encoding builds its vocabulary bottom up: start from single bytes, then repeatedly merge the most frequent adjacent pair into a new token. Common words end up as one token, rare ones as a few pieces. [[nanochat]]'s tokenizer is a BPE tokenizer in the style of GPT-4's.

## The whole algorithm

```python
from collections import Counter

def train_bpe(text: str, merges: int) -> list[tuple[str, str]]:
    tokens = list(text)
    learned = []
    for _ in range(merges):
        pairs = Counter(zip(tokens, tokens[1:]))
        if not pairs:
            break
        (a, b), count = pairs.most_common(1)[0]
        if count < 2:
            break
        learned.append((a, b))
        merged, i = [], 0
        while i < len(tokens):
            if i + 1 < len(tokens) and (tokens[i], tokens[i + 1]) == (a, b):
                merged.append(a + b)
                i += 2
            else:
                merged.append(tokens[i])
                i += 1
        tokens = merged
    return learned
```

Real tokenizers work on bytes rather than characters, split text into words first so merges do not cross spaces, and run in a fast language, but the loop is the same.

## Try it

A small page drawn for this vault runs the same loop in your browser: press **Merge** and watch the pairs fuse. It is a local `.html` file, so Lumiere shows it as a card that opens it.

![[bpe-merge-demo.html]]

## Why it matters

- The vocabulary size sets the size of the embedding table and the output layer.
- Fewer tokens per text means more text per unit of compute, which is why nanochat reports loss in *bits per byte*, a unit that does not depend on the vocabulary.
