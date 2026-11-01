# TOOL-dBoundRoles-4 deviation 41 — the prompt writer composes direct spawns' tasks, harness stages excepted

**Serves:** deviation TOOL-dBoundRoles-4

- **Departs from:** cl-dClosedLoop-0169@cdc1b7f9
- **Hand-off:** design-to-spec
- **Before:** the prompt writer composing every role's task from the driver's details.
- **After:** the prompt writer composes the task of every role spawned directly through `Agent`, its own spawn excepted, and rule 6 refuses an unframed direct spawn while `prompts.author` is `prompt-writer`; a harness stage's prompt is still composed by its harness script.
- **Cause:** design defect
- **Reason:** a harness stage's prompt is assembled inside the workflow script, which has no rendered work order to frame and no tree to render one from; a prompt writer per harness stage doubles every fan and needs the executor that renders each harness item's work order, which is dWellOiledMachine's (TOOL-dBoundRoles-4 §8 F2). The prompt writer's own task is the driver's details rendered mechanically, since framing it would regress without end (§8 F3).
- **Evidence:** `tools/workflows/unattended-unit.js:257-323` composes the builder's prompt in the script; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:16-28` has the executor wrap the prompt writer's output in the work order.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0169@cdc1b7f9
- **Caused-by:** PLAY-dClosedLoop-4
