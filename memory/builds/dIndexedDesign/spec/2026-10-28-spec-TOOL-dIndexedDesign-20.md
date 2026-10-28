# TOOL-dIndexedDesign-20 — two-level re-entry: `design.input`'s pin, `design.reentry`'s additive-versus-breaking diff record, and the re-design inventory

**Status:** OPEN · rev-3 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 9 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0390@a096f77c part 2/2
**Carries:** node:item.design.input
**Carries:** node:item.design.reentry
**Carries:** node:item.design.inventory
**Carries:** node:policy-key.design.reentry
**Carries:** node:record-kind.diff
**Carries:** node:record-kind.inventory

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

gap-flow-01 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:107`)
says a change that breaks a feature cannot be told from one that touches a unit, so re-design has no
granularity but the unit; gap-flow-25 (:131) says a revised plan has no re-design inventory of
completed work. The owner settled two-level re-entry as a policy, `design.reentry` (flow FL-D2, FL-D5,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:250-254`, :290-310), and
that an additive interface change stays at the unit while a breaking one re-designs the feature
(FL-B4, :389-391, :404-405), by a structural diff of the interfaces each feature design declares
(:311-317; v2 P17, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:903-905`).

This unit carries cl-dClosedLoop-0390 in part 2 of 2: the items `design.input`, `design.reentry` and
`design.inventory` of flow-steps
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:235-237`), the
`diff` and `inventory` record kinds, and `design.reentry` read through I3. Part 1, the feature level
itself and fork resolution by `design.forks`, is TOOL-dIndexedDesign-8 (its §8 F1); this unit reads that
unit's feature design records and adds no second grammar for them.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the record-kind factory `record_kinds.py
new` and `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1 S1, S9); the `[[item]]` and
`[[stand-in]]` rows of `tools/loop/loop.toml` (TOOL-dDeclaredLoop-12 S2, -13 S8) and the item factory
(TOOL-dDeclaredLoop-24); `read_feature_designs`, the `feature-design` kind and `--decompose-fixture`
(TOOL-dIndexedDesign-8 S1, S2, S10); `read_spec_section` (TOOL-dIndexedDesign-9, I1);
`read_design_policy` (TOOL-dIndexedDesign-16, I3).

Shared files the build run sequences, in order 8 then 9: `tools/loop/loop.toml`, where
TOOL-dIndexedDesign-8 S11 arms `item.design.decompose`'s row, TOOL-dIndexedDesign-13 S6 adds an
`upstream` entry to that same row and S10 below arms three other rows; `tools/memory-tree/design_lib.py`,
whose feature reader S1 widens after TOOL-dIndexedDesign-8 lands it; and
`tools/memory-tree/BUILD-METHOD.template.md` M2, where TOOL-dIndexedDesign-8 S12 and S12 below each add a
sentence to one paragraph.

- **S1** — The feature reader at a revision. `read_feature_designs(root, slug, rev=None)` gains its
  `rev` argument: absent, it reads the working tree as TOOL-dIndexedDesign-8 S2 states; set, it lists
  the build's `build/` folder at `rev` by `git ls-tree -r --name-only` through `tree_lib.read_git_output`
  (`tools/memory-tree/tree_lib.py:278`), reads each file at its home name `-feature-<seg>.md` through
  `tree_lib.read_blobs_at` (:328), and keeps one whose first `**Serves:**` line, by `tree_lib.BIND_RE`
  (:410) over the first `BIND_HEAD_LINES` (:401) unfenced lines, names kind `feature-design`. Both
  bindings parse a record through one function, `parse_feature_design(text, path)`, split out of the S2
  reader the way `parse_spec_text` was split from `parse_spec`
  (`tools/memory-tree/gen_build_index.py:494-499`). A `feature-design` record not at its home name is a
  refusal at either binding, so the two hold one population. Observed by AC1 and AC2.
- **S2** — The interface diff, `derive_interface_changes(base, head)` in `design_lib.py`, over two values
  of S1: per feature, one change per declared `Interface` element that differs, keyed by the
  interface's name, each classified `additive` or `breaking` from §4's direction table alone, each with
  the units it touches by that table and, for a `breaking` change, the units the base declaration names
  on that interface. `Units` and `Boundary` are read and never classified. Observed by AC1 and AC2.
