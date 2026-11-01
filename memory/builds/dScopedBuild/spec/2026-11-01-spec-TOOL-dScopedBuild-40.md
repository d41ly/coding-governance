# TOOL-dScopedBuild-40 — `derive_kit_dir` never reduces a path to a directory that holds a routed entry, so a nested routed root stays out of an unrouted sibling's write set

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 7 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-41 |
| [2026-11-01-prompt-TOOL-dScopedBuild-40-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-40-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md) | research | TOOL-dScopedBuild-39 TOOL-dScopedBuild-41 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 39
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**, report item **H1**. `TOOL-dScopedBuild-38` S1's fall-through
reduces any unrouted path holding a `/` to its first segment. Where a `ROUTED_PATHS` entry is nested
(`packages/core/`) or is a file under an unrouted directory (`docs/api.md`), that first segment
covers the entry. With entries `["packages/core/"]`, `packages/README.md` reduces to `packages/`, and
`design_lib.check_guard_trips("packages/core/main.py", "packages/")` is True. So one declared sibling
file hands a unit the nested routed root: the scope arm passes its strays, unit 5's lease admits its
writes, and unit 8's claim arm reads its keys as held. Unit 38 S3 and AC2 check only that no result
EQUALS a directory entry, so they cannot see it.

This unit adds one guard to the rule and states its class as "covers no entry". It repairs
`TOOL-dScopedBuild-38` and builds one step after it (order 7).

## 2. Scope (IN)

- **S1** — The guard. After unit 38 S1's rule picks a candidate, a candidate that ends `/` and
  differs from the path is kept only when no entry of `entries` equals it or starts with it.
  Otherwise the path reduces to itself. The guard applies to both directory candidates: the
  fall-through's first segment and a routed path's `<entry><sub>/`. With entries `["packages/core/"]`,
  `packages/README.md` reduces to `packages/README.md`. With `["docs/api.md"]`, `docs/README` reduces
  to `docs/README`. With `["src/", "src/core/"]`, `src/core/x.py` reduces to `src/core/x.py`. This
  supersedes unit 38 S1's unguarded fall-through. Its other clauses stand, and so does every row of
  its §4 table. Observed by AC1.
- **S2** — The class. Over a population of paths and its entries, no result `r` that ends `/` has an
  entry equal to `r` or starting with `r`. This supersedes unit 38 S3's "yields no directory entry"
  and its AC2's "no result equals a `ROUTED_PATHS` entry ending `/`". Observed by AC2.
- **S3** — The fixture. In a routed-commits fixture whose `ROUTED_PATHS` is `src/app/`, a spec for
  `TOOL-tFix-1` declares `src/README`. A commit naming it writes `src/README` and `src/app/x`, and
  `src/app/x` is listed `stray`. Under `refuse` the leg exits 1. Observed by AC3.
- **S4** — Unit 38 answered. Unit 38's acceptance ledger answers its AC2 with a note naming
  `TOOL-dScopedBuild-40 S2`. Observed by AC2.

## 3. Non-goals (OUT)

- A longest-match pick of the entry. The guard makes no result cover an entry. §4 "Alternatives
  rejected" says what a longest match would change.
- Refusing nested entries in `routed_commits.check_conf`. Its validation is not this unit's, and a
  nested entry is a legal adopter config.
- The left-shift checklist entry the report names. No clause of this build names it.
- Rewording unit 38. Each clause is superseded by name.

### Edges

- **consumes-from** `TOOL-dScopedBuild-38` — S1's rule, S3's class and AC2, which S1 guards and S2 restates as covering no entry (id 24)
- **hands-off** `TOOL-dScopedBuild-41` — S1's guard, which closes the nested-entry case that unit's S13 observes (id 4)

## 4. Design

### Evidence

- `routed_commits.py:181-186`: `test_routed_path` returns the first entry the path equals or lies
  under, in declared order.
- `routed_commits.py:138-170`: `check_conf` refuses absolute, climbing, memory-covering and untracked
  entries. It refuses no nested entry.
- `design_lib.py:589-598`: `check_guard_trips` trips a guard under a declared directory, so a write
  set holding `packages/` admits `packages/core/main.py`.
- A probe of unit 38 S1's rule and this guard over the 9775 paths `git ls-files` printed at
  `62d7511a`, with this tree's entries, gave 0 differing reductions and 0 covering results under
  either rule. PINNED on 2026-11-01. The same probe gave `packages/`, `docs/` and `src/` under unit 38
  for the three planted shapes in S1, and each path itself under the guard.

### The rule, after this unit

```
derive_kit_dir(path, entries):
    r = unit 38 S1's reduction of path
    if r != path and r ends "/" and any(e == r or e.startswith(r) for e in entries):
        return path
    return r
```

