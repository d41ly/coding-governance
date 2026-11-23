# TOOL-dTotalRecall-23 — the memory legs read the one index's rows for unchanged blobs and re-parse only changed ones

**Status:** CLOSED · rev-3 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 19 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0234@2a5b797c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-21 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-23-deviation-231.md](../build/2026-10-26-build-TOOL-dTotalRecall-23-deviation-231.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-build-TOOL-dTotalRecall-23-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dTotalRecall-23-1-acceptance-ledger.md) | log | — |
| [2026-11-22-build-TOOL-dTotalRecall-23-1-builder-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-23-1-builder-return.md) | journal | — |
| [2026-11-22-build-TOOL-dTotalRecall-23-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-23-reground-return.md) | research | — |
| [2026-11-23-build-TOOL-dTotalRecall-23-deviation-1007.md](../build/2026-11-23-build-TOOL-dTotalRecall-23-deviation-1007.md) | deviation | — |
| [2026-11-23-build-TOOL-dTotalRecall-23-red-fix-21.md](../build/2026-11-23-build-TOOL-dTotalRecall-23-red-fix-21.md) | red-fix | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-23-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-23-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-23-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-23-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Make the memory legs stop re-parsing the whole memory tree on every run. A leg's per-record parse
becomes a pure reader whose product is stored as rows in the one index, keyed by blob, so a run
reads rows for every blob the index already holds and parses only the blobs that changed. Memory
hygiene took 83 s at 54 MB, about 18 minutes at ten times that tree (gap-mem-43, PINNED there).
On node d it took 174.8 s at this spec's base and 157.3 s at `f711a956`, over 207.8 MB in
14697 tracked files under `memory/` (PINNED 2026-11-22, §8 F4).

## 2. Scope (IN)

Preconditions this unit calls and does not build, each landed and CLOSED: the index file
`tools/playbook/tag_index.py#derive_index_path` (`<git-common-dir>/gov/index-s<INDEX_SCHEMA>.db`), its
connection `tag_index.py#load_index`, the writer `tag_index.py#build_index(root, tree, ctx, con, stats)`
and its sweep `tag_index.py#remove_unheld_rows`, both reached through `tag_index.py#load_view`
(PLAY-dOrderedCharter-19 S4, -51, -55 S16); the module-closure version rule
`tools/memory-tree/import_walk.py#derive_module_closure` (PLAY-dOrderedCharter-44 S3, -55 S15); and
`corpus_ids.py#walk`'s per-process memo, which `gotchas.py --check-with-ids` arms so an unscoped hygiene
run walks the corpus once (TOOL-aHastenedSweep-4).

- **S1** — The leg-row table. `leg_row(blob, reader, version, payload)` in the index file, created
  `IF NOT EXISTS` by its one writer, `build_leg_rows(con, root, tree, entries)` in
  `tools/memory-tree/tree_lib.py`. `tag_index.py#build_index` calls it inside its `BEGIN IMMEDIATE`
  block, after `remove_unheld_rows`, over the tree's `(path, blob)` entries. For each blob under the
  conf's `MEMORY_ROOT` that `leg_row` lacks at a reader's current version, it reads the blob through
  `read_blobs_at` at the tree and writes the reader's row; then it clears every row whose blob no
  `tree_path` or `dirty_path` row holds, as `remove_unheld_rows` clears `blob_row`. A reader whose
  module, params or call raises writes no row for it and never fails the build. Observed by AC1 and
  AC4.
