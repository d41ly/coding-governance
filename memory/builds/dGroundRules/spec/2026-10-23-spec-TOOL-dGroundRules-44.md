# TOOL-dGroundRules-44 — the overlap arm's disjoint row is a real string-prefix trap, and the arm refuses a disjoint row that is not one

**Status:** DEFERRED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

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
answers False for it, the right answer by accident. A `check_writes_intersect` or `covers` staged
to a raw prefix compare therefore passes the arm unit 40 exists to grade.

`TOOL-dGroundRules-40` rev-4 took the respelling itself: its S1 makes the disjoint row the
string-prefix trap `policy` against `policy-x.py`, spelled relative to the suite's prefix `PFX`,
and its AC3 observes the row under `RAW_BOTH`. What id 29 still asks for is a guard on the row: the
arm checks that every disjoint row is a pair a raw prefix compare and containment answer apart
before it grades either rule, so a respelled row cannot pass as the trap again. This unit is that
check. It extends the arm `TOOL-dGroundRules-40` builds at order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The trap row, already `TOOL-dGroundRules-40` S1's, which this unit builds nothing for.
  The `disjoint` row of `OVERLAP_PAIRS` in `tools/check-spec-tokens.test.sh` is `policy` against
  `policy-x.py`, each joined to `PFX` at use. The second path starts with the first as a string,
  and neither sits under the other at a path component boundary. Any row this unit names is spelled
  that way, relative to `PFX`; the suite spells no literal prefix. Observed by AC1, AC2.
- **S2** — The row's own check, the work this unit builds. Before the arm grades either rule, it
  tests each `disjoint` row for a raw string prefix in either direction. A row that has none adds a
  disagreement naming the row and the words `not a string-prefix trap` to the arm's one assertion,
  which then fails. Observed by AC3.
