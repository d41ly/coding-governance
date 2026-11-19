# TOOL-dLandedOwners-4 — the closing review's promoted findings: the kit threaded to every resolver, a failing case for each landed-predicate arm, every withheld file checked, one git-read refusal and the docs aligned

**Status:** SPECCED · rev-1 · 2026-11-19 · node d · Tier-2 · base 515a3e6c · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dLandedOwners-4-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-4-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Close every item of the closing diff review of units 1 to 3,
`memory/builds/dLandedOwners/reviews/2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md`:
M1 to M5 and L1 to L4, the batch the build method's diff-exit rule promotes into one unit. The
shipped predicate already computes the right answer; what this unit adds is a case that can fail on
each of its arms, one resolution root per call, a withheld set read from its one source, a git
failure reported as one, and docs that state what the code does.

## 2. Scope (IN)

- **S1** — M1. `derive_run_kind` takes the modules its caller loaded, as one argument `readers`,
  and resolves no kit of its own. `derive_landed_builds` loads `tree_lib` and the run readers once
  per call, from its `kit`, and hands them on. Observed by AC1 and AC2.
- **S2** — M1's case. `reader-coverage-carried` gains the sub-case `kit-root-threaded`, run with
  the kit resolver refusing every root but the kit copy's, and its `kit-modules-absent` sub-case
  requires the Refusal to name the kit copy's memory-tree directory. Observed by AC2.
- **S3** — M2. `derive_withheld_names(kit)` in `tools/policy/check_policy.py` reads the file names
  the `project-owned` rules of `kit`'s `kit.toml` include. `legacy-homes-withheld-install` checks
  the plan row and the applied target for each such name, `adopter-fresh-target`'s stray check
  reads the same set, and `legacy-homes-present` requires both lists the kit's code reads,
  `legacy-homes.txt` and `unscanned-readers.txt`, among those names. Observed by AC3 and AC4.
- **S4** — M3. The sub-case `landing-other-base`, whose only landing merge carries a base other
  than the one its run record at L carries. Observed by AC5.
- **S5** — M4. The sub-case `rotated-landed`, whose run record at L is `RUN.LANDED.<8 hex>.md`.
  Observed by AC6.
- **S6** — M5. The sub-cases `disposed-ask-landed`, whose ask a status row disposes, and
  `roster-specced-landed`, whose open ask meets a roster with every unit specced. Observed by AC7.
- **S7** — L1. `read_git_or_refuse(repo, *args)` raises `policy.Refusal` naming the git read when
  `policy.run_git` answers None. The two reads of `derive_scanned_files` and the tracked-path read
  of `check_reader_coverage` call it. Observed by AC8.
- **S8** — L2. `help/policy.md` says a row of `unscanned-readers.txt` splits on runs of whitespace,
  spaces or tabs. Observed by AC9.
- **S9** — L3. `derive_withheld_names(kit_dir)` in `tools/govkit/govkit.py`, read by the three
  govkit copies of the policy kit for their ignore list, so no copy spells a withheld name.
  Observed by AC10.
- **S10** — L4. The module docstring of `tools/policy/check_policy.py` states the landed predicate
  as `derive_landed_builds` reads it. Observed by AC11.
- **S11** — The kit README's paragraphs on reader coverage, `reader-coverage-carried`,
  `legacy-homes-withheld-install` and `legacy-homes-present`, and one sentence of `help/policy.md`
  on a failed git read, state what S1 to S7 build. Observed by AC12.
- **S12** — The bug class M1 names, as the record under `memory/gotchas/` that §4 "The bug class"
  gives, with the index re-rendered, its claim in the policy dossier and the map re-rendered.
  Observed by AC13.

## 3. Non-goals (OUT)

- Any change to what the landed predicate answers or to the reader scan's shapes. Every sub-case
  this unit adds must pass on the shipped predicate; a sub-case that does not is a defect in the
  predicate, and the builder stops and reports it as a divergence.
- What the govkit copies of the playbook and memory-tree kits hold, beyond the policy kit's
  withheld set that `stale_edges.py` already applies to them.
- The review's left-shift gates §4 "The left-shifts" marks as not taken: a mutation pass over the
  policy fixtures, a lint of `run_git(...) or ""`, a govkit selfcheck arm against a restated
  ignore list, and the harness-arms leg reading Python return arms. Each is a gate of its own.
