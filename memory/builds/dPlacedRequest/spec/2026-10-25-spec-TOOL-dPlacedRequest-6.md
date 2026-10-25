# TOOL-dPlacedRequest-6 — the items' declarations of the `map` slot and their unfolds

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 14 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0124@b8ada8e4 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

"An item declares its map slot and its unfolds"
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:530-531`): the
work order's `map` slot is filled for the items that declare it, and an item's unfolds list the
namespaces its slot spells out node by node (:593-597). v2's split gave this build "the `map` slot"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:506`) while
the slot's rendering stays dFurnishedOrders' `cl-dClosedLoop-0203`. No item declares either today.
This unit declares `map` on the role items the project map's delivery table names, `unfolds` on
`item.design.inventory`, and a check that each value is legal and each unfold names a registered
namespace.

## 2. Scope (IN)

- **S1** — The `map` declarations: `map = "base"` on the ten item rows of `tools/loop/loop.toml`
  (TOOL-dDeclaredLoop-12 S2) whose actor the delivery table gives the map
  (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:615-629`), as §4
  lists; every other row reads `none`, the unit workers among them, which "get no map". The field's
  schema row is TOOL-dPlacedRequest-8's (I15). Observed by AC1.
- **S2** — The unfolds: `unfolds = ["kit", "policy"]` on `item.design.inventory`, the registry words
  for the kits and the config keys the delivery table's architect row unfolds (:593-595); `kit` is
  PLAY-dOrderedCharter-10's row and `policy` TOOL-dDeclaredLoop-18's. The table's legs, checks,
  populations and markers have no registered namespace, and join the row when the build that
  registers each lands (§8 F2). Observed by AC1.
- **S3** — The check, `check_item_maps(items, namespaces)` in `tools/loop/loop_lib.py`, run by
  `loop_lib.py --check`, the `loop definition` leg's command: a `map` outside `none` and `base` is
  refused naming the item and the value; an `unfolds` on an item whose `map` is `none` is refused,
  since nothing renders the nodes it would list; and an unfold word that is no `ns` of a row of
  `tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19 S2) is refused naming the item and the
  word. The namespace words are read from that file through `resolve_kit_dir("playbook",
  "namespaces.toml", here)`, as PLAY-dOrderedCharter-10 S7's lexicon side reads them, since the loop
  kit imports no sibling. With no registry resolved, the namespace arm prints
  `unarmed — no namespace registry resolves` and the run is not green. Observed by AC2, AC3 and AC4.
- **S4** — The page `help/loop.md` gains a sentence on `map` and `unfolds` beside TOOL-dPlacedRequest-8's
  `seed` section. Observed by AC5.

## 3. Non-goals (OUT)

- The work order's `map` slot and its rendering: dFurnishedOrders' `cl-dClosedLoop-0203`, which reads
  these declarations; until dTotalRecall's renderer lands it renders "not installed".
- `memory.project-map` and `memory.map-unfold`: dFurnishedOrders' keys
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1373`,
  :1376), never read here. Which roles receive the slot under them is that build's join.
- `item.entry.orient`'s declaration: its row is TOOL-dPlacedRequest-3's, which declares `map` there
  from the field this build lands.
- The reviewer's `review.lens` and the reuse scout's house index: no `item.review.lens` row exists among
  dDeclaredLoop's rows (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md:84-86`),
  and the house index is dLinkedLibrary's; dFairHearing declares the lens's `map` when it lands that row.
- The schema rows for `map` and `unfolds`: TOOL-dPlacedRequest-8's one edit of the schema file.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-8` — `item-schema.toml`, whose `map` and `unfolds` rows the declarations here are values of
- **consumes-from** external — the namespace registry `tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19 S2) with its `kit` and `policy` rows (PLAY-dOrderedCharter-10, TOOL-dDeclaredLoop-18), and the item rows (TOOL-dDeclaredLoop-12)
- **hands-off** external — dFurnishedOrders' `map` slot (`cl-dClosedLoop-0203`) reads `map` and `unfolds`; each later build that registers a namespace the delivery table's architect row unfolds adds its word to `item.design.inventory`'s `unfolds`
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The declarations

| Item | Actor | `map` | `unfolds` |
|---|---|---|---|
| `item.plan.triage-judge`, `item.plan.reason` | planner | `base` | |
| `item.design.inventory` | architect | `base` | `kit`, `policy` |
| `item.design.decompose`, `item.design.reason` | architect | `base` | |
| `item.design.seams` | reuse scout | `base` | |
| `item.design.unit-spec`, `item.review.fold` | spec writer | `base` | |
| `item.plan.research`, `item.design.research` | researcher | `base` | |

PINNED 2026-10-25 from the delivery table and flow-steps' actors
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:183-245`, :575);
`loop_lib.py --check` re-derives the declared set at every run.

