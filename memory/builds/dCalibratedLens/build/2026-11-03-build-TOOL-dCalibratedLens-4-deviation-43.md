# TOOL-dCalibratedLens-4 deviation 43 — rev-2 of TOOL-dCalibratedLens-4's spec revised by the round-2 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-4

- **Departs from:** `TOOL-dCalibratedLens-4@rev-2`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-4's spec at rev-2 as `31588f5f0` left it.
- **After:** at `530cadfbd`, rev-3, the round-2 spec audit's disposal fold: §3 gains `- **hands-off** `TOOL-dCalibratedLens-41` — the `loop measure fixtures` row of S9, whose guard that unit widens to the files the measure plants run (round-2 id 13)`, and no other line moves; §9 gains `- rev-3 · 2026-11-02 · §3 · amended at the disposal of the round-2 spec audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: §3 gains the hands-off to unit 41, which widens the `loop measure fixtures` guard (r2 id 13).`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-2 spec audit's disposal (`530cadfbd`) folded its findings here, moving rev-2 to rev-3 with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is editorial: only a §3 edge and a §9 line moved, and no criterion or design text changed.
- **Evidence:** commit `530cadfbd` (`git diff 530cadfbd~1 530cadfbd -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-4.md`); the round-2 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md` (the ids its §9 line names); the departures report's entry 48, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
