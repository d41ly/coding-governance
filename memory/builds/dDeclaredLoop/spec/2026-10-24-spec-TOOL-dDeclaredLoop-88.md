# TOOL-dDeclaredLoop-88 — the round-7 spec audit's 36 minors, batched

**Status:** DEFERRED · rev-6 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 44 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-881.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-881.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-882.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-88-deviation-882.md) | deviation | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-88-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-88-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-88-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-88-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-88-2-spec-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-88-2-spec-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-88-3-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-88-3-spec-writer.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-87 |

<!-- /gen:spec-records -->

## 1. Goal

The round-7 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md`)
exited CONVERGED with 37 confirmed findings over units 83 to 86, the round-6 promotions, PINNED from the
report. Its one high, id 29, is unit 87. This unit is the batch
`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` makes of the rest, every
MEDIUM and every LOW, each by its report id and each its own scope item, where the report merged ids into
one item too. The minors land on 83, 84, 85 and 86, so this unit repairs none in particular and builds
after every unit they name, at order 44, after 89 at the same order.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1 | S1 |
| M2 | MEDIUM | 2, 20 | S2, S3 |
| M3 | MEDIUM | 3, 21 | S4, S5 |
| M4 | MEDIUM | 4, 31 | S6, S7 |
| M5 | MEDIUM | 5 | S8 |
| M6 | MEDIUM | 7 | S9 |
| M7 | MEDIUM | 8 | S10 |
| M8 | MEDIUM | 11 | S11 |
| M9 | MEDIUM | 16 | S12 |
| M10 | MEDIUM | 17 | S13 |
| M11 | MEDIUM | 23 | S14 |
| M12 | MEDIUM | 25 | S15 |
| M13 | MEDIUM | 30 | S16 |
| M14 | MEDIUM | 32 | S17 |
| M15 | MEDIUM | 33 | S18 |
| M16 | MEDIUM | 34 | S19 |
| L1 | LOW | 6, 19 | S20, S21 |
| L2 | LOW | 9 | S22 |
| L3 | LOW | 10, 18, 28, 37 | S23, S24, S25, S26 |
| L4 | LOW | 12, 26 | S27, S28 |
| L5 | LOW | 13 | S29 |
| L6 | LOW | 14 | S30 |
| L7 | LOW | 15 | S31 |
| L8 | LOW | 22, 36 | S32, S33 |
| L9 | LOW | 24 | S34 |
| L10 | LOW | 27 | S35 |
| L11 | LOW | 35 | S36 |

That is 19 MEDIUM and 17 LOW findings by raw id, PINNED from the report. Four defects span two grades,
and each is fixed once across its items: M3 with L4, M12 with L1, M6 with L11, and M11 with L9. The
report refuted no finding.

Re-grounded at rev-6, six items still build, each a change to the code or the plants of the loop kit or
the memory-tree kit: S13, S16, S17, S19, S26 and S33. The other thirty asked a rev bump of a sibling spec
that is CLOSED when this unit builds, re-observed a sibling's pass, or are already true at the tip or in
a committed spec. §3 "The rev-5 items the built code, a committed spec or a frozen record settles" says
what settles each, keeping its number (§8 F5).

## 2. Scope (IN)

The labels keep their rev-5 numbers; every other rev-5 item is in §3.

- **S13** — id 17. `derive_constant_charges(tree, module, is_needle)` in `tools/memory-tree/tree_lib.py`
  is the charge walk `tools/memory-tree/gen_build_index.py#scan_glob_readers` holds at the tip, lifted
  whole: its four charge rules unchanged, its docstring set read from `derive_docstring_ids(tree)` (82
  S8), and its needle test over a str constant's value read as `is_needle(value)`. It answers the sorted
  pairs `(owner, rule)`, one per owner a charge names, `rule` the number of the rule that charged it and
  `module` the first segment of every owner. The charge-rule paragraph of `scan_glob_readers`' docstring
  moves to the new function's, and `scan_glob_readers` points at it. `scan_glob_readers` keeps its
  composed needle and its loop over the kit's modules and answers the owners of
  `derive_constant_charges(tree, <module stem>, lambda s: magic in s)`; its closure `scan_scope` is
  removed, so one walk decides every charge. `derive_conf_constants(loop_lib_path)` in
  `tools/loop/loop_lib.py` answers each name `n` whose pair `(<stem>.n, 2)` the walk answers over that
  file with the two conf names as its needle, a name qualified by the module alone, united with
  `derive_conf_rebinds` (89 S1), the union 89 S2 writes over 87's walk kept. That slice answers
  every name 87 S1's class answers, 87 AC2's probe set unchanged, and also a module-level binding whose
  targets or annotation hold a conf name, which charge rule 2 charges and 87 S1 does not (§4 "The lifted
  charge walk (S13)"). Observed by AC13.
  **Readers:**
  by name: tools/memory-tree/gen_build_index.py, whose function scan_glob_readers holds the one spelling of the closure
  by value: `tools/memory-tree/gen_build_index.py` (the glob-reader self-test arm, which owes the same eight charged names over its planted module, PINNED at the tip)
- **S16** — id 30. `tools/loop/guard.py#run_merge_tree_usage` runs `git merge-tree -h` with
  `env=read_clean_env(LC_ALL="C", LANGUAGE="")`, the two names set in that call's environment alone
  through `tools/loop/loop_witness.py#read_clean_env`, which copies the process environment, so a git
  that ships translations prints its usage header untranslated and `check_write_tree_usage` reads it.
  Its streams are already decoded as UTF-8 with `errors="replace"`. The push arm paragraph of the module
  docstring says the usage probe runs under `LC_ALL=C`. Observed by AC16.
- **S17** — id 32. The plant `push-merge-probe-failed-trailered` joins `PLANTS` in
  `tools/loop/guard.py`, a case of `run_guard_plant`'s fatal-history branch beside
  `push-merge-probe-failed`: the same history and the same probe twin raising `OSError("fx stand-in")`,
  its merge commit carrying the `Gov-Policy:` trailer that `push-merge-unrelated-histories` writes for
  `review.max-rounds` from 4 to none, and adding the change record `policy.review.max-rounds` through
  `write_fixture_record`, as that plant's recorded scenario does. Graded in process, its rows owe the
  failed line naming `probe failed: start failed: fx stand-in`, `0 finding(s)`, `merge-tree runs: 0`
  and exit 0, the owed map's default. Observed by AC17.
- **S19** — id 34. Two plants join `PLANTS` and `run_selftest`'s owed map at exit 1, each over the
  history of 86 S6's `push-merge-tree-fatal-unparseable-parent`, whose main commit appends `FX_REVIEW`
  twice so that main's policy blob does not parse:
  - `push-merge-probe-failed-unparseable-parent` grades in process with the probe twin raising
    `OSError("fx stand-in")`, so the merge is `failed` and the re-merge never runs;
  - `push-merge-conflicted-unparseable-parent` resolves the merge to the run branch's policy bytes plus
    one comment line, so the file differs from both parents and the combined diff lists it, and grades
    in process with `run_merge_tree` answering exit 1, its first line the merge's own tree id and its one
    conflicted path the policy path, so the merge is `conflicted` (75 rev-10 §4 "The re-merge on exit 1").
  Each owes `does not parse at parent <sha8>` naming main's tip, no `Traceback`, and its count line,
  `merge-tree runs: 0` and `merge-tree runs: 1`. Observed by AC19.
- **S26** — id 37. The plant `push-merge-probe-signal` joins `PLANTS` and `run_selftest`'s owed map at
  exit 1, a case of the fatal-history branch whose probe twin answers `(-9, "", "")`. Its rows owe the
  failed line naming `probe failed: signal 9`, the `review.max-rounds` finding and
  `merge-tree runs: 0`. The
  `push-merge-tree-fatal` grade whose re-merge answers `-9` is 86 S22's (§3). Observed by AC26.
- **S33** — id 36. `load_tree_lib()` in `tools/loop/loop_lib.py`, as 89 S6 mints it at order 44 before
  this unit, is the conf-read rule's one route to the memory-tree kit's `tree_lib`: 86 S21's
  `read_memory_tree("tree_lib.py")` and `import tree_lib`, its refusal of a module lacking
  `derive_docstring_ids`, and the call from each of `derive_conf_reads` and `derive_conf_constants`. This
  item extends that function in place with the two catches 89 S6 does not hold (§8 F7), and leaves the
  `derive_docstring_ids` refusal, the route and both calls as 89 writes them. The function raises
  `LoopError` naming `govkit update --kits memory-tree` where `read_memory_tree` raises `LookupError`,
  keeping that message and the places it names, and where the import raises `ImportError` or
  `SyntaxError`, naming that error. The `no-own-conf-read` case of `budget.py` and of
  `breakpoints.py` then reads a miss with no traceback, as 86 S21 has each catch `LoopError`. The
  `conf-read-forms` plant of `tools/loop/budget.py` gains three rows, written inside `run_budget_plant`
  as 86 S10 places its rows, each owing a `LoopError` naming `govkit update --kits memory-tree`:
  - the route's `read_memory_tree` swapped to raise `LookupError`;
  - `tree_lib` set to `None` in `sys.modules` for the call;
  - a scratch folder holding a `tree_lib.py` that does not parse, first on `sys.path`, with the route's
    `read_memory_tree` swapped to answer it and `tree_lib` absent from `sys.modules` for the call.
  Observed by AC33.

## 3. Non-goals (OUT)

- The high's mechanism, the conf-constant class: unit 87.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Following a member name inside a binding's value: 87 §8 F2 keeps the class to charge rule 2's
  predicate, and S13's slice inherits that.
- Pinning the locale of the re-merge call, `run_merge_tree`: its first stderr line is printed and never
  parsed, so a translated line changes no verdict.
- Clearing the credential-store entries the round-6 skeptic's probe left on node `d`: a write to the
  owner's environment outside the repository, as 86 §3 records.
- Refusing a `tree_lib` that lacks `derive_docstring_ids` or `derive_constant_charges`: 89 S6 raises the
  first in `load_tree_lib`, and `TOOL-dDeclaredLoop-90` S4 and S5 refuse the second over
  `TREE_LIB_SYMBOLS` at order 45 (§5 risks).
- A rev bump of any sibling spec: each spec rev-5 amended is CLOSED by order 44 (§8 F5).

### The rev-5 items the built code, a committed spec or a frozen record settles

Read on branch `unattended-declared-loop-d56bf0` at `a339daae2`. "CLOSED here" means CLOSED when this
unit builds, at order 44. Each item's criterion leaves with it.

| Item | What settles it |
|---|---|
| S1 | `TOOL-dDeclaredLoop-83` is CLOSED at order 21 and frozen, and 75 is CLOSED here. 75 rev-10 §4 "The re-merge on exit 1" builds the reading S1 states: an exit 1 whose conflicted paths hold the policy path, or that names no tree, is `conflicted` and graded against the parents, and every outcome but 0 and 1 stays `failed`. |
| S2, S3, S8 | `TOOL-dDeclaredLoop-78` is CLOSED at order 19 and frozen. The push arm paragraph of the module docstring of `tools/loop/guard.py` names the five states; `tools/loop/guard.py#read_remerge_policy` answers `failed` with `probe failed: <detail>` for a failed probe, the re-merge never run; and `tools/loop/guard.py#check_push_range` grades `present` and `absent` against C, `failed` against every parent, and `uncomputable` and `conflicted` against the parents. |
| S4, S5, S20, S21, S27 | `TOOL-dDeclaredLoop-81` is CLOSED at order 20 and frozen. `tools/loop/guard.py#check_write_tree_usage` takes `(rc, text)` and answers `supported`, `unsupported` or `probe failed`; `tools/loop/guard.py#resolve_write_tree_support` answers that answer with its detail; and `read_remerge_policy` opens `support, detail = resolve_write_tree_support()` and carries 85's three branches. 86 rev-8 S2 narrows both answers to an exit of 0 or 129 with a `usage: git merge-tree` line, in the code, at order 42. |
| S6, S7 | `TOOL-dDeclaredLoop-85` is CLOSED at order 21. Its memo is `functools.cache` on `resolve_write_tree_support`, and `run_grade_in_process` inside `run_guard_plant`, the one route every in-process grade takes, clears it before its swaps and after them, so no grade reads an answer another grade's twin or the real probe left. `guard.py --fixture` takes exactly one `--plant`, `tools/loop/guard.py#main` refusing it bare; the whole run is `guard.py --selftest`, every plant in one process through `tools/loop/loop_lib.py#run_selftest_cases`, which the leg `loop guard fixtures` runs on every bar (§8 F2). |
| S9, S36 | `TOOL-dDeclaredLoop-80` rev-6 S4 names the `conf-read-forms` rows of 82, 86 and 87 and every later plant of either module, each inside the boundary, and 80 is CLOSED here. 86 rev-8 AC10 is the boundary plant's own exit, with no clause over 80's text. |
| S10 | 86 rev-8 holds no AC12; its §3 settles its S12, 82 AC5's join naming no spec. |
| S11 | 86 rev-8 AC9 reads the store as `cmdkey //list` and has the build clear its staged target with `cmdkey //delete:<target>`. This unit writes nothing the `url-forms` plant runs, so it re-observes no fetch. |
| S12 | The pass-commit probe is a procedure 75 rev-10 §4 "The pass-commit probe" runs once at 75's pass, as 82 rev-7 §3 records for its S6, and 82 rev-7 AC21 reads its own ledger at 82's pass. Neither ships code, so no route to `tools/run-gates/measure_legs.py#read_profile_legs` is left to build; 82 and 86 are CLOSED here. |
| S14, S28, S31, S35 | 85, 83 and 84 are CLOSED at order 21 and frozen. This unit's own §4 names the map renders it regenerates once, and the build README's regions are the generator's render. |
| S15 | 85 is CLOSED; 86 rev-8 S2 builds the rule in `check_write_tree_usage`. |
| S16's spec half | 85 is CLOSED and 86 is CLOSED here; S16 builds in the code. |
| S18 | 82 rev-7 AC4 re-runs `push-merge-tree-fatal` for `the clean re-merge failed: 128` without the greps of a CLOSED 75. At the tip that plant owes `128 fatal: fx stand-in`, and exit 1 in `run_selftest`'s owed map. |
| S22 | 86 rev-8 amends no sibling spec (its §8 F5), so no passage carries an amendment to observe. |
| S23 | 85 is CLOSED. 86 rev-8 S22 spells a negative exit `signal <n>` in `build_failure_detail`, which `resolve_write_tree_support` calls with the probe's exit, so a killed probe reads `probe failed: signal 9`; S26's plant observes it. |
| S24, S25 | 86 rev-8 S22 makes `tools/loop/guard.py#build_failure_detail` the one spelling of every detail under the failed line, with the signal and empty-stream spellings, and keeps 85's `start failed: <its text>` (its §8 F6). One empty label serves both callers (§8 F6 here). |
| S26's tree-fatal row | 86 rev-8 S22 adds the `(-9, "", "")` grade to `push-merge-tree-fatal`. |
| S29 | 86 rev-8 holds no AC16; its §3 settles its S16 by 80 rev-6 AC4, one `grep -c` per plant. |
| S30 | 86 rev-8 holds no AC18; its §3 leaves 82's pins to 82, and 82 rev-7 cites symbols. |
| S32 | The sketch of 86 rev-8 §4 "The conf-constant kind, after this unit" reaches `tree_lib` through `read_memory_tree("tree_lib.py")` and `import tree_lib`, a module import, never a directory read as a module. |
| S34 | 86 rev-8 §4 Files touched names `memory/map/generated/symbols.json`. |

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-75` — the exit-1 reading of `read_remerge_policy`, which settles S1 and through which S19's conflicted plant grades (id 1)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the five states and the parse refusals the push arm grades by, which settle S2, S3 and S8 (ids 2, 5, 20)
- **consumes-from** `TOOL-dDeclaredLoop-79` — AC10, whose re-observation S22 asked, settled by 86 amending no sibling (id 9)
- **consumes-from** `TOOL-dDeclaredLoop-80` — S4's plant population, which settles S9 and S36 and holds S33's rows inside the boundary (id 7)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the three-answer probe, the `failed` state and the fatal-history plants, which settle S4, S5, S20, S21 and S27 and which S17, S19 and S26 extend (ids 3, 6, 9, 12, 19, 21)
- **consumes-from** `TOOL-dDeclaredLoop-82` — `derive_docstring_ids`, which S13's lifted walk reads, the `conf-read-forms` plant S33 extends, and AC4 and §3, which settle S10, S12 and S18 (ids 8, 9, 16, 17, 33)
- **consumes-from** `TOOL-dDeclaredLoop-83` — its CLOSED spec, which settles S1, S31 and S35 (ids 1, 15, 27)
- **consumes-from** `TOOL-dDeclaredLoop-84` — its CLOSED spec and 78's grade it restated, which settle S2, S3 and S35 (ids 2, 20, 27)
- **consumes-from** `TOOL-dDeclaredLoop-85` — `run_merge_tree_usage`, the memoised resolver, the probe plants and `build_failure_detail`, which S16, S17, S19 and S26 extend and which settle S6, S7, S14, S15, S23 and S28 (ids 4, 10, 18, 19, 23, 25, 26, 27, 30, 31, 32)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S2's narrowed probe, S6's unparseable-parent history, S21's `tree_lib` route and S22's detail builder, which S19, S26 and S33 extend, and its rev-8 text, which settles S10, S11, S22 to S25, S29, S30, S32, S34 and S36 (ids 5, 7, 8, 9, 11, 13, 14, 16, 17, 22, 24, 28, 30, 34, 35, 36, 37)
- **consumes-from** `TOOL-dDeclaredLoop-87` — `derive_conf_constants` as S1 states its class, which S13 computes as the module-level slice of the lifted walk, 87 AC2's answer unchanged (id 17)
- **consumes-from** `TOOL-dDeclaredLoop-89` — `derive_conf_rebinds`, which S13's `derive_conf_constants` unites with its rule-2 slice, and S6's `load_tree_lib`, which S13 calls and S33 extends in place, 89 building first at order 44 (the round-8 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-90` — S13, S24, S33, the lifted-walk sketch, §4 Evidence and Write set, and AC13 and AC33, with `derive_constant_charges`, `load_tree_lib` and `build_failure_detail`, which that unit restates and extends with `TREE_LIB_SYMBOLS` (the round-8 spec audit's ids 2, 3, 5, 6, 7, 11, 13, 15, 16, 21, 22, 25, 26)
- **hands-off** `TOOL-dDeclaredLoop-92` — §3's consumes-from 87 bullet, S13, S24, the lifted-walk sketch and the criteria of S1, S6, S12, S13 and S16, which that unit restates (the round-9 spec audit's ids 1, 5, 6, 22)
- **hands-off** `TOOL-dDeclaredLoop-94` — S18 and its criterion, which that unit cites in 92 S17, S24, whose range it greps, and its criterion's `OSError` spelling, which it restates (the round-10 spec audit's ids 4, 11, 20)
- **hands-off** `TOOL-dDeclaredLoop-96` — S33, which that unit restates over the caller's `need` and any exception the import raises (the round-11 spec audit's ids 7, 9)

