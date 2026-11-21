**Serves:** journal TOOL-dWitnessedBar-55

# TOOL-dWitnessedBar-55 — builder return 2 (run `wf_123ab74c-619`), committed 599c23cef

## Why

The spec as written could be built. I found no divergence: the hook's live `read_policy_key` at .githooks/pre-push:1506-1521 matches the spec's §4 evidence, and every helper the arm reuses is in scope. The first builder (`wf_f6e58a9a-ccd`) built the unit but could not commit while unit 41's files sat uncommitted in the same tree. I checked its work against the spec, re-ran its probe, and committed it as this pass. The spec status moved to CLOSED in the same commit.

## Summary

Committed TOOL-dWitnessedBar-55 as 599c23cef, starting from da5eef59a. The step now reads INHERITED_RED the way the pre-push hook does, and every check below passed. No gate ran.

**What the commit holds (11 files, all staged by name):** (DERIVED from the builder's probe)
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/govkit/steps/inherited_red.py
  - New `check_policy_assignment`: a line counts only if, with one trailing CR cut, it begins exactly `<key>=`.
  - `read_value` takes the last such line and cleans it the way `read_policy_key` does.
  - New `render_gate_rest`: the up takes out only those lines and keeps every other line byte for byte.
  - The witness prints a `not an assignment <file>:<line>` row and still exits 0.
  - `GATE_POLICY_FILE` is read by the same rule.
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/govkit/selftest.py: `check_inherited_red_step` gains AC1 to AC3 targets and the AC4 parity check. AC4 cuts `read_policy_key` live from the hook, runs it under the resolved bash, reads a `K=plain` sentinel first, and confirms all 11 rows were checked. (DERIVED from the builder's probe)
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/help/upgrade-steps.md: the section on where INHERITED_RED's value lives states the rule (S5).
- The acceptance ledger and deviation record 552 (`author-recorded`). I added one sentence to 552 naming the local helper `read_hook_value` nested inside the arm.
- The spec flipped INPROGRESS to CLOSED, with nothing else hand-edited. The index generator added its record rows to the spec and rewrote memory/LIVE.md, memory/backlog/TOOL.md, the dWitnessedBar README and the dClosedLoop as-built view. The map generator changed only memory/map/generated/symbols.json. Every one of these paths was in the declared write set, so no extra `--dispatch` was needed.
- The brief was already recorded (`--brief` reported it unchanged).
- The trailers are `Pass: TOOL-dWitnessedBar-55` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`; I used the charter's spelling, not the harness reminder's "Opus 5.5". The pre-commit hooks passed.
- help/reference/drive.md and help/reference/units.md show as modified, but only line endings differ, no content. They are not this unit's, so I left them unstaged.

**Checks that ran (none is a gate):**
- **Naming lexicon** (`--suggest`, py.function): `check_policy_assignment`, `render_gate_rest` and `read_hook_value` all passed.
- **The first builder's probe** (C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe55.py), re-run over fixtures at %TEMP%/ir55q. It stands in for the `govkit selftest` leg:
  - AC4: the sentinel read `plain`, and all 11 rows plus 3 extra rows gave the same value from the step and from the hook's function. (DERIVED from the builder's probe)
  - AC1: wrote `every-red` and removed both lines.
  - AC2: neither fixture wrote a `blocks` value.
  - AC3: left exactly `export INHERITED_RED=park\n`, and the witness exited 0 naming `.githooks/gate-env.sh@6834ee4b:1`.
  - A CRLF file with no final newline kept its other lines byte for byte.
- **AC5 greps**, standing in for the `docs` leg: "not an assignment" prints lines 442 and 461, inside the section that runs from line 430 to 474. The old wording "line out of each file that held one" is gone.
- **Bug-class checklist** (`gotchas.py --for-diff HEAD~1..HEAD`): it selected 33 classes plus 6 universal. I checked the ones that apply and none needed a change:
  - new local names in a long function: the new block sits at the end of the function;
  - a line claim matched over the whole output: AC3 matches the whole row text;
  - a fixture that passes by finding nothing: the sentinel and the 11-row count guard this;
  - a ledger token wrapped across a line: none is.

**Owed at the close, by the main loop:**
- The spec's legs of §7: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `recall floor arms`, `memory hygiene`, `policy fixtures`, `step-rows-frozen` and `docs`.
- The new arm in tools/govkit/selftest.py (covering AC1 to AC4) has not been seen red yet. Three breaks to stage:
  - for AC1, a reader that takes the first assignment;
  - for AC4, the base reader built on `build_line_re`, on the indented, spaced, leading-tab and BOM rows;
  - for AC3, the base witness, which prints no `not an assignment` row.

Nothing was skipped for running past its time limit.
