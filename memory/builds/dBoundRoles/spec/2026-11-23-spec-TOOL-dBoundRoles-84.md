# TOOL-dBoundRoles-84 — the item schema opens `actor` on `widens = "changes"`, so a patch of a gov item's actor reaches the actor-patch check, which alone admits or refuses it

**Status:** CLOSED · rev-1 · 2026-11-23 · node d · Tier-2 · base 318e20c9 · streams tooling · order 23 · closes TOOL-dDeclaredLoop-120

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 |
| [2026-11-22-build-TOOL-dBoundRoles-84-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dBoundRoles-84-1-acceptance-ledger.md) | journal | — |
| [2026-11-23-build-TOOL-dBoundRoles-84-deviation-841.md](../build/2026-11-23-build-TOOL-dBoundRoles-84-deviation-841.md) | deviation | — |
| [2026-11-23-build-TOOL-dBoundRoles-84-red-fix-36.md](../build/2026-11-23-build-TOOL-dBoundRoles-84-red-fix-36.md) | red-fix | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-84-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-84-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-84-1-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-84-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-84-spec-brief.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-84-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md) | diff-review | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-85 |

<!-- /gen:spec-records -->

## 1. Goal

The loop kit's item schema declares `actor` a bare scalar, with neither `widens` nor `fixed-by` nor
`ref`, so the row checks refuse every `amends` of a gov item's actor as a field fixed by its undeclared
class, before any check could admit a repository role that returns the item's template.
`TOOL-dBoundRoles-20` S6 (the actor patch and `check_actor_patch`, its §8 F8 (iii)) waits on that. This
unit opens `actor` on the scalar direction `changes`, gives it the `actor` ref, and holds every actor
patch at one seat in the item kind's check, which refuses it until the roles kit's actor-patch check
answers there. No other item field moves.

## 2. Scope (IN)

- **S1** — The schema. The `actor` row of `tools/loop/item-schema.toml` gains `widens = "changes"` and
  `ref = "actor"`, and the file's header comment says what each declares. Observed by AC4.
- **S2** — The direction. `changes` joins `SCALAR_DIRECTIONS` in `tools/playbook/row_checks.py`, the
  tuple of scalar direction words `read_field_decl` (`tools/playbook/overlay_rows.py#read_field_decl`)
  admits beside an order; whichever of this unit and `TOOL-dBoundRoles-82` lands first mints it.
  `derive_patch_class` (`tools/playbook/row_checks.py#derive_patch_class`) reads a `changes` operation as
  no operation where the value equals gov's and `widens` otherwise, the semantics TOOL-dWitnessedBar-28
  S4 specs for the word. Observed by AC1 and AC4.
- **S3** — The seat. `check_actor_patches(operations)` in `tools/loop/loop_items.py` returns one refusal
  per classified operation on the field `actor`: a value spelled `role:adopter.<name>`, a repository
  role, is refused because no actor-patch check answers in the kit, naming the item, the overlay row and
  the role; any other value is refused because an actor patch names a repository role, naming the item,
  the row and the value. `check_item_composition`
  (`tools/loop/loop_items.py#check_item_composition`) takes the composition's `operations` as a new
  keyword argument defaulting to none and adds the seat's refusals, and `run_check` hands it the
  payload's `operations`. Observed by AC1 and AC2.
- **S4** — Every other fixed field still refuses. An `amends` of `allowance`, `returns` or `owner`, and
  of `step`, `witness` or `outcomes`, is refused by the row checks as before, naming the field and what
  fixes it. Observed by AC3.
- **S5** — The page. `help/loop.md`, "What you may change on gov's items", says `actor` is open to a
  repository role and admitted by the actor-patch check alone, and that `allowance`, `returns` and
  `owner` stay fixed. Observed by AC5.

## 3. Non-goals (OUT)

- `check_actor_patch`, the roles-kit verb `check_roles.py --check-actor-patch` and its subprocess call
  from the seat: `TOOL-dBoundRoles-20` S6. Until it lands, the seat refuses every actor patch, so this
  unit admits no actor change the tree refused before (§5 security).
- The member fold that lets the exclusion walk read `role:<slot>` as `role.<slot>`:
  `TOOL-dBoundRoles-83`. This unit declares the ref the walk reads.
- `allowance`, `returns`, `owner` and the termination fields: they stay fixed by their undeclared class.
- A repository's own item acting as a gov role: an overlay row with no edge is no operation, and the
  seat reads operations only.

