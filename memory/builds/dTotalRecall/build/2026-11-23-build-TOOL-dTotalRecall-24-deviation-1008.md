# TOOL-dTotalRecall-24 deviation 1008 — the two row builders, the census helper entry, the walk's unread line and its extra flags, and the walk's re-measured hold

**Serves:** deviation TOOL-dTotalRecall-24

- **Departs from:** TOOL-dTotalRecall-24@rev-2 [§4 Inventory, S3, S6, S7, Rollout]
- **Hand-off:** spec-to-code
- **Before:** §4's inventory mints write_feed_lines, add_record_events, derive_record_events and read_record_root; S3 names the caller's row builder without a name; S6 names missing, extra and unread for a refused MEMORY_ROOT; the census helper list stays as TOOL-dPlacedRequest-13 landed it; §4 pins the first walk's hold at 1.03 s on node d; Rollout moves the kit versions in the same commit.
- **After:** tools/lib/gov-feed.sh#derive_feed_row is add_feed_event's append-once read and #derive_record_rows the record range's builder, the two builders write_feed_lines runs under the lock; FEED_WRITER_HELPER_FNS gains write_feed_lines, since add_feed_event's body now reaches the log through it; check_feed's record arm prints unread <ref> walk <tip> where git refuses the walk to a tip a branch reaches; derive_record_events adds --root, --no-color and core.quotePath=false to the spec's flags; the unattended suite's keyless staged copy cuts derive_feed_row's return 0; NODE_LOCK_BOUND's comment pins the hold this pass measured, 4.01 s over 69,097 events (PINNED, 2026-11-23, TOOL-dTotalRecall-24); no kit version moves on the branch.
- **Cause:** builder discovery
- **Reason:** a builder write_feed_lines can call is a function, and the append-once read must stay text-identical for the existing staged copies; the census grades a helper whose body neither appends nor calls an entry, which add_feed_event became; a walk git refuses must not pass as clean; --root keeps a root commit's records under log.showRoot=false; the hold was measured on this node, not node d; govkit.py#cmd_epoch says the lander mints the bump at the push boundary, so a branch owes none.
- **Evidence:** the pass commit of TOOL-dTotalRecall-24 and its acceptance ledger, 2026-11-22-build-TOOL-dTotalRecall-24-1-acceptance-ledger.md
- **Risk:** additive
- **Approver:** author, under the build's author-recorded value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-24
- **Made-by:** owner
