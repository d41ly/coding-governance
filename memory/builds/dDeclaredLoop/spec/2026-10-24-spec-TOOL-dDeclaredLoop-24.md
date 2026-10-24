# TOOL-dDeclaredLoop-24 — the `item` kind in the kinds register, its factory, and the checks over the composed items

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 11 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0109@48e119fc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

The flow's items become a registered kind, `kind.item`, with a factory, a row schema and a gate, so a
repository can add an item to a gov step or patch one of gov's, and every check reads the composition
of gov's items with the repository's at the landed revision, never the overlay text (FA-1, FA-2,
FA-5). Today an adopter cannot add an item to a step or change one of gov's (`gap-flow-19`): no item
kind exists, and the unattended run's extra definition-of-done items are attested facts. The
mechanism is the parents': dOrderedCharter-7's kinds register and factory verb, dOrderedCharter-35's
overlay rows, dOrderedCharter-36's row checks and dSafePassage-10's step gate. This unit registers the
kind, declares its schema and fixed set, and adds the item-specific checks the clause lists.

## 2. Scope (IN)

- **S1** — The kind row: one `[[kind]]` in `tools/playbook/kinds.toml` (dOrderedCharter-7 S4),
  `tag = "kind.item"`, `owner = "dDeclaredLoop"`, `binds` the principles P1, P2, P20 and P24, its
  `population` the `[[item]]` rows of `tools/loop/loop.toml` and of a repository's overlay, its
  `factory`, its `gate` the leg `loop item kind`, and `schema = "tools/loop/item-schema.toml"`
  (dOrderedCharter-35 S10). Observed by AC1 and AC2.
- **S2** — The schema, `tools/loop/item-schema.toml`: its `[kind]` table (`name = "item"`,
  `owner-seat` the segment after the step, so a repository row is `item.<step>.adopter.<name>`), each
  field's `shape`, `ref` role and either `fixed-by` or `widens` (dOrderedCharter-36 S1), and
  `[[fixed-row]]` for every floor item and every step's exit item, whole. In any gov item the `tag`,
  `step`, `witness` and `outcomes` are fixed; `needs` is a constraint set, widening as it shrinks; every
  other open field declares its direction (§4). Observed by AC5 and AC7.
- **S3** — The composition: gov's `[[item]]` rows and the overlay's composed by dOrderedCharter-35's
  `compose_rows` at the landed revision dOrderedCharter-46 S1 defines, so a gov item's `needs` and
  `routes` change only through a pinned `amends` patch (dOrderedCharter-35 S3, S6), and every check of
  S4 and dOrderedCharter-36's `check_rows` runs over the composition. Observed by AC9.
- **S4** — The item checks, `check_item_composition(composition, schema)` in
  `tools/loop/loop_items.py`, each a refusal naming the item: the needs graph acyclic, through
  `TOOL-dDeclaredLoop-12`'s `find_cycles` (I14), with every need resolving to an active item; every
  input naming a record at a version produced by an item in its needs closure whose `returns` names
  that record at that version; and each record's version moved whenever its meaning moves, held by a
  pinned hash per version. Observed by AC3 and AC4.
- **S5** — The fixed set and exclusion refusals the clause plants, through dOrderedCharter-36 S3 and
  S4 on this kind's rows: a patch of a gov item's `witness` or `outcomes`; a `supersedes` of a floor
  item and of an exit item; an exclusion of an item another active item needs, naming the requirer;
  and an exclusion of an item `review.breakpoints` names, naming the key. Observed by AC5 and AC6.
