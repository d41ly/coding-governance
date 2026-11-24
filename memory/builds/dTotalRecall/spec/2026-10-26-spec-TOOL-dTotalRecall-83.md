# TOOL-dTotalRecall-83 — unit 74's `s1-59` count is re-read at the verified parent of unit 59's pass, and the decision it feeds, a deviation record of unit 59, is made again from it

**Status:** CLOSED · rev-4 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 35 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-83-deviation-831.md](../build/2026-10-26-build-TOOL-dTotalRecall-83-deviation-831.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-83-deviation-832.md](../build/2026-10-26-build-TOOL-dTotalRecall-83-deviation-832.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-83-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-83-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-83-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-83-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-83-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-83-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-83-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-83-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-83-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-83-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 9 at HIGH**. It shares item **H1** with id 36, which is
`TOOL-dTotalRecall-84`.

`TOOL-dTotalRecall-74` (order 34), as audited, counted the absorbs-is-absent string of unit 62 §4 over unit 59's spec
at `pass(59)^`, its `s1-59` line, and from that count decided its S3: a 0 means unit 59 built without unit 62's
amendment and owes a deviation record of `TOOL-dTotalRecall-59`. It read that revision from the environment, where an
empty one reads the index blob and a bare `^` reads nothing, both at exit 0. On that path the count comes from unit
62's amended index text, which reads 1 and skips the record, or from an empty string, which reads 0 and fabricates one.

Re-grounded at `f7011dd6f`: unit 74 rev-3 resolves each revision before it reads it, so the fall-through is gone from
the text its pass builds from. It reads `s1-59` at the literal `47afc8937^`, which is `206422580`, where the count is 1,
and writes no record. What stands is the independent check the finding asks for. This unit re-reads that count at the
parent of the commit the driver's own pass rule resolves for unit 59, through `TOOL-dTotalRecall-81`'s guarded read. It
proves that the read can print a 0 and a 1 for the string, and makes S3's decision again from the verified count. That
count is 1, so unit 59 built from unit 62's amended text, no record of unit 59 is owed and this pass writes none. It
repairs `TOOL-dTotalRecall-74`, at step 35, one above that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. `read_at "$(pass_of 59)^" 59` counts the absorbs-is-absent string over unit
  59's spec. The ledger prints the sha read and the count, which §4 pins, beside unit 74's `s1-59` line. Observed by
  AC1 and AC2.
- **S2** — The liveness. The same read over specs 59 and 62 at `653bed738` prints 0 and 1, and the first read with a
  unit off the roster prints a red line. Observed by AC1.
- **S3** — The decision, once. Where S1 reads 0, a deviation record of `TOOL-dTotalRecall-59` naming
  `pass(59)` and the string is owed. S1 reads 1, a property of a blob that cannot move, so none is owed, and the write
  is cut with that reason. §4's write-once read for unit 59 is still made. Where it lists a record, that record asserts
  a departure S1 refutes, and the ledger names it as fabricated, for `TOOL-dTotalRecall-88`'s item M15 (id 44).
  Observed by AC2.
- **S4** — Unit 74's departure. Where the `s1-59` sha or count unit 74's ledger records differs from S1's, a deviation
  record of `TOOL-dTotalRecall-74` names both readings, written only where §4's write-once read for unit 74 lists none.
  Observed by AC2.

## 3. Non-goals (OUT)

- The `s1-46` count and unit 74's S4 record: `TOOL-dTotalRecall-84`, which shares item H1.
- The read itself: `TOOL-dTotalRecall-81`.
- The labels on each printed line: `TOOL-dTotalRecall-90`.
- Unit 59's AC2 run whole, its `kit.toml` grep and the three `legacy_ledger.py` copies (items M3, L3
  and L9, ids 4, 14 and 45): the batch `TOOL-dTotalRecall-88`.
- Merging two records of unit 59 that already exist (item M15, id 44): the batch.
- Editing unit 74's or unit 59's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-74` — its pass at step 34, its `s1-59` line and its S3 decision, which this unit re-makes at a verified revision
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read S1 and S2 run through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4 writes through
- **hands-off** `TOOL-dTotalRecall-89` — its decision table, its recorded S1 and the records it names fabricated, the arm by which that unit grades unit 88's AC13 (the round-1 audit of units 77 to 88, id 1)
- **hands-off** `TOOL-dTotalRecall-90` — its S1 line, its decision table and any record of unit 59 its pass wrote, which that unit re-decides from a labelled line (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-92` — its AC1 line, its order paragraph and its records of units 59 and 74, which that batch corrects and counts (the round-1 audit of units 77 to 88, ids 7, 10, 12, 20, 24, 26)
- **hands-off** `TOOL-dTotalRecall-95` — the Evidence its §4 puts in a record of unit 59, `pass(59)` and the string, the key that unit makes the departure's one key (the round-1 audit of units 89 to 92, id 2)

