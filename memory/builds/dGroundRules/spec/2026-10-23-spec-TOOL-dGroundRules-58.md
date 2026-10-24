# TOOL-dGroundRules-58 — the overlap probe sources the unattended library by its tracked path, so its shell column is a verdict and not a load failure

**Status:** WONTDO · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-58-deviation-46.md](../build/2026-10-23-build-TOOL-dGroundRules-58-deviation-46.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-58-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-58-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-build-brief.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-58-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-task.md) | research | TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-64 |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-59 TOOL-dGroundRules-60 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build's spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
returned CLEAN WITH FIXES with item **H2** at HIGH, raw ids 4, 13 and 20, one defect seen by three
lenses. This unit is **id 4**, the correctness lens: `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6
sources the unattended library by its bare file name, so from the repository root the source fails,
`overlaps` is undefined, and the last field of every row is `127`. `TOOL-dGroundRules-45` AC2 and AC3
cannot pass on a correct build. This unit spells the probe once more with the library's tracked path,
`PAIRS_TABLE_WHOLE` (§4), observes those two criteria through it, and shows the cut spelling answering
`127`, so the probe is seen telling a load failure from a verdict. It changes no code. It repairs
`TOOL-dGroundRules-45`, which sits at order 14, and builds at order 17, after every unit of the spec
run's rounds.

## 2. Scope (IN)

- **S1** — The probe, whole. `PAIRS_TABLE_WHOLE` (§4) is `TOOL-dGroundRules-45`'s `PAIRS_TABLE` with
  the library sourced as `tools/unattended/lib-unattended.sh`, and is the command through which
  `TOOL-dGroundRules-45` AC2 is observed at this unit's close. Observed by AC1.
- **S2** — The added row. `TOOL-dGroundRules-45` AC3, the probe run in a scratch copy after
  `ROW_ADDED` of that unit's §6, is observed through `PAIRS_TABLE_WHOLE`. Observed by AC2.
- **S3** — The negative. `PAIRS_TABLE_CUT` (§4), the same probe with its source operand cut to the
  library's file name, prints `127` as the last field of every row, so the stripped spelling the
  review names is shown to answer differently. Observed by AC3.

## 3. Non-goals (OUT)

- Any change to `check_overlap_pair`, `check_writes_intersect`, `overlaps` or the rows of
  `OVERLAP_PAIRS`. Units 32, 40, 44 and 45 build them; this unit observes them.
- Rewriting `TOOL-dGroundRules-45` §6. A repaired spec's text is not folded (BUILD-METHOD M4); its §3
  names this unit.
- The criteria of units 40, 43 and 52 that route through the probe: `TOOL-dGroundRules-59` (id 13)
  and `TOOL-dGroundRules-60` (id 20).
- The bare-source join and its evidence: `TOOL-dGroundRules-46`, and the minors unit that restates
  that unit's measurement.

### Edges

- **consumes-from** `TOOL-dGroundRules-45` — `PAIRS_TABLE` and `ROW_ADDED`, and the criteria AC2 and AC3, which S1 to S3 observe with the library's path whole
- **hands-off** `TOOL-dGroundRules-59` — `PAIRS_TABLE_WHOLE`, through which that unit observes `TOOL-dGroundRules-40` AC1 to AC3 and `TOOL-dGroundRules-43` AC1 (id 13)
- **hands-off** `TOOL-dGroundRules-60` — `PAIRS_TABLE_WHOLE`, through which that unit observes `TOOL-dGroundRules-52` S5, S12, S21 and AC5 (id 20)
- **hands-off** `TOOL-dGroundRules-54` — `PAIRS_TABLE_WHOLE`, through which that unit observes `TOOL-dGroundRules-44` AC2 on the trap row, a second witness beside `TRAP_SH_WHOLE` (id 9 of the closing diff review round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-45` §6 line 124 sources the library by bare name. `git log` over that spec
  shows one commit, `d794a81bc`, which already holds the bare form, so no committed revision carries
  an original to restore; the whole spelling is the one `TOOL-dGroundRules-40` §4 (`The arm`) and
  `TOOL-dGroundRules-46` §4 write.
- `git ls-files` tracks the library only at `tools/unattended/lib-unattended.sh`, which defines
  `covers` at line 745 and `overlaps` at line 750.
- The probe was run verbatim from the root, as `TOOL-dGroundRules-47` S1 requires, over a scratch
  file holding the two call lines `TOOL-dGroundRules-45` §4 shows in place of the suite, which does
  not hold them at base. The shell field read `0` on the `intersect` row and `1` on the `disjoint`
  row. The cut spelling read `127` on both rows, after
  `lib-unattended.sh: No such file or directory` and `overlaps: command not found`.
