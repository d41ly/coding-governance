# TOOL-dDeclaredLoop-91 — derive_conf_rebinds reads every position a module evaluates: class bodies, defaults, decorators and bases

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 45 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-91-deviation-911.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-91-deviation-911.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-9 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-89-spec-audit.md`)
confirmed finding **id 20 at HIGH**, its item **H1**, alone in that item.

`TOOL-dDeclaredLoop-89` S1 takes only a `FunctionDef` or an `AsyncFunctionDef` as a global loader, and its
module-level walk never enters a `FunctionDef`, `AsyncFunctionDef`, `ClassDef` or `Lambda`. Python
evaluates parts of those nodes in module scope all the same: a class body, a default argument, a
decorator and a class base. A `global` in a class body and a walrus in any of those positions bind a
module name that neither pass answers. A loop module reading `ll.CONF` bound that way passes
`no-own-conf-read`, certified as reading no conf of its own, and 89 S5's priced list would claim a class
that is not total.

This unit states the module-scope walk by POSITION rather than by node kind, admits a class body as a
loader, and proves the class with a plant that executes each row and compares the names the execution
bound with the names the walk answers. It builds immediately after 89 and repairs
`TOOL-dDeclaredLoop-89`.

## 2. Scope (IN)

- **S1** — `derive_conf_rebinds` in `tools/loop/loop_lib.py` takes a `ClassDef` at any depth as a loader,
  as it takes a function. A class whose subtree holds a str `Constant` containing `.memory-tree.conf` or
  `.unattended.conf`, outside the docstring set, answers every name that a `global` in that subtree
  declares and that a `Name` in a store context there binds. Observed by AC1, AC2.
- **S2** — The module-level walk of `derive_conf_rebinds` still never enters a body that runs in its own
  scope, and it now descends every part of a definition that runs in module scope:
  - a `FunctionDef` or `AsyncFunctionDef`: `decorator_list`, `args.defaults`, `args.kw_defaults`, every
    argument annotation and `returns`;
  - a `Lambda`: `args.defaults` and `args.kw_defaults`;
  - a `ClassDef`: `decorator_list`, `bases` and `keywords`.
  The descent applies again to every definition it reaches, so a lambda default inside a class base is
  read. Each `NamedExpr` reached this way answers its target when its value holds such a constant, as 89
  S1 states for a module-level `NamedExpr`. The positions sit in one private table of the module,
  `_MODULE_SCOPE_PARTS`, and a definition kind the table does not name is still not entered, so a
  position added later is one row and an emptied table reads no part at all. Observed by AC1, AC2.
- **S3** — The `conf-read-forms` plant of `tools/loop/budget.py` gains a module-scope group of eight rows,
  each over a sibling scratch `loop_lib.py` as 89 S3 places its rows, each row written across lines:
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
- **S4** — The plant proves the group by execution. It runs each module-scope row with `exec` in a fresh
  namespace that holds only `ROOT = PurePath(".")`, and collects the names the row bound whose `str()`
  value contains a conf name. Every name in that set must be among the names `derive_conf_constants`
  answers over the same row, or the row fails naming the names the walk missed. The check is one-way on
  purpose: the binding set also answers `g` for the lambda row, an over-report on the rule's fail-closed
  side, while a name the execution bound and the walk missed is the defect. The rows are the plant's own
  literals, so `exec` reads no input from outside the fixture. Observed by AC1, AC3.
- **S5** — 89 S1, 89 S5 and the 87 §3 bullet that 89 S5 writes state the positions S2 lists, in this unit's
  rev bumps of 89 and 87. That bullet's priced list keeps 89 S5's five forms and gains one: a `type`
  statement, whose value is evaluated lazily and binds a type alias rather than a path. Observed by AC4.

## 3. Non-goals (OUT)

- Charging by scope. The class-body loader reads the class's whole subtree, as 89 §3 rules for a
  function, and never asks which scope a constant belongs to.
- A walrus in an annotation or a type parameter bound. Python 3.14.5, this node's interpreter, refuses
  both as a `SyntaxError`, probed 2026-10-24. S2 descends annotations anyway, because the class is stated
  by position and the position costs nothing.
- The report's left-shift checklist entry, that a binding-form walk enumerates every position evaluated
  in module scope with a plant row each. The class is recorded at the close. S4's execution parity is
  this matcher's guard of that class.
- Coverage outside `tools/loop/loop_lib.py`, as 89 §3 keeps it.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-89` — `derive_conf_rebinds` as S1 states it, the `conf-read-forms` rows of S3 and S5's priced list, which this unit extends to every position evaluated in module scope (the round-9 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-87` — §3's binding-form bullet, which 89 S5 writes and S5 restates to the positions (the round-9 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-92` — 87 §3's binding-form bullet as S5 restates it, whose per-form tokens that unit's criterion reads
- **hands-off** `TOOL-dDeclaredLoop-94` — S5, AC3 and AC4, which that unit restates: AC3's scratch copy gains `tools/memory-tree/` and AC4 the greps over 89 and 87 (the round-10 spec audit's ids 10, 19, 27)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 89 S1 takes `FunctionDef` and `AsyncFunctionDef` as loaders, and its walk skips `FunctionDef`,
  `AsyncFunctionDef`, `ClassDef` and `Lambda` whole
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md`, §2 S1 and the sketch
  "The conf-constant class, after this unit").