- **S3** — The re-entry level, `derive_reentry_level(changes, values, flags)`: a feature re-enters at
  `feature` when any value of `values` holds by §4's trigger table, and at `unit` otherwise; the route is
  `item.design.decompose` for `feature` and `item.design.unit-spec` for `unit` (flow-steps:236).
  `values` is read once per run by the literal call `read_design_policy("design.reentry", root)` (I3),
  a list; `flags` are the CLI's `--flag` values, admitted only for `review-cross-unit-flaw` and
  `planner-or-owner-flag`. Observed by AC3 and AC4.
- **S4** — The diff record, kind `diff`, tag `record.diff`, registered by `python record_kinds.py new
  diff --tag record.diff --writer "design_lib.py --reentry --write" --check "memory hygiene" --field
  Feature --field Base --field Head --field Change --field Affected --field Triggers --field Level
  --field Route` (I15). Home `memory/builds/<slug>/build/<date>-build-<unit id>-diff-<n>.md`, `<unit id>`
  the feature's first unit in its `Units` order at head, or at base for a feature head no longer
  declares, and `<n>` the next number free for that unit; bound `**Serves:** diff <every unit the
  feature declares at base or head>`; fields as §4's example spells them. Observed by AC5 and AC9.
- **S5** — The re-entry CLI, `python design_lib.py --reentry <slug> --base <rev> [--head <rev>] [--flag
  <value>]... [--write]`, `--head` defaulting to `HEAD`: one line per change, `design-lib: reentry
  <feature> · <element> · <field> <op> · <class>`, one per feature, `design-lib: reentry <feature> ·
  level <unit|feature> · triggers <values or none> · route <item>`, and one population line naming the
  features read at each side and what the diff does not check. `--write` writes S4's record per changed
  feature. Exit 0 when every feature is classified; 1 on a usage error or a `--flag` S3 does not admit;
  2 on a record S1 refuses, a revision naming no commit, or a key S3 cannot resolve. Observed by AC1 to
  AC5.
- **S6** — The input pin, `python design_lib.py --input <slug> --kind <kind> <path> [--at <rev>]`,
  `--at` defaulting to `HEAD`. The kinds and their routes are `item.design.input`'s `outcomes` and
  `routes` in `tools/loop/loop.toml`, read with `tomllib` by `read_input_kinds(root)` through
  `resolve_kit_dir("loop", "loop.toml", here)` carried inline, the shape
  `tools/check-spec-tokens.py:243` carries, so no second list of kinds exists. It prints
  `design-lib: input <slug> · <kind> · <path>@<sha8> · route <item>`, `<sha8>` the commit `--at`
  names. Exit 0; 1 on a kind the row's outcomes do not hold, naming them, or a path the revision does
  not hold; 2 on no loop kit or no `item.design.input` row. Observed by AC6.
- **S7** — The inventory record, kind `inventory`, tag `record.inventory`, registered by `python
  record_kinds.py new inventory --tag record.inventory --writer hand --check "memory hygiene" --field
  Input --field Of --field Verdict`. Home
  `memory/builds/<slug>/build/<date>-build-<unit id>-inventory-<n>.md`, `<unit id>` the first id its
  `Verdict` lines name; bound `**Serves:** inventory <each unit id a Verdict line names>`; fields
  `- **Input:** <path>@<sha8>`, the pin S6 printed; one `- **Of:** <slug> @ <rev>` per build whose built
  units it rules on (the revised build itself, a superseded build at its kept branch's tip, or a
  withdrawn parent under `deps.on-parent-withdrawn = "adopt-parent-work"`); one `- **Verdict:** <unit
  id> · <verdict> · <reason>` per built unit, `<verdict>` one of §4's three verdict forms. Observed by
  AC7 and AC9.
- **S8** — The inventory join, `check_inventory(root, conf, slug)` in `gen_build_index.py` and its mode
  `python gen_build_index.py --inventory <slug>`: for each `inventory` record of the build and each `Of`
  line, the units whose spec reads `CLOSED` at `<rev>`, read by `read_tree_paths` (:3481),
  `read_blobs_at_rev` (:3486) and `parse_spec_text` (:494). Findings, each naming the record, the unit
  and the token: a `CLOSED` unit with no `Verdict`; a unit with two; a `Verdict` for a unit not
  `CLOSED` there; a verdict outside §4's forms or an empty reason; an amending unit that is not a unit
  of `<slug>` or is the built unit itself, or whose spec's `section.goal` and `section.scope` bodies,
  read through `design_lib.read_spec_section`, name the built unit's id in backticks in neither; a
  record with no `Of` or no `Input`. One population line names the records, builds and units graded and
  what the join does not check. Exit 1 on a finding, 0 on none, 2 on an `Of` revision naming no commit
  or a record it cannot read. Observed by AC7 and AC8.
