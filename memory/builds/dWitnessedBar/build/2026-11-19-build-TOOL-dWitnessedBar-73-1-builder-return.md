**Serves:** journal TOOL-dWitnessedBar-73

# TOOL-dWitnessedBar-73 — builder return 1 (run `wf_224f48c2-3e7`), committed 563d828df

## Why

Unit 73 is built from spec rev-5 and committed as one pass commit, with a `Pass: TOOL-dWitnessedBar-73` trailer and the spec status set to CLOSED. The spec held at HEAD except for one path: it left the kickoff manifest re-stamp out of Files touched. `tools/gate-legs.json` is on the `watch:` line in `memory/guides/SESSION-KICKOFF.md`, so that file had to change in the same commit. As the brief directs, I declared it with `--dispatch` (admitted) together with the widen-17 record, so this is not a divergence. The orientation card said this unit was DEFERRED and not buildable, but the spec header read INPROGRESS and every write was admitted.

## Summary

What changed, by spec item:
- **S6:** the `run-gates gov canary` guard in `tools/gate-legs.json` now includes `.githooks/pre-push`.
- **S8:** the govkit comment beside `_check_exists_refused` now spells `<prefix>/memory-tree/gen_build_index.py` on the same line as `1:x`.
- **S23:** in all three `legacy_ledger.py` copies (they stay byte-identical, checked with diff), `seed --all` on a root with no HEAD and no registration now prints `seed: no HEAD: <reason>` on stderr and exits 0. The docstring says so too.
- **`tools/lib/resolve-python.test.sh`:**
  - S1 and S2: under the plant, the loop and `child` assert HEAD is `refs/heads/master`; every loop fixture except `detached` asserts a file at `.git/$ll_ref`.
  - S4 and S5: the recorder now records each call's argv beside its timeout. It runs over child, corrupt-missing and corrupt-chain, and checks the `--show-toplevel` and `ls-files -z` calls plus a 4-member union, naming any member that is missing.
  - S11: four stand-ins on the chain fixture's `symbolic-ref` and `for-each-ref` calls.
  - S23: a new `corrupt-empty` fixture for the empty case.
- **`tools/run-gates/run-gates.gov.test.sh`:**
  - S9: the hook's keys are derived from the cut's `case` labels and each gets an old-then-new record.
  - S14: a fresh `"$BASH" -c` lists `rec_` variables over a record holding only `verdict<TAB>GREEN`.
  - S10: two new sweep cases, `is_file` and `stat-denied`, and a stand-in link `gov-signers-l` placed in every case.
  - S12: the `PM_SCRUB` count uses the widened predicate with comment lines dropped.
  - S22: the `bsp_bw` line reuses post-merge's fold.
  - S15: `FLOOR_ASSERTIONS=72`, counted from the source with each loop at its population: 68 before this unit plus 4 new.
- **Records:** shell-role widened under widen-17, with the rows set to the measured 1420 and 773 (unit 75's precedent). Kickoff `last-audit` re-stamped at the base. Acceptance ledger written at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger.md`. `gen_build_index --write` output committed. `gen_map --write` changed nothing.

Checks that ran (each a probe of changed code, standing in for the suite or leg named; no gate, suite or bar ran):
- `bash -n` on both suites passed.
- The recorder's and the four S11 stand-ins' Python ran over scratch fixtures under `%TEMP%/s73f` (stands in for the resolver suite's section `2o`): all 4 members present, the two AC4 lines matched, `git not runnable:`, rc=1, no Traceback.
- S23 ran over `%TEMP%/s73e` through the `tools/lib/` copy's `main` (stdout empty, rc=0) and through `run_seed_cli` from each of the three copies (stands in for AC21's arm).
- The sweep's Python ran against `verdict_backends.py`: all 5 cases held (stands in for the gov canary).
- The S9 and S14 lines ran over HEAD's hook and three scratch hooks: green on HEAD; the scratch hooks named `rec_st`, `rec_verdict` and `rec_sha`. These are probes, not the recorded RED-first observations.
- The S12 predicate printed 1/2/2/2/2/1 and the S22 fold matched the reader's words.
- AC6 and AC8 greps; AC7 in a scratch clone at `%TEMP%/s73c` (exit 1 with the hook pathspec, 0 without).
- AC16 to AC19 greps and the gate-legs walk: 16 held and 6 run for unit 67.

Owed to the main loop at the close:
- The legs of §7, among them `install-prefix (shipped surface)` for S8 and the python resolver parity.
- Both suite runs. AC15 needs the suite's `PASS (<n> assertions)` count to equal 72 in a scratch clone at 563d828df.
- RED-first for the gov-suite `New arm:` line: a `selftests` case keeping its first value (reaches `rec_st`), a sweep testing existence (reaches `gov-signers-d` and `gov-signers-l`), a `declare` write of `PM_SCRUB`, and a `rec_verdict` read.
- RED-first for the resolver-suite `New arm:` line: deleting `-c init.defaultBranch=master` (must name `refs/heads/main`), a literal branch file, `for-each-ref` spawned outside `subprocess.run` (use `Popen`, because `check_output` goes through the patched `run`), and dropping the S23 stderr line from the `tools/lib/` copy.
- Every staged break against a `.py` file runs as S13 says: `__pycache__` cleared and `PYTHONDONTWRITEBYTECODE=1` exported.
- The ledger lines section 4 Rollout puts in other units' ledgers: AC3, AC13, AC16 and AC19 in unit 67's; AC15's net-delta 0 and AC19 in unit 66's.

The bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran and selected 43 classes. Acting on it: every new arm asserts a non-empty population; every line claim is anchored; the shell is resolved as `$BASH`; and none of the new variable names collides with an existing one in either suite. No other command was skipped for its bound.
