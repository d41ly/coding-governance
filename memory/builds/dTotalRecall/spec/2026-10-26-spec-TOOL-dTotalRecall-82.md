# TOOL-dTotalRecall-82 — unit 71's `pass67` count is re-read at unit 67's verified pass commit, and the deviation record of unit 67 it decides is written once

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 22 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**. It shares item **H2** with id 37, which is
`TOOL-dTotalRecall-81`.

`TOOL-dTotalRecall-71` (order 21) counts unit 57's edge to unit 56 over unit 57's spec at unit 67's
pass commit, its `pass67` line, and writes a deviation record of `TOOL-dTotalRecall-67` where unit
67 certified the edge and that count is 0. With PASS67 empty, the read falls through to the index.
At step 21 the index holds the edge `TOOL-dTotalRecall-72` has just written, so the probe prints
`pass67 1`, S3 writes no record, and unit 67's false certification goes unrecorded. That record is
what unit 71 exists to write.

This unit re-reads that count at unit 67's pass commit through `TOOL-dTotalRecall-81`'s guarded
read, which refuses an unresolved pass instead of reading the index. It then makes S3's decision
again on one stated condition and writes the record of unit 67 once, where it is owed and absent.
It repairs `TOOL-dTotalRecall-71`, at step 22, one above that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. `read_at "$(pass_of 67)" 57` counts the edge string of §4 over unit 57's
  spec at unit 67's pass commit. The ledger prints the sha and the count beside unit 71's `pass67`
  line. Observed by AC1.
- **S2** — The decision. Unit 67's figure is the count its AC1 ledger line recorded for the edge row
  at its TIP. A deviation record of `TOOL-dTotalRecall-67` is owed where that figure is at least 1 and
  S1 reads 0. Observed by AC2.
- **S3** — The record, once. Where S2 owes a record and
  `git grep -l "deviation TOOL-dTotalRecall-67" -- memory/builds/dTotalRecall/build` lists none whose
  Evidence names the edge row, this pass writes it through the door. Where unit 71 wrote one already,
  this pass writes none. Where unit 71's `pass67` differs from S1, this pass names unit 71's line as
  read at a revision other than unit 67's pass, in the same ledger line. Observed by AC2.

## 3. Non-goals (OUT)

- The read itself, its liveness and the resolution of PASS67: `TOOL-dTotalRecall-81`.
- Unit 71's `tip`, `without` and `only` lines, which read the working tree at its base and are not
  revision reads. Their liveness fixtures are item M1 (id 2), the batch `TOOL-dTotalRecall-88`'s.
- The wording of unit 71's S3 and AC2 against each other (item M13, id 41): the batch's.
- Editing unit 71's or unit 67's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-71` — its `pass67` line and its S3 decision, which this unit re-makes at a verified revision
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read S1 runs through; without it the re-read repeats the index fall-through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door the record of S3 is written through
- **hands-off** `TOOL-dTotalRecall-90` — its S1 line, its AC1 record and its decision table, which that unit re-makes from a labelled line (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-92` — its AC1 line and its write-once guard, which that batch reads for an empty S1 and re-runs anchored (the round-1 audit of units 77 to 88, ids 10, 12, 20, 24)

## 4. Design

### The re-read

```bash
# run from the repository root, with unit 81 §4's two functions sourced
cat > "$SCRATCH/s82.txt" <<'STRINGS'
**consumes-from** `TOOL-dTotalRecall-56`
STRINGS
P=$(pass_of 67) && read_at "$P" 57 "$SCRATCH/s82.txt"
```

It prints the sha, the count and the edge string on one line, or a red line where pass(67) does
not resolve. A red stops this pass: no decision is made from an unresolved pass.

PINNED, measured 2026-10-26 at `af814dba8`: the edge string prints 0 over spec 57 at `653bed738`
and at `af814dba8`, read by the same `read_at`. So S1 can read either value once unit 72 writes the
edge at step 21.

### The decision table

| Unit 67's recorded tip figure | S1 | Action |
|---|---|---|
| 1 or more | 0 | the record of unit 67 is owed: write it unless one exists |
| 1 or more | 1 or more | none; unit 67's certification holds at its pass |
| 0 | any | none; unit 67 did not certify the edge, and its own S2 owed the write |

The recorded tip figure is read by eye from unit 67's AC1 ledger line, as unit 71 §5 reads it, and
quoted in this unit's ledger line.

### The deviation record

`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-67`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`: `Departs from`
naming `TOOL-dTotalRecall-67` at its rev, `Hand-off` `spec-to-code`, `Cause` `review finding`, the
approver under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`), `Caused-by`
`TOOL-dTotalRecall-82`. Its Evidence names the edge row, unit 67's recorded figure, S1's sha and
count, and item B1 of the round-6 audit with item H2 of this one.

### Why order 22

The re-read rests on unit 81's read, at step 22, and on unit 71's pass at step 21. The §3 edge to
unit 81 runs that pass first.

### Inventory

Minted: nothing in code; at most one deviation record of `TOOL-dTotalRecall-67`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, and the record S3 writes)

### Alternatives rejected

- **Trust unit 71's S3 outcome.** It was decided from a count that may be the index's.
- **Write the record whenever S1 reads 0.** Unit 71 may have written it, and a second record lists
  one departure twice (the class of item M15, id 44).
- **Re-read at the working tree.** Unit 72 has written the edge there by step 22, which is the
  reading the defect produced.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass-commit walk and one blob read.
- error / empty / loading states — an unresolved pass(67) is a red line and the pass stops. An
  absent blob is a red line.
- observability — the ledger line names S1's sha and count, unit 71's `pass67` and unit 67's figure.
- risks — unit 67's figure is prose in its ledger, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's re-read runs at this pass's base, it prints one line holding a 40-hex sha, a
  count and the edge string, and that sha equals `pass_of 67`.
  Red when: the read prints a count with no sha, or reads at a revision that is not unit 67's pass.
  figure: the count is DERIVED by the read at the pass; the base values are PINNED in §4.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-82" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names S1's count, unit 71's `pass67` and unit 67's recorded tip
  figure. Where §4's table owes a record,
  `git grep -l "deviation TOOL-dTotalRecall-67" -- memory/builds/dTotalRecall/build` prints exactly
  one record naming the edge row.
  Red when: a record is owed and none names the edge row, or two do.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's read through unit 81's probe, whose liveness that unit
observes.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 10
  (HIGH, item H2, shared with id 37).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-90, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-81`'s guarded read, itself built on `pass_commit`
(`tools/unattended/lib-unattended.sh:1026`) and `tree_lib.read_blobs_at`
(`tools/memory-tree/tree_lib.py:328`), and the record door `gov_record.py new deviation` that
`TOOL-dTotalRecall-2` builds. `python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls. The recall
query below found this audit's fix text,
unit 74's §5 claim that `git show` refuses an empty revision, which the audit refuted, and the
`aUnmannedHelm` review that guarded a base by `rev-parse --verify` before reading it. No existing
seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
