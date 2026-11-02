# TOOL-dCalibratedLens-13 — the `lens` kind and namespace: gov's lenses tagged, a repository's lenses from its overlay, the fixed set with the five slots, and lens tags joined to the step gate

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 15 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0470@dfafc75a whole
**Carries:** node:tag-namespace.lens

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |

<!-- /gen:spec-records -->

## 1. Goal

A lens exists only as a literal in the review harness, so an adopter's lens has no home beyond per-call
notes (gap-review-17). TOOL-dFairHearing-13 moves gov's lenses into a catalogue, `tools/workflows/lenses.toml`;
this unit makes the `lens` a registered kind with its own namespace, as the flow adoption settled for
every row a repository may add (FA-1, FA-5; `2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`
items 1 to 3 and 9): gov's lenses tagged `lens.<key>`, a repository's lenses as `[[lens]]` rows of its
overlay chosen by `review.opt-in`, the kind's fixed set declared with the harness's five lens slots among
it, and lens tags joined to dSafePassage's step gate, so a gov lens cannot vanish from an adopter's
install without a change record naming its successor.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dFairHearing-13 (the
catalogue, `render_lenses.py` and the `LENS_SLOTS` count) and -3 (the opt-in swap and `OPTIN_LENSES`);
PLAY-dOrderedCharter-7 S4 and S7 (the kinds register and the record factory), -15 S7 (the change
record), -19 S2 (the namespace registry and `tag_index.py`), -35 S1 to S10 (the overlay's rows and a
kind's `schema` key) and -36 S1 to S7 (the fixed set and the exclusion refusals); TOOL-dDeclaredLoop-26
§8 F5 (the playbook kit's `compose` verb on `overlay_rows.py`); TOOL-dWitnessedBar-11 (`leg_factory.py
new`). The build run re-grounds on each and stops the unit when one is absent.

- **S1** — The namespace. A `[[namespace]]` row in `tools/playbook/namespaces.toml` in
  PLAY-dOrderedCharter-19 S2's shape: `ns = "lens"`, `owner = "dCalibratedLens"`, `layer =
  "layer.flow"`, `source` the `key` of each `[[lens]]` row of `tools/workflows/lenses.toml` and of the
  overlay `.governance/instructions.toml`, `extractor = "tag_index:extract_lens"`, `role = "describes"`.
  `extract_lens` in `tools/playbook/tag_index.py` yields `lens.<key>` for each gov row and
  `lens.adopter.<name>` for each overlay row, each tag derived by `derive_lens_tag` and never typed. Each
  tag addresses its row's `brief`, so a brief is an instruction unit a return or a finding can cite by
  that tag (§8 F1). Observed by AC1.
- **S2** — The kind. A `[[kind]]` row `kind.lens` in `tools/playbook/kinds.toml` (PLAY-dOrderedCharter-7
  S4): `owner = "dCalibratedLens"`, `binds = ["principle.p8"]`, `population = "python
  {prefix}/workflows/render_lenses.py members"`, `factory = "python {prefix}/workflows/render_lenses.py
  new"`, `gate = "lens kind fixtures"`, and `schema = "tools/workflows/lens-schema.toml"`
  (PLAY-dOrderedCharter-35 S10). `members` prints each composed row's tag, one per line. `new <name>`
  appends a gov `[[lens]]` row with `default_in = []` and `optin = false`, the state a lens holds until its
  losing test (TOOL-dFairHearing-13 §4); given `adopter.<name>` it writes nothing and prints the overlay
  row and the `instructions_edit.py` command that would add it, since `instructions.edit` is the one door
  to the overlay (PLAY-dOrderedCharter-15 S2). Observed by AC1.
- **S3** — The composition. `read_lens_composition(root, rev)` in `tools/workflows/render_lenses.py` returns
  gov's rows and the overlay's `[[lens]]` rows composed by `compose_rows` (PLAY-dOrderedCharter-35),
  which runs `check_rows` (PLAY-dOrderedCharter-36 S7), reached as the playbook kit's `compose` verb run
  as a subprocess found through the inline `resolve_kit_dir`, as TOOL-dBoundRoles-20 S3 reaches it; with
  the playbook kit absent it returns gov's rows and prints one note naming it. An overlay row's harness
  key is `adopter-<name>` (§8 F3), and the render fills `OPTIN_LENSES` (TOOL-dFairHearing-3 S6) from every
  composed `optin = true` row, the repository's included, so a repository lens can be swapped into a run.
  A repository row whose `default_in` is not empty is refused, exit 2, naming the row: a repository
  lens fills a slot only by a swap, never as a sixth default. Observed by AC2 and AC4.
- **S4** — The fixed set, declared in `tools/workflows/lens-schema.toml` in PLAY-dOrderedCharter-36 S1's
  grammar (§4 "The schema"), `owner-seat = "adopter"`: `key`, `brief` and `kinds` fixed by the renderer's
  parse; `default_in` fixed by `parser=tools/workflows/check-verifier-fanout.sh#LENS_SLOTS`, the five lens
  slots; `presets` open, widening on `add`; `optin` open, an ordered scalar `false` then `true`. An
  `amends` patch adding a literal to a gov row's `default_in` is the planted patch adding a sixth slot,
  refused by PLAY-dOrderedCharter-36 S3 naming the row, `default_in` and `LENS_SLOTS`. Observed by AC3.
- **S5** — `review.opt-in` chooses. Its value grammar is TOOL-dFairHearing-3 S9's, the key's owner: a
  map keyed by literal name whose values map an opt-in lens key to the default it replaces.
  `derive_opt_in_tags(value, rows)` in `render_lenses.py` returns the lens tag of every opt-in key the
  value names, through `derive_lens_tag`, refusing a key that names no composed `optin = true` row,
  naming `review.opt-in` and the key; a repository lens is chosen by naming its harness key,
  `adopter-<name>`. `check_opt_in_exclusions(rows, exclude, opt_in)`, called by `read_lens_composition`
  after the composition's checks as TOOL-dBoundRoles-20's `check_core_fields` is, refuses an
  `instructions.exclude` entry naming a tag `derive_opt_in_tags` returns, naming `review.opt-in`, the
  literal and the key: PLAY-dOrderedCharter-36 S4 compares a key's members with a tag verbatim and the
  map's members are no tags, so the rule lives here once (§8 F2). Observed by AC4 and AC5.
- **S6** — Lens tags joined to dSafePassage's step gate. A `[[class]]` row `lens` in
  `tools/govkit/surface-classes.toml` (TOOL-dSafePassage-10 S1): `reader =
  "{prefix}/workflows/render_lenses.py:read_lens_members"`, every gov row's `key` in `lenses.toml` at
  the tree it reads, empty where the file is absent (`tools/govkit/step_gate.py`'s reader contract,
  `:32-35`); `plant = "{prefix}/workflows/render_lenses.py:write_lens_plant"`, staging the removal of one
  gov row whose `default_in` is empty, so the render still fills every slot; `witness =
  "{prefix}/workflows/render_lenses.py:read_lens_successors"`, each key whose `lens.<key>` tag a change
  record (PLAY-dOrderedCharter-15 S7) ends with a `Successor` that is one tag, the record read through
  the change kind's reader of PLAY-dOrderedCharter-7 S7's factory, never a parser of this unit's. A lens
  tag that vanishes with no change record reds; one whose change record names its successor passes; one whose
  record says `Successor: none` reds. Observed by AC6.
- **S7** — The gate. The leg `lens kind fixtures`, made by `leg_factory.py new` (TOOL-dWitnessedBar-11)
  as a `[[gate_leg]]` row of `tools/workflows/kit.toml` rendered into `tools/gate-legs.json`, running
  `python {prefix}/workflows/render_lenses.py --fixture`, its `enforces` holding `principle.p8`
  (PLAY-dOrderedCharter-7 S5). The fixture, `render_lenses.py --fixture --plant <case>`, builds a scratch
  repository under `%TEMP%` with a short name holding gov's catalogue, a template and an overlay, and
  runs each case of §4 "The cases" against its expected observation. Observed by AC2 to AC5 and AC7.
- **S8** — The docs: `help/overlay-rows.md` (PLAY-dOrderedCharter-35's page) gains "Adding your own lens":
  the overlay row, its tag, how `review.opt-in` chooses it, and what is fixed; `help/step-gate.md`'s "How
  a class joins" names the `lens` class and its witness; `tools/workflows/README.md`'s catalogue section
  names the kind, the schema and the overlay key form. NOT OBSERVED by a criterion: prose, read by the
  closing review.

## 3. Non-goals (OUT)

- The catalogue, its six fields, its renderer and the slot count: TOOL-dFairHearing-13. The opt-in swap,
  `optIn` and `review_pin.py`: TOOL-dFairHearing-3. This unit composes rows into them and adds no field.
- Lens removal by a swap or by excluding a default, a freed slot filled by an opt-in, and turning a
  `review.opt-in` member into an `optIn` pair for a run: TOOL-dCalibratedLens-14.
- Lenses for Plan, Test, Deploy and Maintain and `review.<stage>.effort`: TOOL-dCalibratedLens-1.
- The row mechanism, the pins, `instructions.exclude`, the fixed-set and exclusion refusals and the
  widening classifier: PLAY-dOrderedCharter-35 and -36, called on one more kind and never re-specced.
- Re-rendering an adopter's harness when its overlay changes: the install's render, which reads the
  composition from S3 on each run.
- A repository lens's replay result: TOOL-dCalibratedLens-14 ("recording a replay result when one ran
  and never owing one").

### Edges

- **hands-off** `TOOL-dCalibratedLens-14` — `lens.<key>`, `derive_opt_in_tags` and the refusal of an exclusion of an opt-in key `review.opt-in` names, which a swap, an exclusion of a default and the slot an opt-in fills read
- **hands-off** `TOOL-dCalibratedLens-1` — `kind.lens` and the `lens` namespace, under which the stage lenses' rows are tagged
- **consumes-from** external — TOOL-dFairHearing-13 and -3, PLAY-dOrderedCharter-7 S4 and S7, -15 S7, -19 S2, -35, -36, TOOL-dDeclaredLoop-26 §8 F5's `compose` verb, TOOL-dWitnessedBar-11 and TOOL-dSafePassage-10 S1, each specced and unbuilt at base `8bec4cef` but the last, built

## 4. Design

### The namespace and kind rows

```toml
# tools/playbook/namespaces.toml
[[namespace]]
ns = "lens"
owner = "dCalibratedLens"
layer = "layer.flow"
source = "tools/workflows/lenses.toml and .governance/instructions.toml, the key of each [[lens]] row"
extractor = "tag_index:extract_lens"
role = "describes"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md"
join-armed-by = "dCalibratedLens"

# tools/playbook/kinds.toml
[[kind]]
tag = "kind.lens"
owner = "dCalibratedLens"
binds = ["principle.p8"]
population = "python {prefix}/workflows/render_lenses.py members"
factory = "python {prefix}/workflows/render_lenses.py new"
gate = "lens kind fixtures"
schema = "tools/workflows/lens-schema.toml"
```

P8 names a repository's "lenses" among the rows that live in its overlay and change gov's rows by the
same edges (v2's `[principles]`). The extractor sits in the playbook kit's `tag_index.py` beside the
other kinds' extractors, since the index runs it and reads the catalogue as data.

### The schema

```toml
# tools/workflows/lens-schema.toml
[kind]
name = "lens"
owner-seat = "adopter"                     # lens.adopter.<name>

[[field]]  key = "key"         shape = "scalar"  fixed-by = ["parser=tools/workflows/render_lenses.py#check_catalogue"]
[[field]]  key = "brief"       shape = "scalar"  fixed-by = ["parser=tools/workflows/render_lenses.py#check_catalogue"]
[[field]]  key = "kinds"       shape = "set"     fixed-by = ["parser=tools/workflows/render_lenses.py#check_catalogue"]
[[field]]  key = "default_in"  shape = "set"     fixed-by = ["parser=tools/workflows/check-verifier-fanout.sh#LENS_SLOTS"]
[[field]]  key = "presets"     shape = "set"     widens = "add"
[[field]]  key = "optin"       shape = "scalar"  widens = [false, true]
```

`brief` is fixed because a changed brief is a different lens: a repository adds its own row and swaps it
in. `default_in` is fixed because every default slot is one of the five a literal holds; the slot count
keeps its one home in the fan-out leg (TOOL-dFairHearing-13 §4), and the schema cites it rather than
restating it.

### The tag and the key

| Row | Catalogue key | Harness key | Tag |
|---|---|---|---|
| gov | `coherence` | `coherence` | `lens.coherence` |
| overlay | `security` | `adopter-security` | `lens.adopter.security` |

`derive_lens_tag(key, origin)` is the one derivation: the extractor, `members`, the step gate's reader
and `derive_opt_in_tags` all call it. TOOL-dFairHearing-13's `check_catalogue` gains one rule: a gov key
may not begin `adopter-`, so no harness key of the repository collides with one of gov's.

### The cases

| Case | Planted | Observed |
|---|---|---|
| `repository-swap` | an overlay row `security`, `optin = true`, `presets = ["unit-spec"]` | the rendered template's `OPTIN_LENSES` holds `key: 'adopter-security'` and `members` prints `lens.adopter.security` |
| `sixth-slot` | an overlay `amends` of `lens.coherence@<hash8>` with `default_in = { add = ["diff-review"] }` | the composition is refused naming `lens.coherence`, `default_in` and `LENS_SLOTS` |
| `adopter-default` | an overlay row with `default_in = ["unit-spec"]` | the render exits 2 naming the row |
| `exclude-opted` | `review.opt-in` mapping `adopter-security` to `coherence` under `unit-spec`, and `instructions.exclude = ["lens.adopter.security"]` | the composition is refused naming `review.opt-in`, `unit-spec` and `adopter-security` |
| `opt-in-unknown` | `review.opt-in` mapping `adopter-missing` to `coherence` | `derive_opt_in_tags` refuses naming `review.opt-in` and `adopter-missing` |

### Inventory

Minted: the `lens` namespace row; `extract_lens` (`tools/playbook/tag_index.py`); the `kind.lens` row;
`tools/workflows/lens-schema.toml`; in `tools/workflows/render_lenses.py` the verbs `members`, `new` and
`--fixture`, and the functions `read_lens_composition`, `derive_lens_tag`, `derive_opt_in_tags`,
`check_opt_in_exclusions`,
`read_lens_members`, `write_lens_plant` and `read_lens_successors`; the step-gate class `lens`; the leg
`lens kind fixtures`; the harness key form `adopter-<name>`. Each function was answered OK by
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this base.

### Migration

Additive. With an empty overlay the composition is gov's rows, so the rendered harness is byte-identical
to TOOL-dFairHearing-13's render. The step gate's `lens` class joins on its first landing and reads as
joining, never red, on that landing (`tools/govkit/step_gate.py:32-35`).

§6 runs a sibling's file by its basename: `gov_tag.py` is `tools/playbook/gov_tag.py` (TOOL-dBoundRoles-14 S5).

### Files touched (estimate)

- `tools/playbook/namespaces.toml` (S1)
- `tools/playbook/tag_index.py` (S1, `extract_lens`)
- `tools/playbook/kinds.toml` (S2)
- `tools/workflows/lens-schema.toml` (new, S4)
- `tools/workflows/render_lenses.py` (S2, S3, S5, S6, S7)
- `tools/workflows/kit.toml` (S7, the leg row)
- `tools/gate-legs.json` (S7, the render of the leg row)
- `tools/govkit/surface-classes.toml` (S6)
- `tools/govkit/selftest.py` (the arm in §7)
- `tools/workflows/README.md` (S8)
- `help/overlay-rows.md` and `help/step-gate.md` (S8)
- `help/reference/kinds.md` (the kinds register's page, re-rendered by `python tools/playbook/render_playbook.py --reference`)

## 5. Production-readiness checklist

- security — no new write path into the tree: the overlay is written only through `instructions.edit`,
  and `new` given an adopter name writes nothing. An overlay row's brief reaches the harness through the
  renderer's escape (TOOL-dFairHearing-13 §4), so a quote or a backslash in a repository's brief cannot
  break out of its string; the overlay's guard is the one door's.
- perf / scale — one `compose` subprocess per render and per `members`; the catalogue holds tens of rows.
- error / empty / loading states — the playbook kit absent: gov's rows and one note; the catalogue absent
  at a tree the step gate reads: an empty class there, joining; a refused composition: exit 2 naming the
  row, the field and the source, never a partial render.
- observability — `members` lists every tag with its origin derivable from the tag, and the update's
  delta report (PLAY-dOrderedCharter-34) lists each repository lens row as the repository's.
- risks — a harness key of the form `adopter-<name>` must pass TOOL-dFairHearing-3 S1's lens-key check
  for `optIn`; the arm in §7 runs the swap over stub agents to observe it, and a refusal there is a
  defect of this unit's key form, fixed here.
- testing — each criterion is a probe or a fixture of this unit's code; the arms in §7 are observed RED
  then GREEN by the main loop at the close.
- migration — §4 "Migration".
- user docs — `help/overlay-rows.md` and `help/step-gate.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python render_lenses.py members` runs over this tree after the build, it
  prints one `lens.<key>` line per `[[lens]]` row of `lenses.toml` and no other, and
  `python gov_tag.py show lens.coherence` resolves the tag to that row; `render_lenses.py
  new adopter.security` writes nothing and prints a `[[lens]]` row and an `instructions_edit.py` command.
  Red when: a tag is typed in a row instead of derived, or the factory writes the overlay.
  figure: DERIVED, the catalogue's row count at the run.
- **AC2** — When `render_lenses.py --fixture --plant repository-swap` runs, it exits 0 with the rendered
  `OPTIN_LENSES` holding `key: 'adopter-security'` and `members` printing `lens.adopter.security`.
  Red when: the render reads gov's catalogue alone, so the repository lens never reaches a run.
- **AC3** — When `--plant sixth-slot` runs, the composition is refused and the output names
  `lens.coherence`, `default_in` and `LENS_SLOTS`.
  Red when: `default_in` is declared open, so the patch composes a literal of six default slots.
- **AC4** — When `--plant adopter-default` runs, the render exits 2 naming the overlay row.
  Red when: a repository row takes a default slot.
- **AC5** — When `--plant exclude-opted` runs, the composition is refused naming `review.opt-in`,
  `unit-spec` and `adopter-security`; when `--plant opt-in-unknown` runs, `derive_opt_in_tags` exits 2
  naming `review.opt-in` and
  `lens.adopter.missing`.
  Red when: an exclusion of a lens `review.opt-in` names composes, or an unknown member is dropped.
- **AC6** — When `python tools/govkit/step_gate.py --fixture --plant lens` runs, it exits 1 with a
  `step-gate: RED lens:<key> vanished` line; with the plant's change record naming a successor tag
  committed beside it, it exits 0; with that record's `Successor` reading `none`, it exits 1.
  Red when: the class reads no change record, or reads `none` as a successor.
- **AC7** — When `python tools/govkit/step_gate.py --list` runs over this tree after the build, it prints
  the class `lens` with a member count equal to the catalogue's row count.
  Red when: the class row is missing or its reader returns nothing at the tip, which the gate refuses as
  an empty class.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures` · `govkit acceptance matrix` · `playbook render selftest` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `step-gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `lens kind fixtures` is new and not in the manifest at base; its arm is declared below.

New arm: tools/workflows/render_lenses.py · covers AC2 AC3 AC4 AC5 · the `--fixture` cases of §4 "The cases", each planting one overlay or policy row · none
New arm: tools/govkit/selftest.py · covers AC6 · the step gate's fixture planting a vanished gov lens, with and without a change record naming its successor · none
New arm: tools/workflows/tier2-review.test.sh · covers AC2 · the rendered fixture harness run over stub agents with `optIn` swapping `adopter-security` for a default, the stub recorder seeing that finder · none

## 8. Open questions

- **F1 — What makes a gov lens's brief a unit?** Options: (a) a `[[unit]]` row per brief in the workflows
  kit's `instructions.toml` (PLAY-dOrderedCharter-9 S1), the brief's text moved there; (b) the catalogue
  row as the unit, its tag `lens.<key>` addressing its `brief`, nothing copied; (c) a pointer unit per
  lens. (a) breaches the unit's `block` budget of 600 bytes for four of today's ten briefs, the spec
  briefs measuring 548 to 1,170 bytes in `tools/workflows/tier2-review.template.js:817-841` (measured
  2026-11-02 at base), and retires a field of TOOL-dFairHearing-13's schema; (c) is a second home for
  one fact. RESOLVED (agent, 2026-11-02, delegated): (b), rung 1: the flow adoption's item 3, "A lens is
  a catalogue row whose brief is a unit" (`flow-roles-adoption.md:169`). widens: none · relaxes: none
- **F2 — How does this unit read `review.opt-in`, and where is the exclusion of a lens it names
  refused?** TOOL-dFairHearing-3 S9, the key's owner, spells the value as a JSON map keyed by literal
  name; the landed catalogue row is a `set` of names (`tools/policy/catalogue.toml:418-422`), which
  TOOL-dDeclaredLoop-20 S2 reads one member per line; TOOL-dCalibratedLens-14 S2 and §8 F2 read the
  map. Options: (a) read the owner's map through one function, `derive_opt_in_tags`, and refuse the
  exclusion in a lens-kind check after the composition's, filing the grammar disagreement as an ask;
  (b) respell the value as a set of lens tags, so PLAY-dOrderedCharter-36 S4 refuses it verbatim, which
  loses the default each opt-in replaces and disagrees with TOOL-dCalibratedLens-14. RESOLVED (agent,
  2026-11-02, delegated): (a), rung 3, the option the sibling unit agrees with. The ask the main loop
  files in `memory/builds/dFairHearing/BACKLOG.md`: "`review.opt-in`'s value grammar is spelled twice,
  a JSON map in TOOL-dFairHearing-3 S9 and a set of names in `tools/policy/catalogue.toml:418-422`;
  accept one grammar both read, seen as `policy.py check` admitting a value `review_pin.py --opt-in`
  parses". widens: none · relaxes: none
- **F3 — How does a repository lens's harness key avoid gov's?** Options: (a) `adopter-<name>`, with gov
  keys refused that prefix; (b) `adopter.<name>`, widening TOOL-dFairHearing-13's key pattern to a dot.
  (b) changes the pattern every reader of a lens key (`LENS_KEYS`, `lensNotes`, the lens-yield table)
  already assumes. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Where do the step-gate class's reader, plant and witness live?** The brief places the reader in
  `step_gate.py`; the item, stage and leg kinds place theirs in their own kit's module
  (TOOL-dDeclaredLoop-24 S7, -25, TOOL-dWitnessedBar-28). Options: (a) `render_lenses.py`, the
  catalogue's module; (b) `step_gate.py`. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3: the class
  row's `<path>:<function>` form loads any module under the tool root (`step_gate.py:96-118`), and the
  catalogue's parse stays in one kit. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 13 (`cl-dClosedLoop-0470@dfafc75a`), the
  flow adoption's items 1 to 3 and 9 and FA-1 and FA-5, the brief's S7, TOOL-dDeclaredLoop-27 S1 and S2
  and TOOL-dBoundRoles-20 as the kind's templates, and the step gate, its class table and the policy
  catalogue read at base `8bec4cef`.

## 10. Reuse audit

The seams extended are the step gate's class table and its own-record witness, the shape
`read_fixture_successors` shows (`tools/govkit/surface-classes.toml`, `tools/govkit/step_gate.py:364`,
`:207`); the catalogue's renderer `render_lenses.py` and its `OPTIN_LENSES` token (TOOL-dFairHearing-13
S2, -3 S6); the kinds register and the namespace registry, in the row forms TOOL-dDeclaredLoop-27 and
TOOL-dBoundRoles-20 fill for the scenario, role and workflow kinds; and PLAY-dOrderedCharter-36's checks,
called on one more kind. `python tools/codebase-map/reuse_lookup.py "a class of adopter-visible members
whose vanish needs a change record naming a successor"` ranked name stems (`records`, `adopt`, `need`)
and runlog's record functions, and no step-gate reader; reading `step_gate.py` found the witness seam.
Where the brief and source disagree: the brief puts `read_lens_members` in `step_gate.py`, where every
sibling kind keeps its class functions in its own kit (§8 F4); TOOL-dFairHearing-3 S9 reads `review.opt-in` as a
JSON map, where the catalogue row is a set (§8 F2).

Recall terms used: `python tools/memory-recall/query.py "how does a repository add its own review lens and how is a gov lens retired" --terms "lens kind namespace review.opt-in overlay instructions.toml step gate surface class lenses.toml five slots fixed set"`

### Alternatives rejected

- **Briefs moved into `[[unit]]` rows** (F1 a). Rejected by measuring the spec literal's briefs against
  PLAY-dOrderedCharter-9 S1's `block` budget: four exceed 600 bytes.
- **A dotted harness key** (F3 b). Rejected by reading TOOL-dFairHearing-13 §4's `key` pattern,
  `^[a-z][a-z0-9-]*$`, and the readers it lists.
- **The generic `[[retired]]` row as the lens's witness.** Rejected by reading `write_witness_row`
  (`tools/govkit/step_gate.py:572-584`), whose `[[retired]]` row carries `successor = "none"` and still
  witnesses its member: it admits a vanish with no successor, which the clause reds.
