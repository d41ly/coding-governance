# TOOL-dWellOiledMachine-83 — the supervisor start claim taken and broken through the tree's guarded mkdir lock, lifted into the kit library

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 30 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-83-deviation-831.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-83-deviation-831.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 30, item H4, at HIGH. TOOL-dWellOiledMachine-78 S4 breaks a stale start claim by renaming it
to `<slug>.starting.stale.<own pid>` and re-checks nothing after the rename. When ticks A and B both
judge one claim stale, B renames, deletes and makes a fresh claim, then A's rename moves B's FRESH
claim, and both ticks hold a claim: the double start the unit exists to prevent. The tree already has
a non-waiting `mkdir` lock that breaks only under a `.break` guard and re-checks staleness under it,
`write_claim_push_lock` (`tools/unattended/unattended.sh:2331-2353`). This unit lifts that lock into the
kit library as the one factory of its kind, takes the start claim through it, and deletes 78 S4's
rename break.

## 2. Scope (IN)

- **S1** — The factory lifted. `tools/unattended/lib-unattended.sh` gains
  `check_node_lock_stale <dir>`, `write_node_lock <dir> <owner> <until-epoch> <event-stem> [stale-fn]`
  and `remove_node_lock <dir> <owner>`, the bodies of `check_claim_push_lock_stale`,
  `write_claim_push_lock` and `remove_claim_push_lock` (`tools/unattended/unattended.sh:2325-2359`) with
  three parameters added: the deadline written to `until`, the stem of the two health events
  (`<stem>-lock-broken`, `<stem>-guard-cleared`), and the stale test the guard re-runs, defaulting to
  `check_node_lock_stale`. Return codes and the guard's one-minute self-heal are unchanged.
  Observed by AC3.
  **Readers:** by name: `tools/unattended/unattended.sh`, the claim writer's three call sites, re-pointed to the
  factory, and READER NOT IN TREE for `write_node_lock` and `remove_node_lock`, which this item adds. by value: NO VALUE READERS — the lock's files are read
  only by the factory itself and the lander's wait, which reads `until` as before.
- **S2** — The three driver functions deleted. `check_claim_push_lock_stale`, `write_claim_push_lock`
  and `remove_claim_push_lock` leave `tools/unattended/unattended.sh`, which sources the library and
  calls S1's functions. Observed by AC3.
  **Readers:** by name: `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh`, as
  in S1. by value: NO VALUE READERS — the deleted bodies move whole.
- **S3** — The start claim through the factory. The tick takes `<slug>.starting` with
  `write_node_lock <claim> <tick token> <now + 2 * SUPERVISOR_BEAT_SECONDS> supervisor-start check_supervisor_claim_stale`,
  where `check_supervisor_claim_stale` is 78 S4's dead-claim test (a builder finding 78's test inline
  names it so) and the tick token is the tick pid and stamp 78 S3 records. A busy return prints
  `supervisor — <slug> · starting elsewhere` and starts nothing; the winner releases with
  `remove_node_lock <claim> <tick token>`, so a release never removes a claim a breaker made.
  Observed by AC1, AC2.
  **Readers:** by name: `tools/unattended/resume-tick.sh`, the tick that takes the claim. by value: NO VALUE READERS — the claim directory is read only by the ticks that race for it.
- **S4** — The rename break deleted. 78 S4's `rename to <slug>.starting.stale.<own pid>` and its
  single retry are removed: the factory's guarded break is the only path that removes a stale claim.
  Observed by AC2.
  **Readers:** by name: `tools/unattended/resume-tick.sh` (or the runtime kit's copy once
  TOOL-dWellOiledMachine-28 moves it, READER NOT IN TREE), the one tick that spells the stale name. by value: NO VALUE READERS — the stale name was deleted by the tick that made it.

## 3. Non-goals (OUT)

- No change to which claims are stale: 78 S4's test stands, and its incomplete-claim arm is
  TOOL-dWellOiledMachine-80's.
