# TOOL-dRankedPlan-11 — each role item's memory read set sized at Plan, as `id#tag` keys

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0379@f1807fe1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |

<!-- /gen:spec-records -->

## 1. Goal

A role's work order today names a static `reads:` key list per role file (`tools/roles/handoff.py`'s
`render_handoff`, :312), the same for every build, and nothing sizes what a role will read for the
build in hand. The memory structure research settled that each item declares its read set as
`id#tag` keys (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-memory-structure-b.md:126`),
and v2 made dTotalRecall this build's parent because "its read sets are dTotalRecall's keys"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:800`). This
unit gives the plan record (I3, TOOL-dRankedPlan-16) a `Read sets` field (shared interface I16): for
each role item after Plan, its memory read set as `id#tag` keys, each set budgeted for its role by
`check_read_set` (TOOL-dTotalRecall-9 S6) when the plan record is checked, so the sizes are known
before Design and a work order can be handed exactly those keys.

## 2. Scope (IN)

- **S1** — The field, I16's grammar: `- **Read sets:** <item tag>: <key>, <key>; <item tag>: none;
  …`, entries joined by `; `, keys by `, `, each key `<id>#<tag>` (PLAY-dOrderedCharter-24's `id#tag`
  form, its table at spec line 143), the id a record key `record show` resolves and the tag a
  section tag of that record's kind (TOOL-dTotalRecall-9 S1, S2). `none` is an item's empty set, and
  the whole field `none` declares every item's set empty, the value TOOL-dRankedPlan-16 S8 writes for a
  patch or repeat build, which never reaches Plan; it prints `read set — every role item: none`. The
  shape check in `tools/memory-tree/plan_fields.py` (TOOL-dRankedPlan-13 S1), listed in
  `FIELD_CHECKS` as `Read sets`, refuses a bare `<id>` with no `#<tag>` (a whole record is not a read
  set key), a malformed tag, a repeated item or a repeated key within one item, naming each. Observed
  by AC1.
- **S2** — The population. Unless the field is `none`, every role item of the loop definition after
  Plan carries exactly one entry: each row `read_items` returns (TOOL-dDeclaredLoop-12 S1) whose `actor` is `role:<role>` and
  whose `step` is neither `step.plan` nor `none`. The check refuses a missing item, an entry naming an
  item outside that set (a command item, a Plan item, an unknown tag), naming each. `plan_fields.py`
  imports `read_items` in process from the loop kit found through `backlog.resolve_kit_dir`
  (`tools/memory-tree/backlog.py:1758`); with no loop kit the check exits 2 naming it. Observed by AC2
  and AC6.
- **S3** — The size. For each entry with keys, the check calls `check_read_set(root, role, keys)`
  (TOOL-dTotalRecall-9 S6, in `tools/memory-tree/record_find.py`, imported within the kit), `<role>`
  read from the item's actor, and prints `read set — <item tag> · <role> · <bytes> B of <cap> B`.
  `memory.over-budget` decides what an over-budget set does, inside `check_read_set`: a refusal
  refuses this field naming the item, the role, the bytes and the cap; a report passes and prints
  the report's `memory over budget:` line; `off` passes. A key `record show` cannot resolve, or a
  superseded slice `memory.superseded-slices` refuses, refuses the field naming the key. This unit
  reads no policy key. Observed by AC3 and AC4.
- **S4** — The hand-down: `python tools/memory-tree/plan_fields.py reads <slug> <item tag>` prints
  the item's keys, one per line, nothing for `none`, and exits 2 for an item the field does not list,
  the list a work order's renderer passes as `render_handoff --read <key>` (TOOL-dTotalRecall-9 S8).
  Observed by AC5.
- **S5** — The declaration: one `requires_if` row on `tools/memory-tree/kit.toml`, `{ kit = "loop",
  why = … }`, in the shape of its `drift-audit` row (`tools/memory-tree/kit.toml:8`): a DECLARATION
  `govkit selfcheck` grades that selects no kit, naming `plan_fields.py`'s in-process `read_items`
  import and its exit 2 with no loop kit. NOT OBSERVED by a criterion: `govkit selfcheck` grades the
  row at the close.
