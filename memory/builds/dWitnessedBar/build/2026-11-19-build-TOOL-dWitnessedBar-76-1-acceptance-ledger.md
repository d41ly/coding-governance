# TOOL-dWitnessedBar-76 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-76

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21, GNU bash 5.3.9 `x86_64-pc-cygwin`, through one scratch probe that sources the suite's own
lines, `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` through `check_canary_keys` and the arm
from its `rgf_fn` cut of `.githooks/pre-push#read_green_file` through the `rec_fp` compare, over a
hand-built record laid out as the AC12 arm's. The record `run_local_plant` builds is the main loop's at the
close. The suite passed `bash -n`. The shell-role seed measures the suite at 784 past 773, widened under
`2026-11-21-build-TOOL-dWitnessedBar-76-widen-18`. No `a=$((a+1))` was added: the loop gates the
`rec_sha` and `rec_fp` compares' existing counts, so `a` counts 2 over this slice as before and the floor
stays as `TOOL-dWitnessedBar-73` S15 states it (DERIVED from the builder's probe).

**Evidences:** TOOL-dWitnessedBar-76
- AC1 — `fingerprint:rec_fp` — S3's `fingerprint` `sed` over the cut changed one `diff` line and the
  canary's `sed` over that variant one; sourced over the record, its mutant gave
  `printf %s "$rec_fp" | wc -c` 40 and `rec_sha` 41. The `fingerprint:rec_fp` grep names the
  `CANARY_KEYS` line, `grep -c '^check_canary_keys()'` printed 1, the `rec_fp` byte-measure grep printed
  nothing, and neither `rgf_crb` nor `rgf_mr` remains (DERIVED from the builder's probe).
- AC2 — `byte check was not seen red` — over the built suite the slice printed no line, `fail` 0,
  `rgf_seen` naming `rec_sha rec_fp`. Over a scratch copy whose `check_canary_keys` skips `rec_fp`, one
  `diff` line from the suite, it printed
  `gov-canary: the rec_fp byte check was not seen red on its liveness variant (it passed a value that lost its CR)`,
  `fail` 1, the `rec_fp` compare uncounted. The arm's exit over a scratch clone is OWED to the main loop
  at the close, with the `New arm:` arm's RED-first observation (DERIVED from the builder's probe).
- AC3 — `it named rec_sha whose CR arrived` — over a scratch copy whose `check_canary_keys` prints
  `rec_sha` before every `rec_fp` it prints, the slice printed the `rec_fp` line with
  `it named rec_sha whose CR arrived`, `fail` 1. A `CANARY_KEYS` whose `sha` key is misspelt printed the
  `rec_sha` line with `variant changed 0 lines`. The scratch-clone run is OWED to the main loop at the
  close (DERIVED from the builder's probe).