## 4. Design

### The re-read

```bash
# run from the repository root, with unit 81 §4's first bash fence sourced from a file under $SCRATCH
cat > "$SCRATCH/s83.txt" <<'STRINGS'
`absorbs` is absent
STRINGS
if P=$(pass_of 59); then read_at "$P^" 59 "$SCRATCH/s83.txt"; else echo "$P"; fi
read_at 653bed738 59 "$SCRATCH/s83.txt"
read_at 653bed738 62 "$SCRATCH/s83.txt"
```

The first read is S1, taken by the sha it prints, never by a line's position. The other two are S2. A red line stops the
pass, and no decision is made from it. `pass_of` prints its red line on stdout, so the substitution captures it and
rev-3's `P=$(pass_of 59) && read_at` printed nothing where the pass did not resolve; the `else` prints it. Unit 81's
fence sources the launcher resolver and the driver's library itself. The fence goes in a script file under `$SCRATCH`.

PINNED 2026-11-24 at `f7011dd6f`, these reads: `206422580b7363ab9582e37ffe7de7c25773a721 1`, then
`653bed738685c8d41ee71fbf740a5e3654bdd703` with 0 over spec 59 and with 1 over spec 62, each followed by the string.
`pass_of 59` printed `47afc89374e539d933728b5f0a06b9678a4ac388`, the one commit the `Pass:` trailer of unit 59 names,
and the first read with 999 printed `red 999 no pass commit`. An empty revision and a bare `^` each printed a red line
and returned 1. Both S2 counts are the ones measured 2026-10-26 at `af814dba8`.

### The decision table

| S1 | A record of unit 59 naming the departure | Action |
|---|---|---|
| 0 | none | write it |
| 0 | one | none |
| 1 or more | none | none |
| 1 or more | one or more | name it in the ledger as fabricated, its count unverified |

The third row holds: S1 is 1 (PINNED above), and the read below lists no record of unit 59 (DERIVED 2026-11-24 at
`f7011dd6f`). The rows on a 0 stand as the rule `TOOL-dTotalRecall-89` and `TOOL-dTotalRecall-90` re-read.

### The deviation records

None of unit 59 is owed (S3). The key `TOOL-dTotalRecall-95` reads stays this one: a record of unit 59 for this
departure would carry in its Evidence `pass(59)`, the string, unit 62's §4 "The amendments to unit 59" and unit 70's
AC1 line, with S1's sha and count, as unit 74 §4 names it. The build's one record of unit 59,
`2026-10-26-build-TOOL-dTotalRecall-59-deviation-591`, is its roster record and names neither.

The write-once read, from `memory/builds/dTotalRecall/build/`, for unit 59 and the same with 74:

```bash
grep -lE 'pass\(59\)|absorbs. is absent' *-build-TOOL-dTotalRecall-59-deviation-*.md
```

It reads the door's own file names in the working tree, so a record not yet committed counts and a ledger quoting one
does not. At `f7011dd6f` it lists nothing for either unit and exits 1, and with `roster` for the pattern it lists
`-59-deviation-591` and `-74-deviation-741` (DERIVED 2026-11-24), so it is seen both ways and those records never count.

S4's record is written by
`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-74 --title <text>`,
which refuses a missing `--title` or required field (`tools/memory-tree/build_records.py#write_new_record`). It takes
one `--field` per required name of the deviation entry of `tools/memory-tree/build_records.py#KINDS`:

- `Departs from` `TOOL-dTotalRecall-74@rev-<n> [§6 AC1]`, the rev unit 74's header holds at its pass.
- `Hand-off` `spec-to-code`; `Cause` `review finding`; `Risk` `loosening`, as the recorded figure certifies a reading
  the blob does not hold.
- `Before` the sha and count unit 74's ledger records; `After` S1's; `Reason` the read that gave the recorded figure.
- `Approver` opening with the role `author`, under the chain's `author-recorded` value
  (`tools/memory-tree/deviation_join.py#HOST_APPROVAL`, `PLAY-dClosedLoop-4`).