- **S2** — The readers. `LEG_READERS` in `tree_lib.py` maps a reader name to a `<module>:<function>`
  reader and a `<module>:<function>` params function, the tag index's extractor spelling
  (`tag_index.py#load_extractors`), each module loaded from memory-tree's own directory by a computed
  path, so the tag index's own closure does not take it in. `params(root)` returns `(key, arg)`: `key`
  a canonical string and `arg` what the reader takes. A reader is `fn(text, arg)`, `text` None for a
  blob that is not UTF-8, and returns a JSON-able product. Its version, `derive_leg_version(name,
  root)`, is DERIVED: the first 12 hex of the SHA-256 over the bytes of every module of its module's
  closure under `derive_module_closure`, in path order, then `key`. Three readers:
  - `unfenced-head`, `tree_lib:extract_head_lines`: the first `BIND_HEAD_LINES` lines
    `tree_lib.py#unfenced` yields, or `{"undecodable": true}`; its key is empty.
  - `id-harvest`, `corpus_ids:extract_ids` (S4); its params, `corpus_ids:derive_id_params`, return the
    grammar bundle `corpus_ids.py#grammar` builds for root as `arg` and, as `key`, that bundle's `ID`
    pattern and its four anchor patterns (`id_grammar.py#build_grammar`), so every conf input the
    grammar folds in moves the version.
  - `spec-head`, `design_lib:extract_spec_head`, beside the two readers it calls: a spec's first five
    unfenced lines, its `design_lib.py#read_spec_writes` words and its `design_lib.py#read_spec_edges`
    consumes targets; its key is empty.
  Observed by AC4 and AC7.
- **S3** — The row read, `read_rows_at(root, paths, reader)` in `tree_lib.py`, returning
  `({path: product}, counts)` over working-tree paths. One `git ls-files -s -z` names each path's
  blob and one `git diff --name-only --no-renames -z HEAD` the paths that differ from HEAD, as
  `tag_index.py#build_overlay` reads them. A path absent from that diff whose blob `leg_row` holds at
  the reader's current version is answered from the row. Every other path, edited, staged, untracked
  or absent from git's index, is read through `read_text` and parsed, a `UnicodeDecodeError` handing the
  reader None and an `OSError` standing as the product `{"unreadable": "<message>"}`. The index file
  is `tag_index.py#derive_index_path`'s, its kit reached through memory-tree's inline `resolve_kit_dir`
  block (`backlog.py#resolve_kit_dir`) at call time, opened read-only as a SQLite URI
  (`file:...?mode=ro`), one `SELECT` per 999 blobs. An absent playbook kit, an absent file, a file
  without `leg_row` or any `sqlite3.Error` is the index-absent case. `counts` is `{"index": n,
  "parsed": m, "absent": bool}`. Observed by AC1, AC2, AC3 and AC5.
- **S4** — The adopters, each output unchanged:
  - `corpus_ids.py#walk` splits its per-line loop into the pure `extract_ids(text, grammar)`: per line,
    its number, the `missing:` ids, the anchor it defines with the line's text (check 13's ask row reads
    it), the ids it cites and its backticked and link-target tokens, each read from the line with its
    `missing:` forms blanked, as today. The path-dependent classification stays in `walk`, every
    `continue` with it, so `_walk_continues`' population is unchanged. `walk` reads its corpus
    through `read_rows_at` under `id-harvest`; an undecodable or unreadable path is read by `read` as
    today.
  - `tree_lib.py#read_bindings` classifies each record from its `unfenced-head` product, an
    undecodable one skipped and an unreadable one its `unreadable:` row, as today. A keyword-only
    `counts` dict, when passed, gains the call's counts; every other caller passes none.
  - `gen_build_index.py#collect` reads each spec through `read_rows_at` under `spec-head` and a new
    `parse_spec_head(lines, path, alt)`, which `parse_spec_text` also calls on its own first five
    unfenced lines; an undecodable spec is read by `parse_spec` as today.
  Observed by AC1, AC6 and AC7.
- **S5** — The recall leg, no code. TOOL-dTotalRecall-21 S8 grades the `check-recall` leg over the
  node's index through `load_served_set`, whose `write_recall_rows` extracts only the (path, blob)
  pairs `fts_blob` lacks (its F5 and F6), and TOOL-dTotalRecall-9 S4 keeps that leg through `record
  find`; unit 21's S5 takes out `check-recall.py#build_served_dir`, the throwaway index this item once
  seeded. NOT OBSERVED by this unit's criteria: unit 21's AC3 observes the leg extracting `0 blob(s)`
  for a committed, unchanged file.
