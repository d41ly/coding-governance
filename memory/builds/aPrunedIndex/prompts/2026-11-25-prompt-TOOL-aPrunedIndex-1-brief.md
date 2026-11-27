# Brief — aPrunedIndex: the tag check costs what its own worktree's rows cost

**Serves:** research TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4
**Caused-by:** TOOL-aPrunedIndex-1

## The prompt

> Find why `python tools/playbook/gov_tag.py check` is slow and make it reliably fit its 420 s ceiling, without raising the ceiling and without changing any verdict. (PINNED, 2026-11-25)

The sentence is the opening task of the building session, written by the session that started it
(`local_7d7a756d-b405-4fbc-b780-41bb67de56c2`).

## The brief

### Goal
`gov_tag.py check` reliably fits its 420 s ceiling on the node's shared tag index with every verdict unchanged, because rows (PINNED, 2026-11-25)
of extractor versions the reading worktree does not derive stop costing it anything.

### Items
1. Every full-view read starts from the reading worktree's own versions, through an index on `path_row(extractor, version)`, and `read_defined` asks for no DISTINCT. Today `read_defined` scans all 17.8M rows in tag order and every `read_rows` scans the table. [planned TOOL-aPrunedIndex-1]
2. A build finds whether a path's rows are already named through a partial index of the `parsed` rows, and a build or overlay with no blob loads no parse ledger. Today 30,228 probes walk every version's rows to find 24 to write. [planned TOOL-aPrunedIndex-2]
3. A build's sweep, and an overlay's replacement of its dirty rows, delete only rows that the trees and dirty rows they drop held and nothing else holds; `--gc` keeps the full sweep. Today each build scans both row tables. [planned TOOL-aPrunedIndex-3]
4. `--gc` skips a worktree whose HEAD tree holds no `namespaces.toml` under the kit's directory, naming it, and still refuses a worktree whose registry should be there and cannot be read. Today four worktrees of 104 that predate the registry make it refuse. It closes KICK-dKeptSession-87's accept. [planned TOOL-aPrunedIndex-4]

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

## Drawn from the session

> On a clean index (270 MB) the unmodified check takes 85 s. (PINNED, 2026-11-25)
— agent, 2026-11-25, the run over a private fresh index

> the planner ignores the new version index unless told to start from the version list
— agent, 2026-11-25, the padded-index run

## Owner confirmation

Asked: Approve the aPrunedIndex plan: units 1-4 with a spec audit?
Answer: Yes, units 1-4 and audit

The question was put, and the answer received, in the session `local_7d7a756d-b405-4fbc-b780-41bb67de56c2`, which relayed
the owner's words whole on 2026-11-25 and said they are this go and nothing wider. It covers the build. The live index's
first open and the landing are asked again in the building session.
