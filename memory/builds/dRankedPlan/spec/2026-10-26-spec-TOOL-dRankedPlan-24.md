# TOOL-dRankedPlan-24 — one reader of a build's disposition records for an item, bounded to the current crossing

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 4 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-24-deviation-241.md](../build/2026-10-26-build-TOOL-dRankedPlan-24-deviation-241.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 21 at HIGH**. It shares item **H4**, "a disposition from an earlier crossing releases a later
`plan.exit`", with findings 5 and 39, which `TOOL-dRankedPlan-25` and `TOOL-dRankedPlan-26` close.
Finding 21 is the reuse face: `TOOL-dRankedPlan-9` S4's `terminal-command` arm and
`TOOL-dRankedPlan-10` S4's gate each look up a disposition record naming `item.plan.exit` with no
freshness bound, while `TOOL-dRankedPlan-4` S3 applies "added after its newest transition" to the same
records by its own read. After `TOOL-dRankedPlan-15`'s B6 move back to `planning`, the first exit's
record still sits in `build/` and ratifies the second. This unit mints the one reader,
`read_item_disposition`, bounded to records added after the build's newest transition, and re-points
the `terminal-command` arm to it; unit 10's gate is `TOOL-dRankedPlan-25`'s and unit 4's lookup is
built on it. It repairs `TOOL-dRankedPlan-9`.

## 2. Scope (IN)

- **S1** — The reader. `read_item_disposition(repo, slug, item)` in `tools/loop/ratify.py` reads the
  build's disposition records (`record-kind.disposition`, `TOOL-dDeclaredLoop-16` S4) through the
  record factory's `read_record` (PLAY-dOrderedCharter-7 S7), keeps those whose `Item` is `item` and
  which `check_disposition_record` admits (`TOOL-dDeclaredLoop-16` S5), and of those keeps the ones
  added after the build's newest transition: the commit that added the record, `git log
  --diff-filter=A -1 --format=%H -- <path>`, has the newest transition's commit, read through
  `read_transitions(build, repo)` (`TOOL-dDeclaredLoop-3` S7), as a proper ancestor. It returns the
  newest kept record as `(path, fields, added_sha)`, or `None`. A build with no transition record
  bounds nothing, every admitted record counting. Observed by AC1 and AC2.
- **S2** — The `terminal-command` arm re-pointed. `read_plan_ratification`'s `terminal-command` arm
  (`TOOL-dRankedPlan-9` S4) takes its record from `read_item_disposition(repo, slug,
  "item.plan.exit")` and keeps its own `Channel` test, `terminal`. This supersedes unit 9 S4's
  unbounded "the build's `build/` folder holds a disposition record … whose `Item` is
  `item.plan.exit`". Observed by AC1.
- **S3** — The plants `terminal-reentry` and `reader-bound` join `ratify.py --fixture --plant <case>`
  (`TOOL-dRankedPlan-9` S7). `terminal-reentry`: a `terminal` record for `item.plan.exit`, the
  `plan.exit` move, B6 back to `planning`; `ratify.py tFix` then answers unratified, and once a second
  `terminal` record is committed, ratified. `reader-bound`: `read_item_disposition` over a record added
  in the same commit as the newest transition, one added before it and one after. Observed by AC1 and
  AC2.
- **S4** — The readers that take it. `TOOL-dRankedPlan-10` S4's disposition admission is re-pointed by
  `TOOL-dRankedPlan-25`. `TOOL-dRankedPlan-4` S3's `read_build_disposition` is built on S1, asking it
  once per item of its three moves and taking the newest answer, so its "added after its newest
  transition" rule is this reader's and spelled nowhere else. NOT OBSERVED by a criterion here: each
  reader's own criteria observe it.

## 3. Non-goals (OUT)

- Which Disposition word releases a gate: `TOOL-dRankedPlan-26`'s `check_releasing_disposition`.
- The disposition record, its fields and its value check: `TOOL-dDeclaredLoop-16`'s, read and never
  changed.
- The other values of `plan.ratification`: `request`, `hook-keyword` and `signed-commit` read no
  disposition record.

### Edges

- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`'s `terminal-command` arm and `ratify.py --fixture`, which S2 re-points and S3 plants into; without the module there is no home for the reader
- **hands-off** `TOOL-dRankedPlan-25` — `read_item_disposition`, through which that unit bounds `check_plan_exit`'s disposition admission to the current crossing
- **hands-off** `TOOL-dRankedPlan-4` — `read_item_disposition`, on which that unit's `read_build_disposition` is built so its freshness rule is not spelled twice
- **hands-off** `TOOL-dRankedPlan-34` — S1's add commit, which that unit replaces with the record's first appearance under any name (spec audit of units 19 to 29, id 26)
- **hands-off** `TOOL-dRankedPlan-35` — §4's "the kept record whose `added` is newest", which that unit orders by ancestry with a conflict hold (spec audit of units 19 to 29, id 28)
- **hands-off** `TOOL-dRankedPlan-37` — the `reader-bound` plant, `read_item_disposition` and §10's missing `Hold` seam, which that unit extends with merged adds and uncommitted records and answers with an ask (spec audit of units 19 to 29, ids 13, 14, 27)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-9` S4 (spec lines 54-58) and `TOOL-dRankedPlan-10` S4 (lines 51-56) each admit any
  record naming `item.plan.exit`; neither bounds it in time.
- `TOOL-dDeclaredLoop-16` S5's `check_disposition_record` checks only that the `Disposition` is in the
  item's outcome set, so it adds no freshness.
- `TOOL-dRankedPlan-4` S3: `apply_build_disposal` "reads the build's disposition records … added after
  its newest transition", the precedent this reader takes as its rule.
- `TOOL-dRankedPlan-15` §4 "The flow": B6 back to `planning`, then step 5's ratification, then step 6's
  second `plan.exit`.

### The bound

```
read_item_disposition(repo, slug, item)
  newest = read_transitions(slug, repo)[0].commit, or None
  for each disposition record of the build, admitted, Item == item:
      added = git log --diff-filter=A -1 --format=%H -- <path>
      keep when newest is None or (newest != added and newest is an ancestor of added)
  return the kept record whose `added` is newest, or None
```

A record committed together with the move it releases cannot exist: the record precedes the move it
lets through, so "strictly after" loses no legitimate case.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_item_disposition` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_item_disposition --as py.function` answered OK |
| `terminal-reentry`, `reader-bound` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. Its first readers are this unit's arm and, one order later, unit 10's gate.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **The bound in each reader.** Three readers would each spell "added after the newest transition",
  the drift the audit names; one reader holds it.
- **The reader in `tools/loop/loop_lib.py` beside `check_disposition_record`.** That module is
  dDeclaredLoop's, outside this build's write set; `ratify.py` is this build's loop-kit module and
  already holds the two Plan readers of the record.
- **Bound by file date.** A record's file-name date is the day it was written, coarser than a commit,
  and two crossings in one day would share it.

## 5. Production-readiness checklist

- security — narrows: a stale owner act no longer releases a later crossing. No new write path.
- perf / scale — one `git log` per disposition record of the build naming the item, a handful.
- error / empty / loading states — no record, or none fresh, answers `None`, and each caller says
  why in its own line.
- observability — the plants print which record the reader kept.
- risks — a disposition written before a backward move and meant for the next crossing must be
  written again; that is the owner act the clause asks for at each crossing.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no surface changes; unit 9's help section already says the record is the owner's
  act.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant terminal-reentry` runs, `ratify.py tFix`
  under `terminal-command` exits 1 after the B6 move with only the first record present, and exits 0
  printing `ratified — terminal-command` and the second record's path once it is committed.
  Red when: the first crossing's record ratifies the second.
- **AC2** — When the plant `reader-bound` runs, `read_item_disposition` returns the record added after
  the newest transition, and `None` when only the record added before it and the one added in its
  commit are present.
  Red when: a record not strictly after the newest transition is kept.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 · the `terminal-reentry` and `reader-bound` plants under `--fixture`, staged by a reader that keeps every admitted record · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 21 (HIGH, item H4,
  shared with findings 5 and 39), repairing `TOOL-dRankedPlan-9`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-34`, the hands-off edge to `TOOL-dRankedPlan-35`, the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The rule reused is `TOOL-dRankedPlan-4` S3's "added after its newest transition", lifted into one
reader over dDeclaredLoop's `read_transitions` and `check_disposition_record` and the factory's
`read_record`; no code exists at base 0689e7fa, where the loop kit and the factory are unbuilt.
`python tools/codebase-map/reuse_lookup.py "bound a disposition record lookup to records added after
the build's newest transition"` ranked name stems only (`build`, `records`, `build_commit`,
`build_fixture`), so no existing seam fits beyond the rule this unit lifts. The recall query returned
the audit's H4 item and `TOOL-dRankedPlan-4`'s S3, which agree.

Recall terms used: `python tools/memory-recall/query.py "which disposition record releases a re-entered plan.exit" --terms "disposition record item.plan.exit freshness newest transition B6 revision terminal-command fallback read_transitions"`
