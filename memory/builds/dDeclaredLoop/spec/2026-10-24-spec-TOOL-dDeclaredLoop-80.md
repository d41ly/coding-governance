# TOOL-dDeclaredLoop-80 — the no-own-conf-read rule stops at a named fixture boundary, so the plants that write the confs are outside its population

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-80-deviation-801.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-80-deviation-801.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-80-deviation-802.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-80-deviation-802.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`)
confirmed finding **id 20 at HIGH**, its item **H1**, alone in that item. The same defect is item M1 at
medium (ids 1 and 11), batched into `TOOL-dDeclaredLoop-82`. `TOOL-dDeclaredLoop-76` S2 counts every
non-docstring string constant ending in a conf name, and its S3 runs that rule over the whole of
`tools/loop/budget.py` and `tools/loop/breakpoints.py`. Those two modules hold the `--fixture` plants
that must write those confs into scratch trees, and no spec names a constant the plants could use
instead. Built as written, the `no-own-conf-read` plant is red at 76's own pass and in the two fixture
legs, and the builder must exempt code ad hoc or weaken the rule.

This unit draws one syntactic boundary around fixture code and states it in the rule. It builds
immediately after 76 and repairs `TOOL-dDeclaredLoop-76`.

## 2. Scope (IN)

- **S1** — The fixture boundary. `derive_conf_reads(path)` (76 S2) passes over every node a function
  definition encloses, its decorators, its signature and its body with nested definitions, where the
  definition is a `FunctionDef` or `AsyncFunctionDef` whose name, split on `_`, holds the token
  `fixture` or `plant`. Every other node stays in the population: a module-level constant, a class body
  and a function whose name holds neither token. Observed by AC1, AC2.
- **S2** — Every conf name the two modules' fixture code spells sits inside the boundary: each plant
  body, and each helper that seeds or asserts a scratch tree, is a function S1 bounds. The plants
  already built at this pass, 60 AC2, 64 AC1, 72 S4 and 76 AC3, are renamed or moved into one where they
  are not, and each still answers to its `--plant` name. Observed by AC1, AC3.
- **S3** — The `no-own-conf-read` plant prints `fixture boundary: <n> functions — <names>` before its
  hits, so the size of what S1 passed over is read on every run and a boundary that swallows a module
  shows as a number. Observed by AC1.
- **S4** — The rule exits 0 over both modules once every plant this build adds to them exists: 75 S6's
  plant and 79 AC20's and AC25's plants are written inside the boundary, as this unit's hands-off
  bullets to 75 and 79 record. Observed by AC4.

## 3. Non-goals (OUT)

- A name or attribute read of a conf-name constant from `tools/loop/loop_lib.py`, a conf name in the
  middle of a string, an aliased reader call and the async docstring scope: ids 1, 30, 12 and 17, scope
  items of `TOOL-dDeclaredLoop-82`, which keeps a read outside the boundary counted.
- 76 §4 Evidence's list of the conf-writing plants: id 11, `TOOL-dDeclaredLoop-82`.
- What either reader reads or prints: 72 S1 and 75 S5, S7 and S8, unchanged.
- A spec-lint check that a static rule over a module names where its sibling plants sit, the finding's
  left-shift: the class is recorded at the close; S1 and AC2 are this rule's boundary and its fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-76` — `derive_conf_reads` in `tools/loop/loop_lib.py` and the `no-own-conf-read` plant of `budget.py` and `breakpoints.py`, whose population this unit bounds
