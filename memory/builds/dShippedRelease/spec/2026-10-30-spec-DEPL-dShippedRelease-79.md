# DEPL-dShippedRelease-79 — `review` starts `unfired`, so `pending` means fired and still open

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B1 with id 28
(DEPL-dShippedRelease-80). Unit 1 S2 writes `review: pending` at `--deploy record`, which runs before
`--deploy review`, so the first read of every landing takes unit 60 S1's `pending` arm, prints the pin
and exits 3 with no `--trigger`. The field holds one word for never fired and for fired, so unit 60's
rule that only this verb's own write proves a fired trigger cannot be built. This unit gives the
never-fired state its own word. The walk that reads it is unit 80.

## 2. Scope (IN)

- **S1** — The initial value. `--deploy record` writes `review: unfired`, and `core` and `distill`
  keep `pending`. Observed by AC1.
- **S2** — The one writer of `pending`. `run_deploy_review` writes `pending` only after `--trigger`
  exits 0, as unit 14 S1 orders it, and a trigger that exits non-zero leaves `unfired` and stops the
  walk with that exit. Observed by AC2.
- **S3** — The close term. `check_landing_review` fails `unfired`, printing
  `close — <slug> · held · check_landing_review · unfired`. `check_review_field` (unit 73) reads it
  outside its pass and forgery arms, so a landing nobody walked never prints `forged`. Observed by
  AC3.

## 3. Non-goals (OUT)

- The walk's order of arms and the row check: DEPL-dShippedRelease-80, the other half of item B1.
- `core` and `distill`: each keeps `pending`, since no reader of those two asks whether a trigger
  fired.
- What `pending` prints past a dead review: review id 97, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `--deploy record`'s field write, whose initial `review` value this unit moves
- **consumes-from** `DEPL-dShippedRelease-14` — `run_deploy_review`, `check_landing_review` and the value table this unit extends
- **consumes-from** `DEPL-dShippedRelease-60` — the first step, which reads the word this unit makes unambiguous
- **consumes-from** `DEPL-dShippedRelease-73` — `check_review_field`, which reads `unfired` outside its arms
- **hands-off** `DEPL-dShippedRelease-80` — `unfired`, the value the walk's arm order branches on
- **hands-off** `DEPL-dShippedRelease-106` — the value table, which the minors batch reads for review id 20

## 4. Design

### Evidence

- Unit 1 S2 writes `core`, `distill` and `review` as `pending`, and its §4 line reads `review: pending | <DEPL-dShippedRelease-14's line>`.
- Unit 14's Migration says `--deploy review` is the first thing to move the field, and unit 4 §4 "The one commit" puts `record` ahead of `[landing review]`.
- Unit 60 S1 prints the pin and exits 3 on `pending` with no `--trigger`; the field holds no provenance (report ids 1, 28).

### Supersedes

- Unit 1 S2's "`review` as `pending`" and its §4 `review:` line: `review` reads `unfired`, then the unit 14 values.
- Unit 14 §4 "The field": a row joins the table, `unfired` | fails | `close — <slug> · held · check_landing_review · unfired`.
- Unit 14's Migration sentence "A record written before this unit reads `pending`": no such record exists, and a record reads `unfired` from its first write.
- Unit 73 S3's "any other reading" for this one value.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `unfired` | a value of the record's `review` field | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6
- `help/deploy.md`: the initial value, one sentence

### Alternatives rejected

- **`pending · fired <sha8>`, a suffix.** Every reader of the literal `pending` then parses a tail, and the tail repeats the SHA the record already holds. Refuted by a grep: units 1, 14 and 60 each spell the bare word.
- **`-`, as `patch-key` and `carries` start.** In those fields `-` means no value, and here it would read as `unreadable field` in unit 14's table.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a record written by a build older than this unit does not exist, since unit 1 and this unit land in one build.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/deploy.md` gains one sentence on `unfired`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-initial` runs `--deploy record` on a landing
  with no planted field, `python deploy_items.py read-landing <sha>` prints `review<TAB>unfired` and
  `distill<TAB>pending`.
  Red when: the record writes `pending`, so the first walk takes the fired arm.
- **AC2** — When `--case review-trigger-fails` stubs `--trigger` to exit 1 under
  `review.deploy = "owed"`, `--deploy review` exits 1 and `read-landing` still prints
  `review<TAB>unfired`.
  Red when: `pending` is written ahead of the trigger, so a review that never fired holds for ever.
- **AC3** — When `--case review-close-unfired` runs `--deploy close` on a record reading `unfired`, it
  exits 3 printing `held · check_landing_review · unfired`, and neither stream holds `forged`.
  Red when: a landing nobody walked reads as passed, or as tampered.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · the `review-` cases, their failing case `review: pending` written at the record · none

## 8. Open questions

- **F1 — What tells never fired from fired and open?** Options: (a) a distinct initial value,
  `unfired`; (b) a suffix on `pending`; (c) `-`. (b) moves every reader of the literal and (c) means
  no value elsewhere on the record. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, one word per
  state and no parser. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (BLOCKER, item B1) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is `run_deploy_review` and its value table (unit 14 S1, S2), with unit 1 S2's writer.
`python tools/codebase-map/reuse_lookup.py "separate a field that was never fired from one fired and still open"`
ranked name-stem helpers (`field`, `opened`, `ask_field`, `check_paths_never_lost`) and no state reader,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent units. The
recall probe surfaced TOOL-dPlacedRequest-5's breakpoint disposition and report item B1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what value does the landing record hold for a review that never fired" --terms "landing review field pending trigger not-placed unfired disposed run_deploy_review breakpoint walk record"`
