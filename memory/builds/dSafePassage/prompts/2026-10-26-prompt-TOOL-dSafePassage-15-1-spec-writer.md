**Serves:** research TOOL-dSafePassage-15

# Brief: TOOL-dSafePassage-15's AC4 compares the converged receipt without `carry`

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-15 back as a DIVERGENCE (`wf_6763024f-40d`), and the run revises the spec under M2.

## The brief

### Goal

AC4 observes the convergence S1 to S4 can deliver — a killed `update --write` over a schema-3 receipt re-runs to the uninterrupted run's receipt in every field but `carry` — and states why `carry` is out, so the unit is buildable as designed.

**The defect.** AC4 (and its Red-when) says the re-run after a kill during the schema step's up "exits 0 with the same receipt bytes". Below schema 4, move 3 persists nothing (S1), and `_cmd_update` writes no receipt between its write loop and the walk (`tools/govkit/govkit.py` from :9289 to the walk call at :11459). So after the kill the receipt on disk is the pre-run one while the files are already at B; the re-run's write loop finds `tools/demo/one.txt` current and drops that row's `carry`, which DEPL-dCarriedReceipt-9 S2 makes output-only, recomputed every run and popped when the run carried nothing (`govkit.py` ~:10164-10172). The builder measured both runs exit 0, both receipts at schema 4 with steps `govkit/receipt-schema-4`, `fx/s1`, `fx/s2` all applied, and the bytes differing only in that row's `carry`.

**The direction.** Option (a): AC4 compares the re-run's receipt with the uninterrupted run's after removing `carry` from every `files` row, requires them equal, and requires `carry` to be the ONLY key that differs (so a dropped step row or a different `gov_commit` still reds it). One sentence states why `carry` is excluded, citing DEPL-dCarriedReceipt-9 S2. Do not make `one.txt` identical at A and B to dodge it, and do not change `update`'s receipt writes: that is outside S1 to S5 and Files touched.

### Items

1. **Revise TOOL-dSafePassage-15** as a rev bump dated 2026-10-26, still `DEFERRED`: AC4 and its Red-when as above; any other criterion or §5/§7 text that claims byte-identical convergence of a schema-3 `update` re-run says the same. One §9 line names this brief.
2. **Cross-read** TOOL-dSafePassage-2 (its `kill-walk` plant converges byte-identical because its move 3 persists the receipt; confirm nothing there claims the schema-3 case) and TOOL-dSafePassage-5 (the upgrade-walk leg's byte-identical claims) on M2's axes; fix a disagreement only in the one document that is wrong, with a rev bump and §9 line.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- AC4 names `carry`, the exclusion, the only-difference requirement, and DEPL-dCarriedReceipt-9.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them.
- `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-15 READY.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no change to `update`'s receipt writes or to `carry`'s semantics.
- No commit, no stage into the real index, no deviation record.

### Reuse

The builder's work-in-progress patch, kept for the rebuild: `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-dSafePassage-15-wip.patch`; read it for the plant names your text may cite.
