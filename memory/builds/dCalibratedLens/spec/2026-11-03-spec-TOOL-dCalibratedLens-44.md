# TOOL-dCalibratedLens-44 — every line the shape arm renders is held free of a literal bracket, apart from a markdown link, so a `SPEC` line that leaks its group reds

**Status:** OPEN · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 14 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-44-deviation-441.md](../build/2026-11-03-build-TOOL-dCalibratedLens-44-deviation-441.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 12, HIGH, of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). The report merges ids 12 and 27
into its item H3; id 27 is `TOOL-dCalibratedLens-45`. Unit 31's shape arm checks a rendered line only
by asking `buildShapeRegex` to admit it, and the guard's lazy field rule `(?:(?! · ).)+?` absorbs `x[`
and `x]`: a node probe of the live guard printed `true` for `- SPEC — [x](x) · review x[ · open x]`.
So a renderer that leaks the `SPEC` group's brackets, the shape every build message carries, passes
the arm, and unit 31 AC3's claim that the reverted renderer's `SPEC` line is refused is false. This
unit adds the assertion the guard cannot make: no rendered line carries a bracket outside a markdown
link. It repairs `TOOL-dCalibratedLens-31`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 31's text (rev-2, id 12): S2
  names this unit's assertion beside the guard check, and AC3's staged red reads `returned` and
  `merged` refused by the guard and `SPEC` caught by this unit's assertion. Observed by AC1.
- **S2** — The bracket assertion, in unit 31's shape arm of `tools/hooks/format-guard.test.sh`. For
  each line the arm renders, it takes out every markdown link, a `[` run free of brackets, then `](`,
  a run free of parentheses and `)`, and asserts that what remains holds no `[` and no `]`. One
  assertion per rendered line, separate from the guard's; the suite's `FLOOR_ASSERTIONS` rises by
  the count, and the arm's SKIP lowers the floor by the same count. A failing line prints
  `FAIL shape <head> <form> — a literal bracket in <line>`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Changing `buildShapeRegex`. Tightening the guard's field rule to refuse `[` would change what the
  hook admits in every live message, the hooks kit's contract and not this build's.
- How a render error is reported, and the second form of a shape: `TOOL-dCalibratedLens-45`, id 27.
- A spec-audit checklist entry that every staged break is probed against the live guard, the
  finding's left-shift line. It is the bug class `staged-break-substitutes-a-synthetic-value`, which
  the catalogue already hands every spec review.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-31` — the shape arm in `tools/hooks/format-guard.test.sh` and the lines it renders, which this assertion reads; without the arm there is no rendered line to hold

## 4. Design

### Evidence

- The review's node probe with the live `buildShapeRegex` (`tools/hooks/format-guard.js:164-179`):
  `true` for `- SPEC — [x](x) · review x[ · open x]`, `false` for the full-form `merged` and
  `returned` lines of the base renderer (finding ids 12 and 27).
- `AGENTS.md:63-64`: the `SPEC` shape carries the link `[<unit-id>](<path>)` and the group
  `[ · open <ids|none>]`; the `agent` shape carries the link `prompt [<name>](<path>)`.
- The `[grammar]` rule (`AGENTS.md:76`): the bracket of an optional group never appears in an
  emission.

### The assertion, by example

```
- SPEC — [x](x) · review x[ · open x]   ->  - SPEC —  · review x[ · open x]   ->  FAIL, `[` left
- SPEC — [x](x) · review x · open x     ->  - SPEC —  · review x · open x     ->  ok
```

### Inventory

No identifier is minted. The assertion is part of unit 31's arm.

### Files touched (estimate)

- `tools/hooks/format-guard.test.sh` — S2

### Alternatives rejected

- **Grade only lines whose definition carries a group.** A shape gaining a group later would be
  unheld until someone edits the arm; one assertion per line holds every shape the fence defines.
- **Strip only `[ · ` and `]`.** A leaked `[` with no ` · ` after it would pass.

## 5. Production-readiness checklist

- security — N/A: a test assertion.
- perf / scale — one substitution and two membership tests per rendered line.
- error / empty / loading states — an arm that rendered no line asserts nothing; unit 31's floor
  counts the lines, so a vanished population reds the floor.
- observability — the failing line is printed whole with its head and form.
- risks — a shape adding a literal bracket outside a link: the assertion reds it, which is the
  `[grammar]` rule.
- testing — AC1 and AC2 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe applies the assertion's link pattern and bracket test to
  `- SPEC — [x](x) · review x[ · open x]` and to `- SPEC — [x](x) · review x · open x`, the first
  fails and the second holds.
  Red when: the leaked group passes, or a line whose only bracket is a link fails.
- **AC2** — When `node -e` loads `format-guard.js` and the arm runs with unit 31's group handling
  staged out of `render_shape_line`, the `SPEC` line is admitted by `buildShapeRegex` and refused by
  this assertion.
  Red when: the `SPEC` leak passes the arm.
  permission: the arm is unit 31's, built at order 13.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/hooks/format-guard.test.sh · covers AC2 · the shape arm's bracket assertion, staged red by `render_shape_line` with its group handling taken out · FLOOR_ASSERTIONS raised by the lines asserted

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 12 (HIGH, item H3, shared with id 27) of the
  round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`; unit 31 amended at the
  disposal (its rev-2).

## 10. Reuse audit

The seam extended is unit 31's shape arm and the suite's own `check`-style FAIL lines; the guard is
read through its exported `buildShapeRegex`, never copied. `python
tools/codebase-map/reuse_lookup.py "assert a rendered line carries no literal bracket"` ranked
`check_line` and `render_line` in `tools/runlog/runlog_lib.py` by name stem; `check_line` grades a
runlog line's own grammar and says nothing about a bracket, so no seam fits beyond the arm.

Recall terms used: `python tools/memory-recall/query.py "how is a rendered shape line held to the
format guard regex" --terms "buildShapeRegex render_shape_line bracket group staged break format guard
arm RolesError FLOOR_ASSERTIONS"`
