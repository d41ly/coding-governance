# TOOL-dTotalRecall-59 — the merged legacy registration is judged at the run's real compare base, a first seed, and the `absorbs` read that base can never feed is cut

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 29 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md](../build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md) | deviation | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, its item **H3**, alone in that item. `TOOL-dTotalRecall-52`
(order 28) says the merged home "gains every causes row its base lacked" and is refused `gained`,
and S2 builds an `absorbs` read of the absorbed population's home at the compare base to prevent
that. `compare_to_base` judges at `resolve_compare_base` (`tools/codebase-map/map_lib.py:1502`,
`TOOL-dWitnessedBar-13` §4), HEAD's merge-base with `origin/main`, which is `462d20f3` throughout
this run. Neither home exists there: units 1 and 19 mint both on the unmerged run branch. The
factory reads a home absent at the base as a first seed, every row `seeded`
(`TOOL-dWitnessedBar-51` S30), never as `gained`. So unit 52's AC2 prints `first seed`, and its
`absorbs` read reads nothing. After the close merge, `legacy-records` never reaches `main`, because
unit 52 S3 deletes its home first, so no base anywhere will ever hold it. This unit grounds the
judgement on the real base, cuts `absorbs`, and proves `shrink-only` on a fixture base that does
hold the merged home. It repairs `TOOL-dTotalRecall-52`.

## 2. Scope (IN)

- **S1** — The judgement at the run's base. At this run's compare base the merged
  `record-kinds-legacy` home is absent, so `compare_to_base` reads it as a first seed and names no
  `gained` key. Nothing is added to make that so: it is the factory's S30 rule, observed. Observed by
  AC1.
- **S2** — `absorbs` is cut. The registration field `absorbs`, its read in `compare_to_base`, its
  refusal of a live or tracked absorbed population, and the `absorbs` line of the
  `record-kinds-legacy` table in `tools/memory-tree/kit.toml` are deleted, as is the §7 arm unit 52
  added for them. Observed by AC2.
  **Readers:** by name: READER NOT IN TREE — `absorbs` is minted by `TOOL-dTotalRecall-52` in this
  build and is absent at base `462d20f3` · by value: NO VALUE READERS — no compare base this run or
  any adopter reaches holds the absorbed home, so the union it built was always the registration's
  own base rows.
- **S3** — `shrink-only` proved where it can bite. A fixture whose base commit holds the merged home
  shows a planted extra `causes` row named `gained`, and an unchanged home naming none. Observed by
  AC3.

## 3. Non-goals (OUT)

- The triple key and the old name's carriers: `TOOL-dTotalRecall-52` S1 and S3, unchanged.
- The factory's absent-home and legacy-grammar rules: `TOOL-dWitnessedBar-51` S30's.
- Re-keying any base that holds `legacy-records`: no such base exists, which is S2's reason.

### Edges

- **consumes-from** `TOOL-dTotalRecall-52` — the merged registration and its `absorbs` field, read
  and refusal in `tools/lib/legacy_ledger.py`, which this unit cuts; without them there is nothing
  to remove and S1 has no registration to judge
- **hands-off** `TOOL-dTotalRecall-60` — the registration with `absorbs` cut, against which that unit
  re-observes unit 52's AC3 grep for ids 6 and 12
- **consumes-from** `TOOL-dTotalRecall-62` — S2 as that unit amends it in step 28, observing `absorbs` absent (the round-1 audit of units 54 to 60, id 2)
- **hands-off** `TOOL-dTotalRecall-66` — the fixture and its plant `merged-home-gained`, which that unit moves into the factory's arm and scrubs of the caller's environment (the round-1 audit of units 54 to 60, ids 6, 19, 31, 34 and 37)

## 4. Design

### The registration after this unit

```toml
[[ledger]]
population = "record-kinds-legacy"
key = "record"
fields = ["path", "section", "check"]     # check: kind-schema | causes
drain = "key"
direction = "shrink-only"
```

### The fixture

A scratch repository under `%TEMP%/<short>`, a short path because a clone under the run's scratch
directory fails with `Filename too long`. Its `origin/main` commit holds a merged home of two rows;
the working branch holds three, the third a `causes` row neither base row carried. `compare_to_base`
run there resolves the merge-base as its base, as it does in this repository.

### Inventory

Minted: the fixture plant `merged-home-gained` in `legacy_ledger.py`'s self-test. Deleted: the
`absorbs` field, its read and its refusal. Naming cell: none.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/kit.toml`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

`TOOL-dTotalRecall-53` builds at order 29 too and writes `legacy_ledger.py` (S6), so BUILD-METHOD M6
sequences the two passes.

### Alternatives rejected

- **Keep `absorbs` for an adopter whose base holds `legacy-records`.** No adopter receives that
  population: it is minted and deleted on this run branch, and kits ship from `main`.
- **Seed the merged home on `main` before the build.** It would need a landing outside this build's
  write rule and changes nothing a correct build needs.

## 5. Production-readiness checklist

- security — no new surface; a field and its read are removed.
- perf / scale — one fewer home read per compare while the field stood.
- error / empty / loading states — the first-seed reading prints `first seed record-kinds-legacy
  <n> rows`.
- observability — the first-seed line names the population and its count.
- risks — none: the deleted read only ever read an absent home.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none: the field never reached `main`.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe run from `tools/lib/` calls `compare_to_base` from
  `legacy_ledger.py` for the `record-kinds-legacy` registration at the pass tip, it prints
  `first seed record-kinds-legacy` with the working row count and names no `gained` key.
  Red when: it names a `gained` key, or reads a base home this run's merge-base does not hold.
- **AC2** — When `git grep -n "absorbs" -- legacy_ledger.py` runs from `tools/lib/`, and
  `git grep -n "absorbs" -- tools/memory-tree/kit.toml` from the root, at the pass tip, each prints
  nothing.
  Red when: the field, its read or its refusal survives.
- **AC3** — When the same probe runs in the fixture of §4, it names the planted `causes` key `gained`;
  with the planted row removed, it names none.
  Red when: a row the base home lacked passes `shrink-only`.
  fixture: the scratch repository under `%TEMP%/<short>`; the pass makes it.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/lib/legacy_ledger.py · covers AC3 · the plant `merged-home-gained`, a fixture base holding the merged home, staged by reading the base as absent; it replaces unit 52's absorbed-population arm · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 13
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-62, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is the ledger factory's own base read, `compare_to_base` at `resolve_compare_base`
(`TOOL-dWitnessedBar-13` §4, `tools/codebase-map/map_lib.py:1502`), with its absent-home rule
(`TOOL-dWitnessedBar-51` S30); this unit adds nothing to it and removes the one field unit 52 added.
`python tools/codebase-map/reuse_lookup.py "a shrink-only keyed baseline of counted sites"` is the
lookup the factory's own §10 records, and `git merge-base HEAD origin/main` printed `462d20f3` here.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
