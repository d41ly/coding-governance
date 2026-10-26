# TOOL-dTotalRecall-68 — the census keep registry is a `[[ledger]]` population read through the ledger factory, so a keep added later is refused `gained`

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 32 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-68-deviation-681.md](../build/2026-10-26-build-TOOL-dTotalRecall-68-deviation-681.md) | deviation | — |
| [2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-67 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 61 to 66
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md`)
confirmed finding **id 16 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-65`
(order 31) moves the census keep rows into `memory/project/census-kept-paths.txt`. It reads them
with its own parser, modelled on `transition_audit.read_registry`
(`tools/memory-tree/transition_audit.py:762-774`, a whitespace split), and names no `[[ledger]]`
registration. The parent build dWitnessedBar, declared in this README's `parents:`, points every
`memory/project/*.txt` at its ledger factory. `TOOL-dWitnessedBar-16` S1 derives that population.
Its S4 says no reader keeps a parser of the old grammar, and its AC1 is red on a registry with no
registration. This build already registers its own project home that way (`TOOL-dTotalRecall-19`
S7, `legacy-records`). The keep list is graded by no engine, so a keep row added later to quiet the
cause or alias census meets no `shrink-only` ratchet. The repository also gains a second parser of a
grammar its parent retires.

This unit registers the registry as the `[[ledger]]` population `census-kept-paths`, direction
`shrink-only`, and converts its rows to the factory's row grammar. `read_kept_path` reads them
through the factory's `read_rows`. The census check judges the home against its base, so a row
the base lacked is a red finding named `gained`. It repairs `TOOL-dTotalRecall-65`, at step 32, one
above that unit's order.

## 2. Scope (IN)

- **S1** — The registration. A `[[ledger]]` table in `tools/memory-tree/kit.toml`, population
  `census-kept-paths`, as §4's block states. Observed by AC1.
- **S2** — The rows. `memory/project/census-kept-paths.txt` is rewritten through the factory's
  `write_rows`, with the header its registration renders. Each of unit 65's rows becomes one factory
  row, its reason whole and its `records` field `-`, at the pass base's SHA with disposition
  `seeded`. Observed by AC1 and AC4.
- **S3** — One parser. `read_kept_path(census, path, root)` in `tools/memory-tree/tree_lib.py`
  returns the row whose `census` and `path` fields match, as a mapping of the registration's named
  fields and the factory's tail, or `None`. It reads through `legacy_ledger.read_rows` and splits
  no line itself. Each malformed row the factory returns is a red finding naming its line in both
  `record_causes.py --check` and `record_kinds.py --check`. Observed by AC3 and AC4.
  **Readers:** by name: READER NOT IN TREE — unit 65's row parser is minted in this build and is
  absent at base `462d20f3` · by value: `check_cause_writers` and `check_alias_compares`, which read
  the reason of the row `read_kept_path` returns.
- **S4** — The ratchet runs. `record_causes.py --check` calls `compare_to_base` for the
  `census-kept-paths` registration and prints each refusal as a red finding with its key. A `None`
  base prints its reason as unresolved, never as green. Observed by AC2 and AC4.
- **S5** — Unit 66 tells the rows apart by name. Before unit 66's pass, its S36, its §4 "The
  registry row after S36", its AC28, its Inventory and its §8 F3 take §4's text. A pinned writer is
  then told by its `records` field and its `keep:` disposition, never by a field count. Each change
  is a rev bump with a §9 line naming this unit. Observed by AC5.

## 3. Non-goals (OUT)

- The ledger factory itself, `tools/lib/legacy_ledger.py` and its inline copies:
  `TOOL-dWitnessedBar-13`'s, in the parent build. This unit reads its `read_registrations`,
  `read_rows`, `write_rows` and `compare_to_base`.
- The census domain and the uniqueness of a `(census, path)` pair: the batch
  `TOOL-dTotalRecall-70` (id 29).
- A measurement of each row's count. This unit adds no seed, so a count is compared with the base
  (`raised`) and never re-measured. The registration's empty `seed` states that.
- A `merge=rows` line in `.gitattributes`. This build's other ledger, `legacy-records`, carries
  none either, so one rule for both is a follow-up for the close's left-shift step (BUILD-METHOD M8).
- `.memory-tree.conf`. Unit 65's `PROJECT_REGISTRY_EXTRA` entry stands, and this pass writes no
  watched file.

### Edges

- **consumes-from** `TOOL-dTotalRecall-65` — `census-kept-paths.txt`, its rows and `read_kept_path(census, path, root)`, which this unit registers, converts and re-points onto the factory
- **hands-off** `TOOL-dTotalRecall-66` — S36's pinned-writer row, which that unit writes in the factory grammar with its `records` glob and `keep:` disposition, read by named field
- **hands-off** `TOOL-dTotalRecall-70` — the factory row grammar, over which that unit states the row-grammar items (ids 4, 13, 17, 28) and adds the census domain and the unique pair (id 29)
- **hands-off** `TOOL-dTotalRecall-73` — the `census-kept-paths` registration and S4's `compare_to_base` call, which that unit points at one home re-rooted under the conf's memory root (the round-1 audit of units 67 to 70, id 5)
- **hands-off** `TOOL-dTotalRecall-76` — `kept-row-gained`, the registration, the `--check` compare and its factory precondition, which that batch scrubs, re-roots, exits on and re-reads (the round-1 audit of units 67 to 70, ids 6, 21, 26, 27, 29)

## 4. Design

### The registration

```toml
[[ledger]]
population = "census-kept-paths"
leg = "record causes (causes and orphans over the legacy population)"
seed = []
key = "key"
fields = ["census", "path", "reason", "records"]
drain = "key"
direction = "shrink-only"
home = "memory/project/census-kept-paths.txt"
```

The table follows `TOOL-dWitnessedBar-13` §4 "The registration" and the `legacy-records` table of
`TOOL-dTotalRecall-19` S7. The leg is that unit's S12 leg, which runs `record_causes.py --check`.
The reason is a key field, so a keep whose reason is reworded is a new key. `shrink-only` then
refuses it as `gained`, just as it refuses a new keep.

### The home

```text
# ledger · census-kept-paths · key key census,path,reason,records · direction shrink-only · drain key
check_cause_writers	memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py	pinned instrument	-	1	<sha>	seeded
check_alias_compares	memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py	pinned instrument	-	1	<sha>	seeded
```

Rows are TAB-separated, which is the factory's grammar (`TOOL-dWitnessedBar-13` §4 "The ledger
file"). A reason of several words is one field. `-` in `records` marks a plain keep, as `-` marks
a record row with no section in `legacy-records`. The count is the number of census hits the row
keeps in its file, taken from the census output at the pass base. `<sha>` is the pass base.

### After unit 66

Unit 66 S36 adds the pinned departures writer's row. Its `records` field holds the record glob, and
its disposition is `keep:<ask id>`, the factory's own disposition for a keep held by an ask:

```text
check_cause_writers	<deviations.py path>	pinned instrument	<record glob>	1	<sha>	keep:<ask id>
```

### The amendment to unit 66

Each change below is one rev bump on unit 66's spec, with a §9 line of the form
`rev-<N> · <date> · S36 §4 AC28 §8 · amended by TOOL-dTotalRecall-68 (id 16, item H2) ...`.

- S36's first sentence reads: "One keep table: `CAUSE_WRITER_PINNED`'s row joins the registry, its
  `records` field the record glob and its disposition `keep:<ask id>`, and the constant gives way to
  that row (§8 F3)."
- §4 "The registry row after S36" holds the block above. Its paragraph reads: "A row whose `records`
  field is `-` is a plain keep. A row whose `records` field is a glob is a pinned writer, its ask the
  id of its `keep:` disposition, which S26 resolves. `read_kept_path` returns the row by its named
  fields, and no reader counts fields."
- AC28's second clause reads "keeps the pinned writer's records by its registry row's `records`
  glob".
- The Inventory's "the registry's two optional fields" reads "the pinned row's `records` glob and
  `keep:` disposition".
- §8 F3's option (a) reads "the registry, its `records` field and `keep:` disposition".

### Order inside step 32

Unit 66 also builds at order 32 and writes the registry's pinned row. This unit therefore hands off
to it by a §3 edge, and BUILD-METHOD M6 runs this pass first. `TOOL-dTotalRecall-69` shares the step
and writes only `memory/guides/SESSION-KICKOFF.md`, so its pass is disjoint from this one.

### Inventory

Minted: the `[[ledger]]` population `census-kept-paths`; the fixture plant `kept-row-gained` in
`record_causes.py --fixture`. Naming cell: none, no function minted.

### Files touched (estimate)

- `tools/memory-tree/kit.toml`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `memory/project/census-kept-paths.txt`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Read the rows with `read_rows(..., tail=("reason",))`.** `TOOL-dWitnessedBar-13` S9 keeps that
  form for adapters of today's four-field registries until `TOOL-dWitnessedBar-16` converts them.
  A new registry written in it would be a population the parent retires.
- **Key fields `census` and `path` only, with the reason outside the key.** The factory's row has no
  free-text column after the key, and its tail is count, SHA and disposition. The reason would have
  nowhere to live, and `--check` prints it.
- **Keep unit 65's parser and add a registration beside it.** That is two readers of one file, and
  the parent's S4 refuses it.

## 5. Production-readiness checklist

- security — no new write surface. The home is written by the factory's atomic `write_rows`, and
  read as before.
- perf / scale — one registration read and one base compare per census run, over ten rows or fewer.
- error / empty / loading states — an absent home is no rows and a first seed. A malformed row is a
  red finding naming its line. A `None` base prints its reason as unresolved.
- observability — each kept hit prints its row's whole reason. Each refusal prints `gained`,
  `raised` or `edited` with its key.
- risks — at the run's base `462d20f3` no home exists, so this run reads the home as a first seed and
  names no `gained` key. The ratchet bites once the home is on the default branch. AC2 proves it on a
  fixture base that holds the home.
- testing — AC1 to AC5 by the pass; the arm of §7 at the close.
- migration — unit 65's rows are rewritten one for one in this pass's commit, with nothing dropped.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe run from `tools/lib/` prints the `census-kept-paths` entry of
  `legacy_ledger.read_registrations(root)` at the pass tip, it shows direction `shrink-only` and the home S2
  rewrites, `census-kept-paths.txt` under `memory/project/`. `python legacy_ledger.py read census-kept-paths` from the
  same directory then exits 0.
  Red when: the population is unregistered, or a row of its home is malformed.
- **AC2** — When `python record_causes.py --fixture --plant kept-row-gained` runs from
  `tools/memory-tree/`, it builds a scratch repository whose `origin/main` commit holds a two-row
  home and whose working tree adds a third. There, `--check` prints a red finding naming `gained`
  and the third row's key. With that row removed, it names none.
  Red when: a keep the base lacked passes.
  fixture: the scratch repository under `%TEMP%/<short>`. A clone under the run's scratch directory
  fails with `Filename too long`, and the plant makes it.
- **AC3** — When `python -c "import inspect, tree_lib; s = inspect.getsource(tree_lib.read_kept_path); print('read_rows' in s, '.split(' in s)"`
  runs from `tools/memory-tree/` at the pass tip, it prints `True False`.
  Red when: the accessor parses rows itself.
- **AC4** — When `python record_causes.py --check` runs from `tools/memory-tree/` at the pass tip, it
  exits 0. Each build-folder file it keeps is printed on one line with its whole reason, for example
  `kept pinned instrument` or `kept outside the write set`. The `census-kept-paths` compare prints a
  first seed with the row count.
  Red when: a reason is cut at a space, a row is lost in the conversion, or the compare prints
  nothing.
- **AC5** — When the joined-text probe of `TOOL-dTotalRecall-67` §4 runs over
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md` at this pass's tip,
  `a row with five is a pinned writer` and `by its five-field row` each print 0, and
  `amended by TOOL-dTotalRecall-68` prints at least 1.
  `git merge-base --is-ancestor <this unit's pass commit> <unit 66's pass commit>` also exits 0
  once unit 66 builds.
  Red when: unit 66 still tells rows apart by count, or builds before this pass.
  figure: both stale phrases print 1 at this spec's writing, PINNED 2026-10-26 at `653bed738`.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC2 · the plant `kept-row-gained`, staged by skipping S4's compare against the base · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 61 to 66, id 16
  (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-73, TOOL-dTotalRecall-76, each the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is the parent's ledger factory, `tools/lib/legacy_ledger.py`
(`TOOL-dWitnessedBar-13` S1, S2 and S10), registered the way `TOOL-dTotalRecall-19` S7 registers
`legacy-records`. `transition_audit.read_registry` (`tools/memory-tree/transition_audit.py:762-774`)
is the parser this unit stops modelling. `TOOL-dWitnessedBar-16` §4 converts that function itself.
`python tools/codebase-map/reuse_lookup.py "a shrink-only ledger registration for a project path list read by the census"`
ranked name-stem neighbours (`read`, `read_text`, `census`), and not the factory. The factory is
absent at base `462d20f3` because its build is DEFERRED. The recall query below found it, through
`TOOL-dWitnessedBar-13` and `TOOL-dWitnessedBar-24`, and the decision `TOOL-bQuiltedLantern-3`.

Recall terms used: `python tools/memory-recall/query.py "how is a memory/project registry registered as a ledger population and ratcheted" --terms "ledger registration shrink-only legacy_ledger read_rows project registry PROJECT_REGISTRY_EXTRA census keep gained"`
