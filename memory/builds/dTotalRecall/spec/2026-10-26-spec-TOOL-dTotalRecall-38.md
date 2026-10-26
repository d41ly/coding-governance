# TOOL-dTotalRecall-38 — every id reader that splits on a hyphen parses through the grammar, found by the reader census and proved by the flip probe

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 8 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-5` §4
"The readers" calls its inventory derived, but `id_grammar.py --readers` finds regex literals only.
Ten Python readers take an id's slug by splitting on a hyphen, each verified at base `462d20f3`:
`tools/memory-tree/backlog.py:1042`, `:1407` and `:1664`; `tools/memory-tree/gen_build_index.py:3541`
and `:4073`; `tools/memory-recall/check-recall.py:511`; `tools/memory-recall/query.py:1463`;
`tools/drift-audit/drift_report.py:708`; `tools/memory-tree/migrate_backlog.py:329` and `:337`. Under
the hyphenated `in-slug` flip, `TOOL-d2026-10-26ClosedLoop-3` splits into five parts, so each reader
files, matches or grades against `d2026` or nothing. The flip probe checks only `mint_re`,
`BUILD_SLUG_RE` and `ID_RE`, so it prints `ok` over readers that are wrong. This unit gives the
grammar one id parser, re-points every split reader to it, widens the census to the split shapes, and
makes the flip probe run the parser and the census in the flipped clone. It repairs
`TOOL-dTotalRecall-5`.

## 2. Scope (IN)

- **S1** — One parser, `parse_id_parts(ident, root)` in `tools/memory-tree/id_grammar.py`, returning
  `(family, slug, seq)` from `grammar_for(root).ID_RE` matched whole, `seq` an integer. An ident the
  grammar does not match raises `ValueError` naming it; a caller that today answers `""` or `None`
  for a malformed id catches that and keeps its answer. Observed by AC1.
- **S2** — The census reads the split shapes. `id_grammar.py --readers` also lists every line of its
  population that splits a value on a hyphen where the value's name holds `id`, `slug` or `unit`,
  case ignored: Python `.split("-")` and `.rsplit("-"`, shell `cut -d-` and `cut -d '-'`, `IFS=-`, and
  the expansions `${<name>%-*}`, `${<name>%%-*}`, `${<name>#*-}` and `${<name>##*-}`. The predicate is
  run over the real tree before the first edit, and its hit count is recorded in the pass commit's
  `Decided:` trailer with each hit kept and why. Observed by AC2.
- **S3** — Each split reader S2 lists is re-pointed, by the disposition table `TOOL-dTotalRecall-5` §4
  "The readers" gives its kit. A Python reader calls `parse_id_parts`, reached through its kit's existing
  route to `id_grammar`; a shell reader matches the id against the class
  `check-memory-hygiene.sh --print-slug-class` prints. The ten readers of §1 are among them. A
  reader keeps its own function name, so its callers do not change. Observed by AC2 and AC3.
- **S4** — The flip probe proves the readers. For each flip, `id_grammar.py --flip-probe <clone>`
  checks two more things: `parse_id_parts("TOOL-<new slug>-3", <clone>)` returns the planted slug and the
  sequence `3`; and `--readers` over the clone lists no split-shaped line outside the entry points and
  the kept hits. Under the hyphenated `in-slug` flip, `read_slug` from
  `tools/memory-tree/migrate_backlog.py` and the slug half of `build_id_sort_key` return
  `d2026-10-26ClosedLoop` for `TOOL-d2026-10-26ClosedLoop-3`. Observed by AC4.

## 3. Non-goals (OUT)

- The grammar, its keys, its shell and JavaScript exports and the regex half of the census:
  `TOOL-dTotalRecall-5`'s.
- The marker that excludes a kept hit from the census output: the batch `TOOL-dTotalRecall-43`
  carries it for the round-1 audit's id 13, and it reads S2's widened predicate.
- Splits on other separators, and splits of values whose names do not say they hold an id. The census
  names its shapes; a reader outside them is out of this unit's reach and is stated so in S2.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py`, its `grammar_for` and `ID_RE`, the
  `--readers` predicate S2 widens and the `--flip-probe` S4 extends
- **hands-off** `TOOL-dTotalRecall-43` — the widened `--readers` predicate, whose kept hits that unit's
  marker excludes from the census output (the round-1 audit's id 13)
- **hands-off** `TOOL-dTotalRecall-44` — the widened `--readers` split predicate, which that unit keys on the split's shape (the round-1 audit of units 36 to 43, id 1)
- **hands-off** `TOOL-dTotalRecall-45` — `parse_id_parts` and the re-point routes of §4, which that unit takes for three further readers (the round-1 audit of units 36 to 43, id 35)
- **hands-off** `TOOL-dTotalRecall-46` — `parse_id_parts`, whose body that unit rebuilds on `tree_lib.build_id_token_re` (the round-1 audit of units 36 to 43, id 22)
- **hands-off** `TOOL-dTotalRecall-53` — `--readers`, `--flip-probe` and the re-pointed readers, which that unit marks, probes and holds to their base answers (the round-1 audit of units 36 to 43, ids 2, 9, 13 and 23)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` on `tree_lib.build_id_token_re`, landed in step 8 before this pass; S1 is met by that body, which this pass re-points its readers onto and does not rewrite, as §4's rule for a landed spelling says (the round-1 audit of units 44 to 53, id 1)

## 4. Design

### The parser

```python
def parse_id_parts(ident: str, root) -> tuple:
    m = grammar_for(root).ID_RE.fullmatch(ident)
    if m is None:
        raise ValueError(f"not an id under this tree's grammar: {ident}")
    return m.group("family"), m.group("slug"), int(m.group("seq"))
```

The group names are the ones `TOOL-dTotalRecall-5` S4 gives `ID_RE`; if the landed grammar spells
them otherwise, the pass uses the landed spelling and bumps this spec's rev first.

### The ten readers at base

| Site | Today | After |
|---|---|---|
| `backlog.py:1042`, `:1407` | `ask.id.split("-")[1]` | `parse_id_parts(ask.id, root)[1]`, `""` on `ValueError` |
| `backlog.py:1664` | `parts = ask.id.split("-")` | `parse_id_parts` |
| `gen_build_index.py:3541` | `ask_id.split("-")[1]` | `parse_id_parts` |
| `gen_build_index.py:4073` | sort key from `split("-")` and `rsplit("-", 1)` | `parse_id_parts` |
| `check-recall.py:511` | `i.split("-")[1] != spec["slug"]` | `parse_id_parts` through memory-recall's route |
| `query.py:1463` | `seg = rid.split("-")` | `parse_id_parts` through memory-recall's route |
| `drift_report.py:708` | `parts = uid.split("-")` | `parse_id_parts` through drift-audit's route; both kits require memory-tree |
| `migrate_backlog.py:329`, `:337` | `parts = ident.split("-")` | `parse_id_parts` |

### Inventory

Minted: `parse_id_parts` in `tools/memory-tree/id_grammar.py`; the split shapes of the census. Naming cell:
`parse_id_parts` is asked of `python tools/lexicon/lexicon.py --suggest parse_id_parts --as py.function` at the
pass, and a flagged name takes the lexicon's suggestion before any caller is written.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/query.py`
- `tools/drift-audit/drift_report.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

Each further site S2's census lists at the pass is added here as a rev bump before its edit.

### Alternatives rejected

- **Test each reader's own extraction in the flip probe.** The readers' slug logic sits inside
  functions with other inputs, so a per-site probe would rebuild each caller's context; one parser
  every reader calls, and a census that finds any reader that does not, proves the same thing once.
- **Keep the splits and forbid hyphens in slugs.** It refuses the `in-slug` hyphenated value the clause
  names, which `TOOL-dTotalRecall-5`'s flips table carries.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one compiled regex per root, cached by `grammar_for`.
- error / empty / loading states — an id the grammar refuses raises `ValueError` in `parse_id_parts`; each
  caller keeps its existing answer for a malformed id.
- observability — `--readers` prints each hit with its file and line; the flip probe prints one line
  per check.
- risks — a reader whose value name says nothing about ids escapes the census, which S2 states.
- testing — AC1 to AC4 by the pass; the arms of §7 at the close.
- migration — none: the default grammar parses every existing id as the splits did.
- user docs — none under `help/`: no page covers id parsing.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `parse_id_parts("TOOL-dTotalRecall-38", ".")` from
  `id_grammar.py`, it returns `("TOOL", "dTotalRecall", 38)`; with `"TOOL-x"` it
  raises `ValueError`.
  Red when: the parser splits on a hyphen, or answers a malformed id with a guess.
- **AC2** — When `python id_grammar.py --readers` runs at the pass base, it lists the
  ten lines of §1 among its split hits; at the pass tip it lists none of them, and every split hit it
  still lists is named as kept in the pass commit's `Decided:` trailer.
  Red when: the predicate reads regex literals only, so the base run lists none of the ten.
- **AC3** — When `git grep -nE '(id|slug|unit)[A-Za-z_]*\.r?split\("-"' -- tools/memory-tree
  tools/memory-recall tools/drift-audit` runs at the pass tip, it prints no line outside
  `id_grammar.py` and the kept hits.
  Red when: a re-point is skipped and the split survives in a reader.
- **AC4** — When `python id_grammar.py --flip-probe <clone>` runs over a scratch clone
  under `%TEMP%/<short>`, the hyphenated `in-slug` row prints `ok`, its `parse_id_parts` check returns
  `d2026-10-26ClosedLoop`, and its census check lists no unkept split; with one re-point reverted in
  the clone, that row prints the census check's failure and the probe exits 1.
  Red when: the probe passes over a reader that still splits.
  fixture: the scratch clone `TOOL-dTotalRecall-5` §4 "The flips" makes; the pass makes it.

## 7. Gates

`tier2-review self-test` · `drift-audit selftest` · `drift-audit records` · `backlog migration selftest` · `build-index selftest` · `build README slot contract` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/id_grammar.py · covers AC2 AC4 · the `--readers` split plants `py-split`, `sh-cut` and `sh-expansion`, and the flip probe's census check, staged by reverting one re-pointed reader to its split · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 17 (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-44, TOOL-dTotalRecall-45, TOOL-dTotalRecall-46, TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dTotalRecall-5`'s `id_grammar.py`: its `grammar_for(root).ID_RE` is the
pattern `parse_id_parts` matches, and its `--readers` predicate and `--flip-probe` are the two modes this unit
widens. No id parser exists to extend: `git grep -nE "def (split_id|parse_id|id_parts|unit_slug|slug_of)"
-- tools` printed nothing at base, and `python tools/codebase-map/reuse_lookup.py "parse a unit id into
family slug and sequence"` ranked name-stem neighbours (`parse`, `slug`, `parse_spec_h1`), of which
`tree_lib.parse_spec_h1` reads a spec's H1 and returns the whole id without splitting it.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
