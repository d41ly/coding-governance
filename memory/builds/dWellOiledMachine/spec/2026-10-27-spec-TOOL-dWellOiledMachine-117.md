# TOOL-dWellOiledMachine-117 — spec 115's AC4 asks git for the two files at their repository paths, grounded by a reading from the root

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 73 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-117-deviation-1171.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-117-deviation-1171.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`),
finding 9, item H1, at HIGH. Item H1 merges findings 1, 9, 18 and 21, and each takes its own unit:
finding 1 is TOOL-dWellOiledMachine-116, finding 18 is TOOL-dWellOiledMachine-118 and finding 21 is
TOOL-dWellOiledMachine-119.

Finding 9 is the grounding half of 115 AC4. Its first clause requires
`git ls-files --error-unmatch supervise.py door_fixture.py` to exit 0, but a bare pathspec matches
only a file at the repository root, as 115 S7 and S8 record, and the two files are built at
`tools/runtime/supervise.py` and `tools/memory-tree/door_fixture.py`. The clause exits 1 on every
history, so AC4 can never pass. This unit spells the two repository paths in that clause and records
the probe readings that ground it in 115 §4.

## 2. Scope (IN)

- **S1** — 115 AC4's first clause rewritten. Spec 115 takes a rev bump, its §9 line naming this unit
  and finding 9, whose AC4 opens "When
  `git ls-files --error-unmatch 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`
  runs, it exits 0", that code span on one line, in place of the bare-name clause. The paths are
  quoted so the `spec tokens` paths join skips them while units 90 and 94 have not built the files
  (finding 17, TOOL-dWellOiledMachine-120). Observed by AC1, AC2.
- **S2** — 115 §4 Evidence gains the line "From the repository root at 63dbec5e8,
  `git ls-files --error-unmatch supervise.py door_fixture.py` exits 1 because neither file sits at the
  root, and the same command over `tools/runtime/supervise.py` and `tools/memory-tree/door_fixture.py`
  exits 1 because units 90 and 94 have not built them; AC4 runs after both have (finding 9)."
  Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 115 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 115 makes are applied. At this
  unit's own pass, at order 73, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's grep over 108 AC8: finding 1, TOOL-dWellOiledMachine-116.
- AC4's red case and the reverted-S6 reading: finding 18, TOOL-dWellOiledMachine-118.
- AC6's walk over bare names: finding 21, TOOL-dWellOiledMachine-119.
- The quoting of S6's pathspecs in 108 AC8: finding 17, TOOL-dWellOiledMachine-120.
- No spec-lint leg that runs each criterion from the repository root before promotion. That is the
  report's left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — AC4's first clause and §4 Evidence, which this unit rewrites before spec 115's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 63dbec5e8 from the repository root:
  `git ls-files --error-unmatch supervise.py door_fixture.py` printed "did not match any file(s)" for
  both and exited 1. The quoted full-path form printed the same for both paths and exited 1;
  `tools/runtime/` does not exist yet.
- 90 S20 names `supervise.py --fixture` and `door_fixture.py` as the two fixtures, and 90's Files
  touched and §7 arm lines place them at the two full paths, as 94's Files touched does.
- `NOT_A_TOKEN` (`tools/memory-tree/design_lib.py:525`) matches a word that opens with `'`, and
  `check_path_shaped` in `tools/check-spec-tokens.py` returned `False` for
  `'tools/runtime/supervise.py'` and `True` for the unquoted path in a probe run 2026-10-27.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 115's rev cell moves)

### Alternatives rejected

- **Run the bare pathspec from each file's directory.** AC4 then needs two working directories, and
  115's §6 preamble says every command runs from the repository root.
- **Unquoted full paths.** They read red in the `spec tokens` paths join until units 90 and 94 build
  the files (finding 17).

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — one `git ls-files` call.
- error / empty / loading states — either file absent exits 1 and AC4 reads red.
- observability — `git ls-files --error-unmatch` names each path it cannot match.
- risks — none beyond 115's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`. Each command runs from the repository root; the
predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC4 of spec 115>` is piped to
  `grep -c "error-unmatch 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"`, it
  prints 1, and piped to `grep -c "git ls-files --error-unmatch supervise.py"` it prints 0; and
  `awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec 115> | tr -s '\n ' ' ' | grep -c "neither file sits at the root"`
  prints 1.
  Red when: AC4 still asks git for a bare name, or the reading that grounds the clause is missing.
- **AC2** — When `git ls-files --error-unmatch 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`
  runs at this unit's pass, after units 90 and 94 have built, it exits 0, and
  `git ls-files --error-unmatch supervise.py door_fixture.py` exits 1.
  Red when: the full-path clause cannot pass on a correct build, or a bare pathspec would.
- **AC3** — When `check_amended_before_built 115 117 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 115 lands after unit 90's build commit, the earliest build
  that spec 115's corrections reach, as 115 AC17's pair for spec 98 names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a `git ls-files` probe or a history probe at this
unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, finding
  9 (H1).

## 10. Reuse audit

The seams reused are `git ls-files --error-unmatch`, the liveness probe 108 S8 already chose,
`NOT_A_TOKEN` (`tools/memory-tree/design_lib.py:525`), which makes a quoted word invisible to the
paths join, and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`). No new probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "skip a quoted word when grading a path token in a spec criterion"`
ranked name-stem neighbours only (`skip`, `resolve_prefix_token`, `read_spec_revisions`), so no
existing seam fits beyond the two named above, which reading `tools/check-spec-tokens.py` found. The
recall query below ranked two earlier briefs that tell a writer to quote an untracked path inside a
command among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
