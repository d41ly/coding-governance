# TOOL-dTotalRecall-46 — the `parse_id_parts` unit 54 built reads the named groups of `tree_lib.build_id_token_re`, and a correction suffix parses

**Status:** INPROGRESS · rev-7 · 2026-11-22 · node d · Tier-2 · base b71b6dd0 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-46-deviation-461.md](../build/2026-10-26-build-TOOL-dTotalRecall-46-deviation-461.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-46-deviation-462.md](../build/2026-10-26-build-TOOL-dTotalRecall-46-deviation-462.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-46-reground-2-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-46-reground-2-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-46-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-46-reground-return.md) | research | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-46-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-46-reground-2-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-reground-2-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-46-reground-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-reground-2-spec-writer.md) | log | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-46-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-46-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-38` S1
at base `462d20f3` built `parse_id_parts` by reading `m.group("family")`, `m.group("slug")` and
`m.group("seq")` from `grammar_for(root).ID_RE`. That regex is built from unnamed alternations
(`tools/memory-tree/id_grammar.py#build_grammar` over `tools/memory-tree/id_grammar.py#_eras`, where
PLAY-dOrderedCharter-18 moved them out of `extract.py`), and `TOOL-dTotalRecall-5` S4 names none, so
every call raises `IndexError: no such group`. Its `int(seq)` also raises on a correction id such as
`TOOL-aDrainedSluice-9b`, which the session era's `[a-z]*` tail admits (`#_eras`). The named groups
already exist: `tools/memory-tree/tree_lib.py#build_id_token_re` carries `fam`, `slug`, `seq` and
`rev`, and unit 5 S13 bound its slug class to the grammar at step 7 (`202a354a4`,
`tools/memory-tree/tree_lib.py#read_slug_class`). `TOOL-dTotalRecall-54` built the parser on that
regex at step 8 (`74af3faa4`), and this unit observes it. It repairs `TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — The parser is `TOOL-dTotalRecall-54`'s. `parse_id_parts(ident, root, *, alt=None)` in
  `tools/memory-tree/id_grammar.py`, landed at step 8 (`74af3faa4`), matches `ident` whole with
  `tree_lib.build_id_token_re(alt, root)`, reached through `load_sibling`, `alt` by default
  `grammar_for(root).families` joined, and returns `(family, slug, seq)` from the groups `fam`,
  `slug` and `seq`. This unit's pass builds no body and observes that one. Observed by AC1.
- **S2** — A correction suffix parses. Before the match unit 54's body strips one trailing run of
  lowercase letters after the final digits, the session era's `[a-z]*`, so `TOOL-aDrainedSluice-9b`
  returns `("TOOL", "aDrainedSluice", 9)`. No re-pointed caller reads the suffix (DERIVED 2026-11-22,
  `git grep -n parse_id_parts -- tools`): seven take the slug, and three sort keys compare the
  sequence as a number (`tools/memory-tree/backlog.py#build_ask_sort_key`,
  `tools/memory-tree/migrate_backlog.py#build_id_sort_key`, the `ids.sort` key in
  `tools/memory-tree/gen_build_index.py#cmd_new_build`), where the split shape
  `int(i.rsplit("-", 1)[1])` still spelled by `tools/memory-tree/gen_build_index.py#_roster_sort_key`
  raises on the same id. Observed by AC2.
- **S3** — Unit 54's body raises `ValueError` naming any id `build_id_token_re` does not
  match whole, a flat-era `ARCH-001` and a node-scoped `ABL-d119` among them, and each caller keeps
  the answer it gives a malformed id. Observed by AC3.

## 3. Non-goals (OUT)

- The grammar, `grammar_for`, `ID_RE` and the slug class: `TOOL-dTotalRecall-5`'s.
- Which callers parse: `TOOL-dTotalRecall-38`'s ten and `TOOL-dTotalRecall-45`'s four.
- What each re-pointed caller answered for the flat and node-scoped eras: the batch
  `TOOL-dTotalRecall-53` holds that answer equal to base for id 2.