- **S9** — The key. The catalogue row (`tools/policy/catalogue.toml:46-51`, owner dIndexedDesign)
  gains `summary` and the `usage` line `design.reentry = ["interface-change", "planner-or-owner-flag"]`,
  its allowed set, `empty = "never"` and default unchanged; the name leaves
  `tools/policy/unsummarised-keys.txt` (:57) through `python policy.py lists --write`; no second row is
  added. Observed by AC4 and AC10.
- **S10** — The items go live. The `[[stand-in]]` rows of `item.design.input`, `item.design.reentry` and
  `item.design.inventory` leave `tools/loop/loop.toml`; the three rows' `witness` name
  `design_lib.py --input`, `design_lib.py --reentry` and `gen_build_index.py --inventory`, and the
  `returns` of the second and third name `record-kind.diff` and `record-kind.inventory`. Their needs,
  outcomes and routes stay as TOOL-dDeclaredLoop-12 transcribed them. Observed by AC9.
- **S11** — The plants. TOOL-dIndexedDesign-8's `--decompose-fixture <dir> --plant <case>` gains the
  cases of §6: `reentry-additive`, `reentry-consumer`, `reentry-breaking`, `input`, `inventory`,
  `inventory-missing`, `inventory-unbuilt`, `inventory-amender` and `inventory-of`, each a scratch
  repository whose base and head are two commits, so one fixture writer serves both units. Observed by
  AC1 to AC8.
- **S12** — The prose. `tools/memory-tree/BUILD-METHOD.template.md` M2's Act paragraph (:56-58) gains one
  sentence: a plan revision's re-design inventory is an `inventory` record joined by
  `gen_build_index.py --inventory`, and an amendment's interface change is classified by a `diff`
  record, additive staying at the unit and a breaking change or a held `design.reentry` trigger
  re-designing the feature. `memory/guides/BUILD-METHOD.md` re-renders. Observed by AC11.

## 3. Non-goals (OUT)

- Part 1 of the clause: the feature design record, the roster kind, fork records and `design.forks`
  (TOOL-dIndexedDesign-8).
- Classifying a change to `Units` or `Boundary`: neither is an interface, and a unit joining or leaving
  a feature is `design.decompose`'s act, which the inventory records.
- Deciding the two judgment triggers: whether a review names a cross-unit flaw, or the planner or owner
  flags a feature, is the caller's, passed as `--flag`.
- Writing the inventory: its writer is the architect (`hand`), as flow-steps:237 names the actor.
- Running the loop: routing from a printed route to the next item, and the transition rows, are
  dDeclaredLoop's (TOOL-dDeclaredLoop-12, -13).
- Pinning a kept branch's tip: the caller names the revision on the `Of` line; this unit reads it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-8` — `read_feature_designs`, the `Interface` fields S2 diffs and the `--decompose-fixture` writer S11 extends; without them there is no declaration to diff
- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section`, the reader S8's amender test reads `section.goal` and `section.scope` through
- **consumes-from** `TOOL-dIndexedDesign-16` — `read_design_policy`, I3, the one reader S3 calls for `design.reentry`; without it the level has no trigger set
- **consumes-from** external — TOOL-dTotalRecall-1's `record_kinds.py new` (S4, S7) and TOOL-dDeclaredLoop-12, -13 and -24's item and stand-in rows (S10), DEFERRED at base
- **hands-off** external — §8 F3's ask to dOrderedCharter and F1's ask to dDeclaredLoop
- **hands-off** `TOOL-dIndexedDesign-34` — the `diff` and `inventory` kinds of S4 and S7, which that unit makes typed, and the diff record's name, which it takes from the factory (report id 21, HIGH)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 10 and 48, each a scope item of that batch unit
- **hands-off** `TOOL-dIndexedDesign-43` — S7's inventory grammar, one `Of` line per build and one `Verdict` line per built unit, which that unit's repeatable set admits (id 13)

## 4. Design

### Evidence

- No reader of a feature design exists at base, and TOOL-dIndexedDesign-8 S2 states "Part 2's
  structural diff reads these fields and no other".
- `design.reentry` has its catalogue row and no reader (`tools/policy/catalogue.toml:46-51`,
  `tools/policy/unsummarised-keys.txt:57`); `policy.py get design.reentry` prints the three default
  members one per line, and `[]` is refused for a set whose row says `empty = "never"`
  (`tools/policy/policy.py:164`).
- The house reads a pinned tree as bytes through one batch, `tree_lib.read_blobs_at`, and parses a
  record's text apart from its file (`gen_build_index.py:494-499`, :3481-3504).
- The feature transition F6 re-enters on `item.design.reentry` with outcome `breaking`, and the unit
  transition U5 with `spec wrong`
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-13.md:174`, :181).
- The only re-design prose is M2's AMEND act (`memory/guides/BUILD-METHOD.md:56-58`).

