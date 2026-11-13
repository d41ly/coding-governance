# TOOL-dDeclaredLoop-18 — the `step`, `item`, `policy` and `command` tag namespaces, with their extractors

**Status:** INPROGRESS · rev-4 · 2026-11-13 · node d · Tier-2 · base ed497191 · streams tooling · order 1 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0103@2d82c817 whole
**Carries:** node:tag-namespace.step
**Carries:** node:tag-namespace.item
**Carries:** node:tag-namespace.policy
**Carries:** node:tag-namespace.command

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-build-TOOL-dDeclaredLoop-18-deviation-181.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-18-deviation-181.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-18-deviation-182.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-18-deviation-182.md) | deviation | — |
| [2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return.md) | journal | — |
| [2026-11-13-build-TOOL-dDeclaredLoop-18-2-builder-return.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-18-2-builder-return.md) | journal | — |
| [2026-11-13-build-TOOL-dDeclaredLoop-18-deviation-183.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-18-deviation-183.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md) | research | TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-56 |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-18-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-18-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-18-build-brief.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-18-build-brief.md) | journal | — |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-18-spec-brief.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-18-spec-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Register the four tag namespaces this build owns, `step`, `item`, `policy` and `command`, each a row of
the namespace registry with its declaring source and its extractor, so every tag minted in them joins
the core's tag-shape check, and every catalogue key's name is among the `policy` namespace's tags. Until
this unit lands, a tag in any of the four reads `namespace '<ns>' is not registered`, the first rule of
`tools/playbook/tag_index.py#derive_tag_fault` (the owner's tag-grammar answers; systems.md
`[design-tags]`, "Owners").

## 2. Scope (IN)

- **S1** — Four `[[namespace]]` rows in `tools/playbook/namespaces.toml`, each carrying every field of
  `REGISTRY_FIELDS`, as §4 "### The four rows" spells them. Observed by AC5 and AC8.
- **S2** — `extract_step` and `extract_item` in `tools/playbook/tag_index.py`, each one call of
  `derive_tag_rows` over the loop definition `tools/loop/loop.toml`: `step.<seg>` from each `[[step]]`
  row's `tag` and `item.<step>.<name>` from each `[[item]]` row's `tag`, the forms shared interface I2
  fixes. Observed by AC3.
- **S3** — `extract_policy` in `tools/playbook/tag_index.py`: one `tag` row `policy.<name>` per
  catalogue row of `tools/policy/catalogue.toml` whose `name` is all literal segments, and one `family`
  row per distinct literal prefix of the rows whose `name` carries a `<word>` or `*` segment (§8 F3).
  Observed by AC1, AC2 and AC6.
- **S4** — `extract_command` in `tools/playbook/tag_index.py`: one `tag` row `command.<kit>.<verb>` per
  `[[command]]` row of each kit descriptor `extract_kit` reads, `<kit>` the descriptor's `id` (§8 F2).
  Observed by AC4.
- **S5** — The family join, per §4 "### The family join": `derive_family_tags` in
  `tools/playbook/tag_index.py` reads the `family` rows and the citations under them, asks
  `read_declared_keys`, a function this unit adds to `tools/playbook/policy_value.py`, which of them a
  catalogue row matches, and hands the matched tags to `check_namespace_joins` and to `check_resolves`
  as declared (§8 F6, F7). A refused read declares nothing. Observed by AC6.
- **S6** — The fixture plants on `gov_tag.py --fixture --plant <case>`: `policy-ns-word`,
  `policy-catalogue`, `policy-family`, `loop-rows`, `loop-bad-seg` and `command-rows`, per §4
  "### The plants". Observed by AC1, AC2, AC3, AC4 and AC6.
- **S7** — The name-check point: the four namespace words reach `lexicon.py --tags` through the
  registry they now sit in, with no list typed elsewhere. Observed by AC7.
- **S8** — The two pages that list the registered namespaces: `tools/playbook/README.md`'s table of
  later namespaces and the build that arms each, and `help/tags.md`'s table of namespaces and the
  sentence under it, each naming this unit's four rows as registered. Observed by AC5.
- **S9** — The two seam lines of `memory/map/features/policy.md` that spell a Python seam as a
  backticked `policy.<symbol>` span are written in the charter's `path#symbol` form, so the armed
  `policy` namespace grades neither as a citation. Observed by AC8.

## 3. Non-goals (OUT)

- The grammar, the registry file, the index, the resolver, the shape check and the join factory:
  PLAY-dOrderedCharter-19's and PLAY-dOrderedCharter-10's, called here and never re-specced.
- The declaring sources' rows. The loop definition's `[[step]]` rows are TOOL-dDeclaredLoop-1's, its
  `[[item]]` rows TOOL-dDeclaredLoop-12's and TOOL-dDeclaredLoop-9's, the catalogue dGroundRules-1's,
  and the `[[command]]` rows the command factory's (TOOL-dDeclaredLoop-6). This unit reads whatever
  rows exist when it builds; later rows join as data.
