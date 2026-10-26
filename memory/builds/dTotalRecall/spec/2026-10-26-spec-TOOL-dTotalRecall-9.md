# TOOL-dTotalRecall-9 — the memory extractors, `record find` and `record show` over the one index, and the per-item read budget

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0220@d0de1caf whole

**Carries:** node:tag-namespace.section

**Carries:** node:tag-namespace.record

**Carries:** node:tag-namespace.feature

**Carries:** node:tag-namespace.class

**Carries:** node:tag-namespace.marker

**Carries:** node:policy-key.memory.item-budget

**Carries:** node:policy-key.memory.load-budget

**Carries:** node:policy-key.memory.over-budget

**Carries:** node:policy-key.memory.superseded-slices

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Memory has no index by key or section (gap-mem-20) and no read budget per item (gap-mem-21): an agent
finds a record by full-text search over a per-worktree cache and reads whole files. This unit registers
the `section`, `record`, `feature` and `class` extractors (and the `marker` namespace) into the one
index; reshapes memory-recall's `query.py` into `record find`, which returns at most 40 rows and no
content, reads rotated records under `memory/archive/` beside live ones, and takes over the
`check-recall` leg; adds `record show <id>#<tag>[@blob]`, one section; declares section tags per record
kind with legacy anchors derived; and holds a work order's memory slices to `memory.item-budget`, answered
as `memory.over-budget` says and outside `budgets.enforce`, with a superseded slice refused or marked as
`memory.superseded-slices` says, and the default load's memory share reported at session start against
`memory.load-budget` (systems `[design-memory-structure]`, `:504-548`).

## 2. Scope (IN)

Preconditions this unit calls and does not build, each cited by its parent spec: the registry
`tools/playbook/namespaces.toml`, the index and its writer `build_index`, the resolver `gov_tag.py`
and `TAG_RE` (PLAY-dOrderedCharter-19 S1, S2, S4, S6); the `id#tag` address form, unarmed until this
unit (PLAY-dOrderedCharter-24 §4, -28 §3); `policy_value.py`'s contract (PLAY-dOrderedCharter-7 §4) through
the memory-tree adapter (TOOL-dTotalRecall-8 S10); the caps census `tools/policy/caps.toml` and its `exempt`
class (TOOL-dGroundRules-9 S1); the load-set check in `render_handoff` (PLAY-dOrderedCharter-11 S4); the
card's `memory —` cell and `measure_index` (PLAY-dOrderedCharter-14 S2, S3); and the four catalogue rows
landed with no `summary` or `usage` (TOOL-dGroundRules-1 S3, S6).

