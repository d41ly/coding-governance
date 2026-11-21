# TOOL-dPlacedRequest-24 — the offline queue under one guarded node lock, appended once and flushed honestly

**Status:** CLOSED · rev-8 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-24-deviation-241.md](../build/2026-10-25-build-TOOL-dPlacedRequest-24-deviation-241.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-24-deviation-242.md](../build/2026-10-25-build-TOOL-dPlacedRequest-24-deviation-242.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-24-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-24-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dPlacedRequest-24-red-fix-9.md](../build/2026-11-19-build-TOOL-dPlacedRequest-24-red-fix-9.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-24-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-24-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-24-divergence-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-24-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 56 at HIGH**, its item **H9**. `TOOL-dPlacedRequest-1` §4 "The offline queue"
has every successful read in every session on the node read, push and rewrite
`<git-common-dir>/gov-queue.log` line by line, with no lock and no idempotence key. Two concurrent
flushes push one commit; the loser's update fails as `[remote rejected]`, so its line is kept (rc 2)
and its next flush reads `[up to date]` and resolves it as `flushed` (§4 Evidence, PINNED
2026-11-19). But each rewrites the file from its own read and can drop a line appended between,
losing a queued acquisition; and re-running an offline acquire queues a second line for one ref and
tip, which yields spuriously. This unit repairs `TOOL-dPlacedRequest-1`: the queue is read and
rewritten only under a node lock, and a line is appended once per ref and cached tip.

The lock is the second node-local lock this build mints, after `TOOL-dPlacedRequest-13`'s
`gov-feed.lock`, so it is built as one factory both take, carrying the guarded stale break the
deleted claim-push lock had (charter rule `[reuse]`).

## 2. Scope (IN)

- **S1** — The lock factory is the shared `write_dir_lock`, `check_dir_lock_stale`,
  `remove_dir_lock` and `write_dir_lock_pid` (`tools/unattended/unattended.sh#write_dir_lock`), which
  TOOL-aPiecewiseGrade-6 made generic from the claim-push lock: a `.break` guard serialising a stale
  break, a release only by the owner token, a hold in seconds and a health-event stem per call, and
  that unit's S9 pid staleness rule. This unit mints one lock function, S2's retrying take. It moves the four definitions,
  with `read_proc_token`, `check_proc_gone` and `PT_TOKEN` that they call, verbatim into the
  `gov_feed_sh` block (`tools/lib/gov-feed.sh`, inline byte-identical in every copy), so the driver's
  inline copy of the block is their one definition in `unattended.sh` and `post-merge.sh` carries the
  same bytes. The one edit is `read_proc_token`'s read of `${PROCFS_ROOT:-/proc}`, so a carrier with
  no driver reads `/proc`. Every node lock passes the stem `node`, so its events read
  `node-lock-broken` and `node-guard-cleared`; the event's log path in a carrier with no `ROOT` is
  `TOOL-dPlacedRequest-36`'s, and the hold it passes is `NODE_LOCK_BOUND`, which S2 mints.
  **Readers:** rebuilt against the tree `TOOL-dPlacedRequest-11` leaves at order 1. by name:
  `write_dir_lock`, `check_dir_lock_stale`, `remove_dir_lock`, `write_dir_lock_pid`,
  `read_proc_token` and `check_proc_gone`, spelled by `tools/unattended/unattended.sh` (the
  definitions, `init_spec_token_check`'s take and release, the process-ledger readers, and the two node
  locks of S2) and `tools/unattended/unattended.test.sh` (the GH37 blocks, which drive the factory under
  a test stem); each keeps its name and signature, so the move changes no reader. `write_claim`'s take
  is gone with unit 11 S6. by value: `tools/unattended/README.md`'s health-event sentence, which spells
  the `spec-tokens-*` pair after unit 11 S7 and gains the `node-lock-broken` and `node-guard-cleared`
  pair here. Observed by AC5, AC6 and AC7.
- **S2** — Both node locks are taken through it. `gov_feed_sh` assigns `NODE_LOCK_BOUND=10` at its
  top, minted here, and `TOOL-dPlacedRequest-37` guards it against a driver name. `add_feed_event`'s
  `gov-feed.lock` (`TOOL-dPlacedRequest-13` §4 step 1) and the queue's new `gov-queue.lock`, each in
  the common dir, are each taken through `write_dir_lock_wait <lock dir> <token> "$NODE_LOCK_BOUND"
  node <ceiling>`, minted here in `gov_feed_sh` beside `write_dir_lock`: it calls `write_dir_lock`
  every 50 ms until it takes or the ceiling passes, returning 0 taken or 1 busy, the one retry loop on
  a lock in the tree. Both callers pass a 5 s ceiling, and `TOOL-dPlacedRequest-49` S25's
  `requests.lock` calls it too; the feed keeps its rule that a lock it cannot take is a
  `feed: NOTE -` line and rc 0. Observed by AC3 and AC6.
- **S3** — Appended once. `add_gov_queue <ref> <cached tip> <commit>` takes `gov-queue.lock`; a line
  whose `ref` and cached tip equal the new one already queues the write, so it appends nothing and the
  caller prints `queued — already · <tail>`. A lock it cannot take in 5 s prints `lease not written —
  gov-queue.lock busy` and exits 2, with nothing queued. Observed by AC1 and AC3.
- **S4** — Flushed under the lock, pushed outside it. `write_gov_queue` takes the lock, reads the
  lines and releases it; pushes each line through `write_gov_ref`, oldest first, with no lock held;
  then takes the lock again, re-reads the file, and rewrites it without exactly the lines it resolved,
  so a line appended during the pushes is kept. A lock it cannot take skips this flush with one
  `queue: NOTE -` line, and the next successful read flushes. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `leases.offline`'s values or to which callers it governs: `TOOL-dPlacedRequest-1` S10
  and `TOOL-dPlacedRequest-23`.
- No placeholder for an empty cached tip: the queue line's `-` for a create is finding 57's, an item of
  `TOOL-dPlacedRequest-34`.
- No proof that two breakers racing a stale `gov-feed.lock` cannot share a `seq`: that criterion is
  finding 36's, an item of `TOOL-dPlacedRequest-34`, observed over this factory.
- No lock across the network: a push is never made while a node lock is held, so a slow remote holds
  no other session.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — `add_gov_queue`, `write_gov_queue` and `gov-queue.log`, which this unit puts under the lock and makes idempotent; without them there is no queue to guard
- **consumes-from** `TOOL-dPlacedRequest-13` — the `gov_feed_sh` block and `add_feed_event`'s `gov-feed.lock`, which the factory joins and replaces; without the block the factory has no shared home
- **hands-off** `TOOL-dPlacedRequest-34` — `write_dir_lock` and the queue line, which that unit's items for findings 36 and 57 observe and extend
- **hands-off** `TOOL-dPlacedRequest-36` — `write_dir_lock`'s two health events, which that unit writes through the lock's common dir and `health_log_sh`
- **hands-off** `TOOL-dPlacedRequest-37` — `NODE_LOCK_BOUND`, minted by S2, and the `until` deadline it sets, which that unit's arm guards so no take reads `REMOTE_BOUND`
- **hands-off** `TOOL-dPlacedRequest-38` — the `gov_feed_sh` lock functions, which that unit's parity-leg arm runs per inline copy under `set -u`
- **hands-off** `TOOL-dPlacedRequest-39` — `remove_dir_lock`, which that unit's contained append calls from its `EXIT` trap
- **hands-off** `TOOL-dPlacedRequest-41` — `add_gov_queue`'s dedupe and `write_gov_queue`'s order, which that unit narrows to a record compare and chains per ref
- **hands-off** `TOOL-dPlacedRequest-43` — the flush's confirming read, `gov-feed.lock`'s spelling in `gov-feed.sh` and the lock factory, which that unit's items for findings 34, 12 and 39 amend and reuse
- **hands-off** `TOOL-dPlacedRequest-49` — `write_dir_lock`'s write order, which that unit's item for finding 14 makes `owner` before `until`, and `write_dir_lock_wait`, which its S25 calls

## 4. Design

### Evidence

- The shared factory: `write_dir_lock <lock dir> <owner token> <seconds it may hold> <stem>` takes
  the directory, and on a stale lock takes a `.break` guard, re-checks staleness under it, removes and
  retakes the lock, and records `<stem>-lock-broken`, or `<stem>-guard-cleared` for a guard older than
  a minute; `check_dir_lock_stale` reads `until`, else the age, else every recorded process gone;
  `remove_dir_lock` checks the owner token (`tools/unattended/unattended.sh#write_dir_lock`,
  `#check_dir_lock_stale`, `#remove_dir_lock`, blob `875eaadf`). At that blob its callers are
  `write_claim` (stem `claim-push`) and `init_spec_token_check` (stem `spec-tokens`); after
  `TOOL-dPlacedRequest-11` S6 at order 1, `init_spec_token_check` alone, and this unit adds the two
  node locks.
- `TOOL-dPlacedRequest-11` S6 deletes `write_claim`'s take of `claim-push.lock` and the lander's wait,
  and keeps the factory; `TOOL-dPlacedRequest-13` §4 step 1 re-specifies an unguarded break for the
  feed, which S2 replaces with the factory.
- The fact the flush rests on, PINNED 2026-11-19 by a probe of git 2.54.0 against a scratch bare
  origin (builder run `wf_495a7364-a80`): `git push --porcelain --force-with-lease=<ref>: origin
  <c>:<ref>` with the remote ref already at `<c>` exits 0 and prints `=` and `[up to date]`, because
  git tests up to date before the lease, and prints `[rejected] (stale info)` only when the remote
  tip is a different commit; `write_gov_ref` (`tools/lib/gov-ref.sh#write_gov_ref`) reads a line not
  opening with `!` as rc 0, `(stale info)` as rc 1 and any other refusal, `[remote rejected]`
  included, as rc 2. So a loser of two concurrent flushes keeps its line and its next flush prints
  `flushed`, and no path prints a false `yield`.

### The queue under the lock

```
add_gov_queue ref tip commit
  write_dir_lock gov-queue.lock tok NODE_LOCK_BOUND node   (50 ms retries, 5 s)   busy -> exit 2
  line with ref and tip present?      yes -> release, "queued — already"
  append ref TAB tip TAB commit TAB queued-utc
  remove_dir_lock gov-queue.lock tok

write_gov_queue
  lock; snapshot = every line; unlock
  for each line, oldest first:  write_gov_ref ref tip commit   (no lock held)
    rc 0 -> resolved
    rc 1 -> resolved (yield, health event)
    rc 2 -> kept
  lock; rewrite = file now, less the resolved lines; unlock
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `gov-queue.lock` | node-local directory | none |
| `node-lock-broken`, `node-guard-cleared` | health events, the factory's stem `node` | none |
| `NODE_LOCK_BOUND` | block constant in `gov_feed_sh` | none |
| `write_dir_lock_wait` | shell function in `gov_feed_sh` | `write`, OK |
| `queued — already` | output line | none |

Moved, not minted: the `write_dir_lock` family, `read_proc_token` and `check_proc_gone`, into
`gov_feed_sh` under their own names.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: the factory moved in, `NODE_LOCK_BOUND`, and the feed's lock taken
  through it
- `tools/unattended/unattended.sh`: the factory's definitions moved into the inline block,
  `add_gov_queue` and `write_gov_queue`
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the queue arms
- `tools/unattended/STOPS.template.md`: section 7's offline queue sentence names the lock and the
  dedupe
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/unattended/README.md`: the health-event sentence gains the `node-*` pair
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **A lock held across the flush's pushes.** Every queued push is bounded by `REMOTE_BOUND`, so a
  flush of n lines would hold every other session for n bounds; the resolved-lines rewrite needs no
  such hold.
- **A second lock implementation for the queue.** The feed already has one; two node locks are the
  kind's second instance, which the charter's `[reuse]` rule makes a factory.
- **Lock functions minted from the old claim-push bodies.** The tree already holds that factory as
  `write_dir_lock`; a renamed copy beside it would miss the pid staleness rule and diverge (finding 15
  of the round-1 audit of 2026-11-19).
- **Deduping by the commit.** A re-run offline acquire builds a new commit with new stamps on the same
  tip, so the commit never repeats; the ref and cached tip do.

## 5. Production-readiness checklist

- security — no new surface: both files stay in the common dir and are never pushed.
- perf / scale — two lock takes per flush and one per append, each a `mkdir`.
- error / empty / loading states — a busy lock refuses an append with exit 2 and skips a flush with a
  NOTE; an empty queue flushes nothing.
- observability — `queued — already`, the NOTE lines and the two renamed health events.
- risks — the factory keeps its stated blind spots (the comment above
  `tools/unattended/unattended.sh#check_dir_lock_stale`): four writers in one window around a stalled
  breaker, and a wall-clock step. And `tools/run-gates/post-merge.sh` runs under `set -u` with no
  `ROOT` and no `add_health_event`, so the moved factory's stale-break path, which calls
  `add_health_event "$(resolve_health_log "$ROOT")"` (`tools/unattended/unattended.sh#write_dir_lock`),
  reaches those unset names there until `TOOL-dPlacedRequest-36` lands; S1 already defers that
  carrier's event log path to that unit.
- testing — the probes of §6 and the arm in §7.
- migration — none: the queue and the lock are new in this build.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; `help/loop.md` anchors the driver's verbs beside its `--claims` paragraph, and this unit adds no verb.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-1` AC7's scratch clone and bare origin, `RUN_CLAIMS=on`.

- **AC1** — When the origin is renamed away and `--lease acquire build tOff` runs twice, the second
  prints `queued — already` and `grep -c '' gov-queue.log` prints 1.
  Red when: a re-run offline acquire queues a second line for one ref and tip.
- Removed at rev-8, the criterion once labelled AC2: its S5 trigger, a lost push whose remote tip is the queued commit, cannot occur (§4 Evidence).
- **AC3** — When a probe holds `gov-queue.lock` with a live `until` and calls `add_gov_queue`, the call
  exits 2 within 6 s printing `gov-queue.lock` and the file is unchanged. When the probe instead wraps
  `write_dir_lock`, the original kept under another name by `eval` of `declare -f`, so each call
  appends one line to a scratch count file and the wrapper removes the planted lock once the first
  call has returned busy, the call appends one line to `gov-queue.log` and the count file holds at
  least two lines.
  Red when: an append runs without the lock, or a build that tries once and exits busy appends,
  which the count's one line shows.
- **AC4** — When a probe overrides `write_gov_ref` with a stub that appends a second line to
  `gov-queue.log` while the first line is pushed, `write_gov_queue` resolves the first line and
  the file then holds exactly the second.
  Red when: a rewrite from the flush's first read drops a line appended during the pushes.
- **AC5** — When two background probes call `write_dir_lock` with stem `node` on one planted lock whose `until` has
  passed, exactly one prints `taken`, and the health log gains one `node-lock-broken` line.
  Red when: both breakers take the lock, the planted case being a scratch copy with the `.break` guard
  cut.
- **AC6** — When `awk` cuts each `gov_feed_sh` block from `gov-feed.sh`, `unattended.sh` and
  `post-merge.sh`, `cmp` finds the cuts equal and each defines `write_dir_lock`, and
  `grep -n 'gov-feed.lock' gov-feed.sh` names it only as `write_dir_lock`'s or `remove_dir_lock`'s
  argument.
  Red when: a copy drifts, or the feed keeps a lock of its own.
- **AC7** — When `grep -c '^write_dir_lock()' tools/unattended/unattended.sh` runs it prints 1, and
  the `awk` cut of `unattended.sh` from `# >>> gov_feed_sh` to `# <<< gov_feed_sh`, piped to the same
  `grep -c`, prints 1, so the one definition sits inside the inline block; `git grep -nE '(write|remove)_node[_]lock|check_node[_]lock_stale' -- tools`
  prints nothing; and `awk '/^## 9\./{s=1} /^## 10\./{s=0} !s && /(write|remove)_node[_]lock|check_node[_]lock_stale/'`
  over `memory/builds/dPlacedRequest/spec/*.md`, which skips each revision log's history, prints
  nothing.
  Red when: the tree holds a second lock factory, the definition stays outside the block, or a spec
  still names one.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC5 · the queue arms over a planted lock and a stub writer, staged against `TOOL-dPlacedRequest-1`'s unlocked queue · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does the queue's lock come from?** (a) One factory in `gov_feed_sh` restoring the
  guarded claim-push lock, taken by the feed and the queue; (b) a copy of the feed's unguarded lock for
  the queue; (c) the claim-push lock kept in the driver for the queue alone. (b) is a second copy of a
  lock with the stale-break race finding 36 names; (c) leaves the feed's copy beside it.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the charter's `[reuse]` rule at a kind's
  second instance. widens: none · relaxes: none. Rev-5 carries (a) as the shared `write_dir_lock`
  family moved into the block, the guarded claim-push lock as TOOL-aPiecewiseGrade-6 left it.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 56 (HIGH, item H9).
- rev-2 · 2026-10-25 · promoted fix brief: S1 gains its **Readers:** clause for the three renamed lock
  functions and two events; AC6 cites `gov-feed.sh` by basename, the file `TOOL-dPlacedRequest-13`
  creates.
- rev-3 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-36, hands-off TOOL-dPlacedRequest-37, hands-off
  TOOL-dPlacedRequest-38, hands-off TOOL-dPlacedRequest-39, hands-off TOOL-dPlacedRequest-41,
  hands-off TOOL-dPlacedRequest-43.
- rev-4 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-5 · 2026-11-19 · §2 S1, S2 · §3 Edges · §4 Evidence, The queue under the lock, Inventory, Files
  touched, Alternatives rejected · §5 · §6 AC5, AC6, AC7 · §8 F1 · §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`
  finding 15 (H3) and findings 16 and 33 (H4): S1 moves the shared `write_dir_lock` family into
  `gov_feed_sh` instead of minting a second factory from bodies the base no longer holds, every node
  lock passes the stem `node`, and AC7 observes one definition and no spec naming another. §7 also names `scratch-guard self-test`, `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-6 · 2026-11-19 · §2 S1, S2 · §3 Edges · §4 Evidence, Inventory, Files touched · §6 AC3, AC7 ·
  folds `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 1 (M1), S2 mints
  `NODE_LOCK_BOUND=10` at this unit's own order, so its takes expand no empty hold, and the hands-off
  to TOOL-dPlacedRequest-37 names the guard; finding 3 (M2), AC3's retry half releases the lock on the
  call's own busy return and counts at least two attempts; finding 4 (L1), S1's Readers and §4
  Evidence are rebuilt against the tree unit 11 leaves; finding 5 (L2), the `queued — already` row
  joins the Inventory table; finding 6 (L3), AC7 cuts the block and finds the definition inside it.
- rev-7 · 2026-11-19 · §2 S1, S2 · §3 Edges · §4 Inventory, Files touched · §5 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 12 (L4), S2 mints
  `write_dir_lock_wait`, the one retrying take its two locks and unit 49 S25 call; finding 16 (M7),
  the user-docs line names `help/loop.md`, which anchors the driver's verbs; finding 17 (M8), this
  unit's own pass regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-8 · 2026-11-19 · §1 · §2 S5 · §4 Evidence, The queue under the lock · §5 · §6 AC2 · §7 · folds
  `2026-11-19-prompt-TOOL-dPlacedRequest-24-divergence-brief`, the builder's DIVERGENCE of run
  `wf_495a7364-a80`: git 2.54.0 tests up to date before the lease, so a loser of two concurrent
  flushes keeps its line (rc 2) and its next flush prints `flushed`; the goal says so, S5 and AC2 are
  deleted with their `ls-remote` branch and perf line, AC2's id is left as a gap, the Evidence section now records the
  measurement PINNED, and §5 risks name `post-merge.sh`'s unset `ROOT` and `add_health_event` until
  TOOL-dPlacedRequest-36.

## 10. Reuse audit

The seam extended is the shared `write_dir_lock` family
(`tools/unattended/unattended.sh#write_dir_lock`), moved unchanged into the `gov_feed_sh` block
`TOOL-dPlacedRequest-13` mints, and `TOOL-dPlacedRequest-1`'s two queue functions. The recall below
ran at the pinned base, before TOOL-aPiecewiseGrade-6 renamed the claim-push lock into that family;
rev-5 read the factory at blob `875eaadf`. `python
tools/codebase-map/reuse_lookup.py "serialise a node-local append-only file with a directory lock and
a guarded stale break"` ranked `corpus_files`, `ask_filed_in` and `check_lease_only_diff`, name stems
only, none a lock; the claim-push lock is the tree's one guarded lock, found by reading the claim
block. `python tools/memory-recall/query.py "how is a node-local file serialised between sessions"`
returned TOOL-aMendedFleet-48 and TOOL-aGraftedHelix-37, whose specs mint and harden that lock, and the
audit's H9; none disagrees with source.

Recall terms used: mkdir lock stale break guard claim-push.lock gov-queue.log flush idempotence node-local