- **S6** — The announce line, `leg rows: <reader> <n> from the index, <m> parsed`, or `leg rows:
  <reader> index absent, <m> parsed`. `corpus_ids.py --check` prints it among its notes, prefixed
  `HYGIENE advisory ` as its other non-gating notes are, since `check-memory-hygiene.sh#add_offender_keys`
  keys every other line of a red run; `gen_build_index.py --check` and `--print-bindings` print one per
  reader on stderr, summing every `read_bindings` call of the run. Observed by AC5 and AC6.
- **S7** — The fixture, `write_leg_fixture(root)` in `tree_lib.py`: a scratch git repository holding a
  conf, an empty namespace registry and a planted memory tree that `gen_build_index.py --check`
  accepts. One record carries its Serves line inside a fence, one is undecodable, one is CRLF, one is
  a spec, one cites an id and a dead path, one is edited and uncommitted, and one is untracked.
  Observed by AC1 to AC5 and AC7.

## 3. Non-goals (OUT)

- Building or freshening the index from a leg. A leg only reads it, so a fresh clone with no index
  parses everything, as today, and says so (§8 F1).
- The hygiene leg's own bash checks and the rest of `gotchas.py --check`, whose cost outside the
  shared walk is path matching in `gotchas.py#selectable`, not a parse (§8 F4). Each can join later by
  adding a reader to `LEG_READERS`. That narrowing is deviation record 231.
- Reads pinned at a revision, such as `gen_build_index.py#read_backlog_at_rev`: they keep reading blobs
  through `read_blobs_at`; `read_rows_at` reads the working tree only, which every adopter reads.
- Rows for a worktree's dirty blobs: `build_overlay` writes none, so an edited file is parsed on
  every run until its commit.
- `gov_tag.py --gc`: `tag_index.py#remove_dead_versions` collects no `leg_row` version, so an edited
  reader's old rows stay until their blobs leave every tree; TOOL-dTotalRecall-43 S21 moves the rows
  onto `blob_row`, which `--gc` collects.
- The index schema, its freshness ledger and its writer: PLAY-dOrderedCharter-19 S4 and -44. The FTS
  tables and their freshness: unit 21's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-21` — `build_fts_rows` and `fts_blob`, the per-blob rows the recall leg reads for an unchanged blob: unit 21's S8 grades the `check-recall` leg over them, which carries this unit's S5, and without it that leg re-extracts its whole corpus
- **consumes-from** `TOOL-dTotalRecall-9` — `record find`'s `check-recall` leg, which grades through unit 21's served sets (its S4); S5 names that leg as the recall half of this unit's goal and adds no code to it
- **hands-off** `TOOL-dTotalRecall-43` — `leg_row` and `LEG_READERS`, which that unit moves onto PLAY-dOrderedCharter-44's extractor mechanism (the round-1 audit's id 27)

## 4. Design

### The row and its key

```sql
CREATE TABLE IF NOT EXISTS leg_row(blob TEXT, reader TEXT, version TEXT, payload TEXT,
                                   PRIMARY KEY (blob, reader, version));
```

`payload` is canonical JSON, such as `{"head": ["**Serves:** research X-1", ...]}` or
`{"undecodable": true}`. A blob is content-addressed and a reader is a pure function of the blob's
bytes and its params, so a row is right for every path, branch and worktree holding the blob under
the same params. The version moves when a module of the reader's closure moves or its params do, so
an edited reader or a changed id grammar is never answered by an old row. Each walk's
path-dependent work stays in the walk and runs on the product every time: `corpus_ids`' present-tense
and append-only tests, `read_bindings`' typed-name rule, and the spec's id taken from its file name.

### The write