- The loop kit; dDeclaredLoop's pending termination row, which ask `TOOL-dLandedOwners-5` carries;
  the owner's flagged bar.

### Edges

- **hands-off** external — a mutation pass for the `policy fixtures` leg that stubs each conjunct of
  the landed predicate and each alternative of `RUN_RECORD` and requires a case to go red (M3, M4)
- **hands-off** external — a `policy check` lint that reds `run_git(...) or ""` outside an
  allow-list of reads whose empty output is valid (L1)
- **hands-off** external — a govkit selfcheck arm that reds an ignore list restating a withheld
  name (L3)

## 4. Design

### What the tree holds today

- `derive_run_kind` calls `load_tree_lib_or_refuse()` and `load_run_readers()` with no argument,
  so both resolve from the module's `KIT`; `derive_landed_builds` resolves the same modules from
  its `kit` and calls `derive_run_kind` once per candidate base
  (`tools/policy/check_policy.py#derive_run_kind`, `tools/policy/check_policy.py#derive_landed_builds`).
  It is its only caller, by `git grep -n derive_run_kind -- tools/` on 2026-11-19 (PINNED).
- Run at this spec's base with `kit="tools/policy"` and a spy on `resolve_kit_dir`,
  `derive_landed_builds` over dDeclaredLoop and dSafePassage resolved 8 times (PINNED, 2026-11-19),
  2 from the given root and the rest from the module's absolute `KIT`: AC1's probe.
- `load_tree_lib` and `load_run_readers` call the module global `resolve_kit_dir`, which is
  `policy.resolve_kit_dir` (`tools/policy/check_policy.py#load_tree_lib`,
  `tools/policy/check_policy.py#load_run_readers`). `load_run_readers` checks each module's file
  before it imports, so `sys.modules` cannot hide a missing file.
- `build_carried_repo` writes `RUN.md` once, as `RC_RUN.format(base)` on the branch `run`, and
  writes `BACKLOG.md` only for `spec-run-landed`, with `RC_ASK` and no status row
  (`tools/policy/check_policy.py#build_carried_repo`). `RC_CARRIED` maps each sub-case to the count
  it grades or the text its Refusal names (`tools/policy/check_policy.py#RC_CARRIED`).
- `run_legacy_withheld_install`, the stray check of `run_fresh_target` and `run_legacy_present`
  each name `policy.LEGACY_LIST` alone (`tools/policy/check_policy.py#run_legacy_withheld_install`,
  `tools/policy/check_policy.py#run_fresh_target`, `tools/policy/check_policy.py#run_legacy_present`).
  `run_legacy_present` already reads the `project-owned` rules out of `kit.toml` with `tomllib`.
- The `project-owned` rule includes both lists
  (`tools/policy/kit.toml@da41b1f18986442d5465db015b7c9f40d5a467b2:35`).
- `derive_scanned_files` and `check_reader_coverage` read git through `policy.run_git(...) or ""`,
  and `policy.run_git` answers None on a non-zero exit or an OSError
  (`tools/policy/check_policy.py#derive_scanned_files`, `tools/policy/check_policy.py#check_reader_coverage`,
  `tools/policy/policy.py#run_git`). Each failing read, staged by AC8's probe at this spec's base,
  printed no Refusal (PINNED, 2026-11-19).
- The three govkit copies spell `shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt")`
  (`tools/govkit/shims.py@e70d5f7e0a01eab28248ad7e7032a17e89c879e2:428`,
  `tools/govkit/fixtures/stale_edges.py@a14d44cb632b7255dc276f2dbdfdd4e280ef55b9:44`,
  `tools/govkit/fixtures/retired_edits.py@2688653ee63f64c85b571609241e240ebd823b22:138`).
  `stale_edges.py` applies its one `IGNORE` to its policy, playbook and memory-tree copies.
- `help/policy.md` says "first two runs of spaces"
  (`help/policy.md@b502511ca62f7d2e8066012c21da59f31f3fa8ff:170`), while
  `tools/policy/check_policy.py#read_unscanned_readers` splits with `line.split(None, 2)`.
- The module docstring defines landed as "every spec in its build folder terminal at the landed
  revision" (`tools/policy/check_policy.py@782ffc07d438b13df81bf6dde4c7395739f11eca:20`).

