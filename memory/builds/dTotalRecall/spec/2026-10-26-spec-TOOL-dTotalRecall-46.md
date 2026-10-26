# TOOL-dTotalRecall-46 — `parse_id_parts` reads the named groups of `tree_lib.build_id_token_re`, and a correction suffix parses

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-38` S1
builds `parse_id_parts` by reading `m.group("family")`, `m.group("slug")` and `m.group("seq")` from
`grammar_for(root).ID_RE`. That regex is built from unnamed alternations (`tools/memory-recall/extract.py:163-169`),
and `TOOL-dTotalRecall-5` S4 names none, so every call raises `IndexError: no such group`. Its
`int(seq)` also raises on a correction id such as `TOOL-aDrainedSluice-9b`, which the session era
admits (`extract.py:165`). The named groups already exist: `build_id_token_re` (`tools/memory-tree/tree_lib.py:428-432`)
carries `fam`, `slug`, `seq` and `rev`, and unit 5 re-points its slug class to the grammar. This unit
rebuilds the parser on that regex. It repairs `TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — `parse_id_parts(ident, root)` in `tools/memory-tree/id_grammar.py` matches `ident` whole with
  `tree_lib.build_id_token_re(alt)`, `alt` being the family alternation `tree_lib._id_alternation` builds
  from the root's conf, as `gen_build_index.py:580` builds it. It returns `(family, slug, seq)` from the
  groups `fam`, `slug` and `seq`, `seq` an integer. `ID_RE` is not read, and the shared era
  alternation gains no group. Observed by AC1.
- **S2** — A correction suffix parses. Before the match the parser strips one trailing run of
  lowercase letters after the final digits, the session era's `[a-z]*`, so `TOOL-aDrainedSluice-9b`
  returns `("TOOL", "aDrainedSluice", 9)`. No re-pointed caller reads the suffix: each takes the slug,
  and the one sort key compares sequences, where today's `int(i.rsplit("-", 1)[1])` raises on the same
  id. Observed by AC2.
- **S3** — An id `build_id_token_re` does not match whole, a flat-era `ARCH-001` and a node-scoped
  `ABL-d119` among them, raises `ValueError` naming it, and each caller keeps the answer it gives a
  malformed id. Observed by AC3.

## 3. Non-goals (OUT)

- The grammar, `grammar_for`, `ID_RE` and the slug class: `TOOL-dTotalRecall-5`'s.
- Which callers parse: `TOOL-dTotalRecall-38`'s ten and `TOOL-dTotalRecall-45`'s three.
- What each re-pointed caller answered for the flat and node-scoped eras: the batch
  `TOOL-dTotalRecall-53` holds that answer equal to base for id 2.
- Returning the suffix. A caller that needs it is a later unit's, which widens the tuple then.

### Edges

- **consumes-from** `TOOL-dTotalRecall-38` — `parse_id_parts` in `id_grammar.py`, whose body this unit
  rebuilds under its name and signature
- **consumes-from** `TOOL-dTotalRecall-5` — `tree_lib.build_id_token_re` with its slug class bound from
  the grammar, the named-group regex this parser matches
- **hands-off** `TOOL-dTotalRecall-53` — `parse_id_parts` on `build_id_token_re`, whose answers for the flat and node-scoped eras that unit holds to base (id 2)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` on `build_id_token_re`, already built at step 8, which this unit's AC1 to AC3 observe (the round-1 audit of units 44 to 53, id 1)
- **hands-off** `TOOL-dTotalRecall-60` — the parser's family read and its era refusal, which that unit re-observes with the cited and declared families (the round-1 audit of units 44 to 53, ids 18 and 19)
- **consumes-from** `TOOL-dTotalRecall-63` — AC1's cited-family case, written into this spec in step 9 before this pass (the round-1 audit of units 54 to 60, id 3)
- **consumes-from** `TOOL-dTotalRecall-64` — S1, §4 and the edge to unit 38 as that unit amends them in step 9 before this pass, so this pass observes unit 54's body and builds none (the round-1 audit of units 54 to 60, id 22)

## 4. Design

### The parser

```python
SUFFIX_RE = re.compile(r"(?<=\d)[a-z]+$")