## 4. Design

### Write set

This pass writes `tools/loop/guard.py` (S16, S17, S19, S26), `tools/loop/loop_lib.py` (S13, S33),
`tools/loop/budget.py` (S33's rows), `tools/memory-tree/tree_lib.py` and
`tools/memory-tree/gen_build_index.py` (S13). It writes the carriers `tools/loop/README.md`, whose
`derive_conf_constants` row and reach paragraph name the lifted walk (S13) and whose `load_tree_lib` row,
written by 89 S4, gains the refusals S33 adds, and the reach comment of `tools/loop/kit.toml` (S13). It
writes the generated map files `python tools/codebase-map/gen_map.py --write` renders, once. It writes no
spec but this one, and mints no `load_tree_lib`: 89 S6 does.

### The lifted charge walk (S13)

```
tree_lib.derive_constant_charges(tree, module, is_needle) -> sorted [(owner, rule)]
    docs = derive_docstring_ids(tree)                                    # 82 S8
    the walk scan_glob_readers holds at the tip, its four rules unchanged, with its needle test
    read as is_needle(value); each charged owner answered with the number of its rule
gen_build_index.scan_glob_readers(kit_dir):
    magic = ":(" + "glob)"                                               # stays here, composed
    for each *.py directly in kit_dir:
        owners of derive_constant_charges(ast.parse(<file>), <stem>, lambda s: magic in s)
loop_lib.derive_conf_constants(loop_lib_path):
    tl   = load_tree_lib()                                               # 89 S6, with S33's catches
    tree = ast.parse(<file>)                                             # missing or unparseable -> 86 S13's LoopError
    rule2 = {n for (owner, rule) in tl.derive_constant_charges(tree, <stem>, <a conf name in s>)
             if rule == 2 and owner == <stem> + "." + n and "." not in n}
    return rule2 | derive_conf_rebinds(tree, tl.derive_docstring_ids(tree))      # 89 S1, S2
```

Charge rule 2 takes every `Name` under a module-level `Assign`, `AnnAssign` or `AugAssign` target, and
charges a needle constant anywhere under that statement, its value, targets and annotation alike. 87
S1 reads the value alone, so the slice is wider by a binding such as `D[".unattended.conf"] = 1` or an
annotation holding a conf name, and equal on every binding 87's rows plant.

### The tree_lib route (S33)

89 S6's loader, the two `except` arms this unit's only lines in it:

```
load_tree_lib():                                                         # 89 S6
    try:   read_memory_tree("tree_lib.py"); import tree_lib              # 89 S6
    except LookupError as e:                -> LoopError("memory-tree kit", "<e> — govkit update --kits memory-tree")              # S33
    except (ImportError, SyntaxError) as e: -> LoopError("memory-tree kit", "<its kind>: <e> — govkit update --kits memory-tree")  # S33
    no derive_docstring_ids in tree_lib     -> 86 S21's LoopError         # 89 S6, untouched
    return tree_lib
```

### The probe module of AC13

A scratch `loop_lib.py` the probe writes, its expected answer DERIVED from these bytes:

```
from pathlib import Path
ROOT = Path(".")
CONF = ROOT / ".unattended.conf"
SUFFIX = "x"
SUFFIX += ".memory-tree.conf"
A, B = ".memory-tree.conf", 1
if True:
    GUARDED = ROOT / ".memory-tree.conf"
D = {}
D[".unattended.conf"] = 1
OTHER = ROOT / "other.toml"
class K:
    KC = ".unattended.conf"
def f():
    local = ".unattended.conf"
def load():
    global G
    G = ROOT / ".unattended.conf"
```

`CONF`, `SUFFIX`, `A`, `B` and `GUARDED` are 87 AC2's shapes; `D` is the target-held name charge rule 2
adds; `G` is 89 S1's global loader; `OTHER`, `K.KC` and `local` answer nothing.

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `a339daae2`, through `git archive` into a scratch
copy, unless named otherwise; `tools/loop/` is absent from this worktree's main. `derive_conf_reads`,
`derive_conf_constants`, `derive_docstring_ids`, `derive_conf_rebinds`, `load_tree_lib`, the `no-own-conf-read` and
`conf-read-forms` plants, 86's unparseable-parent plant and 86's detail spellings are not built at that
tip: they are read on the committed specs §5 "Dependency" names.

- `tools/loop/guard.py#resolve_write_tree_support` is memoised by `functools.cache`.
  `run_grade_in_process` inside `tools/loop/guard.py#run_guard_plant` calls its `cache_clear` before
  the swaps and registers it after them, and every in-process grade goes through it.
  `tools/loop/guard.py#main` refuses `--fixture` without `--plant`, and the leg `loop guard fixtures`
  runs `guard.py --selftest`, which runs every plant through
  `tools/loop/loop_lib.py#run_selftest_cases`, `main` called in process.
- `tools/loop/guard.py#run_merge_tree_usage` runs `git merge-tree -h` with `text=True`,
  `encoding="utf-8"`, `errors="replace"` and `env=read_clean_env()`, no keyword set.
  `tools/loop/loop_witness.py#read_clean_env` answers `os.environ` less the memory-tree kit's
  `GIT_ENV_LEAKS`, with its keywords set.
- The fatal-history branch of `run_guard_plant` serves `push-merge-tree-fatal`, `push-merge-probe-failed`
  and `push-merge-probe-silent` from one table of swaps, needles and re-merge counts, each grade owing
  the failed line, the dropped `review.max-rounds` key and its count. The recorded scenario of
  `push-merge-unrelated-histories` writes its trailer from
  `render_policy_trailer(policy, ("review", "max-rounds"), 4, None)` and its record through
  `write_fixture_record`, and owes `0 finding(s)`.
- `tools/loop/guard.py#check_push_range` skips an `uncomputable` or `conflicted` merge whose combined
  diff omits the policy file or whose blob equals its first parent's, so the conflicted plant's merge
  writes bytes of its own; its `failed` branch takes no skip. Both branches refuse a parent whose policy
  blob `parse_policy_bytes` answers `None` as `does not parse at parent <sha8>`.
- `tools/memory-tree/gen_build_index.py#scan_glob_readers` holds the closure `scan_scope`, its inline
  docstring set and its composed needle `magic`. Its one call is `_scan_table23` in
  `tools/memory-tree/gen_build_index.py#cmd_selftest`, whose glob-reader arm owes eight charged names
  over its planted module.
- A probe of that walk over the tip's `tools/loop/loop_lib.py`, its needle the two conf names, charged
  four conf-name constants, each to a function, `read_builds_dir`, `read_driver_conf` and
  `resolve_memory_root`, by rule 1, and none by rule 2.
- `tools/loop/loop_lib.py#read_memory_tree` puts the kit `tools/loop/loop_lib.py#resolve_kit_dir` finds
  on `sys.path` and raises its `LookupError`, which names the receipt and both probes it looked in.
  `tools/loop/loop_lib.py` imports no `tree_lib`; `loop_witness.py`, `loop_transition.py` and
  `upstream.py` reach it inside functions through `read_memory_tree`.
- `tools/loop/loop_lib.py#LoopError` subclasses `ValueError` and reads `<where>: <what>`.
- 89 S6 mints `load_tree_lib()` holding 86 S21's route and its `LoopError` for a module lacking
  `derive_docstring_ids`, called by `derive_conf_reads` and `derive_conf_constants`, and catches no
  `LookupError`, `ImportError` or `SyntaxError`; its §8 F5 resolves the one loader, and its AC5 grades the
  route's single site and the `derive_docstring_ids` refusal
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md`, §2 S6, §8 F5, AC5, rev-5).
  90 rev-5's loader sketch names the `LookupError` and the `ImportError` or `SyntaxError` refusals
  "88 S33's refusal" (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md`, §4,
  rev-5).
