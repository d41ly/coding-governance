# TOOL-dLinkedLibrary-5 — the generated views: the decision log's holds-now view and the reuse view

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 9 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0242@866cebbc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

Which decisions hold today is found only by walking supersession chains by hand, though 47 log rows
chain a supersession or narrowing (gap-mem-02) and memory-recall's supersession map already tags
superseded hits; and no view lists the reuse entries an owner has accepted. Layer-memory `[views]`
names both among the owner's generated views: the decision log's "holds now" view, which renders
that map, and the reuse view, "features and conventions by area, with their directives". This unit
renders the two through TOOL-dLinkedLibrary-6's library-view seam, beside dTotalRecall's README routing
and relation graph, which it reads by linking to them and never renders again.

## 2. Scope (IN)

- **S1** — Two rows of `VIEWS` in `tools/memory-tree/library_views.py`: `holds-now` at
  `views/holds-now.md` with its renderer `render_holds_now`, an empty render red; and `reuse` at
  `views/reuse.md` with `render_reuse`, an empty render the line `No reuse entry yet.` and no finding.
  `LIBRARY_VIEWS` in `.memory-tree.conf` reads `research holds-now reuse`. Observed by AC3, AC4 and AC6.
- **S2** — The holds-now population. The log's rows are the id-anchored records
  `id_grammar.extract_records` (PLAY-dOrderedCharter-18 S1) returns for `memory/DECISIONS.md`; the
  supersession edges are those `id_grammar.extract_supersessions` returns over the log, its rotated
  archives under `memory/archive/` and every spec the build index lists; the map is
  `id_grammar.derive_supersession_map(edges, defined)`, `defined` the ids of the log, its archives and
  those specs. A row holds now when no `whole` edge names it old; it is narrowed when only `partial`
  edges do. The recall kit's copies, `tools/memory-recall/extract.py:673` and :706, are never
  imported (shared interface I7). Observed by AC1 and AC7.
- **S3** — The holds-now view. Under the H1 `# Holds now — the decision log after supersession`, the
  count line `<h> rows hold now · <s> superseded · <p> narrowed`; then one `## <family heading>` per
  `## ` heading of the log, in the log's order, each a table of its holding rows in log order, `| <id>
  | <build> | <decides> | <decision> | <narrowed by> |`: `<build>` a relative link to the build's
  README, where dTotalRecall's routing region (TOOL-dTotalRecall-4 S5) and relation graph
  (TOOL-dTotalRecall-6 S7) stand; `<decides>` the row's `decides` targets as TOOL-dLinkedLibrary-22's
  `derive_decision_rows` (`tools/memory-tree/row_grammar.py`, its S5 and S6) returns them, the
  commit that first added the row among them; `<decision>` the row's text with `|` escaped; `<narrowed by>` the ids
  of its partial edges, or `—`. A last section `## Superseded` lists each superseded row as `<old> →
  <new>[, <new>…]`. Observed by AC1 and AC2.
- **S4** — The reuse view. Under the H1 `# Reuse — features and conventions, with their directives`,
  the count line `<a> accepted · <p> proposed`; then `## Features` and `## Conventions`, the two areas
  an entry's part sits in, each a table of its accepted entries sorted by `reuse.tag`, `| <tag> |
  <directive> | <needs> | <anchors> | <build> |`; then `## Proposed, awaiting the owner`, one row per
  `proposed` entry with a relative link to its proposal record. A `rejected` entry is not rendered.
  The entries are those TOOL-dLinkedLibrary-1's `read_reuse_entries` returns. Observed by AC3 and AC4.
- **S5** — Never rendered again. `render_library_views` refuses a `VIEWS` row whose file is not under
  `<MEMORY_ROOT>/views/`, naming the row, before any render, so no library view writes a build README
  or the regions dTotalRecall renders there. Observed by AC5.
