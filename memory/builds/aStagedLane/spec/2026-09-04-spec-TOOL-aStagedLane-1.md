# TOOL-aStagedLane-1 — the pass-order leg grades builds that carry no run-state file

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4 |
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md) | spec-audit | TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4 |

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
  **The range INCLUDES that commit.** The walk being reused is `rev-list "$base..HEAD"`, which
  excludes its anchor, so the anchor is taken as `<first>^` — and where `<first>` is a root commit
  with no parent, the walk runs from the root instead. A commit that creates the build folder and
  writes product code for a unit in one act is the violation this widening exists to catch, and an
  exclusive anchor drops exactly it.
- **S2b** — a build whose `RUN.md` exists but yields no usable `base:` — a line that is not
  hex-shaped, or a sha that does not resolve — falls back to the folder anchor of S2 rather than
  being skipped. After S6 closes the `opened:` lever this is the last remaining way for a graded run
  to exempt its own build by committing one bad line, and it would leave a build with a garbage
  `RUN.md` more exempt than a build with none.
- **S2c** — a CLOSED unit in the run-state-free population whose build commit is NOT found inside
  the derived range is searched for ONCE more, in the history strictly before the anchor. **That
  search uses the SAME build-commit predicate as the in-range one, unchanged: a whole-token subject
  match AND a path touched outside the record surface** — the build's own folder, plus
  `GENERATED_INDEXES`, plus `SHARED_RECORDS`, which `.unattended.conf` sets to
  `memory/DECISIONS.md memory/backlog`. Rev-3 wrote only the first half, which would have made the
  probe a false-positive engine: a `backlog(TOOL-xFoo-1): open the row` commit touching only
  `memory/backlog/TOOL.md` ordinarily lands before the build folder exists, and a predicate without
  the exclusion reports it as a violation and reds the bar on a build that did nothing wrong. The
  script's own comment records that dropping this exclusion once "made a CONFORMING run unlandable",
  and §3's second non-goal forbids changing the definition in any case. A hit is a VIOLATION: product
  code naming that unit landed before the build folder existed, so it necessarily landed before any
  spec for it. A miss stays in the `unbuilt-in-range` tally.
- **S2d — the pre-anchor probe is BOUNDED BY CONSTRUCTION, because its cost cannot be measured
  before S1 lands.** Rev-3 bounded it with "5 units across the whole tree", a figure that appears in
  no section of this spec and, worse, measures the wrong population: `unbuilt` is incremented only
  after the `RUN.md` gate, so no reading of it has ever seen a run-state-free build. The three such
  builds inside the cutoff carry 20 CLOSED units whose miss rate is simply unknown, and HEAD is 1969
  commits, so an unbounded pre-anchor walk per miss is not obviously cheap. The probe therefore
  takes a DECLARED commit cap, and what it truncates is COUNTED on the liveness line — a probe that
  gave up must say so rather than reporting a miss as a clean result.
- **S3** — the liveness assertion gains a count for the widened population: builds graded that carry
  no run-state file. The line ALREADY prints four counts — builds graded, builds skipped by the
  cutoff, builds `with no pinned run BASE`, and units `unbuilt-in-range` — while the block comment
  above it at line 246 says "THREE COUNTS"; that comment is stale and is corrected in the same
  commit. **`skipped_norun` is RETIRED, not retained.** Rev-3 kept it and justified it with a
  residual population that does not exist: the counter is incremented at exactly three sites — no
  `RUN.md`, a `base:` that is not hex-shaped, a sha that does not resolve — S1 closes the first and
  S2b routes the other two to the folder anchor, and an absent or unreadable `base:` yields the
  empty string, which is not hex-shaped, so it lands in the second. Every path is closed, and a
  field pinned at zero printed beside four that move is the DEAD PROBE class this leg's own header
  makes load-bearing. After this unit the line prints FIVE: graded, skipped-by-cutoff,
  run-state-free-graded, `unbuilt-in-range`, and the pre-anchor violations S2c finds, plus S2d's
  truncation count where it is non-zero.
- **S4** — the cost ceiling for this leg is re-declared against a fresh reading taken after S1, S2c
  AND S2d have landed — not after S1 alone, since the pre-anchor probe is the part whose cost is
  unmeasured — with the reading written beside it, in BOTH carriers that declare one:
  `tools/unattended/run-unattended-gates.sh` (`BUDGET_pass_order_history`, currently 90) and the
  `pass-order history` row of `tools/gate-legs.json` (currently 900). **The 900 is the one that
  binds the merge bar**; the 90 bounds only the on-demand kit runner, and the comment beside it
  claiming "Matches the ceiling its gate-legs.json row declares — one figure, two readers" was made
  false by `TOOL-dRetiredFork-40`, which raised the manifest row to 900 deliberately so that a leg
  running under the concurrent pool would not be killed at a standalone bound. That comment is
  DELETED rather than corrected, since the two figures answer different questions and the parity it
  asserts should never be restored. The reading behind the current values: the leg costs **463 s on
  node `a`, measured 2026-09-04 under load** with two concurrent builds running, against 134 s
  recorded by `TOOL-dSealedTally-2`. A ceiling is derived from the loaded reading, because a bound
  that fires on normal concurrent execution is worse than no bound.
