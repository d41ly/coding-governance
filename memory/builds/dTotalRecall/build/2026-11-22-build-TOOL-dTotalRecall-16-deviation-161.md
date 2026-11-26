# TOOL-dTotalRecall-16 deviation 161 — the purpose write refuses an `--ask` its value does not take

**Serves:** deviation TOOL-dTotalRecall-16

- **Departs from:** `TOOL-dTotalRecall-16@rev-6` [§2 S5]
- **Hand-off:** spec-to-code
- **Before:** S5 refuses `--ask <id>` only where the id is no open ask, and S6 gives each `none` registry row under `ledger` and `derive` its own pending, so an `--ask` given beside those values has no stated outcome; nor has an `--ask` given without `--write`.
- **After:** `tools/memory-tree/record_kinds.py#write_purposes` exits 2 writing nothing on an `--ask` under any value but `review`, and `main` exits 2 on `--ask` without `--write`; a row already pending is re-written by replacing its `purpose =` line, the one-line write S5 states, and the view is re-rendered after each write as `new` re-renders it.
- **Cause:** builder discovery
- **Reason:** an owner ask filed under a value that records no ask would be dropped silently; a refusal is what the kit's other malformed-argument paths do.
- **Evidence:** the pass commit of TOOL-dTotalRecall-16; `record_kinds.py --fixture --plant review-write` and `--plant value-derive` over the worktree.
- **Risk:** stricter
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-16
