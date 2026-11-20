**Serves:** journal TOOL-dWitnessedBar-57

# TOOL-dWitnessedBar-57 — builder return 1 (run `wf_87c41b7b-f8c`), committed 593e58112e339b2046d12463c97f5238ea712afb

## Why

TOOL-dWitnessedBar-57 is built as the spec states and committed. I checked every claim the spec makes about current code against the tree before the first edit, and all of them held: the predicates, symbols and line positions it cites, the S2 probe's 86 10 96, the S8 probe's 8, the pack probe, the pass-commit rule for AC15, AC17, AC19 and AC20, and every item it marks present at HEAD. Nothing diverged, so the spec's only edit is its status header, now CLOSED and dated 2026-11-20.

## Summary

Pass commit 8359ae2b8ec35e742dcc26a1fa59f274ea5a1041 carries `Pass: TOOL-dWitnessedBar-57`. The bug-class checklist over it selected line-claim-matched-over-the-whole-output, and that found a real defect: the `held` fixture's no-`--selection` check could pass off the previous run's output line, which also contains `--selection`. Fix commit 593e58112e339b2046d12463c97f5238ea712afb (also `Pass: TOOL-dWitnessedBar-57`) makes it read only the error lines that run printed.

What was built:
- **S1, S3, S4** (`tools/lib/refuse-wrong-shell.sh`): both readers now share one call test. A call is `$(resolve_python`, or `resolve_python` as the first word of a command, indented or after `;`, `&`, `|`, `!` or `if`/`then`/`do`/`else`. A `resolve_python()` definition is never counted as a call. `--coverage` now prints a `dropped:` line naming `tools/lib/resolve-python.sh` with its reason.
- **S5** (`tools/run-gates/measure_legs.py`): `scan_bare_bash` shape 4 now also flags `shutil.which(<variable>)` when its own expression compares that variable to "bash".
- **S7**: the `resolve_bash_py` block is now carried once, in `tools/memory-tree/tree_lib.py`. `row_grammar.py` and `corpus_ids.py` import `scan_bash` from there; the block still matches its canonical byte for byte.
- **S9, S10** (`tools/memory-tree/ratchet.py`): an armed but empty `conf-scalar-pins` beside an assigned pin now prints `empty seed conf-scalar-pins` and the re-seed steps, exit 1. Two new plants: `empty-seed` and `unarmed-home`.
- **S11** (`check_home_admitted` in `tools/lib/legacy_ledger.py`, copied into the memory-tree and gate-lint copies): a seed home must resolve, symlinks followed, inside the work tree, outside the git dir and not git-ignored. Otherwise it prints `outside the tree <path>` or `ignored <path>` and writes nothing. An absolute path that lands inside the tree is accepted.
- **S12** (`tools/codebase-map/adopt-codebase-map.test.sh`): arms 7 and 8 read the exempt file's name from the adopter's own seed call, and fail if none is found.
- **S14** (`tools/govkit/selftest.py`): new LF and CRLF arm for `inherited_red.py up`.
- **S18**: `tools/drift-audit/drift_report.py --gate-health` now requires `--selection` (exit 2 without it, fixtures included); the selection's quarantine and level rows are left out of the bar. The `held` fixture adds a quarantined leg, and `tools/drift-audit/selftest.py` now runs all five fixture cases with an empty selection file. In `tools/run-gates/verdict_flow.py`, `write_gate_health` passes the run's `selection` file, or an empty temporary file it deletes afterwards; its fixture covers both.
- **New arm cases** in `tools/lib/resolve-python.test.sh`: AC1, AC2 and AC3 in the order fixture, AC6, and AC10 in part 2o.
- **Records**: the three grown shell files were widened under `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-57-widen-2.md`, with their rows set to the measured 353, 116 and 1167. I also wrote the acceptance ledger, committed RUN.md, and committed what `gen_build_index.py --write` and `gen_map.py --write` regenerated. The extra paths were declared with `--dispatch`: widen-2, `memory/map/generated/symbols.json`, and widen-1, which ended up unused because the widen command wrote widen-2.

Checks run, each standing in for a gate it cannot replace:
- **AC1–AC3:** `refuse-wrong-shell.sh --coverage` on the tree (96 files, exit 0) and over a scratch fixture under `%TEMP%`, standing in for the python resolver leg. (DERIVED from the builder's probe)
- **AC4:** `scan_bare_bash` called directly on a fixture repo and on the gov tree (no hits), and `regen.run_command` returning 127 with `BASH` empty, for measure-legs selftest.
- **AC8, AC9:** `ratchet.py --fixture --plant empty-seed` and `--plant unarmed-home` both pass, for ratchet selftest.
- **AC10:** `legacy_ledger.py seed --home` on a scratch repo for all five cases.
- **AC12:** `inherited_red.py up` on LF and CRLF fixtures, for govkit selftest.
- **AC16:** `drift_report.py --gate-health --fixture held|differs|write --selection <empty>` all ok, and the bare form exits 2, for drift-audit selftest.
- `verdict_flow.py --fixture flakes-record` ok.
- Grep and git-log probes for AC5, AC6, AC7, AC11, AC13, AC15, AC17, AC19–AC22.
- `bash -n` and `py_compile` on the edited files, and the naming lexicon `--suggest` for every new name: all OK.
Only the naming lexicon's `--suggest` ran; no gate leg, suite or bar ran.

Owed at the close:
- Every section 7 leg.
- The RED-first observation of all six New arm lines.
- AC14: the shell-role derivation on the `push-main.sh --prepare` merge.
- AC18's second half: `govkit selfcheck` in a scratch copy with `when = "exists:"`. Its command is a gate leg's, so I did not run it.
- AC13's record-schema half (the `runlog record schema` leg).
- The `memory hygiene` leg after the `tree_lib.py` move.
- The lexicon leg's offender pin: the move removes two inline copies of `wrong_shell_at` and adds one.

Choices you may want to revisit, each recorded as a Decided trailer:
- The AC10 cases live in `resolve-python.test.sh` part 2o, next to the factory's existing fixture repo, because `legacy_ledger.py` has no self-test. The New arm line names `tools/lib/legacy_ledger.py` only as where its staged break lands.
- The drift report's own `gate_health` signal still reads no selection; only `--gate-health` requires `--selection`.
- `tools/run-gates/README.md` and `tools/drift-audit/README.md` still show the `--gate-health` command without `--selection`. Neither file is in the spec's Files touched, so I left them.

The two edits to `help/reference/drive.md` and `help/reference/units.md` in the working tree are not mine and were left unstaged.
