# TOOL-dBoundRoles-58 deviation 581 — the round-3 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-58

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-58`, from the round-3 spec audit: spec-audit round1 of units 45-51 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 2 39 3 4 37 46 5 8 15 32 21 33 11 17 34 22 23 24 25 31 42 45 47 48 (items M1-M18) and LOW ids 9 10 12 38 19 26 27 28 35 49 50 (items L1-L10).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-3 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-58` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-58
- **Caused-by:** PLAY-dClosedLoop-2
