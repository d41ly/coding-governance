# TOOL-dCalibratedLens-20 — every Loop Review record carries a `**Serves:**` line naming its kind, so the registry's field check reaches it

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-20-deviation-201.md](../build/2026-11-02-build-TOOL-dCalibratedLens-20-deviation-201.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 36, HIGH, item H2 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). The `value-ledger`,
`loop-review` and `keep` rows claim `check = "record-kinds"`, but under TOOL-dTotalRecall-42 S5
`derive_record_kind` returns the row named by `canonical_kind(<the record's Serves kind>)` and None
for a record with no Serves line, and none of the three templates (spec-2 §4 "The snapshot", spec-3
§4 "The record", spec-5 §4 "The keep record") carries one. The field check therefore grades nothing:
a snapshot missing `Window` passes, and spec-5 AC9 cannot pass. This unit gives each template a
`**Serves:** <kind> <owning unit id>` line and joins the three kinds to the record-kind token list,
so the check reaches every record, and proves it with a planted record missing a field. It repairs
`TOOL-dCalibratedLens-3`, the unit that lands the second of the three templates.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the three sibling specs' text (each at
  rev-2, its §4 "Amendments (round-1 spec audit)", id 36): the snapshot's third line is
  `**Serves:** value-ledger TOOL-dCalibratedLens-2`, the record's `**Serves:** loop-review
  TOOL-dCalibratedLens-3` and the keep's `**Serves:** keep TOOL-dCalibratedLens-5`, each id the unit
  whose spec owns the kind; and each kind joins `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`
  and the closed `<kind>` list of `tools/memory-tree/HYGIENE.template.md`, rendered into
  `memory/HYGIENE.md`, in the pass that lands its row, as TOOL-dTotalRecall-11 S3 joins `shape-run` and
  TOOL-dWellOiledMachine-32 joins `act`. Observed by AC1.
- **S2** — The proof, a `--fixture` plant `serves-kinds` in `tools/loop/loop_review.py`: in a scratch
  worktree it writes one snapshot and one record through the landed writers, commits them, and runs
  `python <memory-tree kit>/record_kinds.py --check` there as a bounded subprocess (60 s): exit 0. With
  the snapshot's `**Window:**` line cut it exits 1 naming the snapshot and `Window`; with the
  record's `**Ledger:**` line cut it exits 1 naming the record and `Ledger`. Observed by AC2.
- **S3** — The staged break: the same plant with the writers' Serves line dropped. The check must then
  name each record as kind None (`home-kind mismatch` in TOOL-dTotalRecall-42's counts) or fail the
  plant, so a template that loses its line cannot pass silently. Observed by AC3.
- **S4** — Each writer's own output carries the line: `price --dry-run` and `record --key 2026-W45`
  print a body whose third line opens `**Serves:** `. Observed by AC4.

## 3. Non-goals (OUT)

- The homes: `TOOL-dCalibratedLens-19`, id 1. That unit makes them disjoint; this one makes the kind
  decide, so either alone leaves a gap TOOL-dTotalRecall-42 §4 "The kind decides" names.
- Binding the records to a spec's records region. `read_bindings` reads records under the build
  folders only (`tools/memory-tree/tree_lib.py:421-425`), so a record under `memory/loop-review/` is
  never listed in TOOL-dCalibratedLens-2's, -3's or -5's records region; the Serves line names the
  kind's owning unit and nothing more.
- Dropping `check = "record-kinds"` from the rows, the other option the review names: it leaves
  spec-5 AC9 unpassable and the three schemas declared and never graded.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `render_ledger_snapshot` and `write_ledger_snapshot`, whose template S1 amends; without them there is no snapshot to grade
- **consumes-from** `TOOL-dCalibratedLens-3` — `render_loop_record`, `write_loop_record` and the `--fixture` frame the plant joins
- **consumes-from** external — TOOL-dTotalRecall-42 S5 and TOOL-dTotalRecall-53 S21 (`derive_record_kind`, the kind read from a record's Serves line) and PLAY-dOrderedCharter-42 (`TYPED_RECORD_KINDS`), DEFERRED at base; a build-run precondition, re-grounded at the build run
- **hands-off** external — when the landed `check_record_kinds` takes a record's kind only from `read_bindings`, whose population is the build folders, AC2 reds at the build run and the main loop files this ask on dTotalRecall: THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS · accept `derive_record_kind` reads the Serves kind of a record under any `fields` row's home, seen on a planted `memory/loop-review/` record missing a field

## 4. Design

### Evidence

- `read_bindings` (`tools/memory-tree/tree_lib.py:471`) builds its population from `record_paths`
  (`:421-425`), the build folders' non-spec kind folders, and gives a record with no Serves line kind
  None (`:496-497`). Read at base `8bec4cef`.
- `RECORD_KIND_TOKENS` is a fixed tuple at base (`tree_lib.py:406`); `TYPED_RECORD_KINDS` is
  PLAY-dOrderedCharter-42 S1's and TOOL-dTotalRecall-18 S7's concatenation, absent at base.
- TOOL-dTotalRecall-42 S5 grades a record's fields only against the row `derive_record_kind` returns.

### The line

```markdown
# Value ledger — 2026-W45

