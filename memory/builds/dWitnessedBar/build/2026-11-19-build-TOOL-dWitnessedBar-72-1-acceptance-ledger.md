# TOOL-dWitnessedBar-72 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-72

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (`uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`), through a scratch
probe that sources the arm's own lines, cut from `tools/run-gates/run-gates.gov.test.sh` from
`rgf_t=$(mktemp -d)` to `rm -rf "$rgf_t"`, so the record is the one `run_local_plant` builds, with `ROOT`
at three scratch trees under `%TEMP%/w72`: HEAD's `.githooks/pre-push` and two copies of it, each one
`diff` line from it. The suite passed `bash -n`. The shell-role seed's `measure_code_lines` measures the
suite at 716 past 715, widened under `2026-11-21-build-TOOL-dWitnessedBar-72-widen-14`. No `a=$((a+1))`
was added: the `rec_fp` compare's increment is now behind the canary as the `rec_sha` compare's is, so
over the hook `a` counts what it did before and the floor stays as it was. The §7 legs and the
`New arm:` line's RED-first observation are the main loop's at the close.

**Evidences:** TOOL-dWitnessedBar-72
- AC1 — `gov-canary: the planted CR never reached read_green_file on ` — over HEAD's hook the mutant's `printf %s "$rec_fp" | wc -c` printed 41 and `tail -c1 | od -c` printed `\r`, the canary's measurement read `41 cr 41 cr`, `a` counted 4, `fail` stayed 0 and no `gov-canary: the planted CR` line printed. With `ROOT` at a copy whose case is `fingerprint) rec_fp=$(awk -F'\t' '$1=="fingerprint"{print $2}' "$1") ;;`, the count was 1, the measurement read `41 cr 40`, and the arm printed `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621; the CR-strip assertion is not counted`, `fail` 1, `a` 2, two fewer than over the hook. Against a copy with the same read followed by `; rec_fp=${rec_fp%$'\r'}`, the count was 2 and the same line printed, `fail` 1, `a` 2. The arm as it stood at `001ee47f8`, over the bare-read copy, printed no line with `fail` 0 and `a` 4: the Red-when this unit closes.
- AC2 — `fingerprint)` — `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` piped to `grep -c 'fingerprint)'` printed 1, and to `grep -c '"fingerprint"'` printed 0. This pass changed nothing in `.githooks/pre-push`.
- AC3 — `rec_fp` — OWED to the main loop at the close: unit 67 AC2's break, a `read_green_file` without its one CR strip, staged on a Windows node and recorded in unit 67's ledger as a second `- AC2 — ` line carrying the arm's failing line naming `rec_fp`, the `uname -s` and `TOOL-dWitnessedBar-72`. This pass's probe is not that record.
