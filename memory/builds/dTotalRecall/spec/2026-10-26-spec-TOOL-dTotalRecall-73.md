# TOOL-dTotalRecall-73 — the census and its base compare read one registry path: the `census-kept-paths` registration re-rooted under the conf's memory root

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-75 TOOL-dTotalRecall-74 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 5 at HIGH**, its item **H1**. Item **M8** (id 20) addresses the same literal
home at MEDIUM with a corrected fix pointing the other way, and the report asks for one source of
truth applied to both. This unit is that source. The batch `TOOL-dTotalRecall-76` applies it to M8.

`TOOL-dTotalRecall-68` (order 32) registers the keep registry with
`home = "memory/project/census-kept-paths.txt"` in `tools/memory-tree/kit.toml`, and its S4 has
`record_causes.py --check` call `compare_to_base` for that registration. `TOOL-dWitnessedBar-13` §4
gives `compare_to_base(root, reg)` the registration's home as a literal path. Unit 68's S3 routes
`read_kept_path` through the factory's `read_rows` and never says which path it reads, so unit 65's
S2 path stands: `<root>/<MEMORY_ROOT>/project/census-kept-paths.txt`, the memory root read from the
conf. For an adopter whose memory root is not `memory`, the census reads one file and the
shrink-only compare grades another, or an absent one that always reads as a first seed. Gov sets
`MEMORY_ROOT=memory`, so gov cannot see the split.

This unit gives both readers one registration. `resolve_kept_registration(root)` returns the
`census-kept-paths` registration with its home re-rooted under the conf's memory root. The census
reads its rows at that home, and `--check` passes that same registration to `compare_to_base`. Each
prints the home it read, so a split is visible on one run. It repairs `TOOL-dTotalRecall-68`, at
step 33, one above that unit's order.

## 2. Scope (IN)

- **S1** — The one registration. `resolve_kept_registration(root)` in
  `tools/memory-tree/tree_lib.py` takes the `census-kept-paths` entry of
  `legacy_ledger.read_registrations(root)` and returns a copy of it whose home is
  `<MEMORY_ROOT>/project/<the basename of the registered home>` and whose other fields are the
  registration's own. The memory root is read from the
  conf exactly as unit 65's S2 reads it. An absent registration is a red finding naming
  `census-kept-paths`, never `None` read as no keeps. Observed by AC1 and AC2.
- **S2** — The census reads it. `read_kept_path(census, path, root)` reads `read_rows` at the home of
  `resolve_kept_registration(root)` and joins no path of its own. Unit 65's path join gives way to
  it. Observed by AC1 and AC3.
  **Readers:** by name: READER NOT IN TREE — unit 65's path join is minted in this build and is
  absent at base `462d20f3` · by value: `read_kept_path`, its one reader, which this item points at
  the registration's home.
- **S3** — The compare reads it. `record_causes.py --check` passes the registration S1 returns to
  `compare_to_base`, never the literal one `read_registrations` returns. The census line and the
  compare line each print the home they read. Observed by AC2.
- **S4** — The plant `kept-home-rooted` in `record_causes.py --fixture` builds a scratch tree whose
  conf sets `MEMORY_ROOT=docs/memory`, with the registry under `docs/memory/project/` and the
  registration's literal home under `memory/project/`. There `--check` prints one home, under
  `docs/memory/project/`, on both lines. Observed by AC2.

## 3. Non-goals (OUT)

- The ledger factory, `tools/lib/legacy_ledger.py` and its inline copies, and its
  `Registration` type: `TOOL-dWitnessedBar-13`'s. This unit reads `read_registrations`, `read_rows`
  and `compare_to_base`, and copies a registration with one field changed.
- The factory-side readers of a literal home: the `<home> merge=rows` line in `.gitattributes`, the
  duplicate-home refusal and the merge class's header read. For an adopter whose memory root is not
  `memory` they still read the literal path. That gap is the factory's, handed off below.
- The registry's row grammar, its census domain and its message text: units 68 and 70, and the
  batch `TOOL-dTotalRecall-76` for item M8's consumers and item M4's messages.
- Editing unit 68's spec, frozen once its unit builds at order 32.

### Edges

- **consumes-from** `TOOL-dTotalRecall-68` — the `census-kept-paths` registration and S4's `compare_to_base` call, which this unit points at one re-rooted home
- **hands-off** `TOOL-dTotalRecall-76` — `resolve_kept_registration`, the one home that batch's item for id 20 names to unit 66's docs-root plant and unit 70's messages and admission
- **hands-off** external — `TOOL-dWitnessedBar-13`'s owner: a `[[ledger]]` home that resolves under an adopter's memory root, for the `merge=rows` line, the duplicate-home refusal and the header read
- **hands-off** `TOOL-dTotalRecall-87` — `resolve_kept_registration` and its plant `kept-home-rooted`, whose memory-root join that unit routes through one resolver (the round-1 audit of units 71 to 76, id 39)
- **hands-off** `TOOL-dTotalRecall-88` — its AC3, its hand-off and `resolve_kept_registration`, which that batch observes by the join, completes by an ask and re-roots by prefix (the round-1 audit of units 71 to 76, ids 3, 20, 24, 27, 30, 43)

## 4. Design

### The resolution

```python
def resolve_kept_registration(root):
    """The census-kept-paths registration, its home under this tree's memory root."""
    reg = <the entry of legacy_ledger.read_registrations(root) whose population is census-kept-paths>
    home = f"{<MEMORY_ROOT read from the conf, as read_kept_path reads it>}/project/{PurePosixPath(reg.home).name}"
    return <a copy of reg whose home is home and whose every other field is reg's>
```

