# TOOL-aPiecewiseGrade-1 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-1

No merge bar, no self-test suite and no gate ran in this pass. The criteria were observed by the
spec's pass probe, `pg1.sh` in the run's scratch, removed after the pass, run once over the built
checker, the checker at the pass's starting commit `85473ca9d` as the base, and the worktree's
memory-tree kit. The fixture repository was `%TEMP%/pg1`, the cache `%TEMP%/pg1c/cache`.

Three places where the probe differs from section 4's description, none of them in what a line
reports:
- The base checker runs from the fixture's own tool root, copied over the built one for its run and
  back after it. A first run kept it in a separate directory, and every step's AC1 comparison then
  differed on one line only: the size join's `no policy kit` sentence names the directories it
  looked in, which are the checker's own.
- The fixture's `.memory-tree.conf` is never committed, as in the suite's recipe, so the cutoff
  relation reads `value not yet committed` rather than refusing a key set on its own commit day.
- The forged `run` entry's key is the SHA-1 of the context digest, captured from the built
  checker's own `derive_spec_context`, and a replay that also re-runs the `run` line: the key a
  checker that replayed such lines would accept. A first run took that replay from
  `derive_input_digest` without `names`, which refuses the entry's `member` lines.

**Evidences:** TOOL-aPiecewiseGrade-1
- AC1 — `cmp` — at every one of the eleven steps the base checker's plain stdout, stderr and status
  equalled the built checker's: the probe's `AC1 base ok`. A second probe over the same fixture ran
  `--spec` on two live specs, `--pass-spec HEAD~3..HEAD` and `--list` with the base checker, the built
  one, and the built one under `SPEC_TOKENS_CACHE`: all three equal for each, statuses 1, 0 and 0.
  The comparison over this worktree with `python tools/check-spec-tokens.py` is the main loop's, at
  the close.
- AC2 — `same 1` and `moved 1` — every `step` line read `same 1`, and `closed`, `retired`,
  `carries`, `packet`, `isfile`, `cited`, `kit` and `cutoff` read `moved 1`:
  `step closed moved 1 same 1 rc 1/1 graded 0`, `step retired moved 1 same 1 rc 1/1 graded 1`,
  `step carries moved 1 same 1 rc 1/1 graded 0`, `step packet moved 1 same 1 rc 1/1 graded 0`,
  `step isfile moved 1 same 1 rc 1/1 graded 0`, `step cited moved 1 same 1 rc 1/1 graded 1`,
  `step kit moved 1 same 1 rc 1/1 graded 2`, `step cutoff moved 1 same 1 rc 1/1 graded 2`.
- AC3 — `moved 0 same 1 rc 0/0 graded 0` — printed as `step rerun moved 0 same 1 rc 0/0 graded 0`;
  the `carries`, `packet` and `isfile` lines above read `same 1` with `moved 1`, and re-graded no
  spec, so each join's moved answer came from the run and not from an entry.
- AC4 — `graded 3` and `regraded 1` — `step seed moved 1 same 1 rc 0/0 graded 3`, then
  `step onespec moved 0 same 1 rc 1/1 graded 1` and
  `regraded 1 memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md`, the edited spec.
- AC5 — `forged run miss corrupt miss` — printed as written.
- AC6 — `untouched 1 generation ok` — printed as written: after each of the eleven promotions the
  next generation was gone and the cache held one `.json` and one `.inputs` per live spec.
- AC7 — `record cold 1 warm 1` — printed as written; the warm run re-graded no spec.
- AC8 — `grep -c 'promotes <dir>.next only under its own bracket' tools/check-spec-tokens.py` —
  printed 1.

Owed to the main loop at the close. These were written and not run:
- The new arm in `tools/check-spec-tokens.test.sh`, the `PG1` assertions after the input-record
  arms, covers AC2 to AC7. It must be seen RED on each staged break the spec's `New arm:` line names,
  a key that leaves out the `read` lines, which reds `PG1 cited`, and a mode that reuses the
  previous run's packet answer, which reds `PG1 packet`, and GREEN once each is restored.
- `FLOOR_ASSERTIONS` was raised 260 -> 275 by reading, the arm's 15 `check_input_arm` calls. The
  close confirms the executed count.
- AC1 over this worktree, and the legs section 7 names, the codebase map's freshness over the
  regenerated `memory/map/generated/symbols.json` among them.