`build_index` returns at once for a tree `tree_built` holds under its digest, and that digest folds in
the tag extractors' versions, not the leg readers'. So rows for a tree are written when the tree is
first built: after any commit, since the tree moves, and after an edit to `tree_lib.py`, which sits in
`tag_index.py`'s own closure (`tag_index.py#derive_extractor_versions`) and so rebuilds every tree.
A reader edit or a conf edit not yet committed costs parses until the next tree, announced (§8 F5).

### The read

```
read_rows_at(root, paths, reader) -> ({path: product}, {"index": n, "parsed": m, "absent": bool})
```

1. Resolve each path's blob, and the paths that differ from HEAD (S3).
2. Reach `tag_index.derive_index_path(root)` and open that file read-only; any failure is the
   index-absent case (§8 F6).
3. One `SELECT blob, payload FROM leg_row WHERE reader = ? AND version = ? AND blob IN (...)` per 999
   blobs.
4. Read and parse the misses through `read_text` and the reader.

### Inventory

Minted: the table `leg_row`; the functions `build_leg_rows`, `read_rows_at`, `derive_leg_version`,
`extract_head_lines`, `extract_ids`, `derive_id_params`, `extract_spec_head`, `parse_spec_head` and
`write_leg_fixture`; the constant `LEG_READERS`; the reader names `unfenced-head`, `id-harvest` and
`spec-head`; the announce line. Each function passed `python tools/lexicon/lexicon.py --suggest <name>
--as py.function` on 2026-11-22, and a helper the pass adds leads with a verb of `.lexicon.conf`'s
VERBS table.

### Migration

None. `tree_lib.py`'s edit moves every tag extractor's version, so the first tag build after landing
re-runs them once, as any `tree_lib.py` edit does, and fills `leg_row`. A node whose index is not yet
rebuilt parses everything and prints the index-absent or the counted line.

### Rollout

Live on landing. Output is byte-identical to a full read (AC1, AC6, AC7), so no switch is needed.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/corpus_ids.py`: `extract_ids` split from `walk`, `derive_id_params`
- `tools/memory-tree/design_lib.py`: `extract_spec_head`
- `tools/memory-tree/gen_build_index.py`: `parse_spec_head`, the S6 lines, the arm
- `tools/playbook/tag_index.py`: `build_index` calls `build_leg_rows`
- `help/tags.md`, one sentence: the index holds the memory legs' rows too, and the legs print `leg rows:`
- `memory/map/generated/symbols.json`, regenerated by the codebase-map kit's generator

### Alternatives rejected

- **Register the readers as tag extractors now.** `blob_row` rows are tag rows that every tag check
  reads through `path_row`, and the extractor version folds in no params, so a FAMILIES edit would
  serve an old harvest; TOOL-dTotalRecall-43 S21 adds the params digest and makes that move.
- **Change `read_blobs_at`'s return type behind a keyword.** Its 15 call sites pin its
  `{(rev, path): text}` shape (DERIVED, `git grep -n "read_blobs_at(" -- tools`). `read_rows_at`
  composes `read_text` instead.
- **The leg writes the rows it parsed.** That makes a second writer of the index, and
  PLAY-dOrderedCharter-19 S4 makes `build_index` its writer (§8 F1).
- **Store the whole text per blob.** Reading costs little: `corpus_ids.py#read` took 0.8 s of a
  19.4 s profiled walk (PINNED 2026-11-22, §8 F4). The parse is the cost.

## 5. Production-readiness checklist

- security — no new write path: the leg opens the index read-only, and the one writer runs inside
  `build_index`'s transaction.
- perf / scale — one `git ls-files`, one `git diff` and one query per 999 blobs per adopter call; the
  targets are `walk`, `read_bindings` and `collect`'s spec parse, about 15 s of the 157.3 s leg (DERIVED
  from §8 F4's PINNED times). A cold build, as on a CI clone, pays the three readers over every memory blob
  once inside the `tags` leg, its cost DERIVED by the pass; that leg's evidenced maximum is 210 s (PINNED,
  `tools/run-gates/ceiling-evidence.txt`) under its 420 s ceiling (PINNED, `tools/gate-legs.json`).
