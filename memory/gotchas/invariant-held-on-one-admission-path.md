---
name: invariant-held-on-one-admission-path
description: an invariant one admission path enforces is silently absent on every other path into the same resource, and the spec that states it reads as covering them all
kind: class
universal: false
---

# The rule held where it was written

## Symptom

A resource has several ways in. A unit adds an invariant to one of them, and its spec states the
invariant for the resource. The other paths admit as before, so the invariant fails there, and no arm
reaches them, because the arms were written against the path the unit changed.

## The instance

TOOL-aPairedSlots-5 kept one bar per worktree on the turnstile's slot claim in
`tools/run-gates/run-gates.sh`. The docs key TOOL-aPairedSlots-4 had added never asked, so a doc-only
bar ran beside its own worktree's holder (aPairedSlots closing review, M3).

## The remedy

When an invariant is added, list every admission path, the claim, the docs key, nesting and any
fail-open among them, and give the audit a column per path, so a new path shows an empty cell.

## Gating

Gated by `tools/run-gates/run-gates.turnstile.test.sh` arm 46, for the docs key only.
