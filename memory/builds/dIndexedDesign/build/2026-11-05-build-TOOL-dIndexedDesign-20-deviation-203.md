# TOOL-dIndexedDesign-20 deviation 203 — TOOL-dIndexedDesign-20's spec re-grounded against its parents, cross-read 2026-11-05

**Serves:** deviation TOOL-dIndexedDesign-20

- **Departs from:** `TOOL-dIndexedDesign-20@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dIndexedDesign-20`'s spec as the revision at `TOOL-dIndexedDesign-20@rev-3` reads it, whose S4 and S7 register `diff` and `inventory` with no `--purpose` and no TOOL-dTotalRecall-18 columns, and whose S10 names `record-kind.diff` and `record-kind.inventory` in `returns` with no version
- **After:** the spec at rev-4, revised for the cross-check record's rows 95 and 99: S4 and S7 pass `--purpose`, declare form `fields` and set tr18's columns through its landed verb, each row `unarmed` until its first record; S10 writes `@1`, its `[[record-version]]` rows deferred to spec 34's pass; AC9 runs `record_kinds.py --check`, red on a missing column or an unversioned `returns`, as the brief `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md` states.
- **Cause:** review finding
- **Reason:** This build's first cross-read against its parents found the spec disagreeing with a parent that did not move in either revision: TOOL-dTotalRecall-16 S2 refuses a `record_kinds.py new` without `--purpose`, and TOOL-dTotalRecall-18 S1 requires the `home`, `lifecycle`, `readers` and `layer` columns, and TOOL-dDeclaredLoop-24 writes `returns` as `record-kind.<name>@<n>`; the owner asked on 2026-11-05 for a cross-read of this build against the parent revisions it never read, and no code has started.
- **Evidence:** `memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md`, and the rev-4 line in this spec's §9.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-20-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dIndexedDesign-17
- **Caused-by:** 2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck
