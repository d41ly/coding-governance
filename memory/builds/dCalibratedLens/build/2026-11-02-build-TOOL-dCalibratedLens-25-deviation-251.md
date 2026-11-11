# TOOL-dCalibratedLens-25 deviation 251 — the round-1 spec audit promoted a unit for its high H7

**Serves:** deviation TOOL-dCalibratedLens-25

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dCalibratedLens-25`: the `returned` line's units field sits before the agent id, and the format guard's fixtures and its leg's guard follow the fence, so the guard's agent-id test and its self-test fixtures hold.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-1 spec audit, item H7 (finding id 35). This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-1 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-25` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-25.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-1 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-25
- **Caused-by:** TOOL-dCalibratedLens-25
