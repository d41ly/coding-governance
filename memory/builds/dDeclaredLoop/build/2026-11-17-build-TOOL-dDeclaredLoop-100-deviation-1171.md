# TOOL-dDeclaredLoop-100 deviation 1171 — the settled-items row S3 names `parse_conf` a `TREE_LIB_SYMBOLS` member, which it is not

**Serves:** deviation TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-117

- **Departs from:** `TOOL-dDeclaredLoop-100@rev-2` [§3 S3]
- **Hand-off:** code-to-record
- **Before:** row S3 of the settled-items table says `TREE_LIB_SYMBOLS` holds two names and 95 rev-3 §3 settles `parse_conf` as a member (its S1).
- **After:** `TREE_LIB_SYMBOLS` holds two names, `derive_docstring_ids` and `derive_constant_charges`, and 95 rev-3 §3 settles `parse_conf` as no member of it (its S1); `parse_conf` is a member of `CONF_READERS`, as row S21 of the same table says.
- **Cause:** review finding
- **Reason:** the closing diff review's round 1 confirmed row S3 contradicting row S21, unit 95's §3 row S1 and the tuple in `tools/loop/loop_lib.py` (its item 5, finding 7); the spec is CLOSED and frozen, so this record carries the correction and the spec's text stays as landed.
- **Evidence:** `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md`, item 5; `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` and `tools/loop/loop_lib.py#CONF_READERS`; row S1 of the §3 table of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-95.md`.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1
