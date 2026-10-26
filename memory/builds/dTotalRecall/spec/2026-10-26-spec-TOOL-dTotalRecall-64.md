# TOOL-dTotalRecall-64 — unit 46's spec observes unit 54's parser body and designs none of its own

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**. It shares item **H3** with id 3, which `TOOL-dTotalRecall-63`
closes. `TOOL-dTotalRecall-54` lands `parse_id_parts` at step 8 on `grammar_for(root).families` and
rejects `tree_lib._id_alternation`, which reads conf `FAMILIES` only (`tree_lib.py:416-418`). But
`TOOL-dTotalRecall-46` was only edge-folded, its rev-2 log reading "nothing else moved". Its S1 and
§4 code still build the body on `tree_lib.build_id_token_re(tree_lib._id_alternation(conf))`, with a
`read_root_conf` that exists nowhere in the tree, and its consumes-from edge to unit 38 still reads
"whose body this unit rebuilds". Unit 38's hands-off line says the same. Two units design one
function body, and a unit-46 builder following its S1 overwrites unit 54's cited-family body at step
9.

This unit finishes the supersession unit 54 began: unit 46's spec observes unit 54's body and
designs none, and unit 38's line names unit 54 as the builder. It repairs `TOOL-dTotalRecall-54`.

## 2. Scope (IN)

- **S1** — Unit 46's S1 names unit 54's body. `TOOL-dTotalRecall-46` S1 takes §4's text: the parser is
  the one unit 54 landed at step 8, and unit 46's pass builds no body of its own. Its S2 and S3 read
  as observations of that body. Observed by AC1 and AC2.
- **S2** — Unit 46's §4 carries no second design. Its parser code block, its `read_root_conf`
  paragraph and its first alternative give way to §4's text; its §5 perf line, Files touched, §7 New
  arm line and §10 follow. Observed by AC1.
- **S3** — The edges agree. Unit 46's consumes-from line to unit 38 and unit 38's hands-off line to
  unit 46 name unit 54 as the body's builder. Observed by AC1.
- **S4** — The amendments land before unit 46's pass, each a rev bump with its §9 line naming this
  unit, in this unit's pass at order 9, which unit 46 consumes by a §3 edge. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The body: `TOOL-dTotalRecall-54`'s, unchanged.
- The cited-family case in unit 46's AC1: `TOOL-dTotalRecall-63`'s, for id 3.
- Retiring unit 46. Its criteria still observe the body at step 9 and units 53 and 60 consume them,
  so it stays and builds nothing.
- Unit 38's own scope, which re-points readers onto the body and is unchanged.

### Edges

- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` on `grammar_for(root).families`, the
  body unit 46's amended S1 names
- **hands-off** `TOOL-dTotalRecall-46` — S1, §4 and the edge to unit 38 amended so that unit's pass
  observes `parse_id_parts` and builds no body
- **hands-off** `TOOL-dTotalRecall-70` — the amendments to units 46 and 38 and AC1 and AC2, which that unit re-reads over joined text and both segments, recording unit 38's departure (the round-1 audit of units 61 to 66, ids 5, 9, 10, 11, 14, 31 and 32)

## 4. Design

### The amendments to unit 46

Each is a rev bump with one §9 line of the form
`rev-<N> · <date> · S1 S2 S3 §4 §5 §7 §10 §3 · amended by TOOL-dTotalRecall-64 (id 22, item H3) ...`.

- S1:

  > **S1** — The parser is `TOOL-dTotalRecall-54`'s. `parse_id_parts(ident, root)` in
  > `tools/memory-tree/id_grammar.py`, landed at step 8, matches `ident` whole with
  > `tree_lib.build_id_token_re` over `grammar_for(root).families` and returns `(family, slug, seq)`
  > from the groups `fam`, `slug` and `seq`. This unit's pass builds no body and observes that one.
  > Observed by AC1.

- S2 and S3 open "Unit 54's body" where they now open "Before the match the parser" and "An id".
- §4 "The parser" reads, in place of its code block and the paragraph under it: "Unit 54's body
  (`TOOL-dTotalRecall-54` §4), which this unit observes. `tree_lib._id_alternation` is not read: it
  builds from conf `FAMILIES` alone (`tree_lib.py:416-418`) and omits cited families. A pinned token
  `X-y-1@rev-2` is refused, because an id reader receives an id."
- §4 Inventory reads "Minted: nothing." Files touched reads "none: the pass observes unit 54's body",
  and its M6 sentence is struck. The first alternative reads "Build the body here. Unit 54 builds it
  at step 8, so a second body would overwrite the cited-family read."
- §5 perf / scale reads "none: unit 54's body"; testing reads "AC1 to AC3 by the pass".
- §7: the New arm line is struck, unit 54's arm covering the same cases at the close.
- §10: the seam sentence names `TOOL-dTotalRecall-54`'s body and `grammar_for(root).families`, and
  `_id_alternation` only as the read it rejects.
- §3: the consumes-from line to unit 38 reads "the ten readers re-pointed onto `parse_id_parts`,
  whose body unit 54 builds and this unit's criteria observe".

### The amendment to unit 38

Its hands-off line to unit 46 reads "`parse_id_parts`, whose body `TOOL-dTotalRecall-54` builds on
`tree_lib.build_id_token_re` and that unit observes", with a rev bump and a §9 line naming this unit.

### Inventory

Minted: nothing in code. Amended: the two spec files below.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md`

`TOOL-dTotalRecall-63` also writes unit 46's spec at order 9, so BUILD-METHOD M6 sequences the two
passes; both precede unit 46's.

### Alternatives rejected

- **An edge-fold on unit 46 alone.** It is what left S1 and §4 standing; the class is an amendment
  that leaves its other half standing.
- **Retire unit 46 as superseded.** Its criteria are consumed by units 53 and 60, and a retirement
  written mid-run changes no roster the harness already handed out.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — none.
- error / empty / loading states — none at runtime; a missing amendment is AC1's red.
- observability — each amended spec's §9 line names this unit and the finding.
- risks — unit 46's and unit 38's revs move after their audit; the new text is this spec's §4, which
  the audit of this unit reviews.
- testing — AC1 by the pass; AC2 at unit 46's pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `grep -cE "read_root_conf|_id_alternation\(conf\)|whose body this unit rebuilds"` runs
  over `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md` at this pass's tip
  it prints `0`, `grep -c "whose body that unit rebuilds"` over
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md` prints `0`, and
  `grep -c TOOL-dTotalRecall-64` over each file's §9 prints at least 1.
  Red when: either spec still designs or promises a second body.
- **AC2** — When unit 46's pass tip is reached, a `python -c` probe reading `parse_id_parts` with
  `ast.get_source_segment` from `git show <unit 54's pass commit>` of `id_grammar.py`, run from
  `tools/memory-tree/`, and from the working file prints the two segments equal.
  Red when: unit 46's pass rewrote the body.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: this unit writes spec text, and unit 54's arm holds the body at the close.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, id 22
  (HIGH, item H3 shared with id 3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-70, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is unit 54's body, `parse_id_parts` on `tree_lib.build_id_token_re`
(`tools/memory-tree/tree_lib.py:428`) over `grammar_for(root).families`
(`tools/memory-recall/extract.py:599`); unit 46 reads it and mints nothing. `git grep -n read_root_conf -- tools`
printed nothing here, so the conf read unit 46 §4 names does not exist.
`python tools/codebase-map/reuse_lookup.py "amend a sibling spec before its unit builds"` ranked
name-stem neighbours and no seam for an amendment, so no existing seam fits beyond the body named here.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
