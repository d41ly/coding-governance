# TOOL-dTotalRecall-23 — the memory legs read the one index's rows for unchanged blobs and re-parse only changed ones

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 19 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0234@2a5b797c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-21 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-23-deviation-231.md](../build/2026-10-26-build-TOOL-dTotalRecall-23-deviation-231.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Make the memory legs stop re-parsing the whole memory tree on every run. A leg's per-record parse
becomes a pure reader whose product is stored as rows in the one index, keyed by blob, so a run
reads rows for every blob the index already holds and parses only the blobs that changed. Memory
hygiene took 83 s at 54 MB, about 18 minutes at ten times today's tree (gap-mem-43,
night-pass-two.md:228-230). On node d at this spec's base it took 174.8 s (§8 F4).

## 2. Scope (IN)

Every surface below calls PLAY-dOrderedCharter-19 S4's index (`<git-common-dir>/gov/index.db`,
`tools/playbook/tag_index.py` `build_index`), PLAY-dOrderedCharter-44 S1 to S3's per-extractor
version rule and PLAY-dOrderedCharter-19 S10's `common_git_dir` as those specs name them. All three
are DEFERRED at base `462d20f3`.

- **S1** — The leg-row table. `index.db` gains `leg_row(blob, reader, version, payload)`, one row per
  blob and leg reader, written by `build_leg_rows(conn, root, blobs)` in
  `tools/memory-tree/tree_lib.py`. `tag_index.build_index` calls it in its own transaction, over every
  blob under the memory root it parses, the way it calls unit 21's `build_fts_rows`. No other writer
  exists. Observed by AC1 and AC4.
- **S2** — The readers. `LEG_READERS` in `tree_lib.py` maps a reader name to a pure function of a
  blob's text and to a `params(root)` function naming the conf inputs it reads. A reader's `version`
  is DERIVED: the first 12 hex characters of the SHA-256 of its module's bytes followed by
  `params(root)`, as PLAY-dOrderedCharter-44 S3 derives an extractor's from its module. This unit
  registers two readers. `unfenced-head` holds the first `BIND_HEAD_LINES` unfenced lines of a text
  with their line numbers, or `undecodable`, and its params are empty. `id-harvest` holds the
  per-line ids defined, ids cited, `missing:` forms and path tokens that `corpus_ids.walk`
  (`tools/memory-tree/corpus_ids.py:494`) reads from one file, and its params are the id grammar's
  pattern and the conf keys the harvest reads. Observed by AC4 and AC8.
- **S3** — The row read, `read_rows_at(root, requests, reader)` in `tree_lib.py`, returning
  `(products, counts)`. A request is `(rev, path)`, `rev` a revision or the constant `WORKTREE`. One
  `git cat-file --batch-check` (a revision) or one `git ls-files -s` plus one
  `git diff --name-only HEAD` (the working tree) resolves each path's blob. A blob whose `leg_row` the
  index holds at the reader's current version is answered from the row. Every other request is read
  through `read_blobs_at` (a revision) or `read_text` (the working tree) and parsed. A working-tree
  path that differs from HEAD, or is untracked, is never answered from a row. `counts` is
  `{"index": n, "parsed": m}`. Observed by AC1, AC2, AC3 and AC5.
- **S4** — The adopters, the per-record walks the hygiene leg runs. `corpus_ids.walk` splits its
  per-file loop into the pure `harvest_ids(text, grammar)`, read through S3 under `id-harvest`, and
  the path-dependent classification it keeps. That walk runs twice per hygiene run, in
  `corpus_ids.py --check` and in `gotchas.py --check`'s `load_defined_ids`. `read_bindings`
  (`tree_lib.py:471`) classifies each record from its `unfenced-head` product. `collect` in
  `tools/memory-tree/gen_build_index.py` reads each spec's status header through a new
  `parse_spec_head(lines, path, alt)` that `parse_spec_text` (`gen_build_index.py:491`) also calls.
  Every adopter's output is unchanged. Observed by AC1, AC6 and AC8.
