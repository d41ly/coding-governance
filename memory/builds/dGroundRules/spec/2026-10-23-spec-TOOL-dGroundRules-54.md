# TOOL-dGroundRules-54 — the trap row's verdicts observed a second time through the whole overlap probe, which reads the pair from the suite and spells none

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-54-deviation-42.md](../build/2026-10-23-build-TOOL-dGroundRules-54-deviation-42.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 |
| [2026-10-23-prompt-TOOL-dGroundRules-54-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-54-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 9 at HIGH** under item **H1**, which it shares with ids 5, 12, 14 and 19.
Id 9 is H1 seen from seams. `TOOL-dGroundRules-44` AC2 restates the trap pair in `TRAP_PY` and
`TRAP_SH`, beside the suite row its own S1 spells and the probe `TOOL-dGroundRules-45` builds to read
that row. Each restatement is a fresh chance to strip the pair, and `TRAP_SH` was stripped the same way
`PAIRS_TABLE` was. The review names the route this finding owes: observe AC2 through the repaired
probe, so the pair is spelled only in the suite. `TOOL-dGroundRules-53` repairs `TRAP_SH` itself for
ids 5 and 12. This unit is id 9's promotion: it observes `TOOL-dGroundRules-44` AC2 through
`PAIRS_TABLE_WHOLE` of `TOOL-dGroundRules-58`, which reads the pair off the suite's call line. That
gives AC2 a second witness that shares no spelling with unit 53's. It repairs
`TOOL-dGroundRules-44`, which sits at order 14, and reads unit 58's probe, which sits at order 17, so
it builds at order 18.

## 2. Scope (IN)

- **S1** — The built-tree half of `TOOL-dGroundRules-44` AC2 through the probe. On the built tree,
  `PAIRS_TABLE_WHOLE` prints one line whose third field is `disjoint`. Its first two fields are the
  pair `TRAP_PROBE` of `TOOL-dGroundRules-44` §6 lists, and it ends `False 1`. Observed by AC1.
- **S2** — The red half through the probe. In a scratch copy where `RAW_BOTH` of
  `TOOL-dGroundRules-44` §6 is staged, the same line ends `True 0`. Observed by AC2.
- **S3** — No spelling of the pair. This spec spells neither path of the trap row in a literal or a
  criterion; both criteria read the pair from the suite, through `PAIRS_TABLE_WHOLE` and
  `TRAP_PROBE`. Observed by AC1.

## 3. Non-goals (OUT)

- `TRAP_SH_WHOLE` and the shell literal's repair: `TOOL-dGroundRules-53`. The two units observe one
  criterion through two probes, and neither reads the other.
- Any edit to the text of `TOOL-dGroundRules-44` §6 or `TOOL-dGroundRules-58` §4. Each gains only
  the hands-off line to this unit.
- The `intersect` row and the added-row case. `TOOL-dGroundRules-58` observes those, and AC2 of
  `TOOL-dGroundRules-44` grades the trap row only.
- Any change to `overlaps`, `covers`, `check_writes_intersect` or the suite.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — AC2, the trap row its S1 spells, `TRAP_PROBE` and the `RAW_BOTH` staging, which S1 and S2 observe the trap row's verdicts over; without them there is no criterion to witness
- **consumes-from** `TOOL-dGroundRules-58` — `PAIRS_TABLE_WHOLE`, the probe that sources the library by its tracked path and reads each pair from the suite; without it the shell field is `127`

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-44` §6 spells `TRAP_PY` and `TRAP_SH` with the trap pair restated, and
  `TRAP_PROBE` reads the pair from the suite. `TOOL-dGroundRules-58` §4 spells
  `PAIRS_TABLE_WHOLE`, which greps `^check_overlap_pair ` call lines and prints each row's two paths,
  its expected answer, the Python verdict and the shell exit.
- `PAIRS_TABLE_WHOLE`'s shell half was run from the root of a scratch tree that holds the tracked
  library and a mock suite with the two call lines of `TOOL-dGroundRules-45` §4. The `disjoint`
  line's shell field read `1`. With the library's `covers` staged to a raw prefix compare,
  `case "$_cb" in "$_ca"*) return 0 ;; esac`, it read `0`.
- The Python field needs `check_writes_intersect`, which `TOOL-dGroundRules-32` (order 10) adds to
  `tools/memory-tree/design_lib.py`; the tree holds none today.

### How the line is picked

The criteria select the line by its third field, so they need no spelling of the pair: `PAIRS_TABLE_WHOLE`
piped through `awk '$3 == "disjoint"'`. AC1 compares that line's first two fields with the first two
of the one line `TRAP_PROBE` prints, so both probes are shown to read the same row.

### Inventory

No identifier is minted.

### Files touched (estimate)

None. The unit observes a criterion through another unit's probe and writes no product file.

### Alternatives rejected

- **`TRAP_SH_WHOLE` of `TOOL-dGroundRules-53` as this unit's probe too.** It would make one witness
  out of two units, which leaves id 9's finding, the restated pair, where it is.
- **A third probe spelled here.** `PAIRS_TABLE_WHOLE` already reads the row; a third spelling is the
  drift id 9 finds.

## 5. Production-readiness checklist

- security — N/A: a read-only probe over a tracked suite and library.
- perf / scale — one interpreter and one shell start per row, two rows.
- error / empty / loading states — a suite with no `disjoint` call line leaves the filter printing
  nothing, which AC1 reds; a library that does not load leaves `127`, which AC1 reds.
- observability — the line carries the row, its expected answer and both verdicts.
- risks — none: no product file changes.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr54`, checked out at the commit under test. `PAIRS_TABLE_WHOLE` is
spelled in §4 of `TOOL-dGroundRules-58`; `TRAP_PROBE` and `RAW_BOTH` in §6 of `TOOL-dGroundRules-44`.

- **AC1** — When `PAIRS_TABLE_WHOLE` runs on the built tree and its output is filtered by
  `awk '$3 == "disjoint"'`, it prints exactly one line ending `False 1`, whose first two fields equal
  the first two of the line `TRAP_PROBE` prints.
  Red when: either rule answers the trap row as intersecting, the library does not load, or the
  probe reads a row other than the one the trap probe lists.
  fixture: units 32, 40, 44 and 45 built; at base the suite holds no call line.
- **AC2** — When `RAW_BOTH` is staged in the scratch copy and the AC1 command runs from that copy's
  root, the line ends `True 0`.
  Red when: the trap row is a pair a raw prefix compare and containment answer alike, so the staged
  regression passes the probe unseen.

## 7. Gates

`memory hygiene` · `spec-tokens self-test`

The suite arm that stages `RAW_BOTH` is `TOOL-dGroundRules-44`'s `New arm:` line; this unit adds no
arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 9 (HIGH, item H1) of the closing diff
  review round 1 by the review's single-spelling route, through `PAIRS_TABLE_WHOLE` of
  `TOOL-dGroundRules-58`, with the probe's shell half run over a mock suite and a raw-prefix staging
  on 2026-10-23.

## 10. Reuse audit

The seam reused is `PAIRS_TABLE_WHOLE`, the probe `TOOL-dGroundRules-58` §4 spells over the suite's
call lines; this unit filters its output and builds nothing beside it. `python
tools/codebase-map/reuse_lookup.py "run one suite function alone on a staged row to observe its
refusal line"` ranked `rows`, `row` and `run`, name-stem hits that hold no overlap probe, so no
existing seam fits beyond the probe reused. The recall probe returned `TOOL-dGroundRules-45`, whose
probe unit 58 repairs, and `TOOL-dGroundRules-44`, `TOOL-dGroundRules-42` and `TOOL-dGroundRules-47`;
all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
