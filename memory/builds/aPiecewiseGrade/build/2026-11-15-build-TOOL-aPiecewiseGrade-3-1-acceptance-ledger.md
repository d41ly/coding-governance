# TOOL-aPiecewiseGrade-3 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-3

No merge bar, no self-test suite and no gate ran in this pass. The criteria were observed by the
spec's pass probe, `pg3.sh` and `pg3.py` in the run's scratch, removed after the pass. `pg3.py`
compiles a checker's source under a given path into a fresh `cst` module, wraps `load_kit_module`
with a per-name counter and calls `main` with stdout captured. `pg3.sh` ran it over the checker at
the pass's starting commit `ce6c0af75` and over the built one, under the same path and argv, with
`SPEC_TOKENS_INPUTS` unset, the fixtures under `%TEMP%/pg3f` and `%TEMP%/pg3k`.

The first run's fixture committed `.memory-tree.conf`, so both checkers refused it as a cutoff not
strictly past its own commit day, with zero loads. The fixture was corrected to the suite's recipe,
where the conf is staged and never committed, and the fixture steps were re-run alone. The `real`
line below is from the first run: that step reads the worktree only, which the fixture fix did not
touch.

**Evidences:** TOOL-aPiecewiseGrade-3
- AC1 — `same 1` — `real rc 0/0 same 1`, `fixture rc 1/1 same 1` and `legs rc 0/0 same 1`. The
  fixture's captured output carries its `[guards]` hit, `guarded leg <- tools/x/thing.sh`.
- AC2 — `loads <n>/0` — `real ... loads 75664/0 wall 219990/43088`, `fixture ... loads 5/0` and
  `legs ... loads 1/0`. The `real` built wall is below its base wall. The base checker, which has no
  decorator, is this criterion's named red. Walls in ms, one run each on node `a`. <!-- PINNED ce6c0af75 -->
- AC3 — `nokit rc 1/1 same 1` — printed as written, then `refused 1` and
  `nokitlegs rc raised/raised same 1 loads 1/1`. Each raising call still enters `load_kit_module`,
  so nothing was cached.
- AC4 — `grep -c "@functools.lru_cache(maxsize=None)" tools/check-spec-tokens.py` — printed 1, and
  `grep -A1` shows `def load_design_lib():` on the next line.

Owed to the main loop at the close. These were written and not run:
- The new arm in `tools/check-spec-tokens.test.sh`, `memo guards hit`, covers AC2. It must be seen RED
  with the decorator removed and GREEN once the decorator is restored.
- `FLOOR_ASSERTIONS` was raised 259 -> 260 by reading. The close confirms the executed count.
- The §7 legs, among them the suite's TOOL-dTrueNorth-31 AC11 namesake arm, which this change must
  leave green.