- `C:/Program Files/Git/mingw64/share/locale` does not exist on node `d`, so git 2.54.0.windows.1 there
  prints no translated usage, read 2026-11-17: PINNED. That git prints its usage header through gettext
  is UNVERIFIED here, from the report's reading of git's parse-options.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_constant_charges` | Python function in `tools/memory-tree/tree_lib.py` | `py.function`, verb-first |
| `push-merge-probe-failed-trailered`, `push-merge-probe-failed-unparseable-parent`, `push-merge-conflicted-unparseable-parent`, `push-merge-probe-signal` | `PLANTS` names in `tools/loop/guard.py` | none |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for
`derive_constant_charges`, leading with the declared verb `derive`, run in the scratch copy of the tip on
2026-11-17. `load_tree_lib` is 89's inventory row (89 §4 Inventory), and S33 mints no name.

### Files touched (estimate)

- `tools/loop/guard.py` (S16, S17, S19, S26)
- `tools/loop/loop_lib.py` (S13's slice; S33's two catches inside 89 S6's `load_tree_lib`)
- `tools/loop/budget.py` (S33's three rows)
- `tools/loop/README.md` (S13; S33's refusals on 89 S4's `load_tree_lib` row)
- `tools/loop/kit.toml` (S13)
- `tools/memory-tree/tree_lib.py` (S13)
- `tools/memory-tree/gen_build_index.py` (S13)
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

### Alternatives rejected

- **One unit per minor.** The batch rule forbids it.
- **Rev bumps of the CLOSED siblings at this pass.** The spec-exit rule keeps a CLOSED spec frozen (§8 F5).
- **A memo keyed to the probe object (S6).** 85's clearing already isolates every grade (§8 F2).
- **An empty label per caller (S24).** One label reads true for both callers (§8 F6).
- **A catch at each call site of the loader (S33).** It writes the same two catches twice (§8 F7).
- **A loader of this unit's own (S33).** 89 S6 mints `load_tree_lib` first at order 44; a second
  definition is two specs minting one name, the divergence the second builder meets (§8 F7).
- **Keeping 87's walk beside the lifted one (S13).** Two walks deciding one question is id 17's defect
  (§8 F4).
- **Two batch units, the guard items and the rest.** The kept items are disjoint by file, but S17, S19
  and S26 alone would be a unit of three plants, and a split now moves an order every later batch cites.

## 5. Production-readiness checklist

- security — S16 keeps a capable git on a translated locale from reading as a failed probe; S17, S19 and
  S26 keep a failed probe, a conflicted re-merge and a killed probe refusing as the code does today.
- perf / scale — S13 replaces one walk with one walk; S33's rows run in process, milliseconds; S17, S19
  and S26 add four scratch histories to `loop guard fixtures`, seconds each.
- error / empty / loading states — S33 names an unlocatable, unloadable or unparseable `tree_lib`
  instead of a traceback.
- observability — each refusal names its case and `govkit update --kits memory-tree`.
- risks — S13 edits a governance kit's engine, observed by the glob-reader arm's eight owners and the
  `conf-read-forms` rows. The slice answers more names than 87 S1 on a binding whose target or
  annotation holds a conf name, the fail-closed side. Between this unit and 90, a memory-tree kit older
  than this unit lacks `derive_constant_charges`, and `derive_conf_constants` ends in `AttributeError`;
  90 S4 and S5 refuse it by name at order 45, and govkit ships both kits from one tree.
- testing — AC13, AC16, AC17, AC19, AC26 and AC33 as plants, probes and greps; the arms under §7,
  observed at the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed.
- user docs — none under `help/`: `help/policy.md`'s probe sentence, which 86 S2 writes, stays true.
  The kit carriers are `tools/loop/README.md` and `tools/loop/kit.toml` (§4 Write set).

### The sweep

Read at the tip `a339daae2` in the scratch copy; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `run_merge_tree_usage`'s environment (S16) | its one caller `resolve_write_tree_support`; the plants `push-merge-probe-failed`, `push-merge-probe-silent` and `push-merge-old-git-usage` and this unit's four, which swap the probe whole; `push-merge-no-write-tree`, which swaps the resolver; the real probe under node `d`'s git | a swapped probe never reaches `subprocess.run`; the real probe still answers `supported` |
| `PLANTS` of `guard.py` gains four (S17, S19, S26) | `run_selftest`'s owed map; the `--plant` choices; the leg `loop guard fixtures`; its row in `tools/run-gates/selftest-budgets.txt`, 90 seconds PINNED, and its manifest ceiling, 300 seconds PINNED | three owed entries of 1 and the trailered plant at the default 0; `tools/govkit/usage.toml` holds no row for `guard.py`, 0 rows PINNED; the pass times the four plants by direct CLI and re-prices the row by that file's rule where the sum crosses it, raising no ceiling |
| `scan_glob_readers` reduced to a call of `derive_constant_charges` (S13) | `_scan_table23` in `cmd_selftest`, under `build-index selftest`, its arm owing eight charged names PINNED; 82 AC8's grep of `body[0]` over `scan_glob_readers`; every importer of `tree_lib`; the `DELEGATES` of `tools/memory-tree/check-verdict-epoch.sh`, which name both files | no owner moves; the lifted walk keeps 82 S8's call; a new name and no moved one; `KIT_MEMORY_TREE_VERSION` is minted at the lander, the gate printing `owed at the lander` off the push boundary |
| `derive_conf_constants` answering the slice (S13) | its caller `derive_conf_reads`; the `conf-read-forms` rows of 86, 87 and 89; the `no-own-conf-read` case of `budget.py` and `breakpoints.py` over the two live modules | every planted row's conf name sits in its binding's value, which rule 2 charges as 87 S1 does; the kit's own `loop_lib.py` binds no conf name at module level at the tip (§4 Evidence) |
| 89 S6's `load_tree_lib` gains two catches (S33) | its two callers `derive_conf_reads` and `derive_conf_constants`; the `no-own-conf-read` case of both modules, which catches `LoopError` (86 S21); 89 AC5's probes of the route's one site and the `derive_docstring_ids` refusal; 89 S4's `load_tree_lib` row in `tools/loop/README.md`; `python -c "import loop_lib"` in every loop leg | each new refusal is a `LoopError`; the route, the `derive_docstring_ids` refusal and both calls stay 89's bytes, so 89 AC5 keeps its answer; the loader still runs inside the call, so the import adds no module-level reach; no name is minted, so the symbol row is 89's and unmoved |
| `derive_constant_charges` minted (S13) | `memory/map/generated/symbols.json` and its three siblings, under `codebase-map coverage + freshness`; the lexicon offender pin | `python tools/codebase-map/gen_map.py --write`; it leads with a declared verb |
| the module docstring of `guard.py`, `tools/loop/README.md` and the reach comment of `tools/loop/kit.toml` | `install-prefix (shipped surface)` and `kit epoch (shipped bytes move, the version moves)`; no other gate reads them | each line names a function, a conf or a govkit command, never a kit path; `KIT_LOOP_VERSION` is owed at the lander |
| this spec's citations | `memory/project/positional-refs.txt`, 7 rows PINNED for this spec, under `positional (the citation check alone)` | rev-6 cites the build method by its alias tag and code by symbol only, so the commit landing it runs `python tools/playbook/positional.py shrink` |
| this spec's numbers | 89, 90, 92, 94 and 96 cite S1, S2, S6, S9, S12, S13, S16, S18, S24, S31, S33, S35 and AC1, AC7, AC9, AC13, AC18, AC22 and AC24 by number, DERIVED by the grep below | every number is kept, a settled one in §3's table; each sibling's re-ground owns its own text |

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -e run_merge_tree_usage -e build_failure_detail -e resolve_write_tree_support "$B" -- tools   # guard.py alone
git grep -n -w -e scan_glob_readers -e scan_scope "$B" -- tools                  # gen_build_index.py alone
git grep -n -w -e derive_conf_reads -e derive_conf_constants -e derive_docstring_ids -e derive_conf_rebinds -e load_tree_lib "$B" -- tools   # none: 76 to 89 unbuilt
git grep -n '"tree_lib.py"' "$B" -- tools/loop                                 # loop_witness, loop_transition, upstream
git show "$B:tools/govkit/usage.toml" | grep -c 'loop/guard.py'                 # 0
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop guard fixtures'
git show "$B:tools/gate-legs.json" | grep -A8 '"loop guard fixtures"' | grep ceiling
git show "$B:tools/memory-tree/check-verdict-epoch.sh" | grep '^DELEGATES='       # names tree_lib.py and gen_build_index.py
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-88.md'   # 7
git grep -o -h -e '88 S[0-9]*' -e '88 AC[0-9]*' "$B" -- memory/builds/dDeclaredLoop/spec | sort | uniq -c
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED; the one minted
  function leads with a declared verb.
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead.
- The refusal ceilings and families: no `*.sh` is edited, and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` and `tools/memory-tree/check-arms.py#branches`
  read tracked `*.sh` files alone. The driver's ceiling stays 343 PINNED and
  `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb or flag is added, so no usage row and no anchor.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added; the two
  memory-tree files are `DELEGATES` already, which moves only the version the lander mints; no
  `[[upgrade]]` row is owed; and no file the `watch:` line of `memory/guides/SESSION-KICKOFF.md` names is
  edited.

### Dependency

Built and CLOSED: `TOOL-dDeclaredLoop-81` and `TOOL-dDeclaredLoop-85` (orders 20 and 21), whose
`guard.py` code S16, S17, S19 and S26 extend. Unbuilt, read on their committed specs:
`TOOL-dDeclaredLoop-76` rev-6 (order 37) for `derive_conf_reads` and the `no-own-conf-read` case;
`TOOL-dDeclaredLoop-80` rev-6 (order 38) for the fixture boundary; `TOOL-dDeclaredLoop-75` rev-10 (order
39) for the exit-1 reading; `TOOL-dDeclaredLoop-82` rev-7 (order 41) for `derive_docstring_ids` and the
`conf-read-forms` plant; `TOOL-dDeclaredLoop-86` rev-8 (order 42) for the narrowed probe, the
unparseable-parent history, the in-function route and the detail spellings; `TOOL-dDeclaredLoop-87`
rev-5 (order 43) for the conf-constant class and its rows; and `TOOL-dDeclaredLoop-89` rev-5, which
builds first at order 44, for `derive_conf_rebinds`, `load_tree_lib` and its rows. Each builds before this unit; where a
landed shape differs from its committed spec, the pass reads the landed one and records the difference
as a deviation. `TOOL-dDeclaredLoop-68` is building now, `TOOL-dDeclaredLoop-34` is deferred against ask
TOOL-dDeclaredLoop-113, and `TOOL-dDeclaredLoop-33`'s numeric direction against ask
TOOL-dDeclaredLoop-114; none moves a read this unit makes. The reuse probes and the lexicon's suggest
verb ran in the scratch copy of the tip; 89 rev-5 and 90 rev-5 were read through `git show` at
`240095e82`; the spec-token checker ran in this worktree; the locale reading ran on node `d`.

## 6. Acceptance criteria

Each `python guard.py` and `python budget.py` command below runs in `tools/loop/`.

- **AC13** — When `grep -c "def scan_scope"` runs over `tools/memory-tree/gen_build_index.py`, it prints
  0, and `grep -c "^def derive_constant_charges"` over `tools/memory-tree/tree_lib.py` prints 1. A
  `python -c` probe in `tools/memory-tree/` calls `tree_lib.derive_constant_charges` with module `m` and
  the needle `lambda s: "NEEDLE" in s` over a parsed module holding `"NEEDLE"` in a function `f`, a
  module-level binding `X`, a class-level `L.append` in class `K`, a module-level `M.append` and the
  module docstring; it answers `[('m', 4), ('m.K', 3), ('m.X', 2), ('m.f', 1)]`.
  A second probe there, calling `gen_build_index.scan_glob_readers` on a scratch folder holding `m.py`
  with a `:(glob)` constant in the same five places, answers `['m', 'm.K', 'm.X', 'm.f']`. A `python -c`
  probe in `tools/loop/` calling
  `loop_lib.derive_conf_constants` on §4's probe module answers
  `['A', 'B', 'CONF', 'D', 'G', 'GUARDED', 'SUFFIX']`, sorted, and
  `python budget.py --fixture --plant conf-read-forms` prints `held`.
  Red when: the lift moves an owner or a rule number, or a second walk stays beside the lifted one.
  figure: each expected answer is DERIVED from the bytes its probe writes.
- **AC16** — When a `python -c` probe imports `guard`, swaps `guard.subprocess.run` for a recorder of one
  call answering exit 129 with empty streams, and calls `run_merge_tree_usage()`, the `env` it recorded
  maps `LC_ALL` to `C` and `LANGUAGE` to the empty string, and `os.environ` is equal before and after.
  With `LC_ALL=de_DE.UTF-8` exported,
  `python -c "import guard; print(guard.resolve_write_tree_support()[0])"` prints `supported`.
  Red when: the probe inherits the caller's locale, so a translated usage header reads `probe failed`.
  fixture: node `d`'s git ships no catalogs (§4 Evidence), so the second half cannot show a
  translation; the first half is the discriminating one.
- **AC17** — When `python guard.py --fixture --plant push-merge-probe-failed-trailered` runs, it exits 0
  printing `probe failed: start failed: fx stand-in`, `0 finding(s)`, `merge-tree runs: 0` and the
  plant's `all held` line.
  Red when: a failed probe refuses whatever the trailer names, staged by having `check_push_range` add
  a finding of its own for a `probe failed` detail.
- **AC19** — When `python guard.py --fixture --plant push-merge-conflicted-unparseable-parent` and
  `python guard.py --fixture --plant push-merge-probe-failed-unparseable-parent` run, each exits 1
  printing `does not parse at parent ` and its `all held` line and no `Traceback`, the first printing
  `merge-tree runs: 1` and the second `merge-tree runs: 0`.
  Red when: the conflicted or the probe-failed grade reads the unparseable parent as the empty table,
  skips the merge or raises, staged by parsing the parents past the first without the `None` test.
- **AC26** — When `python guard.py --fixture --plant push-merge-probe-signal` runs, it exits 1 printing
  `probe failed: signal 9`, `merge-tree runs: 0` and its `all held` line, and no `Traceback`.
  Red when: the resolver spells the probe's exit itself, so a killed probe prints `-9`.
- **AC33** — When `python budget.py --fixture --plant conf-read-forms` runs, its three `tree_lib` rows
  each answer a `LoopError` naming `govkit update --kits memory-tree`, the unlocatable row's naming
  `looked in` too, and the plant prints `held` with no `Traceback`. A `python -c` probe with
  `loop_lib.read_memory_tree` swapped to raise `LookupError("looked in a, b and c")` finds
  `loop_lib.load_tree_lib()`, `derive_conf_constants` on a scratch `loop_lib.py`, and `derive_conf_reads`
  on a scratch module beside it each raising `LoopError`. A `python -c` probe parsing `loop_lib.py` with
  `ast` finds the `LookupError`, `ImportError` and `SyntaxError` handlers inside `load_tree_lib` alone,
  and `grep -c "^def load_tree_lib"` over `loop_lib.py` prints 1.
  Red when: `LookupError`, `ImportError` or `SyntaxError` ends the rule in a traceback, or a catch sits at
  a call site, or a second `load_tree_lib` is defined beside 89's.
  figure: the 1 is DERIVED from the built file, 89 S6's one definition.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory-recall kit selftest` · `drift-audit selftest` · `playbook render selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `every held leg is budgeted, every budget row resolves` · `lexicon naming predicates` · `positional (the citation check alone)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop legs this pass keeps green sit outside the base manifest the leg line is joined against, each