```toml
[[item]]
tag = "item.design.inventory"
map = "base"
unfolds = ["kit", "policy"]
```

### The check, in order

1. `map` in `none`, `base`, an absent field reading `none`.
2. `unfolds` empty unless `map` is `base`.
3. Each unfold word an `ns` of the registry, or the run unarmed when no registry resolves.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_item_maps` | function | `py.function`, OK |
| `map`, `unfolds` values on ten rows | data | none |

### Migration

None: no item row carries either field before this unit, and an absent field reads `none`.

### Rollout

Live at landing; the declarations stay inert until dFurnishedOrders' slot reads them.

### Files touched (estimate)

- `tools/loop/loop.toml`: `map` on ten rows, `unfolds` on one
- `tools/loop/loop_lib.py`: `check_item_maps`
- `help/loop.md`

### Alternatives rejected

- **Unfold words for legs, checks, populations and markers now.** No row registers them, and minting
  their names here would spell a later build's namespaces for it (§8 F2).
- **An unregistered unfold read as `unarmed`.** A misspelt word would then pass as merely early.

## 5. Production-readiness checklist

- security — declarations only; no write path.
- perf / scale — one registry read per check.
- error / empty / loading states — an absent registry prints `unarmed` and is not green; an absent
  field reads `none`.
- observability — each refusal names the item, the field and the value or word.
- risks — the architect's unfolds are two of the delivery table's six until the other namespaces are
  registered.
- testing — the plants of §6.
- migration — none.
- user docs — `help/loop.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs over the tree, it lists the ten items of §4 with
  `map base`, `item.design.inventory` with `unfolds kit, policy`, and every other item with
  `map none`.
  Red when: a delivery-table role item declares no map, or a unit worker declares one.
- **AC2** — When `python loop_lib.py --fixture --plant map-bad` plants `map = "full"`, `--check` exits 1
  naming the item and `full`.
  Red when: a value outside the two passes.
- **AC3** — When the plant `unfold-unregistered` plants `unfolds = ["legs"]` and the plant
  `unfold-no-map` plants `unfolds = ["kit"]` beside `map = "none"`, `--check` exits 1 naming each item
  and, for the first, the word `legs`.
  Red when: an unfold names no registered namespace, or unfolds stand without a map.
- **AC4** — When the plant `no-registry` hides `namespaces.toml`, `--check` prints
  `unarmed — no namespace registry resolves` and exits non-zero.
  Red when: an absent registry reads as every unfold registered.
- **AC5** — When `grep -n "unfolds" loop.md` runs in `help/`, it finds the sentence naming `map`'s two
  values and what an unfold lists.
  Red when: the fields land and the page does not name them.

## 7. Gates

`spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC2 AC3 AC4 · the `map-bad`, `unfold-unregistered`, `unfold-no-map` and `no-registry` fixture cases under the `loop definition` leg, the failing case staged by `unfold-unregistered` · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it.
  RESOLVED (agent, 2026-10-25, delegated): `OPEN`.
- **F2 — The delivery table's architect row unfolds legs, checks, config keys, populations, markers
  and kits; four of the six have no registered namespace. What does `item.design.inventory` declare?**
  Options: (a) the two registered words now, the rest added by the builds that register them; (b)
  invented words for the four, held on a pending list; (c) the six prose names, each unregistered word
  read as `unarmed`. (b) spells namespaces later builds own; (c) lets a misspelt word pass. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the survivor; `unfolds` widens by `add`
  (TOOL-dPlacedRequest-8 S1), so each later word is an additive change.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 6, the project map's `[tiers]` and
  `[delivery]` sections and v2:506.
- rev-2 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seams extended are the item rows of `tools/loop/loop.toml` (TOOL-dDeclaredLoop-12 S1), the field
rows TOOL-dPlacedRequest-8 lands in the item kind's schema, and the namespace registry
(PLAY-dOrderedCharter-19 S2), read the way PLAY-dOrderedCharter-10 S7's lexicon side reads it. Scout C
named the `reuse` task field (`TASK_FIELDS` at `tools/roles/handoff.py:97`) as where the slot will sit;
source agrees, and that slot is dFurnishedOrders'. `python tools/codebase-map/reuse_lookup.py "declare
per item which namespaces a work order's map slot unfolds"` ranked the map kit's internals (`map_root`,
`render_map_md`, `load_map_tree`), none declaring anything per item, so no existing seam holds the
declaration. Scout C's open point read `memory.project-map` as dBoundRoles'; v2:1373 gives it to
dFurnishedOrders, the later source, and this unit reads it from neither.

Recall terms used: `python tools/memory-recall/query.py "which items carry the map slot and what do they unfold" --terms "map slot unfolds item-declared design.inventory namespaces delivery project-map PM-6 item-schema widens"`
