# TOOL-dPlacedRequest-37 — the node lock's deadline is the block's own bound, never the driver's `REMOTE_BOUND`

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-37-deviation-371.md](../build/2026-10-25-build-TOOL-dPlacedRequest-37-deviation-371.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-37-deviation-372.md](../build/2026-10-25-build-TOOL-dPlacedRequest-37-deviation-372.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 13 at HIGH**. It shares item **H1**, "the node-lock factory is not self-contained
in the `gov_feed_sh` block", with findings 2, 24 and 32, which `TOOL-dPlacedRequest-36`,
`TOOL-dPlacedRequest-38` and `TOOL-dPlacedRequest-39` close. `TOOL-dPlacedRequest-24` S1 builds
`write_node_lock` from `write_claim_push_lock`, whose deadline is `$(( $EPOCHSECONDS + REMOTE_BOUND +
10 ))` (`tools/unattended/unattended.sh:2347` at the pinned base). `REMOTE_BOUND` is the driver's
(`:162`); `tools/run-gates/post-merge.sh` and `tools/push-main.sh` define none and run under `set -u`
(`:26`, `:64`), so the first lock take in either aborts with `REMOTE_BOUND: unbound variable`.
`TOOL-dPlacedRequest-24`'s Files touched also leaves `tools/push-main.sh` out. This unit repairs
`TOOL-dPlacedRequest-24` at order 5: the deadline is a constant the block itself carries, so every
carrier, the lander's included, takes the lock with nothing from its host.

## 2. Scope (IN)

- **S1** — The block's own bound. `gov_feed_sh` assigns `NODE_LOCK_BOUND=10` at its top, and
  `write_node_lock` writes `until` as `$(( EPOCHSECONDS + NODE_LOCK_BOUND ))`; no line of the block
  reads `REMOTE_BOUND`. Ten seconds covers a holder's whole critical section, since no node lock is
  held across a network call (`TOOL-dPlacedRequest-24` §3), and it is twice the 5 s retry a waiter
  spends. Observed by AC1 and AC2.
- **S2** — The lander's copy. `tools/push-main.sh` carries no `gov_feed_sh` block at order 5; it gains
  one at `TOOL-dPlacedRequest-15` S5 (order 9), cut-equal to the canonical, so it takes the lock with
  this bound and no driver name. That unit's §4 names `tools/push-main.sh` among its files, and
  `TOOL-dPlacedRequest-13`'s `gov_feed_sh` parity row finds the copy by `git grep` once it exists.
  NOT OBSERVED here: the copy is built after this unit, and `TOOL-dPlacedRequest-38`'s carrier arm
  reads it at the close.

## 3. Non-goals (OUT)

- No change to the health event path: finding 2's, `TOOL-dPlacedRequest-36`.
- No standing arm over every carrier: finding 24's, `TOOL-dPlacedRequest-38`.
- No change to the staleness rule: `check_node_lock_stale` reads `until` as
  `check_claim_push_lock_stale` does (`:2325-2330`).
- No environment override of the bound: a lock deadline is no operator knob.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-24` — `write_node_lock` and its `until` deadline, which this unit takes off the driver's bound; without the factory there is no deadline to move
- **hands-off** `TOOL-dPlacedRequest-15` — `tools/push-main.sh`'s inline `gov_feed_sh` copy, which carries `NODE_LOCK_BOUND` and so takes the lock under `set -u` with no driver name
- **hands-off** `TOOL-dPlacedRequest-49` — S1, AC1 and §4, which that unit's items for findings 15, 27, 30 and 37 fix, sequence and bound against every section the lock covers
- **hands-off** `TOOL-dPlacedRequest-52` — `NODE_LOCK_BOUND`, which that unit's items for findings 12 and 31 name as the placed race's margin and its discard bound

## 4. Design

### Evidence

- `write_claim_push_lock` writes `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` into `until`
  (`unattended.sh:2347`); `REMOTE_BOUND="60"` (`:162`) is the bound of one remote call, which the
  claim-push lock was held across.
- `grep -n 'REMOTE_BOUND'` over `post-merge.sh` and `push-main.sh` prints nothing at the base; both
  set `set -u`. `push-main.sh` already reads `EPOCHSECONDS` (`:306`), so bash 5 holds there.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: `NODE_LOCK_BOUND` and the deadline
- `tools/unattended/unattended.sh`: the inline block, carried
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the deadline arm

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `NODE_LOCK_BOUND` | block constant in `gov_feed_sh` | none |

### Alternatives rejected

- **`${NODE_LOCK_BOUND:-70}`, the review's example.** An environment default is a second channel that
  leaves no diff, and 70 s is the claim-push lock's push window, which no node lock covers; a crash
  inside the feed's append would cost every append on the node 70 s of `feed: NOTE` lines.
- **A deadline argument on every call.** Both callers would pass the same figure.

## 5. Production-readiness checklist

- security — none.
- perf / scale — none: one arithmetic expansion.
- error / empty / loading states — a crashed holder's lock is breakable 10 s after its take, not 70.
- observability — `until` holds the bare epoch as before.
- risks — a holder stalled more than 10 s inside its microsecond section can be broken while live;
  the guarded break then admits one breaker, as `TOOL-dPlacedRequest-24` §5 states.
- testing — the probes of §6 and the arm in §7.
- migration — none: the factory is new in this build.
- user docs — none: no guide states the lock's deadline.

## 6. Acceptance criteria

The probe cuts the `gov_feed_sh` block with `awk` from `# >>> gov_feed_sh` to `# <<< gov_feed_sh` and
runs in a scratch git repository with common dir `$c`.

- **AC1** — When `env -i PATH="$PATH" bash -c 'set -u; <gov_feed_sh cut of post-merge.sh>;
  write_node_lock "$c/gov-feed.lock" t1; echo rc=$?'` runs with no `REMOTE_BOUND` set, it prints
  `rc=0` and `$c/gov-feed.lock/until` reads a value within 1 of `EPOCHSECONDS` plus 10.
  Red when: the deadline reads a driver name, the staged case being the verbatim claim-push body,
  which prints `REMOTE_BOUND: unbound variable`.
- **AC2** — When `awk` cuts `gov_feed_sh` from `gov-feed.sh` and `grep -c 'REMOTE_BOUND'` runs over
  the cut, it prints 0, and `grep -c '^NODE_LOCK_BOUND=10$'` over it prints 1.
  Red when: a later edit routes the deadline back through the driver's bound.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the deadline written by a take with no driver name set, staged against the verbatim claim-push body · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What bounds a node lock's deadline?** (a) A block constant of 10 s; (b) the review's
  `${NODE_LOCK_BOUND:-70}`; (c) an argument per call. (b) keeps a push window no node lock spans and
  opens an environment channel; (c) passes one figure twice. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound with its example value replaced by the
  bound the holder's section needs. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  13 (HIGH, item H1, shared with findings 2, 24 and 32).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-24`'s factory, itself the claim-push lock at the pinned base
(`tools/unattended/unattended.sh:2325-2360`); only its deadline expression changes. `python
tools/codebase-map/reuse_lookup.py "lock deadline bound for a node-local mkdir lock"` returned name-stem
hits only (`read_bound_key`, `boundedParallel`), none a lock deadline; `read_bound_key` reads a conf
key, which a lock's deadline is not. `python tools/memory-recall/query.py "what bounds the node lock
deadline"` returned TOOL-aGraftedHelix-37, whose spec sets the claim-push lock's `until` rule, and
scout A's row; neither disagrees with source.

Recall terms used: node lock deadline until REMOTE_BOUND claim-push.lock mkdir stale break gov-feed.lock bound
