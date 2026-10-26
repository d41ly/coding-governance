# TOOL-dDeclaredLoop-89 — the conf-constant class covers a module name a global loader rebinds, and module-level walrus, for and with targets

**Status:** DEFERRED · rev-4 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 44 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-89-deviation-891.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-89-deviation-891.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-89-deviation-892.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-89-deviation-892.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-89-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-89-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-90 |

<!-- /gen:spec-records -->

## 1. Goal

The round-8 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md`)
confirmed finding **id 19 at HIGH**, its item **H1**, alone in that item. The report links H1 to item
M1 (ids 1, 9 and 21, MEDIUM), batched into `TOOL-dDeclaredLoop-90`. M1 settles which binding predicate the
slice uses, and this unit adds the binding forms that predicate never reaches.

`TOOL-dDeclaredLoop-87` S1 counts only an `Assign`, an `AnnAssign` or an `AugAssign` that no function and no
class encloses. The repo's lazy-init loader, a module-level `CONF = None` and then
`def load(): global CONF; CONF = HERE.parent / ".unattended.conf"`, falls outside that class. So do
module-level `NamedExpr`, `For` and `With` targets. A loop module reading `ll.CONF` after such a loader
then passes `no-own-conf-read`, certified as reading no conf of its own when it does.
`TOOL-dDeclaredLoop-88` S13's rule-2 slice keeps the gap, because charge rule 1 charges a constant inside a
function to that function and never to the module name it rebinds.

This unit adds the missing binding forms as one pass of `derive_conf_constants`, separate from the rule-2
slice. It names every other way Python binds a module name as a priced non-goal. It builds immediately
after 87 and repairs `TOOL-dDeclaredLoop-87`.

## 2. Scope (IN)

- **S1** — `derive_conf_rebinds(tree, docs)` in `tools/loop/loop_lib.py` answers two sets of module names
  from a parsed `loop_lib.py`.
  - **Global loaders.** Take each `FunctionDef` or `AsyncFunctionDef` at any depth whose subtree holds a str
    `Constant` containing `.memory-tree.conf` or `.unattended.conf`, outside the docstring set `docs`.
    Every name that a `global` statement in that subtree declares, and that a `Name` in a store context in
    that subtree binds, is answered.
  - **Module-level targets.** Take each `NamedExpr`, `For`, `AsyncFor`, `With` or `AsyncWith` reached from
    `tree.body` without entering a `FunctionDef`, `AsyncFunctionDef`, `ClassDef` or `Lambda`. Every `Name`
    in its target is answered when its source expression holds such a constant: a `NamedExpr`'s value, a
    `For`'s iterable, or the context expression of the same `with` item.
  Observed by AC2.
- **S2** — `derive_conf_constants` answers the union of its binding set and `derive_conf_rebinds`' set.
  The binding set is 87 S1's walk, or 88 S13's rule-2 slice once 88 has built. The docstring set is
  `derive_docstring_ids` of `tools/memory-tree/tree_lib.py` (82 S8) over the `loop_lib.py` tree. The
  call reaches it through 86 S21's in-function route, so a `tree_lib` lacking it refuses as 86 S21
  states. Whichever of 88 and this unit builds second writes the union. Observed by AC1, AC2.
- **S3** — The `conf-read-forms` plant of `tools/loop/budget.py` gains seven rows. Each row sits over a
  sibling scratch `loop_lib.py`, as 86 S15 places it, and the rows 86 AC13 and 87 S3 plant are kept:
  - `CONF = None` with `def load(): global CONF; CONF = HERE.parent / ".unattended.conf"`, read as
    `ll.CONF`: one `conf constant` hit;
  - `def read_kit_conf(): global KIT_CONF; with open(ROOT / ".memory-tree.conf") as fh: KIT_CONF = fh.read()`,
    read as `ll.KIT_CONF`: one hit;
  - `if (WCONF := ROOT / ".unattended.conf").exists(): pass`, read as `ll.WCONF`: one hit;
  - `for FCONF in (ROOT / ".memory-tree.conf",): pass`, read as `ll.FCONF`: one hit;
  - `with open(ROOT / ".unattended.conf") as FH: pass`, read as `ll.FH`: one hit;
  - `def reset(): global COUNTER; COUNTER = 0`, read as `ll.COUNTER`: no hit;
  - `def note(): """Reads .unattended.conf."""; global NOTE; NOTE = 1`, read as `ll.NOTE`: no hit.
  The last two rows are the liveness negatives: a global loader with no conf name, and one whose only
  conf name is its docstring. Observed by AC1.
- **S4** — Every sibling spec that describes how `derive_conf_constants` decides membership names the
  second pass, each as a rev bump with its §9 line. The specs are found by grepping the function name
  under `memory/builds/dDeclaredLoop/spec/`:
  - 87 S1, its §4 sketch "The conf-constant kind, after this unit" and its §3 first non-goal;
  - 88 S13 and its §4 sketch "The lifted charge walk (S13)";
  - 86 S13 and its §4 sketch "The conf-constant kind, after this unit";
  - 82 S1's conf-constant kind.
  Each says that `derive_conf_constants` also answers `derive_conf_rebinds`' names, citing this unit's S1.
  Observed by AC3.
- **S5** — 87 §3 gains one non-goal bullet and 87 §5 risks gains one line, in S4's rev bump of 87. The
  §3 bullet prices every other form that binds a module name, each with its reason:
  - an import in `loop_lib.py`, which needs a followed name (87 §8 F2);
  - an `except ... as` name, unbound when its handler ends;
  - a `match` capture pattern, of which `tools/` holds no module-level instance at base;
  - a `def` or `class` name, read through a call (82's `reader call` kind);
  - a name bound through `globals()` or `setattr`, which no parse can see.
  The §5 line names the global-loader rule's over-match: a function whose subtree holds a conf name
  anywhere answers every global it rebinds. Observed by AC4.

## 3. Non-goals (OUT)

- Following a name bound elsewhere, such as `from runlog_lib import CONF_NAME` in `loop_lib.py`, or
  `CONF = ROOT / CONF_NAME`. 87 §8 F2 keeps the class to constants written in the binding's own source,
  and this unit does not reopen that fork.
- Charging by scope. The global-loader rule reads a function's whole subtree, nested definitions
  included, and never asks which function a constant belongs to. That question is charge rule 1's, and
  88 S13 lifts it into `tree_lib`. A scope-exact test would be a second walk answering rule 1's question.
- Coverage outside `loop_lib.py`. The kind stays 82 S1's: names `loop_lib.py` binds and other loop modules
  read.
- The report's left-shift, a checklist entry that a class over binding statements names every way the
  language binds a module name. The class is recorded at the close, and S5's bullet is that list for
  this matcher.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-87` — `derive_conf_constants` as S1 states it and the `conf-read-forms` rows of S3, to which this unit adds the global-loader and module-level target pass (the round-8 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S13's sibling `loop_lib.py` rule, S15's scratch placement and S21's in-function route to `tree_lib`, through which the pass reads the docstring set
- **consumes-from** `TOOL-dDeclaredLoop-82` — S1's conf-constant kind, which S4 extends to the pass, and S8's `derive_docstring_ids`
- **hands-off** `TOOL-dDeclaredLoop-88` — `derive_conf_rebinds`, which S13's `derive_conf_constants` unites with its rule-2 slice where 88 builds after this unit
- **hands-off** `TOOL-dDeclaredLoop-90` — `derive_conf_rebinds`' sentences in 87 S1 and 86 S13, which that unit's restatements keep, and its `tree_lib` call, which that unit's refusal class covers
- **hands-off** `TOOL-dDeclaredLoop-91` — `derive_conf_rebinds` as S1 states it, S3's `conf-read-forms` rows and S5's priced list, which that unit extends to every position evaluated in module scope (the round-9 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-92` — S3's `with`-held row, S4's restatement sites and AC3 and AC4, which that unit restates (the round-9 spec audit's ids 8, 16, 21)
- **hands-off** `TOOL-dDeclaredLoop-94` — the sketch "The conf-constant class, after this unit", §3's charging-by-scope bullet and §5 risks, which that unit restates to `load_tree_lib` and 91's class-body loader (the round-10 spec audit's ids 19, 24, 27)
- **hands-off** `TOOL-dDeclaredLoop-99` — S5's sub-bullet on a `def` or `class` name read through a call, which that unit restates onto `CONF_READERS` (the round-12 spec audit's id 19)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 87 S1 counts an `Assign`, an `AnnAssign` with a value or an `AugAssign` that no function and no class
  encloses, and its §3 prices only a conf path "read through a call"
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-87.md`, §2 S1, §3).
- Charge rule 1 charges a constant inside a function to that function, and rule 2 answers only the targets
  of an `Assign`, `AnnAssign` or `AugAssign` outside every function (`scan_scope` in
  `tools/memory-tree/gen_build_index.py:5167-5186`).
- `merge-rows.py`'s `read_kit_conf` is the idiom: module-level `_KIT_CONF = None` (line 278), then
  `global _KIT_CONF`, `with open(root / ".memory-tree.conf", ...)` and `_KIT_CONF = conf` in the function
  (`tools/memory-tree/merge-rows.py:300-323`). The conf name is in the `with`, not in the rebinding's value.
  S3's second row plants that shape.
- A probe of every `*.py` under `tools/` counted 21 functions holding a `global` statement. Three of
  their subtrees hold a conf name: `read_kit_conf` and `anchors` in `merge-rows.py`, and `cmd_selftest`
  in `gen_build_index.py`. `anchors` names the conf only in its docstring and a comment. `cmd_selftest`
  holds it only in nested functions. The same probe counted module-level `For` 64 times, `With` 28 times,
  `NamedExpr` once, `ExceptHandler` 32 times and `Match` 0 times.
- `tools/loop/` is absent at base, so `derive_conf_constants` and `budget.py` are sibling-minted, by 86 S13
  and 87 S1.

### The conf-constant class, after this unit

```
derive_conf_constants(loop_lib_path):
    tree  = ast.parse(read(loop_lib_path))          # missing or unparseable -> 86 S13's refusal
    tl    = 86 S21's in-function tree_lib route     # lacking a symbol -> its named refusal
    docs  = tl.derive_docstring_ids(tree)
    return binding_set(tree) | derive_conf_rebinds(tree, docs)    # binding_set: 87 S1, or 88 S13's slice

derive_conf_rebinds(tree, docs):
    holds(e) = any str Constant in ast.walk(e), outside docs, containing a conf name
    for f in every FunctionDef | AsyncFunctionDef in ast.walk(tree):
        if holds(f):
            answer {names of Global nodes in ast.walk(f)} & {Name.id, ctx Store, in ast.walk(f)}
    for n reached from tree.body, never entering FunctionDef | AsyncFunctionDef | ClassDef | Lambda:
        NamedExpr          and holds(n.value)                 -> answer n.target.id
        For | AsyncFor     and holds(n.iter)                  -> answer every Name in n.target
        With | AsyncWith:  each item with holds(item.context_expr) -> every Name in item.optional_vars
```

### Inventory

- `derive_conf_rebinds(tree, docs)`, a public function of `tools/loop/loop_lib.py`. It is a module-level
  `def`, so the codebase-map symbol tier gains a row and this pass regenerates
  `memory/map/generated/symbols.json` once.

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2), `tools/loop/budget.py` (S3) and
`memory/map/generated/symbols.json`. Inside this build's folder it amends the specs of 82, 86, 87 and 88 as
rev bumps, one per spec, each with its §9 line. The build README's regions are the generator's render.
The write set meets 88's in `loop_lib.py`, `budget.py`, `symbols.json` and the 82, 86 and 87 specs. The
two units share order 44, and BUILD-METHOD M6 clause 1 sequences them; S2 reads the same whichever
builds first.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `memory/map/generated/symbols.json`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Pricing the forms as non-goals only (the skeptic's first option).** That leaves the global loader, the
  repo's lazy-init idiom, certifying a conf read as none. The rule is fail-closed, so the more complete
  option survives M3's vetoes.
- **Adding the forms to 88's rule-2 slice.** Rule 2 answers targets of three statement kinds outside every
  function. A rebinding under `global` sits inside one. Widening rule 2 would move `scan_glob_readers`'
  answer for the `:(glob)` needle too, which TOOL-dTrueNorth-23's AC5 arm grades.
- **Reading charge rule 1's owners from `tree_lib.derive_constant_charges` for the loader test.** That
  symbol is minted by 88, which shares this unit's order, so the pass would depend on a unit the dispatch
  may run after it. The subtree test needs no scope tracking and answers the loader idiom S3 plants.

## 5. Production-readiness checklist

- security — closes the route by which a global loader or a module-level target hands a conf path to a
  loop module that the rule then certifies as reading none.
- perf / scale — one `ast.walk` per function and one module-scope walk of one file, once per rule run.
- error / empty / loading states — a missing or unparseable `loop_lib.py` keeps 86 S13's named refusal; a
  `tree_lib` lacking `derive_docstring_ids` keeps 86 S21's; S3's two negatives show the set is not every
  global.
- observability — each hit keeps its kind, `conf constant`, and names its line.
- risks — the global-loader rule reads a whole subtree, so a function holding a conf name anywhere,
  nested functions included, answers every global it rebinds. That is over-reporting, the rule's
  fail-closed side. NOT SEEN: a name bound through `globals()` or `setattr`, and a conf name composed
  from pieces.
- testing — AC1 to AC4 as plant rows, a direct probe and greps; the arm under §7, observed at the close.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, each of its
  global-loader, `with`-held-loader, walrus, `for`-target and `with`-target rows answers one
  `conf constant` hit. Its `COUNTER` and `NOTE` rows answer none, and every row 86 AC13 and 87 AC1 name
  still answers as they state.
  Red when: `derive_conf_constants` answers only the binding set, so a loop module reading `ll.CONF` after
  `def load(): global CONF; CONF = ...` reads as no conf read.
- **AC2** — When a `python -c` probe imports `loop_lib` from `tools/loop/` and calls
  `derive_conf_constants` on a scratch `loop_lib.py` written by the probe, it answers exactly the expected
  set. The file holds the five hit shapes of S3 under distinct names `CONF_G`, `KIT_CONF`, `WCONF`, `FCONF`
  and `FH`, the two negatives `COUNTER` and `NOTE`, and three more. `def peek(): global PEEK; return ".unattended.conf"`
  declares a global it never binds. `def outer(): LOCAL = ".unattended.conf"` binds a local. `PLAIN = ".memory-tree.conf"`
  is an ordinary binding. The answer holds `CONF_G`, `KIT_CONF`, `WCONF`, `FCONF`, `FH` and `PLAIN`, and
  none of `COUNTER`, `NOTE`, `PEEK` and `LOCAL`.
  Red when: a docstring counts as a conf name, a declared but unbound global is answered, a function local
  leaks into the module set, or the union drops the binding set.
  figure: the scratch file is written by the probe, so each expected name is DERIVED from its bytes.
- **AC3** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over the 87 spec, `awk '/^- \*\*S13\*\*/,/^- \*\*S14\*\*/'`
  over the 88 and 86 specs, and `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over the 82 spec are each piped to
  `grep -c "derive_conf_rebinds"`, each prints at least 1. Run the same way, the ranges
  `awk '/^### The conf-constant kind, after this unit/,/^### Files touched/'` over 87,
  `awk '/^### The lifted charge walk/,/^### Evidence/'` over 88 and
  `awk '/^### The conf-constant kind/,/^### Evidence/'` over 86 each print at least 1. The specs sit under
  `memory/builds/dDeclaredLoop/spec/`, and each prints 0 at HEAD.
  Red when: a sibling spec still describes `derive_conf_constants` by the binding set alone beside code
  that answers the union.
- **AC4** — When `awk '/^## 3/,/^### Edges/'` over the 87 spec is piped to
  `grep -c "except\|capture pattern\|globals()"`, it prints at least 1. When `awk '/^## 5/,/^## 6/'` over
  it is piped to `grep -c "subtree"`, it prints at least 1.
  Red when: a binding form is neither in the class nor priced, so a reader takes the class as total.
  figure: both greps print 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted leg this pass keeps green, outside the base manifest and declared by the unit that
mints it: `loop budget fixtures`, which runs `budget.py --fixture`; it is no leg at HEAD.

New arm: tools/loop/budget.py · covers AC1 · the global-loader, with-held loader, walrus, for-target and with-target rows with the plain-global and docstring-only negatives, staged with derive_conf_rebinds answering the empty set · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Price the forms as non-goals, or cover them (id 19)?** (a) name a module name rebound under
  `global` and module-level walrus, `for` and `with` targets as 87 §3 non-goals, priced in §5; (b) cover
  them as a pass separate from the rule-2 slice and price the rest. The report's correction admits both.
  (a) leaves the repo's lazy-init loader certified as reading no conf, the finding's consequence, and the
  rule's fail-closed purpose rules it out. (b) satisfies every criterion (a) would and closes the route.
  RESOLVED (agent, 2026-10-24, delegated): (b), S1 to S5. widens: none · relaxes: none
- **F3 — How does the loader test decide that a function reads a conf?** (a) the function's whole subtree
  holds a conf name outside docstrings; (b) charge rule 1's owner is the function, read from 88's
  `derive_constant_charges`; (c) a scope-exact walk of this unit's own. (b) depends on a symbol minted by
  a unit sharing this order. (c) answers rule 1's question with a second walk, the two-walks defect 88 §8
  F4 removes. (a) answers S3's rows and over-reports only on the fail-closed side. RESOLVED (agent,
  2026-10-24, delegated): (a), S1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-8 spec audit's id 19 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-91 and TOOL-dDeclaredLoop-92, written by the round-9 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-99, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is `derive_conf_constants`, which 86 minted, 87 restated and 88 slices. This unit unites one pass
into it, and no second reader of `loop_lib.py` is minted. The docstring set is `tree_lib`'s
`derive_docstring_ids` (82 S8), reached by 86 S21's route.
`python tools/codebase-map/reuse_lookup.py "find module names a function rebinds through a global statement"`
ranked `read_host_name`, `module_inventory`, `build_baseline_findings` and `find_block`, none a binding walk, so no
existing seam fits the rebinding test beyond the charge walk §3 declines to duplicate. The memory-recall
query returned 87's own spec, the round-8 report's H1 and 88's lifted-walk sketch.

Recall terms used: conf constant derive_conf_constants global loader module-level binding walrus for with target charge rule
