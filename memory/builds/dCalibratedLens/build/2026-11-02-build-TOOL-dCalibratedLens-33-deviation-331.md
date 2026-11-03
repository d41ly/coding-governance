# TOOL-dCalibratedLens-33 deviation 331 — the round-2 spec audit promoted a unit for its high H1

**Serves:** deviation TOOL-dCalibratedLens-33

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, and `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-33`: the three Loop Review homes are observed disjoint by listing each home, never inferred from the record-kind check, so unit 19's disjointness claim is observed itself and a path two homes list goes red.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-2 spec audit, item H1 (finding id 2, shared with ids 11 and 26), and repairs `TOOL-dCalibratedLens-19`. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-2 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-33` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-33.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-2 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-33
- **Caused-by:** TOOL-dCalibratedLens-33
