**Serves:** journal TOOL-dWitnessedBar-97

# TOOL-dWitnessedBar-97 — builder return 1 (run `wf_d8ecbc48-ca8`), committed a2675ab889b9e2d5cba5f78050636e3c27fbcce3

## Why

Unit 97 is records-only at its pass (spec-97 §4 Rollout). Every claim the spec makes about current code still holds at base, so it could be built as written. At the pass the build writes the unit's acceptance ledger with AC1 to AC10 owed to the close, and sets the spec status to CLOSED. The notes in units 88 to 92's ledgers, every fixture root and the scratch clones belong to the close.

## Summary

Unit 97 is committed and its spec is marked CLOSED. All ten acceptance criteria (AC1 to AC10) are still owed to the close. No gate, suite or bar ran.

**Commit** `a2675ab88` (base `f055359e7`), with subject naming TOOL-dWitnessedBar-97 and trailers `Pass: TOOL-dWitnessedBar-97` and `Co-Authored-By`. Files, all in the declared write set:
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-97-1-acceptance-ledger.md (new). One line per criterion, each opening with a backticked token that criterion spells.
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-97.md. The status changed from INPROGRESS to CLOSED (date already 2026-11-21), and the generator added the new ledger to its records region.
- memory/builds/dWitnessedBar/RUN.md (the dispatch row the main loop staged).
- memory/builds/dWitnessedBar/README.md, memory/backlog/TOOL.md and memory/LIVE.md, rewritten by `gen_build_index.py --write`. With unit 28 deferred, the build's derived status is now DEFERRED.

**Checks that ran** (fixture and probe level; they stand in for the AC3, AC5 and AC10 reads the close runs):
- I checked each symbol the spec cites against the tree. `pass_commit`, `next_anchor`, `read_pass_declarations`, `check_gen_region_only`, `read_attribution_tokens` and `build_commit` are all in tools/unattended/lib-unattended.sh. The call `check_gen_region_only "$1^:$2" "$1:$2"` is in check-unattended.sh. `resolve_python` is in tools/lib/resolve-python.sh. The canary's "visited" line, which returns 3, is in run-gates.gov.test.sh. Spec-92 last moved at `3ffc6c67c`. All of this matches the spec.
- I ran the spec's §4 "The derivation's identity" script under the scratch directory. It printed checksum 788872005, and the extracted derivation printed 28 and `spec/2026-10-25-spec-TOOL-dWitnessedBar-90.md`, exit 0.
- I ran §4's pass-commit read. It printed `PASS COMMIT TOOL-dWitnessedBar-89 05fdf49d3… paths 0` and `PASS COMMIT TOOL-dWitnessedBar-90 b5a33a39c… paths 0`, with no `BODY EDIT` and no `NO PASS COMMIT` line, exit 0.
- Re-recording the brief with `--brief` returned "already recorded, unchanged". The commit hook's staged memory-hygiene check passed, and the commit landed.
- `gotchas.py --for-diff HEAD~1..HEAD` exited 0 with 28 classes. I acted on the ones that apply: no token wraps across a line, no inline fence, the ledger carries `**Serves:**`, and no pipe sits in a table cell.

**Owed to the close** (only a gate, a suite or a close-time fixture can observe these):
- AC1 and AC2: the scratch-root fixtures for `NO NOTE 92 S4 resolve_python:`, run through the note check composed as S8 states.
- AC3: the five `script <c>` notes, the `NOTES OK 5` read, and a scratch copy carrying spec-90's checksum.
- AC4: the isolated third clone of 92 AC2 under %TEMP%, 92 S2's note, and its note-check read. This is a run of the suite's arm, so it is the main loop's.
- AC5: the read re-run, plus 92 S5's note in unit 90's ledger.
- AC6: 91 S2's note, the answer count for `90 2`, and its doubled-answer red copy.
- AC7 to AC9: the scratch roots for two ledgers, a delta ledger, no ledger, and the label inside an answer line. AC8 also needs the full note-table read for `NOTES OK 29`.
- AC10: the `BODY EDIT` red in a scratch clone under %TEMP%.
- Gates the spec's §7 names: `memory hygiene`, `recall floor` and `recall floor arms`.

There is no `New arm:` line, so no RED-first observation is owed for this unit. Nothing was skipped on a timeout.

The working tree still holds help/reference/drive.md and help/reference/units.md modified; they are not this unit's and were left unstaged.
