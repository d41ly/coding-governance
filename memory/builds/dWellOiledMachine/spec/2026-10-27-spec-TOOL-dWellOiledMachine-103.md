# TOOL-dWellOiledMachine-103 — spec 96's AC5 checks its ordering by ancestry: the parse amendment is an ancestor of unit 93's build commit

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 68 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-103-deviation-1031.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-103-deviation-1031.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 20, item H1, at HIGH. Item H1 also carries findings 1, 11, 19, 29, 12, 30, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98 to -102 and -104 to -107. Finding 20 is 96 AC5: filtered by
`TOOL-dWellOiledMachine-(93|96)`, the subject-order probe prints e446e9582 first, the round-3 spec
commit naming 93, so it never observes whether 93's parse was amended before unit 93's pass. A late
amendment lets unit 93 build the verbatim parse and publish wrong `yes` cells tree-wide. This unit
rewrites AC5 to call TOOL-dWellOiledMachine-98's predicate, loaded from spec 95, and drops the `<BASE>`
placeholder AC5 alone used.

## 2. Scope (IN)

- **S1** — 96 AC5 rewritten. Spec 96 takes a rev bump, its §9 line naming this unit and finding 20,
  whose AC5 reads: "When `check_amended_before_built 93 96 93` runs at this unit's pass, it exits 0.
  Red when: the amendment of spec 93 is not an ancestor of unit 93's build commit, and 93 builds the
  verbatim parse." Observed by AC1, AC2.
- **S2** — 96's §6 preamble loads the predicate. The same rev bump replaces the preamble's
  "and `<BASE>` is the build run's pinned `base:` fact in `memory/builds/dWellOiledMachine/RUN.md`"
  with "and `check_amended_before_built` is the function spec 95's §6 defines, loaded by
  `eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"` from the repository
  root", spelling spec 95's path in full because 96's preamble defines no `<spec 95>`,
  the eval code span kept on one line, since no other criterion of spec 96 spells `<BASE>`.
  Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 96 and whose subject names this unit and not
  TOOL-dWellOiledMachine-93. At this unit's own pass, at order 68, nothing is written: the pass runs
  AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98. 96 S4's terms: finding 12,
  TOOL-dWellOiledMachine-102. The staged red case: finding 30, TOOL-dWellOiledMachine-104.
- No change to 96 AC1 to AC4, AC6 or AC7.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-96` — AC5 and the §6 preamble, which this unit rewrites before unit 96's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the rewritten AC5 loads from spec 95 and calls
- **hands-off** `TOOL-dWellOiledMachine-113` — AC1's last clause, which counts the loader in spec 96's §6 preamble alone (round-5 promotions audit, finding 20)
- **hands-off** `TOOL-dWellOiledMachine-115` — §3 Edges and §4 Evidence, which gain the edge to unit 104, the two loader copies and bullet-label citations (round-5 promotions audit, findings 1, 8 and 24)

## 4. Design

### Evidence

- 96 AC5 is `git log --reverse --format=%s <BASE>..HEAD | grep -E "TOOL-dWellOiledMachine-(93|96)([^0-9]|$)" | head -1`
  (`spec-96.md:179-181`), and `<BASE>` appears in 96's §6 preamble and in AC5 only
  (`grep -n "<BASE>"` over spec 96 prints lines 150 and 179, measured 2026-10-27).
- Re-run 2026-10-27, AC5's probe prints the subject of e446e9582, which names TOOL-dWellOiledMachine-93
  and predates any amendment (finding 20's appendix row).
- `check_amended_before_built 93 96 93` exits 1 on this tree today: no amendment and no build commit
  exist (TOOL-dWellOiledMachine-98 §4).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-96.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 96's rev cell moves)

### Alternatives rejected

- **A content anchor on `derive_arm_suite_path`.** It is absent from spec 93 today and would work
  here, but finding 31 shows the scheme fails for another spec; one predicate for all three is the
  point of TOOL-dWellOiledMachine-98.
- **Keeping `<BASE>` in the preamble.** It would be a placeholder no criterion reads.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — the predicate returns 1 on any empty population.
- observability — the rewritten AC5's exit status.
- risks — none beyond 96's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<AC5 of 96>` is the output of `awk '/^- \*\*AC5\*\*/{p=1} /^- \*\*AC6\*\*/{p=0} p' <spec 96> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<AC5 of 96>` is piped to `grep -c "check_amended_before_built 93 96 93"`, it prints
  1, and piped to `grep -c "head -1"` it prints 0; `grep -c "<BASE>" <spec 96>` prints 0; and
  `grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'" <spec 96>` prints 1.
  Red when: AC5 still orders by the first subject a log prints, or the preamble neither loads the
  predicate nor drops the unused placeholder.
- **AC2** — When `check_amended_before_built 93 96 93` runs at this unit's pass, after unit 93 has
  built, it exits 0.
  Red when: the amendment of spec 93 landed after unit 93's build commit.
- **AC3** — When `check_amended_before_built 96 103 93` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 96 lands after unit 93's build commit, so unit 96's pass ran
  the old AC5.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  20 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-113, TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95 rather than copied. The probe
`python tools/codebase-map/reuse_lookup.py "check that a spec amendment commit landed before the unit's
build commit"` ranked `build_commit` among name-stem hits that are not this predicate; the recall query
below ranked the round-4 report's fix and TOOL-dTotalRecall-67's ancestry criterion among its first
hits.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