- The `scenario` namespace: TOOL-dDeclaredLoop-27's row, beside these.
- The adopter forms `step.adopter.<name>`, `item.<step>.adopter.<name>` and
  `item.adopter.<stage>.<name>` as overlay rows: TOOL-dDeclaredLoop-24's and -25's. The extractors
  already yield whatever tag the source row holds, so those rows need no second extractor.
- A packet node id such as `policy-key.review.max-rounds` is a `carries.py` node and never a tag.
- Expanding a placeholder key into concrete tags (§8 F3).
- Any change under `tools/policy/`: the policy kit's modules and its catalogue are read and never
  edited.
- The `[[policy]]` rows of an instruction overlay as `policy` members: `extract_policy` reads the
  catalogue alone.
- A second namespace with `family` rows, and a registry of per-namespace family resolvers: the
  `policy` namespace is the one instance.
- A family prefix as a tag: `policy.review` cited on its own stays undeclared, and `show` and `where`
  resolve no `family` row.
- The lexicon's grading of a tag's name past the namespace word: dMindYourWords'.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-1` — the `step` namespace row and `extract_step`, so the loop definition's `step.<stage>` tags (`step.plan`, `step.design`, `step.build`, `step.test`, `step.deploy`) are registered members the shape check grades
- **hands-off** `TOOL-dDeclaredLoop-9` — the `item` namespace row and `extract_item`, so each `item.<step>.<name>` tag an item row declares is a registered member
- **consumes-from** external — the policy kit's `read_revision`, `parse_key` and `read_catalogue_row` in `tools/policy/policy.py`, loaded in process by `load_policy_kit` of `tools/playbook/policy_value.py`; without them S5 has no key-to-row matcher and every citation under a family reads undeclared

## 4. Design

Every claim below about current code was read at `cb34ba60`.

### The four rows

Appended to the `[[namespace]]` rows of `tools/playbook/namespaces.toml`, before its `[[native]]` rows.
Every row carries `owner = "dDeclaredLoop"` and `join-armed-by = "dDeclaredLoop"`; `dDeclaredLoop` is a
`[[build]]` slug of `memory/project/chain.toml`, so the `purpose` arm grades the owner.

| `ns` | `layer` | `source` | `extractor` | `role` | `purpose-source` |
|---|---|---|---|---|---|
| `step` | `layer.flow` | `each [[step]] row's tag in {prefix}/loop/loop.toml` | `tag_index:extract_step` | `selects` | `{prefix}/loop/loop.toml` |
| `item` | `layer.flow` | `each [[item]] row's tag in {prefix}/loop/loop.toml` | `tag_index:extract_item` | `selects` | `{prefix}/loop/loop.toml` |
| `policy` | `layer.instruction` | `each [[key]] row's name in {prefix}/policy/catalogue.toml, policy.<name> each, and one family row per literal prefix of the names carrying a placeholder segment` | `tag_index:extract_policy` | `describes` | `{prefix}/policy/catalogue.toml` |
| `command` | `layer.distribution` | `each [[command]] row's verb in a tracked kit.toml or *.kit.toml descriptor, command.<id>.<verb> each` | `tag_index:extract_command` | `describes` | `{prefix}/govkit/registry.toml` |

Each `purpose-source` is the path-only form, the one form of
`tools/playbook/tag_index.py#check_namespace_purpose` that holds for these four.

- A `<path>#<field>` source is red unless its path ends `.toml` or `.py`, which is why the rev-3
  Markdown path with a `#design-tags` field could not land.
- A `<path>#<field>` source over the catalogue would read each member through `read_toml_field`, which
  finds a row by the value of its tag key. A catalogue row's key holds `review.rounds` and the member
  is `policy.review.rounds`, so no member is ever found. Only 30 of the catalogue's 272 rows carry a
  `summary` (PINNED, read 2026-11-13), so the field would not grade the rest either.
- `{prefix}/loop/loop.toml` is not in the view until TOOL-dDeclaredLoop-1 lands, so the `step` and
  `item` rows print `pending` and are never red; the arm prints them path-only from then on.
- `{prefix}/govkit/registry.toml` is the path the `kit` row already names, the one tracked file that
  lists every descriptor a `command` row can sit in.

What the path-only form does not check: no member's purpose is read, only that the path is tracked.

The layers follow `tools/playbook/tag_index.py#check_owned`, which reds a tag minted in a core-layer
namespace by a source inside a kit whose descriptor is `optional` or `expansion`. `layer.flow` is the
loop's own core layer. `layer.instruction` is the layer `tools/policy/kit.toml` declares, so the
catalogue's rows are owned. `command` rows sit in every kit's descriptor, optional kits included, so the
row takes `layer.distribution`, the `expansion` layer the `kit` row takes for the same reason.

`step` and `item` select: an instruction unit's `scope` names them (PLAY-dOrderedCharter-11 S1).
`tools/playbook/tag_index.py#check_namespace_joins` grades every `selects` namespace alike: its
`selects` direction prints `unarmed` until some unit's `scope` names a tag of the namespace, and from
then every declared member that selects no unit is red. No unit names a `step` or `item` tag at
landing, so both print `unarmed` in that direction.

### The extractors

