# TOOL-dDeclaredLoop-86 — the round-6 spec audit's 22 minors, batched

**Status:** CLOSED · rev-8 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 42 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-861.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-861.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-862.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-862.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-86-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-86-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-86-deviation-863.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-86-deviation-863.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-86-red-fix-60.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-86-red-fix-60.md) | red-fix | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-86-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-86-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-86-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-86-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-86-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-86-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
exited CONVERGED with 25 confirmed findings over units 80 to 82, the round-5 promotions. Its three highs
are units 83, 84 and 85, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every
MEDIUM and every LOW, each by its report id and each its own scope item, where the report merged ids into
one item too. The minors land on several units, so this unit repairs none in particular and builds after
every unit whose spec or code they name, at order 42. Where a minor is the medium grade of a defect a high
unit closes, the item here is what that grade's fix asks beyond the high unit's mechanism.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 18 | S1 |
| M2 | MEDIUM | 9 | S2 |
| M3 | MEDIUM | 4 | S3 |
| M4 | MEDIUM | 11, 17 | S4, S5 |
| M5 | MEDIUM | 3 | S6 |
| M6 | MEDIUM | 15 | S7 |
| M7 | MEDIUM | 14 | S8 |
| M8 | MEDIUM | 23 | S9 |
| M9 | MEDIUM | 25 | S10 |
| M10 | MEDIUM | 26 | S11 |
| M11 | MEDIUM | 27 | S12 |
| M12 | MEDIUM | 28 | S13 |
| L1 | LOW | 10 | S14 |
| L2 | LOW | 5 | S15 |
| L3 | LOW | 6 | S16 |
| L4 | LOW | 12 | S17 |
| L5 | LOW | 13 | S18 |
| L6 | LOW | 16 | S19 |
| L7 | LOW | 19 | S20 |
| L8 | LOW | 21 | S21 |
| L9 | LOW | 29 | S22 |

That is 13 MEDIUM and 9 LOW findings by raw id. M1 and M2 are the medium grades of H1 and H2, whose
mechanisms are units 83, 84 and 85. M3 and L1 are one defect at two grades, fixed once across S3 and S14.
The report's four refuted findings, ids 2, 8, 20 and 22, are not in the disposal population.

Re-grounded at rev-8, eight items still build: S2, S6, S9, S10, S13, S15, S21 and S22, each a change to
the loop kit's code or its plants. The other fourteen asked a rev bump of a sibling spec that is CLOSED
by order 42, or are already true at the tip; §3 "The rev-7 items the built code, a committed spec or a
frozen record settles" says what settles each, keeping its number (§8 F5).

## 2. Scope (IN)

- **S2** — id 9. `check_write_tree_usage(rc, text)` in `tools/loop/guard.py` answers `supported` only
  where `rc` is 0 or 129, a line of `text` opens `usage: git merge-tree`, and the text names
  `--write-tree`. It answers `unsupported` where `rc` is 0 or 129, such a line is present, and the text
  does not name `--write-tree`. Every other outcome is `probe failed`, a text naming `--write-tree`
  with no usage line or under another exit code included. The push arm paragraph of the module
  docstring and the merge sentence of the push check in `help/policy.md` say that a probe exiting other
  than 0 or 129, or printing no `usage: git merge-tree` line, is a failed probe. Observed by AC2.
  **Readers:**
  by name: tools/loop/guard.py, the write-tree resolver, the predicate's one caller
  by value: .githooks/pre-push, the policy push arm block, which turns the arm's exit into the `policy-unrecorded` refusal
- **S6** — id 3. The plant `push-merge-tree-fatal-unparseable-parent` joins `PLANTS` in
  `tools/loop/guard.py`, a branch of `run_guard_plant` beside `push-merge-tree-fatal`, owed exit 1 by an
  entry of `run_selftest`'s owed map. It builds that plant's history, a run branch merging main and
  keeping its own policy file, except that main's commit appends `FX_REVIEW` twice, so `[review]` is
  declared twice and main's policy blob does not parse. It grades in process with `run_merge_tree`
  answering `(128, "", "fatal: fx stand-in\n")`, so the merge is `failed`. Its rows owe the failed line,
  the refusal `does not parse at parent <sha8>` naming main's tip, and exit 1. The `failed` branch of
  `check_push_range` already refuses that way; the plant is the arm that keeps it. Observed by AC6.
- **S9** — id 23. Every `git fetch` the `url-forms` plant of `tools/loop/position.py` runs, the port-9
  fetch of `TOOL-dDeclaredLoop-77` and the loopback HTTP fetch of `TOOL-dDeclaredLoop-82` S23 alike,
  goes through `read_git` with the arguments `-c credential.helper=` before `fetch`, so no configured
  credential helper runs, and with `env=read_clean_env(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")`,
  the two names set in that call's environment alone. Observed by AC9.
- **S10** — id 25. The `conf-read-forms` rows S13 adds and the `loop_lib.py` stubs S15 writes are built
  inside a function `derive_fixture_boundary` answers, never in a module-level table, as
  `TOOL-dDeclaredLoop-80` rev-6 S4 already states for this unit's rows. Observed by AC10.
