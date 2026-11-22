# TOOL-dTotalRecall-54 — `parse_id_parts` lands on the named-group regex in step 8, ahead of the readers unit 38 re-points onto it

**Status:** DEFERRED · rev-5 · 2026-11-22 · node d · Tier-2 · base 8b8b1374 · streams tooling · order 8 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-54-deviation-541.md](../build/2026-10-26-build-TOOL-dTotalRecall-54-deviation-541.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-54-round3-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-54-round3-fix-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-54-reground-2-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-54-reground-2-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-54-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-54-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-54-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-54-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-54-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-54-round3-fix-brief.md) | research | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-54-alt-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-alt-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-spec-writer.md) | log | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-38`
(order 8) S1 builds `parse_id_parts` on `m.group("family")`, `m.group("slug")` and `m.group("seq")`
of `grammar_for(root).ID_RE`. That regex has no named groups: `grammar_for` builds it through
`tools/memory-tree/id_grammar.py#build_grammar` from unnamed `(?:...)` alternations, where
PLAY-dOrderedCharter-18 moved it out of `extract.py`, and `TOOL-dTotalRecall-5` S4 adds none.
`TOOL-dTotalRecall-46` rebuilds the body correctly, but at order 9. So at unit 38's own pass every
call raises `IndexError`, its AC1 and AC4 are red there, and its ten re-pointed readers, which catch
only `ValueError`, crash on every id until step 9.

The defect sat in the hand-off from unit 5 (order 7) to unit 38: unit 38's §4 at base
`462d20f3` read "the group names are the ones `TOOL-dTotalRecall-5` S4 gives `ID_RE`", and unit 5
gives none. A repair placed after unit 38 cannot make unit 38's own pass green, and the skeptic's
ruling rejects ordering unit 46 first, because unit 38's later pass would overwrite the body. This unit therefore takes the step
right after unit 5, the step unit 38 sits in, and lands the working parser before unit 38's pass by
a declared edge. Unit 38's pass then finds the function built and re-points its readers onto it, as
its §4 rule for a landed spelling already says. It repairs `TOOL-dTotalRecall-5`.

## 2. Scope (IN)

- **S1** — The parser. `parse_id_parts(ident, root)` in `tools/memory-tree/id_grammar.py` matches
  `ident` whole with `tools/memory-tree/tree_lib.py#build_id_token_re(alt, root)`, `alt` being
  `"|".join(grammar_for(root).families)`: the declared and cited families together, the one set
  `tools/memory-tree/id_grammar.py#grammar_for` already reads through
  `tools/memory-tree/id_grammar.py#resolve`. The same `root` goes to both, so the slug class
  `build_id_token_re` binds is that tree's, never this repo's (`TOOL-dTotalRecall-5` §8 F9). `root`
  may be `None`, the default grammar of the tree the module lives in, which unit 38's readers with no
  root in scope pass (its S1). It returns
  `(family, slug, seq)` from the groups `fam`, `slug` and `seq`, with `seq` an integer. It reads no
  group of `ID_RE` and makes no conf read of its own. Observed by AC1.
  The signature is `parse_id_parts(ident, root, *, alt=None)`. A caller that passes the keyword-only
  `alt`, a family alternation, has the family part matched against it, and `grammar_for(root)` is
  not called. The slug class still comes from `root`, through `build_id_token_re`. With `alt`
  omitted, the tree's families apply as above. Unit 38's readers whose validator binds a caller's
  family list pass it (its §8 F4). Observed by AC6.
- **S2** — A correction suffix parses. Before the match the parser strips one trailing run of
  lowercase letters after the final digits, the session era's `[a-z]*`
  (`tools/memory-tree/id_grammar.py#_eras`), so `TOOL-aDrainedSluice-9b` returns `("TOOL", "aDrainedSluice", 9)`. Observed by AC2.
- **S3** — Refusals. An ident `build_id_token_re` does not match whole raises `ValueError` naming
  it. That covers a flat-era `TOOL-001` and a node-scoped `TOOL-d119` of a declared family, an
  undeclared family, a malformed `TOOL-x`, and a pinned `TOOL-dTotalRecall-38@rev-2`. Observed by
  AC3.
