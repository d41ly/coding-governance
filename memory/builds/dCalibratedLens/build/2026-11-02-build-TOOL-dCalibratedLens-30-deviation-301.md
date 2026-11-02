# TOOL-dCalibratedLens-30 deviation 301 — the round-1 spec audit promoted its minors into one batch unit

**Serves:** deviation TOOL-dCalibratedLens-30

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dCalibratedLens-30`: the round-1 audit's 41 minors are batched into one unit, each correction carried by the sibling spec it lands on, and six arms hold the classes no sibling owns.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, and batches a review's mediums and lows into one unit, the one exception to one mechanism per spec; this unit carries the round-1 spec audit's minors batch, 30 MEDIUM and 11 LOW, finding ids 5 32 6 7 8 9 10 46 17 18 25 26 27 28 29 30 31 33 37 38 39 40 41 42 43 44 45 51 53 54 11 12 13 14 20 21 22 23 24 34 47. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-1 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-30` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-30.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-1 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-30
- **Caused-by:** TOOL-dCalibratedLens-30