- **S5** — The recall leg. The `check-recall` leg that unit 9's `record find` takes over builds a
  throwaway index for its served tree (`build_served_dir`, as unit 21 S8 leaves it). Before that
  build, it copies from the node's index the `fts_record`, `fts_chunk` and `fts_supersession` rows and
  the `fts_blob` row of every served blob that the node's `fts_blob` holds at the current `digest`.
  `build_index` then runs `build_fts_rows` only for the blobs left. Observed by AC7.
- **S6** — The announce line. Each adopter prints one line,
  `leg rows: <reader> <index> from the index, <parsed> parsed`, or
  `leg rows: <reader> index absent, <parsed> parsed` when no index file exists. A cold index is
  visible, never silent. Observed by AC5 and AC6.
- **S7** — The fixture, `write_leg_fixture(root)` in `tree_lib.py`: a scratch git repository holding
  a planted memory tree of records. One record carries its Serves line inside a fence, one is
  undecodable, one is CRLF, one is a spec, one cites an id and a dead path, one is edited and
  uncommitted, and one is untracked. Observed by AC1 to AC5 and AC8.

## 3. Non-goals (OUT)

- Building or freshening the index from a leg. A leg only reads it, so a fresh clone with no index
  parses everything, as today, and says so (§8 F1).
- The hygiene leg's own bash checks, about 113 s of its 174.8 s (§8 F4), and the rest of
  `gotchas.py --check`, whose cost outside the shared walk is path matching in `selectable`, not a
  parse. Each can join later by adding a reader to `LEG_READERS`. That narrowing is deviation record
  231.
- The index schema, its freshness ledger and its writer: PLAY-dOrderedCharter-19 S4 and
  PLAY-dOrderedCharter-44.
- The FTS tables themselves and their move into `index.db`: unit 21's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-21` — `build_fts_rows` and `fts_blob`, the per-blob rows a memory leg reads for an unchanged blob: S5 copies the rows `fts_blob` marks current, `build_fts_rows` runs for the rest, and `build_leg_rows` joins `build_index`'s transaction the same way
- **consumes-from** `TOOL-dTotalRecall-9` — `record find`'s `check-recall` leg, whose served index S5 seeds from the node's rows; the `record` and `section` rows its filters read are written by the served index's own `build_index`, since S5 seeds only the FTS rows
- **hands-off** `TOOL-dTotalRecall-43` — `leg_row` and `LEG_READERS`, which that unit moves onto PLAY-dOrderedCharter-44's extractor mechanism (the round-1 audit's id 27)

## 4. Design

### The row and its key

```sql
CREATE TABLE leg_row(blob TEXT, reader TEXT, version TEXT, payload TEXT,
                     PRIMARY KEY (blob, reader, version));
```

`payload` is canonical JSON, such as `{"head": [[3, "**Serves:** research X-1"], ...]}` or
`{"undecodable": true}`. A blob is content-addressed and a reader is a pure function of the blob's
bytes and its params, so a row is right for every path, branch and worktree holding the blob under
the same params. The version moves when the reader's module moves or its params do, so an edited
reader or a changed id grammar is never answered by an old row. Each walk's path-dependent work
stays in the walk and runs on the product every time: `corpus_ids`' present-tense and append-only
tests, and `read_bindings`' deviation-name rule.

### The read

```
read_rows_at(root, requests, reader) -> ({(rev, path): product}, {"index": n, "parsed": m})
```

1. Resolve the blobs in one call per state (S3).
2. Open `<common_git_dir>/gov/index.db` read-only (`file:...?mode=ro`, a SQLite URI). An absent
   file, or one without `leg_row`, is the index-absent case.
3. One `SELECT blob, payload FROM leg_row WHERE reader = ? AND version = ? AND blob IN (...)` per
   999 blobs.
4. Parse the misses through `read_blobs_at` or `read_text` and the reader.

`common_git_dir` reaches `tree_lib.py` as a third inline copy under the existing `common_git_dir`
parity row (PLAY-dOrderedCharter-19 S10), so no kit imports another. `corpus_ids.py` already imports
`tree_lib` (`corpus_ids.py:159-160`).

### Inventory