- **S5** — `tools/unattended/check-pass-order.test.sh` gains arms for the new population: a
  run-state-free build whose unit was built before its spec must be observed RED, and the same build
  with the spec commit first must be observed green.
- **S6** — the grading cutoff is read from the commit being graded rather than from the working
  tree, so editing a build README's `opened:` field in the working copy can no longer exempt that
  build from the leg. The comparison itself is unchanged; only the source of the value moves. This
  costs one object read per build and none per unit.
  **This NARROWS the lever; it does not remove it.** The parent build's closing review names the
  class as "the grading cutoff is read from a field the graded run authors" and records that the
  doctored value survives into a clean clone. The run commits the README, so the COMMITTED value is
  still the run's to choose, and this unit multiplies the population that field governs. What S6
  buys is that the value must be committed to work, which puts it in the diff a reviewer reads. The
  stronger option the parent review prescribes — deriving the date with
  `git log --diff-filter=A -1 --format=%cs -- "$readme"`, or redding on disagreement — is NOT taken
  here, because it re-dates every existing build against its own file-add commit and the cutoff's
  whole purpose is grandfathering; changing what `opened:` MEANS is a separate unit. The residual is
  written into the leg's header, where a gate states what it does not check.

## 3. Non-goals (OUT)

- Not auditing the existing corpus for builds this widening will red. The date cutoff is the
  control and S1 does not move it. A build the widened leg reds is a finding for whoever lands it,
  not a migration this unit performs.
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
`tools/unattended/run-unattended-gates.sh` and `tools/gate-legs.json` for the two ceilings, and the
kit descriptor only if the leg's guard changes. Five files, two of them declarations. `gate-legs.json`
was absent from this list at rev-2, which is how S4 came to name one carrier of a figure that has
two.

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
  every run-state-free build the cutoff admits, and the leg is already over the RUNNER's ceiling at
  463 s against 90, while sitting inside the manifest ceiling of 900 that actually binds the merge
  bar. **S2c's cost is UNMEASURED and is bounded by construction instead**, per S2d. Rev-3 wrote
  "5 across the whole tree"; that figure is in no section of this spec and counts a population the
  `RUN.md` gate structurally excludes, so it says nothing about the builds S1 adds. The three
  run-state-free builds inside the cutoff carry 20 CLOSED units whose miss rate is unknown until S1
  lands, and records-only units — the ordinary `unbuilt` shape — are the class most likely to miss.
- residual lever — the COMMITTED `opened:` value is still authored by the graded run. S6 narrows
  the working-tree edit and does not close the class; the leg's header says so.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings beyond gate output.
- error / empty / loading states — a build with no CLOSED unit contributes nothing and must be
  counted as skipped rather than passing silently.
- observability — S3's liveness line is the whole of it, including the retirement of a counter S1
  and S2b leave with no reachable increment site.
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
- **AC3** — When `bash tools/unattended/check-pass-order.sh` runs over the real tree, its liveness
  line names the run-state-free-graded count explicitly and that count is NON-ZERO, and it no longer
  prints `with no pinned run BASE`. A cardinality is not the criterion: the line already printed four
  counts before any change, so counting fields cannot distinguish a landed unit from an unlanded one.
  Rev-3's "the four counts printed before this unit are all still present" was worse than useless —
  it REQUIRED the retired counter to survive, blessing a field S1 and S2b leave permanently zero.
- **AC11** — When `grep -n 'skipped_norun' tools/unattended/check-pass-order.sh` runs after this
  unit, it returns nothing: the counter is gone rather than pinned at zero. A liveness field with no
  reachable increment site is a dead probe whichever value it prints.
- **AC12** — When a fixture build with no `RUN.md` has a pre-anchor commit that names its unit id and
  touches ONLY a `SHARED_RECORDS` path, `check-pass-order.sh` does NOT report a violation for that
  unit. This is the false-positive arm: the pre-anchor window admits product commits and record
  commits alike, and a predicate without the record-surface exclusion reds a conforming build.
- **AC13** — When a fixture drives the pre-anchor probe into S2d's declared commit cap,
  `bash tools/unattended/check-pass-order.sh` reports the truncation as its own count on the liveness
  line. A probe that gave up and a probe that found nothing print the same thing otherwise.
- **AC4** — When `bash tools/unattended/check-pass-order.test.sh` runs, every arm passes and the
  arm count reported exceeds the count recorded before this unit.
- **AC5** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs AFTER S1, S2c and S2d
  have all landed, the `pass-order history` leg finishes inside its re-declared ceiling; that ceiling
  carries the reading it was set against on the line beside it; and the `pass-order history` row of
  `tools/gate-legs.json` carries a ceiling at least as large, with the stale parity comment gone from
  the runner. The reading is taken after the pre-anchor probe exists, not after S1 alone: S2c is the
  part whose cost nothing has measured.
