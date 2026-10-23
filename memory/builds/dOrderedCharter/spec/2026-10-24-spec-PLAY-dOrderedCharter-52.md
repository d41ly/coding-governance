# PLAY-dOrderedCharter-52 — the TOML-table merge envelope is total: every base, ours and theirs state has a row, and an unlisted one is a conflict

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 18 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-24-build-PLAY-dOrderedCharter-52-deviation-521.md](../build/2026-10-24-build-PLAY-dOrderedCharter-52-deviation-521.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 33 at HIGH**, its item **H3**. `PLAY-dOrderedCharter-45` S3 states the table
class's envelope as an eleven-row table that claims to be whole, but has no row for a key ours left
unchanged and theirs deleted, for a key both sides deleted, or for a key only theirs added. S4 builds
the output from "ours' entries in ours' order", and its key-set postcondition compares against the
set S3 derived, which has no rule for these cases. Read literally, a unit theirs deleted is emitted
because ours still holds it unchanged, so a retired instruction unit returns to every node's
manifest at exit 0 on the commonest one-sided change. This unit makes the envelope a closed table
over every reachable state, symmetric between the sides, with any state the table does not list
resolving to a conflict, and proves the table total by enumeration. It repairs unit 45 and is built
right after it.

## 2. Scope (IN)

- **S1** — The side states. Per key, against the base, each side is in exactly one state: with the
  key in the base, `unchanged`, `changed` or `deleted`; with the key absent from the base, `absent`
  or `added`. Where both sides are `changed` or both `added`, the pair is further `same` or `different`
  by unit 45 S3's folded comparison. Observed by AC1.
- **S2** — The table, a module-level mapping `TABLE_ENVELOPE` in `tools/memory-tree/merge-rows.py`
  from `(base, ours, theirs[, agreement])` to a result, holding these fourteen rows. Unit 45 S3's
  eleven are rows 1 to 8, 10, 13 and 14 here. Observed by AC1 to AC3.

  | # | Base | Ours | Theirs | Result |
  |---|---|---|---|---|
  | 1 | present | unchanged | unchanged | base |
  | 2 | present | changed | unchanged | ours |
  | 3 | present | unchanged | changed | theirs |
  | 4 | present | changed | changed, same | ours |
  | 5 | present | changed | changed, different | **conflict** |
  | 6 | present | deleted | unchanged | deleted |
  | 7 | present | deleted | changed | **conflict** |
  | 8 | present | changed | deleted | **conflict** |
  | 9 | present | unchanged | deleted | deleted |
  | 10 | absent | added | absent | ours |
  | 11 | absent | absent | added | theirs |
  | 12 | present | deleted | deleted | deleted |
  | 13 | absent | added | added, same | ours, once |
  | 14 | absent | added | added, different | **conflict** |

  This supersedes unit 45 S3's table as the envelope's definition.
  **Readers:** by name: READER NOT IN TREE — the table it supersedes is unit 45 S3's, built at unit
  45's pass, and a grep for TABLE_ENVELOPE, resolve_tables and TableConflict outside memory/builds
  finds no reader today. by value: `resolve_tables` (S3), the one reader of a row's result, and the
  totality suite in `tools/memory-tree/merge-rows.test.sh` (S5).
- **S3** — The catch-all. `resolve_tables` looks every key's state up in `TABLE_ENVELOPE`; a state the
  mapping does not hold raises `TableConflict` naming the key, so a missed row fails closed rather
  than defaulting to a side. Observed by AC3.
- **S4** — The output. A clean result is ours' surviving entries in ours' order, then theirs' entries
  whose result is `theirs` and that ours does not hold, in theirs' order; an entry whose result is
  `deleted` is emitted nowhere. Unit 45 S4's three postconditions hold unchanged, the key set now
  being the set of keys whose result is not `deleted`. This supersedes unit 45 S4's "then theirs'
  additions in theirs' order" by naming row 11 as the source of those additions. Observed by AC2.
- **S5** — Totality, proved. The driver's suite enumerates every reachable state, the ten with the key
  in the base and the four with it absent, against `TABLE_ENVELOPE`, and fails on any state with no
  row and on any row no state reaches. Observed by AC1.
- **S6** — The plants, through unit 15's fixture, `python tools/playbook/instructions_edit.py fixture
  --plant <case>`: `merge-theirs-delete` (row 9), `merge-both-delete` (row 12) and `merge-theirs-add`
  (row 11). Observed by AC2.

## 3. Non-goals (OUT)

- The class's selection, its chunk cut and its postconditions: unit 45 S1, S2 and S4.
- The newline contract and the conflict label's arm in `main()`: the round-2 minors batch,
  `PLAY-dOrderedCharter-55`.
- Merging inside one entry: every both-sides change stays the author's.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-45` — `resolve_tables`, `TableConflict`, the chunk cut and the postconditions, which S2 to S4 complete; without them there is no table class to make total
- **hands-off** `PLAY-dOrderedCharter-55` — the table class's newline contract and its conflict-label arm (ids 34, 35), built over this unit's mapping

## 4. Design

### Evidence

Read at `ce13efbe`; the seam is unit 45's design. Its S3 table has eleven rows and none for rows 9, 11
or 12 above; its S4 orders the output from ours, then "theirs' additions", and compares the key set
with "the set S3 derived". Unit 45's AC3 plants both-edit, delete-edit, edit-delete and same-add only.
`merge()` (`tools/memory-tree/merge-rows.py:1227`) is the dispatch unit 45 S1 routes from, and `main()`
(`:1538-1552`) writes the whole-file conflict body for any exception that is not `ViewShardRefused`.

### Why a mapping and not branches

A table written as nested `if` branches has no way to say it is complete; a mapping keyed by the
state tuple can be enumerated, so S5's suite can fail on the row a later edit forgets. The reachable
domain is small and closed: three base-present side states squared, with the `changed`-`changed`
pair split in two, is ten; two base-absent side states squared, less the unreachable `absent`-`absent`,
with `added`-`added` split in two, is four.

### Inventory

Minted: `TABLE_ENVELOPE`, the side-state names, and the plants `merge-theirs-delete`,
`merge-both-delete` and `merge-theirs-add`. Naming cells: `lexicon naming predicates` grades the
Python names.

### Files touched (estimate)

- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/playbook/instructions_edit.py` (the fixture's plants)

### Rollout

Live at landing, order 18, after unit 45 at order 17. Units 3 and 41 share order 18 and write none of
these files.

### Alternatives rejected

- **Adding the three rows alone, keeping branch logic**: right today, and silent the next time a state
  is added.
- **Treating any one-sided delete as a conflict**: safe, but it conflicts on the commonest one-sided
  change, which the base-present rows 6 and 9 resolve without ambiguity.

## 5. Production-readiness checklist

- security: no new surface; the driver still writes only `%A`.
- perf / scale: one mapping lookup per key.
- error / empty / loading states: an unlisted state is a whole-file conflict naming the key.
- observability: the conflict label names the key, as unit 45 S4 states.
- risks: a key whose base entry does not parse is refused by unit 45 S2 before any lookup.
- testing: AC1 to AC3; the enumeration runs in the driver's suite.
- migration: none.
- user docs: the driver's docstring renders the fourteen rows beside its two planes.

## 6. Acceptance criteria

- **AC1** — When the driver's suite enumerates the reachable states against `TABLE_ENVELOPE`, every
  state has one row and every row is reached.
  Red when: a state has no row, or a row is unreachable.
- **AC2** — When `python instructions_edit.py fixture --plant merge-theirs-delete` and
  `--plant merge-both-delete` run, each exits 0 with the key absent from `%A`, and
  `--plant merge-theirs-add` exits 0 with the key present once.
  Red when: a unit theirs deleted is emitted, or theirs' addition is dropped or doubled.
- **AC3** — When a probe removes row 9 from `TABLE_ENVELOPE` in a scratch copy and runs
  `merge-theirs-delete`, the merge exits 1 with the whole-file conflict naming the key.
  Red when: a state the table does not hold resolves to a side.

## 7. Gates

`row-keyed merge driver replay` · `memory hygiene` · `check-wiring self-test` · `playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `verdict epoch (kit version dates the engine)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/merge-rows.test.sh · covers AC1 AC2 AC3 · the state enumeration and the three plants' inputs, each failing case staged by deleting its row from the mapping · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 15's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What a state the table does not list resolves to.** Options: (a) a conflict; (b) ours; (c)
  the base. (b) and (c) are the silent take the driver's fail-closed rule exists to prevent. RESOLVED
  (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 33 (HIGH, item H3).

## 10. Reuse audit

The seam extended is unit 45's `resolve_tables` in `tools/memory-tree/merge-rows.py`, dispatched from
`merge()` (`:1227`), with `write_conflict_body` (`:1333`) kept as the one conflict writer. `python
tools/codebase-map/reuse_lookup.py "three-way merge table of every base ours theirs state"` ranked
`merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`), `resolve_compare_base` and
`plan_state` by name stem; `merge` is the seam and none of them holds a state table, so the mapping is
new. The recall query returned TOOL-aMendedLedger-1 and TOOL-aMendedLedger-9, the driver's
fail-closed design, which S3's catch-all keeps.

Recall terms used: `python tools/memory-recall/query.py "how does merge-rows handle a key deleted on one side and unchanged on the other" --terms "merge-rows delete unchanged resurrect three-way base ours theirs envelope conflict fail closed"`