An extractor is called `fn(ctx, path, None)` to ask whether it reads `path`, answering `""` or `None`,
and `fn(ctx, path, text)` for its rows, each `(tag, kind, line, end_line, text)`
(`tools/playbook/tag_index.py`, its module docstring). A member is kind `tag`, the kind
`DEFINE_KINDS` holds: `check_tag_shape`, `derive_namespace_state`, `check_namespace_joins` and
`read_defined` read no other kind as a member.

| Function | Reads `path` when | Rows |
|---|---|---|
| `extract_step(ctx, path, text=None)` | it is `loop/loop.toml` under the tool root | `derive_tag_rows(text, "step")` |
| `extract_item(ctx, path, text=None)` | the same path | `derive_tag_rows(text, "item")` |
| `extract_policy(ctx, path, text=None)` | it is `policy/catalogue.toml` under the tool root | a `tag` row per literal name, a `family` row per placeholder prefix |
| `extract_command(ctx, path, text=None)` | `extract_kit` reads it: a `kit.toml` or `*.kit.toml` base name | a `tag` row `command.<id>.<verb>` per `[[command]]` row |

The tool root is the parent of `ctx["kit"]`, as `check_namespace_purpose` derives its `troot`; a root
install's `.` adds no segment. One private helper beside `_read_kit_file` holds that compare for the
three extractors that read a sibling kit's file.

`extract_policy` and `extract_command` read their rows through `read_toml_tags`, which keys a table's
rows by `ROW_TAG_KEYS`. This unit adds two entries to that map, `"key": "name"` and
`"command": "verb"`, so each row's line is its own `name =` or `verb =` line and its span ends where
`read_toml_tags` ends it. The map is also read by `read_toml_field`, where the two entries change no
verdict: no `purpose-source` of these rows names a field.

`extract_policy` over each `(name, line, end_line)`:

- A name with no `<word>` and no `*` segment yields `("policy." + name, "tag", line, end_line, <the
  span's text>)`, as `derive_tag_rows` builds a row.
- Any other name contributes its literal prefix, the segments before its first placeholder segment.
  Each distinct prefix yields one `("policy." + prefix, "family", line, line, <that line>)` at the
  first row that carries it. A name whose first segment is a placeholder has no prefix and yields
  nothing; the catalogue holds none (PINNED, read 2026-11-13).

`extract_command` reads the descriptor's top-level `id` as `extract_kit` does; a descriptor with no
string `id` yields nothing.

No extractor validates: each yields the row's spelling as written, so a malformed tag reaches
`check_tag_shape`, which reds it with `derive_tag_fault`'s reason. Registering the row is what puts the
namespace among the shape check's words.

### The catalogue in the `policy` namespace

dGroundRules-1 §4 lets a catalogue `name` carry a placeholder segment `<word>` or `*`. The catalogue
holds 272 rows, 264 literal names and 8 with a placeholder (PINNED, read 2026-11-13 by a `tomllib`
parse): `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.model.<role>.<harness>`,
`roles.harness.<role>`, `roles.auth.<role>`, `review.<stage>`, `review.<stage>.effort` and
`budgets.*`. Their literal prefixes are six: `policy.roles.effort`, `policy.roles.model`,
`policy.roles.harness`, `policy.roles.auth`, `policy.review` and `policy.budgets`. No prefix is also a
literal name.

`derive_tag_fault` over the 264 member tags and the six family tags, against the ten registered words
and this unit's four, returns no fault, and the longest member tag is 39 bytes (PINNED, the same
read). The red the clause names is a first segment that is a namespace word: a catalogue row
`name = "step.timeout"` yields `policy.step.timeout`, which `derive_tag_fault` refuses as
`first segment 'step' is a namespace word`.

### The family join

The `family` kind is minted here. Its readers:

| Reader | Change |
|---|---|
| `check_tag_shape` | reads `DEFINE_KINDS + ("selector", "family")`, so each prefix is shape-graded and reaches the name-check with the tags |
| `derive_family_tags(con, ctx)`, new | reads the `family` rows; returns the cited tags a catalogue row declares, and its lines |
| `check_namespace_joins` | a new keyword `family=()`, the tags joined to their namespace's `members` |
| `check_resolves` | a new keyword `family=()`, the tags joined to `defined` for its `names no row` test (§8 F6) |

Every other reader is unchanged. `derive_namespace_state` counts `DEFINE_KINDS` alone, so a namespace
holding only `family` rows stays `unarmed`. `read_defined`, `resolve_address`, `check_owned`,
`check_retired` and `check_namespace_purpose` read no `family` row.

`derive_family_tags(con, ctx)` returns `(tags, lines)`:

1. It reads the view's `family` rows. With none it returns `(set(), [])` and reads no policy, so a
   fixture or an install with no placeholder name pays nothing and needs no policy kit.
2. Its candidates are the graded spans `read_population` returns for the families' namespaces, the
   spans outside `<MEMORY_ROOT>/builds/`, that carry no `#`, are not in `read_defined`, and have a
   family tag as a dot-prefix: `text.startswith(family + ".")`. With none it reads no policy.
3. It strips the namespace word from each candidate and calls
   `read_declared_keys(keys, ctx["root"], "HEAD")` once. The candidates whose key is in the answer are
   `tags`.
