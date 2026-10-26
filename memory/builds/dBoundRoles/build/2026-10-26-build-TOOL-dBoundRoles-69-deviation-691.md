# TOOL-dBoundRoles-69 deviation 691 — the round-8 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-69

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-69`, from the round-8 spec audit: spec-audit round1 of units 65 and 66 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 2 13 3 7 21 8 22 12 16 15 6 23 19 (items M1-M8) and LOW ids 5 9 11 17 18 (items L1-L5).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, left unaudited by the owner's stop after round 8, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-8 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-69` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-69.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-69
- **Caused-by:** PLAY-dClosedLoop-2
