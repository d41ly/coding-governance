# TOOL-dGroundRules-44 — the overlap arm's disjoint row is a real string-prefix trap, and the arm refuses a disjoint row that is not one

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-44-deviation-32.md](../build/2026-10-23-build-TOOL-dGroundRules-44-deviation-32.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-44-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-44-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 29 at BLOCKER**, item **B1**, which no other id shares. The row
`TOOL-dGroundRules-40` labels the string-prefix pair, `tools/policy/a.py` against
`tools/policy/ab.py`, is not one: neither string starts with the other, so a raw `startswith`
answers False for it, the right answer by accident. The arm then passes a `check_writes_intersect`
or `covers` staged to a raw prefix compare, which is the regression unit 40 exists to catch, and its
AC3 expects an answer under that staging that cannot occur. This unit is id 29's promotion: the
disjoint row becomes a pair where a raw prefix compare and containment disagree, and the arm checks
that every disjoint row is such a pair before it grades either rule, so a respelled row cannot pass
as the trap again. It repairs `TOOL-dGroundRules-40`, which sits at order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The trap row. The `disjoint` row of `OVERLAP_PAIRS`, the table `TOOL-dGroundRules-40` S1
  places in `tools/check-spec-tokens.test.sh`, is `tools/policy/a` against `tools/policy/ab.py`.
  The second path starts with the first as a string, and neither sits under the other at a path
  component boundary. Observed by AC1, AC2.
- **S2** — The row's own check. Before the arm grades either rule, it tests each `disjoint` row for a
  raw string prefix in either direction. A row that has none fails the arm with a line naming the row
  and the words `not a string-prefix trap`. Observed by AC3.
- **S3** — `TOOL-dGroundRules-40` AC3 restated with the trap row. Under `RAW_BOTH`, both rules answer
  the trap row as intersecting, `True` and exit `0`, which the expected column rejects. On the built
  tree they answer `False` and exit `1`. Observed by AC2.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect` or `overlaps`. Both answer the trap row correctly (§4
  Evidence for `overlaps`; `check_writes_intersect` is first graded once `TOOL-dGroundRules-32` is
  built).
- A third row. The directory-over-file row and the trap row cover the two rules the arm grades.
- The probes' single spelling: `TOOL-dGroundRules-45`. The bare-name source join:
  `TOOL-dGroundRules-46`. The bug-class record: `TOOL-dGroundRules-47`.

### Edges

- **consumes-from** `TOOL-dGroundRules-40` — the `OVERLAP_PAIRS` table and its arm in `tools/check-spec-tokens.test.sh`, whose disjoint row S1 respells and whose loop S2 extends; without them there is no row to repair
- **hands-off** `TOOL-dGroundRules-45` — the trap row as S1 spells it, which that unit's probe reads from the suite rather than restating
- **hands-off** `TOOL-dGroundRules-53` — AC2's shell half, which that unit observes with `TRAP_SH_WHOLE` in place of the stripped `TRAP_SH` (ids 5 and 12 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-54` — AC2, which that unit observes a second time through `PAIRS_TABLE_WHOLE`, reading the trap pair from the suite rather than from `TRAP_PY` and `TRAP_SH` (id 9 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-55` — AC3's read of the table, which that unit records as the side-read form of `criterion-asserts-what-its-own-command-cannot-show.md` (id 12 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-56` — S2's row check, which that unit observes refusing through `check_overlap_pair` run alone, in place of AC3's read of the table (id 14 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-57` — the `NOT_A_TRAP` staging, which that unit spells whole as `NOT_A_TRAP_WHOLE` so `TRAP_PROBE` lists the row (id 19 of the closing diff review round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `0ced625e1`.

- `tools/unattended/lib-unattended.sh:745-750` defines `covers` as "b is a, or sits under it" over
  normalised paths, and `overlaps` as `covers` in either direction.
- Sourcing `tools/unattended/lib-unattended.sh` from the repository root, `overlaps` returned 0 for
  `tools/policy/` against `tools/policy/x.py` and 1 for `tools/policy/a` against `tools/policy/ab.py`.
- In Python, `a.startswith(b) or b.startswith(a)` printed `True` for the trap row and `False` for
  `tools/policy/a.py` against `tools/policy/ab.py`, the row unit 40 wrote (review id 29).
- `tools/check-spec-tokens.py:581` `check_guard_trips`, which `TOOL-dGroundRules-32` S9 has
  `check_writes_intersect` call in either direction, matches the exact path or a path under the
  guard at a `/` boundary, so it answers False both ways for the trap row.

### The arm after S1 and S2

```text
OVERLAP_PAIRS (TOOL-dGroundRules-40 S1):
    tools/policy/       tools/policy/x.py      intersect
    tools/policy/a      tools/policy/ab.py     disjoint          # S1

for each row (a, b, want):
    if want == disjoint and not (a startswith b or b startswith a):       # S2
        fail naming the row and "not a string-prefix trap"; next row
    (TOOL-dGroundRules-40's two verdict checks, unchanged)
```

The S2 test is plain string comparison in the suite and calls neither rule it guards, so a rule
staged wrong cannot also silence the row check.

### Inventory

No identifier is minted. The check sits inside the arm's row loop.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **`tools/pol` against `tools/policy/x.py`.** It is also a trap, but it spans a segment boundary;
  the sibling-file trap is the one a raw compare meets between two files of one directory.
- **The trap stated only in a criterion.** A criterion is observed once and a respelling can shorten
  it; the row check runs on every run of the suite.

## 5. Production-readiness checklist

- security — N/A: a test suite's table and one string test.
- perf / scale — one string comparison per row.
- error / empty / loading states — a disjoint row that is not a trap fails the arm by name.
- observability — the failure line names the row and the reason.
- risks — none beyond the suite.
- testing — AC1 to AC3.
- migration — the suite's assertion count, raised by the row check.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr44`, checked out at the commit under test. The literal probes and
stagings are spelled whole here, once, and the criteria name them:

```text
TRAP_PROBE  = python -c "import re
rows = [l.split() for l in open('tools/check-spec-tokens.test.sh', encoding='utf-8') if 'disjoint' in l and l.count('tools/policy/') == 2]
for r in rows:
    a, b = [t for t in r if t.startswith('tools/policy/')]
    raw = a.startswith(b) or b.startswith(a)
    inside = a.rstrip('/') == b.rstrip('/') or b.startswith(a.rstrip('/') + '/') or a.startswith(b.rstrip('/') + '/')
    print(a, b, raw, inside)"
TRAP_PY     = python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d; print(d.check_writes_intersect(['tools/policy/a'], ['tools/policy/ab.py']))"
TRAP_SH     = bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'
RAW_BOTH    = in the scratch copy, check_writes_intersect and covers both staged to a raw string
              startswith in either direction
NOT_A_TRAP  = in the scratch copy, the disjoint row respelled a.py tools/policy/ab.py
```

- **AC1** — When `TRAP_PROBE` runs on the built tree, it prints one line ending `True False`.
  Red when: the disjoint row is a pair a raw prefix compare and containment answer alike.
- **AC2** — When `TRAP_PY` and `TRAP_SH` run on the built tree, they print `False` and `1`; when
  `RAW_BOTH` runs and they run in that copy, they print `True` and `0`.
  Red when: the trap row cannot tell a raw prefix compare from containment, so the arm's expected
  column could not either.
- **AC3** — When `NOT_A_TRAP` runs and `TRAP_PROBE` runs in that copy, it prints one line ending
  `False False`, the row S2's check refuses by name.
  Red when: a respelled disjoint row that both rules answer alike reaches the verdict checks.

## 7. Gates

`spec-tokens self-test` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC2 AC3 · `RAW_BOTH` staged in a scratch copy, where the trap row's verdict check reds, and `NOT_A_TRAP` staged there, where the row check reds by name · that suite's assertion count, raised by the row check

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 29 (BLOCKER, item B1) of the round-1 spec
  audit of units 35 to 43, from the review's sound fix, with `overlaps`, `check_guard_trips` and a
  raw prefix compare run on the trap row on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-53`, `TOOL-dGroundRules-55`, `TOOL-dGroundRules-56`, `TOOL-dGroundRules-57`, the reciprocal ends the disposal of
  the closing diff review round 1 wrote; no scope or criterion moved.
- rev-3 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-54`, the reciprocal end of id 9's promotion, and
  the edge to `TOOL-dGroundRules-53` narrowed to ids 5 and 12; no scope or criterion moved.

## 10. Reuse audit

The seam extended is the arm `TOOL-dGroundRules-40` S1 places in `tools/check-spec-tokens.test.sh`,
with `overlaps` (`tools/unattended/lib-unattended.sh:750`) and `check_writes_intersect` as its two
subjects; nothing is built beside them. `python tools/codebase-map/reuse_lookup.py "read test table
rows from a suite file to probe two overlap rules"` ranked name-stem hits only (`rows`, `row`,
`read`), none of which tests a row's own shape, so the row check is three lines inside the loop that
exists. The recall probe returned `TOOL-dGroundRules-42`, `TOOL-dGroundRules-40` and the open ask
`TOOL-aKeyedAnnotation-9`; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
