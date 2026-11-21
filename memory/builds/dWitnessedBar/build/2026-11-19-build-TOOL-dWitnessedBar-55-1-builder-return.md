**Serves:** journal TOOL-dWitnessedBar-55

# TOOL-dWitnessedBar-55 — builder return 1 (run `wf_f6e58a9a-ccd`), a divergence, nothing committed

## Why

The code is built and checked, but no commit could pass the hooks while sibling TOOL-dWitnessedBar-41's uncommitted work shares this worktree.

(1) Running `gen_build_index.py --write` rewrote memory/builds/dWitnessedBar/README.md: unit 55's row went to CLOSED and the record count from 559 to 561. Declaring that file with `--dispatch` was refused by UNATTENDED check 49, because README.md is in TOOL-dWitnessedBar-41's declared set. That refusal is binding, so README.md was not staged.

(2) The pre-commit hook then failed:
- the memory-hygiene build-index freshness check found the build index stale: memory/LIVE.md, memory/backlog/TOOL.md and memory/builds/dWitnessedBar/README.md. The renderer reads the worktree, and the hook named ten render inputs with unstaged changes, among them 41's .githooks/pre-push and 41's spec. memory/backlog/TOOL.md and README.md are both 41's declared paths.
- The codebase-map gate found memory/map/generated/symbols.json STALE.

(3) Waiting for 41 to land was refused by scratch-guard: a role agent may not poll, and the bounded `sleep 5` loop counted as polling.

The worktree spec for 41 already reads CLOSED, so 41's `git commit` would have taken in whatever sat in the shared index. I saved the pass as a patch and unstaged every path of mine, which leaves only memory/builds/dWitnessedBar/RUN.md staged, with its dispatch rows.

No spec divergence was found. Every claim in the spec checked out against the tree, including the blob-pinned citations 1ecf9aa6 and f499fbac, `check_frozen`, `resolve_shell_argv` and the parser slice.

## Summary

I built TOOL-dWitnessedBar-55 but did not commit it: the hooks cannot pass while unit 41's work is uncommitted in the same worktree (see `why`).

**What is built.** The edits are in the worktree, unstaged. A patch of them is at C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-55.patch. It covers:
- **C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/govkit/steps/inherited_red.py**
  - New `check_policy_assignment`: a line counts only if, after cutting one trailing CR, it begins exactly `<key>=`.
  - `read_value` now reads the way the hook's `read_policy_key` does: lines split on LF, the last assignment wins, cut at the first whitespace before a `#`, trailing spaces and tabs and leading spaces stripped, one pair of quotes removed. The BOM cut and `build_line_re` are gone.
  - New `render_gate_rest`: the `up` deletes only assignments and keeps every other line byte for byte.
  - The witness prints `not an assignment <file>:<line>` for each line matching `(?<!\w)INHERITED_RED\s*=` that is not an assignment, and that does not fail it.
  - The module docstring now states the reader rule.
- **tools/govkit/selftest.py**: `check_inherited_red_step` gains AC1 to AC3 targets and the AC4 parity check. AC4 cuts `read_policy_key` from `.githooks/pre-push`, from its `read_policy_key() {` line to the first column-0 `}`, and runs it under `resolve_shell_argv` bash. A sentinel `K=plain` must read back first, and the check confirms all 11 S4 rows were graded.
- **help/upgrade-steps.md**: the section on where INHERITED_RED's value lives now states the rule, the `up` and the `not an assignment` witness line.
- **The acceptance ledger** memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-55-1-acceptance-ledger.md.
- **Deviation record 552** (memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-55-deviation-552.md, `author-recorded`). It covers two choices the spec left open or that I made differently:
  - what "spells the key" means;
  - putting the new checks inside `check_inherited_red_step` rather than in a second function beside it. A second function would copy that arm's two helpers and add a name the spec's Inventory does not list.
- **The spec status flip to CLOSED**, plus the generator's record rows.

**Checks that ran.** None of these is a gate:
- The naming lexicon passed `check_policy_assignment` and `render_gate_rest`.
- A scratch probe (C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe55.py) stands in for the `govkit selftest` leg:
  - the sentinel read `plain`;
  - all 11 S4 rows plus 3 extra rows gave equal values from the cut hook function and the new `read_value`;
  - over fixtures at `%TEMP%/ir55p`:
    - AC1: `blocks = "every-red"` written, both lines removed.
    - AC2: neither the export-only nor the park-then-empty fixture wrote a `blocks` value.
    - AC3: the file was left as `export INHERITED_RED=park\n` and the witness exited 0 naming `.githooks/gate-env.sh@6834ee4b:1`.
    - A file with CRLF and no final newline kept its other lines byte for byte.
- An inline replay of the base reader (`build_line_re`) read `land` on the indented, spaced, leading-tab and BOM rows, where the hook reads `park`, `park`, `\tland` and nothing. So the new parity arm can go red.
- The AC5 greps: "not an assignment" prints lines 442 and 461 inside the section, and "line out of each file that held one" prints nothing.

**Not run: owed at the close.**
- The legs of §7: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `recall floor arms`, `memory hygiene`, `policy fixtures`, `step-rows-frozen` and `docs`.
- The new arm's RED-first observations in tools/govkit/selftest.py:
  - AC1, by staging a reader that takes the first assignment;
  - AC4, against the base `read_value`;
  - AC3, against the base witness, which prints no `not an assignment` row.
- `gotchas.py --for-diff HEAD~1..HEAD` was not run because there is no commit. I ran `gotchas.py --for-paths` over the three product paths instead and checked the new code against the classes it selected (fixtures that find nothing, a local colliding with an earlier one); nothing needed changing.

**To land it after 41's commit is on HEAD:**
1. Apply the patch, or stage the worktree paths as they are.
2. Declare memory/builds/dWitnessedBar/README.md for unit 55; check 49 refused this while 41 was in flight.
3. Rerun `python tools/memory-tree/gen_build_index.py --write` and `python tools/codebase-map/gen_map.py --write` (memory/LIVE.md, the as-built view and symbols.json are already declared).
4. Stage the regenerated files and commit with `Pass: TOOL-dWitnessedBar-55`.
