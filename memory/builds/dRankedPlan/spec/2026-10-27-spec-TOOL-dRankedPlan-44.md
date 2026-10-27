# TOOL-dRankedPlan-44 — dormancy disposal orders its kept dispositions across items by ancestry, and holds on a conflict

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 12 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-44-deviation-441.md](../build/2026-10-27-build-TOOL-dRankedPlan-44-deviation-441.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 22 at HIGH**, item **H6**, against `TOOL-dRankedPlan-35`. Unit 35 S1 orders kept disposition
records by ancestry, but only within one item. `TOOL-dRankedPlan-24` S4 builds `TOOL-dRankedPlan-4`
S3's `read_build_disposition` by asking the reader once per item of its three moves and "taking the
newest answer", and no spec redefines that pick. So two merged dispositions for different moves, a
`pause` written on one machine and a `withdrawn` on another, reach a pick with no ancestry order and no
conflict hold, and `write_transition` records whichever move code order chooses. Unit 35 §3 says
dispose "reads the same answer through the reader it is built on", which is not yet true, and the
"newest" rule ends up spelled twice. This unit passes the union of the three moves' kept records to
unit 35's one order, with the conflict test over the `(Item, Disposition)` pair. The defect lands in
`read_build_disposition`, which unit 4 builds at order 11, so this unit repairs `TOOL-dRankedPlan-4`
and sits one order above it.

## 2. Scope (IN)

- **S1** — The kept set, factored. `read_kept_dispositions(repo, slug, items)` in
  `tools/loop/ratify.py` returns the records `TOOL-dRankedPlan-24` S1's bound keeps whose `Item` is any
  of `items`, as `(path, fields, added)`, dated as `TOOL-dRankedPlan-34` and `TOOL-dRankedPlan-43` date
  them. `read_item_disposition(repo, slug, item, why=None)` becomes
  `derive_newest_disposition(repo, read_kept_dispositions(repo, slug, (item,)), why)`, so its answers
  do not change. Observed by AC3.
- **S2** — The conflict key. `derive_newest_disposition` (`TOOL-dRankedPlan-35` S1) compares unranked
  records by the pair of their `Item` and their `Disposition`, the word resolved as unit 35 S1 resolves
  it. Records that share one item compare by the word alone, exactly as unit 35 states, so no
  single-item caller changes. Observed by AC1 and AC3.
- **S3** — The pick across items. `read_build_disposition(repo, slug, why=None)`
  (`tools/loop/loop_transition.py`, `TOOL-dRankedPlan-4` S3) calls `read_kept_dispositions` once with
  the items `DISPOSAL_MOVES` names, keeps the records whose `(Item, Disposition)` names one of its
  moves, as unit 4 S3 already filters, and returns `derive_newest_disposition` over them. This
  supersedes unit 24 S4's "asking it once per item of its three moves and taking the newest answer".
  Observed by AC1 and AC2.
- **S4** — The held line. When `read_build_disposition` answers `None` with a conflict, `dispose
  --build <slug>` prints `dispose — <slug> held: disposition conflict <path> <path>…`, exits 1 and
  writes nothing. This is the line `TOOL-dRankedPlan-4`'s edge to unit 35 promises. The "Dormant
  builds" section of `help/plan.md` (`TOOL-dRankedPlan-4` S6) gains one sentence naming the hold and
  its release, one more record committed on top of both. Observed by AC1 and AC4.
- **S5** — The plant. `dispose-conflict` joins `loop_transition.py --fixture` beside unit 4's
  `dispose-*` plants. Two branches fork after the build's newest transition. One commits an
  `item.life.request` `pause` record and the other an `item.life.close` `withdrawn` record, and both are
  merged. `dispose` holds. A third record, `item.life.request` `pause`, is then committed on top of the
  merge, and `dispose` applies B19. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The order itself, and which records are fresh: `TOOL-dRankedPlan-35`, `TOOL-dRankedPlan-24`,
  `TOOL-dRankedPlan-34` and `TOOL-dRankedPlan-43`, read here.
- The three moves and their table: `TOOL-dRankedPlan-4` §4 "The three moves", unchanged.
- `check_plan_exit` and the `terminal-command` arm. Each asks one item, `item.plan.exit`, and S2 keeps
  their answers.

### Edges

- **consumes-from** `TOOL-dRankedPlan-35` — `derive_newest_disposition` and its `why` convention, whose conflict key S2 widens to the item; without it there is no order to pass the union to
- **consumes-from** `TOOL-dRankedPlan-4` — `read_build_disposition`, `DISPOSAL_MOVES`, `dispose` and its `dispose-*` plants, whose per-item pick S3 supersedes with one ordered pick; without them there is no disposal to order

## 4. Design

### Evidence

- `TOOL-dRankedPlan-24` S4: `read_build_disposition` asks the reader "once per item of its three moves
  and taking the newest answer".
- `TOOL-dRankedPlan-35` S1 orders "the records `TOOL-dRankedPlan-24`'s bound keeps", one item's set,
  and §3 says dispose "reads the same answer through the reader it is built on".
- `TOOL-dRankedPlan-4` §4 "The three moves": `item.life.request` `pause` (B19), `item.life.close`
  `withdrawn` (T11) and `item.life.close` `superseded` (T12). Two items carry three moves.
- `git grep -n read_build_disposition -- memory/builds/dRankedPlan/spec/` names only units 4 and 24,
  run 2026-10-27, so no other spec picks across that reader's answers.

### The answer after this unit

| Kept records naming a move | `read_build_disposition` |
|---|---|
| none | `None`, `dispose` held with no owner disposition (unit 4 S4) |
| one | that record's move |
| several, one a descendant of all the others | that record's move |
| several unranked, one `(Item, Disposition)` pair | the path-sorted first, so that move |
| several unranked, two pairs | `None`, `disposition conflict <paths>` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_kept_dispositions` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_kept_dispositions --as py.function` answered OK |
| `dispose-conflict` | `loop_transition.py` fixture plant | none |

### Rollout

Live at landing, at order 12, one step after unit 4 builds `dispose`. A build disposed from one machine
reads the move it read before.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `tools/loop/loop_transition.py`: S3 to S5
- `help/plan.md`: S4's sentence

### Alternatives rejected

- **Order each item's answer by its `added` commit after the per-item pick.** Two per-item winners from
  two machines are incomparable for the same reason two records are, so the pick stays code order.
- **Let one item outrank the other.** A fixed precedence of `item.life.close` over `item.life.request`
  would pick a move the owner may not have meant last; the hold asks the owner once.

## 5. Production-readiness checklist

- security — narrows: concurrent dispositions for different moves no longer move a build by code
  order.
- perf / scale — one kept-set read per `dispose` instead of two, and one ancestry test per pair.
- error / empty / loading states — S4's held line names every unranked path.
- observability — the held line and the plant's output.
- risks — a conflict holds the build until the owner commits one record on top of the merge, the act
  unit 35 already asks for.
- testing — `dispose-conflict`, red and green, and AC3's single-item probe.
- migration — none.
- user docs — S4's sentence in `help/plan.md`'s "Dormant builds" section.

## 6. Acceptance criteria

- **AC1** — When `python loop_transition.py --fixture --plant dispose-conflict` runs `dispose --build
  tFix` after the merge, it exits 1 printing `disposition conflict` with both record paths, and writes
  no transition.
  Red when: a `pause` and a `withdrawn` written on two machines move the build by code order.
- **AC2** — When the same plant commits its third record and runs `dispose` again, one transition
  record `To: paused` is written and `dispose` exits 0.
  Red when: a record above both sides is not taken.
- **AC3** — When the `one-commit` case of `reader-bound` (`TOOL-dRankedPlan-35` S3) runs at this unit's
  tip, `read_item_disposition` answers as unit 35 AC1 states.
  Red when: the factored kept set or the widened key changes a single-item answer.
- **AC4** — When `grep -c "disposition conflict"` runs over the help page `plan.md` at this unit's
  tip, it prints at least 1, inside the "Dormant builds" section.
  Red when: a user meets the held line with no page explaining it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/loop_transition.py · covers AC1 AC2 · the `dispose-conflict` plant, staged by a `read_build_disposition` that asks each item and takes the later answer · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 22 (HIGH,
  item H6, found against `TOOL-dRankedPlan-35`), repairing `TOOL-dRankedPlan-4`, whose
  `read_build_disposition` carries the defect.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-35`'s `derive_newest_disposition`, which gains the item in its
key, and `TOOL-dRankedPlan-24`'s bound, factored out of `read_item_disposition` so the dormancy reader
takes the same kept set instead of a second freshness rule. `python tools/codebase-map/reuse_lookup.py
"pick the newest of several records by commit ancestry and refuse a tie"` was run by unit 35 and ranked
name stems only, so no seam beyond those two fits. The recall query returned unit 35, unit 4 and this
audit's H6 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "which disposition governs across the three dormancy moves" --terms "read_build_disposition dormancy dispose newest disposition conflict item move ancestry union kept records"`
