# TOOL-dTotalRecall-84 — unit 74's `s1-46` count is re-read at the verified parent of unit 46's pass, and its S4 record of unit 70's reading is made from that count

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 35 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 36 at HIGH**. It shares item **H1** with id 9, which is
`TOOL-dTotalRecall-83`.

`TOOL-dTotalRecall-74` (order 34) prepends `os.environ['P46']` to its revision and relies on
`check=True`. An unresolved `pass(46)^` therefore reads the current index text or an empty string as
a count, never a red. Its `s1-46` line counts ``Minted: `SUFFIX_RE` `` over unit 46's spec, and its
S4 sets that count beside the one unit 70's AC8 line recorded, naming a false certification of
unit 70 where unit 70 recorded 1 or more and the count is 0. Read at no verified revision, S4 either
certifies unit 70's reading on the index's text or names a false certification that is not there.

This unit re-reads `s1-46` at the verified parent of unit 46's pass through
`TOOL-dTotalRecall-81`'s guarded read, proves the read can print a 0 and a 1 for that string, and
makes S4's comparison again from the verified count. It repairs `TOOL-dTotalRecall-74`, at step 35,
one above that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. `read_at "$(pass_of 46)^" 46` counts ``Minted: `SUFFIX_RE` `` over unit 46's
  spec. The ledger prints the sha read and the count. Observed by AC1.
- **S2** — The liveness. The same read prints 1 over spec 46 and 0 over spec 64 at `653bed738`.
  Observed by AC1.
- **S3** — S4 made again. The ledger sets S1's count beside unit 74's `s1-46` and beside the count
  unit 70's AC8 line recorded for the string. Where unit 70 recorded 1 or more and S1 reads 0, a
  deviation record of `TOOL-dTotalRecall-70` names the false certification. Where unit 74's `s1-46`
  differs from S1, a deviation record of `TOOL-dTotalRecall-74` names both counts and S1's sha. Each
  record is written only where `git grep -l` over the build folder lists none naming that string for
  that unit. Observed by AC2.

## 3. Non-goals (OUT)

- `s1-59` and the record of unit 59: `TOOL-dTotalRecall-83`, which shares item H1.
- The read itself: `TOOL-dTotalRecall-81`.
- Unit 46's body, which unit 70's S16 and S17 judge by the code. The string is a PINNED text reading,
  and this unit only corrects the record of it, as unit 74 §3 states.
- Editing unit 74's, unit 70's or unit 46's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-74` — its `s1-46` line and its S4 comparison, which this unit re-makes at a verified revision
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read S1 and S2 run through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3 writes through
- **hands-off** `TOOL-dTotalRecall-90` — its S1 line and its comparison, which that unit re-makes from a labelled line (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-92` — its AC1 line and its record of unit 74, which that batch reads and counts (the round-1 audit of units 77 to 88, ids 7, 10, 12, 20, 24, 26)

## 4. Design

### The re-read

```bash
# run from the repository root, with unit 81 §4's two functions sourced
cat > "$SCRATCH/s84.txt" <<'STRINGS'
Minted: `SUFFIX_RE`
STRINGS
P=$(pass_of 46) && read_at "$P^" 46 "$SCRATCH/s84.txt"
read_at 653bed738 46 "$SCRATCH/s84.txt"
read_at 653bed738 64 "$SCRATCH/s84.txt"
```

The first line is S1, the other two S2. A red line stops the pass.

PINNED, measured 2026-10-26 at `af814dba8` with unit 81's `read_at`: the string prints 1 over spec
46 and 0 over spec 64 at `653bed738`.

### The comparison

| Unit 70's AC8 figure | S1 | Record |
|---|---|---|
| 1 or more | 0 | unit 70's false certification, once |
| any | equal to unit 74's `s1-46` | none of unit 74 |
| any | different from unit 74's `s1-46` | unit 74's departure, once |

Unit 70's and unit 74's figures are prose in their ledgers, read by eye and quoted.

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`, `Hand-off`
`spec-to-code`, `Cause` `review finding`, the approver under the chain's `author-recorded` value
(`PLAY-dClosedLoop-4`) and `Caused-by` `TOOL-dTotalRecall-84`. Its Evidence names the string, S1's
sha and count, the figure it departs from and item H1.

### Why order 35

Unit 74 records its reading at step 34. Step 35 is the first step after it.

### Inventory

Minted: nothing in code; at most one deviation record each of `TOOL-dTotalRecall-70` and
`TOOL-dTotalRecall-74`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, and the records of S3)

### Alternatives rejected

- **A 0 taken from a copy with the string deleted.** That copy is built from the needle and reads 0
  by construction (item M1, id 2). Spec 64 at `653bed738` is an independent text that does not hold
  the string, so its 0 is a reading.
- **Keep unit 74's S4 record.** It was made from a count read at no verified revision.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass-commit walk and three blob reads.
- error / empty / loading states — an unresolved pass(46) or an absent blob is a red line and stops
  the pass.
- observability — the ledger names S1's sha and count beside both recorded figures.
- risks — the recorded figures are prose, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's three reads run at this pass's base, the first prints the sha of
  `git rev-parse "$(pass_of 46)^"` with a count, and the other two print 1 over spec 46 and 0 over
  spec 64 with the sha `653bed738685`.
  Red when: the first read prints a count without that sha, or a liveness read prints otherwise.
  figure: the liveness counts are PINNED in §4, measured 2026-10-26; S1's count is DERIVED.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-84" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names S1's count beside unit 74's `s1-46` and unit 70's AC8
  figure. Where §4's table owes a record, `git grep -l "deviation TOOL-dTotalRecall-70" -- memory/builds/dTotalRecall/build`
  or the same for `TOOL-dTotalRecall-74` prints one record naming the string.
  Red when: a record is owed and absent, or two name one departure.

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

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 36
  (HIGH, item H1, shared with id 9).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-90, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-81`'s guarded read and the record door `gov_record.py new deviation`
of `TOOL-dTotalRecall-2`. `python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls. The recall
query below found this audit's fix text,
unit 74's §5 claim that `git show` refuses an empty revision, which the audit refuted, and the
`aUnmannedHelm` review that guarded a base by `rev-parse --verify` before reading it. No existing
seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
