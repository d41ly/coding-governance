# TOOL-dTotalRecall-86 — unit 76's S5 and S6 reads of unit 70's table and unit 46's strings are made again at verified revisions, so an unresolved pass is a red and never a count

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 38 at HIGH**. It shares item **H3** with id 11, which is
`TOOL-dTotalRecall-85`.

`TOOL-dTotalRecall-76` (order 35) feeds `REV=pass(T)^` into `git show REV + ':./…'` for its S5,
every row of unit 70's §4 table but the absorbs row, and its S6, two of unit 70's AC8 strings over
unit 46's spec. Its AC2 is red when "a failed `git show` is recorded as 0", and nothing enforces
that: `git show '^:./<spec>'` exits 0 with no output, and `git show ':./<spec>'` exits 0 with the
index blob. An S5 or S6 row whose unit has no resolvable pass commit yields a silent 0 or a read of
later text, and AC2's red cannot fire.

This unit makes the S5 and S6 reads again through `TOOL-dTotalRecall-81`'s guarded read, so an
unresolved pass is a printed red and never a count, proves each string can print both values over
independent texts, and makes each decision unit 76's S5 and S6 owed. It repairs
`TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The S5 reads. Each of the nine rows of §4's table is counted over its target spec at
  `"$(pass_of T)^"` by `read_at`, and set beside the count unit 76's AC2 line recorded and the
  count unit 70's AC1 line recorded. Observed by AC1 and AC2.
- **S2** — The S6 reads. `whose body this unit rebuilds` and `rebuilds the parser on that regex`
  are counted over unit 46's spec at `"$(pass_of 46)^"`, beside unit 76's and unit 70's AC8 counts.
  Observed by AC1 and AC2.
- **S3** — The liveness. Each string is counted over its target spec, its amending spec and spec 55
  at `653bed738`, printing §4's pinned pair and a 0. Observed by AC1.
- **S4** — The decisions. A row whose verified count fails its wanted value owes a deviation record
  of its target unit, as unit 76's S5 states, written only where `git grep -l` over the build folder
  lists none naming that string. A row whose verified count differs from unit 76's recorded one is
  named in one deviation record of `TOOL-dTotalRecall-76`, written once. Observed by AC2.

## 3. Non-goals (OUT)

- Unit 76's S1 to S4 reads: `TOOL-dTotalRecall-85`, which shares item H3.
- The absorbs row of unit 70's table and the ``Minted: `SUFFIX_RE` `` string:
  `TOOL-dTotalRecall-83` and `TOOL-dTotalRecall-84`.
- Unit 46's body, which unit 70's S16 and S17 judge by the code.
- The read itself: `TOOL-dTotalRecall-81`.
- Editing a landed spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S5 and S6 and its AC2 ledger line, whose counts this unit re-reads at verified revisions
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read every row runs through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4 writes through
- **hands-off** `TOOL-dTotalRecall-92` — its records and its write-once guard, which that batch scans for a malformed, duplicated or uncommitted record (the round-1 audit of units 77 to 88, ids 12, 15, 20, 24, 26)

## 4. Design

### The rows

Unit 70 §4's table, the absorbs row left out, with S6's string added. "1" wants at least 1, "0"
wants 0, and S6's string, which unit 64 amends nowhere, has no wanted value and is recorded only.

| T | Amending spec | String | Wanted | Liveness at `653bed738`: target, amending |
|---|---|---|---|---|
| 52 | 62 | `first seed record-kinds-legacy` | 1 | 0, 4 |
| 59 | 62 | `it replaces unit 52's absorbed-population arm` | 0 | 1, 1 |
| 46 | 63 | `ZED-aFoo-2` | 1 | 0, 5 |
| 46 | 64 | `This unit's pass builds no body and observes that one` | 1 | 0, 1 |
| 46 | 64 | `whose body unit 54 builds and this unit's criteria observe` | 1 | 0, 1 |
| 46 | 64 | `whose body this unit rebuilds` | 0 | 1, 2 |
| 55 | 61 | `whose last rows they are after unit 53` | 1 | 0, 1 |
| 56 | 61 | `whose last row it is after unit 53` | 1 | 0, 1 |
| 57 | 61 | `this one follows units 55 and 56` | 1 | 0, 1 |
| 46 | 64 | `rebuilds the parser on that regex` | none | 1, 0 |

PINNED, measured 2026-10-26 at `af814dba8` with unit 81's `read_at`: every pair in the last
column, and a 0 for every string of the table over spec 55 at `653bed738`. Each string is
therefore seen to read a 0 over an independent text and 1 or more over another, whatever its row
wants.

### The reads

One strings file per target spec, each written by a heredoc whose delimiter is quoted, then:

```bash
# run from the repository root, with unit 81 §4's two functions sourced
for T in 52 59 46 55 56 57; do
  P=$(pass_of "$T") && read_at "$P^" "$T" "$SCRATCH/s86-$T.txt" || echo "red rows of $T"
  read_at 653bed738 "$T" "$SCRATCH/s86-$T.txt"
done
for A in 55 61 62 63 64; do for T in 52 59 46 55 56 57; do read_at 653bed738 "$A" "$SCRATCH/s86-$T.txt"; done; done
```

A red line for a target stops that target's decisions, and the ledger names its rows as unresolved,
never as 0.

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`, `Hand-off`
`spec-to-code`, `Cause` `review finding`, the approver under the chain's `author-recorded` value
(`PLAY-dClosedLoop-4`) and `Caused-by` `TOOL-dTotalRecall-86`. Its Evidence names the row, the
verified sha and count, and item H3.

### Why order 36

Unit 76 records its S5 and S6 counts at step 35. Step 36 is the first step after it.

### Inventory

Minted: nothing in code; deviation records where a row fails its wanted value or differs from unit
76's count.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4)

### Alternatives rejected

- **Verify REV inside unit 76's probe and re-run it.** Unit 76's spec is frozen once its unit builds,
  and unit 81's read already verifies a revision once.
- **Liveness at the working tree.** Later amendments sit there, so it cannot read the 0 a target
  held before its amending unit.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — six pass-commit walks and thirty blob reads, each one `git cat-file --batch`.
- error / empty / loading states — an unresolved pass or an absent blob is a red line for its target,
  never a 0.
- observability — the ledger names each row's sha and count beside unit 76's and unit 70's counts.
- risks — the recorded counts are prose, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's reads run at this pass's base, every row prints a 40-hex sha equal to
  `git rev-parse "$(pass_of T)^"` with a count, or a `red` line naming its target, each liveness
  read prints the pair of §4's last column, and the reads over spec 55 at `653bed738` print 0 for
  every string.
  Red when: a row prints a count with no sha or at another revision, or a liveness pair differs.
  figure: the liveness pairs are PINNED in §4, measured 2026-10-26; the row counts are DERIVED.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-86" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names each row's verified count beside unit 76's and unit 70's.
  For each row that fails its wanted value, `git grep -l "deviation TOOL-dTotalRecall-<T>" -- memory/builds/dTotalRecall/build`
  prints one record naming the string.
  Red when: a failing row has no record or two, or a count was recorded for an unresolved target.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's reads and their liveness pairs.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 38
  (HIGH, item H3, shared with id 11).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-81`'s guarded read, unit 70 §4's table as its row list, and the
record door `gov_record.py new deviation` of `TOOL-dTotalRecall-2`.
`python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls. The recall
query below found this audit's fix text,
unit 74's §5 claim that `git show` refuses an empty revision, which the audit refuted, and the
`aUnmannedHelm` review that guarded a base by `rev-parse --verify` before reading it. No existing
seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
