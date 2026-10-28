# TOOL-dSafePassage-73 — the forward and reverse walks read "no up on record" through one predicate, so a step re-applied by its witness after a rollback keeps its `via` mark

**Status:** DEFERRED · rev-4 · 2026-10-28 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-28

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md) | research | TOOL-dSafePassage-72 TOOL-dSafePassage-74 TOOL-dSafePassage-75 |
| [2026-10-28-prompt-TOOL-dSafePassage-73-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-73-build-brief.md) | journal | — |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-72 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

The forward walk marks a step `"via": "witness"` only where the walk-start receipt holds no record
of it (`tools/govkit/upgrade_steps.py:1990`), while the reverse walk reads a `rolled-back` record as
no up on record (`:2139`). So a step whose witness holds with no up, the common case for an adopter
with no `.agent-cap.conf`, is recorded `applied` with no `via` on its second up, and its second
rollback stops at `witness still holds after down; before-image ... absent` on every retry. This
unit closes H3 (id 4) of the closing diff review, round 1: both walks ask one predicate, and a
`rolled-back` record with no before-image reads as no up on record in both.

## 2. Scope (IN)

- **S1** — The predicate. `test_up_unrecorded(state: str | None, image_present: bool) -> bool` in
  `tools/govkit/upgrade_steps.py`, beside `derive_down_verdict`. It returns True where `state` is
  None or `rolled-back` and `image_present` is False. Observed by AC1.
- **S2** — The forward walk asks it. Move 1 of `run_step_walk`
  (`tools/govkit/upgrade_steps.py:1990`) sets
  `fresh = test_up_unrecorded(began.get(row.id), derive_image_path(target, row.id).exists())`.
  A row whose walk-start record is `rolled-back`, whose witness holds and which has no image is
  recorded `applied` with `"via": "witness"`. Observed by AC2 and AC3.
- **S3** — The reverse walk asks it. Move 3 of `run_reverse_walk` (`:2136-2140`) marks the row
  `"witness"` where `test_up_unrecorded(None if record is None else record["state"], bool(paths))`
  holds, the same reading it makes today, now through the predicate. Observed by AC1 and AC4.
- **S4** — The texts. `run_step_walk`'s docstring (`:1939-1942`) and `help/upgrade-steps.md` at
  lines 164-166 and 200-202 say the mark is set where the receipt held no record of the step, or a
  `rolled-back` one, as the walk began, and no before-image exists. Each help passage carries the
  words ``or a `rolled-back` one`` unbroken on one line. Observed by AC5.
- **S5** — The plant. The `rollback` fixture family gains `witness-only-reup`
  (`ROLLBACK_PLANTS`, `tools/govkit/upgrade_steps.py:3501-3503`). It runs `witness-only`'s walk to
  C, a reverse walk to A, a second walk to C and a second reverse walk to A, with `s2.witness-absent`
  planted so s2's witness holds with no up throughout. After the second walk it prints
  `rollback: fx/s2 recorded via witness after a rollback`, and the second reverse walk must print
  the four `rolled-back` lines, exit 0 and leave the target's bytes equal to their bytes before the
  first walk. `check_step_rollback`'s table (`tools/govkit/selftest.py:4484`) gains its row.
  Observed by AC3.

## 3. Non-goals (OUT)

- `derive_down_verdict`'s `never_ran` (`tools/govkit/upgrade_steps.py:2068`). It asks a different
  question, whether the last record lets a missing image mean "never ran", and it already reads an
  `applied` row `via` its witness that way. With S2 the second up writes that mark, so it needs no
  change.
- The upgrade-walk leg's `marked` oracle (`tools/govkit/upgrade_walk.py:749`) and its `reup` case,
  which never runs a second down. An oracle that calls the predicate under test cannot catch the
  predicate's regression, and that file's findings are TOOL-dSafePassage-77's.
- `derive_reverse_steps`' skip of a `rolled-back` row, which is L1 (id 11), batched into
  TOOL-dSafePassage-76.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-33's `via` mark and its scoped
no-image rule; TOOL-dSafePassage-40's walk-start reading, whose §4 table row "`rolled-back` · either
· `applied`, no `via`" this unit's §4 restates; TOOL-dSafePassage-39's move 3 mark; and
TOOL-dSafePassage-49 S5, which reads a `rolled-back` row as no up on record. The edge join counts
CLOSED specs, and a CLOSED spec cannot take the matching `hands-off` line.

## 4. Design

### Observed at base

A scratchpad probe on node a on 2026-10-28 drove the `rollback` family's scratch gov through
`FIXTURE_WALK_CHILD` and `FIXTURE_REVERSE_CHILD` four times over one target, with
`s2.witness-absent` planted, at `83817478`.

