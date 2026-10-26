# TOOL-dFurnishedOrders-34 — the posture read's failures named and bounded: a `breakpoints.py list` that fails, hangs or prints no `attendance —` line, and a policy read that fails, each an unreadable posture with its cause

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 8c395e3c · streams tooling · order 22 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed finding **id 30 at HIGH**, report item **H3**. Id 3 shares that item and takes
`TOOL-dFurnishedOrders-33`.

Id 30 is the failure envelope of the item. `TOOL-dFurnishedOrders-16` S1 reads the posture as
`read_policy_setting("attendance", root)` and the members on the `attendance —` line of `python
tools/loop/breakpoints.py list`. `TOOL-dFurnishedOrders-28` S2 names only turn-side causes, and its S3
bounds only the `turns` subprocess. A posture read that exits non-zero, prints no `attendance —` line,
hangs, or whose policy read fails has no stated outcome and no bound, so it can hold a run's question
or hang its dispatch on a path no criterion observes.

This unit names each posture cause as an unreadable posture, which `TOOL-dFurnishedOrders-33`'s row
answers inside a window, and bounds the posture subprocess as unit 28 bounds `turns`. It repairs
`TOOL-dFurnishedOrders-28` and builds one step after it (order 22), after unit 33 by the dispatch's
id sort.

## 2. Scope (IN)

- **S1** — The causes. The posture half of `derive_attended` (`tools/roles/roles_lib.py`) is
  unreadable, each with one `<why>` naming the cause, when: `breakpoints.py list` exits non-zero
  (`<why>` names its exit and first stderr line); it exits 0 and prints no line opening
  `attendance —`; or `read_policy_setting("attendance", root)` raises. The absent loop kit is unit
  33's cause. Observed by AC1.
- **S2** — The bound. The `breakpoints.py list` subprocess runs with stdin closed and output captured
  under a 10-second bound, the bound `TOOL-dFurnishedOrders-28` S3 gives `turns`; expiry is an
  unreadable posture whose `<why>` names the bound. Observed by AC2.
- **S3** — One answer per cause. Inside a window each cause answers as unit 33's row decides; outside
  a window, unit 16's `unread` row. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The posture-unreadable row and the absent loop kit: `TOOL-dFurnishedOrders-33`.
- The turn half's causes and bound: `TOOL-dFurnishedOrders-28`.
- One bounded runner for every roles subprocess: the minors batch `TOOL-dFurnishedOrders-37`, for ids
  20 and 37, re-points this read through it.
- `breakpoints.py` itself: KICK-dKeptSession-17's, absent from this tree at `8c395e3c`.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-28` — the 10-second bound of S3 and the turn-side cause list, which S1 and S2 extend to the posture half (id 30)
- **consumes-from** `TOOL-dFurnishedOrders-33` — the posture-unreadable row inside a window, which each cause of S1 and S2 answers through (ids 3 and 30)
- **hands-off** `TOOL-dFurnishedOrders-37` — the bounded posture read, which unit 37 S12 re-points through `run_slot_reader` (id 20)

## 4. Design

### The posture read, after this unit

```
posture half
  resolve_kit_dir("loop", "breakpoints.py")   LookupError        -> unread: no loop kit (unit 33)
  read_policy_setting("attendance", root)      raises             -> unread: policy read failed: <exc>
  python breakpoints.py list, 10 s, stdin closed
                                               expired            -> unread: breakpoints.py list timed out after 10s
                                               exit != 0          -> unread: breakpoints.py list exited <rc>: <stderr line>
                                               no "attendance —"  -> unread: breakpoints.py list printed no attendance line
                                               members            -> readable
```

### Inventory

Minted: the four `<why>` texts of §4. No function, flag or key.

### Migration

None: no answer is stored.

### Rollout

Live at landing. `KIT_ROLES_VERSION` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **Leave the posture read unbounded.** A hung read hangs the dispatch that asked the door.
- **A posture bound of its own size.** Two reads of one answer would carry two bounds; unit 28 F2 sized
  the turn read's, and the posture read is the smaller of the two.

## 5. Production-readiness checklist

- security — no new write path; the subprocess reads stdin from nothing.
- perf / scale — the bound caps the posture read at 10 seconds per owner question.
- error / empty / loading states — each cause is named in the source.
- observability — the door's line names the cause.
- risks — a loop kit slow on a cold cache reads unread once; the source names the bound.
- testing — AC1 and AC2 by probes over stub `breakpoints.py` files; the arm of §7 at the close.
- migration — none.
- user docs — none beyond unit 33's paragraph, which names an unreadable posture.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.derive_attended(root, since=T1)` in a fixture whose
  `breakpoints.py` is a stub that exits 2, then one that exits 0 printing no `attendance —` line, then
  with `read_policy_setting` made to raise, over a transcript whose only owner turn is before T1, each
  returns `False` and a source opening `away: unread since` T1 that names its cause; without `since`
  each returns `True` and a source opening `unread:`.
  Red when: a failed posture read inside a run reads attended, or one cause is answered two ways.
  fixture: a scratch kit copy with stub loop files and a transcripts root under `%TEMP%`.
- **AC2** — When the stub `breakpoints.py` sleeps past the bound, the call with `since` returns within
  about 12 seconds, `False`, and a source naming `timed out`.
  Red when: a hung posture read hangs the owner question.

## 7. Gates

`roles catalogue` · `roles adopter self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · stub posture readers that exit non-zero, print no attendance line, sleep past the bound, and a raising policy read, staged by reading the posture with no bound and no exit check · none

## 8. Open questions

- **F1 — How long may the posture read take?** Options: (a) 10 seconds, unit 28's bound for `turns`;
  (b) unbounded, as unit 16 states none; (c) 30 seconds, `CHECKER_BOUND_S`
  (`tools/roles/handoff.py:102`). (b) can hang a dispatch; (c) lets one owner question take 40 seconds
  with the turn read beside it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, one bound for
  the two halves of one answer, PINNED 2026-10-26 by this choice. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-16`, `-28` and `-33`, and
  KICK-dKeptSession-17's `breakpoints.py`, are specced and unbuilt at `8c395e3c`. RESOLVED (agent,
  2026-10-26, delegated): the build run re-grounds on each at the pass and stops this unit if a named
  section of units 16, 28 or 33 is still absent then; the absent loop kit is unit 33's cause, and the
  stubs of AC1 stand in for it, rung 1, the brief's rule for unbuilt parents. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the spec audit of the round-1 promotions, id 30
  (HIGH, item H3, shared with id 3).

## 10. Reuse audit

The seams extended: the posture half of `derive_attended` (`TOOL-dFurnishedOrders-16` S1) and unit 28
S3's bounded subprocess, whose run shape is `handoff.py`'s checker run (`tools/roles/handoff.py:268-276`:
stdin from `DEVNULL`, captured output, a timeout). `python tools/codebase-map/reuse_lookup.py "read the
attendance posture and fail when the loop kit is absent"` ranked `read`, `read_text`, `fail` and
`absent`, none a posture reader, so no existing seam fits beyond the ones named. The recall probe
returned unit 28 and the audit's H3 text, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "what does an unreadable attendance posture
answer inside an unattended run" --terms "attendance posture breakpoints loop kit unread away window
since derive_attended hold stall"`
