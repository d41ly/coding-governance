# TOOL-dMindYourWords-12 — the definition context the lexicon reads through the `tools/lib` extraction primitive

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 4 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0273@e1bd67f4 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md](../build/2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md) | research | TOOL-dMindYourWords-11 TOOL-dMindYourWords-13 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

One extraction primitive in `tools/lib`, which dTotalRecall builds (TOOL-dTotalRecall-13, LX-2), and
which the lexicon calls over the working tree, the index or a revision, so neither the lexicon nor the
map requires the other. TOOL-dTotalRecall-13 §3 and TOOL-dTotalRecall-8 §3 hand this build the one
part they leave out: the definition context, that is the enclosing class, the bases resolved through
imports, the decorators with aliases resolved and the module's imports. Every forced-name reader of
this build needs that context (lexicon review `[integration]` :421-427), and today the lexicon has
none of it: `_python_defs` (`tools/lexicon/lexicon.py:425`) records `(name, lineno)` pairs with no
class, and `extract_decorators` (`:2527`) records a decorator by its written last segment, so
`from typing import override as ov` reads as `ov`.

## 2. Scope (IN)

Build-run precondition: TOOL-dTotalRecall-13 (the `extract_code` block, `read_defs_at`, the kit copies
and the parity row) and TOOL-dTotalRecall-8 (`extract_ranges(src, ext)`) are built first. dTotalRecall
is an ancestor of this build (through dLinkedLibrary and dWellOiledMachine), so they land before this
build run. Until they land the lexicon reads what it reads at base: `extract_decorators` by last
written segment, no bases, no enclosing class; and units 2, 4, 5 and 8, which read this unit's
context, cannot build.

- **S1** — The context option on the primitive. `extract_ranges(src, ext, *, context=False)` in the
  canonical block of `tools/lib/extract_code.py` gains a keyword-only `context` flag. Off, every row
  and the return shape are TOOL-dTotalRecall-8's, byte for byte, so the code record and its parity are
  untouched. On, for a `python-ast` extension, the same single `ast` walk that yields the ranges also
  yields, per definition row, `enclosing` (the qualified name of the class whose body holds the
  definition, or `None`), `bases` (for a class row, each base resolved per §4 "Resolution") and
  `decorators` (each decorator resolved the same way, a call decorator read by its callee), and, per
  module, `imports`, the map from each module-level bound name to its dotted target. For every other
  extension the context fields are empty and nothing is refused. Observed by AC1, AC2, AC3, AC9.
- **S2** — The state reader carries the option. `read_defs_at(root, state, paths=None, cache=None, *,
  armed=None, sets=None, context=False)` passes `context` through to `extract_ranges` for each blob of
  a `python-ast` extension, so the working tree, the index and a revision each answer with context in
  one listing and one batched blob read, the cost TOOL-dTotalRecall-13 §4 "The states" prices. Off,
  its return is TOOL-dTotalRecall-13's shape unchanged. The cache key gains `context`. Observed by AC4.
- **S3** — The copies. The canonical edit is copied byte for byte into `tools/lexicon/extract_code.py`,
  `tools/codebase-map/extract_code.py` and `tools/memory-tree/extract_code.py`, held by the existing
  `extract_code` row of `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`; no row is added.
  Observed by AC8.
- **S4** — The lexicon's accessor (I5). `read_definition_context(root, state, conf, paths=None)` in
  `tools/lexicon/lexicon.py` returns `{(path, lineno, name): row}` keyed exactly as
  `extract_decorators` keys today, each row holding `qualname`, `enclosing`, `bases` and `decorators`,
  plus `{path: imports}`, over `state` `worktree`, `index` or a revision, by one `read_defs_at(...,
  context=True)` call from the lexicon's own `extract_code.py`. It never imports a sibling kit
  (`check_self_containment`, `lexicon.py:2359`). Observed by AC4, AC7.
