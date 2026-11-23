# TOOL-dBoundRoles-81 — the compose verb reads gov's role files and workflow entries as rows, through a reader the namespace row declares

**Status:** INPROGRESS · rev-1 · 2026-11-23 · node d · Tier-2 · base 318e20c9 · streams tooling · order 23 · closes TOOL-dBoundRoles-77

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |
| [2026-11-22-prompt-TOOL-dBoundRoles-81-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-81-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-81-1-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-81-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-81-spec-brief.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-81-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The playbook kit's `compose` verb reads gov's rows of a kind only as `[[<kind>]]` TOML tables keyed
`tag`, read from the one blob its namespace row's `source` names. Gov's roles are front-matter files
under a glob, and gov's workflows are `[[workflow]]` entries keyed `name`, so neither kind has gov rows
to compose beside an overlay's. `TOOL-dBoundRoles-20` S3 (`compose_roles`, `compose_workflows`, its §8
F8 (i)) waits on that. This unit lets a namespace row declare the reader that turns its source into
rows, reads a glob source blob by blob, and gives the roles kit, which owns both grammars, the verb
mode that prints them as rows tagged from their names.

## 2. Scope (IN)

- **S1** — The roles kit prints rows. `check_roles.py --print-rows role|workflow` reads one text on
  standard input and grades nothing, beside `--print-tag-rows` (`tools/roles/check_roles.py#print_tag_rows`).
  `role`: the text is one role file, parsed by `tools/roles/roles_lib.py#parse_front_matter`; it prints
  one JSON object, `tag` `role.<name>` and every front-matter key, each value folded by its
  `role-schema.toml` shape as §4 "The row form" states. `workflow`: the text is a `workflows.toml`;
  it prints one JSON object per `[[workflow]]` entry, `tag` `workflow.<name>` and every key of the
  entry as TOML reads it, its `stages` rows included. A text that does not parse, and an entry typing
  `tag`, print the defect on stderr and exit 2. Observed by AC1 and AC2.
- **S2** — The declared reader. A `[[namespace]]` row of `tools/playbook/namespaces.toml` may carry
  `rows`, a `<module>:<function>` spelled and resolved as its `extractor` is
  (`tools/playbook/tag_index.py#resolve_extractor_module`). `read_kind_source`
  (`tools/playbook/overlay_rows.py#read_kind_source`) calls that function once per source blob at HEAD,
  as `(ns, path, text)`, and takes the rows it returns; a row with no `rows` key reads as today. Each
  row carries `origin` the kind and `source` the blob's tree path. Observed by AC1 and AC3.
- **S3** — A glob source. A `source` carrying `*` or `?` names every path HEAD holds that the glob
  matches, one segment deep under its directory, as `extract_role` matches a role file
  (`tools/playbook/tag_index.py#extract_role`); each matched blob is read at HEAD. A glob matching no
  path answers as an absent blob does today: the kind is unarmed, exit 2, naming the source. Observed
  by AC1 and AC4.
- **S4** — The one reader of both kinds. `read_roles_rows(ns, path, text)` in
  `tools/playbook/tag_index.py`, beside `read_roles_tag_rows`, runs `check_roles.py --print-rows <ns>`
  through `resolve_roles_verb` (`tools/playbook/tag_index.py#resolve_roles_verb`) by subprocess, never
  an import, and returns its rows. A verb exit 2 refuses the composition, exit 1, naming the blob's path
  and the verb's stderr line; a roles kit that does not resolve leaves the kind unarmed, exit 2, naming
  the reader. Observed by AC4.
- **S5** — The `role` namespace row of `tools/playbook/namespaces.toml` gains
  `rows = "tag_index:read_roles_rows"`, and the file's header comment names the optional key. The
  `workflow` row is `TOOL-dBoundRoles-20` S1's and carries the same key (§3 Edges). Observed by AC5.

## 3. Non-goals (OUT)

- The `workflow` namespace row, the `schema` key on `kind.role` and `kind.workflow`, and both row
  schema files: `TOOL-dBoundRoles-20` S1 and S2's. Until they land, `compose --kind role` in gov's own
  tree still answers `unarmed` for want of a schema (`tools/playbook/kinds.toml@2dd6325c:74-82`); this
  unit's criteria observe the reader in a fixture tree that registers both.
