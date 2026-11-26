# TOOL-dTotalRecall-23 deviation 1007 — the leg readers' empty params, the walk's call-graph arm, a failed git read and the announce lines' homes

**Serves:** deviation TOOL-dTotalRecall-23

- **Departs from:** TOOL-dTotalRecall-23@rev-3 [§2 S2, S3, S4, S6]
- **Hand-off:** spec-to-code
- **Before:** S2 maps each reader to a reader and a params function; S3 names no answer for a git read that fails; S4 keeps every continue in walk and says nothing of the selftest arm that reads walk's call graph; S6 names the channel of each announce line and not where it is made.
- **After:** `tools/memory-tree/tree_lib.py#LEG_READERS` spells None for the params of `unfenced-head` and `spec-head`, whose key is empty; `tree_lib.py#read_rows_at` parses every path when `git ls-files -s` or `git diff HEAD` fails, an unborn HEAD say; `tree_lib.py#build_leg_rows` reads blobs in batches of `LEG_READ_CHUNK` and writes no further row when a batch read fails; the call-graph arm in `tools/memory-tree/corpus_ids.py#cmd_selftest` reads the anchor route's call in `extract_ids`, which now holds the per-line loop; `walk` returns its counts as `legs` and `corpus_ids.py#main` appends the note under `--check` alone, so `--report` and every caller of `walk`'s notes print as before; `gen_build_index.py#print_leg_lines` prints at the `--check` and `--print-bindings` exits after flushing stdout.
- **Cause:** builder discovery
- **Reason:** a params function for an empty key would be a symbol no reader needs; a failed git read must cost parses, never a raise or a wrong row; a cold build over every memory blob in one batch holds every blob at once; the call-graph arm read walk's route call, which S4's split moves into extract_ids; walk's notes are compared exactly by existing arms, and a stderr line printed before a block-buffered stdout would land among the verdict lines check 9 splits.
- **Evidence:** the pass commit of TOOL-dTotalRecall-23 and its acceptance ledger, 2026-11-22-build-TOOL-dTotalRecall-23-1-acceptance-ledger.md
- **Risk:** additive
- **Approver:** author, under the build's author-recorded value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-23
- **Made-by:** owner