declared by the unit that built or mints it: `loop guard fixtures` (`TOOL-dDeclaredLoop-2`),
`loop budget fixtures` (`TOOL-dDeclaredLoop-30`), `loop breakpoint fixtures` (`TOOL-dDeclaredLoop-19`),
whose `no-own-conf-read` plant runs the conf-read rule, the leg `loop definition`, which runs
`loop_lib.py --check`, and the leg `loop definition fixtures` (`TOOL-dDeclaredLoop-67`). None carries
a `guard`, so every bar runs each.

New arm: tools/loop/guard.py · covers AC17 AC19 AC26 · the trailered probe-failed plant, the conflicted and probe-failed unparseable-parent plants and the probe-signal plant, each staged as its criterion's Red when · none
New arm: tools/loop/budget.py · covers AC13 AC33 · the three tree_lib refusal rows, staged with the route's LookupError and import errors left to propagate, and the conf-read-forms rows read through the slice, staged with derive_constant_charges answering rule 4 for a module-level binding · none
New arm: tools/memory-tree/gen_build_index.py · covers AC13 · the glob-reader arm's eight owners read through the lifted walk, staged with derive_constant_charges charging a module-level binding to the module · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records; first resolved 2026-10-24.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (the Derived line PLAY-dClosedLoop-2)
- **F2 — How does a plant isolate the probe memo (ids 4, 31)?** (a) The plant hook clears the memo
  before and after each grade; (b) the memo is keyed to the probe object it called; (c) every probe
  plant replaces `resolve_write_tree_support` itself. Rev-5 took (b), weighing (a)'s reset a builder
  could reach from the production path. 85 then landed (a): `run_grade_in_process` clears the
  `functools.cache` memo around every in-process grade, and the leg `loop guard fixtures` runs every
  plant in one process. (b) now rewrites a CLOSED unit's working code for no failing case, and the
  reset (a) uses is the cache's own. Recommendation: (a), S6 and S7 settled in §3.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F3 — Which spelling does the one detail builder keep for an exit code (id 18)?** (a) The re-merge's
  `<rc> <line>`; (b) the probe's `rc <rc> <line>`. (a) is the spelling 85 landed and 86 rev-8 S22
  keeps, and the plants' needles read it; (b) moves every needle that names an exit code. First resolved
  2026-10-24. Recommendation: (a).
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F4 — Lift the charge walk, or record in §10 why not (id 17)?** (a) Lift the walk into `tree_lib`
  and slice it; (b) keep 87's own walk and name charge rule 2 as the rejected seam. (b) leaves two walks
  deciding one question, the defect, and 82 S8 already lifts the docstring half of that walk into
  `tree_lib`. 82 §4's rejection of this extraction weighed `derive_conf_reads`, which has no use for the
  scope tracking; `derive_conf_constants` needs exactly rule 2's module scope. First resolved
  2026-10-24. Recommendation: (a), S13.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F5 — What becomes of the items that amend a sibling spec CLOSED before order 44?** Rev-5 had this
  pass rev-bump the specs of 75, 78 to 86 and observe 79. 78, 81, 83, 84 and 85 are CLOSED now, and 75,
  79, 80, 82 and 86 build at orders 39 to 42, so every one is CLOSED when this unit builds. (a) Rev-bump
  them at this pass anyway; (b) each spec-text item leaves this unit's scope, settled where the built
  code or a committed spec already holds it, as 82 rev-7 and 86 rev-8 did for their own; (c) keep each
  as an observation this pass records. (a) writes frozen records, which the spec-exit rule forbids; (c)
  observes specs no builder reads after their close. Recommendation: (b), with the code items S13, S16,
  S17, S19, S26 and S33 kept.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (b)
