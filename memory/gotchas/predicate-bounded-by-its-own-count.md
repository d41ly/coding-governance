---
name: predicate-bounded-by-its-own-count
description: a predicate about other processes' holdings that walks only up to this process's own configured count misses a neighbour configured higher
kind: class
universal: false
---

# It looked only as far as it would go itself

## Symptom

A process asks whether any holder conflicts with it, and walks the holders from 1 to its OWN count. A
neighbour configured with a larger count holds a slot beyond that range, so the predicate finds no
conflict and the process claims beside it. The same count, read from the process's own
configuration, also decided that the predicate need not run at all.

## The instance

`check_worktree_unheld` in `tools/run-gates/run-gates.sh` returned at once at one slot and otherwise
read slots 1 to the runner's own `TS_SLOTS`, so a one-slot bar claimed beside its own worktree's
slot-2 holder (aPairedSlots closing review, M2). The nesting test beside it already read every beacon
present, for the same reason.

## The remedy

A predicate about other holders reads every holder present, by a glob over what exists, never a range
this process derives from its own settings.

## Gating

Gated by `tools/run-gates/run-gates.turnstile.test.sh` arm 45, for the worktree rule only.