- **S4** — The landing precedes unit 38's pass. This unit's pass commit lands in step 8 before
  `TOOL-dTotalRecall-38`'s, which consumes it by the §3 edge, and unit 38's pass re-points its
  readers onto this body without rewriting it. Observed by AC4.
- **S5** — Importing `id_grammar.py` still imports no sibling, as its module docstring states. The
  parser reaches `tree_lib` on first call through `load_sibling(name)`, the path guard and import
  spelled inline today three times (DERIVED, `grep -c "sys.path.append"
  tools/memory-tree/id_grammar.py`): `tools/memory-tree/id_grammar.py#_parse_spec_h1`, and the two
  copies `TOOL-dTotalRecall-5` landed at `202a354a4`, `tools/memory-tree/id_grammar.py#read_slug_policy`
  and `tools/memory-tree/id_grammar.py#read_recorded_grammars`. All three and the parser call the one
  helper (§8 F3). Observed by AC5.

## 3. Non-goals (OUT)

- Which readers call the parser: unit 38's ten and `TOOL-dTotalRecall-45`'s three.
- The grammar, `grammar_for`, `ID_RE` and the slug class bound into `build_id_token_re`:
  `TOOL-dTotalRecall-5`'s, CLOSED at rev-12 and landed at `202a354a4`. Its S13 binds the slug group
  through `tools/memory-tree/tree_lib.py#read_slug_class` with a trailing `root=None` (its §8 F9),
  replacing the literal `[A-Za-z0-9]+` (its F10). This unit consumes that landed token and changes
  none of it.
- The per-root regex cache: `TOOL-dTotalRecall-66` S35's. This body compiles per call, and
  `grammar_for` caches the default grammar alone; the slug grammar under it is cached per root
  (`tools/memory-tree/id_grammar.py#derive_slug_grammar`).
- The other passes of step 8. This unit builds first in step 8, before `TOOL-dTotalRecall-38` and
  then `TOOL-dTotalRecall-4`, and writes nothing either of them owns (§4).
- Unit 46's own pass. It builds nothing this unit has built; its criteria are observed over this
  body at step 9.
- Returning the suffix. A caller that needs it is a later unit's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py` with `grammar_for`, and
  `tree_lib.build_id_token_re` with its slug class bound from the grammar, landed at `202a354a4`;
  without them the parser has no module and no named-group regex
- **hands-off** `TOOL-dTotalRecall-38` — `parse_id_parts(ident, root, *, alt=None)`, with `root` and
  the keyword-only `alt` of S1, landed in step 8 before that unit's pass, whose readers it re-points
  onto this body without rewriting it (its §8 F4)
- **hands-off** `TOOL-dTotalRecall-45` — `parse_id_parts`, landed at step 8, on which that unit's three
  readers run at step 9 (the round-1 audit of units 44 to 53, id 2)
- **hands-off** `TOOL-dTotalRecall-46` — `parse_id_parts` on `build_id_token_re`, already built when
  that unit's pass runs at step 9, which observes it by its AC1 to AC3
- **hands-off** `TOOL-dTotalRecall-60` — the parser's family set and its refusal fixtures, which
  that unit re-observes for the round-1 audit of units 44 to 53's ids 18 and 19
- **hands-off** `TOOL-dTotalRecall-63` — `parse_id_parts` and its cited-family case, which that unit carries into unit 46's AC1, so unit 46's pass observes this body rather than rebuilding it (the round-1 audit of units 54 to 60, id 3)
- **hands-off** `TOOL-dTotalRecall-64` — `parse_id_parts`, the body that unit has unit 46's spec name and observe (the round-1 audit of units 54 to 60, id 22)
- **hands-off** `TOOL-dTotalRecall-66` — `parse_id_parts`, whose refusals, per-root cache and `ConfError` that unit settles (the round-1 audit of units 54 to 60, ids 21, 38 and 39)
- **hands-off** `TOOL-dTotalRecall-6` — `parse_id_parts`, whose slug names the build a relation's unit-id target belongs to

## 4. Design

### The parser

