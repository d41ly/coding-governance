# PLAY-dOrderedCharter-19 — the tag grammar, its namespace registry, the derived SQLite tag index and its one resolver, and the join factory moved to the core

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 4 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0049@a87d159d whole
**Carries:** node:system.tags
**Carries:** node:policy-key.tags.slice
**Carries:** node:policy-key.tags.retired-cites
**Carries:** node:policy-key.tags.bare-refs
**Carries:** node:tag-namespace.doc
**Carries:** node:tag-namespace.unit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md) | research | PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

No section tag has a resolver and no citation is checked: 1,438 citations, 788 of them ambiguous
(`gap-found-20`), and the designed index, one JSON file per tree, measured about 30 s to rebuild and
1.6 GB to load at ten times today's tree (`gap-found-33`). This unit lands the tag grammar, its
namespace registry, one derived SQLite index per node at `<git-common-dir>/gov/index.db` shared by
every worktree and re-parsing only the blobs a commit changed, and one resolver, `gov tag`, with
`gov tag show`, `where`, `refs` and `check`, under three policy keys, and the `tags` leg pack. With it the join factory leaves the
optional codebase-map kit for the core and `tools/lib`, beside `map_lib.resolve_compare_base`'s siblings, so no core build imports codebase-map (H5), and positional
references gain alias rows and a keyed list (systems `[cross]`, `[design-tags]`; the night pass two,
point 3, the owner's NT-15; C1-F3, DA-M9, FM10).

## 2. Scope (IN)

- **S1** — The grammar (shared interface S4): `tag := <ns>.<seg>(.<seg>)*`, `seg :=
  [a-z0-9][a-z0-9-]*`, at most 64 bytes, compiled once in `tools/playbook/tag_index.py` as `TAG_RE`
  and `TAG_MAX_BYTES`, with `parse_tag` returning the namespace and segments or the rule broken. The
  namespace words are read from the registry, never typed beside it. Observed by AC1.
- **S2** — The registry, `tools/playbook/namespaces.toml`: one `[[namespace]]` row per namespace
  with `ns`, `owner` (a chain build), `layer`, `source`, `extractor` (`<module>:<function>`), `role`
  (`selects` or `describes`), `purpose-source` and `join-armed-by`, read by `read_namespaces`. This
  unit writes the `doc` and `unit` rows; PLAY-dOrderedCharter-10 adds its eight. Observed by AC9.
- **S3** — The `doc` namespace: a tag `doc.<name>` for the charter (`doc.charter`, the path
  `.memory-tree.conf`'s `CHARTER` names) and for each of `memory/guides/*.md`, `memory/HYGIENE.md`
  and `memory/TEMPLATE-SPEC.md`, `<name>` its file stem lower-cased; each `##` heading of those
  documents is a section row `doc.<name>#<seg>`, `<seg>` the heading's text lower-cased, each run of
  characters outside `[a-z0-9]` folded to one hyphen and the ends trimmed, so the heading
  `## M5 — Recall and reuse` is `m5-recall-and-reuse`. The `unit` namespace: a
  tag per `[[unit]]` row of every `<kit>/instructions.toml` and of `.governance/instructions.toml`
  (shared interfaces S10 and S14); empty until PLAY-dOrderedCharter-9 lands rows, and printed as
  `unarmed`, never green, while empty. Observed by AC9.
- **S4** — The index, `<git-common-dir>/gov/index.db`, written by the extractors alone through
  `build_index`, never committed and never loaded whole. Tables: `tree_path(tree, path, blob)`;
  `blob_row(blob, extractor, tag, kind, line, end_line, text)` for what a blob holds;
  `path_row(path, blob, extractor, tag, kind, line)` for what a path names, a citation among them;
  `dirty_path(worktree, path, blob)` for a worktree's uncommitted edits; `tree_built(tree, built_at)`.
  The tree id is only the freshness key. A commit re-parses only blobs no `blob_row` holds. A full
  rebuild from an empty file writes identical rows. Observed by AC2 to AC5.
- **S5** — The worktree overlay. A worktree with uncommitted edits to tracked files is served its
  HEAD tree with those paths' working-tree blobs, recorded as its own rows marked `dirty` in `dirty_path`, keyed by the
  worktree's path, never served to another worktree; the freshness check exempts them. SQLite's lock
  serialises concurrent writers. Observed by AC4.
- **S6** — The resolver, `tools/playbook/gov_tag.py` (shared interface S5), invoked
  `python tools/playbook/gov_tag.py <verb> <address>`, standing in for `gov tag` (§8 F1):
  `show` returns the tag's row, or its subtree, every tag with it as a dot-prefix, as `tags.slice`
  says (`leaf` or `subtree`, default `leaf`); `where` prints `path:line`; `refs` prints every citation
  of it; `check` runs S7. Output is text, or JSON with `--json`, the index's only JSON. Observed by
  AC6.
- **S7** — Two checks under `check`. `retired`: new text citing a retired tag, or a retired name
  minted again, as `tags.retired-cites` says (`refuse-new` red, `warn` printed and exit 0, `allow`
  silent; default `refuse-new`); new text is a citation absent from the base tree, the base read by
  `resolve_compare_base`. `resolves`: a citation that resolves to no row is red, and bare
  references read as `tags.bare-refs` says (§4 "### Bare references"; default `charter-only`).
  The retired set is the index's `retired` rows, which an extractor writes; the change-record
  extractor that fills them is PLAY-dOrderedCharter-15's. Observed by AC7 and AC8.
  **Readers:** by name: READER NOT IN TREE — this item retires no name; it grades retirements that
  change records will carry, and its only reader, `gov_tag.py`, is new in this unit · by value: NO VALUE READERS —
  the retired set is empty until PLAY-dOrderedCharter-15's extractor writes it.
- **S8** — The three keys, `tags.slice`, `tags.retired-cites` and `tags.bare-refs`, each a catalogue
  row with its values, default, summary and usage from v2 `[policies]` (v2:1349, 1350, 1352), read
  through dGroundRules' one reader once it lands and with the catalogue default until then. A
  `--set <key>=<value>` flag is honoured under `--fixture` only. Observed by AC6 to AC8.
  **Readers:** by name: READER NOT IN TREE — the three keys are new and retire nothing; their one
  reader is dGroundRules' policy reader, which has not landed · by value: NO VALUE READERS — until
  that reader lands each key reads its catalogue default.
- **S9** — The join factory (shared interface S2): `compute_coverage` with its `Coverage` class,
  `resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions`, moved
  from `tools/codebase-map/map_lib.py` (`:1373`, `:1390-1404`, `:1502`, `:1530`) to the canonical `tools/lib/coverage_join.py`, and
  shipped inline in `tools/memory-tree/coverage_join.py` under a `coverage_join` row of
  `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS`. The consumers, `gen_map.py`, `map_diff.py`,
  `selftest.py`, `test_codebase_map.template.py` and its copy `test_codebase_map.py`, are rewritten to
  import the four names from memory-tree's module, which codebase-map already `requires`
  (`tools/codebase-map/kit.toml:7`); `map_lib` re-exports them for `install.deprecation-window`
  releases; the template is re-copied into adopters through govkit's update. Observed by AC10.
- **S10** — The common-dir resolver (shared interface S3): `common_git_dir` canonicalised from
  `tools/memory-recall/query.py:248-257` into `tools/lib/common_dir.py`, under a `common_git_dir`
  `PARITY_ROWS` row whose copies are `query.py`'s and `tag_index.py`'s. Observed by AC11.
- **S11** — Positional references aliased to tags: `tools/playbook/aliases.toml`, one `[[alias]]`
  row per positional label that never moved, the BUILD-METHOD `M`-steps and the hygiene checks,
  `ref = "<doc> <label>"`, `target = "doc.<name>#<seg>"`, resolved by `where` and `show`; and the
  live positional references kept by key, `tools/playbook/positional-refs.txt`, one
  `<path>\t<ref>` row each, seeded from `gov_tag.py --list-positional`, until dWitnessedBar's
  migration registers it as a ledger population. Never a count. Observed by AC12.
- **S12** — The `tags` leg pack (shared interface S21): the leg `tags (the resolver's checks)` in
  `tools/gate-legs.json`, argv `python {prefix}/playbook/gov_tag.py check`, carrying `"pack":
  "tags"`, a new key never an overloaded `chunk`; `pack` joins the run-gates canary's known-key set
  (`tools/run-gates/run-gates.test.sh:244,580`), and the leg gains its meta-gate rows. Observed by
  AC13.
- **S13** — The fixture, `gov_tag.py --fixture --plant <case>`, a scratch git repository with two
  worktrees, a three-row registry and planted documents. Observed by AC2 to AC8.
- **S14** — The `owned` arm of `check`, the systems record's check table row: a tag minted in a
  namespace whose row's `layer` is a core layer, by a declaring source that sits in a kit whose
  descriptor's `layer` is an `optional` or `expansion` row of `tools/playbook/layers.toml`, is red,
  so an expansion declaring `item.build.x` is refused and an expansion mints only under its own
  namespace. Observed by AC14.

## 3. Non-goals (OUT)

- The shape check over registered namespaces, the both-ways joins and the lexicon hand-off:
  PLAY-dOrderedCharter-10's, which adds them to `check`.
- `gov tag bundle` (PLAY-dOrderedCharter-25), file:line citations and the `positional` check under
  `tags.positional` (PLAY-dOrderedCharter-26), the edge grammar (PLAY-dOrderedCharter-24 and -28).
- The `section` and `record` namespaces and memory's extractors and read verbs: dTotalRecall's, which
  also moves recall's FTS5 tables into `index.db`; the schema leaves room by keying every table by
  blob or path and blob.
- A `gov` launcher: §8 F1.
- Converging the three other re-derivations of the common dir (`tools/drift-audit/drift_report.py`,
  `tools/branch-reconcile/`, `tools/lib/health_log.py`): each is written differently and none is
  this clause's; they stay as they are.
- Migrating live positional references: Convergence's.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-18` — `repo_root` and the moved grammar, through which `doc.charter`'s path is read from the conf
- **consumes-from** `PLAY-dOrderedCharter-16` — `tools/playbook/layers.toml` and each descriptor's `layer` key, which the `owned` arm reads
- **hands-off** `PLAY-dOrderedCharter-10` — the eight namespace rows, the shape check and the both-ways joins added to `check`
- **hands-off** `PLAY-dOrderedCharter-15` — the change-record extractor that writes the index's retired rows, a rename, split or retirement each read from its change record
- **hands-off** `PLAY-dOrderedCharter-22` — the `purpose-source` and `owner` fields' checks over `tools/playbook/namespaces.toml`
- **hands-off** `PLAY-dOrderedCharter-25` — the `bundle` verb on `tools/playbook/gov_tag.py`
- **hands-off** `PLAY-dOrderedCharter-26` — the `positional` check over `tools/playbook/positional-refs.txt`
- **hands-off** `PLAY-dOrderedCharter-31` — the `map_lib` re-export declared as a deprecation
- **hands-off** `PLAY-dOrderedCharter-24` — `read_namespaces` and each row's `role`, which the edge registry's selector class reads
- **hands-off** `PLAY-dOrderedCharter-28` — the resolver and the `tags` leg pack, which the edge checks join
- **hands-off** `PLAY-dOrderedCharter-1` — the tag grammar's `seg` shape, which the catalogue's tags pass
- **hands-off** `PLAY-dOrderedCharter-3` — the `doc` namespace, each registered document's tag
- **hands-off** `PLAY-dOrderedCharter-7` — the join factory `compute_coverage` and its `PARITY_ROWS` row, the resolver and the `tags` pack
- **hands-off** `PLAY-dOrderedCharter-9` — the `unit` namespace and `extract_unit`, which that unit points at its registry's reader
- **hands-off** `PLAY-dOrderedCharter-12` — the resolver a pointer's target resolves through
- **hands-off** `PLAY-dOrderedCharter-20` — the tag grammar and the namespace registry a unit row's `tag`, `scope` and `required-by` are graded against
- **hands-off** `PLAY-dOrderedCharter-29` — the tag index, its `doc` sections, the `retired` check, the aliases file and the `tags` pack
- **hands-off** `PLAY-dOrderedCharter-35` — the tag grammar, the namespace registry and the `owned` arm, which that unit widens to admit the adopter segment
- **hands-off** `PLAY-dOrderedCharter-37` — the tag resolver each page's unit tag resolves through
- **consumes-from** external — dGroundRules' catalogue (`cl-dClosedLoop-0007`) and reader (`cl-dClosedLoop-0008`), and dSafePassage's shim and update for the re-copied template
- **hands-off** `PLAY-dOrderedCharter-40` — the doc extractor reading the reference registry's rows, so each page's registry tag is declared (finding 2)
- **hands-off** `PLAY-dOrderedCharter-44` — S4's freshness keyed on the extractor and its version as well as the blob, with a parse ledger and a schema stamp (finding 76)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 11, 44, 55, 77 and 78, which that batch unit corrects after this unit lands, each by the item its report id names
- **hands-off** `PLAY-dOrderedCharter-51` — `tree_built` keyed on the tree and its extractor-versions digest, and every read filtered to the reading worktree's own versions (round-2 id 30)
- **hands-off** `PLAY-dOrderedCharter-55` — the index's order-5 independence, its in-place schema rebuild and the dirty rows' canonical worktree key (round-2 ids 4, 31, 41)

## 4. Design

### Data model

```toml
# tools/playbook/namespaces.toml
[[namespace]]
ns = "doc"
owner = "dOrderedCharter"
layer = "layer.instruction"
source = "the CHARTER path, memory/guides/*.md, memory/HYGIENE.md, memory/TEMPLATE-SPEC.md"
extractor = "tag_index:extract_doc"
role = "describes"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"
join-armed-by = "dOrderedCharter"
```

`purpose-source` and `owner` are written here and graded by PLAY-dOrderedCharter-22.

### The index

`build_index(root, tree)` lists the tree's paths and blobs with one `git ls-tree -r`, inserts
`tree_path` rows, and for each blob no `blob_row` holds runs every extractor whose source matches the
path, reading blobs through `tree_lib.read_blobs_at` (`tools/memory-tree/tree_lib.py:328`). An
extractor yields definitions into `blob_row` and path-keyed facts into `path_row`. A path deleted from
the tree loses its `tree_path` row; its blob's rows stay while another path holds the blob, so the
planted case, one blob at two paths with one deleted, rebuilds to the rows a cold build writes. One
transaction per build; WAL off, since every worktree opens the one file. The index's writes follow
recall's SQLite pattern (`tools/memory-recall/query.py:381` `_write_set`).

The citation extractor scans tracked `.md`, `.py`, `.sh`, `.js`, `.toml` and `.json` text outside
fences for tokens `TAG_RE` matches whose namespace is registered, and for `<doc>#<seg>` sections.

### Bare references

A bare reference is a backticked or bracketed name equal to a registered tag less its namespace. Under
`charter-only` it resolves to the `practice` namespace alone, wherever it stands, and a bare name
matching no practice is not a reference. Under `unique` it resolves against every namespace and is red
where two match. Under `never` any bare name matching a tag outside the charter is red. Each value is
planted in the fixture.

### The CLI

```
python tools/playbook/gov_tag.py show|where|refs|check <address> [--json]
python tools/playbook/gov_tag.py check [--base <rev>]
python tools/playbook/gov_tag.py --rebuild | --list-positional
python tools/playbook/gov_tag.py --fixture --plant <case> [--set <key>=<value>]
```

Every line opens `tags:`. `check`'s summary carries namespaces, tags, citations, unresolved,
retired-cited, bare refs and each empty namespace named `unarmed`, DERIVED at the run.

### The join factory

The canonical block in `tools/lib/coverage_join.py` carries its own inline copy of the remote ladder
(`remote_ladder_py`, `tools/lib/resolve_remote.py:17`), as `map_lib` does today. `map_lib` keeps the
four names as `from coverage_join import ...` after resolving memory-tree's directory, so an adopter
whose older `test_codebase_map.py` calls `m.compute_coverage` still runs. Without that line the
codebase-map leg reds, which is the clause's planted case.

### Inventory

Minted: `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/namespaces.toml`,
`tools/playbook/aliases.toml`, `tools/playbook/positional-refs.txt`, `tools/lib/coverage_join.py`,
`tools/memory-tree/coverage_join.py`, `tools/lib/common_dir.py`; the constants `TAG_RE`,
`TAG_MAX_BYTES`; the functions `parse_tag`, `read_namespaces`, `build_index`, `extract_doc`,
`extract_unit`, `extract_citations`, `resolve_address`, `check_retired`, `check_resolves`,
`build_tags_fixture`; the tables named in S4; the verbs `show`, `where`, `refs`, `check`; the flags
`--json`, `--base`, `--rebuild`, `--list-positional`, `--fixture`, `--plant`, `--set`; the leg named in
S12; the manifest key `pack`; the prefix `tags:`; the parity rows `coverage_join` and
`common_git_dir`. Naming cells: each function is checked with `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` at the pass.

### Migration

Additive. `index.db` is derived and built on first use; deleting it costs one rebuild. An adopter's
`test_codebase_map.py` keeps working through the re-export for the window.

### Rollout

Live at landing under the catalogue defaults; the leg runs over gov's tree.

### Files touched (estimate)

- `tools/playbook/tag_index.py` (new)
- `tools/playbook/gov_tag.py` (new)
- `tools/playbook/namespaces.toml` (new)
- `tools/playbook/aliases.toml` (new)
- `tools/playbook/positional-refs.txt` (new)
- `tools/playbook/README.md`
- `tools/lib/coverage_join.py` (new)
- `tools/lib/common_dir.py` (new)
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/coverage_join.py` (new)
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/codebase-map/test_codebase_map.template.py`
- `tools/memory-recall/query.py`
- `tools/gate-legs.json`
- `tools/run-gates/run-gates.test.sh`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/playbook.md`
- the catalogue file of `cl-dClosedLoop-0007`, for the three keys' rows, at the path dGroundRules lands

### Alternatives rejected

- **One JSON file per tree**: the measured 30 s and 1.6 GB (NT-15).
- **Path-keyed rows only**: one blob sat at 24 paths at `e1a54ac67`, so a rename re-parses what did
  not change (the night pass two's review).
- **The join factory left in `map_lib`**: the core would import an optional kit (H5).

## 5. Production-readiness checklist

- security: the index is derived and local; the resolver reads only; `--set` is fixture-only, so the leg cannot be relaxed past the policy file; no network.
- perf / scale: a cold build parses every blob once; a one-file commit re-parses one blob; both DERIVED at the pass by the fixture's `--rebuild` timing, and the leg's `ceiling` set from the measured run.
- error / empty / loading states: an unreadable registry exits 2; an empty namespace prints `unarmed`; a locked database waits on SQLite's busy timeout and then exits 2 naming it.
- observability: one summary line and one line per red.
- risks: a tag-shaped token in prose that is not a citation; only registered namespaces are read, and `resolves` reds such a token, which the author answers by writing the full tag or quoting it otherwise.
- testing: AC1 to AC14 and §7's arms.
- migration: §4 "### Migration".
- user docs: a page `help/tags.md` for `gov tag` and the three keys, and its line in `help/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0,'tools/playbook'); import tag_index as t; print([t.parse_tag(x)[1] for x in ('layer.memory','Layer.memory','layer..x','layer.-x','layer.' + 'a'*60)])"`
  runs, the first is accepted and each other names its broken rule, the last the 64-byte limit.
  Red when: a segment outside `seg`'s shape, or an over-long tag, parses.
- **AC2** — When `python gov_tag.py --fixture --plant rebuild` runs, it builds the
  index, dumps every row sorted, deletes `index.db`, rebuilds, and prints the two dumps equal.
  Red when: a rebuild from nothing writes a different row set.
- **AC3** — When `--plant two-paths` runs, one blob at two paths with one path deleted in the next
  commit, the incremental index's rows equal a cold build's at that commit, and the surviving path
  still resolves.
  Red when: rows are keyed by path alone, so the deletion drops the surviving path's rows.
- **AC4** — When `--plant dirty` runs, two worktrees edit one tracked path differently, each `show`
  returns its own working-tree text, and neither sees the other's `dirty_path` row.
  Red when: an uncommitted edit is served to another worktree.
- **AC5** — When `--plant one-commit` runs, a commit changing one file of a built tree re-parses
  exactly one blob, and the summary says `1 blob parsed`.
  Red when: a commit re-parses unchanged blobs.
- **AC6** — When `--plant slice` runs, `show layer.memory` returns one row under `--set
  tags.slice=leaf` and the row with `layer.memory.recall` under `--set tags.slice=subtree`.
  Red when: the key does not move the slice.
- **AC7** — When `--plant retired` runs, a citation of a retired tag added after the base exits 1
  under `refuse-new`, exits 0 with a `WARN` line under `warn`, exits 0 silent under `allow`; a
  citation already at the base exits 0 under `refuse-new`; a retired name minted again exits 1 under
  every value.
  Red when: old text is refused, new text passes, or a reused name passes.
- **AC8** — When `--plant bare` runs, a bare `land` resolves to `practice.land` under
  `charter-only`; a bare name two namespaces hold exits 1 under `unique` naming both; a bare name
  outside the charter exits 1 under `never` and the same name inside the charter exits 0.
  Red when: a value's planted case reads the same as another's.
- **AC9** — When `python gov_tag.py where doc.build-method` runs on the tree, it prints
  `memory/guides/BUILD-METHOD.md:1`; `where doc.build-method#m5-recall-and-reuse` prints the line of
  `## M5`; `check` prints `unit` as `unarmed` before PLAY-dOrderedCharter-9's rows land.
  Red when: the `doc` namespace has no extractor, or an empty namespace reads green.
- **AC10** — When the parity row's block extraction is reproduced by
  `diff <(cd tools/lib && sed -n '/>>> coverage_join/,/<<< coverage_join/p' coverage_join.py) <(cd tools/memory-tree && sed -n '/>>> coverage_join/,/<<< coverage_join/p' coverage_join.py)`,
  it prints nothing; `git grep -n "m\.compute_coverage\|m\.resolve_compare_base\|m\.derive_baseline_additions\|m\.drop_touched_exemptions" -- tools/codebase-map`
  prints nothing; and in a scratch copy with `map_lib.py`'s re-export line deleted and the base's
  `test_codebase_map.py` restored, `python tools/codebase-map/test_codebase_map.py` exits non-zero
  naming `compute_coverage`, and with the line kept exits as the tree does.
  Red when: a consumer still reaches a moved name through `map_lib`, or the re-export is not what
  keeps an older copy working.
  fixture: a copy under `%TEMP%`.
- **AC11** — When the two `common_git_dir` blocks in `tools/memory-recall/query.py` and
  `tag_index.py` are compared with the canonical `common_dir.py` by the
  same `sed` extraction, both match; and `python gov_tag.py --rebuild` run in a linked
  worktree writes `<git-common-dir>/gov/index.db`, the main repository's.
  Red when: the index lands under `.git/worktrees/<name>/`, which `git worktree remove` deletes.
- **AC12** — When `python gov_tag.py where "BUILD-METHOD M5"` runs, it prints the
  line of `## M5` in `memory/guides/BUILD-METHOD.md`; and `positional-refs.txt` holds
  one `<path>\t<ref>` row per line `--list-positional` prints, and no count.
  Red when: a positional label resolves nowhere, or the live references are held as a number.
- **AC13** — When `python -c "import json, sys; print([l['name'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l.get('pack') == 'tags'])" tools/gate-legs.json`
  runs, it prints the leg of S12; and `git grep -n "\"pack\"" -- tools/run-gates/run-gates.test.sh`
  finds the key in both known-key sets.
  Red when: the pack is spelled through `chunk`, or the canary refuses the new key.
- **AC14** — When `python gov_tag.py --fixture --plant owned` runs, a fixture expansion
  kit whose declaring source mints `layer.fixture-x` in the core `layer` namespace exits 1 naming the
  kit and the tag; the same tag minted by a core kit's source exits 0.
  Red when: an expansion mints in a core namespace.

## 7. Gates

`memory hygiene` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `memory-recall kit selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/playbook/gov_tag.py · covers AC9 AC12 · the new `tags` leg over the tree, its failing case staged by citing `doc.no-such-doc` in a guide · none
New arm: tools/playbook/adopt-playbook.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC14 · the playbook-render selftest runs `gov_tag.py --fixture` under every plant of S13 and S14 · none
New arm: tools/lib/resolve-python.test.sh · covers AC10 AC11 · the `coverage_join` and `common_git_dir` parity rows, each failing case staged by editing one copy · none
New arm: tools/codebase-map/selftest.py · covers AC10 · the selftest's coverage and base arms import the four names from memory-tree's module · none

## 8. Open questions

- **F1 — Whether a `gov` launcher ships now, or the module stands in.** Options: (a) a launcher
  dispatching `gov tag <verb>`; (b) `python tools/playbook/gov_tag.py <verb>`, its verbs exactly
  `gov tag`'s. A launcher on a user's path is an install location, and installing an entry point is
  distribution's, an expansion; no clause of this build names an install location, so (a) fails veto
  2 outside the grant. RESOLVED (agent, 2026-10-23, delegated): (b), rung 3; a later launcher is a pure
  dispatcher over the same verbs. widens: none · relaxes: none
- **F2 — Where the join factory ships.** The brief places the canonical in `tools/lib`, which ships
  nothing. Options: (a) an inline copy in `map_lib` and consumers unchanged; (b) an inline copy in a
  memory-tree module, consumers importing it, `map_lib` re-exporting. (a) leaves no consumer
  rewritten and keeps the factory in the optional kit, which H5 forbids. RESOLVED (agent, 2026-10-23,
  delegated): (b), rung 1, the clause's "its consumers rewritten in the move's unit while `map_lib`
  re-exports", and codebase-map already requires memory-tree. widens: none · relaxes: none
- **F3 — What `charter-only`, `unique` and `never` each mean for a bare reference.** The systems
  table names `unique`'s and `never`'s reds and no third. RESOLVED (agent, 2026-10-23, delegated):
  §4 "### Bare references", rung 3, the reading under which each value has its own planted red.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-40, PLAY-dOrderedCharter-44, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-51, PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seams extended: `compute_coverage` and its three siblings (`tools/codebase-map/map_lib.py:1373,
1404, 1502, 1530`), moved and not rewritten; the `PARITY_ROWS` canonical-copy table
(`tools/lib/resolve-python.test.sh:168-184`); `common_git_dir` (`tools/memory-recall/query.py:248`);
blob reads through `read_blobs_at` (`tools/memory-tree/tree_lib.py:328`); recall's SQLite build
pattern (`tools/memory-recall/bench.py:88`, `query.py:381`). `reuse_lookup.py "build a blob-keyed
SQLite cache of what each file defines and cites"` ranked `key`, `keys`, `build`, `build_commit`,
`build_fixture` and `read_conf_key`, none an index of definitions; `bench.py`'s `build_index` is an FTS
ranking index, not a definition index, so no tag index exists. Where the scout and source disagree:
the run-gates canary's known-key set (`run-gates.test.sh:244,580`) refuses a new leg key, which the
scout's `pack` proposal did not name.

Recall terms used: `python tools/memory-recall/query.py "how is the tag index keyed and shared across worktrees" --terms "tag index sqlite index.db git-common-dir blob path dirty worktree resolver gov tag NT-15"`
