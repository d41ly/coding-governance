**Serves:** research TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52

# Round-6 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-1-5-spec-writer.md`, run direct/ab45740eb34796610, extracted from its transcript by script.

I fixed both items in specs 50 and 52. Nothing outside `memory/builds/dFurnishedOrders/spec/` changed, nothing is committed, and no index was rendered.

**R1 · foreign ids leading table cells (check 13).** The "reach at authoring" table in `TOOL-dFurnishedOrders-50` (lines 138-143) now leads each of its four rows with the reached spec's path instead of its unit id. The header now reads `reached spec`. The four paths I checked exist:
- `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`
- `memory/builds/aScoutedSeam/spec/2026-10-11-spec-DEPL-aScoutedSeam-1.md`
- `memory/builds/aScoutedSeam/spec/2026-10-11-spec-KICK-aScoutedSeam-1.md`
- `memory/builds/aScoutedSeam/spec/2026-10-11-spec-TOOL-aScoutedSeam-3.md`

The table-row pattern check 13 uses (`A_TABLE`, `tools/memory-recall/extract.py:187`) only reads an id that opens the first cell. A path starting `memory/` no longer matches. I grepped 50, 51 and 52 for all four record-start patterns (heading, bold list item, table row, dash row) and found no other foreign id in that position. Only the spec headings matched, each naming its own unit.

**R2 · missing codebase-map legs in §7 (`[guards]`).** I added `codebase-map kit selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e` to the §7 leg line of both specs, around the existing `codebase-map coverage + freshness`. They are spelled exactly as in `tools/gate-legs.json:804`, `:819` and `:844`. In `-50` this is line 244 and in `-52` line 384. Units 50 and 52 stay `rev-1` with no §9 line, since all three units are new and uncommitted.

**Checks:**
- **Hygiene checks 2, 12 and 25:** passed (exit 0, "ran checks 2 12 25") in a throwaway clone with every spec in the folder committed. The only output was check-25 notices about other specs and older dFurnishedOrders units, none about 50 to 52. I deleted the clone afterwards.
- **Anchor probe:** I ran the four patterns from `extract.py` over specs 50 to 52. It found no id from another build in a position check 13 counts as defined.
- **Spec-token check:** not run. scratch-guard blocks my role from it, so it is still for you to run.

**Still for you to run on the real tree:** `python tools/check-spec-tokens.py` (should print no line naming a `memory/builds/dFurnishedOrders/spec/` file) and the whole hygiene gate (should print no check-13 line naming dFurnishedOrders).

Files changed:
- `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-50.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-52.md`