```python
SUFFIX_RE = re.compile(r"(?<=\d)[a-z]+$")

def load_sibling(name: str):
    here = str(pathlib.Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.append(here)  # APPEND, never insert(0, ...), as the three copies do today
    return importlib.import_module(name)

def parse_id_parts(ident: str, root, *, alt: str | None = None) -> tuple:
    if alt is None:
        alt = "|".join(grammar_for(root).families)
    token_re = load_sibling("tree_lib").build_id_token_re(alt, root)
    m = token_re.fullmatch(SUFFIX_RE.sub("", ident))
    if m is None or m.group("rev") is not None:
        raise ValueError(f"not an id under this tree's grammar: {ident}")
    return m.group("fam"), m.group("slug"), int(m.group("seq"))
```

`grammar_for(root).families` is `conf.families + conf.cited_families`
(`tools/memory-tree/id_grammar.py#build_grammar`), so an adopter that declares
`RECALL_CITED_FAMILIES` parses a cited id that `ID_RE` already accepts.
`tools/memory-tree/tree_lib.py#_id_alternation` is not used: it reads a conf dict's `FAMILIES` only
and omits cited families. A one-argument `build_id_token_re(alt)` would bind this repo's slug class
for a scratch or target tree, the failure unit 5's F9 names. In `_parse_spec_h1`, `read_slug_policy`
and `read_recorded_grammars` the `here` line, the path guard and the `tree_lib` import line become
one `load_sibling("tree_lib")` call, the `from tree_lib import` names read as its attributes. Their
callers see no change: `extract_records` and `extract_supersessions` call `_parse_spec_h1`, and
`derive_slug_grammar` alone calls the other two (`git grep -n "read_slug_policy\|read_recorded_grammars" -- tools`).
`importlib` joins the module's standard-library imports. A tree with no usable conf raises
`ConfError` out of `grammar_for`, which the parser lets pass; `TOOL-dTotalRecall-66` S39 settles it.
`grammar_for` itself already imports `tree_lib`, through `read_slug_policy` under
`derive_slug_grammar`, so a first parser call finds it loaded; the lazy import AC5 observes is the
module's, not the call's.

### The order inside step 8

Units 38, 4 and this unit share order 8. This unit and unit 38 both write `id_grammar.py`, and unit
38 reads this unit's output, so BUILD-METHOD M6 clauses 1 and 2 sequence the two passes, this one
first. Unit 4 writes neither file and builds third, so the step runs 54, then 38, then 4.

### Inventory

