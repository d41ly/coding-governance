# TOOL-aRoutedQuill-10 — spec brief

**Serves:** journal TOOL-aRoutedQuill-10

node a · 2026-10-10 · authored by the run's main loop. A unit the closing review promoted.

- **Source.** H1 in `reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md`, and the left-shift B1 names there: the landing push grades the
  routed-commits leg in RANGE mode, which never sees origin's commits, while remote CI runs it in
  WHOLE mode. A push that carries a merge of the remote's tip therefore lands a red only CI sees.
- **Mechanism, one.** When the pushed range carries a merge whose parent is the remote's tip (or any
  commit not on the pushed branch's remote side), the pre-push run of the routed-commits leg also
  grades WHOLE mode, so the landing push sees what remote CI will see. Read `.githooks/pre-push`,
  `tools/run-gates/run-gates.sh` and `routed_commits.py` to find the one seam; the spec picks it.
- **Tier.** Tier-2: it changes when a gate leg runs and what it grades.
- **Order 8.** After TOOL-aRoutedQuill-9.
