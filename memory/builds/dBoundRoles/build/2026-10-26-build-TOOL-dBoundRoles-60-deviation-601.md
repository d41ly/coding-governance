# TOOL-dBoundRoles-60 deviation 601 — the round-4 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-60

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-60`, from the round-4 spec audit: spec-audit round1 of units 52-58 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 1 12 24 2 16 3 4 14 27 5 13 7 36 9 29 15 22 25 28 30 33 34 35 37 (items M1-M16) and LOW ids 6 19 8 11 17 31 18 20 23 26 32 38 39 (items L1-L11).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-4 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-60` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-60
- **Caused-by:** PLAY-dClosedLoop-2
