---
name: record-omits-a-figure-its-spec-names
description: a spec says a record will carry a figure, and the record is committed without it, so the figure the spec promised a reader exists nowhere in the tree
kind: class
universal: false
---

# A record omits a figure its spec names

## Symptom

A spec's design or acceptance says the record a run writes carries a figure: a variance, a count, a spread. The run
writes the record from what it measured, the figure is not among what it chose to print, and the record is
committed without it. The spec still promises the figure, and a reader who goes to the record for it finds nothing.

## Where it bit

The dTotalRecall closing review, round 3, of 2026-11-26
(`memory/builds/dTotalRecall/reviews/2026-11-26-review-TOOL-dTotalRecall-122-closing-diff-review-round3.md`,
finding 14). The second map-replay verdict record,
`memory/builds/dTotalRecall/build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-verdict.md`, was committed
without each arm's per-audit variance that its spec named, so the noise it printed could not be traced to the
spread that made it.

## The fix

- Before the record's commit, grep it for each figure its spec says it carries, and derive any that is missing from
  the output the record already quotes, never by typing it.

## Gate

Not gated, no machine gate: no reader joins a spec's promised figures to the record that should carry them. This is
a documented check, selected by `gotchas.py --for-diff` whenever a diff touches the records above.

## What this does NOT say

- It coexists-with `a-folded-field-leaves-its-row-shape-docs-behind`: there the code moves and the documents that
  describe it stay behind; here the spec is ahead and the record it describes never caught up.
