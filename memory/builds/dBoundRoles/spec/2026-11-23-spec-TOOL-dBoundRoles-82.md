# TOOL-dBoundRoles-82 — a scalar field declares `widens = "rises-only"`, so an overlay may raise its number and never lower it

**Status:** CLOSED · rev-1 · 2026-11-23 · node d · Tier-2 · base 318e20c9 · streams tooling · order 23 · closes TOOL-dBoundRoles-78

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 |
| [2026-11-22-build-TOOL-dBoundRoles-82-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dBoundRoles-82-1-acceptance-ledger.md) | journal | — |
| [2026-11-23-build-TOOL-dBoundRoles-82-deviation-821.md](../build/2026-11-23-build-TOOL-dBoundRoles-82-deviation-821.md) | deviation | — |
| [2026-11-23-build-TOOL-dBoundRoles-82-red-fix-34.md](../build/2026-11-23-build-TOOL-dBoundRoles-82-red-fix-34.md) | red-fix | — |
| [2026-11-23-build-TOOL-dBoundRoles-82-red-fix-35.md](../build/2026-11-23-build-TOOL-dBoundRoles-82-red-fix-35.md) | red-fix | — |
| [2026-11-22-prompt-TOOL-dBoundRoles-82-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-82-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-82-1-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-82-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-TOOL-dBoundRoles-82-spec-brief.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-82-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md) | diff-review | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |

<!-- /gen:spec-records -->

## 1. Goal

A scalar field's `widens` is an order of listed values, so a field holding an open integer, a role's
`budget`, cannot declare that an overlay `amends` may raise it and never lower it.
`TOOL-dBoundRoles-20` S5 (a role's `budget` widening as it rises, its §8 F8 (ii)) waits on that. This
unit adds one scalar direction word to the row grammar, `rises-only`: a greater number widens and is
admitted, a lesser one is refused naming the field, and a value that is no number is refused.

## 2. Scope (IN)

- **S1** — The declaration. `read_field_decl` (`tools/playbook/overlay_rows.py#read_field_decl`) admits
  a scalar's `widens` as either an order of two or more distinct values, as today, or one word of
  `SCALAR_DIRECTIONS`, a tuple `tools/playbook/row_checks.py` declares beside `REF_ROLES`. This unit puts
  `rises-only` in it. Any other string still refuses as declaring no direction, and its red names the
  words. Observed by AC4.
- **S2** — The classifier. `derive_patch_class` (`tools/playbook/row_checks.py#derive_patch_class`)
  reads a `rises-only` operation through `derive_number`, a new function of the same module: an integer
  that is no boolean, or a string of decimal digits, read as its integer; anything else is no number. A
  new value greater than gov's widens; equal is no operation; lesser raises `ValueError` naming both
  values and the word, which `check_rows` turns into a red naming the row, the edge, gov's tag and the
  field, as it does a value outside an order. A new value that is no number raises the same way. Gov's
  own value that is no number ranks below every number, as gov's value outside an order does. Observed
  by AC1, AC2 and AC3.
- **S3** — Both edges. A `supersedes` that lowers a `rises-only` field is refused as an `amends` is,
  since `derive_entry_ops` (`tools/playbook/row_checks.py#derive_entry_ops`) already writes the
  changed scalar as a `set` operation. Observed by AC2.
- **S4** — The page. `help/overlay-rows.md`, section "What you may not change, and how a widening is
  reported", names `rises-only` beside the set directions and the ordered scalar, and adds a lowering
  of one to the refusal list; the docstrings of `overlay_rows.py` and `row_checks.py` name it. Observed
  by AC5.

## 3. Non-goals (OUT)

- Declaring any field `rises-only`. `budget` on `tools/roles/role-row-schema.toml` is
  `TOOL-dBoundRoles-20` S5's file and row; the item kind's `deadline` and `on-deadline` stay fixed
  (`tools/loop/item-schema.toml@829f39a6:61-64`) until TOOL-dDeclaredLoop-33's own fork opens them.
- A two-way numeric direction, where a lesser number narrows and is admitted: TOOL-dWitnessedBar-28 S4
  specs one as `rises` for a gate leg's `ceiling`, and the ask TOOL-dDeclaredLoop-114 asks one as
  `raise` for durations. Neither is this ask's, and neither word is minted here (§8 F1).
- Durations, units or a policy-tag value compared at its value.

`TOOL-dBoundRoles-20` consumes this unit through
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`, which binds the relation over
that spec: S5 declares `budget` on its role row schema with `widens = "rises-only"`, and a lowering patch then meets
the refusal naming `budget`.

### Edges

- **hands-off** external — TOOL-dWitnessedBar-28 S4: `SCALAR_DIRECTIONS` and `derive_number`, the tuple its `rises` and `changes` join and the number reader its `rises` reuses, rather than a second reader

## 4. Design

### Evidence

Read at HEAD `4b7916726`, whose `tools/` tree equals base `318e20c9`'s:

- `read_field_decl` refuses a scalar `widens` that is no list of two or more distinct values, its red
  `widens <value> declares no direction: a scalar widens along an order of at least two distinct
  values`. The gap, probed in-process: `read_field_decl` over a scalar `budget` with `widens = "rise"`
  returns that red, and with `widens = ["low", "high"]` returns none.
- `derive_patch_class` handles `add` and `remove`, then reads a scalar's `order = decl["widens"]` with
  `order.index`, so a word would be read as a sequence of characters.
- `check_rows` calls `derive_patch_class` for each operation of an applied edge on a field declaring
  `widens`, turns its `ValueError` into `row-checks: red · widens · <row> <edge> <gov> · field <f> ·
  <message>`, and appends every other result to `operations` (`tools/playbook/row_checks.py#check_rows`).
- `FIELD_KEYS` (`tools/playbook/overlay_rows.py@b7c1062b:77`) already holds `widens`, so no schema key
  is added; `PATCH_KEYS` stays the set directions.
- A role's `budget` is a decimal string in its front matter (`tools/roles/agents/gov-builder.agent.md`,
  `budget: 8212`), and `TOOL-dBoundRoles-81` prints it raw; an overlay row written in TOML holds an
  integer.

