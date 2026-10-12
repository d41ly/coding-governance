# TOOL-aPrimedIndex-8 — the lander's review minors, batched, and the fixture that names a unit

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 4 · closes TOOL-aPrimedIndex-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPrimedIndex-8-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPrimedIndex-8-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md) | journal | DEPL-aPrimedIndex-1 TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 |

<!-- /gen:spec-records -->

## 1. Goal

Close the MEDIUM and LOW findings of closing review round 1 that land in the lander and its suite
(M3, M8, M9, and L2's arms). Adopt the inherited arm-26 red filed as TOOL-aPrimedIndex-5 in the same
pass: its cure is the mechanism L2 needs, a fixture that defines the unit a commit names.

## 2. Scope (IN)

- **S1** (M3) — Both lander paths snapshot the untracked files before the regeneration runs, and on
  its failure clean every untracked file it created, after the existing reset, so the tree is as the
  lander found it. Observed by AC1.
- **S2** (M8) — The attended refusal for a failed regeneration gets an arm, arm 32, asserting its
  whole text, and the commit-failure refusal beside it is pinned in
  `memory/project/unarmed-branches.txt` as its mint twin is, so the harness-arms leg passes.
  Observed by AC2.
- **S3** (M9) — Arm 25's fixture lands a tree without the run-gates kit's regeneration verb as well,
  so its lexicon and govkit skips are reached again. Observed by AC3.
- **S4** (L2, TOOL-aPrimedIndex-5) — A fixture helper writes a spec defining the unit a fixture
  commit names. Arm 29 asserts the regen commit's whole subject, ` for <unit>` included, and arm 26
  asserts the mint commit's. Observed by AC4.

## 3. Non-goals (OUT)

- The attended failure path is not reset to its pre-attempt sha: it keeps the reconcile merge and the
  mint commit, as the mint refusal already does; TOOL-aPrimedIndex-7 corrects the README's claim.
- No change to `regen.py`; its findings are TOOL-aPrimedIndex-7's.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-4` — the lander paths and arms being repaired.

## 4. Design

### The cleanup

Each caller captures `git ls-files --others --exclude-standard -z` before `run_regen`. On failure,
after its reset, it removes every path in the new listing that the first did not hold, NUL-safe, with
`git clean -f -q --`. Both callers start from a tree they refused to touch while dirty, so every path
removed is one the regeneration wrote.

### Inventory

One new shell function in `tools/push-main.sh`, `remove_new_untracked` (verb `remove`), and one in
`tools/push-main.test.sh`, `write_unit_spec` (verb `write`).

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `memory/project/unarmed-branches.txt`
- `memory/builds/aPrimedIndex/BACKLOG.md`
- `memory/map/generated/symbols.json`

## 5. Production-readiness checklist

- security: the cleanup removes only paths absent from the snapshot taken on a tree the lander had
  just required clean.
- perf / scale: two `ls-files` calls per failed regeneration.
- error / empty / loading states: an empty difference removes nothing.
- observability: unchanged refusal lines; arm 32 pins the attended one.
- risks: a file another process creates during the regeneration would be removed; the lander already
  refuses to share its tree.
- testing: arms 25, 26, 29, 30 and 32, run as slices against the base lander and the built one.
- migration: none.
- user docs: N/A — the README correction is TOOL-aPrimedIndex-7's.

## 6. Acceptance criteria

- **AC1** — When arm 30's failing `regen.py` first writes an untracked file and then exits 1,
  `--prepare` refuses and `git status --porcelain` is empty afterwards. Red when: the file survives,
  as it does with the cleanup removed.
- **AC2** — When arm 32 runs the attended landing over a `regen.py` that exits 1, the output carries
  the lander's whole regeneration refusal, which ends `Aborted (no push).`, and the remote's main does not move; `check-arms.py --check` then exits 0. Red when:
  either refusal site is neither armed nor pinned.
- **AC3** — When arm 25 runs as a slice, it prints its `ok` line with both skips named. Red when:
  the regeneration refuses before the merge-loss check's lexicon skip.
- **AC4** — When arms 26 and 29 run as slices over fixtures that define their units, arm 26 sees
  `for TOOL-tFix-26` on the mint subject and arm 29 sees the regen subject end in its unit. Red when:
  either subject lacks its unit.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `push-main self-test` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/push-main.test.sh · covers AC1 AC2 AC3 AC4 · a littering failing regen.py, an attended failing regen.py, arm 25's fixture, and fixtures with and without a unit spec · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from closing review round 1's lander minors.

## 10. Reuse audit

The cleanup extends the lander's existing failure paths in `tools/push-main.sh`, and the pin mirrors
rows 107-108 of `memory/project/unarmed-branches.txt`. The unit-naming reader is `read_newest_unit` in
`tools/memory-tree/routed_commits.py`; the fixture satisfies its spec-at-HEAD rule rather than
changing it. `reuse_lookup.py` returned no lander helper for snapshotting untracked files.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
