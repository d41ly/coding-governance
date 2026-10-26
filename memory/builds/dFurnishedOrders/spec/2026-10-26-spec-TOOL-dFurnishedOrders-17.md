# TOOL-dFurnishedOrders-17 — the `code` slot rendered per item from its declared seed, as ranges under `memory.code-budget`

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 16 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0208@b6c1dedb whole
**Carries:** node:policy-key.memory.code-budget
**Carries:** node:policy-key.memory.code-roles

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |

<!-- /gen:spec-records -->

## 1. Goal

The `code` slot rendered per item from its declared seed: the seed's definitions with their ranges,
their callers, callees and tests and their kit's siblings, as ranges under `memory.code-budget`, for
the roles `memory.code-roles` names, with the map's delivery extended to the researcher and the
prompt writer, rendering "not installed" until dTotalRecall's `code` record lands (night pass, point
3). Today no work order carries code (gap-roles-22): the spec writer and the builder get no
neighbourhood of the code their unit changes, and the researcher and the prompt writer get no map.
On the replayed dispatch the night pass measured, a one-hop neighbourhood of 5 KB held 16 of the 20
files the spec writer read and all 12 of the builder's
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:211-212`).

## 2. Scope (IN)

- **S1** — Who gets the slot: `render_code_slot` in `tools/roles/roles_lib.py` renders `### code`
  (J4) in a work order whose role is in `derive_role_set` (unit 12, J16) of `memory.code-roles`
  (`working-roles`, `every-role` or `structural-roles`, default `every-role`); a role outside the set
  gets no block. Observed by AC1.
- **S2** — The seed, J17: TOOL-dPlacedRequest-8 S4's `resolve_item_seed`, run as `loop_lib.py seed
  <item> --build <slug> --unit <id>` in a subprocess of the loop kit found by `resolve_kit_dir("loop",
  "loop_lib.py", KIT_DIR)`; its paths are the seed, and its line `unarmed — <source>: <why>`, a
  missing loop kit or a work order naming no item renders `not-installed` with that reason.
  Observed by AC2.
- **S3** — The rows and their source: the slot's body is the rows `python code_record.py
  neighbourhood <path>…` prints for the seed, the reader found by `resolve_kit_dir("memory-tree",
  "code_record.py", KIT_DIR)`, each row in the grammar of §4 "The rows", ordered `def`, `caller`,
  `callee`, `test`, `sibling`. No `code_record.py` resolved, or one answering the verb with exit 2,
  renders `not-installed: dTotalRecall's code record has not landed`; a record that prints no row for
  the seed renders `searched-empty`. A printed row outside the grammar, a body line among them, is
  not handed, and the block's last line counts it. Observed by AC3 and AC4.
- **S4** — The budget, `memory.code-budget`, a `<n>k` value read as n × 1,024 bytes (default `16k`,
  NP-8), through J1's policy read; over it, unit 11's `derive_slot_cut` keeps whole rows in S3's
  order and its cut line names the query that lists the rest, `python code_record.py neighbourhood
  <path>…`. Observed by AC5.
- **S5** — The map's delivery extended: `gov-researcher` joins `ROLE_SETS`' `structural-roles` row
  (`project-map.md:627`), so the researcher's work order carries `### map` under unit 12's rule; and
  the prompt writer reaches its actor's `map` and `code` slots through the work order it frames
  (`project-map.md:628`): `render --for <dest>` (TOOL-dBoundRoles-4 S1) computes `### map` and
  `### code` for `<dest>`, so both sit inside the prompt writer's `### input:work-order`, while
  `gov-prompt-writer` itself is in no set. Observed by AC6.
- **S6** — The docs: `help/roles.md` "How a task reaches an agent" (`:13-27`) names the `code`
  slot, its budget, `memory.code-roles` and the researcher and prompt writer's map;
  `tools/roles/README.md`'s handoff section names `render_code_slot` and the row grammar. Observed by
  AC7.

