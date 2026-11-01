# TOOL-dTendedCadence-58 — the close's version and manifest criteria graded over the build's own non-merge commits, the ones the prepared merge's first parent does not reach

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 18 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
HIGH, item H4. Unit 48 AC9 runs `git diff f4597719..HEAD` over two version carriers at the close
(spec-48:270-272), and AC18 walks every `f4597719..HEAD` commit touching two watched files
(:298-301). The build closes on the prepared merge, into which the minting `--prepare` writes each
owed kit version (`tools/push-main.sh:26-31`), and that merge brings main's commits into the range.
So AC9 shows the minted `KIT_DRIFT_AUDIT_VERSION` line, AC18 walks commits that are no ancestor of
the re-stamp, and both red on every correct build. This unit states the population both criteria
grade: the build's own commits, merges excluded.

## 2. Scope (IN)

- **S1** — The population. The build's own commits are `git rev-list --no-merges HEAD ^<P>`, `<P>`
  the first parent of the prepared merge, which `check_prepared_merge` requires to be the tip the
  remote advertised (`tools/push-main.sh:505-538`), found as that function finds it, `git rev-list
  --first-parent --min-parents=2 --max-count=1 HEAD`. With no prepared merge on `HEAD` the
  population is `git rev-list --no-merges f4597719..HEAD`. The prepared merge is a merge, so its
  minted lines are outside the population; main's commits are reachable from `<P>`, so they are
  outside it too. Observed by AC1 and AC2.
- **S2** — The version criterion, unit 48 AC9 over that population: no commit of it adds a line
  assigning `KIT_DRIFT_AUDIT_VERSION` in `tools/drift-audit/drift_report.py` or
  `KIT_UNATTENDED_VERSION` in `tools/unattended/unattended.sh`. Observed by AC1.
- **S3** — The manifest criterion, unit 48 AC18 over that population: every commit of it touching
  `tools/gate-legs.json` or `skills/session-kickoff/manifest-check.sh` is an ancestor of the commit
  of it moving `last-audit` in `memory/guides/SESSION-KICKOFF.md`. Observed by AC2.

## 3. Non-goals (OUT)

- Which carriers and which watched paths the criteria cover: unit 48 names two of each, and ids 37
  and 34 widen them, TOOL-dTendedCadence-59.
- Minting at the landing: `tools/push-main.sh`, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-48` — AC9 and AC18, whose base-to-HEAD ranges this unit grades over the build's own non-merge commits
- **hands-off** `TOOL-dTendedCadence-59` — the population rule, which that unit's carrier and watch-list criteria grade over

## 4. Design

The two commands, as the close runs them:

```bash
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD)
if [ -n "$t" ]; then own="HEAD ^$t^1"; else own="f4597719..HEAD"; fi
git log --no-merges -p $own -- tools/drift-audit/drift_report.py tools/unattended/unattended.sh \
    | grep -E '^\+KIT_(DRIFT_AUDIT|UNATTENDED)_VERSION'
git rev-list --no-merges $own -- tools/gate-legs.json skills/session-kickoff/manifest-check.sh
```

The second's output feeds `git merge-base --is-ancestor <c> <restamp>` per commit, `<restamp>` the
newest commit of the population touching `memory/guides/SESSION-KICKOFF.md`. A first-parent walk
from `HEAD` would be wrong here: the prepared merge's FIRST parent is main's tip, so that walk reads
main's history and skips the build's.

### Files touched (estimate)

N/A — no file is written; the criteria are observed at the close over the tree's history.

## 5. Acceptance criteria

- **AC1** — When the first command of §4 runs at the close, after the last `--prepare`, it prints
  nothing; on a scratch clone with a prepared-shaped merge, where a branch commit adds
  `KIT_DRIFT_AUDIT_VERSION = "9.9"` it prints that line, and where only the merge or a commit of the
  merge's first parent adds it, it prints nothing.
  Red when: a pass hand-bumps a version the lander mints, or the prepared merge's mint or a main
  commit is graded.
- **AC2** — When the second command of §4 runs at the close and each commit it prints is passed to
  `git merge-base --is-ancestor <c> <restamp>`, each exits 0, and the commits it prints are a subset
  of `git log --no-merges --format=%H $own`, with no commit reachable from `<P>`.
  Red when: a watched file moves after the re-stamp, or a main commit merged by the prepare is
  walked.
  fixture: the close's prepared merge; the scratch-clone halves need a three-commit history and one
  merge.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 18 (HIGH, item H4) of the round-1 spec
  audit of units 35 to 48.

## 9. Reuse audit

The seam is `check_prepared_merge`'s own derivation of the prepared merge from the graph
(`tools/push-main.sh:505-538`), whose first command this unit reuses verbatim. Where it disagrees
with the report: the report's fix walks `--first-parent`, which on a prepared merge reads main, so
this unit excludes `<P>`'s history instead. `python tools/codebase-map/reuse_lookup.py "list a
build's own pass commits excluding merges"` ranked `merge`, `build`, `build_commit`
(`tools/unattended/lib-unattended.sh:1186`, which grades a given range and derives none) and
`build_grammar`; the lander's `--carry` reads what a push would publish through the local default
branch, not a build's own passes, so no existing seam fits beyond the graph walk.

Recall terms used: `python tools/memory-recall/query.py "how is a close criterion kept off the
prepared merge's minted kit versions" --terms "prepared merge mint kit version first-parent no-merges
range close criterion manifest re-stamp"`
