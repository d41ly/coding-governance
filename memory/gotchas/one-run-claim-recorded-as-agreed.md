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
- Probe: each `[agreement]` or `[cross]` row that names both runs carries two return citations, unless
  its crediting cell itself says "re-measured here". A phrase in another cell re-measures that cell's
  claim, not the credit.

It has no machine gate yet, because the comparison tables are prose; the probe above is the gate a
comparison script would carry. Its first version, run on 2026-10-16, matched only the spelling
"<layer> A and B", which no `[agreement]` row uses, so it read every `[agreement]` row and checked
none (the follow-up round's H1). The corrected probe counts a credit in either form, reports a row it
cannot place, and prints how many rows it matched. It was red on 36 `[agreement]` rows and one
`[cross]` row, and on a planted row of each population, and green once each row cited each run's
line (the comparison record's `[follow-up]`). The debt round's two reviews of that fold
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md`
and `-b.md`) found it still exempting a row whose "re-measured here" sat in another cell, and counting
that row as checked, so three rows passed with no citation. Its revision reads the exemption from the
crediting cell and counts exempt rows apart. It was red on those three rows, where the version before
it was green, and is green once they cite each run
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md`,
`[probes-expansions]`). Its second revision, after the folds' closing review, reads each table by the
renderer's grammar: an indented or pipe-less row had still dropped out, and the run had stayed green
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`,
`[probes-final]`).
