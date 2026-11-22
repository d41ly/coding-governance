**Serves:** journal TOOL-dWitnessedBar-74

# TOOL-dWitnessedBar-74 — builder return 1 (run `wf_c191cf83-648`), committed 6a12d559c

## Why

The spec could be built as written. Every claim it makes about current code held at the base: the inline `rec_sha` test sat in `rgf_mr`, the hook's case reads `sha) rec_sha=$_rg_v`, the canary's sed matched one line, and the shell-role row was 716 after unit 72. No divergence.

## Summary

Unit TOOL-dWitnessedBar-74 is built and committed as 6a12d559c, on top of d94b52e24. The commit carries `Pass: TOOL-dWitnessedBar-74` and the spec status is set to CLOSED.

What changed in tools/run-gates/run-gates.gov.test.sh:
- **S1:** a new top-level function, `check_cr_reached() ( LC_ALL=C; . "$1" || exit 1; read_green_file "$2"; _cc_v=${!3}; [ "${#_cc_v}" -eq 41 ] && [ "${_cc_v: -1}" = $'\r' ] )`. The canary's mutant is now also written to `$rgf_t/cut-mut.sh`, and `rgf_ok` calls `check_cr_reached "$rgf_t/cut-mut.sh" "$rgf_rec" rec_sha`. The `rec_fp` half stays inline in `rgf_mr` and now expects `41 cr`.
- **S2:** each run writes a variant whose `sha` case reads `rec_sha=${_rg_v%?}` to `$rgf_t/cut-var.sh`, plus its canary mutant `cut-var-mut.sh`. It counts the `diff` lines opening `>` for both and requires `check_cr_reached` to return non-zero on the mutant for `rec_sha`.
- **S3:** if the liveness check fails, the arm prints `gov-canary: the rec_sha byte check was not seen red on its liveness variant (<reason>)` and sets `fail=1`. The `rec_sha` compare's count is then gated on both `rgf_ok` and `rgf_live`. No assertion was added, so `FLOOR_ASSERTIONS` is unchanged.

Other files in the commit:
- memory/project/shell-role.txt: widened with `ratchet.py widen`, which wrote memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-74-widen-15.md. The count was then set to 735, the value the seed measured, as unit 51 S1 directs.
- memory/map/generated/symbols.json: `gen_map.py --write` added `check_cr_reached`.
- The acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-74-1-acceptance-ledger.md.
- The spec status set to CLOSED, plus its generated records table.
- RUN.md, README.md, LIVE.md and backlog/TOOL.md from `gen_build_index.py --write`.
- help/reference/drive.md and units.md were already modified before this pass and were not staged.

Checks that ran (none is a gate or suite):
- `bash -n` on the suite.
- A probe cutting `check_cr_reached` and the hook's `read_green_file` over a hand-built record laid out like AC12's. Each `diff` counted 1 line. The variant's mutant gave `rec_sha` 40 bytes and `rec_fp` 41. `check_cr_reached` returned 0 on the canary's mutant and 1 on the variant's mutant for `rec_sha`, whether called directly or inside `$(...)`. (DERIVED from the builder's probe)
- A probe running the arm's own lines, from `rgf_t=$(mktemp -d)` through `rm -rf`, over the real `run_local_plant` record with TMPDIR at %TEMP%/w74 (since removed):
  - Over the built tree: no liveness line, fail 0, a 4, as before.
  - Suite copy whose comparison line is `true`: printed `(it passed a value that lost its CR)`, fail 1, a 3.
  - Hook copy spelling `rec_sha="$_rg_v"`: printed `(variant changed 0 lines)`, fail 1, a 3.
- AC1's greps: `^check_cr_reached()` counts 1, the call grep names 2 lines, and the `rec_sha` byte-measure grep prints nothing. (DERIVED from the builder's probe)

These probes stand in for `run-gates gov canary` (AC1 to AC3) and for `portability (shell lines only shrink)`, through the seed measure.

Owed to the main loop at the close:
- The legs of §7: `run-gates gov canary` (with GATE_SELFTESTS), `portability (shell lines only shrink)`, `recall floor`, `recall floor arms` and `memory hygiene`. Check 23 on the new ledger is held under `--staged`.
- The suite's non-zero exit for AC2 and AC3 in scratch clones.
- The `New arm:` RED-first observation of both staged breaks.

Bug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` was run over the commit. The ledger-token-wrap class was acted on: every ledger line has an even number of backticks and each bullet's lead token is on its first line. Nothing else it named applied. Nothing was skipped for running past its time limit.
