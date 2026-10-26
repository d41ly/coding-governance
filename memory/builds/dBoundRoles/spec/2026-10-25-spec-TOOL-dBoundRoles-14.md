# TOOL-dBoundRoles-14 — the `role` and `field` tag namespaces, their extractors and the role binding join

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 1 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0179@f74e2fff whole
**Carries:** node:tag-namespace.role
**Carries:** node:tag-namespace.field

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-6 TOOL-dBoundRoles-15 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-26 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

Register the two tag namespaces this build owns, `role` and `field`, each a row of the namespace
registry with its declaring source and its extractor, so every role slot is a `role.<slot>` tag and
every read key and harness stage key a `field.` tag the core's shape check grades. Until this unit
lands, PLAY-dOrderedCharter-10 S5 keeps every `role` tag red on purpose, and the `reads` vocabulary
keeps its own `:` separator beside the tag grammar's `.` (research-tags-b F1).

## 2. Scope (IN)

- **S1** — Two `[[namespace]]` rows in `tools/playbook/namespaces.toml`, in PLAY-dOrderedCharter-19
  S2's row shape (`ns`, `owner`, `layer`, `source`, `extractor`, `role`, `purpose-source`,
  `join-armed-by`), per §4 "### The two rows". Observed by AC4.
- **S2** — `extract_role` in `tools/playbook/tag_index.py`: one member `role.<slot>` per role file
  `tools/roles/agents/<slot>.agent.md`, `<slot>` the front matter's `name`, parsed by
  `roles_lib.parse_front_matter` imported through `resolve_kit_dir("roles", "roles_lib.py", here)`,
  so no second front-matter grammar exists. The row's text carries the role's raw `rules` value for
  S5. Observed by AC1.
- **S3** — `extract_field` in `tools/playbook/tag_index.py`: one member `field.<family>.<name>` per
  read key of `READ_FAMILIES` in `tools/roles/roles_lib.py`, its text the native key
  (`task:title`), and one member `field.stage.<seg>` per stage key of every `tools/roles/workflows.toml`
  entry, `<seg>` the key folded by `roles_lib.derive_stage_field_tag`. Observed by AC3.
- **S4** — The one read-key vocabulary, kept in `tools/roles/roles_lib.py`: `READ_KEYS` is derived
  from a new literal `READ_FAMILIES` (a dict from family to its field names, the same 23 keys
  `READ_KEYS` holds at base), `derive_field_tag(key)` maps a native key to its tag, and
  `parse_read_key(entry)` accepts either spelling, `task:title?` or `field.task.title?`, and returns
  the native key and its optional flag. R3 in `tools/roles/check_roles.py` and `render_handoff` in
  `tools/roles/handoff.py` read every `reads` entry through `parse_read_key` and nothing else.
  Observed by AC5 and AC6.
- **S5** — The role binding join, `check_role_bindings` in `tools/playbook/gov_tag.py`, run under
  `check`, the widening of the rule-tag binding (`check_rule_tags`, `tools/roles/roles_lib.py:257`)
  to `role.<slot>` both ways, per §4 "### The binding join". It prints `unarmed` while no indexed
  unit row names a `role.` selector, never green. Observed by AC2.
- **S6** — The cited-but-undeclared join for both namespaces through PLAY-dOrderedCharter-10 S4's
  `check_namespace_joins`: a `role.` or `field.` tag cited anywhere the index reads and declared by no
  extractor is red, naming the citation's path and line. Observed by AC1 and AC3.
- **S7** — Gov's ten role files' `reads:` lines rewritten to the tag spelling (`input:spec` becomes
  `field.input.spec`), and the catalogue region of `tools/roles/README.md` re-rendered by
  `check_roles.py --write`. A handoff's task block keeps the native key as its `###` heading, so its
  bytes and its task-sha are unchanged for the same inputs. Observed by AC6.