### The direction table

A change to a declared interface, keyed by its name, is classified from this table alone, the rule
PLAY-dOrderedCharter-36 S5 states for its rows (direction declared per field, class derived from the
declaration); a name present at one side only is an interface added or removed, so a rename reads as
both.

| Field | Operation | Class | Units it touches |
|---|---|---|---|
| interface | added | `additive` | its producer and consumers at head |
| interface | removed | `breaking` | its producer and consumers at base |
| `producer` | changed | `breaking` | the old and the new producer |
| `contract` | changed | `breaking` | its producer and consumers |
| `consumers` | a consumer added | `additive` | that consumer |
| `consumers` | a consumer removed | `breaking` | that consumer |

### The trigger table

| `design.reentry` value | Holds for a feature when |
|---|---|
| `interface-change` | any of its changes is `breaking` |
| `two-plus-units` | its changes touch two or more distinct units |
| `review-cross-unit-flaw` | `--flag review-cross-unit-flaw` is given |
| `planner-or-owner-flag` | `--flag planner-or-owner-flag` is given |

Under the default set an additive change stays at the unit and a breaking one re-designs the feature,
FL-B4's settlement; a set without `interface-change` lets the owner keep a breaking change at the unit
(§8 F1).

### A diff record

```markdown
# Diff — feature.record-door

**Serves:** diff TOOL-tFix-1 TOOL-tFix-2

- **Feature:** feature.record-door
- **Base:** 1a2b3c4d
- **Head:** 5e6f7a8b
- **Change:** record door · contract changed · breaking
- **Affected:** TOOL-tFix-1 TOOL-tFix-2
- **Triggers:** interface-change two-plus-units
- **Level:** feature
- **Route:** item.design.decompose
```

### The inventory verdicts

| Verdict form | Means |
|---|---|
| `kept` | the built unit stands as built |
| `amended <unit id>` | a new unit of the revised build changes it, its spec naming the built unit |
| `retired` | the built unit's work is withdrawn; a new unit owes any code change |

A built unit is never revised in place (v2 P19, :914); every verdict carries its reason.

### What it does not check

Whether a contract change is truly breaking in meaning (a re-spelled token reads `breaking`); a change
to an interface nobody declared; whether a `--flag` was warranted; whether an inventory's verdicts are
the right ones; an `Of` line the architect left out; and a hand-edited diff record, which re-running
`--reentry` over its `Base` and `Head` would print differently.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `parse_feature_design`, `derive_interface_changes`, `derive_reentry_level`, `read_input_kinds` | functions in `design_lib.py` | `py.function`, asked at the pass |
| `check_inventory` | function in `gen_build_index.py` | `py.function`, asked at the pass |
| `--reentry`, `--base`, `--head`, `--flag`, `--write`, `--input`, `--kind`, `--at` | flags of `design_lib.py` | `cli.flag`, asked at the pass |
| `--inventory` | flag of `gen_build_index.py` | `cli.flag`, asked at the pass |
| `diff`, `inventory` | record kinds, rows of `record-kinds.toml` | none |
| `Feature`, `Base`, `Head`, `Change`, `Affected`, `Triggers`, `Level`, `Route`, `Input`, `Of`, `Verdict` | record fields | none |

### Migration

None: no feature design, diff or inventory record exists at base.

### Rollout

