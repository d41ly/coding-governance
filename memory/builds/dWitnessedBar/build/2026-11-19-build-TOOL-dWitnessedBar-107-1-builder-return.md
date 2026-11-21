**Serves:** journal TOOL-dWitnessedBar-107

# TOOL-dWitnessedBar-107 — builder return 1 (run `wf_58d52771-d89`), committed 71ba863c24f4213b967529cda182f438b7d5ed61

## Why

TOOL-dWitnessedBar-107 is built as its spec (rev-1) states and committed in one pass commit. The commit carries the `Pass: TOOL-dWitnessedBar-107` trailer, and the spec header moved INPROGRESS -> CLOSED in that commit. Every spec claim I probed held at HEAD: both blobs, the d75ea52b and 04da8977 cited lines, `read_local_verdict`'s unread first argument, the canary loop line, `FLOOR_ASSERTIONS=80` with unit 90's owner line, and the shell-role count of 853. Three choices the spec did not state are recorded as deviation 1071 (`author-recorded`), so no divergence was raised.

## Summary

**What changed**
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/verdict_backends.py`:
  - **S1:** `run_verify_peer` now does steps 1 to 9 in order. It works out the tree and slot before the bar, reads the slot's run_id before and after the bar, and runs the bar with `GATE_RUN_ID` removed from its environment. It refuses a slot the bar did not write, reads the slot through `read_local_verdict({}, sha, tree, repo)`, and publishes only a witnessed GREEN on exit 0 or a RED on a non-zero exit. It re-reads the run_id before signing, and the tag carries the reader's state and the run_id the bar wrote.
  - **S2:** new `read_slot_run_id`, placed beside `read_local_verdict`.
  - **S3:** new `peer-stale-slot` row in `PLANTS`, a branch for it in `run_peer_plant`, and the new `run_stale_slot_plant` (one candidate, a stub bar driven by `VB_STUB_BAR`, eight scenarios).
  - **S5:** one added sentence in the module docstring.
- **S4**, `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh`: `peer-stale-slot:0` is appended to the line holding `remote-green:0`, `FLOOR_ASSERTIONS` goes from 80 to 81 with its `# RAISED` comment below it, and the loop's block comment gains one sentence. Unit 90's owner line is untouched.
- **S5**, `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/help/verdict-backends.md`: one paragraph added under "Running the peer verifier".
- **Records in the same commit:** the acceptance ledger at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-107-1-acceptance-ledger.md` and deviation 1071 at `memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-107-deviation-1071.md`.
- **Generated files, also committed:** `memory/map/generated/symbols.json` from `gen_map.py --write`; and from `gen_build_index.py --write`, the spec's generated records block plus `memory/LIVE.md`, `memory/backlog/TOOL.md`, the dWitnessedBar README and the dClosedLoop as-built file. `RUN.md` is in the commit too.
- Every path outside the main loop's declared write set was declared first with `--dispatch --writes`, and none was refused.

**Deviation 1071**
- Scenario 4 counts the verdict refs in its own `python -c` process through `run_scenario`, because the helper's signature in S3 gives it no handle on the scenario list. The result it adds is the one the spec names.
- Scenario 1 passes `VB_STUB_BAR=""`, which the stub reads as unset.
- If the re-read before signing (step 8) fails with an `OSError`, the candidate is refused with step 8's "rewritten while it was read" message instead of crashing.

**Checks that ran (each stands in for the gate named)**
- **AC1 to AC4, standing in for the gov canary's `peer-stale-slot:0` case:** `python tools/run-gates/verdict_backends.py --fixture --plant peer-stale-slot` over its scratch fixture, with ssh-keygen running, printed `8 of 8 scenario(s) held · all held` and exited 0. Scenario 1 printed `at run r0, a record it did not write`; scenario 2 `reads NONE` and `reused 1 leg(s) from the cache`; scenario 3 `the bar exited 1` and `reads GREEN`; scenario 4 `verdict refs: 0`. The RED tag carried `run_id s-red` and the GREEN tag `run_id s-clean`, the second run having `GATE_RUN_ID=s-red` set.
- **AC5, standing in for the shell-role leg:** the greps printed what AC5 names (line 788), and `sh_hygiene.py --shell-role --measure` printed 853.
- **AC6:** `grep -c 'not published'` printed 1, and `GATE_RUN_ID` appears in the help paragraph, the docstring and step 3's `env.pop`.
- **Naming lexicon:** `lexicon.py --suggest` returned OK for `read_slot_run_id` and `run_stale_slot_plant`.
- **Python reads leg:** `py_compile` passed. This is only a compile check, not that leg.

**Owed at the close (main loop, after every unit is terminal)**
- The New arm's RED-first observation: the `peer-stale-slot:0` canary case run against the base `run_verify_peer`. It has not been seen red, and covers AC1 to AC4.
- The gov canary run under `GATE_SELFTESTS`, with its floor of 81.
- The legs of §7: lexicon naming, python reads, portability/shell-role, memory hygiene, spec tokens.

**Bug-class checklist**
- `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit and selected 27 classes plus 6 universal.
- Acted on:
  - **fixture-passes-by-finding-nothing:** the plant does plant the `reused_cache 1` slot, and scenario 1 names `r0`.
  - **heredoc-escape:** the stub is a raw Python string, and its tab-separated records parsed correctly.
  - **ledger-token-wrapped:** each ledger token is on one line and spelled exactly as in its criterion.
  - **pipe-in-a-code-span:** none of my records holds a table.
  - **guard-above-a-fold:** the no-file and unchanged-run_id refusals are separate branches, so neither is dead.

**Other notes**
- Nothing timed out or was skipped.
- The plant left a scratch directory under `%TEMP%/vb107`, because the existing `run_fixture` cleanup does not raise when it fails. I removed it by hand.
- `help/reference/drive.md` and `help/reference/units.md` were already modified when I started. I did not touch or stage them.