| Entries | Path | Unit 38 | After this unit |
|---|---|---|---|
| `packages/core/` | `packages/README.md` | `packages/` | `packages/README.md` |
| `docs/api.md` | `docs/README` | `docs/` | `docs/README` |
| `src/app/` | `src/README` | `src/` | `src/README` |
| `src/ src/core/` | `src/core/x.py` | `src/core/` | `src/core/x.py` |
| `src/ lib/` | `src/pkg/x.py` | `src/pkg/` | `src/pkg/` |

### Inventory

Minted: nothing. `derive_kit_dir` is unit 3's, as unit 38 widens it. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 7, one step after unit 38 (order 6). It ties with units 5 and 36 at order 7. Both
write `tools/memory-tree/routed_commits.py`, so BUILD-METHOD M6 sequences all three within the step.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: the guard in `derive_kit_dir`
- `tools/memory-tree/routed_commits.py`: the selftest case of S3

### Alternatives rejected

- **Guard only the fall-through, as the report's fix words it.** A routed path's `<entry><sub>/`
  covers a nested entry the same way. With `src/ src/core/`, `src/core/x.py` would still reduce to
  the whole `src/core/` root, so S2's class would not hold.
- **Pick the longest matching entry as well.** It changes only the grain under a nested entry:
  `src/core/sub/y.py` would reduce to `src/core/sub/` rather than to itself. A narrower write set
  lists a stray, which `refuse` and `warn-and-ask` report, and it never admits a write. Nothing in
  this tree declares a nested entry.

## 5. Production-readiness checklist

- security — narrows a write set: a declared unrouted file no longer covers a routed root beneath
  its parent.
- perf / scale — one prefix test per entry for each directory candidate.
- error / empty / loading states — unchanged; a blank or invalid `ROUTED_PATHS` stays `check_conf`'s
  `Refusal`.
- observability — `--kit-dir` prints each reduction, the guarded ones included.
- risks — under a nested entry a declared file reduces to itself, so a sibling write lists as stray.
  §4 "Alternatives rejected" weighs it.
- testing — AC1 and AC2 by probe, AC3 in the routed-commits selftest.
- migration — none.
- user docs — none under `help/`; unit 3's `help/build-scope.md` describes the write set without the
  reduction's rows.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `design_lib.derive_kit_dir` on four planted fixture paths, each
  returns its own path: the file `README.md` under `packages/` with `["packages/core/"]`;
  `docs/README` with one entry, the file `api.md` under `docs/`; `src/README` with `["src/app/"]`;
  and the file `x.py` under `src/core/` with `["src/", "src/core/"]`. On `src/main`, `src/pkg/x`
  and `lib/y` with `["src/", "lib/"]` it returns `src/main`, `src/pkg/` and `lib/y`.
  Red when: an unrouted parent's first segment, or a routed `<entry><sub>/`, covers an entry.
- **AC2** — When `python -c` runs `design_lib.derive_kit_dir` over every path `git ls-files` prints,
  with `routed_commits.check_conf`'s entries for this tree, and over the four planted pairs of AC1,
  no result `r` ending `/` has an entry equal to `r` or starting with `r`.
  Red when: the planted pairs run under unit 38 S1's unguarded rule, which yields `packages/`.
  figure: DERIVED at observation; 0 covering results over this tree at `62d7511a` under either rule.
- **AC3** — When the routed-commits fixture sets `ROUTED_PATHS` to `src/app/` by `set_fixture_conf`,
  a spec for `TOOL-tFix-1` declares `src/README`, and a commit naming it writes `src/README` and
  `src/app/x`, `check_routed_commits` under `refuse` exits 1 and the `stray` line names `src/app/x`.
  Red when: the declared sibling admits the nested `src/app/` root.
  fixture: built by `routed_commits.build_fixture`, as unit 38 AC3's is.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC3 · the `src/app/` fixture with a declared `src/README` and a stray `src/app/x`, staged by removing the guard so the fall-through returns `src/` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 38's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 36 to 39, id 24
  (HIGH, item H1).

## 10. Reuse audit

The seam is unit 38 S1's `derive_kit_dir(path, entries)`, guarded in place rather than restated, and
`routed_commits.test_routed_path` (`tools/memory-tree/routed_commits.py:181`) stays its matching
rule. `python tools/codebase-map/reuse_lookup.py "reduce an unrouted path to a directory that holds
no routed root entry"` ranked `repo_root`, `map_root`, `resolve_memory_root` and `resolve_entry`.
None is a path reduction, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does the kit directory reduction treat a nested routed root under an unrouted parent" --terms "derive_kit_dir ROUTED_PATHS fall-through first segment nested entry covers routed root stray write set"`
