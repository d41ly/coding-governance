# TOOL-dLinkedLibrary-75 deviation 751 — the round-4 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dLinkedLibrary-75

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-74`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-75`, the reuse-tag sweep reads a hyphenated feature name, and shows its red on a planted tag.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of units 65 to 74 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) finding id 25 at HIGH, report item H1 (ids 12 and 41 bind the same defect at MEDIUM, item M3, batched in TOOL-dLinkedLibrary-80); repairs TOOL-dLinkedLibrary-74. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-4 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-75` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-75.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-75
- **Caused-by:** PLAY-dClosedLoop-2