- Grading the rows. The verb prints a row and validates nothing, as `print_tag_rows` does; the roles
  catalogue's R2 and R6 grade a role file and an entry.
- `compose_roles`, `compose_workflows` and every reader re-pointed to the composition:
  `TOOL-dBoundRoles-20` S3.
- A second kit's front-matter or TOML-by-name source. A later kind declares its own `rows` reader.

`TOOL-dBoundRoles-20` consumes this unit through
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`, which binds the relation over
that spec: S1's `workflow` namespace row carries `rows = "tag_index:read_roles_rows"`, S3's composers wrap the role and
workflow rows `compose --kind role|workflow` then prints, and S2's `schema` registration arms them in gov's tree.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `4b7916726`, whose `tools/` tree equals base `318e20c9`'s (`git diff --stat 318e20c9 HEAD
-- tools/` prints nothing):

- `read_kind_source` takes the namespace row's `source`, reads ONE blob at HEAD through
  `tree_lib.read_blobs_at`, and returns `tomllib.loads(text).get(kind, [])`; HEAD holding no blob at
  the source returns None, which `run_compose` prints as `unarmed`.
- The `role` namespace row names `source = "{prefix}/roles/agents/*.agent.md"`
  (`tools/playbook/namespaces.toml@e78d0b57:198`), so the blob read finds no blob and the kind is
  unarmed whatever its schema.
- `derive_row_composition` keys gov's rows as `{r["tag"]: r}`
  (`tools/playbook/overlay_rows.py#derive_row_composition`), so a `[[workflow]]` entry, which carries
  `name` and no `tag` (`tools/roles/workflows.toml@15d75ad5:8`), raises `KeyError`.
- The gap, probed: `python tools/playbook/overlay_rows.py compose --kind role` prints
  `overlay-rows: unarmed · kind role · tools/playbook/kinds.toml lists no such kind with a schema` and
  exits 2, the same for `workflow`, since neither kind row carries `schema` at HEAD; with a schema
  registered, the glob reaches `read_blobs_at` as a path and answers unarmed.
- `tools/playbook/tag_index.py#read_roles_tag_rows` is the precedent: the role grammar is the roles
  kit's `parse_front_matter`, reached by `check_roles.py --print-tag-rows` through `resolve_roles_verb`
  by subprocess, since a kit imports no sibling kit (TOOL-dBoundRoles-14 §8 F5).
- `REGISTRY_FIELDS` (`tools/playbook/tag_index.py#read_namespaces`) lists the keys a namespace row
  must carry and refuses none beside them, so an optional `rows` key needs no reader change there.

### The row form

`--print-rows role` folds each front-matter value by the shape `tools/roles/role-schema.toml` declares
for its key, read through `tools/roles/roles_lib.py#load_role_schema`:

| `role-schema.toml` shape | printed as | example key |
|---|---|---|
| `list` | a list of its comma-separated entries, stripped, empty ones dropped | `tools`, `reads`, `rules`, `shapes`, `gates` |
| `entries` | a list of its `;`-separated entries, stripped, as `parse_never_entries` splits them | `never` |
| `class` | a list holding its one class (§8 F2) | `writes` |
| `slot`, `text`, `bool`, `template` | the raw string | `name`, `budget`, `agent`, `return` |

An entry keeps its spelling: a `gates` entry `lexicon naming predicates?` keeps its optional `?`, which
`TOOL-dBoundRoles-83`'s leg fold strips. `budget` stays the decimal string the file holds, which
`TOOL-dBoundRoles-82`'s rising direction reads as a number.

```
$ python check_roles.py --print-rows role < agents/gov-builder.agent.md
{"tag": "role.gov-builder", "name": "gov-builder", "tools": ["Read", "Grep", ...], "writes": ["product"],
 "budget": "8212", "gates": ["lexicon naming predicates?"], ...}
```

### The source read

