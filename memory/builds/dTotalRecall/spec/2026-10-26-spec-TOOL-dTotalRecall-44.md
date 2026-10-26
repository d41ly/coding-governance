# TOOL-dTotalRecall-44 — the split census keys on the split's shape, so it lists every id reader whatever its value is named

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-build-TOOL-dTotalRecall-44-round2-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-44-round2-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-44-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-44-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-44-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-44-round2-fix-brief.md) | research | — |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**. It shares item **H1** with id 35, which `TOOL-dTotalRecall-45`
closes. `TOOL-dTotalRecall-38` S2 lists a hyphen split only where the split value's name holds `id`,
`slug` or `unit`. Two of that unit's own ten readers split a value named `i`:
`tools/memory-recall/check-recall.py:511` (`i.split("-")[1] != spec["slug"]`) and
`tools/memory-tree/gen_build_index.py:4073` (`i.split("-")[1]` in a sort key), both read at base
`462d20f3`. So unit 38's AC2 is red by construction, and its census prints clean over a reader that
still splits. This unit keys the predicate on the split's shape and reads no value name. It repairs
`TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — The Python split shape. `id_grammar.py --readers` lists a line that calls `.split("-")` or
  `.split('-')` with no maxsplit argument, unless the call is indexed `[0]` at once. The family is the
  text before the first hyphen, so a hyphen inside a slug cannot move index 0, while index 1, a later
  index, a slice, an unpacking and a bound list all can. A `.rsplit("-", 1)` indexed `[1]` or `[-1]` is
  not listed, because it reads the sequence after the last hyphen. The predicate reads no value name.
  Observed by AC1 and AC2.
- **S2** — The shell shapes `TOOL-dTotalRecall-38` S2 names (`cut -d-`, `cut -d '-'`, `IFS=-` and the
  four suffix and prefix expansions) are listed by shape too, whatever the variable is named.
  Observed by AC1.
- **S3** — The plants. The `--readers` fixture gains five planted lines: three it must list
  (`i.split("-")[1]`, `spec_id.split('-')[1][0]` and `fam, slug, seq = x.split("-")`) and two it must
  not (`x.split("-")[0]` and `x.rsplit("-", 1)[1]`), so the shape can fail both ways. Observed by AC1.

## 3. Non-goals (OUT)

- Re-pointing any reader. The ten of unit 38's §1 are unit 38's, and the three further id readers the
  shape finds are `TOOL-dTotalRecall-45`'s.
- The parser `parse_id_parts`: `TOOL-dTotalRecall-38`'s, made sound by `TOOL-dTotalRecall-46`.
- The kept-hit marker: the batch `TOOL-dTotalRecall-53` makes `--readers` read it.
- A data-flow test of whether a split value came from an id regex. The shape is what a reader of an
  id does, and a non-id hit is kept by name.

### Edges

- **consumes-from** `TOOL-dTotalRecall-38` — the widened `--readers` split predicate and its fixture,
  whose name condition this unit replaces with the shape
- **hands-off** `TOOL-dTotalRecall-53` — the shape-keyed split census, whose index-0 and kept splits that unit marks and whose flip case it extends (ids 9, 13 and 23)
- **hands-off** `TOOL-dTotalRecall-60` — the split predicate and AC2's thirteen sites, which that unit widens to maxsplit and rsplit shapes and matches by line text (the round-1 audit of units 44 to 53, ids 20 and 39)

## 4. Design

### The predicate

```text
python  \.split\((["'])-\1\)(?!\[0\])        a split with no maxsplit, not indexed [0]
shell   cut -d ?'?-'? | IFS=- | \$\{[A-Za-z_]+(%%?-\*|##?\*-)\}
```

The JavaScript half of the census is unit 5's regex-literal arm and is unchanged.

### The reading at base

`git grep -nE "\.r?split\(['\"]-['\"]" -- tools` printed 27 lines at base `462d20f3` (PINNED,
2026-10-26). S1's shape lists 16 of them: unit 38's ten; `tools/branch-reconcile/branch_reconcile.py:520`,
`tools/memory-tree/gen_build_index.py:8576` and `tools/memory-tree/row_grammar.py:1116`, three id readers
outside unit 38's table; and `tools/govkit/selftest.py:379`, `tools/memory-tree/row_grammar.py:1730`
and `tools/run-gates/measure_legs.py:607`, which split a file name or a date and are kept. The other
eleven are a `[0]`, a maxsplit or an `rsplit` sequence read, for example
`tools/memory-tree/gen_build_index.py:3793` and `tools/memory-tree/backlog.py:1683`, which take the
family at index 0.

### Inventory

Minted: none. The plants join the fixture `TOOL-dTotalRecall-38` S2 builds.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`

`TOOL-dTotalRecall-46` also writes this file at order 9, so BUILD-METHOD M6 sequences the two passes.

### Alternatives rejected

- **Add `i` to the name list.** The next reader named `x` or `rid` escapes the same way.
- **Trace each split's receiver back to an id regex.** It needs a data-flow pass the census does not
  have, and the shape already separates the readers that break from those that do not.

## 5. Production-readiness checklist

- security — no new surface: a read-only census.
- perf / scale — one regex per line over the tool root, as today.
- error / empty / loading states — an empty census prints its count, `0 split reader(s)`.
- observability — each hit prints its path, line and shape.
- risks — a non-id split of the same shape is listed; it is kept by name, so a false hit costs one
  line of record and never a silent pass.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no page covers the census.

## 6. Acceptance criteria

- **AC1** — When `python id_grammar.py --readers` runs over the fixture holding S3's five plants, it
  lists the three positive plants and neither negative one.
  Red when: the predicate still reads the value's name, so `i.split("-")[1]` is not listed, or it lists
  a `[0]` read.
- **AC2** — When the tip's `id_grammar.py --readers` runs in a scratch worktree checked out at the
  parent of `TOOL-dTotalRecall-38`'s pass commit, it lists each of the ten lines of that unit's §1,
  `check-recall.py:511` and `gen_build_index.py:4073` among them, and the three further id readers of §4.
  Red when: any of those thirteen lines is not listed.
  fixture: the scratch worktree under the run's scratch directory; the pass makes it.
- **AC3** — When `python id_grammar.py --readers` runs at the pass tip, every split hit it lists is
  either kept in a pass commit's `Decided:` trailer or one of the three readers `TOOL-dTotalRecall-45`
  re-points.
  Red when: an unkept id reader is listed that no unit re-points.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `build-index selftest`

New arm: tools/memory-tree/id_grammar.py · covers AC1 · the five shape plants, staged by restoring the value-name condition · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 1
  (HIGH, item H1 shared with id 35).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dTotalRecall-38` S2's split predicate inside `id_grammar.py --readers`
(`TOOL-dTotalRecall-5`), its one census; this unit changes its key and adds no walker.
`python tools/codebase-map/reuse_lookup.py "list every hyphen split that reads an id"` ranked name-stem
neighbours and no census of split shapes, so no existing seam fits beside that predicate.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
