---
name: append-without-an-idempotence-key
description: a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green
kind: class
universal: false
---

# The retry writes it twice

## Symptom

A command appends rows to a shared record that only grows, such as a decision log, a backlog shard or a
ledger. A run that dies after the append and is relaunched appends again. The witness compares sets,
so a second copy of a row still matches. The record is append-only, so the duplicate can only be
superseded, never removed.

## Where it bit

The library round, 2026-10-16. `deploy.distill`, which appended major decisions to `memory/DECISIONS.md`,
declared neither idempotence nor reconciliation, against the `[rules]` of the step definitions
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`). The round's review
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`, M5) caught it. The
fold moved the append to `build.distill`, idempotent and keyed by build and fork.

It bit again in the night pass two's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`).
The opposite edge: keys that were declared but coarser than the events. Two answers from one item derived one message
id, and a create-only problem ref per path kept the first problem filed against a file and refused the rest.

## The fix

- Declare the key that makes a row unique, and skip a row whose key is already present.
- Make the witness a one-to-one join on that key, so a second row for one key is red.
- Probe it: a fixture log with one row duplicated must turn the witness red.

The row writers under `tools/memory-tree/` are its population. It has no machine gate yet: its gate is
the witness itself, which the chain build that implements the command builds.
