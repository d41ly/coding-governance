# TOOL-aMeasuredDrag-8 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-8

No merge bar and no self-test suite ran in this pass. The pass started at 20e4294f. AC1 ran as the
spec's own block, saved as `md8-ac1.sh` in the session scratchpad, with `bash -s` from the worktree
root in Git Bash. AC2 and AC3 ran in the worktree after the edit and AC2 again on the commit.

**Evidences:** TOOL-aMeasuredDrag-8
- AC1 — `mismatches=0` — against `2026-09-06` the block printed `dates=213 skipped_old=103
  skipped_new=103 mismatches=0`, PINNED at 20e4294f. Against `2026-09-01` it printed
  `dates=213 skipped_old=84 skipped_new=84 mismatches=0`, PINNED at 20e4294f. No `MISMATCH` line printed in either run, the README opened
  on the cutoff included.
  - before (the `sort -C` pipeline, 213 compares): 81894 ms for `2026-09-06` and 70638 ms
    for `2026-09-01`, PINNED at 20e4294f.
  - after (the bash `[[ < ]]` compare, 213 compares): 32 ms for `2026-09-06` and 328 ms
    for `2026-09-01`, PINNED at 20e4294f.
  - spawn baseline: 2891 ms and 2354 ms per ten `/usr/bin/true`, PINNED at 20e4294f. The
    spec's figure is 0.55 s to 0.62 s, PINNED at 6d98c39ca, so this machine was under load when
    sampled, as TOOL-aMeasuredDrag-7's ledger also found.
  - The edited line itself, `sed -n 368p` of `check-brief-recorded.sh` evaluated with the cutoff
    `2026-09-06`, skips `2026-09-05` and `2025-12-31` and grades `2026-09-06` and `2026-09-07`.
- AC2 — `3	3` — `git diff --numstat HEAD~1 HEAD` over the two scripts prints `3	3` for each file,
  and `grep -c "sort -C"` prints `0` for each.
- AC3 — `bash -n` — both scripts exit 0 under `bash -n`. The `BRIEF_RECORDED_CUTOFF` grep prints
  line 368 of `check-brief-recorded.sh` and the `PASS_ORDER_CUTOFF` grep prints line 330 of
  `check-pass-order.sh`.

**Owed to the close (the main loop, after every unit is terminal):**
- No new arm. Spec §6 adds none, so no RED-first observation is owed.
- The gates in spec §6: `brief-recorded` and `pass-order history`. Each leg's `build(s) skipped by
  the <cutoff> cutoff` count should match AC1's `skipped_new` for the same HEAD. The held suites
  `unattended brief-recorded selftest` and `unattended pass-order selftest` re-observe the cutoff in
  both directions.
