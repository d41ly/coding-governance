# TOOL-dWitnessedBar-74 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-74

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (`uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`), through two scratch
probes. The first cuts `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` and HEAD's
`.githooks/pre-push#read_green_file` and reads a hand-built record laid out as the AC12 arm's. The second
sources the arm's own lines, cut from the suite from `rgf_t=$(mktemp -d)` to `rm -rf "$rgf_t"`, so the
record is the one `run_local_plant` builds, under `TMPDIR` at `%TEMP%/w74`. The suite passed `bash -n`.
The shell-role seed measures the suite at 735 past 716, widened under
`2026-11-21-build-TOOL-dWitnessedBar-74-widen-15`. No `a=$((a+1))` was added: the liveness check gates
the `rec_sha` compare's existing count, so over the hook `a` counts 4 as it did before and the floor
stays as it was. The §7 legs and the `New arm:` line's RED-first observation are the main loop's at the (DERIVED from the builder's probe)
close.

**Evidences:** TOOL-dWitnessedBar-74
- AC1 — `check_cr_reached` — TOOL-dWitnessedBar-84 S1: this criterion's no-second-copy clause is graded for `rec_sha`, the one key `check_cr_reached` served at this unit's pass, `7c579ad47`; unit 72's inline `rec_fp` comparison, present at that pass (`tools/run-gates/run-gates.gov.test.sh@7c579ad47:889-890`), is the copy `TOOL-dWitnessedBar-76` S2 moved, and `TOOL-dWitnessedBar-76` AC1 with `TOOL-dWitnessedBar-84` AC2 are the whole-suite observation. TOOL-dWitnessedBar-84 S3, observed with checks that exist at order 40 and reading no `CANARY_KEYS`: `git show 7c579ad47:tools/run-gates/run-gates.gov.test.sh | grep -c 'check_cr_reached .*rec_sha'` printed 2, the canary's assertion and the liveness call, and `TOOL-dWitnessedBar-84` AC2's probe over that blob with `rec_(sha|fp)` read as `rec_sha` printed nothing. TOOL-dWitnessedBar-84 S4: the `rec_sha` grep below reads one key and four measures, `wc -c`, `tail -c`, `${#` and `: -1}`, and misses `od` and `cut -c`; `TOOL-dWitnessedBar-84` AC2's probe, which reads both keys and every byte measure, is the observation of this criterion's Red-when for a second copy in any spelling. TOOL-dWitnessedBar-84 S7, S8: the symbol-tier key `check_cr_reached` was rendered at `7c579ad47` by `python tools/codebase-map/gen_map.py --write`, and `codebase-map coverage + freshness`, the unguarded leg the minted function moves, is the leg the close runs for it under `TOOL-dWitnessedBar-84` §7.
  S2's `sed` over the cut changed one `diff` line, and the canary's `sed` over
  that variant changed one; sourced over the AC12-layout record, the variant's mutant gave
  `printf %s "$rec_sha" | wc -c` 40 and `rec_fp` 41, and `check_cr_reached` returned 1 on it for
  `rec_sha` and 0 for `rec_fp`; on the canary's mutant it returned 0 for both, and on the unmutated cut 1
  for `rec_sha`, called directly and inside `$(...)`. `grep -c '^check_cr_reached()'` printed 1, the
  `check_cr_reached "…" "…" rec_sha` grep named two lines, the canary's call and S2's, and the
  `rec_sha` byte-measure grep printed nothing.
- AC2 — `gov-canary: the rec_sha byte check` — the arm over the built tree printed no such line, `fail` 0,
  `a` 4. Over a scratch suite copy whose `check_cr_reached` comparison line reads `true`, one `diff` line
  from the suite, the arm printed `gov-canary: the rec_sha byte check was not seen red on its liveness variant (it passed a value that lost its CR)`,
  `fail` 1, `a` 3. The suite's exit over that copy is OWED to the main loop at the close, with the
  `New arm:` arm's RED-first observation.
- AC3 — `variant changed 0 lines` — TOOL-dWitnessedBar-84 S6 supersedes the quoted-spelling red below: the `<key>)` edit in `tools/run-gates/run-gates.gov.test.sh#check_key_variant` now matches `\(<key>) <var>=\)"\{0,1\}\$_rg_v"\{0,1\}`, so a `sha) rec_sha="$_rg_v" ;;` arm is edited and seen red, and only an arm split across two lines still prints `tail variant changed 0 lines` and `length variant changed 0 lines` (`TOOL-dWitnessedBar-84` AC6).
  With `ROOT` at a scratch tree whose `.githooks/pre-push` spells the
  case `sha) rec_sha="$_rg_v" ;;`, one `diff` line from the hook, the arm printed
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (variant changed 0 lines)`,
  `fail` 1, `a` 3. The run in a scratch clone is OWED to the main loop at the close.
