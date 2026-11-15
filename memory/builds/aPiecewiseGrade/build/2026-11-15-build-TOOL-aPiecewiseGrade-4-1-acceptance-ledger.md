# TOOL-aPiecewiseGrade-4 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-4

No merge bar, no self-test suite and no gate ran in this pass. The criteria were observed by the
spec's pass probe, `pg4.sh` in the run's scratch, removed after the pass, run once over the built
checker and the worktree's memory-tree kit, with the fixture repository at `%TEMP%/pg4`. The same
probe over the checker at the pass's starting commit `1bf06ff36` printed `dotnext 1` and an empty
named directory on its `cold`, `warm` and `step` lines, so those lines can move.

One place where the suite's arm is stronger than section 4 describes: the `PG4` third assertion
also snapshots `git status --porcelain` of the fixture, because a mode run with no named directory
writes `graded.list` into its cwd, which a snapshot of the cache and its parent cannot see.

**Evidences:** TOOL-aPiecewiseGrade-4
- AC1 — `cold graded 3 entries 3 dotnext 0 same 1` and
  `warm graded 0 entries 3 untouched 1 dotnext 0 same 1` — both printed as written.
- AC2 — `missing made 0 same 1` and `planted kept 1` — both printed as written.
- AC3 — `alone wrote 0 same 1` and `selfnamed wrote 0 same 1` — both printed as written.
- AC4 — `record cold 1 warm 1` — printed as written; the warm run re-graded no spec.
- AC5 — `regraded 1` — every `step` line began with the string its `check_grade_step` call
  expects, `step seed moved 1 same 1 rc 0/0 graded 3` through
  `step onespec moved 0 same 1 rc 1/1 graded 1`, then
  `regraded 1 memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md`, the edited spec.
- AC6 — `grep -c '\.next' tools/check-spec-tokens.py` — printed 0, and
  `grep -c 'promotes SPEC_TOKENS_CACHE_NEXT only under its own bracket' tools/check-spec-tokens.py`
  printed 1.

Owed to the main loop at the close. These were written and not run:
- New arm, the `PG4` assertions after the `PG1` arm in `tools/check-spec-tokens.test.sh`, covering
  AC1 to AC3: RED on restoring the old `rmtree` and `makedirs` of the fixed next name, which reds
  the first two, and RED on the mode run on `SPEC_TOKENS_CACHE` alone, which reds the third; GREEN
  once each is restored.
- New arm, the `PG1` arm moved onto the named directory with its steps unchanged, covering AC4 and
  AC5: RED on keeping the fixed next name in the trace's skip prefixes, which reds its record
  assertion; GREEN once restored.
- `FLOOR_ASSERTIONS` raised by reading by the `PG4` arm's three `check_input_arm` calls
  (TOOL-aPiecewiseGrade-4); the close confirms the executed count.
- The legs section 7 names.
