# TOOL-dTotalRecall-9 — the memory extractors, `record find` and `record show` over the one index, and the per-item read budget

**Status:** CLOSED · rev-7 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

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
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-9-deviation-91.md](../build/2026-10-26-build-TOOL-dTotalRecall-9-deviation-91.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-9-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dTotalRecall-9-1-acceptance-ledger.md) | log | — |
| [2026-11-22-build-TOOL-dTotalRecall-9-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-9-reground-return.md) | research | — |
| [2026-11-23-build-TOOL-dTotalRecall-9-deviation-1006.md](../build/2026-11-23-build-TOOL-dTotalRecall-9-deviation-1006.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-8 TOOL-dTotalRecall-11 TOOL-dTotalRecall-15 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-43 TOOL-dTotalRecall-76 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-11-22-prompt-TOOL-dTotalRecall-9-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-9-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-9-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-9-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-9-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-9-reground-spec-writer.md) | log | — |
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

Preconditions this unit calls and does not build, each cited by its parent spec and read at HEAD
`ed5a7d523`: the registry `tools/playbook/namespaces.toml`, read by `tag_index.py#read_namespaces`, each
row carrying every field of `tag_index.py#REGISTRY_FIELDS`; the index, its writer `tag_index.py#build_index`,
its served view `tag_index.py#load_view`, the resolver `gov_tag.py` and `tag_index.py#TAG_RE`
(PLAY-dOrderedCharter-19 S1, S2, S4, S6); the `id#tag` address form, parsed by `edge_grammar.py#FORMS` and
answered `unarmed` by `edge_grammar.py#resolve_edge` until this unit (PLAY-dOrderedCharter-24 §4, -28 §3);
the memory-tree kit's one policy read `tree_lib.py#read_policy_value` (TOOL-aNimbleMend-8 S7); the caps
census `tools/policy/caps.toml`, its `exempt` class (`budgets.py#OUTSIDE`) and `check_policy.py#CAP_CASES`
(TOOL-dGroundRules-9 S1); the load-set check `handoff.py#render_handoff` runs through
`roles_lib.py#check_load_set` (PLAY-dOrderedCharter-11 S4); the card's `memory —` cell, derived by
`manifest-check.sh`'s `derive_memory_line` from `memory_index.py#measure_index` (PLAY-dOrderedCharter-14 S2,
S3); the four catalogue rows landed with no `summary` or `usage` (TOOL-dGroundRules-1 S3, S6); and each
leg's one declaration, from which `tools/run-gates/leg_factory.py --write` renders `tools/gate-legs.json`
(TOOL-dWitnessedBar-11 S1, S2).

- **S1** — The extractors, in `tools/playbook/record_extract.py` (§8 F7), each one `[[namespace]]` row of
  `tools/playbook/namespaces.toml` with `extractor = "record_extract:<function>"` (I12), `owner` and
  `join-armed-by` `dTotalRecall`, `layer` `layer.memory`, and every other field of `REGISTRY_FIELDS`. Each
  keeps the contract `tag_index.py#load_extractors` and `#_derive_applicable` call: `extract_<x>(ctx, path,
  text=None)` answers `None` for a path it does not read, and with `text` returns the `(tag, kind, line,
  end_line, text)` rows `tag_index.py#_write_parsed` writes to `blob_row`. A row defines its tag only where
  its `kind` is one of `tag_index.py#DEFINE_KINDS`, the rows `#derive_namespace_state` counts and
  `#check_resolves` grades citations against.
  - `record` (`extract_record`): one `tag` row per `[[record-kind]]` row of
    `tools/memory-tree/record-kinds.toml`, its `tag` cell at its line, so each `record.<kind>` that
    `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` cite resolves, a pocket kind with no
    record file among them; and one `record` row per record, a kind no definition counts, tag
    `record.<kind>`, `text` its key, the kind the row `derive_record_kind` returns (TOOL-dTotalRecall-42
    S5, §8 F8), empty where it returns `None`. A record is an id-anchored entry
    (`id_grammar.py#extract_records`' anchors, a spec's defining H1 among them) or a record file under a
    build's `build`, `reviews` or `prompts` folder (`tree_lib.py#record_paths`), keyed by its file stem
    (TOOL-dTotalRecall-19 S5); the source includes `memory/archive/`.
  - `section` (`extract_section`): one `section` row per heading of a record file or spec, tag
    `section.<seg>`, with `line` and `end_line` its extent; an authored `## [section.<seg>] Title` heading
    gives its tag, a heading whose title its kind's `sections` table maps gives the mapped tag, and any
    other heading takes `section.<derive_anchor(...)>` as `read_legacy_anchors` admits under
    `memory.legacy-anchors`.
  - `feature` (`extract_feature`): one `tag` row per `gov:feature <tag>` anchor in tracked code, tag the
    anchor's `feature.*` tag; none exists at HEAD (DERIVED, `git grep -n "gov:feature" -- ':!memory'`).
  - `class` (`extract_class`): one `tag` row per `memory/gotchas/*.md` record whose front matter says
    `kind: class`, tag `class.<name>`; each name fits `tag_index.py#TAG_MAX_BYTES`
    (longest 61 bytes DERIVED by `git grep -h "^name:" -- 'memory/gotchas/*.md'`).
  - `marker` (`extract_marker`): one `tag` row per `gov:<word>` marker in tracked text whose word fits
    `seg`, tag `marker.<word>`.
  An empty namespace prints `unarmed`, never green (PLAY-dOrderedCharter-19 S3): `gov_tag.py#run_check`
  prints `tags: unarmed <ns>`. Observed by AC1 and AC2.
