# TOOL-dDeclaredLoop-12 — each step a program of items with declared needs, outcomes and routes

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 6 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0097@56655276 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

Each of the five gov steps becomes a program of items in the loop definition: every item declared with
its tag, actor, inputs by layer, instruction scope, allowance, return template, closed outcome set,
computed witness and routes, and the items' declared needs forming an acyclic graph. Today item
declarations are incomplete and the records disagree (`gap-flow-13`); the item audit's tables, folded
into flow-steps (flow-steps.md:13-14, "The audit's fixes are applied"), are the input.

## 2. Scope (IN)

- **S1** — The item schema, `[[item]]` rows in `tools/loop/loop.toml`, with the keys of §4 "### Data
  model", read through `read_items(kit_dir, step=None)` in `tools/loop/loop_lib.py`. Observed by AC1.
- **S2** — The rows: one per item of flow-steps' `[plan]`, `[design]`, `[build]`, `[test]` and `[deploy]`
  tables, 61 in all, each tag `item.<step>.<name>` (shared interface I2), transcribed from the table's
  Actor, Needs, Does, Proven by, Then and Owner cells. Observed by AC1.
- **S3** — The program check, `check_program(items, steps)`: every need names a declared item; the
  needs graph is acyclic; every item's outcome set is non-empty and closed, a list or the reference
  `dispositions` read by `read_outcome_set`; every outcome has one route; every route names a declared
  item of the program, `transition` (a cross-step move, read by the transition table), or `stand-in`
  with its tool named; every input names a layer tag of `tools/playbook/layers.toml`; and each step's
  `exit` item is declared in that step. Observed by AC2.
- **S4** — The instruction scope, derived and never typed: for each item, PLAY-dOrderedCharter-11 S1's
  `derive_load_set(units, reader, item=<tag>)`, printed by `loop_lib.py --check` per item, `unarmed`
  while no instruction unit selects an item. Observed by AC6.
- **S5** — The needs-graph helper (shared interface I14): `tools/lib/needs_graph.py` with
  `order_by_needs(nodes, needs)` and `find_cycles(edges, live=None)`, extracted at this, the third
  instance, from `derive_install_order` (`tools/govkit/govkit.py:911`) and `_scan_cycles`
  (`tools/memory-tree/backlog.py:1271`); copies inline between `# >>> needs_graph_py -- canonical copy:
  needs_graph.py in the gov lib dir (byte-identical; gated)` and `# <<< needs_graph_py` in
  `tools/govkit/govkit.py`, `tools/memory-tree/backlog.py` and `tools/loop/loop_lib.py`, under one
  `needs_graph_py` row of `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`. Observed by AC3 and AC5.
- **S6** — Both callers re-pointed in this unit: `derive_install_order` keeps its name and its refusal,
  ordering through `order_by_needs`; `_scan_cycles` is replaced at its one call site by `find_cycles`.
  Observed by AC4.
  **Readers:** by name: `tools/memory-tree/backlog.py`, whose one call at :1109 is re-pointed to the
  helper · by value: `tools/memory-tree/backlog.py`, which reports each returned cycle at :1109; the
  helper returns the same tuples in the same order.

## 3. Non-goals (OUT)

- The per-field declaration check, one actor of one kind, an allowance, a return schema and a classed
  witness, and the role defaults read through `roles_lib.py`: TOOL-dDeclaredLoop-9's, over these rows.
- Computing each witness: TOOL-dDeclaredLoop-17's; this unit declares the `witness` field.
- The transition tables a `transition` route reaches, and the join of each item's routes to them both
  ways: TOOL-dDeclaredLoop-13's.
- The default failure route and the frontier: TOOL-dDeclaredLoop-14's.
- The breakpoint program's items (`item.review.*`): TOOL-dDeclaredLoop-20's.
- The entry, adopt, lifecycle and probe items: owned by dPlacedRequest, dLinkedLibrary, dWellOiledMachine
  and dTotalRecall, never steps of the five.
- The `item` kind, its factory and composition with a repository's items: TOOL-dDeclaredLoop-24's.
- Counted edges and reachability over the needs graph: TOOL-dDeclaredLoop-33's, beside this helper.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py` and `loop.toml`, and each `[[step]]` row's `exit`, without which no program has a step to belong to
- **consumes-from** `TOOL-dDeclaredLoop-16` — `read_outcome_set` and the `dispositions` reference, so a placing item's outcome set is the one declared set
- **hands-off** `TOOL-dDeclaredLoop-9` — `needs`, the declared dependencies of each item row, and the rows whose fields that unit checks
- **hands-off** `TOOL-dDeclaredLoop-13` — each `[[item]]` row's closed `outcomes` and its `routes`, whose `transition` route the transition tables join both ways
- **hands-off** `TOOL-dDeclaredLoop-24` — `needs`, the declared dependencies of each item row, whose acyclicity check through the I14 helper the composition reads
- **hands-off** `TOOL-dDeclaredLoop-27` — `needs`, the I14 helper whose acyclicity check the scenario successor chains reuse
- **hands-off** `TOOL-dDeclaredLoop-33` — `needs`, the declared dependencies of each item row, and the I14 helper beside which the counted-edge rule is added

