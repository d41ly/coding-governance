# TOOL-dBoundRoles-10 deviation 102 — `roles.no-spawn = executor-role-session` refuses the stand-in until the executor lands

**Serves:** deviation TOOL-dBoundRoles-10

- **Departs from:** cl-dClosedLoop-0175@79a1c7d0
- **Hand-off:** design-to-spec
- **Before:** `roles.no-spawn`, whose default `executor-role-session` has the executor start a role session for an item no agent can take (v2:1182; `roles.md:385-389`).
- **After:** `driver.reads`, under whose `state-reads-only` the main loop's `Grep` and `Glob` are refused and its `Read` admitted, and under whose `none-scout-only` all three are refused, the main loop's Bash reads unseen by the arm; `prompts.author`; and `roles.no-spawn`, under whose `executor-role-session` this build refuses `handoff.py render --stand-in`, naming the route that is always open, a role spawned through `Agent` or a listed harness, and naming dWellOiledMachine as the build whose executor starts the role session.
- **Cause:** external
- **Reason:** the executor is dWellOiledMachine's and does not exist at base; admitting the stand-in under this value would do the inline work RL-8 asked to eliminate, and starting a session from the renderer would build the executor here (TOOL-dBoundRoles-10 §8 F3).
- **Evidence:** scout B's row for cl-0175 (`memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md:27`, "`executor-role-session` has no seam, since act sessions are Runtime's"); the owner's RL-8 answer (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md:368-373`).
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0175@79a1c7d0
- **Caused-by:** PLAY-dClosedLoop-4
- **Supersedes:** 2026-10-25-build-TOOL-dBoundRoles-10-deviation-101