- **AC7** — When a fixture build has NO `RUN.md`, and a commit writing product code and naming its
  unit id lands BEFORE the commit that creates the build folder, `check-pass-order.sh` exits
  non-zero and names that unit. The unit must NOT appear only in the `unbuilt-in-range` tally: that
  is the count the leg's own header warns must not be read as benign, and letting the most flagrant
  violation land there is the hole this criterion exists to close.
- **AC8** — When a fixture build's violating build commit IS the build folder's own first commit,
  `check-pass-order.sh` exits non-zero. An exclusive range anchor drops exactly this commit, so the
  arm pins the boundary rather than assuming it.
- **AC9** — When a fixture build carries a `RUN.md` whose `base:` line is garbage, that build is
  GRADED through the folder anchor rather than skipped, and a build-before-spec violation inside it
  is still observed RED.
- **AC10** — When a fixture build's COMMITTED `opened:` is back-dated to before the cutoff, the
  build is skipped — and the leg's header states that this remains possible, so the residual is
  declared rather than discovered.
- **AC6** — When a fixture build's committed `opened:` field is inside the cutoff and its
  working-tree copy is edited to a date outside it, `bash tools/unattended/check-pass-order.sh`
  still grades that build. The bypass is observed working before S6 lands and observed refused
  after.

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
  RESOLVED (owner, 2026-09-04): read `opened:` from the commit being graded. In scope as S6, with
  the withdrawn non-goal replaced and AC6 observing the bypass before and after.

- **F2 — should a run-state-free build be graded from its folder's first commit, or from the first
  commit carrying any of its unit ids?** The folder anchor is cheaper and is what S2 specifies. The
  id anchor is tighter for a build whose folder was created long before work started.
  Recommendation: the folder anchor, and revisit only if a real build shows the gap.
  RESOLVED (owner, 2026-09-04): the folder anchor, exactly as S2 already specifies.
  **RE-PUT at rev-3, because neither option disclosed the hole and the ruling rests on that.** The
  spec audit established that BOTH anchors put the flagrant case — product code committed first,
  the build folder and its spec created afterwards — strictly OUTSIDE the range, where the unit
  lands in `unbuilt-in-range` and the leg reports clean. That is the exact violation the widening
  exists to catch, and the owner ruled without it being stated in either option.
  Options, with the residual now stated: keep the folder anchor and let the flagrant case stay
  invisible; walk the full commit graph per unit, which has no hole and is rejected in Alternatives
  for a cost the 463 s reading now makes concrete; or keep the folder anchor and add ONE pre-anchor
  search for the units the range search did not resolve.
  RESOLVED (agent, 2026-09-04, delegated): the third. The full walk fails AC5's ceiling, which is a
  gate already written in this spec, so veto 1 discards it. The remaining pair is not a real choice:
  the third option is the first plus a bounded probe that closes the hole, so it satisfies strictly
  more of the stated acceptance criteria and leaves no follow-up open. In scope as S2c, observed by
  AC7. The RANGE half is settled separately by S2's inclusive anchor and AC8.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-04 · both forks resolved at the owner's scope-approval turn. F1 moved the cutoff
  read into scope as S6, withdrew the non-goal that had deferred it, and added AC6; F2 confirmed S2
  unchanged.
- rev-3 · 2026-09-04 · round-1 spec audit folded: B3, H1, H2, H3, H4, H5. F2 RE-PUT and re-resolved
  under the mandate, because the audit showed neither of its options disclosed that both anchors
  exempt the flagrant case — S2c and AC7 close it. S2 made the range inclusive of the folder's first
  commit (AC8); S2b routes an unusable `RUN.md` base to the folder anchor instead of a silent skip
  (AC9); S3 corrected — the liveness line already printed FOUR, not three, and the stale ":246 THREE
  COUNTS" comment is fixed in the same commit — and AC3 rewritten to name the new count rather than
  count fields, since the old wording was satisfied by the unmodified script; S4 now names BOTH
  ceiling carriers, records which one binds the merge bar, carries the 463 s loaded reading, and
  deletes rather than restores the false "one figure, two readers" parity comment; S6 and F1
  restated as a NARROWING with the parent review's finding cited and the residual routed to the
  leg's header, with AC10 covering the committed back-date that remains possible.
- rev-4 · 2026-09-04 · round-2 spec audit folded: findings 4, 5 and 6 — all three defects the rev-3
  FOLD introduced, not defects rev-2 carried. S2c had specified the pre-anchor probe as a bare
  whole-token id match, dropping the record-surface exclusion the in-range predicate carries: that
  is a false-positive engine on the one path this leg reports a hard violation, and a reproduced
  failure the script's own comment documents. AC12 arms it. S3 had RETAINED `skipped_norun` on a
  residual population that does not exist — S1 and S2b between them close all three of its increment
  sites — so the field would have been pinned at zero forever, and AC3 as written REQUIRED it to
  survive; the counter is retired and AC11 observes the retirement. S2d added because rev-3 bounded
  the probe's cost with "5 units across the whole tree", a figure in no section of this spec that
  counts a population the `RUN.md` gate structurally excludes; the cost is unmeasurable before S1
  lands, so the probe is bounded by construction and its truncations are counted (AC13). AC5's
  reading moves to after S2c and S2d rather than after S1 alone.

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