## 4. Design

### Data model

```toml
# tools/loop/loop.toml
[[item]]
tag = "item.plan.recommend"            # item.<step>.<name>
step = "step.plan"
actor = "command:plan.recommend"       # <kind>:<name>, one actor, of one kind
needs = ["item.plan.lease"]            # the items whose witnesses it waits for
inputs = ["layer.memory:plan record"]  # <layer tag>:<what it reads>
allowance = "none"                     # what it may write
returns = "record-kind.recommendation" # its return template: the record kind it writes
outcomes = ["review", "no-review"]     # closed; or "dispositions"
witness = { class = "history", by = "the recommendation record" }
owner = "dDeclaredLoop"
[item.routes]
review = "transition"
no-review = "item.plan.exit"
```

| Key | Required here | From the flow-steps table |
|---|---|---|
| `tag`, `step`, `owner` | yes | Item, its section, Owner |
| `actor` | yes | Actor, one per item (flow-steps `[rules]`: an item a policy chooses the actor of is one item per value) |
| `needs` | yes, `[]` for none | Needs |
| `inputs` | yes for a non-role actor | Needs and Does, each with its layer |
| `allowance`, `returns` | yes for a non-role actor | Does and Proven by |
| `outcomes`, `routes` | yes | Then |
| `witness` | yes | Proven by |

A role actor's absent `inputs`, `allowance` and `returns` are its role's, which TOOL-dDeclaredLoop-9
resolves through `roles_lib.py`; this unit does not copy them.

| Step | Items (flow-steps.md, PINNED 2026-10-24) |
|---|---|
| `step.plan` | 11 |
| `step.design` | 13 |
| `step.build` | 14 |
| `step.test` | 10 |
| `step.deploy` | 13 |

### The program check

`check_program` builds the needs graph from every row, asks `order_by_needs` for an order, and turns a
`NeedsCycle` into one refusal naming each cycle once, as `find_cycles` rotates it to its smallest member.
A need naming no row is refused before ordering. Then, per item: `outcomes` non-empty and repeating no
word; `routes` holding exactly the outcomes as keys; each route's target a declared item tag, the word
`transition`, or `stand-in:<path>` naming today's tool (flow-steps `[rules]`, "A route into a later
build reaches today's stand-in"); each input's layer tag a row of PLAY-dOrderedCharter-16's register.
Each step's `[[step]]` `exit` must be a declared item of that step.

### The helper

```python
def order_by_needs(nodes, needs):        # -> list; Kahn, ready queue sorted; raises NeedsCycle(stuck)
def find_cycles(edges, live=None):       # -> [tuple]; each cycle once, rotated to its smallest member
```

`order_by_needs` is `derive_install_order`'s loop (`tools/govkit/govkit.py:932-941`) with the
descriptor read lifted out: govkit passes `{kit: requires within the selection}` and raises its own
`Refusal` from `NeedsCycle.stuck`, so its message is unchanged. `find_cycles` is `_scan_cycles`
(`tools/memory-tree/backlog.py:1271-1292`) with the fold's terminal test passed as `live`, a predicate
over a node, so backlog passes `lambda a: fold.statuses.get(a) not in TERMINAL`.

### Inventory

Minted: the `[[item]]` table and its keys of §4, the sub-table `routes`, the route words `transition` and
`stand-in:<path>`; `read_items` and `check_program` in `tools/loop/loop_lib.py`; `tools/lib/needs_graph.py`
with `order_by_needs`, `find_cycles` and `NeedsCycle`; the parity marker `needs_graph_py`; the plants
`needs-cycle`, `needs-unresolved`, `outcome-unrouted`, `route-unresolved`, `input-no-layer`,
`exit-missing` and `scope-selected`. Naming cells: each function is asked of `python
tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive for the loop. The two re-pointed callers return the same answers (AC4).

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/README.md`
- `tools/lib/needs_graph.py`
- `tools/lib/resolve-python.test.sh`
- `tools/govkit/govkit.py`
- `tools/memory-tree/backlog.py`

### Alternatives rejected

- **A third cycle check written inside the loop kit**: the [reuse] rule's second-instance extraction is
  already owed at the second, and this is the third.
- **Typing each item's instruction scope**: the load set is derived from the units' `scope`
  (PLAY-dOrderedCharter-11 S1), and a typed copy drifts from it.

## 5. Production-readiness checklist

- security — no write path; the rows are committed data.
- perf / scale — 61 rows, one graph; Kahn is linear in the edges.
- error / empty / loading states — each refusal names the item and the field; the instruction scope is
  `unarmed` while no unit selects items, never empty and green.
- observability — `loop_lib.py --check` prints each step's items in their needs order.
- risks — a transcription error in a row is caught by the program check only where it breaks a need,
  an outcome or a route; the per-field check is TOOL-dDeclaredLoop-9's.