- A `python -I` probe executed a class-body `global`, a default-argument walrus, a keyword-default walrus,
  a lambda-default walrus, a class-base walrus and a decorator walrus under Python 3.14.5. All six bound
  module names. A walrus in a function body and one in a class body bound none at module level.
- The same probe compiled a walrus in a parameter annotation, in a return annotation and in a type
  parameter bound. Each raised `SyntaxError`.
- Charge rule 1 in `scan_scope` recurses into a whole `FunctionDef` with the function as owner, its
  decorators and defaults included, and a `ClassDef` with the class as owner
  (`tools/memory-tree/gen_build_index.py:5174-5179`). 88's rule-2 slice therefore answers none of these
  module names.
- `tools/loop/` is absent at base, so `derive_conf_rebinds` and `budget.py` are sibling-minted, by 89 S1
  and 86 S13.

### The module-scope walk, after this unit

```
_MODULE_SCOPE_PARTS = {                       # the parts of a definition Python runs in module scope
    FunctionDef | AsyncFunctionDef: (decorator_list, args.defaults, args.kw_defaults,
                                     every arg annotation, returns),
    Lambda:                          (args.defaults, args.kw_defaults),
    ClassDef:                        (decorator_list, bases, keywords),
}

derive_conf_rebinds(tree, docs):
    for d in every FunctionDef | AsyncFunctionDef | ClassDef in ast.walk(tree):      # S1: classes too
        if holds(d): answer {Global names in ast.walk(d)} & {Store names in ast.walk(d)}
    walk(tree.body)

walk(nodes):                                  # module scope only
    for n in nodes:
        if n is a FunctionDef | AsyncFunctionDef | Lambda | ClassDef:    # 89 S1's four kinds, still never entered
            walk(_MODULE_SCOPE_PARTS.get(kind of n, ()))                 # S2: only the parts the table names
        else: answer 89 S1's NamedExpr, For and With targets at n; walk(children of n)
```

### Inventory