**Serves:** value-ledger TOOL-dCalibratedLens-2

**Key:** 2026-W45
```

The line sits in the first 12 unfenced lines, as HYGIENE's "Record bindings" requires; the kind
token is the row's `name`, so `canonical_kind` returns it unchanged.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `serves-kinds` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 to S4, the plant

### Alternatives rejected

- **No Serves line, the kind derived from the home alone.** TOOL-dTotalRecall-42 S5 decides by the
  Serves kind by design, and a home-derived kind is the reading that ancestor replaced.
- **One shared Serves kind `loop-review` for all three.** Three rows, three field lists: one kind
  would grade a keep against the record's fields, the defect id 1 names.

## 5. Production-readiness checklist

- security — no new write path; the line is constant text written by the two existing writers.
- perf / scale — one check subprocess per plant run.
- error / empty / loading states — an absent `record_kinds.py` fails the plant with an `unread` line.
- observability — the check names the record and the missing field.
- risks — an ancestor that never reads Serves outside the build folders leaves the check blind; AC2
  reds at the build run and the ask in §3 is filed, rather than the gap passing.
- testing — the plant of S2 and its staged break of S3.
- migration — N/A: no record exists under `loop-review/` at base.
- user docs — N/A: no help page shows a record's head.

## 6. Acceptance criteria

- **AC1** — When `grep -c '\*\*Serves:\*\* value-ledger TOOL-dCalibratedLens-2\|\*\*Serves:\*\* loop-review TOOL-dCalibratedLens-3' loop_review.py`,
  run from the loop kit directory, and `grep -c 'keep TOOL-dCalibratedLens-5' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md`,
  run from the repository root, both run after this unit's pass, the first counts at least 2 and the
  second at least 1.
  Red when: a template carries no Serves line, or unit 5's keep template was not amended.
- **AC2** — When `python loop_review.py --fixture --plant serves-kinds` runs, the check exits 0 over the
  whole records, and 1 naming `Window` for the cut snapshot and `Ledger` for the cut record.
  Red when: a record missing a required field passes.
  fixture: `record_kinds.py` is TOOL-dTotalRecall-1's and -42's, absent at `8bec4cef`.
- **AC3** — When the plant `serves-kinds` runs under the staged break of S3, it fails, naming the records the check
  read as kind None.
  Red when: records without the line pass as graded.
- **AC4** — When `python loop_review.py price --dry-run --key 2026-W45` runs in the fixture, its third
  output line of the snapshot body is `**Serves:** value-ledger TOOL-dCalibratedLens-2`.
  Red when: the writer's output lacks the line.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 · the `serves-kinds` plant, staged red by writers that drop the Serves line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 36 (HIGH, item H2) of the round-1 spec audit;
  the templates of units 2, 3 and 5 amended at the disposal (their rev-2).

## 10. Reuse audit

The seam extended is the record-kind token list the ancestors grow per kind, TOOL-dTotalRecall-11 S3
(`shape-run`) and TOOL-dWellOiledMachine-32 (`act`): a kind joins `TYPED_RECORD_KINDS` and HYGIENE's
closed list in the pass that lands its row, so its Serves line binds. `python
tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an unread line, never
the walk's exit"`, run once for the set, ranked name stems only; `read_bindings`
(`tools/memory-tree/tree_lib.py:471`) was read by hand, and it is where this unit's precondition
lives. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's order
follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
