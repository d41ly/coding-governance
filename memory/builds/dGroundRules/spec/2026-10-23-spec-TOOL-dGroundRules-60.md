# TOOL-dGroundRules-60 — unit 52's overlap observations taken through the whole probe, with the Python column shown graded on its own

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-60-deviation-48.md](../build/2026-10-23-build-TOOL-dGroundRules-60-deviation-48.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-58-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-task.md) | research | TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-60-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-60-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build's spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
returned CLEAN WITH FIXES with item **H2** at HIGH, raw ids 4, 13 and 20. This unit is **id 20**, the
intent lens: `TOOL-dGroundRules-52` AC5 and the scope items it observes, S5, S12 and S21, route
through `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6, whose shell column is `127` on every row, so the
observations that unit inherits fail on a correct build. S21 says `check_writes_intersect` is first
graded by that probe's Python column; nothing shows the column graded apart from the shell one. This
unit observes unit 52's four items through `PAIRS_TABLE_WHOLE` of `TOOL-dGroundRules-58` §4, and
stages the Python rule alone wrong, so a right `overlaps` is seen not to hide a wrong
`check_writes_intersect`. It changes no code. It repairs `TOOL-dGroundRules-52` at order 16 and
consumes `TOOL-dGroundRules-58` at order 17, so it builds at order 18.

## 2. Scope (IN)

- **S1** — The table. `TOOL-dGroundRules-52` AC5, and through it that unit's S5, S12 and S21, is
  observed at this unit's close through `PAIRS_TABLE_WHOLE` in place of `PAIRS_TABLE`.
  Observed by AC1.
- **S2** — The Python column alone. With `check_writes_intersect` alone staged to a raw string
  `startswith` in either direction, `PY_RAW` (§4), the `disjoint` row's Python field turns `True`
  while its shell field stays `1`, so S21's first grading of the render's rule is observed failing
  on its own. Observed by AC2.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect`, `overlaps` or the rows of `OVERLAP_PAIRS`.
- The probe's spelling: `TOOL-dGroundRules-58`. The criteria of units 40 and 43 that unit 45 routes:
  `TOOL-dGroundRules-59`.
- Every other item of `TOOL-dGroundRules-52`; this unit observes the four that route through the
  probe.
- Rewriting `TOOL-dGroundRules-52` §6. Its §3 names this unit (BUILD-METHOD M4).

### Edges

- **consumes-from** `TOOL-dGroundRules-58` — `PAIRS_TABLE_WHOLE`, the probe S1 and S2 run; without it unit 52's observations route through a probe whose shell column is `127`
- **consumes-from** `TOOL-dGroundRules-52` — S5, S12, S21 and AC5, which S1 observes and S2 shows failable

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-52` S5 (line 77) and S12 (line 102) observe `TOOL-dGroundRules-40` AC2 and
  `TOOL-dGroundRules-43` AC1 through `PAIRS_TABLE`; S21 (line 128) names its Python column as the
  first grading of `check_writes_intersect`; AC5 (line 324) runs it. Its edge to
  `TOOL-dGroundRules-45` names the probe.
- `TOOL-dGroundRules-44` S1 spells the `disjoint` row `tools/policy/a` against `tools/policy/ab.py`,
  a raw string prefix and no containment. `covers` (`tools/unattended/lib-unattended.sh:745`) reads
  containment at a path component boundary, so the shell field stays `1` while only the Python rule
  is staged.

### The staging

```text
PY_RAW = in a scratch copy, check_writes_intersect of tools/memory-tree/design_lib.py staged to
         answer True when either path starts with the other as a string; covers left as built
```

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

### Alternatives rejected

- **`RAW_BOTH` of `TOOL-dGroundRules-40` §6 reused for S2.** It stages both rules, so both fields
  move together and the Python column is never seen graded alone, which is S21's claim.

## 5. Production-readiness checklist

- security — N/A: a read-only probe and a scratch copy.
- perf / scale — two rows, run twice.
- error / empty / loading states — an empty table prints nothing, which AC1 reds.
- observability — each line carries the row, its expected answer and both verdicts.
- risks — S2 needs the trap row of `TOOL-dGroundRules-44` S1; with a row a raw compare answers
  disjoint, AC2 is red.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: a gov-only probe.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr60`, checked out at the commit under test. `PAIRS_TABLE_WHOLE` is spelled in
`TOOL-dGroundRules-58` §4 and `PY_RAW` in §4 here.

- **AC1** — When `PAIRS_TABLE_WHOLE` runs on the built tree, on each line the last two fields are
  `True 0` for `intersect` and `False 1` for `disjoint`.
  Red when: either overlap rule, the Python one included, disagrees with the table.
  fixture: units 32, 40, 44 and 45 built.
- **AC2** — When `PY_RAW` runs and `PAIRS_TABLE_WHOLE` runs from that copy's root, the `disjoint`
  line ends `True 1`.
  Red when: the Python field is not read apart from the shell field, so a wrong
  `check_writes_intersect` passes behind a right `overlaps`.

## 7. Gates

`memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting raw finding id 20 (HIGH, item H2) of the closing diff
  review of the spec run, as unit 52's observations taken through the whole probe, with the Python
  rule staged alone so its first grading is seen failing.

## 10. Reuse audit

No existing seam fits beyond the ones observed: the probe is `TOOL-dGroundRules-58`'s, and the
staging narrows `RAW_BOTH` of `TOOL-dGroundRules-40` to one rule; nothing is built.
`python tools/codebase-map/reuse_lookup.py "source a shell library by its tracked path and probe two
overlap rules per table row"` ranked `overlaps` of `tools/unattended/lib-unattended.sh` and name-stem
hits that hold no pair. The recall probe returned `TOOL-dGroundRules-42`, `TOOL-dGroundRules-46` and
`TOOL-dGroundRules-47`, and the open ask `TOOL-aKeyedAnnotation-9`; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal restored
when a respelling cut it to its basename" --terms "acceptance criterion literal stripped respelled
basename fenced block library source whole path paths join PAIRS_TABLE"`