- **S5** — The path selector is honoured. Before the call, the accessor keeps only the paths for which
  `check_out_of_scope(rel, rows)` (TOOL-dMindYourWords-15, I17) returns `None`, the rows read from
  `conf`'s `OUT_OF_SCOPE:` block, so a record under `memory/builds/**` carries no context in any
  state. Observed by AC7.
- **S6** — `extract_decorators` becomes an adapter over S4 at the working tree: for each site it
  returns the last dotted segment of each RESOLVED decorator, so `@app.route` still yields `route`
  and `@ov` bound by `from typing import override as ov` yields `override`. Its signature and key are
  unchanged, so the decorator selectors of `CELLS` (`lexicon.py:2732`) read it as before. Observed by
  AC6.
- **S7** — The frozen pair stays frozen. `extract_text` and `extract` keep returning
  `(functions, types, imports)` with each function entry a `(name, lineno)` pair: two call sites in
  `tools/drift-audit/drift_report.py` (`:1307`, `:1432`) unpack it positionally outside any
  `ValueError` catch. Observed by AC5.

## 3. Non-goals (OUT)

- The primitive itself, its block, its states, its copies and the map's call: TOOL-dTotalRecall-13.
  Ranges, body hashes and call sites: TOOL-dTotalRecall-8. This unit adds a flag and its fields and
  re-specs neither.
- What a forced name is: the packs, base matching and the three cases are TOOL-dMindYourWords-2's;
  markers verified against packs are TOOL-dMindYourWords-4's; the import census is
  TOOL-dMindYourWords-8's. This unit hands them the context and grades nothing.
- JavaScript and TypeScript context. Class membership, `extends` and import resolution for them are
  the primitive's second wave (lexicon review `[forced]` item 1); their rows carry empty context.
- A live import to resolve a base (lexicon review `[forced]` item 5): resolution is static, from the
  module's own syntax tree.
- Resolving a name through another module's re-exports: a base imported from a module that itself
  imports it is resolved to the dotted name the importing module wrote, and following it further is
  TOOL-dMindYourWords-2's, against committed pack data.
