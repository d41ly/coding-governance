# TOOL-dTotalRecall-38 — every id reader that splits on a hyphen parses through the grammar, found by the reader census and proved by the flip probe

**Status:** DEFERRED · rev-4 · 2026-11-22 · node d · Tier-2 · base 8b8b1374 · streams tooling · order 8 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-38-deviation-381.md](../build/2026-10-26-build-TOOL-dTotalRecall-38-deviation-381.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-38-deviation-382.md](../build/2026-10-26-build-TOOL-dTotalRecall-38-deviation-382.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-38-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-38-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-38-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-38-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-38-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-38-reground-spec-writer.md) | journal | — |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-5` §4
"The readers" calls its inventory derived, but its `id_grammar.py --readers` finds regex literals only.
Ten Python readers take an id's slug by splitting on a hyphen. Each was verified at base `462d20f3` and
again at `c344bdc40` under these names: `tools/memory-tree/backlog.py#derive_verdicts`,
`tools/memory-tree/backlog.py#derive_ready`, `tools/memory-tree/backlog.py#build_ask_sort_key`,
`tools/memory-tree/gen_build_index.py#build_grade_row`, `tools/memory-tree/gen_build_index.py#cmd_new_build`
(its asks' sort key), `tools/memory-recall/check-recall.py#derive_probe_labels`,
`tools/memory-recall/query.py#measure_answer_used`, `tools/drift-audit/drift_report.py#_parse_slug`,
`tools/memory-tree/migrate_backlog.py#build_id_sort_key` and `tools/memory-tree/migrate_backlog.py#read_slug`.
Under the hyphenated `in-slug` flip, `TOOL-d2026-10-26ClosedLoop-3` splits into five parts, so each
reader files, matches or grades against `d2026` or nothing. Unit 5's flip probe checks only `mint_re`,
`BUILD_SLUG_RE` and `ID_RE`, so it prints `ok` over readers that are wrong. This unit re-points every
split reader onto the one id parser, `parse_id_parts`, which `TOOL-dTotalRecall-54` lands earlier in
this step. It also widens the census to the split shapes and makes the flip probe run the parser and
the census in the flipped clone. It repairs `TOOL-dTotalRecall-5`.

## 2. Scope (IN)

- **S1** — The one parser is `parse_id_parts(ident, root)` in `tools/memory-tree/id_grammar.py`, as
  `TOOL-dTotalRecall-54` lands it earlier in step 8 on the named groups `fam`, `slug` and `seq` of
  `tools/memory-tree/tree_lib.py#build_id_token_re`. It returns `(family, slug, seq)` with `seq` an
  integer and raises `ValueError` naming an ident it does not match whole. This pass writes no parser
  body. `grammar_for(root).ID_RE` carries no named group (`tools/memory-tree/id_grammar.py#build_grammar`),
  so a body on it raises `IndexError`. A caller that today answers `""`, `None` or the id itself for a
  malformed id catches the `ValueError` and keeps that answer. A reader with no root in scope passes
  `None`, the default grammar of the tree its module lives in (`tools/memory-tree/id_grammar.py#grammar_for`).
  Observed by AC1.
- **S2** — The census reads the split shapes. `id_grammar.py --readers` also lists every line of its
  population that splits a value on a hyphen where the value's name holds `id`, `slug` or `unit`,
  case ignored: Python `.split("-")` and `.rsplit("-"`, shell `cut -d-` and `cut -d '-'`, `IFS=-`, and
  the expansions `${<name>%-*}`, `${<name>%%-*}`, `${<name>#*-}` and `${<name>##*-}`. The predicate is
  run over the real tree before the first edit, and its hit count is recorded in the pass commit's
  `Decided:` trailer with each hit kept and why. A split answers right under a hyphenated slug, and is
  kept with that reason, when it reads the family at index 0, reads the sequence after the last hyphen,
  or strips exactly the first and the last segment. A value that is not a unit id is kept, naming what
  it is. The predicate reads the value's name, so the two `i`-named readers of §1 are not listed (§8 F2).
  Observed by AC2.
- **S3** — Each of the ten readers of §1 is re-pointed, whether S2 lists it or not, by the disposition
  table that `TOOL-dTotalRecall-5` §4 "The readers" gives its kit. A Python reader calls
  `parse_id_parts`, reached through its kit's existing route to `id_grammar`. In memory-tree that route
  is a sibling import. In memory-recall it is the `id_grammar` module that
  `tools/memory-recall/extract.py#resolve_kit_dir` puts on the path. In drift-audit it is
  `tools/drift-audit/drift_report.py#load_memory_tree`. Both of those kits require memory-tree
  (`tools/memory-recall/kit.toml@c344bdc40:8`, `tools/drift-audit/kit.toml@c344bdc40:15`). Every other
  hit S2 lists is re-pointed the same way or kept by S2's reasons. A shell reader that is re-pointed
  matches the id against the class `check-memory-hygiene.sh --print-slug-class` prints. A reader keeps
  its own function name, so its callers do not change. Observed by AC2 and AC3.
- **S4** — The flip probe proves the readers. For each flip, `id_grammar.py --flip-probe <clone>`
  checks two more things. First, `parse_id_parts("TOOL-<new slug>-3", <clone>)` returns the planted
  slug and the sequence `3`. Second, `--readers` over the clone lists no split hit, by path and line
  text, that `--readers` over the probe's own tree does not also list (§8 F3). A re-point reverted in
  the clone fails this check, and the tip's own kept hits do not. Under the hyphenated `in-slug` flip,
  `tools/memory-tree/migrate_backlog.py#read_slug` and the slug half of
  `tools/memory-tree/migrate_backlog.py#build_id_sort_key` return `d2026-10-26ClosedLoop` for
  `TOOL-d2026-10-26ClosedLoop-3`. The parse check holds only where the slug class of
  `build_id_token_re` is bound from the grammar, which `TOOL-dTotalRecall-5` hands to unit 54 (§3
  Edges). Observed by AC4.

## 3. Non-goals (OUT)

- The grammar, its keys, its shell and JavaScript exports and the regex half of the census:
  `TOOL-dTotalRecall-5`'s. The parser body: `TOOL-dTotalRecall-54`'s, landed earlier in this step.
- The marker that excludes a kept hit from the census output: the batch `TOOL-dTotalRecall-43`
  carries it for the round-1 audit's id 13, and it reads S2's widened predicate.
- Splits on other separators, and splits of values whose names do not say they hold an id. The census
  names its shapes, and a reader outside them is out of this unit's reach and is stated so in S2.
  `TOOL-dTotalRecall-44` keys the census on the split's shape at order 9.
- The three split readers outside §1, `tools/memory-tree/row_grammar.py#scan_records`,
  `tools/branch-reconcile/branch_reconcile.py#derive_names` and
  `tools/memory-tree/gen_build_index.py#render_spec_skeleton`: `TOOL-dTotalRecall-45` re-points them
  at order 9, and any of them S2 lists is kept here naming that unit.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py`, its `grammar_for` and `ID_RE`, the
  `--readers` predicate S2 widens and the `--flip-probe` S4 extends, and `tree_lib.build_id_token_re`
  with its slug class bound from the grammar, without which S4's parse check fails under the
  hyphenated flip
- **hands-off** `TOOL-dTotalRecall-43` — the widened `--readers` predicate, whose kept hits that unit's
  marker excludes from the census output (the round-1 audit's id 13)
- **hands-off** `TOOL-dTotalRecall-44` — the widened `--readers` split predicate, which that unit keys on the split's shape (the round-1 audit of units 36 to 43, id 1)
- **hands-off** `TOOL-dTotalRecall-45` — `parse_id_parts` and the re-point routes of §4, which that unit takes for three further readers (the round-1 audit of units 36 to 43, id 35)
- **hands-off** `TOOL-dTotalRecall-46` — `parse_id_parts`, whose body that unit rebuilds on `tree_lib.build_id_token_re` (the round-1 audit of units 36 to 43, id 22)
- **hands-off** `TOOL-dTotalRecall-53` — `--readers`, `--flip-probe` and the re-pointed readers, which that unit marks, probes and holds to their base answers (the round-1 audit of units 36 to 43, ids 2, 9, 13 and 23)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` on `tree_lib.build_id_token_re`, landed in step 8 before this pass; S1 is met by that body, which this pass re-points its readers onto and does not rewrite, as S1 and §4's rule for a landed spelling say (the round-1 audit of units 44 to 53, id 1)

## 4. Design

### The parser

This pass calls `parse_id_parts` as unit 54 landed it and writes no body. Where the landed name,
signature or tuple differs from S1, the pass uses the landed spelling and bumps this spec's rev first.

### The ten readers

| Reader | Today | After |
|---|---|---|
| `tools/memory-tree/backlog.py#derive_verdicts`, `tools/memory-tree/backlog.py#derive_ready` | `ask.id.split("-")[1]`, `ask_id.split("-")[1]` | `parse_id_parts(<id>, root)[1]`, `""` on `ValueError` |
| `tools/memory-tree/backlog.py#build_ask_sort_key` | `parts = ask.id.split("-")` | `parse_id_parts`, `("", 0, ask.id)` on `ValueError` |
| `tools/memory-tree/gen_build_index.py#build_grade_row` | `ask_id.split("-")[1]`, else the id | `parse_id_parts`, the id on `ValueError` |
| `tools/memory-tree/gen_build_index.py#cmd_new_build` | sort key from `split("-")` and `rsplit("-", 1)` | `parse_id_parts`'s slug, family and sequence |
| `tools/memory-recall/check-recall.py#derive_probe_labels` | `i.split("-")[1] != spec["slug"]` | `parse_id_parts` through memory-recall's route |
| `tools/memory-recall/query.py#measure_answer_used` | `seg = rid.split("-")` | `parse_id_parts` through memory-recall's route, `None` on `ValueError` |
| `tools/drift-audit/drift_report.py#_parse_slug` | `parts = uid.split("-")` | `parse_id_parts` through drift-audit's route, `None` on `ValueError` |
| `tools/memory-tree/migrate_backlog.py#build_id_sort_key`, `tools/memory-tree/migrate_backlog.py#read_slug` | `parts = ident.split("-")` | `parse_id_parts`, each keeping its malformed-id answer |

### The census at HEAD

At `c344bdc40` (DERIVED 2026-11-22), S2's Python shapes, matched by
`git grep -niE '(id|slug|unit)[A-Za-z_]*\.r?split\("-"' -- 'tools/*.py' 'skills/*.py' '.githooks/*'`,
list 13 lines (DERIVED, that command), eight of them readers of §1. Its shell shapes list 14 lines
(DERIVED, `git grep -niE` over `tools/`, `skills/` and `.githooks/` for S2's `cut`, `IFS=-` and
expansion shapes). No hit outside the ten needs a re-point, so Files touched gains no code file. Each
of the others is kept by a reason of S2:

| Hit | Kept as |
|---|---|
| `tools/memory-tree/backlog.py#render_family_view`, `tools/memory-tree/gen_build_index.py#cmd_asks`, `tools/loop/loop_lib.py#resolve_item_seed` | the family at index 0 |
| `tools/codebase-map/map_lib.py#measure_typed_counts` | not a unit id: an inventory id's last segment |
| `tools/memory-tree/row_grammar.py#scan_records` | `TOOL-dTotalRecall-45`'s re-point (§3) |
| `${unit#*-}` in `tools/unattended/pass-tree.sh`, `${id#*-}` in `tools/unattended/unattended.sh` and in two fixtures of `tools/unattended/unattended.test.sh` | the first and the last segment stripped |
| `${_rs_id##*-}` and `${ownid%%-*}` in `tools/unattended/unattended.sh` | the sequence, and the family |
| `cut -d- -f2` in the ask stub of `tools/unattended/unattended.test.sh` | a test stub echoing the legacy ids its suite plants |
| the push-shape `mid` of `.githooks/pre-push.runlog.test.sh`, and six `pid` expansions under `tools/run-gates/` and in `tools/unattended/unattended.sh` | not a unit id: a push shape and process ids |

The pass re-runs its own predicate before the first edit, and its `Decided:` trailer records that
count, not this one.

### Inventory

Minted: the split shapes of the census, and the flip probe's parse and census checks. No function is
minted: `parse_id_parts` is unit 54's, and `scan_readers` and `run_flip_probe` are unit 5's. The
lexicon answered `python tools/lexicon/lexicon.py --suggest parse_id_parts --as py.function` with OK
on 2026-11-22.

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
  functions with other inputs, so a per-site probe would rebuild each caller's context. One parser
  that every reader calls, and a census that finds any reader that does not, proves the same thing once.
- **Keep the splits and forbid hyphens in slugs.** It refuses the `in-slug` hyphenated value the clause
  names, which `TOOL-dTotalRecall-5`'s flips table carries.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one compiled regex per root, cached beside `grammar_for` by unit 54; the probe's census
  check runs `--readers` twice per flip.
- error / empty / loading states — an id the grammar refuses raises `ValueError` in `parse_id_parts`;
  each caller keeps its existing answer for a malformed id.
- observability — `--readers` prints each hit with its file and line; the flip probe prints one line
  per check.
- risks — a reader whose value name says nothing about ids escapes the census, which S2 states and
  unit 44 closes; the census check passes a split the tip itself still carries, which AC2 grades.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none for records. A flat-era or node-scoped id, which the parser refuses, now takes each
  caller's malformed-id answer where the split took a segment. `TOOL-dTotalRecall-53` S3 holds those
  answers to base.
- user docs — none under `help/`: no page covers id parsing.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `parse_id_parts("TOOL-dTotalRecall-38", ".")` from
  `id_grammar.py`, it returns `("TOOL", "dTotalRecall", 38)`; with `"TOOL-x"` it
  raises `ValueError`.
  Red when: the parser splits on a hyphen, or answers a malformed id with a guess.
- **AC2** — When `python id_grammar.py --readers` runs at the pass base, its split hits include the
  eight readers of §1 whose split value is named for an id (all but `derive_probe_labels` and
  `cmd_new_build`); at the pass tip it lists none of the ten, and every split hit it still lists is
  named as kept, with a reason of S2, in the pass commit's `Decided:` trailer.
  Red when: the predicate reads regex literals only, so the base run lists none of the eight.
- **AC3** — When `git grep -nE '(id|slug|unit)[A-Za-z_]*\.r?split\("-"' -- tools/memory-tree
  tools/memory-recall tools/drift-audit` runs at the pass tip, it prints no line outside
  `id_grammar.py` and the kept hits; and `git grep -nF 'i.split("-")[1]' --
  tools/memory-recall/check-recall.py tools/memory-tree/gen_build_index.py`, which prints both
  `i`-named readers at base, prints nothing.
  Red when: a re-point is skipped and the split survives in a reader.
- **AC4** — When `python id_grammar.py --flip-probe <clone>` runs over a scratch clone
  under `%TEMP%/<short>`, the hyphenated `in-slug` row prints `ok`, its `parse_id_parts` check returns
  `d2026-10-26ClosedLoop`, and its census check lists no split hit the probe's own tree does not list.
  With one re-point reverted and committed in the clone, that row prints the census check's failure
  naming the reverted line, and the probe exits 1.
  Red when: the probe passes over a reader that still splits.
  fixture: the scratch clone `TOOL-dTotalRecall-5` §4 "The flips" makes; the pass makes it.

## 7. Gates

`tier2-review self-test` · `drift-audit selftest` · `drift-audit records` · `backlog migration selftest` · `build-index selftest` · `build README slot contract` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `policy fixtures` · `memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/id_grammar.py · covers AC2 AC4 · the `--readers` split plants `py-split`, `sh-cut` and `sh-expansion`, and the flip probe's census check, staged by reverting one re-pointed reader to its split · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — What does AC2 hold of the two `i`-named readers at this pass?** S2's predicate reads the
  value's name, and `derive_probe_labels` and `cmd_new_build` split a value named `i`, so rev-3's AC2
  ("lists the ten lines of §1") was red by construction (the round-1 audit of units 36 to 43, id 1,
  whose repair unit 44 builds at order 9). Options: (a) AC2 names the eight readers the predicate
  reaches; S3 re-points all ten from §1's table; AC3 greps the two `i` lines gone by text; (b) key the
  predicate on the split's shape here; (c) keep AC2 as written. (b) takes unit 44's scope and breaks
  §3's non-goal on value names, and (c) fails its own criterion; veto 1 discards both. RESOLVED
  (agent, 2026-11-22, delegated): (a), the only survivor. widens: none · relaxes: AC2's base list,
  from ten readers to the eight the predicate reaches, AC3 grepping the other two
- **F3 — Which kept set does the flip probe's census check read at this pass?** S4 asked for no split
  "outside the kept hits", which the pass names only in its `Decided:` trailer. The machine-read marker
  is `TOOL-dTotalRecall-43` S14's, order 27 (the round-1 audit of units 36 to 43, id 9). Options: (a)
  a differential: a clone hit that `--readers` over the probe's own tree does not list, matched by path
  and line text, is the failure; (b) build unit 43's marker here; (c) a constant list of kept hits in
  `id_grammar.py`. (b) breaks §3's marker non-goal (veto 1); (c) types an inventory beside the code it
  describes, which the charter's derive rule forbids. RESOLVED (agent, 2026-11-22, delegated): (a). It
  reads no list, catches AC4's reverted re-point, and leaves a split still at the tip to AC2.
  `TOOL-dTotalRecall-53` S16 later makes the check skip a marked line. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 17 (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-44, TOOL-dTotalRecall-45, TOOL-dTotalRecall-46, TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-4 · 2026-11-22 · §1 · S1 to S4 · §3 · §4 · §5 · AC2 to AC4 · §7 · §8 · §10 · re-grounded at
  `c344bdc40` per `2026-11-22-prompt-TOOL-dTotalRecall-38-reground-brief`: the ten readers are cited by
  symbol; S1 points at unit 54's body because `ID_RE` has no named group; the census at HEAD is
  re-derived with every hit's disposition; AC2 names the eight readers the predicate reaches (F2); the
  probe's census check is a differential (F3); §7 gains `memory-recall kit selftest` and `policy
  fixtures`, which `tools/memory-tree/backlog.py`'s guards name.

## 10. Reuse audit

The seams extended are `TOOL-dTotalRecall-5`'s, in `id_grammar.py`: its `--readers` predicate
(`scan_readers`) and `--flip-probe` (`run_flip_probe`) are the two modes this unit widens. The parser
this unit's readers call is `TOOL-dTotalRecall-54`'s, on `tools/memory-tree/tree_lib.py#build_id_token_re`,
the named-group regex `_expand_ids` and `read_id_pins` already match through. No other id parser exists:
`git grep -nE "def (split_id|parse_id|id_parts|unit_slug|slug_of)" -- tools` printed nothing at
`c344bdc40`. `python tools/codebase-map/reuse_lookup.py "parse a unit id into family slug and sequence"`
ranked name-stem neighbours (`parse`, `parse_unit_rows`, `parse_spec_h1`). Of these,
`tools/playbook/instruction_units.py#parse_unit_rows` reads a manifest's `[[unit]]` tables, and
`tools/memory-tree/tree_lib.py#parse_spec_h1` returns a spec's whole id without splitting it.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
