# TOOL-dLandedOwners-1 — acceptance ledger

**Serves:** journal TOOL-dLandedOwners-1

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, or by a `python -c` probe calling the unit's functions, from the worktree root, with the landed
revision L at `5a311c9f` (the remote-tracking `origin/main` at this pass; the spec's figures were pinned at
`51971579`, and no owner landed in between). Every red was a staged break made inside the probe's own
process, by replacing a name on the imported module, so no file was edited to observe it. The fixture
repositories were made by the case's own `tempfile.mkdtemp(prefix="pol-")` under `%TEMP%` and removed by
`remove_repo`; the real repository's refs were never written.

**Evidences:** TOOL-dLandedOwners-1
- AC1 — `derive_landed_owners('.')` printed
  `['aNimbleMend', 'aTrimmedWait', 'dDeclaredLoop', 'dFoldedAudit', 'dGroundRules', 'dOrderedCharter', 'dSafePassage']`.
  Red: at the pass's base `5c73ff5e` the same probe printed
  `['aNimbleMend', 'aTrimmedWait', 'dFoldedAudit', 'dGroundRules', 'dOrderedCharter']`.
- AC2 — `derive_landed_builds('.', [...])` over the seven builds printed
  `['dDeclaredLoop', 'dFairHearing', 'dSafePassage', 'dTrueNorth']`, and over `[]` printed `set()`.
  Red: with `derive_run_kind` replaced by a function answering `build`, it printed all seven, so
  `dPlacedRequest`, `dRankedPlan` and `dWellOiledMachine` joined.
- AC3 — `2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py --ref "$L" --default-ref "$L" --claims none`
  exited `0` in 59 s (PINNED, this pass), and `derive_landed_builds` over its `builds[].slug` list printed
  `['dDeclaredLoop', 'dFairHearing', 'dGroundRules', 'dOrderedCharter', 'dSafePassage', 'dTrueNorth']`,
  equal to the sorted `landed` list, `equal True`. Red: with `RUN_RECORD` replaced by a pattern matching
  nothing, so half 2 finds no run record, it printed
  `['dFairHearing', 'dGroundRules', 'dOrderedCharter', 'dTrueNorth']`, `False`.
- AC4 — `run_reader_carried('reader-coverage-carried')`, under `add_source_read` installed as `run_fixture`
  installs it, printed five sub-case lines: `case carried-landed: red` with
  `graded 1 · reader coverage: fixture.planted (owner bPlanted, landed at 130a0fdc) has no reader`,
  `case spec-run-landed: green`, `case run-unlanded: green` and `case base-unresolved: green` each with
  `graded 0` and the announce line, and `case kit-modules-absent: refused` naming
  `requires memory-tree, which does not resolve: <the kit copy's tool root>/memory-tree holds no gen_build_index.py`;
  it returned `(5, 0)`, and the `memory-tree` reads it recorded were exactly `backlog.py`, `design_lib.py`,
  `gen_build_index.py`, `row_grammar.py` and `tree_lib.py`. Red: with half 2 cut off as in AC3,
  `carried-landed` printed `WRONG: graded 0` and `kit-modules-absent` did not refuse, `(5, 2)`; with
  `derive_run_kind` answering `build`, `spec-run-landed` printed `WRONG: graded 1`; with the base's commit
  check bypassed, `base-unresolved` printed `WRONG` with a refusal naming `not a tree object`. The case's
  run through `check_policy.py --fixture reader-coverage-carried`, with the guard-trace and count lines,
  is the `policy fixtures` leg's and is the main loop's at the close.
- AC5 — `run_reader_coverage('reader-coverage')` returned `(11, 0)` and
  `run_reader_relocated('reader-coverage-relocated')` returned `(2, 0)`. Red: with `derive_landed_builds`
  wrapped to call `load_run_readers` first, the relocated case's present repository printed
  `WRONG: 1 finding(s) · no landed owners to grade` naming `holds no gen_build_index.py`, `(2, 1)`.
- AC6 — the timing probe printed `3.4`; a second probe counting the git calls read the owners in 2.7 s
  (PINNED, this pass) with `log` called 18 times (PINNED, this pass), once per build reaching half 2.
  Red: not observable as written. Those `log` calls took 0.7 s (PINNED, this pass) over 130 run records in
  the tree (PINNED, this pass), so a log per run record stays far under `15`; the main loop owns that red.
- AC7 — `grep -n "RUN.md" help/policy.md` found the "Landed means" bullet at lines 150 and 152, naming the
  run record and "a unit carried forward as `DEFERRED`"; `grep -n "derive_landed_builds\|reader-coverage-carried"`
  over `tools/policy/README.md` found the arms-table row, the arm paragraph and the fixture paragraph.
  Red: at the base, `grep -n "A build whose specs are still" help/policy.md` found line 149; it finds
  nothing now.
