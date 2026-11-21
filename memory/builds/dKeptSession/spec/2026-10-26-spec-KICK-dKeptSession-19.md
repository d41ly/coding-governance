# KICK-dKeptSession-19 — the catalogue's reader join, and the shrink-only list factory it extracts

**Status:** CLOSED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 2 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0157@7d569b91 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-16 KICK-dKeptSession-20 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-11-21-build-KICK-dKeptSession-19-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-19-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-19-red-fix-4.md](../build/2026-11-21-build-KICK-dKeptSession-19-red-fix-4.md) | red-fix | — |
| [2026-11-21-build-KICK-dKeptSession-19-red-fix-5.md](../build/2026-11-21-build-KICK-dKeptSession-19-red-fix-5.md) | red-fix | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 |
| [2026-11-21-prompt-KICK-dKeptSession-19-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-19-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-19-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-19-divergence-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

gap-spine-10: a catalogue key that no unit on its owner build's `[chain]` row names is a key a spec
writer cannot find a reader for. The away pass ran the predicate over the tree, found too many
failures for it to arm as a red, and gave dKeptSession the join with today's unnamed keys held as a
shrink-only population
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md@c2a407b0:362`).
This unit lands that join as a policy kit arm over the design view, and the shrink-only list it
writes through one factory extracted from the policy kit's two hand-rolled lists, since this is the
third.

## 2. Scope (IN)

- **S1** — The factory (shared interface I7), in `tools/policy/policy.py`, in two layers. The lower
  two: `read_shrink_base(kit, name, base)` returns the names of the list file `name` under the kit in
  the commit `base`, read by `parse_list` (`tools/policy/policy.py#parse_list`), or None where that
  commit holds no such file, and raises the `Refusal` `read_base_pairs` raises today where the kit is
  in no git repository (`tools/policy/policy.py#read_base_pairs`); `write_shrink_file(kit, name,
  header, names)` writes the header then one line per name, UTF-8 with LF endings, as `write_list`
  writes (`tools/policy/policy.py#write_list`). The upper two are built on them.
  `check_shrink_list(kit, name, derived, compare, unlisted)` returns the findings and a note against
  a derived set and `compare`, the (sha or None, why) `resolve_compare_base` answered
  (`tools/policy/policy.py#resolve_compare_base`, the inlined copy of `tools/lib/compare_base.py`): a
  derived name the list lacks, its why `unlisted`; a listed name no longer derived, stale; a listed
  name the base's list lacks, grown; every note and every other why as `check_list` words it
  (`tools/policy/policy.py#check_list`), "absent at the base is never an empty list" kept.
  `write_shrink_list(kit, name, header, derived)` writes the list's names intersected with the
  derived set, sorted, seeding an absent list with the whole set, and returns the names it drained.
  Observed by AC4 and AC5.
- **S2** — The two existing lists on it. `check_list(kit, compare)` and `write_list(kit)` keep the
  signatures the `summary-new-key` case calls (`tools/policy/check_policy.py#run_fixture`) and become
  one call each, `check_shrink_list(kit, LIST, <derived>, compare, "lacks a summary or a usage and is
  not listed")` and `write_shrink_list(kit, LIST, LIST_HEADER, <derived>)`, the derived set
  `derive_unsummarised(load_catalogue(kit))`, so their verdicts and messages are unchanged. The
  legacy-home list keeps its compare, marks, reports and new-home refusal
  (`tools/policy/policy.py#check_legacy_homes`) and moves only its two file operations.
  `read_base_pairs(kit, base)` maps `read_shrink_base(kit, LEGACY_LIST, base)`'s rows onto their
  (home, key) pairs, None kept; its `repo` argument goes, since the base is a commit of the kit's
  repository (`resolve_compare_base(kit)`), which is the repository under test in every `lists` run
  and over gov's tree. `write_legacy_homes` writes its derived rows, `<home> <key> <mark>`, by
  `write_shrink_file(kit, LEGACY_LIST, LEGACY_HEADER, rows)`
  (`tools/policy/policy.py#write_legacy_homes`): every derived row, so a header-only list is seeded
  and a typed row corrected as at the base, and nothing where a row is new to the base's list.
  Observed by AC4 and AC5.
- **S3** — The join, `derive_unnamed_keys(rows, design)` in `policy.py`: the sorted names of the
  catalogue rows whose `name` is among no clause's backticked names, `extract_clause_tokens`
  (`tools/memory-tree/design_lib.py#extract_clause_tokens`), on the row's `owner` build in the design
  `read_design` returns (`tools/memory-tree/design_lib.py#read_design`). The design is read by
  `load_design(kit, root)` in `policy.py`: the memory-tree kit's `design_lib` found by the inlined
  `resolve_kit_dir` (`tools/policy/policy.py#resolve_kit_dir`), as `load_tree_lib` finds `tree_lib`
  (`tools/policy/check_policy.py#load_tree_lib`), over the caller's conf as `read_design_conf` reads
  it (`tools/memory-tree/design_lib.py#read_design_conf`). It raises `LookupError` where no
  memory-tree kit is found and lets `read_design`'s `DesignRefusal` through. The kit already
  `requires` memory-tree (`tools/policy/kit.toml#requires`). Observed by AC1 and AC2.
- **S4** — The list `tools/policy/unnamed-keys.txt` under `UNNAMED_HEADER`, graded by
  `check_unnamed_list(kit, design, compare)` in `policy.py`: `check_shrink_list` over
  `UNNAMED_LIST`, `derive_unnamed_keys(load_catalogue(kit), design)` and `UNNAMED_WHY`, "unnamed and
  not listed", the one grade `lists --check` and S5's arm both call, as both call `check_list` for
  the summary list. `cmd_lists` (`tools/policy/policy.py#cmd_lists`) reads it against the one compare
  base it reads for the other two lists, the design read once by `load_design(KIT, top)`. Where that
  raises `LookupError`, or the `DesignRefusal` whose `blank` holds all four `DESIGN_KEYS`
  (`tools/memory-tree/design_lib.py#DesignRefusal`), or, for `--check`, the list is absent, both
  verbs print `policy lists: unnamed-keys.txt · not graded · <why>`, add no finding and write
  nothing: a kit copy with no memory-tree kit beside it, as `build_legacy_repo` builds
  (`tools/policy/check_policy.py#build_legacy_repo`), exits as it did. Any other `DesignRefusal` is
  printed and exits 2, as `cmd_lists` treats a `Refusal`. Otherwise `--check` prints
  `policy lists: unnamed-keys.txt · <note>` and its findings, counted in its exit, and `--write`
  writes by `write_shrink_list(KIT, UNNAMED_LIST, UNNAMED_HEADER, <derived>)`, seeding an absent
  list. It is gov's own and withheld from installs, as `legacy-homes.txt` is: its name joins the
  `project-owned` `[[files]]` rule of `tools/policy/kit.toml`. Observed by AC1 and AC5.
- **S5** — The arm `arm_reader_join` in `ARMS` of `tools/policy/check_policy.py`
  (`tools/policy/check_policy.py#ARMS`), `empty = "announce"`: `load_design(kit, repo)` then
  `check_unnamed_list`. Every run prints its population, `<n> of <m> catalogue key(s) named on their
  owner's row · <k> listed`. Where every `DESIGN_*` key is blank, as in every adopter, or the list is
  withheld, the arm prints `policy-check: arm_reader_join · not graded · <why>` and grades nothing; a
  `LookupError` or any other `DesignRefusal` is the one finding, as `arm_reader_coverage` reds a
  memory-tree miss (`tools/policy/check_policy.py#arm_reader_coverage`). Its row in the kit README's
  "Each arm in an adopter" table (`tools/policy/README.md`). Observed by AC2, AC3 and AC6.
- **S6** — The page `help/policy.md` says what the list holds and how a key leaves it: a clause on
  its owner's row names it, through a deviation record, and `lists --write` drains it. Observed by
  AC7.

## 3. Non-goals (OUT)

- Naming any listed key: each leaves the list when its owner build's row names it, by that build's
  deviation, never by this unit.
- Reading an owned node (`node:policy-key.<key>`) as naming a key: the clause says "named by a
  unit"; a spec's node binding is graded by the carries join, not here (§8 F1).
- The policy namespaces' purposes list: KICK-dKeptSession-16's, the factory's fourth caller.
- A gate on the design view's own shape: memory-tree's `read_design_view` refuses a malformed view
  (`tools/memory-tree/design_lib.py#read_design_view`).
- The codebase map's baseline: a TOML table of inventory keys compared by `coverage_join`'s
  `derive_baseline_additions` (`tools/lib/coverage_join.py`), not a list file of names.

### Edges

- **hands-off** `KICK-dKeptSession-16` — `write_shrink_list` with `check_shrink_list`, which the namespace purposes' awaiting-review list is written and graded by
- **consumes-from** external — the policy kit's `parse_list`, `check_list`, `write_list`, `read_base_pairs`, `check_legacy_homes`, `write_legacy_homes`, `resolve_compare_base`, `resolve_kit_dir`, `cmd_lists`, `ARMS`, `load_tree_lib`, `build_repo` and `build_legacy_repo`; memory-tree's `read_design`, `read_design_conf`, `DesignRefusal` and `extract_clause_tokens` in `tools/memory-tree/design_lib.py`; each landed at this spec's base

## 4. Design

### The factory

```
read_shrink_base(kit, name, base)                         -> [names], or None where absent at base
write_shrink_file(kit, name, header, names)               -> None
check_shrink_list(kit, name, derived, compare, unlisted)  -> ([(name, why)], note)
write_shrink_list(kit, name, header, derived)             -> removed names
```

The upper two are `check_list` and `write_list` with the list's file name, its derivation, its
header and its not-listed why made arguments, the base read and the write moved into the lower two.
The legacy list's rows carry three fields and a mark, its compare names typed and stale rows, and
its write writes every derived row or, on a new home, nothing; draining by intersection would drop
a typed row and seed a header-only list empty. So it keeps its compare and write policy and calls
the lower two alone, and its reports stay word for word, which its three fixture cases pin.

### The join

```
design = read_design(root, read_design_conf(root))        # memory-tree, DESIGN_* keys
names(build) = union of extract_clause_tokens(text) over design["builds"][build]
unnamed = sorted(row.name for row in catalogue if row.name not in names(row.owner))
findings, note = check_shrink_list(kit, UNNAMED_LIST, unnamed, compare, UNNAMED_WHY)
```

A placeholder name such as `roles.harness.<role>` is matched as spelled: a clause names it with the
placeholder or not at all. A row whose owner is not a build of the view is unnamed.

### The list

```
# unnamed-keys.txt - GENERATED by `python <this kit>/policy.py lists --write`, never edited.
# The catalogue keys no clause on their owner build's row names (gap-spine-10), sorted.
# SHRINK-ONLY: `lists --check` reds a key named now, a new unnamed key, and a key the list at
# the compare base did not carry. A key leaves when its owner's row names it.
bar.inline-red-fixes
```

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `read_shrink_base`, `write_shrink_file`, `check_shrink_list`, `write_shrink_list`, `derive_unnamed_keys`, `load_design`, `check_unnamed_list` | functions, lexicon cell py.function, each passed by `lexicon.py --suggest` 2026-11-21 | `tools/policy/policy.py` |
| `UNNAMED_LIST`, `UNNAMED_HEADER`, `UNNAMED_WHY` | constants, no declared lexicon cell | `tools/policy/policy.py` |
| `tools/policy/unnamed-keys.txt` | generated list | new |
| `arm_reader_join` | arm, lexicon cell py.function | `tools/policy/check_policy.py` |
| `reader-join` (an outcome case), `reader-join-blank` | fixture cases | `tools/policy/check_policy.py` |

### Migration

The list is seeded by the first `lists --write`, with no list at the compare base, which seeds the
baseline as the legacy list's first write does.

### Files touched (estimate)

- `tools/policy/policy.py`: the factory's four functions, the two lists moved onto them, the join,
  `load_design`, `check_unnamed_list`, `cmd_lists` reading the third list
- `tools/policy/unnamed-keys.txt` (new)
- `tools/policy/check_policy.py`: `arm_reader_join` and its two cases
- `tools/policy/kit.toml`: the list withheld from installs
- `tools/policy/README.md`: the arm's row
- `help/policy.md`

### Alternatives rejected

- **A red gate on every unnamed key.** The away pass ran it first: it cannot arm, so the population is
  held shrink-only, which the clause states.
- **A third hand-rolled list.** The charter's `[reuse]` rule extracts a kind's factory at its second
  instance; this is the third.
- **Moving the legacy list's whole compare onto the factory.** Its identity is a pair, its rows carry
  a mark and its write refuses growth, so a shared compare would change its reports; only its read
  and write halves move.
- **The shared join factory `coverage_join`.** It compares a TOML baseline keyed by inventory id; the
  policy lists are header-and-names text files, so moving them onto it would change every list's
  format and its readers.

## 5. Production-readiness checklist

- security — reads only; the one write is the generated list, by `lists --write`.
- perf / scale — one design read per run, over the view's rows (509 at `31fbb903`, PINNED 2026-11-21); one set lookup per catalogue row.
- error / empty / loading states — blank `DESIGN_*` keys announce; a `DesignRefusal` other than the
  blank state is one finding naming the key and the cause in the arm, and exit 2 in `lists`, where a
  missing memory-tree kit is not graded so a kit copy without it keeps its other two lists. What no
  check here sees: gov's own list deleted reads not graded, as the legacy list's would but for its
  `legacy-homes-present` case.
- observability — the population line names named, total and listed counts.
- risks — the view changes when a deviation moves a clause, so a key can leave the list without this
  kit changing; the stale finding names it and `lists --write` drains it.
- testing — the two cases of the criteria below and the arm; the moved lists keep their existing
  cases.
- migration — the first write seeds the list.
- user docs — `help/policy.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python policy.py lists --write` then `python policy.py lists --check` run in gov's
  tree, the check exits 0 and prints a `policy lists: unnamed-keys.txt · ` line, and `grep -vc "^#"
  unnamed-keys.txt` in the policy kit prints the count `derive_unnamed_keys` gives.
  Red when: a listed key is now named, or the list misses an unnamed key.
  figure: the count is DERIVED by `derive_unnamed_keys` at each run.
  figure: PINNED 2026-11-21, 48 of 273 catalogue keys unnamed over the view's 509 rows at `7424f8c0`, against the away pass's 116 of 220.
- **AC2** — When `python check_policy.py --fixture reader-join` builds `build_repo`'s copy, gives
  it a design of `read_design`'s shape, `{"builds": ...}`, seeds its list copy by
  `write_shrink_list` over that design and commits it as its base, then plants on the catalogue copy
  a row owned by `dKeptSession` that no clause names, `check_unnamed_list` reds naming it `unnamed
  and not listed`; when it adds a clause naming a listed key, it reds naming that key `stale`; the
  unplanted copy is green.
  Red when: either plant reads green.
- **AC3** — When the `reader-join` case plants a catalogue row no clause names and adds its name to
  the list copy above the committed copy, as `seed_list_grew` does for the summary list,
  `check_unnamed_list` reds naming it `added to a shrink-only list above the base`.
  Red when: the list grows silently.
- **AC4** — When `grep -n "read_shrink_base(\|write_shrink_file(" policy.py` runs in the policy kit,
  its lines are the two definitions and calls inside `check_shrink_list`, `read_base_pairs`,
  `write_shrink_list` and `write_legacy_homes` alone; `grep -c '"show", f"{base}' policy.py` prints
  1 and `grep -c "_HEADER + " policy.py` prints 0.
  Red when: a list keeps its own base read or file write.
  figure: PINNED 2026-11-21, the last two print 2 and 2 at `7424f8c0`: `check_list`'s and `read_base_pairs`' reads, `write_list`'s and `write_legacy_homes`' writes.
- **AC5** — When `python check_policy.py --fixture list-grew` runs after the move, and the same
  command with `summary-new-key`, `legacy-homes`, `legacy-homes-main-dropped` and
  `legacy-homes-present` in its place, each case reads as it read before it, its exits and its `legacy homes` reports unchanged though the kit
  copy `build_legacy_repo` builds holds no memory-tree kit.
  Red when: a moved list's verdict or message changes.
- **AC6** — When the `reader-join-blank` case runs `python check_policy.py --repo <dir>` over a
  scratch repository whose `.memory-tree.conf` leaves every `DESIGN_*` key blank, it prints
  `policy-check: arm_reader_join · not graded` and no finding under that line.
  Red when: the arm reds or reads green with nothing graded.
- **AC7** — When `grep -n "unnamed-keys" policy.md` runs in the help directory, it prints the
  paragraph naming how a key leaves the list.
  Red when: the page omits the list.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC6 · the `reader-join` case's planted row, naming clause and grown list over its own design on `build_repo`'s copies, and `reader-join-blank`'s scratch conf leaving every `DESIGN_*` key blank · none

## 8. Open questions

- **F1 — Does a spec's owned-node binding count as a unit naming a key?** (a) Only a clause's
  backticked name on the owner's row, the clause's "named by a unit on its owner build's row"; (b)
  also a `**Carries:** node:policy-key.<key>` line in an owner build's spec. (b) puts the carries
  instrument's join, a record, into a product arm, and grades specs, not the design. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, the clause's words. widens: none · relaxes: none. At
  `c2a407b0` most unnamed keys are owned nodes the carries join grades, and those a build added after
  the view are no build's node, so (b) would not name them either (PINNED 2026-11-21: 37 and 11).
- **F2 — Does the legacy-home list move onto the factory whole?** (a) Its read and write halves only,
  its compare its own; (b) whole, its compare generalised over a row identity and a mark. (b) changes
  the list's reports, which three fixture cases pin. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the most reuse that leaves every verdict as it is. widens: none · relaxes: none
- **F3 — How do the legacy list's base read and file write reach the factory, and where does the
  not-listed finding's wording come from?** (a) Two lower helpers, `read_shrink_base` and
  `write_shrink_file`, that the upper two are built on and the legacy list calls, with the wording
  an argument of `check_shrink_list`; (b) the upper two alone, which return no names at the base
  for `read_base_pairs`, and whose intersecting write seeds `build_legacy_repo`'s header-only list
  empty and drops a typed row, so AC5 cannot hold. RESOLVED (agent, 2026-11-21, delegated): (a),
  rung 3, by the main loop on the builder's DIVERGENCE (run `wf_eac72422-66e`): the most reuse that
  leaves every verdict as it is. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-11-21 · S1 S2 S3 S4 S5 · §3 · §4 · §5 · AC1 · §7 · §8 F1 · §10 · re-grounded on the
  landed tree at `c2a407b0` under the brief
  `2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief`: the policy kit and the
  memory-tree design reader are in the tree, so every function is cited by symbol; S3 names its
  design loader, `load_design`; S4 names the `kit.toml` rule that withholds the list; AC1's figure
  re-measured; F1's reason re-measured, its pick kept; the Gates line names the policy legs the
  Files touched trip; the shared join factory recorded as no fit. Nothing narrowed: no landed unit builds the factory, the join or the list.
- rev-3 · 2026-11-21 · S1 S2 S3 S4 S5 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 · §7 · §8 F3 · §10 ·
  the builder's divergence resolved under the brief
  `2026-11-21-prompt-KICK-dKeptSession-19-divergence-brief`: S1 names the lower helpers
  `read_shrink_base` and `write_shrink_file` and the `unlisted` wording argument; S2 moves the
  legacy list onto the lower two only, its seeding and correcting kept; S4 adds
  `check_unnamed_list`, the grade `lists` and the arm share, and the `lists` states where no design
  loads, so `build_legacy_repo`'s copy exits as before; AC2 and AC3 grade over a design the case
  builds, since no memory-tree kit sits beside `build_repo`'s copy; AC4's greps count the lower
  helpers; AC1 re-pinned at `7424f8c0`, its figure unchanged. Nothing narrowed.

## 10. Reuse audit

The seams extended: the policy kit's `check_list` and `write_list`
(`tools/policy/policy.py#check_list`, `#write_list`), the legacy list's `read_base_pairs`,
`check_legacy_homes` and `write_legacy_homes`, the one compare base `resolve_compare_base`, read once
in `cmd_lists`, and the arm shape of `arm_reader_coverage`
(`tools/policy/check_policy.py#arm_reader_coverage`) with its cross-kit load `load_tree_lib`; the
join input is memory-tree's `read_design` and `extract_clause_tokens`
(`tools/memory-tree/design_lib.py#read_design`, `#extract_clause_tokens`), its conf keys
`DESIGN_RECORD`, `DESIGN_BASELINE`, `DESIGN_VIEW` and `DESIGN_NODES` in `.memory-tree.conf`, and its
all-blank state the `blank` field of `DesignRefusal` (`tools/memory-tree/design_lib.py#DesignRefusal`).
The lower helpers extend `check_list`'s base read and `write_list`'s write, `parse_list` the one
list parser (`tools/policy/policy.py#parse_list`); the `reader-join` case extends `build_repo`
(`tools/policy/check_policy.py#build_repo`) and the `list-grew` seed
(`tools/policy/check_policy.py#seed_list_grew`).
`python tools/codebase-map/reuse_lookup.py "shrink-only generated list checked against compare
base"`, re-run 2026-11-21, ranked `check`, `checks`, `resolve_compare_base` in
`tools/lib/compare_base.py` and its inlined copies, `resolve_generated_indexes` and `read_id_list`:
no list factory exists at this base. Its compare base is the one this factory reads; the shared join
factory `tools/lib/coverage_join.py` compares a TOML baseline, which no policy list is. `python
tools/memory-recall/query.py` with the terms below returned this build's brief, this spec and scout
A's row 6. Disagreement: the brief's 116 of 220 is the away pass's figure; the predicate over today's
view and catalogue gives the AC1 figure.

Recall terms used: catalogue reader join unnamed keys shrink-only list owner build row clause tokens gap-spine-10
