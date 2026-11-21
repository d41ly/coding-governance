# KICK-dKeptSession-19 — the catalogue's reader join, and the shrink-only list factory it extracts

**Status:** DEFERRED · rev-2 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 2 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0157@7d569b91 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-16 KICK-dKeptSession-20 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-33 |
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

- **S1** — The factory (shared interface I7), in `tools/policy/policy.py`: `check_shrink_list(kit,
  name, derived, compare)` returns the findings and a note for a list file of names under the kit,
  against a derived set and the list at the compare base `resolve_compare_base` answered
  (`tools/policy/policy.py#resolve_compare_base`, the inlined copy of `tools/lib/compare_base.py`): a
  derived name the list lacks, a listed name no longer derived (stale), and a listed name the base's
  list lacks (grown), with "absent at the base is never an empty list" kept; `write_shrink_list(kit,
  name, header, derived)` writes the list's names intersected with the derived set, sorted, under
  its header, seeding an absent list with the whole set. Observed by AC4 and AC5.
- **S2** — The two existing lists on it. `check_list` and `write_list`
  (`tools/policy/policy.py#check_list`, `#write_list`) become callers of S1 for
  `unsummarised-keys.txt`, their verdicts and messages unchanged. The legacy-home list's base read
  (`tools/policy/policy.py#read_base_pairs`) and its file write (`#write_legacy_homes`) take S1's
  read and write halves, its row identity the pair (home, key); its typed-row compare, its marks and
  its write refusal on a new home (`#check_legacy_homes`) stay its own. Observed by AC5.
- **S3** — The join, `derive_unnamed_keys(rows, design)` in `policy.py`: the sorted names of the
  catalogue rows whose `name` is among no clause's backticked names, `extract_clause_tokens`
  (`tools/memory-tree/design_lib.py#extract_clause_tokens`), on the row's `owner` build in the design
  `read_design` returns (`tools/memory-tree/design_lib.py#read_design`). The design is read by
  `load_design(kit, root)` in `policy.py`: the memory-tree kit's `design_lib` found by the inlined
  `resolve_kit_dir` (`tools/policy/policy.py#resolve_kit_dir`), as `load_tree_lib` finds `tree_lib`
  (`tools/policy/check_policy.py#load_tree_lib`), over the caller's conf as `read_design_conf` reads
  it (`tools/memory-tree/design_lib.py#read_design_conf`). The kit already `requires` memory-tree
  (`tools/policy/kit.toml#requires`). Observed by AC1 and AC2.
- **S4** — The list `tools/policy/unnamed-keys.txt`, GENERATED by `python policy.py lists --write`
  and graded by `lists --check` through S1, read against the same one compare base `cmd_lists` reads
  for the other two lists (`tools/policy/policy.py#cmd_lists`). It is gov's own and withheld from
  installs, as `legacy-homes.txt` is: its name joins the `project-owned` `[[files]]` rule of
  `tools/policy/kit.toml`. Observed by AC1 and AC3.
- **S5** — The arm `arm_reader_join` in `ARMS` of `tools/policy/check_policy.py`
  (`tools/policy/check_policy.py#ARMS`), `empty = "announce"`: S1's findings over S3's set and S4's
  list. Every run prints its population, `<n> of <m> catalogue key(s) named on their owner's row ·
  <k> listed`. Where every `DESIGN_*` key is blank, as in every adopter, `read_design` raises its
  `DesignRefusal` naming them, and where the list is withheld, the arm prints `policy-check:
  arm_reader_join · not graded · <why>` and grades nothing. Its row in the kit README's "Each arm in
  an adopter" table (`tools/policy/README.md`). Observed by AC2, AC3 and AC6.
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
- **consumes-from** external — the policy kit's `check_list`, `write_list`, `read_base_pairs`, `check_legacy_homes`, `write_legacy_homes`, `resolve_compare_base`, `resolve_kit_dir`, `cmd_lists`, `ARMS` and `load_tree_lib`; memory-tree's `read_design`, `read_design_conf` and `extract_clause_tokens` in `tools/memory-tree/design_lib.py`; each landed at this spec's base

## 4. Design

### The factory

```
check_shrink_list(kit, name, derived, compare) -> ([(name, why)], note)
write_shrink_list(kit, name, header, derived)  -> removed names
```

Both halves are `check_list` and `write_list` with the list's file name, its derivation and its
header made arguments. `check_list` becomes `check_shrink_list(kit, LIST,
derive_unsummarised(load_catalogue(kit)), compare)`. The legacy list's rows carry three fields and a
mark and its write refuses a new home rather than draining, so it keeps its own compare and write
policy and reads its base and writes its file through S1's helpers; its reports stay word for word,
which its three fixture cases pin.

### The join