Live at landing; each item's stand-in leaves in the commit its witness lands in.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1, S2, S3, S5, S6, S11
- `tools/memory-tree/gen_build_index.py`: S8 and the arms of §7
- `tools/memory-tree/record-kinds.toml`: S4, S7, written by the factory
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`: S9
- `tools/loop/loop.toml`: S10
- `tools/memory-tree/BUILD-METHOD.template.md`, render `memory/guides/BUILD-METHOD.md`: S12

### Alternatives rejected

- **A second feature-record reader for the base side** — lost to `[one-fact]`: two parsers of one record
  can disagree on a field, while one parser with two bindings is the house's answer to a pinned read ·
  `tools/memory-tree/gen_build_index.py:497-499`
- **Reading the base by a scratch worktree** — lost to cost: a checkout per run where one `ls-tree` and
  one `cat-file --batch` read the build's records · `tools/memory-tree/tree_lib.py:328-334`
- **The kinds as a list in `design_lib.py`** — lost to `[one-fact]`: the item row already declares its
  outcomes and routes, and a second list would need a parity check of its own ·
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-12.md:118-131`
- **The inventory join in `design_lib.py`** — lost to the import graph: `gen_build_index.py` imports
  `design_lib` and holds the pinned spec reader the join needs (§8 F5) ·
  `tools/memory-tree/gen_build_index.py:548`

## 5. Production-readiness checklist

- security — reads tracked blobs at named revisions and the policy kit's value by its own reader;
  writes only the diff record, under the build's own folder.
- perf / scale — two `ls-tree` and two batch reads per `--reentry`; one per `Of` line for `--inventory`.
- error / empty / loading states — exit 2 naming an unreadable record, a revision naming no commit or
  an unresolved key; a build with no feature design prints that it classified nothing.
- observability — every change, level and finding names its feature, unit and token; each population
  line names what it does not check.
- risks — a re-spelled contract token reads `breaking`, which errs toward re-designing the feature.
- testing — each plant's red case and its clean twin, each `design.reentry` value planted, `[]`
  refused.
