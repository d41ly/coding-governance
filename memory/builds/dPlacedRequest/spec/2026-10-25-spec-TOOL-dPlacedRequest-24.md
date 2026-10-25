# TOOL-dPlacedRequest-24 — the offline queue under one guarded node lock, appended once and flushed honestly

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-24-deviation-241.md](../build/2026-10-25-build-TOOL-dPlacedRequest-24-deviation-241.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-24-deviation-242.md](../build/2026-10-25-build-TOOL-dPlacedRequest-24-deviation-242.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 56 at HIGH**, its item **H9**. `TOOL-dPlacedRequest-1` §4 "The offline queue"
has every successful read in every session on the node read, push and rewrite
`<git-common-dir>/gov-queue.log` line by line, with no lock and no idempotence key. Two concurrent
flushes push one commit, and the loser prints a false `yield` with a `lease-yielded` health event;
each rewrites the file from its own read and can drop a line appended between, losing a queued
acquisition; and re-running an offline acquire queues a second line for one ref and tip, which yields
spuriously. This unit repairs `TOOL-dPlacedRequest-1`: the queue is read and rewritten only under a
node lock, a line is appended once per ref and cached tip, and a lost push whose remote tip is the
queued commit is a landing, not a yield.

The lock is the second node-local lock this build mints, after `TOOL-dPlacedRequest-13`'s
`gov-feed.lock`, so it is built as one factory both take, carrying the guarded stale break the
deleted claim-push lock had (charter rule `[reuse]`).

## 2. Scope (IN)

- **S1** — The lock factory, in the `gov_feed_sh` block (`tools/lib/gov-feed.sh`, inline
  byte-identical in every copy): `write_node_lock <dir> <owner token>` returns 0 taken or 1 busy,
  `remove_node_lock <dir> <owner token>` removes it only while its `owner` file reads that token, and
  `check_node_lock_stale <dir>` reads its `until` deadline or, with none, its age. Their bodies are
  `write_claim_push_lock`, `remove_claim_push_lock` and `check_claim_push_lock_stale` at the pinned
  base (`tools/unattended/unattended.sh:2325-2360`), which `TOOL-dPlacedRequest-11` S6 deletes, renamed,
  with the `.break` guard serialising a stale break and the health events renamed
  `node-lock-broken` and `node-lock-guard-cleared`. **Readers:** by name: `write_claim_push_lock`,
  `remove_claim_push_lock` and `check_claim_push_lock_stale`, spelled by `tools/unattended/unattended.sh`
  (:2325-2444) and `tools/unattended/unattended.test.sh` (:16150-16279), and the two lock events,
  spelled by `tools/unattended/README.md` (:250); TOOL-dPlacedRequest-11 S6 retires each name and
  answers for those readers, and this item mints only the new names. by value: NO VALUE READERS, since
  the factory's only callers, the feed and the queue, are new in this build. Observed by AC5 and AC6.
- **S2** — Both node locks are taken through it. `add_feed_event`'s `gov-feed.lock`
  (`TOOL-dPlacedRequest-13` §4 step 1) and the queue's new `gov-queue.lock`, each in the common dir,
  each retried every 50 ms for up to 5 s; the feed keeps its rule that a lock it cannot take is a
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
- **S5** — A lost push that landed is landed. When `write_gov_ref` returns 1 for a queued line, one
  bounded `ls-remote` of the ref through `observe_remote` reads the remote tip: equal to the queued
  commit, the line is resolved as landed, with no `yield` line and no `lease-yielded` event; any other
  tip is today's `yield`. Observed by AC2.

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
- **hands-off** `TOOL-dPlacedRequest-34` — `write_node_lock` and the queue line, which that unit's items for findings 36 and 57 observe and extend
- **hands-off** `TOOL-dPlacedRequest-36` — `write_node_lock`'s two health events, which that unit writes through the lock's common dir and `health_log_sh`
- **hands-off** `TOOL-dPlacedRequest-37` — the `until` deadline, which that unit takes from `NODE_LOCK_BOUND`, never `REMOTE_BOUND`
- **hands-off** `TOOL-dPlacedRequest-38` — the `gov_feed_sh` lock functions, which that unit's parity-leg arm runs per inline copy under `set -u`
- **hands-off** `TOOL-dPlacedRequest-39` — `remove_node_lock`, which that unit's contained append calls from its `EXIT` trap
- **hands-off** `TOOL-dPlacedRequest-41` — `add_gov_queue`'s dedupe and `write_gov_queue`'s order, which that unit narrows to a record compare and chains per ref
- **hands-off** `TOOL-dPlacedRequest-43` — the flush's confirming read, `gov-feed.lock`'s spelling in `gov-feed.sh` and the lock factory, which that unit's items for findings 34, 12 and 39 amend and reuse
- **hands-off** `TOOL-dPlacedRequest-49` — `write_node_lock`'s write order, which that unit's item for finding 14 makes `owner` before `until`

## 4. Design

### Evidence

- The guarded lock at the base: `write_claim_push_lock` takes the directory, and on a stale lock takes
  a `.break` guard, re-checks staleness under it, removes and retakes the lock, and records
  `claim-push-lock-broken` (`tools/unattended/unattended.sh:2331-2354`, the event at `:2351`);
  `check_claim_push_lock_stale` reads `until`, else the age (`:2325-2330`); `remove_claim_push_lock`
  checks the owner token (`:2355-2360`). The block's comment, opening at `:2305`, states what the lock
  does not check (`:2318-2324`), and the factory keeps that paragraph.
- `TOOL-dPlacedRequest-11` S6 deletes the lock, its break and its wait with the lander's hold, and
  `TOOL-dPlacedRequest-13` §4 step 1 re-specifies an unguarded break for the feed.

### The queue under the lock

```
add_gov_queue ref tip commit
  write_node_lock gov-queue.lock      (50 ms retries, 5 s)   busy -> exit 2, nothing queued
  line with ref and tip present?      yes -> release, "queued — already"
  append ref TAB tip TAB commit TAB queued-utc
  remove_node_lock

write_gov_queue
  lock; snapshot = every line; unlock
  for each line, oldest first:  write_gov_ref ref tip commit   (no lock held)
    rc 0 -> resolved
    rc 1 -> ls-remote ref == commit ? resolved (landed) : resolved (yield, health event)
    rc 2 -> kept
  lock; rewrite = file now, less the resolved lines; unlock
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_node_lock`, `remove_node_lock` | shell functions, in `gov_feed_sh` | `write` and `remove`, OK |
| `check_node_lock_stale` | shell function, in `gov_feed_sh` | `check`, OK |
| `gov-queue.lock` | node-local directory | none |
| `node-lock-broken`, `node-lock-guard-cleared` | health events | none |
| `queued — already` | output line | none |

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: the factory, and the feed's lock taken through it
- `tools/unattended/unattended.sh`: the inline block, `add_gov_queue` and `write_gov_queue`
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the queue arms
- `tools/unattended/STOPS.template.md`: section 7's offline queue sentence names the lock and the
  dedupe
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **A lock held across the flush's pushes.** Every queued push is bounded by `REMOTE_BOUND`, so a
  flush of n lines would hold every other session for n bounds; the resolved-lines rewrite needs no
  such hold.
- **A second lock implementation for the queue.** The feed already has one; two node locks are the
  kind's second instance, which the charter's `[reuse]` rule makes a factory.
- **Deduping by the commit.** A re-run offline acquire builds a new commit with new stamps on the same
  tip, so the commit never repeats; the ref and cached tip do.

## 5. Production-readiness checklist

- security — no new surface: both files stay in the common dir and are never pushed.
- perf / scale — two lock takes per flush and one per append, each a `mkdir`; one `ls-remote` per lost
  push only.
- error / empty / loading states — a busy lock refuses an append with exit 2 and skips a flush with a
  NOTE; an empty queue flushes nothing.
- observability — `queued — already`, the NOTE lines and the two renamed health events.
- risks — the factory inherits the claim-push lock's stated blind spots (`:2318-2324`): four writers
  in one window around a stalled breaker, and a wall-clock step.
- testing — the probes of §6 and the arm in §7.
- migration — none: the queue and the lock are new in this build.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-1` AC7's scratch clone and bare origin, `RUN_CLAIMS=on`.

- **AC1** — When the origin is renamed away and `--lease acquire build tOff` runs twice, the second
  prints `queued — already` and `grep -c '' gov-queue.log` prints 1.
  Red when: a re-run offline acquire queues a second line for one ref and tip.
- **AC2** — When the origin is restored with its `refs/gov/leases/tOff/build` planted at the queued
  commit and `--lease flush` runs, it exits 0, prints no `yield`, the health log gains no
  `lease-yielded` line and `gov-queue.log` is empty; with the ref planted at another commit, it prints
  `yield`.
  Red when: a push another flush already landed is reported as lost.
- **AC3** — When a probe holds `gov-queue.lock` with a live `until` and calls `add_gov_queue`, the call
  exits 2 within 6 s printing `gov-queue.lock` and the file is unchanged; with the lock removed after
  1 s by a background `rm`, the call appends one line.
  Red when: an append runs without the lock.
- **AC4** — When a probe overrides `write_gov_ref` with a stub that appends a second line to
  `gov-queue.log` while the first line is pushed, `write_gov_queue` resolves the first line and
  the file then holds exactly the second.
  Red when: a rewrite from the flush's first read drops a line appended during the pushes.
- **AC5** — When two background probes call `write_node_lock` on one planted lock whose `until` has
  passed, exactly one prints `taken`, and the health log gains one `node-lock-broken` line.
  Red when: both breakers take the lock, the planted case being a scratch copy with the `.break` guard
  cut.
- **AC6** — When `awk` cuts each `gov_feed_sh` block from `gov-feed.sh`, `unattended.sh` and
  `post-merge.sh`, `cmp` finds the cuts equal and each spells `write_node_lock`, and
  `grep -n 'gov-feed.lock' gov-feed.sh` names it only as `write_node_lock`'s argument.
  Red when: a copy drifts, or the feed keeps a lock of its own.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the queue arms over a planted lock, a planted landed tip and a stub writer, staged against `TOOL-dPlacedRequest-1`'s unlocked queue · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does the queue's lock come from?** (a) One factory in `gov_feed_sh` restoring the
  guarded claim-push lock, taken by the feed and the queue; (b) a copy of the feed's unguarded lock for
  the queue; (c) the claim-push lock kept in the driver for the queue alone. (b) is a second copy of a
  lock with the stale-break race finding 36 names; (c) leaves the feed's copy beside it.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the charter's `[reuse]` rule at a kind's
  second instance. widens: none · relaxes: none

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

## 10. Reuse audit

The seam extended is the guarded claim-push lock at the pinned base
(`tools/unattended/unattended.sh:2318-2360`), restored as a generic factory in the `gov_feed_sh`
block `TOOL-dPlacedRequest-13` mints, and `TOOL-dPlacedRequest-1`'s two queue functions. `python
tools/codebase-map/reuse_lookup.py "serialise a node-local append-only file with a directory lock and
a guarded stale break"` ranked `corpus_files`, `ask_filed_in` and `check_lease_only_diff`, name stems
only, none a lock; the claim-push lock is the tree's one guarded lock, found by reading the claim
block. `python tools/memory-recall/query.py "how is a node-local file serialised between sessions"`
returned TOOL-aMendedFleet-48 and TOOL-aGraftedHelix-37, whose specs mint and harden that lock, and the
audit's H9; none disagrees with source.

Recall terms used: mkdir lock stale break guard claim-push.lock gov-queue.log flush idempotence node-local
