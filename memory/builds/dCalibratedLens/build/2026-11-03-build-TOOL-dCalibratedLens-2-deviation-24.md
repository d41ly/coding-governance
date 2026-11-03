# TOOL-dCalibratedLens-2 deviation 24 — rev-3 of TOOL-dCalibratedLens-2's spec revised by the round-3 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-2

- **Departs from:** `TOOL-dCalibratedLens-2@rev-3`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-2's spec at rev-3 as `530cadfbd` left it.
- **After:** at `2e6c6e34c`, rev-4, the round-3 spec audit's disposal fold: §3's `- **hands-off** `TOOL-dCalibratedLens-41` — the `loop-review selftest` row of S11, whose guard that unit widens to the files the loop plants run (round-2 id 13)` reads `- **hands-off** `TOOL-dCalibratedLens-46` — the `loop-review selftest` row of S11, whose guard that unit widens, in the row's declaration, to the files the loop plants run (round-2 id 13, round-3 id 22)`, and no other line moves; §9 gains `- rev-4 · 2026-11-03 · §3 · amended at the disposal of the round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: §3's hands-off of the row's guard names `TOOL-dCalibratedLens-46` in place of unit 41, which takes the widening into the leg's declaration (r3 id 22).`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-3 spec audit's disposal (`2e6c6e34c`) folded its findings here, moving rev-3 to rev-4 with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is editorial: only a §3 edge and a §9 line moved, and no criterion or design text changed.
- **Evidence:** commit `2e6c6e34c` (`git diff 2e6c6e34c~1 2e6c6e34c -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-2.md`); the round-3 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md` (the ids its §9 line names); the departures report's entry 34, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