### The kit threaded (M1)

`derive_run_kind(repo, build, base, conf, families, readers)`: `readers` is the tuple
`(tree_lib, gen_build_index, backlog, row_grammar)`. Its body reads those four names out of
`readers` and calls no loader. `derive_landed_builds` keeps `tree_lib` from its
`load_tree_lib_or_refuse(kit)`, takes the three run readers from its one `load_run_readers(kit)`,
and passes the four to every `derive_run_kind` call. Each docstring says where the modules come
from. Nothing about what either function answers changes.

### The carried sub-cases (M1, M3, M4, M5)

`RC_CARRIED` keeps its shape, `sub-case -> count graded or Refusal text`, and gains five entries.
`build_carried_repo` reads its sub-case by name, as it reads `spec-run-landed` today. It mints one
constant, `RC_DISPOSAL`, the status row `- WONTDO · TOOL-bPlanted-9 · the ask is withdrawn`, which
`tools/memory-tree/backlog.py#extract_row` reads as class `status`, verb `WONTDO`, by a probe on
2026-11-19. Every new sub-case lands through a `--no-ff` merge of `run` into main.

| Sub-case | `BACKLOG.md` at B | Unit 2 spec at B | Units 1 and 2 on `run` | After the landing merge, on main | Graded |
|---|---|---|---|---|---|
| `kit-root-threaded` | none | `OPEN` | `CLOSED`, `DEFERRED` | nothing | 1 |
| `landing-other-base` | none | `OPEN` | `CLOSED`, `DEFERRED` | a commit writing `RUN.md` with `base:` the landing merge | 0 |
| `rotated-landed` | none | `OPEN` | `CLOSED`, `DEFERRED` | a commit renaming `RUN.md` to `RUN.LANDED.<B's first 8 hex>.md` | 1 |
| `disposed-ask-landed` | `RC_ASK`, then `RC_DISPOSAL` | absent | `DEFERRED`, `DEFERRED` | nothing | 1 |
| `roster-specced-landed` | `RC_ASK` | `OPEN` | `CLOSED`, `DEFERRED` | nothing | 1 |

Why each can fail, and on what:

- `landing-other-base`: L's record carries the merge's own commit, and the only merge touching
  `RUN.md` carries B. With the intersection `bases[b] &` in `derive_landed_builds` the landing set
  is empty and nothing is graded. Without it, B lands, `derive_run_kind` answers `build`, and the
  sub-case grades 1.
- `rotated-landed`: L holds no `RUN.md`, so only the rotated alternative of `RUN_RECORD` lists a
  record. The merge log still finds the landing merge on the `RUN.md` path, whose `RUN.md` carries
  B. With `RUN_RECORD` narrowed to `^RUN\.md$` no record is listed and the sub-case grades 0.
- `disposed-ask-landed`: the ask is disposed, so `derive_run_kind` answers `build` before it reads
  the roster. With the disposal arm broken, the ask reads open, unit 2 has no spec at B, the answer
  is `spec`, and the sub-case grades 0.
- `roster-specced-landed`: the ask is open and every roster unit is specced at B, so only the last
  line of `derive_run_kind` answers, `build`. Made to answer `spec`, the sub-case grades 0.
- `kit-root-threaded`: `run_reader_carried` sets the module global `resolve_kit_dir` to a nested
  `resolve_copy_only(home, anchor, here)` for this sub-case's `check_reader_coverage` call alone,
  restoring it in a `finally`. `resolve_copy_only` raises a `LookupError` naming `here` when
  `Path(here).absolute()` is not the kit copy's, and otherwise answers as the saved resolver does.
  On the base's code, `derive_run_kind` resolves from `KIT`, so the call refuses naming the policy
  kit's own path and the case prints `WRONG`. Threaded, it grades 1.

`kit-modules-absent` keeps its Refusal text, `gen_build_index.py`, and its check also requires the
kit copy's memory-tree directory, the directory `build_carried_repo` copies the modules into, as a
POSIX path inside the Refusal's `why`. A Refusal naming a root other than the copy's fails it.
Neither refusal case can be hidden by `sys.modules`: `resolve_copy_only` refuses before any import,
and `load_run_readers` checks each file before it imports.

