# TOOL-dGroundRules-57 — the not-a-trap staging spelled whole, so the trap probe lists the row the row check refuses

**Status:** WONTDO · rev-1 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-57-deviation-45.md](../build/2026-10-23-build-TOOL-dGroundRules-57-deviation-45.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 |
| [2026-10-23-prompt-TOOL-dGroundRules-57-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-57-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 19 at HIGH** under item **H1**, which it shares with ids 5, 9, 12 and 14.
Id 19 is H1 seen from intent. `TOOL-dGroundRules-44` stages `NOT_A_TRAP` as the disjoint row
respelled `a.py tools/policy/ab.py`, so the staged line carries one `tools/policy/` where
`TRAP_PROBE` keeps only lines carrying two. The probe therefore prints nothing in that copy, and
AC3's expected line ending `False False` can never print. The same fence spells the trap pair whole
elsewhere, so the basename was never forced. Id 19's `TRAP_SH` half is `TOOL-dGroundRules-53`'s.
This unit is id 19's promotion for its `NOT_A_TRAP` half: the staging becomes one literal edit that
spells both paths of the non-trap pair whole, and the probe half of `TOOL-dGroundRules-44` AC3 is
observed with it. It repairs `TOOL-dGroundRules-44`, which sits at order 14, so it builds at order
17.

## 2. Scope (IN)

- **S1** — The staging. `NOT_A_TRAP_WHOLE` (§4) is one `sed` edit in a scratch copy's suite. It
  rewrites the trap row's first path to `tools/policy/a.py` and keeps the whitespace between the
  two paths, so the row is the non-trap pair with both paths whole, in the table form
  `TOOL-dGroundRules-44` §4 sketches and in the call-line form `TOOL-dGroundRules-45` S1 gives it.
  It stands in `NOT_A_TRAP`'s place wherever `TOOL-dGroundRules-44` §6 names it. Observed by AC1.
- **S2** — The probe half of `TOOL-dGroundRules-44` AC3 restated. In that copy, `TRAP_PROBE` of
  `TOOL-dGroundRules-44` §6 prints exactly one line, naming the non-trap pair and ending
  `False False`. Observed by AC2.

## 3. Non-goals (OUT)

- Any edit to the text of `TOOL-dGroundRules-44` §6. That spec gains only the hands-off line to this
  unit; its `NOT_A_TRAP` is read through S1, never respelled in place.
- The row check's refusal, which the other half of `TOOL-dGroundRules-44` AC3 names:
  `TOOL-dGroundRules-56`, which runs it in the copy this unit stages.
- `TRAP_SH`: `TOOL-dGroundRules-53`. The class record: `TOOL-dGroundRules-55`.
- Any change to `TRAP_PROBE`, the suite or either overlap rule.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — the trap row and `TRAP_PROBE`, which S1 stages against and S2 runs; without them there is no row to respell and no probe to list it
- **hands-off** `TOOL-dGroundRules-56` — the copy `NOT_A_TRAP_WHOLE` stages, in which that unit runs the row check and observes its refusal by name

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-44` §6 spells `NOT_A_TRAP` as "the disjoint row respelled a.py
  tools/policy/ab.py", and `TRAP_PROBE` keeps the lines carrying `disjoint` and exactly two
  `tools/policy/`. The spec has one committed revision (`d794a81bc`), so the original staging is
  taken from the review's sound fix: `tools/policy/a.py` against `tools/policy/ab.py`.
- The suite's overlap arm is not yet built: `OVERLAP_PAIRS` and `check_overlap_pair` appear nowhere
  in `tools/check-spec-tokens.test.sh` today. Units 40, 44 and 45 build it, at orders 13 and 14.
- A mock suite holding the two call lines of `TOOL-dGroundRules-45` §4 was built in the session
  scratchpad. `TRAP_PROBE` printed `tools/policy/a tools/policy/ab.py True False` there. After
  `NOT_A_TRAP_WHOLE`, `STAGED_ROW` printed `1` and `TRAP_PROBE` printed
  `tools/policy/a.py tools/policy/ab.py False False`.
- The staging's `\( \+\)` group keeps any run of spaces, so it matches the table form, where
  `TOOL-dGroundRules-44` §4 aligns the paths in columns, and the call-line form, where one space
  separates them.

### The literals

They are spelled here, in §4, so the paths join over §6 never grades their operands and no sweep can
respell them to a basename. Run each verbatim from the root of the scratch copy.

```text
NOT_A_TRAP_WHOLE = sed -i 's#tools/policy/a\( \+\)tools/policy/ab\.py#tools/policy/a.py\1tools/policy/ab.py#' tools/check-spec-tokens.test.sh
STAGED_ROW       = grep -c 'tools/policy/a\.py \+tools/policy/ab\.py' tools/check-spec-tokens.test.sh
```

### Inventory

No identifier is minted. `NOT_A_TRAP_WHOLE` and `STAGED_ROW` are literal labels inside this spec.

### Files touched (estimate)

None. The unit stages a scratch copy and restates a criterion; it writes no product file.

### Alternatives rejected

- **`NOT_A_TRAP` restated as prose with the paths whole.** Prose is what a builder respells; a
  `sed` edit run verbatim either stages the row or matches nothing, which AC1 sees.
- **`TRAP_PROBE` loosened to keep a line with one `tools/policy/`.** It would print the respelled
  row and hide the respelling, which is the defect this unit closes.

## 5. Production-readiness checklist

- security — N/A: an edit to a scratch copy and a read-only probe.
- perf / scale — one `sed` pass and one interpreter start.
- error / empty / loading states — a staging that matches nothing leaves `STAGED_ROW` at `0`, which
  AC1 reds before AC2 can pass on the unstaged row.
- observability — `TRAP_PROBE` prints the row it reads and both answers.
- risks — none: no product file changes.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

Every command runs from the root of a scratch copy: a git clone of this repository under
`%TEMP%/gr57`, checked out at the commit under test, where `NOT_A_TRAP_WHOLE` has run. The two
literals are spelled in §4; `TRAP_PROBE` is spelled in §6 of `TOOL-dGroundRules-44`.

- **AC1** — When `STAGED_ROW` runs, it prints `1`.
  Red when: the staging matches no line, so the copy still holds the trap row and AC2 reads the
  built tree.
- **AC2** — When `TRAP_PROBE` runs, it prints exactly one line, ending `False False`, whose first two
  fields are the two staged paths.
  Red when: the staged row carries a path the probe filters out, so the probe prints nothing and the
  non-trap row is never listed.

## 7. Gates

`memory hygiene` · `spec-tokens self-test`

The suite arm that stages a non-trap row is `TOOL-dGroundRules-44`'s `New arm:` line; this unit
adds no arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 19 (HIGH, item H1) of the closing diff
  review round 1 for its `NOT_A_TRAP` half, from the review's sound fix, with both literals and
  `TRAP_PROBE` run against a mock of the arm on 2026-10-23.

## 10. Reuse audit

The seam reused is `TRAP_PROBE` of `TOOL-dGroundRules-44` §6, which already reads the suite's rows;
the unit adds a staging and builds nothing beside the probe. `python
tools/codebase-map/reuse_lookup.py "run one suite function alone on a staged row to observe its
refusal line"` ranked `rows`, `row` and `run`, name-stem hits that stage no suite row, so no
existing seam fits the staging itself. The recall probe returned `TOOL-dGroundRules-45`, whose rows
this staging matches in either form, and `TOOL-dGroundRules-42` and `TOOL-dGroundRules-47`, whose
whole-literal rule this unit follows; all agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
