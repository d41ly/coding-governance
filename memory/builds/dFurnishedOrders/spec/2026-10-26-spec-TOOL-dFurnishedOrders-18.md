# TOOL-dFurnishedOrders-18 — the work order selecting instruction units by `feature.*`, and its code-notes slot filled from the tag's bundle as `annotations.delivery` says

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 18 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0209@97727c41 whole

**Carries:** node:policy-key.annotations.delivery

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |

<!-- /gen:spec-records -->

## 1. Goal

Orienting on one feature, `roles`, took about 42 calls and 734 KB read whole, and its bare name hit
44 code files of which 16 were real readers (night pass, point 4,
`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:231-272`). The
design answers it by attaching instructions and notes to a feature's tag: "pulling a feature's tag
brings its instructions with its regions". This unit makes the work order select its instruction
units by `feature.*` once dLinkedLibrary arms that selector, and fills the order's code-notes slot from
the tag's bundle, delivered in the work order, on demand or not at all as `annotations.delivery` says.

## 2. Scope (IN)

- **S1** — The feature arm of the load set. `derive_load_set(units, reader, item=None, features=())`
  (PLAY-dOrderedCharter-11 S1, `tools/playbook/load_sets.py`) selects a unit whose `scope` carries a
  `feature.<name>` tag in `features`. While the namespace registry `tools/playbook/namespaces.toml`
  (PLAY-dOrderedCharter-19 S2) holds no `feature` row, the feature part selects nothing and reports
  `unarmed — feature.*: no feature namespace is registered`, never empty and green, as that unit's item
  part reports an unregistered selector. The `derive` verb takes `--feature <tag>`, repeated, and
  prints one `feature · <unit tag> · <text>` line per unit its feature part selects, `<text>` the
  unit's `text` field (PLAY-dOrderedCharter-9 S1), or its `unarmed` line. Observed by AC1.
- **S2** — The work order's feature units. `render_order_instructions(root, role, item, features)` in
  `tools/roles/handoff.py`, called by `render_handoff` (`:312`) for a work order cut with `--item`
  (TOOL-dBoundRoles-3 S1), runs `load_sets.py derive --reader <role> --item <tag>` with one `--feature`
  per feature, found through `roles_lib.resolve_kit_dir("playbook", "load_sets.py", KIT_DIR)`, and
  renders the units its feature part added in an `### instructions` block, as `instructions.slices`
  says: under `handed` one `- <unit tag> · <text>` line per unit, under `pointer` one
  `- <unit tag> · python tools/playbook/gov_tag.py show <unit tag>` line, never the unit's text. The key
  is read once per render through `read_policy_setting("instructions.slices", root)`
  (TOOL-dBoundRoles-21 S1), as TOOL-dFurnishedOrders-8 S4 reads it. The block renders through
  `render_slot("instructions", state, body)` (TOOL-dFurnishedOrders-4 S1), whose closed `ORDER_SLOTS`
  gains `instructions`: `filled` when a unit is added, `searched-empty` when the
  feature part is armed and adds none, `not-installed: <why>` when it reports `unarmed`, the order
  carries no feature, or no playbook kit resolves. Observed by AC2 and AC3.
- **S3** — The order's features. `render_handoff` passes `features=()` until dLinkedLibrary's house
  index lands and hands an item's feature tags; the hand-over is that index's reader filling the
  argument, and no flag lets a caller type features in its place. With none, S2 renders
  `not-installed: no feature tags for this order; dLinkedLibrary's house index hands them`. Observed by
  AC3.
- **S4** — The code notes from the bundle. `read_code_notes(root, features)` in `handoff.py` returns
  the `(rows, rest)` pair TOOL-dFurnishedOrders-11's `render_code_notes_slot(rows, rest)` renders into
  `### code-notes` under its `CODE_NOTES_BYTES` cap: for each feature in order it runs
  PLAY-dOrderedCharter-25 S1 and S3's `python tools/playbook/gov_tag.py bundle <tag> --inline --bytes
  2048`, each printed row one entry of `rows`, and `rest` names the query by tag,
  `python tools/playbook/gov_tag.py bundle <tag>` per feature, where the rows past the cap are read
  (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:217-218`). The cut to
  the cap is unit 11's `derive_slot_cut`, whole rows only; this unit cuts nothing a second time. No
  feature, no `gov_tag.py` resolved or a bundle refusal returns `rows` as None, which that renderer
  reads `not-installed`; armed features whose bundles print no row return an empty list, read
  `searched-empty`. Observed by AC4.
