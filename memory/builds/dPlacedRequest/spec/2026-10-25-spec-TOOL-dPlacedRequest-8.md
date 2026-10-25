# TOOL-dPlacedRequest-8 — each item's declared code seed: its write set, its scope paths or its question's paths

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 13 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0126@b35ab44f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

P32 says every role sees the code its item touches, and "each item declares a seed"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1029-1034`):
the night pass computes an item's `code` slot "from the item's declared seed: its write set, its scope
paths, or its question's paths"
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:207-208`). No item
declares one today, and no item row exists yet. This unit adds the `seed` field to the item kind's
schema, beside the `map` and `unfolds` fields TOOL-dPlacedRequest-6 fills, declares a seed on each role
item that reads code, and resolves a declared seed to the list of repository paths the later `code`
slot reads, each source with no reader yet printing `unarmed`.

## 2. Scope (IN)

- **S1** — The schema rows, I15 of the brief, in one edit to `tools/loop/item-schema.toml`
  (TOOL-dDeclaredLoop-24 S2), each in that file's field shape: `seed`, `shape = "scalar"`, its values
  `none`, `write-set`, `scope-paths` and `question-paths`, `widens = ["none", "write-set",
  "question-paths", "scope-paths"]`; `map`, `shape = "scalar"`, its values `none` and `base`,
  `widens = ["none", "base"]`; and `unfolds`, `shape = "set"`, `widens = "add"`. An absent `seed` or
  `map` reads `none` and an absent `unfolds` reads empty. Observed by AC1.
- **S2** — The declarations: `seed` on the role items of `tools/loop/loop.toml` (TOOL-dDeclaredLoop-12
  S2) whose actor reads code, from the delivery the project map gives each role
  (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:615-629`), as
  §4's table lists. Every other item declares none. Observed by AC2.
- **S3** — The check, `check_item_seeds(items)` in `tools/loop/loop_lib.py`, run by `loop_lib.py
  --check`, the `loop definition` leg's command (TOOL-dDeclaredLoop-1): a `seed` outside the four
  values is refused naming the item and the value; a `seed` on an item whose actor is not a role is
  refused, since only a role's work order carries a `code` slot. Observed by AC3.
- **S4** — The resolver, `resolve_item_seed(item, *, build=None, unit=None, question=None)` in
  `tools/loop/loop_lib.py` and its command line `python tools/loop/loop_lib.py seed <item tag>
  [--build <slug>] [--unit <id>] [--question <text>]`, I16 of the brief: repository-relative,
  forward-slash, deduplicated paths in first-seen order, each normalised by `resolve_ask_path`
  (`tools/memory-tree/gen_build_index.py:3185`, its rule restated as a function of the loop kit, which
  imports no sibling), or the one line `unarmed — <source>: <why>`. Per value:
  `write-set`, the unit's spec's `### Files touched` paths, read by the unattended kit's one reader
  `read_files_touched` (`tools/unattended/unattended.sh:3389`) through S5's verb; `question-paths`, the
  path tokens of the question text, through the same verb's stdin form; `scope-paths`, `unarmed`
  until the plan record carries a scope, which dRankedPlan's `plan.record` writes; `none`, nothing.
  A missing `--unit` for `write-set` or `--question` for `question-paths` exits 2 naming it. Observed
  by AC4, AC5 and AC6.
- **S5** — The one path-token rule. `read_files_touched`'s awk token test (`tools/unattended/unattended.sh:3404`,
  a backticked `[A-Za-z0-9._/-]+` word holding a `/` or ending in an extension) moves into
  `read_path_tokens`, which `read_files_touched` calls unchanged in output, and a read-only verb
  `unattended.sh --path-tokens [--files-touched <rev> <spec>…]` prints, with `--files-touched`, the
  specs' declared paths as `read_files_touched` reads them, and without it, the path tokens of the text
  on stdin. The loop kit resolves the driver as an optional sibling; with none, both sources print
  `unarmed — no unattended driver resolves`. Observed by AC5 and AC7.
- **S6** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on `seed`, its four
  values and the `seed` command. Observed by AC8.

## 3. Non-goals (OUT)

- The `code` slot and its rendering: dFurnishedOrders' `cl-dClosedLoop-0208`; the `code` record the
  slot reads: dTotalRecall's `cl-dClosedLoop-0219`. This unit hands them the path list.
- The `map` and `unfolds` values on the item rows and their check: TOOL-dPlacedRequest-6; this unit
  lands their schema rows only, so one edit of the schema file carries all three fields.
