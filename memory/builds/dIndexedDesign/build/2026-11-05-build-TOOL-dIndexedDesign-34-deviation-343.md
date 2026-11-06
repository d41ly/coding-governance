# TOOL-dIndexedDesign-34 deviation 343 — TOOL-dIndexedDesign-34's spec re-grounded against its parents, cross-read 2026-11-05

**Serves:** deviation TOOL-dIndexedDesign-34

- **Departs from:** `TOOL-dIndexedDesign-34@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dIndexedDesign-34`'s spec as the revision at `TOOL-dIndexedDesign-34@rev-3` reads it, which adds the per-kind table rows of `diff` and `inventory` and no `[[record-version]]` row hashing them
- **After:** the spec at rev-4, revised for the cross-check record's row 99, as spec 20's fold places it: a new S3 adds the two `[[record-version]]` rows in `tools/loop/item-schema.toml` in the commit of the S1 rows they hash, observed by a new AC5 that reds when a hash moves while the version stays 1, as the brief `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md` states.
- **Cause:** review finding
- **Reason:** This build's first cross-read against its parents found the spec disagreeing with a parent that did not move in either revision: TOOL-dDeclaredLoop-24 versions every `returns`, and spec 20's `@1` needs rows that hash what this unit adds; the owner asked on 2026-11-05 for a cross-read of this build against the parent revisions it never read, and no code has started.
- **Evidence:** `memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md`, and the rev-4 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-20-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dIndexedDesign-17
- **Caused-by:** 2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck
