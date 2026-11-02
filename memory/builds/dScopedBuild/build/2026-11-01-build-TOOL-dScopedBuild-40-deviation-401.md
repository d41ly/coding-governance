# TOOL-dScopedBuild-40 deviation 401 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dScopedBuild-40

- **Departs from:** dScopedBuild [roster]
- **Hand-off:** design-to-spec
- **Before:** dScopedBuild's roster carries fifteen units, `TOOL-dScopedBuild-1` to `TOOL-dScopedBuild-15`, one per clause of its row, beside `TOOL-dScopedBuild-16`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dScopedBuild-40`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md: spec-audit round1 of units 36-39 finding id 24 at HIGH, report item H1.
- **Evidence:** the spec audit, `memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md`; the rescope add row for `TOOL-dScopedBuild-40` in `memory/builds/dScopedBuild/RUN.md`; the unit's spec, `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-40.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dScopedBuild-40
- **Caused-by:** PLAY-dClosedLoop-2
