# PLAY-dOrderedCharter-35 — the overlay's row mechanism for every registered kind: adopter-segment tags, field patches, whole-row replacements, exclusions, row pins and stale rows

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 33 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0065@35e9932a whole
**Carries:** node:policy-key.instructions.exclude

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md) | research | PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

A repository changes one of gov's structured rows (an item, a role, a leg, any kind a later build
registers) the way it changes one of gov's instruction units: from its own row in its overlay, through a
typed and pinned edge, never by editing gov's row. This unit builds that mechanism once, for every
registered kind, and proves it on one fixture kind that names no later build's kind. Today the only
adopter override of a shipped artifact is `[[own]]`, a whole-file claim (`resolve_owned_rows`,
`tools/govkit/govkit.py:1551-1598`), and a repository row placed beside gov's either reds `unique` or is
lost at update (`gap-found-29`, closed with units 32 and 33).

## 2. Scope (IN)

- **S1** — The rows' home and origin. A registered kind's repository rows sit in the overlay
  `.governance/instructions.toml` (S14, unit 32's file and reader) as `[[<kind>]]` tables in the
  kind's shipped schema. Every row read from the overlay carries `origin` = the repository, derived
  from the file it was read from and never typed: a row typing any other `origin` is refused, naming
  the row. One reader, `read_overlay_rows` in `tools/playbook/overlay_rows.py`, reads them through unit
  32's overlay reader and parses no TOML itself. Observed by AC1.
- **S2** — `owned` admits the `adopter` segment. A repository row's tag sits in a registered namespace
  with `adopter` in the owner seat its kind's schema declares (`owner-seat`), so `role.adopter.<name>`
  and `item.<step>.adopter.<name>` are the repository's and never collide with a gov tag. The tags
  pack's `owned` arm (unit 19's, in `tools/playbook/gov_tag.py`) admits such a tag only on an
  overlay row, refuses it on any row gov's packs ship, and refuses an overlay row of a gov kind whose
  tag carries no `adopter` seat. Observed by AC2 and AC3.
- **S3** — Amend, as a field patch. An overlay row carrying an `amends` edge (S6) to
  `<tag>@<hash8>` names gov's row and changes only the fields it names: a set field takes `add` and
  `remove` lists, a scalar takes a value. Every field the patch leaves alone flows from gov's row as
  shipped. Observed by AC4.
- **S4** — Replace, as a whole row. An overlay row carrying a `supersedes` edge to `<tag>@<hash8>`
  answers to gov's tag in the composition, so every dependent naming gov's tag resolves to it.
  Observed by AC5.
- **S5** — Exclude, over every registered kind. `instructions.exclude`, this unit's policy key, takes
  `none` or a set of gov tags of any registered kind the overlay holds; each listed gov row is absent
  from the composition and its state reads `excluded`. A listed tag no registered kind holds is
  refused. The key is read through dGroundRules' one reader (`cl-dClosedLoop-0008`) once it lands, with
  the catalogue default `none` until then; its catalogue row carries v2:1245's values, default, a
  summary and a usage. Which exclusions are refused is unit 36's. Observed by AC6 and AC12.
- **S6** — Pins over a row's canonical form. A pin's `<hash8>` is S7's shared normaliser (unit 24's
  extraction of `derive_clause_hash`, `tools/memory-tree/design_lib.py:169-173`) applied to the row's
  canonical form (§4), so a reordering of keys or a re-wrap of a string is not a change. A pin missing
  its `@`, one with a malformed hash, and one matching no revision of gov's row are each refused.
  Observed by AC7.
- **S7** — Change records cover rows. The change record unit 15's `instructions.edit` writes (S12, S13)
  takes a row tag of any registered kind as its subject. Its `editorial` or `semantic` mark is unit
  33's classifier run over the two canonical forms, and its `successor` (a tag, a list for a split,
  `none` for an ending) re-points or orphans a patch edge: a renamed row's patch follows its successor
  and keeps its pin; a split or ended row orphans it, an orphaned amendment is held out of the
  composition and an orphaned whole-row replacement runs on its own, each filing an order. Observed by
  AC8 and AC11.
