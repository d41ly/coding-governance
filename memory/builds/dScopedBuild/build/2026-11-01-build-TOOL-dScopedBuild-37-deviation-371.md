# TOOL-dScopedBuild-37 deviation 371 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dScopedBuild-37

- **Departs from:** dScopedBuild [roster]
- **Hand-off:** design-to-spec
- **Before:** dScopedBuild's roster carries fifteen units, `TOOL-dScopedBuild-1` to `TOOL-dScopedBuild-15`, one per clause of its row, beside `TOOL-dScopedBuild-16`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dScopedBuild-37`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md: spec-audit round1 of units 25-35 finding id 22 at HIGH, report item H2.
- **Evidence:** the spec audit, `memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`; the rescope add row for `TOOL-dScopedBuild-37` in `memory/builds/dScopedBuild/RUN.md`; the unit's spec, `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-37.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dScopedBuild-37
- **Caused-by:** PLAY-dClosedLoop-2
