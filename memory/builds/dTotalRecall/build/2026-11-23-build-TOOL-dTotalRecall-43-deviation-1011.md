# TOOL-dTotalRecall-43 deviation 1011 — the line-break rule's further callers, the stream plan's path and root, and where the new arms live

**Serves:** deviation TOOL-dTotalRecall-43

- **Departs from:** `TOOL-dTotalRecall-43@rev-8` [§2 S6, S14, S15, S16, S36, S37, S44, S58]
- **Hand-off:** spec-to-code
- **Before:** S37 names check_line_break's callers as check_row_value, the factory's two checks and each --edge; S58 grades a stream plan from its text alone; S36 says a missing path is counted and names no counter; S44 seeds each caller and names no helper; S16 and S17 name no fixture main worktree; the New arm lines name each subject and no suite file holding the arm.
- **After:** `tools/memory-tree/record_kinds.py`'s two purpose checks and `tools/memory-tree/ratchet.py`'s --reason and --key checks call `backlog.py#check_line_break` too, so AC37's one line-break function holds; `record_kinds.py#check_fence_records` calls a validator as (text, path=, root=) and `check_stream_plan` joins its units through `record_kinds.py#check_plan_units`; `extract_code.py#read_defs_at` takes a `missing` list; `tag_index.py#read_authored_anchors` seeds every caller of `derive_anchor`; the memory measure's fixture main worktree is C:/fx/repo and the shell-other plant's bare word is memories, since the bare root now counts; the arms sit in `tools/lexicon/selftest.py`, `tools/runlog/selftest.py`, `tools/memory-recall/selftest.py` and `build_records.py`'s door-header plant, and `tools/govkit/selftest.py`'s retag arm expects the [section.<anchor>] tag S6 writes.
- **Cause:** builder discovery
- **Reason:** AC37 counts one memory-tree function testing for a line break and the record kinds' and the ratchet's checks each tested one of their own; a README's ids: and the tree's id grammar are read by path and root, which a text-only validator cannot reach; the two kept arms and the fixture paths are where the spec's criteria are observed.
- **Evidence:** the pass commit of TOOL-dTotalRecall-43 and its acceptance ledger, `2026-11-23-build-TOOL-dTotalRecall-43-2-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-43
- **Made-by:** owner
