# TOOL-dDeclaredLoop-91 — derive_conf_rebinds reads every position a module evaluates: class bodies, defaults, decorators and bases

**Status:** INPROGRESS · rev-4 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 45 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-91-deviation-911.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-91-deviation-911.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-91-1-builder-return.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-91-1-builder-return.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-91-red-fix-61.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-91-red-fix-61.md) | red-fix | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-91-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-91-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-91-2-spec-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-91-2-spec-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-91-3-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-91-3-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-91-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-91-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-91-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-91-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-9 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-89-spec-audit.md`)
confirmed finding **id 20 at HIGH**, its item **H1**, alone in that item.

`TOOL-dDeclaredLoop-89` S1 takes only a `FunctionDef` or an `AsyncFunctionDef` as a global loader, and its
module-level walk never enters a `FunctionDef`, `AsyncFunctionDef`, `ClassDef` or `Lambda`. Python
evaluates parts of those nodes in module scope all the same: a class body, a default argument, a
decorator, a class base and a class keyword. A `global` in a class body and a walrus in any of those
positions bind a module name that neither pass answers. A loop module reading `ll.CONF` bound that way
passes `no-own-conf-read`, certified as reading no conf of its own, and the `NOT SEEN` clause 89 S5
writes into the docstring of `derive_conf_rebinds` can only price the gap.

This unit states the module-scope walk by POSITION rather than by node kind, admits a class as a loader,
and proves the class with a plant that executes each row and compares the names the execution bound
with the names the rule answers. It builds at order 45, after 89 at order 44, and repairs
`TOOL-dDeclaredLoop-89`.

Re-grounded at rev-4 on the branch tip `97ef56324`. `derive_conf_rebinds`, its docstring, its README row
and the `conf-read-forms` plant are built there, and 80, 82 and 86 to 90 are CLOSED, so this unit reads them as
they landed (§4 Evidence, §5 "Dependency"). rev-2's restatements in the specs of 87 and 89 give way to
the two carriers 89 rev-5 keeps, the docstring of `derive_conf_rebinds` and its row in the loop kit's
README (§8 F4).

## 2. Scope (IN)

- **S1** — `derive_conf_rebinds(tree, docs)` in `tools/loop/loop_lib.py` takes a `ClassDef` at any depth as
  a global loader, as 89 S1 takes a function. A class whose subtree holds a str `Constant` containing
  `.memory-tree.conf` or `.unattended.conf`, outside the docstring set `docs`, answers every name that a
  `global` in that subtree declares and that a `Name` in a store context there binds. The constant is
  tested with the one conf-name predicate 89 S1 calls. Observed by AC1, AC2.
- **S2** — The module-level walk of `derive_conf_rebinds` still never enters a body that runs in its own
  scope, and it now descends every part of a definition that Python evaluates in module scope when the
  definition runs:
  - a `FunctionDef` or `AsyncFunctionDef`: `decorator_list`, `args.defaults` and `args.kw_defaults`;
  - a `Lambda`: `args.defaults` and `args.kw_defaults`;
  - a `ClassDef`: `decorator_list`, `bases` and `keywords`.
  The descent applies again to every definition it reaches, so a lambda default inside a class base is
  read. Each `NamedExpr` reached this way answers its target when its value holds such a constant, as 89
  S1 states for a module-level `NamedExpr`. The positions sit in one private module-level table of
  `loop_lib.py`, `_MODULE_SCOPE_PARTS`, keyed by the `ast` class name and holding dotted attribute paths,
  a `None` entry of `kw_defaults` passed over. The walk reads only the parts the table names, so a
  position added later is one entry and an emptied table reads no part at all. Observed by AC1, AC2, AC3.
- **S3** — The `conf-read-forms` plant of `tools/loop/budget.py` gains a module-scope group of rows,
  written in its branch of `run_budget_plant`, the function 80 S1 bounds, and never in a module-level
  table (80 S4, 86 S10). Each row sits over a sibling scratch `loop_lib.py`, as 86 S15 places it, and is
  written across lines:
  - `class Cfg:` with `global CONF_K` and `CONF_K = ROOT / ".unattended.conf"` in its body, read as
    `ll.CONF_K`: one `conf constant` hit;
  - `def f(x=(DCONF := ROOT / ".memory-tree.conf")): pass`, read as `ll.DCONF`: one hit;
  - `def fk(*, y=(KWCONF := ROOT / ".unattended.conf")): pass`, read as `ll.KWCONF`: one hit;
  - `g = lambda x=(LCONF := ROOT / ".unattended.conf"): x`, read as `ll.LCONF`: one hit;
  - `class KB(type(BCONF := ".memory-tree.conf")): pass`, read as `ll.BCONF`: one hit;
  - a decorator `@(lambda fn, _=(DECO := ROOT / ".unattended.conf"): fn)` over `def h(): pass`, read as
    `ll.DECO`: one hit;
  - `def h2(): (HLOCAL := ".unattended.conf")`, read as `ll.HLOCAL`: no hit;
  - `class K2:` with `KATTR = (KW := ".unattended.conf")` in its body, read as `ll.KW`: no hit.
  The last two are the liveness negatives: a walrus in a function body binds a local, and one in a class
  body binds a class attribute. Observed by AC1.
- **S4** — The plant proves the group by execution. For each module-scope row it runs the row's
  `loop_lib.py` source with `exec` in a fresh namespace holding only `ROOT = PurePath(".")`, and collects
  every name but `__builtins__` that the row bound and whose `str()` value contains a conf name. Every
  name in that set must be among the names `derive_conf_constants` answers over the row's scratch
  `loop_lib.py`. Each row prints one parity line naming the names the rule missed, or `none`, and a
  missed name is a miss of the case, which then ends `MISSED` and exits 1. A parity line prints only
  from the names `derive_conf_constants` answered, which it reaches through `load_tree_lib`, so where
  that call refuses no parity line prints (§8 F6). The check is one-way on
  purpose: `derive_conf_constants` also answers `g` for the lambda row, since charge rule 2 charges the
  constant to that assignment's target (88 S13), an over-report on the rule's fail-closed side, while a
  name the execution bound and the rule missed is the defect. The rows are the plant's own literals, so
  `exec` reads no input from outside the fixture. Observed by AC1, AC3.
- **S5** — The carriers. The docstring of `derive_conf_rebinds`, which 89 S5 writes, states S1's class
  loader, which reads a `global` in a class body, and the parts S2 reads, naming `_MODULE_SCOPE_PARTS`, a
  decorator, a default argument, a class base and a class keyword. Its `NOT SEEN` clause keeps every
  other form 89 S5 lists, and drops the sub-bullet naming a `global` in a class body and a walrus in a
  default argument, a decorator or a class base. It gains one form, a `type` statement, which binds a type alias whose value is evaluated lazily
  and never a path. The over-match paragraph, which stands before `NOT SEEN` in the landed docstring,
  reads "a function or a class whose subtree" holds a conf name, and stays where it stands: the clause
  opens on forms "each binding a module name of `loop_lib.py` outside both passes", and an over-match is
  the rule's fail-closed over-report, a name the rule answers, so it is no member of that list. The row
  89 S4 writes for `derive_conf_rebinds(tree, docs)` in the table of `tools/loop/README.md`, under "The
  reader, `loop_lib.py`", says a class is a loader too and names the decorator, default and class-base
  positions. Observed by AC4.
  **Readers:**
  by name: `tools/loop/README.md`, whose `derive_conf_rebinds(tree, docs)` row points at the docstring's `NOT SEEN` clause and is edited by this item too
  by value: NO VALUE READERS — no code and no gate parses the docstring or the row; a person reads them, and each `__doc__` read under `tools/loop/` at the tip is a module's own argparse summary

## 3. Non-goals (OUT)

- Charging by scope. The class loader reads the class's whole subtree, as 89 §3 rules for a function,
  and never asks which scope a constant belongs to.
- A walrus in a parameter annotation, a return annotation, a type-parameter bound or default, or the
  value of a `type` statement. Python 3.15.2, the probe's interpreter, refuses each as a `SyntaxError`
  when the module compiles, probed 2026-11-17, and the kit's interpreter floor is 3.15
  (`tools/lib/python-floor.txt`). None of them binds a name in a module that imports, so S2 does not
  descend them (§8 F3).
- The report's left-shift checklist entry, that a binding-form walk enumerates every position evaluated
  in module scope with a plant row each. The class is recorded at the close. S4's execution parity is
  this matcher's guard of that class.
- Coverage outside `tools/loop/loop_lib.py`, as 89 §3 keeps it.
- A rev bump of any sibling spec. 87 and 89 are CLOSED at orders 43 and 44 when this unit builds (§8
  F4), and 92 and 94 are re-grounded before their builders run.

### The rev-2 items the built code or a committed spec settles

Read on branch `unattended-declared-loop-d56bf0` at `9c06b8ef8`.

| Item | What settles it |
|---|---|
| rev-2 S5's 89 half | 89 rev-5 §8 F4 moves its restatements into the carriers the code keeps, its S4 row in `tools/loop/README.md` and its S5 `NOT SEEN` clause in the docstring of `derive_conf_rebinds`. 89 is CLOSED at order 44, so S5 edits those two carriers. |
| rev-2 S5's 87 half | 87 rev-6 §3 holds no binding-form bullet, since 89 rev-5 no longer writes one there. The priced list lives in the docstring, and the `type` statement joins it there (S5). |
| rev-2 AC4 | Its greps read 89's and 87's spec text, frozen once CLOSED, so it could never turn green. AC4 now reads the docstring and the README row. |
| 94 S12 and S13 over this spec | 94 builds at order 48, after this unit is CLOSED, and cannot amend it. Its two items on this spec's own text are written here: AC3's copy holds `tools/memory-tree/`, and its parity line shows `tree_lib` resolved there (§8 F5, F6), and S5's over-match reads "a function or a class whose subtree" (§8 F5). 94's re-ground owns its own text. |

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-89` — `derive_conf_rebinds` as S1 states it, the `conf-read-forms` rows of S3, the README row of S4 and the `NOT SEEN` clause of S5, which this unit extends to every position evaluated in module scope (the round-9 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-87` — S1's binding class, which `derive_conf_constants` answers and S4's parity reads, and the `conf-read-forms` rows of S3, which AC1 keeps answering; the §3 binding-form bullet 87 rev-6 no longer holds is settled in §3's table (the round-9 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-92` — the `NOT SEEN` clause of the docstring of `derive_conf_rebinds` as S5 restates it, the carrier of the priced forms in place of 87 §3's bullet, whose per-form tokens that unit's criterion reads
- **hands-off** `TOOL-dDeclaredLoop-94` — S5, AC3 and AC4, which that unit restated; this revision writes AC3's three-folder copy and S5's class-or-function over-match itself, since this unit is CLOSED before 94 builds (the round-10 spec audit's ids 10, 19, 27)

## 4. Design

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `97ef56324`, through `git show` and a
`git archive` scratch copy of that tip's `tools/`; `tools/loop/` is absent from this worktree's main.

- `tools/loop/loop_lib.py#derive_conf_rebinds` takes a `FunctionDef` or an `AsyncFunctionDef` as a
  global loader and walks its module-level targets from `tree.body`, passing over every `FunctionDef`,
  `AsyncFunctionDef`, `ClassDef` and `Lambda` whole. Its docstring states the two passes, then the
  global-loader over-match in a paragraph of its own, "a function whose subtree holds a conf name
  anywhere", then the `NOT SEEN` clause, whose last form is a `global` in a class body and a walrus in a
  default argument, a decorator or a class base. Its row in `tools/loop/README.md` names a `def` or
  `async def` loader and a module-level walrus, `for` or `with` target, and points at the clause.
- `tools/loop/loop_lib.py#derive_conf_constants` parses the file, calls `load_tree_lib`, and answers the
  rule-2, module-qualified slice of `derive_constant_charges` united with `derive_conf_rebinds`;
  `tools/loop/loop_lib.py#load_tree_lib` raises `LoopError` naming `govkit update --kits memory-tree`
  where `tree_lib` cannot be located, does not import, or lacks a name of `TREE_LIB_SYMBOLS`, the last
  refusal reading `has no <name>`. `tools/memory-tree/gen_build_index.py#scan_glob_readers` states the charge rule:
  rule 1 charges a constant to its innermost function, "its decorators and signature included", rule 2
  answers the targets of an `Assign`, `AnnAssign` or `AugAssign` outside every function, qualified by the
  enclosing classes, and rule 3 the innermost class. The slice keeps names qualified by the module alone,
  so of S3's names it answers only `g`, the lambda row's assignment target.
- A `python -I` probe under Python 3.15.2 executed each shape in a fresh namespace. A class-body
  `global`, a default-argument walrus, a keyword-default walrus, a positional-only default walrus, a
  lambda-default walrus, a class-base walrus, a class-keyword walrus, a decorator walrus and a walrus in
  the default of a function with type parameters each bound a module name. A walrus in a function body
  and one in a class body bound none at module level. `type TA2 = ".unattended.conf"` bound a type
  alias whose `str()` names no conf.
- The same probe found a walrus in a parameter annotation, a return annotation, a type-parameter bound,
  a type-parameter default, a `type` statement's value and the bases of a class with type parameters
  each parsed by `ast.parse` and refused as a `SyntaxError` at compile.
- `tools/lib/python-floor.txt` declares the floor 3.15, which `tools/lib/resolve-python.sh` reads.
- `tools/loop/loop_lib.py#derive_conf_reads` imports `ast` inside the function, and the module-level
  imports of `tools/loop/loop_lib.py` hold no `ast`. S2's table is keyed by class name, so the module
  still loads no `ast`.
- `tools/loop/budget.py#run_budget_plant` prints `held` or `MISSED <why>` for its case, exiting 0, 1, or
  2 where a kit does not resolve; a failed `check` inside it is a miss. `tools/loop/budget.py#run_selftest`
  runs every `PLANTS` case and owes `held`. Its `conf-read-forms` branch writes each row's module beside
  a scratch `loop_lib.py` and checks what `derive_conf_reads` answers, catching no `LoopError` from
  those rows. Its last three rows, 88 S33's unlocatable, blocked and unparseable `tree_lib`, swap the
  route in process, and each prints and owes `govkit update --kits memory-tree`.
- A scratch copy of the tip's `tools/loop/`, `tools/lib/` and `tools/memory-tree/` resolves the
  memory-tree kit from its `loop/` through `tools/loop/loop_lib.py#read_memory_tree`. With
  `_MODULE_SCOPE_PARTS = {}` appended to the copy's `loop_lib.py`, `python budget.py --fixture --plant
  conf-read-forms` in its `loop/` exited 0 printing `held`, and `govkit update --kits memory-tree` on 3
  lines, the three `tree_lib` rows'. A copy without `tools/memory-tree/` exited 1 on a `LoopError`
  traceback before the case printed any row: probed 2026-11-17, PINNED.
- `tools/codebase-map/map_lib.py#python_symbols` captures the module-body `def` and `class` names with
  no leading underscore and the `__all__` names; a table assignment is neither.
- The `CELLS` block of `.lexicon.conf` declares no `py.constant` cell, so no lexicon cell grades a
  module-level table.
- `tools/gate-legs.json` holds `loop budget fixtures`, running `budget.py --selftest` under a ceiling of
  300 seconds PINNED, and `tools/run-gates/selftest-budgets.txt` prices it at 498 seconds PINNED.

### The module-scope walk, after this unit

```
_MODULE_SCOPE_PARTS = {                  # the parts of a definition Python evaluates in module scope
    "FunctionDef":      ("decorator_list", "args.defaults", "args.kw_defaults"),
    "AsyncFunctionDef": ("decorator_list", "args.defaults", "args.kw_defaults"),
    "Lambda":           ("args.defaults", "args.kw_defaults"),
    "ClassDef":         ("decorator_list", "bases", "keywords"),
}

derive_conf_rebinds(tree, docs):                                                    # 89 S1, extended
    for d in every FunctionDef | AsyncFunctionDef | ClassDef in ast.walk(tree):    # S1: classes too
        if holds(d): answer {Global names in ast.walk(d)} & {Store names in ast.walk(d)}
    walk(tree.body)

walk(nodes):                                                   # module scope only
    for n in nodes:
        if n is a FunctionDef | AsyncFunctionDef | Lambda | ClassDef:       # its body is never entered
            walk(the nodes at each path _MODULE_SCOPE_PARTS.get(<class name of n>, ()) names,
                 a None entry passed over)                                   # S2
        else: answer 89 S1's NamedExpr, For and With targets at n; walk(children of n)
```

### The parity half (S4)

```
for each module-scope row of conf-read-forms:
    ns = {"ROOT": PurePath(".")}; exec(<the row's loop_lib.py source>, ns)
    bound  = {k for k, v in ns.items() if k != "__builtins__" and a conf name is in str(v)}
    missed = bound - derive_conf_constants(<the row's scratch loop_lib.py>)
    print("loop: fixture · parity · <row> · missed " + (", ".join(sorted(missed)) or "none"))
    check(not missed, "<row>: the rule missed <missed>, which the execution bound")
```

### The probe file of AC2

The probe writes these bytes; each expected name is DERIVED from them.

```python
from pathlib import PurePath
ROOT = PurePath(".")
class Cfg:
    global CONF_K
    CONF_K = ROOT / ".unattended.conf"
def f(x=(DCONF := ROOT / ".memory-tree.conf")): pass
def fk(*, y=(KWCONF := ROOT / ".unattended.conf")): pass
g = lambda x=(LCONF := ROOT / ".unattended.conf"): x
class KB(type(BCONF := ".memory-tree.conf")): pass
@(lambda fn, _=(DECO := ROOT / ".unattended.conf"): fn)
def h(): pass
def h2(): (HLOCAL := ".unattended.conf")
class K2:
    KATTR = (KW := ".unattended.conf")
class KN(type((lambda x=(NESTED := ".unattended.conf"): x)())): pass
```

A probe of the sketch over these bytes answered exactly `BCONF`, `CONF_K`, `DCONF`, `DECO`, `KWCONF`,
`LCONF` and `NESTED`, the set `exec` of the same bytes bound. With the table emptied it answered `CONF_K`
alone, and the landed `derive_conf_rebinds` answered none: PINNED, 2026-11-17. Over every `*.py` under
the tip's `tools/`, 188 files PINNED at `97ef56324`, the sketch and the landed rule answered the same
names, `_SLOT_DATA_DIR` in `tools/memory-tree/gen_build_index.py` and `_ANCHOR_AT`, `_GRAMMAR` and
`_KIT_CONF` in `tools/memory-tree/merge-rows.py`, and the kit's own `loop_lib.py` answered none.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `_MODULE_SCOPE_PARTS` | private module-level table in `tools/loop/loop_lib.py` | none: no `py.constant` cell is declared |

No function is minted, so the lexicon's suggest verb has no name to grade. The codebase-map symbol tier
captures no assignment, so `memory/map/generated/symbols.json` does not move.

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2 and S5's docstring), `tools/loop/budget.py` (S3, S4)
and `tools/loop/README.md` (S5's row). It writes no spec but this one, and the build README's regions
are the generator's render. The write set meets 90's in `tools/loop/loop_lib.py` and
`tools/loop/budget.py`. The two units share order 45, BUILD-METHOD M6 clause 1 sequences them, and 90
is CLOSED at rev-6 at the tip, so this pass reads its edits as landed.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/README.md`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Pricing the forms as unseen only (the report's alternative).** That leaves a decorator or default
  walrus certified as reading no conf. The rule is fail-closed, so covering them survives M3's vetoes
  and satisfies every criterion the pricing would.
- **Listing the forms the report named as extra node kinds.** That repeats the defect at the next form.
  A table of positions evaluated in module scope is the class, and S4 measures it.
- **Execution parity over the whole `conf-read-forms` plant.** Its global-loader rows bind only when the
  loader is called, and its `with` rows open files. Parity over the module-scope group measures exactly
  the positions this unit adds.
- **Restating the class in the frozen specs of 87 and 89.** A CLOSED spec is frozen (§8 F4).
- **Descending annotations, as rev-2 did.** At the floor no walrus there compiles (§8 F3).

## 5. Production-readiness checklist

- security — closes the route by which a class body, a default, a decorator, a base or a class keyword
  hands a conf path to a loop module that the rule then certifies as reading none. `exec` runs only the
  plant's own literals.
- perf / scale — one more node kind per subtree test and a bounded descent per definition, once per
  rule run; the parity half runs one `exec` of a few lines per row.
- error / empty / loading states — a missing or unparseable `loop_lib.py` keeps 86 S13's named refusal;
  S3's two negatives show the walk does not enter a body.
- observability — each hit keeps its kind, `conf constant`, and names its line; a parity line names
  every missed name.
- risks — a class whose subtree holds a conf name answers every global it rebinds, the fail-closed side
  89 §5 already names for functions. NOT SEEN: a name bound through `globals()` or `setattr`, and the
  forms S5's clause keeps.
- testing — AC1 to AC4 as plant rows, a direct probe and a docstring probe; the arm under §7, observed at
  the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed.
- user docs — `tools/loop/README.md`'s row, S5. `help/loop.md` lists plant names, and S3 adds rows to an
  existing plant, so no help sentence moves.

### The sweep

Read at `97ef56324`; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `derive_conf_rebinds` answers class loaders and module-scope parts (S1, S2) | its one caller `derive_conf_constants` (89 S2, 88 S13), and through it `derive_conf_reads` and the `no-own-conf-read` case of `budget.py` and of `breakpoints.py` over the kit's own modules; 80 S3's staged module and its sibling (86 S15); the `conf-read-forms` rows of 82, 86, 87, 88, 89 and 90; the probe modules of 88 AC13 and 89 AC2 | over the tip's 188 files PINNED the sketch answers what the landed rule answers, and the kit's own `loop_lib.py` none, a probe the pass re-runs over the landed file; no sibling `loop_lib.py` those rows and probes write, as their specs give the bytes, holds a `global` inside a class or a walrus in a default, decorator, base or keyword; 88 AC13's `class K` holds no `global` |
| `_MODULE_SCOPE_PARTS` minted (S2) | `python -c "import loop_lib"` in every loop leg, `loop definition` among them; the codebase-map symbol tier; the lexicon's cells | a literal table of strings, so no import moves at load; `python_symbols` captures no assignment; no `py.constant` cell is declared |
| the module-scope group and parity in `conf-read-forms` (S3, S4) | `run_selftest` of `budget.py` under `loop budget fixtures`, its row of 498 seconds PINNED in `tools/run-gates/selftest-budgets.txt` and its ceiling of 300 seconds PINNED; the `no-own-conf-read` case over `budget.py` itself; the `--plant` choices and the usage anchor of `budget.py` in `help/loop.md` | no `PLANTS` key is added; the rows and the `exec` sit inside the function 80 S1 bounds, so their conf names stay outside the graded population; each row is one parse and one `exec`, milliseconds |
| the docstring and the README row (S5) | their readers; the greps 89 AC4 runs over the docstring; the spec text of 92 and 94 that cites them | `class body`, `default argument` and `subtree` stay in the docstring, in the half before `NOT SEEN`; 92 and 94 are re-grounded before their builders |
| shipped bytes | `install-prefix (shipped surface)` and `kit epoch (shipped bytes move, the version moves)` | the new lines name confs, AST fields and module files, never a kit path; `KIT_LOOP_VERSION` is owed at the lander, as for 89 |
| this spec's citations | `memory/project/positional-refs.txt`, its 1 row PINNED for this spec, `BUILD-METHOD M6`, under `positional (the citation check alone)` | rev-4 keeps that citation in §4 Write set and adds no line citation, citing code by symbol |
| this spec's numbers | 94 cites S1, S5 and AC3 by number, the grep below | every number is kept; 94's re-ground owns its own text |

```
B=branch/unattended-declared-loop-d56bf0
git grep -c -w -e derive_conf_rebinds -e derive_conf_constants -e load_tree_lib "$B" -- tools/loop
    # README.md 6, budget.py 3, kit.toml 1, loop_lib.py 15
git grep -n -w -e _MODULE_SCOPE_PARTS "$B" -- tools help                              # no match
git grep -c -e "conf-read-forms" "$B" -- tools help                                   # budget.py 7
git show "$B:tools/gate-legs.json" | grep -A10 '"loop budget fixtures"'                # ceiling 300
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop budget fixtures'      # 498
git show "$B:tools/govkit/usage.toml" | grep -c 'id = "script:{prefix}/loop/budget.py'  # 6
git show "$B:tools/lib/python-floor.txt"                                              # 3.15
git show "$B:.lexicon.conf" | grep -E '^VERB_OFFENDER_PIN|^  py\.'
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-91.md'   # 1
git grep -o -h -E "91 (S|AC)[0-9]+|91 §[0-9]+" "$B" -- memory/builds/dDeclaredLoop/spec | sort | uniq -c
    # 2 91 AC3, 1 91 S1, 2 91 S5, all in 94's spec
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git show "$B:tools/memory-tree/check-verdict-epoch.sh" | grep -c 'loop/'             # 0
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED; no function is
  minted.
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead.
- The refusal ceilings and families: no `*.sh` is edited, and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` reads tracked `*.sh` files alone. The driver's
  ceiling stays 343 PINNED and `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb or flag is added, so no usage row and no anchor.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added, the
  `DELEGATES` of `tools/memory-tree/check-verdict-epoch.sh` name no loop module, no `[[upgrade]]` row is
  owed, and no file the `watch:` line of `memory/guides/SESSION-KICKOFF.md` names is edited.

### Dependency

Built and CLOSED at the tip, read as they landed: `TOOL-dDeclaredLoop-80` rev-6 (order 38) for
`derive_fixture_boundary` and the row placement; `TOOL-dDeclaredLoop-82` rev-8 (order 41) for the
conf-constant kind, `derive_docstring_ids` and the `conf-read-forms` plant; `TOOL-dDeclaredLoop-86` rev-8
(order 42) for `derive_conf_constants`, the sibling `loop_lib.py` rule and the row placement;
`TOOL-dDeclaredLoop-87` rev-6 (order 43) for the binding walk and its rows; `TOOL-dDeclaredLoop-89` rev-5
(order 44) for `derive_conf_rebinds`, its docstring, its README row, `load_tree_lib` and its rows;
`TOOL-dDeclaredLoop-88` rev-6 (order 44) for the rule-2 slice that `derive_conf_constants` unites with
`derive_conf_rebinds` and S33's three `tree_lib` rows; and `TOOL-dDeclaredLoop-90` rev-6 (order 45) for
`TREE_LIB_SYMBOLS` and its rows, sharing two files with this unit (§4 Write set).
`TOOL-dDeclaredLoop-76` is CLOSED and `derive_conf_reads` is built at the tip.
`TOOL-dDeclaredLoop-92` (order 46) and `TOOL-dDeclaredLoop-94` (order 48) are DEFERRED and build after
it. `TOOL-dDeclaredLoop-34` is DEFERRED and moves no read this unit makes. The probes and the reuse
probe ran in the scratch copy of the tip; the memory-recall query and the spec-token checker ran in
this worktree, cut from main.

## 6. Acceptance criteria

Each `python budget.py` and `python -c` command below runs in the loop kit's folder.

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs, it exits 0 and the case prints
  `held`. Each of its `CONF_K`, `DCONF`, `KWCONF`, `LCONF`, `BCONF` and `DECO` rows answers one
  `conf constant` hit, the `HLOCAL` and `KW` rows answer none, and each module-scope row prints a parity
  line ending `missed none`. Every row an earlier unit planted in the case still answers as its spec
  states.
  Red when: the walk skips a definition whole, so `ll.DCONF` bound by a default walrus reads as no conf
  read.
- **AC2** — When a `python -c` probe writes §4's probe file to a scratch `loop_lib.py`, parses it with
  `ast` and calls `loop_lib.derive_conf_rebinds(tree, set())`, it answers exactly `CONF_K`, `DCONF`,
  `KWCONF`, `LCONF`, `BCONF`, `DECO` and `NESTED`, and none of `HLOCAL` and `KW`. The file holds no
  docstring, so the empty set is its docstring set.
  Red when: the descent does not apply again inside a base, a class is no loader, or a body's local leaks
  into the module set.
  figure: the scratch file is written by the probe, so each expected name is DERIVED from its bytes.
- **AC3** — When `tools/loop/`, `tools/lib/` and `tools/memory-tree/` are copied into a `tools/` folder
  under the run's scratch directory, the line `_MODULE_SCOPE_PARTS = {}` is appended to the
  `loop_lib.py` of the copy's `loop/`, and `python budget.py --fixture --plant conf-read-forms` runs in
  that `loop/`, it exits 1 and prints a parity line naming `DCONF` as missed. That line prints only from
  the names `derive_conf_constants` answered after `load_tree_lib` returned (S4), so it is the
  observation that `tree_lib` resolved in the copy (§8 F6). The three `tree_lib` rows 88 S33 planted
  print `govkit update --kits memory-tree` in the copy as in the uncopied tree, and AC3 reads no line of
  theirs.
  Red when: the parity half compares the walk with itself, so a walk that skips a position still passes,
  or the copy cannot resolve `tree_lib`, so no parity line prints and a bare non-zero exit passes for a
  parity failure.
- **AC4** — When a `python -c` probe splits `loop_lib.derive_conf_rebinds.__doc__` at its first
  `NOT SEEN`, the text before it holds each of `_MODULE_SCOPE_PARTS`, `decorator`, `default argument`,
  `class base`, `class body` and `or a class whose subtree`, the last in the over-match paragraph S5
  keeps where it stands. The text after it holds `type alias`, and none of `decorator`,
  `default argument` and `class base`. When
  `grep "derive_conf_rebinds(tree, docs)"` over the kit's `README.md` is piped to `grep -c "class"` and
  to `grep -c "decorator"`, each prints at least 1.
  Red when: the docstring still prices a covered position as unseen, or names no `type` statement, so a
  reader takes the class as total or the walk as partial.

## 7. Gates

`install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop legs this pass keeps green, built and in the manifest at the tip but outside the base manifest
the line above is joined against: `loop budget fixtures`, which runs `budget.py --selftest`,
`loop breakpoint fixtures` and `loop definition`, the last since it imports `loop_lib`.

New arm: tools/loop/budget.py · covers AC1 AC3 · the module-scope group of conf-read-forms with its execution parity, staged with _MODULE_SCOPE_PARTS emptied · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records; first resolved 2026-10-24.
  RESOLVED (agent, 2026-11-16, delegated): (`**Derived:** PLAY-dClosedLoop-2`).
  widens: none · relaxes: none
- **F2 — Cover the forms, or price them (id 20)?** (a) cover them by position, with a class loader and
  execution parity; (b) name each in the priced list with its reason. The report admits both. (b) leaves
  a default or decorator walrus certified as reading no conf, the finding's consequence. (a) satisfies
  every criterion (b) would and closes the route. First resolved 2026-10-24.
  RESOLVED (agent, 2026-11-16, delegated): (a), S1 to S5.
  widens: none · relaxes: none
- **F3 — Does S2's table hold the annotation positions?** (a) yes, as rev-2 wrote, every argument
  annotation and `returns`; (b) no, only the positions where a walrus compiles. At the kit's floor of
  3.15 a walrus in an annotation is a `SyntaxError`, so (a) answers a name only for a module that never
  imports, a table entry the unit does not use. The round-9 report's own correction lists decorators,
  defaults, bases and keywords alone. Recommendation: (b).
  RESOLVED (agent, 2026-11-16, delegated): (b), S2.
  widens: none · relaxes: none
- **F4 — Where do rev-2's restatements in 87 and 89 go, now that both are CLOSED when this unit
  builds?** (a) rev-bump them at this pass anyway; (b) restate the class in the carriers the code keeps,
  the docstring of `derive_conf_rebinds` and its README row, as 89 §8 F4 does. (a) writes a frozen
  record, which the build method's SPEC-exit rule forbids. (b) puts each fact beside what it describes
  and is read by AC4. Recommendation: (b).
  RESOLVED (agent, 2026-11-16, delegated): (b), S5.
  widens: none · relaxes: none
- **F5 — Who writes 94's items on this spec's own text, AC3's copy and S5's over-match?** (a) 94, as its
  rev-3 plans; (b) this revision. 94 builds at order 48, after this unit is CLOSED, so (a) amends a
  frozen record, and AC3 without `tools/memory-tree/` exits non-zero for a reason that is no parity
  failure. Recommendation: (b).
  RESOLVED (agent, 2026-11-16, delegated): (b), S5 and AC3.
  widens: none · relaxes: none
- **F6 — Which line of AC3's copy run shows that `tree_lib` resolved there?** rev-3's "prints no
  `govkit update --kits memory-tree`" cannot hold: the same case runs 88 S33's three `tree_lib` rows,
  each printing that command and holding only when it does, and AC1 keeps every planted row
  (2026-11-17-build-TOOL-dDeclaredLoop-91-1-builder-return). (a) the parity line itself, which prints
  only from the names `derive_conf_constants` answered after `load_tree_lib` returned; (b) no
  `has no derive_` refusal in the output; (c) the three `tree_lib` rows printing as they do in the
  uncopied tree. (b) holds in a copy that resolved nothing, since an unlocatable kit refuses with
  `looked in`, never `has no`. (c) reads rows that swap the route in process, so the unlocatable and
  unparseable rows print the same with or without a memory-tree kit, and a copy lacking one ends in a
  traceback before any row prints (§4 Evidence). (a) prints only where the route resolved in the copy
  and reads no line a planted row prints. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a), S4 and AC3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-9 spec audit's id 20 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-17 · §1 · S1 to S5 · §3 · §4 · §5 · AC1 to AC4 · §7 · §8 · §10 · re-grounded on
  branch/unattended-declared-loop-d56bf0 at `9c06b8ef8` by the brief
  2026-11-17-prompt-TOOL-dDeclaredLoop-91-1-spec-writer; mechanism, carries, order and status kept. 87 and
  89 are CLOSED when this unit builds (F4): S5 edits the docstring of `derive_conf_rebinds` and its README
  row in place of their specs, and AC4 reads those carriers. S2's table holds no annotation position
  (F3), keyed by class name. S3's rows sit inside the plant's bounded branch. S4 compares with
  `derive_conf_constants` as 88 S13 builds it. AC2 calls the function on a parsed tree. AC3 copies the
  three folders and S5 names the class-or-function over-match, 94's items on this spec (F5). Python is
  3.15.2 and the probes re-ran at the tip; line citations made symbol citations; the sweep.
- rev-4 · 2026-11-17 · §1 · S4 · S5 · §3 · §4 · §5 · AC3 · AC4 · §8 · re-grounded on
  branch/unattended-declared-loop-d56bf0 at `97ef56324` after the builder return
  2026-11-17-build-TOOL-dDeclaredLoop-91-1-builder-return; mechanism, carries, order and status kept.
  AC3 observes `tree_lib` resolved in the copy by its parity line, which S4 prints only from
  `derive_conf_constants`'s answer, in place of an absent update command 88 S33's rows print (F6). S5
  keeps the over-match paragraph before `NOT SEEN`, where it landed, and AC4 reads it there. The units
  rev-3 read on their specs are read as landed; the sweep's figures are re-read: the two greps that
  matched nothing now match, the positional registry holds 1 row, the leg's budget is 498 seconds and
  budget.py's usage rows 6.

## 10. Reuse audit

The seam is 89's `derive_conf_rebinds`, extended in place, and the `conf-read-forms` plant of `budget.py`
that 82 mints and 86 to 90 extend. No second reader of `loop_lib.py` is minted.
`python tools/codebase-map/reuse_lookup.py "walk every expression a def or class evaluates in module scope: decorators, defaults, bases"`,
run in the scratch copy of the tip on 2026-11-17, ranked `walk` (`tools/memory-tree/corpus_ids.py`),
`scope`, `resolve_compare_base`, `ScopeRefused` and `derive_scope`, none a module-scope expression walk,
so no existing seam fits beyond the charge walk 89 §3 declines to duplicate. The memory-recall query
returned 89's spec, 87's spec, this spec, the run record's add row for this unit and the round-9
report's H1.

Recall terms used: derive_conf_rebinds class body global loader walrus default argument lambda decorator class base module scope conf constant