Minted: `parse_id_parts`, `load_sibling` and `SUFFIX_RE` in `tools/memory-tree/id_grammar.py`.
Naming cell: `python tools/lexicon/lexicon.py --suggest parse_id_parts --as py.function` printed `OK`
at `c344bdc40` and again at `e514feb71`, as did `--suggest load_sibling`, which leads with the
declared verb `load`; `SUFFIX_RE` has no cell, `--as py.constant` answering that no CELLS row names
it. `git grep -nE "def (load_sibling|parse_id_parts)\b|SUFFIX_RE" -- tools skills` printed nothing at
`e514feb71`.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-recall/selftest.py` (the arm of §7, §8 F2)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Order unit 46 before unit 38.** Unit 38 creates the function, so its later pass would overwrite
  the working body with the broken one (the skeptic's ruling on id 1).
- **Place this repair after unit 38, at order 9.** Unit 38's AC1 and AC4 are red at its own pass,
  and no later step can make that pass green.
- **Name groups inside `ID_RE`'s era alternation.** Python's `re` refuses a group name repeated
  across alternatives, so each era would need its own names; `build_id_token_re` already holds the
  one session-era shape with them.

## 5. Production-readiness checklist

- security — no new surface: a pure parser.
- perf / scale — one regex compiled per call until `TOOL-dTotalRecall-66` S35 caches it per root,
  and for an explicit root `grammar_for`'s own rebuild.
- error / empty / loading states — `ValueError` naming the id for every ident the session-era regex
  does not match whole; `ConfError` from `grammar_for` on a tree with no usable conf.
- observability — the error names the id.
- risks — a suffixed id and its parent parse to the same tuple; no caller at base keeps them apart.
- testing — AC1 to AC5 by the pass; the arm of §7 at the close.
- migration — none: the function is new at this step.
- user docs — none under `help/`: no page covers id parsing.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `parse_id_parts("TOOL-dTotalRecall-38", ".")` from
  `id_grammar.py`, it returns `("TOOL", "dTotalRecall", 38)`, and so does the call with root `None`;
  in a scratch tree whose `.memory-tree.conf` declares `RECALL_CITED_FAMILIES` with `ZED` and
  `RECALL_NODE_TAG_CLASS` with `a-f`, this repo's parser called with that tree's root returns
  `("ZED", "aFoo", 2)` on `ZED-aFoo-2` and raises `ValueError` on `TOOL-xFoo-3`; and `grep -c "ID_RE"`
  over the function's source prints `0`.
  Red when: the parser reads a group `ID_RE` lacks and raises `IndexError`, refuses a cited family,
  or binds this repo's slug class for the scratch root and returns a tuple for `TOOL-xFoo-3`.
  fixture: the scratch tree under the run's scratch directory; the pass makes it.
- **AC2** — When the same probe calls it with `TOOL-aDrainedSluice-9b`, it returns
  `("TOOL", "aDrainedSluice", 9)`.
  Red when: the suffix raises `ValueError` or reaches `int()`.
- **AC3** — When the probe calls it with `TOOL-001`, `TOOL-d119`, `ARCH-aFix-3`, `TOOL-x` and
  `TOOL-dTotalRecall-38@rev-2`, each raises `ValueError` naming the id.
  Red when: any of them returns a guessed tuple, or a declared family's flat or node-scoped shape
  passes.
- **AC4** — When `git log --format=%s` lists this build's pass commits at unit 38's pass tip, this
  unit's commit precedes unit 38's, and at that tip `grep -c "build_id_token_re"` over
  `parse_id_parts`' source prints at least 1 while unit 38's AC1 probe returns its tuple.
  Red when: unit 38's pass runs first, or rewrites the body onto `ID_RE`'s groups.
- **AC5** — When a `python -c` probe imports `id_grammar` alone, `"tree_lib" in sys.modules` prints
  `False`, and after one `parse_id_parts` call it prints `True`; and `grep -c "sys.path.append"
  tools/memory-tree/id_grammar.py` prints `1`, the guard inside `load_sibling`.
  Red when: the module imports `tree_lib` at module level, or a copy of the path guard stays beside
  the helper.
- **AC6** — When the AC1 probe calls `parse_id_parts("EXMP-aFoo-2", None)`, it raises `ValueError`,
  `EXMP` being no family of this tree (`.memory-tree.conf` `FAMILIES`); and
  `parse_id_parts("EXMP-aFoo-2", None, alt="EXMP|OTHR")` returns `("EXMP", "aFoo", 2)`. Passing `alt`
  positionally raises `TypeError`.
  Red when: `alt` is ignored and the tree's families refuse the id, `alt` replaces nothing because
  the families are joined in anyway, or the keyword is not keyword-only.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `build-index selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `policy fixtures` · `drift-audit selftest` · `playbook render selftest` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-recall/selftest.py · covers AC1 AC2 AC3 AC5 AC6 · the parser cases plain, cited, caller-bound `alt`, suffixed, flat, node-scoped, undeclared and pinned, through `make_repo(conf=...)`'s throwaway tree as `read_grammar` probes `grammar_for`, the parser of the memory-tree directory `make_repo` copies from (`resolve_kit_dir` off `KIT`) over that tree's root for the foreign-root case, the path-guard count, plus the import check, staged by reading `ID_RE`'s groups again · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which suite holds the parser's arm?** `id_grammar.py` has no self-test mode and no leg runs
  it at HEAD; no sibling spec adds one. Options: (a) an `id_grammar.py --selftest` and a new leg;
  (b) `tools/memory-recall/selftest.py`, run by `memory-recall kit selftest`, whose `make_repo` copies
  every memory-tree `*.py` into a throwaway tree with a given conf and whose `read_grammar` already
  probes `grammar_for` there; (c) `tools/memory-tree/gen_build_index.py --selftest`, a build-index
  suite. (a) adds a public surface; veto 2 discards it. (b) and (c) both observe AC1 to AC3 and AC5;
  (b) reuses the grammar's own fixture, the tie-break. RESOLVED (agent, 2026-11-22, delegated): (b),
  rung 2. widens: none · relaxes: none
