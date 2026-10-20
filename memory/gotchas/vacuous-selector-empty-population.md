---
name: vacuous-selector-empty-population
description: a path selector that matches nothing prints nothing, and nothing is what a passing check prints
kind: class
universal: false
---

# A selector that matches nothing looks exactly like a check that found nothing

## Symptom

A gate is green. It has always been green. It is green because its path selector matches zero files,
so its finding list is empty, so the emptiness test is false and it prints nothing — which is
precisely what a check prints when it passes.

## Where it bit

`tools/memory-tree/check-memory-hygiene.sh` at the 1.5 flatten. Six selectors changed segment count
in one commit: checks 4, 5, 8, 12, the index set and check 10. Any one left at the old count would
have disarmed its check permanently, with no symptom.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Four set-valued keys
accepted the empty set, `transitions.record`, `card.store`, `tests.landing-levels` and `platforms.supported`, so an
ordinary key could switch off a floor invariant or a verdict level. Every set-valued key now says whether it may be
empty, and the schema refuses an empty value where it may not.

## The fix, and the trap inside the fix

Every selector over a population a real tree has asserts that population is NON-EMPTY. The first
draft of that guard redded a freshly scaffolded repo, because a repo with no builds legitimately has
an empty build population — measured by running `tools/memory-tree/adopt-memory-tree.sh --scaffold`
into a scratch repo, not by reading the code.

So the guard compares TWO granularities: a PRECONDITION asking whether a file of that KIND exists
anywhere under the memory root, and the POPULATION at the exact path the check expects.
Equal-and-zero is a young tree; precondition non-zero with an empty population is a mis-segmented
selector, and only that reds.

Gated by `tools/memory-tree/check-memory-hygiene.sh` (its empty-population report), with both states
armed in `tools/memory-tree/check-memory-hygiene.test.sh`.
