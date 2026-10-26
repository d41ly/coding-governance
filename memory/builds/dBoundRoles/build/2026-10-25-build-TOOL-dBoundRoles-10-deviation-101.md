# TOOL-dBoundRoles-10 deviation 101 — `state-reads-only` enforced on the search tools only

**Serves:** deviation TOOL-dBoundRoles-10

- **Departs from:** cl-dClosedLoop-0175@79a1c7d0
- **Hand-off:** design-to-spec
- **Before:** `driver.reads`, whose default `state-reads-only` lets the main session read only cheap state: `next`, a record it was handed, a short git state command (v2:1179; `roles.md:377-378`).
- **After:** under `state-reads-only` the main loop's `Grep` and `Glob` are refused and its `Read` is admitted; under `none-scout-only` all three are refused; the main loop's Bash reads are not seen by the arm.
- **Cause:** design defect
- **Reason:** no record of what the driver was handed exists at base, so a `Read` restricted to handed records has nothing to join against; a typed list of readable paths would refuse BUILD-METHOD M7's reads of the method and of the current spec, a governance carrier's procedure (TOOL-dBoundRoles-10 §8 F1). The driver's binding record that names what it was handed is dWellOiledMachine's.
- **Evidence:** `tools/hooks/scratch-guard.fragment.json` matches no read tool at base; `memory/guides/BUILD-METHOD.md` M7 steps 3 and 4 read the method and the current spec whole; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:535` places the session binding record in Runtime.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0175@79a1c7d0
- **Caused-by:** PLAY-dClosedLoop-4
