**Serves:** research TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58

# Round-3 fix pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-5-spec-writer.md`, run direct/a7916d3046ca9d311, extracted from its transcript by script.

All five reds in the brief are fixed in their named specs and nothing else changed. Each spec stays at `rev-1`.

**Files changed:**
- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-53.md`: P1. S1 now has a `**Readers:**` clause.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-55.md`: P1. S2 now has a `**Readers:**` clause.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-58.md`: P1 for S21 and S30, which now have `**Readers:**` clauses, and P2 for S19.

**Readers found with `git grep`:**
- **53 S1 and 58 S21:** neither retires anything. The check flags them because of the words "drop" and "deletes". Following the brief, I still wrote both halves:
  - The name half cites the readers that already do the same strip: `tools/roles/handoff.py:1025` for 53, and `tools/roles/roles_lib.py:252` and `tools/hooks/agent-cap.js:2051` for 58.
  - The value half is `NO VALUE READERS`: the stripped character is removed only from the check's own copy of each line.
- **55 S2:** `derive_overlay_expected` is spelled in no product file today. Unit 54 creates it in `tools/govkit/selftest.py` when it is built.
  - By name, the clause cites the specs that spell it: unit 54's spec, 49:65 and 19:99.
  - By value, it names `tools/govkit/selftest.py`, where S3's compare is the one reader and is deleted in the same pass.
- **58 S30:** the end-of-walk clause is spelled only at `2026-10-26-spec-TOOL-dBoundRoles-48.md:40-41`. By value, it names `tools/roles/handoff.py`, whose `render_handoff` collects every refusal line into `refusals`.
- **58 S19 (P2):** unit 39's spec never spells `resolve_subagent_dir`. The file that does is unit 50's spec: its S21 creates the helper and assigns unit 39's route test to it.
  - The name half now cites `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md` and `tools/roles/handoff.py`.
  - It adds `READER NOT IN TREE` for the route test itself, because that test is only built in unit 39's pass.

**Checks:** I copied the working tree into a throwaway clone, ran `gen_build_index.py --write` and committed there. `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` then exited 0. Its output had no lines about dBoundRoles, so no name I cited was left ungraded. I then deleted the clone. Nothing is committed, and no index was regenerated in the worktree.
