# TOOL-aPairedSlots-6 — the unattended driver's gate backstop stays correct with two holders

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base b6cd02bc · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-8 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 |

<!-- /gen:spec-records -->

## 1. Goal

The unattended driver bounds its close's bar by the runner's wall plus its queue bound plus a
margin, read from `--print-profile`. That sum stays a correct bound when the turnstile admits two
holders and the profile prints a `slots` key, and an arm pins it so a later stricter parse cannot
break it silently.

## 2. Scope (IN)

- **S1 — the argument, recorded.** A bar's elapsed time is its queue wait plus its own run. The
  wait is bounded by `TS_MAXWAIT` whatever the slot count, because a waiter fails open at that
  bound; the run is bounded by the wall, which the runner arms after the acquire at every width.
  So `wall + queue + margin` bounds a bar at any slot count, and a doc-only bar, which never
  waits, is bounded with room to spare. The argument is written beside `parse_gate_profile` in
  `tools/unattended/lib-unattended.sh`. Observed by AC1.
- **S2 — the arm.** The backstop arms in `tools/unattended/unattended.test.sh` gain one whose
  fixture profile prints `slots` 2 beside `wall`, `queue` and `ceiling_max`, and which asserts the
  pinned backstop is the same sum as without it. Observed by AC1.

## 3. Non-goals (OUT)

- Any change to the backstop's arithmetic, `GATE_BOUND`, the margin or the wall.
- Reading `slots` into the driver: nothing it decides depends on the count.

## 4. Design

`parse_gate_profile` reads the keys it knows and ignores the rest, which is the runner's stated
contract for `--print-profile` ("adding a key is safe; a reader takes the keys it knows"). The arm
is what turns that contract into a check on this reader: a parse that began refusing unknown keys
would red it on the day `slots` reached the profile.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.test.sh`

## 5. Acceptance criteria

- **AC1** — When the driver's preflight runs over a fixture whose profile command prints `slots`
  2 with wall 5 and queue 20, it pins `gate-backstop: <25 + margin> (wall 5 + queue 20 + margin <m>)`,
  the line the arm without `slots` pins.
  Red when: `parse_gate_profile` refuses or misreads an unknown key, and the backstop is not pinned.

## 6. Gates

`unattended kit gate`

New arm: tools/unattended/unattended.test.sh · covers AC1 · a parse that refuses unknown keys · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft.
