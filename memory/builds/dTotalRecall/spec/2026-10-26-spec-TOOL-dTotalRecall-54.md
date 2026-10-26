# TOOL-dTotalRecall-54 — `parse_id_parts` lands on the named-group regex in step 8, ahead of the readers unit 38 re-points onto it

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 8 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-build-TOOL-dTotalRecall-54-round3-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-54-round3-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-54-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-54-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-54-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-54-round3-fix-brief.md) | research | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-38`
(order 8) S1 builds `parse_id_parts` on `m.group("family")`, `m.group("slug")` and `m.group("seq")`
of `grammar_for(root).ID_RE`. That regex has no named groups: `grammar_for`
(`tools/memory-recall/extract.py:572-601`) builds it from unnamed alternations, and
`TOOL-dTotalRecall-5` S4 adds none. `TOOL-dTotalRecall-46` rebuilds the body correctly, but at
order 9. So at unit 38's own pass every call raises `IndexError`, its AC1 and AC4 are red there,
and its ten re-pointed readers, which catch only `ValueError`, crash on every id until step 9.

The defect sits in the hand-off from unit 5 (order 7) to unit 38: unit 38 §4 reads "the group
names are the ones `TOOL-dTotalRecall-5` S4 gives `ID_RE`", and unit 5 gives none. A repair placed
after unit 38 cannot make unit 38's own pass green, and the skeptic's ruling rejects ordering unit
46 first, because unit 38's later pass would overwrite the body. This unit therefore takes the step
right after unit 5, the step unit 38 sits in, and lands the working parser before unit 38's pass by
a declared edge. Unit 38's pass then finds the function built and re-points its readers onto it, as
its §4 rule for a landed spelling already says. It repairs `TOOL-dTotalRecall-5`.

## 2. Scope (IN)

- **S1** — The parser. `parse_id_parts(ident, root)` in `tools/memory-tree/id_grammar.py` matches
  `ident` whole with `tree_lib.build_id_token_re(alt)` (`tools/memory-tree/tree_lib.py:428-432`),
  `alt` being `"|".join(grammar_for(root).families)`: the declared and cited families together, the
  one set `grammar_for` already reads through `recall_conf.resolve(root)` (`extract.py:586-599`).
  It returns `(family, slug, seq)` from the groups `fam`, `slug` and `seq`, with `seq` an integer.
  It reads no group of `ID_RE` and makes no conf read of its own. Observed by AC1.
- **S2** — A correction suffix parses. Before the match the parser strips one trailing run of
  lowercase letters after the final digits, the session era's `[a-z]*` (`extract.py:163`), so
  `TOOL-aDrainedSluice-9b` returns `("TOOL", "aDrainedSluice", 9)`. Observed by AC2.
- **S3** — Refusals. An ident `build_id_token_re` does not match whole raises `ValueError` naming
  it. That covers a flat-era `TOOL-001` and a node-scoped `TOOL-d119` of a declared family, an
  undeclared family, a malformed `TOOL-x`, and a pinned `TOOL-dTotalRecall-38@rev-2`. Observed by
  AC3.
- **S4** — The landing precedes unit 38's pass. This unit's pass commit lands in step 8 before
  `TOOL-dTotalRecall-38`'s, which consumes it by the §3 edge, and unit 38's pass re-points its
  readers onto this body without rewriting it. Observed by AC4.

## 3. Non-goals (OUT)

- Which readers call the parser: unit 38's ten and `TOOL-dTotalRecall-45`'s three.
- The grammar, `grammar_for`, `ID_RE` and the slug class bound into `build_id_token_re`:
  `TOOL-dTotalRecall-5`'s.
- Unit 46's own pass. It builds nothing this unit has built; its criteria are observed over this
  body at step 9.
- Returning the suffix. A caller that needs it is a later unit's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py` with `grammar_for`, and
  `tree_lib.build_id_token_re` with its slug class bound from the grammar; without them the parser
  has no module and no named-group regex
- **hands-off** `TOOL-dTotalRecall-38` — `parse_id_parts`, landed in step 8 before that unit's pass,
  whose readers it re-points onto this body without rewriting it
- **hands-off** `TOOL-dTotalRecall-45` — `parse_id_parts`, landed at step 8, on which that unit's three
  readers run at step 9 (the round-1 audit of units 44 to 53, id 2)