`TOOL-dBoundRoles-20` consumes this unit through
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`, which binds the relation over
that spec: S6 replaces the repository-role refusal of the seat `check_actor_patches` with its
`check_roles.py --check-actor-patch` call, and S7's exclusion refusal reads `ref = "actor"` on the item schema's `actor`.

### Edges

- **hands-off** external — TOOL-dWitnessedBar-28 S4: the scalar direction `changes`, landed here with the semantics that spec gives it, so its `argv` row declares it and adds only `rises`

## 4. Design

### Evidence

Read at HEAD `4b7916726`, whose `tools/` tree equals base `318e20c9`'s:

- `actor` is `name = "actor"` and `shape = "scalar"` alone (`tools/loop/item-schema.toml@829f39a6:46-48`),
  and the schema's header says a field declaring neither class is fixed, deny by default.
- The gap, probed in-process: `read_kind_schema(root, "item")["decl"]["actor"]` is
  `{'ref': None, 'fixed-by': None, 'widens': None}`, and `check_rows` over an `amends` of
  `item.build.core`'s actor to `role:adopter.triager` returns `row-checks: red · fixed · ... · field
  actor · fixed by its undeclared class`.
- `run_check` reads the compose payload and prints `loop: patch <row> on <tag> · <field> <op> ·
  <class>` for each of its `operations` (`tools/loop/loop_items.py#run_check`), so the seat reads the
  same list the kit already prints.
- `check_item_roles` (`tools/loop/loop_items.py#check_item_roles`) reads a `role:` actor's slot and
  refuses an expansion, a non-core or a cycle role; it does not judge a patch, and stays as it is.
- TOOL-dWitnessedBar-28 S4 specs `changes` as "every change `widens`" on the same two functions, and is
  unbuilt (status DEFERRED); `TOOL-dBoundRoles-82` adds `rises-only` to the same tuple.

### The seat

```python
REPO_ROLE = "role:%s." % ADOPTER                       # role:adopter.<name>

def check_actor_patches(operations):
    out = []
    for op in operations or ():
        if op.get("field") != "actor":
            continue
        where = "item %s · actor patched to %r by %s" % (op["tag"], op["value"], op["row"])
        if isinstance(op["value"], str) and op["value"].startswith(REPO_ROLE):
            out.append(where + " · a repository role acts in a gov item once the roles kit's actor-patch "
                               "check admits it, and none answers here")
        else:
            out.append(where + " · an actor patch names a repository role, %s<name>" % REPO_ROLE)
    return out
```

The block is the design's shape; the pass fits it to the module. A `supersedes` writing another actor
is a `set` operation too (`tools/playbook/row_checks.py#derive_entry_ops`), so the seat holds it as it
holds an `amends`.

### Inventory

Minted: `widens = "changes"` and `ref = "actor"` on the item schema's `actor`; the direction word
`changes` in `SCALAR_DIRECTIONS`; `check_actor_patches` and `REPO_ROLE` in `tools/loop/loop_items.py`;
the keyword `operations` of `check_item_composition`; the plants `patch-actor-repo`, `patch-actor-gov`
and `patch-allowance`. The function name is asked of `python tools/lexicon/lexicon.py --suggest
check_actor_patches --as py.function` at the pass.

### Migration

None: no overlay in the tree patches an actor, and the item rows' canonical forms do not move, since a
schema declaration is no part of a row.

### Rollout

Live at landing. Units 82 and 83 hold the same order and write `tools/playbook/row_checks.py`, so the
declared write sets intersect and `--dispatch` refuses a second pass while the first is open (M6
condition 1).

### Files touched (estimate)

