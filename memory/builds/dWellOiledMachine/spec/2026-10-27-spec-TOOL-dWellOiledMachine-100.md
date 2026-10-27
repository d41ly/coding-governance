# TOOL-dWellOiledMachine-100 — spec 95's AC2 checks its ordering by ancestry: each rev bump is an ancestor of unit 90's build commit

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-100-deviation-1001.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-100-deviation-1001.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 19, item H1, at HIGH. Item H1 also carries findings 1, 11, 29, 12, 20, 30, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98, -99 and -101 to -107. Finding 19 is 95 AC2's first half: over
RUN.md's base 0689e7fa, `git log --reverse` filtered by `TOOL-dWellOiledMachine-(90|95)` prints
089c397aa first, the round-2 spec commit, so `head -1` can never print unit 95's amendment. Read
literally the criterion is red on a correct build; read loosely it is green with no amendment. This
unit rewrites that half to call TOOL-dWellOiledMachine-98's predicate for both specs unit 95 amends,
keeping the second half, the `design_lib` history count, which works.

## 2. Scope (IN)

- **S1** — 95 AC2 rewritten. Spec 95 takes a rev bump, its §9 line naming this unit and finding 19,
  whose AC2 reads: "When `check_amended_before_built 90 95 90` and
  `check_amended_before_built 93 95 90` run at this unit's pass, each exits 0; and
  `git log --format=%s <BASE>..HEAD -- tools/memory-tree/design_lib.py | grep -cE "TOOL-dWellOiledMachine-90([^0-9]|$)"`
  prints 0. Red when: a rev bump of spec 90 or spec 93 is not an ancestor of unit 90's build commit,
  or unit 90's pass edits `design_lib`." Spec 93 is checked against unit 90's build commit because
  95 S3 claims both rev bumps land before unit 90's pass. Observed by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 95 and whose subject names this unit and neither
  TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93. At this unit's own pass, at order 67,
  nothing is written: the pass runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate and the §6 sentence that loads it: finding 1, TOOL-dWellOiledMachine-98.
- 95 S3's terms and §5: finding 11, TOOL-dWellOiledMachine-99. The staged red case: finding 29,
  TOOL-dWellOiledMachine-101.
- No change to AC2's second half, which the report found working.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-95` — AC2, whose first half this unit rewrites before unit 95's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the rewritten AC2 calls

## 4. Design

### Evidence

- 95 AC2's first half is `git log --reverse --format=%s <BASE>..HEAD | grep -E "TOOL-dWellOiledMachine-(90|95)([^0-9]|$)" | head -1`
  and requires this unit's amendment commit (`spec-95.md:136-140`); 95's §6 preamble defines `<BASE>`
  as RUN.md's pinned base (`spec-95.md:129-130`), which is 0689e7fa (`RUN.md:30`).
- Re-run 2026-10-27 at this spec's writing, that probe prints the subject of 089c397aa, which names
  TOOL-dWellOiledMachine-90 and predates every amendment.
- 95 S1 rev-bumps spec 90 and 95 S2 rev-bumps spec 93, and 95 S3 claims both land before unit 90's
  pass (`spec-95.md:29-53`).
- `check_amended_before_built 90 95 90` and `93 95 90` both exit 1 on this tree today: no amendment
  and no build commit exist (TOOL-dWellOiledMachine-98 §4).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 95's rev cell moves)

### Alternatives rejected

- **The subject probe with a later range start.** Any start before the amendment admits the next
  commit that names an id, and a start after it is a value nobody can know when the spec is written.
- **Spec 90 alone.** 95 S2's rev bump of spec 93 would then carry the same claim and no observer.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — the predicate returns 1 on any empty population.
- observability — the rewritten AC2's two exit statuses.
- risks — none beyond 95's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<AC2 of 95>` is the output of `awk '/^- \*\*AC2\*\*/{p=1} /^- \*\*AC3\*\*/{p=0} p' <spec 95> | tr -s '\n ' ' '`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<AC2 of 95>` is piped to `grep -c "check_amended_before_built 90 95 90"`, to
  `grep -c "check_amended_before_built 93 95 90"` and to `grep -c "design_lib.py"`, each prints 1, and
  piped to `grep -c "head -1"` it prints 0.
  Red when: AC2 still orders by the first subject a log prints, or drops a spec or the history half.
- **AC2** — When `check_amended_before_built 90 95 90` and `check_amended_before_built 93 95 90` run
  at this unit's pass, after unit 90 has built, each exits 0.
  Red when: either rev bump of 95 landed after unit 90's build commit.
- **AC3** — When `check_amended_before_built 95 100 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 95 lands after unit 90's build commit, so unit 95's pass
  ran the old AC2.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  19 (H1).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), called with the two specs 95 amends; AC2's working half
is kept as written. The probe `python tools/codebase-map/reuse_lookup.py "check that a spec amendment
commit landed before the unit's build commit"` ranked `build_commit` among name-stem hits that are not
this predicate; the recall query below ranked the round-4 report's fix and TOOL-dTotalRecall-67's
ancestry criterion among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
