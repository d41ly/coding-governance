# PLAY-dOrderedCharter-51 — the shared tag index keeps each extractor version's rows apart, and each worktree reads only its own

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 6 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-24-build-PLAY-dOrderedCharter-51-deviation-511.md](../build/2026-10-24-build-PLAY-dOrderedCharter-51-deviation-511.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 30 at HIGH**, its item **H2**. The tag index is one file,
`<git-common-dir>/gov/index.db`, shared by every worktree (`PLAY-dOrderedCharter-19` S4).
`PLAY-dOrderedCharter-44` keys its parse ledger on `(blob, extractor)`, holding one version per pair,
derives the version from the module file in the building worktree, and clears another version's rows
before it re-runs; unit 19's `tree_built(tree)` short-circuit never consults the ledger. Two worktrees
whose extractor bytes differ, which this build's own run worktree and main do, evict each other's
rows on every build, and a worktree whose tree is already marked built is served rows another
worktree's extractor wrote, with nothing printed. This unit keeps every version's rows side by side,
filters every read to the reading worktree's own versions, keys freshness on the tree and those
versions together, and collects a version only when no live worktree derives it. It repairs unit 44
and is built right after it.

## 2. Scope (IN)

- **S1** — The key. `blob_parsed` is keyed `PRIMARY KEY (blob, extractor, version)`, and `blob_row`
  and `path_row` each gain a `version` column holding the version of the extractor run that wrote the
  row. Rows of two versions of one extractor over one blob coexist. This supersedes
  `PLAY-dOrderedCharter-44`'s data model key `(blob, extractor)`. Observed by AC1.
- **S2** — What a build runs. A build derives its own `{extractor: version}` map as unit 44 S3 does,
  from the building worktree's registry and module files, and runs an extractor over a blob only when
  `blob_parsed` holds no row for that blob, extractor and version. A build never deletes a row of
  another version. This supersedes unit 44 S2's "has its old rows for that blob cleared" and its §4
  Flow step 4. Observed by AC1 and AC2.
  **Readers:** by name: READER NOT IN TREE — the clearing it supersedes is unit 44 S2's design, built
  at unit 44's pass, and a grep for blob_parsed, tree_built and path_row over tools, skills and
  .githooks finds no reader today. by value: NO VALUE READERS — a row of another version is index data
  in the per-node SQLite file, read only by `gov_tag.py`'s build and resolver, which unit 19 lands.
- **S3** — What a read serves. Every resolver verb of `tools/playbook/gov_tag.py` (`show`, `where`,
  `refs`, `check`) and the `--dump` the fixtures compare reads `blob_row` and `path_row` joined to the
  reading worktree's own map: a row is served only when its `(extractor, version)` pair is in that
  map. A worktree is never served a row its own extractor bytes did not produce. Observed by AC1 and
  AC3.
- **S4** — Freshness. `tree_built` is keyed `(tree, versions)`, where `versions` is the first 12 hex
  characters of the SHA-256 of the map's `extractor=version` pairs, sorted and joined by newlines. A
  worktree whose tree was built under another digest is not fresh, and its build parses only its
  missing triples. This supersedes unit 19 S4's "The tree id is only the freshness key". Observed by
  AC3.
- **S5** — Collection. `python tools/playbook/gov_tag.py --rebuild` and a new `--gc` flag delete the
  rows, ledger rows and `tree_built` rows of every `(extractor, version)` pair no live worktree
  derives. The live set is each worktree `git worktree list --porcelain` names, its map derived from
  its own working-tree registry and module files; a worktree whose registry cannot be read refuses the
  collection, exit 2 naming it, rather than collecting its versions. A plain build collects nothing.
  Observed by AC4.
  **Readers:** by name: none — the collection deletes index rows, data no reader spells by name; the
  same grep finds no reader of those tables today. by value: `gov_tag.py`'s resolver verbs (S3), which
  serve only versions a live worktree derives, so a collected row is one no live reader is served.
- **S6** — The plants, through unit 19's fixture, `python tools/playbook/gov_tag.py --fixture --plant
  <case>`: `two-versions` (two worktrees of one fixture repository whose extractor module differs,
  built alternately twice) and `served-across` (worktree A builds a tree, worktree B on the same tree
  with another extractor version reads it before building). Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- How a version is derived: unit 44 S3's rule, extended to the extractor's import closure by the
  round-2 minors batch (`PLAY-dOrderedCharter-55`).
- The schema stamp and its rebuild: unit 44 S4, which `INDEX_SCHEMA`'s bump to this unit's tables
  triggers once.
- The dirty-worktree overlay's keys: unit 19 S5 and the minors batch.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-44` — `blob_parsed`, the derived version and the schema stamp, which S1 to S4 re-key; without them there is no ledger to key per version
- **consumes-from** `PLAY-dOrderedCharter-19` — `build_index`, `tree_built`, the resolver verbs and the fixture, which S2 to S6 extend
- **hands-off** `PLAY-dOrderedCharter-55` — the round-2 minors on the same index (ids 4, 14, 18, 19, 31, 32), each observed over this unit's per-version tables

## 4. Design

### Evidence

Read at `ce13efbe`; the seam is units 19 and 44, not yet code. Unit 19 S4 places the index at
`<git-common-dir>/gov/index.db`, shared by every worktree, and makes the tree id the only freshness
key. Unit 44's data model has `PRIMARY KEY (blob, extractor)` with the comment that "a version move
replaces the row rather than adding a second", and its Flow step 4 deletes the other version's
`blob_row` and `path_row` rows. `git rev-parse --git-common-dir` in this worktree resolves to the main
checkout's `.git`, so the run worktree and main share one file.

### Data model

```sql
CREATE TABLE blob_parsed (
  blob TEXT NOT NULL, extractor TEXT NOT NULL, version TEXT NOT NULL,
  PRIMARY KEY (blob, extractor, version)
);
-- blob_row and path_row: + version TEXT NOT NULL
CREATE TABLE tree_built (tree TEXT NOT NULL, versions TEXT NOT NULL, built_at TEXT NOT NULL,
  PRIMARY KEY (tree, versions));
```

### Flow

1. Derive this worktree's map and its `versions` digest.
2. `tree_built(tree, versions)` present: read, filtered to the map.
3. Absent: for each (path, blob) and each matching extractor, run it when
   `blob_parsed(blob, extractor, version)` is absent; write its rows and ledger row in one
   transaction; stamp `tree_built(tree, versions)`.

### Inventory

Minted: the `version` columns, the `versions` digest, the flag `--gc`, the plants `two-versions` and
`served-across`. Naming cells: `lexicon naming predicates` grades the Python names.

### Files touched (estimate)

- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`

### Rollout

Live at landing, order 6, after unit 44 at order 5. `PLAY-dOrderedCharter-22` shares order 6 and
writes both files, so the dispatch sequences the two (M6). `INDEX_SCHEMA` moves, so every node's
index rebuilds once under unit 44 S4.

### Alternatives rejected

- **One index file per worktree.** Correct, but every worktree then parses the whole repository from
  nothing, which the shared file exists to avoid.
- **Keeping the one-version key and refusing a build whose version differs**: it puts main's `tags`
  leg in an outage whenever a run branch edits an extractor.
- **Collecting on every build**: registries differ per branch, so each worktree would delete the
  other's live rows.

## 5. Production-readiness checklist

- security: no new surface; the file stays in the git common dir, never committed.
- perf / scale: a version an extractor no longer derives costs disk until `--gc`; reads add one join
  on an indexed pair. Alternating builds of two versions parse nothing on the second round.
- error / empty / loading states: an unreadable registry in another worktree refuses `--gc`, exit 2;
  a plain build never reads other worktrees.
- observability: `--gc` prints `tag-index — collected: <n> rows of <m> versions`.
- risks: a worktree deleted without `git worktree prune` still counts as live until pruned, which
  keeps its rows, the safe side.
- testing: AC1 to AC4 by fixture under unit 19's selftest arm.
- migration: the schema bump rebuilds every node's index once.
- user docs: unit 19's index paragraph in `tools/playbook/README.md` gains the per-version rule.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant two-versions` runs, each worktree's
  `--dump` equals a cold build at its own extractor version, and neither carries a row of the other's.
  Red when: one worktree's build evicts or overwrites the other's rows.
- **AC2** — When the same plant builds the two worktrees alternately a second time, each second build
  reports `0 blobs parsed`.
  Red when: alternating builds re-parse a population the other worktree parsed.
- **AC3** — When `--plant served-across` runs, worktree B's first `show` builds B's missing triples and
  serves none of A's version's rows.
  Red when: a tree marked built by another version is read as fresh.
- **AC4** — When `--gc` runs after one fixture worktree is removed and pruned, the removed worktree's
  version leaves every table, and the live worktree's dump is unchanged.
  Red when: a live worktree's rows are collected, or a dead version's rows survive `--gc`.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 · the playbook-render selftest runs the two plants and the collection, each failing case staged by unit 44's one-version key · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 19's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How worktrees with different extractor bytes share one index.** Options: (a) rows keyed per
  version, reads filtered per worktree, collection over live worktrees; (b) one file per worktree;
  (c) a refusal when versions differ. (b) re-parses the repository per worktree and (c) is an outage
  on main. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 30 (HIGH, item H2).

## 10. Reuse audit

The seam extended is unit 19's `build_index` and resolver over unit 44's ledger, both in
`tools/playbook/tag_index.py`, re-keyed rather than replaced; the freshness pattern stays recall's
`ensure_cache` manifest (`tools/memory-recall/query.py:712`), which keys on the producer's version.
`python tools/codebase-map/reuse_lookup.py "shared sqlite cache keyed per producer version across
worktrees"` ranked `key`, `keys`, `read_conf_key` and `add_scratch_worktree` by name stem; none keys a
shared store per producer, so no existing seam fits the per-version filter and it is new code. The
recall query returned TOOL-aMendedFleet-32 and TOOL-aPairedSlots-5 on stores shared across worktrees.

Recall terms used: `python tools/memory-recall/query.py "how is a cache shared across worktrees kept correct when each worktree has different code" --terms "git common dir shared index worktree version cache thrash eviction sqlite extractor"`