- Returning the suffix. A caller that needs it is a later unit's, which widens the tuple then.

### Edges

- **consumes-from** `TOOL-dTotalRecall-38` — the ten readers re-pointed onto `parse_id_parts`,
  whose body unit 54 builds and this unit's criteria observe
- **consumes-from** `TOOL-dTotalRecall-5` — `tree_lib.build_id_token_re` with its slug class bound from
  the grammar, the named-group regex this parser matches
- **hands-off** `TOOL-dTotalRecall-53` — `parse_id_parts` on `build_id_token_re`, whose answers for the flat and node-scoped eras that unit holds to base (id 2)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` on `build_id_token_re`, already built at step 8, which this unit's AC1 to AC3 observe (the round-1 audit of units 44 to 53, id 1)
- **hands-off** `TOOL-dTotalRecall-60` — the parser's family read and its era refusal, which that unit re-observes with the cited and declared families (the round-1 audit of units 44 to 53, ids 18 and 19)
- **consumes-from** `TOOL-dTotalRecall-63` — AC1's cited-family case, written into this spec in step 9 before this pass (the round-1 audit of units 54 to 60, id 3)
- **consumes-from** `TOOL-dTotalRecall-64` — S1, §4 and the edge to unit 38 as that unit amends them in step 9 before this pass, so this pass observes unit 54's body and builds none (the round-1 audit of units 54 to 60, id 22)

## 4. Design

### The parser

Unit 54's body (`TOOL-dTotalRecall-54` §4), which this unit observes. `tree_lib._id_alternation` is not
read: it builds from conf `FAMILIES` alone (`tools/memory-tree/tree_lib.py#_id_alternation`) and omits
cited families. A pinned token `X-y-1@rev-2` is refused, because an id reader receives an id.

### Inventory

Minted: nothing.

### Files touched (estimate)

none: the pass observes unit 54's body

### Alternatives rejected

- **Build the body here.** Unit 54 builds it at step 8, so a second body would overwrite the
  cited-family read.
- **Return `seq` as a string with its suffix.** Unit 38's AC1 and its sort-key reader compare integers.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — none: unit 54's body
- error / empty / loading states — `ValueError` on any id the session-era regex does not match whole.
- observability — the error names the id.
- risks — a caller that wanted a suffixed id kept distinct from its parent sees them sort together;
  none exists at HEAD: two sort keys break the tie on the whole id, and `cmd_new_build` sorts ids
  `read_idlist` admitted through `build_id_token_re`, whose `\d+$` takes no suffix.
- testing — AC1 to AC3 by the pass
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe run from the repository root, with `tools/memory-tree` on
  `sys.path`, calls `id_grammar.parse_id_parts("TOOL-dTotalRecall-38", ".")`, it returns
  `("TOOL", "dTotalRecall", 38)`, and `grep -c 'ID_RE'` over the function's `inspect.getsource`
  prints `0` (grep exits 1 on no match). In a scratch tree whose `.memory-tree.conf` declares `RECALL_CITED_FAMILIES` with
  `ZED`, the call on `ZED-aFoo-2` returns `("ZED", "aFoo", 2)`.
  That conf also declares `MEMORY_ROOT` and `FAMILIES`, without which `id_grammar.py#resolve` refuses.
  Red when: the parser reads a group `ID_RE` lacks, or refuses a cited family.
  fixture: the scratch tree under the run's scratch directory; the pass makes it.
- **AC2** — When the same probe calls it with `TOOL-aDrainedSluice-9b`, it returns
  `("TOOL", "aDrainedSluice", 9)`.
  Red when: the suffix raises `ValueError` or reaches `int()`.
