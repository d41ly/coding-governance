# TOOL-dFurnishedOrders-12 — the work order's `map` slot for the roles `memory.project-map` names, with each item's unfolds

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 15 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0203@325cbb22 whole
**Carries:** node:policy-key.memory.project-map
**Carries:** node:policy-key.memory.map-unfold

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |

<!-- /gen:spec-records -->

## 1. Goal

The work order's `map` slot for the roles `memory.project-map` names, with the unfolds each item
declares, none or all as `memory.map-unfold` says (PM-6), rendering "not installed" until
dTotalRecall's renderer lands. Today no work order carries the project map: `render_handoff`
(`tools/roles/handoff.py:312`) renders no slot, and `memory/map/generated/MAP.md` is the codebase-map
kit's dossier map, not the project map (scout B, row 12). The delivery the owner chose, PM-1's
"Structural roles (Recommended)", has no reader.

## 2. Scope (IN)

- **S1** — The role sets, J16: `derive_role_set(value, roles)` in `tools/roles/roles_lib.py`, over
  the values `structural-roles`, `every-role`, `working-roles` and `owner-only`, by §4 "The role
  sets". `structural-roles` and `working-roles` are the two rows of `ROLE_SETS`, declared once beside
  the function; `every-role` is every role of the role index whose `acts-as` is `item`
  (TOOL-dBoundRoles-1 S6); `owner-only` is the empty set. A value outside the four, or a declared
  slot no role file of `roles` holds, raises `RolesError` naming it. Observed by AC1.
- **S2** — Who gets the slot: `render_map_slot` in `roles_lib.py` renders `### map` (J4) in a work
  order when its role is in `derive_role_set` of `memory.project-map`, and, under
  `structural-roles`, the work order's item declares `map = "base"` (TOOL-dPlacedRequest-6 S1) or
  the work order names no item. Under `every-role` the item's `map` is not read; under `owner-only`
  no work order carries the slot. A role outside the set gets no block, as the delivery table's unit
  workers "get no map". Observed by AC2 and AC3.
- **S3** — The unfolds, PM-6, as `memory.map-unfold` says: `item-declared`, the item's `unfolds`
  list (TOOL-dPlacedRequest-6 S2), empty with no item; `none`, no unfold; `all`, every `ns` of the
  namespace registry `tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19 S2), read through
  `resolve_kit_dir("playbook", "namespaces.toml", KIT_DIR)`, and the unfold list `unarmed` with no
  registry resolved. Observed by AC4.
- **S4** — The body, through unit 4's `render_slot`: with the renderer resolved,
  `resolve_kit_dir("memory-tree", "gov_map.py", KIT_DIR)` (TOOL-dTotalRecall-14 S2), the slot is
  `filled` with `python gov_map.py`'s level 0 and then, per unfold in its declared order, `python
  gov_map.py <ns>`'s level 1, each run as a subprocess in the repository. With no renderer resolved,
  it renders `not-installed: dTotalRecall's renderer has not landed (unfolds: <list>)`, the list being
  S3's answer, `none` or `unarmed`, so each value of the key is visible before the map exists.
  Observed by AC4 and AC5.
