# TOOL-dCalibratedLens-19 — the three Loop Review record kinds homed at their id-rules' globs, so no record sits under another kind's home

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-19-deviation-191.md](../build/2026-11-02-build-TOOL-dCalibratedLens-19-deviation-191.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1, HIGH, item H1 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). The `value-ledger`
row (unit 2), the `loop-review` row (unit 3) and the `keep` row (unit 5) of
`tools/memory-tree/record-kinds.toml` each set `home = "<MEMORY_ROOT>/loop-review/"` with
`form = "fields"` and a different field list (spec-2 §4 "The registry row", spec-3 §4 "The registry
row", spec-5 §4 "The registry row"). The ancestor these rows meet is TOOL-dTotalRecall-42 at rev-2,
read at its newest revision: its S4 refuses a home that ends in `/` or names a directory, naming the
row, so all three rows red the check as written; its S5 grades a record only against the row its
Serves kind names, so a record under two homes is graded once and overlapping homes give no red.
TOOL-dTotalRecall-1 S4's reading, every record under a home graded by that home's row, is the one -42
S5 replaced. This unit makes each home the glob of its own `id-rule`, which S4 admits and which keeps
each home naming its own kind's files, and proves it on a tree holding a snapshot and a record. It
repairs `TOOL-dCalibratedLens-3`, the unit at which the second row of the shared home lands.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the three sibling specs' text (each at
  rev-2, its §4 "Amendments (round-1 spec audit)", id 1): the `value-ledger` home is
  `memory/loop-review/*-value-ledger-*.md`, the `loop-review` home `memory/loop-review/*-loop-review-*.md`
  and the `keep` home `memory/loop-review/*-keep-*.md`, each the glob of the row's `id-rule`, spelled
  with this repository's memory root as TOOL-dTotalRecall-42 S1 spells the shape-run home; and unit 2
  S8's check-3 prose names `loop-review/` and its THREE kinds. The folder, the file names and every
  reader of a record path are unchanged, because the glob narrows what a row admits and moves no
  file. That the three globs match disjoint files is observed by `TOOL-dCalibratedLens-33`'s
  `disjoint-homes` case, never inferred from the record-kind check, which grades by Serves kind.
  Observed by AC2.
- **S2** — The proof, a `--fixture` plant `three-homes` in `tools/loop/loop_review.py`: in a scratch
  worktree it writes one snapshot through `write_ledger_snapshot` and one record through
  `write_loop_record`, commits them, and runs `python <memory-tree kit>/record_kinds.py --check` there
  as a bounded subprocess (60 s). The check exits 0, and the same tree with the snapshot's
  `**Window:**` line absent exits 1 naming the snapshot's path and `Window` and not naming the record,
  the per-record grading TOOL-dTotalRecall-42 S5 gives. The plant writes no keep at this order: the
  `keep` row is unit 5's, at order 11, and unit 5 adds its keep to this plant in that pass (round-2 id
  1, `TOOL-dCalibratedLens-35`). A `record_kinds.py` absent from the scratch tree's kit prints
  `three-homes — unread · record_kinds.py absent` and fails the plant, never passes it. Observed by
  AC2 and AC3.
- **S3** — The plant's red twin is `TOOL-dCalibratedLens-32`'s `bare-home` case: the real
  `loop-review` row's home rewritten in place to the bare folder, which TOOL-dTotalRecall-42 S4
  refuses naming the row. Its red rests on that clause; no case here expects a cross-graded record,
  since -42 S5 gives none. Observed by AC3.

## 3. Non-goals (OUT)

- Moving any record to another folder. A directory per kind was the alternative the skeptic offered
  first; it re-points every reader (units 15, 16 and 17 read records under the folder) for a result a
  narrower glob already gives (§4 "Alternatives rejected").
- A `record-kinds` check that refuses two `fields` homes matching one path. TOOL-dTotalRecall-42
  rejected that check in its own design ("deciding by the Serves kind needs no disjoint homes"), and
  this unit does not re-open an ancestor's ruling; the disjoint globs make the class harmless here.
- The `**Serves:**` line each template needs for TOOL-dTotalRecall-42 S5's kind derivation:
  `TOOL-dCalibratedLens-20`, id 36.
