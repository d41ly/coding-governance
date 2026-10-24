# TOOL-dSafePassage-10 deviation 154 — TOOL-dSafePassage-10's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-10

- **Departs from:** `TOOL-dSafePassage-10@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-10`'s spec as the revision at `TOOL-dSafePassage-10@rev-2` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-3, revised for the cross-check record's rows 33 and 34: the `policy` class reads each `[[key]]` name of the folder's own `tools/policy/catalogue.toml` with `tomllib`, so the base and the tip each read their own catalogue; AC5 reds a reader that opens one fixed catalogue; F6 re-resolved.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-10-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