```
design = read_design(root, read_design_conf(root))        # memory-tree, DESIGN_* keys
names(build) = union of extract_clause_tokens(text) over design["builds"][build]
unnamed = sorted(row.name for row in catalogue if row.name not in names(row.owner))
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
| `check_shrink_list`, `write_shrink_list`, `derive_unnamed_keys`, `load_design` | functions | `tools/policy/policy.py` |
| `UNNAMED_LIST`, `UNNAMED_HEADER` | constants | `tools/policy/policy.py` |
| `tools/policy/unnamed-keys.txt` | generated list | new |
| `arm_reader_join` | arm | `tools/policy/check_policy.py` |
| `reader-join`, `reader-join-blank` | fixture cases | `tools/policy/check_policy.py` |

### Migration

The list is seeded by the first `lists --write`, with no list at the compare base, which seeds the
baseline as the legacy list's first write does.

### Files touched (estimate)

- `tools/policy/policy.py`: the factory, the join, `load_design`, `cmd_lists` reading the third list
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
  blank state is one finding naming the key and the cause.
- observability — the population line names named, total and listed counts.
- risks — the view changes when a deviation moves a clause, so a key can leave the list without this
  kit changing; the stale finding names it and `lists --write` drains it.
- testing — the two cases of the criteria below and the arm; the moved lists keep their existing
  cases.
- migration — the first write seeds the list.
- user docs — `help/policy.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python policy.py lists --write` then `python policy.py lists --check` run in gov's
  tree, the check exits 0 and prints `unnamed-keys.txt` with the count it carries.
  Red when: a listed key is now named, or the list misses an unnamed key.
  figure: the count is DERIVED by `derive_unnamed_keys` at each run.
  figure: PINNED 2026-11-21, 48 of 273 catalogue keys unnamed over the view at `31fbb903`, against the away pass's 116 of 220.
- **AC2** — When the `reader-join` case adds to its catalogue copy a row owned by `dKeptSession` that
  no clause names, `arm_reader_join` reds naming it as unnamed and not listed; when it plants a
  listed key that a clause of its owner's row names, the arm reds naming it stale; each unplanted
  copy is green.
  Red when: either plant reads green.
- **AC3** — When the `reader-join` case adds a name to the list above its base's copy, `python
  policy.py lists --check` exits 1 naming it as added to a shrink-only list.
  Red when: the list grows silently.
- **AC4** — When `grep -n "def check_shrink_list\|def write_shrink_list" policy.py` and `grep -c
  "check_shrink_list(\|write_shrink_list(" policy.py` run in the policy kit, two definitions print
  and the call count covers the three lists.
  Red when: a list keeps its own copy of the base read or the write.
- **AC5** — When `python check_policy.py --fixture list-grew` and the `legacy-homes`,
  `legacy-homes-main-dropped` and `legacy-homes-present` cases run after the move, each reads as it
  read before it.
  Red when: a moved list's verdict or message changes.
- **AC6** — When the `reader-join-blank` case runs `python check_policy.py --repo <dir>` over a
  scratch repository whose `.memory-tree.conf` leaves every `DESIGN_*` key blank, it prints
  `arm_reader_join · not graded` and no finding.
  Red when: the arm reds or reads green with nothing graded.
- **AC7** — When `grep -n "unnamed-keys" policy.md` runs in the help directory, it prints the
  paragraph naming how a key leaves the list.
  Red when: the page omits the list.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC6 · the `reader-join` cases' planted row, stale name and grown list, staged on copies of the catalogue and the list · none

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

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-11-21 · S1 S2 S3 S4 S5 · §3 · §4 · §5 · AC1 · §7 · §8 F1 · §10 · re-grounded on the
  landed tree at `c2a407b0` under the brief
  `2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief`: the policy kit and the
  memory-tree design reader are in the tree, so every function is cited by symbol; S3 names its
  design loader, `load_design`; S4 names the `kit.toml` rule that withholds the list; AC1's figure
  re-measured; F1's reason re-measured, its pick kept; the Gates line names the policy legs the
  Files touched trip; the shared join factory recorded as no fit. Nothing narrowed: no landed unit builds the factory, the join or the list.

## 10. Reuse audit

The seams extended: the policy kit's `check_list` and `write_list`
(`tools/policy/policy.py#check_list`, `#write_list`), the legacy list's `read_base_pairs`,
`check_legacy_homes` and `write_legacy_homes`, the one compare base `resolve_compare_base`, read once
in `cmd_lists`, and the arm shape of `arm_reader_coverage`
(`tools/policy/check_policy.py#arm_reader_coverage`) with its cross-kit load `load_tree_lib`; the
join input is memory-tree's `read_design` and `extract_clause_tokens`
(`tools/memory-tree/design_lib.py#read_design`, `#extract_clause_tokens`), its conf keys
`DESIGN_RECORD`, `DESIGN_BASELINE`, `DESIGN_VIEW` and `DESIGN_NODES` in `.memory-tree.conf`.
`python tools/codebase-map/reuse_lookup.py "shrink-only generated list checked against compare
base"`, re-run 2026-11-21, ranked `check`, `checks`, `resolve_compare_base` in
`tools/lib/compare_base.py` and its inlined copies, `resolve_generated_indexes` and `read_id_list`:
no list factory exists at this base. Its compare base is the one this factory reads; the shared join
factory `tools/lib/coverage_join.py` compares a TOML baseline, which no policy list is. `python
tools/memory-recall/query.py` with the terms below returned this build's brief, this spec and scout
A's row 6. Disagreement: the brief's 116 of 220 is the away pass's figure; the predicate over today's
view and catalogue gives the AC1 figure.

Recall terms used: catalogue reader join unnamed keys shrink-only list owner build row clause tokens gap-spine-10
