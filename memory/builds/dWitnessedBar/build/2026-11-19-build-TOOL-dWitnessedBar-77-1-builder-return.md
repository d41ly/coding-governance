**Serves:** journal TOOL-dWitnessedBar-77

# TOOL-dWitnessedBar-77 — builder return 1 (run `wf_7f4b2302-8e5`), committed 7228b0a9a

## Why

TOOL-dWitnessedBar-77 S1 is built as its rev-4 spec states it, with no divergence. Every code claim in section 4 Evidence still held at base: lines 904-910, the liveness split at 922, `set -u` at line 31, and the shell-role row at 784. The pass commit closes the spec header and carries `Pass: TOOL-dWitnessedBar-77`.

## Summary

Built and committed as 7228b0a9a, starting from base 1f34660b7. S1 is done. S2 and AC2 are owed to the main loop at the close.

What changed in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh:
- The canary now gathers its slot values in one array, `rgf_whats`. It holds `count <n>` alone when the line count fails. Otherwise it holds each variable `check_canary_keys` prints, split as `for rgf_g in $rgf_miss`.
- `rgf_ok` is 1 only when the array is empty.
- One loop over the array runs unit 75 S2's emission statement for each value.
- The cut to the first printed variable, `${rgf_miss%%$'\n'*}`, is gone.

Other files in the same commit:
- The suite's row in memory/project/shell-role.txt went from 784 to 787, the measured count. `ratchet.py widen` wrote the record memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-77-widen-19.md.
- New acceptance ledger: memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-77-1-acceptance-ledger.md.
- The spec status moved from INPROGRESS to CLOSED; the date was already 2026-11-21.
- The files `gen_build_index.py --write` rewrote: memory/LIVE.md, memory/backlog/TOOL.md, the build README and the spec's records table.
- memory/builds/dWitnessedBar/RUN.md.

No function was added, so `gen_map` was not needed. No kickoff manifest watches these paths. Every path was in the declared write set. The two unstaged `help/reference/*.md` edits that were already in the tree were not touched.

Checks that ran, none of them a gate or suite:
1. `bash -n` on the suite passed.
2. A scratch probe, C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe77.sh. It sources the suite's own `check_cr_reached`, `CANARY_KEYS` and `check_canary_keys`, then runs the edited block under `set -u`, bash 5.3.9, `uname -s` MINGW64_NT-10.0-22621. It reads a hand-built record laid out like the AC12 record, over cuts of `.githooks/pre-push#read_green_file`. Results:
   - Hook as it is: no line printed, `fail` 0.
   - `fingerprint` edit alone: one `for rec_fp;` line.
   - Both `sha` and `fingerprint` cases reading `${_rg_v%?}`: a `for rec_sha;` line, then a `for rec_fp;` line, and no `for count` line.
   - No strip line: one `for count 0;` line and no variable line.
   - RED-first by probe: the suite as base has it printed `for rec_sha` alone on the both-keys cut.
3. The AC1 grep prints one line, holding ` for $rgf_what;`.

This probe stands in for the `run-gates gov canary` leg's AC1 half. It uses a hand-built record, not the one `run_local_plant` builds.

Owed to the main loop at the close:
- AC1's run of the arm over scratch clones under %TEMP%.
- The `New arm:` RED-first observation of that arm: the both-keys hook, and the strip-less hook.
- S2 and AC2: the `- AC1 — ` line in unit 72's acceptance ledger, quoting the `for rec_fp` line from a Windows scratch clone.
- The legs `run-gates gov canary`, `portability (shell lines only shrink)`, `recall floor`, `recall floor arms` and `memory hygiene`.

Bug-class checklist, `gotchas.py --for-diff HEAD~1..HEAD`, was run and acted on:
- guard-above-a-fold-makes-its-fallback-dead applies. Inside the loop `rgf_ok` is always 0, so the statement's `[ "$rgf_ok" = 1 ] ||` guard can never be true. I kept it because S1 names unit 75 S2's statement as the one run per value, and recorded that in a `Decided:` trailer. Removing it would be a deviation from the spec; that is the closing review's call.
- ledger-token-wrapped: each ledger token sits on one physical line.
- two-answers and amendment-left-standing: no comment or doc still says the slot names only the first variable.
- staged-break-substitutes-a-synthetic-value: the probe's record is hand-built, so the `run_local_plant` record run stays owed.

Nothing was skipped for running past its time bound.
