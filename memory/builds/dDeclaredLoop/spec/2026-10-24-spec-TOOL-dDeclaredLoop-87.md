# TOOL-dDeclaredLoop-87 — the conf-constant kind is stated as a class: any module-level binding whose value holds a conf name, and every import that binds it

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 43 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-87-deviation-871.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-87-deviation-871.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-7 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md`)
confirmed finding **id 29 at HIGH**, its item **H1**, alone in that item. The report pairs it with item
M10, id 17, a MEDIUM batched into `TOOL-dDeclaredLoop-88`, which lifts the walk this unit's class is
graded by.

`TOOL-dDeclaredLoop-86` S13 defines `derive_conf_constants` by listing value shapes one by one: a str
`Constant`, a `JoinedStr`, a `BinOp` of strings, and a `Path(...)` or `PurePath(...)` call over one of
those. The repo binds a conf path mostly as `root / ".memory-tree.conf"` and
`os.path.join(root, ".memory-tree.conf")`, a `BinOp` with a non-str operand and a call the list does not
name. A `loop_lib.py` binding `CONF = HERE.parent / ".unattended.conf"` is then no `conf constant`, and a
loop module reading `ll.CONF` is certified as reading no conf of its own. 86 AC13 plants only the listed
shapes, so it stays green.

This unit states the class instead of its instances, plants the repo's dominant idioms, and makes an
aliased from-import a named, observed route. It builds immediately after 86 and repairs
`TOOL-dDeclaredLoop-86`.

## 2. Scope (IN)

- **S1** — `derive_conf_constants(loop_lib_path)` in `tools/loop/loop_lib.py` answers every name bound
  by an `Assign`, an `AnnAssign` with a value, or an `AugAssign` of that file that no function and no
  class encloses, a binding under a module-level `if`, `try` or `with` included, whose value expression
  holds anywhere in its syntax subtree a str `Constant` that contains `.memory-tree.conf` or
  `.unattended.conf`. A `JoinedStr`'s literal parts are such constants. Every `Name` in the binding's
  targets is answered, a tuple target included. The value's shape is never tested, so a `BinOp` of any
  operands, any call and any argument count are inside the class. Observed by AC1, AC2.
- **S2** — A name `derive_conf_reads` reaches through `from loop_lib import <name> as <alias>` counts the
  alias as the bound name, through 82 S10's `derive_import_aliases`, beside `import loop_lib as <alias>`,
  the plain from-import and 86 S13's star import. Observed by AC1.
- **S3** — The `conf-read-forms` plant of `tools/loop/budget.py` gains five rows, each over a sibling
  scratch `loop_lib.py` as 86 S15 places it, and keeps 86 AC13's three:
  - `CONF = ROOT / ".unattended.conf"`, read as `ll.CONF`: one `conf constant` hit;
  - `CONF = os.path.join(ROOT, ".memory-tree.conf")`, read as `ll.CONF`: one hit;
  - `CONF = Path(ROOT, "cfg", ".unattended.conf")`, read as `ll.CONF`: one hit;
  - `from loop_lib import CONF as C`, read as `C`: one hit;
  - `OTHER = ROOT / "other.toml"`, read as `ll.OTHER`: no hit.
  The last row is the plant's liveness negative. Observed by AC1.
- **S4** — 86 S13, its §4 sketch "The conf-constant kind, after this unit" and 86 AC13 are restated to
  S1's class and S3's rows, as a rev bump of 86 with its §9 line. 82 S1's "bound at module level in
  `tools/loop/loop_lib.py` to a string constant naming a conf" reads "to a value whose syntax subtree
  holds a string constant naming a conf", as a rev bump of 82 with its §9 line. Observed by AC3.

## 3. Non-goals (OUT)

- Where the walk lives: id 17 lifts `scan_glob_readers`' charge walk into `tools/memory-tree/tree_lib.py`
  and makes `derive_conf_constants` its module-level slice, a scope item of `TOOL-dDeclaredLoop-88`. S1's
  class is charge rule 2's own predicate restricted to module level, so the lift moves no answer AC2
  reads.
- A binding whose value holds no conf-name constant and names another member, such as
  `CONF = ROOT / CONF_NAME`. Charge rule 2 does not follow names either, and a grep of `tools/` for a
  module-level binding that composes a conf-name constant bound elsewhere found none. Following names is
  a second rule with no instance to plant.
- A conf path a function builds and returns, read through a call: 82's `reader call` kind is the route
  for a call, and S1 counts bindings only.
- The report's left-shift, a checklist entry that a syntactic matcher states its class and plants the
  repo's dominant idiom: the class is recorded at the close, and S3's rows are this matcher's fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-86` — `derive_conf_constants`, the sibling `loop_lib.py` rule and the `conf-read-forms` rows of S13, S15 and AC13, which this unit restates from a shape list to the class (the round-7 spec audit's id 29)
- **consumes-from** `TOOL-dDeclaredLoop-82` — S1's conf-constant kind and S10's `derive_import_aliases`, through which an aliased from-import binds a member
- **hands-off** `TOOL-dDeclaredLoop-88` — `derive_conf_constants` as S1 states it, which that unit re-implements as the module-level slice of the lifted charge walk, with AC2's answer unchanged (the round-7 spec audit's id 17)