- **AC3** — When the probe calls it with `ARCH-001`, `ABL-d119`, `TOOL-x` and `TOOL-dTotalRecall-38@rev-2`,
  each raises `ValueError` naming the id.
  Red when: any of them returns a guessed tuple.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `build-index selftest` · `memory-recall kit selftest` · `drift-audit selftest` · `playbook render selftest` · `policy fixtures`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Does the re-ground fold units 63's and 64's amendments into this spec?** At base `c2143acf` no
  `parse_id_parts` exists; `TOOL-dTotalRecall-54` lands it at step 8 on `grammar_for(root).families`,
  and `TOOL-dTotalRecall-64` S1 to S4 rewrite this spec's S1, §4, §5, §7 New arm line, §10 and the
  edge to unit 38 to observe that body, with `TOOL-dTotalRecall-63` S1 adding AC1's cited case, both
  in their own order-9 passes ahead of this one. Options: (a) fold both now; (b) re-ground only what
  the landed tree moved and leave the rewrite to those passes. (a) does their passes' work, so their
  AC1 greps could never be seen red (veto 1), and changes Scope intent the re-ground brief bars.
  RESOLVED (agent, 2026-11-22, delegated): (b), the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 22
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-63, TOOL-dTotalRecall-64, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-4 · 2026-11-22 · §1 S1 §4 §7 §8 §10 · re-grounded at base `c2143acf` per
  `2026-11-22-prompt-TOOL-dTotalRecall-46-reground-brief`: §1 and §10 cite `build_grammar`, `_eras`,
  `build_id_token_re` and `_id_alternation` as `path#symbol`; S1 cites `read_spec_revs`; §4's conf
  read is `id_grammar.py#load_conf`, not `tree_lib.parse_conf`, and its Inventory names unit 54's
  `SUFFIX_RE` and the five declared lexicon cells; §7 names the four further legs guarding
  `id_grammar.py`; F2 leaves units 63's and 64's amendments to their passes.
- rev-5 · 2026-11-22 · AC1 · the cited-family case, added by TOOL-dTotalRecall-63 (id 3, item H3 shared with id 22)
- rev-6 · 2026-11-22 · S1 S2 S3 §4 §5 §7 §10 §3 · amended by TOOL-dTotalRecall-64 (id 22, item H3)
  so this pass observes unit 54's body and builds none: S1 names `parse_id_parts` as landed at
  `74af3faa4`, S2 and S3 read as observations of it; §4's code block, its conf-read paragraph, the
  `SUFFIX_RE` mint and the file estimate give way, the first alternative rejecting a second body;
  §5 perf and testing follow; §7's New arm line is struck, unit 54's arm covering the same cases at
  the close; §10 names unit 54's body as the seam; the consumes-from edge to unit 38 names unit 54 as
  the body's builder.
- rev-7 · 2026-11-22 · title §1 S2 §3 §5 AC1 §8 · re-grounded at base `b71b6dd0` per
  `2026-11-22-prompt-TOOL-dTotalRecall-46-reground-2-brief`: the title and §1 name unit 54 as the
  parser's builder and this unit as its observer; S2 names the three sort keys at HEAD; §3 counts
  unit 45's four readers; §5's risk is checked at HEAD; AC1's probe runs from the repository root,
  where `tools/memory-tree/` stopped on the conf refusal, and names the scratch conf's two required
  keys; F2 says base where it said HEAD.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-54`'s body, `tools/memory-tree/id_grammar.py#parse_id_parts` on
`tools/memory-tree/tree_lib.py#build_id_token_re`, the one named-group id regex, its `alt` by default
`grammar_for(root).families` (`tools/memory-tree/id_grammar.py#grammar_for`); this unit observes it
and mints nothing. `tools/memory-tree/tree_lib.py#_id_alternation` is only the read it rejects, conf
`FAMILIES` without the cited families. `TOOL-dTotalRecall-38` §10 said no id parser
exists to extend; that held for a parser function, and the regex this unit reads was missed there.
`python tools/codebase-map/reuse_lookup.py "parse a unit id into family slug and sequence"` ranked
name-stem neighbours and not this regex at base `462d20f3`, which is why the probe missed it.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
