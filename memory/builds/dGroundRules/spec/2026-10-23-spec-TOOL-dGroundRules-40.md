# TOOL-dGroundRules-40 — the overlap arm pins each pair's expected answer, so the render's rule and the dispatcher's are graded against the truth and not only against each other

**Status:** CLOSED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-40-deviation-28.md](../build/2026-10-23-build-TOOL-dGroundRules-40-deviation-28.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-40-deviation-64.md](../build/2026-10-23-build-TOOL-dGroundRules-40-deviation-64.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-40-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-40-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-23-prompt-TOOL-dGroundRules-40-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-40-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-39-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-39-staleness-probe-brief.md) | research | TOOL-dGroundRules-39 TOOL-dGroundRules-41 |
| [2026-10-24-prompt-TOOL-dGroundRules-40-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-40-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-40-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-40-probe-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 17 at HIGH**, which shares item **H3** with ids 2
(`TOOL-dGroundRules-39`), 21 (`TOOL-dGroundRules-41`) and 25 (`TOOL-dGroundRules-42`). Id 17 is H3
on the overlap rule: `TOOL-dGroundRules-34` AC15 and AC16 carry their pairs stripped of their
directories, and AC16 sources a bare file name, so neither can pass as spelled.

The arm those criteria were to certify already exists. `TOOL-dGroundRules-32` built it at 5412bbecd
in `tools/check-spec-tokens.test.sh`: it runs two pairs through `check_writes_intersect` and through
`overlaps` and grades each rule against fixed answers, as one assertion (§4 Evidence). Three faults
remain in it. Its disjoint pair is no string-prefix trap: a raw `startswith` in either direction
calls it disjoint too, so two rules staged to a raw compare pass it, which is why
`TOOL-dGroundRules-34` AC17 cannot red and is handed here. Its pairs are spelled twice, once per
rule, with no expected column, and its failure names neither the row nor the rule. And its comment
claims a staging that cannot red it.

This unit is id 17's promotion. It adds the table, the two pairs spelled once beside the answer each
rule must give, the disjoint row being a pair a raw compare calls overlapping; a failure naming the
row and the rule that disagreed; and a corrected comment. Its own criteria spell the pairs whole.
It repairs `TOOL-dGroundRules-34`, which sits at order 12, so it builds at order 13.

## 2. Scope (IN)

- **S1** — The table. The arm `TOOL-dGroundRules-32` built in `tools/check-spec-tokens.test.sh`
  reads its two pairs from one table of three columns: the two paths, each spelled relative to the
  suite's install prefix `PFX` and joined to it at use, and the expected answer. The answer is
  `intersect` for the directory-over-file pair and `disjoint` for the string-prefix pair: a
  directory without its trailing slash against a sibling file whose name extends the directory's,
  which a raw `startswith` calls overlapping and containment calls disjoint (§4 The arm). The pairs
  are spelled once in that file. Observed by AC4.
- **S2** — The verdicts. For each row, `check_writes_intersect` of `tools/memory-tree/design_lib.py`
  must answer `True` exactly when the column says `intersect`, and `overlaps` of
  `tools/unattended/lib-unattended.sh` must exit 0 exactly then. A row where either disagrees with
  the column fails the arm, and the failure line names each disagreeing row with the rule that
  disagreed. Observed by AC1, AC2, AC3.
- **S3** — `TOOL-dGroundRules-34` AC15 and AC16 restated whole, as the direct probes of S2.
  Observed by AC1, AC2.
- **S4** — The arm's comment. The comment over the arm (`tools/check-spec-tokens.test.sh:1705-1708`,
  read at 74d17b3a0) says a raw prefix compare calls its disjoint pair overlapping, and that testing
  one direction only reds the arm; neither holds (§4 Evidence). It is rewritten to say the table's
  disjoint row is the pair a raw `startswith` calls overlapping, and that staging both rules to a
  raw compare in either direction is what reds the arm. It names the row by its column and spells
  no path of the table. Observed by AC4, AC5.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect` or `overlaps`. Both answer correctly today for both pairs
  (§4 Evidence); this unit grades them.
- More pairs. The two cover the directory-over-file rule and the string-prefix trap
  `check_guard_trips` names in its docstring ("never a bare prefix",
  `tools/memory-tree/design_lib.py:591`), whose containment `covers` and `overlaps` share
  (`tools/unattended/lib-unattended.sh:745-750`); a third would differ only in detail.
- The other corrupted criteria of item H3: `TOOL-dGroundRules-39`, `TOOL-dGroundRules-41` and
  `TOOL-dGroundRules-42`.

### Edges

- **consumes-from** `TOOL-dGroundRules-34` — the arm S17 narrows to two pairs and the parity S16 states, which S1 holds in one table and S2 grades against an expected column; its AC17, observed by this unit's AC3 on the disjoint row a raw `startswith` calls overlapping, a new pair that replaces the `a.py`/`ab.py` pair, which a raw `startswith` cannot confuse; and the arm comment its §5 hands off, which S4 corrects
- **hands-off** `TOOL-dGroundRules-44` — the `OVERLAP_PAIRS` disjoint row, which that unit respells as a real string-prefix trap and guards with a row check (id 29 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-45` — the arm's rows, which that unit makes call lines one probe lists, in place of `PAIRS_PY` and `PAIRS_SH` (id 20 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — AC2 and the §3 claim about `check_writes_intersect`, which that unit observes through `PAIRS_TABLE` (ids 30 and 17 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-59` — AC1, AC2 and the probe half of AC3, which that unit observes through `PAIRS_TABLE_WHOLE`, under `RAW_BOTH` for AC3 (id 13 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 74d17b3a0.

