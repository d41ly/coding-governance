# TOOL-dSafePassage-8 deviation 152 — TOOL-dSafePassage-8's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-8

- **Departs from:** `TOOL-dSafePassage-8@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-8`'s spec as the revision at `TOOL-dSafePassage-8@rev-2` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-3, revised for the cross-check record's row 27: the external edge, the risks line and the note under the gates no longer expect the minimal guard to refuse a landing, since the lander fires no pre-commit; the guard binds TOOL-dSafePassage-1's unit-pass commit.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-8-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