- The commit check over the index and the bar's comparison at a revision: TOOL-dMindYourWords-9's. S4
  answers those states for any caller and wires none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-15` — `check_out_of_scope`, the predicate S5 filters paths
  through; without it a record under `memory/builds/**` carries context into every forced-name reader
- **hands-off** `TOOL-dMindYourWords-2` — `extract_ranges` with `context=True`, read through S4, whose
  `bases` and `enclosing` decide whether a member or prefix row applies
- **hands-off** `TOOL-dMindYourWords-4` — `extract_ranges` with `context=True`, read through S4, whose
  resolved `decorators` find a marker under any alias
- **hands-off** `TOOL-dMindYourWords-8` — `extract_ranges` with `context=True`, whose per-module
  `imports` feed the import census
- **hands-off** `TOOL-dMindYourWords-5` — `extract_ranges` with `context=True`, read through S4, whose
  `qualname` spells a method's site key `<path>::<Class>.<name>` (I3)
- **consumes-from** external — TOOL-dTotalRecall-13 S1 to S4 and TOOL-dTotalRecall-8 S2, DEFERRED at
  base, built by the ancestor build dTotalRecall before this build run

## 4. Design

### Resolution

One rule for a base and a decorator, applied to the expression as written:

| Expression | Result | `how` |
|---|---|---|
| `Name` bound by a module-level `import a.b as c`, `from a import B as C` or `import a` | the import's dotted target (`c` to `a.b`, `C` to `a.B`, `a` to `a`) | `import` |
| `Attribute` chain `x.y.Z` whose head `x` is bound as above | the head's target joined with `.y.Z` | `import` |
| a relative import, `from .m import B` | `.m.B`, the leading dots kept, as `_python_defs` keeps them (`lexicon.py:446-452`) | `import` |
| `Name` bound by a module-level class or function definition | its qualified name in the module | `local` |
| `Name` that is a Python builtin (`object`, `Exception`) | `builtins.<name>` | `builtin` |
| anything else: a name bound only inside a function, a subscript, a call | the expression's source text | `unresolved` |

Each resolved entry is a pair `(dotted, how)`. Resolution reads module-level bindings only: a name an
import inside a function binds resolves `unresolved`, which TOOL-dMindYourWords-2 grades as its
"unresolved base" case rather than guessing. A call decorator `@d(x)` resolves its callee `d`.

### The context row

```python
# extract_ranges(src, "py", context=True), one definition row, beside TOOL-dTotalRecall-8's fields
{"qualname": "Outer.Inner.m", "enclosing": "Outer.Inner",
 "bases": [],                                    # a class row lists its bases
 "decorators": [("typing.override", "import")]}
# and once per module
{"imports": {"ov": "typing.override", "H": "logging.Handler", "lg": "logging"}}
```

The flag is keyword-only and defaults off, the shape `extract_text`'s `sets` keyword took for the same
reason (`lexicon.py:2232-2236`): a caller that never passes it is on exactly the previous behaviour.
The walk is the one `extract_ranges` already makes: the context is recorded on the nodes it visits,
so a lexicon run parses each Python file once for its pairs and once for its ranges, and
`extract_decorators`' own `ast.parse` (`lexicon.py:2561`) goes with its body.

### The calls

| Caller | State | What it reads |
|---|---|---|
| `extract_decorators`, adapter (S6) | `worktree` | decorators, last segment |
| the forced-name, marker and suppression units, 2, 4 and 5 | `worktree` | `enclosing`, `bases`, `decorators`, `qualname` |
| the import census, unit 8 | `worktree` | `imports` |
| a commit-time or bar-time reader | `index`, a revision | the same rows at the staged tree and at the base |

### Inventory

Minted: the keyword `context` on `extract_ranges` and on `read_defs_at`; the row fields `enclosing`,
`bases`, `decorators` and the module field `imports`; `read_definition_context` in
`tools/lexicon/lexicon.py`, cell `py.function`, answered `OK` by `lexicon.py --suggest
read_definition_context --as py.function` at base.

### Migration

None. No stored record holds context, and the flag defaults off for every existing caller.

### Rollout

Live when built: the adapter's alias resolution is the only change an existing run can observe, and
only on a decorator bound through an import alias, of which the tree holds none today (§5 risks).

### Files touched (estimate)

- `tools/lib/extract_code.py`
- `tools/lexicon/extract_code.py`, its copy
- `tools/codebase-map/extract_code.py`, its copy
- `tools/memory-tree/extract_code.py`, its copy
- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`

### Alternatives rejected

- **A second context walk in the lexicon**, a sibling of `extract_decorators` reading bases. The clause
  and the parent's hand-off put the context in the primitive so the map and the lexicon read one
  extraction (TOOL-dTotalRecall-13 §3, first bullet); a lexicon-side walk keeps a third parse per file
  and a second Python reader of class structure. Rejected by rung 1, the clause's text.
- **Widening `extract_text`'s pair to carry context.** Rejected by test: `grep -n 'for nm, _ln in'
  tools/drift-audit/drift_report.py` prints `:1307` and `:1432`, each a positional unpack outside any
  `ValueError` catch, so a third element raises on the `drift-audit records` leg, which has no guard.
- **Resolving a base by importing its module.** Rejected by the lexicon review's measurement (`[forced]`
  item 5): pytest imports under one of this node's interpreters and not the other, so a live import
  grades two nodes differently.

## 5. Production-readiness checklist

- security — reads source text only; no import, no evaluation of the parsed code, no write.
- perf / scale — the context is recorded inside the walk `extract_ranges` already makes; under `index`
  and a revision the blobs come from the one `git cat-file --batch` `read_defs_at` makes.
- error / empty / loading states — an unparseable blob yields the empty triple and no context, the
  fail-closed rule `read_defs_at` states; a non-Python extension yields empty context.
- observability — the accessor's rows are what TOOL-dMindYourWords-2 prints as a forced name's source;
  this unit prints nothing of its own.
- risks — the decorator adapter changes the selected set only for an aliased decorator; at base no
  tracked Python file decorates a definition through a name a module-level `import ... as` binds
  (PINNED: 0 such sites over every tracked `*.py`, 39 files holding an alias, an `ast` walk at
  `ba8b3c8c4`), so no `CELLS` row's population moves.
- testing — the arms of §7, each on a planted source or a planted fixture repository.
- migration — none.
- user docs — the lexicon README's extraction section names the context and the alias rule.

## 6. Acceptance criteria

- **AC1** — When `extract_ranges` from the lexicon's `extract_code.py` reads the planted source
  `from typing import override as ov` / `class C(B):` / `    @ov` / `    def m(self): ...` with
  `context=True`, the row for `C.m` carries `decorators` `[("typing.override", "import")]` and
  `enclosing` `C`; with `context` omitted the rows equal TOOL-dTotalRecall-8's output for that source.
  Red when: the decorator reads `ov`, or the default call's rows gain a field.
- **AC2** — When the same call reads the planted module `from logging import Handler as H` /
  `import logging as lg` / `class Local: ...` / `class X(H): ...` / `class Y(lg.Handler): ...` /
  `class Z(Local): ...` / `class V(Exception): ...` / `class W(Unknown): ...`, the `bases` of `X` and
  `Y` are each `("logging.Handler", "import")`, of `Z` `("Local", "local")`, of `V`
  `("builtins.Exception", "builtin")` and of `W` `("Unknown", "unresolved")`.
  Red when: an aliased base resolves to its alias, or `W` resolves to anything but `unresolved`.
- **AC3** — When the call reads `from .m import B as BB` / `class Outer:` / `    class Inner(BB):` /
  `        def m(self): ...` / `def f(): ...`, the module's `imports` maps `BB` to `.m.B`, the row of
  `Outer.Inner.m` carries `enclosing` `Outer.Inner` and `qualname` `Outer.Inner.m`, and the row of `f`
  carries `enclosing` `None`.
  Red when: the leading dot is flattened, or a nested method names the outer class.
- **AC4** — When `read_definition_context(root, state, conf)` runs in a fixture repository whose
  committed `a.py` decorates `m` with `@ov`, whose index stages `a.py` decorating it with `@final` bound
  by `from typing import final`, and whose working tree adds `@cache` bound by
  `from functools import cache`, state `HEAD` reads `typing.override`, state `index` reads
  `typing.final`, and state `worktree` reads both `typing.final` and `functools.cache`.
  Red when: the index state reads working-tree bytes, or the revision reads the index.
  fixture: the selftest builds the repository; none exists in the tree.
- **AC5** — When `extract_text(src, "parser", "python-ast")` reads AC1's source after this unit, every
  entry of its first element is a 2-tuple `(name, lineno)`.
  Red when: an entry carries a third element.
- **AC6** — When `extract_decorators` runs over a fixture corpus holding AC1's `@ov` and a planted
  `@app.route` with `app` bound by `app = Flask()`, it yields `{"override"}` for `m` and `{"route"}`
  for the route handler, and a fixture `.lexicon.conf` row `py.function+decorator:override  snake`
  routes `m` into that cell.
  Red when: the adapter yields `ov`, or the route handler loses `route`.
- **AC7** — When the fixture repository of AC4 also holds `r.py` under `memory/builds/tX/build/`,
  decorated with `@ov`, and its `.lexicon.conf` carries an `OUT_OF_SCOPE:` row `memory/builds/**`
  with a reason, `read_definition_context` returns no key for that path in any of the three states.
  Red when: the record's definition carries context.
  fixture: as AC4; the block grammar is TOOL-dMindYourWords-15's.
- **AC8** — When the `extract_code` block is cut from the canonical `extract_code.py` under `tools/lib/`
  and from each of the three kit copies with the markers `# >>> extract_code` and `# <<< extract_code`, the four cuts
  are byte-identical and each holds `context=False`.
  Red when: one copy differs by a byte, or a copy lacks the flag.
- **AC9** — When `extract_ranges(src, "sh", context=True)` reads `f() { :; }`, it returns the shell
  row with `enclosing` `None` and empty `bases` and `decorators`, and raises nothing.
  Red when: a non-Python extension refuses or invents context.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `drift-audit records` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC5 AC6 AC9 · the planted sources, each failing case staged by resolving through the alias text instead of the import map, and the adapter staged to keep the written segment · none

New arm: tools/lexicon/selftest.py · covers AC4 AC7 · the fixture repository's three states and its out-of-scope record, staged by reading the index state from the working tree and by skipping the selector · none

The parity of AC8 is held by the existing `extract_code` row of `tools/lib/resolve-python.test.sh`,
which TOOL-dTotalRecall-13 adds; this unit moves no floor there.

## 8. Open questions

- **F1 — Where does the context live: on the primitive's rows, or in a lexicon-side walk?** Options:
  (a) a keyword-only `context` flag on `extract_ranges` and `read_defs_at`, rows gaining fields only
  when asked; (b) a separate accessor in the block beside `extract_ranges` with its own walk; (c) a
  lexicon-only walk. (b) and (c) each add a walk the clause's "one extraction primitive" and LX-2
  fold into one, and (c) puts the class reader in one kit only, so the map would re-derive it.
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 1: the clause and the parent's hand-off name one
  primitive the map and the lexicon each call, and the unit brief reads "extending `extract_ranges`
  rather than adding a third walk". widens: none · relaxes: none
- **F2 — What does a base bound only inside a function resolve to?** Options: (a) `unresolved`; (b)
  the innermost binding's target. (b) needs scope analysis per function body, a second resolver beside the
  module-level one, for a binding no pack row can name statically. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the lexicon review's own case: an unresolved
  base grades as debt and is reported unresolved (`[forced]` item 1). widens: none · relaxes: none
- **F3 — Does the decorator adapter keep the written segment for `CELLS` selectors?** Options: (a) the
  resolved segment, so an aliased decorator is selected by its real name; (b) the written segment, as
  today. (b) keeps a selector blind to the alias the clause asks to resolve. RESOLVED (agent,
  2026-10-29, delegated): (a), rung 3, the most feature-rich survivor; §5 risks measures that no
  population moves at base. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 12, the lexicon review `[integration]`
  :421-441 and `[forced]` items 1 and 5, TOOL-dTotalRecall-13 §2 to §4 and TOOL-dTotalRecall-8 S2 and
  S3, scout C's row and its shared interface 2, and the spec brief's I5 and I17.

## 10. Reuse audit

The seams extended are TOOL-dTotalRecall-8's `extract_ranges(src, ext)` and TOOL-dTotalRecall-13's
`read_defs_at` (each DEFERRED at base, their specs read whole), and `extract_decorators`
(`tools/lexicon/lexicon.py:2527`), which becomes the adapter. `python tools/codebase-map/reuse_lookup.py
"read a definition's enclosing class, bases and decorators resolved through imports"` ranked only
name-stem helpers (`read`, `resolve`, `resolve_kit_dir`); none reads a syntax tree's bindings, so no
existing seam fits the resolution itself, and it is new code inside the walk the parent already makes.
The recall probe's first hit, TOOL-dDeclaredLoop-91, reads decorators and bases for a different
question (module-scope rebinds of a conf) and resolves no import. Scout C's row holds at `ba8b3c8c4`:
`extract_decorators` at `:2527` and `_python_defs` at `:425`; its claim that the record reader is at
`:4113` holds too. Where record and source disagree: the brief's "`extract_text` pair at
`lexicon.py:2532-2540`" cites the docstring that describes the pair; the positional readers are
`drift_report.py:1307` and `:1432`, which §2 S7 cites.

Recall terms used: `python tools/memory-recall/query.py "where does the lexicon read decorators and bases of a definition through imports" --terms "extract_decorators extract_ranges extract_code primitive bases decorators aliases imports lexicon definition context"`
