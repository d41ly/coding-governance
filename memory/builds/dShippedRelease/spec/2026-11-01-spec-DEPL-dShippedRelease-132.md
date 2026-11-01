# DEPL-dShippedRelease-132 — two spellings of one range read as one pair, and what stays ambiguous is priced

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H4, which stands beside
id 60 in the minors batch. Unit 109 §5 says the harness's opening holds one range, but S1's read over tracked
diff-review records gave 7 ambiguous. Three of those state one range twice, at 8 hex in a quoted
`gotchas.py --for-diff` command and at 40 hex on the range line, and S1's "distinct" does not fold spellings.
Such a report is refused at exit 2 and the landing holds until an owner answers. This unit folds spellings
and prices the refusal that remains.

## 2. Scope (IN)

- **S1** — The fold. In `read_report_range`, two pairs are one when each end of one is a case-insensitive
  prefix of the same end of the other, and the longer pair is kept. Unit 109 S4's prefix compare then reads one
  pair however the report spells it. Observed by AC1, AC2.
- **S2** — What remains. Pairs still distinct after S1 read `ambiguous`, unit 110 S2 refuses them at exit 2, and
  `dispose-with-reason` is the way out. The read picks no first pair and no labelled line, because unit 109 S2
  takes the token and never the label. Observed by AC3.
- **S3** — The record. Unit 109 §5's risks line reads: a report stating two ranges is refused, 4 of the 244
  tracked records read so, and §4 here holds the tally. NOT OBSERVED: the correction of a record.

## 3. Non-goals (OUT)

- The `<8hex>...<8hex>` plant of unit 109 AC1: review id 60, in the minors batch.
- Reading the pair on the line holding the word `range`: §8 F1.
- A corpus probe of every report reader: the audit's left-shift item, and §4's tally is its one instance.

### Edges

- **consumes-from** `DEPL-dShippedRelease-109` — S1's read and §5's risks line, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-110` — S2's refusal of `ambiguous`, which prices what remains
- **hands-off** `DEPL-dShippedRelease-138` — the fold, whose AC1 plant id 60 adds

## 4. Design

### Evidence

- `tools/workflows/review_replay.py:75` is `RANGE`, 7 to 40 hex at each end, so an 8-hex and a 40-hex spelling are two tokens.
- `memory/builds/aBatchedArm/reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round2.md` holds the `--for-diff` form beside the 40-hex range line.

### The tally

S1's block, run read-only over `git ls-files 'memory/**/reviews/*.md'`, on records opening `**Serves:** diff-review`
and holding a verdict heading. PINNED at `e8ced8ac`.

| Opening holds | Records |
|---|---|
| one pair | 142 |
| two spellings of one pair, folded by S1 | 3 |
| no pair | 95 |
| two distinct pairs | 4 |

The four are aGraftedHelix-29, aProvenReuse round 3, dLoggedFlight round 2 and dPolishedVitrine round 2.

### Supersedes

- Unit 109 S1's "two distinct pairs read `ambiguous`": "distinct" is S1's.
- Unit 109 §5's risks line, and "the harness's opening holds one".

### Files touched (estimate)

- `tools/workflows/review_replay.py`: S1, S2

### Alternatives rejected

- **The pair on the line holding the word `range`.** It reads the label, which unit 109 S2 refuses, and the harness's agent spells that line freely.

## 5. Production-readiness checklist

- security — N/A — a read over a blob the door already reads.
- perf / scale — N/A — one fold over a handful of tokens.
- error / empty / loading states — S2 names the state that stays refused, and the tally prices it.
- observability — the door prints the kept pair, or `ambiguous`.
- risks — an honest report quoting a second range in its opening is refused, 4 of 244 at `e8ced8ac`, and it costs an owner's answer; a first-pair read would bind a report to a range nobody chose.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/review_replay.py --facts <plant>` reads an opening holding a
  `gotchas.py --for-diff <a8>..<b8>` provenance line and the 40-hex range line of the same commits, it prints that
  one 40-hex pair.
  Red when: two spellings of one range read `ambiguous`, and an honest report is refused.
- **AC2** — When `--facts` reads `memory/builds/dAlignedCarrier/reviews/2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md`
  by hand at the pass, it prints one `range` pair and not `ambiguous`.
  Red when: the fold misses a real report's spelling.
  fixture: a tracked gov record, so this is read once and no arm reads it.
- **AC3** — When `--facts` reads a plant whose opening holds two genuinely different pairs, it prints `ambiguous`.
  Red when: the fold merges two ranges that share no end.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/workflows/review_replay.py · covers AC1 AC3 · the two inline plants, their failing case the pairs compared whole · `ARMS_DECLARED` rises by one

## 8. Open questions

- **F1 — What answers a pair that stays distinct?** Report item H4 names two arms. Options: (a) a refusal priced by
  its measured rate; (b) the pair on the line holding the word `range`. (b) stands against unit 109 S2, which
  takes the token and never the label, and the skeptic prefers (a). RESOLVED (agent, 2026-11-01, delegated):
  (a), rung 3, the report's preferred fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 22 (HIGH, item H4) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is `read_report_range` (unit 109 S1), over `RANGE` at `tools/workflows/review_replay.py:75`.
`python tools/codebase-map/reuse_lookup.py "fold two spellings of one commit range"`
ranked the name-stem helpers `build_commit` and `pass_commit` and no range reader, so no existing seam fits
outside that function. The recall probe surfaced unit 109 and this round's report, which agree with
this reading.

Recall terms used:
`python tools/memory-recall/query.py "how are two spellings of one sha compared" --terms "prefix compare short sha 40-hex range fold distinct pair ambiguous opening report for-diff"`