- **S6** — The fixture cases `holds-now`, `holds-now-decides`, `holds-now-empty`, `reuse`,
  `reuse-empty` and `outside-views`, added to `python library_views.py --fixture`, which
  `gen_build_index.py --selftest` already runs case by case (TOOL-dLinkedLibrary-6 S7). Observed by AC1
  to AC5.
- **S7** — The docs: the memory-tree README's library-view section names the two views and their
  sources; `KIT_MEMORY_TREE_VERSION` moves. NOT OBSERVED by a criterion: prose, graded by `memory
  hygiene` at the close.

## 3. Non-goals (OUT)

- The seam, the switch, the host, the orphan scan and the folder: TOOL-dLinkedLibrary-6's.
- The log's rows and their routing, and the reuse entries and their states: TOOL-dLinkedLibrary-1's.
- The `decides` segment's grammar and its reader `derive_decision_rows`: TOOL-dLinkedLibrary-22's.
- The README routing region and the relation graph: dTotalRecall's, linked here and never rendered.
- The archive's rows as holding decisions: they left the log by rotation, so the view renders the
  live log; the archive is read only for the ids an edge resolves against.
- Ranking entries or rows by use: the views list, they do not score.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-6` — `library_views.py`, the seam whose `VIEWS` table this unit's two rows join and whose host renders and compares them
- **consumes-from** `TOOL-dLinkedLibrary-1` — `reuse.toml`, the entries `read_reuse_entries` returns, with their states, for the reuse view
- **consumes-from** `TOOL-dLinkedLibrary-22` — `decides`, the targets each holding row's `<decides>` cell renders
- **consumes-from** external — PLAY-dOrderedCharter-18 S1's `id_grammar.py` (`extract_records`, `extract_supersessions`, `derive_supersession_map`); TOOL-dTotalRecall-4 S5 and -6 S7, the README regions the build cell links to; each DEFERRED at base and built before this build run
- **hands-off** `TOOL-dLinkedLibrary-52` — the holds-now view's `<build>` cell, which unit 52 links only where the README is tracked (id 23)
- **hands-off** `TOOL-dLinkedLibrary-53` — the §7 leg line, which unit 53 completes with `policy fixtures` unless this unit's pass adds it first (id 56)

## 4. Design

### Evidence

- `extract_supersessions` (`tools/memory-recall/extract.py:673`) yields `(old, new, kind, pattern)`
  from P1 `supersedes <id>`, P2 `superseded by <id>` and P3, a spec status line's `superseded by` list;
  `derive_supersession_map` (:706) drops an edge whose end `defined` lacks and returns `{old: [[new,
  kind], …]}`. `query.py` calls both (:352-355). PLAY-dOrderedCharter-18 S1 moves them unchanged into
  `tools/memory-tree/id_grammar.py`.
- `memory/DECISIONS.md` holds four family sections (:8, :14, :20, :140) and 213 rows at `82a392696`
  (PINNED); `memory/archive/DECISIONS.2026-08-10.md` holds the 79 rows its rotation note (:3) names.
- A row's id names its build: `<FAMILY>-<slug>-<seq>`, and `memory/builds/<slug>/README.md` exists for
  each build the log's ids name, the routing and relation regions rendered there by dTotalRecall.

### The holds-now view, in shape

```markdown
<!-- generated by tools/memory-tree/gen_build_index.py --write from memory/DECISIONS.md; do not hand-edit -->
# Holds now — the decision log after supersession

<h> rows hold now · <s> superseded · <p> narrowed

## TOOL — tooling

| Id | Build | Decides | Decision | Narrowed by |
|---|---|---|---|---|
| TOOL-aExample-3 | <relative link to ../builds/aExample/README.md> | feature.x | <row text> | — |

## Superseded

- TOOL-aExample-1 → TOOL-aExample-3
```

### The reuse view, in shape

```markdown
# Reuse — features and conventions, with their directives

<a> accepted · <p> proposed