## 4. Design

### Evidence

Read 2026-10-24 at the worktree tip.

- 86 S13 and its §4 sketch list the value shapes `Constant str | JoinedStr | BinOp of str |
  Path(<one of these>) | PurePath(<one of these>)`, and 86 AC13 plants a `Path(".unattended.conf")`
  binding, an annotated `CONF: str = ".memory-tree.conf"` and a star import
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md`, §2 S13, §4, §6 AC13).
- 82 S1 already names `from loop_lib import <name>` "or either aliased" as a route, and 82 S10 mints
  `derive_import_aliases(tree)`; 86 S13 and AC13 name only the star import
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md`, §2 S1, S10).
- A grep of `tools/` for conf-name string constants found the joins `pathlib.Path(top) / ".memory-tree.conf"`
  (`tools/branch-reconcile/branch_reconcile.py:418`), `root / ".memory-tree.conf"`
  (`tools/check-spec-tokens.py:724`) and `os.path.join(root, ".memory-tree.conf")`
  (`tools/memory-tree/corpus_ids.py:169`, `tools/memory-tree/check-arms.py:180`), and the module-level
  `CONF_NAME = ".memory-tree.conf"` (`tools/runlog/runlog_lib.py:42`). None is under `tools/loop/`, which
  is unbuilt at base; these are the idioms a loop_lib author copies.
- Charge rule 2 of `scan_glob_readers` charges a needle constant to every `Name` in the targets of the
  innermost enclosing module-level `Assign`, `AnnAssign` or `AugAssign`, at any depth below it
  (`tools/memory-tree/gen_build_index.py:5146`, `scan_scope` at :5167-5186).

### The conf-constant kind, after this unit

```
derive_conf_constants(loop_lib_path):
    tree = ast.parse(read(loop_lib_path))         # missing or unparseable -> 86 S13's refusal, unchanged
    for each Assign | AugAssign | AnnAssign-with-value reached from tree.body
            without entering a FunctionDef, AsyncFunctionDef or ClassDef:    # if, try, with descended
        if any node in ast.walk(binding.value) is a str Constant containing a conf name:
            answer every Name in its targets
derive_conf_reads(path):
    ... 86's walk, unchanged; a local name maps through derive_import_aliases before the member test
```

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

The pass changes the body of a function 86 adds and mints no module-level symbol, so
`memory/map/generated/symbols.json` does not move. The build README's regions are the generator's render.

### Alternatives rejected

- **Adding the three missing shapes to S13's list.** It closes the planted cases and leaves the next
  idiom out, the defect itself; the report's fix and its left-shift both ask for the class.
- **Folding the walk lift into this unit.** S1 is the predicate, the lift is where its code lives, and M2
  makes them two mechanisms; the report grades them as two findings, and id 17 is batched.
- **Importing `loop_lib` and reading its values.** 82 S1 reads the bindings by parsing, never by
  importing, so a module with an import-time effect is never run by the rule.

## 5. Production-readiness checklist

