---
title: Gossip Protocols
aliases:
  - Epidemic protocols
type: concept
status: developing
created: 2026-11-09
updated: 2026-11-17
reading_time: 4
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Consensus-and-Replication-Map|Consensus and Replication Map]]"
tags:
  - ds/membership
  - note
---

# Gossip Protocols

In a gossip protocol every node periodically picks a few random peers and shares what it knows. Information spreads the way a rumour does: slowly at first, then all at once.

## Why it works

If each informed node tells one random peer per round, the number of informed nodes roughly doubles until most nodes know. The last few stragglers take a little longer, so everyone has heard after about

$$\log_2 N + \ln N + O(1)$$

rounds.^[A standard result for push gossip. The constants change if nodes pull or do both, and a real network drops some messages.] Doubling is why a thousand nodes need only fifteen to twenty rounds, and why losing a few messages hardly matters.

## What it is used for

- **Membership:** who is in the cluster, and who has not been heard from lately ([Failure detection](/wiki/resources/notes/Failure-Detection.md)).
- **Anti-entropy:** two replicas compare summaries of their data and exchange only the differences.
- **Aggregation:** sums and averages computed without a central node.

## A round, in code

```python
import random

def gossip_round(me: str, peers: list[str], state: dict[str, int], send) -> None:
    """Send our view of heartbeat counters to two random peers."""
    for peer in random.sample(peers, k=min(2, len(peers))):
        send(peer, dict(state))


def merge(mine: dict[str, int], theirs: dict[str, int]) -> dict[str, int]:
    """Keep the larger heartbeat counter for each node."""
    return {k: max(mine.get(k, 0), theirs.get(k, 0)) for k in mine.keys() | theirs.keys()}
```

> [!info] The trade-off
> Gossip has no leader and no single point of failure, but it gives only *eventual* agreement: for a few rounds two nodes may hold different views.
