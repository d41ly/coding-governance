# TOOL-dWellOiledMachine-116 — spec 115's AC4 greps 108 AC8 for the two full paths S6 writes, and for the bare pathspec as gone

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 73 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-116-deviation-1161.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-116-deviation-1161.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`),
finding 1, item H1, at HIGH. Item H1 merges findings 1, 9, 18 and 21, and each takes its own unit:
finding 9 is TOOL-dWellOiledMachine-117, finding 18 is TOOL-dWellOiledMachine-118 and finding 21 is
TOOL-dWellOiledMachine-119.

Finding 1 is the coherence half of 115 AC4. 115 S6 rewrites 108 AC8 from the bare names to the two
full paths, but AC4 still requires `<AC8 of spec 108>` to contain
`error-unmatch supervise.py door_fixture.py`. That grep prints 1 before S6 lands and 0 after it, so
AC4 contradicts the scope item it observes, and its one green path is reverting S6. This unit
rewrites that clause to count the full paths S6 writes and to require the bare pathspec gone.

## 2. Scope (IN)

- **S1** — 115 AC4's grep clause rewritten. Spec 115 takes a rev bump, its §9 line naming this unit
  and finding 1. AC4's second clause is the one that pipes `<AC8 of spec 108>` to two counts and ends
  at the first "each prints 1"; it wraps over three lines. It becomes, each code span on one line:
  "`<AC8 of spec 108>` piped to `grep -c "tools/runtime/supervise.py"`, to
  `grep -c "tools/memory-tree/door_fixture.py"` and to `grep -c "only a file at the repository root"`
  each prints 1, and piped to `grep -c "error-unmatch supervise.py"` prints 0". AC4's first clause
  and its red case are TOOL-dWellOiledMachine-117's and -118's, and its last clause, over
  `<§4 of spec 108>`, stays. Observed by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 115 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 115 makes are applied. At this
  unit's own pass, at order 73, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's `git ls-files` clause and the base reading that grounds it: finding 9,
  TOOL-dWellOiledMachine-117.
- AC4's red case and the reading that shows a reverted S6 reads red: finding 18,
  TOOL-dWellOiledMachine-118.
- AC6's walk over bare names: finding 21, TOOL-dWellOiledMachine-119.
- The quoting of the paths S6 writes: finding 17, TOOL-dWellOiledMachine-120. The clause above holds
  either way, because a quoted path still contains the unquoted string.
- No spec-lint leg that applies scope items to a scratch copy and runs the criteria over it. That is
  the report's left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — AC4's second clause, which this unit rewrites before spec 115's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

Re-run 2026-10-27 at HEAD 63dbec5e8, with `<AC8 of spec 108>` sliced and flattened as 115's §6
preamble defines it:

| 108 AC8 | `tools/runtime/supervise.py` | `tools/memory-tree/door_fixture.py` | `only a file at the repository root` | `error-unmatch supervise.py` |
|---|---|---|---|---|
| as committed | 0 | 0 | 0 | 1 |
| scratch copy, 115 S6 and S8 applied | 1 | 1 | 1 | 0 |

The scratch copy was made both with S6 as written and with TOOL-dWellOiledMachine-120's quoted
pathspecs; both print the second row.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 115's rev cell moves)

### Alternatives rejected

- **Grep the whole rewritten pathspec, `error-unmatch` and both paths.** Its spelling depends on
  whether TOOL-dWellOiledMachine-120's quotes land, so two units would own one string.
- **Drop the clause and rely on AC4's `git ls-files` half.** That half reads the tree, not 108 AC8,
  so it cannot tell whether S6 was applied.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — four greps over one bullet.
- error / empty / loading states — an absent AC8 bullet prints 0 for each full path and reads red.
- observability — AC2 prints the four counts before and after S6.
- risks — none beyond 115's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`. Each command runs from the repository root; the
predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC4 of spec 115>` is piped to `grep -c 'grep -c "tools/runtime/supervise.py"'` and
  to `grep -c 'grep -c "error-unmatch supervise.py"'`, each prints 1, and piped to
  `grep -c 'grep -c "error-unmatch supervise.py door_fixture.py"'` it prints 0.
  Red when: AC4 still requires the bare pathspec string that S6 removes.
- **AC2** — When `git show 63dbec5e8:<spec 108>` is sliced to AC8 and flattened as `<X of spec N>` is,
  the four counts of the rewritten clause print 0, 0, 0 and 1; and over `<AC8 of spec 108>` at this
  unit's pass, after spec 115's amendments of spec 108 have landed, they print 1, 1, 1 and 0.
  Red when: the rewritten clause reads green on 108 AC8 before S6 lands, or red after it.
- **AC3** — When `check_amended_before_built 115 116 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 115 lands after unit 90's build commit, the earliest build
  that spec 115's corrections reach, as 115 AC17's pair for spec 98 names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, finding
  1 (H1).

## 10. Reuse audit

The seams reused are 115's own `<X of spec N>` slice, which AC4 already pipes, and
TOOL-dWellOiledMachine-98's predicate over `build_commit` (`tools/unattended/lib-unattended.sh:1186`),
loaded from spec 95 rather than copied. No new probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "slice one section of a spec and count a token in it"`
returned lexical neighbours only (`counts` and `slice` in two suites, `read_spec_revisions` in
`design_lib.py`); none slices a spec section for a criterion, so no existing seam fits beyond the
idiom named above. The recall query below ranked this finding's own report and two earlier briefs that
quote an untracked path inside a criterion among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