- **S8** — The fixture plants, on PLAY-dOrderedCharter-19 S13's `gov_tag.py --fixture --plant
  <case>`: `role-rows`, `role-binding` and `field-rows`. Observed by AC1, AC2 and AC3.
- **S9** — The name-check point: `role` and `field` reach `lexicon.py --tags`, PLAY-dOrderedCharter-10
  S7's hand-off, through the registry they now sit in, and `tools/playbook/README.md`'s line naming
  the build that arms each later namespace loses its `role` entry. Observed by AC7.

## 3. Non-goals (OUT)

- The grammar, the registry file, the index, the resolver, the shape check and the join factory:
  PLAY-dOrderedCharter-19's and PLAY-dOrderedCharter-10's, called here and never re-specced.
- The `workflow` namespace and the adopter forms `role.adopter.<name>` and `workflow.adopter.<name>`:
  TOOL-dBoundRoles-20's. `extract_role` yields whatever `name` a role file carries, so an adopter
  role file joins as data once that unit composes it.
- The item actor's native id `role:<slot>` (TOOL-dDeclaredLoop-24 S6) stays as it is; whether an
  actor names a declared role is that kind's composition check, not this join.
- Renaming the harness stage keys themselves. `specWriter`, `diffFinder` and their siblings are JSON
  keys every harness template reads (`tools/workflows/tier2-review.template.js:236`,
  `tools/workflows/unattended-build.template.js:455`); only their tags are folded (§8 F2).
- The `[[workflow.stages]]` row form: TOOL-dBoundRoles-22 re-points `extract_field`'s stage half to
  each row's `key` when it moves the table.
- Expanding a `field` tag into the work order: TOOL-dBoundRoles-3 reads the tags when it renders.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-19's registry, index, resolver and fixture, and PLAY-dOrderedCharter-10's `check_tag_shape` and `check_namespace_joins`; without them neither row has a reader
- **hands-off** `TOOL-dBoundRoles-1` — `role.<slot>`, the member each new role file it adds becomes
- **hands-off** `TOOL-dBoundRoles-20` — `role.<slot>`, the member set a repository's roles compose beside
- **hands-off** `TOOL-dBoundRoles-19` — `role.<slot>`, the tag each house file moved into the overlay selects its role by
- **hands-off** `TOOL-dBoundRoles-3` — `field.<family>.<name>`, the tag a work order names each handed input by
- **hands-off** `TOOL-dBoundRoles-22` — `field.<family>.<name>`, with `field.stage.<seg>` read from the stage rows it moves to
- **hands-off** `TOOL-dBoundRoles-43` — `READ_FAMILIES`, `extract_role` and the cited-but-undeclared join, which unit 43 extends to the work order, `handoff.py`'s vocabulary and the overlay's role rows (ids 15, 34, 38 and 63 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-59` — `parse_read_key`, through which unit 59 folds each entry unit 53's read check reads (id 21 of the round-1 audit of units 52 to 58)
- **hands-off** `TOOL-dBoundRoles-60` — `parse_read_key`, through which unit 60 reads 58 AC5's control role, and §3, where unit 60's pass mirrors unit 52's new edge (ids 22 and 23 of the round-1 audit of units 52 to 58)

## 4. Design

### The two rows

```toml
# tools/playbook/namespaces.toml, beside PLAY-dOrderedCharter-10's eight
[[namespace]]
ns = "role"
owner = "dBoundRoles"
layer = "layer.roles"
source = "tools/roles/agents/*.agent.md"
extractor = "tag_index:extract_role"
role = "selects"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"
join-armed-by = "dBoundRoles"

[[namespace]]
ns = "field"
owner = "dBoundRoles"
layer = "layer.roles"
source = "tools/roles/roles_lib.py, tools/roles/workflows.toml"
extractor = "tag_index:extract_field"
role = "describes"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"
join-armed-by = "dBoundRoles"
```

`role` selects: an instruction unit's `scope` names a role (layer-roles `[tags]`, "every instruction
unit names the roles it binds"; PLAY-dOrderedCharter-11 S1 selects by it). `field` describes: it names
an input, and no unit selects by it. `layer.roles` is v2 `[layers]`' core row for the roles layer
(v2:816), and the roles kit is core, so PLAY-dOrderedCharter-19 S14's `owned` arm admits both.

| `ns` | Members at base | Source |
|---|---|---|
| `role` | 10, one per file under `tools/roles/agents/` | each file's `name` |
| `field` | 23 read keys plus 7 distinct stage keys | `READ_FAMILIES`; each `stages` key |

The counts are PINNED, measured 2026-10-25 at `4ed9e567` (`ls tools/roles/agents`, `READ_KEYS` at
`tools/roles/roles_lib.py:36-40`, the four `stages` tables at `tools/roles/workflows.toml:37`, `:47`,
`:57`, `:67`); the check DERIVES them at every run.

### The extractors

