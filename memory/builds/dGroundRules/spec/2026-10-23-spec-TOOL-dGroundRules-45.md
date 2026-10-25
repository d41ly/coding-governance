# TOOL-dGroundRules-45 — the overlap probes read their pairs from the arm's table, so no criterion spells a pair a second time

**Status:** CLOSED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-45-deviation-33.md](../build/2026-10-23-build-TOOL-dGroundRules-45-deviation-33.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-45-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-45-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-45-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-45-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-43-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-43-staleness-probe-brief.md) | research | TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-46 |
| [2026-10-24-prompt-TOOL-dGroundRules-45-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-45-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-45-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-45-probe-fix-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-52-edge-repair-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-52-edge-repair-brief.md) | research | TOOL-dGroundRules-52 TOOL-dGroundRules-60 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-57 TOOL-dGroundRules-58 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 20 at HIGH**, which shares item **H1** with ids 1
(`TOOL-dGroundRules-47`) and 10 (`TOOL-dGroundRules-46`). Id 20 is H1 seen from reuse: the overlap
pairs were spelled once in the suite and again in each criterion that observed them, and a
restatement had stripped the library path and the pair prefixes, so the criteria running it could
not pass.

That instance is closed. `TOOL-dGroundRules-34` is CLOSED, its AC15 and AC16 handed to
`TOOL-dGroundRules-40`, and `TOOL-dGroundRules-40` rev-4 spells `PAIRS_PY` and `PAIRS_SH` with whole
pairs, `PAIRS_SH` sourcing `tools/unattended/lib-unattended.sh` by its tracked path (§4 Evidence).
The class stands: the pairs still live in the suite's table and again in those two literals, which
`TOOL-dGroundRules-43` AC1 re-runs, and every restatement is a fresh chance to strip them. This unit
is id 20's promotion: the arm's rows take a form a probe can list, and one probe reads those rows the
way the arm grades them and runs both rules on each, so a criterion can observe the pairs without
spelling them. It reshapes the arm `TOOL-dGroundRules-40` builds at order 13, so it builds at order
14.

## 2. Scope (IN)

- **S1** — The row form. Each row of `OVERLAP_PAIRS` in `tools/check-spec-tokens.test.sh` is one
  call line at column 0, `check_overlap_pair` followed by the two paths and the expected answer,
  spelled as `TOOL-dGroundRules-40` rev-4 spells them: each path relative to the suite's install
  prefix `PFX`, the disjoint row being that unit's string-prefix trap (§4 The arm after S1). The
  function joins `${PFX}` to each path, runs both verdict checks, and adds each disagreement to the
  list `TOOL-dGroundRules-40`'s one assertion names; it calls no `arm` and moves no counter. So
  `grep '^check_overlap_pair '` lists exactly the rows the arm grades. Observed by AC1, AC3.
- **S2** — The probe. `PAIRS_TABLE` (§6) reads those lines, joins this repository's `PFX` to each
  path as the arm does, sources `tools/unattended/lib-unattended.sh` by its tracked path, and prints,
  for each row, the two whole paths, the expected answer, the answer of `check_writes_intersect` and
  the exit of `overlaps`. It spells no pair of its own. Observed by AC2, AC3.
- **S3** — The consumers. `TOOL-dGroundRules-40` AC1 and AC2, and `TOOL-dGroundRules-43` AC1, already
  run as spelled once `TOOL-dGroundRules-40` rev-4's whole `PAIRS_PY` and `PAIRS_SH` stand; at this
  unit's close they are observed a second time through `PAIRS_TABLE`, whose lines carry the answers
  those literals print, read from the rows the arm grades. The probe half of `TOOL-dGroundRules-40`
  AC3, under its `RAW_BOTH`, is `TOOL-dGroundRules-59`'s (§3 Edges). Observed by AC2.

## 3. Non-goals (OUT)

- The trap row's spelling: `TOOL-dGroundRules-40` rev-4. The row check: `TOOL-dGroundRules-44`.
  This unit reads the rows as those units leave them.
- Any change to `check_writes_intersect` or `overlaps`.
- Any change to the arm's one assertion or its FAIL line: `TOOL-dGroundRules-40`.
- The bare-name source join and the bug-class record: `TOOL-dGroundRules-46` and
  `TOOL-dGroundRules-47`.

### Edges