- **S13** — id 28. `derive_conf_constants(loop_lib_path)` in `tools/loop/loop_lib.py` answers the set of
  module-level names that file binds by an `Assign` or `AnnAssign` whose value is a str `Constant`, a
  `JoinedStr`, a `BinOp` over such values, or a `Path(...)` or `PurePath(...)` call over one, and whose
  source text contains `.memory-tree.conf` or `.unattended.conf`. It reads the file with `ast.parse`,
  never an import, and raises `LoopError` naming the path where the file is missing or does not parse.
  `derive_conf_reads(path)` takes the conf-constant set of 82 S1 from `derive_conf_constants` over the
  `loop_lib.py` in the folder holding `path`, and counts `from loop_lib import *` as binding every member
  of that set as a local name, so a later read of one is kind `conf constant`. The `conf-read-forms`
  plant of `tools/loop/budget.py` gains four rows (§4 "The added rows"). Observed by AC13.
  **Readers:**
  by name: READER NOT IN TREE — the conf-read rule and every plant case that calls it land at orders 37 to 41 and are absent at the branch tip
  by value: the `no-own-conf-read` case of `budget.py` and of `breakpoints.py` and the `conf-read-forms` plant, whose held line and exit read the answer; a missing or unparseable sibling `loop_lib.py` is a refusal after this unit
- **S15** — id 5. Every call of `derive_conf_reads` on a scratch module has a `loop_lib.py` beside it.
  The scratch module of 82 AC1 and its scratch `loop_lib.py` are siblings in one scratch folder, and the
  module 80 S3's case writes into its scratch folder gains a one-line `loop_lib.py` sibling that binds no
  conf name, so the two `conf name` hits 80 AC2 owes there still hold. Where 82's build reaches its
  scratch `loop_lib.py` through an argument or a fixed path, that route gives way to the sibling rule,
  every call edited in the same commit, and `derive_conf_reads` keeps the one parameter `path`
  (§8 F3). Observed by AC15.
  **Readers:**
  by name: READER NOT IN TREE — the conf-read rule and its plant cases land at orders 37 to 41 and are absent at the branch tip
  by value: NO VALUE READERS — the answer over each module is unchanged; only where the constants are read from moves
- **S21** — id 21. `derive_conf_reads` reaches the memory-tree kit's `tree_lib` inside the function
  alone, through `read_memory_tree("tree_lib.py")` and then `import tree_lib`, as
  `tools/loop/loop_witness.py#read_clean_env` reaches it, and never at the import of `loop_lib`. Where
  the loaded module lacks `derive_docstring_ids` (82 S8), it raises `LoopError` naming the loaded file
  and `govkit update --kits memory-tree`. The `no-own-conf-read` case of each module catches it as a
  miss, printing it on its `MISSED` line, and exits non-zero with no `Traceback`. Observed by AC21.
  **Readers:**
  by name: READER NOT IN TREE — the conf-read rule lands at order 37 and is absent at the branch tip
  by value: NO VALUE READERS — the docstring ids are the same set, read from the same module
- **S22** — id 29. `build_failure_detail(outcome, text)` in `tools/loop/guard.py`, the one spelling of
  every detail under `the clean re-merge failed:`, spells an exit code in two more ways: a negative code
  reads `signal <n>`, n its absolute value, the signal's number; and a code whose `text` holds no
  non-blank line is followed by `(no stderr)` in place of git's first line. An `OSError` keeps its
  built spelling, `start failed: <its text>` (§8 F6). The `push-merge-tree-fatal` plant grades its
  history three more times in process, `run_merge_tree` raising `OSError("fx stand-in")`, answering
  `(-9, "", "")` and answering `(128, "", "")`, each row owing exit 1 and its spelling. The push arm
  paragraph of the module docstring names the three spellings. Observed by AC22.
  **Readers:**
  by name: tools/loop/guard.py, the write-tree resolver and the re-merge reader, the builder's two callers
  by value: NO VALUE READERS — the detail is printed on the failed line, and only this module's own plant rows match it, by substring

## 3. Non-goals (OUT)

- The three highs' mechanisms: units 83, 84 and 85, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 2, 8, 20 and 22.
- Deleting the credential-store entries the round-6 skeptic's own probe left on node `d`: a write to the
  owner's environment outside the repository, which this unit does not price.
- Pinning the probe's locale: `TOOL-dDeclaredLoop-88` S16 (§5 risks).
- A rev bump of any sibling spec: each spec this unit's rev-7 amended is CLOSED by order 42 (§8 F5).

### The rev-7 items the built code, a committed spec or a frozen record settles

Read on branch `unattended-declared-loop-d56bf0` at `77130f241`.