- **S2** — Section tags per kind: the registry `tools/memory-tree/record-kinds.toml` gains the column
  `sections`, which `record_kinds.py#LATER_COLUMNS` admits as this unit's, a list of `{ tag, required,
  heading }` per kind, `heading` the section's title with its `<n>. ` number stripped, the keys of
  `gen_build_index.py#SPEC_TITLE_NUMBERS` on the spec row (`Goal` to `section.goal`, through `Reuse
  audit`), so a Tier-1 spec's renumbered headings map as a Tier-2 spec's do. `required` is true for the
  eight sections both tiers carry and false for `Production-readiness checklist` and `Reuse audit`, which
  a Tier-1 spec may omit (`memory/TEMPLATE-SPEC.md`, "Tier profiles"). One reader, `read_sections(row)` in
  `tools/memory-tree/record_kinds.py`, returns the cell, refusing one that is not a list of such tables
  by its kind's name; a kind with no cell maps no heading and requires none. A new record written
  through the door with a required section missing is refused by name before any byte is written:
  `check_sections(row, text)` in `record_kinds.py` returns the missing tags, and the spec handler's
  scaffold `gen_build_index.py#cmd_new_spec` calls it between `render_spec_skeleton` and `write_text`.
  The spec row is the only row a `sections` cell lands on, so no `fields` kind's write moves. Observed
  by AC3.
