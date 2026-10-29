# TOOL-dMindYourWords-40 deviation 401 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dMindYourWords-40

- **Departs from:** dMindYourWords [roster]
- **Hand-off:** design-to-spec
- **Before:** dMindYourWords's roster carries seventeen units, `TOOL-dMindYourWords-1` to `TOOL-dMindYourWords-17`, one per clause of its row, beside `TOOL-dMindYourWords-18`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dMindYourWords-40`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md id 6 (HIGH, item H4, shared with id 15): the graft-file arms of units 30 to 32 inherit GIT_GRAFT_FILE=/dev/null from the unattended close bar, so cutting the pin leaves them green
- **Evidence:** the spec audit, `memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`; the rescope add row for `TOOL-dMindYourWords-40` in `memory/builds/dMindYourWords/RUN.md`; the unit's spec, `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-40.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dMindYourWords-40
- **Caused-by:** PLAY-dClosedLoop-2
