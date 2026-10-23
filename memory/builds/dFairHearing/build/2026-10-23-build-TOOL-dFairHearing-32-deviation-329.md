# TOOL-dFairHearing-32 deviation 329 — the round-5 spec audit's disposal folded two hands-off edges into the audited spec

**Serves:** deviation TOOL-dFairHearing-32

- **Departs from:** `TOOL-dFairHearing-32@rev-1`
- **Hand-off:** spec-revised
- **Before:** TOOL-dFairHearing-32's spec as the round-4 spec audit read it at rev-1 and its disposal left it at rev-2 (`96a0fb304`): §3 holds no hands-off edge to TOOL-dFairHearing-38 or -40, and AC8's comparison and its `%TEMP%/fgc` fixture are this unit's alone.
- **After:** at `c9fd32b9a`, rev-3: §3 gains `- **hands-off** TOOL-dFairHearing-38 — finding id 1 (item H1, shared with id 11) of the round-5 spec audit: AC8's comparison and its %TEMP%/fgc fixture, re-run there with a staged break as the observation of a selected verdict` and `- **hands-off** TOOL-dFairHearing-40 — the round-5 spec audit's finding id 28: where resolveKitDir, this unit's S25 port, disagrees with resolve_kit_dir.py on unit 37's rows 8 and 9, the cure is that unit's (its S17)`, and a §9 rev-3 line naming both; no criterion's text changed.
- **Cause:** review finding
- **Reason:** the round-5 spec audit's high H1 (ids 1 and 11) found unit 37's AC4 expecting argparse's `unrecognized arguments` from `gotchas.py`, which has no argparse. Its disposal promoted TOOL-dFairHearing-38 to re-run this unit's AC8 comparison with a staged break, and batched minor id 28, unit 37's rows 8 and 9 against this unit's `resolveKitDir` port, into TOOL-dFairHearing-40 (BUILD-METHOD M4). The folds moved the spec audited at rev-1 with no audit of the move, and the owner's stop after round 5 leaves no round to audit it. Risk is additive: only edges and a §9 line moved, but the first has unit 38 re-run this unit's AC8.
- **Evidence:** commit `c9fd32b9a` (`git diff c9fd32b9a~1 c9fd32b9a -- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-32.md`); the round-5 audit whose disposal made the folds, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md` (H1, ids 1 and 11; id 28); the audit pin `TOOL-dFairHearing-32@rev-1` in `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`, added at `96a0fb304`; the owner's stop, `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`; the departures report's entry 23, quoted in `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the spec-audit disposal stage that made the folds, recorded after the fact under the departures brief, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2
