---
name: remote-write-without-an-unreachable-outcome
description: a compare-and-swap push to a shared ref names its outcomes for won, lost and refused but none for a remote it cannot reach, so the builder either blocks every write or mints locally and collides on reconnection
kind: class
universal: false
---

# A remote write has no unreachable-remote outcome

## Symptom

A design mints ids or claims names by a compare-and-swap push to the remote. It gives the push a closed outcome set:
claimed, claimed by another key, lease refused. Nothing says what happens when the remote cannot be reached. So the
builder picks one of two. It blocks every record write, against a warn-only offline policy. Or it mints a local id,
which collides with another clone's once both reconnect.

## Where it bit

dClosedLoop's whole-design audit, 2026-10-18
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, M13). `entry.claim` and
the ask family's counter ref had an outcome for every reachable case, and the offline rule covered leases only.

## The fix

- Every remote compare-and-swap write names its unreachable-remote outcome in its closed set, tied to the offline
  policy.
- It never mints a local id. It queues the request keyed by content and mints on reconnection, or it refuses.
- Probe it with the remote made unreachable.

## Gate

No machine gate holds this class: it lives in the design of a remote write. The documented check is the
fix's probe, the write run with the remote made unreachable.
