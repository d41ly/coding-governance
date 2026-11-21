**Serves:** journal TOOL-dWitnessedBar-80

# TOOL-dWitnessedBar-80 — builder return 1 (run `wf_152b67bc-051`), committed a967359a8

## Why

The spec, rev-4, matched the tree at base. The tail call at tools/run-gates/run-gates.gov.test.sh line 948 and the header comment at lines 845 and 849-850 were as cited. check_key_variant's body was untouched. The suite measured 797 code lines, and no file outside the suite spelled the old texts. So no divergence. Unit 80 is built and committed.

## Summary

Unit TOOL-dWitnessedBar-80 is built and committed as a967359a8 on top of dbbf94f72. No gate, suite or bar ran: AC1 and AC3 were checked by probe and grep, and AC2's arm run is left for the main loop at the close.

**What changed**
- S1: the per-key liveness loop's tail call to `check_key_variant` in `tools/run-gates/run-gates.gov.test.sh` now passes `'${_rg_v%?}x'`, a 41-byte value ending in `x`, instead of `'${_rg_v%?}'`.
- S3: the same call's label is now `'tail '` and its passed reason is `'the tail variant passed a value whose last byte is not CR'`. The other-lead argument `'it named'` is unchanged.
- The header comment now names `<var>=${_rg_v%?}x` and says it fails the tail test alone.
- No line of the function's body changed. `sh_hygiene.py#measure_code_lines` still reads 797, so the shell-role row and `symbols.json` are unchanged.

**Same commit**
- The spec's status header was set to CLOSED (date already 2026-11-21); that is the only hand edit to the spec.
- The new acceptance ledger is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-80-1-acceptance-ledger.md`.
- `memory/builds/dWitnessedBar/RUN.md` went in with the pass.
- I ran `gen_build_index.py --write` and committed what it rewrote: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README and the spec's generated records table.
- The build status now reads DEFERRED because no unit is INPROGRESS any more; unit 79's pass made the same edit.
- The trailers are `Pass: TOOL-dWitnessedBar-80` and Co-Authored-By. I did not stage `help/reference/drive.md` or `help/reference/units.md`, which were already modified in the worktree.

**Checks that ran**
These stand in for the `run-gates gov canary` leg. The probe sourced the suite's own `check_cr_reached`, `CANARY_KEYS`, `check_canary_keys` and `check_key_variant`, plus the loop from `rgf_seen=` to `done`. It ran over a cut of `.githooks/pre-push#read_green_file` and a hand-built record in the AC12 layout.
- **AC1:** for `sha` and for `fingerprint`, the variant and its mutant each differ from their source by exactly one line. The mutant reads its own key's value as 41 bytes ending in `x` and the other key's as 41 bytes ending in CR. (DERIVED from the builder's probe)
- **AC2, by probe:** on the code as built, the loop printed nothing, with `fail` at 0 and both keys seen red. With `check_cr_reached` checking only the length, it printed `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the tail variant passed a value whose last byte is not CR)` and the same line for `rec_fp`, with `fail` at 1. Putting the old `${_rg_v%?}` back under that same break printed nothing, which is the defect this unit removes.
- **AC3:** the code-line grep for `_rg_v%?}x` and the `grep -cF` for the label and reason each printed 1. The whole-file greps for `_rg_v%\?\}($|[^x])` and `lost its CR` each printed 0.
- `bash -n` passed on the suite.
- The commit's hooks ran `memory-hygiene --staged`, which passed.
- `gotchas.py --for-diff HEAD~1..HEAD` printed its checklist (exit 0). I acted on three items: each ledger token sits on one line and is spelled by its own criterion; there is no pipe-bearing table; and a `git grep` over `tools/`, `help/`, `.githooks/` and `skills/` found no reader of the old texts outside the suite.

**Left for the main loop at the close**
- AC2's arm run over a scratch clone, including its non-zero exit, as part of the `run-gates gov canary` leg (held unless GATE_SELFTESTS is set).
- The `memory hygiene` leg over the whole tree.
- The red-first observation of the new arm declared in section 7, in `tools/run-gates/run-gates.gov.test.sh`: stage a suite copy whose `check_cr_reached` has no last-byte test, and expect the tail-variant line for `rec_sha` and `rec_fp`.

No command timed out or was skipped. Probe files are under `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u80`.