| Run | Exit | `fx/s2` after it |
|---|---|---|
| walk to C | 0 | `applied`, `via` `witness` |
| reverse to A | 0 | `rolled-back` |
| walk to C | 0 | `applied`, no `via`; `step fx/s2 · skipped (witness holds)` |
| reverse to A | 1 | `applied`, `witness still holds after down; before-image .governance/steps/fx/s2.before.json absent` |

### The rule, one table for both walks

```
test_up_unrecorded(state, image_present):
    return state in (None, "rolled-back") and not image_present
```

| Record the walk reads | Image on disk | Forward move 1, witness holds | Reverse move 3 mark |
|---|---|---|---|
| none | absent | `applied`, `via` `witness` | `witness` |
| none | present | `applied`, no `via` | none |
| `rolled-back` | absent | `applied`, `via` `witness` (was: no `via`) | `witness` |
| `rolled-back` | present | `applied`, no `via` | none |
| `failed` | either | `applied`, no `via` | none |

A `rolled-back` record says the last down completed, so any up before it was undone, which is
TOOL-dSafePassage-49 S5's reading. An image on disk after it says an up ran since, so the image
still wins. A `failed` record says an up may have spawned, so it is never read as unrecorded.

The forward walk reads its record from the walk-start receipt (`began`, `:1958`), the reverse walk
from the receipt before move 3 rewrites it (`:2117`). Image presence stays each caller's own read,
`derive_image_path(...).exists()` and `read_image_paths`' non-empty list, both of which test the one
image path.

### Inventory

Minted: the function `test_up_unrecorded` in `tools/govkit/upgrade_steps.py`, a top-level name
`memory/map/generated/symbols.json` maps, so this pass regenerates that file.
`python tools/lexicon/lexicon.py --suggest test_up_unrecorded --as py.function` answered OK on
2026-10-28, leading with the declared verb `test`. The plant `witness-only-reup` and the arm tag
`[dSP-73]` are minted. No `Refusal` site, conf key, gate leg or receipt field.

### Migration

None. A receipt that already holds a step `applied` with no `via` after a rollback keeps it, and
its next rollback stops as today until the operator runs it again from a state this unit writes.
§8 F1 settles that no repair is made, since no adopter can hold that state.

### Rollout

Live at landing, in order 16 with TOOL-dSafePassage-72, -74 and -75, sequenced by M6 because all
four write `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`. The pass runs
`python tools/codebase-map/gen_map.py --write` and commits `symbols.json` with the code, as
TOOL-dSafePassage-81 §4 Rollout does, so the pre-commit map gate passes.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The review's inline fix at `:1990` alone.** It closes the instance and leaves two spellings of
  one question, which is the class the review names: two guards, one question, two answers.
- **Read `rolled-back` as an up on record in the reverse walk instead.** That breaks
  TOOL-dSafePassage-49 S5, whose plant `rolled-back-witness-holds` needs the mark.
- **Let `derive_down_verdict` read a `rolled-back`-then-applied row as never run.** The receipt
  holds only the last state, so that history is not on record to read.

## 5. Production-readiness checklist

- security: N/A — no path, spawn, input or environment changes.
- perf / scale: none; one function call where an expression stood.
- error / empty / loading states: a row with no record and a row recorded `rolled-back` read the same,
  so neither falls through to a third branch.
- observability: the plant prints s2's `via` after the second walk, so a red names the walk that
  dropped the mark.
- risks: a `rolled-back` row whose up was re-run by hand outside a walk, with its image then lost,
  would be marked and downed by its exit. That is TOOL-dSafePassage-33's accepted risk for a row
  recorded nowhere, now extended to one recorded `rolled-back`.
- testing: the `witness-only-reup` plant and the predicate table, under §7's `New arm:` line.
- migration: none.
- user docs: `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

The probes run from the repository root.

- **AC1** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_steps as us; print([us.test_up_unrecorded(s, i) for s in (None, 'rolled-back', 'failed', 'applied') for i in (False, True)])"`
  runs, it prints `[True, False, True, False, False, False, False, False]`.
  Red when: `rolled-back` with no image reads False, as `:1990` reads it at base.
- **AC2** — When `git grep -n "test_up_unrecorded(" -- tools/govkit/upgrade_steps.py` runs, it
  prints the `def` line and one call in each of `run_step_walk` and `run_reverse_walk`, and
  `git grep -n "row.id not in began" -- tools/govkit/upgrade_steps.py` prints nothing.
  Red when: either walk keeps its own spelling of the question.