- **S5** — `annotations.delivery`, read once per render through `read_policy_setting` with its
  catalogue row `tools/policy/catalogue.toml:1349-1353`, default `work-order`, as the default when
  the setting reads None. Under `work-order` the block holds S4's rows. Under `on-demand` `rows` is the
  `rest` lines themselves, so the block hands the query by tag and inlines nothing. Under `off`
  `render_handoff` does not call `render_code_notes_slot` and the work order carries no
  `### code-notes` block. Observed by AC5.
- **S6** — The docs. `tools/roles/README.md`'s handoff section and `help/roles.md`'s "How a task
  reaches an agent" name the `### instructions` and `### code-notes` blocks, the three delivery values
  and the dLinkedLibrary hand-over. Observed by AC6.

## 3. Non-goals (OUT)

- Registering the `feature` namespace, the `gov:feature` and `gov:note` annotations and the house index
  that maps an item's seed to its features: dLinkedLibrary's. This unit reads the selector and the
  features once they exist and builds neither.
- The bundle verb, its fold and its inline budget semantics: PLAY-dOrderedCharter-25. The load-set
  deriver, its other selectors and its refusals: PLAY-dOrderedCharter-11.
- The code-notes slot's head, `render_code_notes_slot`, its 2 KB cap and `derive_slot_cut`:
  TOOL-dFurnishedOrders-11. This unit passes the slot its rows.
- The protocol slices under `### Method slices` and the key's catalogue row: TOOL-dFurnishedOrders-8.
  This unit reads the key for the feature units it adds.
- `annotations.lookup` and the read hook under `annotations.grammar: pushed-at-read`: dLinkedLibrary's.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-8` — `instructions.slices`, whose `handed` or `pointer` value decides how each feature-selected unit is rendered into the order; without it the block has no rendering rule
- **consumes-from** `TOOL-dFurnishedOrders-11` — `### code-notes`, the slot and its 2 KB cap, rendered by `render_code_notes_slot` from the rows S4 reads off the tag's bundle; without it the notes have no slot and no cap
- **consumes-from** `TOOL-dFurnishedOrders-4` — `render_slot`, the one renderer of the `### instructions` and `### code-notes` state lines
- **consumes-from** external — PLAY-dOrderedCharter-11 S1's `derive_load_set` and its `derive` verb; PLAY-dOrderedCharter-25 S1 and S3's `gov_tag.py bundle --inline --bytes`; PLAY-dOrderedCharter-19 S2's `namespaces.toml`; TOOL-dBoundRoles-3 S1's `--item`; TOOL-dBoundRoles-23 S1's `FRAME_SLOTS`
- **hands-off** external — dLinkedLibrary: registering `feature` and handing each order's feature tags to `render_handoff`, which arms S1 to S4 with no change here

## 4. Design

### The flow

```
render_handoff --item <tag>
  features = ()                                    S3: dLinkedLibrary fills this
  render_order_instructions(root, role, item, features)
    load_sets.py derive --reader <role> --item <tag> [--feature <t>]...
      -> the feature part: unit tags | "unarmed — feature.*: <why>"
    -> ### instructions   slot instructions · filled | searched-empty | not-installed: <why>
  annotations.delivery
    work-order -> read_code_notes(root, features) -> (rows, rest)
                    gov_tag.py bundle <t> --inline --bytes 2048    per feature, in order
    on-demand  -> rows = rest, one "python tools/playbook/gov_tag.py bundle <t>" line per feature
    off        -> no block
    -> render_code_notes_slot(rows, rest)    unit 11: ### code-notes, cut by derive_slot_cut
```

### The blocks

```
### instructions

slot instructions · not-installed: no feature tags for this order; dLinkedLibrary's house index hands them

### code-notes

slot code-notes · not-installed: no code-notes source; the tag's bundle fills this slot
```

Both sit in `## Task`, so the task-sha covers them. `### instructions` sits in TOOL-dBoundRoles-23's
`boundaries` slot beside the charter rule blocks, since a unit instructs; `### code-notes` sits where
TOOL-dFurnishedOrders-11 places it. A feature-selected unit already in the role's static block is not
repeated: the derive call returns the item's set, and S2 renders only the units its feature part adds.

### One cap, one cut

