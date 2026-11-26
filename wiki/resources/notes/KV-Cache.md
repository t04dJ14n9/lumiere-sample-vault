---
title: KV Cache
aliases:
  - Key-value cache
type: concept
status: developing
created: 2026-11-22
updated: 2026-11-25
reading_time: 2
reviewed: false
para: resource
area: "[[wiki/areas/LLM-Study|LLM Study]]"
mocs:
  - "[[wiki/resources/mocs/Training-and-Inference-Map|Training and Inference Map]]"
tags:
  - llm/inference
---

# KV Cache

Generating text is one token at a time. Without a cache, each new token recomputes attention keys and values for the whole prefix, so a reply of $n$ tokens costs about $n^2$ work. Keeping each layer's keys and values from earlier steps makes every new step cost about the same. nanochat's `engine.py` is its inference engine with a KV cache.

## The idea in code

```typescript
type Layer = { keys: number[][]; values: number[][] };

function step(cache: Layer[], token: number[], project: (l: number, t: number[]) => [number[], number[]]) {
  cache.forEach((layer, l) => {
    const [k, v] = project(l, token); // only the new token is projected
    layer.keys.push(k);
    layer.values.push(v);
    // attention for the new token reads all of layer.keys and layer.values
  });
}
```

## What it costs

The cache trades compute for memory. Per token it stores a key and a value in every layer:

$$\text{bytes per token} = 2 \times L \times d \times \text{bytes per number}$$

For long conversations or many users at once this memory, not the weights, becomes the limit. That is why serving systems page, share or compress the cache.

> [!question] Open
> How much of nanochat's inference time is attention over the cache, and how much is the MLPs? Measure with `scripts/infer_bench.py`.

Back to the [[Transformer-Block#^attention|attention formula]].
