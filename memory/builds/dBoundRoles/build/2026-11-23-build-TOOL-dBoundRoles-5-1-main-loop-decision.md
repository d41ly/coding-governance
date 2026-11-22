**Serves:** journal TOOL-dBoundRoles-5

# TOOL-dBoundRoles-5 — the main loop's decision over the first builder's divergence

Run `wf_8d0b1045-394` built the unit from rev-6 at `51870e685` and committed nothing. The pre-commit hook refused its
commit for a path outside the declared write set. Its staged change is kept as a patch in the session scratchpad,
which applies cleanly at `51870e685`. No spec writer can be spawned directly on this run: the session's spawn guard
predates TOOL-dBoundRoles-17's `item=`. So the main loop decides each returned item by M3 as a delegated resolution,
and the next builder builds them under the one deviation record its brief names. widens: none · relaxes: none.

1. `memory/map/features/roles.md` joins the write set. The new `SubagentStop` launcher `tools/roles/return-check.sh`
   enters the codebase map's `harness-hooks` inventory, so the roles dossier claims that key, and the map generator's
   output rides the same commit.
2. `tools/roles/render_agents.py` and `tools/workflows/unattended-build.test.sh` join the write set. They are the
   files the spec's two `New arm:` lines name, so the plants of §4's inventory are written in them.
3. `tools/workflows/tier2-review.test.sh` joins the write set. Its `checkStageOpts` arm counts the template's
   `agent(` calls and their stage options. It learns `runWithRetries(prompt, opts)` as a call that carries the
   options it is handed, so each stage the helper wraps is still counted once with its own options. The planted
   probe check reads the same way. The arm's population and verdict are unchanged.
4. The fragment's reach before TOOL-dBoundRoles-39. Once merged into `.claude/settings.json`, the return check sees
   every typed stop, harness stages included, until unit 39 builds its route test at order 16. This session's hooks
   run from the primary tree, so no stop of this run is graded before landing, and unit 39 lands with this run.
   The merge stays in this unit, as S5 states.
