# TOOL-dScopedBuild-39 deviation 391 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dScopedBuild-39

- **Departs from:** dScopedBuild [roster]
- **Hand-off:** design-to-spec
- **Before:** dScopedBuild's roster carries fifteen units, `TOOL-dScopedBuild-1` to `TOOL-dScopedBuild-15`, one per clause of its row, beside `TOOL-dScopedBuild-16`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dScopedBuild-39`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md: spec-audit round1 of units 25-35 minors batch, MEDIUM ids 1 2 3 4 5 6 7 12 13 14 15 23 27 28 30 31 and LOW ids 8 9 10 16 17 18 19 20 21 24 25 29 32.
- **Evidence:** the spec audit, `memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`; the rescope add row for `TOOL-dScopedBuild-39` in `memory/builds/dScopedBuild/RUN.md`; the unit's spec, `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-39.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dScopedBuild-39
- **Caused-by:** PLAY-dClosedLoop-2
