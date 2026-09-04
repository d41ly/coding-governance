# DEPL-dSealedTally-5 — the govkit self-test grades the tree, not the commit's ref-reachability

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-1 · base 0f19429a · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`python tools/govkit/selftest.py` red 46 arms on a `--no-ff` merge commit made on a detached head,
and passed all 1074 over the byte-identical tree on a branch. The suite drives `update`, whose
`--to` defaults to `HEAD`, and `demand_published_vintage` refuses a commit no ref contains. Make the
suite's verdict a function of the tree it grades.

## 2. Scope (IN)

- **S1** The suite pins the gov vintage it hands `update` to a REF-REACHABLE commit rather than
  letting it default to `HEAD`, so a detached head is no longer a refusal.
- **S2** The pin is DERIVED, not spelled: the suite asks git which ref-reachable commit describes
  the tree under test, and REFUSES with a named reason if it cannot find one, rather than falling
  back to a default that would reintroduce the coupling.
- **S3** A liveness assertion: an arm proving the pin actually took effect, so a run where the
  derivation silently returned `HEAD` is distinguishable from one where it worked.
- **S4** `demand_published_vintage` itself is unchanged. It is a correct guard and the bug is that
  the suite hands it an argument the suite chose.

## 3. Non-goals (OUT)

- Not relaxing `demand_published_vintage`. Refusing a vintage no ref names is what stops a branch
  nobody shipped becoming an adopter's baseline, and weakening it to make a test pass would be the
  test dictating the product.
- Not making the `govkit selftest` leg skip on a detached head. A skip that looks like a pass is
  the class this repo gates against; the suite should RUN and grade the tree.
- Not auditing other legs for the same coupling. Empirically only this one red at the merge commit,
  and a sweep is a separate unit if one is wanted.

## 4. Design

### Data model

A module-level resolution in `tools/govkit/selftest.py`: ask `git for-each-ref --contains HEAD
--count=1` for a ref that already contains the working commit, and use `HEAD` when one exists. When
none does — the detached-merge case — walk to the first ancestor that IS ref-reachable via
`git rev-list --max-count=1 HEAD --not --branches --remotes` inverted, or more simply take
`git rev-parse HEAD^{commit}`'s nearest described ancestor. The value is passed to every `update`
invocation as an explicit `--to`.

The REFUSAL matters more than the happy path: if no ref-reachable ancestor exists at all, the suite
prints a named refusal saying the tree cannot be graded here and why, rather than proceeding.

### Files touched (estimate)

`tools/govkit/selftest.py` (~50 lines: the resolution, its refusal, the `--to` threading through the
`update` helper, and the liveness arm).

### Alternatives rejected

Creating a temporary ref pointing at `HEAD` for the duration of the suite. Rejected: it mutates the
repository the suite is grading, and a crashed run leaves the ref behind. Deriving an existing
ancestor reads and writes nothing.

## 5. Production-readiness checklist

- security — N/A — a test harness change; the guard it stops tripping is untouched.
- perf / scale — one `for-each-ref` per suite run, not per arm.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a repository with no refs at all is the refusal case, named.
- observability — the suite prints which vintage it pinned, so a reader can tell a pinned run from
  an unpinned one without reading the code.
- risks — the derivation could silently pick a WRONG ancestor, grading an older tree. S3's liveness
  arm exists for exactly that, and the printed vintage makes it visible.
- testing + left-shift gates — the liveness arm; and the real regression test is that the suite now
  passes on a detached head, which is checkable directly.
- migration / rollback — reverting the commit is the rollback.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/selftest.py` runs on a detached `--no-ff` merge commit whose
  tree matches a branch tip, it exits 0, where at base `0f19429a` it exits 1 with 46 failing arms.
- **AC2** — When `python tools/govkit/selftest.py` runs on that same tree checked out as a branch, it still exits 0 with an arm
  count strictly greater than the 1074 at base, so the fix adds coverage rather than removing arms.
- **AC3** — When the suite starts, it prints the gov vintage it pinned and whether that vintage is
  `HEAD` or a derived ancestor, observable in `tools/govkit/selftest.py`'s own stdout.
- **AC4** — When no ref-reachable commit can be derived, the suite prints a named refusal and exits
  non-zero rather than silently defaulting to `HEAD`, proved by an arm in
  `tools/govkit/selftest.py` driving the resolution against a fixture repository with no refs.

## 7. Gates

`govkit selftest` · `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1 GATE_SELFTESTS=1`, run
once from a detached merge commit as AC1's own observation.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The 92/93 and 1074/1074 figures are from `dRatifiedSeam`'s
  own landing, recorded in its closing diff review.

## 10. Reuse audit

No existing seam fits — the evidence is that `tools/govkit/selftest.py` has no vintage-resolution
layer at all today: every `update` invocation in it relies on the `--to HEAD` default, which is the
coupling being removed. `reuse_lookup.py` returned no candidate in the self-test's own harness
layer, and `demand_published_vintage` is the guard rather than a seam to extend.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
