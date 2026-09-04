# TOOL-aStagedLane-1 — the pass-order leg grades builds that carry no run-state file

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Extend the `pass-order history` merge-bar leg to builds that never had an unattended run, so a unit
whose build commit predates a conforming spec reds the bar on any build. Today that check covers
unattended builds alone, which means the rule it enforces is unenforced everywhere else.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-pass-order.sh` grades a build whose folder holds no `RUN.md`.
  Its line 25 declares the current exclusion, and that declaration is what this unit removes. The
  per-unit predicate is unchanged: for a unit the build README's generated region carries as CLOSED,
  the commit that built it must have a conforming, non-THIN spec for that id at its first parent.
- **S2** — the commit range for a run-state-free build is derived from the build folder rather than
  from a run's pinned base, because such a build has no pinned base to read. The range start is the
  earliest commit touching `memory/builds/<slug>/`, found with a path-scoped log over that directory
  alone, so the walk is bounded by the folder's own history and not by the repository's.
- **S3** — the liveness assertion gains a fourth count: builds graded with no run-state file. The
  three counts already reported are builds graded, builds skipped by the cutoff, and units
  `unbuilt-in-range`. A widened population that reports no separate count cannot be told from a run
  where the widening did nothing.
- **S4** — the cost ceiling for this leg is re-declared in `tools/unattended/run-unattended-gates.sh`
  against a fresh reading taken after S1 lands, with the reading written beside it. The leg is
  already over its declared ceiling, and enlarging its population without re-declaring turns a
  breach into a permanent one.
- **S5** — `tools/unattended/check-pass-order.test.sh` gains arms for the new population: a
  run-state-free build whose unit was built before its spec must be observed RED, and the same build
  with the spec commit first must be observed green.

## 3. Non-goals (OUT)

- Not closing the self-authored cutoff field. `check-pass-order.sh` reads `opened:` from the working
  tree, so one character disables the leg for that build. This unit inherits that weakness over a
  larger population and carries the fork in section 8 rather than fixing it silently.
- Not changing the per-unit predicate, the first-parent anchor, or the build-commit definition. Each
  was settled by `TOOL-dBriefedPass-3` and re-deciding them here would put two answers in the tree.
- Not grading builds the cutoff excludes. The date gate stays exactly as it is; this unit widens
  which builds the gate can see, never which dates it admits.
- Not touching `--dispatch`. That verb's run-state requirement is correct, because a dispatch
  declares a write set against a run and there is no run to declare it against.

## 4. Design

### Data model

A build is graded when its README parses and its generated units region carries at least one CLOSED
unit. Today a run-state file is an additional requirement; after this unit it is not. The run-state
file, where present, still supplies the pinned base, so unattended builds keep the cheaper range
they have now and nothing about their grading moves.

### The range, for a build with no pinned base

The current walk is anchored on a run's base sha. A run-state-free build has none, so the anchor
becomes the build folder's own first commit. A path-scoped log over `memory/builds/<slug>/` returns
that in one command and bounds the walk to commits that touched the build, which is the same
population the per-unit search already filters down to. The alternative, walking the whole history
per unit, was rejected under Alternatives rejected below.

### Files touched (estimate)

`tools/unattended/check-pass-order.sh`, `tools/unattended/check-pass-order.test.sh`,
`tools/unattended/run-unattended-gates.sh` for the ceiling, and the kit descriptor only if the leg's
guard changes. Four files, one of them a declaration.

### Alternatives rejected

Walking the full commit graph per unit needs no range at all and is the simplest predicate to state.
It is rejected on cost: the leg already costs 134 seconds against a declared 90, recorded by
`TOOL-dSealedTally-2`, and an unscoped per-unit walk multiplies that by the unit count. A check
nobody can afford to run is a check nobody runs.

Grading only builds that opt in through a README field was rejected because an opt-in gate is
satisfied by not opting in, which is the shape this unit exists to remove.

## 5. Production-readiness checklist

- security — N/A. The check reads history and writes nothing.
- perf / scale — the binding concern. See S4 and Alternatives rejected; the population grows by
  every run-state-free build the cutoff admits, and the leg is already over its ceiling.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings beyond gate output.
- error / empty / loading states — a build with no CLOSED unit contributes nothing and must be
  counted as skipped rather than passing silently.
- observability — the fourth liveness count in S3 is the whole of it.
- risks — a widened population may red builds already landed on the default branch. The date cutoff
  is the control, and S1 does not move it.
- testing + left-shift gates — S5, with the red observed before the green.
- migration / rollback — reverting the commit restores the current population exactly; no state is
  written anywhere.
- user docs — none. This is a merge-bar leg, not a user-facing feature.

## 6. Acceptance criteria

- **AC1** — When a fixture build with no `RUN.md` holds a CLOSED unit whose build commit precedes
  its spec commit, `bash tools/unattended/check-pass-order.sh` exits non-zero and names that unit id.
  The RED is observed and recorded before the fix that greens it.
- **AC2** — When the same fixture is re-staged with the spec commit first, `check-pass-order.sh`
  exits 0 and the unit appears in the graded count.
- **AC3** — When `check-pass-order.sh` runs over the real tree, its liveness line reports four
  counts, one of them the run-state-free builds graded, and none of the four is absent.
- **AC4** — When `bash tools/unattended/check-pass-order.test.sh` runs, every arm passes and the
  arm count reported exceeds the count recorded before this unit.
- **AC5** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs, the `pass-order
  history` leg finishes inside its re-declared ceiling, and that ceiling carries the reading it was
  set against on the line beside it.

## 7. Gates

The `pass-order history` leg in `tools/gate-legs.json`, its self-test
`tools/unattended/check-pass-order.test.sh`, the unattended `--checks` runner in
`tools/unattended/run-unattended-gates.sh`, and `python tools/memory-tree/check-arms.py` for the new
branches. The full bar is `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — the cutoff is read from a field the graded build authors.** `check-pass-order.sh` reads
  `opened:` from the working tree, so editing one character in a README exempts that build from the
  leg. It was recorded as a medium finding in the parent build's closing review and is still open.
  This unit multiplies the blast radius by widening the population that field governs.
  Options: read `opened:` from the commit being graded rather than the working tree, which costs one
  extra object read per build; or refuse a build whose working-tree `opened:` disagrees with its
  committed value; or leave it and record the exposure.
  Recommendation: read it from the commit being graded. It is the smaller change, it removes the
  lever entirely, and the extra read is per build rather than per unit.

- **F2 — should a run-state-free build be graded from its folder's first commit, or from the first
  commit carrying any of its unit ids?** The folder anchor is cheaper and is what S2 specifies. The
  id anchor is tighter for a build whose folder was created long before work started.
  Recommendation: the folder anchor, and revisit only if a real build shows the gap.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a build's pass order from commit history without a
run-state file"` returned no seam for this unit. Its top candidates were `run` in
`tools/settings-merge.py` and four `build_*_index` functions, matched on the name stems `run` and
`build`; the corpus it searches is 645 Python symbols and this unit's subject is a shell script, so
the tool cannot see the surface being changed. The real seam was found by reading:
`tools/unattended/check-pass-order.sh` already implements the per-unit predicate, the first-parent
anchor and the liveness line, so this unit changes that script's population and reuses every
judgement inside it. No new script is added.

Recall terms used: `pass-order run-state RUN.md unattended dispatch plan_state spec-before-build
merge-bar cutoff attended build-complete M2`. The query was why the pass-order gate skips builds
with no run-state file; it returned 39 hits, and the two that bind this unit are the working-tree
cutoff finding in the parent build's closing review and the ceiling breach recorded as
`TOOL-dSealedTally-2`.