- migration — none.
- user docs — M2's sentence; `help/policy.md` lists keys from the catalogue, whose row gains its
  summary.

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --decompose-fixture <dir> --plant reentry-additive` writes a base
  whose `feature.record-door` declares `record door` and a head that adds `close record` (producer
  `TOOL-tFix-1`, consumer `TOOL-tFix-2`), `design_lib.py --reentry tFix --base HEAD~1` run there with no
  policy file prints `close record · interface added · additive`, level `unit` and route
  `item.design.unit-spec`, and exits 0.
  Red when: an added interface reads `breaking`, or the default set routes it to `item.design.decompose`.
- **AC2** — When `--reentry tFix --base HEAD~1` runs over `--plant reentry-breaking`, whose head changes
  `record door`'s contract, removes an interface and removes a consumer, it prints each of the three
  changes `breaking`, names `TOOL-tFix-1` and `TOOL-tFix-2` as affected, and prints level `feature` and
  route `item.design.decompose`; over `--plant reentry-consumer`, which only adds a consumer, it prints
  one `additive` change touching that consumer alone.
  Red when: a removal or a contract change reads `additive`.
- **AC3** — When a committed `.governance/policy.toml` sets `design.reentry = ["interface-change"]`,
  `--reentry` prints level `feature` over `reentry-breaking` and `unit` over `reentry-additive`; with
  `["two-plus-units"]` it prints `feature` over `reentry-additive`, whose change touches two units, and
  `unit` over `reentry-consumer`, whose change touches one.
  Red when: either value holds where its row of the trigger table does not, or fails where it does.
- **AC4** — When the committed set is `["review-cross-unit-flaw"]`, `--reentry` over `reentry-breaking`
  prints level `unit`, over `reentry-consumer` with `--flag review-cross-unit-flaw` prints `feature`, and
  with `--flag planner-or-owner-flag` prints `unit`; with `["planner-or-owner-flag"]` the latter prints
  `feature`; with `[]` it exits 2 naming `design.reentry`; and `--flag interface-change` exits 1.
  Red when: a flag outside the set raises the level, or the empty set is read as a value.
- **AC5** — When `--reentry tFix --base HEAD~1 --write` runs twice over `reentry-breaking`, it writes
  `…-TOOL-tFix-1-diff-1.md` and then `…-diff-2.md`, each bound `**Serves:** diff TOOL-tFix-1
  TOOL-tFix-2`, whose `Change`, `Triggers`, `Level` and `Route` lines equal the printed ones.
  Red when: the record and the printed classification differ.
- **AC6** — When `--plant input` writes a loop row whose outcomes are `amendment` and `plan revision`,
  `python design_lib.py --input tFix --kind amendment <path>` prints `amendment`, the path at the head's
  sha8 and route `item.design.reentry`, and `--kind "plan revision"` prints `item.design.inventory`;
  `--kind patch` exits 1 naming the two outcomes; a path the head does not hold exits 1; with no loop
  row it exits 2.
  Red when: a kind the row does not declare is admitted.
- **AC7** — When `python gen_build_index.py --inventory tFix` runs over `--plant inventory`, whose record
  rules `kept`, `amended TOOL-tFix-4` and `retired` on three `CLOSED` units, it exits 0; over
  `inventory-missing` (a `CLOSED` unit with no verdict), `inventory-unbuilt` (a verdict for an `OPEN`
  unit) and `inventory-amender` (an amending spec naming the built unit in neither its Goal nor its
  Scope) it exits 1 naming the unit and the token.
  Red when: any of the three plants exits 0.
- **AC8** — When `--inventory tFix` runs over `--plant inventory-of`, whose `Of` line names build `tOld`
  at a revision where `TOOL-tOld-1` read `CLOSED` and HEAD reads it `WONTDO`, it exits 1 until a
  `Verdict` names `TOOL-tOld-1`, then 0; with the `Of` revision naming no commit it exits 2.
  Red when: the join reads the build at HEAD instead of the named revision.
- **AC9** — When `python -c` loads `record-kinds.toml` and `loop.toml` with `tomllib`, the first holds
  rows `diff` and `inventory` tagged `record.diff` and `record.inventory`, and the second holds no
  `[[stand-in]]` row for `item.design.input`, `item.design.reentry` or `item.design.inventory`, whose
  `witness` names `--input`, `--reentry` and `--inventory`.
  Red when: a row is missing, or a stand-in survives its witness.
- **AC10** — When `python policy.py get design.reentry` runs with no policy file it prints
  `interface-change`, `review-cross-unit-flaw` and `planner-or-owner-flag`; after `python policy.py lists
  --write` the unsummarised list no longer names `design.reentry`; and `grep -n
  'read_design_policy("design.reentry"' design_lib.py` finds the literal reader.
  Red when: the row stays unsummarised or no literal call reads the key.
- **AC11** — When `grep -n "re-design inventory" BUILD-METHOD.md BUILD-METHOD.template.md` runs over the
  render and its template, both print M2's sentence naming `design.reentry`, and the render matches its
  template.
  Red when: the render or the template omits it.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `policy check` · `policy fixtures` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each re-entry, input and inventory plant red and its clean twin green, the four `design.reentry` values and `[]` planted, staged by classifying a removal `additive` · none

## 8. Open questions

- **F1 — What does `interface-change` add once FL-B4 keeps an additive change at the unit?** Options: (a) it is the breaking-change trigger: present, a breaking change re-designs the feature, and a set without it keeps one at the unit; (b) breaking always re-designs the feature and `interface-change` also raises an additive change, which under the default set contradicts FL-B4; (c) breaking always re-designs the feature and the value is inert. (b) fails FL-B4's settled default; (c) leaves a catalogue value no reader can see. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the option that keeps every value live and the owner's set adjustable (FL-D5, "user-adjustable, per the flexibility principle"), equal to flow-steps:236 under the default. It makes a feature re-entry possible on a held trigger with no breaking change, which TOOL-dDeclaredLoop-13's row F6 reads only as `breaking`: an ask for dDeclaredLoop, target TOOL-dDeclaredLoop-13, accept row F6's outcome reads `item.design.reentry`'s feature-level outcome, a breaking change or a held `design.reentry` trigger, seen on a planted additive change under `two-plus-units` moving its feature to `decomposed`. widens: none · relaxes: none
- **F2 — Where does `design.input` get the input's kind?** Options: (a) the caller names it with `--kind`, checked against the item row's outcomes; (b) derived from the input record's own kind; (c) derived where a kind exists, declared otherwise. (b) and (c) need a map from record kinds to input kinds whose plan, plan revision, patch and finding kinds belong to builds that are not this build's ancestors and name no kind at base. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the most capable option that names no unlanded kind; the row stays the one list. widens: none · relaxes: none
- **F3 — Is PLAY-dOrderedCharter-36 S5's widening classifier the seam?** Options: (a) call its `classify_patch`; (b) state the same rule, a direction declared per field and the class derived from it, as §4's table in `design_lib.py`. (a) is unbuilt, in a build that is not this build's ancestor, and classifies a patch against gov's row rather than one revision against another. RESOLVED (agent, 2026-10-28, delegated): (b), rung 3, and since whichever lands second is the rule's second instance, an ask for dOrderedCharter, target PLAY-dOrderedCharter-36, accept S5's classifier and this unit's direction table read one declared-direction function, extracted by whichever lands second, seen on both callers classifying a planted removal through it. widens: none · relaxes: none
- **F4 — How does each non-structural trigger hold?** Options: (a) `two-plus-units` counts the distinct units the diff's changes touch by §4's table, and the two judgment values hold only on the caller's `--flag`; (b) `two-plus-units` counts the units the input names, and the judgment values are read from a review record. (b) reads an input shape and a review field no landed or ancestor spec defines. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, derivable from the diff alone. widens: none · relaxes: none
- **FACT-QUESTION · F5 — Can the inventory join live in `design_lib.py`?** Probe: `grep -n "design_lib\." tools/memory-tree/gen_build_index.py`. Observation that decides: `gen_build_index.py` calling into `design_lib`, which makes the reverse import a cycle. Liveness: the probe prints nothing where no call exists. Run at writing: it prints the calls at :548-549, `design_lib.read_spec_writes` and `design_lib.read_spec_edges`. RESOLVED (agent, 2026-10-28, delegated): the join lives in `gen_build_index.py`, beside `read_tree_paths`, `read_blobs_at_rev` and `parse_spec_text`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 8 part 2/2 as TOOL-dIndexedDesign-8 §8 F1
  splits it, gap-flow-01 and gap-flow-25, flow FL-D2, FL-D5 and FL-B4, flow-steps:235-237, v2 P17 and
  P19 and its `[policies]` row, scout C's row 8, and the parent rows of TOOL-dDeclaredLoop-12, -13, -24
  and TOOL-dTotalRecall-1.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from edges of TOOL-dIndexedDesign-34, TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-43, promoted by the round-1 spec audit of units 31 to 38; nothing else
  moved.

## 10. Reuse audit

The seams extended are TOOL-dIndexedDesign-8's `read_feature_designs` and `--decompose-fixture`, the
pinned-read pair `tree_lib.read_git_output` and `tree_lib.read_blobs_at`
(`tools/memory-tree/tree_lib.py:278`, :328), `tree_lib.BIND_RE` (:410) for the Serves line,
`gen_build_index`'s `read_tree_paths`, `read_blobs_at_rev` and `parse_spec_text` (:3481, :3486, :494),
the inline `resolve_kit_dir` (`tools/check-spec-tokens.py:243`), and `read_design_policy` (I3); each line
verified at `4bf0f400d`. `python tools/codebase-map/reuse_lookup.py "classify an interface change
between two revisions as additive or breaking by a structural diff of declared fields"` ranked name
stems (`field`, `changed`, `classify` in `tools/govkit/census.py`, `read_spec_revisions`,
`declared_list`); none diffs two declarations, and `read_spec_revisions` reads a spec's history rather
than a record's fields, so no existing seam fits the classifier and S2 adds it beside the reader it
calls. A second probe, "give each completed unit of a revised plan a verdict kept amended or retired and
join it to every built unit", ranked `plan`, `plan_state` and several `derive_*_verdict` functions, each
a verdict over runs, branches or reviews, none over units; no existing seam fits the inventory join. The
recall query's hit for flow-steps cites :218, the chunk's first line, where the `design.reentry` row
sits at :236; scout C's citations of `design_lib.py:528`, :543 and :601 and `catalogue.toml:47` hold at
`4bf0f400d`.

Recall terms used: `python tools/memory-recall/query.py "how does design re-enter at the unit or the feature after an amendment, and inventory completed units after a plan revision" --terms "design.reentry re-entry additive breaking interface diff record inventory kept amended retired plan revision feature design"`