- **consumes-from** `TOOL-dGroundRules-40` — the `OVERLAP_PAIRS` arm in `tools/check-spec-tokens.test.sh`, its `PFX`-relative rows, its trap row and its one assertion naming every disagreement, whose rows S1 gives a listable form, and the criteria AC1 and AC2 S3 observes through `PAIRS_TABLE`
- **consumes-from** `TOOL-dGroundRules-44` — the row check, which S1's row function carries unchanged
- **consumes-from** `TOOL-dGroundRules-43` — AC1, which S3 observes a second time through `PAIRS_TABLE`, beside the whole `PAIRS_PY` and `PAIRS_SH` it runs
- **hands-off** `TOOL-dGroundRules-60` — `PAIRS_TABLE`, which that unit's S2 runs to show the Python column graded apart from the shell one (id 20 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 7a600abf5.

- In `tools/check-spec-tokens.test.sh` the arm under the comment `TOOL-dGroundRules-32 S9` is still
  the form `TOOL-dGroundRules-32` built: its pairs spelled twice through `${PFX}`, in `wi_py` and in
  the `wi_sh` loop, and one assertion. `TOOL-dGroundRules-40` rev-4, DEFERRED at order 13, gives it
  the table, the trap row and the FAIL line naming every disagreement; this unit builds on that.
- The suite sets `PFX` from `KIT_REL`, the directory it sits in, with its trailing slash,
  `tools/` here, and spells every fixture path through it.
- The same arm resolves the library with the suite's own `resolve_kit_dir` into `UNATTENDED_DIR` and
  sources it inside a subshell, so `overlaps` never enters the suite's shell.
- `overlaps` in `tools/unattended/lib-unattended.sh` is `covers` in either direction;
  `check_writes_intersect` in `tools/memory-tree/design_lib.py` holds `check_guard_trips` in either
  direction.
- `TOOL-dGroundRules-40` rev-4 §6 spells `PAIRS_PY` and `PAIRS_SH` with whole pairs, `PAIRS_SH`
  sourcing `tools/unattended/lib-unattended.sh`; `TOOL-dGroundRules-34` reads CLOSED at rev-9 in the
  build README's status table.