Each bundle is asked for at most the slot's whole cap, so no single bundle can print more inline
content than the slot holds, and the bundle never cuts a range mid-content (PLAY-dOrderedCharter-25
S3). Across features the rows are concatenated in feature order and cut once, by unit 11's
`derive_slot_cut` inside `render_code_notes_slot`, which keeps whole rows and names `rest` on its cut
line. The cap is spelled once, as `CODE_NOTES_BYTES`; the literal `2048` on the bundle call reads it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `features` | keyword argument of `derive_load_set` | none |
| `--feature` | flag of `load_sets.py derive` | none |
| `render_order_instructions`, `read_code_notes` | functions in `handoff.py` | `py.function`, OK |
| `instructions` | member of `ORDER_SLOTS`, the `### instructions` block head | none |

### Migration

None stored. A work order rendered before this unit carries neither block.

### Rollout

Live at landing; both blocks read `not-installed` until dLinkedLibrary lands, and arm with no change
here when its reader hands features.

### Files touched (estimate)

- `tools/playbook/load_sets.py`
- `tools/roles/handoff.py`
- `tools/roles/roles_lib.py`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `help/roles.md`

### Alternatives rejected

- **A `--feature` render flag the driver types.** It has the driver type what the house index derives,
  the `[derive]` rule's defect, and adds a public flag no clause names.
- **The order's features derived now from the tag index's `feature` rows whose sites meet the seed.**
  That is the house index's relation, dLinkedLibrary's mechanism, which the brief forbids building here.
- **A running budget split across features here.** It is a second cut beside unit 11's
  `derive_slot_cut`, two rules for one cap.

## 5. Production-readiness checklist

- security — no new write path; the bundle's content is the repository's own bytes, which the role
  could read anyway; the inline budget bounds what a render pulls.
- perf / scale — one `derive` subprocess and at most one `bundle` subprocess per feature per render,
  none until features exist.
- error / empty / loading states — `filled`, `searched-empty` and `not-installed: <why>` for both
  blocks; `off` renders no code-notes block by the owner's choice.
- observability — each state line names its reason; the absent policy kit prints one note line.
- risks — a feature-scoped unit that duplicates a static-block unit; S2 renders only the units the
  feature part adds.
- testing — AC1 to AC6 by fixtures of the load-set deriver and the renderer; the arms of §7 at the
  close.
- migration — none.
- user docs — `help/roles.md` names both blocks and the delivery values (S6).

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `load_sets.derive_load_set` over a fixture registry holding a unit
  scoped `feature.roles`, with `features=("feature.roles",)`, the unit is selected once a planted
  `namespaces.toml` declares a `feature` row, and without that row the call selects nothing and its
  report carries `unarmed — feature.*`.
  Red when: an unregistered selector reads as an empty set, so "no feature units" passes green.
- **AC2** — When `python -c` calls `handoff.render_order_instructions` over the same fixture with
  `features=("feature.roles",)` and `instructions.slices` set to `pointer`, the returned block opens
  `### instructions`, reads `slot instructions · filled` and holds the unit as a pointer; with `handed`
  it holds the unit's text.
  Red when: the block hands the unit whole under `pointer`, or ignores the key.
  fixture: TOOL-dFurnishedOrders-8's slice rendering, built before this unit's pass in build order.
- **AC3** — When `python handoff.py render --role gov-builder --build tFix --unit TOOL-tFix-1 --item
  item.build.unit-pass --stdout` runs in a scratch adopter, its `## Task` holds `### instructions` with
  `slot instructions · not-installed: ` naming dLinkedLibrary, and `### code-notes` with
  `slot code-notes · not-installed: `.
  Red when: either block is absent or reads `searched-empty`, so a role reads "nothing applies" from a
  selector nobody armed.
- **AC4** — When `python -c` calls `handoff.read_code_notes` with two planted features whose
  `gov_tag.py bundle` fixture rows exceed 2048 bytes together, and passes its pair to
  `render_code_notes_slot`, the block reads `slot code-notes · filled`, holds whole rows of both
  features in feature order within 2048 bytes, and its cut line names the two `gov_tag.py bundle`
  queries; with no feature the pair renders `not-installed`.
  Red when: the rows are cut a second time here, or a row is split, so the slot hands half a range.
  fixture: PLAY-dOrderedCharter-25's `--fixture --plant` repository, built before this build run.
- **AC5** — When AC4's render runs under `annotations.delivery = "on-demand"`, the block holds one
  `gov_tag.py bundle` query line per feature and no inlined content; under `off` the work order carries
  no `### code-notes` head; under the default it inlines as AC4 says.
  Red when: `off` still delivers notes, or `on-demand` inlines them.
- **AC6** — When `grep -n 'code-notes' README.md` runs in `tools/roles/` and
  `grep -n 'annotations.delivery' help/roles.md` runs at the root, each names the block and the three
  delivery values.
  Red when: a role reads a block no page explains.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/load_sets.py · covers AC1 · its selftest plants a `feature`-scoped unit with and without a registered `feature` row, staged by a selector that reads unregistered as empty · none
