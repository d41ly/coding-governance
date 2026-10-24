# TOOL-dGroundRules-60 — unit 52's overlap observations taken through the whole probe, with the Python column shown graded on its own

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-60-deviation-48.md](../build/2026-10-23-build-TOOL-dGroundRules-60-deviation-48.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-58-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-task.md) | research | TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-60-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-60-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 |
| [2026-10-24-prompt-TOOL-dGroundRules-60-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-60-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-60-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-60-probe-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build's spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
returned CLEAN WITH FIXES with item **H2** at HIGH, raw ids 4, 13 and 20. This unit is **id 20**, the
intent lens. `TOOL-dGroundRules-52` S21 says `check_writes_intersect` is first graded by the Python
column of `PAIRS_TABLE` (`TOOL-dGroundRules-45` §6), which that unit's AC5 runs; nothing shows that
column graded apart from the shell one, so a wrong `check_writes_intersect` could pass behind a right
`overlaps`. This unit stages the Python rule alone wrong and reads the probe's disjoint line, so the
Python column is seen failing on its own. It changes no code. It consumes `TOOL-dGroundRules-45` at
order 14 and observes `TOOL-dGroundRules-52` S21 and AC5 at order 16, so it builds at order 18.

## 2. Scope (IN)

- **S2** — The Python column alone. With `check_writes_intersect` alone staged to a raw string
  `startswith` in either direction, `PY_RAW` (§6), `PAIRS_TABLE` of `TOOL-dGroundRules-45` §6 prints
  the disjoint row of `TOOL-dGroundRules-40` S1, `policy` against `policy-x.py` joined to `PFX`, with
  its Python field `True` while its shell field stays `1`, so the first grading `TOOL-dGroundRules-52`
  S21 claims is observed failing on its own. Observed by AC2.

S2 and AC2 keep their rev-1 ids; §9 rev-2 records why there is no S1 and no AC1.

## 3. Non-goals (OUT)

- Any change to `check_writes_intersect`, `overlaps` or the rows of `OVERLAP_PAIRS`.
- The probe and its row form: `TOOL-dGroundRules-45`. The trap row's spelling:
  `TOOL-dGroundRules-40` S1.
- The probe run on the built tree: `TOOL-dGroundRules-52` AC5 and `TOOL-dGroundRules-45` AC2 already
  observe it, and with them `TOOL-dGroundRules-52` S5 and S12; this unit adds no second spelling.
- Rewriting `TOOL-dGroundRules-52` §6. Its §3 names this unit (BUILD-METHOD M4).

### Edges

- **consumes-from** `TOOL-dGroundRules-45` — `PAIRS_TABLE` and the `check_overlap_pair` call lines it reads, the probe S2 runs; without them the suite holds no call line and the probe prints nothing
- **consumes-from** `TOOL-dGroundRules-40` — the disjoint row of `OVERLAP_PAIRS`, `policy` against `policy-x.py` relative to `PFX`, the string-prefix trap S2 needs; without it a raw `startswith` answers the row as the built rule does
- **consumes-from** `TOOL-dGroundRules-52` — S21 and AC5, whose Python column S2 shows graded apart from the shell one

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 8eab342e0.

- `OVERLAP_PAIRS` in `tools/check-spec-tokens.test.sh`, built by `TOOL-dGroundRules-40` (CLOSED),
  holds the rows `policy/ policy/x.py intersect` and `policy policy-x.py disjoint`, each relative to
  `PFX`, which the suite sets from `KIT_REL` with its trailing slash, `tools/` here. The suite holds no
  `check_overlap_pair` call line yet; `TOOL-dGroundRules-45` S1 gives each row that form.
- `PAIRS_TABLE` (`TOOL-dGroundRules-45` §6) joins `tools/` to each path, runs
  `check_writes_intersect` from `tools/memory-tree` and `overlaps` from
  `tools/unattended/lib-unattended.sh`, both by repository-relative path, and prints the two paths,
  the expected answer, the Python answer and the shell exit; its `PAIRS_WANT` holds the disjoint
  line ending `disjoint False 1`.
- `TOOL-dGroundRules-52` S21 names `PAIRS_TABLE`'s Python column as the first grading of
  `check_writes_intersect`; its AC5 runs the probe on the built tree and reads both columns together.
- `check_writes_intersect` in `tools/memory-tree/design_lib.py` holds `check_guard_trips` in either
  direction, which takes the exact path or a path under it, never a bare string prefix. `overlaps`
  in `tools/unattended/lib-unattended.sh` is `covers` in either direction, a containment test at a
  path component boundary that calls no Python, so staging the Python rule alone leaves the shell
  field as built.
- Run, from the repository root: the two lines of the block below printed `1` and `True`, so a raw
  `startswith` calls the disjoint row intersecting while `covers` calls it disjoint.

```text
bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy tools/policy-x.py; echo $?'
python -c "print('tools/policy-x.py'.startswith('tools/policy'))"
```

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

### Alternatives rejected

- **`RAW_BOTH` of `TOOL-dGroundRules-40` §6 reused for S2.** It stages both rules, so both fields
  move together and the Python column is never seen graded alone, which is S21's claim.
- **A criterion running `PAIRS_TABLE` on the built tree.** `TOOL-dGroundRules-52` AC5 and
  `TOOL-dGroundRules-45` AC2 are that observation; a third run adds no red case.
- **`PAIRS_TABLE_WHOLE`.** Its spelling unit is closed WONTDO, and `TOOL-dGroundRules-45` rev-3's
  `PAIRS_TABLE` already sources the library by its tracked path and prints whole paths.

## 5. Production-readiness checklist

- security — N/A: a read-only probe and a scratch copy.
- perf / scale — two rows, run once in the scratch copy.
- error / empty / loading states — a suite with no call line makes the probe print nothing, so no
  disjoint line, which AC2 reds.
- observability — each line carries the row, its expected answer and both verdicts.
- risks — S2 needs the string-prefix trap of `TOOL-dGroundRules-40` S1, `policy` against
  `policy-x.py` relative to `PFX`; with a disjoint row a raw `startswith` also answers disjoint, the
  Python field stays `False` and AC2 is red.
- testing — AC2.
- migration — none.
- user docs — N/A: a gov-only probe.

## 6. Acceptance criteria

Every command runs from a repository root, under bash: `PAIRS_TABLE` reads repository-relative
paths, so in the scratch copy it runs with the copy's root as its working directory. A scratch copy
is a git clone of this repository under `%TEMP%/gr60`, checked out at the commit under test.
`PAIRS_TABLE` is spelled in `TOOL-dGroundRules-45` §6; the staging and the expected line here:

```text
PY_RAW      = in the scratch copy, check_writes_intersect of tools/memory-tree/design_lib.py staged
              to answer True when either path starts with the other as a string; covers left as built
PY_RAW_WANT = tools/policy tools/policy-x.py disjoint True 1
```

- **AC2** — When `PY_RAW` runs and `PAIRS_TABLE` runs from the scratch copy's root, its `disjoint` line is `PY_RAW_WANT`.
  Red when: the probe's Python field reads anything but `check_writes_intersect`, so a wrong one passes behind a right `overlaps`, or the disjoint row is respelled to a pair a raw `startswith` calls disjoint.
  fixture: green from `TOOL-dGroundRules-45`'s close, before this unit, which builds nothing; `PY_RAW` is the staged break that shows the column failable, and the respelled row is the later change that reds it.

## 7. Gates

`memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting raw finding id 20 (HIGH, item H2) of the closing diff
  review of the spec run, as unit 52's observations taken through the whole probe, with the Python
  rule staged alone so its first grading is seen failing.
- rev-2 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §9 §10 · disagreements, from the read-only probe of steps 15 to 20 at e1c7051cb, restated at 8eab342e0 with units 1 to 41 built: S1 and AC1 ran `PAIRS_TABLE_WHOLE` on the built tree, the same observation as `TOOL-dGroundRules-52` AC5 and `TOOL-dGroundRules-45` rev-3 AC2; AC2 and the edges consumed `TOOL-dGroundRules-58`, now closed WONTDO with `TOOL-dGroundRules-51`, -53, -54, -57 and -59; §4 and §5 named the old disjoint row of `TOOL-dGroundRules-44` S1, a nested pair, where `TOOL-dGroundRules-40` S1 owns the trap `policy` against `policy-x.py` relative to `PFX`; the evidence cited moved lines by number. Ruled: S1 and AC1 leave the spec and S2 and AC2 keep their ids; AC2 runs `PAIRS_TABLE` of `TOOL-dGroundRules-45` and reads its disjoint line as `PY_RAW_WANT`; §4 and §5 restate the row as `TOOL-dGroundRules-40` S1 owns it; `TOOL-dGroundRules-52` is cited by S21 and AC5; every citation by symbol or AC id; AC2 is restated as green before this unit, with its staged break and the later change that reds it; no criterion consumes a literal of a WONTDO unit.

## 10. Reuse audit

No existing seam fits beyond the ones observed: the probe is `TOOL-dGroundRules-45`'s `PAIRS_TABLE`,
the row is `TOOL-dGroundRules-40`'s, and the staging narrows `RAW_BOTH` of `TOOL-dGroundRules-40` to
one rule; nothing is built. `python tools/codebase-map/reuse_lookup.py "stage one overlap rule to a
raw string prefix and read the probe's python column apart from the shell column"` ranked `overlaps`
of `tools/unattended/lib-unattended.sh` and name-stem hits (`read`, `probe`, `raw`) that hold no
pair. The recall probe returned `TOOL-dGroundRules-40`, `TOOL-dGroundRules-44` and this spec's
rev-1; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is the render's overlap rule graded
apart from the dispatcher's" --terms "check_writes_intersect overlaps PAIRS_TABLE python column
staged raw startswith disjoint trap row"`