Each takes a blob's path and text, as the index runs every extractor whose `source` matches the path
(PLAY-dOrderedCharter-19 S4), and yields `(tag, kind, line)` with the row text the index stores.

```
extract_role(path, text)   -> ("role.<name>", "member", line of `name:`), text = the raw `rules` value
extract_field(path, text)  -> roles_lib.py:    ("field.<family>.<name>", "member", line), text = "<family>:<name>"
                              workflows.toml:  ("field.stage.<seg>", "member", line), text = the stage key
```

`extract_field` reads `READ_FAMILIES` from the blob with `ast.parse` and `ast.literal_eval` of that
one assignment, so the index reads the committed vocabulary, never the importing process's module.
The `workflows.toml` half parses the blob with `tomllib`. The extractors never validate: a malformed
`name` reaches PLAY-dOrderedCharter-10 S3's `check_tag_shape`, which reds it with its reason.

### The read-key vocabulary

```python
READ_FAMILIES = {"task": ("title", "goal", "in", "out", "todo", "reuse", "acceptance", "gates"),
                 "card": ("route", "records", "classes", "read", "open", "reuse"),
                 "brief": ("goal", "items", "acceptance", "gates", "non-goals"),
                 "input": ("spec", "diff", "question", "prompt")}
READ_KEYS = frozenset("%s:%s" % (f, n) for f, names in READ_FAMILIES.items() for n in names)
```