4. A `PolicyRefused` leaves `tags` empty, so every candidate is red as undeclared in both arms, and
   the line carries the reader's own words.
5. It returns one line: `tags: join policy · families · <f> families, <c> cited under one, <d>
   declared by the catalogue`, with ` · refused: <line>` appended on a refused read.

`tools/playbook/gov_tag.py#run_check` calls it once, passes `tags` to both checks and prints the line
with the joins' lines. The default keeps the `check_namespace_joins` call in
`tools/playbook/instruction_units.py` as it is.

`read_declared_keys(keys, root, rev="HEAD") -> set[str]` is added to
`tools/playbook/policy_value.py`, the playbook kit's one module that reaches the policy kit. It is the
row walk `tools/playbook/policy_value.py#read_tag_policy` already runs, without the value:

- `load_policy_kit()`, a `LookupError` raised as `PolicyRefused`.
- `rows = policy.read_revision(str(root), rev)["rows"]`, the catalogue's rows and the overlay's at
  `rev`, the rows `policy.py get` matches against; a `policy.Refusal` raised as `PolicyRefused`.
- For each key, `policy.read_catalogue_row(policy.parse_key(key), rows)`. A key the call returns for
  is in the answer; a `policy.Refusal` of one key leaves that key out and the walk goes on.

`read_catalogue_row` is the policy kit's one key-to-row matcher, so no second matcher exists and no
refusal text is compared. No value is read, so a key whose row carries a derived default is declared:
`policy.py get review.build --explain --rev HEAD` exits 2 with `carries a derived default no reader
computes yet`, which is why the rev-3 read through `read_policy_value` could not be the signal (§8
F7). The fan-out is bounded: one in-process read per `check`, one row match per candidate.

What the family join does not check: a citation under a family whose key the matcher accepts is
declared whatever the placeholder stands for, so `policy.review.nosuchstage` is declared by
`review.<stage>`. The matcher reads the policy kit's catalogue on disk, and `extract_policy` reads the
tracked one; in a worktree they are one file.

### The plants

Six names join `PLANTS` in `tools/playbook/gov_tag.py`, each built by `build_tags_fixture` on the
`SHAPE_PLANTS` shape, its registry rows through `derive_fixture_row`. A sibling kit's path is
`instruction_units.derive_tool_rel("policy", "catalogue.toml")` or `("loop", "loop.toml")`.

| Plant | Registry rows | Files | Exit | Prints |
|---|---|---|---|---|
| `policy-ns-word` | `policy`, `step` | a catalogue of one row, `name = "step.timeout"` | 1 | `· shape · policy.step.timeout · first segment 'step' is a namespace word` |
| `policy-catalogue` | `policy` | the installed policy kit's `catalogue.toml`, byte for byte | 0 | `tags: plant policy-catalogue · <m> members of <l> literal names, <f> families of <p> prefixes` |
| `policy-family` | `policy` | a catalogue of `tags.slice` and `review.<stage>`; the guide cites `policy.review.build` and `policy.review.build.nope` | 1 | `` `policy.review.build.nope` is cited and undeclared in policy ``, and never a line holding `` `policy.review.build` `` |
| `loop-rows` | `step`, `item`, both `selects` | a loop definition of `[[step]] tag = "step.plan"` and `[[item]] tag = "item.plan.exit"` | 0 | `tags: plant loop-rows · where: rc=0 0, check: rc=0` |
| `loop-bad-seg` | `step` | a loop definition of `[[step]] tag = "step.Plan"` | 1 | `· shape · step.Plan · segment 'Plan' is outside [a-z0-9][a-z0-9-]*` |
| `command-rows` | `command` | a `[[command]]` row, `verb = "new"` and `run`, appended to `tools/corekit/kit.toml`; the guide cites `command.corekit.new` and `command.corekit.old` | 1 | `` `command.corekit.old` is cited and undeclared in command ``, and never a line holding `` `command.corekit.new` `` |

- `policy-catalogue` reads `<m>` and `<f>` from the index, the view's `tag` and `family` rows under
  `policy.`, and `<l>` and `<p>` from its own `tomllib` parse of the same bytes, which shares no code
  with `extract_policy`. It exits 0 only when `m == l`, `f == p`, both are above zero and `check` is
  green.
- `policy-family` needs one literal name so the namespace is armed; a catalogue of placeholder names
  alone is `unarmed` and grades no citation. Its matcher is the installed policy kit's, whose
  catalogue holds `review.<stage>` and no three-segment row matching `review.build.nope` (PINNED, read
  2026-11-13). The plant copies no kit and runs no subprocess: `run_fixture` runs in process, and
  `load_policy_kit` resolves the policy kit from the playbook kit's own directory,.
- `loop-rows` runs `where step.plan`, `where item.plan.exit` and `check`, and prints the three exits
  on one line, the form the `reference-row` plant prints.
- `loop-bad-seg` and `command-rows` need no branch of `run_plant`: they fall to its closing `check`.

In `tools/playbook/adopt-playbook.sh` the rows of `policy-ns-word`, `loop-rows`, `loop-bad-seg` and
`command-rows` join the tag resolver's `run_plant_rows` block, each with the block's `$_tk` flags. The
rows of `policy-catalogue` and `policy-family` reach the policy kit, so they run in a block of their
own guarded by `check_sibling_kit policy policy.py`, which prints `UNARMED` where no policy kit is
installed. Each plant builds one scratch repository; the `bad-seg` plant measured 2.2 s on 2026-11-13,
and the six rows' wall-clock ceiling is 60 s together.

### The command namespace

A command tag is `command.<kit>.<verb>`: `<kit>` is the descriptor `id`, already a `kit` namespace
member (`kit.<id>`), and `<verb>` is the verb's own segment. Its declaring source is a `[[command]]`
row in that kit's descriptor, holding `verb` and `run`. No descriptor holds one at `cb34ba60`, so the
namespace is `unarmed` at landing; TOOL-dDeclaredLoop-6's command factory writes the rows. A
descriptor table of rows is the shape `[[drive]]` already has in `tools/codebase-map/kit.toml`.

### The live tree at landing

`policy` is armed at landing with the catalogue's literal names, so every backticked or bracketed
`policy.<seg>` span of tracked Markdown outside `<MEMORY_ROOT>/builds/` is graded. Six distinct spans
exist (PINNED, a `git grep` on 2026-11-13).

| Span | Where | Reads as |
|---|---|---|
| `policy.py`, `policy.toml`, `policy.json` | `tools/policy/README.md`, `help/roles.md` | a file name: each is the base name of a tracked path, counted and never red |
| `policy.resolve`, `policy.validate` | `memory/map/features/policy.md`, two seam lines | undeclared and unresolved, two reds each, until S9 |
| `step.build` | `help/tags.md` | not graded: `step` is `unarmed` until the loop definition lands, and S8 rewrites the sentence |

S9 writes the two seam ids as `tools/policy/policy.py#resolve` and `tools/policy/policy.py#validate`.
A span holding `/` is outside `SPAN_RE`, so neither is a citation, and each is the charter's
`path#symbol` form, naming a top-level `def` of that module. The
map's seam parser keys on the `seam:` prefix and the first id token only
(`tools/codebase-map/map_lib.py#parse_affordance`), so the dossier's affordance block still parses.
The dossier's other two seam ids carry an underscore, sit outside `SPAN_RE`, and are left as written.

The policy keys also become bare-reference tails in `check_resolves`. Under `tags.bare-refs =
charter-only`, the value the landed revision reads (read 2026-11-13), only a `practice.` match counts,
so no line moves. Under `unique` or `never` every backticked policy key is a bare reference.

### Inventory

Minted: the four rows of S1; `extract_step`, `extract_item`, `extract_policy`, `extract_command`,
`derive_family_tags` and `read_declared_keys`; the `family` row kind; the `ROW_TAG_KEYS` entries `key`
and `command`; the `[[command]]` descriptor table with keys `verb` and `run`; the six plants of S6.
Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at the pass.

### Migration

Additive, with one respelling. The registry gains four rows and no row moves; the two dossier spans of
S9 are respelled in the commit that registers `policy`, since either alone leaves the `tags` leg red or
the respelling unexplained. Reverting the commit restores both.

### Rollout

Live at landing on the `tags` leg, whose `check` runs every registered namespace's extractor, the
shape check, both joins and the name-check. `step`, `item` and `command` land `unarmed`; `policy`
lands armed.

### Files touched (estimate)

- `tools/playbook/namespaces.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`
- `tools/playbook/policy_value.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`
- `help/tags.md`
- `memory/map/features/policy.md`

### Alternatives rejected

- **The extractors in the loop kit.** The loop kit does not exist at this unit's order, and the index
  imports every other extractor from its own module (§8 F4).
- **A placeholder key expanded into concrete tags.** `budgets.*` ranges over measured-file paths that
  are not tag-shaped, and `<role>` and `<workflow>` range over namespaces no build has registered yet.
- **`memory/map/` left out of the graded population.** That is a second population rule in
  `read_population` for two spans the charter's own cite form already spells.

## 5. Production-readiness checklist

- security — no write path; the extractors parse committed blobs read-only with `tomllib`, and the
  family join reads the policy kit's rows and writes nothing. A refused policy read declares no tag.
- perf / scale — four extractors over the loop definition, the catalogue and the kit descriptors; the
  index re-parses only changed blobs. The family join costs one policy read per `check`, and none when
  no citation sits under a family, the state of the tree at landing.
- error / empty / loading states — an empty namespace prints `unarmed`, never green; a malformed row
  reaches the shape check, which names it; a refused policy read prints its line and reds every
  candidate.
- observability — `check` counts the new members in its `<n> namespaces, <n> tags` line and names
  each armed namespace on its `joins` line; the family join prints its own line. `policy`, a
  `describes` namespace, also prints its unused members on one long `join policy` line once any unit
  row exists, printed and never red.
- risks — a catalogue key a later build adds with a namespace word first reds at that build's pass,
  which is the intent. A family row hides a placeholder segment from the shape check. A Markdown page
  that backticks a `policy.<symbol>` code reference reds from landing on; S9 clears the two that
  exist.
- testing — the plants of S6, observed by a pass through the fixture; the suite arm in §7 is observed
  RED then GREEN by the main loop at the close.
