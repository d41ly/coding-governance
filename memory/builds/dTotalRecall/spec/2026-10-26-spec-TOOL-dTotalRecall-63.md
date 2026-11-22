# TOOL-dTotalRecall-63 — unit 46's own pass reds a parser that refuses a cited family, so unit 54's body is held at step 9

**Status:** DEFERRED · rev-4 · 2026-11-22 · node d · Tier-2 · base 94e17798 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-63-deviation-631.md](../build/2026-10-26-build-TOOL-dTotalRecall-63-deviation-631.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-63-reground-2-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-63-reground-2-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-63-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-63-reground-return.md) | research | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-spec-writer.md) | log | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-64 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**. It shares item **H3** with id 22, which `TOOL-dTotalRecall-64`
closes. `TOOL-dTotalRecall-54` §3 says unit 46's pass "builds nothing this unit has built", and its
§4 rejects `tree_lib._id_alternation` because it reads conf `FAMILIES` only and omits cited
families (`tools/memory-tree/tree_lib.py#_id_alternation`). Nothing observes that claim at unit 46's
pass. Unit 46's AC1 to AC3 plant no cited family, unit 54's AC4 is observed at unit 38's tip only, and unit 54's arm, which does plant
one, runs at the close with the bar. So a unit-46 pass that rebuilds the body onto
`_id_alternation` passes its own criteria at step 9, and every cited-family id then raises
`ValueError` in each re-pointed reader that takes the default alternation, surfacing only at the
close: unit 38's `tools/drift-audit/drift_report.py#_parse_slug`,
`tools/memory-recall/check-recall.py#derive_probe_labels` and
`tools/memory-recall/query.py#measure_answer_used`, and unit 45's readers. A caller that binds
`alt` (`tools/memory-tree/backlog.py#ANY_FAMILY`, or `_id_alternation(conf)` in
`tools/memory-tree/gen_build_index.py#cmd_new_build`) keeps its own answer.

Unit 64 corrects what unit 46 designs. This unit makes unit 46's own pass observe the cited family,
so a rebuild is red at step 9 and not at the close: unit 46's AC1 gains unit 54's cited case, and
unit 54's claim is observed at unit 46's tip. It repairs `TOOL-dTotalRecall-54`.

## 2. Scope (IN)

- **S1** — The cited case joins unit 46's criterion. `TOOL-dTotalRecall-46` AC1 gains §4's clause: in a
  scratch tree whose `.memory-tree.conf` declares `RECALL_CITED_FAMILIES` with `ZED`,
  `parse_id_parts("ZED-aFoo-2", tree)` returns `("ZED", "aFoo", 2)`. Its Red-when names a refused
  cited family. The amendment is a rev bump with its §9 line naming this unit, written in this
  unit's pass ahead of unit 46's by the §3 edge. Observed by AC1.
- **S2** — Unit 54's claim is observed at unit 46's tip. There the parser still reads the families
  `grammar_for(root)` reads and spells no `_id_alternation`, and unit 54's pass commit precedes unit
  46's. Observed by AC2.

## 3. Non-goals (OUT)

- What unit 46 designs and builds: `TOOL-dTotalRecall-64` amends its S1, §4 and edge for id 22.
- The parser body: `TOOL-dTotalRecall-54`'s, unchanged.
- The refusal plants for a malformed slug: the batch `TOOL-dTotalRecall-66` adds them for id 39.

### Edges

- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` and its cited-family fixture, landed at
  step 8 in `74af3faa4`, whose behaviour this unit's criterion carries into unit 46's pass
- **hands-off** `TOOL-dTotalRecall-46` — AC1's cited-family case, which that unit's pass observes over
  the body it does not rebuild
- **hands-off** `TOOL-dTotalRecall-70` — the amendment to unit 46 and AC2, which that unit re-reads with the fixture conf spelled whole and by ancestry (the round-1 audit of units 61 to 66, ids 9, 12, 31 and 33)

## 4. Design

### The amendment to unit 46

AC1 of `TOOL-dTotalRecall-46` gains, after its present first sentence, the clause and fixture below,
and its present Red-when line, which names `IndexError` alone, gives way to the one quoted:

> In a scratch tree whose `.memory-tree.conf` declares `RECALL_CITED_FAMILIES` with `ZED`, the call on
> `ZED-aFoo-2` returns `("ZED", "aFoo", 2)`. Red when: the parser reads a group `ID_RE` lacks, or
> refuses a cited family. fixture: the scratch tree under the run's scratch directory; the pass makes
> it.

The rev bump's §9 line, one line, reads
`rev-<N> · <date> · AC1 · the cited-family case, added by TOOL-dTotalRecall-63 (id 3, item H3 shared with id 22)`.

### Why this catches the rebuild

`_id_alternation(conf)` builds its alternation from `FAMILIES` alone, so a body built on it refuses
`ZED-aFoo-2` with `ValueError` while unit 54's default, `"|".join(grammar_for(root).families)` when
`alt` is None (`tools/memory-tree/id_grammar.py#parse_id_parts`), admits it,
`grammar_for` building through `conf.families + conf.cited_families`
(`tools/memory-tree/id_grammar.py#build_grammar`, where PLAY-dOrderedCharter-18 moved it out of
`extract.py`). The case therefore separates the two bodies by behaviour, and the source count of AC2 names which one stands.
Observed on 2026-11-22 at `94e17798` in a scratch tree declaring `FAMILIES="tooling:TOOL"` and
`RECALL_CITED_FAMILIES="ZED"`: the default call returns the tuple, and the same call with
`alt=tree_lib._id_alternation(id_grammar.load_conf(tree))`, which is `TOOL`, raises `ValueError`.