## 3. Non-goals (OUT)

- The `code` record, its derivation, its tables and the reader of a seed's neighbourhood over them:
  TOOL-dTotalRecall-8, a later build's surface this unit uses as a stand-in. This unit fixes the rows
  it reads (§4) and names the hand-over; it builds no query over the record.
- The `git grep` floor for a language with no extractor (night-pass.md:218): the record's readers'.
- The seed resolver and the items' seed declarations: TOOL-dPlacedRequest-8.
- The map slot itself and `memory.project-map`: unit 12. Purposes enriched by an agent workflow
  (night pass point 3, item 3): dTotalRecall's `memory.code-enrich`.
- The not-in-view cause computed from the `code` slot: dCalibratedLens (`cl-dClosedLoop-0465`).
- A catalogue row: both keys have one (`tools/policy/catalogue.toml:1398`, `:1404`).

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-4` — `render_slot`, the head and state line `### code` renders through
- **consumes-from** `TOOL-dFurnishedOrders-11` — `derive_slot_cut`, the whole-row cut S4 applies under `memory.code-budget`
- **consumes-from** `TOOL-dFurnishedOrders-12` — `derive_role_set`, read for `memory.code-roles`, and its `structural-roles` row, which S5 extends with `gov-researcher`
- **consumes-from** external — TOOL-dPlacedRequest-8 S4 (`resolve_item_seed`), TOOL-dBoundRoles-4 S1 (`render --for`), TOOL-dBoundRoles-17 S1 (`--item`); DEFERRED at base
- **hands-off** external — dTotalRecall: TOOL-dTotalRecall-8's `code` record lands a `neighbourhood` reader printing §4's rows, which fills this slot; until then it renders `not-installed`

## 4. Design

### The rows

```
<path>:<line>-<end_line> · <kind> <qualified name> · def
<path>:<line>-<end_line> · <kind> <qualified name> · caller <seed definition>
<path>:<line>-<end_line> · <kind> <qualified name> · callee <seed definition>
<path>:<line>-<end_line> · <kind> <qualified name> · test <seed definition>
<path> · sibling
```

`CODE_ROW_RE` in `roles_lib.py` is the grammar's one spelling. A range and a name, never a body
(night-pass.md:210): a row carrying anything else is not handed. A sibling is a file of the same kit
as a seed file, a file-level relation as TOOL-dTotalRecall-8 S6 defines kit membership, so it carries
no range. Under the cap the order is the table's: a role first needs the definitions it will touch,
then who calls them, then what they call, then what tests them.

### The slot

```
### code

slot code · filled
tools/roles/handoff.py:312-424 · function render_handoff · def
tools/roles/handoff.py:1001-1040 · function main · caller render_handoff
… 41 row(s) past 16384 B: python code_record.py neighbourhood tools/roles/handoff.py
```

### Who gets which slot

| Role | `map` (unit 12, `memory.project-map`) | `code` (this unit, `memory.code-roles`) |
|---|---|---|
| `gov-researcher` | joins `structural-roles` here | by the key; `every-role` by default |
| `gov-prompt-writer` | its actor's, inside `### input:work-order` | its actor's, the same way |
| every other role | unit 12's rule | by the key |

v2:1366 states the working roles with "the prompt writer through its actor", which S5 reads as the
`--for` route rather than a set member.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_code_slot` | function, `roles_lib.py` | `py.function`, OK |
| `CODE_ROW_RE` | constant, `roles_lib.py` | no constant cell is declared |
| `gov-researcher` in `ROLE_SETS["structural-roles"]` | data | none |
| the reader's verb `neighbourhood`, named as the hand-over | none built here | none |

### Migration

Additive: every work order under the default `every-role` gains one `### code` block reading
`not-installed`, so each `task-sha` moves once at landing.

### Rollout