- error / empty / loading states — an absent kit, file or table, or a corrupt file, is the index-absent
  case, announced; a decode or read failure keeps each walk's current behaviour; a reader that raises
  in `build_leg_rows` writes no row and leaves the tag build green.
- observability — the S6 line on every adopted run.
- risks — a stale index only costs parses; a reader whose params miss a conf input it reads would
  serve a stale product, which AC7's grammar flip pins.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — one re-run of the tag extractors, as §4 says.
- user docs — `help/tags.md` gains one sentence, as §4 lists.

## 6. Acceptance criteria

- **AC1** — When a probe calls `write_leg_fixture` from `tools/memory-tree/tree_lib.py` under `%TEMP%`,
  builds its index with `tag_index.load_view` over `derive_context(root, <its registry>)`, and calls
  `read_bindings` there twice, once with the index file present and once with it moved aside, the two
  dicts are equal and the first call's `counts` answers every committed unchanged record from the index.
  Red when: the planted fenced Serves line, the CRLF record or the spec reads differently from the row
  than from the text.
- **AC2** — When the fixture commits one more record after the index build and the probe runs
  `read_rows_at` over the fixture's paths, `counts` shows `parsed` 3 (the new commit's blob, the edited
  file and the untracked file) and every other path `index`.
  Red when: an unchanged blob is re-parsed, or a changed one is served from a row.
- **AC3** — When the fixture's uncommitted edit adds a Serves line, `read_bindings` reports the edited
  binding, not the committed one.
  Red when: a working-tree path that differs from HEAD is answered from its HEAD blob's row.
- **AC4** — When the probe inserts a `leg_row` for a fixture blob under another `version`,
  `read_rows_at` parses that blob, and `build_leg_rows` writes rows under the derived version only;
  when `LEG_READERS` names a module that does not load, `load_view` completes and writes the other
  readers' rows; after a commit edits a record and the index builds again, no `leg_row` row names the
  old blob.
  Red when: a row written by another version of a reader is served, a reader's failure fails the tag
  build, or rows outlive every tree holding their blob.
