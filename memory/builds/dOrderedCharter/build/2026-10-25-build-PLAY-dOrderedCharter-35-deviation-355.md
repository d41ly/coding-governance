# PLAY-dOrderedCharter-35 deviation 355 — PLAY-dOrderedCharter-35's spec revised for the owner's fork picks and the parent audit

**Serves:** deviation PLAY-dOrderedCharter-35

- **Departs from:** `PLAY-dOrderedCharter-35@rev-4`
- **Hand-off:** spec-revised
- **Before:** `PLAY-dOrderedCharter-35`'s spec as the revision at `PLAY-dOrderedCharter-35@rev-4` reads it.
- **After:** the spec at rev-5: `instructions.exclude`'s default read as `[]` (none), as the built catalogue holds it (audit P11).
- **Cause:** external
- **Reason:** the parent audit `2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit` found this spec's assumption or text off, and the owner asked for it fixed where possible before the build run; no code has started.
- **Evidence:** `memory/builds/dOrderedCharter/build/2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit.md`, the brief `memory/builds/dOrderedCharter/prompts/2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md`, and the rev-5 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-32-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** 2026-10-25-build-PLAY-dOrderedCharter-1-parents-audit
