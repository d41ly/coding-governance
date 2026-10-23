# TOOL-dFairHearing-1 deviation 19 — the round-2 spec audit's disposal folded a hands-off edge into the audited spec

**Serves:** deviation TOOL-dFairHearing-1

- **Departs from:** `TOOL-dFairHearing-1@rev-2`
- **Hand-off:** spec-revised
- **Before:** TOOL-dFairHearing-1's spec as the round-1 spec audit read it at rev-2 and its own disposal left it at rev-3 (`c993af496`): §3 holds no hands-off edge to TOOL-dFairHearing-25, and replay 1's two design-audit runs, scored and verdicted, are answered by this unit's AC4, AC5 and AC9.
- **After:** at `32afb3770`, rev-4: §3 gains `- **hands-off** TOOL-dFairHearing-25 — finding id 1 (item H1) of the spec audit of units 20 to 23: replay 1's two design-audit runs, scored and verdicted on unit 23's corrected contract (its S1 to S6); this unit's AC4, AC5 and AC9's replay-1 half are superseded by its AC1 to AC5 and AC7`, and §9 the line `rev-4 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-25, which runs replay 1 after unit 23's corrections and supersedes AC4, AC5 and AC9's replay-1 half.`; no criterion's text changed.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes each confirmed finding at a review's exit. The round-2 spec audit's high H1 (id 1) found unit 23 correcting the replay contract after unit 1 has already run replay 1 on it, so its disposal promoted TOOL-dFairHearing-25 to run replay 1 after unit 23 and folded the hands-off edge here, moving the spec audited at rev-2 with no audit of the move. Risk is additive rather than editorial: only an edge and a §9 line moved, but the edge hands three of this unit's criteria (AC4, AC5, AC9's replay-1 half) to unit 25.
- **Evidence:** commit `32afb3770` (`git diff 32afb3770~1 32afb3770 -- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md`); the round-2 audit whose disposal made the fold, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md` (H1, id 1); the audit pin `TOOL-dFairHearing-1@rev-2` in `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`, added at `c993af496`; the departures report's entry 13, quoted in `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