- The reviewer's seed: no `item.review.lens` row exists among the rows dDeclaredLoop lands
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md:84-86`); dFairHearing
  declares it from S1's values when it lands that row (§8 F2).
- The entry and probe items: TOOL-dPlacedRequest-3 and -7 declare their own `seed`, `none` unless they
  name one.
- A plan-record scope reader: dRankedPlan's.

### Edges

- **hands-off** `TOOL-dPlacedRequest-6` — `item-schema.toml`, whose `map` and `unfolds` rows this unit lands for that unit's item values and check
- **consumes-from** external — dDeclaredLoop, built before this build run: the item kind's schema file (TOOL-dDeclaredLoop-24 S2), the item rows and `read_items` (TOOL-dDeclaredLoop-12 S1, S2) and the `loop definition` leg (TOOL-dDeclaredLoop-1)
- **hands-off** external — dFurnishedOrders' `code` slot (`cl-dClosedLoop-0208`) reads `resolve_item_seed`; dRankedPlan's plan record arms `scope-paths`; dFairHearing declares the reviewer's seed
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### Data model

```toml
# tools/loop/item-schema.toml, three rows beside TOOL-dDeclaredLoop-24's
[field.seed]
shape = "scalar"
values = ["none", "write-set", "scope-paths", "question-paths"]
widens = ["none", "write-set", "question-paths", "scope-paths"]

[field.map]
shape = "scalar"
values = ["none", "base"]
widens = ["none", "base"]

[field.unfolds]
shape = "set"
widens = "add"
```

The table spelling follows whatever TOOL-dDeclaredLoop-24's build lands for its own rows; the
values and directions above are this unit's. A scalar's `widens` lists its values narrowest first
(PLAY-dOrderedCharter-36 S5): a later `seed` hands a broader neighbourhood, a unit's files, then a
question's paths, then a design's scope.

### The declarations

| Item | Actor | `seed` |
|---|---|---|
| `item.design.inventory`, `item.design.decompose`, `item.design.reason` | architect | `scope-paths` |
| `item.design.unit-spec`, `item.review.fold` | spec writer | `write-set` |
| `item.build.unit-pass`, `item.build.fix-pass`, `item.build.revert-pass`, `item.build.resolve` | builder | `write-set` |
| `item.test.attribute`, `item.test.reason` | tester | `write-set` |
| `item.plan.research`, `item.design.research` | researcher | `question-paths` |

PINNED 2026-10-25 from the project map's delivery table and flow-steps' actors
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:183-364`); the
check re-derives which items carry a seed at every run.

### The resolver

```
seed item.build.unit-pass --build dExample --unit TOOL-dExample-3
tools/loop/loop_lib.py
tools/loop/item-schema.toml
help/loop.md

seed item.design.inventory --build dExample
unarmed — scope-paths: no plan record carries a scope; dRankedPlan's plan.record arms it
```

`write-set` finds the unit's spec as the file under `memory/builds/<slug>/spec/` whose H1's first
token is the unit id, the predicate `tree_lib.parse_spec_h1` reads, and hands its path to
`--path-tokens --files-touched HEAD <spec>`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `seed`, `map`, `unfolds` | item fields | none |
| `check_item_seeds`, `resolve_item_seed` | functions | `py.function`, OK |
| `seed` | verb of `loop_lib.py` | none |
| `read_path_tokens` | shell function | `sh.function`, asked at the pass |
| `--path-tokens`, `--files-touched` | flags of `unattended.sh` | none |

### Migration

None: no item row exists before TOOL-dDeclaredLoop-12 lands them, and an absent field reads `none`.

### Rollout

Live at landing; the `code` slot that reads the paths renders "not installed" until dTotalRecall's
record lands, so nothing consumes the list yet but the command.

### Files touched (estimate)

- `tools/loop/item-schema.toml`
- `tools/loop/loop.toml`: `seed` on the rows §4 lists
- `tools/loop/loop_lib.py`
- `tools/unattended/unattended.sh`: `read_path_tokens` and the `--path-tokens` verb
- `help/loop.md`

### Alternatives rejected

- **A third copy of the path-token rule in Python.** `read_files_touched` and
  `tools/check-spec-tokens.py`'s `extract_files_touched` (:530) already hold two; the loop kit calls
  the unattended kit's reader instead of adding a third.
- **The card's `task:in` as the scope-paths stand-in.** It is prose whose path tokens are incidental
  (`tools/roles/handoff.py:166` reads it as text); `unarmed` says what is missing.

## 5. Production-readiness checklist

- security — the verb reads tracked specs and stdin and writes nothing; a `--question` is text, never
  a path to open.
- perf / scale — one bounded subprocess per resolution.
- error / empty / loading states — a source with no reader prints `unarmed`; a missing argument exits
  2; a unit with no spec exits 2 naming it.
- observability — each `unarmed` line names its source and the build that arms it.
- risks — a builder's real write set can exceed its declared one; the seed is what was declared.
- testing — the plants of §6.
- migration — none.
- user docs — `help/loop.md` (S6).

## 6. Acceptance criteria