The basename comes from the registration, so the filename has one spelling in the tree, in
`tools/memory-tree/kit.toml`. How the copy is made follows the factory's `Registration` type, which
is absent at base `462d20f3` (UNVERIFIED until `TOOL-dWitnessedBar-13` lands it). At gov the result's
home is the literal home, because `.memory-tree.conf` sets `MEMORY_ROOT=memory`.

### The two lines

```text
census-kept-paths home memory/project/census-kept-paths.txt · read by the census
census-kept-paths home memory/project/census-kept-paths.txt · compared at <base sha>
```

`--check` prints both, with the compare's verdict after the second. A split between them is a red
finding naming both homes.

### Why one registration and not two paths agreed

`compare_to_base` reads the home it is given. Passing it the re-rooted registration makes the census
and the compare one read by construction. A path computed twice and compared would be the C6 class
the item names, two answers to one question, with a third line to keep them equal.

### Order inside step 33

`TOOL-dTotalRecall-70` and `TOOL-dTotalRecall-75` share step 33. Unit 70 writes `tree_lib.py` and
`record_causes.py` too, so the two passes are not disjoint, and BUILD-METHOD M6 sequences them in
either order. Unit 70's items read the registry through `read_kept_path`, whose signature this unit
keeps. Unit 75 writes only `memory/guides/SESSION-KICKOFF.md`.

### Inventory

Minted: `resolve_kept_registration` in `tools/memory-tree/tree_lib.py`; the fixture plant
`kept-home-rooted` in `record_causes.py --fixture`. Naming cells: `resolve_kept_registration` is
asked of the lexicon's `--suggest` under `--as py.function`, which answered `OK` at writing, led by
the declared verb `resolve`.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **The literal home wins** (item H1's corrected fix). `read_kept_path` reads the registered path,
  and unit 65's conf path gives way. An adopter with another memory root must keep its registry
  under `memory/project/`, outside its memory tree. Unit 66's AC7 plant `kept-row-docs-root` and
  unit 70's S8 messages, which name `<MEMORY_ROOT>/project/`, then contradict the engine (§8 F1).
- **The conf path for the census, the literal home for the compare** (item M8's corrected fix). That
  is the split this item names, kept.
- **A `{memory_root}` token in the registered home.** The factory designs no token resolution, and
  its other readers of `home` would read the token as a path (§3).

## 5. Production-readiness checklist

- security — no new write surface. The home stays under the tree's own memory root.
- perf / scale — one registration read per census run, as before.
- error / empty / loading states — an absent registration is a red finding. An absent home is a
  first seed, as unit 68's S4 reads it.
- observability — both lines print the home they read.
- risks — an adopter's factory-side readers still use the literal home, handed off in §3.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none. Gov's home does not move.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, pathlib, tree_lib; print(tree_lib.resolve_kept_registration(pathlib.Path(sys.argv[1]).resolve()).home)"`
  runs from `tools/memory-tree/` at the pass tip, given the repository root as its one argument, it
  prints the home `tools/memory-tree/kit.toml` registers for `census-kept-paths`, unchanged.
  Red when: gov's resolved home differs from its registered one.
- **AC2** — When `python record_causes.py --fixture --plant kept-home-rooted` runs from
  `tools/memory-tree/`, `--check` prints the census line and the compare line, each naming
  the registry's file under the `project` folder of the fixture's memory root `docs/memory`.
  Red when: the compare names `memory/project/`, or the two lines name different homes.
  fixture: the plant's scratch tree, made in a `tempfile.TemporaryDirectory()` the plant removes.
- **AC3** — When `python -c "import inspect, tree_lib; s = inspect.getsource(tree_lib.read_kept_path); print('resolve_kept_registration' in s, 'project' in s)"`
  runs from `tools/memory-tree/` at the pass tip, it prints `True False`.
  Red when: the accessor joins its own path beside the registration's.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC2 · the plant `kept-home-rooted`, staged by passing the literal registration to `compare_to_base` · none

## 8. Open questions

- **F1 — Which file is the registry's one source of truth for both readers (ids 5 and 20)?** Options:
  (a) the registered literal home, read by the census and the compare alike; (b) the conf-derived
  path for the census and the literal home for the compare; (c) the registration with its home
  re-rooted under the conf's memory root, passed to both. (b) keeps the split this unit exists to
  close and fails AC2; veto 1 discards it. (a) passes AC2 only by moving an adopter's registry out of
  its memory tree, and contradicts unit 66's AC7 plant and unit 70's S8 messages. (c) satisfies every
  criterion above and both units' text. RESOLVED (agent, 2026-10-26, delegated): (c), rung 3, the
  most feature-rich survivor. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 5
  (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-87, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is the factory's own `compare_to_base(root, reg)` (`TOOL-dWitnessedBar-13` §4, "The
factory's functions"), which reads the home of the registration it is given, so this unit changes
the registration and not the compare. The memory-root read is the one unit 65's S2 already makes in
`read_kept_path`. `python tools/codebase-map/reuse_lookup.py "a shrink-only ledger registration for a project path list read by the census"`
ranked name-stem neighbours and not the factory, which is absent at base `462d20f3`. The recall
query below found `TOOL-dWitnessedBar-13` and its literal-home rule, and no reader that re-roots a
home. No existing seam fits beyond the factory's compare and unit 65's root read.

Recall terms used: `python tools/memory-recall/query.py "how is a memory/project registry registered as a ledger population and ratcheted" --terms "ledger registration shrink-only legacy_ledger read_rows project registry PROJECT_REGISTRY_EXTRA census keep gained"`
