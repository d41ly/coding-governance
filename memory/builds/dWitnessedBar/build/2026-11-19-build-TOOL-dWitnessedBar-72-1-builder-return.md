**Serves:** journal TOOL-dWitnessedBar-72

# TOOL-dWitnessedBar-72 — builder return 1 (run `wf_17c7e5af-02a`), committed fa536b7cd90ea1f469146ee88bf13443a15ea603

## Why

TOOL-dWitnessedBar-72 is built as spec rev-4 describes. Before writing anything I checked the spec against the tree and found no divergence. The suite comment at line 836 said "uncanaried". The rec_sha compare's count was gated on rgf_ok, and the rec_fp compare's count was a bare a=$((a+1)). In .githooks/pre-push, read_green_file reads `fingerprint) rec_fp=$_rg_v ;;`, and AC2's two greps print 1 and 0. The suite measured 715 code lines, matching its shell-role row.

## Summary

TOOL-dWitnessedBar-72 is committed as fa536b7cd90ea1f469146ee88bf13443a15ea603 on base c02a7d3a35d39b42d9cc3c0b1bb8ed840e999440. AC1 and AC2 were observed by probe on this node; AC3 and the New arm's RED-first observation are owed to the main loop at the close.

**What changed** in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh:
- The mutant subshell `rgf_mr` now measures `rec_fp` the same way it measures `rec_sha`, with the CR test reading `rgf_crb`.
- `rgf_ok` is set only when the diff count is 1 and `rgf_mr` reads `41 cr 41 cr`.
- The `rec_fp` compare's `a=$((a+1))` is now gated on `rgf_ok`, as the `rec_sha` compare's is.
- The arm comment calls the `rec_fp` grading canaried instead of "uncanaried".
- `.githooks/pre-push` is unchanged; S2 already held.

**Records in the same commit:**
- The shell-role row in memory/project/shell-role.txt went from 715 to 716 through `ratchet.py widen`, with the widen record memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-72-widen-14.md. I declared that file with `--dispatch` and it was admitted.
- The acceptance ledger is memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md.
- The spec status header is now CLOSED.
- RUN.md and the files `gen_build_index --write` rewrote are included: LIVE.md, backlog/TOOL.md, the build README and the spec's generated records block. The regenerated index now shows the build as DEFERRED.
- No function was added, so `gen_map` was not needed. No file on the kickoff manifest's watch list was touched.
- `--brief` was already recorded and reported "unchanged".

**Checks that ran** (each stands in for the `run-gates gov canary` leg, which did not run):
- `bash -n` on the suite passed.
- A scratch probe sourced the arm's own lines, from `rgf_t=$(mktemp -d)` to `rm -rf "$rgf_t"`, over the record `run_local_plant` builds. `ROOT` pointed at copies of the hook under %TEMP%/w72 (since deleted), on `uname -s` MINGW64_NT-10.0-22621:
  - **HEAD's hook:** `rgf_mr` read `41 cr 41 cr`, `a`=4, `fail`=0, and no canary line printed. The mutant's `printf %s "$rec_fp" | wc -c` printed 41 and `tail -c1 | od -c` showed `\r`.
  - **Bare `$(awk ...)` fingerprint read** (one diff line): count 1, `rgf_mr` read `41 cr 40`, the line `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621` printed, `fail`=1, `a`=2. That is two fewer than over the hook, so both compares went uncounted.
  - **Same read followed by the strip** (one diff line): count 2, the same line printed, `fail`=1, `a`=2.
  - **The arm as it stood at base, over the bare copy:** stayed green (`a`=4, `fail`=0). That is the Red-when this unit closes.
- AC2's two greps printed 1 and 0.
- `measure_code_lines` measured the suite at 716.

**Owed to the main loop at the close:**
- AC3: stage unit 67 AC2's break (a `read_green_file` without its CR strip) on a Windows node, and add a second `- AC2 — ` line to unit 67's ledger. That line quotes the failing line naming `rec_fp` and the `uname -s` value, and names TOOL-dWitnessedBar-72.
- The New arm's RED-first observation for the canary's `rec_fp` assertion in tools/run-gates/run-gates.gov.test.sh: the bare-read copy and the stripped-read copy, as above.
- The legs of §7: `run-gates gov canary` (only with GATE_SELFTESTS set), `portability (shell lines only shrink)`, `recall floor`, `recall floor arms` and `memory hygiene`.

`gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 30 classes. I checked the relevant ones and none needs action. The probe uses the shipped record rather than a synthetic one, each ledger token sits on one line, and the comment's other clauses still hold. The canary's failure-line wording is left as unit 70 wrote it, because its key slot belongs to units 75 and 77. No command timed out.
