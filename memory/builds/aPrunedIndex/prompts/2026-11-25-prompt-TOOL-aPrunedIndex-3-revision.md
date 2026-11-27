# Revision — aPrunedIndex: unit 3 leaves a replaced edit's rows to `--gc`

**Serves:** research TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4

## The prompt

> Keep until --gc (Recommended)

The owner's answer in the building session, 2026-11-25, to the question quoted whole under the last heading below.

## The brief

### Goal
Revise TOOL-aPrunedIndex-3: the overlay releases nothing. When a worktree's dirty rows are replaced, the rows only the old
edit held stay until `--gc`'s full sweep. So the window finding 16 named does not open, and everything that exists for it
goes: `check_view_held`, the refusal, its five call sites, the `moved-view` plant, the help sentence, and the edits to
`edge_grammar.py`, `instruction_units.py` and the read verbs. The build's sweep stays bounded to what it drops, and `--gc`
keeps the full sweep. The spec says plainly what it leaves: rows of replaced edits, and any legacy orphan. Correct each
sibling spec's mention of the removed names and of the overlay's release (rev bump and revision-log line), and nothing else
in them.

### Items
3. A build's sweep deletes only rows that the trees and the dirty rows of gone worktrees it drops held and nothing else holds; `build_overlay` is unchanged in what it deletes; `--gc` keeps the full sweep. [planned TOOL-aPrunedIndex-3]

Also, in units 1, 3 and 4, section 4's files touched name the acceptance ledger, the journal record under `memory/builds/aPrunedIndex/build/` with one line per criterion, where it is not named yet: hygiene check 23 refuses a CLOSED Tier-2 spec without one.

### Acceptance
`check`'s output on one index is byte-equal before and after. A plant pads a fixture's index with dead versions and reds on
each of: a read that scans every version's rows, a probe that walks them, a sweep that walks them. Each is seen red on its
staged break. Wall and CPU before and after are recorded, alternating on one private copy of one index. For item 4, a plant
with a worktree at a commit before the registry collects, and one with the registry deleted from its working tree refuses.

### Gates
`tags (the resolver's checks)`, `instruction edits (manifest checks)`, `edges (every declared edge parses, is registered and resolves)`,
`lexicon naming predicates`, `spec tokens (a spec's own names resolve)`, and the full bar at the close.

### Non-goals
No ceiling change. No change to what a row holds, how a version is derived, the schema number or the file's name. No
write-ahead log. No held copy of the view in a temporary table. `positional.py` and its `git blame` are left. No automatic
collection in a plain build. No run of `--gc`, VACUUM or a deletion on either live index file.

### Limitations
The index is shared by every worktree of the node, and other sessions run bars against it: nothing in this build opens the
live index with the new code before the owner says so in the building session, since the first open adds two SQL indexes
(about 205 s of write lock and 1 GB, measured on the copy). A fixture uses its own scratch repository. `tools/loop/position.py` (PINNED, 2026-11-25)
and `tools/memory-tree/routed_commits.py` are not edited. An edit to `tag_index.py` is a new extractor version, so the units
land together.

### Reuse
The seams are `SCHEMA`, `VIEW_JOIN`, `read_defined`, `_write_parsed`, `_write_path_rows`, `remove_unheld_rows`,
`build_overlay` and `read_live_versions` in `tools/playbook/tag_index.py`, the `--fixture --plant` runner of
`tools/playbook/gov_tag.py`, and the plant table of `tools/playbook/adopt-playbook.sh`. The reuse probe named no other
eviction or row-index seam. Records: KICK-dKeptSession-87, `0200dd0cc` (the same scan fixed in two of three readers),
PLAY-dOrderedCharter-51 (versions side by side, and `--gc`'s refusal), TOOL-aQueuedIndex-1 (the write lock).
Recall terms used: tag index shared worktree gc dead versions path_row tree_built sweep index-s3 fts_chunk vacuum read_rows ceiling


## Owner's answers, 2026-11-25, in the building session

Asked: aPrunedIndex unit 3: when a worktree's uncommitted edit is replaced by a newer one, what should happen to the old edit's rows in the shared tag index?
Answer: Keep until --gc (Recommended)

Asked: May this session open the live shared tag index with the new code?
Answer: Yes, once built (Recommended)

The second was shown as: once all four units are built and measured on private copies, when the closing review is clean and
before the bar; two SQL indexes, about 205 s of write lock and about 1 GB, once on the machine; no `--gc`, vacuum or delete. (PINNED, 2026-11-25)