- **S6** — The factory, `python tools/loop/loop_items.py new <name> --step <step> --actor <kind:name>
  --witness-by <text> --owner <build>`, run by dOrderedCharter-7 S6's `python tools/playbook/core.py
  new item <name> …`: it appends a gov `[[item]]` row that the gate passes. Observed by AC1.
- **S7** — Item tags joined to dSafePassage's step gate (I16): a `[[class]]` row `item` in
  `tools/govkit/surface-classes.toml` (dSafePassage-10 S1), its reader the composed item tags, its
  plant one vanished gov item, and its own-record witness the change records (I13) naming a vanished
  tag's successor (dSafePassage-10 S4). Observed by AC8.
- **S8** — The gate leg `loop item kind`, running `loop_items.py check --selftest`, its `enforces`
  holding the kind's `binds` (dOrderedCharter-7 S2, S5), with the rows a new leg owes, and a section
  of `help/loop.md`. Observed by AC2 and AC10.

## 3. Non-goals (OUT)

- No item row and no field beyond the schema: the 61 rows and their keys are `TOOL-dDeclaredLoop-12`'s,
  the per-field declaration check `TOOL-dDeclaredLoop-9`'s, and the `upstream` field
  `TOOL-dDeclaredLoop-29`'s, which adds it to this schema.
- No overlay mechanism: rows, patches, pins, exclusions, the widening classifier and the change
  record's successor map are dOrderedCharter-35's and -36's, called and never re-specced.
- No step gate: dSafePassage-10's gate, reader contract and fixture; this unit adds one class row.
- No repository stage or splice row: `TOOL-dDeclaredLoop-25`'s, whose items are this kind's rows.
- No other kind's factory: `TOOL-dDeclaredLoop-6` follows this row's shape for seven more kinds.
- No record kind's factory: the record kind's own kind is dConvergedCharter's (foundations C4's
  assignment); this unit pins versions over the record factory's existing kind rows.
- No counted-edge or reachability rule: `TOOL-dDeclaredLoop-33`'s, beside the I14 helper.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-12` — `needs`, the declared dependencies of each item row, whose acyclicity check through the I14 helper the composition reads
- **consumes-from** `TOOL-dDeclaredLoop-9` — `item.<step>.<name>`, the declared item rows the `item` kind registers
- **consumes-from** `TOOL-dDeclaredLoop-13` — the `loop.toml` transition rows, whose exit items this unit's fixed set keeps whole
- **hands-off** `TOOL-dDeclaredLoop-6` — `kind.item`, the first of this build's kind rows with a factory and schema, whose row shape the six rows there follow
- **hands-off** `TOOL-dDeclaredLoop-25` — `kind.item`, the kind of a repository stage's items and its exit item, whose composition checks hold them as they hold a gov step's
- **hands-off** `TOOL-dDeclaredLoop-29` — `kind.item`, the item kind's schema file, to which that unit adds the `upstream` field
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 13, 14, each a scope item of that unit

## 4. Design

### The kind row

```toml
[[kind]]
tag = "kind.item"
owner = "dDeclaredLoop"
binds = ["principle.p1", "principle.p2", "principle.p20", "principle.p24"]
population = "python {prefix}/loop/loop_items.py members"
factory = "python {prefix}/loop/loop_items.py new"
gate = "loop item kind"
schema = "tools/loop/item-schema.toml"
```

P1 (one loop, declared once), P2 (witnessed hand-offs), P20 (the flow above the build) and P24 (the
checklist is a program) are the principles v2's enforcement table pins to this build's item clauses
(v2:1823-1846). The population is a reader command because the kind's rows live in two files.

### The schema

| Field | `shape` | `ref` | Class | Source of the class |
|---|---|---|---|---|
| `tag` | scalar | | fixed | `parser=tools/playbook/tag_index.py#extract_item` |
| `step` | scalar | | fixed | `principle=principle.p20` |
| `witness` | scalar | | fixed | `principle=principle.p2` |
| `outcomes` | set | | fixed | `principle=principle.p24` |
| `owner` | scalar | | fixed | `parser=tools/loop/loop_table.py#read_stand_ins` |
| `returns` | scalar | | fixed | `parser=tools/loop/loop_items.py#check_item_composition` |
| `needs` | set | `needs` | open, `widens = "remove"` | FA-5: a constraint set |
| `routes` | set of `<outcome>=<target>` | | open, `widens = "add"` | any changed pair adds one, so it reads widening |
| `actor` | scalar | `actor` | open, `widens = ["owner", "hook", "command", "executor", "role"]` | later is less witnessed |
| `inputs` | set | | open, `widens = "add"` | a permission set: what it reads |
| `allowance` | set | | open, `widens = "add"` | a permission set: what it writes |

