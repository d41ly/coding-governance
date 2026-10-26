# TOOL-dTotalRecall-52 — the one legacy registration is keyed by path, section and check, absorbs its second population through a declared base re-key, and leaves no carrier of the old name

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 28 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 37 at HIGH**, its item **H8**, alone in that item. `TOOL-dTotalRecall-43` S19
folds the `[[ledger]]` population `legacy-records` (`TOOL-dTotalRecall-19` S7) into
`record-kinds-legacy` (`TOOL-dTotalRecall-1` S8), "keyed by path and section with a field `check`".
Both seeds hold one row per tracked record, so the slices share keys and collide. The merged home
gains every `causes` row its base lacked, which the factory's `shrink-only` direction refuses as
`gained` (`TOOL-dWitnessedBar-13` §4, "The direction predicates"). And the old name's carriers stay
uninventoried: `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` entry, the home
`memory/project/legacy-records.txt`, and the `--population legacy-records` calls in unit 19's seed,
fixture and leg. Built as written, the merge loses a slice or is refused. This unit keys the merged
registration by the triple, declares how its base is read, and clears the old name by value. It
repairs `TOOL-dTotalRecall-43`.

## 2. Scope (IN)

- **S1** — The key. The `record-kinds-legacy` table in `tools/memory-tree/kit.toml` declares
  `key = "record"` with `fields = ["path", "section", "check"]`, so a record legacy for both checks
  holds two rows, one per `check` value, and `drain = "key"` drains one slice's row only. Observed by
  AC1.
- **S2** — The declared base re-key. A registration may carry `absorbs = [{ population = "<name>",
  check = "<value>" }]`. `compare_to_base` in `tools/lib/legacy_ledger.py` then reads, beside the
  registration's own base rows, each absorbed population's home at the compare base, sets `check` on
  each of its rows, and judges the working rows against that union, as `carry_renames` re-keys a
  renamed path before the judgement. A key the union lacks is still `gained`. A registration that
  absorbs a population still registered, or whose home is still tracked at the working tree, is
  refused by name. Observed by AC2.
- **S3** — The old name's carriers. The `legacy-records` table leaves `tools/memory-tree/kit.toml`, its
  home `memory/project/legacy-records.txt` is deleted, its `PROJECT_REGISTRY_EXTRA` entry leaves
  `.memory-tree.conf`, and each `--population legacy-records` call in `tools/memory-tree/record_causes.py`
  reads `--population record-kinds-legacy` with the `causes` slice. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — `legacy-records` and its home are minted by
  `TOOL-dTotalRecall-19` S7 in this build and are absent at base `462d20f3` · by value:
  `check_causes` and `check_orphans` read the `causes` slice's rows, and `check_record_kinds` the
  `kind-schema` slice's, each through `legacy_ledger.py` after this item.

## 3. Non-goals (OUT)

- The decision to keep one registration: `TOOL-dTotalRecall-43` S19's, for the round-1 audit's id 25.
- The ledger factory's other directions and fields: `TOOL-dWitnessedBar-13`'s.
- The per-check row counts as a criterion of their own: the batch `TOOL-dTotalRecall-53` observes the
  slices for ids 51 and 12.

### Edges

- **consumes-from** `TOOL-dTotalRecall-43` — S19's merged `record-kinds-legacy` registration and its
  `check` field, which this unit re-keys and carries past `shrink-only`
- **consumes-from** `TOOL-dTotalRecall-19` — the `legacy-records` population, its home and its
  `--population` call sites, which S3 clears by value
- **consumes-from** external — `tools/lib/legacy_ledger.py`, `compare_to_base` and `carry_renames`
  (`TOOL-dWitnessedBar-13`), the factory whose base read S2 extends by one declared field
- **hands-off** `TOOL-dTotalRecall-53` — the triple-keyed `record-kinds-legacy` registration, whose per-slice drain and fixture name that unit observes (ids 12 and 51)
- **hands-off** `TOOL-dTotalRecall-59` — the `absorbs` field, its read and its refusal, which that unit cuts and whose `shrink-only` judgement it proves on a fixture base (the round-1 audit of units 44 to 53, id 13)
- **hands-off** `TOOL-dTotalRecall-60` — AC3's retirement grep and the `.memory-tree.conf` edit, which that unit re-observes and re-stamps (the round-1 audit of units 44 to 53, ids 6, 12 and 32)
- **consumes-from** `TOOL-dTotalRecall-62` — S2, AC2 and the registration block as that unit amends them in step 28 before this pass, so this pass builds no base re-key and reads the first seed (the round-1 audit of units 54 to 60, id 2)

## 4. Design

### The registration after this unit

```toml
[[ledger]]
population = "record-kinds-legacy"
key = "record"
fields = ["path", "section", "check"]     # check: kind-schema | causes
drain = "key"
direction = "shrink-only"
absorbs = [{ population = "legacy-records", check = "causes" }]
```

The `absorbs` row stays until the next compare base already holds the merged home; at that base the
union adds nothing, and the pass that lands after it may cut the row with no `gained` finding.

### Inventory

Minted: the optional registration field `absorbs` and its refusal in `tools/lib/legacy_ledger.py`.
Naming cell: none, a TOML key being no surface of the lexicon's closed set (function, type, file,
constant).

### Files touched (estimate)

- `tools/memory-tree/kit.toml`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/record_causes.py`
- `.memory-tree.conf`
- `memory/project/legacy-records.txt` (deleted)
- the merged registration's home, as `TOOL-dTotalRecall-1` S8 names it

### Alternatives rejected

- **Mark each `causes` row `widened:<record>`.** It spends the factory's per-row escape on 4,244 rows
  that gained nothing.
- **Keep two registrations.** It reopens the round-1 audit's id 25, which unit 43 closed.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one more home read at the compare base while `absorbs` stands.
- error / empty / loading states — an `absorbs` naming a live registration or a tracked home is a
  refusal by name.
- observability — `compare_to_base` names each absorbed population it read.
- risks — an `absorbs` row left after its base moved reads an empty union and changes nothing.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — the merged home's rows carry `check`; the old home is deleted in the same commit.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `tomllib` probe reads the `record-kinds-legacy` table of `tools/memory-tree/kit.toml`
  and its home at the tip, the key fields are `path`, `section` and `check`, and no two rows share all
  three.
  Red when: two rows collide on the declared key.
- **AC2** — When `legacy_ledger.py`'s `compare_to_base` judges the merged home at the pass tip against
  the pass base, it names no `gained` key; with one extra `causes` row planted, it names that key
  `gained`.
  Red when: the merge is refused, or a row neither base home held passes.
- **AC3** — When `git grep -n "legacy-records" -- tools .memory-tree.conf memory/project` runs at the
  tip, it prints nothing, and `git ls-files memory/project` lists no `legacy-records.txt`.
  Red when: a carrier of the old name stays live.

## 7. Gates

`kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/lib/legacy_ledger.py · covers AC2 · an absorbed fixture population and one gained row, staged by reading the registration's own base rows only · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 37
  (HIGH, item H8).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-59, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-62, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is the ledger factory's base read, `compare_to_base` with its `carry_renames`
re-key (`TOOL-dWitnessedBar-13` §4), whose rename re-key S2's absorbed re-key follows; the registration
grammar keeps its closed `key` set and gains one optional field, as `verbatim` was added.
`python tools/codebase-map/reuse_lookup.py "a shrink-only keyed baseline of counted sites"` is the
lookup that factory's own §10 records; no ledger merge exists at base, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