### The classifier's new arm

```python
SCALAR_DIRECTIONS = ("rises-only",)        # TOOL-dBoundRoles-84 adds "changes"

def derive_number(value):                   # None for no number
    if isinstance(value, bool): return None
    if isinstance(value, int): return value
    if isinstance(value, str) and value.isdecimal() and value.isascii(): return int(value)
    return None

# in derive_patch_class, before the order arm:
if order == "rises-only":
    new, old = derive_number(value), derive_number(gov_value)
    if new is None: raise ValueError(f"value {value!r} is no number, which a rises-only field holds")
    if old is not None and new == old: return None
    if old is not None and new < old:
        raise ValueError(f"value {value!r} is below gov's {gov_value!r}: a rises-only field is never lowered")
    return "widens"
```

The block is the design's shape; the pass fits it to the module. A word of `SCALAR_DIRECTIONS` this
unit does not handle is unreachable, since `read_field_decl` admits only the words the tuple holds and
each word's unit adds its own arm. `TOOL-dBoundRoles-84` adds `changes` to the same tuple; whichever of
the two lands first mints it, and the other adds its word.

### Inventory

Minted: `SCALAR_DIRECTIONS` (shared with unit 84, §4 above), the direction word `rises-only`,
`derive_number`, and the fixture field `reach` with the plants `rises-raise`, `rises-text`,
`rises-lower`, `rises-word` and `rises-unknown`. The function name is asked of
`python tools/lexicon/lexicon.py --suggest derive_number --as py.function` at the pass.

### Migration

None: no schema in the tree declares a word today, so every composition reads as before.

### Rollout

Live at landing. Units 81, 83 and 84 hold the same order and each writes
`tools/playbook/overlay_rows.py`, and 83 and 84 write `tools/playbook/row_checks.py` too, so the
declared write sets intersect and `--dispatch` refuses a second pass while the first is open (M6
condition 1).

### Files touched (estimate)

- `tools/playbook/overlay_rows.py` (`read_field_decl`, the module docstring)
- `tools/playbook/row_checks.py` (`SCALAR_DIRECTIONS`, `derive_number`, `derive_patch_class`, the docstring)
- `tools/playbook/fixtures/row_kind.py` (the field `reach`, the plants)
- `tools/playbook/render_playbook.py` (the selftest rows running the plants)
- `help/overlay-rows.md`

### Alternatives rejected

- **An order listing every allowed value.** `budget` is open; no finite list holds it.
- **A new schema key such as `floor`.** `widens` already answers "which way does this field open", and a
  second key is a second answer to one question.

## 5. Production-readiness checklist

- security — narrows nothing and widens nothing by itself: the word opens a field only where a schema
  declares it, and the field still refuses a lowering.
- perf / scale — one integer compare per operation.
- error / empty / loading states — a lowering, a non-number and an unknown word each refuse naming the
  field; gov's own non-number reads below every number.
