# TOOL-dWellOiledMachine-111 — spec 108's AC21 checks its amendment of spec 97 against every unit that amendment reaches, from 90 to 94

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 71 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-111-deviation-1111.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-111-deviation-1111.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-115 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-5 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`),
finding 5, item H2, at HIGH. Item H2 also carries finding 29, closed by TOOL-dWellOiledMachine-112.

Finding 5 is 108 AC21. For spec 97 it runs only `check_amended_before_built 97 108 94`, and unit 94
is order 67. But the batch's amendment of spec 97 corrects text that earlier units consume: 108 S21
corrects 97 S20, which rev-bumps spec 92 (order 31); 108 S9 and S10 correct 97 S1, whose rewrite of
94 S14 reaches 90 AC20 (order 65); and 108 S22 corrects 97 S15, which bumps spec 93 (order 66). A
bump that lands after unit 92 builds and before unit 94 builds still exits 0. This unit rewrites
AC21's spec-97 clause as one predicate call per unit that amendment reaches, so the earliest is
covered and the unit out of order is named.

## 2. Scope (IN)

- **S1** — 108 AC21 rewritten. Spec 108 takes a rev bump, its §9 line naming this unit and finding
  5, whose AC21 reads: "When `check_amended_before_built 95 108 90` and
  `check_amended_before_built 96 108 93` run, each exits 0, and when
  `for n in 90 91 92 93 94; do check_amended_before_built 97 108 $n || echo $n; done` runs, it prints
  nothing. Red when: a rev bump of this batch lands after the build commit of a unit whose spec it
  corrects, directly or through spec 97's own amendments, and the loop prints that unit." Observed
  by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 108 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. At this unit's own pass, at order 71, nothing is written: the
  pass runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The staged red case for the rewritten clause: finding 29, TOOL-dWellOiledMachine-112.
- AC21's clauses for specs 95 and 96 stay as written: spec 95 corrects specs 90 and 93 and spec 96
  corrects spec 93, so units 90 and 93 are already the earliest each reaches.
- No derivation of the unit list from the amended spec's S-bullets. That is the report's left-shift
  line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-108` — AC21, which this unit rewrites before unit 108's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate the rewritten loop and AC3 call
- **hands-off** `TOOL-dWellOiledMachine-112` — the rewritten loop, which 112's fixture extracts from 108 AC21 and runs

## 4. Design

### Evidence

- 108 AC21 runs `check_amended_before_built 97 108 94` and no other call for spec 97 (finding 5's
  appendix row, re-read 2026-10-27).
- The orders, from each status header: 92 is 31, 91 is 56, 90 is 65, 93 is 66 and 94 is 67.
- 97's Files touched lists specs 91, 92, 93 and 94. 97 S1 rev-bumps spec 94, whose S14 rewrites 90's
  AC20, so 108's corrections of 97 S1 reach unit 90 one spec further on.
- On a scratch fixture repository under `%TEMP%`, run 2026-10-27, the loop printed `92` where the
  bump landed after unit 92's build commit and before the other four, while
  `check_amended_before_built 97 108 94` exited 0 on the same history. TOOL-dWellOiledMachine-112
  carries that fixture.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 108's rev cell moves)

### Alternatives rejected

- **One call against unit 92, the earliest.** It covers every case today but cannot say which unit
  built on uncorrected text, and it goes stale if a later amendment reaches an earlier unit.
- **A loop over 91 to 94 only, the specs 97 lists.** It misses unit 90, which 97 reaches through 94
  S14.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — five predicate calls instead of one; each is cheap where the predicate caches
  attribution (TOOL-dWellOiledMachine-115).
- error / empty / loading states — the predicate returns 1 on any empty population, and the loop
  prints that unit.
- observability — the loop names each unit out of order.
- risks — none beyond 108's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<AC21 of 108>` is the output of `awk '/^- \*\*AC21\*\*/{p=1} /^- \*\*AC22\*\*/{p=0} /^## 7\./{p=0} p' <spec 108> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<AC21 of 108>` is piped to
  `grep -c 'for n in 90 91 92 93 94; do check_amended_before_built 97 108 $n || echo $n; done'`, it
  prints 1, and piped to `grep -c "97 108 94"` it prints 0.
  Red when: AC21 still checks spec 97's amendment against unit 94 alone.
- **AC2** — When `for n in 90 91 92 93 94; do check_amended_before_built 97 108 $n || echo $n; done`
  runs at this unit's pass, after units 90 to 94 have built, it prints nothing.
  Red when: the batch's amendment of spec 97 landed after one of the five build commits.
- **AC3** — When `check_amended_before_built 108 111 92` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 108 lands after unit 92's build commit, so unit 108's pass
  ran the old AC21.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  5 (H2).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95, and the per-unit loop shape that
TOOL-dWellOiledMachine-106 gives 97 AC15. The probe `python tools/codebase-map/reuse_lookup.py "check
that a spec amendment commit landed before the unit's build commit"` ranks `build_commit` among
name-stem hits, as recorded for units 98 and 106, and no loop helper exists in code.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
