# TOOL-dCalibratedLens-12 deviation 122 — rev-1 of TOOL-dCalibratedLens-12's spec revised by the round-1 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-12

- **Departs from:** `TOOL-dCalibratedLens-12@rev-1`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-12's spec at rev-1 as its first pass `59d3d8e57` wrote it, the revision the round-1 spec audit pinned at `31588f5f0`.
- **After:** at `31588f5f0`, rev-2, the round-1 spec audit's disposal fold: §4 gains `### Amendments (round-1 spec audit)`; S1 and S4 open with an `(amended, …)` mark; §9 gains `- rev-2 · 2026-11-02 · §3 §4 §7 S1 S4 · amended at the disposal of the round-1 spec audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec audit)": ids 23, 51 and 39 (`TOOL-dCalibratedLens-30`); §3 gains the hands-off to unit 30.`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-1 spec audit's disposal (`31588f5f0`) folded its findings here, moving rev-1 to rev-2 with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is additive rather than editorial: design or criterion text moved, not only an edge, a spelling, a pin or a §9 line.
- **Evidence:** commit `31588f5f0` (`git diff 31588f5f0~1 31588f5f0 -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-12.md`); the round-1 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md` (the ids its §9 line names); the audit pin `TOOL-dCalibratedLens-12@rev-1` in `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`, added at `31588f5f0`; the departures report's entry 19, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
