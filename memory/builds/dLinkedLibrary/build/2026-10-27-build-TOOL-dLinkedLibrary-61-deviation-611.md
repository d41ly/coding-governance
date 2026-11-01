# TOOL-dLinkedLibrary-61 deviation 611 — the round-2 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dLinkedLibrary-61

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the round-1 spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-53`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-61`, `--observe` kills the process tree at its bound and routes each run's output to a file.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of units 37 to 53 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) finding id 24 at HIGH, report item H5; repairs TOOL-dLinkedLibrary-49. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-61` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-61
- **Caused-by:** PLAY-dClosedLoop-2
