# TOOL-dPlacedRequest-60 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-60

The unit was observed from its spec at rev-6 on base `c4dbce6a3`. Built: nothing, as the spec's Files
touched estimate states; its three items were folded by the re-grounding into the AC2 and revision
log of `TOOL-dPlacedRequest-57` at rev-5, which this pass reads and does not edit. No gate, suite or
bar ran in this pass. Every reading below is the criterion's own command run over the tree, or over
a scratch copy of spec 54 made under the run's scratch directory and removed after.

**Evidences:** TOOL-dPlacedRequest-60
- AC1 — `f&&/^(- |#|$)/{exit}`: the criterion's read of 57's AC2 printed the bullet through its `fixture:` line, and `grep -cF` of the closer over that output printed 1. (DERIVED)
- AC1 — `the same way`: `grep -c` over the same output printed 0. (DERIVED)
- AC1 — `AC2`: the same output held no line opening with `#`, by `grep -c '^#'` printing 0, though the Gates heading follows the bullet after one blank line. (DERIVED)
- AC1 — `AC1`: the read 57's AC2 spells, run over 54's spec, printed the `- **AC1**` label line once and no line holding `AC2`. (DERIVED)
- AC1 — `AC2`: the red case, the unbounded `awk '/^- \*\*AC2\*\*/{f=1} f'` over 57, printed the `## 7. Gates` heading once. (DERIVED)
- AC2 — `TOOL-dPlacedRequest-57`: on the scratch copy, whose one changed line against 54 respells that name as `the run` inside AC1, the read's output under `grep -c TOOL-dPlacedRequest-57` printed 0. (DERIVED)
- AC2 — `TOOL-dPlacedRequest-57`: `awk '/^- \*\*AC1\*\*/{f=1} f'` over the same copy, under the same `grep -c`, printed 1, from the revision log; the copy's Non-goals and Edges still name it. (DERIVED)
- AC2 — `Red when:`: 57's AC2 `Red when:` names a scratch copy of 54 whose AC1 lacks `TOOL-dPlacedRequest-57` while its Non-goals and revision log still name it, read off the bullet the read printed. (DERIVED)
- AC3 — `TOOL-dPlacedRequest-60`: the criterion's `sed` cut of 57's revision log under `grep -c` printed 2, the rev-2 line and the rev-5 line folding this unit's read into AC2. (DERIVED)

## Readings beside the criteria

- The unit's commits change no file outside the build folder, so no function is minted, renamed or deleted. (DERIVED)

## Items diverged

None: each criterion was observed as written.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec declares no new arm.
