---
name: refinement-replaces-the-rule-it-refines
description: a finer rule added for part of a population is applied to the whole of it, so the coarse rule's answer is discarded for every member the finer rule never named
kind: class
universal: false
---

# A refinement replaces the rule it refines

## Symptom

A coarse rule answers for a whole population, and a finer rule is added for the members that can say more. The
finer rule is wired as the answer for every member of a record that carries it, rather than for the members it
names. The coarse answer is dropped for the rest, so a member the finer rule never looked at reads whatever the
finer rule said about its neighbours.

## Where it bit

The dTotalRecall closing review, round 3, of 2026-11-26
(`memory/builds/dTotalRecall/reviews/2026-11-26-review-TOOL-dTotalRecall-122-closing-diff-review-round3.md`,
finding 4). `tools/codebase-map/map_lib.py#measure_dossier_staleness` graded a dossier carrying `symbols` by its
anchored definitions' hashes alone, so a commit moving another path the dossier claims, one no anchor named, left
the dossier fresh. Commit ancestry, the coarse rule, was the right answer for that path and was discarded.

## The fix

- Scope the refinement to the members it names, and keep the coarse rule for every other member: there, the hashes
  grade the anchored files and every other claimed path stays on ancestry.
- Write one case for a member the refinement does not name, seen red with the refinement applied to the whole.

## Gated by

`tools/codebase-map/selftest.py`, whose `test_anchored_dossier_staleness` commits a second claimed file no anchor
names and asserts the anchored dossier reads stale.

## What this does NOT say

- It coexists-with `reseed-at-a-later-sha-launders-the-base`: there a second run of the same rule over the whole
  population resets the answer the first gave; here a different, finer rule is applied to members it never named.