- **S5** — The budget and its answer are the map's own: `memory.map-budget` and `memory.map-overflow`
  (TOOL-dTotalRecall-14 S6), applied by the renderer to level 0 (project-map.md:532-533, "its own
  budget and its own answer when it runs over"). An unfold is printed whole, as its item declared it.
  A renderer exit of 1 under `refuse` refuses the render, naming `memory.map-budget` and the
  renderer's line. Observed by AC5.
- **S6** — The policy reads, J1: both keys through the policy kit's `resolve(key, repo, rev)`
  (`tools/policy/policy.py:752`), found by `resolve_kit_dir("policy", "policy.py", KIT_DIR)`; with no
  policy kit, each reads its catalogue default (`structural-roles`, `item-declared`) and the render's
  notes say so. Observed by AC2 and AC4.
- **S7** — The docs: `help/roles.md` "How a task reaches an agent" (`:13-27`) names the `map` slot,
  which roles get it under each value and what an unfold adds; `tools/roles/README.md`'s handoff
  section names `derive_role_set` and `render_map_slot`. Observed by AC6.

## 3. Non-goals (OUT)

- The project map's renderer, its nodes, tiers, cache and budget: TOOL-dTotalRecall-14.
- The items' `map` and `unfolds` declarations and their check: TOOL-dPlacedRequest-6.
- The orientation scout's card cell: unit 13 (`cl-dClosedLoop-0204`). The reuse scout's map inside
  the house index: unit 11's slot and dLinkedLibrary's index.
- The map for the researcher and the prompt writer, and the `code` slot: unit 17
  (`cl-dClosedLoop-0208`), which extends the delivery this unit renders.
- The owner's session loading the map (`memory.default-load`, PM-7): dWellOiledMachine's.
- A catalogue row: both keys have one (`tools/policy/catalogue.toml:1446`, `:1464`).

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-4` — `render_slot`, the head and state line `### map` renders through
- **hands-off** `TOOL-dFurnishedOrders-17` — `derive_role_set`, which unit 17 reads for `memory.code-roles` and whose `structural-roles` row it extends with the researcher
- **consumes-from** external — TOOL-dBoundRoles-1 (the roster's slots and `acts-as`), TOOL-dBoundRoles-3 S1 (the item's declaration at render), TOOL-dPlacedRequest-6 S1 and S2 (`map`, `unfolds`), TOOL-dTotalRecall-14 S2 and S6 (`gov_map.py` and its budget), PLAY-dOrderedCharter-19 S2 (`namespaces.toml`); DEFERRED at base
- **hands-off** external — TOOL-dTotalRecall-14's renderer fills the slot this unit declares; its §3 line 96 and PLAY-dOrderedCharter-17:72 give the delivery to dBoundRoles, which the clause gives here

## 4. Design

### The role sets

| Value | Members | Source |
|---|---|---|
| `structural-roles` | `gov-orienter`, `gov-planner`, `gov-architect`, `gov-spec-writer`, `gov-reviewer` | PM-1, `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:400`: the orientation scout, planners, architects, spec writers, and the coherence and reuse lenses |
| `working-roles` | `gov-spec-writer`, `gov-builder`, `gov-tester`, `gov-researcher`, `gov-architect`, `gov-reviewer` | v2:1366, the prompt writer reaching its slots through its actor |
| `every-role` | every role of `.claude/roles.json` whose `acts-as` is `item` | TOOL-dBoundRoles-1 S6 |
| `owner-only` | none | v2:1373 |

The two typed rows are PINNED 2026-10-26 from those lines; `derive_role_set` re-checks every member
against the role files at each call, so a slot renamed in the roster refuses rather than silently
matching nothing. A `cycle` role, the prompt writer, is in no set: it frames a destination's work
order, whose slots are the destination's (TOOL-dBoundRoles-4 S1).

### The slot

```
### map

slot map · not-installed: dTotalRecall's renderer has not landed (unfolds: kit, policy)
```

and, with the renderer:

```
### map

slot map · filled
map 3f2a… · nodes 412 · lines 96 · folded legs,checks
…level 0…

#### kit
…level 1 of kit…
```

The block sits inside `## Task` with the other slot blocks, so the `task-sha` covers it, as
project-map.md:632-633 requires ("The slot is hashed with the work order").

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_role_set` | function, `roles_lib.py` | `py.function`, OK |
| `render_map_slot` | function, `roles_lib.py` | `py.function`, OK |
| `ROLE_SETS` | constant, `roles_lib.py` | no constant cell is declared |

### Migration

Additive: a structural role's work order gains one block inside `## Task` and its `task-sha` moves
once at landing.

### Rollout

Live at landing; the slot renders `not-installed` until TOOL-dTotalRecall-14 lands its renderer.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **The role sets read off `layer` alone**, J16's wording: every core role carries `layer.roles`
  (§8 F1), so the field cannot tell a structural role from a working one.
- **The item's `map` alone deciding.** It cannot express `every-role` or `owner-only`, so two of the
  key's three values would read nothing.

## 5. Production-readiness checklist

- security — no new write path; the map is derived from the repository's own index and handed to
  roles that could read it anyway.
- perf / scale — one renderer subprocess per work order and one per unfold; the renderer caches by
  tree (TOOL-dTotalRecall-14 S7), and level 0 is held to `memory.map-budget`.
- error / empty / loading states — `not-installed` with its unfold list; `unarmed` unfolds with no
  registry; a renderer refusal refuses the render by name.
- observability — the state line names the unfolds a role would get, and the render's notes name a
  policy fallback.
- risks — `structural-roles` names slots TOOL-dBoundRoles-1 creates; until they exist the set
  refuses, which §8 F4 settles.
- testing — AC1 to AC6 by a scratch adopter with a planted index, item rows and stub renderer; the
  arm of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md` by S7.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.derive_role_set` over a planted role index for each of
  the four values, it returns the five `structural-roles` slots, the six `working-roles` slots, every
  index role whose `acts-as` is `item` and the empty set; with the value `some-roles`, or with
  `gov-planner` removed from the planted role files, it raises `RolesError` naming the value or the
  slot.
  Red when: a declared slot missing from the roster matches nothing silently.
- **AC2** — When `handoff.py render --stdout` runs in a scratch adopter for `gov-spec-writer` and
  for `gov-builder`, with a committed `.governance/policy.toml` setting `memory.project-map` to
  `structural-roles`, `every-role` and `owner-only` in turn, the spec writer's `## Task` holds `###
  map` under the first two and not the third, and the builder's holds it under `every-role` only.
  Red when: a unit worker gets the map under the default, or `owner-only` still hands one.
  fixture: the policy file is committed, since `resolve` reads the landed revision.
- **AC3** — When the AC2 render for `gov-spec-writer` under `structural-roles` names an item whose
  planted declaration carries `map = "none"`, no `### map` block renders; with `map = "base"`, it
  renders.
  Red when: the item's declaration is ignored, so the reviewer gets the map under every lens.
- **AC4** — When the AC2 render for `gov-spec-writer` names an item declaring `unfolds = ["kit",
  "policy"]` and no `gov_map.py` resolves, with `memory.map-unfold` set to `item-declared`, `none`
  and `all` in turn, the state line reads `not-installed` and names `(unfolds: kit, policy)`, then
  `(unfolds: none)`, then every `ns` of a planted `namespaces.toml`; with no registry planted, `all`
  names `unarmed`.
  Red when: `all` and `item-declared` render the same list.
- **AC5** — When a stub `gov_map.py` that prints a header line for no argument and a `#### <ns>`
  block for one argument is planted in the scratch memory-tree kit, the AC4 render under
  `item-declared` reads `slot map · filled` with the header first and the `kit` then `policy` blocks
  after it; with the stub exiting 1 and printing a budget line, the render exits 1 naming
  `memory.map-budget`.
  Red when: the unfolds render before level 0, or a refused map is handed anyway.
- **AC6** — When `grep -n 'memory.project-map' roles.md` and `grep -n 'memory.map-unfold' roles.md`
  run in `help/`, each names its key and its values.
  Red when: the page says nothing of which roles get the map.

## 7. Gates

`policy fixtures` · `roles adopter self-test` · `roles catalogue` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/adopt-roles.test.sh · covers AC2 AC4 · each `memory.project-map` and `memory.map-unfold` value rendered over a planted index, item and registry · none

## 8. Open questions

- **FACT-QUESTION · F1 — Can TOOL-dBoundRoles-1's `layer` tell the structural roles from the
  working ones, as J16 words it?** Probe: `sed -n 120,134p` over
  `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`, counting the roster rows
  carrying `layer.roles` and `layer.runtime`. Observation, run 2026-10-26: 12 rows carry
  `layer.roles`, the twelve core roles, structural and working alike; 1 carries `layer.runtime`
  (`gov-session`). Liveness: the second count is 1, so the probe sees a row whose layer differs.
  RESOLVED (agent, 2026-10-26, delegated): it cannot; the sets are declared, F2. Rung 2. widens:
  none · relaxes: none
- **F2 — Where are the two typed sets declared?** Options: (a) `ROLE_SETS` in `roles_lib.py`
  beside `derive_role_set`, every member re-checked against the role files at each call; (b) a
  per-role field in TOOL-dBoundRoles-2's `role-schema.toml`, rendered into the role index, which is
  unbuilt at base and touches every role file. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  tie-broken by fewer open questions: it waits on no unbuilt schema, and the both-ways check keeps
  it from drifting from the roster. J16's `layer` wording is respelled as `acts-as` for `every-role`
  only, the one value the roster's fields can derive. widens: none · relaxes: none
- **F3 — How do the item's `map` and `memory.project-map` combine?** TOOL-dPlacedRequest-6 §3 leaves
  "which roles receive the slot under them" to this build. Options: (a) the role set alone; (b) the
  role set, and under `structural-roles` the item's `map = "base"` as well, the role set alone when
  no item is named; (c) the item's `map` alone. (c) fails AC2's `every-role` and `owner-only` cases
  (veto 1); (a) hands the reviewer the map under every lens, where PM-1 names only the coherence and
  reuse lenses. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most feature-rich
  survivor. widens: none · relaxes: none
- **F4 — The parents this unit calls.** Unit 4's `render_slot` (order 4) precedes it;
  TOOL-dBoundRoles-1 and -3, TOOL-dPlacedRequest-6, TOOL-dTotalRecall-14 and PLAY-dOrderedCharter-19
  are DEFERRED at base. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on
  `render_slot` and on TOOL-dBoundRoles-1's slots and `acts-as`, and stops this unit if any is still
  absent then, since `derive_role_set` refuses a set naming a missing slot; the renderer's absence
  is the `not-installed` state, an absent item field reads `none` as TOOL-dPlacedRequest-6's
  Migration states, and an absent registry is `unarmed`. Rung 1, the build order the brief fixes.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 12, the brief's J1, J4, J16 and D2,
  scout B's row 12, project-map.md PM-1, PM-6 and `[delivery]`, and the source at `1a3ce03d`.

## 10. Reuse audit

The seams extended: `render_handoff`'s `## Task` composition (`tools/roles/handoff.py:312-424`);
unit 4's `render_slot`; `load_roles` (`tools/roles/roles_lib.py:355`) and the role index
`render_roles_index` writes (`tools/roles/render_agents.py:207`), which `every-role` reads; and
`resolve_kit_dir` (`roles_lib.py:97`) for the renderer, the registry and the policy kit. `python
tools/codebase-map/reuse_lookup.py "hand a role the project map for the roles a policy key names"`
ranked name-stem noise (`key`, `map_root`, `render_map_md`, `load_policy`); `render_map_md` renders
the codebase-map kit's dossier map, not the project map, and no role-set reader exists, so
`derive_role_set` is new. The recall probe returned scout B's row 12, the packet's policy rows and
TOOL-dPlacedRequest-6's scout row, whose brief line calls both keys dBoundRoles'; that spec's own §3
names them this build's, matching the catalogue (`tools/policy/catalogue.toml:1446-1449`,
`:1464-1467`).

Recall terms used: `python tools/memory-recall/query.py "which roles receive the project map slot
and its unfolds" --terms "project map slot structural roles map-unfold unfolds item-declared PM-6 PM-1
gov_map renderer"`