- **S3** — `record find` in `tools/memory-tree/record_find.py` (§8 F7), `scan_records`, run as `python
  gov_record.py find [<question> --terms <words>] [--kind <k>] [--tag <t>] [--build <slug>] [--paths
  <glob>]`, standing in for `gov record find`. It reaches `tag_index.py` through the kit's inline
  `resolve_kit_dir` block at call time, never at import, and exits 2 naming the playbook-render kit where
  that does not resolve. Filters read the `record` and `section` rows of the served view
  (`tag_index.py#load_view`, `#VIEW_JOIN`); a question reads TOOL-dTotalRecall-21's FTS tables over the
  connection its `load_served_set` (TOOL-dTotalRecall-21 S3) returns with `recall_view` filled, that
  memory-recall function reached through `resolve_kit_dir` at call time and its kit named in an exit 2
  where it does not resolve, so a filter-only `find` needs no recall kit. `query_expr`, `search`, `rrf`,
  `run_rollup`, `derive_supersession_order` and `run_fusion` (`query.py#query_expr` through
  `query.py#run_fusion`, as TOOL-dTotalRecall-21 S4 leaves them, `search` and `run_fusion` taking that
  connection) move into `record_find.py`, unchanged in ranking; `load_served_set`, `write_recall_rows`
  and the recall digest stay with recall's extraction in `query.py`, and `render_supersession_tag` stays
  with the two renderers it serves.
  `query.py` keeps its CLI as a thin adapter that imports the moved names, so a `query.<name>` caller
  (`tools/memory-recall/selftest.py`'s) still resolves. At most 40 rows, one per record, `key · kind ·
  build · bytes · path:line`, no content, superseded rows hidden; past 40, the last line reads `<total>
  rows match; narrow with --kind, --build or --paths`. Observed by AC4 and AC5.
- **S4** — The `check-recall` leg taken over: `tools/memory-recall/check-recall.py` grades `record find`'s
  ranking through `record_find.query_expr` and `record_find.run_fusion`, its floor unchanged, and
  `tools/memory-recall/test_recall_floor.py`'s arms run through the same. The guards of the `recall floor`
  and `recall floor arms` legs each gain `{prefix}/memory-tree/record_find.py` in the leg's one
  declaration, its `[[exempt_leg]]` row in `tools/govkit/registry.toml` (TOOL-dWitnessedBar-11 S1), so an
  edit to the finder runs the floor and its arms; `python tools/run-gates/leg_factory.py --write` then
  renders `tools/gate-legs.json`, since a guard edited in the manifest alone reds `--check` (its S2).
  Each leg keeps its name and every other field of its row. Observed by AC6.
- **S5** — `record show` in `record_find.py`, `read_section(root, address)`, run as `python gov_record.py
  show <id>[#<tag>][@<blob>]`: the section's text sliced from its blob at the row's `line` to `end_line`,
  or the whole record with no `#<tag>`. `@<blob>` reads that blob's rows where the index holds them; a
  blob no live tree or worktree holds has lost its rows (`tag_index.py#remove_unheld_rows`), so its bytes
  are read from git and sectioned by `extract_section`. An unknown key, tag or blob exits 2 naming it.
  The `id#tag` form is armed through the same reader in both its resolvers: `edge_grammar.py#resolve_edge`'s
  `id#tag` branch, which answers `unarmed` at HEAD, and `gov_tag.py show`, whose
  `tag_index.py#resolve_address` reads tags alone; the playbook README's sentence calling the form
  `unarmed` (`tools/playbook/README.md@ed5a7d523:418`) is rewritten. No tracked header edge line takes the
  `id#tag` form at HEAD (DERIVED by a grep), so arming it reds none. Observed by AC7.
- **S6** — The item budget, `check_read_set(root, role, keys)` in `record_find.py`, run as `gov_record.py
  budget --role <role> <key>…`: the bytes of each key's `record show` slice, summed against the role's
  `memory.item-budget` read through `tree_lib.py#read_policy_value` (`measured` reads 96,000 bytes for
  every role until a role has 30 sliced work orders measured; `96` or `128` reads that many KB for every
  role; a per-role value reads that role's), a KB being 1,000 bytes. Over it, `memory.over-budget`
  answers: `refuse` exits 2 naming role, bytes and cap; `report`, the default, prints `memory over
  budget: <role> <bytes> B > <cap> B` and exits 0; `off` prints nothing. Observed by AC8.
- **S7** — Superseded slices: a key whose record the supersession map names superseded (S3's
  `derive_supersession_order` over the map `id_grammar.py#derive_supersession_map` builds from the served
  pairs' `fts_supersession` edges, TOOL-dTotalRecall-21 S4) is, under
  `memory.superseded-slices`, refused (`refuse`, the default: exit 2 naming the key and its successor)
  or marked (`mark`: the key passes, followed by `superseded-by <id>`). Observed by AC9.
- **S8** — The work order: `handoff.py#render_handoff` and its `render` verb take `--read <key>`,
  repeated; before writing it runs `gov_record.py budget` as a subprocess, the memory-tree kit found
  through `resolve_kit_dir`, as `roles_lib.py#check_load_set` runs the load-set check, and writes a
  `reads:` list, one key per line with its bytes and any mark. A refusal refuses the render. The memory
  slices are outside PLAY-dOrderedCharter-11's load-set budget and its route-back, and one `[[cap]]` row
  in `tools/policy/caps.toml`, `name = "memory-slices"`, `class = "exempt"`, a `family` row whose home is
  `policy:memory.item-budget` and whose enforcer is the finder, keeps them out of `budgets.enforce`'s
  refusal (I16). It is the census's first `exempt` row, so the file header's "No `exempt` row exists
  today" goes, and `check_policy.py#CAP_CASES` gains its case, `derive_outside_probe_plant` as the other
  outside rows take; its enforcer makes no request naming it (`check_policy.py#arm_cap_census`). Observed
  by AC8 and AC10.
- **S9** — The default load's memory share: `render_card` renders the card's other cells first, and
  `derive_memory_line` passes their byte count to `memory_index.py measure --card-bytes <n>`; the `memory
  —` cell (`memory_index.py#render_memory_line`) reports the card and the auto-memory index's remainder,
  each against `memory.load-budget` and each its own budget, not a share of it, at session start.
  Observed by AC11.
- **S10** — The four keys' catalogue rows gain `summary` and a `usage` line each row admits
  (`memory.item-budget = 128`, an integer, since that row's `allowed` holds `96` and `128` as integers and
  `policy.py#check_value` refuses the string; `memory.over-budget = "refuse"`,
  `memory.superseded-slices = "mark"`, `memory.load-budget = "16k"`), and their names leave
  `tools/policy/unsummarised-keys.txt` through `policy.py lists --write`; the mirror lands in a second
  commit. Observed by AC12.
- **S11** — The user pages: `help/tags.md`'s namespace table gains the five rows, its count of registered
  namespaces moves with them, and its line saying `record` joins with dTotalRecall says it joined, with
  `gov_tag.py show <id>#<tag>`; `help/size-caps.md`'s list of caps outside the switch gains the exempt
  memory slices. NOT OBSERVED by a criterion: prose, which the docs leg and the closing review read.

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
- The memory-tree kit's `requires_if` declaration of its reach into the playbook-render kit's index:
  TOOL-dTotalRecall-43 S10, the round-1 audit's id 11.
- The `sections` column's parity arm against `SPEC_TITLE_NUMBERS`: TOOL-dTotalRecall-43 S25, id 31.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record-kinds.toml`, whose rows this unit gives the `sections`
  column and whose `tag` cells define the `record` namespace's members
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py`, the door CLI that gains the `find`, `show`
  and `budget` verbs
- **consumes-from** `TOOL-dTotalRecall-10` — `derive_anchor`, which derives a legacy heading's section
  tag
- **consumes-from** `TOOL-dTotalRecall-19` — `memory.legacy-anchors` through `read_legacy_anchors`, and
  the `record-key` native class `record show` resolves an `<id>` through
- **consumes-from** `TOOL-dTotalRecall-21` — `build_fts_rows`, `load_served_set`, `search` and
  `run_fusion` over a connection, and the `fts_record`, `fts_chunk` and `fts_supersession` tables
  `record find` searches
- **consumes-from** `TOOL-dTotalRecall-42` — `derive_record_kind`, which gives the `record` extractor
  each record's kind; without it overlapping homes give every review one kind
- **hands-off** `TOOL-dTotalRecall-23` — `record find` and the `record` and `section` rows, which the
  memory legs read for an unchanged blob
- **hands-off** `TOOL-dTotalRecall-12` — `record find` and `record show`, two of the shell commands the
  re-measure counts
- **hands-off** `TOOL-dTotalRecall-43` — `record_extract.py`, the `sections` column and `record_find.py`, which that unit changes for the round-1 audit's ids 7, 11, 12, 31, 34, 45 and 62
- **hands-off** `TOOL-dTotalRecall-14` — the `record`, `feature` and `marker` namespace rows, which that unit gives a `map` field, and the `record.<kind>` rows its map reads a record kind's purpose for
- **hands-off** `TOOL-dTotalRecall-15` — the `class` and `record` namespaces, which its disk census joins

## 4. Design

### The rows

Every extractor returns rows `(tag, kind, line, end_line, text)`, which `tag_index.py#_write_parsed`
writes to `blob_row` beside the blob and the extractor's version (PLAY-dOrderedCharter-19 S4). For one
kind and one of its record files:

| extractor | tag | kind | line, end_line | text |
|---|---|---|---|---|
| `record`, the registry row | `record.shape-run` | `tag` | the row's line, the same | the kind's name |
| `record`, a record | `record.shape-run` | `record` | 1, last | its key |
| `section` | `section.findings-2` | `section` | the heading's line, the line before the next heading of its level or above | the heading |

A key resolves to its rows through the served view: `tag_index.py#load_view` fills `view_path` from the
HEAD tree's `tree_path` rows with this worktree's `dirty_path` rows over them, and `VIEW_JOIN` serves only
those paths' rows, so a dirty row wins for its worktree. The key is the `text` of a `record` row, its path
the served path holding that blob. `record show <key>#<tag>` slices the blob's bytes between the two
lines; with `@<blob>` it reads that blob whatever the tree.

### The section table

```toml
[[record-kind]]
name = "spec"
sections = [
  { tag = "section.goal", required = true, heading = "Goal" },
  { tag = "section.scope", required = true, heading = "Scope (IN)" },
  # … one row per key of SPEC_TITLE_NUMBERS, through
  { tag = "section.reuse-audit", required = false, heading = "Reuse audit" },
]
```

A heading's title is matched with its leading `<n>. ` stripped. A legacy heading the table maps takes
the table's tag; an unmapped untagged heading takes its derived anchor under `derived`, nothing under
`none`, and an authored tag only under `retag`. An authored tag is unique in its record; a derived one is
not graded (TOOL-dTotalRecall-10).

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

Minted: `tools/playbook/record_extract.py` (`extract_record`, `extract_section`, `extract_feature`,
`extract_class`, `extract_marker`); `tools/memory-tree/record_find.py` (`scan_records`, `read_section`,
`check_read_set` and the moved fusion functions); `read_sections` and `check_sections` in
`tools/memory-tree/record_kinds.py`; the verbs `find`, `show` and `budget`; five namespace rows; the
`sections` column; the `memory-slices` cap row and its case; `handoff.py render --read`; the fixture
plants of §7. Naming cells: each new function leads with a verb of `.lexicon.conf`'s VERBS table
(`extract`, `scan`, `read`, `check`), asked of the lexicon's `--suggest` under `--as py.function` at the
pass. The moved `query_expr`, `search` and `rrf` lead with no declared verb; they leave `query.py` as they
arrive in `record_find.py`, so the two-sided `VERB_OFFENDER_PIN` in `.lexicon.conf` holds unmoved.

### Migration

The five extractors join `tag_index.py#derive_extractor_versions`' map, so the versions digest moves and
the index builds the new rows once on its next build; no record is rewritten. `query.py`'s CLI keeps its
arguments and output, so a caller of it sees no change.

### Files touched (estimate)

- `tools/playbook/record_extract.py` (new)
- `tools/playbook/namespaces.toml`
- `tools/playbook/edge_grammar.py` (the `id#tag` branch of `resolve_edge`)
- `tools/playbook/gov_tag.py` (`show` of an `id#tag` address, and the fixture plants)
- `tools/playbook/adopt-playbook.sh` (the plant rows of its tag-resolver block)
- `tools/playbook/memory_index.py`
- `tools/playbook/README.md`
- `tools/memory-tree/record_find.py` (new)
- `tools/memory-tree/gov_record.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/record_kinds.py` (`read_sections`, `check_sections`)
- `tools/memory-tree/gen_build_index.py` (`cmd_new_spec` calls `check_sections`)
- `tools/memory-tree/check-memory-hygiene.test.sh` (the finder's and the door's arms)
- `tools/memory-tree/README.md`
- `tools/memory-recall/query.py`
- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/test_recall_floor.py`
- `tools/roles/handoff.py`
- `skills/session-kickoff/manifest-check.sh`
- `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp: its `watch:` line names
  `skills/session-kickoff/manifest-check.sh` and `tools/gate-legs.json`)
- `tools/policy/caps.toml`
- `tools/policy/check_policy.py` (`CAP_CASES`)
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `tools/govkit/registry.toml` (the two recall legs' guards)
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`)
- `help/tags.md`
- `help/size-caps.md`

### Alternatives rejected

- **`record find` returning content.** The read budget exists because whole-file reads are the cost; a
  finder that returns content is a second read channel nothing budgets.
- **A cutoff on `record find`'s population for the archive.** FK-11-1 reads rotated records beside live
  ones; the corpus walk already admits `archive/` (`tools/memory-recall/extract.py@ed5a7d523:29`).
- **The item budget inside `budgets.enforce`.** MS-3 keeps memory slices out of that switch, and
  `memory.over-budget` is the one answer.
- **Record rows alone defining the `record` namespace.** A pocket kind holds no record file, so its
  `record.<kind>` citation in the two HYGIENE files would read unresolved once the namespace is armed
  (`tag_index.py#check_resolves`); the registry rows define every kind (S1).

## 5. Production-readiness checklist

- security — read-only over tracked records and the index; the handoff's new argument is a key list,
  each key resolved before any write, and a refused key refuses the render.
- perf / scale — `record find` reads rows, not files; `record show` reads one blob slice. The extractors
  read each blob once (`tag_index.py#_write_parsed` skips one `blob_parsed` holds); the pass times a cold
  `gov_tag.py --rebuild` against the `tags (the resolver's checks)` leg's `ceiling`.
- error / empty / loading states — an empty namespace prints `unarmed`; an unknown key exits 2 naming it;
  a refused policy read exits 2 naming the key; an unresolved playbook-render kit exits 2 naming it.
- observability — the total line, the report line and the card cell each name the figures.
- risks — the 40-row cap hides matches past it; the total line names them and the filters narrow.
  Arming four namespaces grades each citation of them outside `memory/builds/`: at HEAD the `record.<kind>`
  citations of the two HYGIENE files, which the registry rows define, and under the shipped
  `tags.bare-refs = charter-only` the new tails raise no bare reference (`tag_index.py#check_resolves`).
- testing — AC1 to AC12 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — `tools/memory-tree/README.md` gains the three verbs; `help/tags.md` and `help/size-caps.md`
  as S11 says.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe run from `tools/playbook/` loads the view at the pass tip
  (`tag_index.load_view`) and prints `tag_index.derive_namespace_state`, `record`, `section`, `class` and
  `marker` read above 0, `class` at the count `git grep -l "^kind: class" -- 'memory/gotchas/*.md' | wc -l`
  prints, `record` at the `[[record-kind]]` row count of `record-kinds.toml`, and `feature` at 0, which
  `gov_tag.py#run_check` prints as `tags: unarmed feature`; and `python gov_tag.py show record.witness`
  prints that kind's registry row.
  Red when: an empty `feature` namespace prints green, a namespace row is registered with no
  extractor, or a pocket kind's `record.<kind>` names no row.
  figure: DERIVED at observation; 174 class records and 49 kind rows at `ed5a7d523`.
- **AC2** — When `python gov_record.py show <stem>#section.findings-2` runs over a fixture build record
  whose untagged `## Findings` repeats, the second section is returned, and the record's `record.<kind>`
  row names the stem as its key.
  Red when: the section extractor folds headings itself instead of calling `derive_anchor`.
- **AC3** — When `gov_record.py new spec <id> --tier 2` runs in a fixture whose `TEMPLATE-SPEC.md`
  skeleton lacks `## 6. Acceptance criteria`, it exits 2 naming `section.acceptance-criteria` and writes
  no file; `--tier 1` over the shipped template writes its spec; a legacy spec's `## 1. Goal` resolves as
  `section.goal`.
  Red when: the section table is read for legacy headings but not for new records, or a Tier-1 spec is
  refused for a section its tier omits.
- **AC4** — When `python gov_record.py find --build dClosedLoop` runs, it prints 40 rows and a 41st line
  naming the total and `--kind`; with `--kind deviation --build dTotalRecall` every row it prints names
  the kind `deviation`, and its total line names that build's count of deviation records.
  Red when: the cap truncates silently, so 40 rows print and nothing names the rest.
  figure: DERIVED at observation by `git ls-files`; at `ed5a7d523` dClosedLoop held 594 record files and
  dTotalRecall 138 deviation records.
- **AC5** — When `gov_record.py find` runs with a question whose only answer is a decision row held in a
  dated file under `memory/archive/`, it returns that row's key; with a decision another names superseded,
  only the successor's row prints.
  Red when: the archive is outside the record extractor's source, or a superseded row is returned.
- **AC6** — When `python check-recall.py --data-dir <a scratch index>` runs from `tools/memory-recall/`, its
  graded rows equal those the pass's base computes, and `git grep -n "def run_fusion" -- tools` prints one
  line, in `record_find.py`; and `python leg_factory.py --check` run from `tools/run-gates/` exits 0 while
  the `recall floor` and `recall floor arms` rows of `tools/gate-legs.json` list
  "{prefix}/memory-tree/record_find.py" in their guards.
  Red when: the leg grades a copy of the fusion that `record find` does not run, or a guard is edited
  in the manifest alone, so `--check` exits 1 naming its leg.
- **AC7** — When `gov_record.py show <key>#section.nope` runs, it exits 2 naming `section.nope`; `show
  <key>@<an older blob of it>` returns that blob's text, a blob no live tree holds included; `gov_tag.py
  show <key>#<tag>` prints the same section as `record show`, and a `python -c` probe of
  `edge_grammar.resolve_edge` over `<key>#<tag>` returns `resolved`.
  Red when: `id#tag` still answers `unarmed` in `edge_grammar.py#resolve_edge`.
- **AC8** — When `python handoff.py render --role gov-builder --build <slug> --read <key>` runs in a fixture
  whose key's slice is 130,000 bytes, it renders and prints `memory over budget: gov-builder 130000 B >
  96000 B` under the default; with `memory.over-budget = "refuse"` committed, it exits 2 and writes no file;
  under `off` it prints no report line.
  Red when: the report line is missing its role or bytes, or `refuse` renders the file.
- **AC9** — When the fixture's decision `DEC-tFix-1` is superseded by `DEC-tFix-2` and `handoff.py render
  --role gov-builder --build <slug> --read DEC-tFix-1` runs, it exits 2 naming `DEC-tFix-2`; with
  `memory.superseded-slices = "mark"` it renders and the `reads:` line carries `superseded-by DEC-tFix-2`.
  Red when: a superseded decision is handed to a builder unmarked.
- **AC10** — When `budgets.enforce = "refuse"` is committed in the AC8 fixture, the over-cap render still
  succeeds under `report`, and `python budgets.py resolve memory-slices` run from `tools/policy/` prints
  that `memory-slices` is `exempt`, outside the switch.
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

`recall floor` · `recall floor arms` · `memory-recall kit selftest` · `build-index selftest` · `memory hygiene` · `playbook render selftest` · `govkit acceptance matrix` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `routed-commits selftest` · `govkit selftest` · `govkit refusal join` · `policy fixtures` · `tier2-review self-test`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 AC4 AC5 AC7 AC8 AC9 · the plants of `record_find.py --fixture --plant <case>`, a planted 41-row build, an archived decision, a superseded decision handed to a builder, an over-cap read set under each `memory.over-budget` value and a blob no tree holds, and the door's missing-section refusal beside TOOL-dTotalRecall-2's arms, run by the `memory-hygiene self-test` leg, staged by the cap line cut, by `memory.superseded-slices` read and ignored and by `check_sections` skipped · none
New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 · rows of its tag-resolver block over `gov_tag.py --fixture --plant <case>`, a fixture build record with a repeated untagged H2, a legacy spec heading, a pocket kind's citation and an empty `feature` namespace, run by the `playbook render selftest` leg, staged by `extract_section` folding headings without `derive_anchor` · none
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
  first") and the brief's rule that a spec calls each parent surface as its spec names it. Discharged
  for the landed parents in rev-5. widens: none · relaxes: none
- **F7 — Where do the extractors and the finder live, the index having landed in the playbook-render
  kit?** `tag_index.py#resolve_extractor_module` loads `<module>.py` only beside the registry or from its
  own kit, both `tools/playbook/`, and the memory-tree kit declares `requires = []`
  (`tools/memory-tree/kit.toml`). Options: (a) `record_extract.py` in `tools/playbook/`, importing
  memory-tree's modules as every extractor may through `tag_index.py#load_memory_tree`, and
  `record_find.py` in memory-tree beside its door, reaching `tag_index.py` through the inline
  `resolve_kit_dir` block at call time, as `record_kinds.py` reaches the roles and loop kits, and
  memory-recall's `load_served_set` the same way for a question; (b) both in
  memory-tree, `resolve_extractor_module` widened to read memory-tree's directory; (c) both in the
  playbook-render kit, the door and `query.py` reaching the finder there. (b) adds a second module rule
  to the index TOOL-dTotalRecall-8 F6 ruled on; (c) moves the `recall floor` guard path and puts the
  memory finder outside the memory kit. RESOLVED (agent, 2026-11-22, delegated): (a), M3, every
  criterion met with no change to the index's rules; tie-break reuse of `resolve_extractor_module` and
  TOOL-dTotalRecall-8 F6's placement, per `2026-11-22-prompt-TOOL-dTotalRecall-9-reground-brief`.
  widens: none · relaxes: none
- **F8 — Which kind does the `record` extractor give a record, when homes overlap at HEAD?**
  `spec-audit` and `diff-review` share `memory/builds/*/reviews/*.md`, and `research`'s
  `memory/builds/*/build/*.md` admits every typed kind's records (`tools/memory-tree/record-kinds.toml`).
  Options: (a) `derive_record_kind(path, text, rows)`, TOOL-dTotalRecall-42 S5 at order 15, the Serves
  kind deciding and the home admitting; (b) one row by file order, TOOL-dTotalRecall-43 S13 re-pointing it
  later. (b) gives every review one kind and every typed record `research`, so AC4's `--kind deviation`
  arm reads a wrong set. RESOLVED (agent, 2026-11-22, delegated): (a), M3 veto 1 on AC4 for (b), per
  `2026-11-22-prompt-TOOL-dTotalRecall-9-reground-brief`; it meets TOOL-dTotalRecall-43 S13's item at this
  unit. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 9, the brief's I8, I11, I12, I15 and I16, scout
  B's row for cl-0220, systems `[design-memory-structure]` and `[design-tags]`, and `query.py`,
  `extract.py` and `handoff.py` read at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-26 · §2 preconditions, S4 · §4 Files touched · §6 AC6 · re-grounded on dWitnessedBar at
  `443775a2f`, by the cross-check record `2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck`, row
  27: the `recall floor` guard is edited in its `[[exempt_leg]]` declaration and the manifest
  regenerated by `leg_factory.py --write`, which AC6 observes through `--check`.
- rev-4 · 2026-11-22 · §2 preconditions · §3 Edges · AC6 · §7 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-16-unit8-edges-brief`: the `consumes-from TOOL-dTotalRecall-8`
  bullet is deleted, since that unit mints no `policy_value.py`, and §2's preconditions name the landed
  `tree_lib.py#read_policy_value` as the policy read; AC6's guard string is quoted, not backticked, so
  the path join stops reading a `{prefix}` spelling as an untracked path, its observation unchanged;
  the leg line gains the four legs whose guards `tools/policy/caps.toml`,
  `tools/govkit/registry.toml` and `tools/memory-tree/query.py` trip.
- rev-5 · 2026-11-22 · §2 preconditions · S1 to S10 · S11 added · §3 · §4 · §5 · AC1 · AC3 · AC4 ·
  AC6 · AC7 · AC9 · AC10 · §7 · §8 F6 · F7 and F8 added · §10 · re-grounded at `ed5a7d523` per
  `2026-11-22-prompt-TOOL-dTotalRecall-9-reground-brief`: `record_extract.py` moves beside the registry
  and the finder reaches the index and unit 21's `load_served_set` at call time, its moved `search` and
  `run_fusion` taking a connection as unit 21's rev-3 leaves them (F7); registry rows define
  `record.<kind>`, record rows take the kind `record`, and `derive_record_kind` gives a record's kind
  (F8, unit 42's hands-off mirror beside); `sections` maps unnumbered titles; the door refuses in
  `cmd_new_spec`; `id#tag` arms `resolve_edge`; the usage is the integer `128`; the cap row brings its
  case; both recall legs guard the finder; the arms move to suites legs run; the help pages and the
  kickoff manifest join Files touched; the leg line gains `tier2-review self-test`.
- rev-6 · 2026-11-23 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dTotalRecall-14's
  consumes-from edge, per `2026-11-22-prompt-TOOL-dTotalRecall-14-reground-brief`; nothing else moved.
- rev-7 · 2026-11-23 · §3 · a hands-off bullet mirrors TOOL-dTotalRecall-15's edge, per
  `2026-11-22-prompt-TOOL-dTotalRecall-15-reground-brief`.

## 10. Reuse audit

The seams extended are memory-recall's fusion (`query.py#query_expr` through `query.py#run_fusion`),
moved into `record_find.py` rather than copied; its record anchors (`id_grammar.py#extract_records` and
`#anchor_at`, moved there by PLAY-dOrderedCharter-18) for the `record` extractor; unit 42's
`derive_record_kind` (TOOL-dTotalRecall-42 S5) for a record's kind; `gotchas.py#parse_front_matter` for a
class record's front matter; its supersession readers (`id_grammar.py#extract_supersessions`,
`#derive_supersession_map` and `query.py#derive_supersession_order`) for S7; `handoff.py#render_handoff` as the work order and
`roles_lib.py#check_load_set`'s subprocess reach for its budget call; `check_policy.py#CAP_CASES`'
`derive_outside_probe_plant` for the cap row; and PLAY-dOrderedCharter-19's namespace rows, extractor
contract and `tag_index.py#build_index` for the extractors. No existing seam fits the 40-row cap with a
total line (the only cap is `query.py#RESULT_CAP`, five entries per record), the per-kind section
table, or the item budget. The lookup,
`python tools/codebase-map/reuse_lookup.py "find records by kind tag or build and show one section"`,
ranked generic `build` and `records` stems, `extract_records`, `read_records` and `render_record`; none
filters records by kind or slices a section. Disagreements with source: scout B says no work-order renderer
exists at HEAD, and `render_handoff` renders the role handoff this unit treats as the work order; scout B's
archive citation `extract.py:28-30` is the module docstring (`tools/memory-recall/extract.py@ed5a7d523:29`).
The recall probe returned scout B's row, the packet clause and the brief's row; none disagreed otherwise.

Recall terms used: `python tools/memory-recall/query.py "how does record find and record show read sections from the index under a read budget" --terms "record find record show section extractor item-budget over-budget superseded-slices load-budget work order slice archive"`