- **hands-off** `TOOL-dDeclaredLoop-75` — the fixture boundary, inside which S6's `unset-driver-root` plant writes both confs, so that pass's re-run of the `no-own-conf-read` plant exits 0
- **hands-off** `TOOL-dDeclaredLoop-79` — the fixture boundary, inside which the `trailing-slash-agree` and `no-confs` plants write their confs
- **hands-off** `TOOL-dDeclaredLoop-82` — the fixture boundary, outside which that unit counts a conf-name constant read through a name or an attribute (ids 1, 11)
- **hands-off** `TOOL-dDeclaredLoop-86` — S4's plant population, §4 Files touched and AC4, which that unit widens to every later plant, records 67's shared write in, and splits into one grep per plant (the round-6 spec audit's ids 4, 6, 25)
- **hands-off** `TOOL-dDeclaredLoop-88` — S4's plant population, which that unit widens to the plants of 82, 86 and 87 (the round-7 spec audit's id 7)
- **hands-off** `TOOL-dDeclaredLoop-90` — S4's plant population, which that unit widens to 87's `conf-read-forms` rows (the round-8 spec audit's id 6)
- **hands-off** `TOOL-dDeclaredLoop-99` — S1's fixture boundary, outside which that unit derives the functions of `loop_lib.py` that open a conf (the round-12 spec audit's id 19)

## 4. Design

### Evidence

- 76 S2 counts "a string constant ending `.memory-tree.conf` or `.unattended.conf` anywhere but a
  module, class or function docstring", S3 runs it over each module's own file, and AC1 requires exit 0
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md`, §2, §6).
- The plants writing a conf into a scratch tree from those modules, read in their specs on 2026-10-24:
  60 AC2 and 64 AC1 (`.memory-tree.conf` at `records`), 72 S4 (`confs-disagree`, `unattended-root`), 76
  AC3 (`root-source`), 75 S6 (`unset-driver-root`), and 79 AC20 and AC25 (`trailing-slash-agree`,
  `no-confs`). 76 AC3's own expected answers, `(records, .unattended.conf)`, are conf names in assertion
  code, so the boundary covers asserting as well as seeding.
- The repo's fixture code already carries the token in its function names: `add_plant`,
  `build_fixture`, `run_fixture` and `run_plant_arms` (`tools/memory-tree/deviation_join.py:1085`,
  :1229, :1307, :1522).
- The naming lexicon declares no `fixture` or `plant` verb (`.lexicon.conf:604`, the VERBS table):
  `lexicon.py --suggest plant_root_source --as py.function` answers that `plant` is undeclared, run
  2026-10-24. A leading `plant_` or `fixture_` would red the naming predicates on every definition, so
  the token is matched anywhere in the name.
- `tools/loop/` does not exist at base `ed497191`: every loop path here is a sibling unit's output.

### The boundary

```
derive_conf_reads(path):
    tree = ast.parse(read(path))
    bounded = { id(n) for f in ast.walk(tree)
                if isinstance(f, (FunctionDef, AsyncFunctionDef))
                and {"fixture", "plant"} & set(f.name.split("_"))
                for n in ast.walk(f) }                 # decorators, arguments and body
    for node in ast.walk(tree):
        if id(node) in bounded: continue
        ... 76 S2's two kinds, unchanged
```

`read_planted_root`, `transplant` and `fixtures` hold neither token, so a reader named that way stays in the
population; the match is on whole `_`-separated tokens.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`

### Alternatives rejected

- **A separate fixtures module per reader.** The boundary becomes a file, every plant's spec names
  `budget.py --fixture --plant`, and a reader imported from the fixtures module escapes the scan
  entirely; a name boundary keeps fixture and reader in one scanned file, visible in review.
