# TOOL-dCalibratedLens-6 deviation 64 — rev-3 of TOOL-dCalibratedLens-6's spec revised by the round-3 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-6

- **Departs from:** `TOOL-dCalibratedLens-6@rev-3`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-6's spec at rev-3 as `530cadfbd` left it.
- **After:** at `2e6c6e34c`, rev-4, the round-3 spec audit's disposal fold: §4 gains `### Amendments (round-3 spec audit)`; §3's hands-off to `TOOL-dCalibratedLens-38` ends `holds to the newest add (round-2 id 19, round-3 id 15)` where it ended `holds to the oldest add (round-2 id 19)`; §9 gains `- rev-4 · 2026-11-03 · §3 §4 S2 S6 AC7 · amended at the disposal of the round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, §4 "Amendments (round-3 spec audit)": r3 id 11 (`TOOL-dCalibratedLens-43`), the prefix listing and AC7's non-empty assertion; r3 id 15 (`TOOL-dCalibratedLens-48`), the newest add; §3's hands-off to unit 38 names the newest add.`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-3 spec audit's disposal (`2e6c6e34c`) folded its findings here, moving rev-3 to rev-4 with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is additive rather than editorial: design or criterion text moved, not only an edge, a spelling, a pin or a §9 line.
- **Evidence:** commit `2e6c6e34c` (`git diff 2e6c6e34c~1 2e6c6e34c -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-6.md`); the round-3 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md` (the ids its §9 line names); the departures report's entry 62, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
