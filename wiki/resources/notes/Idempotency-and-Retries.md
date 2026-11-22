---
title: Idempotency and Retries
aliases:
  - Safe retries
type: concept
status: developing
created: 2026-11-12
updated: 2026-11-19
reading_time: 5
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Distributed-Systems-Map|Distributed Systems Map]]"
tags:
  - ds/foundations
  - note
---

# Idempotency and Retries

Because a lost reply looks like a lost request ([[Distributed-Systems-Fundamentals#^three-failures]]), a client that gets no answer has only two choices: give up or try again. Trying again is safe only if the operation is **idempotent**: doing it twice has the same effect as doing it once.

## Which operations are idempotent

| Operation | Idempotent? | Why |
| --- | :---: | --- |
| `SET balance = 100` | Yes | Same final state |
| `balance += 10` | No | Each retry adds again |
| `DELETE /orders/7` | Yes | Already gone is still gone |
| `POST /orders` | No | Creates a new order each time |

## Making a write idempotent

Send an **idempotency key** with the request. The server stores the result under that key and returns the stored result for any repeat.

```typescript
const results = new Map<string, Response>();

async function handle(key: string, run: () => Promise<Response>): Promise<Response> {
  const seen = results.get(key);
  if (seen) return seen; // a retry: return the first answer

  const response = await run();
  results.set(key, response);
  return response;
}
```

In a real service the key and the result must be written in the same transaction as the effect, or a crash between them leaves a half-done retry.

## Retrying politely

Retrying at once, from every client, turns a short outage into a long one. Back off exponentially and add jitter so clients spread out:

$$\text{delay}_n = U(0,\ 1) \cdot \min\bigl(\text{cap},\ \text{base} \cdot 2^{\,n}\bigr)$$

```typescript
function backoff(attempt: number, baseMs = 100, capMs = 10_000): number {
  const ceiling = Math.min(capMs, baseMs * 2 ** attempt);
  return Math.random() * ceiling; // "full jitter"
}
```

> [!caution] Retry storms
> Every layer that retries multiplies the load: three layers with three attempts each turn one request into twenty-seven. Retry at one layer, and cap the total time, not only the count.

## Related

- A toy-store decision: [D-004](/wiki/projects/Toy-Replicated-KV/decisions.md#d-004-client-supplied-request-ids)
