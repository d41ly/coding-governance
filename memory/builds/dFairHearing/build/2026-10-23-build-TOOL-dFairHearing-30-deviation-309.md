# TOOL-dFairHearing-30 deviation 309 — the round-5 spec audit's disposal folded a hands-off edge into the audited spec

**Serves:** deviation TOOL-dFairHearing-30

- **Departs from:** `TOOL-dFairHearing-30@rev-1`
- **Hand-off:** spec-revised
- **Before:** TOOL-dFairHearing-30's spec as the round-4 spec audit read it at rev-1 and its disposal left it at rev-2 (`96a0fb304`): §3 holds no hands-off edge to TOOL-dFairHearing-40, and nothing holds the reports and transcripts its verdict record names on disk past this unit.
- **After:** at `c9fd32b9a`, rev-3: §3 gains `- **hands-off** TOOL-dFairHearing-40 — the round-5 spec audit's minors that read this unit's verdict record, ids 9, 13, 24 and 29: the void column re-derived from each attempt's report and quoted transcript line, so each report and transcript the record names stays on disk until that unit's pass, the record's Serves line read for TOOL-dFairHearing-35, and the ungated class set re-derived (its S9, S24, S25 and S30)`, and §9 the line `rev-3 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (four minors that read the verdict record).`; no criterion's text changed.
- **Cause:** review finding
- **Reason:** the round-5 spec audit's minors ids 9, 13, 24 and 29, filed on how units 35 and 37 read this unit's verdict record, were batched into TOOL-dFairHearing-40 (BUILD-METHOD M4), and the disposal folded the edge here. The fold moved the spec audited at rev-1 with no audit of the move, and the owner's stop after round 5 leaves no round to audit it. Risk is additive: only an edge and a §9 line moved, but the edge keeps every report and transcript this unit's record names on disk until unit 40's pass, a retention this unit did not owe at rev-1.
- **Evidence:** commit `c9fd32b9a` (`git diff c9fd32b9a~1 c9fd32b9a -- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-30.md`); the round-5 audit whose disposal made the fold, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md` (ids 9, 13, 24, 29); the audit pin `TOOL-dFairHearing-30@rev-1` in `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`, added at `96a0fb304`; the owner's stop, `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`; the departures report's entry 22, quoted in `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
