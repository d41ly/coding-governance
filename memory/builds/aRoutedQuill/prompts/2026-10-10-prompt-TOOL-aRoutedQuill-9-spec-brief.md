# TOOL-aRoutedQuill-9 — spec brief

**Serves:** journal TOOL-aRoutedQuill-9

node a · 2026-10-10 · authored by the run's main loop. A unit the closing review promoted.

- **Source.** Round 2's one blocker item, in `reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md`, and B1 in `reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md`. The routed-commits leg
  (`tools/memory-tree/routed_commits.py`) is red in WHOLE mode at head: the reconcile merge
  8f493d467 brought in three cutoff-day mints, d6aae9d18478, 22efab659eaf and 670436cd5f16, that
  touch ROUTED_PATHS, name no unit and are not in `ROUTED_COMMIT_WAIVED`. The B1 fix's message
  claimed exit 0 from a count taken before that merge was committed.
- **Mechanism, one.** The leg reads green in WHOLE mode at the tip that lands: the waiver set is
  complete for every cutoff-day commit any reconcile brought in, and the waiver comment says what
  each group is. The run reconciles origin/main once more before landing, so the spec says the
  waiver set is re-derived from the leg's own WHOLE-mode output at the final tip, never from a list.
- **Left-shift.** A `memory/gotchas/` class for "a history-wide leg graded before the reconcile
  commit is graded on the wrong history", with `gotchas.py --write` and its dossier claim.
- **Tier.** Tier-1 micro-spec: a conf data change plus a gotcha record, no gate semantics.
- **Order 7.** Built before TOOL-aRoutedQuill-10, -11 and -12.
