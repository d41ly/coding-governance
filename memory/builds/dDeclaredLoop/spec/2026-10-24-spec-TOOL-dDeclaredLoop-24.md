# TOOL-dDeclaredLoop-24 — the `item` kind in the kinds register, its factory, and the checks over the composed items

**Status:** DEFERRED · rev-4 · 2026-11-14 · node d · Tier-2 · base ed497191 · streams tooling · order 11 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0109@48e119fc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-build-TOOL-dDeclaredLoop-24-deviation-241.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-24-deviation-241.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-24-deviation-242.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-24-deviation-242.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-24-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-24-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-24-reground-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-24-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

The flow's items become a registered kind with a factory, a row schema and a gate, so a repository
can add an item to a gov step or patch one of gov's from its overlay, and every check reads the
composition of gov's `[[item]]` rows with the repository's at the landed revision, never the overlay
text (FA-1, FA-2, FA-5). Today `kind.item` is registered with no population, factory, gate or
schema, excused by a pending row, so an adopter cannot add or change an item (`gap-flow-19`). The
mechanism is landed (§10). This unit registers the kind, declares its schema and fixed set, gives the
loop kit one way to read a kind's composition, and runs the definition's item checks and a
record-version join over it.

## 2. Scope (IN)

- **S1** — The kind row. The `kind.item` row of `tools/playbook/kinds.toml` takes
  `population = "{prefix}/loop/loop.toml"`, `factory = "python {prefix}/loop/loop_items.py new"`,
  `gate = "loop item kind"` and `schema = "{prefix}/loop/item-schema.toml"`, and its `summary` and
  `usage` are rewritten for the landed factory. Its `owner` and its `binds`, `principle.p16`, stay
  as they are (§8 F8). The `kind` row naming `kind.item` in `tools/playbook/core-pending.txt` is
  deleted, since `tools/playbook/core.py#run_kinds` reds a pending kind whose factory and gate hold.
  `help/reference/kinds.md` is re-rendered by `python tools/playbook/render_playbook.py --reference`.
  Observed by AC2.
  **Readers:** by name: `tools/playbook/kinds.toml`, which declares `kind.item` and keeps it, and
  `help/reference/kinds.md`, which renders its section · by value: `tools/playbook/core.py`, its
  kinds, meta-check and new verbs, which count the pending rows and refuse a pending kind's factory.
- **S2** — The schema, `tools/loop/item-schema.toml`, in the shape
  `tools/playbook/overlay_rows.py#read_kind_schema` reads: a `[kind]` table with `name = "item"` and
  `owner-seat = 2`, so a repository row is `item.<step>.adopter.<name>`; one `[[field]]` row for each
  key of a gov item but `tag`, each with its `shape`, its `ref` where it has one, and its class; and
  one `[[fixed-row]]` for each step's exit item and for the floor item `item.test.verdict`, whole.
  Every `fixed-by` source is a `principle=` tag (§4). Observed by AC5, AC7 and AC11.
- **S3** — The composition read. `tools/playbook/overlay_rows.py` gains
  `derive_kind_composition(root, kind, exclude, records)`, holding the per-kind body that
  `tools/playbook/render_playbook.py#read_kind_rows` runs today: the schema, gov's rows read at
  `HEAD` from the kind's namespace `source`, the overlay's rows, the tag-valued policy where an
  exclusion is set, and `derive_row_composition`. It answers None where the kind's schema file is
  absent from `root`, so a target without the loop kit composes no item row; `read_kind_rows` calls
  it per kind and passes over a None. A `compose --kind <kind>` verb on the same module prints one
  kind's composition as JSON, the verb TOOL-dDeclaredLoop-26 §8 F5 asked for (§8 F5). The `item`
  row of `tools/playbook/namespaces.toml` takes `source = "{prefix}/loop/loop.toml"`, the path form
  that read takes. Observed by AC9, AC12 and AC13.
  **Readers:** by name: `tools/playbook/render_playbook.py`, its kind-rows reader, which hands a
  namespace's `source` to `git show` · by value: `tools/playbook/render_playbook.py`, the same
  reader, and `tools/playbook/tag_index.py`, its namespace reader, which requires a non-empty
  `source` and joins nothing on it.