- `tools/check-spec-tokens.test.sh:1705-1720` is the arm `TOOL-dGroundRules-32` built at
  5412bbecd. It spells its pairs twice, in the `wi_py` probe (:1710-1711) and in the `overlaps`
  loop (:1713), each through `${PFX}`; it compares the first rule's answers to `True False` and
  the second's to the same pair of words (:1716); and it counts one assertion whose FAIL line
  prints both answer strings and names no row and no rule (:1719).
- `tools/check-spec-tokens.test.sh:28-31` sets `PFX`, the install prefix with its trailing slash,
  empty at a root install; every fixture path is spelled through it. In this repository it is
  `tools/`.
- `tools/unattended/lib-unattended.sh:745-750` defines `covers` and `overlaps`, `overlaps` being
  `covers` in either direction over normalised paths.
- `check_guard_trips` (`tools/memory-tree/design_lib.py:589-598`) trips on the exact path or on
  anything under it as a directory, never on a bare prefix, and a declared directory trips a guard
  under it; `check_writes_intersect` (:601-605) holds it in either direction.
- Run: `check_writes_intersect` printed `True` for the directory-over-file pair and `False` for the
  string-prefix pair of the block below; sourcing `tools/unattended/lib-unattended.sh`, `overlaps`
  exited 0 and 1 on them; a raw `startswith` in either direction answered `True` on the
  string-prefix pair, and `False` on the pair the arm runs today, so staging both rules to a raw
  compare leaves today's arm green.
- The comment's second claim fails by reading: `check_guard_trips` trips a file under a directory
  one way and a declared directory over its file the other (:595-598), so either direction alone
  still answers `True` on the directory-over-file pair, and `covers` alone exits 0 on it.
- `TOOL-dGroundRules-34` AC15 and AC16 carry the stripped pairs (review ids 3, 17, 21 and 25); its
  AC17 runs no command and is observed by this unit's AC3 (its rev-9).

### The arm

The table holds each path relative to `${PFX}`, the spelling the suite uses for every path it
names; the arm joins `${PFX}` at use.

```text
OVERLAP_PAIRS (one table, in tools/check-spec-tokens.test.sh, one row per line):
    policy/    policy/x.py    intersect
    policy     policy-x.py    disjoint

read at this repository's prefix, PFX=tools/:
    tools/policy/    tools/policy/x.py    intersect
    tools/policy     tools/policy-x.py    disjoint

for each row (a, b, want), a and b joined to ${PFX}:
    py = python: check_writes_intersect([a], [b])         # True or False
    sh = bash: . <the resolved lib-unattended.sh>; overlaps a b; echo $?
    a disagreement naming the row and "check_writes_intersect" unless py == (want == intersect)
    a disagreement naming the row and "overlaps" unless (sh == 0) == (want == intersect)
one assertion: ok when the table parsed to at least one row and nothing disagreed;
otherwise FAIL, naming every disagreement
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `OVERLAP_PAIRS` | a table in a test suite | `tools/check-spec-tokens.test.sh` |

The lexicon declares no cell for a shell table, so the name is graded by none.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **Today's disjoint pair kept**, two files sharing a directory and a name stem. A raw `startswith`
  calls it disjoint as containment does, so both rules staged to a raw compare pass the arm; that
  is the disagreement that sent `TOOL-dGroundRules-34` AC17 here.
- **One assertion per row.** The floor would rise for no new red case; the one FAIL line already
  names each disagreeing row and rule.
- **The pairs restated in each criterion.** That is the form a respelling shortened; one table read
  by the arm and named by the criteria keeps one spelling.

## 5. Production-readiness checklist

- security — N/A: a test suite's table.
- perf / scale — two rows, one interpreter start and one shell source per row.
- error / empty / loading states — a table that parses to no row fails the arm, never passes it.
- observability — each failure names the row and the rule that disagreed.
- risks — none beyond the suite.
- testing — AC1 to AC5, and §7's arm line.
- migration — none: the arm stays one assertion, so the suite's assertion floor does not move.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root. The literal probes are spelled whole here, once, and the
criteria name them:

```text
PAIRS_PY  = python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import design_lib as d;
            print(d.check_writes_intersect(['tools/policy/'], ['tools/policy/x.py']));
            print(d.check_writes_intersect(['tools/policy'], ['tools/policy-x.py']))"