Every module a sub-case copies is the set `build_carried_repo` copies today, `tree_lib` and
`RUN_READER_MODULES`, each under the `policy fixtures` guard in `tools/gate-legs.json`, as unit 1's
divergence record requires
(`memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-divergence-1.md`).

### The withheld set (M2)

`derive_withheld_names(kit)` answers, in rule order, each `include` of each `[[files]]` rule of
`<kit>/kit.toml` whose `role` is `project-owned`, a string include as a one-name list. It is the
expression `run_legacy_present` holds today, extracted; a `kit.toml` that does not read raises as
`tomllib` and `open` raise, and each caller reports it as it reports that read today.

- `run_legacy_withheld_install` reads the names from `KIT`. For each name it records one `plan`
  check, exactly one row ending `/<name>` and that row `ORDER [project-owned]`, and one `apply`
  check, no file of that name under the target. The receipt and exit checks stay once. An empty
  name list is one `WRONG`, `kit.toml withholds nothing, so this case checks nothing`.
- `run_fresh_target`'s stray check flags a held file whose basename is any of the names, and its
  green line says `no withheld file installed` and lists them.
- `run_legacy_present` keeps its two checks and requires each of `policy.LEGACY_LIST` and
  `UNSCANNED_LIST` among the names, one check per list. These two constants are the names the
  kit's readers open, so a rule edited to drop one reds here even though the install case, driven
  from the same rule, would no longer look for it.

### One git read that refuses (L1)

`read_git_or_refuse(repo, *args)` returns `policy.run_git(repo, *args)` and raises
`policy.Refusal(Path(repo).as_posix(), 0, "git <args> failed, so reader coverage cannot read the tree")`
when that answers None, `<args>` the arguments joined by spaces. Its callers:
`derive_scanned_files`' `rev-parse --show-prefix` at `kit` and its `ls-files` over
`CODE_PATHSPECS`, and `check_reader_coverage`'s `--literal-pathspecs ls-files` over the declared
paths. Empty output stays valid at each: a kit at the repository root has an empty prefix, and a
repository may track no code. Every other `policy.run_git(...) or ""` in the module is left as it
is. `arm_reader_coverage` already turns a Refusal into its one finding.

### The govkit copies (L3)

`derive_withheld_names(kit_dir)` in `tools/govkit/govkit.py`, read through `load_toml`, answers as
the policy kit's helper does. `tools/govkit/shims.py#run_forward_plant` and
`tools/govkit/fixtures/retired_edits.py#build_retired_gov` pass the policy kit directory they
already resolve, and spread the names into their `ignore_patterns` after `"__pycache__"` and
`"*.test.sh"`. `tools/govkit/fixtures/stale_edges.py#IGNORE` is derived the same way, at module
scope, from the policy kit directory that
`govkit.resolve_kit_dir("policy", "policy.py", govkit.GOVKIT_DIR)` answers, so its three copies
ignore what they ignore today plus `unscanned-readers.txt`.

Which, under M3 of the build method. The options were (a) every copied kit's own withheld names,
(b) the policy kit's withheld names wherever the policy kit's set is applied today, and (c) the
literal `"unscanned-readers.txt"` added at each site. (a) also drops `core-pending.txt` and
`instructions-legacy.txt` from `stale_edges.py`'s playbook copy, whose effect on that fixture's
observations is UNVERIFIED and no review item asks for; §3 rules it out, so the first veto
discards it. (b) and (c) trip no veto. (b) is ratified: it closes the drift the finding names and
leaves no restated set to drift again, where (c) leaves the same follow-up the review found.

### The docs (L2, L4, S11)

- `help/policy.md`, the "A declared key" bullet: "split on the first two runs of whitespace, spaces
  or tabs, so the path holds no whitespace". The "Every run says what it graded" bullet gains: a
  git read the check makes that fails stops it with one finding naming the read.
- The module docstring's `arm_reader_coverage` clause: "reds a catalogue key whose owner build has
  landed by `derive_landed_builds` (every spec terminal at the landed revision, or a build-kind run
  record with a first-parent landing merge, TOOL-dLandedOwners-1)". `git grep` for "terminal at the
  landed revision" over `tools/`, `help/` and `README.md` then finds no copy of the old clause.
