---
name: boundary-arm-sits-past-its-margin
description: an inequality with a margin is tested only far from its boundary, so the margin can change and its arm stays green
kind: class
universal: false
---

# The boundary arm sits past its margin

## Symptom

A rule compares against a bound with a margin: a cache entry is served while `now + wait + 1 <= deadline`,
say. Its arm stages one case on each side of the rule, but both sit FAR from the boundary: one entry
whose deadline is hours away, one whose deadline already passed. Both are decided by the deadline
alone, so the `+ 1`, the `wait`, or `<=` against `<` can each change with every arm still green. The arm
reads as a test of the margin, and is a test of the comparison's direction only.

The tell to hand a reviewer: **for each inequality with a margin, is there an arm whose operands sit
exactly on the boundary and one just inside it, and does either use a live clock?** A real clock puts
both reads in one second only by luck, so an arm on the boundary that reads the wall clock reds on load.

## Where it bit

The closing diff review of build `aLightenedLoop`, round 1, item M4
(`memory/builds/aLightenedLoop/reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md`).
The liveness cache's near-expiry arm in `tools/unattended/stop-guard.test.sh` stored a deadline five
seconds in the past, so `readLiveness` in `tools/unattended/stop-guard.js` missed whatever the margin
said, and the arm could not go red with the `wait + 1` margin removed. The review's first proposed fix
reversed the inequality in its own arithmetic, the same blindness one step later.

## The fix

An arm on each side of the boundary, with any clock pinned, each seen red against a copy with the
margin moved. `TOOL-aLightenedLoop-6` calls the exported `readLiveness` with `Date.now` pinned to one
second and a bound whose `wait` is known: a deadline one second inside the margin must spawn again, and
one exactly on it must be served. Dropping the `+ 1` reds the first; widening it reds the second.

Gated: no machine gate. The class is a property of how an arm is placed, which no leg reads; the two
arms above gate this one instance.

## What this does NOT say

It does not say every comparison needs a boundary arm. A rule with no margin, whose two sides are
decided by the comparison's direction alone, is tested by any case on each side.
