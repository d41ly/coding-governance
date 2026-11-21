**Serves:** journal TOOL-dWitnessedBar-108

# TOOL-dWitnessedBar-108 — builder return 2 (run `wf_8a2f101f-175`), committed d609c6a21f5692bd074986a582018656067d2672

## Why

Pass 2 fixes the one defect pass 1 left open. When GIT_DIR is exported, as git does for a pre-push hook in a linked worktree, `tools/run-gates/leg_factory.py#check_precommit_trigger` printed `arm FAIL` for the remove, rename and edit-inside cases. The cause: `precommit.read_staged` uses the caller's environment, but the arm's own git and bash calls drop the GIT_* variables. The fix and the spec's CLOSED status are in commit d609c6a21.

## Summary

Built TOOL-dWitnessedBar-108 pass 2 in commit d609c6a21f5692bd074986a582018656067d2672 (base 732e605d5).

Change: in `tools/run-gates/leg_factory.py#check_precommit_trigger`, every GIT_* variable is now removed from `os.environ` just before the `precommit.read_staged(scratch)` call and put back in a try/finally right after it. `read_staged` itself is unchanged: the real pre-commit hook still uses the caller's environment, which it needs for GIT_INDEX_FILE. No function was added, renamed or removed, so the codebase map was not regenerated. The commit has a `Decided:` trailer explaining why I did not add an env parameter to `read_staged`.

Same commit:
- Spec status header changed from INPROGRESS to CLOSED; the date was already 2026-11-21 and nothing else in the spec changed.
- The AC2 line of `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-108-1-acceptance-ledger.md` gained the pass-2 observations.
- Staged rows in `memory/builds/dWitnessedBar/RUN.md`.
- The three files `gen_build_index.py --write` rewrote: `memory/builds/dWitnessedBar/README.md`, `memory/backlog/TOOL.md`, `memory/LIVE.md`. The build-status line in the README now reads DEFERRED; the generator derives that from unit 28 still being deferred.

Every path is in the declared write set, so no extra `--dispatch` was needed. The `--brief` record already existed and was unchanged. Trailers: `Pass: TOOL-dWitnessedBar-108` and the charter's own trailer, `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, as the last line. AGENTS.md is Level 0 and outranks the harness reminder's "Opus 5.5". The commit hook passed and wrote `Commit-Checked:` at the start of the trailer block, so the charter trailer stays last.

Checks that ran (each is a probe of `check_precommit_trigger`, standing in for the `leg-factory selftest` leg, i.e. `leg_factory.py --selftest`), using scratch repos under %TEMP%/t108a-d, since removed:
- Before the fix, with GIT_DIR and GIT_WORK_TREE exported to this worktree: 3 `arm FAIL` lines, (3, 4). This reproduces the defect.
- After the fix, same exports: 4 `arm ok` lines, (0, 4), and both variables were back in the environment afterwards.
- After the fix, nothing exported: 4 `arm ok` lines, (0, 4).
- After the fix, GIT_DIR exported and `read_staged` swapped in-process for the old `--diff-filter=ACMR` argv: the remove and rename cases still print `arm FAIL`, (2, 4). The arm still goes red when it should.

Bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`): 29 classes selected, none needs action. The red case was seen; the swap used the real old argv, not a made-up value; the ledger's AC2 token stays on one line.

Owed to the close (the main loop runs these; nothing was skipped or timed out here):
- `python tools/run-gates/leg_factory.py --selftest` in full, the `leg-factory selftest` leg, ideally once with GIT_DIR exported.
- The RED-first observation of every `New arm:` line in spec section 7: leg_factory (AC2), check-memory-hygiene.test.sh (AC5), py_reads.py (AC7, AC8), unattended.test.sh (AC10, AC11).
- The legs of §7 and the bar.