- security — closes the route by which the no-own-conf-read rule certifies a module that reads its conf
  through a joined path constant.
- perf / scale — one `ast.walk` per module-level binding of one file, once per rule run.
- error / empty / loading states — a missing or unparseable `loop_lib.py` keeps 86 S13's named refusal;
  S3's negative row shows the set is not every name.
- observability — each hit keeps its kind, `conf constant`, and names its line.
- risks — a module-level name whose value merely mentions a conf name in another sense, such as a message
  string, now counts as a member; a read of it outside the fixture boundary is reported, never skipped,
  which is the rule's fail-closed side.
- testing — AC1 to AC3 as plant rows, a direct probe and greps; the arm under §7, observed at the close.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, its rows
  binding `ROOT / ".unattended.conf"`, `os.path.join(ROOT, ".memory-tree.conf")` and
  `Path(ROOT, "cfg", ".unattended.conf")` and its aliased from-import row each answer one `conf constant`
  hit, its `OTHER = ROOT / "other.toml"` row answers none, and 86 AC13's three rows still answer one each.
  Red when: the matcher lists node shapes, so a `BinOp` with a non-str operand, an `os.path.join` call or
  an aliased from-import reads as no conf read.
- **AC2** — When a `python -c` probe imports `loop_lib` from `tools/loop/` and calls
  `derive_conf_constants` on a scratch `loop_lib.py` holding those four bindings, an `AugAssign`
  `SUFFIX += ".unattended.conf"`, a tuple target `A, B = ".memory-tree.conf", 1`, a binding
  `GUARDED = ROOT / ".memory-tree.conf"` under a module-level `if`, `OTHER`, and a conf name bound inside
  a function, it answers exactly `CONF`, `SUFFIX`, `A`, `B` and `GUARDED` for the bindings that carry
  one, never `OTHER` and never the function-local name.
  Red when: an `AugAssign`, a tuple target or a conditional binding is dropped, or a function body leaks
  into the module set.
  figure: the scratch file is written by the probe, so each expected name is DERIVED from its bytes.
- **AC3** — When `awk '/^- \*\*S13\*\*/,/^- \*\*S14\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md` is piped to
  `grep -c "subtree"`, it prints at least 1, and `grep -c "BinOp of str"` over the same file prints 0; and
  `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md` piped to
  `grep -c "syntax subtree"` prints at least 1.
  Red when: 86 or 82 still defines the kind by a shape list beside this unit's class.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted leg this pass keeps green, outside the base manifest and declared by the unit that
mints it: `loop budget fixtures`, which runs `budget.py --fixture`; it is no leg at HEAD.

New arm: tools/loop/budget.py · covers AC1 · the joined-path, os.path.join, multi-argument Path and aliased from-import rows with the non-conf negative, staged against 86 S13's shape list · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Does a binding that names another member join the class?** (a) no: a binding joins only on a
  conf-name constant in its own value, charge rule 2's predicate at module level; (b) yes: a binding
  naming a member joins too, in statement order. (b) adds a rule no instance in `tools/` exercises and
  splits this predicate from the walk id 17 lifts, so 88's slice would change AC2's answer. RESOLVED
  (agent, 2026-10-24, delegated): (a), S1 and §3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-7 spec audit's id 29 (HIGH, item H1).

## 10. Reuse audit

The seam is 86's `derive_conf_constants`, restated in place, and 82 S10's `derive_import_aliases` for the
aliased route; no second reader of `loop_lib.py` is minted. S1's predicate is charge rule 2 of
`scan_glob_readers` (`tools/memory-tree/gen_build_index.py:5146`) at module level, found by the
memory-recall query through `TOOL-dTrueNorth-32`'s charge-rule section; lifting that walk is id 17's, in
`TOOL-dDeclaredLoop-88`.
`python tools/codebase-map/reuse_lookup.py "find the module-level names a string constant holding a needle is bound to"`
ranked `holder`, `boundedParallel`, `read_host_name` and `module_inventory`, none a binding walk, and it
did not rank `scan_glob_readers`, where the hit is stale only by omission.

Recall terms used: charge rule scan_glob_readers needle constant module-level binding Assign AnnAssign conf constant derive_conf_constants
