# TOOL-dGroundRules-49 — the help page's guard line observed by the leg query with its path whole, and by the trace when it is taken out

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-49-deviation-37.md](../build/2026-10-23-build-TOOL-dGroundRules-49-deviation-37.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 11 at HIGH**, which shares item **H2** with ids 2
(`TOOL-dGroundRules-48`) and 22 (`TOOL-dGroundRules-50`). Id 11 is H2 seen from grounding: the
reviewer ran `TOOL-dGroundRules-41`'s `HELP_LEGS`, `--legs-for` over a bare `policy.md`, and the
checker refused with exit 2 because no such path is tracked, so AC5 can never name
`policy fixtures` and S2's guard line is observed by no criterion that can pass. This unit is id 11's
promotion. It changes no code: it observes S2 twice, once through the leg query with the page path
whole, and once through the standing check that holds the line on every run of the leg, the guard
trace of `TOOL-dGroundRules-33`, which reds the page's in-process read when the line is taken out of
the guard. It repairs `TOOL-dGroundRules-41`, which sits at order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The query, whole. `HELP_LEGS_WHOLE` (§5) asks `tools/check-spec-tokens.py --legs-for`
  for `help/policy.md`, and is the command through which `TOOL-dGroundRules-41` AC5 is observed at
  this unit's close. Observed by AC1.
- **S2** — The standing observer. With `help/policy.md` taken out of the `policy fixtures` guard in
  a scratch copy, `--fixture adopter-fresh-target`, which reads the page in process
  (`TOOL-dGroundRules-41` S1), prints a `guard-trace` `WRONG` naming the page; restored, it prints
  none. Observed by AC2.

## 3. Non-goals (OUT)

- The guard line itself, `TOOL-dGroundRules-41` S2, and the trace, `TOOL-dGroundRules-33`. This
  unit observes them.
- The install-section count and the case's witness line: `TOOL-dGroundRules-48` and
  `TOOL-dGroundRules-50`.

### Edges

- **consumes-from** `TOOL-dGroundRules-41` — S2's `help/policy.md` line in the `policy fixtures` guard and S1's in-process read of the page, which S1 and S2 observe
- **consumes-from** `TOOL-dGroundRules-33` — the guard trace of `--fixture`, which S2 uses as the standing observer of the guard line
- **hands-off** `TOOL-dGroundRules-52` — `HELP_LEGS_WHOLE`, through which that unit observes `TOOL-dGroundRules-41` AC5 (id 31)

## 4. Design

`TOOL-dGroundRules-41` §4 says the page is read in process so the trace sees the read, and that
S2's guard line is what keeps the trace green; S2 here is that sentence staged to fail. The trace's
`WRONG` line form is `policy-fixture: guard-trace · WRONG <path>` (`TOOL-dGroundRules-33` S3).
`python tools/check-spec-tokens.py --legs-for help/policy.md` printed `no guarded leg` on 2026-10-23,
before the page or its guard line exists.

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

## 5. Acceptance criteria

Every command runs from the repository root. `check_policy.py` names the policy kit's file under the
kit, as `TOOL-dGroundRules-41` §6 does. A scratch copy is a git clone of this repository under
`%TEMP%/gr49`, checked out at the commit under test. Literals are spelled whole here, once:

```text
HELP_LEGS_WHOLE = python tools/check-spec-tokens.py --legs-for help/policy.md
GUARD_DROPPED   = in the scratch copy's tools/gate-legs.json, the "help/policy.md" entry of the
                  "policy fixtures" row's guard list taken out
```

- **AC1** — When `HELP_LEGS_WHOLE` runs on the built tree, its output names `policy fixtures`.
  Red when: an edit to the help page alone skips the leg that holds it.
- **AC2** — When `GUARD_DROPPED` runs and `python check_policy.py --fixture adopter-fresh-target`
  runs in that copy, it prints a `guard-trace` `WRONG` line naming `policy.md`; with the entry
  restored it prints no `guard-trace` `WRONG`.
  Red when: the guard line can go missing with the leg green.

## 6. Gates

`memory hygiene`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 11 (HIGH, item H2) of the round-1 spec
  audit of units 35 to 43, from the review's sound fix and the guard trace unit 41 §4 names, read on
  2026-10-23.

## 9. Reuse audit

The seams observed are `print_legs_for` of `tools/check-spec-tokens.py:637`, the leg query, and the
guard trace `TOOL-dGroundRules-33` builds; nothing is built, so no existing seam needs extending.
`python tools/codebase-map/reuse_lookup.py "read test table rows from a suite file to probe two
overlap rules"` ranked no seam that holds a guard line. The recall probe returned
`TOOL-dGroundRules-41` and `TOOL-aKeyedAnnotation-9`; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
