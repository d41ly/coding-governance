# TOOL-dGroundRules-59 — the overlap criteria of units 40 and 43 observed through the whole probe, the raw-compare staging included

**Status:** WONTDO · rev-1 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-59-deviation-47.md](../build/2026-10-23-build-TOOL-dGroundRules-59-deviation-47.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-58-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-task.md) | research | TOOL-dGroundRules-58 TOOL-dGroundRules-60 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-59-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-59-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-60 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build's spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
returned CLEAN WITH FIXES with item **H2** at HIGH, raw ids 4, 13 and 20. This unit is **id 13**, the
verification lens: the probe's shell column is `127` on every row, so no criterion routed through
`PAIRS_TABLE` can pass on a correct build. `TOOL-dGroundRules-45` S3 routes four of them through it:
`TOOL-dGroundRules-40` AC1, AC2 and the probe half of AC3, and `TOOL-dGroundRules-43` AC1. Through
`TOOL-dGroundRules-40` S3 those also carry `TOOL-dGroundRules-34` AC15 and AC16, and through
`TOOL-dGroundRules-34` S15 the probe of `TOOL-dGroundRules-32` AC9. This unit observes the four
through `PAIRS_TABLE_WHOLE` of `TOOL-dGroundRules-58` §4, on the built tree and under unit 40's
`RAW_BOTH` staging. It changes no code. It repairs units 40, 43 and 45 at orders 13 and 14, and
consumes `TOOL-dGroundRules-58` at order 17, so it builds at order 18.

## 2. Scope (IN)

- **S1** — The verdicts. `TOOL-dGroundRules-40` AC1, the Python column, and AC2, the shell column,
  and `TOOL-dGroundRules-43` AC1, which runs both, are observed at this unit's close through
  `PAIRS_TABLE_WHOLE`, in place of `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6 and of
  `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6. Observed by AC1.
- **S2** — The raw-compare staging. The probe half of `TOOL-dGroundRules-40` AC3 is observed through
  `PAIRS_TABLE_WHOLE` run from the root of a scratch copy staged with `RAW_BOTH` of that unit's §6:
  both rules answer every row as intersecting, which the expected column rejects on the `disjoint`
  row. Observed by AC2.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect`, `overlaps` or the rows of `OVERLAP_PAIRS`.
- The trap row's spelling and the row check: `TOOL-dGroundRules-44`, and the units that repair its
  literals. S2 reads the `disjoint` row as that unit leaves it, a real string-prefix trap.
- The probe's own spelling and `TOOL-dGroundRules-45` AC2 and AC3: `TOOL-dGroundRules-58`.
- Unit 52's observations through the probe: `TOOL-dGroundRules-60`.
- Rewriting any repaired spec's §6. Each names this unit in its §3 (BUILD-METHOD M4).

### Edges

- **consumes-from** `TOOL-dGroundRules-58` — `PAIRS_TABLE_WHOLE`, the probe S1 and S2 run; without it the criteria route through a probe whose shell column is `127`
- **consumes-from** `TOOL-dGroundRules-40` — AC1, AC2 and the probe half of AC3, and the `RAW_BOTH` staging, which S1 and S2 observe
- **consumes-from** `TOOL-dGroundRules-43` — AC1, which S1 observes
- **consumes-from** `TOOL-dGroundRules-45` — S3's routing of those criteria, which S1 and S2 take through the whole probe

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-45` S3 routes `TOOL-dGroundRules-40` AC1, AC2 and the probe half of AC3, and
  `TOOL-dGroundRules-43` AC1, through `PAIRS_TABLE`, whose library source is bare (review ids 4, 13
  and 20).
- `TOOL-dGroundRules-40` §6 `PAIRS_SH` (lines 129 and 130) also sources the library bare and strips
  the pairs; `TOOL-dGroundRules-43` AC1 runs `PAIRS_PY` and `PAIRS_SH` of that section.