- `tools/policy/README.md`: the arm paragraph says half 2 loads the run readers once and hands
  them to `derive_run_kind`, and the arm table's findings cell and the arm paragraph say that a
  git read of reader coverage that fails is a Refusal naming it. The `reader-coverage-carried`
  paragraph names every sub-case and drops its typed count of repositories. The
  `legacy-homes-withheld-install` text says it checks every withheld file, each name the
  `project-owned` rules of `kit.toml` include, and the `legacy-homes-present` text says both lists
  must be among those names.

### The left-shifts

| Item | The review's gate | Taken here | Class the checklist carries |
|---|---|---|---|
| M1 | a case where only the copy's root resolves; record the class | yes: `kit-root-threaded` and the record of §4 "The bug class" | `kit-argument-dropped-at-an-inner-call`, new |
| M2 | the install case driven from `kit.toml`'s `project-owned` includes | yes, with the descriptor check keyed on the readers' constants | `rule-stated-with-no-check-that-fails` |
| M3 | a mutation pass stubbing each predicate conjunct | no: a gate over the fixture leg's own source, its own unit; §3 Edges | `rule-stated-with-no-check-that-fails` |
| M4 | each alternative of a record-name regex planted, checked by that pass | the rotated alternative is planted; the pass is M3's | `rule-stated-with-no-check-that-fails` |
| M5 | the harness-arms discipline over `derive_run_kind`'s returns | no: `tools/memory-tree/check-arms.py` discovers shell `fail` branches only, by its docstring; each return arm is reached by a sub-case here | `refusal-branch-with-no-arm` |
| L1 | a `policy check` lint of `run_git(...) or ""` | no: a new arm, its own unit; §3 Edges | `staged-break-substitutes-a-synthetic-value` |
| L2 | a row grammar stated once, the other docs pointing to it | no gate fits a sentence; the wording is fixed | `two-answers-to-one-question` |
| L3 | one shared helper, and a govkit selfcheck arm against a restatement | the helper, yes; the arm, no; §3 Edges | `two-answers-to-one-question` |
| L4 | grep every prose restatement when a predicate is replaced | yes, as AC11's grep | `amendment-leaves-its-other-half-standing` |

Every class but the first exists under `memory/gotchas/`, so only the first owes a record.

### The bug class

`memory/gotchas/kit-argument-dropped-at-an-inner-call.md`, front matter verbatim:

```
---
name: kit-argument-dropped-at-an-inner-call
description: a function that takes a resolution root calls a helper that resolves again from its own default root, so the caller's root is honoured at one call and silently replaced at the next
kind: class
universal: false
---
```

Its body holds a Symptom, a Where it bit naming this build's review record and M1, and The fix:
thread the root, or hand the callee what the caller already loaded, and run a case where only the
caller's root resolves. It says "Gated by `tools/policy/check_policy.py`, the `policy fixtures`
leg's `kit-root-threaded` sub-case", and that no gate covers the class elsewhere. It names
`grammar-bound-to-the-wrong-root`, the sibling class where a module binds its root at import.
`python tools/memory-tree/gotchas.py --write` re-renders the index. The policy dossier's
`gotcha-classes` list gains `kit-argument-dropped-at-an-inner-call.md`, and
`python tools/codebase-map/gen_map.py --write` re-renders the map, which also carries the new
functions' symbols.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `derive_run_kind(repo, build, base, conf, families, readers)` | function, re-signed | `"spec"` or `"build"` |
| `derive_withheld_names(kit)` | function, `tools/policy/check_policy.py` | `[name]` |
| `read_git_or_refuse(repo, *args)` | function, `tools/policy/check_policy.py` | git's stdout, or a Refusal |
| `RC_DISPOSAL` | constant | `"- WONTDO · TOOL-bPlanted-9 · the ask is withdrawn\n"` |
| `resolve_copy_only(home, anchor, here)` | nested function in `run_reader_carried` | the kit directory, or LookupError |
| `kit-root-threaded`, `landing-other-base`, `rotated-landed`, `disposed-ask-landed`, `roster-specced-landed` | `RC_CARRIED` sub-cases | §4 "The carried sub-cases" |
| `derive_withheld_names(kit_dir)` | function, `tools/govkit/govkit.py` | `[name]` |
| `kit-argument-dropped-at-an-inner-call` | bug class record | §4 "The bug class" |