- No change to the claim's parent directory or to a non-`EEXIST` failure: TOOL-dWellOiledMachine-89's.
- No change to the claim-push lock's behaviour: its deadline, its events and its release move whole.
- TOOL-dPlacedRequest-24 (DEFERRED) names the same three functions for its offline-queue block in
  `gov_feed_sh`; that unit is outside this build, and §8 F1 records the choice.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-78` — the start claim of S3 and the stale test and rename break of S4, which this unit puts behind the guarded lock
- **consumes-from** external — TOOL-aGraftedHelix-37's `write_claim_push_lock`, `check_claim_push_lock_stale` and `remove_claim_push_lock` in `tools/unattended/unattended.sh`, the landed lock this unit lifts
- **hands-off** `TOOL-dWellOiledMachine-92` — S1's lifted factory and §8 F1's claim on TOOL-dPlacedRequest-24, which that unit hands to the other build by an ask row (finding 22)
- **hands-off** `TOOL-dWellOiledMachine-94` — S3's claim layout, S1's stale tests, the claim-push lock's criterion, the call-site count and the symbol render (findings 4, 19, 21, 29, 30, 44)

## 4. Design

### Evidence

- `write_claim_push_lock` breaks a lock only under the `<lock>.break` guard, re-runs
  `check_claim_push_lock_stale` under it, and its header says "no breaker removes a lock another
  breaker made" (`tools/unattended/unattended.sh:2305-2353`); `remove_claim_push_lock` releases only
  while `owner` reads the caller's token (`:2355-2359`).
- The suite extracts the three functions by name from the driver and races two writers over a stale
  lock (`tools/unattended/unattended.test.sh:16163-16281`).
- The tick sources the kit library (`tools/unattended/resume-tick.sh:117`) and does not source the
  driver, so the factory must live in the library for the tick to reach it.
- `grep -n "write_node_lock" tools` prints nothing at this base: the names are free in this tree.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_node_lock` | shell function, `lib-unattended.sh` | `write`, OK |
| `remove_node_lock` | shell function, `lib-unattended.sh` | `remove`, OK |
| `check_node_lock_stale` | shell function, `lib-unattended.sh` | `check`, OK |
| `supervisor-start-lock-broken`, `supervisor-start-guard-cleared` | health events | none |
| `stale-claim-race` | `supervise.py --fixture` plant | none |

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`: S1
- `tools/unattended/unattended.sh`: S2 and the three call sites
- `tools/unattended/unattended.test.sh`: the extraction re-pointed to the library
- `tools/unattended/resume-tick.sh` (or `tools/runtime/resume-tick.sh` once TOOL-dWellOiledMachine-28
  moves it): S3, S4
- `tools/runtime/supervise.py`: the race plant

### Alternatives rejected

- **A second guarded lock typed into the tick.** The claim-push lock is the first instance of this
  kind; a copy at the second instance is the drift the charter's reuse rule exists to stop.
- **A re-check after 78's rename.** A rename that succeeded already moved whatever directory sat at
  the name, so a re-check after it cannot undo a move of a fresh claim.

## 5. Production-readiness checklist

- security — exactly one act session per item, which the claim protects; the release is token-keyed.
- perf / scale — one `mkdir` per start, two more on a break.
- error / empty / loading states — a busy factory prints why nothing started.
- observability — a break appends `supervisor-start-lock-broken` to the health log, as the push lock
  does.
- risks — the factory's stated residual, an abandoned guard removed by two writers while a third
  takes it, moves with it unchanged (`tools/unattended/unattended.sh:2318-2324`).
- testing — AC1 to AC3 and the arm in §7.
- migration — none: the claim-push lock keeps its directory, files and event names.
- user docs — none: no verb, key or message a user types changes.

## 6. Acceptance criteria

- **AC1** — When `python supervise.py --fixture --plant double-tick` starts two ticks together twenty
  times with no claim present, every run ends with exactly one supervisor and one `started` line.
  Red when: both ticks take the claim.
- **AC2** — When `--plant stale-claim-race` plants one dead tick's stale claim and starts two reaping
  ticks and one fresh claimer together, twenty times, every run ends with exactly one supervisor, and
  `grep -n "starting.stale" resume-tick.sh` prints nothing.
  Red when: a breaker removes the fresh claim another breaker made and two supervisors start.
- **AC3** — When `grep -n "claim_push_lock" tools/unattended/unattended.sh tools/unattended/lib-unattended.sh`
  runs, it prints nothing, and `type write_node_lock` in a shell that sourced the driver library `lib-unattended.sh`
  prints the function.
  Red when: a second copy of the lock stays in the driver.

## 7. Gates

`unattended kit gate` · `routed-commits selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites are waived for this build's landing (README rule 8); the
claim-push lock's race arm in `unattended.test.sh` moves with the functions it extracts.

New arm: tools/runtime/supervise.py · covers AC1 AC2 · the race plant staged against 78 S4's rename break with no guard · none

## 8. Open questions

- **F1 — Where does the lifted lock live, under which names?** (a) `lib-unattended.sh` under
  TOOL-dPlacedRequest-24's names `write_node_lock`, `remove_node_lock`, `check_node_lock_stale`;
  (b) wait for TOOL-dPlacedRequest-24, DEFERRED in another build; (c) the library under new names.
  (b) leaves this build's double start open on a unit no run here builds; (c) mints a second spelling
  for the factory that unit already named, so the later of the two would rename. (a) closes the race
  now and spells the factory once, so TOOL-dPlacedRequest-24 re-points to this library rather than
  minting. Rung 3, the most capable surviving option, reusing the seam M5 found. RESOLVED (agent,
  2026-10-27, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  30 (H4).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-92, TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is TOOL-aGraftedHelix-37's guarded claim-push lock
(`tools/unattended/unattended.sh:2305-2359`), lifted rather than copied, as the charter's reuse rule
asks at a kind's second instance. The probe `python tools/codebase-map/reuse_lookup.py "break a stale
mkdir lock under a guard and re-check"` ranked `check`, `checks` and `check_line` by name stem, none a
lock; `python tools/codebase-map/reuse_lookup.py "create the parent directory before an atomic
claim"` ranked `check_claim_push_lock_stale` and `write_claim`, the lock this unit lifts. The recall
query below ranked TOOL-aGraftedHelix-37's spec first.

Recall terms used: `python tools/memory-recall/query.py "how is a stale mkdir lock broken safely"
--terms "claim-push lock break guard re-check stale until owner token mkdir turnstile nonce"`
