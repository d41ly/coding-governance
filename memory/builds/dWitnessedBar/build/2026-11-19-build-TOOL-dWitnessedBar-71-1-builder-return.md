**Serves:** journal TOOL-dWitnessedBar-71

# TOOL-dWitnessedBar-71 — builder return 1 (run `wf_49ee0db5-e6b`), committed ced984440

## Why

TOOL-dWitnessedBar-71 is built as spec rev-3 states and committed in one pass commit with a `Pass: TOOL-dWitnessedBar-71` trailer, and its spec status is now CLOSED. I made one change the spec does not state, and recorded it as deviation 712. Unit 70's row for `run-gates.gov.test.sh` in `memory/project/shell-role.txt` had lost the TAB between its count 715 and its sha. While that malformed row stood, `ratchet.py widen` refused the whole file (exit 2, line 107), so the widen the spec requires could not run. I put the TAB back and changed nothing else in that row.

## Summary

The unit is committed as ced984440 on base 7378b97c7. No gate, suite or bar ran.

**What changed in `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/lib/resolve-python.test.sh`, section `2o`:**
- **S1:** a new function, `run_planted_git`, sits inside unit 67's isolated block just above the corrupt-HEAD loop. It puts `GIT_CONFIG_COUNT=2` with `init.defaultRefFormat=reftable` and `init.defaultBranch=main` in front of its one `git` call only. Unit 67's isolation is untouched. The loop's five fixtures and the `child` fixture are now built with `run_planted_git -c init.defaultBranch=master init -q --ref-format=files`. The unit-64 header now opens "Five fresh `git init`s" and says the four broken fixtures exit 1 and `chain` arms.
- **S2:** a plain `run_planted_git init -q "$LL/planted"` must read `reftable` and `refs/heads/main`. If it does not, the arm fails with `resolve-python: the hostile git config is not in effect`. In that case `ll_planted` stays 0 and no AC5 ref-format assertion runs. The comment states what the arm does not check.
- **S3:** the `child` fixture gains the same `--show-ref-format` assertion, naming `child`.

**Records:**
- Shell-role row for the resolver suite: set to the measured 1381, up from 1371, with widen record `2026-11-21-build-TOOL-dWitnessedBar-71-widen-13.md`. I used the measured count rather than widen's +1, following unit 67.
- Deviation 712: the unit-70 row repair.
- Acceptance ledger: `2026-11-19-build-TOOL-dWitnessedBar-71-1-acceptance-ledger.md`.
- Regenerated `memory/map/generated/symbols.json` (adds `run_planted_git`).
- Ran `gen_build_index --write` and committed what it rewrote: `LIVE.md`, `backlog/TOOL.md`, the build README, the spec's records table and the dClosedLoop as-built view, whose deviation count went from 2241 to 2242.
- Three paths were added to the write set with `--dispatch` before I wrote them: the widen record, deviation 712 and that as-built view.

**Checks that ran (each standing in for the resolver leg, `python resolver (behaviour + inline parity + idiom ban)`):**
- `bash -n` on the suite: passed.
- The lexicon graded `run_planted_git` OK.
- A scratch probe under `%TEMP%/p71*` ran the suite's own lines (the function, the S2 proof, the `67 AC5` assertion) with the isolation exported:
  - **AC1:** a planted init read `reftable` and `refs/heads/main`. `GIT_CONFIG_COUNT` read unset afterwards. A caller's own `GIT_CONFIG_COUNT=1` / `core.autocrlf` came back unchanged. The same config exported as `GIT_CONFIG_GLOBAL` was masked (`files`, `refs/heads/master`). The `GIT_CONFIG_COUNT=2` grep prints one line.
  - **AC2:** with the five assignments deleted, the probe printed the not-in-effect line and graded no fixture.
  - **AC3:** a fixture built with the flag read `files`. One built without `--ref-format=files` failed with "the noflag fixture read ref format 'reftable'".
  - **AC4:** checked by grep; it holds.
- The bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran and selected nothing that needed a further change.

**Owed to the main loop at the close:**
- The legs of §7: the resolver suite with GATE_SELFTESTS, `portability (shell lines only shrink)`, `recall floor`, `recall floor arms` and `memory hygiene`.
- Section `2o` run whole, including AC3's grading of the five loop fixtures and `child` in the suite itself.
- The `New arm:` RED-first observations on the real suite:
  - deleting `run_planted_git`'s five assignments should print S2's line (AC2);
  - deleting `--ref-format=files` from either real builder should fail naming the fixture and `reftable` (AC3).
- My probe stood in for those builders with a synthetic one, so the staged break on the real builders has not been seen yet.