```
read_kind_source(root, kind):
  row = the namespace row whose ns is kind
  paths = [source]                      if source holds no * or ?
        = HEAD paths matching the glob  otherwise (git ls-tree -r --name-only HEAD -- <dir>, one segment)
  texts = read_blobs_at(root, [("HEAD", p) for p in paths])
  None (unarmed)                        if no path, or any text is None
  rows = reader(kind, p, text) per p    if row names `rows`, else tomllib.loads(text).get(kind, [])
  each row + {origin: kind, source: p}
```

The reader is loaded as `load_extractors` loads an extractor (`tools/playbook/tag_index.py#load_extractors`),
`tag_index` resolving to this module itself.

### Inventory

Minted: the `--print-rows role|workflow` mode of `check_roles.py`; `read_roles_rows` in
`tools/playbook/tag_index.py`; the optional `rows` key of a `[[namespace]]` row; the fixture plants
`front-matter-rows`, `front-matter-refused` and `front-matter-unarmed`. The function name is asked of
`python tools/lexicon/lexicon.py --suggest read_roles_rows --as py.function` at the pass.

### Migration

None: no stored data changes. A namespace row with no `rows` key, every row but `role` today, reads as
before, so `item`, `stage` and `scenario` compose byte-identically.

### Rollout

Live at landing and dark in gov's tree until `TOOL-dBoundRoles-20` S2 registers the two schemas.
Units 82, 83 and 84 hold the same order and each writes `tools/playbook/overlay_rows.py`, so the
declared write sets intersect and `--dispatch` refuses a
second pass while the first is open (M6 condition 1).

### Files touched (estimate)

- `tools/roles/check_roles.py` (the `--print-rows` mode and its usage line)
- `tools/playbook/tag_index.py` (`read_roles_rows`)
- `tools/playbook/overlay_rows.py` (`read_kind_source`, the module docstring)
- `tools/playbook/namespaces.toml` (the `role` row's `rows` key, the header comment)
- `tools/playbook/fixtures/row_kind.py` (the plants)
- `tools/playbook/render_playbook.py` (the selftest rows running the plants)
- `tools/playbook/README.md` (the reader, beside its `--print-tag-rows` sentence)

### Alternatives rejected

- **The playbook kit parses front matter itself.** A second spelling of `parse_front_matter`'s grammar
  and of the role schema's shapes; [one-fact].
- **An import of `roles_lib`.** A kit imports no sibling kit (TOOL-dBoundRoles-14 §8 F5).
- **Reading the form off the source's spelling** (a glob read as front matter, a row with no `tag`
  tagged from `name`). It types a closed table of source forms in code, and the next kind with another
  form edits the composer.

## 5. Production-readiness checklist

- security — no new write path: the verb reads standard input and prints; the reader runs a kit verb
  `resolve_kit_dir` finds, as the tag index already does.
- perf / scale — one subprocess per role file and one for `workflows.toml`, per composition, over a few
  dozen files.
- error / empty / loading states — a glob matching nothing is unarmed; a file the grammar refuses
  refuses the composition naming the file; an absent roles kit is unarmed naming the reader.
- observability — every refusal names the blob's path and the verb's line.
- risks — a role file R2 would refuse with a key the schema lacks still prints, raw; the catalogue
  leg reds it, not the composition.
