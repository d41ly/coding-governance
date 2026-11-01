# TOOL-dBoundRoles-50 deviation 501 — the round-2 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-50

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-50`, from the round-2 spec audit: spec-audit round1 of units 37-44 minors batched, roles-code half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 4 5 10 11 18 19 25 26 27 28 29 30 33 35 36 37 38 (items M3 M4 M5 M6 M8 M9 M10 M11 M12 M13 M15 M16 M17 M18) and LOW ids 6 12 15 21 22 39 40 (items L1 L4 L6 L7 L8 L9 L10).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-50` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-50
- **Caused-by:** PLAY-dClosedLoop-2
