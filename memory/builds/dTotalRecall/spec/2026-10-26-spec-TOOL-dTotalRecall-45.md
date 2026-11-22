# TOOL-dTotalRecall-45 — the four id readers outside unit 38's table parse through the grammar, each site held gone by file and line

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base 8b8b1374 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-45-deviation-451.md](../build/2026-10-26-build-TOOL-dTotalRecall-45-deviation-451.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-45-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-45-reground-return.md) | research | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-45-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-45-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 35 at HIGH**. It shares item **H1** with id 1, which `TOOL-dTotalRecall-44`
closes. Unit 38's AC3 greps three kits for one quote style only, so it certifies readers it never
reads. Three id readers outside its table split, each read at base `462d20f3` and again at `8b8b1374`:

- `tools/branch-reconcile/branch_reconcile.py#derive_names` adds `i.split("-")[1]` for each id
  `ID_RE.findall` returns from a commit subject (`tools/branch-reconcile/branch_reconcile.py@462d20f3:520`,
  unmoved at `8b8b1374`);
- `tools/memory-tree/row_grammar.py#scan_records` keys each row's `slug` as `rid.split("-")[1]`
  (`tools/memory-tree/row_grammar.py@462d20f3:1116`, `tools/memory-tree/row_grammar.py@8b8b1374:1001`);
- `tools/memory-tree/gen_build_index.py#render_spec_skeleton` writes the node as
  `spec_id.split('-')[1][0]`, single-quoted, which AC3's `"-"` pattern misses
  (`tools/memory-tree/gen_build_index.py@462d20f3:8576`, `tools/memory-tree/gen_build_index.py@8b8b1374:9750`).

A fourth landed after base. `tools/policy/check_policy.py#derive_run_kind` (TOOL-dLandedOwners-1,
`c5255c179`) tests each ask id of a build's `BACKLOG.md` with `a.split("-")[1] == build`
(`tools/policy/check_policy.py@8b8b1374:564`). `TOOL-dTotalRecall-44` rev-3 §8 F2 found it with the
shape-keyed census and handed it here.

Under the hyphenated `in-slug` flip, the first, second and fourth answer `d2026` for
`TOOL-d2026-10-26ClosedLoop-3`, so `derive_run_kind` reads a spec run as a build run. The third still
answers `d`, because a slug's first character is its node whatever follows it, but it is a split the
census lists and no parse holds it. This unit re-points the four and holds every split id reader gone
by file and line, in both quote styles, over the whole tool root. It repairs `TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — `derive_names(subject, top)` in `tools/branch-reconcile/branch_reconcile.py` takes each
  id's slug from `parse_id_parts(i, top)`. It reaches the parser as `TOOL-dTotalRecall-5` §4 "The
  readers" routes a kit that does not require memory-tree: the module's `resolve_kit_dir` copy and
  inline `slug_legacy_py` block, which unit 5 S8 adds at order 7. At HEAD the module carries neither
  (`git grep -n "def resolve_kit_dir" -- tools/branch-reconcile` prints nothing). Where that route
  reports memory-tree unresolved, the slug is the text between the id's first and last hyphen, since
  the legacy shape admits no hyphen in a slug. An id the parser refuses adds no slug. `top` is the
  repository top, which `read_repo_top(inv)` reads once per inventory (§4 "The roots"). Observed by AC1.
- **S2** — `render_spec_skeleton` writes the node as `slug[0]`, `slug` a new keyword-only parameter,
  and reads no part of `spec_id` for it. `cmd_new_spec` passes `parse_id_parts(spec_id, root)[1]` and
  raises an id the parser refuses as the `Problem` naming it. Each of the seven self-test calls passes
  its fixture slug, `aFix` (§8 F2). Observed by AC2.
- **S3** — `scan_records` in `tools/memory-tree/row_grammar.py` keys a row's `slug` from
  `parse_id_parts(rid, root)`, reached by a sibling `import id_grammar` inside the function, and a row
  id the parser refuses keeps `""`. Observed by AC3.
- **S4** — The site assertion. The pass records, in its commit's `Decided:` trailer, the fourteen
  split sites of unit 38's §1 and this unit's §1 by file and line text at the pass base. Observed by AC4.
- **S5** — `derive_run_kind` in `tools/policy/check_policy.py` compares `parse_id_parts(a, repo)[1]`
  with `build`, and an ask id the parser refuses matches no build. It reaches the parser through its
  `readers` argument: `RUN_READER_MODULES` gains `id_grammar` as its last member, so `load_run_readers`
  checks and imports it with the others and returns it fourth, and `derive_landed_builds` hands the
  five-module `readers` on. A `ConfError` from the grammar is raised as the `policy.Refusal` naming
  `.memory-tree.conf`, as the function's other reads refuse. The two docstrings that list the modules
  and the README's `arm_reader_coverage` row name the fifth. Observed by AC5.

## 3. Non-goals (OUT)

- The ten readers of unit 38's table: `TOOL-dTotalRecall-38`'s.
- The census predicate: `TOOL-dTotalRecall-44`'s.
- The family readers `tools/memory-tree/gen_build_index.py#cmd_asks` and
  `tools/memory-tree/backlog.py#render_family_view`. Each takes index 0, which a hyphen in the slug
  cannot move, so each stays as it is.
