# TOOL-dLandedOwners-1 — the policy kit's landed predicate counts a build run that carried a unit forward

**Status:** CLOSED · rev-3 · 2026-11-19 · node d · Tier-2 · base 51971579 · streams tooling · order 1 · closes TOOL-dTrackedAtlas-5 · ratified 2026-11-19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dLandedOwners-1-ledger.md](../build/2026-11-19-build-TOOL-dLandedOwners-1-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md) | research | TOOL-dLandedOwners-2 TOOL-dLandedOwners-3 |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-divergence-1.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-divergence-1.md) | research | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-f1-fold.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-f1-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-1-pinned-facts-fold.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-pinned-facts-fold.md) | research | TOOL-dLandedOwners-2 |
| [2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md](../reviews/2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md) | diff-review | TOOL-dLandedOwners-2 TOOL-dLandedOwners-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/policy/check_policy.py#derive_landed_owners` reads a build as landed only when every spec is
`CLOSED` or `WONTDO`. dDeclaredLoop and dSafePassage each landed a build run that carried one unit
forward as `DEFERRED`, so they read unlanded and their keys go ungraded. This unit gives the policy
kit the predicate `TOOL-dTrackedAtlas-1` took for the schedule (its spec's fork F1, option g),
built from the memory-tree kit's shipped readers, so every landed build run reads landed.

## 2. Scope (IN)

- **S1** — A new function `derive_landed_builds(repo, builds, kit=KIT)` in
  `tools/policy/check_policy.py` returns the members of `builds` that have landed at the landed
  revision. A build has landed in either of two cases. Its specs are all terminal, which is the
  rule as it stands. Or one of its run records is a build-kind run with a landing merge, as §4
  "The predicate" states. Observed by AC1, AC2 and AC3.
- **S2** — `derive_landed_owners(repo, kit=KIT)` keeps its signature, its return type and its
  Refusals, and returns `derive_landed_builds` over the catalogue's owners. Its two callers,
  `#check_reader_coverage` and `tools/loop/termination.py#read_termination_inputs`, are not
  edited. Observed by AC1 and AC5.
- **S3** — A new function `derive_run_kind(...)` in the same file answers `spec` or `build` for one
  build at one run's base, by README rule 1 as §4 "The run kind" states. Observed by AC2 and AC4.
- **S4** — The refusals. Each of these raises `policy.Refusal` naming the cause, and none reads as
  "not landed": a git read that fails; a module of `RUN_READER_MODULES` that the resolved
  memory-tree directory does not hold, or that does not import, when the run-record half runs; and
  a conf that declares no `FAMILIES` when that half runs. Observed by AC4 and AC5.
- **S5** — A fixture case `reader-coverage-carried`, registered in `CASES`, holding five planted
  repositories that §4 "The fixture case" lists. Observed by AC4.
- **S6** — The docs. The "Landed means" bullet of `help/policy.md` states the new predicate. In
  `tools/policy/README.md`, the `arm_reader_coverage` paragraph, its arms-table row and the fixture
  paragraph state the new predicate and the new case. Observed by AC7.
- **S7** — The cost stays inside the `policy check` leg's 120 s ceiling (tools/gate-legs.json@d2f27f18:2092),
  within the bound AC6 pins. Observed by AC6.

## 3. Non-goals (OUT)

- The reader scan, `READER_SHAPES` and `#scan_reader_keys`: unit `TOOL-dLandedOwners-2` owns them.
  Once dDeclaredLoop reads landed, reader coverage reds seven keys that the loop kit reads through a
  module constant, and that unit's scan clears them.
- A disposition for `deviation.approval`, which only a reader under the memory root reads: unit
  `TOOL-dLandedOwners-3` owns it. The wider landed set reds that key too.
- The schedule, the build-state instrument and every other record under `memory/builds/`. This
  unit ports the instrument's predicate and does not call the instrument. The instrument sits under
  the memory root, covers only the 22 chain builds and takes about 41 s (PINNED, 2026-11-19).
- The loop kit's code, `tools/loop/termination.py` included, and the loop's pending list. Fork F1,
  resolved by the owner, leaves dDeclaredLoop's pending row as it stands: the held `loop termination`
  leg reads it stale until a later build bounds the cycle or re-owns the row, and the main loop's ask
  at the close records that.
- Widening `derive_landed_owners` past the catalogue's owners. dFairHearing and dTrueNorth own no
  catalogue key, so that function cannot name them. AC2 observes them through
  `derive_landed_builds`.
- The kit's version constant, `KIT_POLICY_VERSION`: `tools/check-kit-versions.sh` grades its
  shape, not whether it moved.
- The flagged bar and the policy kit's held suite run: the owner waived them for this build.

### Edges

- **hands-off** external — the stale pending row named in fork F1, which this unit does not edit.

## 4. Design

### The predicate

`policy.derive_landed_revision` names the landed revision `L`. The memory root `m` and `FAMILIES`
are read from `L`'s `.memory-tree.conf`. A build `b` of `builds` has landed when either half holds.

1. **Every spec terminal.** `m/builds/b/spec/` holds at least one spec, and every spec's status
   header carries a token in `tools/memory-tree/tree_lib.py#TERMINAL`. This is the base body of
   `#derive_landed_owners`, moved unchanged. An attended build with no run record lands through
   this half: `aTrimmedWait` has no `RUN.md` and reads landed only through it.
2. **A build-kind run with a landing.** This half runs only for a build that half 1 leaves unlanded
   and that holds a run record. A run record is `m/builds/b/RUN.md`, or a rotated
   `m/builds/b/RUN.LANDED.<8 hex>.md` beside it, at `L`. Its base is the first `base:` value in its
   `## Run facts` section. The build has landed when one run record meets three conditions. Its
   base names a commit in this repository. `derive_run_kind` answers `build` at that base. And a
   merge on `L`'s first-parent history touches `m/builds/b/RUN.md`, with the `RUN.md` at that merge
   carrying the same base.

The merges come from the instrument's own call, made once for each build that reaches half 2:
`git log --first-parent --merges --format=%H L -- m/builds/b/RUN.md`, as
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`
makes it. Every blob is read in batches through `tools/memory-tree/tree_lib.py#read_blobs_at`.

A base must be checked to resolve before it is read. `read_blobs_at` answers `None` for an object
the revision does not hold. An unresolved base would therefore read an empty README and BACKLOG,
answer `build`, and count a landing that never happened. A base that names no commit lands nothing,
as the instrument's docstring states for a record "whose base resolves to no commit".

### The run kind

`derive_run_kind` reads README rule 1 at the base `B`. It is the test that
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#derive_run_kind`
and `tools/unattended/unattended.sh#check_spec_run` apply. The answer is `spec` when both halves
hold, else `build`:

- **An open ask.** `m/builds/b/BACKLOG.md` at `B` holds an id-led row whose id's slug is `b`, and
  no status row disposes of that id. Id-led rows are read with
  `tools/memory-tree/row_grammar.py#derive_row_re`. A status row is one that
  `tools/memory-tree/backlog.py#extract_row` reads with class `status` over `#build_grammar` of the
  families, with its verb in `TERMINAL`.
- **An unspecced roster unit.** `m/builds/b/README.md` at `B` has a table row inside its
  `roster:units` pair whose first id names a unit that no spec under `m/builds/b/spec/` at `B`
  defines. The first id is read with `tools/memory-tree/gen_build_index.py#extract_roster_ids` over
  `#build_roster_id_re`. A spec's unit is read with `tools/memory-tree/tree_lib.py#parse_spec_h1`.
  The pair's markers are `gen_build_index`'s `PLAN_OPEN` and `PLAN_CLOSE`.

The dClosedLoop instrument makes the same reading from `bare-ids.py`'s `read_asks` and
`read_roster_units`. This unit makes it from the shipped modules those two call.

### Interface

| Name | Signature | Answers |
|---|---|---|
| `derive_landed_builds` | `(repo, builds, kit=KIT)` | the set of `builds` landed at `L`; `set()` for an empty `builds`, with no git call |
| `derive_run_kind` | `(repo, build, base, conf, families)` | `"spec"` or `"build"`, at a base the caller has resolved |
| `derive_landed_owners` | `(repo, kit=KIT)`, unchanged | `derive_landed_builds(repo, <catalogue owners>, kit)` |

### Loading the memory-tree modules

`#load_tree_lib` already puts the memory-tree kit's directory on the import path, found by
`resolve_kit_dir` from `kit`. A new module constant, `RUN_READER_MODULES`, names the modules half 2
loads: `gen_build_index`, `backlog`, `row_grammar` and `design_lib`. `design_lib` is on the list
because `gen_build_index` imports it at module scope
(`tools/memory-tree/gen_build_index.py@a1bfa9b944d24be88fb3037c302a1bfccf6c2e18:320`).

Half 2 loads them lazily, at the first build that reaches it, in two steps:

1. It checks that the directory `resolve_kit_dir` named holds `<module>.py` for each module of
   `RUN_READER_MODULES`.
2. It then imports `gen_build_index`, `backlog` and `row_grammar`.

An existing fixture repository holds only `tree_lib.py` beside its kit copy and has no run record,
so it never reaches the check. `reader-coverage-relocated` therefore keeps its contract.

The check comes first because the import alone cannot see an absent module in the fixture's
process. `import` answers from `sys.modules` for a module already loaded. It also searches the
whole import path, and `#build_reader_coverage_repo` has put the source tree's memory-tree
directory there through `load_tree_lib()`. So a planted repository lacking `gen_build_index.py`
would still import it.

A missing file raises
`policy.Refusal("kit.toml", 0, "requires memory-tree, which does not resolve: <dir> holds no <module>.py")`.
An `ImportError` or `LookupError` at the import raises the same Refusal with its own cause. This is
the message the existing miss of `tree_lib` uses. A `gen_build_index.Problem` raised for an empty
`FAMILIES` becomes a Refusal naming `.memory-tree.conf`.

### The loop's termination read

`tools/loop/termination.py#check_stale_rows` reds every pending row whose build is in
`gov["landed"]`, whatever the row's kind, and `#read_termination_inputs` fills that set from
`derive_landed_owners`. The pending list carries one dDeclaredLoop row,
`cycle · item.review.dispose -> item.review.fold -> item.review.dispose · dDeclaredLoop`
(`tools/loop/termination-pending.txt@c39334b6f1936fd2adab118ccf4c8a6f75d11357:20`). Once this unit
lands, `termination.py check` reds that row as stale. The `loop termination` leg sits in the
`selftests` chunk, as its row in `tools/gate-legs.json` shows, and the plain bar holds that chunk
(`tools/run-gates/run-gates.sh@7c21a741439a97b9964ec16a6cbc733115ac4fcd:5456`). So the close's bar
does not run it, and the daily held job will. Fork F1 is resolved by the owner as option (a): the
unit builds as specced, the held `loop termination` leg reads the row stale on the daily job until a
later build bounds the cycle or re-owns the row, and the ask the main loop files at the close names
the row and records that.

### The fixture case

`reader-coverage-carried` is an outcome case, run by a new `run_reader_carried(name)` with one
repository per sub-case. A new `build_carried_repo(t, case)` builds each one in the shape of
`#build_reader_coverage_repo`, with these parts:

- a kit copy whose catalogue holds `RC_KEY`, owned by `RC_OWNER`, and no consumer;
- a `.memory-tree.conf` declaring `MEMORY_ROOT="memory"` and `FAMILIES="tooling:TOOL"`;
- `tree_lib.py` and the file of each module in `RUN_READER_MODULES`, copied untracked from the
  resolved memory-tree kit to sit beside the kit copy;
- one bare remote.

The copy reads only those five files. `run_fixture`'s audit hook, `#add_source_read`, records every
source file that the copy opens. `#check_guard_trace` then prints a WRONG for each recorded read that
trips no `policy fixtures` guard. All five trip that guard. Seven other `*.py` files of the kit trip
none of it: `check-arms.py`, `commit_trailers.py`, `coverage_join.py`, `import_walk.py`,
`merge-rows.py`, `migrate_backlog.py` and `transition_audit.py`. These figures come from
`ls tools/memory-tree/*.py | python tools/check-spec-tokens.py --legs-for -` (PINNED, 2026-11-19, at
`1ca00786`).

A scratch probe imported the three modules from the source kit under an audit hook (PINNED,
2026-11-19). It called `derive_row_re`, `build_grammar`, `extract_row`, `build_roster_id_re`,
`extract_roster_ids` and `parse_spec_h1` over dDeclaredLoop's records, and the kit files it opened
were exactly these five. `id_grammar` is imported only lazily, at three sites, and the probe reached
none of them: `tools/memory-tree/row_grammar.py#load_index_builder`, `#derive_relation_successors`
and `tools/memory-tree/backlog.py#_resolve_anchor_at`.

The base commit `B` on `main` holds the build README's `roster:units` pair. A branch `run` then
commits `RUN.md`, whose `## Run facts` holds `base: <B>`, together with the spec edits. That branch
is merged into `main` with `--no-ff` and pushed. `check_reader_coverage` judges each sub-case, and
each prints `case <name>: red|green`.

| Sub-case | Planted | Wants |
|---|---|---|
| `carried-landed` | roster units 1 and 2, both specced at `B`; on `run`, unit 1 `CLOSED` and unit 2 `DEFERRED` | graded 1, `RC_KEY` red |
| `spec-run-landed` | at `B`, an open ask `TOOL-bPlanted-9` in the BACKLOG and unit 2 unspecced; on `run`, both `DEFERRED` | graded 0, the announce line |
| `run-unlanded` | as `carried-landed`, but `run` fast-forwarded onto `main`, so no merge touches `RUN.md` | graded 0, the announce line |
| `base-unresolved` | as `carried-landed`, with the one `RUN.md`'s `base:` set to forty `e` characters; the blob at `L` and at the landing merge is that one file | graded 0, the announce line |
| `kit-modules-absent` | as `carried-landed`, with only `tree_lib.py` beside the kit copy | a Refusal naming the memory-tree kit and `gen_build_index.py` |

### What it does not check

These are the instrument's own limits, or follow from them:

- A landing on the remote that this clone has not fetched reads unlanded.
- A merge that touches `RUN.md` with a run's base for some other reason reads as that run's landing.
- A run record rotated outside the driver is not listed.
- Under `BACKLOG_MODE="shards"`, no build folder holds a BACKLOG, so every run reads build-kind.

These follow from the module check:

- It checks that each module's file is present. It does not check that the module running was loaded
  from that file, since within one process an import reuses the first copy loaded.
- A sibling that a module of `RUN_READER_MODULES` comes to import later is not on the list. In the
  fixture, that sibling imports from the source kit, so the guard trace still records the read.

### Measured on the real tree

On 2026-11-19 (PINNED), a scratch probe built from the modules above read the catalogue's 23
owners at `51971579` in 2.5 s.

- Half 1 alone read five: `aNimbleMend`, `aTrimmedWait`, `dFoldedAudit`, `dGroundRules` and
  `dOrderedCharter`. That is `derive_landed_owners` at base.
- Half 2 alone read six. It added dDeclaredLoop and dSafePassage and dropped `aTrimmedWait`.
- The union of the two halves read seven.
- Over the 22 chain builds, the union read the same six builds the instrument reads, in 2.1 s.
- With `derive_run_kind` forced to `build`, half 2 read all 22, so the kind test is what tells the
  run kinds apart.

### Files touched (estimate)

`tools/policy/check_policy.py`
`tools/policy/README.md`
`help/policy.md`
`memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-1-ledger.md`

### Alternatives rejected

- **Half 2 alone, the schedule's predicate unmodified.** Rejected by the probe above: it drops
  `aTrimmedWait`, an attended build with no run record, so reader coverage would stop grading its
  key.
- **Load the build-state instrument from the policy kit.** Rejected: the brief asks for a form a
  shipped kit can hold, and an adopter's kit cannot reach a record under gov's memory root. The
  instrument also lists only the 22 chain builds.
- **`CENSUS_TERMINAL`, every spec `CLOSED`, `WONTDO` or `DEFERRED`.** Rejected by the instrument's
  fork F1, option b: a spec run carries every unit as `DEFERRED`, so all 22 chain builds would read
  landed.
- **Extract the run-kind test into the memory-tree kit.** Rejected because a shared Python function
  would have only one caller. The dClosedLoop instrument is a CLOSED unit's record, and
  `check_spec_run` is written in bash. This unit composes the kit's existing grammar readers and
  writes no second grammar.
- **Copy every `*.py` of the memory-tree kit into each planted repository.** Rejected because that
  copy reads seven files that trip no `policy fixtures` guard, and each one prints a guard-trace
  WRONG (§4 "The fixture case").
- **Add those seven paths to the `policy fixtures` guard in `tools/gate-legs.json`.** Rejected
  because no case reads them, so the leg would run on edits it cannot be affected by.
- **Run each sub-case's check in a child process, so an absent module fails its import.** Rejected
  because the audit hook sees this process alone, so the child's reads would leave the guard trace.
  The file check gives the same Refusal in-process.

## 5. Production-readiness checklist

- security — No new write path. Every read is a git read at a resolved commit, made with argv
  lists and no shell, and the build slugs come from the catalogue.
- perf / scale — About 2.5 s over 23 owners (PINNED, §4). AC6 bounds it at 15 s, well under the
  `policy check` leg's 120 s ceiling (tools/gate-legs.json@d2f27f18:2092).
- error / empty / loading states — An empty `builds` returns `set()` with no git call, as the base
  function does when there are no owners. A missing module, or a missing conf declaration, is a
  Refusal (S4).
- observability — Unchanged. Reader coverage's summary line names the landed owners, so the two new
  owners appear there.
- risks — The held `loop termination` leg reads dDeclaredLoop's pending row stale on the daily job
  until a later build bounds the cycle or re-owns the row; the owner accepted that at fork F1, and
  the main loop's ask at the close records it. The wider landed set also reds eight reader-coverage keys
  until units 2 and 3 land, so the build lands only with all three units.
- testing — §6, and the new fixture case. The held suite runs only at the flagged bar, which the
  owner waived.
- migration — N/A — no record or file changes shape; only the function's answer widens.
- user docs — `help/policy.md`, its "Landed means" bullet (S6).

## 6. Acceptance criteria

The commands run from the worktree root. `$X` is the run's scratch folder, and `L` is the landed
revision.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
L=$("$PY" -B -c "import sys; sys.path.insert(0, 'tools/policy'); import policy; print(policy.derive_landed_revision('.')[0])")
```

- **AC1** — When
  `"$PY" -B -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(sorted(c.derive_landed_owners('.')))"`
  runs, the list holds `dDeclaredLoop` and `dSafePassage` beside `aNimbleMend`, `aTrimmedWait`,
  `dFoldedAudit`, `dGroundRules` and `dOrderedCharter`.
  Red when: at base it prints those five alone, as observed on 2026-11-19 at `51971579`.
  figure: PINNED at `51971579`; an owner that lands after it may join the list.
- **AC2** — When the probe calls `c.derive_landed_builds('.', [...])` over `dFairHearing`,
  `dTrueNorth`, `dDeclaredLoop`, `dSafePassage`, `dPlacedRequest`, `dRankedPlan` and
  `dWellOiledMachine`, it prints the first four, sorted, and none of the last three.
  Red when: `derive_run_kind` is made to answer `build` always, and the last three join.
- **AC3** — When the instrument runs as
  `"$PY" memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py --ref "$L" --default-ref "$L" --claims none > "$X/state.json"`,
  and the probe passes the instrument's `builds[].slug` list to `c.derive_landed_builds`, the sorted
  answer equals the sorted `landed` list in `$X/state.json`: six builds at `51971579`.
  Red when: half 2 is removed, and the answer lacks dDeclaredLoop and dSafePassage.
  cost: about 41 s, for the instrument (PINNED, measured 2026-11-19).
- **AC4** — When `"$PY" tools/policy/check_policy.py --fixture reader-coverage-carried` runs, it
  exits 0. It prints five `policy-fixture: reader-coverage-carried ·` sub-case lines, one per §4
  sub-case, and then the `guard-trace` lines and the count line that `run_fixture` always adds. No
  line holds `WRONG`. `case carried-landed: red` appears, and `kit-modules-absent` reports the
  Refusal naming `gen_build_index.py`.
  Red when: half 2 is removed, and `carried-landed` prints `WRONG` with `graded 0`.
- **AC5** — When `"$PY" tools/policy/check_policy.py --fixture reader-coverage` and
  `--fixture reader-coverage-relocated` run, each exits 0 with no line holding `WRONG`.
  Red when: the module check runs before half 2 is reached, and the relocated case's present
  repository, which holds only `tree_lib.py`, refuses.
- **AC6** — When
  `"$PY" -B -c "import sys, time; sys.path.insert(0, 'tools/policy'); import check_policy as c; t = time.time(); c.derive_landed_owners('.'); print(round(time.time() - t, 1))"`
  runs, it prints a number under `15`.
  Red when: the merge log runs once per run record, instead of once per build that reaches half 2.
  figure: PINNED; the candidate measured 2.5 s on 2026-11-19.
- **AC7** — When `grep -n "RUN.md" help/policy.md` runs, it finds the "Landed means" bullet naming
  the run record and a unit carried forward. When
  `grep -n "derive_landed_builds\|reader-coverage-carried" tools/policy/README.md` runs, it finds
  the arm paragraph and the fixture paragraph.
  Red when: `grep -n "A build whose specs are still" help/policy.md` still finds the base's
  sentence saying that a build with a `DEFERRED` spec has not landed.

## 7. Gates

The close runs the plain bar once. `policy fixtures` is a guarded leg of the `selftests` chunk, so
the plain bar holds it, and AC4 and AC5 observe its cases directly. `scratch-guard self-test` and
`routed-commits selftest` guard `tools/policy/check_policy.py` too; this unit changes nothing they
read beyond that file's landed predicate. `recall floor` and `recall floor arms` guard the build
folder, where the acceptance ledger is written.

`policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py --fixture reader-coverage-carried · covers AC4 · half 2 of `derive_landed_builds` deleted, so `carried-landed` grades 0 · none

## 8. Open questions

- **F1 — Once dDeclaredLoop reads landed, `termination.py check` reds its pending cycle row as
  stale. How should the build handle it?** The row, quoted in §4 "The loop's termination read",
  excuses a cycle until its owner build lands. dDeclaredLoop landed without bounding the cycle,
  and the old predicate hid that. The brief put only the reader-coverage reds to the owner.
  (a) Build as specced. The main loop files an ask at the close naming the row. The held
  `loop termination` leg reads red on the daily job until a later build bounds the cycle or
  re-owns the row. This leaves one follow-up, and the finding is a true one.
  (b) This unit also deletes the row, which the shrink-only list allows. If gov's counted graph
  still holds the cycle, `counted` reds in its place (UNVERIFIED: no probe ran, because the probe
  is the leg itself). This gives the same red and loses the record of the excuse.
  (c) A fourth unit bounds the cycle in the loop definition. That edits the loop kit, which the
  brief lists as a non-goal, so M3's first veto discards it unless the owner lifts the non-goal.
  (d) This unit re-owns the row to the build that will bound the cycle. No record names such a
  build, so only the owner can choose one.
  Recommendation: (a). It trips no veto, keeps the finding visible and leaves one ask. (d) is
  better if the owner names the build.
  RESOLVED (owner, 2026-11-19): (a), build as specced; the main loop files an ask at the close naming the row.

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.
- rev-2 · 2026-11-19 · §3 · §4 · §5 · §8 · the owner resolved fork F1 as option (a), recorded in
  2026-11-19-prompt-TOOL-dLandedOwners-1-f1-fold; F1 marked RESOLVED and the sentences citing it
  restate the resolution; no design change.
- rev-2 · 2026-11-19 · §2 · §3 · §5 · §6 · the writing-practice leg's pinned-facts reds over
  `c3f402ac1`, folded from 2026-11-19-prompt-TOOL-dLandedOwners-1-2-spec-writer: the leg ceiling
  cites its owning line in `tools/gate-legs.json` and the instrument's measured cost reads PINNED,
  each on its own line; no design change.
- rev-3 · 2026-11-19 · S4 · §4 · §7 · AC4 · AC5 · the builder's divergence at the first build pass,
  folded from 2026-11-19-prompt-TOOL-dLandedOwners-1-divergence-1. The fixture copies only
  `tree_lib.py` and `RUN_READER_MODULES`, since copying every kit `*.py` printed seven guard-trace
  WRONG lines. A file check now comes before the import, since an import in the fixture's process
  never misses. Files touched names the acceptance ledger, and §7 adds the two recall-floor legs
  that guard it. AC4 counts sub-case lines, and
  `base-unresolved` names its one run record. AC5's red is restated for the check.

## 10. Reuse audit

The seam extended is `tools/policy/check_policy.py#derive_landed_owners`, whose body becomes half 1
of `derive_landed_builds`. The predicate is ported from
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`
and from the dClosedLoop instrument's `#derive_run_kind`. It is built from the memory-tree kit's
shipped readers: `tree_lib.py`, `row_grammar.py`, `backlog.py` and `gen_build_index.py`. The policy
kit already reaches them through its declared `requires`, and no grammar is written twice.

`python tools/codebase-map/reuse_lookup.py "whether a build run has landed on the default branch"`
and `"run kind spec run or build run from the roster and open asks"` ranked only helpers that
matched on name stems (`run_git`, `read_blobs_at`, `parse_spec_h1`, `build_grammar`). None of them
answers whether a build run landed. `tools/unattended/lib-unattended.sh#read_landing_commit`
answers a different question, the commit that carries one live run-state file at HEAD, so it is not
reused. The recall probe returned ask `TOOL-dTrackedAtlas-5`, this build's brief and README, and
`TOOL-dGroundRules-8`, the reader-coverage arm's spec. No hit disagreed with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the policy kit decide a build has landed for reader coverage" --terms "derive_landed_owners landed owner reader coverage DEFERRED carried build run landing merge first-parent run kind"`
