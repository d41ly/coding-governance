---
name: hot-path-reads-its-input-twice
description: a read on a hot path is repeated by a callee that re-reads instead of taking what the caller has, which is visible only as time
kind: class
universal: false
---

# A hot path reads its input twice

## Symptom

A caller reads a population to decide whether to go on, then calls a function that reads the same
population again from the top, because that function was written to stand alone. Both reads answer the
same thing, so every verdict and every printed byte is right. The cost shows only as time, on the path
the read was meant to make cheap, and no arm that checks a value can see it.

This differs from a second process re-deriving a decision, which answers a different question, and
from two readers of one config disagreeing. Here one answer is computed twice. The tell to hand a
reviewer: **on a path written to save time, does any callee re-read what its caller already holds?**

## Where it bit

The closing diff review of build `aLightenedLoop`, round 1, item M7
(`memory/builds/aLightenedLoop/reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md`).
`derive_carries_coverage` in `tools/check-spec-tokens.py` reads `read_carries_texts` on its building
path to see whether any chain spec is INPROGRESS, then falls through to `read_carries_specs`, which
called `read_carries_texts` again over every chain spec, on check 29's staged path, the one unit 1 built
to be cheap.

## The fix

A pre-read parameter: the callee takes the caller's answer when one is passed and reads it otherwise,
so its other callers keep their call. A counting shim around the read pins the count. A wall-clock arm
would be too noisy to fail on one extra read.

Gated by the read-count arm of `tools/check-spec-tokens.test.sh`, `AC8 reads 1`, for this instance only.

## What this does NOT say

It does not say a read may never repeat. A second read that must see a tree that may have moved, as a
stability bracket's second read does, is the point of that read, not a waste.
