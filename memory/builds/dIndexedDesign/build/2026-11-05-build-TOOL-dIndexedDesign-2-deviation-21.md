# TOOL-dIndexedDesign-2 deviation 21 — TOOL-dIndexedDesign-2's spec re-grounded against its parents, cross-read 2026-11-05

**Serves:** deviation TOOL-dIndexedDesign-2

- **Departs from:** `TOOL-dIndexedDesign-2@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dIndexedDesign-2`'s spec as the revision at `TOOL-dIndexedDesign-2@rev-2` reads it, whose S7 registers the overlap kind with `record_kinds.py new overlap --tag record.overlap` alone, and which builds `item.design.overlaps`' witness while leaving TOOL-dDeclaredLoop-13 S8's stand-in row for it unmentioned
- **After:** the spec at rev-3, revised for the cross-check record's rows 7 and 9: S7 spells `--writer`, `--check` and `--purpose` and sets tr18's columns through its landed verb, AC9 red on a missing column; a new S10 deletes the stand-in row and points the item's `witness` at `design_lib.py --overlaps`, observed by a new AC11, as the brief `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md` states.
- **Cause:** review finding
- **Reason:** This build's first cross-read against its parents found the spec disagreeing with parents that did not move in either revision: TOOL-dTotalRecall-16 S2 refuses a `record_kinds.py new` without `--purpose`, and TOOL-dTotalRecall-18 S1 requires the `home`, `lifecycle`, `readers` and `layer` columns, and dl13 S8 derives a stand-in row for every item owned outside dDeclaredLoop; the owner asked on 2026-11-05 for a cross-read of this build against the parent revisions it never read, and no code has started.
- **Evidence:** `memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-2-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dIndexedDesign-17
- **Caused-by:** 2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck
