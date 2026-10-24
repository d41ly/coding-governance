# TOOL-dDeclaredLoop-18 — the `step`, `item`, `policy` and `command` tag namespaces, with their extractors

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 1 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0103@2d82c817 whole
**Carries:** node:tag-namespace.step
**Carries:** node:tag-namespace.item
**Carries:** node:tag-namespace.policy
**Carries:** node:tag-namespace.command

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Register the four tag namespaces this build owns, `step`, `item`, `policy` and `command`, each a row of
the namespace registry with its declaring source and its extractor, so every tag minted in them joins
the core's tag-shape check, and every catalogue key's name is among the `policy` namespace's tags. Until
this unit lands, PLAY-dOrderedCharter-10 S5 keeps every `step`, `item` and `policy` tag red on purpose
(the owner's tag-grammar answers; systems.md `[design-tags]`, "Owners").

## 2. Scope (IN)

- **S1** — Four `[[namespace]]` rows in `tools/playbook/namespaces.toml`, in PLAY-dOrderedCharter-19
  S2's row shape (`ns`, `owner`, `layer`, `source`, `extractor`, `role`, `purpose-source`,
  `join-armed-by`), per §4 "### The four rows". Observed by AC5.
- **S2** — `extract_step` and `extract_item` in `tools/playbook/tag_index.py`, yielding `step.<seg>`
  from each `[[step]]` row's `tag` and `item.<step>.<name>` from each `[[item]]` row's `tag` of the
  loop definition `tools/loop/loop.toml`, the forms shared interface I2 fixes. Observed by AC3.
- **S3** — `extract_policy` in `tools/playbook/tag_index.py`: one member `policy.<name>` per catalogue
  row of `tools/policy/catalogue.toml` whose `name` is all literal segments, and one `family` row per
  distinct literal prefix of the rows whose `name` carries a `<word>` or final `*` segment (§8 F3).
  Observed by AC1, AC2 and AC6.
- **S4** — `extract_command` in `tools/playbook/tag_index.py`: one member `command.<kit>.<verb>` per
  `[[command]]` row of each kit descriptor `tools/*/kit.toml`, `<kit>` the descriptor's `id` (§8 F2).
  Observed by AC4.
- **S5** — The per-namespace join, through PLAY-dOrderedCharter-10 S4's `check_namespace_joins`:
  every tag cited in each of the four namespaces is a declared member, a `policy` citation under a
  family prefix resolving through dGroundRules-2 S4's `read_catalogue_row`, the one key-to-row matcher;
  each join prints `unarmed` while its population is empty, never green. Observed by AC4 and AC6.
- **S6** — The fixture plants, on PLAY-dOrderedCharter-19 S13's `gov_tag.py --fixture --plant <case>`:
  `policy-ns-word`, `policy-catalogue`, `policy-family`, `loop-rows`, `loop-bad-seg` and
  `command-rows`. Observed by AC1, AC2, AC3, AC4 and AC6.
- **S7** — The name-check point: the four namespace words reach `lexicon.py --tags`, the hand-off of
  PLAY-dOrderedCharter-10 S6, through the registry they now sit in, with no list typed elsewhere.
  Observed by AC7.
- **S8** — `tools/playbook/README.md`'s line naming the build that arms each later namespace loses its
  `step`, `item` and `policy` entries and names this unit's four rows as registered. Observed by AC5.

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
- Expanding a placeholder key into concrete tags (§8 F3), and a family resolver inside
  PLAY-dOrderedCharter-19 S7's `resolves` check.
- The lexicon's grading of a tag's name past the namespace word: dMindYourWords'.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-1` — the `step` namespace row and `extract_step`, so the loop definition's `step.<stage>` tags (`step.plan`, `step.design`, `step.build`, `step.test`, `step.deploy`) are registered members the shape check grades
- **hands-off** `TOOL-dDeclaredLoop-9` — the `item` namespace row and `extract_item`, so each `item.<step>.<name>` tag an item row declares is a registered member

## 4. Design

### The four rows

```toml
# tools/playbook/namespaces.toml, beside PLAY-dOrderedCharter-10's eight
[[namespace]]
ns = "step"
owner = "dDeclaredLoop"
layer = "layer.flow"
source = "tools/loop/loop.toml, the tag of each [[step]] row"
extractor = "tag_index:extract_step"
role = "selects"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"
join-armed-by = "dDeclaredLoop"
```

| `ns` | `source` | `extractor` | `role` | Members at landing |
|---|---|---|---|---|
| `step` | `tools/loop/loop.toml`, each `[[step]]` row's `tag` | `tag_index:extract_step` | `selects` | 5, once TOOL-dDeclaredLoop-1 lands |
| `item` | `tools/loop/loop.toml`, each `[[item]]` row's `tag` | `tag_index:extract_item` | `selects` | unarmed until TOOL-dDeclaredLoop-12 |
| `policy` | `tools/policy/catalogue.toml`, each `[[key]]` row's `name` | `tag_index:extract_policy` | `describes` | DERIVED from the catalogue |
| `command` | `tools/*/kit.toml`, each `[[command]]` row | `tag_index:extract_command` | `describes` | unarmed until TOOL-dDeclaredLoop-6 |

`step` and `item` select: an instruction unit's `scope` names them (PLAY-dOrderedCharter-11 S1). The
dead-selector arm of PLAY-dOrderedCharter-10 S4 stays named to `reader` and `practice`, as that unit
writes it; a step or item no unit selects is printed, never red, because no unit selects items yet.

### The extractors

Each extractor takes a blob's path and text, as the index runs every extractor whose `source` matches
the path (PLAY-dOrderedCharter-19 S4), parses the TOML with `tomllib`, and yields `(tag, kind, line)`.

```
extract_step(path, text)    -> ("step.<seg>", "member", line)          per [[step]] row
extract_item(path, text)    -> ("item.<step>.<name>", "member", line)  per [[item]] row
extract_policy(path, text)  -> ("policy.<name>", "member", line)       per literal [[key]] name
                               ("policy.<prefix>", "family", line)     per distinct placeholder prefix
extract_command(path, text) -> ("command.<id>.<verb>", "member", line) per [[command]] row
```

The extractor never validates: it yields the row's spelling as written, so a malformed tag reaches
PLAY-dOrderedCharter-10 S3's `check_tag_shape`, which reds it with its reason. The shape check is what
"each joining the core's tag-shape check" names; registering the row is what puts the namespace in
`words`, so a tag in it stops reading "namespace not registered".

### The catalogue in the `policy` namespace

dGroundRules-1 §4 lets a catalogue `name` carry a placeholder segment `<word>` or a final `*`. Eight
of v2's 260 `[policies]` key cells do (PINNED, measured 2026-10-24 over v2 lines 1125-1400):
`roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.model.<role>.<harness>`,
`roles.harness.<role>`, `roles.auth.<role>`, `review.<stage>`, `review.<stage>.effort` and
`budgets.*`. Their literal prefixes are six: `policy.roles.effort`, `policy.roles.model`,
`policy.roles.harness`, `policy.roles.auth`, `policy.review` and `policy.budgets`, each one `family`
row whose text names every catalogue name under it. The shape check grades the family tag, so every
literal segment of every catalogue name is graded, and the first segment of each is checked against
the namespace words. A citation `policy.review.build` is joined as declared when `read_catalogue_row`
returns a row for `review.build`; the join imports that matcher through
`resolve_kit_dir("policy", "policy.py", here)`, the import PLAY-dOrderedCharter-10 S7 makes for the
registry, so no second key matcher exists.

The red the clause names is a first segment that is a namespace word: a catalogue row
`name = "step.timeout"` yields `policy.step.timeout`, whose first segment after the namespace is the
registered word `step`. Over v2's catalogue no first segment is a registered word (PINNED, the same
measurement: `hooks`, `kits` and `builds` are plurals, and `policy-file` is not `policy`), so the
catalogue is green.

### The command namespace

A command tag is `command.<kit>.<verb>`: `<kit>` is the descriptor `id`, already a `kit` namespace
member (`kit.<id>`), and `<verb>` is the verb's own segment. Its declaring source is a `[[command]]`
row in that kit's `kit.toml`, holding `verb` and `run`. No row exists at base, so the namespace is
`unarmed` at landing; TOOL-dDeclaredLoop-6's command factory writes the rows. A descriptor table that
govkit does not read is the precedent PLAY-dOrderedCharter-6 S1 sets with `[[drive]]`.

### Inventory

Minted: the four rows of S1; `extract_step`, `extract_item`, `extract_policy` and `extract_command`;
the `family` row kind of the `policy` namespace; the `[[command]]` descriptor table with keys `verb`
and `run`; the plants of S6. Naming cells: each function is asked of `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` at the pass.

### Migration

Additive. No tag in these namespaces exists in a source at base, so the shape check's first run over
them grades the catalogue and whatever loop rows have landed.

### Rollout

Live at landing on PLAY-dOrderedCharter-19's `tags` leg, which already runs every registered
namespace's extractor and the shape check.

### Files touched (estimate)

- `tools/playbook/namespaces.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py` (the plants of S6)
- `tools/playbook/README.md`

### Alternatives rejected

- **The extractors in the loop kit.** The loop kit does not exist at this unit's order, and the index
  imports every other extractor from its own module (§8 F4).
- **A placeholder key expanded into concrete tags.** `budgets.*` ranges over measured-file paths that
  are not tag-shaped, and `<role>` and `<workflow>` range over namespaces no build has registered yet.

## 5. Production-readiness checklist

- security — no write path; the extractors parse committed blobs read-only with `tomllib`.
- perf / scale — four extractors over three source files; the index re-parses only changed blobs.
- error / empty / loading states — an empty namespace prints `unarmed`, never green; a malformed row
  reaches the shape check, which names it.
- observability — `gov_tag.py check` prints each namespace's member and family counts.
- risks — a catalogue key a later build adds with a namespace word first reds at that build's pass,
  which is the intent; the family rows hide a placeholder segment from the shape check, said in §4.
- testing — the plants of S6, observed by a pass through the fixture; the suite arm in §7 is observed
  RED then GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — none owed: no page under `help/` describes the tag registry; `tools/playbook/README.md`
  is updated by S8.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant policy-ns-word` runs, its fixture catalogue
  holding a row `name = "step.timeout"`, the check exits 1 and names `policy.step.timeout` with the
  reason `first segment is a namespace word`.
  Red when: the `step` row is not registered, so the plant reads `namespace not registered` for the
  word instead of being refused for it, or the policy extractor drops the row.
- **AC2** — When `python gov_tag.py --fixture --plant policy-catalogue` runs over a copy of the catalogue,
  `catalogue.toml`, the check exits 0 and prints the `policy` namespace's member count
  equal to the catalogue's literal-name row count and its family count 6.
  Red when: a literal name is skipped, so the member count falls below the row count.
  figure: the member count is DERIVED at observation from the catalogue copy; the 6 is PINNED,
  measured 2026-10-24.
- **AC3** — When `python gov_tag.py --fixture --plant loop-rows` runs, the index holds `step.plan`
  and `item.plan.exit`; under `--plant loop-bad-seg`, whose row is `tag = "step.Plan"`, the check
  exits 1 naming `step.Plan` with `segment outside seg`.
  Red when: `extract_step` normalises the case, so the malformed row reads green.
- **AC4** — When `python gov_tag.py --fixture --plant command-rows` runs, a fixture `kit.toml` with
  `id = "playbook"` and `[[command]] verb = "new"` yields `command.playbook.new`, and a guide citing
  `command.playbook.old` exits 1 naming it as cited but undeclared.
  Red when: the command join is green on the citation, or the namespace reads green with no rows.
- **AC5** — When `grep -cE '^ns = "(step|item|policy|command)"' namespaces.toml` runs in
  `tools/playbook/`, it prints 4, and `grep -n 'dDeclaredLoop' tools/playbook/README.md` names the
  four rows as registered.
  Red when: a row is missing, so a tag in that namespace still reads `namespace not registered`.
- **AC6** — When `python gov_tag.py --fixture --plant policy-family` runs, its catalogue holding
  `review.<stage>` and a guide citing `policy.review.build` and `policy.reviews.build`, the family
  row `policy.review` is graded, `policy.review.build` joins as declared, and the check exits 1 naming
  `policy.reviews.build` alone.
  Red when: the join matches by string prefix rather than through `read_catalogue_row`, so
  `policy.reviews.build` joins too.
- **AC7** — When `printf 'policy.item.x\n' | python tools/lexicon/lexicon.py --tags` runs, it exits 1
  refusing a first segment that is a namespace word, the word read from the registry.
  Red when: the lexicon reads its namespace words from anywhere but the registry, so `item` is not
  among them.

## 7. Gates

The pass adds no leg: PLAY-dOrderedCharter-19's `tags` leg runs the extractors and the check once its
build lands, and this unit's rows join it as data.

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `lexicon selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC6 · the playbook-render selftest runs `gov_tag.py --fixture` under each plant of S6, its failing case staged by the `policy-ns-word` and `loop-bad-seg` plants · none

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

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 18, the brief's shared interface I2 and
  owned-node table, scout B's row for cl-0103, and PLAY-dOrderedCharter-10 and -19 at base `ed497191`.

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-19's namespace registry and PLAY-dOrderedCharter-10's
extractor module, shape check and per-namespace join, all specced and DEFERRED to that build's run; the
key matcher is dGroundRules-2 S4's `read_catalogue_row`. `python tools/codebase-map/reuse_lookup.py
"register a tag namespace with an extractor and shape check"` ranked generic name stems (`check`,
`extract` in `tools/lexicon/lexicon.py`, `shape` in `tools/govkit/matrix.py`) and named no seam, which
is the expected answer: neither registry nor index exists at base (scout B: no
`tools/playbook/namespaces.toml`, no `tools/policy/`). The segment regex `[a-z0-9][a-z0-9-]*` exists at
`tools/roles/roles_lib.py:63-65`; PLAY-dOrderedCharter-19 S1 compiles its own `TAG_RE`, which this unit
uses. The recall probe returned this build's own brief row, scout B's row and PLAY-dOrderedCharter-10
S1-S3; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how are tag namespaces registered with extractors and shape checked" --terms "namespace registry extractor tag grammar seg shape check namespace word policy catalogue key"`