Live at landing; the block reads `not-installed` until dTotalRecall's record and reader land.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **A query over the record's tables in the roles kit.** It would read another kit's index schema
  directly and specify a later build's mechanism, which the packet's non-goals keep out.
- **The codebase map's symbols as the source until the record lands.** `memory/map/generated/symbols.json`
  holds `id`, `kind` and `file` only, no ranges, callers or tests (scout B, row 17), so it cannot
  give the rows the clause names.

## 5. Production-readiness checklist

- security — no new write path; the rows are ranges and names from the repository's own record,
  and S3 refuses body lines, so no file content reaches a work order through this slot.
- perf / scale — two subprocesses per work order, the seed and the reader; the body is bounded by
  `memory.code-budget`.
- error / empty / loading states — `not-installed` for an unarmed seed, no item, no record or no
  reader; `searched-empty` for a seed with no definition; a dropped row counted.
- observability — the state line names its reason, and the cut line names the query for the rest.
- risks — every work order grows by one block under the default; until the record lands it is one
  line.
- testing — AC1 to AC7 by a scratch adopter with planted stub kits; the arm of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md` by S6.

## 6. Acceptance criteria

- **AC1** — When `handoff.py render --stdout` runs in a scratch adopter for `gov-builder`,
  `gov-orienter` and `gov-spec-writer`, with a committed `.governance/policy.toml` setting
  `memory.code-roles` to `working-roles`, `every-role` and `structural-roles` in turn, `### code`
  renders for the builder and the spec writer but not the orienter under the first, for all three
  under the second, and for the orienter and the spec writer but not the builder under the third.
  Red when: the key is ignored and every role gets the slot under every value.
  fixture: the policy file is committed, since `resolve` reads the landed revision.
- **AC2** — When the AC1 render for `gov-builder` names `--item item.build.unit-pass` and a stub
  `loop_lib.py` prints `unarmed — write-set: no spec`, the block reads `slot code · not-installed:`
  followed by that line; with no `--item`, it reads `not-installed` naming the missing item.
  Red when: an unarmed seed renders `searched-empty`, so a slot that never ran reads as empty code.
- **AC3** — When the AC2 render has a stub seed printing `tools/roles/handoff.py` and no
  `code_record.py` resolves, the block reads `not-installed` naming dTotalRecall's code record; with
  a stub `code_record.py` exiting 2 on `neighbourhood`, it reads the same; with the stub printing no
  row, `slot code · searched-empty`.
  Red when: a missing record renders an empty `filled` block.
- **AC4** — When the stub `code_record.py` prints, out of order, one row of each relation of §4 and
  one line holding a function body, the block reads `slot code · filled`, holds the five rows in the
  order `def`, `caller`, `callee`, `test`, `sibling`, omits the body line, and its last line counts 1
  row not handed.
  Red when: a body line reaches the work order.
- **AC5** — When the stub prints 300 rows of 80 bytes and `memory.code-budget` is set to `4k`, `8k`
  and `16k` in turn, the body is within 4096, 8192 and 16384 bytes, each cut line naming `python
  code_record.py neighbourhood` and the seed path.
  Red when: the `k` is read as 1,000 bytes or the budget is ignored.
- **AC6** — When `python -c` calls `roles_lib.derive_role_set("structural-roles", roles)`, the set
  holds `gov-researcher` and not `gov-prompt-writer`; when `handoff.py render --role
  gov-prompt-writer --for gov-spec-writer --stdout` runs, its `### input:work-order` block holds the
  spec writer's `### map` and `### code` blocks, and the prompt writer's own `## Task` holds neither
  outside it.
  Red when: the prompt writer gets slots of its own, or none of its actor's.
- **AC7** — When `grep -n 'memory.code-budget' roles.md` and `grep -n 'memory.code-roles' roles.md`
  run in `help/`, each names its key and its values.
  Red when: the page names no `code` slot.

## 7. Gates

