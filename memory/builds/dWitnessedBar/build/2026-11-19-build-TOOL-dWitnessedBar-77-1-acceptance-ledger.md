# TOOL-dWitnessedBar-77 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-77

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21, `uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`, under `set -u`, through
one scratch probe that sources the suite's own lines, `tools/run-gates/run-gates.gov.test.sh#check_cr_reached`
through `check_canary_keys`, and evals the arm from its `rgf_mut` line through the loop over `rgf_whats`, each
over a `rgf_fn` cut of `.githooks/pre-push#read_green_file` and a hand-built record laid out as the AC12 arm's:
two `sha` lines the second CR-ended, a CR-ended `fingerprint`. The record `run_local_plant` builds is the main
loop's at the close. The suite passed `bash -n`. The shell-role row measures the suite at 787 past 784, widened
under `2026-11-21-build-TOOL-dWitnessedBar-77-widen-19`. No `a=$((a+1))` was added, so the floor stays as
`TOOL-dWitnessedBar-73` S15 states it (DERIVED from the builder's probe).

**Evidences:** TOOL-dWitnessedBar-77
- AC1 — `never reached read_green_file` — over the cut as the hook has it the slice printed no line, `fail` 0,
  `rgf_ok` 1. Over the cut whose `sha` and `fingerprint` cases both read `${_rg_v%?}` it printed
  `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621 for rec_sha; the CR-strip assertion is not counted`
  then the same line `for rec_fp;`, and no `for count` line; the suite as `1f34660b7` has it printed the
  `for rec_sha` line alone over that cut. Over the cut with no `    _rg_v=${_rg_v%$'\r'}` line it printed the
  `for count 0;` line once and no `for rec_sha` or `for rec_fp` line. The `fingerprint` edit alone printed the
  `for rec_fp` line once. `grep -n 'the planted CR never reached read_green_file on'` over the suite prints
  one line, holding ` for $rgf_what;`. The arm's run over scratch clones is OWED to the main loop at the
  close, with the `New arm:` arm's RED-first observation (DERIVED from the builder's probe).
- AC2 — `for rec_fp` — S2's record in unit 72's acceptance ledger is the main loop's at the close, on a
  Windows node, from a scratch clone staging `fingerprint) rec_fp=${_rg_v%?} ;;`; this pass wrote no line
  there. OWED to the main loop at the close (DERIVED from the spec's S2).
