# TOOL-aTrimmedWait-11 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-11

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-4, from the worktree root at base
`aa1695886`. This ledger rides the builder's commit. The spec header's move to CLOSED is the main loop's: the
scratch-guard hook refused the builder's edit of it, since this session's card routes no unit 11. The
changed code is `tools/memory-tree/check-memory-hygiene.test.sh#derive_partition_lines`, the
partition arm's compare beside it, the fixture arm after it, and `FLOOR_ASSERTIONS`. `<def>`, `L`,
`L4` and `R` are as §6 defines them, run in a Git Bash in this worktree.

The fixture probe is the suite's own fixture-arm lines, cut by line number from the edited suite
into a scratch script under `set -u`, with `HERE` the kit directory and `_PY=python`, run in three
modes: `built` (the suite's `derive_partition_lines`), `red` (the function reduced to
`printf '%s\n' "$1" | grep . | sort -u`, the pipeline at `ff4242f8b`) and `empty` (`_PY=false`, so
the render prints nothing).

**Evidences:** TOOL-aTrimmedWait-11
- AC1 — after `<def>`, `grep -c '^derive_partition_lines() { '` over the suite printed 1, and <!-- PINNED 2026-11-15 -->
  `derive_partition_lines "$L"` and `derive_partition_lines "$L4"` printed the same bytes, one line
  ending `cache hits <n>`. `derive_partition_lines "$L"$'\n'"$R"` printed the same bytes as
  `derive_partition_lines "$L"`. The `red` probe mode, the pipeline at `ff4242f8b`, printed the
  cold-equals-warm FAIL and the recompute FAIL, the red the criterion names.
- AC2 — after `<def>`, `derive_partition_lines` printed different bytes for `"$L"` and
  `"${L4/merges walked 9/merges walked 8}"`, for `"$L"` and `"$L · reader cross-check not run"`, for
  `"${L/check 26/check 12}"` and `"${L4/check 26/check 12}"`, and for
  `"$L"$'\n'"${R/check 26/check 12}"` and `"$L"`: all four pairs read `differ`.
- AC3 — `grep -c 'derive_partition_lines "$out"'` over the suite printed 2, the same grep for <!-- PINNED 2026-11-15 -->
  `derive_partition_lines "$_hs_union"` printed 2, and `grep -c '"$_hs_union" | grep . | sort -u'` printed 0. <!-- PINNED 2026-11-15 -->
- AC4 — `grep -c 'render_liveness'` over the suite printed 1 and the same count for `print_recomputed` <!-- PINNED 2026-11-15 -->
  printed 1, after the fourth assertion's FAIL text was reworded so it no longer named the latter <!-- PINNED 2026-11-15 -->
  (the first probe read 2 on it). `grep -n '_hs_c26'` printed the `mapfile`, the `_hs_cr` strip and <!-- PINNED 2026-11-15 -->
  the four assertions, all after the partition arm's compare. `grep '^FLOOR_ASSERTIONS='` printed
  `FLOOR_ASSERTIONS=749`, with its raise-log line `RAISED 745 -> 749` above it. <!-- PINNED 2026-11-15 -->
  The `built` probe mode ran the four assertions with no FAIL; `empty` printed the three FAILs of
  §4 "The fixture arm" and ran on to its last line, no `unbound variable`.
- AC5 — `git diff --stat ff4242f8b -- tools/` named one file, `tools/memory-tree/check-memory-hygiene.test.sh`, <!-- PINNED 2026-11-15 -->
  and `git diff ff4242f8b` over it removed only the partition arm's compare line, its `diff` line and `FLOOR_ASSERTIONS=745`. <!-- PINNED 2026-11-15 -->
- AC6 — owed to the main loop: the fresh `git clone --no-local` of the builder's commit and the two
  runs of `bash tools/memory-tree/check-memory-hygiene.sh --only 26` in it. That command is the
  hygiene engine, a gate, so this pass did not run it. The function's half of it, a cold and a warm
  liveness line printing the same bytes through `derive_partition_lines`, is AC1's and the fixture
  arm's first assertion, observed above.
- Verdict parity — across the three probe modes, the `built` mode reds nothing, and `red` reds only
  the two assertions the set-aside exists for. Every other arm of the suite is byte-unchanged (AC5).
  The only verdict that moves is the partition arm's on a fresh clone, which §1 and F1 (B) accept.
- Timing — the same command, the fixture probe script, interleaved `red` (before) and `built` (after):
  red 1.041 s, built 1.210 s, red 0.873 s, built 0.843 s, red 0.863 s, built 0.863 s: noise, no measurable move. <!-- PINNED 2026-11-15 -->
  The suite itself was not timed: a pass runs no suite.
- Owed to the close: both `New arm:` lines of §7, observed RED-first by the main loop on a fresh clone
  (the partition arm RED at `ff4242f8b`, the fixture arm RED with the function reduced to the
  pipeline at `ff4242f8b`), AC6, and the gate legs §7 lists.
