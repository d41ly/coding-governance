# TOOL-dWellOiledMachine-102 — spec 96's S4 says what "before unit 93's pass" means, so its ordering claim names the two commits it compares

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 68 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-102-deviation-1021.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-102-deviation-1021.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 12, item H1, at HIGH. Item H1 also carries findings 1, 11, 19, 29, 20, 30, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98 to -101 and -103 to -107. Finding 12 cites 96 AC5 with S4: AC5 is
S4's only observer, its output is fixed at e446e9582 before the build starts, and S4 itself says only
that the rev bump lands "before unit 93's pass". Unit 93's own pass touches spec 93 when it flips its
status, so "the first commit touching spec 93" is no answer either. This unit gives S4 the two commits
and the relation TOOL-dWellOiledMachine-98's predicate tests.

## 2. Scope (IN)

- **S1** — 96 S4 states its terms. Spec 96 takes a rev bump, its §9 line naming this unit and finding
  12, whose S4 reads: "The rev bump lands before unit 93's pass, by the route TOOL-dWellOiledMachine-95
  §8 F1 takes: the build run's main loop makes it at BUILD-METHOD M2's cross-read, before its first
  code pass, as one spec pass whose commit touches spec 93 and whose subject names this unit and not
  TOOL-dWellOiledMachine-93. Before unit 93's pass means that commit is a strict ancestor of unit 93's
  build commit, the one `build_commit` (`tools/unattended/lib-unattended.sh:1186`) selects, as
  `check_amended_before_built` tests; unit 93's own commits touching spec 93 never count, because
  their subjects do not name this unit. At this unit's own pass, at order 67, nothing is written: the
  pass runs AC1 to AC8 and records them. Observed by AC5, AC8." Observed by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 96 and whose subject names this unit and not
  TOOL-dWellOiledMachine-93. At this unit's own pass, at order 68, nothing is written: the pass runs
  AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98.
- 96 AC5's text and §6 preamble: finding 20, TOOL-dWellOiledMachine-103. 96 AC8, its fixture and
  §5's testing line: finding 30, TOOL-dWellOiledMachine-104. S4 names AC8 because that unit adds it.
- No change to 96 S1 to S3 or to the route itself (96 §8 F1 stands).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-96` — S4, which this unit rewrites before unit 96's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate whose ancestry relation S4 names, and which AC3 runs
- **consumes-from** `TOOL-dWellOiledMachine-104` — 96 AC8, which S4's join names as an observer
- **hands-off** `TOOL-dWellOiledMachine-115` — §4 Evidence's citations of spec 96, rewritten by bullet label (round-5 promotions audit, finding 6)

## 4. Design

### Evidence

- 96 S4 names the route and "Observed by AC5", and no commit unit 93's pass is measured by
  (`spec-96.md:50-53`); AC5 is its only observer (`spec-96.md:179-181`).
- Re-run 2026-10-27, AC5's probe over 0689e7fa..HEAD prints the subject of e446e9582, the round-3
  spec commit authoring spec 93 (finding 12's appendix row).
- `build_commit` skips a commit touching only the build's folder
  (`tools/unattended/lib-unattended.sh:1186`), so a spec pass naming unit 93 is never unit 93's build
  commit unless it also touches a path outside that folder; keeping 93 out of the subject keeps the
  two apart.
- The floor of `check_amended_before_built 93 96 93` is 0d8692025, the commit adding spec 96, measured
  2026-10-27 with `git log --diff-filter=A --format=%h -- <spec 96>`.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-96.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 96's rev cell moves)

### Alternatives rejected

- **The first commit after the floor touching spec 93, whatever its subject.** Unit 93's status flip
  is such a commit, so a skipped amendment would be read as one that landed.
- **S4 left as written, the criterion alone corrected.** The claim then has no stated terms.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — AC2 refuses an empty first-amendment subject.
- observability — S4's stated terms.
- risks — none beyond 96's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<S4 of 96>` is the output of `awk '/^- \*\*S4\*\*/{p=1} /^## 3\./{p=0} p' <spec 96> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<S4 of 96>` is piped to `grep -c "not TOOL-dWellOiledMachine-93"`, to
  `grep -c "build_commit"` and to `grep -c "Observed by AC5, AC8"`, each prints 1.
  Red when: S4 still names no commit pair, or lets the subject name the unit it must precede.
- **AC2** — When `git log --reverse --format=%s 0d8692025..HEAD -- <spec 93>` is piped to
  `grep -E '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-96([^A-Za-z0-9-]|$)' | head -1` at this unit's pass,
  it prints one subject, and that subject piped to
  `grep -cE '(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-93([^A-Za-z0-9-]|$)'` prints 0.
  figure: 0d8692025 is PINNED, the commit adding spec 96, measured 2026-10-27.
  Red when: no amendment of spec 93 names unit 96, or its subject names unit 93.
- **AC3** — When `check_amended_before_built 96 102 93` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 96 lands after unit 93's build commit, so unit 96's pass ran
  the old S4.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  12 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`); S4 names its terms rather than inventing a second meaning
of "before the pass". The probe `python tools/codebase-map/reuse_lookup.py "check that a spec amendment
commit landed before the unit's build commit"` ranked `build_commit` among name-stem hits that are not
this predicate; the recall query below ranked the round-4 report's fix and TOOL-dTotalRecall-67's
ancestry criterion among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