PAIRS_SH  = bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy/ tools/policy/x.py;
            echo $?; overlaps tools/policy tools/policy-x.py; echo $?'
RAW_BOTH  = in a scratch copy, check_writes_intersect and covers both staged to a raw string
            startswith in either direction
ARM_ROWS  = grep -cF "policy-x.py" tools/check-spec-tokens.test.sh
ARM_NOTE  = grep -c "testing one direction only" tools/check-spec-tokens.test.sh
```

`ARM_ROWS` greps the disjoint row's second path as the table holds it, relative to `${PFX}` (§4 The
arm), since the suite spells no path through a literal prefix; it counts lines, one per spelling.

- **AC1** — When `PAIRS_PY` runs on the built tree, it prints `True` then `False`, the answers the arm `TOOL-dGroundRules-32` built already demands of the render's rule, now on the table's disjoint row.
  Red when: the render's overlap rule misreads a directory over a file or a shared string prefix.
- **AC2** — When `PAIRS_SH` runs on the built tree, it prints `0` then `1`.
  Red when: the dispatcher's overlap rule misreads either pair.
- **AC3** — When `RAW_BOTH` runs, `PAIRS_PY` there prints `True` then `True` and `PAIRS_SH` prints
  `0` then `0`, the answers the arm's expected column rejects; this is the observation
  `TOOL-dGroundRules-34` AC17 hands here.
  Red when: the probes cannot tell a raw prefix compare from containment, so the arm's column could
  not either.
- **AC4** — When `ARM_ROWS` runs on the built tree, it prints `1`.
  Red when: the disjoint row is spelled more than once in the suite, the arm's comment included, or
  not at all.
- **AC5** — When `ARM_NOTE` runs on the built tree, it prints `0`.
  Red when: the arm's comment still names a staging that cannot red it.

## 7. Gates

`spec-tokens self-test` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC3 · `check_writes_intersect` and `covers` both staged to a raw string startswith in either direction in a scratch copy, red naming the disjoint row once for each rule, where today's pair stays green · none: the arm stays one assertion

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
- rev-4 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §7 §9 · disagreements, from a read-only probe at 74d17b3a0: AC3 could not red, a raw `startswith` calling the old disjoint pair disjoint; `PAIRS_SH` sourced a bare file name and named bare files; the arm already stood, built by `TOOL-dGroundRules-32` against fixed answers; §3 cited `tools/unattended/lib-unattended.sh` for a string-prefix note it does not hold; the citations into `TOOL-dGroundRules-34` had drifted; no edge carried its AC17 or the arm comment; `ARM_ROWS` grepped a literal prefix the suite never spells. Ruled: the disjoint row becomes the directory against its name-extending sibling file; `PAIRS_SH` names whole paths; §1, AC1 and §4 restate the built arm, this unit adding the table and per-row, per-rule failure naming; S4 and AC5 correct the comment, and the consumes-from edge names AC17 and the comment; §3 cites `check_guard_trips`; `ARM_ROWS` greps the `${PFX}`-relative spelling; criteria of `TOOL-dGroundRules-34` cited by AC id.

## 10. Reuse audit

The seams extended are the arm `TOOL-dGroundRules-32` built in `tools/check-spec-tokens.test.sh`
and its two subjects, `check_writes_intersect` in `tools/memory-tree/design_lib.py` and `overlaps`
in `tools/unattended/lib-unattended.sh:750`; nothing new is built beside them.
`python tools/codebase-map/reuse_lookup.py "decide whether two write sets overlap by path containment"`
ranked `overlaps` and `scan_shared_index_overlaps` of `tools/unattended/lib-unattended.sh` as seams;
the first is this unit's subject and the second a caller of it, so no new rule is written. The recall probe returned this audit's H3 and `TOOL-aKeyedAnnotation-9`, the
open ask on the spec-tokens paths join that drove the respelling; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion's path respelled to pass
the spec-tokens paths join" --terms "acceptance criterion path stripped prefix paths join basename
respelled spec-tokens literal fixture"`