- `branch_reconcile.py`'s own `ID_RE`, whose slug class admits no hyphen, and the module's route to
  `id_grammar`; `cmd_new_spec`'s own id match; and `tools/memory-tree/row_grammar.py#id_pattern`:
  unit 5's re-points at order 7, which AC1 to AC3 and AC5 need in the flipped clone. Where
  `cmd_new_spec`'s match still refuses a hyphenated slug, `TOOL-dTotalRecall-60` S14 re-points it.
- The parser's per-root cache and its `ConfError`: `TOOL-dTotalRecall-66` S35 and S39.
  `derive_names` and `scan_records` let `ConfError` pass, as the parser does.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — branch-reconcile's `resolve_kit_dir` copy and
  `slug_legacy_py` block (its S8), the grammar-bound id matches of `ID_RE`, `cmd_new_spec` and
  `row_grammar.py#id_pattern`, and the flipped clone of its §4 "The flips", in which AC1 to AC3 and
  AC5 run
- **consumes-from** `TOOL-dTotalRecall-38` — the re-point routes of its S3, which the four readers
  here take, and its census, whose kept hits name this unit
- **hands-off** `TOOL-dTotalRecall-53` — the three further re-pointed readers, which that unit holds to their base answers for the flat and node-scoped eras (ids 2 and 23)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts`, landed at step 8; without it the four readers of §4 raise at this pass (the round-1 audit of units 44 to 53, id 2)
- **hands-off** `TOOL-dTotalRecall-60` — `render_spec_skeleton`'s re-point and AC2: the keyword `slug`, the refusal and the fixture slug of its S7 to S9, landed here (§8 F2), which that unit re-observes, and the flipped command of its S14 (the round-1 audit of units 44 to 53, ids 2, 10, 16, 17, 29 and 42)

## 4. Design

### The four readers

| Site | At `8b8b1374` | After |
|---|---|---|
| `tools/branch-reconcile/branch_reconcile.py#derive_names` | `{i.split("-")[1] for i in list(names)}` | the slug of `parse_id_parts(i, top)`, skipped on `ValueError` |
| `tools/memory-tree/gen_build_index.py#render_spec_skeleton` | `spec_id.split('-')[1][0]` | `slug[0]`, `cmd_new_spec` passing `parse_id_parts(spec_id, root)[1]` |
| `tools/memory-tree/row_grammar.py#scan_records` | `rid.split("-")[1]` | `parse_id_parts(rid, root)[1]`, `""` on `ValueError` |
| `tools/policy/check_policy.py#derive_run_kind` | `a.split("-")[1] == build` | `parse_id_parts(a, repo)[1] == build`, false on `ValueError` |

### The roots

The parser reads `<root>/.memory-tree.conf` and raises `ConfError` where none sits
(`tools/memory-tree/id_grammar.py#resolve`), so each reader passes the root its tree's conf sits at.

- `derive_names`: `branch_reconcile.py --root` takes any path inside the repository
  (`tools/branch-reconcile/branch_reconcile.py#main`), so `inv["root"]` may name a subdirectory.
  `tools/branch-reconcile/branch_reconcile.py#read_memory_root` already reads the top with
  `rev-parse --show-toplevel` inside its loader. The pass extracts that read into
  `read_repo_top(inv)`, cached under its own `read_cached` key, which `read_memory_root` and
  `derive_coverage` both call. Both calls of `derive_names` sit in
  `tools/branch-reconcile/branch_reconcile.py#derive_coverage`, and no suite calls it (`git grep -n
  "derive_names" -- tools` lists the two and the definition, DERIVED 2026-11-22). Where unit 5's pass
  has landed a top read in this module for its `ID_RE`, the pass uses that one and mints none. The
  branch-reconcile selftest copies `branch_reconcile.py` into a tree without memory-tree, where the
  legacy answer of S1 applies.
- `render_spec_skeleton` holds no root, and `cmd_new_spec` holds one. The self-test's fixture id
  `ARCH-aFix-3` names a family this repository does not declare (`.memory-tree.conf:42`), so a parse
  inside the function would raise on every self-test call (§8 F2).
