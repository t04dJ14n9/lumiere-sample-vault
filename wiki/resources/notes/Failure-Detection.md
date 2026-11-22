---
title: Failure Detection
aliases:
  - Failure detectors
  - Heartbeats
type: concept
status: developing
created: 2026-11-10
updated: 2026-11-18
reading_time: 5
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Consensus-and-Replication-Map|Consensus and Replication Map]]"
tags:
  - ds/membership
  - note
---

# Failure Detection

A node that has stopped answering is either dead or merely slow, and from outside you cannot tell which (see [[Distributed-Systems-Fundamentals#^three-failures|the three failures]]). A failure detector turns that silence into a decision, knowing it will sometimes be wrong.

## Heartbeats and timeouts

The simplest detector: every node sends a heartbeat each $T$ ms, and a node is *suspected* after $k$ missed heartbeats.

- A short timeout detects crashes fast and raises many false alarms.
- A long timeout is calm and leaves a dead node in the cluster for longer.

## Phi accrual

Rather than a yes/no after a fixed timeout, an accrual detector outputs a *suspicion level* that grows with silence. It learns the usual gap between heartbeats and asks how unlikely the current gap is:

$$\varphi(t) = -\log_{10}\,P_{\text{later}}(t - t_{\text{last}})$$

where $P_{\text{later}}$ is the probability, given past gaps, that a heartbeat still arrives after that long.[^phi] A $\varphi$ of 1 means about a 10% chance the node is merely late, a $\varphi$ of 3 about 0.1%. Each application picks its own threshold: a load balancer can react at 1, a database failover waits for 8.

## Two kinds of mistake

| | The node is up | The node is down |
| --- | --- | --- |
| Detector says up | Correct | **Missed failure**, requests time out |
| Detector says down | **False positive**, needless failover | Correct |

> [!bug] False positives are not harmless
> Declaring a slow leader dead and electing another leaves two nodes that each believe they lead. Protocols such as [Raft](/wiki/resources/notes/Raft-Leader-Election.md) stay correct by making the old leader's writes fail the majority check, not by making the detector perfect.

## Sketch

```typescript
class HeartbeatDetector {
  private last = new Map<string, number>();

  constructor(private readonly timeoutMs: number) {}

  heard(node: string, now = Date.now()): void {
    this.last.set(node, now);
  }

  suspected(node: string, now = Date.now()): boolean {
    const seen = this.last.get(node);
    return seen === undefined || now - seen > this.timeoutMs;
  }
}
```

## Related

- Heartbeat counters travel by [gossip](/wiki/resources/notes/Gossip-Protocols.md).
- An archived experiment: [Heartbeat simulator spike](/wiki/archives/Heartbeat-Simulator-Spike.md).

[^phi]: The phi accrual detector of Hayashibara et al. is the best-known version; this note describes only the idea.
