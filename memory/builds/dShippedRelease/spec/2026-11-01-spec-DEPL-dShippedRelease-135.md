# DEPL-dShippedRelease-135 — `record-clean` admits only a return that says it reviewed this landing clean

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 56 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H7, which stands beside
id 16 in the minors batch. Unit 113 S1 admits on `report` null, `exit` `complete` and `pending` empty. The
harness's success return carries those with a numeric `confirmed` and `report: synth?.path || null`, and its
schema's `path` is a bare string, so an empty path reads as clean with confirmed findings. A spec-audit return
passes too, because nothing reads its shape. `record-clean` then writes `## Verdict: CLEAN` and certifies the
landing on a return that is no clean review of it. This unit admits on what a clean return actually says.

## 2. Scope (IN)

- **S1** — The admission. `write_clean_record` admits a return only when, beside unit 113 S1's three keys,
  `confirmed` is `[]` or 0, `unverified` and `uncertain` are absent or 0, `note` is `clean: 0 findings` or
  `all findings adjudicated and refuted`, and `shape` reads `kind=diff-review`. Observed by AC1, AC2, AC3.
- **S2** — The refusal. Any other value refuses, exit 2, writing nothing, printing
  `record-clean — <sha8> · not a clean return · <key>`, the first key that failed. Unit 114 S1's
  `deferred-platform` reading runs first and stands. Observed by AC1, AC2.
- **S3** — The limit, stated. On this path the range line is the verb's own, written from `read_pin_range`, so the
  `landing` term proves nothing here and unit 110 S4's sentence reads for a report the review agent wrote. A stale
  `diff-review` return still passes, and §5 states it. NOT OBSERVED: the statement of a limit.

## 3. Non-goals (OUT)

- `blockers` and unit 114's new table row: review id 16, in the minors batch.
- A re-run, and a failure between the write and the disposal: review id 70, in the minors batch.
- Binding a return to the landing: §5 states the gap, and `tools/workflows/tier2-review.js` carries no such key.

### Edges

- **consumes-from** `DEPL-dShippedRelease-113` — S1 and S4, whose admission this unit restates
- **consumes-from** `DEPL-dShippedRelease-114` — S1's `deferred-platform` reading, which runs first
- **consumes-from** `DEPL-dShippedRelease-110` — S4's sentence, which this unit corrects
- **hands-off** `DEPL-dShippedRelease-138` — S1's key table, which id 16 extends

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1338` and `:1670` are the two clean returns. `confirmed` is `[]` on both, and the second carries `unverified: 0` and `uncertain: 0`.
- `:2020` ff. is the success return: `confirmed: confirmed.length`, `report: synth?.path || null`.
- `:79` renders `review-shape kind=…`, and `:1000` passes the run's `kind`, so `shape` names it on every return.
- The note on a clean path is `clean: 0 findings` at `:1327` and `all findings adjudicated and refuted` at `:1675`, and each deferred note opens `DEFERRED:`.

### What the admission reads

| Key | Read | Why |
|---|---|---|
| `report` | null | a path is `dispose-landing`'s row |
| `exit` | `complete` | `deferred-platform` is unit 114 S1's |
| `pending` | empty | a dead lens is no result |
| `confirmed` | `[]` or 0 | a number above 0 is the success return with an empty `path` |
| `unverified`, `uncertain` | absent or 0 | the two clean returns differ, and a count above 0 is unadjudicated |
| `note` | one of the two clean literals | a third value is a path this unit has not priced |
| `shape` | holds `kind=diff-review` | a spec-audit return names another kind |
| `round`, `appendix` | written | unit 113 S2's bytes |
| `root`, `key`, `identity`, the rest | ignored | nothing in the record depends on them |

### Supersedes

- Unit 113 S1's "takes a return reading `report` null, `exit` `complete` and `pending` empty", and S4's list.
- Unit 110 S4's "the `landing` term reads bytes the review agent wrote", which reads for a report the agent wrote.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **Testing `report` for a non-empty string.** It closes the empty path alone, and a spec-audit return stays admitted.

## 5. Production-readiness checklist

- security — the verb stops certifying a return with confirmed findings or of another kind. A session supplying a stale `diff-review` return still passes: no key binds a return to a landing, and on this path the range line is the verb's own, so the `landing` term proves nothing.
- perf / scale — N/A — a read of a local JSON file.
- error / empty / loading states — §4's table states each key, and S2 names the refusal.
- observability — the refusal names the key that failed.
- risks — a harness note respelled reds this verb at the first real run, the loud direction.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — DEPL-dShippedRelease-113 writes `help/deploy.md`'s line.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py record-clean <sha> <return.json>` runs on a return shaped as the success path
  with `confirmed` 2 and `report` null, it exits 2 printing `confirmed`, and `git status --porcelain` lists no new
  record.
  Red when: an empty path writes `## Verdict: CLEAN` over confirmed findings.
- **AC2** — When it runs on a clean return whose `shape` reads `kind=spec-audit`, and on one whose `note` reads
  `partial`, each exits 2 naming the key.
  Red when: a return of another kind certifies a landing.
- **AC3** — When it runs on each of the two clean returns, shaped as `tools/workflows/tier2-review.js:1338` and `:1670`
  shape them, each writes `## Verdict: CLEAN` and `read-landing` prints `disposed · 0 finding(s)`.
  Red when: the admission refuses a real clean return.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · a success-shaped return with `confirmed` 2, its failing case the three keys of unit 113 S1 alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 56 (HIGH, item H7) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is `write_clean_record` (unit 113 S1), read against the returns at `tools/workflows/tier2-review.js:1338` and `:2020`.
`python tools/codebase-map/reuse_lookup.py "admission test over a harness return keys"`
ranked the name-stem helpers `key`, `keys` and `read_conf_key` and no reader of a return, so no existing seam
fits outside that function. The recall probe surfaced TOOL-aProbedUnit-12, TOOL-dTieredTribunal-5 and unit 114,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what keys does a clean harness return carry" --terms "clean return confirmed unverified uncertain note shape kind report null exit complete pending admission"`