- **S1** — The extractors, in `tools/memory-tree/record_extract.py`, each one `[[namespace]]` row of
  `tools/playbook/namespaces.toml` with `extractor = "record_extract:<function>"` (I12):
  - `record` (`extract_record`): one `blob_row` per record, tag `record.<kind>`, `text` its key, the
    kind the registry row whose `home` holds the path; a record is an id-anchored entry
    (`extract_records`'s anchors) or a record file under a build's `build`, `reviews` or `prompts`
    folder, keyed by its file stem (TOOL-dTotalRecall-19 S5); the source includes `memory/archive/`.
  - `section` (`extract_section`): one row per heading of a record file, tag `section.<seg>`, with
    `line` and `end_line` its extent; an authored `## [section.<seg>] Title` heading gives its tag, a
    heading its kind's `sections` table maps gives the mapped tag, and any other heading takes
    `section.<derive_anchor(...)>` as `read_legacy_anchors` admits under `memory.legacy-anchors`.
  - `feature` (`extract_feature`): one row per `gov:feature <tag>` anchor in tracked code, tag the
    anchor's `feature.*` tag.
  - `class` (`extract_class`): one row per `memory/gotchas/*.md` record whose front matter says
    `kind: class`, tag `class.<name>`.
  - `marker` (`extract_marker`): one row per `gov:<word>` marker in tracked text whose word fits `seg`,
    tag `marker.<word>`.
  An empty namespace prints `unarmed`, never green (PLAY-dOrderedCharter-19 S3). Observed by AC1 and AC2.
- **S2** — Section tags per kind: the registry `tools/memory-tree/record-kinds.toml` gains the column
  `sections`, a list of `{ tag, required, heading }` per kind, `heading` the legacy heading text the tag
  maps (the spec template's numbered headings: `1. Goal` to `section.goal`, through `10. Reuse audit`).
  A new record written through the door with a required section missing is refused by name. Observed by
  AC3.
- **S3** — `record find` in `tools/memory-tree/record_find.py`, run as `python gov_record.py find
  [<question> --terms <words>] [--kind <k>] [--tag <t>] [--build <slug>] [--paths <glob>]`, standing in for
  `gov record find`. Filters read the `record` and `section` rows; a question reads TOOL-dTotalRecall-21's
  FTS tables. `query_expr`, `search`, `rrf`, `run_rollup`, `derive_supersession_order` and `run_fusion`
  move from `tools/memory-recall/query.py` into `record_find.py`, unchanged in ranking, and `query.py`
  keeps its CLI as a thin adapter over them. At most 40 rows, one per record, `key · kind · build · bytes ·
  path:line`, no content, superseded rows hidden; past 40, the last line reads `<total> rows match;
  narrow with --kind, --build or --paths`. Observed by AC4 and AC5.
- **S4** — The `check-recall` leg taken over: `tools/memory-recall/check-recall.py` grades `record find`'s
  ranking through `record_find.run_fusion`, its floor unchanged, and the `recall floor` leg's guard in
  `tools/gate-legs.json` gains `{prefix}/memory-tree/record_find.py`. The leg keeps its name. Observed by
  AC6.
- **S5** — `record show` in `record_find.py`, run as `python gov_record.py show <id>[#<tag>][@<blob>]`:
  the section's text sliced from its blob at the row's `line` to `end_line`, or the whole record with no
  `#<tag>`; `@<blob>` reads that blob's rows. An unknown key or tag exits 2 naming it. `gov_tag.py show`
  resolves the `id#tag` form through the same rows, which arms it. Observed by AC7.
- **S6** — The item budget, `check_read_set(root, role, keys)` in `record_find.py`, run as `gov_record.py
  budget --role <role> <key>…`: the bytes of each key's `record show` slice, summed against the role's
  `memory.item-budget` (`measured` reads 96,000 bytes for every role until a role has 30 sliced work
  orders measured; `96` or `128` reads that many KB for every role; a per-role value reads that role's),
  a KB being 1,000 bytes. Over it, `memory.over-budget` answers: `refuse` exits 2 naming role, bytes and
  cap; `report`, the default, prints `memory over budget: <role> <bytes> B > <cap> B` and exits 0; `off`
  prints nothing. Observed by AC8.
- **S7** — Superseded slices: a key whose record the supersession map names superseded (S3's
  `derive_supersession_order` over TOOL-dTotalRecall-21's `fts_supersession` rows) is, under
  `memory.superseded-slices`, refused (`refuse`, the default: exit 2 naming the key and its successor)
  or marked (`mark`: the key passes, followed by `superseded-by <id>`). Observed by AC9.
- **S8** — The work order: `render_handoff` (`tools/roles/handoff.py:312`) and its CLI take `--read <key>`,
  repeated; before writing it runs `gov_record.py budget` as a subprocess found through
  `resolve_kit_dir`, as PLAY-dOrderedCharter-11 S4 runs its check, and writes a `reads:` list, one key per
  line with its bytes and any mark. A refusal refuses the render. The memory slices are outside
  PLAY-dOrderedCharter-11's load-set budget and its route-back, and one `[[cap]]` row in
  `tools/policy/caps.toml`, `name = "memory-slices"`, `class = "exempt"`, keeps them out of
  `budgets.enforce`'s refusal (I16). Observed by AC8 and AC10.
- **S9** — The default load's memory share: `render_card` passes the card's byte count to
  `memory_index.py measure --card-bytes <n>`, and the `memory —` cell reports the card and the
  auto-memory's remainder, each against `memory.load-budget` and each its own budget, not a share of it,
  at session start. Observed by AC11.
- **S10** — The four keys' catalogue rows gain `summary` and a `usage` line each row admits
  (`memory.item-budget = "128"`, `memory.over-budget = "refuse"`, `memory.superseded-slices = "mark"`,
  `memory.load-budget = "16k"`), and their names leave `tools/policy/unsummarised-keys.txt` through
  `policy.py lists --write`; the mirror lands in a second commit. Observed by AC12.

## 3. Non-goals (OUT)

- Inlining slice content into a work order and writing the slice manifest: dBoundRoles' renderer and the
  executor's. This unit hands keys with their bytes.
- The default load itself, what a session loads (PM-12): dWellOiledMachine's.
- Promoting the auto-memory's standing directives through `instructions.edit` (MS-1):
  PLAY-dOrderedCharter-14 S4 builds `memory_index.py promote` over PLAY-dOrderedCharter-15's command.
- Deriving each role's p90 under `measured` from 30 measured work orders: the Loop Review's.
- The annotations system that writes `gov:feature` anchors and grades `gov:` words: dLinkedLibrary's.
  This unit registers the namespaces and reads what exists.
- memory-recall's why-search, bench and union: dLinkedLibrary's (the fates, SA-6).

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record-kinds.toml`, whose rows this unit gives the `sections`
  column and whose `home` column decides a record's kind
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py`, the door CLI that gains the `find`, `show`
  and `budget` verbs
- **consumes-from** `TOOL-dTotalRecall-10` — `derive_anchor`, which derives a legacy heading's section
  tag
- **consumes-from** `TOOL-dTotalRecall-19` — `memory.legacy-anchors` through `read_legacy_anchors`, and
  the `record-key` native class `record show` resolves an `<id>` through
- **consumes-from** `TOOL-dTotalRecall-8` — `policy_value.py`, the memory-tree kit's `read_policy_value`
  adapter the budget and slice keys are read through
- **consumes-from** `TOOL-dTotalRecall-21` — `build_fts_rows` and the `fts_record`, `fts_chunk` and
  `fts_supersession` tables `record find` searches
- **hands-off** `TOOL-dTotalRecall-23` — `record find` and the `record` and `section` rows, which the
  memory legs read for an unchanged blob
- **hands-off** `TOOL-dTotalRecall-12` — `record find` and `record show`, two of the shell commands the
  re-measure counts
- **hands-off** `TOOL-dTotalRecall-43` — `record_extract.py`, the `sections` column and `record_find.py`, which that unit changes for the round-1 audit's ids 7, 11, 12, 31, 34, 45 and 62

## 4. Design

### The rows

Every extractor writes `blob_row(blob, extractor, tag, kind, line, end_line, text)` (PLAY-dOrderedCharter-19
S4). For one record file:

| extractor | tag | kind | line, end_line | text |
|---|---|---|---|---|
| `record` | `record.shape-run` | `shape-run` | 1, last | its key |
| `section` | `section.findings-2` | `shape-run` | the heading's line, the line before the next heading of its level or above | the heading |

A key resolves to its rows through `path_row` and `tree_path` for the served tree, a dirty row winning for
its worktree. `record show <key>#<tag>` slices the blob's bytes between the two lines; with `@<blob>`
it reads that blob's rows whatever the tree.

### The section table

```toml
[[record-kind]]
name = "spec"
sections = [
  { tag = "section.goal", required = true, heading = "1. Goal" },
  { tag = "section.scope", required = true, heading = "2. Scope (IN)" },
  # … one row per TEMPLATE-SPEC section, through
  { tag = "section.reuse-audit", required = true, heading = "10. Reuse audit" },
]
```

A legacy heading the table maps takes the table's tag; an unmapped untagged heading takes its derived
anchor under `derived`, nothing under `none`, and an authored tag only under `retag`. An authored tag is
unique in its record; a derived one is not graded (TOOL-dTotalRecall-10).

### `record find`

```
python gov_record.py find --kind deviation --build dTotalRecall
2026-10-26-build-TOOL-dTotalRecall-21-deviation-211 · deviation · dTotalRecall · 1834 · memory/builds/dTotalRecall/build/…:1
```

Rows sort by build, then key. A question ranks by today's fusion over the FTS tables, then applies the
same filters and cap. The total line is the only line past the rows, so a reader that counts lines
counts rows plus one at most.

### The budget answer

| `memory.over-budget` | under the cap | over the cap |
|---|---|---|
| `refuse` | render | exit 2, nothing rendered |
| `report` (default) | render | render, report line with role and bytes |
| `off` | render | render |

The answer never reaches `budgets.enforce`: memory slices are its census's `exempt` row, so neither
`warn` nor `refuse` there moves them.

### Inventory

Minted: `tools/memory-tree/record_extract.py` (`extract_record`, `extract_section`, `extract_feature`,
`extract_class`, `extract_marker`), `tools/memory-tree/record_find.py` (`find_records`, `show_record`,
`check_read_set` and the moved fusion functions), the verbs `find`, `show` and `budget`, five namespace
rows, the `sections` column, the `memory-slices` cap row, `handoff.py render --read`. Naming cells: each
function is asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

The index builds the new rows on its next build; no record is rewritten. `query.py`'s CLI keeps its
arguments and output, so a caller of it sees no change.

### Files touched (estimate)

- `tools/memory-tree/record_extract.py` (new)
- `tools/memory-tree/record_find.py` (new)
- `tools/memory-tree/gov_record.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/memory-recall/query.py`
- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/selftest.py`
- `tools/playbook/namespaces.toml`
- `tools/playbook/memory_index.py`
- `tools/roles/handoff.py`
- `skills/session-kickoff/manifest-check.sh`
- `tools/policy/caps.toml`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `tools/gate-legs.json`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **`record find` returning content.** The read budget exists because whole-file reads are the cost; a
  finder that returns content is a second read channel nothing budgets.
- **A cutoff on `record find`'s population for the archive.** FK-11-1 reads rotated records beside live
  ones; the corpus walk already admits `archive/` (`tools/memory-recall/extract.py:24-30`).
- **The item budget inside `budgets.enforce`.** MS-3 keeps memory slices out of that switch, and
  `memory.over-budget` is the one answer.

## 5. Production-readiness checklist

- security — read-only over tracked records and the index; the handoff's new argument is a key list,
  each key resolved before any write, and a refused key refuses the render.
- perf / scale — `record find` reads rows, not files; `record show` reads one blob slice.
- error / empty / loading states — an empty namespace prints `unarmed`; an unknown key exits 2 naming it;
  a refused policy read exits 2 naming the key.
- observability — the total line, the report line and the card cell each name the figures.
- risks — the 40-row cap hides matches past it; the total line names them and the filters narrow.
- testing — AC1 to AC12 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — `tools/memory-tree/README.md` gains the three verbs; no page under `help/` covers memory
  reads.

## 6. Acceptance criteria

- **AC1** — When `gov_tag.py check` runs over the index built at the pass tip, its summary names the
  namespaces `record`, `section`, `class` and `marker` with members, `class` with 145, and `feature` as
  `unarmed`.
  Red when: an empty `feature` namespace prints green, or a namespace row is registered with no
  extractor.
  figure: DERIVED at observation; 145 class records at `fb872a37`.
- **AC2** — When `python gov_record.py show <stem>#section.findings-2` runs over a fixture build record
  whose untagged `## Findings` repeats, the second section is returned, and the record's `record.<kind>`
  row names the stem as its key.
  Red when: the section extractor folds headings itself instead of calling `derive_anchor`.
- **AC3** — When `gov_record.py new spec` renders a fixture spec with `## 6. Acceptance criteria` removed,
  it exits 2 naming `section.acceptance-criteria`; a legacy spec's `## 1. Goal` resolves as
  `section.goal`.
  Red when: the section table is read for legacy headings but not for new records.
- **AC4** — When `python gov_record.py find --build dClosedLoop` runs, it prints 40 rows and a 41st line
  naming the total and `--kind`; with `--kind deviation --build dTotalRecall` it prints only rows of that
  kind with no total line.
  Red when: the cap truncates silently, so 40 rows print and nothing names the rest.
- **AC5** — When `gov_record.py find` runs with a question whose only answer is a decision row held in a
  dated file under `memory/archive/`, it returns that row's key; with a decision another names superseded,
  only the successor's row prints.
  Red when: the archive is outside the record extractor's source, or a superseded row is returned.
- **AC6** — When `python check-recall.py --data-dir <a scratch index>` runs from `tools/memory-recall/`, its
  graded rows equal those the pass's base computes, and `git grep -n "def run_fusion" -- tools` prints one
  line, in `record_find.py`.
  Red when: the leg grades a copy of the fusion that `record find` does not run.
- **AC7** — When `gov_record.py show <key>#section.nope` runs, it exits 2 naming `section.nope`; `show
  <key>@<an older blob of it>` returns that blob's text; `gov_tag.py show <key>#<tag>` prints the same
  section as `record show`.
  Red when: `id#tag` still prints `unarmed` in the resolver.
- **AC8** — When `python handoff.py render --role gov-builder --build <slug> --read <key>` runs in a fixture
  whose key's slice is 130,000 bytes, it renders and prints `memory over budget: gov-builder 130000 B >
  96000 B` under the default; with `memory.over-budget = "refuse"` committed, it exits 2 and writes no file;
  under `off` it prints no report line.
  Red when: the report line is missing its role or bytes, or `refuse` renders the file.
- **AC9** — When the fixture's decision `DEC-tFix-1` is superseded by `DEC-tFix-2` and `handoff.py render
  --role gov-builder --read DEC-tFix-1` runs, it exits 2 naming `DEC-tFix-2`; with
  `memory.superseded-slices = "mark"` it renders and the `reads:` line carries `superseded-by DEC-tFix-2`.
  Red when: a superseded decision is handed to a builder unmarked.
- **AC10** — When `budgets.py` from `tools/policy/` reads the census with `budgets.enforce = "refuse"`
  committed in the AC8 fixture, the over-cap render still succeeds under `report`, and the census lists
  `memory-slices` with class `exempt`.
  Red when: the slices reach the switch, so `refuse` there refuses the render.
- **AC11** — When `render_card` in `manifest-check.sh` renders the card in a fixture whose auto-memory index is 9,000
  bytes, the `memory —` cell names the card's bytes and the index's 9,000 against 8,000, the index marked
  over.
  Red when: the card and the remainder share one budget, so a small card hides the remainder's breach.
- **AC12** — When `python policy.py get <key> --explain` runs from `tools/policy/` for each of the four
  keys, it prints `measured`, `report`, `refuse` and `8k`, and
  `grep -cE "memory\.(item-budget|over-budget|superseded-slices|load-budget)" unsummarised-keys.txt` prints `0`.
  Red when: a `summary` lands and the name stays on the shrink-only list.

## 7. Gates

`recall floor` · `recall floor arms` · `memory-recall kit selftest` · `build-index selftest` · `memory hygiene` · `playbook render selftest` · `govkit acceptance matrix` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates`

New arm: tools/memory-tree/record_find.py · covers AC4 AC5 AC7 AC8 AC9 · its selftest's planted 41-row population, archived decision, superseded decision handed to a builder, and over-cap read set under each `memory.over-budget` value, staged by the cap line cut and by `memory.superseded-slices` read and ignored · none
New arm: tools/memory-tree/record_extract.py · covers AC1 AC2 AC3 · the five extractors over a fixture tree with a repeated H2, a missing required section and an empty `feature` namespace, staged by `extract_section` folding headings without `derive_anchor` · none
New arm: tools/memory-recall/test_recall_floor.py · covers AC6 · the floor arms run through `record_find.run_fusion`, staged by a second fusion copy left in `query.py` · none

## 8. Open questions

- **F1 — How is a record keyed in `record find` and `record show`?** Options: (a) an id-anchored entry by
  its id and a record file by its stem, both one `record` row; (b) ids only, a record file addressed by
  the unit it serves; (c) paths. (b) gives every record of a unit one address; (c) is not an address
  form of PLAY-dOrderedCharter-24's table. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  systems `:518` (`record show <id>#<tag>`) and TOOL-dTotalRecall-19 S5's `record-key` class.
  widens: none · relaxes: none
- **F2 — Where do section declarations live?** Options: (a) a `sections` column on the registry;
  (b) the `section` namespace's own declaring file. systems `:508` puts them in "each record kind's
  registry entry". RESOLVED (agent, 2026-10-26, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — Does `check-recall.py` move into memory-tree with the finder?** Options: (a) it stays in
  memory-recall and grades `record_find`'s fusion, the `recall floor` leg keeping its name and gaining
  the finder in its guard; (b) it moves into memory-tree as a new leg. (b) renames a leg, which the
  design refuses ("a leg keeps its name"), and moves dLinkedLibrary's bench neighbour. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the fates' "the record finder's leg" met with the fewest moves.
  widens: none · relaxes: none
- **F4 — Under `measured`, what does a role's cap read before 30 work orders are measured?** Options:
  (a) 96,000 bytes, v2:1370's "96 for every role until 30 sliced work orders per role are measured";
  (b) no cap. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1370. widens: none · relaxes: none
- **F5 — A work order carries no read set today; where does one enter?** Options: (a) `--read` keys on
  `handoff.py render`, checked and written as a `reads:` list, dBoundRoles' renderer later filling them;
  (b) no entry until dBoundRoles, the budget a library function nothing calls. (b) cannot be seen red on
  a superseded decision handed to a builder, the clause's case. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the only option meeting AC8 and AC9. widens: none · relaxes: none
- **F6 — Every surface this unit calls is specced and unbuilt at HEAD; whose spelling binds?**
  Options: (a) the parent specs' spellings as cited in §2, the build run re-grounding on the landed
  code and bumping this spec's rev before any code where they differ; (b) wait for the parents.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, BUILD-METHOD M2 ("to diverge, change the spec
  first") and the brief's rule that a spec calls each parent surface as its spec names it.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 9, the brief's I8, I11, I12, I15 and I16, scout
  B's row for cl-0220, systems `[design-memory-structure]` and `[design-tags]`, and `query.py`,
  `extract.py` and `handoff.py` read at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are memory-recall's fusion (`tools/memory-recall/query.py:759-935`, `query_expr`
through `run_fusion`), moved into `record_find.py` rather than copied; its record anchors
(`extract_records`, `anchor_at`, `tools/memory-recall/extract.py:551`, moved to `id_grammar.py` by
PLAY-dOrderedCharter-18) for the `record` extractor; its supersession readers (`extract.py:673`, `:706`;
`query.py:862`) for S7; `render_handoff` (`tools/roles/handoff.py:312`) as the work order; and
PLAY-dOrderedCharter-19's namespace rows and `build_index` for the extractors. No existing seam fits the
40-row cap with a total line (the only cap is `RESULT_CAP = 5` per record, `query.py:176`), the per-kind
section table, or the item budget. The lookup,
`python tools/codebase-map/reuse_lookup.py "find records by kind tag or build and show one section"`,
ranked generic `build` and `records` stems, `extract_records`, `read_records` and `render_record`; none
filters records by kind or slices a section. Disagreements with source: scout B says no work-order renderer
exists at HEAD, and `render_handoff` renders the role handoff this unit treats as the work order; scout B's
archive citation `extract.py:28-30` is the docstring at `:24-30`, the durable-home rule at `:190`. The
recall probe returned scout B's row, the packet clause and the brief's row; none disagreed otherwise.

Recall terms used: `python tools/memory-recall/query.py "how does record find and record show read sections from the index under a read budget" --terms "record find record show section extractor item-budget over-budget superseded-slices load-budget work order slice archive"`
