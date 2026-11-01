# DEPL-dShippedRelease-142 — `record-clean` compares the return's `key` with this landing, so a stale clean return is refused

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 16 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md) | research | DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 40 of `reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md`, HIGH, item H4. Unit 135 says
`tools/workflows/tier2-review.js` carries no key binding a return to a landing and marks `key` ignored. The harness
builds that key from the kind, the round and both ends of the range, and every return carries it. So the previous
landing's clean return, or one re-used after a re-fire, writes `## Verdict: CLEAN` under this landing's range line,
which on this path is the verb's own, and no later term can catch it. It needs no adversary, only a wrong file
argument. This unit reads the key, and repairs unit 135, order 15, at the next step.

## 2. Scope (IN)

- **S1** — The row. `write_clean_record` admits a return only when `key` opens
  `diff-review-r<round>-<base12>-<sha12>-`, `<round>` the return's `round`, `<base12>` the first 12 hex of `read_pin_range`'s
  `base`, and `<sha12>` the first 12 hex of the verb's `<sha>`. It is read last, after unit 135 S1's keys, so a return of
  another kind still prints `shape`. Observed by AC1, AC2.
- **S2** — The refusal. A `key` differing, absent, or holding an `unresolved-` subject refuses, exit 2, writing nothing,
  printing `record-clean — <sha8> · not a clean return · key`, unit 135 S2's line. Observed by AC1, AC2.
- **S3** — A refused pin. On a pin refusing with a class there is no base, so the verb refuses, exit 2, printing
  `record-clean — <sha8> · pin refused · <class>`, writing nothing. Unit 114 S3 already sends that landing to
  `dispose-with-reason`, and unit 138 S35 prints the same refusal on `dispose-landing`. Observed by AC3.
- **S4** — The plants. Each clean return `tools/loop/deploy_fixture.py` builds for units 113, 114 and 135 carries the
  `key` that landing's pin derives, so those criteria stand. Observed by AC4.

## 3. Non-goals (OUT)

- `inputPrint`, the key's last field: it hashes the run's inputs, so nothing here can derive it, and S1 compares the
  prefix.
- A spec's statement of what a return lacks citing the line it read: the audit's left-shift item.
- A fixture planting another range against every verb that admits a return: the audit's left-shift item.
- The harness: `tools/workflows/tier2-review.js` keeps its key.

### Edges

- **consumes-from** `DEPL-dShippedRelease-135` — S3, §3's third bullet, §4's row and §5, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-113` — S1's verb and S4's refusals
- **consumes-from** `DEPL-dShippedRelease-114` — §4's table and the `review-harness-return` case, whose plants gain the key
- **consumes-from** `DEPL-dShippedRelease-109` — `read_pin_range`, S1's base

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:59-62` is `deriveSubjectPair`: two full SHAs give `<base12>-<head12>`, and anything else `unresolved-<hash>`.
- `:990-992` is `deriveReviewKey`, `` `${kind}-r${round}-…-${inputPrint}` ``, `:1074` derives it, and both clean returns (`:1338`, `:1670`) and the success return (`:2021`) carry `key`.
- `:191` defaults `kind` to `diff-review`, and unit 14 S3's pin passes that kind with a full `base` and `head`.
- Unit 109 S3: `read_pin_range` reads `base` from that pin's JSON line, so the prefix is computable with no new door.
- Unit 135:41 says the harness "carries no such key", and 135:71 marks `key` ignored. Both are false of the lines above.

### What the admission reads

Unit 135 §4's table, with its last row changed and this row added.

| Key | Read | Why |
|---|---|---|
| `key` | opens `diff-review-r<round>-<base12>-<sha12>-` | a clean return for any other range is no review of this landing |
| `root`, `identity`, the rest | ignored | nothing in the record depends on them |

### Supersedes

- Unit 135 §3's third bullet, "Binding a return to the landing": this unit binds it.
- Unit 135 S3's second sentence, "A stale `diff-review` return still passes, and §5 states it". The first sentence stands, and a stale return now fails S1.
- Unit 135 §4's row `root`, `key`, `identity`, the rest, and §5's "no key binds a return to a landing": §4 and §5 here.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: S4 and the cases of §6

### Alternatives rejected

- **Comparing the whole key.** `inputPrint` hashes the lens set, the specs and the round's context, which the verb cannot derive and which change no binding.
- **A new `landing` field on the harness return.** A second key for the fact the first one states, in a file this build does not own.

## 5. Production-readiness checklist

- security — the verb stops certifying another landing's review. What stays unseen: the key is not signed, so a session able to write a return can write its key, the exposure units 83 to 90 §5 state; and a clean return for this same range at an earlier round still passes, since it reviewed these bytes.
- perf / scale — N/A — one string compare per disposal.
- error / empty / loading states — S2 names the three key states and S3 the refused pin. A dead pin read stays unit 138 S34's and S17's line.
- observability — the refusal names `key`, and the pin's line names the class.
- risks — a harness that respells the key reds this verb at the first real run, the loud direction, and `dispose-with-reason` is the way out.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — DEPL-dShippedRelease-113 writes `help/deploy.md`'s line.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py record-clean <sha> <return.json>` runs on a clean return whose `key` names another
  landing's range, it exits 2 printing `key`, and `git status --porcelain` lists no new record.
  Red when: a stale clean return writes `## Verdict: CLEAN` for an unreviewed landing.
- **AC2** — When it runs on a clean return with `key` absent, and on one holding an `unresolved-` subject, each exits 2
  printing `key`.
  Red when: a return with no bound range passes on the verb's own range line.
- **AC3** — When `python deploy_fixture.py --case record-clean-pin-refused` runs the verb on a landing whose pin refuses
  `linear-history`, it exits 2 printing `pin refused · linear-history`, and no record is written.
  Red when: a refused pin raises, or a return passes with no base to compare.
- **AC4** — When `python deploy_fixture.py --case review-harness-return` and unit 135 AC3's two clean returns run, each
  `key` is derived from that landing's pin, and each writes `## Verdict: CLEAN`.
  Red when: the admission refuses a real clean return, or a plant carries a typed key.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 · `record-clean-stale-key`, its failing case the `key` row cut from the admission · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 40 (HIGH, item H4) of the round-5 spec audit.

## 10. Reuse audit

The seam extended is `write_clean_record` (units 113 and 135), read against `deriveReviewKey` at `tools/workflows/tier2-review.js:990`.
`python tools/codebase-map/reuse_lookup.py "bind a harness return to the commit range it reviewed by its key"`
ranked the name-stem helper `key` and missed `deriveReviewKey`, the seam the report's citation found, so the probe and
the source disagree and the source stands. The recall probe surfaced units 135 and 113, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what binds a harness clean return to the landing it reviewed" --terms "reviewKey key deriveSubjectPair record-clean return base head round stale clean landing"`
