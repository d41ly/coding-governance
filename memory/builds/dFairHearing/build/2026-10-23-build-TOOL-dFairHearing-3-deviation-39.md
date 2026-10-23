# TOOL-dFairHearing-3 deviation 39 — the round-3 spec audit's disposal folded a hands-off edge into the audited spec

**Serves:** deviation TOOL-dFairHearing-3

- **Departs from:** `TOOL-dFairHearing-3@rev-1`
- **Hand-off:** spec-revised
- **Before:** TOOL-dFairHearing-3's spec as the round-1 spec audit read it at rev-1 and its disposal left it at rev-2 (`c993af496`): §3 holds no hands-off edge to TOOL-dFairHearing-32, and its AC7 arm reads its expected no-flag preset as a literal.
- **After:** at `92dd0f46a`, rev-3: §3 gains `- **hands-off** TOOL-dFairHearing-32 — finding id 24 of the round-3 spec audit: this unit's AC7 arm reads its expected no-flag preset from DESIGN_RECORD_PRESET rather than the literal, so a replay-1 hit does not red it (its S19)`, and §9 the line `rev-3 · 2026-10-23 · §3 · the round-3 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-32, which re-pins this unit's AC7 arm to DESIGN_RECORD_PRESET.`; no criterion's text changed.
- **Cause:** review finding
- **Reason:** the round-3 spec audit's medium id 24 found that a replay-1 hit flips the design-record preset this unit's AC7 arm pins as a literal, so that arm would red on a correct flip. Its disposal batched the minor into TOOL-dFairHearing-32 (BUILD-METHOD M4) and folded the edge here, moving the spec audited at rev-1 with no audit of the move. Risk is additive: only an edge and a §9 line moved, but the edge changes what this unit's AC7 arm expects.
- **Evidence:** commit `92dd0f46a` (`git diff 92dd0f46a~1 92dd0f46a -- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md`); the round-3 audit whose disposal made the fold, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md` (id 24); the audit pin `TOOL-dFairHearing-3@rev-1` in `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`, added at `c993af496`; the departures report's entry 21, quoted in `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the fold, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
