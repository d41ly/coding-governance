# TOOL-dCalibratedLens-1 deviation 13 — rev-2 of TOOL-dCalibratedLens-1's spec revised by the round-2 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-1

- **Departs from:** `TOOL-dCalibratedLens-1@rev-2`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-1's spec at rev-2 as `31588f5f0` left it.
- **After:** at `530cadfbd`, rev-3, the round-2 spec audit's disposal fold: §4 gains `### Amendments (round-2 spec audit)`; AC3 opens with an `(amended, …)` mark; §9 gains `- rev-3 · 2026-11-02 · §4 AC3 · amended at the disposal of the round-2 spec audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 id 15 (`TOOL-dCalibratedLens-41`), AC3's text carrying the payload.`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-2 spec audit's disposal (`530cadfbd`) folded its findings here, moving rev-2 to rev-3 with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is additive rather than editorial: design or criterion text moved, not only an edge, a spelling, a pin or a §9 line.
- **Evidence:** commit `530cadfbd` (`git diff 530cadfbd~1 530cadfbd -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md`); the round-2 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md` (the ids its §9 line names); the departures report's entry 9, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
