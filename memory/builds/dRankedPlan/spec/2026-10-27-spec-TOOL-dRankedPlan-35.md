# TOOL-dRankedPlan-35 — the newest disposition is ordered by ancestry, and kept records the order cannot rank hold the gate when their words differ

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-35-deviation-351.md](../build/2026-10-27-build-TOOL-dRankedPlan-35-deviation-351.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 28 at HIGH**, item **H5**. `TOOL-dRankedPlan-24` §4 "The bound" returns "the kept record whose
`added` is newest" and defines no order for two records added in one commit, or on two branches with
no ancestry between them. `TOOL-dRankedPlan-26` S2 rests on that pick, "the newest, so the owner's
latest word governs". The product's stated setting is several machines on one repository. Two
dispositions written on two machines after the transition and then merged leave the pick to whatever
order the code happens to use, so a deferral can lose to a `continue` and release Plan's exit. This
unit defines the order as ancestry, and holds the gate on a conflict when the order cannot rank the
kept records and their words differ. The clause it makes true is unit 26 S2's "the owner's latest word
governs", and the gate it holds is unit 26's. It repairs `TOOL-dRankedPlan-26`, so it sits one order
above it, after units 24, 25 and 26 have all landed.

## 2. Scope (IN)

- **S1** — The order. `derive_newest_disposition(repo, kept, why=None)` in `tools/loop/ratify.py`
  takes the records `TOOL-dRankedPlan-24`'s bound keeps, as `(path, fields, added)`. A record governs
  when every other kept record's `added` commit is a proper ancestor of its own, read by `git merge-base
  --is-ancestor`. When no record governs, the kept records the order leaves unranked are those that are
  no other record's ancestor. If they all carry one `Disposition`, resolved through `resolve_disposition`
  (`TOOL-dDeclaredLoop-16` S2) as unit 26 S1 resolves it, the path-sorted first of them governs. If
  their words differ, the answer is `None`, and `disposition conflict <path> <path>…` is appended to
  `why`. `read_item_disposition` (`TOOL-dRankedPlan-24` S1) gains the same `why` parameter and returns
  this answer. That is the convention `read_plan_ratification` takes for its reason (`TOOL-dRankedPlan-9`
  S1). This supersedes unit 24 §4's "return the kept record whose `added` is newest". Observed by AC1
  and AC2.
- **S2** — The gate and the arm. `check_plan_exit` (`TOOL-dRankedPlan-10` S4, its disposition taken
  through the reader by `TOOL-dRankedPlan-25` S1) passes a `why` list. On a conflict it refuses with
  `plan.exit — held · owner gate · disposition conflict <paths>`. `read_plan_ratification`'s
  `terminal-command` arm (`TOOL-dRankedPlan-24` S2) answers unratified with the same reason. Unit 26 S2's
  "the record it takes is the newest" now means S1's governing record. Observed by AC3 and AC4.
- **S3** — The plants. `reader-bound` (`TOOL-dRankedPlan-24` S3) gains two cases. In `one-commit`,
  two records for `item.plan.exit` are added after the newest transition in one commit, once with
  different words and once with the same word. In `merged-sides`, one record on each of two branches
  forked after the transition is merged, and then a third record is committed on top of the merge. A
  new plant, `conflict-hold`, runs `merged-sides` under the no-table fallback through the `plan.exit`
  move, and runs it again under `terminal-command`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- Which records are fresh, and how each is dated: `TOOL-dRankedPlan-24` and `TOOL-dRankedPlan-34`.
- Which words release: `TOOL-dRankedPlan-26`'s `HOLDING_DISPOSITIONS`, applied to the governing record.
- The dormancy disposal's own line on a conflict: `TOOL-dRankedPlan-4`'s `dispose`, which reads the same
  answer through the reader it is built on.
- A merge resolver that picks a word. A conflict is the owner's to settle by writing one more record.

### Edges

- **consumes-from** `TOOL-dRankedPlan-24` — `read_item_disposition` and its `reader-bound` plant, whose "newest" S1 defines; without it there is no kept set to order
- **consumes-from** `TOOL-dRankedPlan-25` — `check_plan_exit`'s disposition admission through the reader, where S2 prints the conflict
- **consumes-from** `TOOL-dRankedPlan-26` — `check_releasing_disposition` and S2's "the owner's latest word governs", the rule S1 makes defined; without it no word holds the gate
- **hands-off** `TOOL-dRankedPlan-4` — the reader's conflict answer, which that unit's `dispose` prints in its held line and writes nothing on
- **hands-off** `TOOL-dRankedPlan-37` — the reader's `why` list, through which that unit's item for finding 27 names an uncommitted record in the caller's hold line

## 4. Design

### Evidence

- `TOOL-dRankedPlan-24` §4 "The bound": "return the kept record whose `added` is newest", with no
  order named for a shared or an incomparable commit.
- `TOOL-dRankedPlan-26` S2: "The record it takes is the newest, so the owner's latest word governs".
  Its §4 rejects filtering words inside the reader, because the newest word must govern.
- The repository's ancestry test is `git merge-base --is-ancestor`, as used at
  `tools/drift-audit/drift_report.py:474` and `tools/branch-reconcile/branch_reconcile.py:478`.
- `TOOL-dRankedPlan-29` S30 makes a doubled `item.entry.place-owner` record loud rather than settled by
  a newest-wins read, the precedent the audit's fix names.

### The answer

| Kept records after the newest transition | Answer |
|---|---|
| none | `None`, no conflict |
| one | that record |
| several, one a descendant of all the others | that record |
| several unranked, one word | the path-sorted first of the unranked |
| several unranked, different words | `None`, `disposition conflict <paths>` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_newest_disposition` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest derive_newest_disposition --as py.function` answered OK |
| `one-commit`, `merged-sides` | `reader-bound` cases | none |
| `conflict-hold` | `ratify.py` fixture plant | none |

### Rollout

Live at landing. A build whose kept records are ordered, which is every build written from one
machine, reads the record it read before.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **A stated tiebreak, such as commit date or path order, for words that differ.** Commit dates come
  from two clocks, and a path says nothing about the owner's intent, so either picks a word the owner
  may not have meant last. A hold asks the owner once.
- **Raise on a conflict.** Every caller would need its own catch, and one that forgot it would crash a
  move. A `None` with a reason fails closed in every caller, including those that print no reason.

## 5. Production-readiness checklist

- security — narrows: concurrent dispositions no longer release Plan's exit by code order.
- perf / scale — one `merge-base --is-ancestor` per pair of kept records, two or three in practice.
- error / empty / loading states — a conflict holds and names every unranked path.
- observability — the hold line and the predicate's reason name the paths.
- risks — a conflict holds the build until the owner commits one more record on top of the merge, which
  is the one owner act the clause asks for.
- testing — the two `reader-bound` cases and `conflict-hold`, red and green.
- migration — none.
- user docs — N/A — `help/plan.md`'s fallback section already says the owner's disposition releases the
  gate, and a conflict is that release not yet given.

## 6. Acceptance criteria

- **AC1** — When the plant `reader-bound` runs its `one-commit` case with two different words,
  `read_item_disposition` returns `None` and its `why` names `disposition conflict` and both paths.
  With one word it returns the path-sorted first record.
  Red when: two records added in one commit with different words yield a record.
- **AC2** — When the `merged-sides` case runs, the reader returns `None` with the conflict reason
  before the third record, and returns the third record once it is committed on top of the merge.
  Red when: incomparable adds are ordered by code order, or a record above both is not taken.
- **AC3** — When `python ratify.py --fixture --plant conflict-hold` runs the `plan.exit` move through
  `python loop_transition.py record` before the third record, it exits 1 printing `disposition
  conflict`. After the third record carries a releasing word, it exits 0.
  Red when: a deferral and a `continue` written on two machines release Plan's exit.
- **AC4** — When the same plant runs under `terminal-command`, `ratify.py tFix` exits 1 printing
  `disposition conflict`.
  Red when: the predicate's arm ratifies on an unranked pair.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 AC4 · the `one-commit` and `merged-sides` cases and the `conflict-hold` plant, staged by a reader that returns the first kept record in iteration order · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 28 (HIGH,
  item H5), repairing `TOOL-dRankedPlan-26`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-24`'s `read_item_disposition`, which gains the order its "newest"
lacked, and the ancestry test the repository already uses (`tools/drift-audit/drift_report.py:474`).
`python tools/codebase-map/reuse_lookup.py "pick the newest of several records by commit ancestry and
refuse a tie"` ranked name stems only (`records`, `build_commit`, `CensusRefused`), so no existing seam
orders records by ancestry. The loud-on-doubled precedent is `TOOL-dRankedPlan-29` S30. The recall
query returned TOOL-dDeclaredLoop-16, the disposition record's own spec, which names no order, and this
audit's H5 item, and they agree.

Recall terms used: `python tools/memory-recall/query.py "which disposition governs when two were added in one commit or on two branches" --terms "newest disposition ancestry merge-base tie conflict hold incomparable commits owner latest word"`
