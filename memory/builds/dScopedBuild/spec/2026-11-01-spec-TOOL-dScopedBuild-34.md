# TOOL-dScopedBuild-34 — `derive_kit_dir` reduces a file directly under `tools/` or `skills/` to itself, never to the whole root

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 5 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-34-deviation-341.md](../build/2026-11-01-build-TOOL-dScopedBuild-34-deviation-341.md) | deviation | — |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 36 at HIGH**, report item **H10**. `TOOL-dScopedBuild-3` S1's `derive_kit_dir`
names the `tools/<kit>/` and `skills/<skill>/` shapes and a root file, and its fall-through, "any
other path holding a `/` to its first segment", reduces a file directly under `tools/`, such as
`tools/gate-legs.json`, to `tools/`. AC1's four inputs include no such file. 40 tracked files sit
directly under `tools/`, and units 12 and 13 both declare `tools/gate-legs.json`, so any unit that
adds a leg gets the whole of `tools/` as its scope: the scope arm passes strays it never checked,
unit 5's lease admits every `tools/` write as `inside`, and unit 8's claim arm reads every key as held.

This unit makes such a file reduce to itself, tests the reduction over every path shape the tree
holds, and adds the scope-arm case. It repairs `TOOL-dScopedBuild-3` and builds one step after it
(order 5).

## 2. Scope (IN)

- **S1** — The rule, first match wins: a path under `tools/<kit>/` reduces to `tools/<kit>/`; under
  `skills/<skill>/` to `skills/<skill>/`; a file directly under `tools/` or `skills/` to itself; any
  other path holding a `/` to its first segment with a trailing `/`; a root file to itself. The third
  row is new and supersedes unit 3 S1's fall-through for those two roots; `design_lib.py --kit-dir`
  prints it as it prints the others. Observed by AC1 and AC2.
- **S2** — The class over the tree. The rule never reduces a tracked path to `tools/` or `skills/`:
  `derive_kit_dir` over every path `git ls-files` lists yields neither. Observed by AC2.
- **S3** — The scope arm's case. A unit whose spec declares `tools/gate-legs.json` and whose commit
  writes `tools/beta/b` lists `tools/beta/b` as `stray`, and under `refuse` the leg exits 1. This adds
  a case to unit 3 AC2's fixture and changes none of its others. Observed by AC3.

## 3. Non-goals (OUT)

- The consumers of the reduction, unit 5's lease and unit 8's claim arm, which call the function and
  read the fixed answer with no change of their own.
- The overlap probe of TOOL-dPlacedRequest-1 S9, whose rule has the same gap; unit 3 §8 F5's ask
  (TOOL-dScopedBuild-20) points it at this function.
- The left-shift fixture "drawn from `git ls-files` at each depth", which S2 is.

### Edges

- **consumes-from** `TOOL-dScopedBuild-3` — S1's `derive_kit_dir`, whose fall-through S1 narrows, AC1's inputs, and AC2's scope-arm fixture, which S3 extends (id 36)
- **hands-off** `TOOL-dScopedBuild-38` — S1's rule and S2's class over the tree, which that unit restates over `ROUTED_PATHS` (id 26)

## 4. Design

### Evidence

- Unit 3 S1 (`memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-3.md:57-63`) and its
  source rule, TOOL-dPlacedRequest-1 §4 "The overlap reduction"
  (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md:258-260`).
- `git ls-files tools | awk -F/ 'NF==2' | wc -l` printed 40 and the same over `skills` printed 0 at
  `c891f007`, PINNED on 2026-11-01; S2 re-derives the population at observation time.
- Units 12 and 13 name `tools/gate-legs.json` under Files touched, and unit 13 also
  `tools/check-spec-tokens.py`, both files directly under `tools/`.

### The rule, after this unit

| Path | Reduces to |
|---|---|
| `tools/memory-tree/routed_commits.py` | `tools/memory-tree/` |
| `skills/session-kickoff/SKILL.md` | `skills/session-kickoff/` |
| `tools/gate-legs.json` | `tools/gate-legs.json` |
| `.githooks/pre-push` | `.githooks/` |
| `WIRE-INTO-PROJECT.md` | `WIRE-INTO-PROJECT.md` |

### Inventory

Minted: nothing. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 5, one step after unit 3 (order 4), tied with unit 9. Both write
`tools/memory-tree/routed_commits.py`, so M6 sequences them within the step; units 8 (order 6) and 5
(order 7) read the fixed rule.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/routed_commits.py`: the selftest case of S3

### Alternatives rejected

- **Reduce a `tools/` root file to `tools/` and accept the breadth.** It is the defect: one leg file
  declared gives a unit every kit.
- **Reduce every path to itself.** Two files of one kit would no longer overlap, which is what the
  reduction exists for.

## 5. Production-readiness checklist

- security — narrows a write set: a unit declaring a root file of `tools/` no longer covers a kit.
- perf / scale — one more prefix test per path.
- error / empty / loading states — unchanged from unit 3 S1; the new row adds no input it refuses.
- observability — `--kit-dir` prints each reduction.
- risks — a unit that relied on the broad reduction now lists strays it always had; AC3 is that case.
- testing — AC1 and AC2 by probe, AC3 in the routed-commits selftest.
- migration — none.
- user docs — none under `help/`; unit 3's `help/build-scope.md` describes the write set without the
  reduction's rows.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/design_lib.py --kit-dir tools/gate-legs.json
  tools/memory-tree/routed_commits.py skills/session-kickoff/SKILL.md .githooks/pre-push
  WIRE-INTO-PROJECT.md` runs, it prints `tools/gate-legs.json`, `tools/memory-tree/`,
  `skills/session-kickoff/`, `.githooks/` and `WIRE-INTO-PROJECT.md`, one per line.
  Red when: `tools/gate-legs.json` reduces to `tools/`.
- **AC2** — When `python -c` runs `design_lib.derive_kit_dir` over every path `git ls-files` prints in
  this tree, no result equals `tools/` or `skills/`.
  Red when: any tracked path reduces to a whole root.
  figure: DERIVED at observation; 40 files sit directly under `tools/` at `c891f007`.
- **AC3** — When unit 3 AC2's fixture holds a spec for `TOOL-tFix-1` declaring `tools/gate-legs.json`
  and a commit naming it writes `tools/beta/b`, `check_routed_commits` under `refuse` exits 1 and the
  `stray` line names `tools/beta/b`.
  Red when: the declared root file admits a kit's path.
  fixture: unit 3 AC2's, built by `routed_commits.build_fixture`.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC3 · the scope fixture with a declared `tools/gate-legs.json` and a stray kit path, staged by restoring the first-segment fall-through · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 3's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 36
  (HIGH, item H10).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-38,
  the promotions of the round-1 spec audit of units 25 to 35 (id 26).

## 10. Reuse audit

The seam is unit 3 S1's `derive_kit_dir` in `tools/memory-tree/design_lib.py`, the one written form of
the kit-directory rule, narrowed by one row. `python tools/codebase-map/reuse_lookup.py "reduce a path
to its kit directory"` ranked `resolve_kit_dir`, `kit_rel`, `kit_dir`, `build_spec_path_re` and
`resolve_charter_path`; each resolves an install's kit or a charter path and none reduces an
arbitrary path, so no other seam fits. The recall probe returned TOOL-dScopedBuild-20, the ask that
points TOOL-dPlacedRequest-1 S9 at this function.

Recall terms used: `python tools/memory-recall/query.py "how is a path reduced to its kit directory for overlap" --terms "kit-dirs derive_kit_dir overlap reduction tools kit skills first segment root file write set"`