New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC4 AC5 · a work order cut with no features, and the notes read over planted bundles under each delivery value, staged by a reader that splits a row at the cap and by `off` still rendering the block · none

## 8. Open questions

- **F1 — Where does a work order's feature list come from before dLinkedLibrary lands?** Options:
  (a) nowhere: `render_handoff` passes none and both blocks read `not-installed`, the house index's
  reader filling the argument at its landing; (b) derived now from the tag index's `feature` rows whose
  sites meet the item's seed; (c) a `--feature` render flag. (b) builds the house index's relation,
  a later build's mechanism the packet's Non-goals keep out; (c) has a caller type what the design
  derives and adds a public surface no clause names, veto 2. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the clause's own "once dLinkedLibrary arms that selector". widens: none · relaxes: none
- **F2 — Who arms `feature.*`, dLinkedLibrary or dTotalRecall?** The night pass says dTotalRecall
  registers the namespace (night-pass.md:268-269) and PLAY-dOrderedCharter-25 §3 repeats it; the
  clause says dLinkedLibrary. RESOLVED (agent, 2026-10-26, delegated): the clause, rung 1; S1 keys on
  the registry row, not on its author, so either build's landing arms it. widens: none · relaxes: none
- **F3 — Where do feature-selected units render?** J4's eight block heads, `ORDER_SLOTS` in
  TOOL-dFurnishedOrders-4 S1, hold no instruction slot. Options: (a) a ninth point, `instructions`,
  added to `ORDER_SLOTS` and rendered by `render_slot` in the frame's `boundaries` slot; (b) inside the
  role's static block through `render_static_block`; (c) appended to the charter rule blocks. (b) is
  per role and cannot vary by item; (c) gives one block two sources and no state line. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the way TOOL-dFurnishedOrders-11 S6 widens the same renderer's
  state set; the point is named to the main loop as an addition to J4's list. widens: none ·
  relaxes: none
- **F4 — What does `off` render?** Options: (a) no block, the owner's "not at all"; (b) a
  `not-installed` line naming the key. (b) calls a chosen policy an absent component.
  TOOL-dFurnishedOrders-11 S2 puts the block "in every work order"; the clause's `off` narrows that.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1357's values read as the clause words them;
  the disagreement with unit 11's sentence is named to the main loop. widens: none · relaxes: none
- **F5 — The parents this unit calls.** PLAY-dOrderedCharter-11, -19 and -25, TOOL-dBoundRoles-3 and
  -23 are specced and unbuilt at base `2193e25d`. RESOLVED (agent, 2026-10-26, delegated): the build
  run re-grounds on each section and stops the unit if one is still absent then, rung 1, the brief's
  rule for every deferred parent. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 18, the brief's J4, J15 and J19, scout
  B's row for cl-0209, night-pass.md:231-272, systems.md:200-220 and :325-370, PLAY-dOrderedCharter-11
  and -25, and `tools/roles/handoff.py` at base `2193e25d`.

## 10. Reuse audit

The seams extended: PLAY-dOrderedCharter-11's `derive_load_set`, which already reports an unregistered
selector `unarmed` and gains the feature arm beside its item arm; PLAY-dOrderedCharter-25's `bundle`
verb, whose `--inline --bytes` bounds each bundle by the slot's cap; TOOL-dFurnishedOrders-11's
`render_code_notes_slot` and `derive_slot_cut`, which render and cut the rows this unit reads, so the
cap has one cut; `render_handoff`'s blocks list
(`tools/roles/handoff.py:381-416`) and `roles_lib.resolve_kit_dir`, the roles kit's one route to a
sibling kit. `python tools/codebase-map/reuse_lookup.py "select instruction units for a work order by a
feature tag and fill a notes slot from a bundle"` ranked only stem matches (`note`, `units`,
`check_rule_tags`, `derive_int_slots`), none of them a selector or a notes reader; nothing at base
selects by tag or reads a bundle, so the two functions in `handoff.py` are new around the parents'
verbs. Scout B's row agrees with source: `annotations.delivery` exists only as its catalogue row
(`tools/policy/catalogue.toml:1350`). The recall probe returned the brief's and scout B's rows,
PLAY-dOrderedCharter-25's H1 and v2:1760; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how are a work order's code notes and
feature-scoped instructions delivered" --terms "feature selector instruction units load set code-notes
bundle annotations.delivery gov:note tag"`