- `Follow-through` `ask TOOL-dTotalRecall-27`; `Caused-by` `TOOL-dTotalRecall-83`.
- `Evidence` the string, `s1-59`, both readings and item H1 of the round-7 audit
  (`2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1`).

Unit 74's sha is twelve digits long (`206422580b73`, unit 74 rev-3 §4) and is compared as a prefix of S1's.

### Why order 35

Unit 74 records its reading at step 34. Step 35 is the first step after it.
`TOOL-dTotalRecall-76` and `TOOL-dTotalRecall-84` share the step, and neither writes a record of unit 59. Unit 84 may
write a record of unit 74, for `s1-46`, which the write-once read's string tells apart.

### Inventory

Minted: nothing in code; at most one deviation record of `TOOL-dTotalRecall-74`, and none of `TOOL-dTotalRecall-59`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, and the record S4 may owe)

### Alternatives rejected

- **Keep unit 74's S3 outcome alone.** Its revision is a literal its spec names, never resolved by the driver's pass
  rule.
- **Write a record of unit 59 for the check itself.** S1 reads 1, so it would assert a departure that did not happen.
- **Cut S4's record because S1 is settled.** The figure S1 is compared with is unit 74's ledger line, not written until
  its pass.
- **Delete a record S1 shows fabricated.** A deviation record is evidence of what a pass did; the
  batch's item for id 44 owns how two records of one departure are made one.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass-commit walk and three blob reads.
- error / empty / loading states — an unresolved pass(59) or an absent blob is a red line and stops
  the pass. Once a run-state rotation moves unit 59's dispatch row out of `RUN.md`, `pass_of 59` is that red, as unit 81
  §5 states.
- observability — the ledger names S1's sha and count beside unit 74's.
- risks — none beyond the read's own, which unit 81 states. Unit 74's figure is prose in its ledger, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's three reads run at this pass's base, the first prints the sha of
  `git rev-parse "$(pass_of 59)^"`, `206422580b73` abbreviated, with the count 1, and the other two print 0 and 1 over
  specs 59 and 62 with the sha `653bed738685`. In the same shell, §4's first read with 999 as `pass_of`'s number prints
  `red 999 no pass commit`.
  Red when: the first read prints a count without that sha or another count, a liveness read prints otherwise, or an
  unresolved pass prints nothing.
  figure: the shas and counts are PINNED in §4, measured 2026-11-24; the pass's own lines are DERIVED by it.
- **AC2** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-83" -- memory/builds/dTotalRecall/build`
  runs after the pass, the ledger it names has an AC2 line setting S1's sha and count beside unit 74's `s1-59`, quoted
  with its ledger's file name, and the row of §4's decision table that holds. §4's write-once read prints nothing for
  unit 59, or only files the ledger names as fabricated, none caused by this unit. For unit 74 it prints nothing where
  the two readings agree, and exactly one file where they differ.
  Red when: a record of unit 59 is written by this pass, a record of unit 74 is owed and absent, or two name one
  departure.

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
- rev-4 · 2026-11-24 · title §1 S1 to S4 §3 §4 §5 AC1 AC2 §10 · re-grounded at HEAD `f7011dd6f` per
  `2026-11-24-prompt-TOOL-dTotalRecall-83-reground-brief`, over unit 74 rev-3: the Goal's environment revision is
  history; pass(59) is read and S1 pinned at 1, so S3's record is not owed and its write is cut; an unresolved pass
  prints its red, which the `&&` form swallowed; S4's record spells every field
  `tools/memory-tree/build_records.py#KINDS` requires, with `--title`; the write-once read is keyed on the record's file
  name; the order paragraph names unit 84's record of unit 74.

## 10. Reuse audit

The seams, re-read at `f7011dd6f`, are `TOOL-dTotalRecall-81` rev-4's guarded read, CLOSED and run by
`TOOL-dTotalRecall-82`'s pass, and the record door `gov_record.py new deviation` of `TOOL-dTotalRecall-2`, CLOSED.
`python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls; re-run 2026-11-24 it ranks both
again. The recall query below found this audit's fix text, unit 74's §5 claim that `git show` refuses an empty revision,
which the audit refuted and unit 74 rev-3 dropped, and the `aUnmannedHelm` review that guarded a base by
`rev-parse --verify` before reading it. Re-run 2026-11-24 it ranks unit 81 first and adds no other
read of this shape. No existing seam fits beyond them.
`tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder walks of `record_causes.py#check_cause_writers`
and `record_kinds.py#check_alias_compares` are no seam here: this unit reads no marker and no registry.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