Each function name leads with a verb `.lexicon.conf` declares, and `lexicon.py --suggest <name>
--as py.function` answered OK for the three new names on 2026-11-19.

### What it does not check

- That `derive_run_kind` reads no other default-rooted resolver: `kit-root-threaded` refuses only
  `resolve_kit_dir` from another root, and a resolver that bypasses it is unseen.
- A conjunct of the predicate other than the base intersection, the rotated record and the two
  return arms: that is the hands-off mutation pass.
- An include holding a glob: the install case looks for a plan row ending `/<include>`, so a glob
  include finds no row and reds, rather than passing.
- That the govkit copies stand for an install: they copy a source kit into a scratch gov, and only
  the withheld names are taken out.
- A git read outside reader coverage that maps None to an empty string.

### Files touched (estimate)

`tools/policy/check_policy.py`
`tools/policy/README.md`
`help/policy.md`
`tools/govkit/govkit.py`
`tools/govkit/shims.py`
`tools/govkit/fixtures/stale_edges.py`
`tools/govkit/fixtures/retired_edits.py`
`memory/gotchas/kit-argument-dropped-at-an-inner-call.md`
`memory/gotchas/INDEX.md`
`memory/map/features/policy.md`
`memory/map/generated/MAP.md`
`memory/map/generated/CARDS.md`
`memory/map/generated/inventories.json`
`memory/map/generated/symbols.json`
`memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-4-ledger.md`

### Alternatives rejected

- Giving `derive_run_kind` a `kit` parameter: it threads the root, but still resolves and checks
  the module files once per candidate base, which M1 names as the second defect.
- Driving `legacy-homes-present` from `kit.toml` too: a rule edited to drop a list would then drop
  the check with it, so the descriptor check stays keyed on the readers' own constants.
- One withheld-name helper for both kits: the policy kit is copy-installed and self-contained, and
  its fixture reaches the deployer only by loading it in-process, as `budgets-ships-join` does. Each
  kit reads the one source, `kit.toml`, through its own reader.
- `tree_lib.read_git_output` for L1, which raises OSError on a failed read: the scan would then
  need the memory-tree kit loaded, which `check_reader_coverage` with a given `landed` does not.

## 5. Production-readiness checklist

- security — N/A — no new write path; the fixture's resolver swap is scoped to one call and
  restored in a `finally`.
- perf / scale — `derive_landed_builds` resolves the memory-tree kit once per call instead of once
  per candidate base; five more carried sub-cases, each one small repository.
- error / empty / loading states — a failed git read of reader coverage is a Refusal naming it; an
  empty withheld set is a `WRONG`; a sub-case's Refusal must name the copy's root.
- observability — each new sub-case and each withheld name prints its own `policy-fixture:` line.
- risks — the resolver swap in `kit-root-threaded` must not leak into later sub-cases; the
  `finally` restores it before the next sub-case builds.
- testing — the five sub-cases, the tightened `kit-modules-absent`, the per-name withheld checks,
  and AC1 and AC8's direct probes.
- migration — N/A — no data, conf or install shape changes; installs withhold what they withhold
  today.
- user docs — `help/policy.md`: the row grammar's whitespace and a failed git read's finding.

## 6. Acceptance criteria

