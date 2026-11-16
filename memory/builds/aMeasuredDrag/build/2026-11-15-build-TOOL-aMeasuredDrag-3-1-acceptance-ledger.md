# TOOL-aMeasuredDrag-3 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-3

No merge bar and no self-test suite ran in this pass. AC1 and AC2 ran as the spec's own `python -c`
probes, from the worktree root, over the generator this commit records. AC6 and AC9 ran in a clone
at `%TEMP%/md3`, checked out at a2c11ce6, the unit's parent. The "before" captures ran the generator
of a2c11ce6. The "after" captures ran the same checkout with this commit's
`tools/memory-tree/gen_build_index.py` copied over it, so they ran the code this commit records over
the parent's records. This commit's own record edits were not in that checkout: the spec header flip
and this ledger. Each capture first ran `--write` and ended with `git reset -q --hard`. The two new
selftest arms are owed to the close, RED then GREEN.

**Evidences:** TOOL-aMeasuredDrag-3
- AC1 — `OK` — the spec's probe printed `OK` and exited 0. It ran one counting stub twice, a second
  stub once, a refusing stub twice with the memo set, and the first stub twice with the memo at None.
- AC2 — `OK` — the spec's probe printed `OK` and exited 0. The three stubbed readers each saw the
  memo set under `--check --with-verdicts`. `--check-coverage` saw it unset. `_COVERAGE_MEMO` was
  `None` after both calls of `main`.
- AC6 — `diff` — `--check --with-verdicts` printed `build-index: clean (3236 artifact(s))` and exited
  0 at both points (a2c11ce6). `--check-coverage` exited 0 at both points, grading 22 chain builds
  at or after `SPEC_CARRIES_CUTOFF` 2026-10-21 (a2c11ce6). `diff` found each pair's stdout and exit
  equal. Neither run wrote to stderr. The coverage was armed, not off.
- AC9 — `time` — the AC6 `--check --with-verdicts` run, measured 2026-11-15, one sample per point.
  Before, at a2c11ce6: real 65.0 s PINNED, beside a ten-`/usr/bin/true` baseline of 0.412 s PINNED.
  After, with this commit's generator: real 41.7 s PINNED, beside a baseline of 0.386 s PINNED. The
  after-run is shorter than the before-run. The baselines agree to within 0.03 s PINNED, so the
  machine's spawn cost did not move between the two runs.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm A1 (`TOOL-aMeasuredDrag-3 AC1`, in `test_coverage_stub`), under
  `tools/memory-tree/gen_build_index.py --selftest`. It should go RED against `read_carries_coverage`
  at base and GREEN at this commit.
- New arm A2 (`TOOL-aMeasuredDrag-3 AC2`, beside `_read_ordered31`), under the same selftest. It
  should go RED against `main()` at base and GREEN at this commit.
- The gates in spec §7: the build-index selftest, memory hygiene and the rest. They run at the bar.