- **S6** — The plants `reads-shape`, `reads-cover`, `reads-budget`, `reads-hand` and
  `reads-no-loop` join `plan_fields.py --fixture`, run by the `plan-fields selftest` leg
  TOOL-dRankedPlan-13 S10 adds, with a stub loop kit answering planted item rows. Observed by AC1 to
  AC6.
- **S7** — `help/plan.md`'s section "The plan record's intent fields" (TOOL-dRankedPlan-13 S11) gains
  `Read sets`: its grammar, which items carry one, the size line, and `reads`. Observed by AC7.

## 3. Non-goals (OUT)

- The read budget, `record show`, the section tags and the two keys `memory.item-budget` and
  `memory.over-budget`: TOOL-dTotalRecall-9's, called here.
- Rendering a work order and inlining slices: `render_handoff`'s `--read` (TOOL-dTotalRecall-9 S8),
  dBoundRoles' renderer and the executor. S4 hands them the keys.
- A static per-item read set in `tools/loop/loop.toml`: a read set is sized per build, at Plan (§8 F1).
- Plan's own role items, `item.plan.triage-judge`, `item.plan.record`, `item.plan.research` and
  `item.plan.reason`: they run before the plan record exists (§8 F3).
- The module, the leg and the plan-record schema check join: TOOL-dRankedPlan-13's, which this unit
  lists one more field in.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the plan record whose `Read sets` field this unit defines
- **consumes-from** `TOOL-dRankedPlan-13` — `plan_fields.py`, the module, its `FIELD_CHECKS` table, its fixture and the schema check join this unit's field rides
- **hands-off** `TOOL-dRankedPlan-12` — `requires_if`, the memory-tree kit's `loop` row S5 adds, whose `why` that unit extends with `probe.py`
- **consumes-from** external — dTotalRecall: `check_read_set`, `record show` and the section tags (TOOL-dTotalRecall-9 S1, S2, S5, S6); dDeclaredLoop: `read_items` and the item rows' `actor` and `step` (TOOL-dDeclaredLoop-12 S1, S2); the `id#tag` form (PLAY-dOrderedCharter-24); each DEFERRED at base and re-grounded on its landed code
- **hands-off** external — a work order's renderer reads `plan_fields.py reads` and passes each key as `render_handoff --read`; the caller that launches each item is dWellOiledMachine's executor

## 4. Design

### Evidence

- `render_handoff` (`tools/roles/handoff.py:312`) writes a static `reads:` list from the role file
  (:337); there are no per-build keys and no budget at base.
- `memory.item-budget` (`tools/policy/catalogue.toml:1428`, default `measured`) and
  `memory.over-budget` (:1434, `refuse`, `report`, `off`, default `report`) stand in the catalogue at
  base, owner dTotalRecall; their one reader is TOOL-dTotalRecall-9's `check_read_set`.
- `backlog.resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`) is the kit's sibling resolver,
  which the `drift-audit` and `unattended` rows of `tools/memory-tree/kit.toml:8` already declare
  in-process and subprocess reads through.
- TOOL-dTotalRecall-9's own fixture passes a bare id to `--read` (its AC8); the clause asks for
  `id#tag` keys, so S1 is stricter than the budget's own door.

### The field

```
- **Read sets:** item.design.unit-spec: TOOL-dX-1-plan#section.scope, DEC-dX-3#section.decision; item.build.unit-pass: none; item.test.reason: 2026-10-27-review-TOOL-dX-1-spec-audit#section.verdict
```

### The check, per entry

