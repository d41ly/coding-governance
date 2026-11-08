# TOOL-dCalibratedLens-48 deviation 481 — the round-3 spec audit promoted its minors into one batch unit

**Serves:** deviation TOOL-dCalibratedLens-48

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions, and `TOOL-dCalibratedLens-31` to `TOOL-dCalibratedLens-41`, the round-2 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-48`: the round-3 audit's 25 minors are batched into one unit, each correction carried by the sibling spec it lands on, units 46 and 47 among them in their rev-1 text.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, and batches a review's mediums and lows into one unit, the one exception to one mechanism per spec; this unit carries the round-3 spec audit's minors batch, 16 MEDIUM and 9 LOW, finding ids 2 3 4 29 5 6 8 13 14 19 15 20 24 28 31 32 7 16 26 9 10 17 18 21 33, and repairs no unit in particular. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-48` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-03-spec-TOOL-dCalibratedLens-48.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-3 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-48
- **Caused-by:** TOOL-dCalibratedLens-48
