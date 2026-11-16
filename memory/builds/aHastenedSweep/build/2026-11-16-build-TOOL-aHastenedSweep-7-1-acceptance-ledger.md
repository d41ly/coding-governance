# Acceptance ledger — TOOL-aHastenedSweep-7

**Serves:** journal TOOL-aHastenedSweep-7

Built against spec rev-1 in one pass commit, on node a, in the run's worktree at `957322b3b`. The
spec's claims about current code were re-read at that tip before the first edit: the floor line, its
comparison and the PASS line at `tools/memory-tree/check-memory-hygiene.test.sh@78d46e3185e1:4876`,
`:4877` and `:4879`, the last RAISED entry above it, the `TOOL-aRepatriatedFork-42` "to the PRINTED
count" precedent, the presence of the three sibling-kit files the skip branches test for, and the
floor shape `tools/check-testsuite-counts.sh#compliant` accepts. All held.

The observations below are each criterion's own command, run by hand with the change in place before
the commit. No suite, gate leg or bar ran in the pass.

Owed to the main loop at the close:
- AC3: the full hygiene suite prints `PASS (742 assertions)` (PINNED, the figure the close measured
  at `0c1935569`) and no line opening `skip `.
- The `New arm:` line's red-then-green: with unit 3's block wrapped in `if false; then … fi` the
  suite prints `FAIL executed 737 assertions against a floor of 742` (PINNED, DERIVED as 742 less
  unit 3's five) and exits non-zero; restored, it prints the PASS line again.

**Evidences:** TOOL-aHastenedSweep-7
- AC1 — `FLOOR_ASSERTIONS=742` — `grep -cx` printed 1, `grep -c '^FLOOR_ASSERTIONS='` printed 1,
  and `bash -n` over the suite exited 0.
- AC2 — `RAISED 719 -> 742` — `grep -n` printed one line, the head of the comment block that sits
  directly above the floor line; the block names `TOOL-aHastenedSweep-7`, `0c1935569`, `PINNED` and
  says the floor sat below the count before this build began.
- AC3 — `PASS (742 assertions)` (PINNED) — NOT OBSERVED in this pass: the suite run and its staged
  `FAIL executed 737 assertions against a floor of 742` (PINNED) are the main loop's at the close, as the
  criterion's permission line assigns.