- **S8** — A semantic change acting on a row, as `instructions.stale` says. Behind a pin, gov's row
  changed by `semantic` records reads stale; behind `editorial` records only, the pin stands and
  nothing flags. Under `order` the patch is applied over gov's new row and an order is filed; under
  `warn` it is applied over gov's new row and the stale edge is printed and journaled with no order;
  under `refuse` the update is held until `instructions.edit` re-pins the edge. Under `order` and
  `warn` a patch that no longer applies (a patched field gov's new row lacks, or a composition that
  fails a check) is held and gov's row runs as shipped, the order or the warning saying why. Observed
  by AC9, AC10 and AC11.
- **S9** — Each gov row's state, from S22's closed set (`unchanged`, `amended`, `replaced`,
  `excluded`, `stale`, `orphaned`), returned by the composer for unit 34's delta report to print.
  Observed by AC13.
- **S10** — A kind's row schema, found through the kinds register. Unit 7's
  `tools/playbook/kinds.toml` `[[kind]]` row gains one optional key, `schema`, the path of the kind's
  row schema, written only by a kind whose rows an overlay may carry; the schema's `[kind]` table
  carries `name` and `owner-seat`, and its field declarations are unit 36's. A kind
  with no `schema` key holds no overlay rows, and an overlay table naming it is refused. Observed by
  AC1 and AC3.
- **S11** — The fixture kind, `tools/playbook/fixtures/row_kind.py`. It builds a scratch tree holding
  a namespace registry row for the namespace `fixture`, a kind schema declaring one set field, one
  constraint set field and one ordered scalar, a gov pack of three rows and an overlay, plants one
  case, composes, and prints each observation beside what the case expects. The kind names no later
  build's kind, and its schema is the one unit 36's planted reds reuse. Observed by AC1 to AC11 and
  AC13.
- **S12** — The page `help/overlay-rows.md`, linked from `help/README.md`: how a repository adds, amends,
  replaces and excludes a gov row, what a pin is, and what each `instructions.stale` value does to a row
  at update. Observed by AC14.

## 3. Non-goals (OUT)

- Any real kind's rows. Items, roles, workflows, lenses and legs register their kinds, schemas and
  composers in their own builds (dDeclaredLoop, dBoundRoles, dCalibratedLens, dWitnessedBar), and each
  plants its own reds there (flow-roles-adoption item 9). This unit ships the shared engine and one
  fixture kind.
- The row checks: the fixed set, the exclusion refusals and the widening classifier are unit 36's.
- The overlay file, its guarded home and its `repo.` prose units: unit 32's. Units' own pins and their
  `editorial`/`semantic` mark checks: unit 33's. The write door: unit 15's `instructions.edit`, the only
  command that writes an overlay row.
- The delta report's rendering at update: unit 34's. This unit returns each row's state as data.
- A build in flight moving to a new composition at its next step boundary (FA-7): dDeclaredLoop's
  position engine.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-32` — the overlay file `.governance/instructions.toml` and its one reader; without it there is no home for a repository row
- **consumes-from** `PLAY-dOrderedCharter-33` — the `editorial`/`semantic` classifier and the unit-level `instructions.stale` arms this unit runs over rows
- **consumes-from** `PLAY-dOrderedCharter-15` — the change record and `instructions.edit`, the one door that writes and re-pins an overlay row
- **consumes-from** `PLAY-dOrderedCharter-19` — the tag grammar, the namespace registry and the tags pack's `owned` arm this unit widens
- **consumes-from** `PLAY-dOrderedCharter-24` — the edge grammar and S7's shared pin normaliser
- **consumes-from** `PLAY-dOrderedCharter-7` — the kinds register a kind's schema is found through
- **hands-off** `PLAY-dOrderedCharter-36` — the row checks over the composition this unit produces, planted on the fixture kind `tools/playbook/fixtures/row_kind.py` builds
- **hands-off** `PLAY-dOrderedCharter-34` — printing each gov row's state from the S22 set in the update's delta report
- **consumes-from** external — dGroundRules' policy reader and catalogue (`cl-dClosedLoop-0007`, `cl-dClosedLoop-0008`); until they land `instructions.exclude` reads `none` and `instructions.stale` its default `order`
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 7, 21 and 60, which that batch unit corrects after this unit lands, each by the item its report id names
- **hands-off** `PLAY-dOrderedCharter-55` — AC14's pathspec, which unit 49 S24 corrects, is observed at `PLAY-dOrderedCharter-49`'s pass and recorded from that observation; this pass changes no code to satisfy it (round-2 id 2)

## 4. Design

### Data model

A repository row in the overlay, for a kind `fixture` whose schema declares `owner-seat = 1`:

```toml
[[fixture]]                                   # a new repository row
tag = "fixture.adopter.extra"
grants = ["read"]
ceiling = "low"

