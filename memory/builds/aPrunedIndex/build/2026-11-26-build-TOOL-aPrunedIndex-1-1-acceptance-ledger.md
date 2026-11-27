# TOOL-aPrunedIndex-1 — acceptance ledger

**Serves:** journal TOOL-aPrunedIndex-1
**Caused-by:** TOOL-aPrunedIndex-1

No merge bar, no self-test suite and no gate leg ran in this pass, and nothing here opened either live index
file: its mtime reads 2026-11-25 22:11:27 before the pass and after it. Every reading is node a's, 2026-11-26,
from base `b1f8fcccf`, by `--fixture` plants and by probes over private copies in the run's scratch. The
`dead-versions` row's RED-first observation, and the legs of section 7, are owed at the close. The staged reds were observed afterwards at `57c8f95e6`, as the seen-red lines below record.

The four runs of AC4 print `RED · 9 red` under both sources. The nine are unlisted file:line citations in the
diagnosis and the two audit records of this build, committed before this pass. They are owed a
`positional.py pin` before the bar.

**Evidences:** TOOL-aPrunedIndex-1
- AC1 — `python tools/playbook/gov_tag.py --fixture --plant dead-versions` — exit 0: `read_defined` 303 steps then 304, the definitions 447 then 448, LIKE 310 then 311, namespace state 300 then 301, the span population held, over 16 path rows padded to 656. With `VIEW_JOIN` alone in today's order, patched in memory, `read_defined` went from 317 to 10,477 and the plant exited 1. With `path_row_version` out of `SCHEMA` it went from 463 to 9,184 and exited 1.
- AC2 — `dead-versions` — its tag read took 1,025 steps before the 500 rows and 1,025 after, the row the same. With `read_rows` building it on `VIEW_ROWS`, patched in memory, it went from 151 to 3,651 and the plant exited 1. (PINNED, 2026-11-26)
- AC3 — `dead-versions` — with `path_row_version` dropped, `read_defined` went from 463 steps bare to 9,184 over the pad. The reopen through `load_index` gave the index back, 656 path rows and stamp 3. With the pad rolled back, patched in memory, the count stayed at 463 and the plant exited 1.
- AC4 — `gov_tag.py check` — four runs in alternation over one private copy of 4,047,327,232 bytes and 5,986,796 path rows, 12 dead versions padded, 928,535 bytes of output each and the four byte-equal under `cmp`. BASE: 179.3 s wall and 111.6 s CPU, then 166.1 s and 110.1 s. The unit: 89.2 s and 29.8 s, then 136.7 s and 31.5 s. The copy held `path_row_version` for all four, built by the unit's first open in 53.5 s with 5,986,796 rows. The machine ran other work beside them. (PINNED, 2026-11-26)
- AC5 — `EXPLAIN QUERY PLAN` — on that copy, `POINT_ROWS` with `p.tag=?` searches `path_row_tag`, with `p.path=?` searches `path_row_key`, and `VIEW_ROWS` with `p.kind='tag'` searches `path_row_version`. The grep over `tools/playbook/tag_bundle.py` prints the query of `read_node_spans`.
- AC6 — `grep -c "DISTINCT p.tag" tools/playbook/tag_index.py` — prints 0. `path_row_version` counts 3 in `tools/playbook/tag_index.py` and 1 in `tools/playbook/README.md`, and `grep -n "SQL index" help/tags.md` prints the sentence.
- AC7 — `python tools/playbook/gov_tag.py --fixture --plant <case>` — `two-versions`, `served-across`, `extractor-edit`, `charter-dirty` and `bundle-manifest` each exited 0, and so did `held-open`, `schema` and `queued-writers`.
- AC8 — `dead-versions` — its building lines count 0 at the first build, 1 at the reopen, naming `path_row_version`, and 0 on the complete file. With `load_index` printing at every open, patched in memory, they counted 1, 1 and 1, and with it printing none 0, 0 and 0, and the plant exited 1 each time.
- AC9 — `PRAGMA max_page_count` — under the cap `load_index` raised a `TagError` reading `cannot be opened: database or disk is full`, the file held no `path_row_version`, `PRAGMA integrity_check` read `ok` and 5,000 rows stood. With no cap the same open returned and the index was back over 5,000 rows. (PINNED, 2026-11-26)
- AC10 — `SELFTEST_ROWS` — the probe printed one `dead-versions` row, 0 and `reads cost their own version's rows`. `grep -c "bundle plant" tools/playbook/tag_bundle.py` printed 0, `tag plant` is in the docstring, the two arm lines and the two summary lines, `the tag index's row plants` counted 1 in each of `tools/gate-legs.json` and `tools/govkit/registry.toml`, and the old words counted 0 in the second.
- seen-red — `tags bundle selftest` — red `57c8f95e6` — green `57c8f95e6` — `dead-versions`: `VIEW_JOIN` alone in today's order; the `path_row_version` statement removed from `SCHEMA`; `read_rows` building a tag read on `VIEW_ROWS`; the dead pad rolled back after its rows are counted; `load_index` printing its line at every open; and printing none: each exits 1 (PINNED, 2026-11-26)
