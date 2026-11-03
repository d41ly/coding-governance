# TOOL-dCalibratedLens-46 deviation 461 — the round-3 spec audit promoted a unit for its high H4

**Serves:** deviation TOOL-dCalibratedLens-46

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions, and `TOOL-dCalibratedLens-31` to `TOOL-dCalibratedLens-41`, the round-2 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-46`: the guards of `loop measure fixtures`, `loop-review selftest` and `tier2-review self-test` are widened in the declaration each leg lives in under whichever state the build run finds, and rendered where `tools/gate-legs.json` is a render, so the widening survives TOOL-dWitnessedBar-11's factory.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-3 spec audit, item H4 (finding id 22), and repairs `TOOL-dCalibratedLens-41`. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-46` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-03-spec-TOOL-dCalibratedLens-46.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-3 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-46
- **Caused-by:** TOOL-dCalibratedLens-46
