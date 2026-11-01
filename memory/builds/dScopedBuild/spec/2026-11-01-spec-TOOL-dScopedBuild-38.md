# TOOL-dScopedBuild-38 — `derive_kit_dir` reduces over the routed roots `ROUTED_PATHS` declares, so an adopter's `src/` file is never its whole root

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 6 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-37 TOOL-dScopedBuild-36 TOOL-dScopedBuild-39 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 25 to 35
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`)
confirmed finding **id 26 at HIGH**, report item **H3**. `TOOL-dScopedBuild-34` S1 hard-codes `tools/`
and `skills/`, and its fall-through still reduces any other path holding a `/` to its first segment.
`derive_kit_dir` ships in the memory-tree kit, and the kit's conf example ships
`ROUTED_PATHS="src/ lib/"` (`tools/memory-tree/.memory-tree.conf.example:487`). In an adopter laid
out under `src/`, `src/main.py` and `src/pkg/x.py` both reduce to `src/`, so one declared file gives a
unit the whole product root: the scope arm passes every stray, unit 5's lease admits every write as
`inside`, and unit 8's claim arm reads every key as held. Unit 34 AC2 tests only this tree.

This unit states the rule over the routed entries the tree declares, passes them to every caller,
and adds a fixture from the shipped conf example's shape. It repairs `TOOL-dScopedBuild-34` and
builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — The rule, `derive_kit_dir(path, entries)` in `tools/memory-tree/design_lib.py`, `entries`
  the routed entries `routed_commits.check_conf` returns, in their declared order. The entry the path
  lies under is `routed_commits.test_routed_path(path, entries)` (`routed_commits.py:181`), imported
  inside the function, so the matching rule is the leg's own. Then, first match wins: a path equal to
  a file entry reduces to itself; a path directly under a directory entry `<entry>` reduces to itself;
  a path under `<entry><sub>/` reduces to `<entry><sub>/`; any other path holding a `/` reduces to its
  first segment with a trailing `/`; a root file reduces to itself. With this tree's
  `ROUTED_PATHS="tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md"`
  (`.memory-tree.conf:9`) it gives unit 34's table unchanged, so `tools/` and `skills/` are this
  tree's instances of the rule. This supersedes unit 34 S1's hard-coded roots and unit 3 S1's
  one-argument signature. Observed by AC1 and AC2.
- **S2** — The callers pass the entries. Unit 3 S2's `read_unit_writes` gains a fifth parameter,
  `read_unit_writes(unit, spec_text, run_rows, tracked, entries)`, and reduces each kept path with
  them; `check_build_scope` and unit 9's touch join pass the `entries` `check_routed_commits` already
  holds (`routed_commits.py:250`). `python design_lib.py --kit-dir <path>...` reads them through
  `check_conf(load_conf(root), tracked)` at the repo root and exits 2 naming the key on its
  `Refusal`. Observed by AC1 and AC3.
- **S3** — The class over the tree. `derive_kit_dir` over every path `git ls-files` lists, with this
  tree's entries, yields no directory entry of `ROUTED_PATHS`. This supersedes unit 34 S2's two
  literal roots. Observed by AC2.
- **S4** — The adopter's shape. In a routed-commits fixture whose `ROUTED_PATHS` is `src/`,
  `set_fixture_conf`'s default (`routed_commits.py:422`), a unit whose spec declares `src/a` and
  whose commit writes `src/a` and `src/b/c` lists `src/b/c` as `stray`, and under `refuse` the leg
  exits 1. Observed by AC3.
- **S5** — Unit 34 answered. Unit 34's acceptance ledger answers its AC2 with a note naming
  `TOOL-dScopedBuild-38 S3`. Observed by AC2.

## 3. Non-goals (OUT)

- Unit 5's lease and unit 8's claim arm beyond the call. Unit 5 passes `entries` to
  `read_unit_writes` (§3 Edges); unit 8 reads the write set through unit 3's scope arm.
- The overlap probe of TOOL-dPlacedRequest-1 S9; TOOL-dScopedBuild-20 points it at this function.
- The left-shift checklist entry the report names. No clause of this build names it.
- Rewording units 3 and 34; each clause is superseded by name.

### Edges

- **consumes-from** `TOOL-dScopedBuild-34` — S1's rule and S2's class over the tree, which S1 and S3 restate over `ROUTED_PATHS` (id 26)
- **consumes-from** `TOOL-dScopedBuild-3` — S1's `derive_kit_dir` and S2's `read_unit_writes`, whose signatures S1 and S2 widen by `entries`, and AC2's fixture, which S4's case follows (id 26)
- **consumes-from** `TOOL-dScopedBuild-9` — the touch join's `read_unit_writes` call, which S2 passes `entries` (id 26)
- **hands-off** `TOOL-dScopedBuild-5` — S2's `read_unit_writes(unit, spec_text, run_rows, tracked, entries)`, which the `--unit-lease` read calls with `check_conf`'s entries (id 26)
- **hands-off** `TOOL-dScopedBuild-40` — S1's fall-through and S3's class, which that unit guards so no result covers an entry, and AC2, which its S2 supersedes (id 24)
- **hands-off** `TOOL-dScopedBuild-41` — S2's CLI refusal and its callers' `entries`, which that unit's AC13 observes, S2's five-parameter spelling, which its S14 states supersedes unit 5 S2's, and §1's and §4's conf evidence, which its S21 respells (ids 8, 5, 15)
- **hands-off** `TOOL-dScopedBuild-43` — AC2's acceptance-ledger answer, whose note naming `TOOL-dScopedBuild-40 S2` that unit's AC1 reads (id 1)

## 4. Design

### Evidence

- `tools/memory-tree/.memory-tree.conf.example:487`: `ROUTED_PATHS="src/ lib/"`.
- `routed_commits.py:181-186`: `test_routed_path` returns the first entry a path equals or lies under,
  the one routed-path test `deviation_join.py:333` also calls.
- `routed_commits.py:138-170`: `check_conf` normalises each entry and refuses one that names nothing
  tracked, so the entries S1 reads are the leg's validated set.
- `routed_commits.py:420-425`: `set_fixture_conf` defaults `ROUTED_PATHS` to `src/`.

### The rule, after this unit

| Entries | Path | Reduces to |
|---|---|---|
| this tree's | `tools/memory-tree/routed_commits.py` | `tools/memory-tree/` |
| this tree's | `tools/gate-legs.json` | `tools/gate-legs.json` |
| this tree's | `WIRE-INTO-PROJECT.md` | `WIRE-INTO-PROJECT.md` |
| this tree's | `.githooks/pre-push` | `.githooks/` |
| `src/ lib/` | `src/main.py` | `src/main.py` |
| `src/ lib/` | `src/pkg/x.py` | `src/pkg/` |
| `src/ lib/` | `lib/y.py` | `lib/y.py` |

### Inventory

Minted: nothing. `derive_kit_dir` and `read_unit_writes` are unit 3's, each gaining `entries`. No
lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 6, one step after unit 34 (order 5), tied with units 27, 29 and 8. All write
`tools/memory-tree/routed_commits.py`, so BUILD-METHOD M6 sequences them within the step. Unit 5
(order 7) calls the five-parameter `read_unit_writes`.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/routed_commits.py`: the callers of S2 and the selftest case of S4

