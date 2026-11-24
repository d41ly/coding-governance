# TOOL-dBoundRoles-91 — the declaration verb cuts a work order from the composed item kind

**Status:** INPROGRESS · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 45

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-92 |
| [2026-11-24-prompt-TOOL-dBoundRoles-91-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-91-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-91-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-91-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`loop_lib.py declaration`, the verb `handoff.py render --item` cuts a work order from, reads gov's own
item rows and gov's own roles. A repository item the composition admits gets no work order, an admitted
amendment is dropped, and an admitted actor patch is cut for gov's actor. This unit resolves the item,
its outcomes and its role from the composition of the caller's repository.

## 2. Scope (IN)

- **S1** — The row. `run_declaration_command` in `tools/loop/loop_lib.py` still checks gov's definition
  through `read_items`, then takes the row from `read_composed_items(root)` of
  `tools/loop/loop_items.py`, imported inside the function. Where the composition is unarmed that reader
  answers gov's rows; where it refuses, the verb exits 1 printing the refusal. A tag no composed row
  holds exits 1 with today's line. Observed by AC1, AC2, AC5 and AC6.
- **S2** — The outcomes. `derive_outcome_set(row, members, where)` over the composed row, `members` the
  definition's disposition set. The verb no longer calls `read_outcome_set`. Observed by AC1 and AC4.
- **S3** — The role. `read_role_defaults(kit_dir, root=None)` reads `roles_lib.compose_roles(root)` where
  a root is handed and `load_roles` where none is, so its other callers read what they read today. A
  refused role composition is a LoopError naming its first line. The verb resolves the row's actor
  through `roles_lib.derive_repository_slot`, so `role:adopter.<name>` takes the fields of the composed
  role whose slot is `<name>`; the printed `actor` is the row's own string, and `source` names the slot.
  An `adopter.` actor whose slot the composed catalogue holds under another tag exits 1 naming both.
  Observed by AC3 and AC7.
- **S4** — The root. The verb takes `--root <dir>`, the working directory where absent, and reads the
  git toplevel of it; outside a git work tree it exits 1 naming the directory. Observed by AC8.
- **S5** — The renderer. `read_item_declaration(item, role, root)` in `tools/roles/handoff.py` passes
  `--root`, and compares the role it renders with the slot `lib.derive_repository_slot` gives the
  declaration's actor. Observed by AC7.
- **S6** — The plants of `tools/loop/loop_items.py`: `declaration-repo`, `declaration-inputs`,
  `declaration-actor`, `declaration-join`, `declaration-refused` and `declaration-unarmed`. Each runs the
  verb in the scratch repository and holds its output; none runs the scratch's `check`, so each answers
  beside the red `record-kind.flake` pin. Observed by AC1, AC2, AC3, AC4, AC5 and AC6.
- **S7** — The renderer's arm. Arm 46 of `tools/roles/adopt-roles.test.sh` reads the declaration of its
  patched item for the repository role and for gov's. `build_fixture` of that suite copies
  `loop_items.py` beside `loop_lib.py`, as an install holds them. The stub of
  `tools/roles/render_agents.py` takes the third argument. Observed by AC7.
- **S8** — The texts. The verb's usage line and docstrings, `tools/loop/README.md`,
  `tools/roles/README.md` and the "Read one item's declaration" paragraph of `help/loop.md`, its usage
  fingerprint re-stamped. Observed by AC9.

## 3. Non-goals (OUT)

- The `seed` verb beside it, `run_seed_command`, which reads gov's rows the same way. No work order is
  cut from it: `handoff.py` calls the `declaration` verb alone. It is named here for whoever files it.
- The `loop item kind` leg's red on `record-kind.flake`, which no record-version row pins.
- The activated rows of a build's placed scenarios. `handoff.py` composes roles with none handed, and
  this verb matches it.
- `check_item_declarations` and `check_item_roles` in the item check, which grade a repository role's
  item `pending` against gov's catalogue.
- The refused and admitted patches themselves: `check_actor_patches` and the roles kit's check stand.
- Rendering a repository role's body, which an overlay row does not carry.

This unit builds on `TOOL-dBoundRoles-3`'s verb, `TOOL-dBoundRoles-20`'s role composition and
`TOOL-dBoundRoles-84`'s actor patch, all CLOSED.

### Edges

- **consumes-from** external — the playbook kit's `overlay_rows.py compose`, which answers the composed rows, refuses, or says it is unarmed

## 4. Design

### Evidence

Read and probed at HEAD `c31769972`, whose `tools/` and `help/` trees equal base `f3ec096a8`'s:

- `run_declaration_command` (`tools/loop/loop_lib.py@b14af4ca:1898`) builds its rows from
  `read_items(kit_dir)`, its outcomes from `read_outcome_set(kit_dir, tag)` and its roles from
  `read_role_defaults(kit_dir)`, which answers `load_roles`. None takes a root.
- The defect holds. A scratch repository from `loop_items.build_scratch_tree` took an overlay holding
  `item.build.adopter.ship` acting as `role:gov-builder`, an `amends` adding an input to
  `item.test.select`, and an `amends` of `item.build.unit-pass`'s actor to `role:adopter.triager` beside
  that role's row. `overlay_rows.py compose --kind item` exits 0 with all of it composed. The verb exits
  1 on the first, `no [[item]] row declares item.build.adopter.ship`; prints gov's inputs on the second;
  and prints `role:gov-builder` with its `product` allowance on the third. `handoff.read_item_declaration`
  in that scratch raises on the first with the verb's line.
- `roles_lib.compose_roles` there answers the slot `triager` with tag `role.adopter.triager`
  (`tools/roles/roles_lib.py#compose_roles`), so both a lookup by `adopter.triager` and the compare
  `declaration.actor == "role:" + role` (`tools/roles/handoff.py@d123282e:797`) miss it.
- `read_composed_items` (`tools/loop/loop_items.py#read_composed_items`) answers the composed rows, gov's
  rows on an unarmed composition, and raises ValueError on a refused one. `LoopError` is a ValueError
  (`tools/loop/loop_lib.py#LoopError`), and where `loop_lib.py` runs as `__main__` the copy `loop_items`
  imports is another class, so the verb catches ValueError, as `--grade-site` already does.
- `check_actor_patch_file` (`tools/roles/check_roles.py#check_actor_patch_file`) derives a slot by
  `lib.derive_repository_slot("role." + actor.partition(":")[2])`, the idiom S3 and S5 reuse.
- The composition took 2.1 seconds over this tree, PINNED at one reading on 2026-11-24, under the
  renderer's bound `DECLARATION_BOUND_S` of 60.
- `build_fixture` of the roles suite copies `loop_lib.py` and `loop.toml` alone
  (`tools/roles/adopt-roles.test.sh@d84d7502:186`), so its fixtures would fail the import; with
  `loop_items.py` copied the composition is unarmed there, its playbook home holding no `overlay_rows.py`,
  and gov's rows answer.

### The verb

```python
items = read_items(kit_dir)                      # gov's definition holds, as today
from loop_items import read_composed_items       # it imports this module, so here and not at the top
row = {r.get("tag"): r for r in read_composed_items(root)}.get(tag)
data, where = read_definition(kit_dir)
outcomes = derive_outcome_set(row, check_loop(data, where)["dispositions"], where)
roles, _why = read_role_defaults(kit_dir, root)
```

The resolution from a row to the printed object is one function the verb and the join plant both call,
so a row the join resolves is a row the verb prints. The actor's slot is derived before
`resolve_item_declaration`, which is handed the row with `actor` at `role:<slot>`, so that function and
its other callers do not move. With no roles kit there is no helper and no catalogue, and every role
item reads `unarmed`, as today.

The collision refusal of S3 is the one case the helper cannot tell apart: `role:adopter.gov-builder`
derives the slot `gov-builder`, whose composed role carries the tag `role.gov-builder`. The composition
refuses a repository role at a gov slot, so no admitted row means it, and the verb says so rather than
cutting gov's order.

### The plants

A plant of S6 writes its overlay, commits it and runs `loop_lib.py declaration --item <tag> --json --root
<scratch>`, printing one `loop: fixture · declaration · exit <n> · <what it read>` line. `declaration-join`
plants the overlays of the first plants at once, reads every composed tag, resolves a declaration with a
non-empty outcome set for each in one process of the scratch's own modules, and prints the count of rows resolved beside the count composed; an unequal
pair, an empty population or a refusal fails it. `declaration-refused` excludes `item.test.select`, which
`item.test.verdict` needs, as the plant `exclude-needed` does. Their exit is their own and never the scratch `check`'s.

### Inventory

Minted: `derive_composed_declaration` in `tools/loop/loop_lib.py`, graded by `py.function` and asked of
`python tools/lexicon/lexicon.py --suggest derive_composed_declaration --as py.function` at the pass; the
flag `--root`; and the plant names of S6.

### Migration

None. The verb's output is unchanged wherever the overlay holds no item or role row.

### Rollout

Live at landing. No tree carries such an overlay today (the report's reading).

### Files touched (estimate)

- `tools/loop/loop_lib.py` (the verb, `read_role_defaults`, the docstrings, the usage line)
- `tools/loop/loop_items.py` (the plants and their cases)
- `tools/loop/README.md`
- `tools/roles/handoff.py` (`read_item_declaration`, its caller, the module docstring)
- `tools/roles/render_agents.py` (the stub's signature)
- `tools/roles/adopt-roles.test.sh` (arm 46, `build_fixture`, the floor)
- `tools/roles/README.md`
- `help/loop.md`
- `tools/run-gates/selftest-budgets.txt` (the `loop item kind` row, its `plants=` count and its figure)

### Alternatives rejected

- **Compose in `handoff.py` and hand the row to the verb.** The roles kit would then resolve items, which
  the loop kit owns; `read_kind_composition` already calls back into that kit.
- **Fall back to gov's rows where `loop_items.py` does not import.** An install holds both files, so the
  fallback would only hide a broken one and drop the overlay silently.

## 5. Production-readiness checklist

- security — the work order's allowance now follows the composed role, whose write class the actor-patch
  check already holds to gov's ceiling; a refused composition cuts no order.
- perf / scale — one composition per work order, and a second where the overlay holds a role row.
- error / empty / loading states — refused, unarmed, unknown tag, colliding actor and no work tree each
  answer by name.
- observability — `source` names the slot each field came from.
- risks — an uncommitted edit of gov's definition no longer reaches the verb, since the composition reads
  HEAD, as the roles composition beside it does.
- testing — the plants of S6 and arm 46, each with its staged break below.
- migration — none.
- user docs — `help/loop.md` per S8.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/loop_items.py --fixture --plant declaration-repo` runs, it exits 0 and
  its `loop: fixture · declaration` line names `item.build.adopter.ship`, the actor `role:gov-builder`,
  the allowance `product` and the outcome `done`.
  Red when: the row is read from gov's definition, so the verb exits 1.
- **AC2** — When `python tools/loop/loop_items.py --fixture --plant declaration-inputs` runs, it exits 0
  and the line for `item.test.select` holds the added input beside gov's own.
  Red when: the verb prints the row before its `amends`.
- **AC3** — When `python tools/loop/loop_items.py --fixture --plant declaration-actor` runs, it exits 0
  and the line for `item.build.unit-pass` holds the actor `role:adopter.triager` and the triager row's
  `reads`, `writes` and `return`, each sourced `role:triager`; and the plant's second run, over an item
  acting as `role:adopter.gov-builder`, exits 1 naming that actor and `role.gov-builder`.
  Red when: the actor is read unpatched, its fields read `pending`, or the colliding actor is cut for gov's role.
- **AC4** — When `python tools/loop/loop_items.py --fixture --plant declaration-join` runs, it exits 0 and
  prints one count of composed rows equal to its count of declarations, the planted repository item
  among them. figure: DERIVED, both counts read from the scratch at the observation.
  Red when: an item the composed kind admits resolves no declaration, or the population read is empty.
- **AC5** — When `python tools/loop/loop_items.py --fixture --plant declaration-refused` runs, over an
  overlay whose composition refuses, the verb exits 1 printing `the item composition does not read` and
  no JSON, and the plant exits 0.
  Red when: a refused composition falls back to gov's rows.
- **AC6** — When `python tools/loop/loop_items.py --fixture --plant declaration-unarmed` runs, over a
  scratch whose `item-schema.toml` is removed, the verb exits 0 and prints gov's row for
  `item.test.select`, and for `item.build.adopter.ship` exits 1 on `no [[item]] row declares`.
  Red when: an unarmed composition refuses a gov item.
- **AC7** — When a scratch `python -B` probe builds `loop_items.build_scratch_tree()`, commits the
  `declaration-actor` overlay and calls that scratch's
  `handoff.read_item_declaration("item.build.unit-pass", <role>, <scratch>)`, it returns the declaration
  for `triager`, and for `gov-builder` raises naming `role:adopter.triager`; and for
  `item.build.adopter.ship` and `gov-builder` it returns the declaration.
  Red when: `handoff.py` passes no root, or compares the actor with the slot unnormalised.
- **AC8** — When the verb runs as `declaration --item item.build.unit-pass --json` on `tools/loop/loop_lib.py`
  by its absolute path, the working directory `tools/roles`, it exits 0 and prints `"actor": "role:gov-builder"`; with `--root` at a directory in no
  git work tree it exits 1 naming that directory.
  Red when: a subdirectory composes as unarmed, or a directory outside git answers gov's rows.
- **AC9** — When `grep -n "declaration --item" help/loop.md tools/loop/README.md tools/roles/README.md` and
  `grep -n "composed" help/loop.md` run, each page's passage says the rows are the composed ones and the
  `help/loop.md` fingerprint is the one `python tools/govkit/docs_leg.py --fingerprints` prints for
  the `declaration` member of `tools/loop/loop_lib.py`.
  Red when: a page still says the verb reads the definition's rows alone, or the stamp is stale.

## 7. Gates

`loop item kind` · `loop definition` · `loop definition fixtures` · `roles adopter self-test` · `roles render selftest` · `roles catalogue` · `policy fixtures` · `docs` · `help page commands` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_items.py · covers AC1 AC2 · the plants `declaration-repo` and `declaration-inputs`, staged by the verb reading `read_items` again · the `plants=` count of the `loop item kind` budget row, by the plants of S6
New arm: tools/loop/loop_items.py · covers AC3 · the plant `declaration-actor`, staged by dropping the slot derivation, and by dropping the collision refusal · the same count
New arm: tools/loop/loop_items.py · covers AC4 · the plant `declaration-join`, staged by resolving outcomes through `read_outcome_set`, which answers none for a repository item · the same count
New arm: tools/loop/loop_items.py · covers AC5 AC6 · the plants `declaration-refused` and `declaration-unarmed`, staged by answering gov's rows on a refusal and by refusing on unarmed · the same count
New arm: tools/roles/adopt-roles.test.sh · covers AC7 · arm 46's `ac6-held` case reads the declaration for the repository role and refuses gov's, staged by the unnormalised compare · FLOOR_ASSERTIONS and the arm's own line count, by the lines added

The `loop item kind` leg is red at this run's BASE on `record-kind.flake`; these arms are read by their
own `PASS` and `FAIL` lines in its output.

## 8. Open questions

- **F1 — Where is the composition read?** Options: (a) in the verb, through `read_composed_items`, with
  the root handed by the renderer; (b) in the renderer, which hands the verb a row. (a) keeps item
  resolution in the kit that owns it and reads the one reader the loop kit's other callers use.
  RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none
- **F2 — What does an `adopter.` actor whose slot is a gov role's answer?** Options: (a) a refusal naming
  the actor and the role it would have taken; (b) the gov role's declaration, as the helper alone gives;
  (c) `pending`. (b) cuts gov's order for a role nobody declared, and (c) prints an order the renderer
  then passes for gov's role. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (c) > (b) ·
  pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — Is `--root` required?** Options: (a) optional, the git toplevel of the working directory where
  absent; (b) required. (b) breaks the command the help page prints and every hand call. RESOLVED (agent,
  2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none ·
  relaxes: none
- **F4 — Where does the plants' exit come from, beside a red `check`?** Options: (a) the verb's own
  answers, the scratch `check` not run; (b) the scratch `check` as the other plants, the owed exit at its
  red. (b) would pin the red into the cases and break them on the day it is mended. RESOLVED (agent,
  2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief `2026-11-24-prompt-TOOL-dBoundRoles-91-spec-brief`
  and item H5 of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `run_declaration_command`, `read_role_defaults` and `derive_outcome_set` in
`tools/loop/loop_lib.py`, `read_composed_items` and the scratch plants in `tools/loop/loop_items.py`,
`compose_roles` and `derive_repository_slot` in `tools/roles/roles_lib.py`, and `read_item_declaration` in
`tools/roles/handoff.py`. `python tools/codebase-map/reuse_lookup.py "resolve an item's declaration from
the composed item kind"` ranked `read_composed_items` and `read_item_rows` among the loop kit's own names,
the reader this unit calls, so no existing seam fits beyond them. The recall probe returned
`TOOL-dBoundRoles-3` and its deviation 34, `TOOL-dDeclaredLoop-120` and `TOOL-dBoundRoles-33`, the asks that
led to the actor patch, and `TOOL-dBoundRoles-84` §10, which named `read_composed_items` too.

Recall terms used: `python tools/memory-recall/query.py "where does the work order read an item's declaration" --terms "declaration verb work order item composed kind overlay amends actor patch repository role compose read_composed_items handoff render"`
