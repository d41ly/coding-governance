**Serves:** journal TOOL-dWitnessedBar-58

# TOOL-dWitnessedBar-58 — builder return 1 (run `wf_2590829d-f7b`), committed 75914afa1

## Why

Built TOOL-dWitnessedBar-58 as specified. Every blob pin in the spec matched HEAD and no divergence was found. Committed as one pass commit with the Pass trailer, and the spec status set to CLOSED.

## Summary

Commit 75914afa1, base d463c6241. Both new arms passed in fixture probes; no gate, suite or bar ran.
Changes:
- S1/AC1, .githooks/pre-push.test.sh: the IR AC4 c2 push now runs a stub in place of $green that writes ${GATE_BASE_FROM-unset} to ir-base-from under the fixture's git dir and exits 0. A new case passes only if the file reads `inherited`; a missing file fails it.
- S2/AC2, tools/run-gates/run-gates.evidence.test.sh: one new ok/nope pair after unit 56's AC8 run, checking that no .scoped file exists for the tree and the leg's 0.out reads `base_from_seen 0`. FLOOR_ASSERTIONS 309 to 310 with a RAISED note.
- Shell-role: both suites were already over their rows at base (unit 56's growth had no widen record), and these edits grew them further. Per unit 51 S1, ran `ratchet.py widen shell-role` and set the rows in memory/project/shell-role.txt to the measured 2290 and 2415. The record is memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-58-widen-3.md. Neither path is in the spec's Files touched; both were declared with --dispatch before writing.
- Records: acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-58-1-acceptance-ledger.md, spec status CLOSED, RUN.md, and the gen_build_index --write output.
Checks that ran:
- AC1: build_ir_fixture and write_ir_stamp copied out of the hook suite and run with the arm read from the suite file, over a fixture under %TEMP%. The scoped decision printed and the stub file read `inherited`. A FULL push with the caller setting GATE_BASE_FROM=inherited read `unset`. Stands in for the `pre-push self-test` leg.
- AC2: the evidence suite's whole unit-40 block run against the real runner in a scratch clone under %TEMP%. All 7 assertions passed, the new one included. Stands in for the `run-gates evidence` leg.
Owed at the close:
- The legs `pre-push self-test`, `run-gates evidence` and `memory hygiene`.
- Fail-first observation of both New arm lines: the hook-suite stub arm, staged red by deleting the hook's `export GATE_BASE_FROM=inherited`; the evidence-suite leg-output and no-.scoped arm, staged red by deleting the runner's `unset GATE_BASE_FROM`.
- AC3, which S3 assigns to the main loop: rewrite the AC4 line of unit 56's acceptance ledger into the OBSERVED form, naming AC1, AC2 and report id 12.
Generator side effects: gen_build_index now derives the build's status, and ask TOOL-dWitnessedBar-31's, as DEFERRED, since no unit is INPROGRESS and only unit 28 is DEFERRED. The unstaged help/reference/drive.md and help/reference/units.md changes were in the tree before this pass and were left uncommitted.
gotchas.py --for-diff HEAD~1..HEAD selected 31 classes plus 6 universal; the applicable ones (fixture finding nothing, ledger token wrapped, portability, heredoc escape) were checked and needed no change. Every command finished within its timeout.
