# TOOL-aPairedSlots-14 — the two-bar check's overlap guard reads the slots the bars were admitted to

**Status:** CLOSED · rev-1 · 2026-10-12 · node a · Tier-1 · base d3354597 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aPairedSlots-14-1-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aPairedSlots-14-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-15 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H4 (id 30, with M7, id 14): the two-bar check judges that its concurrent pair
overlapped from timestamps taken around the whole runner, queue wait included. The two bars start
together, so those windows overlap even when the turnstile ran them one after the other, and the
check would print PASS for a two-writer claim no two writers exercised.

## 2. Scope (IN)

- **S1 — the overlap is read from the run records.** The concurrent pair overlapped when the newest
  run record of each worktree carries a `slot` key, the two keys are 1 and 2, and each record's
  `acquired` time precedes the other's `ended` time. A queued second bar is not refused: the head-only
  claim makes a genuinely concurrent second bar wait one tick. Observed by AC1.

## 3. Non-goals (OUT)

- A real staged-red pair at one slot. It costs two more full bars, about three hours on node a; the
  guard's failing case is observed on fixture records instead, and the skip is stated here.

## 4. Design

A second bar that waited for the first to finish re-claims the lowest free slot, 1, and a bar at one
slot writes no `slot` key at all, so distinct slots 1 and 2 cannot arise from a serialized pair. The
`acquired` against `ended` comparison adds the time order. Both are read by key from files the runner
writes for every bar.

### Files touched (estimate)

- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh`

## 5. Acceptance criteria

- **AC1** — When `grade` runs over fixture run records whose concurrent pair holds slots 1 and 2 with
  each admitted before the other ended, it reports the overlap; with slots 1 and 1, or with one record
  admitted after the other ended, it names the pair as not overlapping and the check fails.
  Red when: either serialized fixture passes.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing review's round 1.