`policy fixtures` · `roles adopter self-test` · `roles catalogue` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC3 AC4 · a scratch adopter with stub seed and record readers, each `memory.code-roles` value, and a planted body line · none

## 8. Open questions

- **F1 — Who builds the query over the `code` record?** TOOL-dTotalRecall-8 §3 gives "the `code` slot
  in each item's work order and `memory.code-budget`" to dBoundRoles, and the clause gives both to
  this build; the packet keeps dTotalRecall's surfaces as stand-ins. Options: (a) this unit fixes
  the rows it reads and the reader's verb, renders `not-installed` until that reader answers, and
  names the hand-over; (b) this unit writes the query into `code_record.py`, a later build's file
  and mechanism; (c) a query in the roles kit over the index's tables. (b) and (c) fail the packet's
  non-goal on dTotalRecall's surfaces (veto 1). RESOLVED (agent, 2026-10-26, delegated): (a), rung
  1, the brief's rule for a later build's surface; the disagreement with TOOL-dTotalRecall-8 §3 is
  returned for an ask in dTotalRecall's `BACKLOG.md`. widens: none · relaxes: none
- **F2 — What are "their kit's siblings"?** Options: (a) the other files of each seed file's kit,
  one `sibling` row each, no range; (b) every definition of those files with its range. (b) spends
  the budget on code no seed calls before the callers and tests a role needs, and the cut would drop
  them first anyway. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3: kit membership is a
  file's (TOOL-dTotalRecall-8 S6), and the rows a role acts on keep the budget. widens: none ·
  relaxes: none
- **F3 — How is the map's delivery extended to the prompt writer?** Options: (a) the researcher
  joins `structural-roles`, and the prompt writer reaches its actor's slots through `render --for`;
  (b) both join `structural-roles`, so the prompt writer gets a map of its own beside its actor's.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1366's "the prompt writer through its
  actor" and the delivery table's "its actor's `map` and `code` slots, through the work order it
  frames" (`project-map.md:628`). widens: none · relaxes: none
- **F4 — The parents this unit calls.** Units 4, 11 and 12 (orders 4, 14, 15) precede it;
  TOOL-dPlacedRequest-8, TOOL-dBoundRoles-4 and -17 are DEFERRED at base, and dTotalRecall's record is
  a later build's. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on
  `render_slot`, `derive_slot_cut`, `derive_role_set` and `render --for`, and stops this unit if any
  is still absent then; an absent seed resolver, `--item` or record is the `not-installed` state.
  Rung 1, the build order the brief fixes. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 17, the brief's J1, J4, J16 and J17,
  scout B's row 17, the night pass's point 3 and NP-8, NP-9, the project map's delivery table, and
  the source at `1a3ce03d`.

## 10. Reuse audit

The seams extended: `render_handoff`'s `## Task` composition (`tools/roles/handoff.py:312-424`);
unit 4's `render_slot`, unit 11's `derive_slot_cut` and unit 12's `derive_role_set` and
`ROLE_SETS`, each reused rather than copied; `resolve_kit_dir` (`tools/roles/roles_lib.py:97`) for the
loop kit's seed and the memory-tree kit's record reader. `python tools/codebase-map/reuse_lookup.py
"render the code neighbourhood of an item's seed as ranges under a byte budget"` ranked name-stem
noise (`seed`, `render`, `derive_budget_cut`, `read_history_range`); the closest code at base,
`python_symbols`, `scan_js_definitions` and `fan_in` in `tools/codebase-map/map_lib.py` (scout B,
row 17), carry no ranges or callers, so no existing seam gives the rows and the source is the
hand-over of §8 F1. The recall probe returned scout B's row 17 and this build's brief; scout B cites
`map_lib.py:318`, `:427` and `:960`, which this unit does not call.

Recall terms used: `python tools/memory-recall/query.py "how is the code slot rendered from an item's
seed under a byte budget" --terms "code slot seed ranges callers callees tests siblings code-budget
code-roles working roles not installed"`
