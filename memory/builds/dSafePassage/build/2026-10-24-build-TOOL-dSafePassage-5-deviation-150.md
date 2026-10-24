# TOOL-dSafePassage-5 deviation 150 — TOOL-dSafePassage-5's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-5

- **Departs from:** `TOOL-dSafePassage-5@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-5`'s spec as the revision at `TOOL-dSafePassage-5@rev-2` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-3, revised for the cross-check record's rows 17 and 18: the `policy` observation runs gov's `policy.py get --rev` at the walked commit with the target as its working directory, and gains `absent`, so `fanout-cap` reads 2 only with `.agent-cap.conf` gone.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-5-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck
