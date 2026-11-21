**Serves:** journal TOOL-dWitnessedBar-108

# TOOL-dWitnessedBar-108 — builder return 1 (run `wf_d0036dda-3f9`), committed 41d4e7333

## Why

Built TOOL-dWitnessedBar-108 from its rev-1 spec in one pass commit, 41d4e7333, with the spec status set to CLOSED in that commit. The spec's code claims held against the tree before the first write. One defect, found by the bug-class checklist after the commit, is open: the new trigger-parity arm gives a false red when a hook has exported GIT_DIR. scratch-guard refused the fix because the spec is now CLOSED.

## Summary

Pass commit 41d4e7333 on base 74ae4b50d, subject naming TOOL-dWitnessedBar-108. Its trailer block ends with `Pass: TOOL-dWitnessedBar-108` and then `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. That is the charter's value, chosen over the harness reminder's Opus 5.5, as S8 requires. The live commit-msg hook admitted the commit, wrote `Commit-Checked: unattended@1.129` at the start of the trailer block, and left the charter trailer as the last line. The spec's four items fall into four disjoint write sets (§4 "Why one unit"); they were built here as one unit, as the spec says.

OPEN FINDING, not fixed: with GIT_DIR exported, `tools/run-gates/leg_factory.py#check_precommit_trigger` prints `arm FAIL` for the remove, rename and edit-inside cases (probe returned (3, 4)). The cause is that `precommit.read_staged` inherits the environment, while the arm's own git and bash calls drop it. A pre-push bar run from a linked worktree may hit this. The fix is to set the GIT_* variables aside around the `read_staged(scratch)` call. scratch-guard refused the edit after the spec went to CLOSED, so the fix needs a re-dispatch or a new unit.

What changed:
- **S1** `tools/run-gates/precommit.py#read_staged` now runs `--no-renames` with no status filter.
- **S2** `check_precommit_trigger` and its nested `read_runner_verdict` were added to `leg_factory.py --selftest`.
- **S3, S4** `tools/memory-tree/adopt-memory-tree.sh` gains `render_ledger_header`. It renders the first line of all six ledger homes and exits 2 when no header renders. The `unarmed-branches.txt` comment now states the ledger grammar and no longer mentions `ordinal`.
- **S5** `tools/memory-tree/check-memory-hygiene.test.sh` gains the scaffold witness arm.
- **S6** `run_quiet_leg` signature is now `(run, row, n, top)`.
- **S7** `tools/run-gates/py_reads.py` gains the params arm and `--list-params`, with `read_tracked_sources` pulled out as the population both arms share. The new `unread-params` ledger is registered in `tools/govkit/registry.toml`, `PROJECT_REGISTRY_EXTRA` and `.gitattributes`, and `memory/project/unread-params.txt` was seeded with 108 rows. (DERIVED from the builder's probe)
- **S8** The `attribution` verb, `read_charter_trailer` and `check_message_attribution` were added to all three `commit_trailers.py` copies; their inline blocks are still byte-identical.
- **S9** `tools/unattended/unattended.sh#check_commit_message` refuses with code 49 and writes `Commit-Checked:` with `--where start`.
- **S10** The attribution arms were added to `tools/unattended/unattended.test.sh`.
- **S11** `help/tags.md` and `tools/run-gates/README.md` describe the new behaviour.

Also in the commit:
- One widen record, `memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-108-widen-27.md`, covers four shell-role rows. Each row was then set to its measured count, as unit 51 S1 states: adopt-memory-tree.sh 638, check-memory-hygiene.test.sh 3393, unattended.sh 9792, unattended.test.sh 13935. I added `memory/project/shell-role.txt` to the write set with `--dispatch`.
- The kickoff manifest `last-audit` re-stamped at 74ae4b50d.
- The codebase map regenerated, `gen_build_index` rendered, and the acceptance ledger written.

Checks that ran, all probes standing in for gates:
- **AC1, AC2** `read_staged` and `check_precommit_trigger` run in process over a scratch repository. They gave `['a/x']` and `['a/y', 'b/y']`, four `arm ok` lines, and `arm FAIL` for remove and rename with the base argv put back. Stands in for leg-factory selftest.
- **AC3, AC4** The real `--scaffold` over a scratch tree. All six headers equal `render_header`, all six `registry_to_ledger witness` calls and the six conf-pin witnesses exit 0, and the `read_rows` row reads with nothing malformed. The refusal path of `render_ledger_header` exits 2.
- **AC5** The arm's program, cut out of the suite and run alone, exits 0 on the built tree. It printed eight `FAIL scaffold ledger` lines over the scaffolder at 277edcb9. Stands in for memory-hygiene self-test.
- **AC6** `inspect.signature` prints `(run, row, n, top)`.
- **AC7, AC8** `measure_unread_params` and `check_unread_params` run in process: 111 hits, 108 kept rows, no findings. Putting `here` back reads `undeclared site`, and a dropped key reads `unmeasured row`. The four plants answer correctly through `scan_unread_params`. The name arm also ran in process: 0 hits over 209 files. Stands in for the python reads leg and the gov canary. (DERIVED from the builder's probe)
- **AC9** The attribution CLI gives ok, refused for the 5.5 value, refused for a line after the trailer, none, and unarmed. A live `--check-commit` probe refused a 5.5 message with code 49. Stands in for the unattended suite.
- **AC12** grep over both pages.
- The naming lexicon gate (lexicon.py --check) passed.

Owed at the close:
- AC2, AC5, AC7, AC8, AC10 and AC11 as suite or leg observations.
- RED-first observations for all four `New arm:` lines: leg_factory.py at `--diff-filter=ACMR`; check-memory-hygiene.test.sh with the scaffolder at 277edcb9; py_reads.py with `here=HERE` put back; unattended.test.sh with a wrong value or a trailing line.
- The legs of §7.
- The unattended suite's FLOOR_SHARD_4 was not raised (it is a minimum, and no suite ran to count assertions).

Other bug-class items:
- No suite arm reaches these refusal branches: the exit 2 of `render_ledger_header`, the exit 2 when attribution cannot read the message, and the refusals of `check_unread_params`.

Nothing was skipped for a timeout. The pre-existing unstaged edits to help/reference/drive.md and units.md were left alone.