| Entry | Verdict |
|---|---|
| the whole field `none` | passes, `read set — every role item: none` |
| a key with no `#<tag>` | refused, `<key>: a read set key is id#tag` |
| an item outside S2's set, or a role item after Plan with no entry | refused, naming the item |
| keys within the role's budget | `read set — <item> · <role> · <bytes> B of <cap> B` |
| over budget under `refuse` | refused, naming item, role, bytes and cap |
| over budget under `report` | passes, the report line printed |
| a key `record show` cannot resolve | refused, naming the key |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `Read sets` | plan record field | none |
| `check_read_sets` | function in `plan_fields.py` | `py.function`, asked at the pass |
| `reads` | verb of `plan_fields.py` | none |
| `{ kit = "loop" }` | `requires_if` row | none |
| plants `reads-shape`, `reads-cover`, `reads-budget`, `reads-hand`, `reads-no-loop` | fixture cases | none |

### Migration

None: no plan record exists before TOOL-dRankedPlan-16 lands the kind.

### Rollout

Live at landing for every plan record checked after it.

### Files touched (estimate)

- `tools/memory-tree/plan_fields.py`: S1 to S4, S6's plants
- `tools/memory-tree/kit.toml`: S5's `requires_if` row
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`
- `help/plan.md`: S7

### Alternatives rejected

- **A loop-kit read verb by ask**, `loop_lib.py items` (the shape TOOL-dWitnessedBar-3 §8 F6 asks
  dDeclaredLoop for): a wait on another build for a read the kit's declared `requires_if` route gives
  now.
- **Parsing `tools/loop/loop.toml` here**: a second reader of the item rows beside `read_items`.

## 5. Production-readiness checklist

- security — read-only: the check reads records and the loop definition and writes nothing; a key is
  resolved only through `record show`, never opened as a path.
- perf / scale — one `check_read_set` call per role item after Plan, about fifteen per plan, each a
  slice-length read over the one index (TOOL-dTotalRecall-9 S4).
- error / empty / loading states — `none` is an item's empty set; no loop kit and an unresolved key
  each name their cause.
- observability — one size line per item, the report's line under `report`.
- risks — `check_read_set`'s return shape is re-grounded on TOOL-dTotalRecall-9's landed module, and
  the population follows whatever role items the loop definition holds at check time.
- testing — S6's five plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `python plan_fields.py --fixture --plant reads-shape` runs `check tFix --field "Read
  sets"` over `item.build.unit-pass: DEC-tFix-1; item.design.unit-spec: DEC-tFix-1#section.goal,
  DEC-tFix-1#section.goal`, it exits 1 naming `DEC-tFix-1` as not `id#tag` and the repeated key; over
  `item.build.unit-pass: none; item.design.unit-spec: DEC-tFix-1#section.goal` the shape passes, and
  over the whole field `none` the check exits 0 printing `read set — every role item: none`.
  Red when: a bare id or a repeated key passes, or the patch build's `none` is refused.
- **AC2** — When the plant `reads-cover` plants a stub loop definition holding the role items
  `item.design.unit-spec` and `item.build.unit-pass`, the Plan role item `item.plan.record` and the
  command item `item.plan.exit`, a field naming only `item.design.unit-spec` exits 1 naming
  `item.build.unit-pass`; one adding `item.plan.record: none` or `item.plan.exit: none` exits 1 naming
  that item; one naming both role items after Plan passes.
  Red when: a role item after Plan goes unsized, or a Plan or command item is admitted.
- **AC3** — When the plant `reads-budget` plants a record whose section is 130,000 bytes as the one
  key of `item.build.unit-pass` (actor `role:gov-builder`) with `memory.item-budget` at `96`, the
  check under `memory.over-budget = refuse` exits 1 naming `item.build.unit-pass`, `gov-builder`,
  `130000` and `96000`; under `report` it exits 0 printing `memory over budget: gov-builder 130000 B >
  96000 B`; under `off` it exits 0 printing the size line alone.
  Red when: a refused set passes, or a reported one refuses.
  fixture: `check_read_set` lands with TOOL-dTotalRecall-9; the plant sets the two keys in its policy
  file.
- **AC4** — When the same plant sets a key whose tag the record lacks, the check exits 1 naming that
  key; with a 2,000-byte section it prints `read set — item.build.unit-pass · gov-builder · 2000 B of
  96000 B`.
  Red when: an unresolved key passes, or no size is printed.