- testing — the plants of §4 by a pass through the fixture, and probes of the helper and both callers;
  the suite arms in §7 are observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — `help/loop.md` gains the item program and its check.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs in the loop kit, it exits 0 and prints each step's
  item count, 11, 13, 14, 10 and 13, each item in an order where every need precedes the item.
  Red when: a row is missing, so a need names no declared item and the check refuses it.
  figure: the counts are PINNED, measured over flow-steps' tables 2026-10-24.
- **AC2** — When `python loop_lib.py --fixture --plant needs-cycle` runs, it exits 1 naming the cycle
  once; `--plant needs-unresolved` exits 1 naming the missing need; `--plant outcome-unrouted` exits 1
  naming the item and the outcome without a route; `--plant route-unresolved` exits 1 naming the target;
  `--plant input-no-layer` exits 1 naming the input; `--plant exit-missing` exits 1 naming the step.
  Red when: the routes are read as a free table, so an outcome without a route reads green.
- **AC3** — When `python -c` imports `needs_graph` from `tools/lib/`, `order_by_needs` over `a` needing
  `b` returns `b` then `a`, over `x` and `y` needing each other raises `NeedsCycle` with `stuck` `x` and
  `y`, and `find_cycles` over `a`, `b`, `c` in a ring returns the one tuple `a`, `b`, `c`.
  Red when: `find_cycles` reports the ring three times, once per entry point.
- **AC4** — When a scratch probe calls `derive_install_order` over every kit of
  `tools/govkit/registry.toml` with `tools/govkit/govkit.py` at base `ed497191` and from the working
  tree, the two orders are equal; and `find_cycles` and the base `_scan_cycles` return equal lists over
  a fixture of two cycles and one terminal node.
  Red when: `live` is not applied, so a cycle through a terminal ask is reported.
- **AC5** — When `git grep -l ">>> needs_graph_py" -- tools` runs, it lists `needs_graph.py`
  and the three copies, and `git grep -c "needs_graph_py" -- tools/lib/resolve-python.test.sh` counts
  the row.
  Red when: a copy carries no marker, so the parity population misses it.
- **AC6** — When `python loop_lib.py --fixture --plant scope-selected` runs, a fixture instruction unit
  whose `scope` names `item.plan.record` appears in that item's printed load set and in no other item's;
  without the plant, every item's scope prints `unarmed`.
  Red when: the scope is read from a typed field, so the planted unit does not appear.

## 7. Gates

The pass adds no leg: `check_program` runs under TOOL-dDeclaredLoop-1's `loop definition` leg.

`python resolver (behaviour + inline parity + idiom ban)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `backlog migration selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC1 AC2 AC6 · the `loop definition` leg's fixture plants, the failing case staged by the `needs-cycle` plant · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 · the `needs_graph_py` parity row, its failing case staged by a one-byte edit to the backlog copy · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would carry it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Which items are the five programs?** Options: (a) flow-steps' five step tables, which carry
  the audit's fixes (flow-steps.md:13-14); (b) the audit's own tables (research-flow-items-a.md:28-75),
  which predate the fold and number 31 items for three steps. (b) reintroduces what the fold settled.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — How do this unit and TOOL-dDeclaredLoop-9 split one item's declaration, both clauses naming
  actor, allowance and witness?** Options: (a) this unit declares the schema and seeds every row and
  checks the program's structure, TOOL-dDeclaredLoop-9 checks each field's content and resolves role
  defaults; (b) this unit checks every field. (b) puts the role defaults here, a read of the roles kit
  that clause 9 names. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, one mechanism per spec
  (M2). widens: none · relaxes: none
- **F4 — Where does the needs-graph helper live?** Options: (a) `tools/lib/` with inline copies and a
  parity row; (b) a module in the loop kit that govkit and memory-tree import. (b) makes two kits import
  a sibling, which copy-installed kits cannot. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1,
  shared interface I14 and the charter's Kinds fact. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 12, the brief's shared interfaces I2 and
  I14, scout B's row for cl-0097, flow-steps' step tables, and the two cycle checks read at base
  `ed497191`.

## 10. Reuse audit

The seam extended is the pair of graph checks the scout found, `derive_install_order`
(`tools/govkit/govkit.py:911`) and `_scan_cycles` (`tools/memory-tree/backlog.py:1271`), extracted into
one helper with the canonical-copy pattern of `remote_ladder_py`; the instruction scope is
PLAY-dOrderedCharter-11's `derive_load_set`. `python tools/codebase-map/reuse_lookup.py "acyclic
dependency graph check over declared needs with cycle refusal"` ranked generic stems (`check`,
`refusal`, `need` in `tools/check-kit-versions.sh`, `DesignRefusal`) and named neither graph check,
which the scout found by reading the files. The recall probe returned scout B's row, scout C's row 33
naming the same two primitives, and a skeptic brief on a self-need in `design.streams`, which the
program check refuses as a cycle.

Recall terms used: `python tools/memory-recall/query.py "where is the needs graph cycle check duplicated" --terms "needs graph acyclic cycle derive_install_order _scan_cycles Kahn item program step outcome route"`