- **F6 — Does each caller of `build_failure_detail` name its own empty stream (id 18)?** (a) Keep 86
  rev-8 S22's one label, `(no stderr)`, for the probe and the re-merge alike; (b) add an `empty_label`
  parameter so the probe reads `(no output)`. The probe joins its two streams, so `(no stderr)` prints
  only where both are empty, where it is true; (b) adds a parameter every caller must pass for one word.
  Recommendation: (a), S24 settled in §3.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F7 — Where do S33's catches live, with 89 S6 minting `load_tree_lib` before this unit as the one
  route both `derive_conf_reads` and `derive_conf_constants` call (id 36)?** (a) A catch at each of the
  two call sites; (b) inside 89 S6's `load_tree_lib`, extended in place with the `LookupError` and the
  `ImportError` or `SyntaxError` arms, its route, its `derive_docstring_ids` refusal and both calls left
  as 89 writes them; (c) a loader of this unit's own. (a) writes the same two catches twice, the copy the
  reuse rule forbids at a second instance. (c) has two specs minting one name, the divergence the second
  builder meets. (b) is the loader 90 rev-5 S4 names as 86 S21's route extended in place, whose sketch
  already credits these two refusals to 88 S33, and 92 rev-4 S2 writes where absent, so no later spec
  meets a conflict. Recommendation: (b), S33.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-17, delegated): (b)

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-7 spec audit's 36 minors batched (19 MEDIUM, 17 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-89 and TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-92, written by the round-9 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.
- rev-6 · 2026-11-17 · §1 to §10 · S1 to S36 · AC1 to AC36 · §8 F1 to F7 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `a339daae2` and on the committed specs of TOOL-dDeclaredLoop-75
  rev-10, 76 rev-6, 80 rev-6, 82 rev-7, 86 rev-8, 87 rev-5 and 89 rev-5, per the briefs
  2026-11-17-prompt-TOOL-dDeclaredLoop-88-1-spec-writer and
  2026-11-17-prompt-TOOL-dDeclaredLoop-88-3-spec-writer; mechanism, carries, order and status kept. No
  sibling spec is amended, each being CLOSED by order 44 (F5): thirty items and their criteria move to
  §3 with what settles each, numbers kept. S6 and S7 are settled by 85's landed memo clearing (F2), S24
  by 86 S22's builder (F6), S26's tree-fatal row by 86 S22. S13 writes the union with 89's
  `derive_conf_rebinds` and states the slice's wider set; S33 adds to 89 S6's `load_tree_lib` only the
  `LookupError` and `ImportError` or `SyntaxError` catches 89 does not hold, its `derive_docstring_ids`
  refusal left to 89, so only 89 mints the name (F7); S17 and S19 are written on the fatal-history branch
  and 86 S6's history. The build method is cited by its alias tag; line citations made symbol citations;
  the sweep and the budgets.

