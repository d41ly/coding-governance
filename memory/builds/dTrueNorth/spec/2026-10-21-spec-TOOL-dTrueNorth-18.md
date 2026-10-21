# TOOL-dTrueNorth-18 — two amends of one clause are ordered by a declared supersession, never by path

**Status:** OPEN · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 5

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-18-deviation-17.md](../build/2026-10-21-build-TOOL-dTrueNorth-18-deviation-17.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-18-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-18-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`)
confirmed finding **id 34 at HIGH**, its item **H2**: two amends of one clause are ordered by lexical
path. `TOOL-dTrueNorth-6` S2 and `TOOL-dTrueNorth-8` §4 Evidence take "the later file by path supplies
the row", and path order is lexical, so `…-TOOL-dTrueNorth-16-deviation-6.md` sorts before
`…-TOOL-dTrueNorth-4-deviation-4.md` and `deviation-10` before `deviation-9`. Both records pass the
pin check against the baseline hash, so nothing flags the clash, and the view renders the older
record's text, its citation and the hash that follows them. This unit orders the amends of one
clause by a field the newer record declares, and refuses an order nobody declared. It repairs
`TOOL-dTrueNorth-8`.

## 2. Scope (IN)

- **S1** — An optional record field, `**Supersedes:**`, holding one record id: the stem of another
  record in the `<date>-build-<unit id>-deviation-<n>` grammar `TOOL-dTrueNorth-4` S1 states.
  `read_record` in `tools/memory-tree/deviation_join.py` returns it and names it malformed when its
  value is not one such stem. The "Deviation records" paragraph of
  `tools/memory-tree/HYGIENE.template.md` names the field and its rule, and `memory/HYGIENE.md` is
  re-rendered from it. Observed by AC5 and AC6.
- **S2** — The precedence, in `resolve_clause_rows(records)` in `tools/memory-tree/asbuilt_view.py`,
  which `render_view` calls. A clause's set is the records whose `**Follow-through:**` row names it.
  When every `**After:**` in the set agrees, the later file by path supplies the citation, as the
  instrument's ordering does, so the view keeps `TOOL-dTrueNorth-6` S3's byte identity. When they
  differ, a record a member names in `**Supersedes:**` is superseded, and the one member left is the
  head: it supplies the row's text and citation whatever its path. This supersedes
  `TOOL-dTrueNorth-6` S2's "the later file by path supplies the row" for a set whose texts differ.
  Observed by AC1 and AC3.
- **S3** — The refusals, joining `TOOL-dTrueNorth-6` S4's findings and printed by whichever verb
  prints them (`--check` until `TOOL-dTrueNorth-16` S17 lands, `--check-asbuilt` after): a set whose
  texts differ and that leaves two or more members, or none, unsuperseded is `unordered amends of
  <clause>`, naming every member; and a `**Supersedes:**` naming a record outside the clause's set is
  a finding naming both. The clause's row then renders from the baseline, as a refused record's does.
  Neither path order nor a commit date decides. Observed by AC2 and AC4.
- **S4** — The plants, in `asbuilt_view.py --fixture`: `amends-order`, two amends of one clause whose
  paths sort against their declared order, `…-deviation-10.md` superseding `…-deviation-9.md`;
  `unordered-amends`, the same two with no `**Supersedes:**`; `same-after`, two amends with one
  `**After:**` and no field; and `supersedes-stray`, a field naming a record of another clause. In
  `deviation_join.py --fixture`, `malformed-supersedes`. Observed by AC1 to AC5.
- **S5** — The docs: the docstring of `asbuilt_view.py` and its row in `tools/memory-tree/README.md`
  state S2's rule beside `TOOL-dTrueNorth-8` S1's. Observed by AC6.

## 3. Non-goals (OUT)

- Ordering by the adding commit. History moves under a rebase and a shallow clone, while the field
  is in the record's bytes.
- Overloading `**Caused-by:**`, which names what caused a departure, a decision, an ask or a unit,
  and is not a precedence.
- Any edit of deviation-1 and deviation-4. Their `**After:**` texts agree, so S2 renders them as
  today and the view cites deviation-4.
- The bootstrap instrument `asbuilt.py`, which reads no `**Supersedes:**` and keeps its path order
  until the report-switch step.
- A hygiene arm of its own, the finding's left-shift: S3's finding is the generator's, and checks 9
  and 30 already run that generator.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-4` — `read_record` and the record grammar S1 extends with one optional field
- **consumes-from** `TOOL-dTrueNorth-6` — `render_view`, its row rule and S4's findings, which S2 and S3 amend
- **hands-off** external — dClosedLoop's report-switch step, after which the departures report reads S2's precedence instead of the instrument's path order
- **hands-off** `TOOL-dTrueNorth-20` — the `**Supersedes:**` field, which that unit's decline route for an approval carried for the owner's walk names (the round-2 audit's id 45)

## 4. Design

### Evidence

- The instrument overwrites `changes[cid]` record by record (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py:64`)
  over records sorted by path (`:140`), and its pin check compares each against the baseline hash
  (`:68-69`), so two amends of one clause both pass and the later path wins.
- `TOOL-dTrueNorth-4` S1 lists `**Bound:**`, `**Tier:**` and `**Surface:**` as the optional fields
  and gives `**Caused-by:**` one id of a decision, a record, an ask or a unit (its §4 field table).
- Deviation-1 and deviation-4 both amend `cl-dClosedLoop-0004@c374ccd0` with the clause's text
  unchanged as `**After:**` (`TOOL-dTrueNorth-4` §4 "The records this unit owes").

### The rule

```
set(clause)   = records whose Follow-through row names the clause
same texts    -> the later path cites; text and hash are the shared After
differing     -> head = the one member no member names in Supersedes; it supplies the row
no single head, or a Supersedes outside the set -> finding; the row renders from the baseline
```

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `**Supersedes:**` | optional record field | none |
| `resolve_clause_rows` | function, `asbuilt_view.py` | `py.function`, OK |
| `amends-order`, `unordered-amends`, `same-after`, `supersedes-stray`, `malformed-supersedes` | fixture plants | none |

### Files touched (estimate)

- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/gen_build_index.py` (its self-test's plant table only)
- `tools/memory-tree/routed_commits.py` (its self-test's plant table only)
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **The latest by adding commit.** It needs history for a render that otherwise reads the tree, ties
  when two records land in one commit, and reorders under a rebase.
- **Refusing every pair of amends of one clause.** It forbids a legitimate re-amendment and refuses
  deviation-1 and deviation-4, whose texts agree.

## 5. Production-readiness checklist

- security — no new write path; one optional field read from records already parsed.
- perf / scale — one pass over the records grouped by clause, linear in their count.
- error / empty / loading states — a clause with one record renders as today; a set with no head is
  a named finding, never a silent pick.
- observability — each finding names the clause and every member.
- risks — a chain whose head sorts before another member makes the instrument's `asbuilt.py --check`
  disagree with the product's view until the report-switch step; no such chain exists, and the
  hands-off names the step that lifts it.
- testing — AC1 to AC6 as probes; the arms under §7, observed at the close.
- migration — additive: no record carries the field today, and a set whose texts agree renders the
  bytes it renders at base.
- user docs — the HYGIENE paragraph, the docstring and the kit README row; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant amends-order` runs, it
  exits 0, and the clause's rendered row holds `deviation-10`'s `**After:**` and cites it although
  its path sorts first.
  Red when: the later path supplies the row, so the view cites `deviation-9`.
- **AC2** — When `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant unordered-amends` runs,
  it exits 1 with an `unordered amends of` line naming the clause and both records.
  Red when: either record is chosen silently.
- **AC3** — When `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant same-after` runs, it
  exits 0 citing the later path; and on the tree after the pass,
  `grep -c 'cl-dClosedLoop-0004.*deviation-4' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
  prints 1.
  Red when: a pair whose texts agree is refused, or the view's bytes move for deviation-1 and -4.
- **AC4** — When `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant supersedes-stray` runs,
  it exits 1 naming the record and the id it names.
  Red when: a field naming a record of another clause is ignored.
- **AC5** — When `python3 "tools/memory-tree/deviation_join.py" --fixture --plant malformed-supersedes --policy refuse`
  runs, it exits 1 naming the file and `**Supersedes:**`.
  Red when: `read_record` accepts a value that is no record stem.
- **AC6** — When `git grep -n "Supersedes" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/README.md "tools/memory-tree/asbuilt_view.py"`
  runs, each file names the field and the head rule.
  Red when: one home still says the later path supplies the row.

## 7. Gates

`build-index selftest` · `routed-commits selftest` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC1 AC2 AC3 AC4 · the four as-built plants, each staged against the base rule that lets the later path supply the row · none
New arm: tools/memory-tree/routed_commits.py (its selftest) · covers AC5 · the malformed-supersedes plant against a read_record that accepts any value · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21,
  delegated): (a). widens: none · relaxes: none
- **F2 — What orders two amends of one clause?** (a) An optional `**Supersedes:**` the newer record
  declares, an undeclared order refused. (b) The latest by adding commit, a tie refused. (c)
  `**Caused-by:**` naming the older record. (d) Refuse every pair. (d) refuses deviation-1 and
  deviation-4, failing `TOOL-dTrueNorth-16` AC33's `cl-dClosedLoop-0004` row, so veto 1 discards it;
  (c) gives one field two meanings; (b) reads history the render does not otherwise need and moves
  under a rebase. Recommendation (a), the most criteria met with the fewest follow-ups. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the kit and catalogue edits here?**
  `cl-dClosedLoop-0004` names the record and its fields and `cl-dClosedLoop-0006` the view's rows.
  RESOLVED (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the deviation record's optional Supersedes field and the as-built view's row
  precedence cl-dClosedLoop-0004 and cl-dClosedLoop-0006 name · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-2 spec audit's id 34 (HIGH, item H2).
- rev-2 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "order two records that amend one clause by a
declared supersession"` ranked `records` and `declares` (`tools/memory-tree/gotchas.py`) and
`derive_supersession_map` (`tools/memory-recall/extract.py`). The last is the precedent for a
declared supersession between records, but it maps decision rows in another kit and reads none of
the record grammar, so no existing seam fits the clause rows; the seam extended is
`TOOL-dTrueNorth-6`'s `render_view` and `TOOL-dTrueNorth-4`'s `read_record`. No hit disagreed with
source.

Recall terms used: `python tools/memory-recall/query.py "how does a spec audit's promoted repair unit
close a defect a pass before it would hit" --terms "spec-audit promoted unit repairs order transition
re-render as-built view argv pathspec supersedes amends"`
