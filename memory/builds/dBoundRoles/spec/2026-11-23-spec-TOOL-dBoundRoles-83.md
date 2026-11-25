# TOOL-dBoundRoles-83 — the exclusion walk reads a requirer's member in its own spelling, an actor's `role:<slot>` and a grant's leg name, as the tag it names

**Status:** CLOSED · rev-1 · 2026-11-23 · node d · Tier-2 · base 318e20c9 · streams tooling · order 23 · closes TOOL-dBoundRoles-79

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 TOOL-dBoundRoles-95 |
| [2026-11-22-build-TOOL-dBoundRoles-83-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dBoundRoles-83-1-acceptance-ledger.md) | journal | — |
| [2026-11-23-build-TOOL-dBoundRoles-83-deviation-831.md](../build/2026-11-23-build-TOOL-dBoundRoles-83-deviation-831.md) | deviation | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-83-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-83-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-83-1-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-83-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-83-spec-brief.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-83-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md) | diff-review | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |

<!-- /gen:spec-records -->

## 1. Goal

The exclusion walk of `check_rows` refuses an `instructions.exclude` tag another active row holds in a
`needs`, `actor` or `grants` field, but it compares the field's members with the tag as written. An
item's `actor` spells `role:<slot>`, and a role's `gates` grant holds leg names, so an excluded role an
item acts through, and an excluded leg a role grants, pass unrefused. `TOOL-dBoundRoles-20` S7 (the
exclusion refusals, its §8 F8 (iv)) waits on that. This unit folds each member to the tag it names
before the compare, so both exclusions are refused naming their requirer.

## 2. Scope (IN)

- **S1** — The fold. `derive_ref_tag(value, legs)` in `tools/playbook/row_checks.py` reads one member of
  a ref field as a tag: a string `<seg>:<rest>`, `<seg>` one tag segment and `<rest>` holding no space,
  reads `<seg>.<rest>`; a string whose text before an optional trailing question mark is a key of
  `legs` reads that leg's tag; any other value reads as itself. Observed by AC1, AC2 and AC4.
- **S2** — The walk. `check_rows` (`tools/playbook/row_checks.py#check_rows`) compares each excluded tag
  with every member of a ref field folded by S1. Its red still names the excluded tag, the requirer's
  tag, the ref role and the field, and adds the member as spelled where it differs from the tag, so an
  item acting as `role:gov-builder` is named with that spelling.
  `check_rows` and `derive_row_composition` (`tools/playbook/overlay_rows.py#derive_row_composition`)
  each take `legs` as a new keyword argument defaulting to none, so every caller that passes none
  composes as today. Observed by AC1, AC2 and AC3.
- **S3** — The leg names. `read_leg_names(root)` in `tools/playbook/overlay_rows.py` returns `{name:
  tag}` for every row of the leg manifest `{prefix}/gate-legs.json` at HEAD carrying a string `name`
  and a string `tag`, read through `tree_lib.read_blobs_at` as `read_kind_source` reads a source; an
  absent or unparsable manifest reads empty. `derive_kind_composition`
  (`tools/playbook/overlay_rows.py#derive_kind_composition`) reads it only where an exclusion is set,
  as it reads the tag-valued policy, and hands it on. Observed by AC2.
- **S4** — The page. `help/overlay-rows.md`, the exclusion paragraph of "What you may not change, and
  how a widening is reported", says a requirer's member is read as the tag it names, `role:<slot>` as
  `role.<slot>` and a leg's name as its tag. Observed by AC5.

## 3. Non-goals (OUT)

- Declaring the refs. The item schema's `actor` carrying `ref = "actor"` is `TOOL-dBoundRoles-84`'s,
  and a role's `gates` carrying `ref = "grants"` is `TOOL-dBoundRoles-20` S5's. Until each lands, the
  walk reads no such field in gov's tree; this unit's criteria observe it in the fixture kind, whose
  `actor` and `grants` already declare their refs (`tools/playbook/fixtures/row_kind.py@6b997505:45-47`).
- The matrix arm, "every core item role acts in at least one core item", and the exclusion that leaves
  a role in no item: `TOOL-dBoundRoles-20` S7's.
- A tag-valued policy key's members, which are tags already and are compared as today.