- The Python field raised `AttributeError` on both rows at base: `check_writes_intersect` is
  `TOOL-dGroundRules-32` S9's, unbuilt at base.

### The probe

Spelled whole here, once, in a section the spec-tokens paths join does not read, and named by the
criteria. Each runs from the root of the tree it observes.

```text
PAIRS_TABLE_WHOLE = grep '^check_overlap_pair ' tools/check-spec-tokens.test.sh | while read -r _ a b want; do
                      py=$(python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d; print(d.check_writes_intersect(['$a'], ['$b']))")
                      sh=$(bash -c ". tools/unattended/lib-unattended.sh; overlaps '$a' '$b'; echo \$?")
                      echo "$a $b $want $py $sh"
                    done
PAIRS_TABLE_CUT   = PAIRS_TABLE_WHOLE with the operand of its "." command cut to the library's file
                    name, the spelling of TOOL-dGroundRules-45 §6 line 124
```

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

### Alternatives rejected

- **`TOOL-dGroundRules-45` line 124 respelled in place.** It is the review's own fix, and it rewrites
  a reviewed spec's criterion, which BUILD-METHOD M4 keeps to a promoted unit; the brief for these
  promotions asks for the repair as a unit with a hands-off line on the repaired spec.
- **The library's path held in a shell variable the probe expands.** Unit 46's join cannot read an
  operand held in a variable, so the next respelling would pass unseen.

## 5. Production-readiness checklist

- security — N/A: a read-only probe over a tracked suite and a tracked library.
- perf / scale — two rows; one interpreter and one shell start per row.
- error / empty / loading states — a suite with no call line prints nothing, which AC1's two-line
  count reds; a library that does not load prints `127`, which AC1 reds and AC3 expects.
- observability — each line carries the row, its expected answer and both verdicts.
- risks — the observation needs units 32, 40, 44 and 45 built; before then the Python field is an
  error and the grep finds no row.
- testing — AC1 to AC3.
- migration — none.
- user docs — N/A: a gov-only probe.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr58`, checked out at the commit under test. `ROW_ADDED` is the staging of
`TOOL-dGroundRules-45` §6; `PAIRS_TABLE_WHOLE` and `PAIRS_TABLE_CUT` are spelled in §4.

- **AC1** — When `PAIRS_TABLE_WHOLE` runs on the built tree, it prints two lines, and on each the
  last two fields are `True 0` where the third is `intersect` and `False 1` where it is `disjoint`.
  Red when: either rule disagrees with the row's expected answer, or the library does not load and
  the last field is `127`.
  fixture: units 32, 40, 44 and 45 built; at base the suite holds no `check_overlap_pair` row.
- **AC2** — When `ROW_ADDED` runs and `PAIRS_TABLE_WHOLE` runs from that copy's root, it prints three
  lines, the third naming `tools/a` and `tools/b` and ending `False 1`.
  Red when: the probe reads a list of its own rather than the rows the arm grades.
- **AC3** — When `PAIRS_TABLE_CUT` runs on the built tree, the last field of every line it prints is
  `127`.
  Red when: the cut spelling answers like the whole one, so the probe could not show the stripped
  form the review names.

## 7. Gates

`memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting raw finding id 4 (HIGH, item H2) of the closing diff
  review of the spec run, from the skeptic's sound fix taken as a unit, with the probe run from the
  root over a staged two-row table on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-54`, the reciprocal end of id 9's promotion of the
  closing diff review round 1; no scope or criterion moved.

## 10. Reuse audit

No existing seam fits beyond the one observed: the probe is `TOOL-dGroundRules-45`'s `PAIRS_TABLE`
with the library's tracked path, and nothing is built. `python tools/codebase-map/reuse_lookup.py
"source a shell library by its tracked path and probe two overlap rules per table row"` ranked
`overlaps` and `scan_shared_index_overlaps` of `tools/unattended/lib-unattended.sh`, the rule this
probe observes and a caller of it, and name-stem hits (`rows`, `row`, `probe`) that hold no pair. The
recall probe returned `TOOL-dGroundRules-42`, `TOOL-dGroundRules-46` and `TOOL-dGroundRules-47`,
whose class this is, and the open ask `TOOL-aKeyedAnnotation-9` on the paths join; all agree with
source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal restored
when a respelling cut it to its basename" --terms "acceptance criterion literal stripped respelled
basename fenced block library source whole path paths join PAIRS_TABLE"`