The commands run from the worktree root, after:

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
ROOTS='import sys; sys.path.insert(0, "tools/policy"); import check_policy as c; seen = []; o = c.resolve_kit_dir; c.resolve_kit_dir = lambda h, a, here: seen.append(str(here)) or o(h, a, here); print(sorted(c.derive_landed_builds(".", {"dDeclaredLoop", "dSafePassage"}, kit="tools/policy"))); print(len(seen), sorted(set(seen)))'
FAIL='import sys; sys.path.insert(0, "tools/policy"); import check_policy as c; g = c.policy.run_git; c.policy.run_git = lambda r, *a: None if sys.argv[1] in a else g(r, *a); print(c.arm_reader_coverage(".", c.KIT)[2])'
```

- **AC1** — When `"$PY" -B -c "$ROOTS"` runs, it prints `['dDeclaredLoop', 'dSafePassage']` and
  then `2 ['tools/policy']`: every resolution comes from the root the caller gave.
  Red when: `derive_run_kind` loads its own modules, as at this spec's base, where the second line
  counts 8 and also lists the policy kit's absolute path.
  figure: 2 is DERIVED, the two loads of `derive_landed_builds`; 8 is PINNED, measured 2026-11-19
  at `515a3e6c`.
- **AC2** — When `"$PY" -B tools/policy/check_policy.py --fixture reader-coverage-carried` runs, it
  prints `case kit-root-threaded: red` with no `WRONG` on any line, and the `kit-modules-absent`
  line's Refusal names the kit copy's memory-tree directory.
  Red when: `derive_run_kind` resolves from `KIT` as at this spec's base, where
  `kit-root-threaded` prints `refused` and `WRONG`, its text naming the policy kit's own path.
- **AC3** — When `"$PY" -B tools/policy/check_policy.py --fixture legacy-homes-withheld-install`
  runs, it prints a `plan` and an `apply` line naming `unscanned-readers.txt` and the same two
  naming `legacy-homes.txt`, no `WRONG`.
  Red when: the case as at this spec's base, whose lines name `legacy-homes.txt` alone; or a
  `[[files]]` rule including `unscanned-readers.txt` with `role = "engine"` is staged after the
  `project-owned` rule of `tools/policy/kit.toml`, where the `plan` line for it prints `WRONG`.
  cost: a source snapshot, a deployer `plan` and an `apply`, so minutes rather than seconds
  (UNVERIFIED).
- **AC4** — When `"$PY" -B tools/policy/check_policy.py --fixture legacy-homes-present` runs, it
  prints a descriptor line naming `unscanned-readers.txt`, no `WRONG`.
  Red when: `unscanned-readers.txt` is taken out of the `project-owned` include of
  `tools/policy/kit.toml`, where that line prints `WRONG`; the case as at this spec's base stays
  green under the same edit.
- **AC5** — When the command of AC2 runs, it prints `case landing-other-base: green`, its detail
  `graded 0` and the announce line, no `WRONG`.
  Red when: `bases[b] &` is deleted from the landing set in `derive_landed_builds`, where the
  sub-case grades 1 and prints `WRONG`.
- **AC6** — When the command of AC2 runs, it prints `case rotated-landed: red`, its detail
  `graded 1` and the finding naming `fixture.planted (owner bPlanted, landed at`, no `WRONG`.
  Red when: `RUN_RECORD` is narrowed to `^RUN\.md$`, where the sub-case grades 0 and prints `WRONG`.
- **AC7** — When the command of AC2 runs, it prints `case disposed-ask-landed: red` and
  `case roster-specced-landed: red`, each `graded 1`, no `WRONG`.
  Red when: `disposed.add(row.target)` is deleted from `derive_run_kind`, where
  `disposed-ask-landed` grades 0 and prints `WRONG`; or the last line of `derive_run_kind` returns
  `"spec"`, where `roster-specced-landed` grades 0 and prints `WRONG`.
- **AC8** — When `"$PY" -B -c "$FAIL" --literal-pathspecs`, `"$PY" -B -c "$FAIL" --show-prefix` and
  `"$PY" -B -c "$FAIL" ls-files` run, each prints a list of one finding whose text holds `git`, the
  failing read's own argument and `failed, so reader coverage cannot read the tree`.
  Red when: the reads as at this spec's base, where the first prints a `deviation.approval` finding
  saying `which is not a tracked file`, the second `[]`, and the third one `has no reader` finding
  per graded key.
- **AC9** — When `grep -n "runs of whitespace" help/policy.md` runs, it prints the "A declared key"
  bullet's line, and `grep -n "runs of spaces" help/policy.md` prints nothing.
  Red when: the page as at this spec's base, where the second grep prints line 170 (PINNED).
- **AC10** — When
  `"$PY" -B -c "import sys, pathlib; sys.path.insert(0, 'tools/govkit'); import govkit; print(govkit.derive_withheld_names(pathlib.Path('tools/policy')))"`
  runs, it prints `['legacy-homes.txt', 'unscanned-readers.txt']`, and
  `grep -n '"legacy-homes.txt"' tools/govkit/shims.py tools/govkit/fixtures/stale_edges.py tools/govkit/fixtures/retired_edits.py`
  prints nothing while `grep -c derive_withheld_names` over the same three files counts at least
  one in each.
  Red when: the files as at this spec's base, where the probe raises `AttributeError` and the grep
  prints the three ignore lists.
- **AC11** — When
  `"$PY" -B -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; d = ' '.join(c.__doc__.split()); print('terminal at the landed revision' in d, 'derive_landed_builds' in d)"`
  runs, it prints `False True`, and
  `git grep -n "terminal at the landed revision" -- tools/ help/ README.md` prints nothing.
  Red when: the docstring as at this spec's base, where the probe prints `True False`.
- **AC12** — When `grep -n "kit-root-threaded\|landing-other-base\|rotated-landed\|disposed-ask-landed\|roster-specced-landed" tools/policy/README.md`
  runs, it finds the `reader-coverage-carried` paragraph naming all five;
  `grep -n "every withheld file" tools/policy/README.md` finds the `legacy-homes-withheld-install`
  text; `grep -n "git read of reader coverage" tools/policy/README.md` finds the arm's text; and
  `grep -n "git read" help/policy.md` finds the sentence on a failed git read.
  Red when: the docs as at this spec's base, where each of the four greps prints nothing.
- **AC13** — When `"$PY" tools/memory-tree/gotchas.py --for-paths tools/policy/check_policy.py`
  runs, its checklist names `kit-argument-dropped-at-an-inner-call`, and
  `grep -n "kit-argument-dropped-at-an-inner-call.md" memory/map/features/policy.md memory/map/generated/MAP.md`
  finds the claim in both.
  Red when: the record is absent, as at this spec's base, where neither names the class.

## 7. Gates

The close runs the merge bar once. `policy fixtures` runs every changed case; `policy check` grades
gov's own tree through the re-signed predicate and the refusing reads. The govkit legs guard the
three copies and `govkit.py`; `memory hygiene` grades the new class record and its index; the map
leg grades the dossier claim and the re-rendered map; the recall legs guard the build's records.

`policy fixtures` · `policy check` · `scratch-guard self-test` · `routed-commits selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py --fixture reader-coverage-carried · covers AC2 AC5 AC6 AC7 · each sub-case's break of §6, staged one at a time on the predicate · none
New arm: tools/policy/check_policy.py --fixture legacy-homes-withheld-install · covers AC3 · an engine rule for unscanned-readers.txt staged after the project-owned rule · none
New arm: tools/policy/check_policy.py --fixture legacy-homes-present · covers AC4 · unscanned-readers.txt taken out of the project-owned include · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

## 10. Reuse audit

The seams extended: `tools/policy/check_policy.py#derive_run_kind` and
`tools/policy/check_policy.py#derive_landed_builds`, whose loads become one; the sub-case table of
`tools/policy/check_policy.py#build_carried_repo` and `tools/policy/check_policy.py#run_reader_carried`,
which unit 1 built for exactly this predicate; the `kit.toml` read inside
`tools/policy/check_policy.py#run_legacy_present`, extracted as `derive_withheld_names` at its
second and third uses; `tools/policy/policy.py#run_git` under the one refusing reader; and
`tools/govkit/govkit.py#load_toml` for the deployer's copy of the read.
`python tools/codebase-map/reuse_lookup.py "read the files a kit descriptor withholds from installs"`
and `"run git and refuse naming the read when it fails"` ranked name-stem neighbours:
`tools/memory-tree/tree_lib.py#read_git_output`, which raises OSError and is answered in §4
"Alternatives rejected", `read_git` in other kits, and `resolve_kit_dir`, which this unit threads
rather than replaces; no existing seam reads a descriptor's `project-owned` names outside
`run_legacy_present` and `tools/govkit/govkit.py#resolve_entry`, whose carve-out answers from a
descriptor resolved against the tool root and an install context, more than an ignore list needs. The recall probe returned the review record
this unit closes, unit 1's spec and its divergence record on the fixture guard, and
`TOOL-dGroundRules-17`, the spec that first withheld the legacy list; the dTrackedAtlas build-state
instrument's `derive_landings` is the landing half 2 mirrors, which this unit leaves as it is.

Recall terms used: `python tools/memory-recall/query.py "how does the policy fixture prove each arm of the landed predicate and the withheld list can red" --terms "landed predicate run record rotated base intersection fixture sub-case withheld project-owned kit.toml resolver root threaded refusal"`
