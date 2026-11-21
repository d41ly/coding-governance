# TOOL-dWitnessedBar-70 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-70

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (`uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`), through a scratch
probe that `eval`s the arm's own lines, cut from `tools/run-gates/run-gates.gov.test.sh` from
`rgf_fn=$(awk` to the `rec_sha` compare's failure line, with `ROOT` at four scratch trees under
`%TEMP%/u70p`: HEAD's `.githooks/pre-push` and three copies of it. The record is hand-built with the
arm's byte layout (`verdict<TAB>GREEN<CR>`, two `sha` lines the second CR-ended, `reused_cache` 1 then
0<CR>, a CR-ended `fingerprint`), not by `run_local_plant`; the arm's own record is the main loop's at the
close. The suite passed `bash -n`. The shell-role seed's `measure_code_lines` measures the suite at 715
past 706, widened under `2026-11-21-build-TOOL-dWitnessedBar-70-widen-12`. No `a=$((a+1))` was added: the
`rec_sha` compare's increment is now behind the canary, so the floor stays 54. While probing, a
`*$'\r'` case pattern spelled inside `$(...)` matched a value with no CR on this bash, so the canary's
CR is the variable `rgf_crb`, set outside the subshell. The §7 legs and the `New arm:` line's RED-first (DERIVED from the builder's probe)
observation are the main loop's at the close. (DERIVED from the builder's probe)

**Evidences:** TOOL-dWitnessedBar-70
- AC1 — `lose the CR` — over HEAD's hook the cut and its mutant differed in one `diff` line opening `>` (`_rg_v=${_rg_v%$'\r'}` read as `_rg_v=${_rg_v}`), the mutant's `printf %s "$rec_sha" | wc -c` printed 41 and `tail -c1 | od -c` printed `\r`; the canary held, `a` counted 1 for the compare, `fail` stayed 0 and no `gov-canary: the planted CR` line printed. `grep -c 'lose the CR' tools/run-gates/run-gates.gov.test.sh` printed 0.
- AC2 — `gov-canary: the planted CR never reached read_green_file on ` — with `ROOT` at a copy whose `sha` case is `sha) rec_sha=$(awk -F'\t' '$1=="sha"{v=$2} END{print v}' "$1"); rec_sha=${rec_sha%$'\r'} ;;` (one `diff` line from the hook), the canary counted 2 changed lines, the mutant read 40 bytes ending `b`, and the arm printed `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621; the CR-strip assertion is not counted`, `fail` 1, `a` 0, while the `rec_sha` compare held. Against a copy with `    _rg_v=${_rg_v%$'\r'}` deleted (one `diff` line), the count was 0 and the same line printed, `fail` 1, `a` 0, and the compare printed its own line ending `'b…b\r'`. Against S3's print-every-match copy (one `diff` line), the count was 1, the mutant read 82 bytes, and the same line printed beside the compare's `'a…a|b…b'`. (DERIVED from the builder's probe)
- AC3 — `rec_sha` — OWED to the main loop at the close: the two S3 breaks staged on a Windows node, each recorded in unit 66's ledger as a `- AC2 — ` line carrying the arm's failing lines and `uname -s`. This pass's probe is not that record.
- AC4 — `TOOL-dWitnessedBar-70` — unit 66's ledger line for AC2, rewritten in place, states that at unit 66's build gawk's text-mode input and bash `$(...)` drop the CR on Git for Windows, that unit 69's loop now passes it on, and cites this spec's §4 Evidence; it no longer records the CR-strip half as owed.