- **S3** — The trap row under `RAW_BOTH`, already `TOOL-dGroundRules-40` AC3, which this unit
  builds nothing for. Under `RAW_BOTH` both rules answer the trap row as intersecting, `True` and
  exit `0`, which the expected column rejects; on the built tree they answer `False` and exit `1`.
  AC2 observes it again because S2 is graded only against a row that is a trap. Observed by AC2.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect` or `overlaps`. Both answer the trap row correctly (§4
  Evidence). `TOOL-dGroundRules-32` is built (5412bbecd): the arm that grades both rules exists in
  `tools/check-spec-tokens.test.sh`, and `TOOL-dGroundRules-40` adds its table.
- The trap row's spelling and the `RAW_BOTH` observation: `TOOL-dGroundRules-40` S1 and AC3.
- A third row. The directory-over-file row and the trap row cover the two rules the arm grades.
- The probes' single spelling: `TOOL-dGroundRules-45`. The bare-name source join:
  `TOOL-dGroundRules-46`. The bug-class record: `TOOL-dGroundRules-47`.

### Edges

- **consumes-from** `TOOL-dGroundRules-40` — the `OVERLAP_PAIRS` table and its arm in `tools/check-spec-tokens.test.sh`, its trap disjoint row (its S1, this unit's S1) and its `RAW_BOTH` observation (its AC3, this unit's S3), whose row loop S2 extends; without them there is no row to check
- **hands-off** `TOOL-dGroundRules-45` — the trap row as S1 spells it, which that unit's probe reads from the suite rather than restating
- **hands-off** `TOOL-dGroundRules-53` — AC2's shell half, which that unit observes with `TRAP_SH_WHOLE` in place of `TRAP_SH` (ids 5 and 12 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-54` — AC2, which that unit observes a second time through `PAIRS_TABLE_WHOLE`, reading the trap pair from the suite rather than from `TRAP_PY` and `TRAP_SH` (id 9 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-55` — AC3's read of the table, which that unit records as the side-read form of `criterion-asserts-what-its-own-command-cannot-show.md` (id 12 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-56` — S2's row check, which that unit observes refusing through `check_overlap_pair` run alone, in place of AC3's read of the table (id 14 of the closing diff review round 1)
- **hands-off** `TOOL-dGroundRules-57` — the `NOT_A_TRAP` staging, which that unit spells whole as `NOT_A_TRAP_WHOLE` so `TRAP_PROBE` lists the row (id 19 of the closing diff review round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 7a600abf5, from the repository root.

- `covers` in `tools/unattended/lib-unattended.sh` is "b is a, or sits under it" over normalised
  paths, and `overlaps` beside it is `covers` in either direction.
- `check_guard_trips` in `tools/memory-tree/design_lib.py` matches the exact path or a path under
  the guard at a `/` boundary, never a bare prefix; `check_writes_intersect` beside it holds that in
  either direction (`TOOL-dGroundRules-32` S9). So it answers False both ways for the trap row.
- Run at this repository's prefix, where `PFX` is `tools/`: `TRAP_PY` of §6 printed `False`,
  `TRAP_SH` printed `1`, and a raw `startswith` in either direction printed `True` for the trap row.
- The arm `TOOL-dGroundRules-32` built is the block headed by its S9 comment in
  `tools/check-spec-tokens.test.sh`; at 7a600abf5 it still runs the unit 40 pair through two inline
  lists. `TOOL-dGroundRules-40` rev-4 S1 gives it the `OVERLAP_PAIRS` table read below, and `TRAP_PROBE` of
  §6 printed nothing on that tree and one line per disjoint row on a scratch file holding the table
  as that S1 spells it.

### The arm after S2

```text
OVERLAP_PAIRS (TOOL-dGroundRules-40 S1, each path relative to ${PFX}):
    policy/    policy/x.py    intersect
    policy     policy-x.py    disjoint

for each row (a, b, want), a and b joined to ${PFX}:
    if want == disjoint and not (a startswith b or b startswith a):       # S2
        a disagreement naming the row and "not a string-prefix trap"; next row
    (TOOL-dGroundRules-40's two verdict checks, unchanged)
```

The S2 test is plain string comparison in the suite and calls neither rule it guards, so a rule
staged wrong cannot also silence the row check. Joining `${PFX}` to both paths keeps their string
relation, so the test reads the same before or after the join.

### Inventory

No identifier is minted. The check sits inside the arm's row loop.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **The row check asking either rule.** The staging it guards against would then reach the check
  too; plain string comparison shares no state with the rules it guards.
- **The trap stated only in a criterion.** A criterion is observed once and a respelling can shorten
  it; the row check runs on every run of the suite.

## 5. Production-readiness checklist

- security — N/A: a test suite's table and one string test.
- perf / scale — one string comparison per row.
- error / empty / loading states — a disjoint row that is not a trap fails the arm by name.
- observability — the failure line names the row and the reason.
- risks — none beyond the suite.
- testing — AC1 to AC3.
- migration — none: the row check adds its disagreement to `TOOL-dGroundRules-40`'s list inside
  the arm's one assertion, so the suite's assertion count and its floor do not move.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root, or, in a scratch copy, from that copy's root. The
literal probes and stagings are spelled whole here, once, and the criteria name them. `TRAP_PY` and
`TRAP_SH` name the trap row read at this repository's prefix, `PFX` being `tools/`; `TRAP_PROBE`
and `NOT_A_TRAP` name rows as the suite holds them, relative to `PFX`:

```text
SCRATCH     = a git clone of this repository under %TEMP%/gr44, checked out at the commit under test
TRAP_PROBE  = python -c "import re
for l in open('tools/check-spec-tokens.test.sh', encoding='utf-8'):
    t = re.sub('[\"()]', ' ', l).split()
    p = [w for w in t if w.startswith('policy')]
    if t and t[0] != '#' and t[-1] == 'disjoint' and len(p) == 2:
        a, b = p
        print(a, b, a.startswith(b) or b.startswith(a), a.rstrip('/') == b.rstrip('/') or b.startswith(a.rstrip('/') + '/') or a.startswith(b.rstrip('/') + '/'))"
TRAP_PY     = python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d; print(d.check_writes_intersect(['tools/policy'], ['tools/policy-x.py']))"
TRAP_SH     = bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy tools/policy-x.py; echo $?'
RAW_BOTH    = in SCRATCH, the staging of that name in TOOL-dGroundRules-40 section 6:
              check_writes_intersect and covers both staged to a raw string startswith in either direction
NOT_A_TRAP  = in SCRATCH, the disjoint row of OVERLAP_PAIRS respelled  policy/a.py  policy/ab.py  disjoint
```

`TRAP_PROBE` lists each non-comment line of the suite whose last word is `disjoint` and which holds
exactly two words starting `policy`, so it reads the table row whether it stands alone or as a call
line; it prints the two paths, the raw prefix answer and the containment answer.

- **AC1** — When `TRAP_PROBE` runs on the built tree, it prints one line, naming the trap row's two paths and ending `True False`.
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

New arm: tools/check-spec-tokens.test.sh · covers AC2 AC3 · `NOT_A_TRAP` staged in a scratch copy, where the row check this unit adds reds by name; `RAW_BOTH` staged there reds the verdict check `TOOL-dGroundRules-40` builds in the same arm · none: the row check adds a disagreement to that arm's one assertion

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
- rev-4 · 2026-10-24 · §1 S1 S3 §3 §4 §5 §6 AC1 AC2 AC3 §7 §10 · disagreements, from a read-only probe of
  step 14 at 0860b8c1e: `TOOL-dGroundRules-40` rev-4 already respells the disjoint row as the trap
  `policy` against `policy-x.py` and observes it under `RAW_BOTH`, so S1 and S3 duplicated it;
  S1 and the §4 table spelled a literal `tools/` prefix the suite never spells; `TRAP_PROBE`
  filtered rows holding two `tools/policy/` words and saw neither that row nor a planted one;
  `TRAP_SH` sourced a bare file name and named a bare operand; §4 cited `check_guard_trips` in
  the wrong file; §3 said `TOOL-dGroundRules-32` was unbuilt; citations into
  `tools/unattended/lib-unattended.sh` were by line. Ruled: S1 and S3 restated as
  `TOOL-dGroundRules-40`'s, S2 the work that remains; every row named relative to `PFX`;
  `TRAP_PROBE` filters that row spelling; `TRAP_SH` sources the tracked path and names whole
  paths; `check_guard_trips` cited in `tools/memory-tree/design_lib.py`; §3 states
  `TOOL-dGroundRules-32` built; every citation by symbol; `RAW_BOTH` points at the staging
  `TOOL-dGroundRules-40` spells; the scratch copy's path moved into the fenced block; §5 and the
  arm line had the row check raise the assertion count against `TOOL-dGroundRules-40`'s one
  assertion, ruled: its disagreement joins that list and no count or floor moves.

## 10. Reuse audit

The seam extended is the arm `TOOL-dGroundRules-32` built and `TOOL-dGroundRules-40` S1 tables in
`tools/check-spec-tokens.test.sh`, with `overlaps` of `tools/unattended/lib-unattended.sh` and
`check_writes_intersect` of `tools/memory-tree/design_lib.py` as its two subjects; nothing is built
beside them. `python tools/codebase-map/reuse_lookup.py "check a test table row is a string-prefix
trap before grading two overlap rules"` ranked name-stem hits (`rows`, `row`, `check`, `before`)
and the seam `overlaps`, the arm's own subject; none tests a row's own shape, so the row check is
three lines inside the loop that exists. The recall probe returned `TOOL-dGroundRules-42`,
`TOOL-dGroundRules-47`, `TOOL-dGroundRules-46` and this spec; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
