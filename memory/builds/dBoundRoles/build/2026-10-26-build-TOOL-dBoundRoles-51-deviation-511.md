# TOOL-dBoundRoles-51 deviation 511 — the round-2 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-51

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-51`, from the round-2 spec audit: spec-audit round1 of units 37-44 minors batched, records-and-Skills half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 2 3 13 31 (items M1 M2 M7 M14) and LOW ids 7 8 14 20 (items L2 L3 L5).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-51` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-51.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-51
- **Caused-by:** PLAY-dClosedLoop-2