- The `unarmed` key and the check run after each landing: `TOOL-dCalibratedLens-30`, id 37.
- The red twin, the disjointness case and the graded-by-a-row case: `TOOL-dCalibratedLens-32`, `-33`
  and `-35` (the round-2 audit's ids 26, 2 and 1). The leg's guard reaching `record_kinds.py`:
  `TOOL-dCalibratedLens-41`, id 13.
- AC1 observes only the disposal's text in sibling specs and the row this pass writes, and is a
  precondition, not an observation of the plant (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `write_ledger_snapshot` and the `value-ledger` row, whose home S1 narrows; without them the plant has no snapshot to grade
- **consumes-from** `TOOL-dCalibratedLens-3` — `write_loop_record`, the `loop-review` row and the `--fixture` frame the plant joins; without them there is no record and no plant runner
- **hands-off** `TOOL-dCalibratedLens-32` — the `three-homes` plant and its scratch worktree, which that unit's `bare-home` case mutates (round-2 id 26)
- **hands-off** `TOOL-dCalibratedLens-33` — the plant's committed records, which that unit's `disjoint-homes` case lists (round-2 id 2)
- **hands-off** `TOOL-dCalibratedLens-35` — the records the plant writes, which that unit's `graded-by-a-row` case grades (round-2 id 1)

## 4. Design

### Evidence

- The three rows of `tools/memory-tree/record-kinds.toml` as audited: spec-2 §4 "The registry row" `home = "<MEMORY_ROOT>/loop-review/"`, spec-3
  §4 the same, spec-5 §4 the same, read at the blobs the review record pins (its Reviewed line).
- TOOL-dTotalRecall-42 S1 narrows the shape-run home to `memory/builds/*/build/*-shape-run-*.md`, the
  glob of its id-rule, and its S4 reds a home ending in `/`: the precedent this unit follows.
- The id-rules are disjoint: `<date>-value-ledger-<key>.md`, `<date>-loop-review-<key>.md` and
  `<date>-keep-<key hash>[-<n>].md`. A key is held to `^\d{4}-(W\d{2}|\d{2})$` or
  `^n\d+\.[0-9a-f]{12}$` (spec-2 §4 "The snapshot") and a key hash is 16 hex, so no key spells
  `-value-ledger-`, `-loop-review-` or `-keep-` and no file name matches two globs.

### The keep

The plant writes no keep at this order (round-2 id 1). The keep record's shape is spec-5 §4 "The keep
record", and unit 5 adds one to this plant when it lands the `keep` row.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `three-homes` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 and S3, the plant

### Alternatives rejected

- **A staged break of overlapping homes.** Rejected at the round-2 audit (id 26): TOOL-dTotalRecall-42
  S5 grades by Serves kind, so the overlap exits 0 and the twin can never red.
- **A sibling directory per kind** (`loop-review/reviews/`, `/ledger/`, `/keeps/`). The test: count the
  readers that name the folder in the audited specs, units 2 S7, 15 S6, 16 S6 and 17 S5; each would
  move, and the view's reader too, for a disjointness the id-rule globs already give with none moving.
- **An ask on dTotalRecall to scope S4 by `id-rule`.** It defers the fix to another build's run and
  leaves this build's rows refused by TOOL-dTotalRecall-42 S4 meanwhile.

## 5. Production-readiness checklist

- security — no new write path: the plant writes only under its scratch worktree, through the writers
  units 2 and 3 already contain under the home.
- perf / scale — one `record_kinds.py --check` subprocess per plant run.
- error / empty / loading states — an absent `record_kinds.py` fails the plant with an `unread` line,
  never a pass.
- observability — the check's own lines name the record and the field.
- risks — a fourth kind added under `loop-review/` later must take its own id-rule glob; the
  `bare-home` case reds if a row takes the bare folder.
- testing — the plant of S2; its red twin is `TOOL-dCalibratedLens-32`'s case.
- migration — N/A: no record exists under `loop-review/` at base.
- user docs — N/A: no help page names a registry home.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^home = "memory/loop-review/' record-kinds.toml` runs from the memory-tree
  kit directory after this unit's pass, it prints the `*-value-ledger-*.md` and `*-loop-review-*.md` homes, and
  `grep -c 'home = "memory/loop-review/\*-keep-\*.md"' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md`,
  run from the repository root, prints 1.
  Red when: a row's home is the bare folder, or unit 5's keep row was not amended.
  A precondition read at writing: it greps the disposal's text and the row this pass writes.
- **AC2** — When `python loop_review.py --fixture --plant three-homes` runs from the loop kit
  directory, the plant prints `three-homes — ok` and `record_kinds.py --check` inside it exited 0
  over the snapshot and the record.
  Red when: a narrowed home is refused, or a planted record is graded against another kind's fields.
  fixture: `record_kinds.py` is TOOL-dTotalRecall-1's, absent at `8bec4cef`; a build-run precondition.
- **AC3** — When the same plant runs with the snapshot's `**Window:**` line cut, `record_kinds.py
  --check` exits 1 naming the snapshot's path and `Window` and not the record.
  Red when: the missing field passes, or the record is named for the snapshot's field.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 · the `three-homes` plant, staged red by the snapshot's `**Window:**` line cut; its home red twin is `TOOL-dCalibratedLens-32`'s · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 1 (HIGH, item H1) of the round-1 spec audit;
  the rows of units 2, 3 and 5 amended at the disposal (their rev-2).
- rev-2 · 2026-11-02 · §1 §3 §4 §5 §7 S1 S2 S3 AC1 AC2 AC3 · amended at the disposal of the round-2
  spec audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: §1 re-grounded on
  TOOL-dTotalRecall-42 S4 and S5 (id 11, `TOOL-dCalibratedLens-34`); S3's overlap twin replaced by
  the bare-folder case (id 26, `TOOL-dCalibratedLens-32`); S1's disjointness pointed at the listing
  case (id 2, `TOOL-dCalibratedLens-33`); the plant writes no keep and AC3 reads the snapshot (id 1,
  `TOOL-dCalibratedLens-35`); AC1 stated a precondition (ids 4, 18, 29) and the guard pointer added
  (id 13), both `TOOL-dCalibratedLens-41`; §3 gains the hands-offs to units 32, 33 and 35.

## 10. Reuse audit

The seam extended is TOOL-dTotalRecall-42 S1's home grammar, a row's home narrowed to its id-rule's
glob, applied to three rows instead of one. `python tools/codebase-map/reuse_lookup.py "isolate each
reader so one failure becomes an unread line, never the walk's exit"`, run once for this disposal's
set, ranked name stems only (`read_text`, `read`, `walk`), none a registry home; `record_kinds.py` is
absent at base, so no existing code seam fits and the precedent is the ancestor's spec. The recall
probe returned TOOL-cMendedVintage-19, the ruling that places a promoted repair immediately after the
unit it repairs, which this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