- `TOOL-dGroundRules-40` S3 restates `TOOL-dGroundRules-34` AC15 and AC16, and
  `TOOL-dGroundRules-34` S15 restates `TOOL-dGroundRules-32` AC9's probe; each of those three
  criteria carries the stripped pairs, so this unit's observations are the ones they reach.
- `TOOL-dGroundRules-44` S1 spells the `disjoint` row `tools/policy/a` against `tools/policy/ab.py`.
  Under a raw `startswith` in either direction the pair intersects; under `covers` at
  `tools/unattended/lib-unattended.sh:745` it does not. The `intersect` row, `tools/policy/`
  against `tools/policy/x.py`, intersects under both.
- Sourced by its tracked path, `overlaps` exited `0` for the `intersect` row and `1` for the
  `disjoint` row (`TOOL-dGroundRules-58` §4 Evidence).

### The observations

| Repaired criterion | Field it reads | Observed by |
|---|---|---|
| `TOOL-dGroundRules-40` AC1 | the Python field on both rows | AC1 |
| `TOOL-dGroundRules-40` AC2 | the shell field on both rows | AC1 |
| `TOOL-dGroundRules-43` AC1 | both fields on both rows | AC1 |
| `TOOL-dGroundRules-40` AC3, its probe half | both fields under `RAW_BOTH` | AC2 |

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

### Alternatives rejected

- **`PAIRS_PY` and `PAIRS_SH` respelled whole as this unit's own literals.** A second spelling of the
  pairs is the form that was stripped three times; the rows live once, in the suite, and the probe
  reads them (`TOOL-dGroundRules-45` §4).

## 5. Production-readiness checklist

- security — N/A: a read-only probe and a scratch copy.
- perf / scale — two rows, run twice.
- error / empty / loading states — an empty table prints nothing, which AC1 reds.
- observability — each line carries the row, its expected answer and both verdicts.
- risks — S2 needs the trap row of `TOOL-dGroundRules-44` S1; with a row both compares answer alike,
  AC2 is red, which is the observation that row exists for.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: a gov-only probe.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr59`, checked out at the commit under test. `PAIRS_TABLE_WHOLE` is spelled in
`TOOL-dGroundRules-58` §4 and `RAW_BOTH` in `TOOL-dGroundRules-40` §6.

- **AC1** — When `PAIRS_TABLE_WHOLE` runs on the built tree, the line whose third field is
  `intersect` ends `True 0` and the line whose third field is `disjoint` ends `False 1`.
  Red when: the render's rule or the dispatcher's misreads a directory over a file or a shared
  string prefix, or the library does not load.
  fixture: units 32, 40, 44 and 45 built.
- **AC2** — When `RAW_BOTH` runs and `PAIRS_TABLE_WHOLE` runs from that copy's root, both lines end
  `True 0`.
  Red when: the probe answers the trap row alike with and without a raw prefix compare, so the arm's
  expected column could not reject one.

## 7. Gates

`memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting raw finding id 13 (HIGH, item H2) of the closing diff
  review of the spec run, as the observations `TOOL-dGroundRules-45` S3 routes, taken through the
  whole probe, with the rows and the staging read on 2026-10-23.

## 10. Reuse audit

No existing seam fits beyond the ones observed: the probe is `TOOL-dGroundRules-58`'s and the
staging `TOOL-dGroundRules-40`'s, and nothing is built. `python tools/codebase-map/reuse_lookup.py
"source a shell library by its tracked path and probe two overlap rules per table row"` ranked
`overlaps` of `tools/unattended/lib-unattended.sh`, this unit's subject, and name-stem hits that hold
no pair. The recall probe returned `TOOL-dGroundRules-42`, `TOOL-dGroundRules-46` and
`TOOL-dGroundRules-40`, and the open ask `TOOL-aKeyedAnnotation-9`; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal restored
when a respelling cut it to its basename" --terms "acceptance criterion literal stripped respelled
basename fenced block library source whole path paths join PAIRS_TABLE"`