`TOOL-dBoundRoles-20` consumes this unit through
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`, which binds the relation over
that spec: its S7 and AC7 read, over the composition, the walk that refuses an excluded `role.<slot>` an item's `actor`
names as `role:<slot>` and an excluded `leg.` tag a role's `gates` names by its leg name, each naming the requirer.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `4b7916726`, whose `tools/` tree equals base `318e20c9`'s:

- The walk is `refs = {f: d["ref"] ...}`, then for each excluded tag and each composed row, a red for
  each ref field where `tag in derive_set_value(row.get(f))` (`tools/playbook/row_checks.py#check_rows`):
  a compare of the tag with the members as written.
- An item's actor is spelled `role:<slot>`, for example `actor = "role:gov-orienter"` on
  `item.entry.orient` (`tools/loop/loop.toml`), and the role tag is `role.<slot>` (TOOL-dBoundRoles-14).
- A role's `gates` value is leg names, comma-separated, each optionally ending `?`, for example
  `gates: lexicon naming predicates?` (`tools/roles/agents/gov-builder.agent.md`), split as
  `tools/roles/roles_lib.py@2cf0952a:1463` splits it; the leg's tag is its manifest row's `tag`,
  `leg.lexicon.lexicon-naming-predicates` for that name (`tools/gate-legs.json`).
- The gap, probed in-process: `check_rows` over a scalar `actor` declaring `ref = "actor"`, a row
  holding `role:gov-builder` and `role.gov-builder` excluded returns no red; a set `gates` declaring
  `ref = "grants"` holding `lexicon naming predicates?`, with `leg.lexicon.lexicon-naming-predicates`
  excluded, returns no red.
- `instructions.exclude` holds every excluded tag of every kind, and `derive_row_composition` refuses
  only the tags whose first segment is the composed kind's word that gov ships no row for, so an
  excluded `role.` or `leg.` tag reaches the item kind's walk unrefused by that check.

### The fold

```python
def derive_ref_tag(value, legs):
    if not isinstance(value, str): return value
    head, colon, rest = value.partition(":")
    if colon and SEG_RE.fullmatch(head) and rest and " " not in rest:
        return f"{head}.{rest}"
    name = value[:-1] if value.endswith("?") else value
    return (legs or {}).get(name, value)
```

`SEG_RE` is the tag segment's pattern, `[a-z0-9][a-z0-9-]*`, which the module spells once beside the
function, since `row_checks` imports no `tag_index`. The fold reads a member; it never writes one, so
the composed rows keep their spelling.

### Inventory

Minted: `derive_ref_tag`, `read_leg_names`, the keyword `legs` of `check_rows` and
`derive_row_composition`, and the fixture plants `exclude-actor-spelled`, `exclude-leg-named` and
`exclude-leg-unnamed`. Each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at the pass.

### Migration

None: gov's `instructions.exclude` is empty, and with no exclusion set no member is folded.

### Rollout

Live at landing. Units 81, 82 and 84 hold the same order and write `tools/playbook/row_checks.py`,
`tools/playbook/fixtures/row_kind.py` or `tools/playbook/render_playbook.py`, so the declared write sets
intersect and `--dispatch` refuses a second pass while the first is open (M6 condition 1).

### Files touched (estimate)