- `TOOL-dGroundRules-43` AC1 runs `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6.
- Run: `ROW_COUNT` and `PAIRS_TABLE` of §6, pointed at a scratch file holding a function line, the
  two call lines of §4 and the `ROW_ADDED` line, printed `3` and the block below; at 7a600abf5 the
  suite holds no call line, so both print nothing there.
- `python tools/lexicon/lexicon.py --suggest check_overlap_pair --as sh.function` answered OK.

```text
tools/policy/ tools/policy/x.py intersect True 0
tools/policy tools/policy-x.py disjoint False 1
tools/docs tools/docs-x.md disjoint False 1
```

### The arm after S1

```text
check_overlap_pair() {        # $1 a · $2 b · $3 intersect|disjoint · a and b relative to ${PFX}
    (TOOL-dGroundRules-44's row check, as that unit places it in the row loop)
    py = python: check_writes_intersect([${PFX}$1], [${PFX}$2])
    sh = ( . <the resolved lib-unattended.sh>; overlaps ${PFX}$1 ${PFX}$2 ); its exit
    add the row and "check_writes_intersect" to TOOL-dGroundRules-40's disagreements unless py == ($3 == intersect)
    add the row and "overlaps" to them unless (sh == 0) == ($3 == intersect)
    count the row
}
check_overlap_pair policy/ policy/x.py intersect
check_overlap_pair policy policy-x.py disjoint
TOOL-dGroundRules-40's one assertion: ok when at least one row was counted and nothing disagreed;
otherwise FAIL, naming every disagreement
```

The function runs in the suite's own shell, so the list and the row count it adds to survive the
call; only the library is sourced in a subshell. A call line opens at column 0 and carries no
trailing comment, so the definition line, which carries `()`, is not matched by
`^check_overlap_pair `, and the probe's read takes the line's three fields whole.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_overlap_pair` | sh.function | `tools/check-spec-tokens.test.sh` |

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **One `arm` call per row.** The floor would rise for no new red case, and `TOOL-dGroundRules-40`
  already rejects it: its one FAIL line names each disagreeing row and rule.
- **Whole paths in the call lines.** The suite spells every path through `${PFX}`, never a literal
  prefix, and `TOOL-dGroundRules-40` AC4 greps the row's `PFX`-relative spelling.
- **`PAIRS_SH` respelled in a criterion.** It closes this instance and leaves a second spelling of
  the pairs, which is the form that was stripped twice.
- **A tracked data file both the arm and the probe read.** It adds a file and a reader for two rows
  the suite already holds.

## 5. Production-readiness checklist

- security — N/A: a test suite's table and a read-only probe.
- perf / scale — two rows; the arm and the probe each start one interpreter and one shell per row.
- error / empty / loading states — a table with no call line makes `PAIRS_TABLE` print nothing,
  which AC1's count reds, and leaves the arm no counted row, which its one assertion fails.
- observability — each probe line carries the row and both verdicts.
- risks — none beyond the suite.
- testing — AC1 to AC3.
- migration — none: the rows are graded inside `TOOL-dGroundRules-40`'s one assertion, so the
  suite's assertion floor does not move.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root, under bash. A scratch copy is a git clone of this
repository under `%TEMP%/gr45`, checked out at the commit under test. The literal probes are spelled
whole here, once, and the criteria name them:

```text
ROW_COUNT   = grep -c '^check_overlap_pair ' tools/check-spec-tokens.test.sh
PAIRS_TABLE = grep '^check_overlap_pair ' tools/check-spec-tokens.test.sh | while read -r _ a b want _; do
                a=tools/$a; b=tools/$b
                py=$(python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d; print(d.check_writes_intersect(['$a'], ['$b']))")
                sh=$(bash -c ". tools/unattended/lib-unattended.sh; overlaps '$a' '$b'; echo \$?")
                echo "$a $b $want $py $sh"
              done
PAIRS_WANT  = tools/policy/ tools/policy/x.py intersect True 0
              tools/policy tools/policy-x.py disjoint False 1
ROW_ADDED   = in the scratch copy, the line "check_overlap_pair docs docs-x.md disjoint" appended
              after the table's last row
```

`PAIRS_TABLE` joins `tools/`, the suite's `PFX` in this repository, to each path as the arm joins `${PFX}`.

- **AC1** — When `ROW_COUNT` runs on the built tree, it prints `2`.
  Red when: a row is spelled in a form the arm grades and the probe does not list.
  figure: PINNED, the two rows `TOOL-dGroundRules-40` S1 declares.
- **AC2** — When `PAIRS_TABLE` runs on the built tree, it prints exactly the two lines of `PAIRS_WANT`.
  Red when: either rule disagrees with the table's expected answer on a row, or a row is spelled other than relative to `PFX`.
- **AC3** — When `ROW_ADDED` runs and `PAIRS_TABLE` runs in that copy, it prints three lines, the
  third being the added row with both paths joined to the prefix and ending `disjoint False 1`.
  Red when: the probe reads a list of its own rather than the rows the arm grades.

## 7. Gates

`spec-tokens self-test` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/check-spec-tokens.test.sh · covers AC2 · the trap row's expected answer staged to `intersect` in a scratch copy, where the one assertion reds naming that row once for each rule · none: the arm stays one assertion

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 20 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43, with the pairs spelled once as the arm's call lines and read by one probe,
  and units 34, 40 and 43's literals read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-58`, `TOOL-dGroundRules-59`, the reciprocal ends of the round-1 closing diff
  review's promotions; no scope or criterion moved.
- rev-3 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §7 §9 · disagreements, from a read-only probe of step 14 at 0860b8c1e: §1, §4 and S3 still took `TOOL-dGroundRules-40`'s `PAIRS_SH` as stripped and `TOOL-dGroundRules-34` as open, where `TOOL-dGroundRules-40` rev-4 names whole pairs and sources the library whole and `TOOL-dGroundRules-34` is CLOSED; `PAIRS_TABLE` sourced a bare library name; the call lines spelled whole paths and the old string-prefix row, where `TOOL-dGroundRules-40` rev-4 spells its rows relative to `PFX` with a new trap pair; §4 had a row call reach `arm`, one assertion per row against that unit's one; the evidence cited line numbers that had moved. Ruled: §1, §4 and S3 restate the premise; `PAIRS_TABLE` sources `tools/unattended/lib-unattended.sh` and prints whole paths; the rows follow the `PFX`-relative spelling and the trap pair, and the probe joins the prefix as the arm does; the row function adds to `TOOL-dGroundRules-40`'s disagreements and §5 migration stays none; every moved line cited by symbol, read at 7a600abf5.
- rev-4 · 2026-10-24 · §3 · the hands-off edges to `TOOL-dGroundRules-52`, whose rev-5 no longer consumes `PAIRS_TABLE`,
  and to `TOOL-dGroundRules-58` and `TOOL-dGroundRules-59`, retired WONTDO with their edges withdrawn, leave; a hands-off edge to
  `TOOL-dGroundRules-60` naming `PAIRS_TABLE` lands, the reciprocal of that unit's consumes-from line. No scope, design or
  criterion moved.

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