- **AC5** — When the index file is absent, `read_rows_at` returns every path `parsed` and
  `gen_build_index.py --print-bindings` prints `leg rows: unfenced-head index absent` on stderr.
  Red when: an absent index raises, or is silent.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --check` runs over the fixture with and
  without the index, its output is identical except the `leg rows:` lines.
  Red when: `parse_spec_head` and `parse_spec_text` disagree on a planted spec header.
- **AC7** — When `python tools/memory-tree/corpus_ids.py --check` runs over the fixture with and
  without the index, its output is identical except the `leg rows:` note; when the fixture's
  `FAMILIES` conf key gains a family between two runs, every `id-harvest` path is parsed.
  Red when: `extract_ids` reads differently from the walk's loop, or a changed id grammar is answered
  from rows its old params wrote.

## 7. Gates

`memory hygiene` · `build-index selftest` · `corpus-ids selftest` · `gotchas selftest` · `memory-hygiene self-test` · `tier2-review self-test` · `policy fixtures` · `govkit acceptance matrix` · `playbook render selftest` · `tags (the resolver's checks)` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · a `--selftest` arm over `write_leg_fixture`, staged by `read_rows_at` serving a dirty path from its HEAD row · none
New arm: tools/memory-tree/corpus_ids.py · covers AC7 · a selftest arm comparing the walk with and without the index, staged by `id-harvest`'s params leaving out the family list · none

## 8. Open questions

- **F1 — Does a memory leg bring the index current before it reads, or read only what is there?**
  Options: (a) read only, so a cold or absent index costs today's full parse, announced; (b) the leg
  runs the index's incremental build first; (c) the leg writes rows for what it parsed. (c) makes a
  second index writer, against PLAY-dOrderedCharter-19 S4. (b) makes a fresh CI clone build every
  registered extractor's rows to run one leg, which costs more than the leg does today. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the most capable option no veto removes. widens: none ·
  relaxes: none
- **F2 — Is the stored product the parse result or the text the parse reads?** Options: (a) each
  walk's path-independent product, its conf inputs in the version; (b) each walk's final dict. (b)
  depends on a file's path as well as its blob, so one blob at two paths would need two rows.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — The parents are unbuilt at base `462d20f3`.** `index.db`, `build_index`,
  `common_git_dir`, unit 21's `build_fts_rows` and unit 9's leg are specced and DEFERRED.
  RESOLVED (agent, 2026-10-26, delegated): this spec calls them as their specs name them, and the
  build run re-grounds on the landed code before its pass, rung 1. widens: none · relaxes: none
  Re-grounded at `f711a956` by rev-3: the index, its writer and its version rule landed as §2 names
  them, and unit 21's rev-3 leaves S5 nothing to seed.
- **FACT-QUESTION · F4 — Which of the hygiene leg's walks are per-blob parses worth a row?** Probe:
  time `bash tools/memory-tree/check-memory-hygiene.sh` and each Python engine it delegates to, in a
  clone of the run branch with this build's specs committed, then profile the slowest with `cProfile`.
  Observation, node d, 2026-10-26, at `fb872a37e` (PINNED): the leg 174.8 s; `gotchas.py --check`
  37.6 s, of which `corpus_ids.walk` 17.9 s and path matching in `selectable` most of the rest;
  `corpus_ids.py --check` 15.7 s, mostly `walk`; `gen_build_index.py --check` 4.4 s. Observation,
  node d, 2026-11-22, at `f711a956` (PINNED): the leg 157.3 s; `gotchas.py --check-with-ids`, the one
  walk an unscoped run makes, 30.3 s, profiled 49.2 s with `walk` 19.4 s and `selectable`
  9.7 s; `gen_build_index.py --check` 30.6 s, profiled 45.1 s with `read_bindings` 5.2 s and
  `collect`'s `parse_spec` 3.3 s; `--print-bindings` 9.7 s, profiled 13.9 s with `read_bindings` 5.1 s.
  Unprofiled and in-process (PINNED 2026-11-22): `walk` 6.6 s over 14697 files, `read_bindings` 3.1 s
  over 10759 records (PINNED), and `parse_spec` 2.1 s over 3104 specs (PINNED), `corpus_ids.py#read`
  0.8 s of the profiled walk (PINNED). Liveness: an engine whose time sits outside any per-file loop would show it, as `selectable` does.
  RESOLVED (agent, 2026-10-26, delegated): `corpus_ids.walk`, `read_bindings` and the spec-header read,
  rung 2. The bash checks and `selectable` are departures, recorded as deviation 231. widens: none ·
  relaxes: none
- **F5 — The landed `build_index` returns at once for a built tree; where are leg rows written?**
  Options: (a) inside `build_index`'s transaction, rows written when a tree is first built; (b) a pass
  of its own in `load_view` on every call, as unit 21's F5 writes recall's rows; (c) the leg readers'
  versions folded into `tree_built`'s digest. (b) adds a write transaction and a tree scan to every tag
  verb; (c) rebuilds every tag row on a conf edit no tag extractor reads. RESOLVED (agent, 2026-11-22,
  delegated): (a), rung 3, S1 as written; a reader or conf edit not yet committed costs parses,
  announced, under F1's (a). Brief: `2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief`.
  widens: none · relaxes: none
- **F6 — How does a memory-tree leg find the index file?** Options: (a) `tag_index.py#derive_index_path`,
  its kit reached at call time through `resolve_kit_dir`, an absent kit the index-absent case; (b) a
  third inline `common_git_dir` copy and the file name spelled in `tree_lib.py`. (b) spells the file
  name and `INDEX_SCHEMA` twice, and `derive_index_path` is the one spelling every reader uses.
  RESOLVED (agent, 2026-11-22, delegated): (a), rung 1, one fact in one place. Brief:
  `2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief`. widens: none · relaxes: none
- **F7 — `parse_spec_text` now reads a spec's Files touched and edges from its whole text; how does
  `collect` keep its output from a row?** Options: (a) a third reader, `spec-head`, holding the first
  five unfenced lines with the writes and the consumes; (b) `collect` keeps reading text, departing
  from deviation 231's after-clause. (b) gives up 2.1 s of `collect` per run (PINNED 2026-11-22,
  §8 F4) and needs a further deviation. RESOLVED (agent, 2026-11-22, delegated): (a), rung 3, the
  option the carried clause admits. Brief: `2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 23, the brief's I11 and I14, scout B's
  row for cl-0234, unit 21's `fts_blob`, and the hygiene leg's timing at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved. The Carries pin re-pinned from `eb7b1784` to `2a5b797c`, the hash the as-built view gives cl-dClosedLoop-0234 once deviation 231 states its whole clause as After.
- rev-3 · 2026-11-22 · §1 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · §3 · §4 · §5 · AC1 · AC4 · AC5 · AC6 ·
  AC7 · §7 · §8 · §10 · per `2026-11-22-prompt-TOOL-dTotalRecall-23-reground-brief`, re-grounded over
  HEAD `f711a956`: the index is `index-s<INDEX_SCHEMA>.db`, found through `derive_index_path` (F6), and
  `build_index` returns early for a built tree (F5), so the third `common_git_dir` copy and its
  parity row go; reader versions take the module-closure rule; `read_rows_at` reads the working tree
  only, no adopter reading a revision; the walk runs once per unscoped run since TOOL-aHastenedSweep-4;
  `parse_spec_text` gained writes and edges, so a `spec-head` reader serves `collect` (F7); unit 21's
  rev-3 grades the recall leg over the node's index, so S5 builds nothing and its criterion and arm
  go, the old AC8 now AC7; the row sweep, the reader-failure rule and the S6 channels are named; F4
  re-measured; `harvest_ids` is `extract_ids`, a VERBS verb.

## 10. Reuse audit

The seams extended are `tools/playbook/tag_index.py#build_index`, the index's one writer, whose
transaction `build_leg_rows` joins, and `tools/memory-tree/tree_lib.py`: `read_text` is the miss path
of `read_rows_at`, `read_blobs_at` the write path's reader, and the walks adopted are
`corpus_ids.py#walk`, `tree_lib.py#read_bindings` and `gen_build_index.py#collect`'s spec read
through `#parse_spec_text`. The version rule is the tag index's, `import_walk.py#derive_module_closure`
over a reader's module, and the reader spelling is `tag_index.py#load_extractors`'
`<module>:<function>`. `python tools/codebase-map/reuse_lookup.py "store a per-blob parse product in
the tag index under a derived extractor version"` ranked `read_blobs_at` (SEAM, fan-in 11) and generic
`parse` and `derive` stems, and no per-blob parse store outside the tag index's own tables, which §4
rejects for now. Scout B's line numbers have all moved: read the symbols. Scout B gave `read_text` a
fan-in of 109, counting every `read_text(` token across four definitions. Scout B named
`read_blobs_at` and `read_text` as where the cost sits; the timing probe (§8 F4) puts it in the per-line
parse of `walk`, `read_bindings` and `parse_spec_text`, with `corpus_ids.py#read` under a second.

Recall terms used: `python tools/memory-recall/query.py "how do the memory legs avoid re-reading the whole tree on every run" --terms "index.db blob_row unchanged blobs re-parse memory hygiene legs read_blobs_at read_text NT-15 gap-mem-43"`
