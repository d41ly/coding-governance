# TOOL-dGroundRules-45 — the overlap probes read their pairs from the arm's table, so no criterion spells a pair a second time

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-45-deviation-33.md](../build/2026-10-23-build-TOOL-dGroundRules-45-deviation-33.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 20 at HIGH**, which shares item **H1** with ids 1
(`TOOL-dGroundRules-47`) and 10 (`TOOL-dGroundRules-46`). Id 20 is H1 seen from reuse:
`TOOL-dGroundRules-40` promised its criteria would spell the pairs whole, then restated them a second
time in `PAIRS_SH`, copied from `TOOL-dGroundRules-34` AC16 with the library path and the pair
prefixes stripped, so `TOOL-dGroundRules-40` AC2 and `TOOL-dGroundRules-43` AC1, which runs the same
literal, can never pass. Every restatement of the pairs has been a fresh chance to strip them. This
unit is id 20's promotion: the arm's rows take a form a probe can list, and one probe reads those
rows and grades both rules on each, so the pairs are spelled in exactly one place and every criterion
that observes them goes through it. It repairs `TOOL-dGroundRules-40`, which sits at order 13, so it
builds at order 14.

## 2. Scope (IN)

- **S1** — The row form. Each row of `OVERLAP_PAIRS` in `tools/check-spec-tokens.test.sh` is one
  call line, `check_overlap_pair <a> <b> <intersect|disjoint>`, and `check_overlap_pair` is the arm's
  per-row grading. The table is those call lines, so `grep '^check_overlap_pair '` lists exactly the
  rows the arm grades. Observed by AC1, AC3.
- **S2** — The probe. `PAIRS_TABLE` (§6) reads those lines and prints, for each row, the two paths,
  the expected answer, the answer of `check_writes_intersect` and the exit of `overlaps`. It spells no
  pair of its own. Observed by AC2, AC3.
- **S3** — The consumers. `TOOL-dGroundRules-40` AC1, AC2 and the probe half of its AC3, and
  `TOOL-dGroundRules-43` AC1, are observed at this unit's close through `PAIRS_TABLE`.
  Observed by AC2.

## 3. Non-goals (OUT)

- The trap row's spelling and the row check: `TOOL-dGroundRules-44`. This unit reads the rows as
  that unit leaves them.
- Any change to `check_writes_intersect` or `overlaps`.
- The bare-name source join and the bug-class record: `TOOL-dGroundRules-46` and
  `TOOL-dGroundRules-47`.

### Edges

- **consumes-from** `TOOL-dGroundRules-40` — the `OVERLAP_PAIRS` arm in `tools/check-spec-tokens.test.sh`, whose rows S1 gives a listable form, and the criteria AC1 to AC3 S3 observes through `PAIRS_TABLE`
- **consumes-from** `TOOL-dGroundRules-44` — the trap row and the row check, which S1's call lines carry unchanged
- **consumes-from** `TOOL-dGroundRules-43` — AC1, which S3 observes through `PAIRS_TABLE` in place of the stripped `PAIRS_SH`
- **hands-off** `TOOL-dGroundRules-52` — `PAIRS_TABLE`, through which that unit observes `TOOL-dGroundRules-40` AC2, `TOOL-dGroundRules-43` AC1 and the Python rule's first grading (ids 30, 12 and 17)
- **hands-off** `TOOL-dGroundRules-58` — `PAIRS_TABLE`, which that unit spells whole as `PAIRS_TABLE_WHOLE`, the library sourced by its tracked path, and through which it observes AC2 and AC3 (id 4 of the closing diff review, round 1)
- **hands-off** `TOOL-dGroundRules-59` — S3's routing of `TOOL-dGroundRules-40` AC1 to AC3 and `TOOL-dGroundRules-43` AC1, which that unit takes through `PAIRS_TABLE_WHOLE` (id 13 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `0ced625e1`.

- `TOOL-dGroundRules-40` §6 spells `PAIRS_PY` with whole paths and `PAIRS_SH` with a bare library
  name and stripped pairs; `TOOL-dGroundRules-34` AC16 (:509) carries the same stripped form
  (review ids 1, 10 and 20).
- `TOOL-dGroundRules-43` AC1 runs `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6.
- `tools/check-spec-tokens.test.sh:225` defines `arm`, the suite's assertion helper, which a row
  call reaches.
- `python tools/lexicon/lexicon.py --suggest check_overlap_pair --as sh.function` answered OK.

### The arm after S1

```text
check_overlap_pair() {            # $1 a · $2 b · $3 intersect|disjoint
    (TOOL-dGroundRules-44's row check, then TOOL-dGroundRules-40's two verdict checks, on $1 $2 $3)
}
check_overlap_pair tools/policy/ tools/policy/x.py intersect
check_overlap_pair tools/policy/a tools/policy/ab.py disjoint
```

A call line opens at column 0, so the definition line, which carries `()`, is not matched by
`^check_overlap_pair `.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_overlap_pair` | sh.function | `tools/check-spec-tokens.test.sh` |

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **`PAIRS_SH` respelled whole in a criterion.** It closes this instance and leaves a second
  spelling of the pairs, which is the form that was stripped twice.
- **A tracked data file both the arm and the probe read.** It adds a file and a reader for two rows
  the suite already holds.

## 5. Production-readiness checklist

- security — N/A: a test suite's table and a read-only probe.
- perf / scale — two rows; the probe starts one interpreter and one shell per row.
- error / empty / loading states — a table with no call line makes `PAIRS_TABLE` print nothing,
  which AC1's count reds.
- observability — each probe line carries the row and both verdicts.
- risks — none beyond the suite.
- testing — AC1 to AC3.
- migration — none; the arm grades the same rows.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr45`, checked out at the commit under test. The literal probes are spelled whole here, once,
and the criteria name them:

```text
ROW_COUNT   = grep -c '^check_overlap_pair ' tools/check-spec-tokens.test.sh
PAIRS_TABLE = grep '^check_overlap_pair ' tools/check-spec-tokens.test.sh | while read -r _ a b want; do
                py=$(python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d; print(d.check_writes_intersect(['$a'], ['$b']))")
                sh=$(bash -c ". lib-unattended.sh; overlaps '$a' '$b'; echo \$?")
                echo "$a $b $want $py $sh"
              done
ROW_ADDED   = in the scratch copy, the line "check_overlap_pair tools/a tools/b disjoint" appended
              after the table's last row
```

- **AC1** — When `ROW_COUNT` runs on the built tree, it prints `2`.
  Red when: a row is spelled in a form the arm grades and the probe does not list.
  figure: PINNED, the two rows `TOOL-dGroundRules-40` S1 declares.
- **AC2** — When `PAIRS_TABLE` runs on the built tree, it prints two lines, and on each the last two
  fields are `True 0` where the third is `intersect` and `False 1` where it is `disjoint`.
  Red when: either rule disagrees with the table's expected answer on a row.
- **AC3** — When `ROW_ADDED` runs and `PAIRS_TABLE` runs in that copy, it prints three lines, the
  third naming `tools/a` and `tools/b`.
  Red when: the probe reads a list of its own rather than the rows the arm grades.

## 7. Gates

`spec-tokens self-test` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/check-spec-tokens.test.sh · covers AC2 · the trap row's expected answer staged to `intersect` in a scratch copy, where both verdict checks red · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 20 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43, with the pairs spelled once as the arm's call lines and read by one probe,
  and units 34, 40 and 43's literals read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-58`, `TOOL-dGroundRules-59`, the reciprocal ends of the round-1 closing diff
  review's promotions; no scope or criterion moved.

## 10. Reuse audit

The seam extended is the arm `TOOL-dGroundRules-40` S1 places in `tools/check-spec-tokens.test.sh`;
its rows become the calls of a per-row function inside the same suite, and the probe reads them with
`grep`, so nothing new holds the pairs. `python tools/codebase-map/reuse_lookup.py "read test table
rows from a suite file to probe two overlap rules"` ranked `rows`, `row` and `read`, name-stem hits
that hold no overlap pair; no existing seam fits the probe itself. The recall probe returned
`TOOL-dGroundRules-42`, whose fix keeps a literal whole in a fenced block, and `TOOL-dGroundRules-40`;
both agree with source, and this unit removes the need for a second spelling.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