Minted: the table `leg_row`; the functions `build_leg_rows`, `read_rows_at`, `harvest_ids`,
`parse_spec_head`, `write_leg_fixture`; the constants `LEG_READERS` and `WORKTREE`; the reader names
`unfenced-head` and `id-harvest`; the announce line. Naming cells: each function is asked of the
lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None. A node without `leg_row` parses everything and prints the index-absent line. Its next index
build fills the table.

### Rollout

Live on landing. Output is byte-identical to a full read (AC1, AC8), so no switch is needed.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/corpus_ids.py`: `harvest_ids` split from `walk`
- `tools/memory-tree/gen_build_index.py`
- `tools/playbook/tag_index.py`: `build_index` calls `build_leg_rows`
- `tools/memory-recall/check-recall.py`: S5, wherever unit 9 has moved the leg's served build
- `tools/lib/resolve-python.test.sh`: the `common_git_dir` row gains `tree_lib.py`'s copy

### Alternatives rejected

- **Change `read_blobs_at`'s return type behind a keyword.** Three callers and a selftest arm
  (`gen_build_index.py:6316`) pin its `{(rev, path): text}` shape. `read_rows_at` composes it
  instead.
- **The leg writes the rows it parsed.** That makes a second writer of the index, and
  PLAY-dOrderedCharter-19 S4 makes `build_index` the only one (§8 F1).
- **Store the whole text per blob.** Reading a file costs little. The parse is the cost.

## 5. Production-readiness checklist

- security — no new write path: the leg opens the index read-only, and the only writer is
  `build_index`.
- perf / scale — one git call per state and one query per 999 blobs; the target is the two
  `corpus_ids.walk` runs, PINNED at 15.7 s and 17.9 s of one hygiene run (§8 F4).
- error / empty / loading states — an absent index, an absent table or a corrupt file is the
  index-absent case, announced; a decode failure keeps each walk's current behaviour.
- observability — the S6 line on every run.
- risks — a stale index only costs parses; a reader whose params miss a conf input it reads would
  serve a stale product, which AC8's grammar flip pins.
- testing — AC1 to AC8 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe calls `write_leg_fixture` from `tools/memory-tree/tree_lib.py` under
  `%TEMP%`, runs `python gov_tag.py --rebuild` in it, and calls `read_bindings` there twice, once
  with `index.db` present and once with it moved aside, the two dicts are equal and the first run's
  counts answer every committed unchanged record from the index.
  Red when: the planted fenced Serves line, the CRLF record or the spec reads differently from the
  row than from the text.
- **AC2** — When the fixture commits one more record after the index build and the probe runs
  `read_rows_at` over the tree, `counts` shows `parsed` 3 (the new commit's blob, the edited file
  and the untracked file) and every other request `index`.
  Red when: an unchanged blob is re-parsed, or a changed one is served from a row.
- **AC3** — When the fixture's uncommitted edit adds a Serves line, `read_bindings` reports the
  edited binding, not the committed one.
  Red when: a working-tree path that differs from HEAD is answered from its HEAD blob's row.
- **AC4** — When the probe inserts a `leg_row` for a fixture blob under another `version`,
  `read_rows_at` parses that blob, and `build_leg_rows` writes rows under the derived version only.
  Red when: a row written by another version of a reader is served.
- **AC5** — When `index.db` is absent, `read_rows_at` returns every request `parsed` and the
  adopter's line reads `leg rows: unfenced-head index absent`.
  Red when: an absent index raises, or is silent.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --check` runs over the fixture with
  and without the index, its output is identical except the `leg rows:` line.
  Red when: `parse_spec_head` and `parse_spec_text` disagree on a planted spec header.
- **AC7** — When the recall leg's served build runs over the fixture with the node's index present,
  its `fts_record` and `fts_chunk` rows equal a build from nothing, and its index line names only the
  blobs the node's `fts_blob` lacks as extracted.
  Red when: a row copied at another `digest` is served, or a copied row differs from a fresh
  `build_fts_rows` row for the same blob.
  fixture: needs unit 21's `build_fts_rows` and unit 9's leg landed; the build run has both.
- **AC8** — When `python tools/memory-tree/corpus_ids.py --check` runs over the fixture with and
  without the index, its output is identical except the `leg rows:` line; when the fixture's
  `FAMILIES` conf key gains a family between two runs, every `id-harvest` request is parsed.
  Red when: `harvest_ids` reads differently from the walk's loop, or a changed id grammar is
  answered from rows its old params wrote.