### Alternatives rejected

- **Keep `tools/` and `skills/` and add `src/` and `lib/`.** Any other adopter root has the defect
  again; the conf already declares the roots.
- **Read `ROUTED_PATHS` inside `derive_kit_dir`.** A fixture repository and the tree it runs from
  would share one read, and the function would stop being pure.

## 5. Production-readiness checklist

- security — narrows a write set: one declared file under a routed root no longer covers the root.
- perf / scale — one prefix test per entry per path, as the leg already makes.
- error / empty / loading states — a blank or invalid `ROUTED_PATHS` is `check_conf`'s `Refusal`,
  the CLI's exit 2.
- observability — `--kit-dir` prints each reduction.
- risks — a unit that relied on the broad reduction now lists strays it always had; AC3 is that case.
- testing — AC1 and AC2 by probe, AC3 in the routed-commits selftest.
- migration — none.
- user docs — none under `help/`; unit 3's `help/build-scope.md` describes the write set without the
  reduction's rows.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `design_lib.derive_kit_dir` over `src/main`, `src/pkg/x` and
  `lib/y` with the entries `["src/", "lib/"]`, it returns `src/main`, `src/pkg/` and `lib/y`;
  and `python tools/memory-tree/design_lib.py --kit-dir tools/gate-legs.json
  tools/memory-tree/routed_commits.py WIRE-INTO-PROJECT.md` prints `tools/gate-legs.json`,
  `tools/memory-tree/` and `WIRE-INTO-PROJECT.md`, one per line.
  Red when: a file directly under a declared directory entry reduces to the entry.
- **AC2** — When `python -c` runs `design_lib.derive_kit_dir` over every path `git ls-files` prints,
  with `routed_commits.check_conf`'s entries for this tree, no result equals a `ROUTED_PATHS` entry
  ending `/`.
  Red when: any tracked path reduces to a whole routed root.
  figure: DERIVED at observation from this tree's `ROUTED_PATHS`.
- **AC3** — When the routed-commits fixture keeps `set_fixture_conf`'s `ROUTED_PATHS` of `src/`, a
  spec for `TOOL-tFix-1` declares `src/a`, and a commit naming it writes `src/a` and `src/b/c`,
  `check_routed_commits` under `refuse` exits 1, the `stray` line names `src/b/c`, and `src/a` is not
  listed.
  Red when: the declared file admits the whole `src/` root.
  fixture: built by `routed_commits.build_fixture`, as unit 3 AC2's is.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC3 · the `src/` fixture with a declared `src/a` and a stray `src/b/c`, staged by restoring the first-segment fall-through for every root · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 34's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 25 to 35, id 26
  (HIGH, item H3).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-40 and TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (ids 24, 8, 5, 15).
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-43, the minors batch of the round-1 spec audit of units 40 and 41 (id 1).

## 10. Reuse audit

The seams are unit 3 S1's `derive_kit_dir`, the one written form of the kit-directory rule, and
`routed_commits.test_routed_path` (`tools/memory-tree/routed_commits.py:181`), the leg's own
routed-entry test, reused rather than restated; `check_conf` supplies the entries.
`python tools/codebase-map/reuse_lookup.py "reduce a path to its directory under a routed root
entry"` ranked `repo_root`, `map_root`, `resolve_memory_root` and `resolve_entry`, none a path
reduction, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does a write set reduce a path under an adopter's routed root" --terms "derive_kit_dir ROUTED_PATHS test_routed_path check_conf kit directory reduction src adopter write set stray"`
