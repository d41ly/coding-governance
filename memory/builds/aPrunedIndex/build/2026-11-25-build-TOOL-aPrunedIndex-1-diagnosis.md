# Why the tag check is slow — the diagnosis this build starts from

**Serves:** research TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4

Node a, 2026-11-25, at `3d6c1702a` plus the unlanded aAnsweredPark commits, which touch no file of this kit.

Read-only on the live index; every timing below is on a private copy of `index-s3.db` (12.6 GB, mtime
unchanged across the copy). Nothing in the repository, and neither live index file, was changed.

## Causes, as measured

1. `read_defined` (`tools/playbook/tag_index.py:1052`) asks `SELECT DISTINCT p.tag`. SQLite answers DISTINCT
   in order, so its plan is `SCAN p USING INDEX path_row_tag`: all 17.8M rows, one random lookup each.
   622 s cold, 218 s on the second run. The same join with no DISTINCT: 39 s. `0200dd0cc` fixed this shape in
   `read_rows` and `read_population` with `+p.tag`, and missed this third reader. Called twice per check.
2. Every `read_rows` is `SCAN p`, the whole of `path_row`, whatever the view holds. The served view is 423,156
   rows of 17.8M (2.4%). One check makes about 15 such scans.
3. A build of an unbuilt tree (every landing has one) is worse than the reads. `_write_path_rows` probes
   `path_row` per (path, blob, extractor) through `path_row_key(path, blob)`, so each probe walks every stored
   version's rows of that path, about 1,000. Then `remove_unheld_rows` scans all of `path_row` and `blob_row`.
   Measured for one check on an unbuilt tree (it builds HEAD and the compare base): 1,118 s of 1,843 s, of which
   529 s is 30,228 name probes that found 24 rows to write, and 537 s the two sweeps.

## Why the file grew

- 35 versions of `extract_citations` are stored; the node's worktrees derive 6. Rows of the 29 dead versions are
  never retired: a plain build collects nothing (PLAY-dOrderedCharter-51 S5), only `--gc` does.
- `--gc` refuses today: 4 of 104 worktrees have no `tools/playbook/namespaces.toml`:
  blissful-khayyam-69a7df, deterministic-attended-workflows-943570, deterministic-reuse-workflows-f70c33,
  full-repo-bar-tests-2591de. Filed already as KICK-dKeptSession-87 (LOW).
- Old trees ARE retired (11 trees, 17 `tree_built` rows); old VERSIONS are not.
- `fts_*` and `leg_row` tables are written by the unlanded dTotalRecall branch into the same file.
- An extractor's version hashes its module's whole import closure, so any edit to `tag_index.py` or a module it
  imports is a full new set of rows.
- C: reads at about 26 MB/s sequential uncached (the 12.6 GB copy took 478 s), so footprint is wall time.

## The root, isolated

On a clean index (270 MB, the one version this worktree derives) the UNMODIFIED check takes 85 s. So the cost is the
dead versions' rows, not the checks.

## The fix, prototyped (a patched copy of the module held in the building session's scratch, run on private files)

Two additive indexes on `path_row`, no schema bump: `(extractor, version)`, and a partial
`(path, blob, extractor, version, conf) WHERE kind='parsed'`. `VIEW_JOIN` starts from `view_version` by CROSS JOIN, because
without it the planner still scans. `read_defined` drops DISTINCT. `_write_parsed` returns at once on no blobs. The sweep
deletes only what the trees and dirty rows it drops held. `--gc` keeps the full sweep.

| index | tree | before wall / cpu | after wall / cpu |
|---|---|---|---|
| 12.6 GB copy | built | 835.7 / 369.3 | 65.3 / 26.7 |
| 12.6 GB copy | unbuilt | 1843.4 / 561.7 | 122.1 / 41.0 |
| 3.7 GB, 12 planted dead versions | built | 173.1 / 117.0 | 90.3 / 28.5 |
| 3.7 GB, 12 planted dead versions | unbuilt | 405.6 / 171.7 | 166.4 / 38.3 |

Output byte-equal on both built pairs and on the 3.7 GB unbuilt pair. The 12.6 GB unbuilt pair differs in the summary's
parse counts alone, because the first run parsed 23 blobs and the later one found them parsed.
The walls were taken on a machine running other bars, so they are not one machine state. CPU is the steadier column.
The first open after landing builds the two indexes: about 205 s under the write lock and 1 GB of disk, once per node.
Not in the prototype: dirty rows an overlay replaces must feed the same targeted removal, or they stay until `--gc`.
