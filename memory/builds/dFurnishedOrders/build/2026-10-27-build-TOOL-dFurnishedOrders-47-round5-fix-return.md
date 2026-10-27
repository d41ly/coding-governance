**Serves:** research TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49

# Round-5 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-1-4-spec-writer.md`, run direct/a4f79838588198335, extracted from its transcript by script.

I fixed all three items, each in the spec the brief names, and edited nothing outside `memory/builds/dFurnishedOrders/spec/`. Units 47 to 49 stay `rev-1` with no §9 line. I committed nothing and rendered no index.

**Results**
- **Hygiene gate (checks 2, 12, 25):** in a throwaway clone with every spec of the folder committed, it exited 0, printed no FAILED line, and no line names units 47 to 49.
  - My first clone run failed check 2, but only because the staged review record was not in the clone yet. Once I copied the folder's uncommitted records in, it passed. Nothing in the specs needed changing for that.
- **Spec-token check:** my role can't run it; the hook blocked it. You still need to re-run `python tools/check-spec-tokens.py`.
  - I did probe it partway: I loaded the checker's own `BAR` and `check_path_shaped` and applied them to the §6 criteria of all three specs. The only token it flagged is `.claude/hooks/agent-cap.js` in unit 48 AC9. That path is waived at `memory/project/spec-token-waivers.txt:29`, so it is not a hit.

**R1 · hygiene check 25.** None of the four flagged items actually retires a name. Each one tripped the check because a verb like "delete" or "drop" sat next to a backticked identifier. Following the brief's rule for that case, I reworded them instead of adding `**Readers:**` clauses:
- **Unit 47 S2:** "a problem that dropped a kit's rows" is now "lost".
- **Unit 48 S6:** "deletes each `GIT_ENV_LEAKS` name from `os.environ`" is now "unsets each … name in `os.environ`". This is a runtime action, as the §4 sketch's `os.environ.pop` shows.
- **Unit 48 S11:** the three fixture steps are now described as the cases they produce ("a receipt copy holding no engine row…", "a re-apply whose `deploy.toml` carries no `kit.memory-recall.kit` line…", "a receipt copy holding no row…"). The expected clause for each is unchanged.
- **Unit 48 S23:** "deletes `tools/govkit/__pycache__`…" is now "erases …".

**R2 · unit 48 paths.**
- **AC3:** the two fixture paths are now `<target>/a/govkit/registry.toml` and `<target>/b/govkit/registry.toml`.
- **AC6:** the other two are now described in words: "the exact row S18 adds for the flat source `tools/check-wiring.sh`" and "a `kit.toml` in a new `scratch-kit` directory under `{prefix}`". `tools/check-wiring.sh` is tracked.

**R3 · unit 49 AC2.** The criterion still observes the recorded `dispatch` row in `RUN.md` directly. It now names the file as "the `.test.sh` sibling of `tools/lib/resolve-python.sh` that unit 46 §7 places AC9's arm in", and says it runs no suite.

**Decision for you:** I did not add a `New arm:` line for `tools/lib/resolve-python.test.sh` to unit 49's §7.
- **Why:** that suite is unit 46's arm, and unit 49 does not write it. Declaring it there would claim a RED-then-GREEN arm this unit never stages, and would add a path outside unit 49's Files touched.
- **Current state:** unit 49's existing `New arm:` line for `tools/roles/adopt-roles.test.sh` is unchanged.
- **If you add it anyway:** unit 49 would need to take on that file and stage its own RED-then-GREEN run of it.

Files edited:
- `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-47.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-48.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-49.md`
