# TOOL-dDeclaredLoop-82 — the round-5 spec audit's 23 minors, batched

**Status:** DEFERRED · rev-7 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 41 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-821.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-821.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-822.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-82-deviation-822.md) | deviation | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-82-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-82-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-82-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-82-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-80 |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`)
exited CONVERGED with 25 confirmed findings, PINNED from the report, over units 76 to 79, the round-4
promotions. Its two highs are units 80 and 81, one per id. This unit is the batch BUILD-METHOD M4 makes
of the rest, every MEDIUM and every LOW, each by its report id. It builds after every unit it reads, at
order 41, and repairs none in particular.

Rev-7 re-grounds the batch on branch `unattended-declared-loop-d56bf0` at `77130f24`, built through
order 35 and units 56, 70 and 71 of order 36, and on the committed specs of orders 36 to 40. Every
sibling spec this batch amended builds at an earlier order and is CLOSED when this unit builds, so no
item here rewrites one (§8 F5). An item a committed spec or the built code already settles leaves the
scope, each in §3 with what settles it; the code half of every other item stays here under its rev-6
label, which sibling specs cite.

| Report item | Severity | Report ids | Rev-6 scope items | At rev-7 |
|---|---|---|---|---|
| M1 | MEDIUM | 1, 11 | S1, S2 | S1; S2 in §3 |
| M2 | MEDIUM | 3 | S3 | S3 |
| M3 | MEDIUM | 4 | S4 | S4, its plant; its text half in §3 |
| M4 | MEDIUM | 5 | S5 | §3 |
| M5 | MEDIUM | 6 | S6 | §3 |
| M6 | MEDIUM | 13 | S7 | §3 |
| M7 | MEDIUM | 17 | S8 | S8 |
| M8 | MEDIUM | 29 | S9 | S9, its plant; its text half in §3 |
| M9 | MEDIUM | 30 | S10 | S10 |
| L1 | LOW | 2 | S11 | §3 |
| L2 | LOW | 7 | S12 | §3 |
| L3 | LOW | 8 | S13 | §3 |
| L4 | LOW | 9 | S14 | §3 |
| L5 | LOW | 10 | S15 | S15 |
| L6 | LOW | 12 | S16 | S16, its plant row; its text half in §3 |
| L7 | LOW | 15 | S17 | §3 |
| L8 | LOW | 16 | S18 | §3 |
| L9 | LOW | 18 | S19 | S19, its table rows; its text half in §3 |
| L10 | LOW | 19 | S20 | §3 |
| L11 | LOW | 22 | S21 | S21, its definition-fixtures probe; its `loop selftest` half in §3 |
| L12 | LOW | 24 | S22 | §3 |
| L13 | LOW | 27 | S23 | S23 |

That is 10 MEDIUM and 13 LOW findings by raw id, PINNED from the report. Its five refuted findings, ids
14, 21, 23, 25 and 26, are not in the disposal population. S24, the carriers of the two minted
functions, is new at rev-7 and answers no report id.

## 2. Scope (IN)

The labels keep their rev-6 numbers; every other rev-6 item is in §3.

- **S1** — id 1. Outside `TOOL-dDeclaredLoop-80`'s fixture boundary, `derive_conf_reads` (76 S2, in
  `tools/loop/loop_lib.py`) also counts, as kind `conf constant`, a `Name` or `Attribute` that reaches a
  module-level name of `loop_lib` bound by an `Assign` to a string constant containing a conf name, through
  `import loop_lib`, `from loop_lib import <name>` or either aliased, as S10's `derive_import_aliases`
  answers them. The bindings are read by `ast.parse` of the `loop_lib.py` in the scanned module's own
  folder, never by importing it, and only for a module that imports `loop_lib` in one of those forms; a
  missing or unparseable file there raises, as a module that does not parse does (§8 F6). A read inside
  the boundary is still passed over. Observed by AC1.
- **S3** — id 3. The `url-forms` plant of `tools/loop/position.py` (77 S3 and S4) reaches the mismatch
  skip entry: after 77's reading over the remote `https://u:SECRET@127.0.0.1:9/r.git`, it writes a
  non-empty `FETCH_HEAD` whose one line names `main` of `https://other.example/r` and reads again with no
  fetch. The read list holds 74 S2's `FETCH_HEAD · skipped — no line for main of origin`, and no line the
  plant prints and nothing in the JSON of the position holds `SECRET` (§4 "The plants"). Observed by AC3.
- **S4** — id 4. The plant `push-merge-resurrect-deleted-policy-conflict-elsewhere` joins `PLANTS` of
  `tools/loop/guard.py` and the owed map of `run_selftest` at exit 1: main's tip lacks the policy file, a
  run branch that never touched it conflicts with main on another file, and the resolution keeps the run
  branch's policy bytes with no trailer, so 75 S27's exit-1 reading answers `absent` (§4 "The plants").
  Observed by AC4.
  **Readers:**
  by name: tools/loop/guard.py (its PLANTS table and the owed map of run_selftest, which spell each plant name)
  by value: NO VALUE READERS — the plant adds one fixture name and retires none; the word deleted names its history's policy file
- **S8** — id 17. `derive_docstring_ids(tree)` in `tools/memory-tree/tree_lib.py` answers the ids of the
  docstring constants of the module and of every `ClassDef`, `FunctionDef` and `AsyncFunctionDef` whose body
  opens with one. `scan_glob_readers` in `tools/memory-tree/gen_build_index.py` calls it through the
  module's own `tree_lib` import, in place of its inline set; `derive_conf_reads` calls it inside the
  function, after `read_memory_tree("tree_lib.py")`, in place of the set 76 S2 copies. The glob-reader
  self-test arm's planted module gains an `async def` whose docstring holds the pathspec. Observed by AC8.
  **Readers:**
  by name: tools/memory-tree/gen_build_index.py (scan_glob_readers, whose inline docstring set gives way to the call)
  by value: `tools/memory-tree/gen_build_index.py` (the glob-reader self-test arm, which owes the same charged names over its planted module)
- **S9** — id 29. The plant `push-merge-unparseable-parent` joins `PLANTS` of `tools/loop/guard.py` and
  the owed map of `run_selftest` at exit 1: an octopus merge, one of whose parents holds a policy blob that
  does not parse, refused as `does not parse at parent <sha8>` with no traceback (§4 "The plants").
  Observed by AC9.