## 10. Reuse audit

Each kept item extends the seam its finding names, never a parallel copy: the charge walk of
`tools/memory-tree/gen_build_index.py#scan_glob_readers`, lifted into `tools/memory-tree/tree_lib.py`
beside 82 S8's docstring set (S13); `tools/loop/loop_witness.py#read_clean_env`'s keywords for the
probe's locale (S16); the fatal-history branch and `run_grade_in_process` of
`tools/loop/guard.py#run_guard_plant`, with `run_selftest`'s owed map, for the four plants (S17, S19,
S26); and 89 S6's `load_tree_lib`, which holds 86 S21's route through
`tools/loop/loop_lib.py#read_memory_tree` and gains S33's two catches in place, never a second loader
(S33).
`python tools/codebase-map/reuse_lookup.py "charge each string constant holding a needle to its enclosing function, binding, class or module"`,
run in the scratch copy of the tip on 2026-11-17, ranked `read_bindings`, `read_policy_modules`,
`module_inventory`, `parse_binding_lines` and `check_declared_class`, none a charge walk, and did not
rank `scan_glob_readers`, the seam S13 extends, a hit missed by omission.
`python tools/codebase-map/reuse_lookup.py "run git with a pinned C locale environment so its output is untranslated"`
ranked `run`, `git`, `run_git`, `run_selftest_cases`, `read_git` and `run_fixture_git`, none a locale
pin; `tools/memory-tree/tree_lib.py#build_git_env` pins grafts alone, so S16 sets the two names through
`read_clean_env`. The memory-recall query returned 87's spec, this spec's own lifted-walk sketch and the
round-7 report's id 17 fix, which the skeptic judged sound.

Recall terms used: charge rule scan_glob_readers derive_conf_constants tree_lib lifted walk module-level binding rule 2 docstring
