---
title: "Playbook: Debugging Replica Divergence"
aliases:
  - Replica divergence playbook
type: concept
status: developing
created: 2026-11-14
updated: 2026-11-20
reading_time: 5
reviewed: false
para: resource
area: "[[wiki/areas/Distributed-Systems-Study|Distributed Systems Study]]"
mocs:
  - "[[wiki/resources/mocs/Consensus-and-Replication-Map|Consensus and Replication Map]]"
tags:
  - ds/replication
  - playbook
---

# Playbook: Debugging Replica Divergence

Use this when two replicas that should hold the same data do not.

> [!todo] Before you start
>
> - [ ] Write down the key, the two replicas and the time you noticed.
> - [ ] Stop any repair job that may rewrite one side before you have looked.

## 1. Confirm it is real

Reads from a lagging follower can look like divergence. Ask each replica for its applied position first.

```bash
for host in r1 r2 r3 r4 r5; do
  printf '%s ' "$host"
  curl -s "http://$host:8080/status" | jq -c '{term, commit, applied}'
done
```

| What you see | Meaning | Next step |
| --- | --- | --- |
| Same `commit`, different `applied` | A follower is behind, not diverged | Wait, or check its disk |
| Different `term` | Two leaders have existed | Go to step 3 |
| Same position, different value | Real divergence | Go to step 2 |

## 2. Compare the logs

```bash
diff <(ssh r1 'kv-dump --from 100 --to 140') \
     <(ssh r2 'kv-dump --from 100 --to 140')
```

> [!bug] The usual cause
> An old leader accepted writes after it lost its majority, and a new leader accepted different writes at the same positions. The old leader's entries were never committed, so they are safe to discard.

## 3. Repair

1. Find the last position where all logs agree.
2. Truncate the divergent replica to that position.
3. Let the current leader resend everything after it.

> [!danger] Never repair from the replica that "looks right"
> Trust the position the cluster committed, not your reading of the values. Copying one replica over another can resurrect writes the cluster already rejected.

## 4. Afterwards

- [ ] Record the cause in [discoveries](/wiki/projects/Toy-Replicated-KV/discoveries.md).
- [ ] Add a test that reproduces the sequence.
- [ ] If a stale leader accepted writes, check the [leader election](/wiki/resources/notes/Raft-Leader-Election.md) timeout and the majority check.

Background: [Raft log replication](/wiki/resources/notes/Raft-Log-Replication.md).