- **S10** — id 30. `derive_conf_reads` counts a non-docstring string constant that contains either conf
  name anywhere, not only at its end, and resolves a `Name` callee through `derive_import_aliases(tree)`,
  minted in `tools/loop/loop_lib.py`, before matching 76 S2's reader names `read_design_conf`,
  `read_driver_conf` and `parse_conf`. `derive_import_aliases` answers each local name an absolute
  `import` or `from ... import` binds, aliased or not, mapped to the dotted name it imports. Observed by
  AC10.
- **S15** — id 10. `resolve_memory_root_source` (76 S1) answers `(memory, .memory-tree.conf)` for a tree
  holding `.memory-tree.conf` and no `.unattended.conf`, where the memory-tree conf leaves `MEMORY_ROOT`
  unset, the conf whose branch answered; `default` stays the answer only where neither conf exists. The
  `root-source` plant of `tools/loop/budget.py` gains two trees, each conf alone with the key unset.
  Observed by AC15.
  **Readers:**
  by name: tools/loop/loop_lib.py (resolve_memory_root_source, the one function answering the source)
  by value: `tools/loop/budget.py` and `tools/loop/breakpoints.py`, whose explain line and held line print the source; every memory-tree conf their plants stage sets the key, and the root of the changed branch stays memory
- **S16** — id 12. The `conf-read-forms` plant's docstring-only module holds module, class, function and
  `async def` docstrings, each naming `.unattended.conf`, and answers no hit. Observed by AC16.
- **S19** — id 18. The `url-forms` table gains the regression pairs the comment of
  `tools/unattended/unattended.sh#norm_endpoint` records: `github.com:alice/repo` against
  `github.com:bob/repo` owed unequal, and `git@github.com:alice/repo` against `github.com:alice/repo` owed
  equal. Observed by AC19.
- **S21** — id 22. The pass-commit probe of `TOOL-dDeclaredLoop-75` §4 "The pass-commit probe" runs the
  leg `loop definition fixtures`, which `TOOL-dDeclaredLoop-67` S30 mints, at the pass commit of each
  unit ordered at or after 67 and before this unit whose §4 Files touched names `tools/loop/loop_lib.py`,
  that population derived from the specs at this pass. A `no leg` answer is followed by the leg's exit at the earliest
  later pass commit of the population whose manifest holds the row. Each line is recorded in this unit's
  acceptance ledger; the item writes no code. Observed by AC21.
- **S23** — id 27. The `url-forms` plant derives one expectation from git itself: it serves the scratch's
  bare repository over git's dumb HTTP protocol from `http.server` on `127.0.0.1` at a free port, after
  `git update-server-info`, adds the remote `web` as `http://user:tok@127.0.0.1:<port>/o.git`, fetches it
  with every credential helper cleared, and owes `derive_fetch_url` of the configured URL equal to the URL
  git wrote into `FETCH_HEAD` (§4 "The plants"). The hand-typed rows stay as regressions. Observed by AC23.
- **S24** — The carriers. The table of `loop_lib.py` functions in `tools/loop/README.md` gains a row for
  `derive_import_aliases`, its row for `derive_conf_reads` names the `conf constant` kind, a conf name
  anywhere in a string and an aliased reader call, and the paragraph naming the module's reaches outside
  the standard library names `derive_conf_reads`' import of the memory-tree kit's `derive_docstring_ids`.
  The comment of `tools/loop/kit.toml` that lists the same reaches names it too. Observed by AC24.

## 3. Non-goals (OUT)

- The two highs' mechanisms: units 80 and 81, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 14, 21, 23, 25 and 26.
- A TLS endpoint for S23: git's anonymiser is one rule for every scheme (77 S1), and a certificate in a
  fixture is a surface this unit does not price.
- A conf constant bound by an `AnnAssign`, a `Path(...)` or a star import: `TOOL-dDeclaredLoop-86` S13.
- Any edit of a sibling spec: §8 F5.

### The rev-6 items the built code or a committed spec settles

Read on branch `unattended-declared-loop-d56bf0` at `77130f24`. "CLOSED here" means CLOSED when this unit
builds, at order 41 (§8 F5).

