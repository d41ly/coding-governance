# TOOL-dCalibratedLens-31 deviation 311 — the round-2 spec audit promoted a unit for its blocker B1

**Serves:** deviation TOOL-dCalibratedLens-31

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, and `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-31`: the roles kit's shape renderer renders a shape's optional `[ · …]` group as its content when its fields are held and as nothing when they are not, and an arm holds every fenced shape's rendered line to the format guard's own regex, so no printed `returned` line carries a literal bracket.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER to a unit whose mechanism closes it; this unit closes the one confirmed blocker of the round-2 spec audit, item B1 (finding id 30), and repairs `TOOL-dCalibratedLens-25`. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-2 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-31` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-31.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-2 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-31
- **Caused-by:** TOOL-dCalibratedLens-31
