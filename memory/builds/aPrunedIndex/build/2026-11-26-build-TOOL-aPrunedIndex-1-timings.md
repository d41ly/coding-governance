# aPrunedIndex — `gov_tag.py check` before and after, on one private copy of the node's index

**Serves:** journal TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3
**Caused-by:** TOOL-aPrunedIndex-1

The main loop ran these on 2026-11-26 at `57c8f95e6`, over one copy of `<git-common-dir>/gov/index-s3.db` taken with a plain
file copy on 2026-11-25 at 22:55 (12,586,708,992 bytes, the live file's size and mtime unchanged across the copy) (PINNED, 2026-11-26).
The driver loaded `tag_index.py` either at BASE `3d6c1702a` or at the build's tip into one process, pointed
`derive_index_path` at the copy, and called `gov_tag.main(["check"])`. Both read the extractor versions from the file on
disk, so both serve the same rows; the first run parsed every blob again because the build's edits are a new version.
The machine ran other sessions' work throughout, so wall time is noisy; CPU is the steadier figure. Nothing opened the live
index.

| Step | Code | What | Wall s | CPU s |
|---|---|---|---|---|
| 1 | BASE | `check`, every blob parsed at the new version (15,031) | 1002.8 | 437.1 (PINNED, 2026-11-26) |
| 2 | tip | the first open, which builds `path_row_version` and `path_row_named` | 79.2 | — (PINNED, 2026-11-26) |
| 3 | tip | `check` | 79.8 | 23.2 (PINNED, 2026-11-26) |
| 4 | tip | `check` | 98.9 | 24.5 (PINNED, 2026-11-26) |
| 5 | — | `DROP INDEX` of the two | 1.0 | — (PINNED, 2026-11-26) |
| 6 | BASE | `check` | 361.0 | 260.4 (PINNED, 2026-11-26) |

- Outputs 3, 4 and 6 are byte-equal under `cmp`. Output 1 differs from them on the summary line's parse counts alone,
  `15031 blobs parsed, 15111 extractor runs` against `0 blobs parsed, 0 extractor runs` (PINNED, 2026-11-26).
- The two indexes add 1,052,467,200 bytes to the copy (13,896,175,616 after step 2) (PINNED, 2026-11-26).
- On a built tree the leg's own work falls from 361 s to 80–99 s wall, and from 260 s to 23–25 s CPU (PINNED, 2026-11-26).
- Not measured: the tip parsing every blob of a new version; BASE's first run did that here. The diagnosis measured a full
  build from nothing on a clean 270 MB file at 173 s with the prototype (PINNED, 2026-11-25).