- **hands-off** `TOOL-dTotalRecall-46` — `parse_id_parts` on `build_id_token_re`, already built when
  that unit's pass runs at step 9, which observes it by its AC1 to AC3
- **hands-off** `TOOL-dTotalRecall-60` — the parser's family set and its refusal fixtures, which
  that unit re-observes for the round-1 audit of units 44 to 53's ids 18 and 19
- **hands-off** `TOOL-dTotalRecall-63` — `parse_id_parts` and its cited-family case, which that unit carries into unit 46's AC1, so unit 46's pass observes this body rather than rebuilding it (the round-1 audit of units 54 to 60, id 3)
- **hands-off** `TOOL-dTotalRecall-64` — `parse_id_parts`, the body that unit has unit 46's spec name and observe (the round-1 audit of units 54 to 60, id 22)
- **hands-off** `TOOL-dTotalRecall-66` — `parse_id_parts`, whose refusals, per-root cache and `ConfError` that unit settles (the round-1 audit of units 54 to 60, ids 21, 38 and 39)

## 4. Design

### The parser

```python
SUFFIX_RE = re.compile(r"(?<=\d)[a-z]+$")

def parse_id_parts(ident: str, root) -> tuple:
    alt = "|".join(grammar_for(root).families)
    m = tree_lib.build_id_token_re(alt).fullmatch(SUFFIX_RE.sub("", ident))
    if m is None or m.group("rev") is not None:
        raise ValueError(f"not an id under this tree's grammar: {ident}")
    return m.group("fam"), m.group("slug"), int(m.group("seq"))
```

`grammar_for(root).families` is `conf.families + conf.cited_families` (`extract.py:599`), so an
adopter that declares `RECALL_CITED_FAMILIES` parses a cited id that `ID_RE` already accepts.
`tree_lib._id_alternation` is not used: it reads a conf dict's `FAMILIES` only
(`tree_lib.py:416-418`) and omits cited families. The compiled regex is cached per root beside
`grammar_for`'s own binding, as unit 46 §5 asks.

### The order inside step 8

Units 38, 4 and this unit share order 8. This unit and unit 38 both write `id_grammar.py`, and unit
38 reads this unit's output, so BUILD-METHOD M6 clauses 1 and 2 sequence the two passes, this one
first. Unit 4 writes neither and stays parallel.

### Inventory

Minted: `parse_id_parts` and `SUFFIX_RE` in `tools/memory-tree/id_grammar.py`. Naming cell:
`parse_id_parts` is asked of `python tools/lexicon/lexicon.py --suggest parse_id_parts --as py.function`
at the pass; `SUFFIX_RE` has no cell, the lexicon declaring no constant surface.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
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
- perf / scale — one compiled regex per root, cached beside `grammar_for`.
- error / empty / loading states — `ValueError` naming the id for every ident the session-era regex
  does not match whole.
- observability — the error names the id.
- risks — a suffixed id and its parent parse to the same tuple; no caller at base keeps them apart.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none: the function is new at this step.
- user docs — none under `help/`: no page covers id parsing.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `parse_id_parts("TOOL-dTotalRecall-38", ".")` from
  `id_grammar.py`, it returns `("TOOL", "dTotalRecall", 38)`; in a scratch tree whose
  `.memory-tree.conf` declares `RECALL_CITED_FAMILIES` with `ZED`, the call on `ZED-aFoo-2` returns
  `("ZED", "aFoo", 2)`; and `grep -c "ID_RE"` over the function's source prints `0`.
  Red when: the parser reads a group `ID_RE` lacks and raises `IndexError`, or refuses a cited family.
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

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `build-index selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/id_grammar.py · covers AC1 AC2 AC3 · the parser cases plain, cited, suffixed, flat, node-scoped, undeclared and pinned, staged by reading `ID_RE`'s groups again · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 1
  (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-63, TOOL-dTotalRecall-64, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `tree_lib.build_id_token_re` (`tools/memory-tree/tree_lib.py:428`), the one
named-group id regex `_expand_ids` and `read_id_pins` already match through, fed by
`grammar_for(root).families` (`tools/memory-recall/extract.py:572`), the family read the grammar
already makes. This is the body `TOOL-dTotalRecall-46` §4 designs, with its conf read corrected to
the one that exists. `python tools/codebase-map/reuse_lookup.py "parse a unit id into family slug and sequence"`
ranked name-stem neighbours and not this regex, as unit 46 §10 records.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
