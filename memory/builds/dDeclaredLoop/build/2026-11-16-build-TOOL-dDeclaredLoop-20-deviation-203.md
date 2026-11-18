# TOOL-dDeclaredLoop-20 deviation 203 — the class-count command spelled under the workflows kit's own folder

**Serves:** deviation TOOL-dDeclaredLoop-20

- **Departs from:** `TOOL-dDeclaredLoop-20@rev-5` [§4]
- **Hand-off:** spec-to-code
- **Before:** §4 "The left-shift count" has the DISPOSAL prompt name `review_dispose.py classes` spelled under `{{TOOL_ROOT}}`, as the build harness spells `DRIVER`.
- **After:** the prompt spells it under `{{KIT_DIR}}`, the placeholder the build harness already uses for its own kit's files, such as `unattended-unit.js`; the render reads the same path either way. The `defaults` plant's needle in `tools/loop/review_bounds.py#PLANTS` also gains the four disposal fields, so the plant holds the whole line AC10 names, where the §5 sweep kept the shorter needle.
- **Cause:** builder discovery
- **Reason:** `review_dispose.py` sits in the build harness's own kit, and `{{TOOL_ROOT}}` with a kit folder after it is how the harness names a sibling kit, the unattended driver; its own kit's files go through `{{KIT_DIR}}`.
- **Evidence:** the `leftShiftSentence` constant of `tools/workflows/unattended-build.template.js`, and the `scriptPath` the same template gives `unattended-unit.js`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the render is unchanged, `tools/workflows/review_dispose.py`
- **Caused-by:** TOOL-dDeclaredLoop-20