- **A loop_lib helper that writes the confs, with exported conf-name constants (M1's option b).** The
  plants' assertions still spell the expected source, so the literal returns in assertion code; the
  name-resolution half it proposes is kept, outside the boundary, as `TOOL-dDeclaredLoop-82` S1.
- **A prefix boundary, `fixture_*` and `plant_*`.** Neither is a declared verb, so each such definition
  is a naming-predicate refusal.

## 5. Production-readiness checklist

- security — a read-only parse of the kit's own modules; the boundary narrows nothing a reader does.
- perf / scale — one more `ast.walk` per bounded function per plant run, milliseconds.
- error / empty / loading states — a module with no bounded function prints `fixture boundary: 0
  functions`, never a silent pass.
- observability — S3 prints the bounded functions by name on every run.
- risks — a reader named with the token escapes the rule; the name is visible in review and S3 prints
  it, and AC2 stages a reader that holds the letters but not the token.
- testing — AC1 to AC4 as plants and probes; the arms under §7, observed at the close.
- migration — none: the readers are unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant no-own-conf-read` and the same plant of
  `breakpoints.py --fixture` run in `tools/loop/` at this pass, each exits 0 and prints a
  `fixture boundary:` line naming at least one function. In a scratch copy of `tools/loop/` whose
  `budget.py` gains a module-level `CONF = ".unattended.conf"` and a function `read_records_root`
  returning `(tree / ".memory-tree.conf").read_text()`, the first exits non-zero naming both lines and
  `conf name`.
  Red when: the boundary passes over a module-level constant or a function whose name holds neither
  token.
- **AC2** — When a `python -c` probe calls `derive_conf_reads` on a scratch module holding
  `def check_plant_root(tree)` writing `tree / ".unattended.conf"`, `async def build_fixture_tree(t)`
  returning `".memory-tree.conf"`, and `def read_planted_root(t)` returning `".unattended.conf"`, it
  returns one hit, on the line inside `read_planted_root`.
  Red when: the token is matched as a substring, so `read_planted_root` is bounded, or an async
  definition is not.
- **AC3** — When `--plant unattended-root`, `--plant confs-disagree` and `--plant root-source` run in
  `budget.py --fixture`, and the first two in `breakpoints.py --fixture`, after the move, each exits as
  72 AC1 to AC3 and 76 AC3 state.
  Red when: a plant moved inside the boundary no longer answers to its `--plant` name.
- **AC4** — When the main loop runs the `no-own-conf-read` plant of both fixtures at the close, after
  the passes of `TOOL-dDeclaredLoop-75` and `TOOL-dDeclaredLoop-79`, each exits 0 while
  `grep -c "unset-driver-root\|trailing-slash-agree\|no-confs" budget.py` in `tools/loop/` prints at
  least 3.
  Red when: a later plant spells a conf name outside the boundary.
  fixture: 75 builds at order 39 and 79 at order 40, so this is observed at the close and not at this
  pass.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

This pass keeps the sibling-minted `loop budget fixtures` leg (`TOOL-dDeclaredLoop-30`) and the
`loop breakpoints fixtures` leg (`TOOL-dDeclaredLoop-71`) green, and once `TOOL-dDeclaredLoop-67` mints
them, the leg `loop definition fixtures` and the leg `loop selftest`; none is a leg at HEAD.

New arm: tools/loop/budget.py · covers AC1 AC3 · the no-own-conf-read plant over a scratch copy gaining a module-level conf constant and an unbounded reader, and the moved plants by name · none
New arm: tools/loop/breakpoints.py · covers AC1 · the no-own-conf-read plant over its own module, staged the same way · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Bound the fixture code by a name token, by a separate module, or route it through a loop_lib
  helper (ids 20, 1, 11)?** (a) a function-name token boundary in the one scanned file; (b) a fixtures
  module per reader; (c) a helper writing the confs from exported constants, the rule counting a name
  that resolves to one. (c) leaves the assertion literals in the module; (b) moves every plant's file
  and lets an imported reader escape the scan; (a) is the skeptic's corrected fix and satisfies AC1 of
  76 and this unit. RESOLVED (agent, 2026-10-24, delegated): (a), S1, with (c)'s name-resolution half
  kept outside the boundary by `TOOL-dDeclaredLoop-82`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-5 spec audit's id 20 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-99, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 76's `derive_conf_reads`, extended in place with one bounded set; the boundary's token is
the one the repo's fixture code already names its functions with (`tools/memory-tree/deviation_join.py:1085`).
`python tools/codebase-map/reuse_lookup.py "exempt fixture code from a static scan of a module"` ranked
`fixture`, `scan`, `build_fixture` and `load_affordance_exempt` (`tools/codebase-map/map_lib.py`); none
bounds a syntax-tree walk by an enclosing function, and the affordance exemption is a per-path row, so no
existing seam fits the boundary itself. The memory-recall query returned this build's 76 and 71 specs and
the decision record that an exemption arm must plant a line the rule does match, which AC1 and AC2 do.

Recall terms used: no-own-conf-read fixture plant boundary syntax tree derive_conf_reads conf name budget breakpoints exempt
