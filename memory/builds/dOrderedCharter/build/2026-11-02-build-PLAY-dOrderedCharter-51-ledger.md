# PLAY-dOrderedCharter-51 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-51

Each line is a plant `gov_tag.py --fixture` built in its own scratch repository under the temp root, or a
probe this pass ran with the pass applied. The playbook render selftest, the `tags` leg over the tree and
the `New arm:` line's RED-first observation (each plant's failing case staged by unit 44's one-version
key) are the main loop's at the close: a role agent runs none of them.

**Evidences:** PLAY-dOrderedCharter-51
- AC1 — `--plant two-versions` — exit 0; two worktrees of one fixture repository, the second's `fixture_tags.py` edited and committed, built alternately twice into the one shared index: `incremental rows equal a cold build's` for each worktree, its `--dump` (`read_dump`, the rows at its own versions) against a build from nothing of that worktree alone, and `2 versions of fixture_tags:extract_declared held side by side` in `blob_parsed`. A scratch staging of unit 44's tree-only freshness key and unfiltered view turned `--plant served-across` red (exit 1, `served 1 rows of one's version`); restored. OWED to the main loop: the arm's RED-first observation
- AC2 — `0 blobs parsed` — exit 0 on the same plant; the second round printed `0 blobs parsed, 0 extractor runs` for each worktree and `round 2 parsed 0 and 0 blobs`. OWED to the main loop: the arm's RED-first observation
- AC3 — `--plant served-across` — exit 0; worktree two on the tree worktree one built, its extractor module edited in the working tree, `two parsed 2 blobs on the tree one built; served 0 rows of one's version, and one serves 1` for `layer.memory.recall`, the tag only one's version yields. OWED to the main loop: the arm's RED-first observation
- AC4 — `--gc` — exit 0 on `--plant two-versions`; with worktree two removed and pruned, `tag-index — collected: 11 rows of 1 versions`, then `--gc left 0 rows of its version; the live dump unchanged`. A probe with a live worktree's `namespaces.toml` deleted refused, `--gc: worktree <path>/wt2 cannot be read, so nothing is collected`, and kept all 9 blob rows. OWED to the main loop: the arm's RED-first observation
