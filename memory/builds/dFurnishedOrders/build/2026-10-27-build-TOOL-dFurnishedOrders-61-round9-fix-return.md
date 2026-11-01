**Serves:** research TOOL-dFurnishedOrders-61

# Round-9 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-1-7-spec-writer.md`, run direct/a0a0ad078c7caea9b, extracted from its transcript by script.

I fixed R1 in TOOL-dFurnishedOrders-61. The spec-token check still needs to be re-run on the real tree: the scratch-guard hook stopped me from running it, so the fix is not confirmed until you do.

**Unit**
- `TOOL-dFurnishedOrders-61`: amended. It stays `rev-1` with no §9 line, since it is new and uncommitted.

**What changed**
The checker treats a backticked token as a repo path when it contains a `/` and its last segment has a dot (`tools/check-spec-tokens.py:1104-1121`). It tests the raw text before `{prefix}` is resolved, so `{prefix}/roles/kit.toml` showed up as an untracked path. I described the row in words instead, the way unit 48's fix handled `check-wiring.sh`:
- **S7 (around lines 109-110):** "adds the raw row that spells the roles kit's `kit.toml` under the `{prefix}` token, the row whose resolved form is `tools/roles/kit.toml`".
- **AC4 (around lines 371-374):** "the clone's raw `govkit selftest` guard holds the raw row spelling the roles kit's `kit.toml` under the `{prefix}` token, and neither `{prefix}/roles/` nor `{prefix}/`". I rewrapped the next two lines to fit.

The meaning is unchanged: the guard holds the raw row, and the row resolves to `tools/roles/kit.toml`, which `git ls-files --error-unmatch` confirms is tracked. Every backticked `{prefix}` token left in the file is now either `{prefix}` alone or ends in `/`, and the checker skips both forms. I edited nothing else.

**Checks run**
- **Memory hygiene checks 2, 12 and 25:** I ran these in a throwaway clone (made at `8f5d36ad6`) under the scratch path, with every spec in the folder committed there. They exited 0 and nothing named unit 61. The seven `dFurnishedOrders` lines in the output are check 25's "did not grade — READER NOT IN TREE" notes on units 4, 15, 16, 23 and 30; they are informational and were there before. The clone is deleted.
- **Spec-token check:** please run `python tools/check-spec-tokens.py` on the real tree. It should print no line naming a `memory/builds/dFurnishedOrders/spec/` file.

Nothing is committed and no index was rendered. The only file I touched is `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-61.md`. My edits are unstaged on top of the staged copy (`AM`), so stage it again before you commit.
