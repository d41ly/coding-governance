# TOOL-dGroundRules-28 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-28

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit by the command it names, run on the worktree with this unit's edits in place. Before the
edit, `gotchas.py --for-paths tools/govkit/govkit.py tools/govkit/matrix.py tools/policy/check_policy.py`
selected 8 classes by anchor and none was this one; the record carried 2 anchors, now 5.

**Evidences:** TOOL-dGroundRules-28
- AC1 — `python tools/memory-tree/gotchas.py --for-paths tools/govkit/govkit.py` printed
  "- [ ] test-oracle-read-from-a-historical-sha (path)" with the record's path beneath it.
- AC2 — `python tools/memory-tree/gotchas.py --for-paths tools/govkit/matrix.py` printed the same
  item, "- [ ] test-oracle-read-from-a-historical-sha (path)".
- AC3 — `python tools/memory-tree/gotchas.py --check` exited 0, after `--write` regenerated
  `memory/gotchas/INDEX.md`; its one line was the standing check 19 advisory, and `--report` lists
  none of this record's anchors as selecting no tracked path. `grep -n "HEAD" memory/gotchas/INDEX.md`
  printed line 150, the class's row, whose description now names the HEAD shape beside the literal sha.

`tools/policy/check_policy.py`, the third anchor S2 names, selects the class too: `--for-paths` over it
printed the same item. The `memory hygiene`, `recall floor` and `recall floor arms` legs are the close's.
