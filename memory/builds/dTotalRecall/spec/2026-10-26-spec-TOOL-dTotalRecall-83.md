# TOOL-dTotalRecall-83 — unit 74's `s1-59` count is re-read at the verified parent of unit 59's pass, and the deviation record of unit 59 it decides is written once

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 35 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 9 at HIGH**. It shares item **H1** with id 36, which is
`TOOL-dTotalRecall-84`.

`TOOL-dTotalRecall-74` (order 34) counts the absorbs-is-absent string of unit 62 §4 over unit 59's
spec at `pass(59)^`, its `s1-59` line, and from that count decides its S3: a 0 means unit 59 built
without unit 62's amendment and owes a deviation record of `TOOL-dTotalRecall-59`. Its §5 says an
empty `P59` "is refused by git show". It is not: an empty revision reads the index blob, exit 0, and
the bare `^` an unresolved `pass(59)^` leaves reads nothing, exit 0. On that path the count comes
from unit 62's amended index text, which reads 1 and skips the record, or from an empty string,
which reads 0 and fabricates one. S3's decision then rests on a count read at no revision of unit
59's.

This unit re-reads that count at the verified parent of unit 59's pass through
`TOOL-dTotalRecall-81`'s guarded read, and makes S3's decision again from it, writing the record of
unit 59 once where it is owed and absent. It repairs `TOOL-dTotalRecall-74`, at step 35, one above
that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. `read_at "$(pass_of 59)^" 59` counts the absorbs-is-absent string over unit
  59's spec. The ledger prints the sha read and the count beside unit 74's `s1-59` line. Observed by
  AC1.
- **S2** — The liveness. The same read over specs 59 and 62 at `653bed738` prints 0 and 1, the values
  unit 74 §4 pins. Observed by AC1.
- **S3** — The decision, once. Where S1 reads 0, a deviation record of `TOOL-dTotalRecall-59` naming
  `pass(59)` and the string is owed. Before writing,
  `git grep -l "deviation TOOL-dTotalRecall-59" -- memory/builds/dTotalRecall/build` is read, and the
  record is written only where none names `pass(59)` and the string. Where S1 reads 1 or more and a
  record of unit 59 names this departure, that record was fabricated from an unverified read, and the
  ledger names it for the batch's item M15 (id 44). Observed by AC2.
- **S4** — Unit 74's departure. Where unit 74's `s1-59` differs from S1, a deviation record of
  `TOOL-dTotalRecall-74` names both counts and the sha S1 read. Observed by AC2.

## 3. Non-goals (OUT)

- The `s1-46` count and unit 74's S4 record: `TOOL-dTotalRecall-84`, which shares item H1.
- The read itself: `TOOL-dTotalRecall-81`.
- Unit 59's AC2 run whole, its `kit.toml` grep and the three `legacy_ledger.py` copies (items M3, L3
  and L9, ids 4, 14 and 45): the batch `TOOL-dTotalRecall-88`.
- Merging two records of unit 59 that already exist (item M15, id 44): the batch.
- Editing unit 74's or unit 59's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-74` — its pass at step 34, its `s1-59` line and its S3 record, which this unit re-decides at a verified revision
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read S1 and S2 run through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3 and S4 write through
- **hands-off** `TOOL-dTotalRecall-89` — its decision table, its recorded S1 and the records it names fabricated, the arm by which that unit grades unit 88's AC13 (the round-1 audit of units 77 to 88, id 1)
- **hands-off** `TOOL-dTotalRecall-90` — its S1 line, its decision table and any record of unit 59 its pass wrote, which that unit re-decides from a labelled line (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-92` — its AC1 line, its order paragraph and its records of units 59 and 74, which that batch corrects and counts (the round-1 audit of units 77 to 88, ids 7, 10, 12, 20, 24, 26)
- **hands-off** `TOOL-dTotalRecall-95` — the Evidence its §4 puts in a record of unit 59, `pass(59)` and the string, the key that unit makes the departure's one key (the round-1 audit of units 89 to 92, id 2)

## 4. Design

### The re-read

```bash
# run from the repository root, with unit 81 §4's two functions sourced
cat > "$SCRATCH/s83.txt" <<'STRINGS'
`absorbs` is absent
STRINGS
P=$(pass_of 59) && read_at "$P^" 59 "$SCRATCH/s83.txt"
read_at 653bed738 59 "$SCRATCH/s83.txt"
read_at 653bed738 62 "$SCRATCH/s83.txt"
```

The first line is S1. The other two are S2. A red line from `pass_of` or `read_at` stops the pass,
and no decision is made from it.

PINNED, measured 2026-10-26 at `af814dba8` with unit 81's `read_at`: the string prints 0 over spec
59 and 1 over spec 62 at `653bed738`.

### The decision table

| S1 | A record of unit 59 naming the departure | Action |
|---|---|---|
| 0 | none | write it |
| 0 | one | none |
| 1 or more | none | none |
| 1 or more | one or more | name it in the ledger as read from an unverified count |

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`, `Hand-off`
`spec-to-code`, `Cause` `review finding`, the approver under the chain's `author-recorded` value
(`PLAY-dClosedLoop-4`) and `Caused-by` `TOOL-dTotalRecall-83`. The record of unit 59 carries the
Evidence unit 74 §4 names: `pass(59)`, the string, unit 62's §4 "The amendments to unit 59" and unit
70's AC1 line, with S1's sha and count in place of unit 74's.

### Why order 35

Unit 74 records its reading at step 34. Step 35 is the first step after it.
`TOOL-dTotalRecall-76` and `TOOL-dTotalRecall-84` share the step, and neither writes a record of
unit 59 or 74.

### Inventory

Minted: nothing in code; at most one deviation record each of `TOOL-dTotalRecall-59` and
`TOOL-dTotalRecall-74`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, and the records of S3 and S4)

### Alternatives rejected

- **Keep unit 74's S3 outcome.** It was decided from a count read at no verified revision.
- **Delete a record S1 shows fabricated.** A deviation record is evidence of what a pass did; the
  batch's item for id 44 owns how two records of one departure are made one.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass-commit walk and three blob reads.
- error / empty / loading states — an unresolved pass(59) or an absent blob is a red line and stops
  the pass.
- observability — the ledger names S1's sha and count beside unit 74's.
- risks — none beyond the read's own, which unit 81 states.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's three reads run at this pass's base, the first prints the sha of
  `git rev-parse "$(pass_of 59)^"` with a count, and the other two print 0 and 1 over specs 59 and 62
  with the sha `653bed738685`.
  Red when: the first read prints a count without that sha, or a liveness read prints otherwise.
  figure: the liveness counts are PINNED in §4, measured 2026-10-26; S1's count is DERIVED.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-83" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names S1's count beside unit 74's `s1-59`. Where S1 reads 0,
  `git grep -l "deviation TOOL-dTotalRecall-59" -- memory/builds/dTotalRecall/build` prints one record
  naming `pass(59)`. Where the two counts differ, `git grep -l "deviation TOOL-dTotalRecall-74" -- memory/builds/dTotalRecall/build`
  prints a record naming both.
  Red when: a record is owed and absent, or this pass wrote a second record of one departure.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's read and its two liveness reads.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 9
  (HIGH, item H1, shared with id 36).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-89, TOOL-dTotalRecall-90, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-95, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-81`'s guarded read and the record door `gov_record.py new deviation`
of `TOOL-dTotalRecall-2`. `python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls. The recall
query below found this audit's fix text,
unit 74's §5 claim that `git show` refuses an empty revision, which the audit refuted, and the
`aUnmannedHelm` review that guarded a base by `rev-parse --verify` before reading it. No existing
seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
