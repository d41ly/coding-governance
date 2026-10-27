# TOOL-dWellOiledMachine-105 — spec 97's S24 says what "before units 91 to 94 build" means, and its §5 names the ancestry probe as the detector

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 69 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-105-deviation-1051.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-105-deviation-1051.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 13, item H1, at HIGH. Item H1 also carries findings 1, 11, 19, 29, 12, 20, 30, 21 and 31,
closed by TOOL-dWellOiledMachine-98 to -104, -106 and -107. Finding 13 cites 97 AC15 with S24 and §5's
risks line: S24 claims units 91 to 94 "build and observe the corrected text" and names AC15 as the
observer, and §5 names AC15 as the signal for a skipped M2 cross-read, while AC15 prints e446e9582
forever. S24 also never says which two commits "before" compares, for four units at four orders. This
unit gives S24 the commit pair per unit and re-points §5 at TOOL-dWellOiledMachine-98's predicate.

## 2. Scope (IN)

- **S1** — 97 S24 states its terms. Spec 97 takes a rev bump, its §9 line naming this unit and
  finding 13, whose S24 reads: "The route. Every rev bump above is made by the build run's main loop
  at BUILD-METHOD M2's cross-read, before its first code pass, as one spec pass whose commit touches
  each of specs 91 to 94 and whose subject names this unit and none of TOOL-dWellOiledMachine-91 to
  -94, after the amendments of TOOL-dWellOiledMachine-95 and -96, by the route
  TOOL-dWellOiledMachine-95 §8 F1 takes, so units 91 to 94 build and observe the corrected text.
  Before unit N builds means that commit is a strict ancestor of unit N's build commit, the one
  `build_commit` (`tools/unattended/lib-unattended.sh:1186`) selects, as `check_amended_before_built`
  tests, for each N from 91 to 94. At this unit's own pass, at order 68, nothing is written: the pass
  runs AC1 to AC16 and records them. Observed by AC15, AC16." Observed by AC1, AC3.
- **S2** — 97 §5 names the detector. The same rev bump rewrites spec 97's §5 risks line to "a build
  run that skips M2's cross-read builds units 91 to 94 as first written; AC15 prints each unit whose
  build commit no amendment naming this unit precedes". Observed by AC2.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-97.md`, the one spec spelling the replaced line. by value: NO VALUE READERS — spec prose no program reads.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 97 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-91 to -94. At this unit's own pass, at order 69, nothing is written: the pass
  runs AC1 to AC4 and records them. Observed by AC4.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98.
- 97 AC15's text and §6 preamble: finding 21, TOOL-dWellOiledMachine-106. 97 AC16, its fixture and
  §5's testing line: finding 31, TOOL-dWellOiledMachine-107. S24 names AC16 because that unit adds it.
- No change to 97 S1 to S23 or to the route itself (97 §8 F1 stands).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-97` — S24 and §5's risks line, which this unit rewrites before unit 97's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate whose ancestry relation S24 names, and which AC4 runs
- **consumes-from** `TOOL-dWellOiledMachine-107` — 97 AC16, which S24's join names as an observer
- **hands-off** `TOOL-dWellOiledMachine-115` — §4 Evidence's citations of spec 97, rewritten by bullet label (round-5 promotions audit, finding 6)

## 4. Design

### Evidence

- 97 S24 names the route and "Observed by AC15", and no commit any of units 91 to 94 is measured by
  (`spec-97.md:135-140`); its §5 risks line names AC15 (`spec-97.md:225-226`).
- Re-run 2026-10-27, AC15's probe over 0689e7fa..HEAD prints the subject of e446e9582, which authored
  specs 91 to 94 (finding 13's appendix row).
- Units 91, 92, 93 and 94 sit at orders 56, 31, 66 and 67 (each spec's status header), so one
  "before" for all four is four commit pairs.
- The floor of `check_amended_before_built N 97 N` is 0d8692025, the commit adding spec 97, measured
  2026-10-27 with `git log --diff-filter=A --format=%h -- <spec 97>`.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-97.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 97's rev cell moves)

### Alternatives rejected

- **One "before" against the earliest of the four, unit 92.** Sufficient on a linear branch, but it
  hides which unit built on uncorrected text; one pair per unit names it.
- **S24 left as written, the criterion alone corrected.** The claim then has no stated terms.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — AC3 refuses an empty first-amendment subject for any of the four.
- observability — 97 §5's rewritten risks line.
- risks — none beyond 97's own.
- testing — AC1 to AC4.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<S24 of 97>` is the output of `awk '/^- \*\*S24\*\*/{p=1} /^## 3\./{p=0} p' <spec 97> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<S24 of 97>` is piped to `grep -c "none of TOOL-dWellOiledMachine-91 to -94"`, to
  `grep -c "build_commit"` and to `grep -c "Observed by AC15, AC16"`, each prints 1.
  Red when: S24 still names no commit pair, or lets the subject name a unit it must precede.
- **AC2** — When `awk '/^- risks/{p=1} /^- testing/{p=0} p' <spec 97> | tr -s '\n ' ' '` runs, its
  output piped to `grep -c "no amendment naming this unit precedes"` prints 1.
  Red when: §5 still names the subject-order probe as the detector.
- **AC3** — When, for each N in 91 92 93 94, `git log --reverse --format=%s 0d8692025..HEAD -- <spec N>`
  is piped to `grep -E '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-97([^A-Za-z0-9-]|$)' | head -1` at this
  unit's pass, it prints one subject, and that subject piped to
  `grep -cE '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-9[1-4]([^A-Za-z0-9-]|$)'` prints 0.
  figure: 0d8692025 is PINNED, the commit adding spec 97, measured 2026-10-27.
  Red when: a spec 97 amends has no amendment naming unit 97, or the subject names a unit it precedes.
- **AC4** — When `check_amended_before_built 97 105 94` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 97 lands after unit 94's build commit, the last build before
  unit 97's pass.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  13 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`); S24 names its terms rather than inventing a second meaning
of "before the units build". The probe `python tools/codebase-map/reuse_lookup.py "check that a spec
amendment commit landed before the unit's build commit"` ranked `build_commit` among name-stem hits
that are not this predicate; the recall query below ranked the round-4 report's fix and
TOOL-dTotalRecall-67's ancestry criterion among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