- **AC5** — When the plant `reads-hand` runs `reads tFix item.design.unit-spec`, it prints that item's
  two keys one per line; `reads tFix item.build.unit-pass` over `none` prints nothing and exits 0;
  `reads tFix item.test.reason`, unlisted, exits 2.
  Red when: a key is printed for a `none` set, or an unlisted item exits 0.
- **AC6** — When the plant `reads-no-loop` runs the check with no loop kit beside the memory-tree kit,
  it exits 2 naming the `loop` kit.
  Red when: the coverage half is skipped silently.
- **AC7** — When `grep -n "Read sets" plan.md` runs over the help page, it finds S7's text naming
  `id#tag` and `reads`.
  Red when: the page does not describe the field.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck`

New arm: tools/memory-tree/plan_fields.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the five `reads-*` plants under the `plan-fields selftest` leg, staged by a role item after Plan left out of the field · none

## 8. Open questions

- **F1 — Where does a read set live: the plan record, or a static field on each `loop.toml` item?**
  RESOLVED (agent, 2026-10-26, delegated): the plan record, rung 1: the clause sizes the set "at
  Plan", so it is per build, and a static item field would size every build's set alike, which is
  what `render_handoff`'s role-file `reads:` list already does. widens: none · relaxes: none
- **F2 — Does an over-budget set refuse the plan or only record it?** RESOLVED (agent, 2026-10-26,
  delegated): as `memory.over-budget` says, answered inside `check_read_set`, rung 1: TOOL-dTotalRecall-9
  S6 owns that key and its one reader, so this unit adds no second reader and passes the answer
  through. widens: none · relaxes: none
- **F3 — Which items carry a read set?** Options: (a) every role item after Plan; (b) only the items
  the planner chooses to list; (c) every role item, Plan's included. (b) loses the clause's "each role
  item"; (c) loses because Plan's own role items run before the plan record exists, so their sets
  cannot be sized at Plan. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, with `none` as a
  declared empty set. widens: none · relaxes: none
- **F4 — How does the memory-tree module read the loop definition?** Options: (a) `read_items` in
  process through `backlog.resolve_kit_dir`, declared by a `requires_if` row as the kit's
  `drift-audit` row declares its sibling read; (b) an ask to dDeclaredLoop for a `loop_lib.py items`
  verb; (c) parsing `loop.toml` here. (b) waits on another build; (c) is a second reader of the item
  rows. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, reuse of the kit's own declared route.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 11, research-memory-structure-b.md:126,
  v2:800, TOOL-dTotalRecall-9 S1, S2, S5, S6 and S8, TOOL-dDeclaredLoop-12 S1 and its data model,
  PLAY-dOrderedCharter-24's form table, and scout A's row 4.

## 10. Reuse audit

The seams extended: TOOL-dTotalRecall-9's `check_read_set` and `record show`, called and never
restated; TOOL-dDeclaredLoop-12's `read_items`, imported through the kit's own sibling resolver
`backlog.resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`, verified at base) under a `requires_if`
row shaped as `tools/memory-tree/kit.toml:8`'s; and TOOL-dRankedPlan-13's `plan_fields.py`, whose
`FIELD_CHECKS` table gains one entry. `python tools/codebase-map/reuse_lookup.py "budget the bytes of a
memory read set per item before a work order"` ranked name stems (`read`, `read_text`, `read_conf`,
`read_journal`); none budgets a read set, and no budget exists at base, which matches scout A's row 4:
`handoff.py`'s `reads:` list is static per role, parsed at :337 where scout A cites :336. The recall query returned scout A's row 4,
TOOL-dTotalRecall-9 S6 and the debt-fold review's note that the read-set keys are dTotalRecall's
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md:205`); no record
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is each role item's memory read set sized and budgeted at Plan" --terms "read set id#tag record show check_read_set memory.item-budget memory.over-budget work order reads plan.exit"`
