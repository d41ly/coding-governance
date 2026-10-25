# TOOL-dSafePassage-6 deviation 151 — TOOL-dSafePassage-6's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-6

- **Departs from:** `TOOL-dSafePassage-6@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-6`'s spec as the revision at `TOOL-dSafePassage-6@rev-2` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-3, revised for the cross-check record's rows 19 to 22 and U5 to U7: S7 fills the two catalogue rows dGroundRules lands and drains the unsummarised list, adding no row; the forwarders read through `policy-shim.sh get`, `readPolicy` and `policy.py get` and never name the mirror; the window value is read through `govkit.read_policy_value`; S7 lands with the regenerated mirror in a second commit; F2 re-resolved and F7 added.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-6-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