| Item | What settles it |
|---|---|
| S1 | `TOOL-dDeclaredLoop-81` is CLOSED at order 20 and frozen. `grep -c "any other exit code grades against the parents alone"` over its spec prints 0, and `tools/loop/guard.py#read_remerge_policy` maps exit 1 alone to `conflicted` and every other outcome to `failed`. |
| S3 | 80 rev-6 §4 Files touched records 67's write of both modules at order 38, dispatched in sequence with 67 first (its §8 F3). |
| S4 | 76 rev-6 AC1 owes the exit 0 at 80's pass commit and records the plant's exit and hits at its own pass, as its bullet to this unit says. |
| S5 | 79 builds at order 40 and is frozen at this pass. The exit 0 at 80's pass commit is 80's own AC1. 79 rev-6 AC10 still reads every exit at 76's pass commit as 0 or `no leg`, which is that spec's to restate before its dispatch (§8 F5). |
| S6's spec halves | 81 and 78 are CLOSED at orders 20 and 19 and frozen; `grep -c "the .uncomputable. branch reads"` over the 78 spec prints 0. The `failed` and parents-only branches of `check_push_range` already refuse an unparseable parent `at parent <sha8>`. |
| S7 | `TOOL-dDeclaredLoop-59` is CLOSED at order 17 and frozen. `tools/loop/guard.py#resolve_write_tree_support` reads the feature from the usage probe alone, and a re-merge exit 129 is `failed`. |
| S8, S11, S19 | Restatements of 82 S6's pass-commit probe. 82 builds at order 41 and is frozen at this pass, and this unit runs no pass-commit probe of its own, so no line of its ledger carries a key. The fold is 82's before its dispatch (§8 F5). |
| S9's spec half | 82 §5 is frozen at this pass; this unit's §5 names the credential store. |
| S10's spec half | 80 rev-6 S4 names every later plant of either module, this unit's rows among them. |
| S12, S20 | No leg named `loop selftest` exists or is added (79 rev-6 §3, its S11 and S27); the breakpoints leg is `loop breakpoint fixtures`; and no loop row of `tools/gate-legs.json` carries a `guard`, so 82 AC5's join names no spec (79 rev-6 §3, its S18). |
| S13's and S15's spec halves | 82 S1 and AC1 are frozen at this pass; S13 and S15 build the rule and the layout in the code. |
| S14 | The build README's build-order region prints step 38's Parallel cell `no` at the tip. |
| S16 | 80 rev-6 AC4 is one `grep -c` per plant over `budget.py`. |
| S17 | 76 is frozen at this pass, and 82 S10 builds the rule that counts a conf name anywhere in a string constant, so no code waits on 76's text. |
| S18 | 82 §4 is frozen at this pass, and its pins are line citations, which a spec now writes by symbol; the fold is 82's before its dispatch (§8 F5). |
| S21's and S22's spec halves | 82 S8 and 81 S2 and S3 are frozen at this pass; S21 and S22 build in the code. |

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-59` — S3's missing-feature sentence (id 15), settled by the built probe; 59 is CLOSED
- **consumes-from** `TOOL-dDeclaredLoop-66` — `render_order`, whose step-38 Parallel cell already reads `no` (id 10)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `derive_conf_reads` and the `no-own-conf-read` case of both modules, which S13, S15 and S21 extend (ids 11, 12)
- **consumes-from** `TOOL-dDeclaredLoop-78` — S3's parent-side parse refusal, which S6's plant observes under `failed` (id 3)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S10's probe and AC10, settled outside this unit (id 17)
- **consumes-from** `TOOL-dDeclaredLoop-80` — `derive_fixture_boundary`, inside which S10 builds, and S3's staged module, which S15 gives a sibling `loop_lib.py` (ids 4, 6, 25)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the `failed` state and the `push-merge-tree-fatal` plant, which S6 and S22 extend (ids 3, 18, 29)
- **consumes-from** `TOOL-dDeclaredLoop-82` — `derive_conf_reads`'s conf-constant kind, `derive_docstring_ids`, and the `conf-read-forms` and `url-forms` plants, which S9, S13, S15 and S21 extend (ids 5, 10, 13, 14, 16, 19, 21, 23, 25, 26, 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-85` — `check_write_tree_usage` and `build_failure_detail`, which S2 narrows and S22 extends (id 9)
- **hands-off** `TOOL-dDeclaredLoop-87` — `derive_conf_constants`, S13, its §4 sketch and AC13, which that unit restates from a shape list to the class, with the joined-path and aliased rows (the round-7 spec audit's id 29)
- **hands-off** `TOOL-dDeclaredLoop-88` — S2, S8, S21, S22, the conf-constant sketch, Files touched, §10, AC9, AC10, AC12, AC16 and AC18, and the `failed` plants, which that unit restates, re-spells, gives commands and observes (the round-7 spec audit's ids 5, 7, 8, 9, 11, 13, 14, 16, 17, 22, 24, 28, 30, 34, 35, 36, 37)
- **hands-off** `TOOL-dDeclaredLoop-89` — S13, S15, S21 and the conf-constant sketch, which that unit extends with `derive_conf_rebinds` and whose `tree_lib` route its pass takes (the round-8 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-90` — S2, S13, S21, §10, AC13 and the conf-constant sketch, which that unit restates and observes (the round-8 spec audit's ids 2, 4, 5, 10, 18, 20, 22)
- **hands-off** `TOOL-dDeclaredLoop-92` — §10, which that unit completes with `derive_conf_rebinds` (the round-9 spec audit's id 16)
- **hands-off** `TOOL-dDeclaredLoop-94` — S22's `OSError` spelling, which that unit restates to 88 S24's builder (the round-10 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-96` — S21, which that unit restates over the caller's `need` (the round-11 spec audit's id 9)
- **hands-off** `TOOL-dDeclaredLoop-98` — S15's layout of a scratch module beside a scratch `loop_lib.py`, in which that unit's `declared readers seen` row writes (the round-12 spec audit's id 11)

## 4. Design

### Write set

This pass writes `tools/loop/guard.py` (S2, S6, S22), `tools/loop/position.py` (S9),
`tools/loop/budget.py` (S10, S13, S15, S21), `tools/loop/breakpoints.py` (S21, where its
`no-own-conf-read` case does not already catch a `LoopError`) and `tools/loop/loop_lib.py` (S13, S15,
S21). It writes the carriers `help/policy.md` (S2) and `tools/loop/README.md` (S13), and the generated
map files `python tools/codebase-map/gen_map.py --write` renders. It writes no spec but this one.

### The conf-constant kind, after this unit (S13, S15, S21)

```
derive_conf_reads(path):                                   # one parameter, as 76 S2 states it
    tree    = ast.parse(read(path), path)
    read_memory_tree("tree_lib.py"); import tree_lib       # inside the call, never at module import
    if not hasattr(tree_lib, "derive_docstring_ids"):
        raise LoopError(<tree_lib file>, "has no derive_docstring_ids — govkit update --kits memory-tree")
    docs    = tree_lib.derive_docstring_ids(tree)          # 82 S8
    consts  = derive_conf_constants(<folder of path> / "loop_lib.py")
    star    = the module holds `from loop_lib import *`  -> every member of consts is a local name
    ... 82's walk outside docs and derive_fixture_boundary(tree), unchanged

derive_conf_constants(loop_lib_path):
    missing or unparseable -> LoopError(loop_lib_path, why)
    the module-level Assign and AnnAssign targets whose value is one of
        Constant str | JoinedStr | BinOp of these | Path(<one of these>) | PurePath(<one of these>)
    and whose source text contains ".memory-tree.conf" or ".unattended.conf"
```

### The added rows (S13, S15)

Each `conf-read-forms` row is a scratch folder holding the module the row reads and its `loop_lib.py`
sibling, written inside `run_budget_plant`.

| Row | Sibling `loop_lib.py` binds | The module reads | Owed |
|---|---|---|---|
| a Path binding | `UNATTENDED_CONF_PATH = Path(".unattended.conf")` | `ll.UNATTENDED_CONF_PATH` after `import loop_lib as ll` | one `conf constant` hit |
| an annotated binding | `CONF: str = ".memory-tree.conf"` | `ll.CONF` after `import loop_lib as ll` | one `conf constant` hit |
| a star import | `CONF = ".unattended.conf"` | `CONF` after `from loop_lib import *` | one `conf constant` hit |
| no sibling | no `loop_lib.py` in the folder | `ll.CONF` | a `LoopError` naming `loop_lib.py` |

80 S3's staged module gains the sibling `loop_lib.py` holding the one line `NOTHING = 0`.

### The failure detail, after this unit (S22)

```
build_failure_detail(outcome, text):
    OSError                        -> "start failed: <its text>"                 # 85 S6, unchanged
    code = "signal <-outcome>" if outcome < 0 else "<outcome>"
    line = the first non-blank line of text, else "(no stderr)"
    -> "<code> <line>"
```

`resolve_write_tree_support` passes the probe's joined text, so a probe exiting 129 with no output
reads `129 (no stderr)`, and the `push-merge-probe-silent` row's needle `probe failed: 129` still
matches, since `run_fixture` tests `needle in said`.

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `77130f241`, through `git archive` into a
scratch copy, unless named otherwise. `tools/loop/` is absent from this worktree's main.
`derive_conf_reads`, `derive_fixture_boundary`, `derive_docstring_ids`, the `no-own-conf-read`,
`conf-read-forms` and `url-forms` plants and the HTTP fetch are not built at that tip: they are read on
the committed specs §5 "Dependency" names.

- `tools/loop/guard.py#check_write_tree_usage` answers `supported` for any text naming `--write-tree`
  whatever its exit code, and `unsupported` only for exit 129 with a usage line.
  `tools/loop/guard.py#resolve_write_tree_support` is its one caller, memoised, and swapped plants
  reach it through `run_merge_tree_usage`.
- `tools/loop/guard.py#build_failure_detail` spells an `OSError` `start failed: <its text>` and an exit
  code `<rc>` followed by the first non-blank line of `text` where it has one, so a signal reads as a
  negative number and an empty stderr as the bare code. `tools/loop/guard.py#read_remerge_policy`
  catches an `OSError` from `run_merge_tree` as `failed`.
- `tools/loop/guard.py#check_push_range`'s `failed` branch parses each parent past the first and
  refuses `at parent <sha8>` where one does not parse, as its parents-only branch does; no plant grades
  an unparseable parent under `failed`. The `push-merge-tree-fatal` plant swaps `run_merge_tree` to
  `(128, "", "fatal: fx stand-in\n")` and owes `128 fatal: fx stand-in`; its siblings
  `push-merge-probe-failed` and `push-merge-probe-silent` owe `probe failed: start failed: fx stand-in`
  and `probe failed: 129`.
- On node `d`, `git config --show-origin --get-all credential.helper` printed `manager` from
  `C:/Program Files/Git/etc/gitconfig`, and `git merge-tree -h` under git 2.54.0.windows.1 exited 129
  printing `usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>`: PINNED, 2026-11-16.
- `tools/loop/loop_witness.py#read_clean_env` builds its environment from `os.environ` less the
  memory-tree kit's `GIT_ENV_LEAKS`, with its keywords set, and `tools/loop/loop_witness.py#read_git`
  runs `git -C <repo> <args>`. 77 rev-3 §4 "The plants" runs the `url-forms` fetch through `read_git`
  with `GIT_TERMINAL_PROMPT=0` alone, and 82 S23 adds a fetch from `http://user:tok@127.0.0.1:<port>/r.git`.
  75 rev-10 S34 points `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM` at an empty file in `run_plant`, which
  reaches the fetch only where its environment is inherited, and `read_clean_env` copies the process's.
- `tools/loop/loop_lib.py` imports no `tree_lib` at module level; `tools/loop/loop_lib.py#read_memory_tree`
  resolves the memory-tree kit through `resolve_kit_dir` and puts it on `sys.path`, the route
  `read_clean_env` takes inside its call. `tools/memory-tree/tree_lib.py` holds no
  `derive_docstring_ids` at the tip. `tools/memory-tree/kit.toml` records that govkit cannot express a
  version floor.
- `tools/loop/loop_lib.py#LoopError` subclasses `ValueError` and reads `<where>: <what>`.
  `tools/loop/budget.py#run_budget_plant` catches `LookupError` alone around its cases.
- 82 rev-6 S1 reads the conf-constant bindings by parsing `loop_lib.py` and names no folder, while its
  AC1 reads a scratch `loop_lib.py`. 80 rev-6 S3 has the `no-own-conf-read` case of `budget.py` call
  `derive_conf_reads` on a module it writes into a scratch folder, owing two `conf name` hits.
- The build README's build-order region prints step 38 with Parallel `no`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_conf_constants` | Python function in `tools/loop/loop_lib.py` | `py.function`, verb-first |
| `push-merge-tree-fatal-unparseable-parent` | `PLANTS` name in `tools/loop/guard.py` | none |

`python tools/lexicon/lexicon.py --suggest derive_conf_constants --as py.function` answered OK, leading
with the declared verb `derive`, run in the scratch copy of the tip on 2026-11-16.

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`
- `tools/loop/loop_lib.py`
- `tools/loop/README.md`
- `help/policy.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the guard items and the rest.** At rev-7 the halves shared the 76, 80 and 81
  specs. At rev-8 the guard items, S2, S6 and S22, and the conf-read items, S10, S13, S15 and S21, are
  disjoint by file, but S9 alone would make a third unit for one fetch, and a split now moves an order
  every sibling cites.
- **An explicit `loop_lib_path` argument for `derive_conf_reads` (L2's other option).** The plant's
  scratch copy already puts the two files side by side, and a sibling rule needs no caller to pass the
  kit's own path; the argument would be a second way to say the same thing (§8 F3).
- **A version floor in `tools/loop/kit.toml` for S21.** govkit cannot express one; a named refusal at the
  one call that needs the function is the route the memory-tree kit's own `requires_if` rows take.
- **Rev bumps of the CLOSED siblings at this pass.** BUILD-METHOD's SPEC-exit rule keeps a CLOSED spec
  frozen, with its correction a new unit on top (§8 F5).

## 5. Production-readiness checklist

- security — S9 keeps a planted credential out of the OS credential store and off any prompt: the store
  is a write surface outside the repository, and no helper runs. S13 widens what the no-own-conf-read
  rule sees. S6 and S22 keep a failed re-merge refusing with no traceback.
- perf / scale — S6 adds one plant and S22 three in-process grades to `loop guard fixtures`, each a
  scratch history graded once, seconds.
- error / empty / loading states — S13 and S21 name a missing or broken input instead of answering an
  empty set or raising `AttributeError`; S22 spells a signal and an empty stderr.
- observability — each refusal names its file or case.
- risks — S2 reads a translated usage header as `probe failed`, so on a node whose git ships a
  translation and runs a non-English locale every two-parent merge grades as `failed`, against every
  parent with no exemption, until `TOOL-dDeclaredLoop-88` S16 pins `LC_ALL=C` at order 44. That fails
  closed, and node `d`'s git ships no translation (88 §4). S13 makes a scratch module with no sibling
  `loop_lib.py` refuse, which S15's stubs answer for every caller the committed specs name.
- testing — AC2 to AC22 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed.
- user docs — `help/policy.md`'s push check, S2; `tools/loop/README.md`'s table of `loop_lib.py`
  functions, S13.

### The sweep

Read at the tip `77130f241` in the scratch copy; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `check_write_tree_usage`, narrowed (S2) | its one caller `resolve_write_tree_support`; the plants `push-merge-old-git-usage`, twin `(129, "", "usage: git merge-tree <base-tree> ...")`, `push-merge-probe-silent`, twin `(129, "", "")`, `push-merge-probe-failed`, a twin raising, and `push-merge-no-write-tree`, which swaps the resolver itself; the real git's probe | each answer holds: `unsupported`, `probe failed`, `probe failed`, untouched, and `supported` for git 2.54's exit 129 usage line |
| `build_failure_detail`, two spellings (S22) | its two callers; the needles `128 fatal: fx stand-in`, `probe failed: start failed: fx stand-in`, `probe failed: 129` and the unrelated-history row's `the clean re-merge failed: 128` | the first, second and fourth texts carry a stderr line or an `OSError`; the third now reads `probe failed: 129 (no stderr)`, which still holds the needle as a substring |
| `PLANTS` of `guard.py` gains one (S6) | `run_selftest`'s owed map; the `--plant` choices; the leg `loop guard fixtures`; its row in `tools/run-gates/selftest-budgets.txt`, 90 seconds PINNED, and its manifest ceiling, 300 seconds PINNED | an owed entry of 1; `tools/govkit/usage.toml` holds no row for `guard.py`; the pass times the plant and the three grades by direct CLI and re-prices the row by that file's rule where the sum crosses it, raising no ceiling |
| the `url-forms` fetch arguments (S9) | that plant alone, under `loop position fixtures` | AC9; the plant's owed readings do not move |
| `derive_conf_reads`: the sibling rule, the star import, the in-call `tree_lib` (S13, S15, S21) | the `no-own-conf-read` case of `budget.py` and `breakpoints.py`, 80 S3's staged module, 82's `conf-read-forms` rows; `python -c "import loop_lib"` in every loop leg, `loop definition` among them | S15's stubs; the two real modules sit beside the kit's own `loop_lib.py`; the import adds no module-level reach |
| `derive_conf_constants` minted (S13) | `memory/map/generated/symbols.json` and its three siblings, under `codebase-map coverage + freshness`; the lexicon offender pin | `python tools/codebase-map/gen_map.py --write`; the name leads with a declared verb |
| the module docstring of `guard.py` and `help/policy.md` (S2, S22) | the push check paragraph of `help/policy.md`, which carries no usage anchor; the leg `policy fixtures`, whose guard lists `help/policy.md` and whose fixture reads that page's deferral line; the docstring, read by no gate | the sentences are added in place, and the deferral line does not move |
| shipped bytes | `install-prefix (shipped surface)` and `kit epoch (shipped bytes move, the version moves)` | the new lines name confs, module files and a govkit command, never a kit path; `KIT_LOOP_VERSION` is owed at the lander, as for 76 and 80 |
| this spec's citations | `memory/project/positional-refs.txt`, its 12 rows PINNED for this spec, under `positional (the citation check alone)` | rev-8 cites symbols only, so the commit landing it runs `python tools/playbook/positional.py shrink` |
| this spec's numbers | 76, 80, 87 to 94 and 96 to 100 cite S2, S3, S4, S5, S6, S8, S10, S12, S13, S15, S17, S19, S21, S22 and AC9 to AC22 by number | every number is kept, a settled one in §3's table; each sibling's re-ground owns its own text |

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -e check_write_tree_usage -e build_failure_detail "$B" -- tools        # guard.py alone
git grep -n -e derive_conf_reads -e derive_conf_constants -e derive_docstring_ids "$B" -- tools   # no match
git show "$B:tools/loop/guard.py" | grep -n '"push-merge-probe-silent": 1'
git show "$B:tools/govkit/usage.toml" | grep -c 'loop/guard.py'                     # 0
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop guard fixtures'
git show "$B:tools/gate-legs.json" | grep -A8 '"loop guard fixtures"' | grep ceiling
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-86.md'   # 12
git grep -o -h -e '86 S[0-9]*' -e '86 AC[0-9]*' "$B" -- memory/builds/dDeclaredLoop/spec | sort | uniq -c
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
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added,
  `tools/memory-tree/check-verdict-epoch.sh` names no loop module, no `[[upgrade]]` row is owed, and no
  file the `watch:` line of `memory/guides/SESSION-KICKOFF.md` names is edited.

### Dependency

Built and CLOSED: `TOOL-dDeclaredLoop-81` and `TOOL-dDeclaredLoop-85` (orders 20 and 21), whose
`guard.py` code S2, S6 and S22 extend. Unbuilt, read on their committed specs: `TOOL-dDeclaredLoop-76`
rev-6 (order 37) for `derive_conf_reads` and the `no-own-conf-read` case; `TOOL-dDeclaredLoop-80` rev-6
(order 38) for `derive_fixture_boundary`, the staged module and S4's population; `TOOL-dDeclaredLoop-77`
rev-3 and `TOOL-dDeclaredLoop-75` rev-10 (order 39) for the `url-forms` plant and `run_plant`'s empty
configs; `TOOL-dDeclaredLoop-79` rev-6 (order 40), which writes `budget.py`'s `trailing-slash-agree` and
`no-confs` plants; `TOOL-dDeclaredLoop-82` rev-6 (order 41) for the conf-constant kind, the
`conf-read-forms` rows, `derive_docstring_ids` and the HTTP fetch. Each builds before this unit, which
builds alone at order 42 over their landed code; where a landed shape differs from its committed spec,
the pass reads the landed one and records the difference as a deviation. `TOOL-dDeclaredLoop-87` builds
alone at order 43 over this unit's `derive_conf_constants`. `TOOL-dDeclaredLoop-72` is building now and
`TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113, and `TOOL-dDeclaredLoop-33`'s
numeric direction against ask TOOL-dDeclaredLoop-114; none moves a read this unit makes. The reuse probe,
the lexicon's suggest verb and the spec-token checker ran in the scratch copy of the tip; the
credential-helper and usage probes ran on node `d`'s git.

## 6. Acceptance criteria

Each `python guard.py`, `python position.py` and `python budget.py` command below runs in the loop kit's
folder.

- **AC2** — When a `python -c` probe imports `guard` and calls `check_write_tree_usage` on
  `(0, "usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>")`,
  `(0, "usage: git merge-tree <base-tree> <branch1> <branch2>")`,
  `(128, "error: unknown option --write-tree")` and `(129, "see --write-tree")`, it answers `supported`,
  `unsupported`, `probe failed` and `probe failed`, and `resolve_write_tree_support()` answers
  `supported` under the node's git; and `grep -c "0 or 129"` over `help/policy.md` prints at least 1.
  Red when: a text naming the option with no usage line, or under another exit code, answers `supported`.
- **AC6** — When `python guard.py --fixture --plant push-merge-tree-fatal-unparseable-parent` runs, it
  exits 1 printing `the clean re-merge failed: 128`, `does not parse at parent ` and the plant's
  `all held` line, and no `Traceback`.
  Red when: the `failed` branch raises on the parent, or reads it as holding no keys.
- **AC9** — When `cmdkey //list` is read from Git Bash before and after
  `python position.py --fixture --plant url-forms`, no new credential target for the fixture's loopback
  URL appears, and `grep -c "credential.helper="` over `position.py` prints at least 1. With the
  `-c credential.helper=` arguments staged out, a new target appears, and the build clears it with
  `cmdkey //delete:<target>`.
  Red when: the plant's fetch runs with the node's credential helpers active.
  permission: the staged break writes one dummy entry to the OS credential store, which the build makes
  and clears; a reviewer does not.
  fixture: a node with Git for Windows' `manager` helper; elsewhere both halves read no new entry.
- **AC10** — When `python budget.py --fixture --plant no-own-conf-read` and the same plant of
  `breakpoints.py` run at this pass, each exits 0 and prints a `fixture boundary:` line. In a scratch copy
  of the kit folder whose added `conf-read-forms` bindings sit in a module-level table, the first exits
  non-zero naming `conf name`.
  Red when: a forms table outside the boundary turns the rule red at the close.
- **AC13** — When `python budget.py --fixture --plant conf-read-forms` runs, it prints `held`: the Path
  binding, the annotated binding and the star-import rows each answer one `conf constant` hit, and the
  row with no sibling `loop_lib.py` answers a `LoopError` naming `loop_lib.py`. With
  `derive_conf_constants` staged to count a plain `Assign` of a `Constant` alone, the plant misses.
  Red when: only a plain `Assign` of a `Constant` counts, or a missing `loop_lib.py` yields an empty set.
- **AC15** — When `python budget.py --fixture --plant no-own-conf-read` runs, the staged module's two
  `conf name` hits are read with its stub `loop_lib.py` beside it; with the stub staged out, the case
  misses naming `loop_lib.py`. And
  `python -c "import inspect, loop_lib; print(inspect.signature(loop_lib.derive_conf_reads))"` prints
  `(path)`.
  Red when: the rule reads a fixed `loop_lib.py` while a plant reads a scratch one, or a caller passes it.
- **AC21** — When a scratch copy of the tip's `tools/` folder has `derive_docstring_ids` taken out of
  its copy of `tools/memory-tree/tree_lib.py`, `python -c "import loop_lib"` in its `loop/` exits 0,
  and `python budget.py --fixture --plant no-own-conf-read` there exits non-zero printing
  `govkit update --kits memory-tree` and no `Traceback`.
  Red when: the loop kit imports the function at module load, or raises `AttributeError` at the call.
- **AC22** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs, it exits 1 with its
  `all held` line, its `OSError` row printing `the clean re-merge failed: start failed: fx stand-in`, its
  signal row `signal 9` and its empty-stderr row `128 (no stderr)`, and no `Traceback`. A `python -c`
  probe of `build_failure_detail` on `(-9, "")`, `(128, "")`, `(128, "fatal: x\n")` and
  `(OSError("e"), "")` answers `signal 9 (no stderr)`, `128 (no stderr)`, `128 fatal: x` and
  `start failed: e`.
  Red when: a start failure propagates, a signal reads as a negative code, or an empty stderr leaves a
  bare code.

## 7. Gates

`install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop legs this pass keeps green, built and in the manifest at the tip but outside the base manifest
the line above is joined against: `loop guard fixtures`, `loop position fixtures`,
`loop budget fixtures`, `loop breakpoint fixtures` and `loop definition`.

New arm: tools/loop/guard.py · covers AC6 AC22 · the tree-fatal unparseable-parent plant, and the start-failure, signal and empty-stderr rows, each staged as its criterion's Red when · none
New arm: tools/loop/budget.py · covers AC10 AC13 AC15 · the conf-read-forms rows inside the boundary, the Path, annotated and star-import bindings and the missing sibling, and the staged module's stub, each staged as its criterion's Red when · none
New arm: tools/loop/position.py · covers AC9 · the url-forms fetches with the credential-helper arguments staged out · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records; first resolved 2026-10-24.
  RESOLVED (agent, 2026-11-16, delegated): (`**Derived:** PLAY-dClosedLoop-2`).
  widens: none · relaxes: none
- **F2 — Repair M4 by folding the boundary into 76, building 80 in 76's pass, or moving the observation
  (ids 11, 17)?** (a) fold 80 into 76 as a rev bump; (b) one pass for 76 and 80; (c) move 76 AC1's exit-0
  half and 79 AC10's re-observation to 80's pass commit. (a) and (b) rewrite two audited units' scope or
  dispatch from a batch that builds after both; (c) is id 11's own alternative, judged sound for AC1, and
  S5 extended it to 79 AC10 as the skeptic's correction requires. 76 rev-6 now carries (c) for AC1, and
  79 AC10's half is §8 F5's. First resolved 2026-10-24.
  RESOLVED (agent, 2026-11-16, delegated): (c).
  widens: none · relaxes: none
- **F3 — Where does `derive_conf_reads` find loop_lib (ids 5, 28)?** (a) the `loop_lib.py` beside the
  scanned module; (b) an explicit `loop_lib_path` argument defaulting to the kit's own. Both satisfy
  AC13 and AC15; (b) adds a parameter every caller can mis-pass, and (a) is M12's fix. First resolved
  2026-10-24. RESOLVED (agent, 2026-11-16, delegated): (a), S13 and S15.
  widens: none · relaxes: none
- **F4 — Clear the credential helpers on the fetch call itself, or rely on 75 S34's empty system and
  global configs (id 23)?** (a) `-c credential.helper=` with prompting off on the fetch; (b) state that
  the fetch inherits 75 S34's environment. Both keep the store untouched when built as stated. (b) rests
  the guarantee on another scope item's environment reaching one call, which is the gap the finding
  measured; (a) holds wherever the fetch runs and AC9 observes the store. First resolved 2026-10-24.
  RESOLVED (agent, 2026-11-16, delegated): (a), S9.
  widens: none · relaxes: none
- **F5 — What becomes of the items that amend a sibling spec CLOSED before order 42?** Rev-7 had this
  pass rev-bump the specs of 59, 76, 78, 79, 80, 81 and 82. 59, 78 and 81 are CLOSED now, and 76, 79, 80
  and 82 build at orders 37 to 41, so every one is CLOSED when this unit builds. (a) rev-bump them at
  this pass anyway; (b) each spec-text item leaves this unit's scope, settled where the built code or a
  committed spec already holds it, and named for the sibling's own re-ground where the defect still
  lives in an unbuilt spec, as 80 rev-6 §8 F3 and 76 rev-6 did for this unit's S3, S4, S10 and S16; (c)
  keep each as an observation this pass records. (a) writes a frozen record, which BUILD-METHOD's
  SPEC-exit rule forbids; (c) observes specs no builder reads after their close. The items still live
  in unbuilt specs are 79 AC10's exit at 76's pass commit (S5) and 82 S6, AC5, AC6, AC21 and §4's line
  pins (S8, S11, S12, S18, S19). Recommendation: (b), with code halves kept as S6, S9, S10, S13, S15,
  S21 and S22. RESOLVED (agent, 2026-11-16, delegated): (b).
  widens: none · relaxes: none
- **F6 — How does S22 spell a start failure in 85's one detail builder?** (a) keep the built
  `start failed: <its text>`, the `OSError`'s whole message; (b) `start failed: <strerror>`, rev-7's
  text, which is `None` for an `OSError` built from one message, as every plant's twin is, so the
  plants' needles and 85's printed lines would move. (a) leaves the probe's and the re-merge's start
  lines as 85 landed them and adds only the signal and empty-stderr spellings. Recommendation: (a).
  RESOLVED (agent, 2026-11-16, delegated): (a), S22.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-6 spec audit's 22 minors batched (13 MEDIUM, 9 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-87 and TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-89 and TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-92, written by the round-9 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-6 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.
- rev-7 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-98, written by the round-12 spec audit's disposal; nothing else moved.
- rev-8 · 2026-11-16 · §1 · S1 to S22 · §3 · §4 · §5 · AC1 to AC22 · §7 · §8 · §10 · re-grounded on
  branch/unattended-declared-loop-d56bf0 at `77130f241` by the brief
  2026-11-16-prompt-TOOL-dDeclaredLoop-86-1-spec-writer; mechanism, carries, order and status kept.
  Every sibling rev bump leaves scope, the specs being CLOSED by order 42 (F5): S1, S3, S4, S5, S7, S8,
  S11, S12, S14, S16 to S20 and their criteria move to §3's table with what settles each, numbers kept.
  S2 brings the help sentence; S6 is the plant alone; S9 covers both fetches; S10 is this unit's rows;
  S13 refuses through `LoopError`; S15 stubs 80's staged module; S21 takes `read_memory_tree`; S22 keeps
  85's start spelling (F6). AC9 reads the store as `cmdkey //list`; the loop legs named by their built
  names; line citations made symbol citations; the sweep.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 85's `check_write_tree_usage` (S2)
and `build_failure_detail` (S22), 81's `failed` grade and `push-merge-tree-fatal` plant (S6, S22), 76's
and 82's `derive_conf_reads` and 80's `derive_fixture_boundary` (S10, S13, S15, S21), 77's and 82's
`url-forms` plant through `read_git` and `read_clean_env` (S9), and the loop kit's
`read_memory_tree` route to `tree_lib`, as `read_clean_env` takes it (S21).
`python tools/codebase-map/reuse_lookup.py "probe whether a git subcommand supports an option, distinguishing a failed probe"`
ranked `git`, `probe`, `run_git` and `LaunchFailed`, none a three-way capability answer, so S2 extends
85's predicate.
`python tools/codebase-map/reuse_lookup.py "module-level names bound to a string constant read by parsing a python file with ast"`,
run in the scratch copy of the tip on 2026-11-16, ranked `read_text`, `read`, `parse`, `parse_conf`,
`read_memory_tree` and `read_design_conf`, none a reader of a module's bindings, so no existing seam fits
`derive_conf_constants`: the conf-name constant kind is 82's and lives beside `derive_conf_reads`.

Recall terms used: spec-audit minors batch derive_conf_reads conf constant derive_conf_constants credential helper probe failed build_failure_detail read_memory_tree tree_lib
