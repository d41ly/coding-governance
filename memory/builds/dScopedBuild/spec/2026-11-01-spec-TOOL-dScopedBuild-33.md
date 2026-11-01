# TOOL-dScopedBuild-33 — `read_first_passes` stays in `deviation_join.py` as two landed ancestors leave it, and `read_build_base` reaches it by the lazy import the leg already makes

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 2 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-25 TOOL-dScopedBuild-28 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-35 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 30 at HIGH**, report item **H9**. `TOOL-dScopedBuild-1` S1 moves
`read_first_passes` and `read_commit_times` into `routed_commits.py` "as `deviation_join.py:307-340`
holds them at base". TOOL-dFurnishedOrders-60 S13 moves the per-commit rule into a new
`derive_pass_units` in `deviation_join.py`, and TOOL-dDeclaredLoop-37 S2 makes the reader call
`commit_trailers.attribute` in place of its `re.sub`. Both are DEFERRED units of ancestor builds and
land first, and unit 1 names neither. Copying the base body reverts both; moving the post-parent body
leaves `routed_commits.py` depending on `deviation_join`'s module, the reverse of today's lazy import
(`tools/memory-tree/routed_commits.py:347`).

This unit keeps the readers where the ancestors leave them and has the base reader import them
lazily. It repairs `TOOL-dScopedBuild-1` and builds one step after it (order 2).

## 2. Scope (IN)

- **S1** — The readers stay. `read_first_passes`, `read_commit_times` and TOOL-dFurnishedOrders-60
  S13's `derive_pass_units` stay in `tools/memory-tree/deviation_join.py`, their bodies as
  TOOL-dFurnishedOrders-60 S13 and TOOL-dDeclaredLoop-37 S2 leave them; nothing of them is copied
  into `routed_commits.py`. This supersedes unit 1 S1, its move and its two re-pointed call sites;
  `deviation_join.py`'s own callers (`:521`, `:578` at base) are unchanged. Observed by AC1.
- **S2** — The base reader's import. Unit 1 S2's `read_build_base(repo, slug)` in `routed_commits.py`
  reads the first passes as `deviation_join.read_first_passes(...)` and the times as
  `deviation_join.read_commit_times(...)`, importing `deviation_join` inside the function, as
  `check_deviation_join` already does (`routed_commits.py:347`), so no module-level import of it is
  added and the two modules keep today's direction. Observed by AC2.
- **S3** — The ancestors first. TOOL-dFurnishedOrders-60 S13 and TOOL-dDeclaredLoop-37 S2 are
  build-run preconditions. Where either has not landed when this unit builds, the builder re-grounds
  on the landed body and records the difference as a §9 rev of this spec, as TOOL-dTotalRecall-8 §8 F5
  rules for its parents. NOT OBSERVED: it is a sequencing rule, and AC1 observes the bodies it keeps.
- **S4** — Unit 1 answered. Unit 1 AC1's first two clauses, a `^def read_first_passes` count of 0 in
  `deviation_join.py` and 1 in `routed_commits.py`, are superseded by AC1; its third, the
  `pass-revision` plant's exit, stands. Unit 1's acceptance ledger answers AC1 with a note naming
  `TOOL-dScopedBuild-33 S4`. Observed by AC1.

## 3. Non-goals (OUT)

- `derive_pass_units` itself and the `attribute` call: the two ancestors build them.
- `read_build_base`'s rule for the base: unit 1 S2, and the topological reading id 40 asks of it,
  which `TOOL-dScopedBuild-35` S22 takes.
- The left-shift spec-lint rule the report names. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — S1's move, which S1 and S4 supersede, and S2's `read_build_base`, whose import S2 states (id 30)
- **hands-off** `TOOL-dScopedBuild-3` — its precondition `read_first_passes` "in `tools/memory-tree/routed_commits.py`", which stays in `deviation_join.py` and which unit 3 reads through `read_build_base`, the reader S2's lazy import reaches it by (id 30)
- **hands-off** `TOOL-dScopedBuild-15` — §4's sentence that `read_first_passes` "moves beside `read_routed_commits`", which S1 supersedes; S2's default base still comes from `read_build_base` (id 30)
- **consumes-from** external — TOOL-dFurnishedOrders-60 S13's `derive_pass_units` and TOOL-dDeclaredLoop-37 S2's `attribute` call, DEFERRED at base and an ancestor's

