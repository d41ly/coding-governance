# Acceptance ledger — TOOL-aHastenedSweep-5

**Serves:** journal TOOL-aHastenedSweep-5

Built against spec rev-1 in one pass commit, on node a, in the run's worktree at `8167f280e`. The
spec's claims about current code were re-read at that tip before the first edit: the shell's two
`gotchas.py` launches and its frame-failure fallback line, the `memory-tree/gotchas` contract and its
one `--for-paths` probe clause, the top-level `def`s of `cmd_check`, `cmd_check_with_ids` and `main`
in `gotchas.py`, and `measure_contract_parity` grading an `imports` clause by a static parse.

The observations below are each criterion's own command, run by hand with the change in place before
the commit. The scratch `t5-parity.py` was written to the shape §6 states. The fixtures were built
under `%TEMP%/hs5f`: `old/gotchas.py` from the build's base blob `f25308f0`, `new/gotchas.py` the
tip's copy, `nock/gotchas.py` the tip's copy with `def cmd_check(` renamed. No suite, gate leg or bar
ran in the pass.

Owed to the main loop at the close:
- AC4's `govkit selfcheck` line, refused to this role by the role hook, so it runs with the legs §7
  lists.
- AC7, the live-tree A/B: the whole hygiene run from the parent's `tools/` and from this unit's,
  `cmp`-equal with equal exit codes, recorded here under a `Pass: none` commit.
- No `New arm:` line: the spec declares none, so no red-then-green is owed for this unit.
- The spec's status flip to CLOSED. The role hook refused it to this builder because the session's
  orientation card does not route this unit, and it admits that status-only edit from the main loop.

**Evidences:** TOOL-aHastenedSweep-5
- AC1 — `1/2 clauses hold` — `t5-parity.py --consumer check-memory-hygiene.sh` over the `old`
  fixture printed it and exactly one `FAILS imports cmd_check_with_ids` line.
- AC2 — `2/2 clauses hold` — the same command over the `new` fixture printed it and no `FAILS` line;
  over the `nock` fixture it printed `1/2 clauses hold` and exactly one `FAILS imports cmd_check`
  line.
- AC3 — `3/3 clauses hold` — `t5-parity.py` over the worktree root with
  `tools/memory-tree/gotchas.py` and no filter printed it, the `--for-paths` probe clause run in
  gov's own tree.
- AC4 — `imports cmd_check_with_ids,main check-memory-hygiene.sh` — the `tomllib` read printed the
  `--for-paths` probe line, then it, then `imports cmd_check,main check-memory-hygiene.sh`; the
  `grep -c 'TOOL-aHastenedSweep-5'` over `kit.toml` printed 1. The `govkit selfcheck` line
  `contract memory-tree/gotchas (memory-tree:gotchas.py): 3 clause(s)` is NOT OBSERVED in this pass:
  owed above.
- AC5 — `git diff --name-only HEAD~1..HEAD -- tools/` — on the pass commit it prints only
  `tools/memory-tree/kit.toml`, and the `kit.toml` diff is additions only, below the `--for-paths`
  clause.
- AC6 — `grep -cF` — the fallback line's fixed-string count in the hygiene shell printed 1.
- AC7 — `cmp` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as the
  criterion's permission line assigns.

## Close observations, by the main loop

The live-tree A/B, run by the main loop: the shipped kit at `f25308f01` overlaid on `tools/memory-tree/` in a detached worktree frozen at the subject commit, against that commit's own kit, both over the same tree, stdout, stderr and exit code each compared with `cmp`. Every run shared node a with other work, so the walls are contended (PINNED, 2026-11-15 and 2026-11-16).
- AC7's observation: The whole `check-memory-hygiene.sh` run at `e30d94df9`, every unit of the build in: shipped 663.3 s, changed 239.2 s, 173 lines each, stdout, stderr and exit code identical (PINNED).
- `govkit.py selfcheck` printed `contract memory-tree/gotchas (memory-tree:gotchas.py): 3 clause(s)` and exited 0. This is AC4's line the builder's role could not run.
