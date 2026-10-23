# PLAY-dOrderedCharter-44 — the tag index keys freshness on each extractor as well as each blob, so a newly registered extractor reads old blobs

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 5 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-44-deviation-441.md](../build/2026-10-24-build-PLAY-dOrderedCharter-44-deviation-441.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 76 at HIGH**, its item **H5**. `PLAY-dOrderedCharter-19` S4 keys the tag index's
freshness on the blob alone: a build re-parses only blobs no `blob_row` holds, and nothing stamps
which extractor, or which version of it, produced a row. The index persists in the git common dir,
and units 10, 13, 15 and 3 register extractors after unit 19 lands. On every node that built the
index earlier, those extractors never run over blobs that already have rows, so the `retired` arm and
the namespace joins read stale populations and print green while a cold CI build disagrees. A blob
that yields no rows is parsed again on every build. This unit keys freshness on the blob, the
extractor and the extractor's version, records a parse even when it yields nothing, and stamps the
schema so a mismatch rebuilds. It repairs unit 19 and is built right after it.

## 2. Scope (IN)

- **S1** — The parse ledger. `index.db` gains `blob_parsed(blob, extractor, version)`, one row per
  extractor run over a blob, written in the same transaction as that run's `blob_row` and `path_row`
  rows and written when the run yields none. This supersedes unit 19 S4's "A commit re-parses only
  blobs no `blob_row` holds" and its §4 "for each blob no `blob_row` holds runs every extractor".
  Observed by AC1 and AC2.
- **S2** — What a build runs. `build_index(root, tree)` runs each extractor that the namespace
  registry (`read_namespaces`, unit 19 S2) names and whose source matches a path, over each blob at
  that path for which `blob_parsed` holds no row with that extractor and its current version. An
  extractor whose version moved has its old rows for that blob cleared before it runs again, so no
  row of a superseded version is served. Observed by AC1, AC3 and AC4.
- **S3** — The extractor's version is DERIVED, never typed: the first 12 hex characters of the
  SHA-256 of the bytes of the module file that defines the extractor, the file `read_namespaces`
  resolves from the row's `extractor` value (`<module>:<function>`). Editing an extractor's module
  re-runs it over every blob its source matches. Observed by AC3.
- **S4** — The schema stamp. `index.db` carries `PRAGMA user_version` set to `INDEX_SCHEMA`, a
  module-level integer in `tools/playbook/tag_index.py`. A build that opens a file whose
  `user_version` differs from `INDEX_SCHEMA` starts the file again and builds from nothing, printing one
  `tag-index — rebuilt: schema <old> to <new>` line. Observed by AC5.
- **S5** — The plants, through unit 19's fixture (`python tools/playbook/gov_tag.py --fixture --plant
  <case>`): `new-extractor` (an index built with one extractor, a second registered, one build after
  it), `extractor-edit` (an extractor module's bytes changed between two builds), `tagless` (unit 19's
  `one-commit` case widened with a tracked blob no extractor yields a row for) and `schema` (a file
  stamped with another `user_version`). Observed by AC1 to AC5.

## 3. Non-goals (OUT)

- The index's tables other than `blob_parsed`, its resolver, its CLI and its dirty-worktree overlay:
  unit 19's. The overlay's own lifecycle is a minor of the same review, batched in
  `PLAY-dOrderedCharter-49`.
- Any extractor: each is its registering unit's.
- A version field typed on a namespace row: rejected in §4.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-19` — `build_index`, the `blob_row` and `path_row` tables, `read_namespaces`, the `--fixture` plants and `--rebuild`, which S1 to S5 extend; without them there is no index to key
- **hands-off** `PLAY-dOrderedCharter-51` — rows kept per extractor version, reads filtered to the worktree's own versions and freshness keyed on tree and versions (round-2 id 30)
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 4, 14, 18, 19, 31 and 32: order-5 independence, per-version counts, import-closure versions, the in-place schema rebuild and the registry filter

## 4. Design

### Evidence

Read at `ce13efbe`, and the seam is unit 19's design, not yet code. Unit 19 S4 names the tables and
the freshness rule quoted in §1, and its §4 "The index" runs "every extractor whose source matches the
path" for "each blob no `blob_row` holds". Unit 19 S2 hands later extractors to units 10 and 15
(its §3 Edges), so the registry grows after a node's first build. The pattern this unit reuses is
recall's cache manifest: `ensure_cache` (`tools/memory-recall/query.py:712`) keys freshness on
`CACHE_VERSION` (`:139`), `chunk_max` and `conf_digest` beside the corpus digest (`:731-737`), so a
change in the producer forces a rebuild and a change in the input alone does not.

### Data model

```sql
CREATE TABLE blob_parsed (
  blob      TEXT NOT NULL,
  extractor TEXT NOT NULL,   -- the registry row's extractor value, "<module>:<function>"
  version   TEXT NOT NULL,   -- sha256 of the module file's bytes, first 12 hex
  PRIMARY KEY (blob, extractor)
);
-- PRAGMA user_version = INDEX_SCHEMA
```

One row per (blob, extractor) pair. The pair is the key, so a version move replaces the row rather
than adding a second.

### Flow

1. Open `index.db`; compare `user_version` with `INDEX_SCHEMA`; on a mismatch delete and recreate.
2. Read the registry once and derive `{extractor: version}` by hashing each module file once.
3. List the tree with one `git ls-tree -r`, as unit 19 does.
4. For each (path, blob) and each extractor whose source matches the path, look up
   `blob_parsed(blob, extractor)`. Equal version: skip. Absent: run. Different version: delete that
   extractor's `blob_row` and `path_row` rows for the blob, then run.
5. Write the run's rows and its `blob_parsed` row in the build's one transaction.

A blob two paths hold is parsed once per extractor, as unit 19's two-path case requires.

### Inventory

Minted: the table `blob_parsed`, the constant `INDEX_SCHEMA`, the plant names `new-extractor`,
`extractor-edit`, `tagless` and `schema`, and the line prefix `tag-index — rebuilt:`. Naming cells:
`lexicon naming predicates` grades the Python names.

### Files touched (estimate)

- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`

### Rollout

Live at landing, order 5, after unit 19 at order 4 and before unit 10 registers its eight
namespaces' extractors. A node holding an index unit 19 built has no `user_version` stamp, reads 0,
and rebuilds once.

### Alternatives rejected

- **A typed `version` field on each `[[namespace]]` row.** A version that must be remembered is
  forgotten exactly when an extractor's behaviour moves; the module's bytes move by themselves.
- **Rebuilding the whole index whenever the registry changes.** Correct, but it re-parses every blob
  for every extractor on each registration, where the ledger re-parses only the new extractor's.
- **A sentinel `blob_row` for a blob that yields nothing.** It puts a non-row into the table every
  reader reads, and still says nothing about which extractor ran.

## 5. Production-readiness checklist

- security: no new surface; the file stays in the git common dir and is never committed.
- perf / scale: one hash per extractor module per build, and one primary-key lookup per (blob,
  extractor). A tagless blob is parsed once per extractor version instead of on every build.
- error / empty / loading states: an unreadable module file for a registered extractor exits 2 naming
  the row, never a silent skip; a schema mismatch prints its rebuild line.
- observability: the build summary gains `<n> extractor runs, <m> skipped as fresh`.
- risks: an extractor that imports a helper from another module does not see that helper's edits in
  its version; a change there needs a module edit or `--rebuild`. Stated in the module's docstring.
- testing: AC1 to AC5 by fixture; the plants run under unit 19's selftest arm (§7).
- migration: an index without a stamp rebuilds once on first use.
- user docs: none; `tools/playbook/README.md`'s index paragraph, which unit 19 writes, names the key.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant new-extractor` runs, the second
  build runs the newly registered extractor over every blob its source matches, and the row dump
  after it equals the dump of a cold build with both extractors.
  Red when: the build skips blobs that already hold rows, so the new extractor's rows are missing.
- **AC2** — When `--plant tagless` runs, a commit changing one file of a built tree whose other
  tracked files include a blob no extractor yields a row for reports `1 blob parsed`, and a second
  build with no change reports `0 blobs parsed`.
  Red when: the tagless blob is parsed again on every build.
- **AC3** — When `--plant extractor-edit` runs, the build after the module edit re-runs that
  extractor over its blobs and leaves no row of the old version; the other extractors report every
  blob skipped as fresh.
  Red when: an edited extractor's old rows survive, or every extractor re-runs.
- **AC4** — When `--plant rebuild` (unit 19's AC2 case) runs after this unit, the incremental and the
  cold dumps are equal, `blob_parsed` included.
  Red when: the ledger drifts from what a cold build writes.
- **AC5** — When `--plant schema` opens a fixture `index.db` stamped `user_version` 0, the build prints
  `tag-index — rebuilt: schema 0 to <INDEX_SCHEMA>` and its dump equals a cold build's.
  Red when: a file of another schema is read as current.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC5 · the playbook-render selftest runs the four new plants, each failing case staged by the base freshness rule (skip any blob holding a row) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds, as 89 promoted specs
  in this tree do; (b) none; (c) a part of unit 19's clause. (b) reds unbound and (c) splits a clause
  this unit does not carry.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What stamps an extractor's version.** Options: (a) a typed integer per registry row; (b) the
  hash of the module file's bytes, derived; (c) the hash of the function's source alone. (c) misses a
  module-level constant the function reads. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3, the
  derived value over the typed one (charter `[derive]`), with the helper-module limit stated in §5.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 76 (HIGH, item H5).
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-51, PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seam extended is unit 19's `build_index` and its tables (its S4 and §4 "The index"), which this
unit keys rather than replaces; the freshness pattern is recall's `ensure_cache` manifest
(`tools/memory-recall/query.py:712`, clauses at `:731-737`), which keys on the producer's version
beside the input digest. `python tools/codebase-map/reuse_lookup.py "keep a derived cache fresh when a
new extractor or producer version arrives"` ranked `extract` (`tools/lexicon/lexicon.py`),
`extract_row` (`tools/memory-tree/backlog.py`) and `derive_baseline_additions` by name stem; none keys
a cache on a producer, so the probe disagrees with source on relevance and the seam came from recall.

Recall terms used: `python tools/memory-recall/query.py "how does a persistent derived cache invalidate when its producer changes" --terms "cache freshness manifest CACHE_VERSION conf_digest extractor version rebuild stale index sqlite"`
