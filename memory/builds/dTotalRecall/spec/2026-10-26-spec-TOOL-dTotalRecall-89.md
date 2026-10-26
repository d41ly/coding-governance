# TOOL-dTotalRecall-89 — unit 88's AC13 is answered on both arms of unit 83's decision, so no record of unit 59 is written or kept to satisfy a count the decision rules out

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-89-deviation-891.md](../build/2026-10-26-build-TOOL-dTotalRecall-89-deviation-891.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-89-round8-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-89-round8-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-89-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-89-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-89-round8-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-89-round8-fix-brief.md) | research | — |
| [2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 77 to 88
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item.

`TOOL-dTotalRecall-88` (order 37) requires, in its S19 and its AC13 (spec 88 lines 115-117 and
365-367), exactly one deviation record of unit 59 naming `pass(59)` and the absorbs-is-absent
string, with no condition; its only red is two records. `TOOL-dTotalRecall-83`'s decision table
(spec 83 §4) owes that record only where its verified S1 reads 0. Where S1 reads 1 or more, no record
is owed: with none present, none is written, and an existing one is named in the ledger as
fabricated. On that arm AC13 either reds on a correct tree holding no record, or passes on the very
record unit 83 named fabricated, and a builder writing one to turn AC13 green ships a false record.

This unit answers AC13 again on both arms. It re-derives unit 83's S1 through a labelled read,
counts the live records of unit 59 that name the departure, and grades the count against the arm:
one where S1 reads 0, and where S1 reads 1 or more, every such record named fabricated and none
written at or after unit 83's pass. Where unit 88's own answer differs, a deviation record of unit 88
names it. It repairs `TOOL-dTotalRecall-88`, at order 38, one above that unit's 37.

## 2. Scope (IN)

- **S1** — The arm. `s1 s1-59 59 '^' 59` (`TOOL-dTotalRecall-90` §4) counts the absorbs-is-absent
  string over unit 59's spec at the verified parent of unit 59's pass. The ledger sets the line beside
  unit 83's recorded S1 and unit 90's `s1-59` line. A red line is the unresolved arm. Observed by AC1.
- **S2** — The population. `has_deviation memory/builds/dTotalRecall/build 59` with the tokens
  `pass(59)` and `` `absorbs` is absent `` counts the live records of unit 59 that name the departure.
  The ledger lists each with its path and the commit that added it. Observed by AC1.
- **S3** — The answer. AC13 is graded by §4's table from S1's arm and S2's count. Observed by AC2.
- **S4** — The owed record. Where S1 reads 0 and S2 counts none, this pass writes the record of
  `TOOL-dTotalRecall-59`, once, by `TOOL-dTotalRecall-90` §4's recipe, its Evidence naming `pass(59)`,
  the string, S1's line and the token `audit-77 id 1 s1-59`. Observed by AC2.
- **S5** — Unit 88's departure. Where unit 88's ledger answered AC13 otherwise than S3, a deviation
  record of `TOOL-dTotalRecall-88` names AC13's unconditional count, the arm and S3's answer. It is
  written only where `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1'` prints 0.
  Observed by AC3.

## 3. Non-goals (OUT)

- Making two records of one departure one, by hand or through the door (item M9, id 17): the batch
  `TOOL-dTotalRecall-92`. This unit names each such record and writes none.
- Unit 83's own re-read and decision: `TOOL-dTotalRecall-83`, corrected by `TOOL-dTotalRecall-90`.
- Deleting or editing a record S3 names fabricated. A deviation record is evidence of what a pass
  did, as spec 83 §4 "Alternatives rejected" states.
- Editing unit 88's or unit 83's spec, each frozen once its unit builds.
- The bug-class entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-88` — its S19 outcome and its AC13 answer, which this unit grades again on both arms of unit 83's decision
- **consumes-from** `TOOL-dTotalRecall-83` — its decision table, its recorded S1 and the records it names fabricated, the arm this unit's answer follows
- **consumes-from** `TOOL-dTotalRecall-90` — `s1`, `has_deviation` and its record recipe; without them S1 is taken by position and the count by `git grep`
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, which resolves unit 83's pass for S3's ancestry check
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's and S5's records are written through
- **consumes-from** `TOOL-dTotalRecall-93` — the re-keyed `has_deviation`, through which this unit's S2, S4 and S5 guards and its AC2 and AC3 counts are made in place of unit 90's, which keys a record by its Departs from address (the round-1 audit of units 89 to 92, id 1)
- **consumes-from** `TOOL-dTotalRecall-95` — the one key of unit 59's absorbs departure, `pass(59)` with the string, which every live record of it carries after that unit's pass, so S2 counts and S4 guards every such record (the round-1 audit of units 89 to 92, id 2)
- **hands-off** `TOOL-dTotalRecall-100` — its guards, its AC3 and AC13 answers and its ancestry walk, which that batch makes again at the tip (the round-1 audit of units 89 to 92, ids 13, 14, 16, 21, 26, 31)

## 4. Design

### The reads

```bash
# run from the repository root, with unit 81 §4's and unit 90 §4's functions sourced
cat > "$SCRATCH/s89.txt" <<'STRINGS'
`absorbs` is absent
STRINGS
s1 s1-59 59 '^' 59 "$SCRATCH/s89.txt"
has_deviation memory/builds/dTotalRecall/build 59 'pass(59)' '`absorbs` is absent'
P83=$(pass_of 83) || echo "p83 $P83"
for f in memory/builds/dTotalRecall/build/*-deviation-*.md; do
  grep -q 'pass(59)' "$f" && grep -qF '`absorbs` is absent' "$f" || continue
  A=$(git log --diff-filter=A --format=%H -1 -- "$f"); echo "rec $f added ${A:-untracked}"
  [ -n "$A" ] && { git merge-base --is-ancestor "$P83" "$A" && echo "rec $f at-or-after-p83"; }
done
```

The `rec` lines list candidates for the ledger; the count is `has_deviation`'s, which also reads the
record's address and its `**Supersedes:**` relation. A record with no adding commit is untracked,
which reads as written at this pass.

### The table

| S1 | S2 count | AC13 | Action |
|---|---|---|---|
| 0 | 1 | green | none |
| 0 | 0 | red, an owed record absent | S4 writes it |
| 0 | 2 or more | red, one departure recorded twice | the ledger names each path |
| 1 or more | 0 | green, none owed and none written | none |
| 1 or more | 1 or more | green only where each is named fabricated and none is at or after `pass(83)` | the ledger names each, with its adding commit |
| red | any | unresolved | none; the ledger names the red |

### Why order 38

Unit 88 writes and answers AC13 at order 37, and unit 90 corrects unit 83's decision at 36. This
unit reads both, so it is the first order after unit 88's.

### Inventory

Minted: nothing in code; at most one deviation record each of `TOOL-dTotalRecall-59` and
`TOOL-dTotalRecall-88`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4 and S5)

### Alternatives rejected

- **Take S1 from unit 83's ledger.** Unit 83 read S1 by position, which item H2 showed can be a
  liveness line; S1 re-derived by label is cheap and cannot be that.
- **Write a record of unit 59 whenever none exists.** On the S1-at-least-1 arm that is the false
  record unit 83's table forbids.
- **Hand AC13 back to unit 88 by a rev bump.** A spec is frozen once its unit builds, and unit 88
  builds at 37.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass-commit walk, one blob read and one pass over the build folder's records.
- error / empty / loading states — an unresolved `pass(59)` is the unresolved arm and decides
  nothing; an unresolved `pass(83)` prints its red line and leaves S3's ancestry ungraded.
- observability — the ledger names the arm, the count, each record's path and its adding commit.
- risks — none beyond the read's, which unit 81 states.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's reads run at this pass's base, `s1-59` leads exactly one line, holding a count
  with the sha of `git rev-parse "$(pass_of 59)^"` or a red line, and `has_deviation` prints one
  count.
  Red when: the arm is taken from an unlabelled line, or the count from a file that is not a record.
  figure: both values are DERIVED at the pass.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-89" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names S1's arm, S2's count, each record's path and adding commit,
  and AC13's answer by §4's table. Where S1 reads 0, `has_deviation` for unit 59 with `pass(59)` and
  the string prints 1; where S1 reads 1 or more, no record it counts was added at or after `pass(83)`.
  Red when: a record of unit 59 is written on the S1-at-least-1 arm, or AC13 reads green on the
  S1-is-0 arm with no record.
- **AC3** — When `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1'` runs after the
  pass, it prints 1 where unit 88's AC13 answer differs from AC2's, else 0.
  Red when: the two answers differ and no record names it, or two do.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's labelled read and its count of the build folder.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 77 to 88, id 1
  (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the consumes-from edge to TOOL-dTotalRecall-93, the consumes-from edge to TOOL-dTotalRecall-95, the mirror of TOOL-dTotalRecall-100, each the other end of an edge a unit the
  round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-90`'s `s1` and `has_deviation`, `TOOL-dTotalRecall-81`'s `pass_of`,
and git's own `log --diff-filter=A` and `merge-base --is-ancestor` for a record's adding commit.
`python tools/codebase-map/reuse_lookup.py "count deviation records of one unit by a computed key over the working tree"`
ranked `read_records` (`tools/memory-tree/deviation_join.py:268`) among its SEAM candidates, which
`has_deviation` already reads past for untracked files. The recall query below found this audit's
item H1, spec 83's decision table and spec 88's S19, and no criterion elsewhere that branches a
record count on another unit's decision. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is a count of deviation records graded when another unit decides whether the record is owed" --terms "deviation record unit 59 pass(59) absorbs fabricated decision table S1 AC13 owed arm count"`