## 7. Gates

`memory hygiene` · `build-index selftest` · `corpus-ids selftest` · `gotchas selftest` · `memory-hygiene self-test` · `tier2-review self-test` · `govkit acceptance matrix` · `playbook render selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` · `memory-recall kit selftest`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · a `--selftest` arm over `write_leg_fixture`, staged by `read_rows_at` serving a dirty path from its HEAD row · none
New arm: tools/memory-tree/corpus_ids.py · covers AC8 · a selftest arm comparing the walk with and without the index, staged by `id-harvest`'s params leaving out the family list · none
New arm: tools/lib/resolve-python.test.sh · covers none · the `common_git_dir` parity row with `tree_lib.py`'s copy, staged by one byte changed in that copy · that suite's assertion count, raised by the row
New arm: tools/memory-recall/test_recall_floor.py · covers AC7 · the seeded served build equal to a cold build, staged by copying the rows of a blob `fts_blob` holds at another `digest` · none

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
- **FACT-QUESTION · F4 — Which of the hygiene leg's walks are per-blob parses worth a row?** Probe:
  time `bash tools/memory-tree/check-memory-hygiene.sh` and each Python engine it delegates to, in a
  clone of the run branch at `fb872a37e` with this build's specs committed, then profile the two
  slowest with `cProfile`. Observation, node d, 2026-10-26 (PINNED): the leg 174.8 s; `gotchas.py --check`
  37.6 s, of which `corpus_ids.walk` 17.9 s and path matching in `selectable` most of the rest;
  `corpus_ids.py --check` 15.7 s, mostly `walk`; `gen_build_index.py --check` 4.4 s;
  `transition_audit.py` 3.7 s; `row_grammar.py --check` 0.2 s. Liveness: an engine whose time sits
  outside any per-file loop would show it, as `selectable` does. RESOLVED (agent, 2026-10-26,
  delegated): `corpus_ids.walk`, run twice per hygiene run, with the two walks the brief names, rung 2.
  The bash checks and `selectable` are departures, recorded as deviation 231. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 23, the brief's I11 and I14, scout B's
  row for cl-0234, unit 21's `fts_blob`, and the hygiene leg's timing at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved. The Carries pin re-pinned from `eb7b1784` to `2a5b797c`, the hash the as-built view gives cl-dClosedLoop-0234 once deviation 231 states its whole clause as After.

## 10. Reuse audit

The seam extended is `tools/memory-tree/tree_lib.py`: `read_blobs_at` (`:328`) and `read_text`
(`:383`) become the miss path of `read_rows_at`, and the walks adopted are `corpus_ids.walk`
(`tools/memory-tree/corpus_ids.py:494`), `read_bindings` (`tree_lib.py:471`) and
`gen_build_index.py`'s `parse_spec_text` (`:491`). The index is PLAY-dOrderedCharter-19 S4's, whose
`build_index` already reads blobs through `read_blobs_at` and parses only new blobs. `python
tools/codebase-map/reuse_lookup.py "cache parsed results per blob so unchanged files are not
re-parsed"` ranked `read_blobs_at` (SEAM, fan-in 3), `parse_conf` and `build_cache`
(`tools/memory-recall/query.py:395`), and no per-blob parse cache in the memory tree.
`git grep -l sqlite3 -- tools skills` finds only memory-recall. Scout B's line numbers held at
`462d20f3`, and the source disagreed with the scout twice. Scout B gave `read_text` a fan-in of
109, which counts every `read_text(` token across four definitions (`tree_lib.py:383`,
`migrate_backlog.py:207`, `deviation_join.py:556`, `check-install-prefix.sh:367`). Scout B also
named the two seams the brief repeats, `read_blobs_at` and `read_text`, as where the cost sits.
The timing probe (§8 F4) puts most of it in `corpus_ids.walk` and the bash checks.

Recall terms used: `python tools/memory-recall/query.py "how do the memory legs avoid re-reading the whole tree on every run" --terms "index.db blob_row unchanged blobs re-parse memory hygiene legs read_blobs_at read_text NT-15 gap-mem-43"`