- `scan_records`: its own `root`. Its callers `check_relations`, `cmd_measure_relations` and
  `check_content` are unchanged. The import is plain, the module having put its own directory on
  `sys.path` at import. It is not `load_index_builder`, whose refusals name check 27's arming key,
  which check 28's `check_content` does not read. `scan_engine_imports` bans only the two engines
  `tools/memory-tree/row_grammar.py#ENGINE_OWNERS` names, and `id_grammar` is neither.
- `derive_run_kind`: `repo`, the root its caller judges. The grammar is read from the worktree's conf,
  while the families its other reads take come from the landed revision's (`derive_landed_builds`);
  the two differ only where the worktree's conf has moved past that revision, which this unit does not
  check.

### The policy readers

`tools/policy/check_policy.py#RUN_READER_MODULES` lists `gen_build_index`, `backlog`, `row_grammar`
and `design_lib` at HEAD. Appended last, `id_grammar` leaves the `kit-modules-absent` refusal naming
`gen_build_index.py` first, as the README's `reader-coverage-carried` paragraph states, and
`tools/policy/check_policy.py#build_carried_repo` copies each member beside `tree_lib.py`, so the
`policy fixtures` cases carry it. `load_run_readers` returns `(gen_build_index, backlog, row_grammar,
id_grammar)`; its one caller, `derive_landed_builds`, unpacks four and builds `readers` of five, and
`derive_run_kind`, called there alone, unpacks five. `tools/loop/termination.py` reaches these only
through `derive_landed_owners` and sees no change.

### Inventory

Minted: `read_repo_top` in `tools/branch-reconcile/branch_reconcile.py`, and the keyword `slug` of
`render_spec_skeleton`. Naming cell: `python tools/lexicon/lexicon.py --suggest read_repo_top --as
py.function` printed `OK` on 2026-11-22.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/row_grammar.py`
- `tools/policy/check_policy.py`
- `tools/policy/README.md` (the `arm_reader_coverage` row)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Keep the splits and assert only by grep.** The grep is the assertion; the readers still answer
  `d2026` under the flip until they parse through the grammar.
- **Strip the first and the last segment in each reader.** It answers right under a hyphenated slug,
  but it is a second id parser beside unit 54's, which the charter's reuse rule refuses; S1 keeps it
  only for the legacy shape, where no parser resolves.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — the parser builds the grammar per call until `TOOL-dTotalRecall-66` S35 caches it
  per root; `scan_records` calls it once per keyed row, 330 rows here (DERIVED 2026-11-22, a
  `scan_records` probe at HEAD), at about a quarter of a millisecond a call, measured the same day.
- error / empty / loading states — an id the parser refuses yields no slug, `""`, no match or, in
  `cmd_new_spec`, the `Problem` naming it; `ConfError` passes out of `derive_names` and `scan_records`
  as out of the parser, and is a `policy.Refusal` in `derive_run_kind`.
- observability — none new.
- risks — `derive_names` gains a parameter and `load_run_readers` a member; every caller is in its own
  module and changes with it. The policy fixture's grammar read rides unit 5's policy read from a kit
  copy.
- testing — AC1 to AC5 by the pass; the arm of §7 at the close.
- migration — none: the default grammar gives the same slug for every unhyphenated id, and a flat-era
  or node-scoped id reaches none of the four, since `ID_RE`, the row regex and `cmd_new_spec`'s match
  each require a slug and a sequence.
- user docs — none under `help/`: `help/policy.md` names no reader module.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `derive_names("TOOL-d2026-10-26ClosedLoop-3 fix", <clone>)`
  from the clone's `branch_reconcile.py`, in the flipped clone `TOOL-dTotalRecall-5` §4 "The flips"
  makes, the slug `d2026-10-26ClosedLoop` is in its answer.
  Red when: the answer holds `d2026`.
  fixture: the flipped scratch clone; the pass makes it under the run's scratch directory.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --new-spec TOOL-d2026-10-26ClosedLoop-3
  --tier 2` runs in the same clone, the written header reads `node d`, as it does at base; and a
  `python -c` probe calling `render_spec_skeleton` with `spec_id="TOOL-dFoo-3"` and `slug="xFoo"`
  gets a header reading `node x`.
  Red when: the node is read from `spec_id`, or the command refuses the hyphenated id.
- **AC3** — When a `python -c` probe runs `scan_records` from the clone's `row_grammar.py` over the
  clone holding one committed decision row `TOOL-d2026-10-26ClosedLoop-3`, that row's `slug` is
  `d2026-10-26ClosedLoop`.
  Red when: the slug is `d2026`.
- **AC4** — When `git grep -nE "\.split\(['\"]-['\"]\)" -- tools` runs at the pass tip, its output
  holds none of the fourteen sites S4 records, each matched by file and by the line's text.
  Red when: any one of them still splits, in either quote style.