## 4. Design

### Evidence

- `tools/memory-tree/deviation_join.py:307-340` at base: `read_commit_times`, `read_ancestors` and
  `read_first_passes`, the last tokenising the trailer and subject with `re.sub`.
- TOOL-dFurnishedOrders-60 S13 (`memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-60.md:152-157`)
  and its §4 sketch: `read_first_passes := oldest commit per unit over derive_pass_units (unchanged
  result)`; its AC12 counts `test_routed_path` in `deviation_join.py`.
- TOOL-dDeclaredLoop-37 S2 (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-37.md:42-47`)
  and its probe `git grep -n 'attribute(.*replace' -- tools/memory-tree/deviation_join.py`; its AC2
  is red if the `re.sub` stays.
- `routed_commits.py:347`: `import deviation_join  # noqa: E402  the join's core, a sibling loaded
  only here`, inside `check_deviation_join`; `deviation_join` imports `routed_commits` at module
  level, so a module-level import back would be a cycle.

### Inventory

Minted: nothing. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 2, one step after unit 1 (order 1), tied with unit 14 and `TOOL-dScopedBuild-32`.
Unit 14 also writes `routed_commits.py`, so M6 sequences the two within the step.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`

### Alternatives rejected

- **Move all three readers into `routed_commits.py`.** It re-points both ancestors' call sites,
  breaks TOOL-dFurnishedOrders-60 AC12's count in `deviation_join.py`, and needs a record that the
  ancestors' shape moved, for no caller this build adds.
- **Copy the base body, unit 1 S1 as written.** It reverts both ancestors.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — unchanged: one import on the first `read_build_base` call.
- error / empty / loading states — unchanged; unit 1 S2's refusals stand.
- observability — unchanged.
- risks — an ancestor not landed at build time, which S3 names.
- testing — AC1 by probe, AC2 through unit 1 AC2's fixture.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -c "^def read_first_passes" tools/memory-tree/deviation_join.py
  tools/memory-tree/routed_commits.py` runs on the built tree it prints 1 for the first file and 0
  for the second, and `git grep -n 'attribute(.*replace' -- tools/memory-tree/deviation_join.py`
  prints at least one line.
  Red when: the reader is defined in `routed_commits.py`, or the ancestor's `attribute` call is gone.
- **AC2** — When `python routed_commits.py --build-base tFix` runs over unit 1 AC2's fixture it prints
  the spec commit's sha and exits 0, and `grep -n "^import deviation_join\|^from deviation_join"
  tools/memory-tree/routed_commits.py` prints nothing.
  Red when: the base is wrong, or the module imports `deviation_join` at its top.
  fixture: unit 1 AC2's, built by `routed_commits.build_fixture`.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 1's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Move the post-parent readers, or import them?** Options: (a) move `derive_pass_units` with
  `read_first_passes` into `routed_commits.py`; (b) keep them in `deviation_join.py` and import them
  lazily. (a) breaks TOOL-dFurnishedOrders-60 AC12 as written and re-points two ancestors' bodies; (b)
  changes no ancestor criterion. RESOLVED (agent, 2026-11-01, delegated): (b), rung 3, the survivor
  with fewer readers moved, tie-broken by reuse of the import seam at `routed_commits.py:347`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 30
  (HIGH, item H9).

## 10. Reuse audit

The seam is the existing lazy import of `deviation_join` inside `check_deviation_join`
(`tools/memory-tree/routed_commits.py:347`), reused by `read_build_base`, and the readers stay where
the ancestors leave them. `python tools/codebase-map/reuse_lookup.py "read each unit's first pass
commit from history"` ranked `read`, `read_text`, `units`, `build_commit` and `read_conf`;
`build_commit` answers one commit per unit inside a known window, the reason unit 1 §4 rejected
`pass_commit`, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "where does read_first_passes live after the parents land" --terms "read_first_passes derive_pass_units deviation_join routed_commits attribute commit_trailers first pass move"`