The native key `task:title` stays the vocabulary's member and the tag `field.task.title` its tag, the
two-name form systems.md `[design-tags]` gives a node with a native id ("the resolver accepts both").
`parse_read_key` folds a tag spelling back to the native key before any reader sees it, so
`render_handoff`'s family dispatch (`tools/roles/handoff.py:338-379`) and its `### <key>` block
headings read native keys exactly as at base. A `field.` entry naming no member, or the two spellings
of one key in one `reads` value, is an R3 defect (named twice). A later family (TOOL-dDeclaredLoop-29
S5's `upstream`) joins by one `READ_FAMILIES` entry.

### The stage-key fold

`derive_stage_field_tag(key)` lower-cases each capital and puts a hyphen before it:
`specWriter` → `field.stage.spec-writer`. `STAGE_KEY_RE` (`tools/roles/check_roles.py:110`,
`^[a-z][A-Za-z]*$`) admits no digit and no hyphen, so the fold is injective and no two keys share a tag;
the extractor dedupes a key several workflows share (`skeptic`, `synthesis`).

### The binding join

layer-roles `[tags]` widens the `rules:` binding both ways: a unit's `role.*` scope and each role's
`rules:` must agree. Read from the index: the units' selector fields as PLAY-dOrderedCharter-10 S4
reads them, and the `role` rows' text (S2).

```
for each unit u whose scope names role.<slot> and practice.<tag>:
    red unless <tag> is among <slot>'s rules entries, ? stripped        "unit <u> binds <tag> to role.<slot>, whose rules does not cite it"
for each role <slot> whose rules cites <tag>:
    let B = units whose scope names practice.<tag> and any role. selector
    red when B is non-empty and no unit in B names role.<slot>          "role.<slot> cites <tag>, and no role-bound unit of it selects role.<slot>"
```

A unit naming `practice.<tag>` and no role selector binds every reader, so it is never a disagreement.
`check_rule_tags` itself is unchanged: it still grades a `rules` value against the charter's section 1,
and this join grades the same value against the units.

### Inventory

Minted: the two rows of S1; `extract_role` and `extract_field`; `READ_FAMILIES`, `derive_field_tag`,
`parse_read_key` and `derive_stage_field_tag` in `roles_lib.py`; `check_role_bindings`; the plants of
S8. Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at the pass.

### Migration

Additive. The colon spelling stays legal in every `reads` value, so an adopter's own role file renders
unchanged; gov's ten files move to the tag spelling in this unit (S7). No tag in either namespace is
cited in a source at base, so the joins' first run grades the members alone.

### Rollout

Live at landing on PLAY-dOrderedCharter-19's `tags` leg, which already runs every registered
namespace's extractor, and on the `roles catalogue` leg for R3.

### Files touched (estimate)

- `tools/playbook/namespaces.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`
- `tools/playbook/README.md`
- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/roles/handoff.py`
- `tools/roles/agents/` (the ten `reads:` lines)
- `tools/roles/README.md` (the catalogue region, rendered by `check_roles.py --write`)

### Alternatives rejected

- **Renaming the stage keys to kebab case.** Every harness template and its suite spells them as
  JSON keys, and the fold gives the same tag with none of that churn (§8 F2).
- **`READ_KEYS` read by importing `roles_lib` inside the extractor.** The import reads the working
  tree, and the index's rows are keyed by committed blob (PLAY-dOrderedCharter-19 S4).
- **A second front-matter parser in `tag_index.py`.** `parse_front_matter` refuses an indented,
  repeated or unknown key, and a copy would drift from it.

## 5. Production-readiness checklist

- security — no write path; the extractors parse committed blobs read-only, and `ast.literal_eval`
  evaluates one literal and never runs code.
- perf / scale — two extractors over eleven blobs; the index re-parses only changed blobs.
- error / empty / loading states — an empty population prints `unarmed`, never green; a roles kit the
  index cannot resolve leaves both namespaces `unarmed` with one line saying why.
- observability — `gov_tag.py check` prints each namespace's member count and the binding join's
  graded pair count.
- risks — a role file renamed without its citations reds the join at that pass, which is the intent;
  the fold hides a stage key's case from the shape check, said in §4.
- testing — the plants of S8 and the R3 case, observed by a pass through the fixture and the checker;
  the suite arms in §7 are observed RED then GREEN by the main loop at the close.
- migration — none owed by an adopter, as §4 Migration says.
- user docs — none owed: no page under `help/` describes the tag registry or the `reads` grammar;
  `tools/playbook/README.md` and `tools/roles/README.md` are updated by S7 and S9.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant role-rows` runs, its fixture holding role files
  named `gov-builder` and `gov-skeptic` and a guide citing `role.gov-builder` and `role.gov-buildr`, the
  index holds both `role` members and the check exits 1 naming `role.gov-buildr` alone as cited but
  undeclared.
  Red when: `extract_role` yields nothing, so both citations read undeclared, or the `role` row is
  absent, so both read `namespace not registered`.
- **AC2** — When `python gov_tag.py --fixture --plant role-binding` runs, a unit scoped
  `role.gov-builder` and `practice.yagni` beside a `gov-builder` whose `rules` lacks `yagni` exits 1
  naming the unit; a second unit scoped `practice.verify` and `role.gov-skeptic` beside a
  `gov-builder` citing `verify` exits 1 naming `role.gov-builder`; with both `rules` values fixed it
  exits 0.
  Red when: `check_role_bindings` grades one direction only, so the second plant passes.
- **AC3** — When `python gov_tag.py --fixture --plant field-rows` runs, the index holds
  `field.task.title`, `field.input.spec` and `field.stage.spec-writer`, each once, and a guide citing
  `field.task.titel` exits 1 naming it.
  Red when: the stage half yields `field.stage.specWriter`, which the shape check reds as `segment
  outside seg`, or a shared key such as `skeptic` is yielded twice.
- **AC4** — When `grep -cE '^ns = "(role|field)"' namespaces.toml` runs in `tools/playbook/`, it
  prints 2, and `grep -n 'dBoundRoles' README.md` run there names `role` as registered.
  Red when: a row is missing, so a tag in that namespace still reads `namespace not registered`.
- **AC5** — When `python -c "import roles_lib as l; print(l.parse_read_key('field.task.title?'), l.parse_read_key('task:title'), l.derive_stage_field_tag('diffFinder'))"`
  runs in `tools/roles/`, it prints `('task:title', True) ('task:title', False) field.stage.diff-finder`.
  Red when: the tag spelling is not folded to the native key, so `render_handoff` dispatches it to no
  family.
- **AC6** — When `python check_roles.py` runs in `tools/roles/` over the tree with the ten migrated
  `reads:` lines, it exits 0; with one entry planted as `field.task.titel` it exits 1 with one R3 line
  naming it; and `python handoff.py render --role gov-skeptic --build dBoundRoles --input spec=<a
  spec path> --stdout` prints the same `task-sha=` at base and after the migration.
  Red when: R3 reads the raw entry rather than `parse_read_key`'s result, so a migrated line reds, or
  the task block's heading moves to the tag spelling and the task-sha changes.
- **AC7** — When `printf 'role.field.x\n' | python tools/lexicon/lexicon.py --tags` runs, it exits 1
  refusing a first segment that is a namespace word, the word read from the registry.
  Red when: `field` is not a registered word, so the name passes.

## 7. Gates

The pass adds no leg: PLAY-dOrderedCharter-19's `tags` leg runs the extractors and the joins once its
build lands, and this unit's rows join it as data.

`roles catalogue` · `roles render selftest` · `roles adopter self-test` · `playbook render selftest` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 · the playbook-render selftest runs `gov_tag.py --fixture` under each plant of S8, its failing case staged by `role-rows` and `role-binding` · none
New arm: tools/roles/adopt-roles.test.sh · covers AC6 · a fixture role whose `reads` carries `field.task.titel` stages the failing case, one R3 line, while `field.task.title` yields none · none

## 8. Open questions

- **F1 — Which spelling do gov's own role files carry once the tag exists?** Options: (a) the tag
  spelling `field.task.title`, the colon spelling still legal; (b) keep the colon spelling and emit the
  tag only in the index; (c) the tag spelling with the colon refused, which reds every adopter role
  file on update and needs an upgrade step. (c) widens the unit into a migration nobody asked for, and
  (b) leaves two separators in gov's own text, against research-tags-b F1's "migrate, so one
  separator remains". RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, research-tags-b F1 and
  systems.md `[design-tags]` "the resolver accepts both" for a node with a native id; the colon
  spelling is a native id and is never retired, so no follow-up is owed.
  widens: none · relaxes: none
- **F2 — How do the harness stage keys become tags, when the shape forbids capitals?** Options: (a)
  rename every stage key to kebab case in `workflows.toml` and every harness template and suite;
  (b) fold each key into its tag, `specWriter` to `field.stage.spec-writer`, the key unchanged;
  (c) leave stage keys out of the namespace. (c) fails the brief's shared interface I2, which names
  `field.stage.<key>`; (a) changes a harness argument contract for a name. RESOLVED (agent,
  2026-10-25, delegated): (b), rung 3, the most feature-rich survivor, tie-broken by fewer open
  questions; the fold is injective under `STAGE_KEY_RE`, said in §4.
  widens: none · relaxes: none
- **F3 — Where does the binding join live?** Options: (a) in `tools/playbook/gov_tag.py check`, reading
  the role rows and unit rows the index already holds; (b) in `check_rule_tags`, importing the
  playbook kit's unit reader into the roles kit. (b) makes a core kit's library import a sibling kit
  for every render, and the index already holds both halves. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, reuse of the join seam PLAY-dOrderedCharter-10 S4 sets.
  widens: none · relaxes: none
- **F4 — The parent sections this unit calls are specced and not built at `4ed9e567`.**
  PLAY-dOrderedCharter-19 S2, S4, S13 and PLAY-dOrderedCharter-10 S3, S4, S7 have no code at base.
  RESOLVED (agent, 2026-10-25, delegated): the build run re-grounds on each section at its base and
  stops this unit if one is still absent then, rung 1, the brief's rule for every unbuilt parent.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 14, the brief's shared interface I2 and
  owned-node table, scout A's row for cl-0179, TOOL-dDeclaredLoop-18 as the pattern, and the roles kit
  at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring the edges of TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-59 and TOOL-dBoundRoles-60, the HIGH promotion and the minors batch of the round-1 audit of units 52 to 58; nothing else moved.

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-19's namespace registry and PLAY-dOrderedCharter-10's
extractor module, shape check and per-namespace join, specced and DEFERRED, with TOOL-dDeclaredLoop-18
S1-S6 as the copied pattern; in the kit today the seams are `READ_KEYS`
(`tools/roles/roles_lib.py:36-40`), `parse_front_matter` (`:306`), `check_rule_tags` (`:257`) and R3
(`tools/roles/check_roles.py:197-207`), each verified against source at `4ed9e567`. `python
tools/codebase-map/reuse_lookup.py "register a tag namespace for role slots and read-key fields"` ranked
generic name stems (`read`, `key`, `field`, `read_conf_key`) and named no namespace seam, the expected
answer: neither registry nor index exists at base. The recall probe returned this build's brief row,
scout A's row, TOOL-dDeclaredLoop-18's rows and TOOL-dWitnessedBar-12's `leg` rows as the precedents;
scout A cites `RULE_KEY_RE` at `:65` and `check_rule_tags` at `:257-281`, both as source reads.

Recall terms used: `python tools/memory-recall/query.py "how are the role and field tag namespaces registered" --terms "role namespace field namespace READ_KEYS reads vocabulary stage keys tag extractor namespaces.toml rule tags"`