- **AC5** — When a `python -c` probe in the clone loads the readers as `derive_landed_builds` does,
  through `load_tree_lib` and `load_run_readers`, and calls `derive_run_kind` for the build
  `d2026-10-26ClosedLoop` at a clone commit whose `BACKLOG.md` holds the open ask
  `TOOL-d2026-10-26ClosedLoop-9` and whose README's `roster:units` pair names a unit no spec defines,
  it answers `spec`.
  Red when: it answers `build`, the split's `d2026` matching no build.
  fixture: that commit, added to the flipped clone by the pass.

## 7. Gates

`branch-reconcile selftest` · `build-index selftest` · `row-grammar selftest` · `tier2-review self-test` · `policy fixtures` · `routed-commits selftest` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `memory hygiene` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/row_grammar.py · covers AC3 · a `_tree` fixture whose committed `.governance/policy.toml` carries unit 5's hyphenated `in-slug` flip and whose decision index holds one row `ARCH-d2026-10-26ClosedLoop-3`, its `slug` asserted whole, in the row-grammar selftest, staged by restoring the split · none

`policy fixtures`, `routed-commits selftest` and `scratch-guard self-test` are the legs whose guards
name `tools/policy/` (`tools/gate-legs.json`); `policy fixtures` also names `gen_build_index.py` and
`row_grammar.py`, and its `reader-coverage-carried` cases run `derive_run_kind` on the parser.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does `render_spec_skeleton`'s re-point keep `build-index selftest` green at this pass?**
  Rev-2's `parse_id_parts(spec_id, root)[1][0]` had no root in the function, and under the default
  grammar the self-test id `ARCH-aFix-3`, of an undeclared family, raises `ValueError` at each of its
  seven calls. `TOOL-dTotalRecall-60` S7 to S9 repair that at order 31, after this pass (the round-1
  audit of units 44 to 53, ids 16 and 42). Options: (a) land unit 60 S7 to S9's shape here: a
  keyword-only `slug`, the node `slug[0]`, `cmd_new_spec` passing the parser's slug and refusing as a
  `Problem`, the fixture calls passing `slug="aFix"`; (b) a keyword `root`, each self-test call given a
  scratch tree whose conf declares `ARCH`; (c) hand the site to unit 60 and keep it in the `Decided:`
  trailer. (c) leaves a split AC4 holds gone (veto 1). (a) and (b) both meet AC2 and AC4, and (b)
  leaves unit 60 S7 to replace the signature again. RESOLVED (agent, 2026-11-22, delegated): (a), the
  most feature-rich survivor; unit 60 S7 to S9 re-observe the landed shape. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 35
  (HIGH, item H1 shared with id 1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-11-22 · §1 · S1 to S5 · §3 · §4 · §5 · AC1 to AC5 · §7 · §8 · §10 · re-grounded at
  base `8b8b1374` per `2026-11-22-prompt-TOOL-dTotalRecall-45-reground-brief`: readers cited by
  symbol, lines blob-pinned; S5 and AC5 take `tools/policy/check_policy.py#derive_run_kind`, handed
  here by TOOL-dTotalRecall-44 rev-3 §8 F2, so S4 and AC4 hold fourteen sites; S1 passes the
  repository top through `read_repo_top` and names unit 5 S8's route, which HEAD lacks; S2 lands unit
  60 S7 to S9's keyword `slug` (F2); S3 names its import; AC2 carries `--tier 2`; §3 gains the edge
  with TOOL-dTotalRecall-5; §7 gains the three legs whose guards name `tools/policy/`.

## 10. Reuse audit

The seam extended is `parse_id_parts` in `tools/memory-tree/id_grammar.py`, which `TOOL-dTotalRecall-54`
lands at step 8 on `tools/memory-tree/tree_lib.py#build_id_token_re`; each reader reaches it by the
route `TOOL-dTotalRecall-5` §4 "The readers" gives its kit, and no second parser is written:
`git grep -nE "def (split_id|parse_id|id_parts|parse_id_parts)" -- tools` printed nothing at
`c2143acf3`. The policy reader extends `tools/policy/check_policy.py#load_run_readers` and its
`RUN_READER_MODULES`, the kit's one load of memory-tree modules. `read_repo_top` extracts the top read
`read_memory_root`'s loader spells, its second instance being `derive_names`' root, through the
module's own `read_cached`. No existing seam fits it: `python tools/codebase-map/reuse_lookup.py
"resolve the repository top level directory from any path inside it"` ranked `resolve`,
`resolve_kit_dir` and `resolve_bash`, none of which reads a repository top.
`python tools/codebase-map/reuse_lookup.py "take the slug out of a unit id"` ranked name-stem
neighbours (`parse`, `slug`) and no id parser at base, which is the parser unit 54 mints.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
