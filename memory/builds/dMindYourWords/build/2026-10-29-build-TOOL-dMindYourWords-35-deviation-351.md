# TOOL-dMindYourWords-35 deviation 351 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dMindYourWords-35

- **Departs from:** dMindYourWords [roster]
- **Hand-off:** design-to-spec
- **Before:** dMindYourWords's roster carries seventeen units, `TOOL-dMindYourWords-1` to `TOOL-dMindYourWords-17`, one per clause of its row, beside `TOOL-dMindYourWords-18`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dMindYourWords-35`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md id 30 (HIGH, item H4): the drain edit --measure > <home> truncates the home before --measure reads the rows it carries
- **Evidence:** the spec audit, `memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`; the rescope add row for `TOOL-dMindYourWords-35` in `memory/builds/dMindYourWords/RUN.md`; the unit's spec, `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-35.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dMindYourWords-35
- **Caused-by:** PLAY-dClosedLoop-2