### Order inside step 9

Units 64 and this one both write unit 46's spec, so BUILD-METHOD M6 sequences them; either order
serves, and both precede unit 46's pass by their edges.

### Inventory

Minted: nothing in code. Amended: unit 46's AC1.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md`

### Alternatives rejected

- **Rely on unit 54's arm.** It runs at the close with the bar, after units 38 to 60 have built on a
  broken body.
- **Place the observation after unit 46, at order 10.** A red there cannot make unit 46's own pass
  red, so the rebuild would already be committed.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — one more probe call in unit 46's pass.
- error / empty / loading states — a refused cited family is unit 46's AC1 red.
- observability — the probe prints the tuple or the `ValueError`.
- risks — unit 46's rev moves after its audit; the new text is this spec's §4, which the audit of
  this unit reviews.
- testing — AC1 by the pass; AC2 at unit 46's pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `grep -n "ZED-aFoo-2"` runs over
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md` at this pass's tip it
  prints the AC1 line, and `grep -c "added by TOOL-dTotalRecall-63"` over that spec prints at least 1.
  Red when: unit 46's AC1 plants no cited family, or its §9 carries no amendment line.
- **AC2** — When unit 46's pass tip is reached, a `python -c` probe run from `tools/memory-tree/`
  over the scratch tree of §4 finds `parse_id_parts("ZED-aFoo-2", tree)` returns `("ZED", "aFoo", 2)`,
  the probe
  `python -c "import inspect, id_grammar; print(inspect.getsource(id_grammar.parse_id_parts).count('_id_alternation'))"`
  run there prints `0`, and `git log --reverse --format=%s` lists unit 54's pass commit (`74af3faa4`)
  before unit 46's.
  Red when: unit 46's pass rebuilt the body onto `_id_alternation`, or it refuses a cited family.
  fixture: the scratch tree under the run's scratch directory; unit 46's pass makes it.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: unit 54's arm, `tools/memory-recall/selftest.py#test_id_parts_parse_under_each_tree_grammar`
(its §7 New arm, §8 F2), already plants the cited case at the close; this unit moves its observation into unit 46's pass.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, id 3
  (HIGH, item H3 shared with id 22).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-70, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-3 · 2026-11-22 · §1 §4 §6 §7 §10 · re-grounded at base `c2143acf` per
  `2026-11-22-prompt-TOOL-dTotalRecall-63-reground-brief`: `_id_alternation` and `build_grammar`
  (moved to `id_grammar.py` by PLAY-dOrderedCharter-18) cited as `path#symbol`; §1 names the close, not a
  stale order number; §4 replaces unit 46's rev-4 `IndexError` Red-when and keeps the §9 line on one line;
  AC1 greps the amendment's own form, as unit 46's rev-3 edge-fold line already held the bare id; AC2's
  tuple is returned, not printed; §7 homes unit 54's arm in `tools/memory-recall/selftest.py`.
- rev-4 · 2026-11-22 · §1 §3 §4 §6 §7 · re-grounded at base `94e17798` per
  `2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-brief`, over unit 54 and unit 38 as built: §1
  names the default-alternation readers a rebuild breaks and the `alt`-binding callers it spares;
  §3 and AC2 pin unit 54's pass commit `74af3faa4`; §4 cites the `alt is None` default and the red
  observed with `_id_alternation`; AC2 runs both probes from `tools/memory-tree/` and reads the log
  with `--reverse`, since newest-first lists unit 46's commit first; §7 names the arm by symbol.

## 10. Reuse audit

The seam is unit 54's cited-family fixture (`TOOL-dTotalRecall-54` AC1) and the family read it rests
on, `grammar_for(root).families` (`tools/memory-tree/id_grammar.py#build_grammar`), moved into the criterion of
the pass that could break it. `python tools/codebase-map/reuse_lookup.py "amend a sibling spec before its unit builds"`
ranked name-stem neighbours and no seam for sequencing an observation, so no existing seam fits
beyond the fixture named here.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