`[[fixed-row]]` rows: the five exit items `TOOL-dDeclaredLoop-1`'s `[[step]]` rows name, each
`fixed-by = ["parser=tools/loop/loop_lib.py#read_steps"]`, and the floor item `item.test.verdict`,
`fixed-by = ["floor=floor.verdict-before-move"]`, whose witness the runner writes (FA-9's
"`test.verdict` and `entry.intake` among them",
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:202-203`).
`entry.intake` gains its fixed row when dPlacedRequest declares it as an item. A `floor=` source
resolves once the floor's tags are registered (dOrderedCharter-36 S2), and reads unarmed until then.

### Records at a version

An input that reads a record is written `<layer tag>:record-kind.<name>@<n>`, and `returns` is written
`record-kind.<name>@<n>`; an input naming no record kind is prose and joins nothing.
`[[record-version]]` rows in the schema file pin each record kind's current version:

```toml
[[record-version]]
kind = "record-kind.acceptance"
version = 1
fields = "5c0e9a14"   # hash8 of the record factory kind row's required fields, in canonical order
```

The check recomputes each `fields` hash from `tools/memory-tree/build_records.py`'s kind row. A hash
that moved while `version` did not is red: the record's meaning changed with no bump. A bump re-pins
the hash, and every input still naming the old version then reds the produced-input join until its
item is updated, which is how a meaning change reaches its readers.

### The checks, in order

1. Compose (dOrderedCharter-35 `compose_rows`); a composition finding refuses before step 2.
2. `check_rows(kind, schema, composition, exclude, policy)` (dOrderedCharter-36 S7): the fixed set,
   the exclusions and the widening classifier.
3. `check_item_composition`: needs resolve and are acyclic through `find_cycles`; each record input
   is produced in the needs closure at its version; each record version's hash holds.
4. The step gate's `item` class runs at a landing, over the composed tags at the base and the tip.

### The factory

`new` appends one row with every required field: `tag = "item.<step>.<name>"`, the given `step`,
`actor`, `owner` and `witness = { class = "history", by = <text> }`, `needs = []`, `outcomes =
["done"]` and `routes = { done = "<the step's exit item>" }`, and runs the gate over the result,
removing the row and exiting 1 when it does not pass. A name that would collide with a declared tag
exits 2.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `kind.item` | kind tag | none |
| `tools/loop/item-schema.toml` | schema file | none |
| `tools/loop/loop_items.py` | module | none declared for files |
| `check_item_composition` | function | `py.function`, OK |
| `read_item_members` | function | `py.function`, OK |
| `write_item_plant` | function | `py.function`, OK |
| `read_item_successors` | function | `py.function`, OK |
| `[[record-version]]` | table of the schema file | none |
| `item` | class row of `tools/govkit/surface-classes.toml` | none |
| `loop item kind` | leg | none |

### Migration

None: no repository row of this kind exists before it is registered.

### Rollout

Live on landing. A gov row the schema refuses reds the leg in this unit's build, which the build pass
fixes in the same unit.

### Files touched (estimate)

- `tools/playbook/kinds.toml`
- `tools/loop/item-schema.toml`
- `tools/loop/loop_items.py`
- `tools/loop/kit.toml`: the module, the schema file and the leg declared
- `tools/govkit/surface-classes.toml`: the `item` class row
- `tools/gate-legs.json`: the leg `loop item kind`, argv `python {prefix}/loop/loop_items.py check --selftest`, `enforces` the four principle tags
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/ceiling-evidence.txt`, the new leg's row
- `memory/map/features/loop.md`: the module's claim and the leg in its `gate-legs` list
- `help/loop.md`: the item kind's section

### Alternatives rejected

- **A second register for items.** The kinds register is the `kind` namespace's declaring source
  (dOrderedCharter-7 S4); a second one would be a kind outside the mechanism, which C3 refuses.
- **`routes` fixed.** The clause admits a pinned patch of a gov item's routes; a fixed field refuses
  every patch.
- **Versions on the record factory's rows.** The record kind's factory is dConvergedCharter's; pinning
  here reads the factory and writes nothing into it.

## 5. Production-readiness checklist

- security — every repository row reaches the composition through the overlay's one door, which
  carries the owner's proof (dOrderedCharter-15); the checks only refuse.
- perf / scale — about seventy rows composed once per check; one cycle scan.
- error / empty / loading states — an empty population reads red, as dSafePassage-10 S5 refuses an
  empty class; an unreadable overlay exits 2.
- observability — each refusal names the item, the field or the requirer, and the fixed-by source or
  the key.
- risks — the `actor` order is this unit's judgement of how witnessed each kind's act is (§8 F3), so
  a patch moving an actor reads widening only in that order.
- testing — the plants of §6 under the new leg, and the step gate's own fixture for the class row.
- migration — none.
- user docs — `help/loop.md` (S8).

## 6. Acceptance criteria

- **AC1** — When `python core.py new item demo --step step.test --actor command:demo --witness-by
  "the demo record" --owner dDeclaredLoop` runs in the fixture copy that `python loop_items.py
  --fixture --plant factory` builds, it appends `item.test.demo` and `check` exits 0; the same name run
  again exits 2.
  Red when: the factory writes a row its own gate refuses.
- **AC2** — When `python core.py kinds` runs on the built tree, it passes `kind.item`, its gate leg's
  `enforces` holding the four tags of `binds`; and `python -c` printing each row of
  `tools/gate-legs.json` whose `name` is `loop item kind` shows `enforces`.
  Red when: the kind row names a gate leg that does not enforce its principles.
- **AC3** — When `python loop_items.py --fixture --plant repo-cycle` runs, whose overlay adds
  `item.test.adopter.a` needing `item.test.adopter.b` needing the first, `check` exits 1 naming the
  cycle; `--plant repo-unresolved-need`, a repository item needing `item.test.nosuch`, exits 1 naming
  it.
  Red when: the needs graph is read without the repository's rows.
- **AC4** — When the fixture runs with `--plant repo-input-unproduced`, a repository item reading
  `layer.memory:record-kind.acceptance@1` with no needed item returning it, `check` exits 1 naming the
  input; `--plant version-unbumped`, the acceptance kind's required fields changed at version 1, exits
  1 naming `record-kind.acceptance`; the same with the version bumped and re-pinned exits 0.
  Red when: a record's fields change and no version moves.
- **AC5** — When the fixture runs with `--plant patch-witness` and `--plant patch-outcomes`, each an
  `amends` of a gov item's fixed field, and with `--plant supersede-floor` on `item.test.verdict` and
  `--plant supersede-exit` on `item.build.exit`, each composition is refused naming the row and its
  `fixed-by` source.
  Red when: a fixed field or row of a gov item is patched or replaced.
- **AC6** — When the fixture runs with `--plant exclude-needed`, excluding `item.test.select` that
  `item.test.verdict` needs, the composition is refused naming `item.test.verdict`; with
  `--plant exclude-breakpoint`, excluding an item `review.breakpoints` names, it is refused naming the
  key `review.breakpoints`.
  Red when: an exclusion leaves a need or a breakpoint pointing at nothing.
- **AC7** — When the fixture runs with `--plant patch-remove-need`, the classifier reads it `widens`
  and `derive_widenings` lists it, and `--plant patch-add-need` reads `narrows`.
  Red when: `needs` is classified as a permission set, so removing a need reads narrowing.
- **AC8** — When `python step_gate.py --fixture --plant item` runs over a clone whose tip drops a gov
  item's tag, it exits 1 naming `item:<tag>`; with `--with-row`, a change record naming the tag's
  successor, it exits 0.
  Red when: a vanished item tag passes the step gate with no successor recorded.
  fixture: dSafePassage-10's gate and fixture, landed before this build's build run.
- **AC9** — When the fixture runs with `--plant amended-cycle`, whose overlay text is acyclic and whose
  `amends` adds a need that closes a cycle in the composition, `check` exits 1 naming the cycle.
  Red when: the checks read the overlay text rather than the composition.
- **AC10** — When `grep -n '"loop item kind"' tools/gate-legs.json` runs, it finds the leg row and its
  argv naming `loop_items.py check`, and `grep -n 'kind.item' loop.md` in `help/` finds the section.
  Red when: the leg row is absent or names another command, so no bar runs the check.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `playbook render selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_items.py · covers AC1 AC3 AC4 AC5 AC6 AC7 AC9 AC10 · the `loop item kind` leg, its failing case staged by the `repo-cycle` plant · none

New arm: tools/govkit/step_gate.py · covers AC8 · the step gate's own fixture over the `item` class row, its failing case the class's plant · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24: the tuple
  does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED (agent,
  2026-10-24, delegated): `OPEN`.
- **F2 — How does an input name the record it reads at a version, when `TOOL-dDeclaredLoop-12` writes
  inputs as `<layer tag>:<what>` and `returns` without a version?** Options: (a) a record input written
  `<layer tag>:record-kind.<name>@<n>` and `returns` written `record-kind.<name>@<n>`, prose inputs
  joining nothing; (b) a separate `reads` field. (b) is a second field for one fact. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3, this unit owning the kind's schema; returned to
  `TOOL-dDeclaredLoop-12`'s writer, whose rows take the `@<n>` suffix.
- **F3 — Which direction widens `actor` and `routes`, which dOrderedCharter-36 S5's three forms do not
  name?** Options: (a) `actor` an ordered scalar from the most to the least witnessed kind, `routes` a
  set of pairs whose every change reads widening; (b) both fixed. (b) refuses the pinned patch of
  routes the clause admits. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
- **F4 — Which items are floor items?** v2's floor names invariants, and the adoption record names
  `test.verdict` and `entry.intake` as items whose witness a runner or a hook writes. RESOLVED (agent,
  2026-10-24, delegated): `item.test.verdict` here, `entry.intake` when its build declares it, rung 1.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 24, the flow adoption record's FA-1,
  FA-2 and FA-5 paragraphs, and the parents' landed specs at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

The seams extended are the parents' specced mechanisms, each cited by section above: the kinds
register and `new` verb (dOrderedCharter-7 S4-S6), `compose_rows` and the row schema key
(dOrderedCharter-35 S1-S7, S10), `check_rows`, `read_kind_schema` and `derive_widenings`
(dOrderedCharter-36 S1-S7), the landed revision (dOrderedCharter-46 S1), the class registry and
own-record witness (dSafePassage-10 S1-S4), and `TOOL-dDeclaredLoop-12`'s `find_cycles`, extracted from
`tools/govkit/govkit.py:911` and `tools/memory-tree/backlog.py:1271`, both verified at base. None of
the parents is built, so the build run re-grounds against their landed code. `python
tools/codebase-map/reuse_lookup.py "register a kind with a factory and check composed rows for acyclic
needs"` ranked generic `rows`, `row` and `check` symbols, as scout B found; no seam in the tree fits a
kind register, which the parents build. `python tools/memory-recall/query.py "how does an overlay row
kind get a schema fixed set and widening direction"` returned scout B's row, dOrderedCharter-36's H1
and the night pass's statement of the exclusion and widening rules; none disagrees with the parents'
specs.

Recall terms used: kinds register factory schema fixed-by widens needs constraint set compose_rows check_rows supersedes exclusion step gate