- `tools/loop/item-schema.toml` (`actor`'s two keys, the header comment)
- `tools/playbook/row_checks.py` (`changes` in `SCALAR_DIRECTIONS`, `derive_patch_class`, the docstring)
- `tools/playbook/overlay_rows.py` (`read_field_decl`, where unit 82 has not landed the tuple's read)
- `tools/loop/loop_items.py` (`check_actor_patches`, `check_item_composition`, `run_check`, the plants and cases, the docstring)
- `help/loop.md`

### Alternatives rejected

- **`actor` opened along an order of values.** A repository role's name is the repository's; no list
  gov ships can hold it.
- **A `fixed-by` source that a named check may override.** It makes a fixed field writable, so the
  fixed set stops meaning fixed, and the row checks would have to call a sibling kit.
- **The seat in the playbook kit's row checks.** A role rule there reads the roles kit's verb from the
  wrong kit; the item kind's check is where `TOOL-dBoundRoles-20` §8 F3 and F7 put the call.

## 5. Production-readiness checklist

- security — no widening at landing: an actor patch the row checks refused before is refused by the
  seat now, and only `TOOL-dBoundRoles-20` S6's check can admit one; every other fixed field still
  refuses at the row checks.
- perf / scale — one pass over the payload's operations.
- error / empty / loading states — no actor operation, no seat line; an unarmed composition runs no
  seat, as it runs no other composed check.
- observability — each refusal names the item, the row and the value; the patch line prints the
  operation's class `widens` before it.
- risks — a reader of `read_composed_items`, `position.py` among them, sees a patched actor that
  `loop_items.py check` refuses, as it sees any other composed row a check refuses; the leg `loop item
  kind` is what holds it.
- testing — AC1 to AC5 by the plants, a probe and a grep; the arm of §7 at the close.
- migration — none.
- user docs — `help/loop.md` per S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/loop_items.py --fixture --plant patch-actor-repo` runs, an overlay
  row amending `item.test.select`'s actor to `role:adopter.triager`, it exits 1, prints a `loop: patch`
  line naming `actor set · widens` and a `loop: refused` line naming `item.test.select`,
  `role:adopter.triager` and `actor-patch check`, and prints no `fixed by its undeclared class` line.
  Red when: the row checks still refuse the actor first, or the seat admits the patch.
  fixture: the plant's scratch repository under `%TEMP%`, built by `build_scratch_tree`'s steps.
- **AC2** — When the plant `patch-actor-gov` amends the same actor to `role:gov-builder`, it exits 1
  with a `loop: refused` line naming `role:gov-builder` and `names a repository role`.
  Red when: an actor patch to a gov role or a command composes.
- **AC3** — When the plant `patch-allowance` amends `item.test.select`'s `allowance`, it exits 1 with a
  `loop: refused` line naming `field allowance` and `fixed by its undeclared class`.
  Red when: opening `actor` opened another fixed field.
- **AC4** — When `python -c "import sys; sys.path.insert(0, 'tools/playbook'); import overlay_rows as o; print(o.read_kind_schema('.', 'item')['decl']['actor'])"`
  runs at the repository root, it prints `ref` `actor` and `widens` `changes`.
  Red when: the schema leaves `actor` bare, or `read_field_decl` refuses the word.
- **AC5** — When `grep -n "actor-patch check" help/loop.md` runs, it prints the line of "What you may
  change on gov's items" naming `actor`.
  Red when: the page still calls `actor` fixed.

## 7. Gates

`loop item kind` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_items.py · covers AC1 AC2 AC3 · the `patch-actor-repo`, `patch-actor-gov` and `patch-allowance` cases of `CASES`, staged by leaving `actor` bare in the scratch schema · none

## 8. Open questions

- **F1 — How does a fixed-by-default schema let an actor patch through to a check outside the row
  checks?** Options: (a) `actor` open on the scalar direction `changes`, held at a seat in the item
  kind's check that refuses until the actor-patch check answers; (b) a `fixed-by` source naming a check
  that may override it; (c) `actor` opened with no seat, admitted until `TOOL-dBoundRoles-20` lands.
  (c) admits every actor change in the window, widening the write surface this ask priced (veto 3);
  (b) makes a fixed field writable and has the playbook kit call a sibling kit (veto 2). RESOLVED
  (agent, 2026-11-23, delegated): (a), rung 3, and the word is TOOL-dWitnessedBar-28 S4's `changes`, so
  one word means one thing. options: (a) · pick: (a) · admitted-by: principle.p18 · widens: the row
  grammar's scalar directions, by `changes` · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-23 · initial draft, from the brief
  `2026-11-23-prompt-TOOL-dBoundRoles-84-spec-brief` and the owner's ruling
  `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling`, closing `TOOL-dDeclaredLoop-120`.

## 10. Reuse audit

The seams extended are the item schema `tools/loop/item-schema.toml`, the field reader
`tools/playbook/overlay_rows.py#read_field_decl` and classifier
`tools/playbook/row_checks.py#derive_patch_class`, and the item kind's composed check
`tools/loop/loop_items.py#check_item_composition` (TOOL-dDeclaredLoop-24 S4), whose `run_check` already
reads the payload's operations. The composition is read through the kit's one door,
`tools/loop/loop_items.py#read_composition`, which `tools/loop/composition.py#read_composition_at` also
runs at a pin, so the seat needs no second read. `python tools/codebase-map/reuse_lookup.py "let an
overlay patch of an item actor through to a separate admission check"` ranked `check`,
`OverlayRefused`, `read_composed_items` and `read_item_rows`, none an actor-patch seat, so no existing
seam fits beyond those named. The recall probe found the ask `TOOL-dDeclaredLoop-120`, this unit's
brief and `TOOL-dBoundRoles-33`, the ask that `check_item_composition` call the actor-patch check, which
`TOOL-dBoundRoles-20` S6 answers at this seat.

Recall terms used: `python tools/memory-recall/query.py "how does an overlay amends of a gov item actor reach the actor patch check" --terms "actor patch check_actor_patch item-schema amends actor fixed undeclared class repository role check_item_composition"`
