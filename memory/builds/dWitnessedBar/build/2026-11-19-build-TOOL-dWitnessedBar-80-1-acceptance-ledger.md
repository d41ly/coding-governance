# TOOL-dWitnessedBar-80 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-80

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21, `uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`, through one scratch probe
that sources the suite's own lines, `tools/run-gates/run-gates.gov.test.sh#check_cr_reached`, `CANARY_KEYS`,
`check_canary_keys` and `check_key_variant`, and the arm's liveness loop from its `rgf_seen=` line to its
`done`, over a `rgf_fn` cut of `.githooks/pre-push#read_green_file` and a hand-built record laid out as the
AC12 arm's: `verdict<TAB>GREEN<CR>`, two `sha` lines the second CR-ended, `reused_cache` 1 then 0`<CR>`, a
CR-ended `fingerprint`. The record `run_local_plant` builds is the main loop's at the close. The suite passed
`bash -n`, and `tools/gate-lint/sh_hygiene.py#measure_code_lines` still reads it at 797, its shell-role row
unmoved. No function was added, so the symbol map was not regenerated (DERIVED from the builder's probe).

**Evidences:** TOOL-dWitnessedBar-80
- AC1 — `${_rg_v%?}x` — S1's `sha` edit over the cut, then the canary's `sed`, each counted one `diff` line;
  the sourced mutant over the record read `rec_sha` as 41 bytes, `od -c` of its last byte `x`, and `rec_fp`
  as 41 ending `\r`. The `fingerprint` edit counted one and one, and read `rec_fp` as 41 bytes ending `x` and
  `rec_sha` as 41 ending `\r` (DERIVED from the builder's probe).
- AC2 — `tail variant` — over the suite as built the loop printed no line, `fail` 0, `rgf_seen`
  ` rec_sha rec_fp`. Over a scratch copy of the suite's functions whose `check_cr_reached` tests the count
  alone, its last-byte test cut, it printed
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the tail variant passed a value whose last byte is not CR)`
  and the same line for `rec_fp`, no length-variant reason, `fail` 1, `rgf_seen` empty. The same break with
  the tail call's replacement put back to the forty-byte `${_rg_v%?}` printed no line, `fail` 0, the defect
  this unit removes. The arm's run over a scratch clone, and its exit code, are OWED to the main loop at the
  close, with the `New arm:` arm's RED-first observation (DERIVED from the builder's probe).
- AC3 — `lost its CR` — over the built suite the code-line `grep -c '_rg_v%?}x'` and the `grep -cF` of the
  tail call's label, reason and other lead each printed 1; `grep -cE '_rg_v%\?\}($|[^x])'` and
  `grep -c 'lost its CR'` over the whole file each printed 0 (DERIVED from the builder's probe).