## Features

| Feature | Directive | Needs | Anchors | Build |
|---|---|---|---|---|
| feature.media-picker | MUST reuse the media picker wherever … | media selection; a new page | gov:feature media-picker | dExampleBuild |

## Conventions

## Proposed, awaiting the owner
```

A list cell joins its values with `; ` and escapes `|`. Every figure is DERIVED at each render.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_holds_now`, `render_reuse` | functions, `library_views.py` | `py.function`, asked at the pass |
| the `holds-now` and `reuse` rows of `VIEWS` | view names | none |
| `holds-now.md`, `reuse.md` | the views under `memory/views/` | none |

### Migration

None: the first `--write` after landing creates both files.

### Rollout

Live at landing in gov, where `LIBRARY_VIEWS` names both; an adopter names them to opt in.

### Files touched (estimate)

- `tools/memory-tree/library_views.py`: S1 to S6
- `.memory-tree.conf`: `LIBRARY_VIEWS`
- `tools/memory-tree/README.md`: S7
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`
- `memory/views/holds-now.md` and `memory/views/reuse.md`: new, generated

### Alternatives rejected

- **The supersession map read from the recall index.** Recall is optional; I7 names `id_grammar`'s
  functions as the one map, and a view that read the recall cache would go stale with it.
- **The archive's rows in the holds-now view.** After TOOL-dLinkedLibrary-1's routing the archive holds
  rows routed to other homes; rendering them as holding would undo the split.
- **A rejected entry rendered with its state.** The view lists what an agent may be told to reuse and
  what the owner must rule on; a rejected entry is neither.

## 5. Production-readiness checklist

- security — no new write surface: the generator writes two files under `memory/views/` from
  tracked text, every table cell escaped.
- perf / scale — `extract_supersessions` over the log, one archive and the specs the index already
  lists; measured cost is the build run's, inside a verb that reads every spec already.
- error / empty / loading states — an empty holds-now view is red; an empty reuse view prints its
  line; an edge naming an unknown id is dropped and counted by `derive_supersession_map`, as today.
- observability — each view's count line; `--write` names each file.
- risks — a supersession written in prose the three patterns do not match leaves a row holding; the
  patterns are the recall kit's, moved, and their limits travel with them.
- testing — S6's fixture cases, run by `gen_build_index.py --selftest`.
- migration — none.
- user docs — the memory-tree README; no `help/` page covers memory views.

## 6. Acceptance criteria

- **AC1** — When `python library_views.py --fixture --plant holds-now` renders a log of five rows,
  where row B's text supersedes row A and a spec's status line narrows row C, the view lists B, C, D
  and E under their family headings, C's `Narrowed by` cell naming the spec, `## Superseded` reads `A →
  B`, and the count line reads `4 rows hold now · 1 superseded · 1 narrowed`.
  Red when: A is listed as holding, or C's narrowing is lost.
- **AC2** — When the plant `holds-now-decides` gives row D one `decides=feature.x` segment, D's
  `Decides` cell names `feature.x` beside the commit that added D, and E's names its commit alone.
  Red when: a row's `decides` target is not rendered, or a target is read other than through
  `derive_decision_rows`.
  fixture: the segment's grammar is TOOL-dLinkedLibrary-22's, absent at base until it lands.
- **AC3** — When the plant `reuse` renders two accepted feature entries, one accepted convention, one
  proposal and one rejected proposal, the view holds two rows under `## Features` in tag order, one
  under `## Conventions`, one under `## Proposed, awaiting the owner` whose link names the proposal
  record, no rejected entry, and the count line `3 accepted · 1 proposed`.
  Red when: a rejected entry renders, or an area holds the other's entry.
- **AC4** — When the plant `reuse-empty` renders no entry, the view's body reads `No reuse entry yet.`
  and `gen_build_index.py --check` in the fixture prints no library-view verdict; when the plant
  `holds-now-empty` renders a log with no row, `--check` prints `holds-now.md renders no row` and exits
  1.
  Red when: an empty reuse view reds, or an empty holds-now view passes.
