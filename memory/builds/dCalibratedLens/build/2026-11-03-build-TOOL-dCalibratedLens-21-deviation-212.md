# TOOL-dCalibratedLens-21 deviation 212 — rev-1 of TOOL-dCalibratedLens-21's spec revised by the round-3 disposal, recorded after the fact

**Serves:** deviation TOOL-dCalibratedLens-21

- **Departs from:** `TOOL-dCalibratedLens-21@rev-1`
- **Hand-off:** spec-revised
- **Before:** TOOL-dCalibratedLens-21's spec as the round-2 spec audit pinned it at rev-1 and its own disposal left it at rev-2 (`530cadfbd`).
- **After:** at `2e6c6e34c`, rev-3, the round-3 spec audit's disposal fold: S4's `multi-line answer cannot exit the walk. Observed by AC4.` reads `multi-line answer cannot exit the walk. For a list answer the refusal is per entry: the entry carrying the break is written `<name>: unread · refused value` in its place and the other entries as answered (round-3 id 32, unit 3's r3 id-32 bullet, held by `TOOL-dCalibratedLens-40`'s case). Observed by AC4.`; §9 gains `- rev-3 · 2026-11-03 · S4 · amended at the disposal of the round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`: the refusal's scope for a list answer is the entry (id 32).`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit, and its disposal folds into this spec the text its promoted siblings own; the round-3 spec audit's disposal (`2e6c6e34c`) folded its findings here, moving rev-2 to rev-3, past the rev-1 the round-2 audit pinned, with no audit of the move; no code has started, every unit being DEFERRED to the build run; Risk is additive rather than editorial: design or criterion text moved, not only an edge, a spelling, a pin or a §9 line.
- **Evidence:** commit `2e6c6e34c` (`git diff 2e6c6e34c~1 2e6c6e34c -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-21.md`); the round-3 spec audit whose disposal made the fold, `memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md` (the ids its §9 line names); the audit pin `TOOL-dCalibratedLens-21@rev-1` in `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`, added at `530cadfbd`; the departures report's entry 36, quoted in `memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
