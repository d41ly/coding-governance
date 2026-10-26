# TOOL-dFurnishedOrders-11 — the work order's memory, code-notes, legacy and house-index slots, each under its own budget and its own answer

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 14 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0202@504bb58f whole
**Carries:** node:policy-key.retrofit.slot-bytes
**Carries:** node:policy-key.roles.orientation.house-index

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

The work order's memory slices, code-notes slot and legacy slot, each under its own budget and its
own answer (systems `[cross]`), the legacy slot in its four states and capped by
`retrofit.slot-bytes`, the memory slices rendering "not installed" until dTotalRecall's section
extractors and `record show` land, and the reuse scout's house index handed first, as a pointer or
not at all as `roles.orientation.house-index` says, rendering "not installed" until dLinkedLibrary's
house index lands, each value seen on a planted work order. Today `render_handoff`
(`tools/roles/handoff.py:312`) renders no slot of any kind; the only absent-input line is
`Not supplied, optional:` (`:412-414`).

## 2. Scope (IN)

- **S1** — The memory slot, `### memory`, in every work order: `render_memory_slot` in
  `tools/roles/roles_lib.py`, through unit 4's `render_slot` (J4). It renders
  `not-installed: dTotalRecall's section extractors and record show have not landed` while no
  `record_find.py` resolves through `resolve_kit_dir("memory-tree", "record_find.py", KIT_DIR)`
  (TOOL-dTotalRecall-9 S5); once it resolves, the slot's body is TOOL-dTotalRecall-9 S8's `reads:`
  list, and `searched-empty` when the work order names no memory key. Its budget and its answer are
  `memory.item-budget` and `memory.over-budget`, run by S8's `gov_record.py budget`; this unit prices
  nothing a second time (D4). Observed by AC1.
- **S2** — The code-notes slot, `### code-notes`, in every work order but one whose
  `annotations.delivery` is `off`: `render_code_notes_slot(rows, rest)` in `roles_lib.py`, capped at
  2 KB, `CODE_NOTES_BYTES = 2048`, its rows cut by S5. With no rows source it renders
  `not-installed: no code-notes source; the tag's bundle fills this slot`. Unit 18 passes the rows,
  and under `off` does not call this renderer, so the order carries no `### code-notes` block
  (TOOL-dFurnishedOrders-18 S5 and its §8 F4 decide that value). Observed by AC2.
- **S3** — The legacy slot, `### legacy`, in the work order of each role whose role-index `writes` is
  `product` (`gov-builder` at base, `.claude/roles.json`): `render_legacy_slot` in `roles_lib.py`,
  counts per path and population for the item's write set, capped by `retrofit.slot-bytes` (`512`,
  `1024` or `2048`, default `1024`), in one of four states by §4 "The legacy states". The write set is
  the item's seed, TOOL-dPlacedRequest-8 S4's `resolve_item_seed` (J17), run as `loop_lib.py seed`
  in a subprocess; a seed that prints `unarmed — <source>: <why>`, or a work order naming no item,
  renders `not-installed` with that reason. Observed by AC3 and AC4.
- **S4** — The house index, `### house-index`, in the reuse scout's work order only
  (`gov-reuse-scout`), as `roles.orientation.house-index` says: under `handed` and `pointer` the
  block is the first block of `## Task` after its opening line, and renders `not-installed:
  dLinkedLibrary's house index has not landed (delivery <value>)`; under `off` there is no block.
  `render_house_index_slot` in `roles_lib.py`. Observed by AC5.
- **S5** — The cut: `derive_slot_cut(rows, cap, rest)` in `roles_lib.py`, keeping whole rows in order
  while the kept bytes plus the cut line stay within `cap`, then one line `… <n> row(s) past <cap> B:
  <rest>`, `rest` naming where the remaining rows are read. Rows past a cap are left to that reader
  (systems `[cross]`), never cut mid-row. Observed by AC2 and AC4.
- **S6** — The fourth state: `render_slot`'s closed state set gains `not-seeded`, written in the same
  grammar, `slot <point> · not-seeded: <why>` (J4). Observed by AC6.
- **S7** — The policy reads, J1: `retrofit.slot-bytes` and `roles.orientation.house-index` through the
  policy kit's `resolve(key, repo, rev)` (`tools/policy/policy.py:752`), the kit found by
  `resolve_kit_dir("policy", "policy.py", KIT_DIR)`; with no policy kit resolved, each reads its
  catalogue default (`1024`, `handed`) and the render's notes name the fallback. Observed by AC4 and
  AC5.
