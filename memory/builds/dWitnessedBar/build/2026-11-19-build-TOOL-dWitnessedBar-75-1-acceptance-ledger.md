# TOOL-dWitnessedBar-75 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-75

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (`uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`), through two scratch
probes over five copies of `.githooks/pre-push`: HEAD's hook, one without the line
`    _rg_v=${_rg_v%$'\r'}`, one whose `sha` case reads `sha) rec_sha=${_rg_v%?} ;;`, one whose
`fingerprint` case reads `fingerprint) rec_fp=${_rg_v%?} ;;`, and a file with no `read_green_file`. The
first sources `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` and the canary's lines, cut from
the suite from `rgf_mut=$(printf` to its failure statement, over a hand-built record laid out as the
AC12 arm's. The second sources the arm's own lines, cut from the suite from `check_cr_reached()` to
`rm -rf "$rgf_t"`, with `ROOT` at a scratch tree holding each copy, so the record is the one
`run_local_plant` builds, under `TMPDIR` at `%TEMP%/w75`. The suite passed `bash -n`. The shell-role
seed measures the suite at 738 past 735, widened under `2026-11-21-build-TOOL-dWitnessedBar-75-widen-16`
and the row set to that measured count. No `a=$((a+1))` was added. The §7 legs and the `New arm:`
line's RED-first observation are the main loop's at the close.

**Evidences:** TOOL-dWitnessedBar-75
- AC1 — `the planted CR never reached read_green_file on` — the criterion's `grep -n` printed one line, holding ` for $rgf_what;`; `rgf_what` is set by one `if`/`elif` chain, count then `rec_sha` then `rec_fp`.
- AC2 — `never reached read_green_file` — the arm over HEAD's hook printed no such line, `fail` 0, `a` 4. Without the strip line it printed `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621 for count 0; the CR-strip assertion is not counted`; with the `sha` variant the same prefix with ` for rec_sha;`; with the `fingerprint` variant the same prefix with ` for rec_fp;` (measure `40`); each run printed no line holding another value, and the liveness lines were `mutant changed 0 lines`, `variant changed 0 lines` and none, as the spec's Evidence table names. The no-`read_green_file` copy printed ` for count 0;`. The runs in scratch clones are OWED to the main loop at the close.
- AC3 — `for count 0` — OWED to the main loop at the close: S3's two red records, `for count 0` and `for rec_sha`, beside AC2 in `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-acceptance-ledger.md`, each with its `uname -s`.
