# TOOL-dSafePassage-13 deviation 156 — TOOL-dSafePassage-13's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-13

- **Departs from:** `TOOL-dSafePassage-13@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-13`'s spec as the revision at `TOOL-dSafePassage-13@rev-3` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-4, revised for the cross-check record's row 39, U5 and U6: S7 fills the existing `help.enforce` row and drains the unsummarised list; `help.enforce` is read through `govkit.read_policy_value`, which runs `policy.py get`; S7 lands with the regenerated mirror in a second commit.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-4 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-13-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
