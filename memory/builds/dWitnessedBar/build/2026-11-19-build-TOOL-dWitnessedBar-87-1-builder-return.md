**Serves:** journal TOOL-dWitnessedBar-87

# TOOL-dWitnessedBar-87 — builder return 1 (run `wf_a15e669e-c13`), committed d2a1d891d

## Why

The spec could be built as written. Its claims about the code still hold at HEAD: `grep -c 'lost its CR' tools/run-gates/run-gates.gov.test.sh` prints 0, the per-key loop calls `check_key_variant` with the tail reason first and then the length reason, and the gov suite and .githooks/pre-push have not changed since 6381c364f. The spec's Rollout and the permission lines on AC2 and AC3 say the records for S2 and S3 are written at the close, when the arm runs, after unit 81's own records beside 76 AC2, which are also still owed. So this pass did three things: it probed S1's break, it wrote this unit's own acceptance ledger, and it set the spec to CLOSED. It left the ledgers of units 76 and 81 unwritten. Unit 81's pass took the same route.

## Summary

Committed d2a1d891d on branch/unattended-dwitnessedbar-2ed3b3. Subject names TOOL-dWitnessedBar-87. Trailers are `Decided:`, `Pass: TOOL-dWitnessedBar-87` and `Co-Authored-By`. No code changed.

Files in the commit:
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-87-1-acceptance-ledger.md (new). Each criterion is answered on one line and leads with a token the criterion spells: AC1 `check_canary_keys` (the probe result), AC2 `TOOL-dWitnessedBar-80` (OWED), AC3 `TOOL-dWitnessedBar-76` (OWED).
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-87.md: status INPROGRESS to CLOSED, date 2026-11-21 unchanged. `gen_build_index.py --write` added its records row.
- memory/builds/dWitnessedBar/RUN.md, which holds the rows `--dispatch` staged.
- The generator's rewrites: memory/LIVE.md, memory/backlog/TOOL.md and memory/builds/dWitnessedBar/README.md. The build now reads DEFERRED, and the blocker on ask TOOL-dWitnessedBar-31 is now TOOL-dWitnessedBar-28.

Every path written was in the declared set. The ledgers of units 76 and 81 were declared but not written. The unstaged changes to help/reference/drive.md and help/reference/units.md are not mine and were left alone. `--brief` reported that the brief was already recorded and unchanged.

Check that ran: one scratch probe, C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/p87b/probe.sh. It takes the suite's own code (`check_cr_reached` through `check_key_variant`, the canary's `rgf_whats=()` loop, and the liveness loop from `rgf_seen=` to `done`) and a `rgf_fn` cut of `.githooks/pre-push#read_green_file`. It ran them over a hand-built record shaped like the AC12 arm's, on MINGW64_NT-10.0-22621 with bash 5.3.9.
- **No break:** no line printed, `fail` 0, `rgf_seen` ` rec_sha rec_fp`.
- **Break (`check_canary_keys` skips `rec_fp`, one diff line):** printed the `rec_fp` line with `(the tail variant passed a value whose last byte is not CR)`, then with `(the length variant passed a value one byte short)`. No line held `lost its CR` or `rec_sha byte check`, and no canary `never reached` line printed. `fail` 1, `rgf_seen` ` rec_sha`.

This probe stands in for the `run-gates gov canary` arm, which only the scratch-clone run exercises. It is not that run.

The pre-commit `memory hygiene --staged` hook passed, and check 23 graded this unit. `gotchas.py --for-diff HEAD~1..HEAD` printed its checklist and none of the classes needed a change: every ledger token sits on one line, there are no tables or pipes, and the ledger names the swap of the plant record for a hand-built one.

Owed to the main loop at the close:
- **AC1:** run the arm in a scratch clone under %TEMP%/<short-name>, with the suite copy's `check_canary_keys` skipping `rec_fp`, over the record `run_local_plant` builds, and observe the non-zero exit.
- **AC2:** after unit 81's S4 records beside 76 AC2, write S2's two one-line records beside AC2 in the unit-76 ledger. Each quotes a printed `rec_fp` line, one with the length reason and one with the tail reason, and names `TOOL-dWitnessedBar-80` and `TOOL-dWitnessedBar-87`. Add S2's statement that the reasons from units 79 and 80 stand where `it passed a value that lost its CR` stood.
- **AC3:** write S3's one-line record beside AC3 in the unit-81 ledger. It holds `skip` and names `check_canary_keys`, `rec_fp`, `TOOL-dWitnessedBar-76` AC2 and `TOOL-dWitnessedBar-87`.
- **legs of §7:** `memory hygiene` (full), `recall floor` and `recall floor arms`.

This unit declares no `New arm:`, so no RED-first observation is owed. Nothing was skipped or timed out. No gate, suite, bar or `--selftest` ran.