- **AC3** — When `python tools/govkit/upgrade_steps.py fixture rollback --plant witness-only-reup`
  runs, it exits 0, printing `rollback: fx/s2 recorded via witness after a rollback`, the four lines
  `step fx/s4 · rolled-back` to `step fx/s1 · rolled-back` from the second reverse walk, and
  `rollback: the target's bytes equal their bytes before the walk`.
  Red when: the forward walk keys the mark on `row.id not in began`, so the second reverse walk
  stops at `fx/s2` with `witness still holds after down; before-image
  .governance/steps/fx/s2.before.json absent` and the fixture prints `rollback: FAILED`, as the base
  probe showed.
  cost: about a minute, four walks over a scratch gov.
- **AC4** — When `python tools/govkit/upgrade_steps.py fixture rollback --plant rolled-back-witness-holds`
  and `--plant unrecorded-witness-down-killed` run, each exits 0 as before.
  Red when: S3 changes move 3's reading, so TOOL-dSafePassage-49 S5's or TOOL-dSafePassage-39's
  plant stops.
  cost: about a minute each.
- **AC5** — When `grep -c "or a \`rolled-back\` one" help/upgrade-steps.md` runs, it prints `2`.
  Red when: either help passage still says only "no record".

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `codebase-map coverage + freshness` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/upgrade_steps.py · covers AC3 · the `rollback` family's `witness-only-reup` plant, run by `check_step_rollback`'s table row in `tools/govkit/selftest.py`; observed RED at base 83817478, where the second reverse walk stops at `fx/s2`, and GREEN after the build · none

New arm: tools/govkit/selftest.py · covers AC1 · a `[dSP-73]` check of `test_up_unrecorded`'s eight-cell table beside the in-process verdict table at `:4612-4620`; its failing case is the base reading, `rolled-back` with no image read False · none

## 8. Open questions

- **F1 — Is a receipt the base already left, `applied` with no `via` after a rollback, repaired?**
  - (a) No. The defect needs an adopter to have run up, down and up under the base engine, and gov
    has shipped no release carrying it, so no adopter receipt holds that state. The stop names the
    image and the help page tells the operator to undo the up's writes by hand.
  - (b) Yes, by an upgrade step that marks such a row. That is a new step row and a migration for a
    state no adopter holds.
  - Recommendation: (a). The build is unreleased, so the state exists only in scratch fixtures.
  - RESOLVED (agent, 2026-10-28, delegated): (a), no repair of a receipt already in that state,
    since no adopter can hold it. Rung 3, the mandate delegates it: (a) meets every criterion and
    trips no veto, while (b) adds a step row and a migration no criterion asks for, so no standing
    ruling is invoked and no `widens:` or `relaxes:` field applies.

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, closing H3 (id 4) of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  by `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md`.
- rev-2 · 2026-10-28 · §8 F1 · §4 · F1 resolved as delegated by the coordinator, option (a): no
  repair; §4 Migration says so.
- rev-3 · 2026-10-28 · §7 · the leg line names `policy fixtures`, the leg whose guard
  `tools/govkit/selftest.py`, listed in §4's files touched, trips.
- rev-4 · 2026-10-28 · §4 · §7 · folded this spec's part of M11 and L5 of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md`:
  `symbols.json` in Files touched, regenerated in the pass's commit, with
  `codebase-map coverage + freshness` and `recall floor` on the leg line. The header's node reads
  `a`, the host the probe ran on.

## 10. Reuse audit

The seam extended is the walks' own reading of a step's record: TOOL-dSafePassage-40's walk-start
`began` map (`tools/govkit/upgrade_steps.py:1958`) and TOOL-dSafePassage-39's move 3 mark
(`:2136-2140`), which S1 joins under one predicate placed beside `derive_down_verdict`, the walks'
existing pure judge. The fixture seam is the `rollback` family and its `witness-only` plant
(`:4493-4504`), which S5 runs twice. `python tools/codebase-map/reuse_lookup.py "decide whether a
step's up is on record from its receipt state and its before-image"` ranked `before`, `records`,
`step`, `read_steps` and `read_step_states`, all name-token matches, and none of them decides the
question, so no existing seam fits beyond the two readings above. The recall probe ranked
TOOL-dSafePassage-39 first and TOOL-dSafePassage-33 and -40 third and fifth, the three units whose
rule this predicate now holds in one place.

Recall terms used: `python tools/memory-recall/query.py "when does the forward walk mark a step applied via witness and how does the reverse walk read rolled-back" --terms "via witness rolled-back forward walk reverse walk before-image never ran fresh began mark derive_down_verdict"`
