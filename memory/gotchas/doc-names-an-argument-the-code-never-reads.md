---
name: doc-names-an-argument-the-code-never-reads
description: a descriptor or comment names a caller argument by a spelling the code does not read, so an adopter who follows it passes a key that is silently ignored and the run falls back to the default
kind: class
universal: false
---

# A document names an argument the code never reads

## Symptom

A comment or descriptor tells the reader which argument to pass, and the code reads a different
name. Passing the documented key raises nothing, because an unknown key on an arguments object is
simply never read, so the caller's choice is dropped and the default runs in its place.

## Where it bit

The closing diff review of the dFairHearing build,
2026-11-04-review-TOOL-dFairHearing-1-40-diff-review, id 6. A comment in `tools/workflows/kit.toml`
named the leg manifest's argument legManifest, while the review harness reads gateManifest, and
nothing in the kits read the first spelling.

## The fix

Name the key the code reads, and search for the old spelling across the kits before closing, since
the harness's own argument block and its README were already right.

## Its gate

There is no machine gate: the predicate over every kit's comments found this one line, and a gate
over one instance with no second is a copy of the fix.
