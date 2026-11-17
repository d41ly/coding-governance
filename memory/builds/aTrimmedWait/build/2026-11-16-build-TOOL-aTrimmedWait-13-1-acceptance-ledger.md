# TOOL-aTrimmedWait-13 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-13

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-1, from the worktree root at base
`a55bf78b1`. The probes are the spec's §4 scripts, saved in the run's scratch directory as `t13.sh`
and `t13-parity.sh`; each reads the suite as data. `t13-parity.sh` differs from §4's text in one
line: its fixture repository sits at the run's short temp path rather than a bare `mktemp -d`, as
the run's scratch rule requires. The changed file is `tools/unattended/unattended.test.sh`, at the
`PARITY_ROWS` table, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_1`.

**Evidences:** TOOL-aTrimmedWait-13
- AC1 — after the edit `bash "$SCRATCH/t13.sh"` printed `rowless c50583f10 --check-specs rows 41`,
  `rowless tree none rows 42` and `row 1`. <!-- DERIVED from t13.sh's count of the table's | lines -->
  Before the edit the same run printed `rowless tree --check-specs rows 41` and `row 0`, the red. <!-- DERIVED from t13.sh's count of the table's | lines -->
- AC2 — `bash "$SCRATCH/t13-parity.sh"` printed `parity rc proc=1 inproc=1 output same tree clean`
  and `missing 1`, before the edit and after it alike: the row's argv is the driver's, which the
  pass does not change.
- AC3 — after the edit `bash "$SCRATCH/t13.sh"` printed `loop same 3` and `floors 2 raised 2`;
  before it, `loop same 3` and `floors 0 raised 0`. <!-- DERIVED from t13.sh's count of the loop's same lines -->
  `FLOOR_ASSERTIONS` reads 3377 and `FLOOR_SHARD_1` reads 737, each its base value plus that count. <!-- DERIVED from the floors at a55bf78b1 plus loop same -->
- AC4 — `bash "$SCRATCH/t13.sh"` printed `syntax ok` after the edit, and `git diff --stat` before
  the commit named `tools/unattended/unattended.test.sh` alone, with nine diff lines. <!-- PINNED 2026-11-16 -->
  `git show --name-only --format= HEAD -- tools/ ':!tools/unattended/unattended.test.sh'` over the
  pass commit is the close's to read; this ledger rides that commit.
- AC5 — `python tools/check-spec-tokens.py --spec` over this unit's spec exited 0, and
  `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-13` printed
  `TOOL-aTrimmedWait-13: none carries a refusal --dispatch makes from its spec files` and exited 0.
- Verdict parity — the parity probe printed the same refusal, `missing 1` and the same exit 1 on both
  sides before and after the edit; the only verdict that moved is the row the spec adds, read by
  `t13.sh` as `rowless tree none`.
- Timing — the same command, `bash "$SCRATCH/t13.sh"`, took 2.433 s before and 2.844 s after. <!-- PINNED 2026-11-16 -->
  `bash "$SCRATCH/t13-parity.sh"` took 3.540 s before and 4.882 s after. <!-- PINNED 2026-11-16 -->
- Owed to the close — the driver suite on a frozen clone, whose `parity: check-specs` rows and the
  verb loop's missing FAIL line are the `New arm:` line's GREEN against the run at `c50583f10` as
  its RED, and both floors' executed counts; the merge bar.