- migration — additive with one respelling, as §4 Migration says.
- user docs — `help/tags.md` lists the registered namespaces and names these three as unregistered;
  S8 brings it current, with `tools/playbook/README.md`.

## 6. Acceptance criteria

Each fixture command below ends with the two flags every tag plant takes,
`--set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new`, written `<flags>`.

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant policy-ns-word <flags>` runs, it
  exits 1 and prints a line holding `· shape · policy.step.timeout · first segment 'step' is a
  namespace word`.
  Red when: `extract_policy` yields the row under a kind `check_tag_shape` does not read, or drops it,
  so the tag is never graded and the plant exits 0.
- **AC2** — When `python tools/playbook/gov_tag.py --fixture --plant policy-catalogue <flags>` runs, it
  exits 0 and prints `tags: plant policy-catalogue · <m> members of <l> literal names, <f> families of
  <p> prefixes` with `<m>` equal to `<l>` and `<f>` equal to `<p>`.
  Red when: a literal name is skipped or a placeholder name is yielded as a member, so the counts
  differ and the plant exits 1.
  figure: all four are DERIVED at observation, two from the index and two from the plant's own parse;
  the read of 2026-11-13 gives 264 and 6.
  fixture: the installed policy kit's `catalogue.toml`; the tree holds it today.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant loop-rows <flags>` runs, it exits
  0 and prints `tags: plant loop-rows · where: rc=0 0, check: rc=0`; under `--plant loop-bad-seg` it
  exits 1 and prints a line holding `· shape · step.Plan · segment 'Plan' is outside`.
  Red when: `extract_step` normalises the case, so the malformed row reads green; or `extract_item`
  reads the `[[step]]` table, so `item.plan.exit` resolves to no row.
- **AC4** — When `python tools/playbook/gov_tag.py --fixture --plant command-rows <flags>` runs, it
  exits 1, prints a line holding `` `command.corekit.old` is cited and undeclared in command ``, and
  prints no line holding `` `command.corekit.new` ``.
  Red when: `extract_command` yields no row for the descriptor, so the namespace is `unarmed` and the
  plant exits 0; or it yields the verb without the descriptor's `id`, so `command.corekit.new` is red
  too.
- **AC5** — When `grep -cE '^ns = "(step|item|policy|command)"' tools/playbook/namespaces.toml` runs,
  it prints 4; `grep -c '| dDeclaredLoop |' tools/playbook/README.md` prints 0; and
  `grep -cE '^\| .(step|item|policy|command). \|' help/tags.md` prints 4.
  Red when: a row is missing, so a tag in that namespace still reads `is not registered`; or a page
  still lists the namespace as one a later build arms.
- **AC6** — When `python tools/playbook/gov_tag.py --fixture --plant policy-family <flags>` runs, it
  exits 1, prints a line holding `` `policy.review.build.nope` is cited and undeclared in policy ``,
  prints `tags: join policy · families · 1 families, 2 cited under one, 1 declared by the catalogue`,
  and prints no line holding `` `policy.review.build` ``.
  Red when: the join declares by string prefix rather than through `read_catalogue_row`, so
  `policy.review.build.nope` is declared and the plant exits 0; or `check_resolves` is not handed the
  family tags, so `policy.review.build` prints as `unresolved`; or a refused read declares a tag.
  fixture: the installed policy kit, whose catalogue holds `review.<stage>`; the tree holds it today.
- **AC7** — When `printf 'policy.item.x\n' | python tools/lexicon/lexicon.py --tags` runs, it exits 1
  and prints `lexicon: tag policy.item.x · first segment 'item' is a namespace word`.
  Red when: the `item` row is not in the registry the lexicon reads, so the tag is graded clean and
  the command exits 0, as it does at `cb34ba60`.
- **AC8** — When `python tools/playbook/gov_tag.py check` runs over the tree, it prints no `· join ·`
  and no `· unresolved ·` line holding a `policy.` span, no `· shape ·` line holding `policy.`, and one
  `tags: purpose · pending` line each for `step` and `item`; and
  `git grep -c -e 'policy\.resolve' -e 'policy\.validate' -- memory/map/features/policy.md` prints nothing.
  Red when: the two seam lines keep their spans, so `policy.resolve` prints on a `· join ·` line; or a
  `purpose-source` is spelled in a form the arm reds.
  cost: one index build over the tree, measured at 95 s cold by the `queued-writers` plant's comment in
  `tools/playbook/gov_tag.py`.

## 7. Gates

