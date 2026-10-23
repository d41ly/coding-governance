# TOOL-dGroundRules-40 — the overlap arm pins each pair's expected answer, so the render's rule and the dispatcher's are graded against the truth and not only against each other

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-40-deviation-28.md](../build/2026-10-23-build-TOOL-dGroundRules-40-deviation-28.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-40-deviation-64.md](../build/2026-10-23-build-TOOL-dGroundRules-40-deviation-64.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 17 at HIGH**, which shares item **H3** with ids 2
(`TOOL-dGroundRules-39`), 21 (`TOOL-dGroundRules-41`) and 25 (`TOOL-dGroundRules-42`). Id 17 is H3
on the overlap rule: `TOOL-dGroundRules-34` AC15 reads
`check_writes_intersect(["tools/policy/"], x.py"])`, which is not Python, and AC16 sources a bare
`lib-unattended.sh` and probes `overlaps tools/policy/ x.py`, which answers 1 where S16 needs 0. The
two criteria that were to certify S15 and S16 can never pass, and the arm S17 shapes compares the
two rules only with each other, so two rules wrong the same way pass it. This unit is id 17's
promotion: the arm holds the two pairs once, in one table with the answer each rule must give, and
both rules are graded against that column. Its own criteria spell the pairs whole. It repairs
`TOOL-dGroundRules-34`, which sits at order 12, so it builds at order 13.

## 2. Scope (IN)

- **S1** — The table. The arm `TOOL-dGroundRules-32` S9 adds to `tools/check-spec-tokens.test.sh`,
  narrowed by `TOOL-dGroundRules-34` S17 to two pairs, reads them from one table of three columns:
  the two paths and the expected answer, `intersect` for the directory-over-file pair and
  `disjoint` for the string-prefix pair. The pairs are spelled once in that file.
  Observed by AC4.
- **S2** — The verdicts. For each row, `check_writes_intersect` of `tools/memory-tree/design_lib.py`
  must answer `True` exactly when the column says `intersect`, and `overlaps` of
  `tools/unattended/lib-unattended.sh` must exit 0 exactly then; a row where either disagrees with
  the column is the arm's failure naming the row and the rule. Observed by AC1, AC2, AC3.
- **S3** — `TOOL-dGroundRules-34` AC15 and AC16 restated whole, as the direct probes of S2.
  Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect` or `overlaps`. Both answer correctly today for both pairs
  (§4 Evidence); this unit grades them.
- More pairs. The two cover the directory-over-file rule and the string-prefix trap `overlaps`
  documents (`tools/unattended/lib-unattended.sh:741-750`); a third would differ only in detail.
- The other corrupted criteria of item H3: `TOOL-dGroundRules-39`, `TOOL-dGroundRules-41` and
  `TOOL-dGroundRules-42`.

### Edges

- **consumes-from** `TOOL-dGroundRules-34` — the arm S17 narrows to two pairs and the parity S16 states, which S1 holds in one table and S2 grades against an expected column
- **hands-off** `TOOL-dGroundRules-44` — the `OVERLAP_PAIRS` disjoint row, which that unit respells as a real string-prefix trap and guards with a row check (id 29 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-45` — the arm's rows, which that unit makes call lines one probe lists, in place of `PAIRS_PY` and `PAIRS_SH` (id 20 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — AC2 and the §3 claim about `check_writes_intersect`, which that unit observes through `PAIRS_TABLE` (ids 30 and 17 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-59` — AC1, AC2 and the probe half of AC3, which that unit observes through `PAIRS_TABLE_WHOLE`, under `RAW_BOTH` for AC3 (id 13 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`.

- `tools/unattended/lib-unattended.sh:745-750` defines `covers` and `overlaps`, `overlaps` being
  `covers` in either direction over normalised paths.
- Sourcing `tools/unattended/lib-unattended.sh`, `overlaps` returned 0 for the directory-over-file
  pair and 1 for the string-prefix pair (`TOOL-dGroundRules-34` §4 Evidence, review id 3).
- `TOOL-dGroundRules-32` S9 places `check_writes_intersect` in `tools/memory-tree/design_lib.py` and
  its arm in `tools/check-spec-tokens.test.sh`; the arm "holds its verdict equal to `overlaps`".
- `TOOL-dGroundRules-34` AC15 (:497-501) and AC16 (:502-505) carry the stripped pairs (review ids
  3, 17, 21 and 25).

### The arm

```text
OVERLAP_PAIRS (one table, in tools/check-spec-tokens.test.sh):
    tools/policy/       tools/policy/x.py      intersect
    tools/policy/a.py   tools/policy/ab.py     disjoint

for each row (a, b, want):
    py = python: check_writes_intersect([a], [b])         # True or False
    sh = bash: . tools/unattended/lib-unattended.sh; overlaps a b; echo $?
    fail naming the row and "check_writes_intersect" unless py == (want == intersect)
    fail naming the row and "overlaps" unless (sh == 0) == (want == intersect)
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `OVERLAP_PAIRS` | a table in a test suite | `tools/check-spec-tokens.test.sh` |

The lexicon declares no cell for a shell table, so the name is graded by none.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **Parity between the two rules alone**, as S17 shapes it. Two rules staged to the same raw
  prefix compare agree with each other and pass.
- **The pairs restated in each criterion.** That is the form a respelling shortened; one table read
  by the arm and named by the criteria keeps one spelling.

## 5. Production-readiness checklist

- security — N/A: a test suite's table.
- perf / scale — two rows, one interpreter start and one shell source per row.
- error / empty / loading states — a table that parses to no row fails the arm, never passes it.
- observability — each failure names the row and the rule that disagreed.
- risks — none beyond the suite.
- testing — AC1 to AC4.
- migration — the suite's assertion floor, raised by the arm.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root. The literal probes are spelled whole here, once, and the
criteria name them:

```text
PAIRS_PY  = python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d;
            print(d.check_writes_intersect(['tools/policy/'], ['tools/policy/x.py']));
            print(d.check_writes_intersect(['tools/policy/a.py'], ['tools/policy/ab.py']))"
PAIRS_SH  = bash -c '. lib-unattended.sh; overlaps tools/policy/ x.py;
            echo $?; overlaps a.py ab.py; echo $?'
RAW_BOTH  = in a scratch copy, check_writes_intersect and covers both staged to a raw string
            startswith in either direction
ARM_ROWS  = grep -c "tools/policy/ab.py" tools/check-spec-tokens.test.sh
```

- **AC1** — When `PAIRS_PY` runs on the built tree, it prints `True` then `False`.
  Red when: the render's overlap rule misreads a directory over a file or a shared string prefix.
- **AC2** — When `PAIRS_SH` runs on the built tree, it prints `0` then `1`.
  Red when: the dispatcher's overlap rule misreads either pair.
- **AC3** — When `RAW_BOTH` runs, `PAIRS_PY` there prints `True` then `True` and `PAIRS_SH` prints
  `0` then `0`, the answers the arm's expected column rejects.
  Red when: the probes cannot tell a raw prefix compare from containment, so the arm's column could
  not either.
- **AC4** — When `ARM_ROWS` runs on the built tree, it prints `1`.
  Red when: the pairs are spelled more than once in the suite, or not at all.

## 7. Gates

`spec-tokens self-test` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC3 · `check_writes_intersect` and `covers` both staged to a raw string prefix compare in a scratch copy, where parity alone stays green · that suite's assertion count, raised by the arm

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 17 (HIGH, item H3) of the round-1 spec
  audit of units 33 and 34, from the skeptic's corrected AC15 and AC16 spellings held in one table
  with an expected column, with `overlaps` and the arm's home read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-44`, `TOOL-dGroundRules-45`, `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.
- rev-3 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-59`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.

## 10. Reuse audit

The seams extended are the arm `TOOL-dGroundRules-32` S9 places in `tools/check-spec-tokens.test.sh`
and its two subjects, `check_writes_intersect` in `tools/memory-tree/design_lib.py` and `overlaps`
in `tools/unattended/lib-unattended.sh:750`; nothing new is built beside them.
`python tools/codebase-map/reuse_lookup.py "decide whether two write sets overlap by path containment"`
ranked `overlaps` and `scan_shared_index_overlaps` of `tools/unattended/lib-unattended.sh` as seams;
the first is this unit's subject and the second a caller of it, so no new rule is written. The recall probe returned this audit's H3 and `TOOL-aKeyedAnnotation-9`, the
open ask on the spec-tokens paths join that drove the respelling; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion's path respelled to pass
the spec-tokens paths join" --terms "acceptance criterion path stripped prefix paths join basename
respelled spec-tokens literal fixture"`