[[fixture]]                                   # a field patch of gov's fixture.alpha
tag = "fixture.adopter.alpha-tuned"
edges = "amends=fixture.alpha@1a2b3c4d"
add = { grants = ["write"] }
remove = { needs = ["fixture.beta"] }
ceiling = "high"

[[fixture]]                                   # a whole-row replacement of gov's fixture.gamma
tag = "fixture.adopter.gamma-own"
edges = "supersedes=fixture.gamma@5e6f7a8b"
grants = ["read"]
needs = []
ceiling = "low"
```

- `edges` is S6's one line, `type=target`; the pinned form `<tag>@<hash8>` is legal only for `amends`
  and `supersedes` (S6), and a row carries at most one of the two.
- `add` and `remove` are inline tables keyed by set fields the kind's schema declares; a key naming a
  scalar or an undeclared field is refused. A scalar key on a patch row is the new value.
- `origin` is not a key an author writes. `read_overlay_rows` sets it to `repository` on every row it
  returns; gov's composer sets it to the kit for gov's rows.

**Canonical form.** The row as JSON with keys sorted, set-valued fields sorted, compact separators and
`ensure_ascii=False`, each string value first folded by S7's whitespace rule, and the keys `edges`,
`add` and `remove` left out of gov's row (gov rows carry none). The pin is S7's normaliser over that
text, so it is one function and never a second hash.

**The composer.** `compose_rows(kind, gov_rows, overlay_rows, exclude, stale_mode, records)` in
`tools/playbook/overlay_rows.py` returns `(rows, states, held, stale, orders)`:

1. gov's rows minus every tag `exclude` lists, each such tag's state `excluded`;
2. each `supersedes` row in its target's place, answering to the target's tag, state `replaced`;
3. each `amends` row applied to its target: `add` is a set union, `remove` a set difference, a scalar
   a value, state `amended`;
4. each pin compared with the target's current canonical hash: equal, nothing; behind it with only
   `editorial` records between, nothing; behind it with a `semantic` record, the edge is stale and S8's
   arm for `stale_mode` runs, state `stale`;
5. a target whose change record names a successor tag re-points the edge to it, keeping the pin; one
   whose successor is a list or `none` orphans the edge, state `orphaned`;
6. every remaining gov row `unchanged`; every overlay row with no edge appended as the repository's own.

The composer reads gov's packs and the overlay at the landed revision, as every composer does
(flow-roles-adoption item 11), and returns data: it writes no file. Orders go through the outbox writer
`update` already uses (`write_row_order`, TOOL-dSafePassage-9 S4), called by the update handler unit 33
lands for units; that handler iterates every kind the kinds register lists, and a register listing no
row kind prints `0 row kinds registered` rather than nothing. The `warn` journal is the stale-edge
journal unit 33 writes for units, one line per edge, the row's tag in its subject field.

**The `owned` widening.** `owned` today asks whether a tag sits under a namespace its declaring
contract owns (systems `[design-tags]`, its row "an expansion declaring `item.build.x`"). It gains one
clause: a tag whose segment at the kind's `owner-seat` is `adopter` is owned by the repository, legal
only on a row `read_overlay_rows` returned, and a row from gov's packs carrying it reds. The segment
check reads the seat from the kind's schema, never a typed position, and `adopter` is never a
namespace word, so the tag grammar's first-segment rule stands (flow-roles-adoption `[renamed]`).

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `tools/playbook/overlay_rows.py` (module) | playbook kit | the lexicon's naming predicates |
| `read_overlay_rows`, `compose_rows`, `derive_row_canon`, `apply_row_patch` | that module | the lexicon's naming predicates |
| `tools/playbook/fixtures/row_kind.py` (fixture) | playbook kit | the lexicon's naming predicates |
| the `fixture` namespace and kind | the fixture's scratch tree only, never the product registry | none: the product's `namespaces.toml` gains no row |
| the `owner-seat` schema key | each kind's schema, read through the kinds register | none |
| `help/overlay-rows.md` | `help/` | none |

### Rollout

The mechanism lands dark: no real kind registers rows in this build, so the composer runs only on
the fixture kind and the update handler's iteration announces its empty population. Each later
build's kind arms it by registering its schema and its composer call.

### Files touched (estimate)

- `tools/playbook/overlay_rows.py` (new)
- `tools/playbook/fixtures/row_kind.py` (new)
- `tools/playbook/gov_tag.py` (unit 19's module; the `owned` arm)
- `tools/playbook/render_playbook.py` (its self-test arm)
- `help/overlay-rows.md` (new)
- `help/README.md`

The catalogue row for `instructions.exclude` goes into the catalogue file `cl-dClosedLoop-0007`
defines, whose path the build run re-grounds against the landed parent and adds to this unit's
`--dispatch --writes`.

### Alternatives rejected

- **A second guarded file for structured rows** (`.governance/flow.toml`): FA-1's second option, refused
  by the owner's answer, one file keeping one guard, one door, one report and one exclusion list.
- **A three-way merge of gov's row and the repository's edit**: IA-2's third option; a merge has no
  pin, so gov's later semantic change is invisible to it.
- **Text placement after gov's row** (the unit rule of `amends`): two rows under one tag red `unique`,
  so a row's amendment is a field patch (flow-roles-adoption, the two changes).

## 5. Production-readiness checklist

- security: the overlay is written only through unit 15's guarded command, and this unit adds no write
  path: the composer returns data and the fixture writes only its scratch tree under the run's scratch
  path. A typed `origin` is refused, so a repository row cannot pose as gov's.
- perf / scale: one pass per kind over its gov rows and overlay rows, one canonical hash per pinned
  target; no index and no git walk beyond the change records between a pin and its target's head.
- error / empty / loading states: an unknown kind, an unknown target tag, a malformed pin, a patch key
  the schema does not declare and a listed exclusion no kind holds each refuse naming the row; an
  empty overlay composes to gov's rows, every state `unchanged`.
- observability: every stale edge prints one line naming the row, the pin and the record; every held
  patch says why; the update handler prints its row-kind count, a zero included.
- risks: a later kind's schema declaring the wrong `owner-seat` admits a tag the repository should
  not hold; the `owned` arm's planted reds run on the fixture kind only until that build plants its
  own (`fixture-passes-by-finding-nothing`, `memory/gotchas/fixture-passes-by-finding-nothing.md`).
- testing: the fixture's plants of §6, run by AC1 to AC13 and the self-test arm of §7.
- migration: additive; no row exists to migrate.
- user docs: `help/overlay-rows.md` and its `help/README.md` line (S12).

## 6. Acceptance criteria

- **AC1** — When `python row_kind.py --plant add` runs, it exits 0, the
  composition holding gov's three rows unchanged and the overlay row `fixture.adopter.extra` with
  `origin` `repository`; with `--plant typed-origin` it exits 1 naming the row that typed `origin`.
  Red when: a row that types `origin = "playbook"` composes as gov's row.
- **AC2** — When `python row_kind.py --plant adopter-tag` runs, the `owned`
  arm passes the overlay row `fixture.adopter.extra`; with `--plant gov-adopter` (gov's pack shipping
  `fixture.adopter.x`) it exits 1 with a line naming `owned` and that tag.
  Red when: the `owned` arm admits the `adopter` seat on a row gov's pack ships.
- **AC3** — When `python row_kind.py --plant no-seat` runs (an overlay row
  tagged `fixture.extra`), it exits 1 naming `owned` and the row.
  Red when: an overlay row of a gov kind with no `adopter` seat composes.
- **AC4** — When `python row_kind.py --plant amends` runs, the composed
  `fixture.alpha` carries gov's `grants` plus `write`, gov's `needs` minus `fixture.beta` and
  `ceiling` `high`, and every other field byte-equal to gov's row; with `--plant amends-undeclared`
  (an `add` key the schema does not declare) it exits 1.
  Red when: a field the patch leaves alone differs from gov's, or `remove` is applied as `add`.
- **AC5** — When `python row_kind.py --plant supersedes` runs, the composition
  answers `fixture.gamma` with the overlay row's fields, and gov's `fixture.alpha`, whose `needs` names
  `fixture.gamma`, resolves that need to it.
  Red when: gov's `fixture.gamma` and the replacement both compose, or the dependent's need is
  unresolved.
- **AC6** — When `python row_kind.py --plant exclude --exclude fixture.beta`
  runs, `fixture.beta` is absent from the composition and its state line reads `excluded`; with
  `--exclude fixture.nowhere` it exits 1 naming the tag.
  Red when: an excluded row still composes, or a tag no kind holds is accepted silently.
- **AC7** — When `python row_kind.py --plant pin-reordered` runs (gov's row
  rewritten with its keys in another order and a string re-wrapped), it exits 0 and no edge reads
  stale; `--plant pin-no-at`, `--plant pin-bad-hash` and `--plant pin-unknown` each exit 1 naming the
  edge.
  Red when: a key reorder changes the pin, or a pin whose hash matches no revision of gov's row
  composes.
- **AC8** — When `python row_kind.py --plant renamed` runs, the patch edge
  follows the change record's successor and keeps its pin; with `--plant split` and `--plant ended`
  each edge reads `orphaned`, the orphaned amendment is out of the composition, the orphaned
  replacement composes on its own, and one order is filed per orphan.
  Red when: an orphaned amendment still applies, or an orphan files no order.
- **AC9** — When `python row_kind.py --plant semantic --stale order` runs, the
  patch is applied over gov's new row and one order is filed; with `--stale warn` the patch is
  applied, one stderr line and one journal line name the stale edge, and no order is filed; with
  `--stale refuse` it exits 1, the update held and the line naming the stale edge.
  Red when: any value leaves the stale edge silent, or `warn` files an order.
- **AC10** — When `python row_kind.py --plant vanished-field --stale warn`
  runs (gov's new row lacks the patched `ceiling`), the patch is held, gov's row composes as shipped
  and the warning names `ceiling`; with `--stale order` the same holds and the order says why.
  Red when: a patch of a vanished field is applied to a key gov no longer ships.
- **AC11** — When `python row_kind.py --plant editorial` runs (gov's row
  changed behind the pin by `editorial` records only), it exits 0, the pin standing and no edge stale.
  Red when: an editorial change flags the edge.
- **AC12** — When `git grep -n -e "instructions.exclude"` runs over the catalogue file the parent
  lands, the key's row carries `none` or a set of gov tags as its values, the default `none`, a summary
  and a usage.
  Red when: the key lands with no summary or usage, which `cl-dClosedLoop-0007`'s schema refuses.
  fixture: the catalogue's path is the parent's, re-grounded at the build run (§8 F4).
- **AC13** — When `python row_kind.py --plant states` runs, it prints one line
  per gov row and the six lines carry `unchanged`, `amended`, `replaced`, `excluded`, `stale` and
  `orphaned`, each once.
  Red when: a state outside S22's set is returned, or one of the six never appears.
- **AC14** — When `git grep -n -e "instructions.stale" -- overlay-rows.md help/README.md` runs, it
  finds the page's section on stale rows and the index line linking the page.
  Red when: the mechanism ships with no page under `help/`.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC13 · `run_selftest` runs the fixture over every plant of §6 and asserts each exit and line · none

## 8. Open questions

- **F1 — Where a kind declares its owner seat.** The clause says `owned` admits the `adopter` segment
  "in a registered namespace", and the seat moves per kind (`role.adopter.<name>` against
  `item.<step>.adopter.<name>`). Options: (a) an `owner-seat` key in each kind's schema; (b) the
  segment admitted anywhere in a tag; (c) a typed list of seat positions in `owned` itself. (b) admits
  `fixture.x.adopter` as the repository's and lets the segment drift; (c) is a closed table in code,
  which flow-roles-adoption item 12 refuses.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 3, the one option that both closes the seat per kind and lets a later kind declare its own. widens: none · relaxes: none
- **F2 — What a row's canonical form folds.** FA item 13: "its keys sorted and its values
  normalised". Options: (a) JSON, keys and set values sorted, each string through S7's whitespace
  fold; (b) the TOML text with whitespace folded; (c) a hash per field. (b) reads a key reorder as a
  change, and (c) is a second pin grammar beside S7's.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 1, v2's "pins over a row's canonical form" with the shared normaliser S7 names. widens: none · relaxes: none
- **F3 — Where the row half of the update's stale arms runs.** Options: (a) inside the update handler
  unit 33 lands for units, iterating every registered kind; (b) a second handler in `govkit.py` for
  rows; (c) only in each kind's composer, outside update. (b) is a second copy of the arms, and (c)
  never acts at update, which the clause names. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3,
  one handler and one journal for units and rows. widens: none · relaxes: none
- **F4 — The parent is unbuilt.** The catalogue row of S5 and the reader of both keys are
  dGroundRules' (`cl-dClosedLoop-0007`, `cl-dClosedLoop-0008`), and neither has landed. RESOLVED
  (agent, 2026-10-23, delegated): rung 1, v2's `[chain]` puts dGroundRules before this build; the
  build run re-grounds against the landed parent, spelling the catalogue file and the reader's call as
  the parent ships them, and the catalogue defaults stand until then. widens: none · relaxes: none
- **F5 — Whether the fixture's `fixture` namespace joins the product registry.** The tag check
  requires every tag to sit in a registered namespace. Options: (a) the fixture writes its own
  namespace registry row into its scratch tree; (b) a `fixture` row in `tools/playbook/namespaces.toml`.
  (b) ships a namespace no adopter uses and makes the clause's "naming no later build's kind" a row
  every adopter carries. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-55.

## 10. Reuse audit

No existing seam fits the row patch itself: `grep -rn "instructions.exclude\|policy.adopter" tools`
returns nothing at `ce13efbe`, and the only adopter override of a shipped artifact is `[[own]]`, a
whole-file claim graded in `resolve_owned_rows` (`tools/govkit/govkit.py:1551-1598`), which has no field
patch and no pin. The seams extended are other units' of this build: unit 32's overlay reader, unit
19's `owned` arm, unit 24's S7 normaliser extracted from `derive_clause_hash`
(`tools/memory-tree/design_lib.py:169-173`, verified: the first eight hex of SHA-256 over the text with
each whitespace run folded), unit 33's classifier and stale handler, and the outbox writer
`write_row_order` TOOL-dSafePassage-9 extracts. Per-field collection of defects follows `load_policy`
(`tools/roles/roles_lib.py:373`), which collects every defect and raises once. `reuse_lookup.py "apply
a field patch from an overlay row over a shipped registry row, add and remove on set fields"` ranked
name-token hits only (`rows`, `row`, `field`, `extract_row` in `tools/memory-tree/backlog.py`), none a
patch engine; the scout's row (`memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md:18`)
agrees, and its `load_policy` line number matches source. The recall probe returned the clause and its
design rows (flow-roles-adoption items 4 to 6 and 13) and DEPL-dCarriedReceipt-8, a merge result
stamped as gov's own and overwritten one update later, which is the loss a pinned patch exists to stop.

Recall terms used: `python tools/memory-recall/query.py "how does an adopter patch a shipped gov row without losing the change at update" --terms "overlay amends supersedes field patch pinned hash adopter row stale update order"`
