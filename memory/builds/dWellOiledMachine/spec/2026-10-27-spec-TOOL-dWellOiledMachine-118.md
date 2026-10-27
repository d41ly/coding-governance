# TOOL-dWellOiledMachine-118 — reverting S6 turns spec 115's AC4 red: its red case names the revert and §4 records the reading that shows it

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 73 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-118-deviation-1181.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-118-deviation-1181.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`),
finding 18, item H1, at HIGH. Item H1 merges findings 1, 9, 18 and 21, and each takes its own unit:
finding 1 is TOOL-dWellOiledMachine-116, finding 9 is TOOL-dWellOiledMachine-117 and finding 21 is
TOOL-dWellOiledMachine-119.

Finding 18 is the blast radius of 115 AC4. No correct build can pass it, and the cheap way to green
its grep is to revert S6, which re-ships the bare pathspec S6 exists to remove. Units 116 and 117
make AC4 passable. This unit closes the revert route: AC4's red case names a reverted S6, and 115 §4
records the reading that shows a reverted S6 reads red, so a builder meeting a red AC4 is pointed
at the build, never at S6.

## 2. Scope (IN)

- **S1** — 115 AC4's red case rewritten. Spec 115 takes a rev bump, its §9 line naming this unit and
  finding 18, whose AC4 red case reads "Red when: AC8 keeps a bare pathspec, which exits 1 even after
  both files are tracked, or S6 is reverted, which leaves no full path in 108 AC8." Observed by AC1,
  AC2.
- **S2** — 115 §4 Evidence gains the line "108 AC8 as committed at 63dbec5e8 counts each full path 0
  times and `error-unmatch supervise.py` once, and a scratch copy with S6 applied counts 1 and 0, so
  a reverted S6 turns AC4 red: no green path through AC4 restores a bare pathspec (finding 18)."
  Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 115 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 115 makes are applied. At this
  unit's own pass, at order 73, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's grep over 108 AC8: finding 1, TOOL-dWellOiledMachine-116.
- AC4's `git ls-files` clause: finding 9, TOOL-dWellOiledMachine-117.
- AC6's walk over bare names: finding 21, TOOL-dWellOiledMachine-119.
- No change to S6's target text beyond what TOOL-dWellOiledMachine-120 quotes.
- No spec-lint leg that runs each criterion over the base text. That is the report's left-shift line,
  a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — AC4's red case and §4 Evidence, which this unit rewrites before spec 115's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 63dbec5e8: `<AC8 of spec 108>`, sliced and flattened as 115's §6
  preamble defines it, counts `tools/runtime/supervise.py` 0 times and `error-unmatch supervise.py`
  once. A scratch copy with 115 S6 and S8 applied counts them 1 and 0, with S6's pathspecs quoted
  or not.
- The finding's appendix row: the grep half of AC4 "prints 1 today, before the unit is built", and
  "the cheap way to make the grep pass is to revert S6".

### The staged revert

AC2 stages the revert without writing a file: it pipes `<AC8 of spec 108>` through a `sed -E` that
puts the bare names back, quoted or not, and counts the full path in what comes out.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 115's rev cell moves)

### Alternatives rejected

- **A non-goal forbidding the revert.** A non-goal binds the unit that states it, and spec 115's
  builder reads 115, not this spec.
- **Stage the revert on a scratch copy of spec 108 on disk.** A pipe observes the same counts and
  leaves nothing to clean up.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — one `sed` and two greps.
- error / empty / loading states — an empty AC8 slice counts 0 and reads red, as a revert does.
- observability — AC2 prints the full-path count before and after the staged revert.
- risks — none beyond 115's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`. Each command runs from the repository root; the
predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC4 of spec 115>` is piped to `grep -c "or S6 is reverted"`, it prints 1, and
  `awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec 115> | tr -s '\n ' ' ' | grep -c "no green path through AC4 restores a bare pathspec"`
  prints 1.
  Red when: AC4's red case is silent on a revert, or the reading that shows it red is not recorded.
- **AC2** — When `<AC8 of spec 108>` is piped to `grep -c "tools/runtime/supervise.py"` at this
  unit's pass, it prints 1; and when it is first piped through
  `sed -E "s#'?tools/runtime/(supervise.py)'? '?tools/memory-tree/(door_fixture.py)'?#\1 \2#"`, the
  same count prints 0.
  Red when: 108 AC8 kept the bare names, or the staged revert still counts a full path.
- **AC3** — When `check_amended_before_built 115 118 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 115 lands after unit 90's build commit, the earliest build
  that spec 115's corrections reach, as 115 AC17's pair for spec 98 names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a piped staged revert or a history probe at this
unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, finding
  18 (H1).

## 10. Reuse audit

The seams reused are 115's own `<X of spec N>` slice and TOOL-dWellOiledMachine-98's predicate over
`build_commit` (`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95 rather than copied.
The staged revert is a pipe, so it mints no fixture.

Probe: `python tools/codebase-map/reuse_lookup.py "slice one section of a spec and count a token in it"`
returned lexical neighbours only (`counts` and `slice` in two suites, `read_spec_revisions` in
`design_lib.py`); none slices a spec section for a criterion, so no existing seam fits beyond the
idiom named above. The recall query below ranked this finding's own report among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