- **AC5** — When the plant `outside-views` adds a `VIEWS` row whose file is a build's `README.md`,
  `render_library_views` refuses naming that row and nothing is written; with all three views armed,
  every path it returns starts with `memory/views/`.
  Red when: a library view's path leaves `views/`.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip, it
  reports no drift for `holds-now.md` or `reuse.md`, and the holds-now count line's holding and
  superseded figures sum to the rows `python decision_rubric.py rows` prints.
  Red when: either view drifts from its render, or the view's population is not the log's.
  figure: DERIVED at observation.
- **AC7** — When `grep -nE "memory-recall|from extract import|import extract" library_views.py` runs
  over the module at this unit's tip, it prints nothing, and `grep -n "id_grammar"` there names the
  import of `derive_supersession_map`.
  Red when: the view reads the recall kit's copy of the map.

## 7. Gates

`memory hygiene` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC3 AC4 AC5 · the `--selftest` arm TOOL-dLinkedLibrary-6 adds, gaining the six cases of S6, its failing case the `holds-now` plant listing a wholly superseded row · none

## 8. Open questions

- **F1 — Is an empty reuse view red?** Options: (a) no: it renders `No reuse entry yet.`, while an
  empty holds-now view is red; (b) every library view red when empty, as the research view is; (c)
  the reuse view armed only once an entry exists. RESOLVED (agent, 2026-10-26, delegated): (a), rung
  3, the most feature-rich survivor: (b) reds gov's tree between TOOL-dLinkedLibrary-1's landing and
  the first accepted entry and every adopter that opts in before its first entry, a state the design
  intends (entries arrive one owner disposition at a time), and (c) derives the switch from the
  population, which `[gate]` refuses; the research view's empty red stays, as its layer witness
  names it. TOOL-dLinkedLibrary-6's `VIEWS` row carries the choice per view.
  widens: none · relaxes: none
- **F2 — Which rows does the holds-now view render?** Options: (a) the live log only, its archives
  read for edge resolution; (b) the log and every rotated archive. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1: the clause's view is "the decisions' holds-now view" of "the major-decision
  log" (cl-dClosedLoop-0238, cl-dClosedLoop-0242), and after the routing the archive holds rows whose
  homes are elsewhere. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 5, layer-memory `[views]` and
  `[decisions]` item 2, PLAY-dOrderedCharter-18 S1, TOOL-dTotalRecall-4 S5 and -6 S7, and scout A's
  row 5.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-52, TOOL-dLinkedLibrary-53, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dLinkedLibrary-6's `library_views.py`, whose `VIEWS` table and host this
unit adds two rows to; `id_grammar`'s `extract_records`, `extract_supersessions` and
`derive_supersession_map`, moved by PLAY-dOrderedCharter-18 S1 from `tools/memory-recall/extract.py`
(:673, :706, verified at base) and called, never copied; TOOL-dLinkedLibrary-1's `read_reuse_entries`;
and TOOL-dLinkedLibrary-22's `decides` reader. `python tools/codebase-map/reuse_lookup.py "render the
current holds-now decisions after supersession and the reuse entries as generated views"` ranked
`render`, `render_family_view` and `derive_supersession_map`; the last is the map S2 calls through its
new home, and no existing renderer lists decisions or entries, so no existing seam fits the two view
bodies. Scout A's row cited `render_asbuilt_view` at `gen_build_index.py:1474` and the byte compare at
:2807-2830; the compare TOOL-dLinkedLibrary-6 lands is its own, in the host it adds beside :1474.

Recall terms used: `python tools/memory-recall/query.py "how is the holds-now view of superseded decisions rendered" --terms "holds-now view supersession map derive_supersession_map decision log superseded rows reuse view directives"`
