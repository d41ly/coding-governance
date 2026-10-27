# TOOL-dWellOiledMachine-99 — spec 95's S3 says what "before unit 90's pass" means, and its §5 names the ancestry probe as the detector

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-99-deviation-991.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-99-deviation-991.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 11, item H1, at HIGH. Item H1 also carries findings 1, 19, 29, 12, 20, 30, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98 and -100 to -107. Finding 11 cites 95 AC2 together with S3 and
§5's risks line: S3 claims the rev bumps land "before unit 90's pass" without saying which two
commits that compares, and §5 names AC2 as the signal for a skipped M2 cross-read, while AC2's
subject-order half can never print the amendment. This unit gives S3 the two commits and the relation
TOOL-dWellOiledMachine-98's predicate tests, and re-points §5 at it.

## 2. Scope (IN)

- **S1** — 95 S3 states its terms. Spec 95 takes a rev bump, its §9 line naming this unit and finding
  11, whose S3 reads: "The rev bumps land before unit 90's pass. S1's and S2's rev bumps are made by
  the build run's main loop at BUILD-METHOD M2's cross-read, before its first code pass, as one spec
  pass whose commit touches specs 90 and 93 and whose subject names this unit and neither
  TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93. Before unit 90's pass means that commit is
  a strict ancestor of unit 90's build commit, the one `build_commit`
  (`tools/unattended/lib-unattended.sh:1186`) selects, as `check_amended_before_built` tests. At this
  unit's own pass, at order 66, nothing is written: the pass runs AC1 to AC6 and records them.
  Observed by AC2, AC6." Observed by AC1, AC3.
- **S2** — 95 §5 names the detector. The same rev bump rewrites spec 95's §5 observability line to
  "AC2's ancestry half shows whether each rev bump is an ancestor of unit 90's build commit, and its
  history half whether unit 90's pass touched `design_lib`", and its risks line to "a build run that
  skips M2's cross-read builds 90 S1 as first written; AC2's ancestry half is red at this unit's pass
  in that case, because no commit naming this unit touches spec 90 before unit 90's build commit, and
  the remedy is 93 S3 as first written, which reverts the widening". Observed by AC2.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md`, the one spec spelling the replaced lines. by value: NO VALUE READERS — spec prose no program reads.
- **S3** — The route. S1's and S2's rev bump is made at BUILD-METHOD M2's cross-read, before the first
  code pass, in a spec pass whose commit touches spec 95 and whose subject names this unit and neither
  TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93. At this unit's own pass, at order 67,
  nothing is written: the pass runs AC1 to AC4 and records them. Observed by AC4.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98.
- 95 AC2's text: finding 19, TOOL-dWellOiledMachine-100. 95 AC6 and §5's testing line: finding 29,
  TOOL-dWellOiledMachine-101. S3 names AC6 as an observer because that unit adds it.
- No change to 95 S1 or S2, or to the route itself (95 §8 F1 stands).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-95` — S3 and §5's observability and risks lines, which this unit rewrites before unit 95's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate whose ancestry relation S3 names, and which AC4 runs
- **consumes-from** `TOOL-dWellOiledMachine-101` — 95 AC6, which S3's join names as an observer
- **hands-off** `TOOL-dWellOiledMachine-115` — §4 Evidence's citations of spec 95, rewritten by bullet label (round-5 promotions audit, finding 6)

## 4. Design

### Evidence

- 95 S3 says "as one spec pass whose commit subject names this unit" and "Observed by AC2", and names
  no commit unit 90's pass is measured by (`spec-95.md:50-53`).
- 95 §5's observability and risks lines name AC2's history probe as the signal (`spec-95.md:120-122`).
- `build_commit` is the history leg's definition of the commit that built a unit
  (`tools/unattended/lib-unattended.sh:1186`); it skips a commit touching only the build's folder,
  so a spec pass that names TOOL-dWellOiledMachine-90 is never unit 90's build commit unless it also
  touches a path outside that folder. S1 keeps the two apart by keeping 90 and 93 out of the subject.
- The floor of `check_amended_before_built 90 95 90` is 0d8692025, the commit adding spec 95,
  measured 2026-10-27 with `git log --diff-filter=A --format=%h -- <spec 95>`.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 95's rev cell moves)

### Alternatives rejected

- **S3 left as written, the criterion alone corrected.** The claim then has no stated terms, and a
  reader of S3 cannot tell what AC2 measures.
- **Subjects allowed to name the amended unit.** A spec pass that also touched a generated index
  outside the build folder would be read as unit 90's build commit, and the verdict would go red on a
  correct order.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — AC3 refuses an empty first-amendment subject.
- observability — 95 §5's rewritten lines.
- risks — none beyond 95's own.
- testing — AC1 to AC4.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<S3 of 95>` is the output of `awk '/^- \*\*S3\*\*/{p=1} /^## 3\./{p=0} p' <spec 95> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<S3 of 95>` is piped to `grep -c "neither TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93"`
  and to `grep -c "build_commit"`, each prints 1.
  Red when: S3 still names no commit pair, or lets the subject name the unit it must precede.
- **AC2** — When `awk '/^- (observability|risks)/{p=1} /^- testing/{p=0} p' <spec 95> | tr -s '\n ' ' '`
  runs, its output piped to `grep -o "ancestry half" | wc -l` prints 2, and piped to
  `grep -c "build commit"` prints 1.
  Red when: §5 still names the subject-order probe as the detector.
- **AC3** — When `git log --reverse --format=%s 0d8692025..HEAD -- <spec 90>` is piped to
  `grep -E '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-95([^A-Za-z0-9-]|$)' | head -1` at this unit's pass,
  it prints one subject, and that subject piped to
  `grep -cE '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-9[03]([^A-Za-z0-9-]|$)'` prints 0.
  figure: 0d8692025 is PINNED, the commit adding spec 95, measured 2026-10-27.
  Red when: no amendment of spec 90 names unit 95, or its subject names a unit it must precede.
- **AC4** — When `check_amended_before_built 95 99 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 95 lands after unit 90's build commit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  11 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`); S3 names its terms rather than inventing a second meaning
of "before the pass". The probe `python tools/codebase-map/reuse_lookup.py "check that a spec amendment
commit landed before the unit's build commit"` ranked `build_commit` among name-stem hits that are not
this predicate; the recall query below ranked the round-4 report's fix and TOOL-dTotalRecall-67's
ancestry criterion among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
