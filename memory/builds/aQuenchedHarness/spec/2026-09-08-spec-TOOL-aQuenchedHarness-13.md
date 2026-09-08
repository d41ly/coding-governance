# TOOL-aQuenchedHarness-13 — the sibling's subject cache, which this leg never had

**Status:** CLOSED · rev-1 · 2026-09-08 · node a · Tier-2 · base d499258d · streams tooling · order 13

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`brief-recorded` costs 1760 s against a 900 s ceiling AT ORIGIN/MAIN'S TIP, with nothing of this
build merged. The default branch is currently un-pushable for every node, and the leg that blocks it
is not failing — it passes, slowly, and the runner kills it. Give it the subject cache its own
`build_commit` says a caller must have.

## 2. Scope (IN)

- **S1** — `check-brief-recorded.sh` builds `_SUBJ` in one `git log --format='%H %s'` over HEAD before
  its grading loops, exactly as `check-pass-order.sh` does, so `build_commit` stops paying a
  `git log -1` plus a `tr` per commit PER UNIT. AC1, AC2.
- **S2** — The port carries the sibling's SIZE ASSERTION unchanged: the cache must hold as many
  commits as `rev-list --count HEAD` reports, or the leg refuses with exit 2. AC3.
- **S3** — `check-brief-recorded.test.sh` arms that refusal, with a fixture guard that asserts the
  break had an EFFECT rather than that the edit was written. AC3, AC4.

## 3. Non-goals (OUT)

- **The ceiling is not re-declared.** 255 s sits under 900 s with margin. `TOOL-aSurfacedLexicon-22`
  already records that the sibling's ceiling stopped measuring the walk and started measuring
  contention once memoised; re-deriving ceilings is that row's work, not this unit's.
- **`build_commit` itself is not touched.** The per-commit `git show --name-only` at its tail runs
  only for commits whose subject already names the unit id, which is a handful. The cost was the
  subject read, which happens for every commit.
- **No other caller is audited for the same absence.** This unit fixes the leg that is blocking the
  branch. Whether a third caller of `build_commit` is also uncached is a question this unit RAISES
  and does not answer.

### Edges

- **consumes-from** `none`
- **hands-off** `none`

## 4. Design

`build_commit` walks `$base..HEAD` once per graded unit and needs each commit's subject. Its own
header states the cache is "not an optimisation you may drop" and prices the sibling at 591 s cached
against 3977-5401 s uncached, "the second of which straddles its own 5400 s ceiling, so the leg stops
being able to answer at all". It further records that the cache was once ORPHANED BY A LIFT — built
by its caller, read by nobody, caught by a 6.7x leg-level regression at the push boundary rather than
by anyone reading the code.

`check-brief-recorded.sh` referenced `_SUBJ` zero times. It never had one. The cost is therefore
O(units x commits) in process spawns, and it grows on two axes at once: each landed unit adds a
walk, and each landed commit lengthens every walk. That is why it crossed its ceiling on a landing
rather than on an edit.

The block is the sibling's, ported rather than re-derived, because two spellings of one predicate are
two answers to one question. Its size assertion is the load-bearing half: a read loop that truncates
leaves a cache answering "no such commit" for every id, so every unit grades unbuilt-in-range and the
leg exits 0 — a silent green. Equality is exact because shas are unique.

### Alternatives rejected

- **Raising the ceiling.** The leg would still be 1760 s and still grow with every landing. This
  repo's own backlog already carries nine ceilings raised instead of fixed.
- **Narrowing the graded population.** It would change the verdict. The cache does not.

### Files touched

`tools/unattended/check-brief-recorded.sh` · `tools/unattended/check-brief-recorded.test.sh`

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path; the cache is read-only over commit subjects.
- perf / scale — this IS the unit. One `git log` over 2352 commits replaces two spawns per commit per
  unit.
- error / empty / loading states — a short cache REFUSES (exit 2) rather than grading; a cache miss
  on a single commit falls back to the pair of processes it replaced, so a partial miss is slow
  rather than wrong.
- observability — the refusal names both counts, so the shortfall is readable from the message.
- risks — the silent-green shape if the assertion were dropped. It is armed, not trusted.
- testing — AC3's arm, with its break staged and observed.
- migration — none.
- user docs — N/A; the leg's own header carries the reasoning.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-brief-recorded.sh` runs on this tree, it completes in
  under its 900 s ceiling. Measured 255 s against 2165 s before. Red when: the cache is built but not
  consulted, which is the orphaning the library's header records — the leg would still pass, slowly,
  and only the clock would say so.
  figure: DERIVED at observation.
- **AC2** — When it runs, its stdout is unchanged from the uncached run on the same tree, by
  `diff` over both captures. Observed byte-identical: 12 closed units graded, same excluded
  surface. Red when: the cache's tokenisation
  differs from the per-commit read, so a subject matches differently and a unit changes verdict.
- **AC3** — When the cache reads short by one commit, the leg REFUSES with exit 2 and names both
  counts. Observed on a staged break: `holds 5 commit(s) where history has 2352`, and in the suite as
  `a truncated subject cache REFUSES`. Red when: the assertion is absent and every unit grades
  unbuilt-in-range at exit 0.
- **AC4** — When the arm's fixture fails to truncate anything, the arm says so rather than asserting
  a refusal that had no reason to happen. `git rev-list --count`. Red when: the guard checks that the
  edit was written instead of that it had an effect — which is how this arm's first two spellings
  both passed their guard while testing nothing.

## 7. Gates

`unattended kit gate` · `brief-recorded` · `harness arms (fail branches armed or pinned)` · `bash tools/run-gates/run-gates.sh`

New arm: `tools/unattended/check-brief-recorded.test.sh` · stages a one-commit truncation of the
cache pipeline and asserts the refusal · no floor to move.

## 8. Open questions

None blocking. One raised and not answered: whether any other caller of `build_commit` is also
uncached. This unit fixed the one that was blocking the branch, and the question is worth a grep
rather than a unit.

## 9. Revision log

- rev-1 · 2026-09-08 · built. Found while landing unit 10: the push was refused by a red gate, and
  the red was not this build's. Timed at origin/main's tip to prove it — 1760 s there against 2165 s
  with this build merged, both over a 900 s ceiling. The arm needed two corrections before it tested
  anything: a `sed` whose `&` made `head` an argument to `git log`, and a `head -5` against a fixture
  history shorter than five. Each was caught by a fixture guard rather than by review, and the second
  is why the guard now asserts the break's EFFECT.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` was not the probe; memory-recall was, and it named the seam
exactly: `TOOL-aSurfacedLexicon-22` records that `pass-order history` was memoised on `main` with
"one pass over history into a subject cache, replacing two process spawns per commit walked over
roughly 35000 spawns", landing it at 267 s standalone. That is this fix, on the sibling leg, already
proven. The block is COPIED from `check-pass-order.sh` rather than re-derived, including its size
assertion, because a predicate spelled twice is two answers to one question — and the shared
consumer, `build_commit` in `lib-unattended.sh`, already reads `_SUBJ` when a caller provides one, so
no library change is needed. The seam fits exactly and was extended rather than duplicated.

Recall terms used: subject cache build_commit rev-list per-commit spawn walk size assertion
unbuilt-in-range pass-order brief-recorded ceiling.