- **S8** — The docs: `help/roles.md` "How a task reaches an agent" (`:13-27`) names the four slots,
  their states and the two keys; `tools/roles/README.md`'s handoff section names the renderers.
  Observed by AC7.

## 3. Non-goals (OUT)

- Selecting memory sections and pricing them: TOOL-dTotalRecall-9 S5, S6 and S8, which hand keys with
  their bytes; inlining slice content is not this unit's either.
- Filling the code-notes slot from the tag's bundle and `annotations.delivery`: unit 18
  (`cl-dClosedLoop-0209`).
- The legacy ledger, its registrations and its rows: TOOL-dWitnessedBar-13. Draining the rows is the
  builder's pass, not the renderer's.
- The house index and the map it carries for the reuse scout
  (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:624`):
  dLinkedLibrary's, which has no spec. This unit renders the stand-in only.
- The `map`, `code`, `problems` and `bug-classes` slots: units 12, 17, 20 and 4.
- A catalogue row: both keys have one (`tools/policy/catalogue.toml:1386`, `:1548`).

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-4` — `render_slot`, the one renderer of a slot's head and state line, whose closed state set S6 extends with `not-seeded`
- **hands-off** `TOOL-dFurnishedOrders-18` — `### code-notes`, the slot, its 2 KB cap and `render_code_notes_slot`, which unit 18 fills from the tag's bundle as `annotations.delivery` says
- **hands-off** `TOOL-dFurnishedOrders-17` — `derive_slot_cut`, the whole-row cut unit 17 applies to the `code` slot under `memory.code-budget`
- **consumes-from** external — TOOL-dTotalRecall-9 S5 and S8 (`record show`, the `reads:` list), TOOL-dWitnessedBar-13 S1, S2 and S8 (the legacy ledger and its memory-tree copy), TOOL-dPlacedRequest-8 S4 (`resolve_item_seed`), TOOL-dBoundRoles-17 S1 (the `--item` flag naming the item a seed is resolved for); each absent at base, and its absence is this unit's `not-installed` state
- **hands-off** external — TOOL-dTotalRecall-9 S8 writes its `reads:` list as the body of `### memory`; dLinkedLibrary's house index fills `### house-index` and carries the map for the reuse scout
- **hands-off** `TOOL-dFurnishedOrders-29` — the legacy slot's seed, its two key reads and its ledger load, which unit 29 S10, S9, S6, S8 and S24 settle (ids 30, 16, 29, 27, 26, 57)

## 4. Design

### The blocks

```
## Task

This handoff is for build `tFix`, unit `TOOL-tFix-1`.

### house-index            <- gov-reuse-scout only, first, unless the key is off

slot house-index · not-installed: dLinkedLibrary's house index has not landed (delivery handed)

### input:question
…

### memory

slot memory · not-installed: dTotalRecall's section extractors and record show have not landed

### code-notes             <- absent under annotations.delivery = off

slot code-notes · not-installed: no code-notes source; the tag's bundle fills this slot

### legacy                 <- roles whose writes is product

slot legacy · filled
tools/roles/handoff.py · sh-hygiene 3 · encoding 1
… 4 row(s) past 1024 B: the rest in <the population's ledger at its home>
```

The slot blocks follow the `reads` blocks and precede the charter blocks, inside `## Task`, so the
marker's `task-sha` covers them (`handoff.py:417-421`). Each head is J4's, spelled once.

### The legacy states

| State | When |
|---|---|
| `not-installed: <why>` | no `legacy_ledger.py` resolves through `resolve_kit_dir("memory-tree", "legacy_ledger.py", KIT_DIR)`, its `read_registrations(root)` returns no population, or the seed is unarmed |
| `not-seeded: <population>,…` | a registered population has no ledger file at its `home`, so its check reads unarmed (retrofit.md:384), and no seeded population has a row under the write set |
| `searched-empty` | every registered population is seeded and none holds a row under the write set |
| `filled` | rows under the write set, one line per path, its populations and counts; an unseeded population is named on a last `not seeded: …` line |

The states follow `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md:380-385`.
The ledger module is loaded by file under its own name, the reach F3 of unit 10 records for a sibling
kit's module.

### The budgets, one key and one answer per slot

| Slot | Budget | Over it |
|---|---|---|
| memory | `memory.item-budget` | `memory.over-budget`, S8's |
| code-notes | 2 KB, no key | S5's cut, the rest left to the tag's query |
| legacy | `retrofit.slot-bytes` | S5's cut, the rest left to the population's ledger |
| house-index | none of its own | handed first, or a pointer, or nothing |

systems.md `[cross]` (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:208-220`):
"Each slot has one key and one answer when it runs over". A KB here is 1,024 bytes, as the slot keys
`memory.code-budget` and `memory.map-budget` read a `k`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_memory_slot`, `render_code_notes_slot`, `render_legacy_slot`, `render_house_index_slot` | functions, `roles_lib.py` | `py.function`, OK each |
| `derive_slot_cut` | function, `roles_lib.py` | `py.function`, OK |
| `CODE_NOTES_BYTES` | constant | no constant cell is declared |
| `not-seeded` | a member of `render_slot`'s state set | none |

### Migration

Additive: a work order gains blocks inside `## Task`, so its `task-sha` changes once at landing and
a handoff rendered before it is judged as before.

### Rollout

Live at landing; every slot but the legacy one renders its stand-in state until its source lands.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **A memory block of this unit's own beside S8's `reads:` list.** Two blocks for one slot, each
  priced differently: the shape D4 forbids.
- **The legacy slot in every work order.** systems `[cross]` lists legacy rows among a role item's
  slots, but retrofit's drain is the builder's (`retrofit.md:380-381`), and a role that writes no
  product code can drain nothing it is shown.

## 5. Production-readiness checklist

- security — no new write path: the slots render what the repository's own ledgers and kits hold,
  and a seed path outside the repository is the seed resolver's refusal, not this unit's.
- perf / scale — one subprocess for the seed and one file read per registered population; each slot
  is bounded by its cap.
- error / empty / loading states — the four legacy states, `not-installed` for every absent source,
  `searched-empty` never confused with not run.
- observability — each state line names its reason; the render's notes name a policy fallback.
- risks — the legacy ledger's reader is unbuilt; S3 is written to TOOL-dWitnessedBar-13's S1 and S2
  names, and §8 F4 says what the build run does if they differ.
- testing — AC1 to AC7 by a scratch adopter and planted stub kits; the arm of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md` by S8.

## 6. Acceptance criteria

- **AC1** — When `handoff.py render --role gov-spec-writer --build tFix --unit TOOL-tFix-1 --stdout`
  runs in a scratch adopter holding no `record_find.py`, `## Task` holds one `### memory` block whose
  state line reads `slot memory · not-installed:` naming `record show`; with an empty stub
  `record_find.py` planted in the scratch memory-tree kit, the line reads `slot memory ·
  searched-empty`.
  Red when: the slot is absent, so a missing memory source reads as a work order that needs none.
- **AC2** — When `python -c` calls `roles_lib.derive_slot_cut` on 40 rows of 100 bytes with cap
  2048, the result is at most 2048 bytes, ends with the line naming `row(s) past 2048 B`, and holds
  no partial row; and `render_code_notes_slot(None, None)` reads `not-installed`.
  Red when: a row is cut mid-line, or the cap is exceeded by the cut line.
- **AC3** — When the AC1 render runs for `gov-builder` with `--item item.build.unit-pass` over four
  planted fixtures, it renders `### legacy` as `not-installed` (no ledger module), `not-seeded`
  naming the population (a registration with no ledger file), `searched-empty` (a seeded ledger with
  no row under the seed's paths) and `filled` with `tools/roles/handoff.py` and its count (a row
  under them); for `gov-spec-writer` it renders no `### legacy` block.
  Red when: an unseeded population renders `searched-empty`, so an unarmed check reads as clean.
  fixture: stub `legacy_ledger.py` and `loop_lib.py` modules under the scratch adopter's kit dirs,
  written to TOOL-dWitnessedBar-13 S1, S2 and TOOL-dPlacedRequest-8 S4's names; the tree holds none.
- **AC4** — When the AC3 `filled` fixture holds 30 rows under the seed and a committed
  `.governance/policy.toml` sets `retrofit.slot-bytes` to `512`, `1024` and `2048` in turn, the
  slot's body is within that many bytes each time and its cut line names the value; with no policy
  kit resolved, the body is within 1024 bytes and the render's notes name the fallback.
  Red when: the key is ignored and every value cuts at one size.
  fixture: the policy file is committed in the scratch adopter, since `resolve` reads the landed
  revision.
- **AC5** — When the AC1 render runs for `gov-reuse-scout` with `roles.orientation.house-index` set
  to `handed`, `pointer` and `off` in turn, the first block after the opening line is `###
  house-index` reading `not-installed` and naming `handed`, then the same naming `pointer`, then no
  `### house-index` block at all; for `gov-spec-writer` no `### house-index` block renders under any
  value.
  Red when: `off` still renders a block, or the block sits after the `reads` blocks.
- **AC6** — When `python -c` calls `roles_lib.render_slot` with state `not-seeded` and a reason, the
  line reads `slot legacy · not-seeded: <reason>`; with a state outside the set it raises
  `RolesError` naming the state.
  Red when: an unknown state renders as if it were a fifth one.
- **AC7** — When `grep -n 'retrofit.slot-bytes' roles.md` and `grep -n 'house-index' roles.md` run
  in `help/`, each names its key and its values.
  Red when: the page describes a task with no slots.

## 7. Gates

`policy fixtures` · `roles adopter self-test` · `roles catalogue` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC3 AC5 · a scratch adopter rendering each slot over each planted source, and each `roles.orientation.house-index` value · none

## 8. Open questions

- **F1 — D4: one memory block or two?** TOOL-dTotalRecall-9 S8 already writes a `reads:` list on
  `render_handoff`. Options: (a) `### memory` is that list, rendered through `render_slot`, with this
  unit's `not-installed` state until S5 and S8 land; (b) a block of this unit's own beside it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "rendering not installed until
  dTotalRecall's section extractors and `record show` land" and the brief's D4; (b) gives one slot two
  budgets, which systems `[cross]` refuses. widens: none · relaxes: none
- **F2 — Whose work order carries the legacy slot?** Options: (a) every role's, as systems
  `[cross]` lists a role item's legacy rows; (b) the roles whose role-index `writes` is `product`,
  read off `.claude/roles.json` rather than a typed name, as retrofit's drain gives the slot to the
  builder (`retrofit.md:380-381`). RESOLVED (agent, 2026-10-26, delegated): (b), rung 1, the design
  line naming the slot's reader; (a) hands rows to roles that cannot drain them. widens: none ·
  relaxes: none
- **F3 — What is the legacy slot's write set?** Options: (a) the item's seed, J17's
  `resolve_item_seed`, whose `write-set` value is the unit spec's Files touched; (b) the spec's Files
  touched read by this unit directly. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the
  night pass's seed (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:207-208`)
  and J17, the one reader the brief fixes; (b) is a second reader of one fact. widens: none ·
  relaxes: none
- **F4 — The parents this unit calls.** Unit 4's `render_slot` (order 4) precedes it;
  TOOL-dTotalRecall-9, TOOL-dWitnessedBar-13, TOOL-dPlacedRequest-8 and TOOL-dBoundRoles-17's `--item`
  are DEFERRED at base, and dLinkedLibrary has no spec. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on
  `render_slot` and stops this unit if it is still absent then; each DEFERRED parent's absence is
  this unit's `not-installed` state, and where one has landed by the build run with names other
  than S1 to S3 cite, the build run re-grounds on its landed names and records the change as a rev
  bump with its §9 line, never a silent respelling. Rung 1, the build order the brief fixes.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 11, the brief's J1, J4, J15, J17 and
  D4, scout B's row 11, systems `[cross]`, retrofit `[drain]` and the source at `1a3ce03d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `render_handoff`'s `## Task` composition (`tools/roles/handoff.py:312-424`),
whose `Not supplied, optional:` line (`:412-414`) is today's only absent-input rendering; unit 4's
`render_slot`, the one state-line renderer, which S6 extends rather than copies; `resolve_kit_dir`
(`tools/roles/roles_lib.py:97`) and the load-by-file reach of `read_cap_answer` (`:136-158`) for the
memory-tree and loop kits' modules. `python tools/codebase-map/reuse_lookup.py "render an optional
work order slot with its own byte budget and a not installed state"` ranked name-stem noise
(`note`, `render`, `render_cards_md`, `derive_budget_cut` in `reuse_lookup.py`); `derive_budget_cut`
cuts a ranked list for the lookup's own output and is not a reachable library function of the roles
kit, so S5's cut is new. The recall probe returned this build's brief, scout B's row 11 and
TOOL-dTotalRecall-9's scout row; scout B cites `handoff.py:412-414` and `READ_KEYS` at
`roles_lib.py:36-40`, both matching source at `1a3ce03d`.

Recall terms used: `python tools/memory-recall/query.py "how does a work order hand memory slices,
code notes and the legacy slot under their own budgets" --terms "memory slices code-notes legacy slot
not-seeded retrofit slot-bytes house index reuse scout budget cross"`
