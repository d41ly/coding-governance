# TOOL-dTotalRecall-85 — unit 76's S1 to S4 reads of units 55, 56 and 57 are made again at verified revisions, each count printed beside the sha it was read at

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, graded medium by its finder and high by the skeptic, whose
grade binds. It shares item **H3** with id 38, which is `TOOL-dTotalRecall-86`.

`TOOL-dTotalRecall-76` (order 35) reads five amendment strings over the specs of units 55, 56 and
57 at each unit's `pass(T)^` by its blob probe, its S1 to S4, observed by its AC1. The probe builds
`os.environ['REV'] + ':./…'` and never verifies REV. Its claim that "a failed read raises and is a
red, never a 0" is false: an empty REV reads the index blob, exit 0, and `REV=^` reads nothing, exit
0. An S1 to S4 row whose unit has no resolvable pass commit therefore reads either a silent 0, which
writes a fabricated deviation, or the text after later amendments, which certifies a build from text
the unit never saw.

This unit makes those five reads again through `TOOL-dTotalRecall-81`'s guarded read, proves each
string can print a 0 and a 1 over independent texts, and makes each decision unit 76's S1 to S4
owed from the verified count. It repairs `TOOL-dTotalRecall-76`, at step 36, one above that unit's
order.

## 2. Scope (IN)

- **S1** — The five reads. Each string of §4's table is counted over its target spec at
  `"$(pass_of T)^"` by `read_at`. The ledger prints each sha and count beside the count unit 76's
  AC1 line recorded for that row. Observed by AC1.
- **S2** — The liveness. Each string is counted over its target spec and over its amending spec at
  `653bed738`, or at `af814dba8` for the edge string, printing the pinned 0 and the pinned count of
  §4. Observed by AC1.
- **S3** — The decisions. A row whose verified count is 0 owes a deviation record of its target unit
  naming the string, as unit 76's S1 to S4 state. It is written only where
  `git grep -l "deviation TOOL-dTotalRecall-<T>" -- memory/builds/dTotalRecall/build` lists none
  naming that string. A row whose verified count differs from unit 76's recorded one is named in a
  deviation record of `TOOL-dTotalRecall-76`, one record for every such row of this unit, written
  once. Observed by AC2.

## 3. Non-goals (OUT)

- Unit 76's S5 and S6 reads: `TOOL-dTotalRecall-86`, which shares item H3.
- Unit 76's AC1 working-tree greps, `git grep -n CAUSE_WRITER_KEPT -- tools` and its sibling at the
  tip. They read code and not a revision, so the defect does not reach them.
- The read itself: `TOOL-dTotalRecall-81`.
- Editing a landed spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S1 to S4 and its AC1 ledger line, whose five counts this unit re-reads at verified revisions
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read every row runs through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3 writes through
- **hands-off** `TOOL-dTotalRecall-92` — its records and its write-once guard, which that batch scans for a malformed, duplicated or uncommitted record (the round-1 audit of units 77 to 88, ids 12, 15, 24, 26)

## 4. Design

### The rows

| T | Amending spec | String | Wanted at `pass(T)^` | Liveness at `653bed738`: target, amending |
|---|---|---|---|---|
| 55 | 61 | `holding only the build-folder rows this unit moves` | at least 1 | 0, 1 |
| 55 | 61 | `git grep -n CAUSE_WRITER_KEPT -- tools` | at least 1 | 0, 1 |
| 56 | 61 | ``**hands-off** `TOOL-dTotalRecall-57` `` | at least 1 | 0, 1 |
| 56 | 61 | `git grep -n ALIAS_COMPARE_KEPT -- tools` | at least 1 | 0, 1 |
| 57 | 72 | ``**consumes-from** `TOOL-dTotalRecall-56` `` | at least 1 | 0, and 3 over spec 72 at `af814dba8` |

PINNED, measured 2026-10-26 at `af814dba8` with unit 81's `read_at`: every value in the last column.
Spec 72's 3 counts the bullet of its §4 fence and two prose mentions; any count of 1 or more is the
reading S2 needs.

### The reads

```bash
# run from the repository root, with unit 81 §4's two functions sourced; one strings file per target
cat > "$SCRATCH/s85-55.txt" <<'STRINGS'
holding only the build-folder rows this unit moves
git grep -n CAUSE_WRITER_KEPT -- tools
STRINGS
cat > "$SCRATCH/s85-56.txt" <<'STRINGS'
**hands-off** `TOOL-dTotalRecall-57`
git grep -n ALIAS_COMPARE_KEPT -- tools
STRINGS
cat > "$SCRATCH/s85-57.txt" <<'STRINGS'
**consumes-from** `TOOL-dTotalRecall-56`
STRINGS
for T in 55 56 57; do P=$(pass_of "$T") && read_at "$P^" "$T" "$SCRATCH/s85-$T.txt" || echo "red row $T"; done
for T in 55 56 57 61; do read_at 653bed738 "$T" "$SCRATCH/s85-${T/61/55}.txt"; done
read_at 653bed738 61 "$SCRATCH/s85-56.txt"; read_at af814dba8 72 "$SCRATCH/s85-57.txt"
```

A red line for a row stops that row's decision, and the ledger names the row as unresolved. It is
never read as a 0.

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`, `Hand-off`
`spec-to-code`, `Cause` `review finding`, the approver under the chain's `author-recorded` value
(`PLAY-dClosedLoop-4`) and `Caused-by` `TOOL-dTotalRecall-85`. Its Evidence names the row, the
verified sha and count, and item H3.

### Why order 36

Unit 76 records its S1 to S4 counts at step 35. Step 36 is the first step after it.

### Inventory

Minted: nothing in code; deviation records where §4's rows read 0 or differ from unit 76's.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3)

### Alternatives rejected

- **Verify REV inside unit 76's probe and re-run it.** Unit 76's spec is frozen once its unit builds.
  The guarded read already exists at step 22 as unit 81's, so a second verifier would be a copy.
- **Liveness copies built by deleting the string.** They read 0 by construction (item M1, id 2).
  Specs 55, 56 and 57 at `653bed738` and the amending specs are independent texts.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — three pass-commit walks and ten blob reads.
- error / empty / loading states — an unresolved pass or an absent blob is a red line for its row,
  never a 0.
- observability — the ledger names each row's sha, count and unit 76's recorded count.
- risks — unit 76's counts are prose in its ledger, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's reads run at this pass's base, each of the five rows prints a 40-hex sha equal
  to `git rev-parse "$(pass_of T)^"` with a count, or a `red` line naming the row, and the liveness
  reads print the values of §4's last column.
  Red when: a row prints a count with no sha or at another revision, or a liveness read prints
  otherwise.
  figure: the liveness values are PINNED in §4, measured 2026-10-26; the row counts are DERIVED.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-85" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names each row's verified count beside unit 76's. For a row that
  read 0, `git grep -lE "deviation TOOL-dTotalRecall-5[567]$" -- memory/builds/dTotalRecall/build`
  prints one record of its unit naming the string.
  Red when: a 0 row has no record, a row has two, or a differing row is not named in a record of
  unit 76.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's reads and their liveness reads.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 11
  (HIGH, item H3, shared with id 38).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
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
