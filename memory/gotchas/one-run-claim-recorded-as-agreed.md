---
name: one-run-claim-recorded-as-agreed
description: a comparison of two independent runs records a claim only one run made as what both found, so a single measurement carries the weight of agreement
kind: class
universal: false
---

# One run's claim, recorded as both runs'

## Symptom

Two independent research runs answer one question, and what they agree on is the design's ground. A
claim only one run made, such as a count, a date or a placement, is written into the "both" column or
cited as "A and B". The other run often said something near it, so the row reads naturally, and a
reader takes a single measurement for an agreed one.

## Where it bit

The expansion round, 2026-10-16, in `[agreement]` and `[cross]` of
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`:
- "every run since 2026-10-13 14:03 is red" was integrations B's claim, credited to both runs and
  carried into gap-test-12's evidence, while run A had counted 22 of the last 40 push runs (review A's
  M17, review B's M16);
- integrations A alone measured that `verdict`, `run.host` and `maintain.host` were typed as literal
  lists (review B's L8);
- `peer-node` moved into integrations on integrations B's placement alone, against v2's chain (review
  A's M5, review B's H5).

The returns are
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-integrations-a.md` and
its run B sibling.

## The fix

- Every "both runs" cell cites a line in each return, or says "re-measured here" with the measurement.
- A claim one run made is credited to that run, with the other run's figure beside it.
- A component moved between layers on one run's word is marked single-run, and the move reaches v2's
  chain in the same commit, or is not made.
- Probe: each `[agreement]` or `[cross]` row that names both runs carries two return citations.

It has no machine gate yet, because the comparison tables are prose; the probe above is the gate a
comparison script would carry. Its probe was run by hand on 2026-10-16 over the expansion round's
`[agreement]` and `[cross]`. It was red on four `[cross]` rows that credited both runs with no return
citation, and green once each row cited each run's line (the comparison record's `[closing-review]`).