- `tools/playbook/row_checks.py` (`derive_ref_tag`, the walk, the docstring)
- `tools/playbook/overlay_rows.py` (`read_leg_names`, `derive_kind_composition`, `derive_row_composition`)
- `tools/playbook/fixtures/row_kind.py` (a leg manifest in the plant's tree, the plants)
- `tools/playbook/render_playbook.py` (the selftest rows running the plants)
- `help/overlay-rows.md`

### Alternatives rejected

- **Rewriting the actor and grant spellings to tags.** Every reader of `role:<slot>` and of a `gates`
  name would move, across the loop and roles kits, for a compare one function makes.
- **A schema key naming the namespace a field's members spell.** It types beside each field what the
  member's own spelling and the leg manifest already say.

## 5. Production-readiness checklist

- security — narrows: an exclusion that left a requirer dangling now refuses; no write path changes.
- perf / scale — one manifest read per composition that sets an exclusion, and one dict lookup per
  member.
- error / empty / loading states — an absent manifest folds no leg name and the role fold still runs;
  a member that names nothing reads as itself and matches no tag it did not match before.
- observability — the red names the requirer and the member as spelled.
- risks — a value `<seg>:<rest>` of a non-tag kind, such as `command:test.select`, folds to
  `command.test.select`, which matches only an exclusion of that exact tag.
- testing — AC1 to AC5 by the fixture plants, a grep and the selftest arm of §7 at the close.
- migration — none.
- user docs — `help/overlay-rows.md` per S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/fixtures/row_kind.py --plant exclude-actor-spelled` runs, an
  overlay row `fixture.adopter.actor` holding `actor = "fixture:beta"` and `instructions.exclude`
  listing `fixture.beta`, it exits 1 with a `row-checks: red · exclude` line naming
  `fixture.adopter.actor`, its actor field and `fixture:beta`.
  Red when: the walk compares the member as written, so the exclusion composes.
- **AC2** — When the plant `exclude-leg-named` runs, its tree's leg manifest holding a row named
  `fixture leg` tagged `leg.fixture.fixture-leg`, an overlay row `fixture.adopter.granter` holding
  `grants = ["fixture leg?"]` and `leg.fixture.fixture-leg` excluded, it exits 1 naming
  `fixture.adopter.granter`, its grants field and `fixture leg?`.
  Red when: a leg name is not read as its manifest tag, or the trailing `?` defeats the lookup.
- **AC3** — When the existing plant `exclude-actor` runs, its member written as the tag
  `fixture.beta`, it still exits 1 naming `fixture.adopter.actor`; and `python
  tools/playbook/overlay_rows.py compose --kind item` in gov's tree prints the same `pins` as before the
  unit.
  Red when: the fold drops a member already spelled as a tag, or a composition with no exclusion moves.
  figure: DERIVED, the before-pins printed by the same command at the pass's parent commit.
- **AC4** — When the plant `exclude-leg-unnamed` excludes `leg.fixture.other`, a leg of its manifest
  no member names, it exits 0 and prints no `row-checks: red · exclude` line.
  Red when: the fold matches a member to a tag it does not name.
- **AC5** — When `grep -n "role:<slot>" help/overlay-rows.md` runs, it prints the exclusion paragraph's
  line naming the spelled member.
  Red when: the page does not say a spelled requirer counts.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC4 · the `exclude-actor-spelled`, `exclude-leg-named` and `exclude-leg-unnamed` plants of `tools/playbook/fixtures/row_kind.py`, staged by comparing members as written · none

## 8. Open questions

- **F1 — Where is a member read as a tag?** Options: (a) a fold in the walk, the leg names read from the
  manifest at HEAD; (b) a schema key per field naming the namespace its members spell; (c) the actor
  and grant spellings rewritten to tags across the loop and roles kits. (c) moves every reader of two
  other kits' spellings, a public surface beyond this ask (veto 2); (b) states twice what the member's
  spelling and the manifest already say. RESOLVED (agent, 2026-11-23, delegated): (a), rung 3.
  options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-23 · initial draft, from the brief
  `2026-11-23-prompt-TOOL-dBoundRoles-83-spec-brief` and the owner's ruling
  `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling`, closing `TOOL-dBoundRoles-79`.

## 10. Reuse audit

The seam extended is the walk of `tools/playbook/row_checks.py#check_rows` over its `ref` roles
`needs`, `actor` and `grants`, which gains a fold and no second walk; the leg names come from the one
manifest the `leg` namespace is minted from (`tools/playbook/namespaces.toml@e78d0b57:168`), read at
HEAD as `tools/playbook/overlay_rows.py#read_kind_source` reads a source, and the `role.` spelling from
the `role` namespace row. `python tools/codebase-map/reuse_lookup.py "refuse an exclusion while another
row names the excluded tag in its own spelling"` ranked `rows`, `read_rows`, `PolicyRefused` and
`OverlayRefused`, none a spelling fold, so no existing seam fits beyond the walk. The tag index's own
leg reader, `_read_leg_rows` in `tools/playbook/tag_index.py`, yields a row's tag and its JSON span and
not its name, and `row_checks` imports no `tag_index`, so `read_leg_names` reads the manifest itself.
The recall probe returned the ask `TOOL-dBoundRoles-79`, this unit's brief and the owner's ruling; none
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is an exclusion refused when an item names the excluded role as its actor" --terms "exclusion walk instructions.exclude requirer ref actor grants role:slot leg name gates check_rows"`
