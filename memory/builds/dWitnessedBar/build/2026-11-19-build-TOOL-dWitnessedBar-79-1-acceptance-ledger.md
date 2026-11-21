# TOOL-dWitnessedBar-79 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-79

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21, `uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`, under `set -u`, through
one scratch probe that sources the suite's own lines, `tools/run-gates/run-gates.gov.test.sh#check_cr_reached`
through `check_key_variant`, and the arm's liveness loop from its `rgf_seen=` line to its `done`, over a
`rgf_fn` cut of `.githooks/pre-push#read_green_file` and a hand-built record laid out as the AC12 arm's:
`verdict<TAB>GREEN<CR>`, two `sha` lines the second CR-ended, `reused_cache` 1 then 0`<CR>`, a CR-ended
`fingerprint`. The record `run_local_plant` builds is the main loop's at the close. The suite passed
`bash -n`. The shell-role row measures the suite at 797 past 787, widened under
`2026-11-21-build-TOOL-dWitnessedBar-79-widen-20`. No `a=$((a+1))` was added; the floor is restated by
`TOOL-dWitnessedBar-82` S1 (DERIVED from the builder's probe).

**Evidences:** TOOL-dWitnessedBar-79
- AC1 — `${_rg_v:1}` — S1's `sha` edit over the cut, then the canary's `sed`, each counted one `diff` line;
  the sourced mutant over the record read `rec_sha` as 40 bytes, `od -c` of its last byte `\r`, and `rec_fp` (DERIVED from the builder's probe)
  as 41. The `fingerprint` edit counted one and one, and read `rec_fp` as 40 bytes ending `\r` and `rec_sha` (DERIVED from the builder's probe)
  as 41 (DERIVED from the builder's probe).
- AC2 — `the length variant passed a value one byte short` — over the suite as built the loop printed no line,
  `fail` 0, `rgf_seen` ` rec_sha rec_fp`. Over a scratch suite copy whose `check_cr_reached` compares the
  count with `-ge 0` it printed
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the length variant passed a value one byte short)`
  and the same line for `rec_fp`, no tail-variant reason, `fail` 1, `rgf_seen` empty. At `-ge 41` it printed
  no line, the hole the arm's header comment names. Over a hook copy whose `sha)` case reads
  `rec_sha="$_rg_v"` it printed `(variant changed 0 lines)` then `(length variant changed 0 lines)` for
  `rec_sha` and kept it out of `rgf_seen`. The arm's run over a scratch clone, and its exit code, are OWED to
  the main loop at the close, with the `New arm:` arm's RED-first observation (DERIVED from the builder's
  probe).
- AC3 — `grep -c '^check_key_variant()'` — over the built suite `grep -c '_rg_v:1}'`,
  `grep -cF '=\)\$_rg_v/\1'` and `grep -c '^check_key_variant()'` each printed 1 (DERIVED from the builder's
  probe).