- `_MODULE_SCOPE_PARTS`, a private module-level table of `tools/loop/loop_lib.py`. Its name starts with
  an underscore, so the codebase-map symbol tier skips it (`tools/codebase-map/map_lib.py:351`).

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2) and `tools/loop/budget.py` (S3, S4). Inside this build's
folder it amends the specs of 87 and 89 as rev bumps, one per spec, each with its §9 line. The build
README's regions are the generator's render. The pass mints no public module-level `def`, so
`memory/map/generated/symbols.json` does not move. The write set meets 90's in `loop_lib.py`, `budget.py`
and the 87 spec. The two units share order 45, and BUILD-METHOD M6 clause 1 sequences them.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Pricing the three forms as 87 §3 non-goals (the report's alternative).** That leaves a decorator or
  default walrus certified as reading no conf. The rule is fail-closed, so covering them survives M3's
  vetoes and satisfies every criterion the pricing would.
- **Listing the three forms the report named as extra node kinds.** That repeats the defect at the next
  form. A table of positions evaluated in module scope is the class, and S4 measures it.
- **Execution parity over the whole `conf-read-forms` plant.** Its global-loader rows bind only when the
  loader is called, and its `with` rows open files. Parity over the module-scope group measures exactly
  the positions this unit adds.

## 5. Production-readiness checklist

- security — closes the route by which a class body, a default, a decorator or a base hands a conf path to
  a loop module that the rule then certifies as reading none. `exec` runs only the plant's own literals.
- perf / scale — one more node kind per subtree test and a bounded descent per definition, once per run.
- error / empty / loading states — a missing or unparseable `loop_lib.py` keeps 86 S13's named refusal; S3's
  two negatives show the walk does not enter a body.
- observability — each hit keeps its kind, `conf constant`, and names its line; a parity failure names
  both sets.
- risks — a class whose subtree holds a conf name answers every global it rebinds, the fail-closed side 89
  §5 already names for functions. NOT SEEN: a name bound through `globals()` or `setattr`.
- testing — AC1 to AC4 as plant rows, a direct probe and greps; the arm under §7, observed at the close.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, it exits 0. Each
  of its `CONF_K`, `DCONF`, `KWCONF`, `LCONF`, `BCONF` and `DECO` rows answers one `conf constant` hit, the
  `HLOCAL` and `KW` rows answer none, and each module-scope row prints its execution parity with no
  missed name.
  Every row 86 AC13, 87 AC1 and 89 AC1 name still answers as they state.
  Red when: the walk skips a definition whole, so `ll.DCONF` bound by a default walrus reads as no conf read.
- **AC2** — When a `python -c` probe imports `loop_lib` from `tools/loop/` and calls `derive_conf_rebinds` on a
  scratch `loop_lib.py` written by the probe, it answers exactly `CONF_K`, `DCONF`, `KWCONF`, `LCONF`,
  `BCONF`, `DECO` and `NESTED`, and none of `HLOCAL` and `KW`. The file holds S3's eight shapes and
  `class KN(type((lambda x=(NESTED := ".unattended.conf"): x)())): pass`.
  Red when: the descent does not apply again inside a base, or a body's local leaks into the module set.
  figure: the scratch file is written by the probe, so each expected name is DERIVED from its bytes.
- **AC3** — When a scratch copy of `tools/loop/` under the run's scratch directory has `_MODULE_SCOPE_PARTS`
  emptied, `python budget.py --fixture --plant conf-read-forms` in that copy exits non-zero and prints a
  parity failure naming `DCONF` as missed.
  Red when: the parity half compares the walk with itself, so a walk that skips a position still passes.
- **AC4** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` and `awk '/^- \*\*S5\*\*/,/^## 3/'` over the 89 spec are
  each piped to `grep -c "decorator"`, each prints at least 1. When `awk '/^## 3/,/^### Edges/'` over the 87
  spec is piped to `grep -c "decorator"` and to `grep -c "type. statement"`, each prints at least 1. The
  specs sit under `memory/builds/dDeclaredLoop/spec/`.
  Red when: 87 §3 still claims a total list beside a walk that reads more positions.
  figure: each grep prints 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted leg this pass keeps green, outside the base manifest and declared by the unit that
mints it: `loop budget fixtures`, which runs `budget.py --fixture`; it is no leg at HEAD. The codebase-map
leg is listed because it is the one that reds if a public name slips into `loop_lib.py`.

New arm: tools/loop/budget.py · covers AC1 AC3 · the module-scope group of conf-read-forms with its execution parity, staged with _MODULE_SCOPE_PARTS emptied · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Cover the three forms, or price them (id 20)?** (a) cover them by position, with a class-body
  loader and execution parity; (b) name each in 87 §3 with its reason. The report admits both. (b) leaves
  a default or decorator walrus certified as reading no conf, the finding's consequence. (a) satisfies
  every criterion (b) would and closes the route. RESOLVED (agent, 2026-10-24, delegated): (a), S1 to S5.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-9 spec audit's id 20 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 89's `derive_conf_rebinds`, extended in place, and the `conf-read-forms` plant of `budget.py`
that 86 minted and 87 and 89 extend. No second reader of `loop_lib.py` is minted.
`python tools/codebase-map/reuse_lookup.py "walk every expression a def or class evaluates in module scope: decorators, defaults, bases"`
ranked `scope`, `walk` (`tools/memory-tree/corpus_ids.py`), `ScopeRefused` and `derive_scope`, none a
module-scope expression walk, so no existing seam fits beyond the charge walk 89 §3 declines to
duplicate. The memory-recall query returned 89's spec, the round-9 report's H1 and 87's spec.

Recall terms used: derive_conf_rebinds global loader class body walrus default argument lambda decorator base module scope conf constant