- **F3 — Does `load_sibling` replace the two copies unit 5 landed?** At `202a354a4`
  `read_slug_policy` and `read_recorded_grammars` gained the path guard and import
  `_parse_spec_h1` spells. Options: (a) all three call `load_sibling`; (b) `_parse_spec_h1` alone,
  as rev-4 planned. (b) leaves two copies beside a factory, which the charter's `[reuse]` rule
  forbids; veto 1 discards it. RESOLVED (agent, 2026-11-22, delegated): (a), the one survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 1
  (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-63, TOOL-dTotalRecall-64, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-11-22 · re-grounded at base `8b8b1374` by 2026-11-22-prompt-TOOL-dTotalRecall-54-reground-spec-writer: §1, §2, §4 and §10 re-point `grammar_for`, `build_grammar`, `_eras` and `resolve` to `id_grammar.py`, where PLAY-dOrderedCharter-18 landed them, citing code as `path#symbol`; S1 admits root `None` (unit 38 S1); S5 and AC5 keep the module's sibling import lazy, through `load_sibling`; the cache claim moves to unit 66 S35 and `ConfError` to its S39; §3 states unit 5's pending slug-class binding; §7 names the four further legs guarding `id_grammar.py` and homes the arm in `tools/memory-recall/selftest.py` (F2).
- rev-4 · 2026-11-22 · §3 Edges · per `2026-11-22-prompt-TOOL-dTotalRecall-6-reground-brief`: the Edges block gains the hands-off mirror of TOOL-dTotalRecall-6, whose re-ground consumes `parse_id_parts` to type a unit-id target; nothing else moved.
- rev-5 · 2026-11-22 · S1 · S5 · §3 · §4 · §5 · AC1 · AC5 · §7 New arm · §8 F3 · §10 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-brief`, over unit 5 as landed at `202a354a4`:
  the parser passes `root` to `build_id_token_re`, whose slug class unit 5's F9 bound per root, and
  AC1 gains the foreign-root case that a one-argument call fails; §3 drops the pending-binding
  caveat; `load_sibling` also replaces the two copies of the import unit 5 added (F3), AC5 counting
  one path guard; lexicon and name probes re-run at `e514feb71`.
- rev-5 · 2026-11-22 · S1 · §3 · §4 · AC6 · §7 New arm · per
  `2026-11-22-prompt-TOOL-dTotalRecall-54-alt-brief`, folded into the same rev: `parse_id_parts`
  takes the keyword-only `alt` unit 38 rev-6's F4 consumes, AC6 observing both answers on
  `EXMP-aFoo-2`; §3 states this unit builds first in step 8, before units 38 and 4, and the hands-off
  to unit 38 names `root` and `alt`.

## 10. Reuse audit

The seam extended is `tools/memory-tree/tree_lib.py#build_id_token_re`, the one named-group id
regex `_expand_ids` and `read_id_pins` already match through, fed by `grammar_for(root).families`
(`tools/memory-tree/id_grammar.py#grammar_for`), the family read the grammar already makes. This is
the body `TOOL-dTotalRecall-46` §4 designs, with its conf read corrected to the one that exists.
`python tools/codebase-map/reuse_lookup.py "parse a unit id into family slug and sequence"` ranked
name-stem neighbours (`parse`, `parse_args`, `parse_conf`) and not this regex at `c344bdc40`, as
unit 46 §10 records, and `git grep -nE "def (split_id|parse_id|id_parts|parse_id_parts)" -- tools` printed nothing there.
`load_sibling` extracts the import `tools/memory-tree/id_grammar.py#_parse_spec_h1`,
`tools/memory-tree/id_grammar.py#read_slug_policy` and
`tools/memory-tree/id_grammar.py#read_recorded_grammars` spell today, this parser being its fourth
instance (§8 F3). No existing seam fits it: `reuse_lookup.py "import a sibling module from
this kit directory on first use"` ranked `resolve_kit_dir`, which finds ANOTHER kit's directory,
while `tree_lib` sits beside `id_grammar.py` in this one.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