| Item | What settles it |
|---|---|
| S2 | `TOOL-dDeclaredLoop-80` rev-6 S4 names every conf-writing plant a later unit adds to either module, 75's `unset-driver-root`, 79's `trailing-slash-agree` and `no-confs`, this unit's `conf-read-forms` rows and AC15 trees, and writes each inside its boundary; its §4 Evidence lists them, and its rejected alternative names S1's cross-module constant. 76 is CLOSED here. |
| S4, its text | 75 rev-10 §4 "The re-merge on exit 1" reads an exit 1 whose conflicted paths leave out the policy path as `absent` or `present` from that tree, as for exit 0, and keeps 78's refusal of a `present` C that does not parse; S27's other outcomes stay 81's `failed` state, as 83 wrote. 75 is CLOSED here. |
| S5 | No leg of `tools/gate-legs.json` carries a loop path in its `guard`, as 79 rev-6 §3 (its S18) records, and 75 rev-10 §3 (its S21) records that no `loop selftest` leg is added, so the population S5 amended is empty. |
| S6 | 75 rev-10 §4 "The pass-commit probe" records `no leg` where a commit's manifest lacks the row, never skipped, and 79 rev-6 §4 "The probe's legs" derives 72's legs from the manifest at 79's base, where `loop breakpoint fixtures`, built by `TOOL-dDeclaredLoop-19`, stands; the same section records that unit 71 writes nothing. |
| S7 | 79 rev-6 §4 "The sed-fails plant" makes the apply step fail with a program `sed -E` refuses, inside whatever bash `resolve_bash` answers, with no stub on any PATH, so no PATH order is left to assert. |
| S9, its text | 78 rev-7 §3 names `push-merge-unparseable-parent` as this unit's plant. 78 is CLOSED. |
| S11 | 72 rev-6 AC4 counts reader calls, never the conf names, and 76 rev-6 S4 observes that property on the syntax tree through `no-own-conf-read`, recording 72 AC4 beside its AC1 at the close. 72 is CLOSED here. |
| S12 | 78 rev-7 AC2's `Red when` names the break, an empty `present` C read as `uncomputable`, and its §7 arm line staged AC1 to AC3 red against it at its close. 78 is CLOSED. |
| S13 | 78 rev-7 S4 names `push-merge-unparseable-c`, and its §5 "Dependencies on units built beside this one" records that this unit finds it held. |
| S14 | 77 rev-3 §5 "Dependency" records that 75 writes `tools/loop/position.py` at step 39 and that the two are dispatched in sequence, and the build README's build-order region prints step 39's Parallel cell `no`. |
| S16, its text | 76 rev-6 S2 and §4 "The rule" name `AsyncFunctionDef`, and 76 AC2 observes an `async def` docstring. |
| S17 | 77 rev-3 S2 and §8 F4 put the shim's and the bare repository's paths through `Path.as_posix()`, and its plants fetch through them. |
| S18 | 77 rev-3 §5 risks states the second-`@` and `/`-before-`@` reading, and its §3 hands the no-fetch mismatch staging to S3 here. |
| S19, its text | 77 rev-3 §10 weighs `norm_endpoint` and the runlog `url-userinfo` row and says why neither serves. |
| S20 | 79 rev-6 §3 settles its S11, and its AC11 left its scope, so no typed copy of the held-leg predicate is left to restate. |
| S21, `loop selftest` | No such leg is added (75 rev-10 §3, its S21; 79 rev-6 §3, its S11 and S27), so no pass commit holds one to run. |
| S22 | 79 rev-6 §3 settles its S17 by 75 rev-10 S25 and §8 F6, which raise the render's size row and trim nothing, so no anchor `tools/unattended/check-unattended.sh` parses is at risk. |

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root`'s rule, under 76's source pair, and rev-6 AC4, which 76 S4 observes on the syntax tree; this unit amends no text of 72 (§3, §8 F5)
- **consumes-from** `TOOL-dDeclaredLoop-75` — S27's exit-1 reading, beside which S4 plants the deleted-policy case, S34's empty git config the `url-forms` fetches run under, and §4 "The pass-commit probe", which S21 runs; S27's text and the step-39 share are settled (§3)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `derive_conf_reads`, `resolve_memory_root_source`, the `root-source` and `no-own-conf-read` plants, which S1, S10 and S15 widen and S8 points at the shared docstring set (ids 1, 10, 30); ids 11, 12 and 17's text halves are settled (§3)
- **consumes-from** `TOOL-dDeclaredLoop-77` — `derive_fetch_url`'s user-part rule and the `url-forms` plant, which S3, S19 and S23 extend (ids 3, 18, 27); ids 9, 15, 16 and 22's text halves are settled (§3)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the C states and the parent refusal S4 and S9 plant against; S4's plant list and AC2 are already held (ids 7, 8)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S10's probe, beside which S21 runs the definition fixtures, S23's pre-filter the two guard plants pass, and S21's `url-forms` rows; the `sed-fails` plant and S17, S18 and AC11 are settled (§3)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, outside which S1 counts a conf constant read by name, and inside which the `conf-read-forms` rows and S15's trees are built (ids 1, 11)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the clean re-merge's exit table, which AC4 re-runs through `push-merge-tree-fatal` (id 4)
- **consumes-from** `TOOL-dDeclaredLoop-84` — S4 and AC4, amended to keep 75 S27's exit table; at rev-7 S4 writes no text of 75, and AC4 keeps 84's tree-fatal re-run (the round-6 spec audit's id 7)
- **hands-off** `TOOL-dDeclaredLoop-86` — S1's conf-constant kind, S21's probe, S8, AC1, AC21, §4, §5, §7 and §10, and the `conf-read-forms` and `url-forms` plants, which that unit restates, keys, floors, re-pins and hardens; its asks of S6, S14, AC5, AC6 and AC22 meet items settled at rev-7 (§3) (the round-6 spec audit's ids 5, 10, 13, 14, 16, 19, 21, 23, 25, 26, 27, 28)
- **hands-off** `TOOL-dDeclaredLoop-87` — S1's conf-constant kind, which that unit restates from a string constant to any value whose syntax subtree holds a conf name, an aliased from-import reaching it through S10's `derive_import_aliases` (the round-7 spec audit's id 29)
- **hands-off** `TOOL-dDeclaredLoop-88` — S8's docstring set, AC4, §5 and §10, which that unit reads from the lifted charge walk, gives a class-level half, floors and checks; its asks of S6 and AC5 meet items settled at rev-7 (§3) (the round-7 spec audit's ids 8, 9, 16, 17, 33)
- **hands-off** `TOOL-dDeclaredLoop-89` — S1's conf-constant kind, which that unit extends to `derive_conf_rebinds`' names, and S8's `derive_docstring_ids`, which its pass reads (the round-8 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-90` — S1's conf-constant kind and the conf-read sketch, which that unit restates to the names `derive_conf_constants` answers, and §10, which it completes with `read_profile_legs` (the round-8 spec audit's ids 5, 17)
- **hands-off** `TOOL-dDeclaredLoop-97` — S10's alias resolution and §4's sketch "The conf-read rule, after this unit", whose reader-call set that unit reads from `CONF_READERS` and restates (the round-12 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-98` — the `conf-read-forms` plant and AC10's reader-call row, which that unit extends to every declared conf reader (the round-12 spec audit's id 11)

## 4. Design

### Write set

This pass writes only the files §4 "Files touched" names. It amends no spec (§8 F5); S21 observes and
records and writes no code.

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `77130f24`, through `git archive` into a scratch
copy, unless named otherwise. `tools/loop/` is absent from this worktree's main. `derive_conf_reads`,
`resolve_memory_root_source`, `derive_fixture_boundary`, `derive_fetch_url`, `check_fetch_head` and the
`url-forms` plant are unbuilt at that tip and are read on the committed specs §5 "Dependency" names.

- `tools/loop/guard.py#read_remerge_policy` answers `conflicted` for every merge-tree exit 1 at the tip;
  75 rev-10 §4 "The re-merge on exit 1" reads an exit 1 whose conflicts leave out the policy path from
  its tree, as for exit 0. `tools/loop/guard.py#run_guard_plant` stages `push-merge-resurrect-deleted-policy`
  as main deleting the policy file, the run committing `fx-run.txt`, and the merge keeping the run's file.
- `tools/loop/guard.py#check_push_range` grades an `uncomputable` or `conflicted` merge against its parents
  unless the combined diff leaves out the policy path or the first parent's blob equals the merge's; a
  parent past the first whose blob does not parse reads `does not parse at parent <sha8>`, and a merge
  blob that does not parse reads `at M` first. `PLANTS` holds no plant staging an unparseable parent.
- `tools/memory-tree/gen_build_index.py#scan_glob_readers` builds its docstring ids inline over
  `ast.Module` and its `scopes`, `FunctionDef`, `AsyncFunctionDef` and `ClassDef`. The module imports
  `tree_lib` at module level. Its self-test's planted module, under the glob-reader arm, holds module,
  function and class docstrings and no `async def`. A grep for `body[0].value` across `tools/` finds that
  set and one self-test helper of the same module that reads one function's docstring, left as it is.
- `tools/memory-tree/tree_lib.py` imports no engine of its kit. `tools/loop/loop_transition.py`,
  `tools/chain-packet.py` and `tools/check-spec-tokens.py` read it from outside the kit;
  `tools/loop/loop_lib.py#read_memory_tree` puts the kit's folder on `sys.path`, and
  `tools/loop/loop_transition.py` then imports `tree_lib` inside its function.
- `tools/loop/loop_lib.py` binds no module-level name to a string naming a conf. `tools/loop/budget.py` and
  `tools/loop/breakpoints.py` each import names from `loop_lib`. A probe of S1 and S10's rule, with 80 S1's
  boundary, over the two modules finds no reader call, no conf name mid-string and no conf constant, and
  two conf names in `tools/loop/breakpoints.py#write_pre_placement_tree`, which 80 S2 renames into the
  boundary.
- Every `.memory-tree.conf` a plant under `tools/loop/` writes sets `MEMORY_ROOT`; gov's own
  `.unattended.conf` sets no `MEMORY_ROOT`, and its `.memory-tree.conf` sets `memory`.
- 74 rev-3 S2 prints a skipped file as `<name> · skipped — <reason>`, naming the remote by name and never a
  URL; 77 rev-3 §4 "The plants" stages `url-forms` over `https://u:SECRET@127.0.0.1:9/r.git` and a failing
  fetch, on `tools/loop/position.py#write_position_plant`'s bare `<top>/o.git`; 75 rev-10 S34 runs each
  position plant with `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM` pointed at one empty file.
- The comment of `tools/unattended/unattended.sh#norm_endpoint` records the two regression pairs S19
  plants.
- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1 and Python 3.14: `git fetch` from
  `http://user:tok@127.0.0.1:<port>/r.git`, served by `python -m http.server` over a bare repository
  after `git update-server-info`, wrote `branch 'main' of http://127.0.0.1:<port>/r` into `FETCH_HEAD`,
  and `http://user@127.0.0.1:<port>/r.git/` wrote the same: PINNED, that date.
- `TOOL-dDeclaredLoop-67` rev-4 S30 mints `loop definition fixtures`, argv `loop_lib.py --selftest`, with
  no `guard`. Of the units ordered at or after 67, the specs of 67, 79 and 80 name
  `tools/loop/loop_lib.py` under §4 Files touched; 76, at order 37, is in 79 S10's population.
  `tools/run-gates/lib-attribute.sh#add_scratch_worktree` and
  `tools/run-gates/measure_legs.py#derive_leg_argv`, which 75's probe runs on, are built.

### The conf-read rule, after this unit (S1, S8, S10)

```
derive_conf_reads(path):                                 # 76 S2's, with 80 S1's boundary
    tree    = ast.parse(read(path), path)
    read_memory_tree("tree_lib.py"); from tree_lib import derive_docstring_ids    # inside the function
    docs    = derive_docstring_ids(tree)                 # Module, ClassDef, FunctionDef, AsyncFunctionDef
    bounded = 80 S1's set
    aliases = derive_import_aliases(tree)                # local name -> dotted imported name
    consts  = {}
    if some alias value is "loop_lib" or opens "loop_lib.":                        # §8 F6
        consts = module-level Assign targets of <folder of path>/loop_lib.py whose value is a str
                 Constant containing a conf name, by ast.parse; a missing or unparseable file raises
    for node outside docs and bounded:
        Call, callee Name n with aliases.get(n, n)'s last segment, or Attribute .a with a, among
             read_design_conf, read_driver_conf, parse_conf                    -> (line, "reader call")
        Constant str containing ".memory-tree.conf" or ".unattended.conf"      -> (line, "conf name")
        Name n with aliases[n] == "loop_lib.<c>", or Attribute v.c with aliases[v] == "loop_lib",
             c in consts                                                        -> (line, "conf constant")

derive_import_aliases(tree):
    import a.b as c  -> c: "a.b"         import a.b      -> a: "a"
    from m import n as c -> c: "m.n"     from m import n -> n: "m.n"
    a relative import and a star import bind no entry
```

### The source (S15)

```
resolve_memory_root_source(tree):                        # 76 S1's, one branch changed
    ... 76 S1's body to its memory-tree branch, unchanged
    if mt: return mt, ".memory-tree.conf"
    if (tree / ".memory-tree.conf") is a file: return "memory", ".memory-tree.conf"
    return "memory", "default"
```

### The plants

| Plant | Module | Staged | Owed |
|---|---|---|---|
| `conf-read-forms` | `budget.py` | a branch of `run_budget_plant`, which 80 S1 bounds, writing each row's module into a scratch folder that holds a `loop_lib.py` binding `UNATTENDED_CONF = ".unattended.conf"`, then `derive_conf_reads` over it: (1) `import loop_lib as ll` and `def read_root(tree): return (tree / ll.UNATTENDED_CONF).read_text()`; (2) the same line in `def check_plant_root(tree)`; (3) a `bash -c` string `. "$ROOT/.unattended.conf"; printf %s "$MEMORY_ROOT"` passed to `subprocess.run` in `def read_root_bash()`; (4) `from loop_lib import read_driver_conf as rdc` and `def read_root(tree): return rdc(tree, ["MEMORY_ROOT"])`; (5) module, class, function and `async def` docstrings each naming `.unattended.conf`, nothing else; (6) row 1's module in a second folder with no `loop_lib.py` | one `conf constant`; none; one `conf name`; one `reader call`; none; a raise naming the missing `loop_lib.py` |
| `root-source`, two trees more | `budget.py` | 76's three folders, and two more, each `git init`: one holding `.unattended.conf` as `PHASES_EXTRA=""` alone, one holding `.memory-tree.conf` as `FAMILIES="tool:TOOL"` alone | `(memory, .unattended.conf)` and `(memory, .memory-tree.conf)`, beside 76 AC3's three |
| `push-merge-resurrect-deleted-policy-conflict-elsewhere` | `guard.py` | `push-merge-resurrect-deleted-policy`'s history, with main also adding `fx-run.txt` apart from the run's; the run merges main with `--no-commit`, git stops on `fx-run.txt` alone, the run takes its own `fx-run.txt` and its own policy file and commits with no trailer | exit 1 naming `review.max-rounds`, as that plant owes |
| `push-merge-unparseable-parent` | `guard.py` | from the plant base: `b1` sets `review.max-rounds`, `b2` appends a second `[review]` table, main sets the cap; the merge's tree is main's policy file with `b1`'s value taken, written with `git write-tree` and joined to main, `b1` and `b2` by `git commit-tree`, since an octopus merge of a file that does not parse would make M not parse; graded over `<b2>..<the merge>`, so b2's own commit, which the non-merge grade refuses `on one side`, sits outside the range | exit 1 printing `does not parse at parent <b2's sha8>`, no `Traceback` |
| `url-forms`, the mismatch row | `position.py` | after 77's reading, `FETCH_HEAD` written as one line `<main's sha>\t\tbranch 'main' of https://other.example/r`; the engine reads `r` with no fetch | `stale-remote`; the entry `FETCH_HEAD · skipped — no line for main of origin`; no printed line and nothing in `json.dumps` of the position holds `SECRET` |
| `url-forms`, two table rows | `position.py` | S19's pairs appended to 77's table | as tabled, printed as 77 S3 prints its rows |
| `url-forms`, the git-written row | `position.py` | `git update-server-info` in `<top>/o.git`; a `http.server.ThreadingHTTPServer` on `("127.0.0.1", 0)` serving `<top>` from a daemon thread; `git remote add web http://user:tok@127.0.0.1:<port>/o.git` in `r`; `git -c credential.helper= fetch -q web` through `read_git`, its environment putting `GIT_TERMINAL_PROMPT=0` and `NO_PROXY=127.0.0.1` for that call alone; the server shut down in a `finally` | the row `position: fixture · url-forms · git-written · <derive_fetch_url of the configured URL> against <the URL after `of` on FETCH_HEAD's first line> · equal`, the configured URL holding `user:tok@` |

The git-written row runs last, so its `FETCH_HEAD` is no earlier row's. Its printed row carries the
configured URL only as `derive_fetch_url` spells it, so no user part is printed.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_docstring_ids` | Python function in `tools/memory-tree/tree_lib.py` | `py.function`, verb-first |
| `derive_import_aliases` | Python function in `tools/loop/loop_lib.py` | `py.function`, verb-first |
| `conf-read-forms` | a `PLANTS` name of `budget.py` | none |
| `push-merge-resurrect-deleted-policy-conflict-elsewhere`, `push-merge-unparseable-parent` | `PLANTS` names of `guard.py` | none |
| `conf constant` | a hit kind `derive_conf_reads` answers | none |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for both functions, each
leading with the declared verb `derive`, run on this worktree's main at `179486e8f`, whose
`.lexicon.conf` differs from the tip's in its `VERB_OFFENDER_PIN` alone.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/README.md`
- `tools/loop/kit.toml`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/run-gates/selftest-budgets.txt`, only where a timed reading at the close re-prices a row
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

### Alternatives rejected

- **One unit per minor.** BUILD-METHOD M4 forbids it.
- **Amending the CLOSED siblings' specs, as rev-6 wrote.** §8 F5.
- **Reading the bindings from the kit's own `loop_lib.py` always.** §8 F6.
- **Extracting the whole of `scan_glob_readers`' walk with a predicate.** Its walk carries the charge
  rule's scope tracking, which `derive_conf_reads` has no use for; the docstring set is the part both
  walks share, so S8 extracts that.
- **`derive_import_aliases` in the memory-tree kit's `import_walk.py`.** That module answers which modules
  a file reaches, one row per module name with no local name, for the verdict-epoch closure and the tag
  index; a local-name map has one caller, in this kit.
- **A `CGIHTTPRequestHandler` behind `git http-backend` for S23.** That handler is deprecated in the
  Python 3.14 this node runs; the dumb protocol over `http.server` needs no CGI and was probed.

## 5. Production-readiness checklist

- security — S1 and S10 widen what the no-own-conf-read rule sees. S3 keeps a planted credential off
  every printed line and the JSON; S23's printed row carries no user part. S23's server binds `127.0.0.1`
  alone at a free port for one fetch, and that fetch clears every credential helper under 75 S34's empty
  global and system config, so the OS credential store is never written.
- perf / scale — S23 costs one local HTTP server and one fetch, seconds; S21 costs one scratch worktree
  per probed commit, once at this pass.
- error / empty / loading states — a module importing `loop_lib` with no readable `loop_lib.py` beside it
  raises, never an empty constant set (§8 F6); S21 follows a `no leg` answer to the leg's first exit.
- observability — each hit names its kind; each probe line names the unit, the leg and the exit.
- risks — a conf name composed at run time, or a constant bound by an `AnnAssign`, a `Path(...)` or a star
  import, still passes until 86 S13. The `conf-read-forms` rows spell `read_driver_conf` in `budget.py`
  (the sweep).
- testing — AC1 to AC24 as plants, probes, greps and ledger reads; the arms under §7, observed RED then
  GREEN at the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed.
- user docs — none user-facing; the kit README and its descriptor comment carry the reaches (S24).

### The sweep

Read at the tip `77130f24` in the scratch copy; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `derive_conf_reads` widened (S1, S10) | its callers at this pass: the `no-own-conf-read` cases of `budget.py` and `breakpoints.py` and 80's staged module; 76 AC2's probe module | the base probe, AC1's first step, runs the widened rule over both live modules before any edit, and a hit outside the boundary in a reader stops the pass as a deviation; neither scratch module imports `loop_lib`, so no binding is read (§8 F6), and every hit 76's ending rule found is a containing hit too |
| the same | the legs `loop budget fixtures` and `loop breakpoint fixtures`, which run every plant | both modules import from `loop_lib`, whose file sits beside them; the tip's live hits all sit inside 80's boundary |
| `derive_docstring_ids` minted in `tree_lib.py` (S8) | every importer of `tree_lib`: the memory-tree engines, `loop_transition.py`, `loop_witness.py`, `chain-packet.py`, `check-spec-tokens.py`; govkit's self-test that loads `tree_lib` for its conf-parser parity | a new name and a stdlib `import ast` alone; no name moves, and `tree_lib` still imports no engine |
| `tree_lib.py` and `gen_build_index.py` edited | the `DELEGATES` of `tools/memory-tree/check-verdict-epoch.sh`, which names both | `KIT_MEMORY_TREE_VERSION` is minted by the lander; off the push boundary the gate prints `owed at the lander` and exits 0 |
| `scan_glob_readers`' set (S8) | its one call, the glob-reader self-test arm, which owes eight charged names over its planted module | the set is the same ids; the planted `async def`'s docstring is charged to nothing, so the owed list holds |
| `resolve_memory_root_source`'s memory-tree branch (S15) | 75 S7's explain line and S8's held line; 76 AC3's three folders; 79's `no-confs`; adapt's and every other plant's root | no plant at the tip stages a memory-tree conf without the key, so no owed line moves; the root of the branch stays `memory`; `no-confs` holds neither conf and keeps `default` |
| `PLANTS` of `guard.py` gains two, of `budget.py` one; `position.py`'s `url-forms` gains rows | each module's `run_selftest`, `main` and usage line; `run_selftest`'s owed map in `guard.py` | each reads the dict; the guard plants join the owed map at 1; no flag is added, so the usage rows of `tools/govkit/usage.toml` and the anchors on `help/loop.md` hold |
| the same | budget rows in `tools/run-gates/selftest-budgets.txt`: `loop budget fixtures` 476 seconds PINNED, `loop guard fixtures` 90 seconds PINNED, `loop position fixtures` 411 seconds PINNED, `build-index selftest` 140 seconds PINNED; manifest ceilings 300 seconds PINNED for the loop legs and 350 seconds PINNED for build-index | a row a timed reading at the close passes is re-priced by that file's rule, PINNED with date and node; no ceiling is raised |
| `derive_import_aliases` and `derive_docstring_ids` minted | `memory/map/generated/symbols.json` and its three siblings, under `codebase-map coverage + freshness`; the lexicon offender pin | `python tools/codebase-map/gen_map.py --write` regenerates them; both names lead with a declared verb |
| 72 AC4's grep half | its count of `read_design_conf`, `read_driver_conf` and `parse_conf` over `budget.py`, whose `conf-read-forms` row 4 spells one | 72 is CLOSED and its AC4 is observed at its pass; 76 S4 holds the lasting observation on the syntax tree, which passes over the bounded rows |
| shipped bytes | `install-prefix (shipped surface)` and `kit epoch (shipped bytes move, the version moves)` | the new lines name no kit path; the loop and memory-tree versions are minted at the lander |
| this spec's citations | `memory/project/positional-refs.txt`, its 9 PINNED rows for this spec, line citations among them, under `positional (the citation check alone)` | this revision cites symbols only, so the commit landing it runs `python tools/playbook/positional.py shrink`, which takes the stale rows out |
| this spec's labels | 72, 75 to 81 and 84 name this unit in hands-off bullets; 86, 87, 88, 89, 90, 97 and 98 consume S1, S6, S8, S10, S14, S21, AC4, AC5, AC10, §4's sketch and the two plants | every edge is kept; each kept label keeps its number and meaning, and the sketch keeps its heading; 86's and 88's asks of S6, S14, AC5, AC6 and AC22 meet items in §3 and re-ground at their own pass; 86 S13's missing-file refusal and S15's sibling folder are written here already (S1, F6) |

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -w -e derive_conf_reads -e resolve_memory_root_source -e derive_import_aliases -e derive_docstring_ids "$B" -- tools   # none: 76, 80 and this unit are unbuilt
git grep -n -w scan_glob_readers "$B" -- tools                          # its def, one comment, one call in its self-test
git show "$B:tools/memory-tree/gen_build_index.py" | grep -n 'body\[0\]\.value'
git show "$B:tools/memory-tree/check-verdict-epoch.sh" | grep '^DELEGATES='   # names tree_lib.py and gen_build_index.py
git grep -l -w tree_lib "$B" -- tools
git show "$B:tools/loop/loop_lib.py" | grep -n '^[A-Z_]* *=.*\.conf'      # none
git grep -n 'memory-tree\.conf"' "$B" -- tools/loop                         # each staged conf sets MEMORY_ROOT
git show "$B:tools/loop/guard.py" | grep -c -e unparseable-parent -e conflict-elsewhere   # 0
git show "$B:tools/run-gates/selftest-budgets.txt" | grep -e '^loop budget fixtures' -e '^loop guard fixtures' -e '^loop position fixtures' -e '^build-index selftest'
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-82.md'   # 9
git grep -n 'TOOL-dDeclaredLoop-82' "$B" -- memory/builds/dDeclaredLoop/spec/ | grep -e hands-off -e consumes-from
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED; both minted
  functions lead with a declared verb (§4 "Inventory").
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead, since
  no ceiling or pin is raised.
- The refusal ceilings and families: no `*.sh` is edited, and `tools/memory-tree/check-arms.py#branches`
  and `tools/memory-tree/check-arms.py#scan_refusal_sites` read tracked `*.sh` files alone. The driver's
  ceiling in `REFUSAL_CEILINGS` stays 343 PINNED, and `tools/unattended/unattended.families.txt` does not
  move.
- Help anchors: no verb or flag is added; the three plants are values of the anchored `--plant`.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added, so
  `tools/govkit/subject-pins.tsv` and `tools/gate-legs.json` do not move; the two memory-tree delegates are
  dated at the lander (the sweep); no data changes shape, so no `[[upgrade]]` row is owed; no edited path is
  on the `watch:` line of `memory/guides/SESSION-KICKOFF.md`.

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                  # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'               # the driver's 343
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git show "$B:tools/govkit/subject-pins.tsv" | grep -e '^loop budget fixtures' -e '^loop guard fixtures' -e '^loop position fixtures' -e '^build-index selftest'
```

### Dependency

This unit builds alone at order 41 and reads the landed code of every earlier order. Written on the
committed specs: `TOOL-dDeclaredLoop-72` rev-6 (order 36, building now) for `resolve_memory_root` and AC4;
`TOOL-dDeclaredLoop-76` rev-6 (order 37) for `derive_conf_reads`, `resolve_memory_root_source` and the
`no-own-conf-read` and `root-source` plants; `TOOL-dDeclaredLoop-80` rev-6 (order 38) for
`derive_fixture_boundary` and `write_pre_placement_plant`; `TOOL-dDeclaredLoop-74` rev-3 (order 38) for
`derive_fetch_url`, `check_fetch_head` and the skip entry; `TOOL-dDeclaredLoop-67` rev-4 (order 38) for
`loop definition fixtures`; `TOOL-dDeclaredLoop-75` rev-10 and `TOOL-dDeclaredLoop-77` rev-3 (order 39)
for the exit-1 reading, the empty git config, the pass-commit probe and the `url-forms` plant;
`TOOL-dDeclaredLoop-79` rev-6 (order 40) for its pre-filter, its `url-forms` rows and its budget plants.
`read_driver_conf` (`TOOL-dDeclaredLoop-70`), the guard's C states and refusals (78, 81, 85) and
`read_memory_tree` are built. Units 33, 54, 55, 63 and 64, built since the last re-grounds, touch no
file this unit edits; 64's `pre-placement-records-root` plant stages its memory-tree conf with the key
set. `TOOL-dDeclaredLoop-86` builds next, at order 42, over this unit's code. `TOOL-dDeclaredLoop-34` is
deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s numeric direction against ask
TOOL-dDeclaredLoop-114; neither moves a read this unit makes. The reuse probes and the lexicon suggestion
ran on this worktree's main at `179486e8f`; every other claim was read on the branch tip.

## 6. Acceptance criteria

Each `python budget.py`, `python guard.py` and `python position.py` command below runs in the loop kit's
folder.

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs, its first row answers one
  `conf constant` hit on the `ll.UNATTENDED_CONF` line, its second row, the same line inside
  `check_plant_root`, answers none, and its sixth row, the first row's module with no `loop_lib.py` beside
  it, answers a raise naming that missing file. Before its first edit the pass runs the widened rule over
  `budget.py` and `breakpoints.py` at its base and records every hit with its enclosing function.
  Red when: a name bound to a conf in `loop_lib.py` reads as no read outside the boundary, or a module
  importing `loop_lib` with nothing beside it reads as holding no constant.
- **AC3** — When `python position.py --fixture --plant url-forms` runs, its output holds
  `FETCH_HEAD · skipped — no line for main of origin` and no line holding `SECRET`; with the skip reason
  staged to name the configured URL in place of the remote's name, a line holding `SECRET` appears.
  Red when: the plant's only reading is the failed fetch's `skipped — empty`, so the mismatch path is never
  reached.
- **AC4** — When `python guard.py --fixture --plant push-merge-resurrect-deleted-policy-conflict-elsewhere`
  runs, it exits 1 naming `review.max-rounds`; and `python guard.py --fixture --plant push-merge-tree-fatal`
  exits 1 printing `the clean re-merge failed: 128`.
  Red when: an exit-1 re-merge whose conflicts leave out the policy path reads `conflicted`, so the
  parent's equal blob exempts the merge and the plant exits 0, or a fatal exit falls to the parents.
- **AC8** — When a `python -c` probe imports `tree_lib` from `tools/memory-tree/` and calls
  `derive_docstring_ids` on a module whose `async def` opens with a docstring, the answer holds that
  docstring's id; and `awk '/^def scan_glob_readers/,/^def cmd_selftest/' gen_build_index.py` in
  `tools/memory-tree/` piped to `grep -c "body\[0\]"` prints 0.
  Red when: either walk keeps its own docstring set, or the async scope is missing.
- **AC9** — When `python guard.py --fixture --plant push-merge-unparseable-parent` runs, it exits 1
  printing `does not parse at parent ` and no `Traceback`.
  Red when: the parents' grade reads the unparseable parent as the empty table, skips the merge or raises.
- **AC10** — When `python budget.py --fixture --plant conf-read-forms` runs its third and fourth rows, the
  `bash -c` string answers one `conf name` hit and `rdc(tree, ["MEMORY_ROOT"])` one `reader call` hit.
  Red when: only a trailing conf name counts, or an alias hides the reader.
- **AC15** — When `python budget.py --fixture --plant root-source` runs, the tree holding `.unattended.conf`
  alone without `MEMORY_ROOT` answers `(memory, .unattended.conf)` and the tree holding `.memory-tree.conf`
  alone without the key answers `(memory, .memory-tree.conf)`, beside 76 AC3's three, and it prints `held`.
  Red when: the memory-tree conf's unset-key branch reads `default`.
- **AC16** — When `python budget.py --fixture --plant conf-read-forms` runs its fifth row, the module whose
  module, class, function and `async def` docstrings each name `.unattended.conf` answers no hit.
  Red when: an async docstring reads as a conf name.
- **AC19** — When `python position.py --fixture --plant url-forms` runs, it prints
  `github.com:alice/repo against github.com:bob/repo · unequal` and
  `git@github.com:alice/repo against github.com:alice/repo · equal`.
  Red when: the scp regression pairs `norm_endpoint`'s comment records are absent from the table.
- **AC21** — When this unit's acceptance ledger is read, it holds a `loop definition fixtures` line for the
  pass commit of each unit the derivation names, re-derived by
  `grep -l 'tools/loop/loop_lib.py'` over the §4 Files touched of the specs at orders 38 to 40, each
  line an exit, or `no leg` followed by the leg's exit at a later pass commit, every exit 0.
  Red when: a pass broke the definition fixtures and no line attributes it.
  cost: one scratch worktree per probed commit.
- **AC23** — When `python position.py --fixture --plant url-forms` runs, it prints a `git-written` row reading
  `equal`, its configured URL holding `user:tok@`; with `derive_fetch_url` staged to keep the user part, that
  row reads `unequal`.
  Red when: the only https oracle is a table typed from the same reading 77 S1 implements.
  cost: one local HTTP server and one fetch, seconds.
- **AC24** — When `grep -c "derive_import_aliases"` and `grep -c "derive_docstring_ids"` run over the kit's
  README, tools/loop/README.md, and `grep -c "derive_conf_reads"` over its descriptor, tools/loop/kit.toml,
  each prints at least 1.
  Red when: a library function or a reach ships and the kit's own pages do not name it.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory-recall kit selftest` · `drift-audit selftest` · `playbook render selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `every held leg is budgeted, every budget row resolves` · `lexicon naming predicates` · `positional (the citation check alone)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop legs this pass keeps green sit outside the base manifest the leg line is joined against, each
declared by the unit that built or mints it: `loop budget fixtures` (`TOOL-dDeclaredLoop-30`),
`loop guard fixtures` (`TOOL-dDeclaredLoop-2`), `loop position fixtures`, `loop breakpoint fixtures`
(`TOOL-dDeclaredLoop-19`), whose `no-own-conf-read` plant runs the widened rule, the leg
`loop definition`, which runs `loop_lib.py --check`, and the leg `loop definition fixtures`
(`TOOL-dDeclaredLoop-67`), which runs `loop_lib.py --selftest`. None carries a `guard`, so every bar
runs each.

New arm: tools/loop/budget.py · covers AC1 AC10 AC15 AC16 · the conf-read-forms rows and the two unset-key root-source trees, staged against 76's trailing-only, alias-blind rule and a source reading default for a lone memory-tree conf · none
New arm: tools/loop/guard.py · covers AC4 AC9 · the conflict-elsewhere deleted-policy and unparseable-parent plants, staged against an exit-1 re-merge read as conflicted and a parents' grade reading an unparseable parent as the empty table · none
New arm: tools/loop/position.py · covers AC3 AC19 AC23 · the mismatch-line SECRET row, the scp regression pairs and the git-written http row, each staged as its criterion's Red when · none
New arm: tools/memory-tree/gen_build_index.py · covers AC8 · the glob-reader arm gains an async docstring holding the pathspec, staged against a docstring set without AsyncFunctionDef · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records; first resolved 2026-10-24, re-read at rev-7.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (the Derived line PLAY-dClosedLoop-2)
- **F2 — Which source does an unset key name (id 10)?** (a) the conf whose branch answered; (b) `default`
  wherever the value is the driver's default. (b) prints `default` for a tree whose `.unattended.conf`
  exists and decides the root, hiding which file to edit; (a) names that file, and is the skeptic's sound
  fix. 76 rev-6 already takes (a) for `.unattended.conf`; S15 takes it for `.memory-tree.conf`. First
  resolved 2026-10-24. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F3 — Re-observe 79 AC10 at 72's commit by an absent-leg line, an edge 72 <- 71, or a lower order for
  71 (id 6)?** An edge or an order would amend 71 and 72, both built first; the absent-leg line is
  observable at the pass. First resolved 2026-10-24 as the absent-leg line. At rev-7 S6 is settled in §3,
  75's `no leg` line and 79's derivation holding it, so the pick binds S21's follow-on alone.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (the absent-leg line)
- **F4 — Name the fixture conf through a loop_lib constant only, or count such a constant outside the
  boundary too (id 1)?** Counting it is M1's negative case and the only form that closes the
  `loop_lib.UNATTENDED_CONF` read M1 describes. First resolved 2026-10-24.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (count it, S1)
- **F5 — Where does an item go whose fix is text in a sibling spec that is CLOSED when this unit builds?**
  Every sibling rev-6 amended, 72 and 75 to 79, builds at an earlier order, and the build method's
  spec-exit paragraph holds a CLOSED spec frozen, its correction a new unit on top. (a) Amend them at this
  pass, as rev-6 wrote: it rewrites landed records the build method freezes. (b) Each text half leaves the
  scope, settled where a committed spec or the built code already holds its point (§3), and each code half
  stays here with its own observation. (c) A repair unit amends the unbuilt siblings now: a new unit
  outside this re-ground's mandate, and the siblings' own re-grounds already hold most halves.
  Recommendation: (b). The body is written on it. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (b)
- **F6 — When does `derive_conf_reads` read `loop_lib`'s bindings, and from which file (S1)?** (a) Always,
  from the kit's own `tools/loop/loop_lib.py`: AC1's scratch module could then bind no constant, so S1
  has no failing case. (b) Always, from the `loop_lib.py` beside the scanned module: 76 AC2's probe module
  and 80's staged module sit where none exists, so the read either answers an empty set, a silent empty
  population, or raises on two built plants. (c) From the `loop_lib.py` beside the scanned module, only
  where the module imports `loop_lib` in a form `derive_import_aliases` answers, a missing or unparseable
  file there raising: a module with no such import has no name to resolve, so 76's and 80's scratch
  modules read as at their passes, and both live modules import from `loop_lib`. Recommendation: (c),
  which also writes 86 S15's sibling folder and S13's missing-file refusal. The body is written on it.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (c)

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-5 spec audit's 23 minors batched (10 MEDIUM, 13 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-84 and TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-87 and TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-89 and TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-97 and TOOL-dDeclaredLoop-98, written by the round-12 spec audit's disposal; nothing else moved.
- rev-6 · 2026-11-15 · S4 · AC4 · written by the repair unit TOOL-dDeclaredLoop-84 for id 7 of
  2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit: S4 keeps the rest of 75 S27's exit table as
  TOOL-dDeclaredLoop-83 writes it, and AC4 greps 75 for the retired fallback and for 83's clause and
  re-runs 81's `push-merge-tree-fatal` plant; nothing else moved.
- rev-7 · 2026-11-16 · §1 to §10 · S1 to S24 · AC1 to AC24 · §8 F1 to F6 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `77130f24` and on the committed specs of TOOL-dDeclaredLoop-72
  rev-6, 67 rev-4, 74 rev-3, 75 rev-10, 76 rev-6, 77 rev-3, 79 rev-6 and 80 rev-6 and the CLOSED 78 rev-7,
  per the brief 2026-11-16-prompt-TOOL-dDeclaredLoop-82-1-spec-writer: no sibling spec is amended, its
  siblings being CLOSED at this order (F5); S2, S5 to S7, S11 to S14, S17, S18, S20, S22 and the text
  halves of S4, S9, S16, S19 and S21 move to §3 with what settles each, and their criteria with them; S1
  reads the bindings beside an importing module only (F6); S3 is written on 74's skip entry, S10 on 76's
  three reader names, S15 on 76's settled `.unattended.conf` branch, S21 on 75's probe and 67's leg, S23
  with its credential helper cleared and no user part printed; S24 carries the two minted functions;
  AC4 keeps 84's tree-fatal re-run without the greps of a CLOSED 75; the edges' payloads restated; line
  citations made symbol citations; the sweep and the budgets.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 76's `derive_conf_reads` with 80's
boundary (S1, S10), the docstring set `tools/memory-tree/gen_build_index.py#scan_glob_readers` already
builds, lifted into `tools/memory-tree/tree_lib.py` and reached through the loop kit's own
`tools/loop/loop_lib.py#read_memory_tree` (S8), 76's `resolve_memory_root_source` (S15), 77's `url-forms`
plant over 74's `derive_fetch_url` and the norm_endpoint comment's own pairs (S3, S19, S23), the guard's
`run_guard_plant` histories and `run_selftest` owed map (S4, S9), and 75's pass-commit probe on the
run-gates kit's `add_scratch_worktree` and `derive_leg_argv` (S21).
`python tools/codebase-map/reuse_lookup.py "collect the docstring nodes of a parsed python module"`, on this
worktree's main at `179486e8f`, ranked `parse`, `parse_args`, `parse_conf`, `parse_unit_rows`,
`resolve_python` and `parse_spec_h1`, none a docstring walk; the grep for `body[0].value` across `tools/`
found the set S8 lifts.
`"resolve import aliases of a parsed python module"` ranked `parse`, `resolve`, `resolve_kit_dir`,
`parse_args`, `resolve_prefix_token` and `parse_conf`, none an alias map; the memory-tree kit's
`tools/memory-tree/import_walk.py#scan_imports` answers module names with no local name (§4 "Alternatives
rejected"), so no existing seam fits `derive_import_aliases`.
`"serve a git repository over http for a fetch fixture"` ranked `git`, `fixture`, `run_git`,
`build_fixture`, `read_git_output` and `GIT`, none serving a repository, so no existing seam fits S23's
server.

Recall terms used: spec-audit minors batch derive_conf_reads docstring AsyncFunctionDef url-forms FETCH_HEAD oracle conf constant import alias pass-commit probe loop definition fixtures CLOSED frozen