- testing — AC1 to AC5 by the fixture plants and probes of §6; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no adopter-visible behaviour moves until `TOOL-dBoundRoles-20` S10
  writes `help/roles.md`; `tools/playbook/README.md` names the reader.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/fixtures/row_kind.py --plant front-matter-rows` runs, its
  scratch tree registering `kind.role` and `kind.workflow` with fixture schemas, holding two role files
  and a `workflows.toml` of two entries, and an overlay row `role.adopter.triager`, it prints one
  `row role.<name>` line per role file, `role.adopter.triager` with `origin` `repository`, and one
  `row workflow.<name>` line per entry, each gov row with `origin` its kind and `source` its file.
  Red when: the composer reads the glob as one blob, or keys a workflow entry by a typed `tag`.
  fixture: the plant's scratch repository under `%TEMP%`, built by `build_tree`'s steps.
- **AC2** — When `python tools/roles/check_roles.py --print-rows role < tools/roles/agents/gov-builder.agent.md`
  runs, it prints one JSON object whose `tag` is `role.gov-builder`, whose `tools` and `gates` are lists
  and whose `writes` is `["product"]`; `--print-rows workflow < tools/roles/workflows.toml` prints one
  object per `[[workflow]]` entry, each `tag` `workflow.<name>`.
  Red when: a list-shaped key prints as its raw string, or an entry prints with no derived tag.
- **AC3** — When `python tools/playbook/overlay_rows.py compose --kind item` runs in gov's tree, its
  `pins` equal the pins it printed before the unit; `item` names no `rows` key.
  Red when: a namespace row without `rows` is read through a reader.
  figure: DERIVED, the before-pins printed by the same command at the pass's parent commit.
- **AC4** — When the plant `front-matter-refused` indents a key of one fixture role file, the
  composition exits 1 naming that file and `R2`; when `front-matter-unarmed` commits no role file, it
  exits 2 naming `unarmed` and the glob.
  Red when: a malformed gov role file drops out of the composition silently, or an empty glob composes
  zero rows as green.
- **AC5** — When `grep -n 'rows = "tag_index:read_roles_rows"' tools/playbook/namespaces.toml` runs,
  it prints the `role` row's line.
  Red when: the `role` row names no reader, so gov's roles stay unread once a schema registers.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `roles catalogue` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC1 AC4 · the `front-matter-rows`, `front-matter-refused` and `front-matter-unarmed` plants of `tools/playbook/fixtures/row_kind.py`, staged by reading the glob as one blob · none

## 8. Open questions

- **F1 — Where does the composer learn a kind's row form?** Options: (a) an optional `rows` key on the
  namespace row naming a reader, the roles kit's verb behind it; (b) the form read off the source's
  spelling inside `overlay_rows.py`; (c) the playbook kit imports `roles_lib`. (c) breaks the
  no-sibling-import rule (veto 2, a governance carrier); (b) types a closed table of forms in code and
  spells the role grammar twice. RESOLVED (agent, 2026-11-23, delegated): (a), rung 3, the precedent
  `read_roles_tag_rows` set. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: the
  namespace row's optional keys, by `rows` · relaxes: none
- **F2 — What does a `class`-shaped key such as `writes` print as?** Options: (a) a list holding its one
  class; (b) the raw string. `TOOL-dBoundRoles-20` S5 declares `writes` a set widening on `add`, and
  `set_row_patch` (`tools/playbook/overlay_rows.py#set_row_patch`) unions over `list(value)`, which
  splits a bare string into characters; (b) fails that S5 at its first patch. RESOLVED (agent,
  2026-11-23, delegated): (a), rung 3. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-23 · initial draft, from the brief
  `2026-11-23-prompt-TOOL-dBoundRoles-81-spec-brief` and the owner's ruling
  `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling`, closing `TOOL-dBoundRoles-77`.

## 10. Reuse audit

The seams extended are `tools/playbook/overlay_rows.py#read_kind_source`, which gains the glob read and
the declared reader; the namespace registry's `extractor` resolution
(`tools/playbook/tag_index.py#resolve_extractor_module`, `#load_extractors`), which the `rows` key
reuses; and the roles kit's door for its grammar, `tools/roles/check_roles.py#print_tag_rows` with
`tools/playbook/tag_index.py#read_roles_tag_rows`, which the new mode and reader sit beside. The roles
kit's readers `tools/roles/roles_lib.py#load_roles` and `#load_workflows` read from a kit directory on
disk, never a blob at HEAD, so the verb parses its stdin with `parse_front_matter` and `tomllib` as
`print_tag_rows` does. `python tools/codebase-map/reuse_lookup.py "read gov's rows of a kind from
front-matter files under a glob for the overlay composition"` ranked `read_text`, `read_rows`,
`read_git` and `read_blobs_at`, generic readers, and no front-matter row reader, so no existing seam
fits beyond those named. The recall probe returned the ask `TOOL-dBoundRoles-77`, this unit's brief and
the owner's ruling; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does the compose verb read gov's role files and workflow entries as rows" --terms "compose read_kind_source namespace source glob front-matter role files workflows.toml derive tag name overlay rows"`
