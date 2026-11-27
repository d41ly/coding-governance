# TOOL-dTotalRecall-122 deviation 1018 — the read-back refusal says a moved file is still staged, and the foreign ask row lands under its heading

**Serves:** deviation TOOL-dTotalRecall-122

- **Departs from:** `TOOL-dTotalRecall-122@rev-1` [§4 "S1 — the rollback"]
- **Hand-off:** spec-to-code
- **Before:** the read-back branch prints what the helper answered, whose moved answer ends `, unstaged`; the planted stage appends its foreign line to the file.
- **After:** that branch prints the moved answer with `, unstaged` replaced by `, still staged`, the helper itself as the spec spells it; the planted line is inserted under `## Asks` where the file holds that heading and appended elsewhere.
- **Cause:** builder discovery
- **Reason:** the read-back runs only after the stage took the write, so `unstaged` would be false there; and an ask row appended past `## Dispositions` is no ask, so the read-back accepted the filing and the case could not red.
- **Evidence:** the `foreign read-back` case of the `ask-door` plant, exit 0 with the line appended and exit 3 with it under the heading (DERIVED 2026-11-25); the ledger `2026-11-25-build-TOOL-dTotalRecall-122-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-122
- **Made-by:** owner