def parse_id_parts(ident: str, root) -> tuple:
    conf = read_root_conf(root)          # the conf dict grammar_for(root) builds through tree_lib.parse_conf
    core = SUFFIX_RE.sub("", ident)
    m = tree_lib.build_id_token_re(tree_lib._id_alternation(conf)).fullmatch(core)
    if m is None or m.group("rev") is not None:
        raise ValueError(f"not an id under this tree's grammar: {ident}")
    return m.group("fam"), m.group("slug"), int(m.group("seq"))
```

`read_root_conf` stands for the conf read `grammar_for(root)` already makes, `tree_lib.parse_conf`
(`tools/memory-tree/tree_lib.py:135`) over the root's `.memory-tree.conf`; the pass reuses that read
and mints no reader of its own. A pinned token `X-y-1@rev-2` is refused, because an id reader
receives an id and a pin is `read_id_pins`' to read.

### Inventory

Minted: `SUFFIX_RE` in `tools/memory-tree/id_grammar.py`. Naming cell: none; the lexicon declares
`py.function`, `py.type`, `js.function` and `sh.function` and no constant cell
(`python tools/lexicon/lexicon.py --suggest SUFFIX_RE --as py.constant` says so).

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`

`TOOL-dTotalRecall-44` also writes this file at order 9, so BUILD-METHOD M6 sequences the two passes.

### Alternatives rejected

- **Name groups inside the era alternation.** `ID_RE` is one alternation of three eras, and named
  groups repeated across alternatives need a separate name per era; `build_id_token_re` already holds
  the one session-era shape with the names.
- **Return `seq` as a string with its suffix.** Unit 38's AC1 and its sort-key reader compare integers.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — `build_id_token_re` compiled once per call site's root; cache it beside `grammar_for`.
- error / empty / loading states — `ValueError` on any id the session-era regex does not match whole.
- observability — the error names the id.
- risks — a caller that wanted a suffixed id kept distinct from its parent sees them sort together;
  no such caller exists at base.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `parse_id_parts("TOOL-dTotalRecall-38", ".")` from
  `id_grammar.py`, it returns `("TOOL", "dTotalRecall", 38)`, and `grep -c 'ID_RE' ` over the function's
  source prints `0`.
  Red when: the parser reads a group `ID_RE` lacks, and the call raises `IndexError`.
- **AC2** — When the same probe calls it with `TOOL-aDrainedSluice-9b`, it returns
  `("TOOL", "aDrainedSluice", 9)`.
  Red when: the suffix raises `ValueError` or reaches `int()`.
- **AC3** — When the probe calls it with `ARCH-001`, `ABL-d119`, `TOOL-x` and `TOOL-dTotalRecall-38@rev-2`,
  each raises `ValueError` naming the id.
  Red when: any of them returns a guessed tuple.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `build-index selftest`

New arm: tools/memory-tree/id_grammar.py · covers AC1 AC2 AC3 · the parser cases plain, suffixed, flat, node-scoped and pinned, staged by reading `ID_RE`'s groups again · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 22
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-63, TOOL-dTotalRecall-64, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `tree_lib.build_id_token_re` (`tools/memory-tree/tree_lib.py:428`), the one
named-group id regex, which `_expand_ids` and `read_id_pins` already match through, with
`tree_lib._id_alternation` (`:416`) for its families. `TOOL-dTotalRecall-38` §10 said no id parser
exists to extend; that held for a parser function, and the regex this unit reads was missed there.
`python tools/codebase-map/reuse_lookup.py "parse a unit id into family slug and sequence"` ranked
name-stem neighbours and not this regex, which is why the probe missed it.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
