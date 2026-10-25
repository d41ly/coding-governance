# TOOL-dSafePassage-9 deviation 153 — TOOL-dSafePassage-9's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-9

- **Departs from:** `TOOL-dSafePassage-9@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-9`'s spec as the revision at `TOOL-dSafePassage-9@rev-2` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-3, revised for the cross-check record's rows 29 to 31, U5 and U6: S6 fills the existing `install.retired-edits` row and drains the unsummarised list; the mode is read through `read_policy_value` running gov's `policy.py get` in the target; the helper lives once in `govkit.py`; S6 lands with the regenerated mirror in a second commit.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-9-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
