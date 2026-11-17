# TOOL-dDeclaredLoop-94 — the round-10 spec audit's 24 minors, batched

**Status:** DEFERRED · rev-4 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 48 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-941.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-941.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-942.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-942.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-94-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-94-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-94-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-94-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-93 |

<!-- /gen:spec-records -->

## 1. Goal

The round-10 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md`)
exited CONVERGED with 25 confirmed findings over units 91 and 92, the round-9 promotions. Its one high,
id 1, is unit 93. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The minors land on 91 and 92 both, so this unit repairs neither in particular and builds after every
unit (order 48, above 93's 47).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 12, 15 | S1, S2, S3 |
| M2 | MEDIUM | 3, 17, 21 | S4, S5, S6 |
| M3 | MEDIUM | 22 | S7 |
| M4 | MEDIUM | 23 | S8 |
| M5 | MEDIUM | 4 | S9 |
| M6 | MEDIUM | 24 | S10 |
| M7 | MEDIUM | 27, 19 | S11, S12 |
| M8 | MEDIUM | 10 | S13 |
| M9 | MEDIUM | 11 | S14 |
| L1 | LOW | 6 | S15 |
| L2 | LOW | 7 | S16 |
| L3 | LOW | 8 | S17 |
| L4 | LOW | 9 | S18 |
| L5 | LOW | 13, 29 | S19, S20 |
| L6 | LOW | 14 | S21 |
| L7 | LOW | 16 | S22 |
| L8 | LOW | 20 | S23 |
| L9 | LOW | 25 | S24 |

That is 14 MEDIUM and 10 LOW findings by raw id. The report's four refuted findings, ids 5, 18, 26 and
28, are not in the disposal population.

At rev-4 two items are live, S20 and S21, each a code change in the loop kit. The other twenty-two are
settled at HEAD of `branch/unattended-declared-loop-d56bf0`, or by unit 92's rev-5, which builds at order
46 before this unit. Each spec text they amend sits in a spec that is CLOSED, or CLOSED by the time this
unit builds, and so frozen, and each code half they name already reads as stated, or has nothing left to
change under 92 §8 F3. §3 names each with its evidence. The item ids, and the criterion ids AC14, AC15
and AC16, keep their rev-3 numbers, so a sibling's citation of them still lands.

## 2. Scope (IN)

- **S20** — id 29. `build_failure_detail` in `tools/loop/guard.py` spells an `OSError` as
  `start failed: <detail>`, the detail the first non-blank line of `str(exc)`, stripped, or the
  exception's class name where `str(exc)` holds no non-blank line. That is the rule the function's
  exit-code branch already applies to `text`, so an interior newline in an `OSError` message stays out
  of the one-line refusal. Every one-line spelling 92 S17 fixes keeps its bytes, the four answers of
  92 AC16 among them. The function's docstring and the module docstring's `start failed` clause each say
  "first non-blank line". The `push-merge-tree-fatal` plant gains two rows after the rows 92 S17 adds:
  `start failed, two lines`, an `OSError("a\nb")` raised in place of the clean re-merge, owing
  `the clean re-merge failed: start failed: a`; and `start failed, two lines, the second line`, appended
  after it with the needle idiom of the `graded, no Traceback` row, missed where any line of that grade's
  output is `b`. Its `PLANTS` description names the two-line start. The added grade is priced on the
  `loop guard fixtures` row of `tools/run-gates/selftest-budgets.txt`, as §4 Rollout states.
  Observed by AC14, AC15.
- **S21** — id 14. `load_tree_lib` in `tools/loop/loop_lib.py` tests every name of `TREE_LIB_SYMBOLS`
  on the loaded module and raises one `LoopError` naming every name it lacks, in tuple order joined by
  `, `, where it refused at the first. A module lacking one name gets the refusal text it gets at HEAD.
  Its import catch takes any `Exception` the import raises, after `read_memory_tree`'s `LookupError`, in
  place of the two classes `ImportError` and `SyntaxError`, naming the exception's class as it names
  those two (F6). The function's docstring, and its row in the table of `loop_lib.py` functions in
  `tools/loop/README.md`, say both. The `conf-read-forms` plant of `tools/loop/budget.py` gains two rows
  after 88 S33's three, each a scratch folder of its own first on `sys.path`, with the route's
  `read_memory_tree` swapped to answer it and `tree_lib` absent from `sys.modules` for the call:
  `raising`, a `tree_lib.py` whose body raises `RuntimeError("fx stand-in")`, owing a `LoopError` naming
  `RuntimeError` and `govkit update --kits memory-tree`; and `lacking both`, a `tree_lib.py` defining
  neither name, owing one naming `derive_docstring_ids, derive_constant_charges`. Its `PLANTS`
  description names both rows. Observed by AC16.

## 3. Non-goals (OUT)

- The high's mechanism, 92 AC16's exit code: unit 93, an observation pass at order 47.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Any edit to the specs of units 75, 85, 86, 87, 88, 89, 90, 91 or 92. The first eight are CLOSED at HEAD
  and frozen, and 92, INPROGRESS at order 46, is CLOSED before this unit builds at order 48, so every rev
  bump rev-3 planned on one of them is out.
- A `need` argument to `load_tree_lib`, and `GIT_ENV_LEAKS` behind it. Under 92 §8 F3 (c),
  `tools/loop/loop_witness.py` carries the shared `git_env_leaks_py` block inline and calls no loader, so
  no caller reads a subset of `TREE_LIB_SYMBOLS` and the tuple keeps its two members.
- The `sys.dont_write_bytecode` half of id 14. Every loop entry script sets it at module level, the two
  that reach the loader among them, and `loop_lib.py` is a library whose importer owns the switch.
- A ban on every `tree_lib` route across `tools/loop/`. `read_build_headers` and `read_transition_moves`
  in `tools/loop/loop_transition.py` and `check_upstream_rows` in `tools/loop/upstream.py` import
  `tree_lib` by name, kept by 92 §8 F5 and 90 §8 F7.
- A `tree_lib` loader in any kit but `tools/loop/`, and a change to 88 AC18's rows.
- The twenty-two settled items. Each was read on the branch tip §4 Evidence names:

| Item | Report id | Settled because |
|---|---|---|
| S1 | 2 | 92 rev-5 AC8 grades `tools/loop/loop_witness.py` alone for a str constant naming `tree_lib.py`, so the skew row of `tools/loop/budget.py` meets no ban; the 92 text is frozen at its close |
| S2 | 12 | `run_budget_plant`'s `no-own-conf-read` case in `tools/loop/budget.py` takes the memory-tree kit as the parent of `load_tree_lib().__file__` and calls no locator of its own |
| S3 | 15 | the sweep of 92 rev-5 §5 names the skew row of `budget.py` as a reader of `load_tree_lib`; the 92 text is frozen at its close |
| S4 | 3 | the attribute population is 90 AC4's, built over `tools/loop/loop_lib.py` under 90 §8 F6 (a); 92 rev-5 AC8 holds no population |
| S5 | 17 | an `ast` probe over every `*.py` under `tools/loop/` finds no `load_tree_lib(...)` call as an argument of any call; the 92 text is frozen at its close |
| S6 | 21 | 90 AC4 carries the staged break, a scratch `loop_lib.py` reading `load_tree_lib().kit_rel`; the 92 text is frozen at its close |
| S7 | 22 | the ban would red on the `tree_lib` imports of `loop_transition.py` and `upstream.py`, which 92 §8 F5 and 90 §8 F7 keep; the 92 text is frozen at its close |
| S8 | 23 | 92 rev-5 S8: `read_clean_env` reads the inline `GIT_ENV_LEAKS`, so `loop_witness.py` resolves no kit at import or at first use |
| S9 | 4 | spec text alone, in the frozen 75, 88, 90 and 92 |
| S10 | 24 | spec text alone, in the frozen 89, 90 and 92 |
| S11 | 27 | spec text alone, in the frozen 89; `derive_conf_rebinds` descends `_MODULE_SCOPE_PARTS` for a `FunctionDef`, `AsyncFunctionDef`, `ClassDef` or `Lambda`, as 91 built it |
| S12 | 19 | spec text alone, in the frozen 87, 89 and 91 |
| S13 | 10 | spec text alone, in the frozen 91, whose `conf-read-forms` module-scope rows each carry their exec parity line |
| S14 | 11 | spec text alone, in 92 S17 and the frozen 88; 93 rev-3 observes the plant's exit 1 |
| S15 | 6 | spec text alone, in 92, whose rev-5 settles its S6 and holds no AC6 |
| S16 | 7 | spec text alone, in 92, whose rev-5 settles its S9 and holds no AC9 |
| S17 | 8 | as S16 |
| S18 | 9 | spec text alone, in 92, whose rev-5 settles its S5 and holds no AC5 |
| S19 | 13 | `build_failure_detail` takes two arguments, `(outcome, text)`, and 92 rev-5 AC16 calls it with `""` as its text; no third argument exists |
| S22 | 16 | 92 §8 F3 (c), as the bullet above states |
| S23 | 20 | spec text alone, in the frozen 85, 86 and 88, and in 92 S17 |
| S24 | 25 | the skew row copies two files, `loop_lib.py` and `tree_lib.py`, into the plant's own `tempfile.mkdtemp` root outside the repository, removed in `run_budget_plant`'s `finally`, and checks them in a fresh `sys.executable -I` child, as 90 §8 F8 (a) built it |

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-92` — S17's `OSError` spelling and its two `push-merge-tree-fatal` rows, which S20 extends, and S8, §3 and §8 F3 and F5, whose rev-5 text settles S1, S3 to S8, S14 to S19, S22 and S23 here (the round-10 spec audit's ids 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 29)
- **consumes-from** `TOOL-dDeclaredLoop-93` — 92 AC16's exit 1 as that unit observes it, the exit AC15 states for the same plant and its exit-claim probe counts (the round-10 spec audit's id 11)
- **consumes-from** `TOOL-dDeclaredLoop-91` — the module-scope walk and the `conf-read-forms` module-scope rows as that unit built them, and its frozen S5, AC3 and AC4, which settle S11 to S13 (the round-10 spec audit's ids 10, 19, 27)
- **consumes-from** `TOOL-dDeclaredLoop-90` — `TREE_LIB_SYMBOLS` and its in-order test, which S21 extends to every missing name, the skew row of §8 F8 (a), which settles S2 and S24, and AC4's population, which settles S4 and S6 (the round-10 spec audit's ids 4, 24)
- **consumes-from** `TOOL-dDeclaredLoop-89` — `load_tree_lib` as its S6 minted it, and its frozen sketch, §3 and §5, which settle S10 to S12 (the round-10 spec audit's ids 19, 24, 27)
- **consumes-from** `TOOL-dDeclaredLoop-88` — S33's two catches and three `conf-read-forms` rows, which S21 widens and extends, and S24's `build_failure_detail`, which S20 extends; its frozen S18, AC18 and AC24 settle S14 and S23 (the round-10 spec audit's ids 4, 11, 20)
- **consumes-from** `TOOL-dDeclaredLoop-87` — §3's first non-goal and §5, frozen, which settle S12 and S15 (the round-10 spec audit's ids 6, 19)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S22's `start failed` spelling, frozen, which settles S23 (the round-10 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-85` — S3's `start failed` spelling, frozen, which settles S23 (the round-10 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-75` — S35, frozen, which settles S9 (the round-10 spec audit's id 4)
- **hands-off** `TOOL-dDeclaredLoop-95` — `load_tree_lib` as S21 leaves it, whose tuple that unit restates; rev-4 holds no route probe and no route sketch for it to make hold (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-96` — S21, §5 and §8 F6, with `load_tree_lib` as S21 leaves it; the items, probe and criteria that unit restates on S2, S5, S8, S10, S22 and S24 are settled in §3 here (the round-11 spec audit's ids 2, 3, 4, 5, 7, 9, 10, 12, 13, 14, 15, 16, 17)
- **hands-off** `TOOL-dDeclaredLoop-100` — §5, whose sweep that unit restates; the items it restates on S5, S10 and S24 are settled in §3 here (the round-12 spec audit's ids 3, 4, 5, 16, 23)

## 4. Design

### Write set

This pass writes `tools/loop/guard.py` (S20), `tools/loop/loop_lib.py`, `tools/loop/budget.py` and
`tools/loop/README.md` (S21), and `tools/run-gates/selftest-budgets.txt` (S20, and S21 where §4 Rollout
moves it). It writes no spec and no record.

### The OSError detail, after this unit (S20)

```
if isinstance(outcome, OSError):
    detail = next((ln.strip() for ln in str(outcome).splitlines() if ln.strip()), type(outcome).__name__)
    return "start failed: %s" % detail
OSError("boom")                       -> start failed: boom
FileNotFoundError(2, "No such file")  -> start failed: [Errno 2] No such file
OSError(5, "")                        -> start failed: [Errno 5]
OSError()                             -> start failed: OSError
OSError("a\nb")                       -> start failed: a
OSError("\nb")                        -> start failed: b
```

The first four lines of answers are 92 S17's, unchanged.

### The loader, after this unit (S21)

```
def load_tree_lib():
    try:
        read_memory_tree("tree_lib.py"); import tree_lib
    except LookupError as e:  -> LoopError("memory-tree kit", "<e> — govkit update --kits memory-tree")
    except Exception as e:    -> LoopError("memory-tree kit", "<class>: <e> — govkit update --kits memory-tree")
    missing = [n for n in TREE_LIB_SYMBOLS if not hasattr(tree_lib, n)]
    if missing: LoopError(<loaded file>, "has no <', '.join(missing)> — govkit update --kits memory-tree")
    return tree_lib
```

The `conf-read-forms` loop that runs 88 S33's rows puts each row's own folder first on `sys.path`, in
place of the one folder its `unparseable` row writes, so the two added rows each import their own
`tree_lib.py`.

### Inventory

| Identifier | Where | Naming cell |
|---|---|---|
| `run_unstartable_lines` | a nested def of `run_guard_plant` in `tools/loop/guard.py`, beside `run_unstartable_usage`, raising `OSError("a\nb")` | `py.function`: `python tools/lexicon/lexicon.py --suggest run_unstartable_lines --as py.function` exits 0 |

Where 92's build lands a helper that raises a given `OSError` for its own two rows, the S20 row passes
it `OSError("a\nb")` and mints nothing. The plant rows are labels, not identifiers. The symbol tier
records no nested def: `memory/map/generated/symbols.json` holds no row for `run_unstartable_usage`.

### Rollout

After 92 lands, the builder times `python guard.py --fixture --plant push-merge-tree-fatal` in
`tools/loop/`, the worst of two direct-CLI runs, before the build and again after it. The delta joins
the proxy note of the `loop guard fixtures` row of `tools/run-gates/selftest-budgets.txt`, as units 86
and 88 appended theirs, with this unit's id. Where 1.5 times the new proxy passes the row's budget, the
budget becomes that figure rounded up to a whole second. The builder times
`python budget.py --fixture --plant conf-read-forms` the same way. It ran in 0.7 s PINNED at HEAD, and
the `loop budget fixtures` row moves only where the delta reads a whole second.

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `3c3e0d95`, its tree written by `git archive` into the run's
scratch directory, since this worktree is cut from main, which lacks the loop kit. Every probe ran in
that extracted tree, or in a scratch copy of its `tools/loop/`, `tools/lib/` and `tools/memory-tree/`.

- `tools/loop/guard.py#build_failure_detail` takes `(outcome, text)`. It returns
  `"start failed: %s" % outcome` for an `OSError`, and for an exit code the first non-blank line of
  `text`, stripped, or `(no stderr)`. A `python -I` probe gave `'start failed: a\nb'` for
  `OSError("a\nb")` with `""` as its text.
- `tools/loop/guard.py#run_guard_plant` holds a row where its exit equals the row's owed exit and its
  needle is a substring of its grade's output, so a needle of `start failed: a` holds over `a\nb` too.
  The `graded, no Traceback` row, appended after its grade with a needle computed from that output, is
  the idiom S20's second row reuses. The `push-merge-tree-fatal` plant's 86 S22 tuple holds three rows,
  and `run_unstartable_usage` raises `OSError("fx stand-in")`. 92 rev-5 AC16 owes 8 of 8 scenarios
  PINNED after 92's build.
- `tools/loop/loop_lib.py#load_tree_lib` catches `LookupError`, then `ImportError` and `SyntaxError`, and
  refuses at the first name of `TREE_LIB_SYMBOLS` the module lacks. In a scratch copy, a `tree_lib.py`
  with both `derive_*` defs renamed gave one refusal naming `derive_docstring_ids` alone, and one with
  `raise RuntimeError("fx stand-in")` appended ended in a `Traceback`, each with exit 1. A raise written
  first in the file is a `SyntaxError`, since its `from __future__` import must lead.
- The module body of `tools/memory-tree/tree_lib.py` is stdlib imports, constants and `re.compile`
  calls, so an import failure past `ImportError` and `SyntaxError` comes from a damaged file.
- Every `tools/loop/*.py` but `loop_lib.py` sets `sys.dont_write_bytecode = True` at module level.
  `derive_conf_reads` and `derive_conf_constants`, the loader's two callers in `loop_lib.py`, are called
  from `budget.py` and `breakpoints.py` alone.
- `grep -rn "def load_recall_kit" tools/` prints nothing, so the seam rev-3 named is absent at HEAD.
- `python budget.py --fixture --plant conf-read-forms` exited 0, printed its three `tree_lib` rows held,
  `unlocatable`, `blocked` and `unparseable`, and ran in 0.7 s PINNED.
- `tools/loop/budget.py#run_budget_plant`'s skew row copies `loop_lib.py` and `tree_lib.py`, 106152 and
  38460 bytes PINNED, into a folder under its `tempfile.mkdtemp(prefix="loop-budget-")` root, removed
  by `remove_tree` in its `finally`, and runs `loop_lib.load_tree_lib()` in a `sys.executable -I` child.
- An `ast` probe over every `tools/loop/*.py` found no `load_tree_lib(...)` call as an argument of any
  call, and `tree_lib` imports in `loop_lib.py` inside the loader, in `loop_transition.py` twice, in
  `loop_witness.py` inside `read_clean_env`, which 92 S8 rewrites, and in `upstream.py`.
- `tools/loop/loop_lib.py#derive_conf_rebinds` descends `_MODULE_SCOPE_PARTS` for a `FunctionDef`,
  `AsyncFunctionDef`, `ClassDef` or `Lambda`.
- No `guard` of `tools/gate-legs.json` names `{prefix}/loop/` or the budget file. The
  `{prefix}/run-gates/` guard is carried by eight legs, which the spec-token checker excludes as broad.

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/README.md`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **Rev bumps of the sibling specs, as rev-3 planned.** Each is CLOSED, or CLOSED before this unit
  builds, and a CLOSED spec is frozen.
- **The whole `load_recall_kit` idiom, the bytecode switch included.** That function is absent at HEAD,
  and a library setting a process-wide switch overrides its importer, which already sets it.
- **A by-path load of `tree_lib`, the `load_kit_module` idiom of `tools/check-spec-tokens.py`.** It moves
  how every caller imports, past the `sys.modules` and `read_memory_tree` swaps of 88 S33's rows.
- **Joining the lines of an `OSError` message with a space.** The exit-code branch already reads the
  first non-blank line of git's text, and one rule for both branches is the class.

## 5. Production-readiness checklist

- security — no new write path; the two plant rows write under the plant's own scratch root.
- perf / scale — one in-process grade on the guard plant, two in-process rows on the budget plant, priced
  under §4 Rollout.
- error / empty / loading states — S21 turns any import failure of `tree_lib` into a named refusal, and a
  module lacking both names refuses once; S20 keeps a start failure's refusal on one line.
- observability — one refusal names every missing name; the plant rows name their detail.
- risks — the sweep below names every reader the change reaches.
- testing — AC14 to AC16 as probes and plant runs; the two arms under §7, observed at the close.
- migration — none: no stored data, and an adopter's memory-tree kit is read as before.
- user docs — `tools/loop/README.md`'s `load_tree_lib` row (S21).
  `grep -rln "load_tree_lib\|start failed\|TREE_LIB_SYMBOLS" help/` prints nothing at HEAD, so no help
  page moves, and no verb, flag or usage row is added.

### The sweep

Each count is DERIVED by the command beside it, run on the branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| `build_failure_detail` (S20) | its four calls in `tools/loop/guard.py`, `grep -c "build_failure_detail(" tools/loop/guard.py` printing 5 with the def; the rows owing `start failed: fx stand-in` and `probe failed: start failed: fx stand-in`; 92 S17's two rows | every message they raise is one line, so each keeps its bytes |
| the guard plant's rows (S20) | `run_selftest`'s owed map, 1 for `push-merge-tree-fatal`; the `--plant` choices, which read the `PLANTS` keys; 93's exit-claim probe over `memory/builds/dDeclaredLoop/spec/`, which counts AC15's claim | every grade still exits 1, no key moves, and AC15 states exit 1 |
| the guard plant's cost (S20) | the `loop guard fixtures` row of `tools/run-gates/selftest-budgets.txt`, 140 s PINNED before 92's re-price, and its 300 s PINNED ceiling in `tools/gate-legs.json` | §4 Rollout re-prices the row; the ceiling stays above it |
| `load_tree_lib`'s catch (S21) | 88 S33's three rows, the tuple opening at `grep -n "for name, swap, block, owed in" tools/loop/budget.py`; the `no-own-conf-read` cases of `budget.py` and `breakpoints.py`, each catching `LoopError` | `unlocatable` still raises in `read_memory_tree`, caught as `LookupError` first; `blocked` raises a `ModuleNotFoundError` and `unparseable` a `SyntaxError`, each named as at HEAD |
| `load_tree_lib`'s refusal text (S21) | the skew row of `budget.py`, owing `derive_constant_charges`; 90 AC4's tuple; the README row and the README paragraph on the loop kit's late imports, `grep -n "TREE_LIB_SYMBOLS" tools/loop/README.md` | one missing name reads as at HEAD; the tuple keeps its two members; S21 rewrites the row, and the paragraph's "one that does not import" holds |
| the budget plant's rows (S21) | `run_selftest` of `budget.py` under `loop budget fixtures`; the `no-own-conf-read` grade of `budget.py`'s own file; the `PLANTS` description and `--plant` choices | the rows' strings hold no conf name and sit inside `run_budget_plant`, which 80 S1's boundary bounds; no `PLANTS` key is added |
| the budget plant's cost (S21) | the `loop budget fixtures` row, 498 s PINNED, and its 300 s PINNED ceiling | §4 Rollout; two in-process rows on a plant that ran 0.7 s PINNED |
| the symbol tier | `memory/map/generated/symbols.json` | no module-level def or class is added and the signatures hold, so no row moves |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the branch tip | the one possible new name passes `--suggest` (§4 Inventory), so no offender arrives |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script, `tools/loop/` holds no `.families.txt`, and `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | no written path is watched, so no `last-audit` re-stamp |
| the install-prefix ban | `tools/check-install-prefix.sh` over the shipped loop files | the added strings name no kit path |
| the verdict-epoch delegates, subject pins and upgrade steps | `DELEGATES` in `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py` | the delegates are memory-tree files, none written; no leg, subject or upgrade step moves |
| sibling specs that read this one | 93 §5, 95, 96 and 100, which cite rev-3's items, AC1 to AC13, AC17, AC18 and its sketches, and the CLOSED 90 and 91, `grep -ln "94 [SAr][Ce0-9]" memory/builds/dDeclaredLoop/spec/*.md` less this spec | the four unbuilt ones are each re-grounded before their builder, and 93's observation pass reads no criterion here; 90's and 91's text is frozen record |
| this spec's positional rows | `memory/project/positional-refs.txt`, five rows naming this spec at HEAD, `grep -c "dDeclaredLoop-94.md" memory/project/positional-refs.txt` | rev-4 keeps the `BUILD-METHOD M4` row and cites code by symbol only, so the four file-and-line rows go stale; the commit landing rev-4 runs `python tools/playbook/positional.py shrink` |

Order: this unit reads the code units 88 to 91 built, each CLOSED at HEAD, and 92 S17's spelling, which
lands at order 46. Unit 93, at order 47, writes no file.

## 6. Acceptance criteria

- **AC14** — When a `python -I -c` probe in `tools/loop/` puts that directory on `sys.path`, imports
  `guard` and calls `build_failure_detail` on `OSError()`, `OSError(5, '')`, `OSError("boom")`,
  `FileNotFoundError(2, "No such file")`, `OSError("a\nb")` and `OSError("\nb")`, each with `""` as its
  text, it answers `start failed: OSError`, `start failed: [Errno 5]`, `start failed: boom`,
  `start failed: [Errno 2] No such file`, `start failed: a` and `start failed: b`.
  Red when: an interior newline reaches the one-line refusal, or a leading blank line empties it.
  figure: at HEAD the fifth call answers `start failed: a\nb`, PINNED 2026-11-17.
- **AC15** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs in `tools/loop/`, it exits 1
  and prints `all held`, its row `graded, start failed, two lines` held naming
  `the clean re-merge failed: start failed: a`, and its row
  `graded, start failed, two lines, the second line` held, and no output line is `b`.
  Red when: the `OSError` branch takes `str(exc)` whole, staged by restoring 92 S17's spelling, which
  misses the second-line row.
  figure: the scenario count is DERIVED as 92 AC16's eight plus this unit's two.
- **AC16** — When a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory has both `def derive_docstring_ids(` and `def derive_constant_charges(` renamed in
  its `tree_lib.py`, a `python -I -c` probe in the copy's `loop/` that puts `.` on `sys.path`, calls
  `loop_lib.load_tree_lib()`, and prints a `LoopError` and exits 1 on one, exits 1 printing one line naming
  `derive_docstring_ids, derive_constant_charges`. With `raise RuntimeError("fx stand-in")` appended to
  that `tree_lib.py` instead, it exits 1 printing `RuntimeError` and `govkit update --kits memory-tree`,
  with no `Traceback`. `python budget.py --fixture --plant conf-read-forms` in `tools/loop/` exits 0 and
  prints its `raising` and `lacking both` rows, each naming `govkit update --kits memory-tree`.
  Red when: the loader stops at the first missing name, or lets a non-import error through as a traceback.
  figure: at HEAD the first run names `derive_docstring_ids` alone and the second ends in a `Traceback`, PINNED 2026-11-17.
  fixture: the observer makes the scratch copy; the tree holds none.

## 7. Gates

`loop guard fixtures` · `loop budget fixtures` · `loop breakpoint fixtures` · `loop definition fixtures` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `positional (the citation check alone)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC15 · the two-line rows of push-merge-tree-fatal, staged with build_failure_detail taking str(exc) whole · none
New arm: tools/loop/budget.py · covers AC16 · the raising and lacking-both rows of conf-read-forms, staged with load_tree_lib's HEAD catch and first-name refusal · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — Narrow AC8's ban to resolution forms, or exempt the skew row by name (ids 2, 12, 15)?** (a) the
  forms of S1 and S7; (b) an exemption naming the plant rows; (c) neither, settled in §3. Rev-3 chose (a).
  92 rev-5 AC8 grades `loop_witness.py` alone, so no skew row meets a ban, and the ban across the kit
  would red on the imports 92 §8 F5 keeps. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F3 — One all-symbols refusal for every caller, priced, or a per-caller `need` (ids 16, 23)?** (a) price
  it in 92 §5; (b) `load_tree_lib(need=...)` with the union as default; (c) neither, settled in §3. Rev-3
  chose (b). Under 92 §8 F3 (c) `loop_witness.py` reads no loader, so every caller reads the whole
  tuple. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F4 — Does `loop_witness.py` load at import or at first use (id 23)?** (a) import; (b) first use,
  inside the reading function; (c) neither, settled in §3. Rev-3 chose (b). Under 92 S8 it loads no
  `tree_lib` at all. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F5 — Drop 92 AC9's 87-range half, or label it (id 8)?** (a) drop; (b) label it a regression
  re-observation; (c) neither, settled in §3. Rev-3 chose (b). 92 rev-5 settles its S9 and holds no
  AC9. Recommendation: (c).
  RESOLVED (agent, 2026-11-17, delegated): (c). widens: none · relaxes: none
- **F6 — Does S21 build the halves of id 14 the built loader lacks?** (a) both, one refusal naming every
  missing name and any import exception named by its class; (b) neither, priced here, since the cure is
  one command whatever is missing and the built catches cover a kit that is old rather than damaged;
  (c) the every-name refusal alone. The finding is confirmed, each half costs a line, and 88 S33's rows
  and the skew row keep their text under (a). (b) leaves a damaged `tree_lib.py` ending the criterion
  runner in a traceback. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-10 spec audit's 24 minors batched (14 MEDIUM, 10 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-95 and TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.
- rev-4 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S20 S21 AC14 AC15 AC16 · re-grounded on the code at
  `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-94-1-spec-writer:
  S1 to S19 and S22 to S24 settled in §3, their spec halves in CLOSED specs or 92's, frozen at its close,
  and their code halves built or moot under 92 §8 F3 (c); S20 on 92 S17's spelling; S21 on the built
  loader, its bytecode half settled (F6); F2 to F5 re-marked (c); AC1 to AC13, AC17 and AC18 leave
  with their items; §5's sweep added.

## 10. Reuse audit

S20 extends `build_failure_detail` of `tools/loop/guard.py`, applying to an `OSError` the first-non-blank
line rule its exit-code branch holds, and S20's second row reuses the needle idiom of the
`graded, no Traceback` row of `run_guard_plant`. S21 extends `load_tree_lib` of `tools/loop/loop_lib.py`
and the three `tree_lib` rows 88 S33 wrote in `run_budget_plant` of `tools/loop/budget.py`.
`python tools/codebase-map/reuse_lookup.py "the first non-blank line of an exception's message"` ranked
`check_line`, `unfenced_lines`, `render_line` and `parse_conf_line`, none of which reads an exception.
`python tools/codebase-map/reuse_lookup.py "import a sibling kit module and refuse naming every missing attribute"`
ranked `resolve_kit_dir`, `kit_rel`, `PolicyRefused` and `kit_dir`. `resolve_kit_dir` is the locator
`read_memory_tree` already calls, and none of the others loads a module. `load_recall_kit`, which rev-3
named as the idiom, is absent at HEAD (§4 Evidence), so no existing seam fits beyond the loader itself.

Recall terms used: load_tree_lib TREE_LIB_SYMBOLS build_failure_detail OSError start failed first non-blank line conf-read-forms push-merge-tree-fatal refusal every missing name minors batch