- observability — the refusal names the row, the edge, gov's tag, the field and both values; a raise is
  listed by `derive_widenings` with gov's value.
- risks — a decimal string and an integer compare as numbers, so `"8212"` and `8212` are one value; a
  string with a sign or a decimal point is no number and refuses.
- testing — AC1 to AC5 by the fixture plants, a grep and the selftest arm of §7 at the close.
- migration — none.
- user docs — `help/overlay-rows.md` per S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/fixtures/row_kind.py --plant rises-raise` runs, gov's
  `fixture.beta` carrying `reach = 4` and the overlay amending it to `8`, it exits 0, prints
  `fixture.beta`'s row with `reach` 8, and lists the operation `reach 4->8 widens`; `rises-text`, gov's
  value the string `"4"`, prints the same.
  Red when: a raise of a `rises-only` field is refused, or a decimal string is read as no number.
- **AC2** — When the plant `rises-lower` amends `reach` to `2`, it exits 1 with a `row-checks: red ·
  widens` line naming `fixture.beta`, `field reach` and `never lowered`; a `supersedes` writing `reach
  = 2` refuses the same way.
  Red when: a lowering composes, classified `narrows`.
- **AC3** — When the plant `rises-word` amends `reach` to `"wide"`, it exits 1 naming `field reach` and
  `is no number`.
  Red when: a non-number value composes on a numeric direction.
- **AC4** — When the plant `rises-unknown` writes `widens = "falls"` on `reach`, it exits 1 naming
  `field reach`, `declares no direction` and `rises-only`.
  Red when: an unknown word is admitted as a direction.
- **AC5** — When `grep -n "rises-only" help/overlay-rows.md` runs, it prints the line naming the
  direction and the line naming the lowering refusal.
  Red when: the page does not say a field may rise and never fall.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 AC4 · the five `rises-` plants of `tools/playbook/fixtures/row_kind.py`, staged by classifying a lesser value `narrows` · none

## 8. Open questions

- **F1 — Which word, and is a lowering refused or classified?** Options: (a) `rises-only`, a lowering
  refused, distinct from the two-way `rises` TOOL-dWitnessedBar-28 S4 specs; (b) `rises` with a
  lowering refused; (c) `rises` with a lowering classified `narrows` and admitted. (c) fails the ask's
  accept clause, which refuses a lowering (veto 1); (b) gives dWitnessedBar's planned `rises` the
  opposite meaning, so its gate leg `ceiling` could never be lowered, another build's public surface
  changed beyond this ask (veto 2). RESOLVED (agent, 2026-11-23, delegated): (a), rung 3. options:
  (a) · pick: (a) · admitted-by: principle.p18 · widens: the row grammar's scalar directions, by
  `rises-only` · relaxes: none
- **F2 — Which values read as a number?** Options: (a) an integer that is no boolean, or a string of
  ASCII decimal digits; (b) integers only. Gov's `budget` is a front-matter string
  (`TOOL-dBoundRoles-81` §4 "The row form"), so (b) refuses every patch of a gov role's budget.
  RESOLVED (agent, 2026-11-23, delegated): (a), rung 3. options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-23 · initial draft, from the brief
  `2026-11-23-prompt-TOOL-dBoundRoles-82-spec-brief` and the owner's ruling
  `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling`, closing `TOOL-dBoundRoles-78`.

## 10. Reuse audit

The seams extended are the field reader `tools/playbook/overlay_rows.py#read_field_decl` and the
classifier `tools/playbook/row_checks.py#derive_patch_class`, with `check_rows`' existing turn of a
classifier `ValueError` into a named red; no new refusal path is added. `python
tools/codebase-map/reuse_lookup.py "a scalar field whose overlay patch may raise its number and never
lower it"` ranked `field`, `OverlayRefused`, `read_overlay` and `declared_scalar`, none a numeric
direction, so no existing seam fits beyond those two functions. The recall probe found the ask
`TOOL-dBoundRoles-78`, TOOL-dWitnessedBar-28's spec, which designs `rises` and `changes` for the same
two functions and is unbuilt (status DEFERRED), and the ask TOOL-dDeclaredLoop-114 for `raise`; the
first decided F1's spelling, and the tuple and number reader are shaped for both to reuse.

Recall terms used: `python tools/memory-recall/query.py "how can a scalar field widen as its number rises" --terms "scalar widens order direction rising budget numeric widening classifier read_field_decl derive_patch_class narrows"`
