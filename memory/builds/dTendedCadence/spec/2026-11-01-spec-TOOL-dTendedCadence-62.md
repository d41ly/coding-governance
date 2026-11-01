# TOOL-dTendedCadence-62 — unit 15's breach route spells the red leg's hold `red-leg` in its route list, its S3 and its diagram

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 5 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 27 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dTendedCadence-60), 14 (TOOL-dTendedCadence-61) and 35
(TOOL-dTendedCadence-63). Unit 15 consumes `red-leg` from unit 56 in its §3 edge (spec-15:150), but its
S1 still prints the routes `filed`, `seen`, `held` or `reported` (:50), its S3 says "route `held`"
(:73), and its §4 diagram shows `(held)` (:180). Built from S1 and S3, `run_breach_route` returns
`held`, which unit 56 keys no `over-pin:` line on, so the red leg reads green while offenders stand.
This unit makes unit 15's text return the one name the record reads.

## 2. Scope (IN)

- **S1** — The route list. Spec-15 S1's printed line reads `file — <reading> · key <key hash> ·
  <route>`, the route one of `filed`, `seen`, `red-leg` or `reported`. Corrected in spec-15's text, a
  rev bump with a §9 line naming review id 27. Observed by AC1.
- **S2** — The hold. Spec-15 S3 reads "`red-leg` at the route: nothing is filed, route `red-leg`",
  and its criterion that prints two `· held` lines (:253) prints two `· red-leg` lines. Observed by
  AC1.
- **S3** — The diagram. Spec-15 §4's diagram row for `red-leg` ends `(red-leg)`. Observed by AC1.

## 3. Non-goals (OUT)

- Unit 3's owner-gated direct outcome `held`, which unit 15's §3 edge toward unit 3 (:140) still
  names: it routes to `item.maintain.file`, never to the record, and keeps its name (spec-56 §8 F1).
- The other readers of the hold: TOOL-dTendedCadence-60 (unit 1) and TOOL-dTendedCadence-74 (item M7).

### Edges

- **consumes-from** `TOOL-dTendedCadence-56` — the hold's name `red-leg`, which unit 15's text now returns throughout
- **hands-off** `TOOL-dTendedCadence-15` — S1's route list, S3's route and the §4 diagram, corrected in that unit's spec before it builds at order 7

## 4. Design

Three spans and one criterion of spec-15 move; every other `held` in spec-15 names unit 3's outcome
and stays. Written in this unit's build pass at order 5, before unit 15 builds at order 7.

### Files touched (estimate)

- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md`: S1 to S3

## 5. Acceptance criteria

- **AC1** — When `grep -n "route .held.\|(held)\|· held\|.held. or .reported."
  2026-11-01-spec-TOOL-dTendedCadence-15.md` runs in the spec folder, it prints nothing, where at base
  it prints four lines (:50, :73, :180, :253).
  Red when: unit 15's text still returns the old name on any path the record reads.
  figure: the four base hits are PINNED 2026-11-01 by that command.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 27 (HIGH, item H1) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

No code is written; the seam is spec-15's own text, corrected in place. Recall found no other spelling
of the hold to align with beyond unit 56 S2.

Recall terms used: `python tools/memory-recall/query.py "which route does a breach held by the red
leg carry" --terms "red-leg held route maintain.on-breach run_breach_route over-pin record hold
rename"`