The pass adds no leg: the `tags` leg runs the extractors and the check, and this unit's rows join it as
data. What the leg does not check for this unit: no member's purpose, the path-only form; and no
`step`, `item` or `command` tag, while those three are `unarmed`.

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `lexicon selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `tags (the resolver's checks)` · `policy fixtures` · `recall floor` · `recall floor arms`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC6 · the playbook-render selftest runs `gov_tag.py --fixture` under each plant of S6, four rows in the tag resolver's block and two in a block guarded on the policy kit, its failing case staged by the `policy-ns-word`, `loop-bad-seg`, `command-rows` and `policy-family` plants · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple, so a `DRAFT` header parses as no header and the unit reads MISSING.
  Liveness: the tuple would carry it if the vocabulary admitted it. RESOLVED (agent, 2026-10-24,
  delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives a spec in drafting, rung 2.
  widens: none · relaxes: none
- **F2 — What declares the `command` namespace's members, and what is the form?** No source spells
  the form (scout B, shared interface 5). Options: (a) `command.<kit>.<verb>` from `[[command]]` rows
  in each kit descriptor; (b) members read from the kinds register's `kind.command` population, which
  TOOL-dDeclaredLoop-6 has not designed; (c) members parsed from PLAY-dOrderedCharter-6's `[[drive]]`
  rows, whose `command` field is free text with no verb. (b) leaves the source undefined and (c)
  yields no tag. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the shape shared interface I2
  states and the descriptor home foundations C4 gives a kind's instance ("descriptor and drive
  table"). widens: none · relaxes: none
- **F3 — How does a catalogue name with a placeholder segment join the `policy` namespace?** Options:
  (a) one `family` row per literal prefix, graded by the shape check, a citation under it resolved
  through `read_catalogue_row`; (b) expand each placeholder over a registered namespace's members;
  (c) skip the eight names. (b) fails on `budgets.*`, whose members are paths, and on `<role>` and
  `<workflow>`, whose namespaces are dBoundRoles'; (c) leaves eight names out of "every catalogue key's
  name". RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the only option grading every name.
  widens: none · relaxes: none
- **F4 — Shared interface I1 puts every module this build adds under `tools/loop/`; where do the four
  extractors live?** Options: (a) `tools/playbook/tag_index.py`, beside PLAY-dOrderedCharter-10's
  eight, the module the index imports them from; (b) a new `tools/loop/loop_tags.py`. (b) needs the loop
  kit, which TOOL-dDeclaredLoop-1 creates at order 2, after this unit, and an extractor module in a
  second kit the index must locate. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, tie-broken by
  reuse of the seam PLAY-dOrderedCharter-10 S2 sets; these are functions added to an existing module,
  not a module, so I1's rule is kept for modules. widens: none · relaxes: none
- **F5 — May S5's join call `read_policy_value` with a citation's key, when PLAY-dOrderedCharter-7 §4
  says every call passes its key as a string literal?** The literal is the shape TOOL-dGroundRules-8's
  reader-coverage arm counts as a reader of that key. The join consumes no value: it asks only whether a
  row matches, and a call with a computed key matches neither of that arm's reader shapes, so it is
  neither counted nor red. Options: (a) call `read_policy_value(key, root, rev="HEAD")` with the
  citation's key, a departure from that sentence that this spec states, and ask dOrderedCharter to admit
  it; (b) `tag_index.py` runs `policy.py get` itself through its own inline `resolve_kit_dir`, a second
  playbook-kit caller of the reader, against that section's "the playbook kit's one caller"; (c) an ask
  to dGroundRules for a `policy.py` verb that matches a key to its row and prints no value. (a) keeps
  one caller and one matcher and changes no code of the parent. (b) breaks the one-caller rule. (c) is
  the cleanest surface but waits on a third build. Recommendation (a). RESOLVED (owner, 2026-11-05):
  (a) the computed-key call. The build run files in dOrderedCharter's `BACKLOG.md` the ask "PLAY-dOrderedCharter-7 §4: a caller that resolves a cited key's row, reading no
  value, may pass that key unquoted; the reader-coverage arm neither counts nor reds it". F7 below
  reopens the signal this pick rests on; under F7 (b) no computed-key call is built and no ask filed.
- **F6 — `check_resolves` reds every graded citation into an armed namespace that no defined row
  holds, so a citation the family join declares is still `unresolved`. Does the family set reach
  `check_resolves`?** The rev-3 Non-goal kept "a family resolver inside PLAY-dOrderedCharter-19 S7's
  `resolves` check" out, and the code at `cb34ba60` makes that Non-goal and AC6 exclusive: with
  `policy` armed, `policy.review.build` prints `unresolved · names no row`. Options: (a) `run_check`
  hands the one set `derive_family_tags` returns to `check_resolves` as well as to
  `check_namespace_joins`, one derivation with two readers, and the Non-goal is withdrawn; (b) keep
  the Non-goal, so every valid citation under a family is red on the `tags` leg and S5 has no green
  case; (c) neither arm grades a citation under a family, counted and never red, which needs no
  matcher and leaves a misspelt key under a family unseen. (a) widens this unit's write to one more
  keyword on a function it already calls. (b) cannot land green. (c) drops S5's resolution, which the
  owner's F5 ruling presumes. Recommendation (a). §2 S5, §3, §4 and AC6 are written on (a).
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 6, ER:328: the rev-3 Non-goal is the bound relaxed, a bound the
  spec writer added beyond the clause, and no other option lands green with S5 kept; recorded in
  `2026-11-13-build-TOOL-dDeclaredLoop-18-deviation-183`.
  widens: none · relaxes: the rev-3 Non-goal on a family resolver inside the resolves check
- **F7 — What signals that a catalogue row matches a cited key?** The rev-3 signal was a
  `read_policy_value` call that returns. At `cb34ba60` it does not return for a matched key whose row
  carries a derived default: `policy.py get review.build --explain --rev HEAD` exits 2, and so do
  `review.build.effort`, `roles.effort.builder` and `budgets.x`. All eight placeholder rows are of
  that kind, so under S5's rule every citation under a family reads undeclared. Options: (a) keep the
  subprocess and tell the two refusals apart by their text, `is not a catalogue key` against every
  other line, which copies a policy-kit string into the playbook kit with no parity gate; (b) match in
  process: `read_declared_keys` in `tools/playbook/policy_value.py` calls the policy kit's
  `read_catalogue_row` over `read_revision`'s rows, as `read_tag_policy` in that module already does,
  reading no value; (c) F5's option (c), a `policy.py` verb that matches and prints no value, which
  writes under `tools/policy/` and is outside this unit's scope; (d) the `policy-family` plant sets
  the key and "declared" means set in the policy file, so a correct citation of an unset key is red in
  every repository. (b) uses the one matcher directly, compares no text, and makes F5's computed-key
  call and its ask unnecessary; it departs from the rev-2 sentence that the policy kit is never
  imported, which `read_cap_value` and `read_tag_policy` already depart from. (b) displaces the
  owner's F5 pick, so it is the owner's or the mandate's to take, not this revision's. Recommendation
  (b). §2 S5, §3 Edges, §4 and AC6 are written on (b); under (a) `derive_family_tags` calls
  `read_policy_value` once per candidate instead, and the write set is the same.
  RESOLVED (agent, 2026-11-13, delegated): (b), rung 3: the one matcher called in process meets AC6 with no copied
  text and no follow-up ask; the owner's F5 pick permitted the computed-key call and is left unused, not reversed.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 18, the brief's shared interface I2 and
  owned-node table, scout B's row for cl-0103, and PLAY-dOrderedCharter-10 and -19 at base `ed497191`.
- rev-2 · 2026-10-25 · S5 · §3 Edges · §4 The catalogue in the `policy` namespace · AC6 · §8 F5 · §10 ·
  re-grounded on PLAY-dOrderedCharter-19 rev-5 by
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md` row 55: the policy join
  reads the policy kit by subprocess through `read_policy_value`, never by import, and a `PolicyRefused`
  reads a citation as undeclared; the computed-key call is §8 F5, open for the owner.
- rev-3 · 2026-11-05 · S5 · §8 F5 · the owner resolved F5 to (a), the computed-key call and its ask, per
  the brief `2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks`; S5 names the departure as picked.
- rev-4 · 2026-11-13 · §1 · S1 S2 S3 S4 S5 S6 S8 S9 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 ·
  §7 · §8 F5 F6 F7 · §10 · re-grounded on the code at `cb34ba60` after the builder return
  `2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return`, whose six divergences are answered in
  turn. One: §4 "The four rows" gives each row a path-only `purpose-source`. Two: §4 "The extractors"
  states the five-field row contract and kind `tag`, and §4 "The family join" names the readers of
  `family`. Three: §8 F6, with §3's Non-goal withdrawn and S5 and AC6 written on its option (a). Four:
  §8 F7, the in-process row match, with S5, §3 Edges and AC6 written on its option (b). Five: S9, §4
  "The live tree at landing" and AC8 respell the two dossier spans. Six: §4 "The plants" places the
  counts on the `policy-catalogue` plant, and AC1 and AC3 quote `derive_tag_fault`'s reasons. The
  smaller points: the `policy-family` plant copies no kit, and §4's write set gains
  `tools/playbook/adopt-playbook.sh`, `tools/playbook/policy_value.py`, `help/tags.md` and the
  dossier.

## 10. Reuse audit

The seams extended exist at `cb34ba60`, all in the playbook kit. The registry is
`tools/playbook/namespaces.toml`, read by `read_namespaces`. The extractors reuse `derive_tag_rows` and
`read_toml_tags` with their `ROW_TAG_KEYS` map, and `extract_kit`'s path test. The checks extended are
`check_tag_shape`, `check_namespace_joins` and `check_resolves`. The key matcher is the policy kit's
`read_catalogue_row`, reached as `read_tag_policy` in `tools/playbook/policy_value.py` reaches it. The
plants reuse `SHAPE_PLANTS`, `derive_fixture_row` and the `run_plant_rows` block of
`tools/playbook/adopt-playbook.sh`. `python tools/codebase-map/reuse_lookup.py "register a tag
namespace with an extractor over a TOML table"`, run 2026-11-13, ranked `read_namespaces` and
`check_namespace_joins` of `tools/playbook/tag_index.py` and `build_tags_fixture` of
`tools/playbook/gov_tag.py` among its candidates, the seams named here. No existing seam fits the
`family` kind: a read of `tools/playbook/tag_index.py` for the kinds its readers name finds `doc`,
`section`, `tag`, `retired`, `selector`, `span`, `unclosed` and `parsed`, and none stands for a prefix
that declares the tags under it.

Recall terms used: `python tools/memory-recall/query.py "how are tag namespaces registered with extractors and shape checked" --terms "namespace registry extractor tag grammar seg shape check namespace word policy catalogue key"`
