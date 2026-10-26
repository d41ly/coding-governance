# TOOL-dGroundRules-48 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-48

No merge bar, gate leg or self-test suite ran in this pass, and the unit writes no product file. AC1
ran from this worktree's root at `dd148fbbb`. AC2 ran in a clone made as `SCRATCH` makes it, under
`%TEMP%/gr48` and checked out at `dd148fbbb`, with `HELP_MOVED` staged there by moving the deferral
line from the `## Install` section to under `## Example`; the clone was removed after. Owed at the
close: the `memory hygiene` leg over the built tree. This unit declares no `New arm:` line.

**Evidences:** TOOL-dGroundRules-48
- AC1 — `INSTALL_LINES` of `TOOL-dGroundRules-41` §6 printed `1` on the built tree; `help/policy.md` is tracked, and its deferral line sits at line 103 under `## Install` (line 93), ahead of the next heading at line 114.
- AC2 — after `SCRATCH` and `HELP_MOVED` in the clone, `INSTALL_LINES` printed `0` from the clone's root, while a whole-page `grep -c "mirror deferred" help/policy.md` there still printed `1`, so the count is section-bounded and the first criterion can fail.