- **AC1** — When `grep -n -A3 "seed\|unfolds\|\[field.map\]" item-schema.toml` runs in the loop kit's
  directory, it prints the three rows with their shapes and directions, and `python loop_items.py
  check` passes over them.
  Red when: a row is missing its direction, so the classifier refuses the field.
- **AC2** — When `python loop_lib.py --check` runs over the tree, it prints each of the twelve items
  of §4's table with its `seed`, and every other item with `none`.
  Red when: a role item that reads code declares no seed.
- **AC3** — When `python loop_lib.py --fixture --plant seed-bad` plants `seed = "diff"` and a
  `write-set` seed on a command item, `--check` exits 1 naming each item and value.
  Red when: an unknown value or a non-role seed passes.
- **AC4** — When `python loop_lib.py seed item.build.unit-pass --build tFix --unit TOOL-tFix-1` runs in
  the plant `seed-write`, whose spec lists under Files touched one scratch path twice, once plain and
  once with a leading `./`, and a second scratch path written with a backslash separator (both the
  plant's own, under its temporary directory, never tracked ones), it prints the two paths in
  forward-slash form, once each.
  Red when: a path repeats, keeps a backslash or keeps its `./`.
- **AC5** — When the plant `seed-question` runs `seed item.plan.research --question "is
  tools/x/y.sh racing with tools/x/z.sh?"` with both paths backticked, it prints the two paths; without
  `--question` it exits 2.
  Red when: a question's paths are not found, or a missing question reads as an empty seed.
- **AC6** — When the plant `seed-scope` runs `seed item.design.inventory --build tFix`, it prints one
  `unarmed — scope-paths:` line naming dRankedPlan.
  Red when: an unarmed source prints nothing and reads as an empty seed.
- **AC7** — When `bash tools/unattended/unattended.sh --path-tokens --files-touched HEAD <spec>` runs
  over this spec's own file, it prints the five paths of §4's Files touched, the same lines
  `read_files_touched HEAD` prints for it.
  Red when: the extracted rule changes what `read_files_touched` reads.
- **AC8** — When `grep -n "question-paths" loop.md` runs in `help/`, it finds the section naming the
  four values and the `seed` command.
  Red when: the field lands and the page does not say what each value hands.

## 7. Gates

`spec tokens (a spec's own names resolve)`

The unattended kit's own self-test suites are waived for this build's landing (README rule 8), so S5's
extraction is observed by AC7's direct comparison, never by those suites.

New arm: tools/loop/loop_lib.py · covers AC3 AC4 AC5 AC6 · the `seed-bad`, `seed-write`, `seed-question` and `seed-scope` fixture cases under the `loop definition` leg, the failing case staged by `seed-bad` · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it.
  RESOLVED (agent, 2026-10-25, delegated): `OPEN`.
- **F2 — The project map gives the reviewer "the code slot of the pinned range"
  (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:623`), a fourth
  source the clause does not list. Is it a fourth `seed` value?** Options: (a) a `pinned-range`
  value, a departure from the clause recorded as a deviation; (b) the three values the clause names,
  the reviewer's item taking `write-set`, the declared write sets of the units its range builds; (c)
  defer the reviewer's seed to the build that lands its item. RESOLVED (agent, 2026-10-25,
  delegated): (b) and (c), rung 1: v2's clause names three sources and answers the value set; no
  `item.review.lens` row exists among dDeclaredLoop's rows (dDeclaredLoop-50:84-86), so the reviewer's
  item declares its seed from those three when dFairHearing lands it, and the clause stands
  unamended.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 8, P32, the night pass's point 3 and the
  project map's delivery table.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC4 describes the plant's scratch paths in
  prose, so no illustrative path reads as a repository path.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seams extended are the item kind's schema file (TOOL-dDeclaredLoop-24 S2), with TOOL-dDeclaredLoop-29
S1's `upstream` field as the shape a new field takes; `read_files_touched`
(`tools/unattended/unattended.sh:3389`, its token test at :3404), whose rule S5 lifts into one
function rather than copying; and `resolve_ask_path` (`tools/memory-tree/gen_build_index.py:3185`),
the normalisation the asks join already applies, all verified at base. Scout C cited the token rule at
:3405; source holds it at :3404. `extract_task_fields` (`tools/roles/handoff.py:166`) was the scout's
scope stand-in and is rejected in §4. `python tools/codebase-map/reuse_lookup.py "resolve an item's
declared seed to a list of repo-relative paths"` ranked `resolve`, `seed` (a test helper),
`resolve_kit_dir` and `repo_root`, none a seed resolver, so no existing seam holds the resolution.

Recall terms used: `python tools/memory-recall/query.py "how is an item's code seed resolved to paths" --terms "code seed write-set scope-paths question-paths resolve_item_seed item-schema read_files_touched resolve_ask_path night pass point 3"`
