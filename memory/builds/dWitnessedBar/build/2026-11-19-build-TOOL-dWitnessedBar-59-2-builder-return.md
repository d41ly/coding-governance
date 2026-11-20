**Serves:** journal TOOL-dWitnessedBar-59

# TOOL-dWitnessedBar-59 — builder return 2 (run `wf_15338b0e-3b5`), committed 4657d344dd6cf3bf8dfc449f102a57ae377d7b92

## Why

TOOL-dWitnessedBar-59 is built and committed as one pass. I checked the spec against the tree first and found no divergence. `read_policy_key` in `.githooks/pre-push` reads with a here-string and cuts one trailing CR. The landed step `tools/govkit/steps/inherited_red.py` splits on LF only, with 5 `.split("\n")` calls and no `splitlines`. `check_inherited_red_step` held 11 parity rows and a comment naming a lone CR as unchecked. `build_target` accepts bytes. The previous builder's only blocker was the README conflict with unit 1. That is gone now that unit 1 has landed and the README is in this unit's declared write set.

## Summary

I applied the first builder's saved patch to C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/govkit/selftest.py. It applied cleanly at base b0cf02bad. It adds to `check_inherited_red_step`:
- the AC1 target `ir59-ac1`, where the up must write `every-red` over `park<CR>INHERITED_RED=land`;
- the AC2 target `ir59-ac2`, where the witness must exit 1 with `assigns` once and `not an assignment` nowhere, and the up must leave exactly `A=1\nB=2\n`;
- the AC3 parity row labelled `lone-cr`, whose agreed hook value is `park\rINHERITED_RED=land`. The row-count check now expects 12 rows, and the "WHAT IT DOES NOT CHECK" comment no longer names a lone CR.

Commit 4657d344d contains:
- the selftest change;
- the spec status flip INPROGRESS to CLOSED, dated 2026-11-20 (the pre-commit hook also regenerated the spec's records table);
- the acceptance ledger C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-59-1-acceptance-ledger.md, re-dated to base b0cf02bad;
- the files the index generator rewrote: memory/builds/dWitnessedBar/README.md, memory/LIVE.md and memory/backlog/TOOL.md.

It went through the hooks without `--no-verify`, with explicit paths only, and carries the trailers `Pass: TOOL-dWitnessedBar-59` and `Co-Authored-By`. RUN.md had no uncommitted rows, so it is not in the commit. `gen_map.py --check` exited 0, so `symbols.json` did not change. selftest.py is not on the kickoff manifest's watch list (the hook confirmed this), and no deviation record was needed. `--brief` reported the brief already recorded and unchanged. help/reference/drive.md and help/reference/units.md were already modified before I started, and I left them alone.

Checks that ran:
1. `python -m py_compile` on the edited selftest.py passed.
2. The scratch probe C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe59.py ran the step under `-I` over the AC1 and AC2 fixtures in %TEMP%/ir59p, now deleted. It also cut `read_policy_key` from the hook and ran it under the resolved bash after the K=plain sentinel read `plain`.
   - On the live step, AC1, AC2 and AC3 all passed.
   - On a copy with the 5 `.split("\n")` calls changed to `.splitlines()`, all three failed: AC1 wrote own-mixed-contended; AC2's witness printed `not an assignment` and its up kept ` INHERITED_RED=land`; AC3's `read_value` read `land`.
   - This probe stands in for the `govkit selftest` leg. The RED half was seen in the probe only, not inside the suite.
3. `gotchas.py --for-diff HEAD~1..HEAD` ran with exit 0, and I went through the classes it selected:
   - The new locals (`lone_cr`, `named`, `name`, `agreed`) are not read anywhere later in the function.
   - AC2's substring count over the whole of stdout is what the spec states.
   - The fixture does trigger the lone-CR path, as the red copy shows.
   - The ledger tokens are not wrapped across lines.
   - The step's code has not moved.

Owed to the main loop at the close:
- the `New arm:` RED-first then GREEN observation inside the suite (tools/govkit/selftest.py, AC1 AC2 AC3, staged by `str.splitlines()` in `read_value`, `render_gate_rest` and `cmd_witness`);
- the legs of §7: govkit selftest, govkit refusal join, govkit acceptance matrix, recall floor arms, policy fixtures and memory hygiene.

No command timed out or was skipped.
