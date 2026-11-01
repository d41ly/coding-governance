# TOOL-dBoundRoles-7 deviation 71 — a role agent with no allowance held to its write class

**Serves:** deviation TOOL-dBoundRoles-7

- **Departs from:** cl-dClosedLoop-0172@b73b4974
- **Hand-off:** design-to-spec
- **Before:** shell writes held to the allowance.
- **After:** a role agent's shell write is held to the verdict an `Edit` of the same target meets, its write class through `checkRouted`, and additionally to its work order's `allowance` where the agent's spawned prompt carries one; an agent whose prompt carries no allowance block, every harness stage among them, is held to its class alone, with one witness line.
- **Cause:** design defect
- **Reason:** no harness stage prompt carries an allowance at base, since the harness scripts compose those prompts and the executor that renders a work order for each harness item is dWellOiledMachine's; refusing every repository shell write such an agent makes would stop every harness pass, and admitting them is the escape the clause closes. The class is the ceiling every allowance narrows, so holding to it is the strictest verdict the tree can derive for such an agent (TOOL-dBoundRoles-7 §8 F3).
- **Evidence:** `tools/workflows/unattended-unit.js:262-264` (the `PROMPT` at `:257-323`) hands the builder its brief and spec by path with no allowance block; I12 in `memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md:201-205` defines the allowance as a work-order block TOOL-dBoundRoles-3 renders; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:530-531` binds act shells in Runtime.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0172@b73b4974
- **Caused-by:** PLAY-dClosedLoop-4