- **S4** — The item checks, `check_item_composition` in `tools/loop/loop_items.py`, over the
  composed rows: a copy of the definition holding the composition as its `[[item]]` table, run through
  `tools/loop/loop_lib.py#check_program` (every need declared, no needs cycle with each cycle named,
  outcome sets closed and routed, input layer tags, each step's exit an item of that step),
  `tools/loop/loop_lib.py#check_witness_classes` and
  `tools/loop/loop_lib.py#check_item_declarations`; then the schema's fixed rows joined both ways
  with the step exits and the floor item; then the record join of S5. Each refusal names the item.
  Observed by AC3, AC4, AC9, AC11 and AC13.
- **S5** — Records at a version. `[[record-version]]` rows in `tools/loop/loop.toml`, one per typed
  record kind an item returns or reads, each pinning the kind's current `version` and a `fields`
  hash recomputed from `tools/memory-tree/build_records.py#KINDS`. An input naming a record kind
  must be produced, at that version, by an item in its needs closure; a hash that moved while the
  version did not is red (§4). Observed by AC4.
- **S6** — The fixed set and exclusion refusals the clause plants, drawn by
  `tools/playbook/row_checks.py#check_rows` inside the composition over this kind's schema: an
  `amends` of a gov item's `witness` or `outcomes`; a `supersedes` of the floor item and of an exit
  item; an exclusion of an item another active item needs, naming the requirer; and an exclusion of
  an item `review.breakpoints` names, naming the key. Observed by AC5 and AC6.
- **S7** — The factory, `python tools/loop/loop_items.py new <name> --step <step> --actor <actor>
  --witness-by <text> --owner <build>`, with `--input`, `--allowance` and `--returns` owed by every
  actor but a `role:` one, run by `python tools/playbook/core.py new item <name> ...`. It appends one
  gov `[[item]]` row to the definition beside it, grades the result with the definition's own checks
  and restores the file's bytes and exits 1 when they refuse it. Observed by AC1.
- **S8** — Item tags joined to the step gate: an `item` row in `tools/govkit/surface-classes.toml`,
  its reader each gov `[[item]]` tag of the definition, its plant one gov item row taken out, and its
  witness `tools/playbook/pins.py#read_change_successors`, the change records that end a tag with a
  successor; and the class's row in `tools/govkit/usage.toml`. Observed by AC8.
- **S9** — The leg `loop item kind`, running `loop_items.py check --selftest`, with `enforces`
  holding the kind's `binds`, declared as gov's own `[[exempt_leg]]` of `tools/govkit/registry.toml`
  since the module reaches the playbook kit, to which the loop kit takes no edge. Observed by AC2 and
  AC10.
- **S10** — The pages: a section of `help/loop.md` on the item kind, its factory, its check and its
  plants; `help/overlay-rows.md` naming the item kind as the first registered schema and the
  `compose` verb; and the module's paragraph in `tools/loop/README.md`. Observed by AC10.

## 3. Non-goals (OUT)

- No gov item row but the factory's: the 61 rows, PINNED 2026-11-14 by counting the `[[item]]` tables
  of `tools/loop/loop.toml`, and their keys are `TOOL-dDeclaredLoop-12`'s, the per-field declaration
  check `TOOL-dDeclaredLoop-9`'s, and the `upstream` field `TOOL-dDeclaredLoop-29`'s, which adds it to
  this schema.
- No overlay rule: rows, patches, pins, exclusions, the classifier and the successor walk are
  dOrderedCharter-35's and -36's, called as landed; S3's verb adds no rule, nor an actor ranked by
  kind or a table-shaped field (§8 F6).
- No step gate: dSafePassage-10's gate, reader contract and fixture; this unit adds one class row.
- No repository stage or splice row: `TOOL-dDeclaredLoop-25`'s, whose items are this kind's rows.
- No other kind's factory: `TOOL-dDeclaredLoop-6` follows this row's shape for more kinds.
- No record kind's factory: the record kind's own kind is dConvergedCharter's; this unit pins
  versions over the record factory's existing kind rows and writes nothing into them.
- No counted-edge or reachability rule: `TOOL-dDeclaredLoop-33`'s, beside the needs-graph helper.
- No composition at a pinned revision: `TOOL-dDeclaredLoop-26`'s, which runs the S3 verb in a
  worktree at its pin.
- No version suffix written onto gov's `returns` (§8 F7).

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-12` — `needs`, the declared dependencies of each item row, whose acyclicity check through the needs-graph helper the composition reads
- **consumes-from** `TOOL-dDeclaredLoop-9` — `item.<step>.<name>`, the declared item rows the `item` kind registers
- **consumes-from** `TOOL-dDeclaredLoop-13` — the `loop.toml` transition rows, whose exit items this unit's fixed set keeps whole
- **hands-off** `TOOL-dDeclaredLoop-6` — `kind.item`, the first of this build's kind rows with a factory and schema, whose row shape the six rows there follow
- **hands-off** `TOOL-dDeclaredLoop-25` — `kind.item`, the kind of a repository stage's items and its exit item, whose composition checks hold them as they hold a gov step's; the schema's one `owner-seat` is 2, so a tag `item.adopter.<stage>.<name>` is that unit's to admit
- **hands-off** `TOOL-dDeclaredLoop-29` — `kind.item`, the item kind's schema file, to which that unit adds the `upstream` field
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 13, 14, each a scope item of that unit

## 4. Design

### The kind row

```toml
[[kind]]
tag = "kind.item"
owner = "dDeclaredLoop"
binds = ["principle.p16"]
population = "{prefix}/loop/loop.toml"
factory = "python {prefix}/loop/loop_items.py new"
gate = "loop item kind"
schema = "{prefix}/loop/item-schema.toml"
summary = "A work item of a gov step's program: an [[item]] row of the loop definition, or a repository's own in its overlay."
usage = "python {prefix}/playbook/core.py new item <name> --step <step> --actor <kind:name> --witness-by <text> --owner <build> [--input <layer:what> --allowance <text> --returns <record>]"
```

The population is a tracked path, the shape the register's header declares; the repository's half
is the overlay, which `tools/playbook/overlay_rows.py#read_overlay_rows` reads for every kind
carrying a `schema`. `core.py new item` resolves the factory's script and runs it with the name and
the flags after it (`tools/playbook/core.py#run_new`), and `tools/playbook/core.py#check_kind_row`
grades the factory's file and the gate's `enforces`.

### The schema

`[kind]`: `name = "item"`, `owner-seat = 2`. The fields:

| Field | `shape` | `ref` | Class | Why |
|---|---|---|---|---|
| `step` | scalar | | fixed, `principle=principle.p20` | the clause: a gov item's step |
| `witness` | scalar | | fixed, `principle=principle.p2` | the clause: a gov item's witness |
| `outcomes` | set | | fixed, `principle=principle.p24` | the clause: a gov item's outcome set |
| `actor` | scalar | | fixed, undeclared class | §8 F6 |
| `allowance` | scalar | | fixed, undeclared class | a free-text write grant has no order |
| `returns` | scalar | | fixed, undeclared class | S5's join reads it |
| `owner` | scalar | | fixed, undeclared class | the build that lands the item |
| `needs` | set | `needs` | open, `widens = "remove"` | FA-5: a constraint set |
| `inputs` | set | | open, `widens = "add"` | a read set: reading more widens |
| `routes` | set | | open, `widens = "add"` | §8 F6: patched whole, every change one widening |

A field with neither `fixed-by` nor `widens` reads fixed by its undeclared class
(`tools/playbook/row_checks.py#check_rows`), so the fixed set is deny-by-default. `tag` is no field:
a `supersedes` composes at gov's tag and an `amends` carries no `tag` of its own
(`tools/playbook/overlay_rows.py#derive_row_composition`), so a gov item's tag never changes.

`[[fixed-row]]` rows: the five exit items, PINNED 2026-11-14, the `[[step]]` rows of the definition name,
`item.plan.exit`, `item.design.exit`, `item.build.exit`, `item.test.exit` and `item.deploy.close`,
each `fixed-by = ["principle=principle.p20"]`, and `item.test.verdict`,
`fixed-by = ["principle=principle.p2"]`, whose witness the runner writes (FA-9's "`test.verdict` and
`entry.intake` among them",
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:202-203`).
`entry.intake` gains its row when dPlacedRequest declares it as an item. Only `principle=` sources
are written: `tools/playbook/overlay.py#check_fixed_sources` reads a `parser=` path as written, so a
literal tool path would resolve to nothing at another install prefix and is the spelling the
install-prefix ban refuses in a shipped file, and a `floor=` source refuses while no namespace
registers `floor`.

### The composition read

`derive_kind_composition(root, kind, exclude, records)` returns what `derive_row_composition`
returns, or None where the file the kind row's `schema` names is absent from `root`. Its body is
`read_kind_rows`' loop body today: `read_kind_schema`, the namespace row's `source` resolved through
the tool root and read by `git show HEAD:<path>`, `read_overlay_rows`, `read_tag_policy` at `HEAD`
when `exclude` is non-empty, and `derive_row_composition` under the stale mode `order`.

```text
python <prefix>/playbook/overlay_rows.py compose --kind <kind>
```

It composes the repository at the working directory, `exclude` from
`tools/playbook/overlay.py#read_excluded_tags` and the records from
`tools/playbook/instruction_units.py#read_change_records`, and prints one JSON object: `rows`, the
composed rows; `states`; `held`; `stale`; `operations`, the classified patch operations of the
row checks; and `pins`, each gov row's eight-hex pin over its canonical form, the pin an `amends` or
`supersedes` names. Exit 0; 1 with each red line of an `OverlayRefused`; 2 naming `unarmed` where the
kind is not registered with a schema or its schema file is absent, and on a usage error.

`tools/loop/loop_items.py` finds the playbook kit through `tools/loop/loop_lib.py#resolve_kit_dir`
and runs the verb as a subprocess, so the loop kit imports no playbook module and takes no edge to
that kit; where it does not resolve, `check` prints `unarmed` and exits 2, never green.

### Records at a version

An input that reads a record is written `<layer tag>:record-kind.<name>` or
`<layer tag>:record-kind.<name>@<n>`, and `returns` `record-kind.<name>` or
`record-kind.<name>@<n>`. An input naming no record kind as its whole text after the layer tag is
prose and joins nothing. An unversioned value reads the kind's current version (§8 F7):

```toml
[[record-version]]
kind = "record-kind.acceptance"
version = 1
fields = "<hash8>"   # the kind's KINDS row, its `required` and `closed`, as canonical JSON, SHA-256, eight hex
```

- Every typed kind, a key of `tools/memory-tree/build_records.py#KINDS`, that an item returns or
  reads holds one row; a row whose kind is no typed kind is refused.
- `check` recomputes each `fields` from that kind row. A hash that differs while `version` did not
  move is red, naming the kind: its meaning changed with no bump. A bump re-pins the hash.
- An untyped kind reads version 1 and has no row.
- Each record input of a composed item is met by an item in its needs closure, every tag its
  `needs` name, any-of members included, followed transitively, whose `returns` names that kind at
  that version; otherwise it is refused, naming the item and the input. After a bump, an input
  still pinned at the old version is refused until its item moves.

PINNED 2026-11-14 from the `returns` keys of `tools/loop/loop.toml`: two typed kinds are returned,
`record-kind.acceptance` by `item.build.acceptance` and `record-kind.disposition` by
`item.build.ratify`, so two rows, PINNED, are written; and no gov input names a record kind, so the join
grades repository rows and the plants, and `check` prints the count it joined.

`build_records.py` is the memory-tree kit's, which the loop kit requires. It is imported inside the
function through `read_memory_tree`, which joins `tools/loop/loop_lib.py` from
`tools/loop/loop_witness.py` at this second caller, the witness module importing it from there.

The rows live in the definition and not in the schema file:
`tools/playbook/overlay_rows.py#read_kind_schema` refuses any top table of a schema but `kind`,
`field` and `fixed-row`, and `tools/loop/loop_lib.py#check_loop` reads only its own tables.

### The checks, in order

1. The composition, through the verb. A refusal there, a fixed field or row patched, an exclusion
   another row needs or a policy key names, is printed and refuses before step 2.
2. `check_item_composition`: `check_program`, `check_witness_classes` and `check_item_declarations`
   over the definition holding the composed rows; each step's exit and `item.test.verdict` hold a
   `[[fixed-row]]`, and each `[[fixed-row]]` names a declared item, both ways.
3. The record versions, then the record join.
4. At a landing, the step gate's `item` class over the gov tags at the base and the tip.

`check` prints `loop: items composed · <n> row(s) · <m> repository`, one `loop: patch <row> on <tag> ·
<field> <op> · <class>` line per classified operation, one `loop: record-version <kind> · <n> ·
<hash>` line per row, `loop: record inputs · <n> joined`, and each refusal as `loop: refused · ...`.
Exit 0 green, 1 a refusal, 2 unarmed or a usage error.

### The factory

`new` appends one row to the definition beside it: `tag = "item.<step word>.<name>"`, the given
`step`, `actor`, `owner` and `witness = { class = "history", by = <text> }`, `needs = []`,
`outcomes = ["done"]`, `routes = { done = "<the step's exit item>" }`, and for an actor that is no
`role:` the given `inputs`, `allowance` and `returns`. It then runs `check_loop`, `check_program`,
`check_witness_classes` and `check_item_declarations` over the file as written, since the
composition reads `HEAD` and the row is not yet committed; a refusal restores the file's bytes and
exits 1. A name that is not one tag segment, a name `adopter`, a tag the definition declares, a step
that is no gov step, and a flag owed by the actor's kind and absent each exit 2 before any write.

### The step gate's class

`read_item_members(root)` reads the definition under `root` through `read_definition` and
`read_item_rows`, which grade nothing, so a plant that breaks a need still reads; an absent
definition answers an empty set, the reader contract of `tools/govkit/step_gate.py`.
`write_item_plant(clone)` takes the first `[[item]]` table out of the clone's definition, stages it
and returns `item:<tag>`. The class's `tools/govkit/usage.toml` row is `usage = "none"`: an item
is a definition row, used by no verb, key, hook, leg or page of its own.

### The plants

`--fixture --plant <case>` builds a scratch repository holding a copy of this working tree's tool
root and the conf files the kits read, committed, so a plant reads this tree's code and not `HEAD`'s;
it writes the plant, commits it, runs `check` there as a subprocess and relays its output and exit,
as `tools/playbook/fixtures/row_kind.py#build_tree` commits its fixture kind and policy file.
`PLANTS` holds one case per plant §6 names. `check --selftest` runs `check` over the tree and then every
plant through `tools/loop/loop_lib.py#run_selftest_cases`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/item-schema.toml` | schema file | none declared for files |
| `tools/loop/loop_items.py` | module | none declared for files |
| `check_item_composition` | function | `py.function` |
| `check_record_versions` | function | `py.function` |
| `derive_record_hash` | function | `py.function` |
| `read_composition` | function | `py.function` |
| `write_item_row` | function | `py.function` |
| `read_item_members` | function | `py.function` |
| `write_item_plant` | function | `py.function` |
| `write_fixture_plant` | function | `py.function` |
| `derive_kind_composition` | function of `tools/playbook/overlay_rows.py` | `py.function` |
| `compose` | verb of `tools/playbook/overlay_rows.py` | none |
| `[[record-version]]` | table of the definition | none |
| `item` | class row of `tools/govkit/surface-classes.toml` | none |
| `loop item kind` | leg | none |

### Migration

None: no repository row of this kind can exist before its schema registers, since
`tools/playbook/overlay_rows.py#read_overlay_rows` refuses an overlay table naming no registered row
kind.

### Rollout

Live on landing. In gov, the leg grades gov's own items on every bar. In a target, the next update's
render composes the item kind as it composes units, its delta report printing one line per gov item,
61 PINNED 2026-11-14, and a target holding no loop kit composes none (S3).

### Files touched (estimate)

- `tools/playbook/kinds.toml`: the `kind.item` row
- `tools/playbook/core-pending.txt`: the `kind` row of `kind.item`
- `tools/playbook/namespaces.toml`: the `item` row's `source`
- `tools/playbook/overlay_rows.py`: `derive_kind_composition`, the `compose` verb and its docstring
- `tools/playbook/render_playbook.py`: `read_kind_rows` through `derive_kind_composition`
- `tools/loop/item-schema.toml`
- `tools/loop/loop_items.py`
- `tools/loop/loop.toml`: the `[[record-version]]` rows
- `tools/loop/loop_lib.py`: `read_memory_tree`, and the docstring's sentence on the rows
- `tools/loop/loop_witness.py`: `read_memory_tree` imported from `loop_lib.py`
- `tools/loop/kit.toml`: the comment naming the module's reach
- `tools/loop/README.md`: the module's paragraph
- `tools/govkit/surface-classes.toml`: the `item` class row
- `tools/govkit/usage.toml`: the class row, and a row per command the pages show
- `tools/govkit/registry.toml`: the `[[exempt_leg]]` row
- `tools/gate-legs.json`: the leg `loop item kind`, argv `python {prefix}/loop/loop_items.py check
  --selftest`, `selftests`, `repo`, ceiling 300, `enforces` `principle.p16`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `memory/map/features/loop.md`: the leg in its `gate-legs` list
- `memory/map/generated/`, re-rendered by the codebase-map kit's `gen_map.py --write`
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped, its watch list holding the manifest
- `help/loop.md`: the item kind's section
- `help/overlay-rows.md`: the first registered kind, and the `compose` verb
- `help/reference/kinds.md`, re-rendered by `render_playbook.py --reference`

### Alternatives rejected

- **A second register for items.** The kinds register is the `kind` namespace's declaring source; a
  second one would be a kind outside the mechanism.
- **`routes` fixed.** The clause admits a pinned patch of a gov item's routes, and a fixed field
  refuses every patch.
- **Versions on the record factory's rows.** The record kind's factory is dConvergedCharter's;
  pinning here reads `KINDS` and writes nothing into it.
- **The population as a reader command.** The register's header declares a tracked-path glob.
- **Composing in the loop kit by importing the playbook kit's modules.** §8 F5.

## 5. Production-readiness checklist

- security — every repository row reaches the composition through the overlay's one reader; the
  checks only refuse; the fixed set is deny-by-default, a field declaring no `widens` refusing every
  patch; the factory writes one gov row and restores the file's bytes on a refusal.
- perf / scale — 61 gov rows, PINNED 2026-11-14, composed once per `check` by one subprocess. The
  leg's ceiling is 300 seconds, PINNED 2026-11-14 as `loop computed witness`'s, whose plants also
  build scratch repositories; `tools/run-gates/ceiling-evidence.txt` is the runner's, so no row.
- error / empty / loading states — an unresolved playbook kit, an unregistered kind and an absent
  schema each exit 2 as `unarmed`, never green; an unreadable overlay is the verb's exit 1; an empty
  `[[item]]` table is `check_program`'s refusal, since each step's exit must be a declared item.
- observability — each refusal names the item, the field, the requirer or the key, and the
  `fixed-by` source; each patch prints its class, each version row its hash.
- risks — §8 F6 fixes `actor`, so an adopter cannot re-assign a gov item's actor. Every target's
  render prints the item delta lines. Both kits' versions move where the lander mints them
  (`tools/govkit/govkit.py#cmd_epoch`).
- testing — what the change could newly red, and what keeps each green:
  - `core kinds` and `core meta-check`: the pending row is deleted in the same change, the leg
    exists, enforces `principle.p16` and carries no `guard`.
  - `govkit selftest`: `tools/govkit/selftest.py#check_step_gate_fixture` gains the `item` case,
    held by the class's plant and the witness row the fixture writes.
  - `docs`: the class has its `tools/govkit/usage.toml` row, each command the pages show has a
    usage row and anchor, a block a scratch adopter cannot run carries a `run: no` line, and
    `help/reference/kinds.md` is re-rendered for the row's new `usage`.
  - `step-gate`: no gov item tag leaves the definition in this change.
  - `tags (the resolver's checks)`: the pages and the README backtick only declared item tags, and
    spell every planted tag inside a fence or unbackticked.
  - `install-prefix (shipped surface)`: the shipped files spell `{prefix}`, and the schema writes no
    `parser=` path.
  - `playbook render selftest` and `policy fixtures`: the composition fixture's `delta` plant writes
    its own kinds register, composed as before, and `tools/playbook/pins.py`'s fixtures hold no
    register, so `0 row kinds registered` holds.
  - `loop definition`, `loop transition tables` and `loop checklist tags`:
    `tools/loop/loop_lib.py#check_loop` reads only its own tables, so `[[record-version]]` is not
    read there, and no `[[item]]` row moves.
  - `loop computed witness`: `read_memory_tree` keeps its name and body, imported from
    `loop_lib.py`.
  - `verdict epoch (kit version dates the engine)`: none of its delegates, the memory-tree kit's
    modules, moves; `receipt sync (installed files match the receipt)`: no playbook file is new,
    and gov's receipt holds no loop row.
  - `kickoff-manifest ratchet` and `codebase-map coverage + freshness`: the manifest re-stamped, the
    leg claimed by the loop feature and the map re-rendered.
- migration — none (§4).
- user docs — `help/loop.md`, `help/overlay-rows.md` and `help/reference/kinds.md` (S10, S1).

## 6. Acceptance criteria

- **AC1** — When `python loop_items.py --fixture --plant factory` runs in `tools/loop/`, its scratch
  repository runs `core.py new item demo --step step.test --actor command:demo --input
  "layer.flow:the demo input" --allowance "the demo record" --returns record-kind.demo --witness-by
  "the demo record" --owner dDeclaredLoop`, which appends the row tagged item.test.demo and exits 0;
  `check` over the committed result exits 0; and the same `new` run again exits 2 naming the tag.
  Red when: the factory writes a row its own gate refuses, or writes a declared tag twice.
- **AC2** — When `python tools/playbook/core.py kinds` runs on the built tree, it prints
  `kinds · green` with `kind.item` graded and not pending; `python tools/playbook/core.py meta-check`
  exits 0; and a `python -c` printing the `loop item kind` row of `tools/gate-legs.json` shows
  `enforces` holding `principle.p16`.
  Red when: the kind row names a gate leg that does not enforce its binds, or its pending row stays
  beside a landed factory and gate.
- **AC3** — When `python loop_items.py --fixture --plant repo-cycle` runs there, whose overlay
  adds two repository items of the test step each needing the other, `check` exits 1 naming the
  cycle; `--plant repo-unresolved-need`, a repository item needing an item no row declares, exits 1
  naming that need.
  Red when: the needs graph is read without the repository's rows.
- **AC4** — When `python loop_items.py --fixture --plant repo-input-unproduced` runs there, a
  repository item reading `layer.memory:record-kind.acceptance@1` with no needed item returning it,
  `check` exits 1 naming the input; `--plant repo-input-produced`, the same item needing
  `item.build.acceptance`, exits 0; `--plant version-unbumped`, the acceptance kind's required fields
  changed in the scratch's `build_records.py` at version 1, exits 1 naming `record-kind.acceptance`;
  `--plant version-bumped`, the same with the version 2 and the hash re-pinned, exits 0; and
  `--plant version-stale-input`, that bump beside the produced item's input still at `@1`, exits 1
  naming the input.
  Red when: a record's fields change and no version moves, or a bump leaves a reader at the old
  version unrefused.
- **AC5** — When `python loop_items.py --fixture --plant patch-witness` and
  `--plant patch-outcomes` run, each an `amends` of a gov item's fixed field, and `--plant
  supersede-floor` on `item.test.verdict` and `--plant supersede-exit` on `item.build.exit` run
  there, each exits 1 with the composition refused, naming the row and its `fixed-by` source.
  Red when: a fixed field or row of a gov item is patched or replaced.
- **AC6** — When `python loop_items.py --fixture --plant exclude-needed` runs there, excluding
  `item.test.select`, which `item.test.verdict` needs, it exits 1 naming `item.test.verdict`; with
  `--plant exclude-breakpoint`, excluding an item no other item needs and `review.breakpoints` names,
  it exits 1 naming the key `review.breakpoints`.
  Red when: an exclusion leaves a need or a breakpoint pointing at nothing.
- **AC7** — When `python loop_items.py --fixture --plant patch-remove-need` runs there, its
  `patch` line reads `needs remove · widens`; `--plant patch-add-need` reads `needs add · narrows`;
  and `--plant patch-routes`, an `amends` writing a gov item's `routes` whole, reads
  `routes add · widens`; each patches a gov item no `[[fixed-row]]` holds and exits 0.
  Red when: `needs` is classified as a permission set, so removing a need reads narrowing, or a
  changed route reads as no change.
- **AC8** — When `python tools/govkit/step_gate.py --fixture --plant item` runs, over a clone whose
  tip takes one gov item row out, it exits 1 printing `RED item:` and the tag; with `--with-row`,
  a witness row naming the member, it exits 0.
  Red when: a vanished item tag passes the step gate with no row naming it.
- **AC9** — When `python loop_items.py --fixture --plant amended-cycle` runs there, whose
  overlay text holds no cycle and whose `amends` adds `item.test.verdict` to the needs of
  `item.test.merge`, `check` exits 1 naming that cycle.
  Red when: the checks read the overlay text rather than the composition.
- **AC10** — When `grep -n '"loop item kind"' tools/gate-legs.json` runs, it finds the leg row with
  its argv naming the module and `check`; `grep -n 'kind.item' help/loop.md` finds the section;
  and `grep -n 'compose' help/overlay-rows.md` finds the verb.
  Red when: the leg row is absent or names another command, so no bar runs the check.
- **AC11** — When `python loop_items.py --fixture --plant exit-unfixed` runs there, the
  scratch schema holding no `[[fixed-row]]` for `item.build.exit`, `check` exits 1 naming
  `item.build.exit` and its step.
  Red when: the schema's fixed rows drift from the step exits the definition names.
- **AC12** — When `python loop_items.py --fixture --plant schema-absent` runs there, the scratch
  holding no `item-schema.toml`, the scratch's `overlay_rows.py compose --kind item` exits 2 naming
  `unarmed`, `check` exits 2, and a `python -c` subprocess there calling `read_kind_rows` prints no
  item row.
  Red when: a target holding the playbook kit without the loop kit's schema refuses its render.
- **AC13** — When `python loop_items.py check` runs there on the built tree, it exits 0 printing
  `loop: items composed · 61 row(s) · 0 repository` and two `loop: record-version` lines, PINNED.
  figure: 61 and two PINNED 2026-11-14, the `[[item]]` tables and the typed kinds returned at HEAD.
  Red when: a gov item fails the kind's own checks, or a typed kind returned holds no version row.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `loop definition` · `loop transition tables` · `loop checklist tags` · `loop computed witness` · `core kinds` · `core meta-check` · `core selftest` · `tags (the resolver's checks)` · `step-gate` · `docs` · `install-prefix (shipped surface)` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_items.py · covers AC1 AC3 AC4 AC5 AC6 AC7 AC9 AC11 AC12 AC13 · the `loop item kind` leg's `check --selftest`, its failing case staged by the `repo-cycle` plant · none

New arm: tools/govkit/selftest.py · covers AC8 · `check_step_gate_fixture` reads every class row, so the `item` row arms its own case, its failing case the row's plant with no witness row · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `tools/memory-tree/tree_lib.py#STATUS_TOKENS`. Observation, 2026-10-24: the tuple does not
  hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED (agent,
  2026-10-24, delegated): `OPEN`.
- **F2 — How does an input name the record it reads at a version, when `TOOL-dDeclaredLoop-12` writes
  inputs as `<layer tag>:<what>` and `returns` without a version?** Options: (a) a record input written
  `<layer tag>:record-kind.<name>@<n>` and `returns` written `record-kind.<name>@<n>`, prose inputs
  joining nothing; (b) a separate `reads` field. (b) is a second field for one fact. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3, this unit owning the kind's schema. At rev-4 the unit-12 rows
  landed with no suffix; F7 settles how an unversioned value reads.
- **F3 — Which direction widens `actor` and `routes`, which dOrderedCharter-36 S5's three forms do not
  name?** Options: (a) `actor` an ordered scalar from the most to the least witnessed kind, `routes` a
  set of pairs whose every change reads widening; (b) both fixed. (b) refuses the pinned patch of
  routes the clause admits. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. Its realisation
  over the landed classifier is F6's.
- **F4 — Which items are floor items?** v2's floor names invariants, and the adoption record names
  `test.verdict` and `entry.intake` as items whose witness a runner or a hook writes. RESOLVED (agent,
  2026-10-24, delegated): `item.test.verdict` here, `entry.intake` when its build declares it, rung 1.
- **F5 — How does the loop kit read a kind's composition, when no verb exposes it?** The landed
  `tools/playbook/overlay_rows.py` holds no command, and the owner resolved TOOL-dDeclaredLoop-26 §8
  F5 on 2026-11-05 to a `compose` verb on that module, run as a subprocess, for every loop-kit
  caller, and TOOL-dWitnessedBar-28's re-ground weighed the same verb. No such verb landed.
  Options: (a) this unit lands the verb, a thin read over `derive_row_composition` with the per-kind
  body of `read_kind_rows` held once in `derive_kind_composition`, in the shape the owner chose; (b)
  an import of the playbook modules inside a loop-kit function through `resolve_kit_dir`, as
  `tools/loop/loop_lib.py#read_role_defaults` imports the roles kit's library, an import route the
  owner's ruling did not take; (c) this unit waits on an ask filed with dOrderedCharter,
  whose build has landed. Recommendation (a): the owner's shape, one body for both readers, and no
  wait at order 11.
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 1, the owner's ruling of 2026-11-05 at
  TOOL-dDeclaredLoop-26 §8 F5. widens: none · relaxes: none
- **F6 — How do `actor` and `routes` take F3's directions under the landed classifier?**
  `tools/playbook/row_checks.py#derive_patch_class` ranks a scalar by the value itself, so an order
  of actor kinds refuses every actor value, `role:gov-builder` among them, as outside its order; and
  a field's shape is `set` or `scalar` alone (`tools/playbook/overlay_rows.py#SHAPES`), while
  `routes` is an inline table. Options: (a) `actor` fixed by its undeclared class, and `routes`
  declared `shape = "set"`, `widens = "add"`, patched by writing it whole in an `amends`, which
  `tools/playbook/row_checks.py#derive_entry_ops` reads as one add of the new table and one remove
  of gov's, so every changed route reads widening, an `add` table on it refused by `check_program`;
  (b) both fixed, a departure from the clause's pinned patch of routes; (c) a kind-ranked scalar and a table shape in dOrderedCharter's classifier, a
  change to a landed parent and a new unit. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3, the clause kept with the parent as landed;
  `actor` stays fixed until a classifier ranks it. widens: none · relaxes: none
- **F7 — How does an unversioned `returns` or input read, now that the landed rows carry no `@<n>`?**
  Options: (a) it reads the kind's current version, its `[[record-version]]` row's or 1, so a reader
  pinning `@<n>` is refused after a bump and an unversioned one follows it; (b) this unit writes
  `@1` onto every gov `returns` naming a typed kind and refuses an unversioned value; (c) an
  unversioned value refused with no rewrite, which reds the landed rows. Recommendation (a): no gov
  row moves, and the pinned reader the clause protects is still refused.
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3, the least churn that keeps the clause's red.
  widens: none · relaxes: none
- **F8 — Which principles does the kind bind, and its leg enforce?** Rev-3 bound `principle.p1`,
  `principle.p2`, `principle.p20` and `principle.p24`. The design record's `[enforcement]` table
  names `cl-dClosedLoop-0109` under no principle, a leg enforces its clause's row
  (TOOL-dDeclaredLoop-56 §8 F5), and every kind row binds `principle.p16`. Options: (a) `binds` stays
  `principle.p16` and the leg enforces it; (b) rev-3's four beside it, the leg enforcing five and
  the pending `principle.p24` row deleted, claiming a principle for a clause its row does not name.
  Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 1, the `[enforcement]` table as written.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 24, the flow adoption record's FA-1,
  FA-2 and FA-5 paragraphs, and the parents' landed specs at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-10-25 · S3 · §4 The schema · re-grounded on dOrderedCharter's specs at `462d20f35` per
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md` row 68: unit 36 S2
  refuses a `floor=` source before its namespace registers, so `item.test.verdict` is fixed by
  `principle.p2`; S3 points at TOOL-dDeclaredLoop-26 §8 F5 for how the loop kit reaches `compose_rows`.
- rev-4 · 2026-11-14 · §1 · S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6
  AC7 AC8 AC9 AC10 AC11 AC12 AC13 · §7 · §8 F2 F3 F5 F6 F7 F8 · §10 · re-grounded at HEAD `112ea12ac`
  by the brief 2026-11-14-prompt-TOOL-dDeclaredLoop-24-reground-brief; mechanism, carries, order and
  status kept. Landed names replace specced ones; the kind keeps `principle.p16` (F8) and S1 deletes
  its pending row; seat 2, principle sources, `actor` fixed, `routes` patched whole (F6); version rows
  in the definition (F7); S3 lands the `compose` verb (F5); the leg is gov's `[[exempt_leg]]`; the
  usage, registry, map and kickoff rows joined the write set; code cited by symbol.

## 10. Reuse audit

The seams extended are the landed parents. The register's factory verb
`tools/playbook/core.py#run_new` runs this kit's `new` by its row, and
`tools/playbook/core.py#check_kind_row` grades it. The composition is
`tools/playbook/overlay_rows.py#derive_row_composition` over `read_kind_schema` and
`read_overlay_rows`, with `tools/playbook/row_checks.py#check_rows` inside it and `derive_widenings`
beside it; `tools/playbook/render_playbook.py#read_kind_rows`'s per-kind body is extracted into
`derive_kind_composition`, never copied. The item checks are `tools/loop/loop_lib.py#check_program`
over `derive_needs_order` and `scan_cycles`, the needs-graph helper whose canonical copy is
`tools/lib/needs_graph.py`, with `check_witness_classes`, `check_item_declarations` and
`run_selftest_cases`; the class witness is `tools/playbook/pins.py#read_change_successors`, the
`unit` class's; `read_memory_tree` is extracted from `tools/loop/loop_witness.py`. `python
tools/codebase-map/reuse_lookup.py "compose a registered kind's gov rows with the overlay and check
the composed item needs graph"` ranked generic `rows`, `row` and `check` seams and
`tools/playbook/overlay.py#read_overlay`; no seam ranked composes a kind for a sibling kit, which the
verb supplies. `python tools/memory-recall/query.py "how does the loop kit read a registered kind's
composed rows"` with the terms below returned TOOL-dDeclaredLoop-26 §8 F5's ask, TOOL-dWitnessedBar-28's
re-ground weighing the same verb, and scout B's row for this unit; none disagrees with F5.

Recall terms used: derive_row_composition read_kind_schema compose verb overlay_rows kinds register owner-seat fixed-row widens check_rows TOOL-dDeclaredLoop-26 F5
