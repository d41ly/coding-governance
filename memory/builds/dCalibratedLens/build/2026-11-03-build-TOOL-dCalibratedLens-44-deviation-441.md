# TOOL-dCalibratedLens-44 deviation 441 — the round-3 spec audit promoted a unit for its high H3

**Serves:** deviation TOOL-dCalibratedLens-44

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions, and `TOOL-dCalibratedLens-31` to `TOOL-dCalibratedLens-41`, the round-2 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-44`: the shape arm holds every line it renders free of a literal bracket outside a markdown link, the assertion the format guard's lazy field rule cannot make, so a `SPEC` line that leaks its group's brackets goes red.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-3 spec audit, item H3 (finding id 12, shared with id 27), and repairs `TOOL-dCalibratedLens-31`. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-44` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-03-spec-TOOL-dCalibratedLens-44.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-3 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-44
- **Caused-by:** TOOL-dCalibratedLens-44
