# TOOL-dPlacedRequest-16 — a lease never deleted: a release is a hand-over or a terminal tombstone, the epoch rises for life, and only a run's tombstone is ever pruned

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0134@bacb3ef7 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-16-deviation-161.md](../build/2026-10-25-build-TOOL-dPlacedRequest-16-deviation-161.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A lease's epoch must rise for its whole life, or a claim queued offline wins a unit another node has
already landed, at epoch 1 (gap-conc-13, research-cloud-headless P3 case 3). That holds only if a lease
is never deleted while a queued claim could race it, and if a released lease is told apart from a
finished one: a hand-over any node may take, or a terminal tombstone for a build or unit landed or
withdrawn, which refuses everything but a patch build's draw on its closed root's rework budget (the
layer-memory `[contract]`, v2:780-781, v2:1163). Today a terminal claim is "taken over by the slug's
next run and never deleted" (`tools/unattended/STOPS.template.md:193-194`), the take being the row
`preflight:foreign-terminal` (`tools/unattended/unattended.sh:2290`); never-deleted holds by omission,
and nothing queues a claim or prunes one.

## 2. Scope (IN)

- **S1** — The hand-over: the status `released` joins the reader's set (`unattended.sh:2162`) with the
  verdict `released`. `--lease release <kind> <name> [<sub>]` without `--as` writes it, and every mode
  of the write table reads a `released` record as free: it takes it, parented on its tip, at its epoch
  plus one, whoever released it. Observed by AC1.
- **S2** — A run's end hands its build's lease over: the driver's status writes of `landed` and
  `aborted` on a build lease (`:6383`, `:6634`, `:6770`, `:7620` and `--settle`'s) write `released`,
  the run's own outcome staying in its run-state file; `held` stays `held`. Only the `lease` verb's
  `--as landed` or `--as withdrawn` writes a build or unit lease terminal, at Deploy's release or a
  withdrawal. Observed by AC2.
- **S3** — The tombstone: a build or unit lease whose status is `landed` or `withdrawn`, and a `held`
  record whose parent is such a tombstone (a draw's hold), read the class `foreign-tombstone` in
  `CLAIM_READS` (`:2219`). Every mode refuses it with the cause `tombstone`, the run columns'
  `preflight:foreign-terminal` take included, except `--lease acquire build <slug> --for draw`. A
  cadence `run` lease and a legacy `refs/gov/runs/*` claim keep today's terminal take. Observed by AC3
  and AC4.
- **S4** — The draw: `--for draw` over a tombstone writes `held` at the epoch plus one, parented on the
  tombstone; over a draw's hold it refuses `live-holder` until `TOOL-dPlacedRequest-17` reads that hold
  stale, then takes it the same way. `--lease release build <slug> --as landed` writes the tombstone
  back at the same epoch. TOOL-dDeclaredLoop-30 S7's patch draw (`tools/loop/budget.py`) wraps its
  `patch:<slug>` row in that acquire and release, so concurrent draws on one closed root serialise.
  Observed by AC4.
- **S5** — The epoch for life: an acquisition of a ref the remote does not hold, whose ref this node's
  feed (`TOOL-dPlacedRequest-13`) names, reads the newest commit the feed holds for it. A build or unit
  tombstone there refuses `tombstone`; any other record makes the write a create parented on that commit
  at its epoch plus one, never at 1. Observed by AC5.
- **S6** — The queued claim's age: every successful lease read writes `<git-common-dir>/gov-last-fetch`
  with this node's time, `TOOL-dPlacedRequest-1`'s offline queue records it in the queued record's
  `last-fetch` key, and `write_gov_queue` refuses a queued write whose `last-fetch` is older than
  `leases.queued-claim-days` with the cause `epoch-fence`, removing it from the queue. A write it does
  not refuse is still a compare-and-swap on its recorded tip, so a claim queued after a release by a node
  whose last fetch preceded the lease yields on the moved tip, or is refused by age once the tombstone it
  would race could have been pruned. Observed by AC6 and AC7.
- **S7** — The prune: `unattended.sh --lease prune` prunes, through `write_gov_ref` with an empty
  source on the tip read, each cadence `run` lease and each legacy `refs/gov/runs/*` claim whose status
  is terminal and whose terminal commit `check_deadline_passed` reads older than
  `leases.queued-claim-days`. It never prunes a build or unit lease: naming one prints `prune refused —
  tombstone` and exits 1 with the ref unchanged. No other code path writes an empty source to a
  `refs/gov/leases/*` ref.
  Observed by AC8.
- **S8** — The stops guide's section 7 (`tools/unattended/STOPS.template.md:187-245`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) gains the `released` and `foreign-tombstone` rows, the draw, the
  queued-claim age and the prune, and its sentence "a terminal claim is taken over by the slug's next
  run" is narrowed to cadence and legacy run claims. Observed by AC9.

## 3. Non-goals (OUT)

- No supervisor: dWellOiledMachine's supervisor calls `--lease prune` on its cadence; this unit ships
  the verb and its refusal.
- No rework budget: the draw row and its spent and total are TOOL-dDeclaredLoop-30 S7's; this unit only
  serialises the draw under the root's lease.
- No offer: a hand-over is free to every node; an offer that reorders who takes it is
  `TOOL-dPlacedRequest-20`'s.
- No observer clock: `TOOL-dPlacedRequest-17`'s `check_deadline_passed` judges every age read here.
- No mailbox notice of a take: dKeptSession's.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — `refs/gov/leases/<slug>/build`, the epoch, the `last-fetch` key and the offline queue this unit refines
- **consumes-from** `TOOL-dPlacedRequest-17` — `read_first_seen` and `check_deadline_passed`, which judge the prune age of a tombstone
- **hands-off** external — dWellOiledMachine's supervisor runs `--lease prune`; TOOL-dDeclaredLoop-30's patch draw runs inside S4's acquire and release
- **consumes-from** `TOOL-dPlacedRequest-25` — `derive_lease_renews`, through which the take of a `released` lease and the draw set `renews`, so each opens its tenure renewed
- **hands-off** `TOOL-dPlacedRequest-28` — S5's feed read of an absent ref, which that unit moves into `read_feed_lease_tip` for every create
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-40` — `--lease prune`, which that unit exempts from the id-less refusal so a headless supervisor prunes

## 4. Design

### The statuses

| status | verdict | written by | a later write |
|---|---|---|---|
| `live` | `live` or `stale` | acquire, renew, the run's holder writes | per the table |
| `held` | `held` | `--hold`, a draw | per the table; a draw's hold reads `foreign-tombstone` |
| `released` | `released` | `--lease release`, a run's end | taken by any mode, epoch plus one |
| `landed`, `withdrawn` on a build or unit lease | `terminal`, class `foreign-tombstone` | `--lease release --as` | refused `tombstone` but a draw |
| `landed`, `aborted` on a run lease or a legacy claim | `terminal` | the cadence verb, a legacy run | today's terminal take |

The `--claims` row keeps five fields; `released` and `terminal` are values of its status and verdict
columns.

### The draw

```
unattended.sh --lease acquire build dRoot --for draw   # tombstone -> held, epoch n+1
python tools/loop/budget.py draw … patch:dPatch …      # TOOL-dDeclaredLoop-30 S7's row
unattended.sh --lease release build dRoot --as landed  # held -> landed, epoch n+1
```

A patch build that dies between the two leaves a draw's hold. It refuses every other mode
(`foreign-tombstone`), and once `TOOL-dPlacedRequest-17` reads it stale a later draw takes it, so the
closed root is never released as a free lease.

### Why only a run's tombstone is pruned

A pruned ref restarts at epoch 1 for any node whose feed never named it. A queued claim is refused once
its last fetch is older than `leases.queued-claim-days` (S6), and a tombstone is pruned only once its
terminal commit is that old (S7), so no queued claim outlives the tombstone it would race. A build or
unit tombstone is never pruned, because a patch build's draw on its closed root must always find it
(v2:1163, layer-memory:333-334). A cadence run lease names its period, so a later period is a new ref and
pruning an old one frees nothing anyone would draw on.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `released` | claim status value | none |
| `foreign-tombstone` | `CLAIM_READS` member | graded by leg check 52 |
| `tombstone` | refusal cause | none |
| `--for draw`, `--lease prune` | driver options | none |
| `gov-last-fetch` | node-local file | none |
| `write_lease_prune` | shell function | `write`, OK |

### Migration

None for data. A legacy `refs/gov/runs/*` claim a run left `landed` or `aborted` keeps today's terminal
take, so the slug's next run migrates it onto a live build lease as `TOOL-dPlacedRequest-1` S4 states.
This unit and `TOOL-dPlacedRequest-1` land in one landing, so no build lease ever carries a run's
`landed` from a window between them.

### Rollout

Live with `RUN_CLAIMS`. In this repository a run that ends after the landing hands its build over, and
the next run of the slug takes the hand-over at the epoch plus one, as it took a terminal claim before.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the `released` status and verdict, the `foreign-tombstone` class and
  its rows, the run's status writes, the draw, the epoch read from the feed, `gov-last-fetch`, the
  queued-claim age, `--lease prune`, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the tombstone, draw, prune and queued-claim arms
- `tools/unattended/STOPS.template.md`: section 7
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/loop/budget.py`: the patch draw's acquire and release, at TOOL-dDeclaredLoop-30 S7's site once
  that unit lands
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **A run's `landed` as the build's tombstone.** A spec run lands and its build run follows on the same
  slug; a tombstone there refuses the build run, which no clause intends.
- **A `purpose` key marking a draw's hold.** I6 fixes the keys; the hold's parent already says it
  follows a tombstone.
- **Pruning by the holder's release stamp.** It is a stamp another node wrote; the observer clock is the
  one rule for a cross-node deadline (`TOOL-dPlacedRequest-17`).

## 5. Production-readiness checklist

- security — no new write surface beyond the existing lease ref; the prune deletes only by
  compare-and-swap on the tip it read and refuses every build or unit lease.
- perf / scale — the prune is one read and one delete per prunable ref; the epoch read from the feed is
  one `awk` and one `cat-file` per absent ref.
- error / empty / loading states — a queued write refused by age leaves the queue and names its cause;
  an absent ref the feed never named is a plain create.
- observability — every refusal names `tombstone`, `live-holder` or `epoch-fence` and the ref.
- risks — a node whose feed never named a pruned run lease restarts its epoch at 1, safe only because no
  queued claim outlives the prune age.
- testing — the probes of §6 and the suite arms of §7.
- migration — none for data (§4).
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

- **AC1** — When session `s1` runs `--lease release build tFix` over its live lease at epoch 3 and session
  `s2` on a second fixture clone runs `--lease acquire build tFix`, the acquire exits 0 and the origin's
  lease reads `status: live`, `epoch: 4`, its parent the `released` commit. This is the clause's hand-over
  that some node can take.
  Red when: a hand-over is refused, or taken at the same epoch.
  fixture: two scratch clones of one bare origin, `RUN_CLAIMS=on`, each with a fleet user.
- **AC2** — When a fixture run's `--landed` writes its claim, the origin's build lease reads `released`,
  and `--preflight` of the same slug by a new keepalive takes it at the epoch plus one.
  Red when: a run's landing tombstones its build.
- **AC3** — When `--lease release build tFix --as landed` has run, `--lease acquire build tFix`,
  `--lease take-over build tFix` and `--preflight tFix` each exit 1 printing `tombstone` and the origin's
  lease is unchanged. This is the clause's terminal tombstone acquired for anything but a draw.
  Red when: any mode but the draw takes a tombstone.
- **AC4** — When `--lease acquire build tFix --for draw` runs over that tombstone at epoch 5, the lease
  reads `held` at epoch 6; a second `--for draw` exits 1 printing `live-holder`; `--lease release build
  tFix --as landed` restores `landed` at epoch 6; with the hold's feed sighting planted past
  `leases.expiry-hours`, a second draw takes it at epoch 7.
  Red when: a draw's hold reads free, or two draws hold one root at once.
- **AC5** — When the origin's `refs/gov/leases/run/maintain/2026-10` at epoch 4 is deleted outside the
  kit after this node sighted it, and `--lease acquire run maintain 2026-10` runs, the new commit reads
  epoch 5 and its parent is the deleted tip; with `refs/gov/leases/tFix/build` deleted after this node sighted its tombstone,
  `--lease acquire build tFix` exits 1 printing `tombstone`. This is the clause's pruned lease.
  Red when: a deleted lease restarts at epoch 1, or a deleted tombstone frees its build.
- **AC6** — When a queued acquire's `last-fetch` is planted eight days old under the default
  `leases.queued-claim-days`, `--lease flush` prints `lease refused — epoch-fence`, removes the line and
  writes nothing; at six days, it pushes. This is the clause's stale queued claim.
  Red when: a queued claim older than the bound is pushed.
- **AC7** — When clone A's last fetch read no lease for `tQ`, clone B acquires and releases `tQ`, and A,
  offline, queues an acquire of `tQ` and then reconnects, `--lease flush` prints `yield` and the origin
  keeps B's chain; with B's lease a pruned cadence lease and A's `last-fetch` planted past the bound, it
  prints `epoch-fence`. This is the clause's claim queued after a release by a node whose last fetch
  preceded the lease.
  Red when: A's queued claim lands at epoch 1.
- **AC8** — When `--lease prune` runs over a cadence lease terminal for eight days, a legacy run claim
  terminal for eight days, one terminal for six days and a build tombstone terminal for a year, it
  deletes the first two and leaves the other two; `--lease prune build tFix` exits 1 printing
  `prune refused — tombstone`. This is the clause's planted prune of a closed build's tombstone.
  Red when: a build or unit tombstone is deleted, or a young one is pruned.
- **AC9** — When `grep -n 'released\|tombstone\|--for draw\|leases.queued-claim-days'` runs over
  `STOPS.template.md`, each is found in section 7, and the terminal-take sentence names cadence and
  legacy run claims only.
  Red when: the guide still says every terminal claim is taken by the slug's next run.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the hand-over, tombstone, draw, epoch, queued-claim and prune arms, staged by restoring `preflight:foreign-terminal`'s take for a build lease and by cutting the age refusal · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — Which run claims does "a run claim's terminal tombstone" name, now that run claims are build
  leases?** (a) Cadence `run` leases and legacy `refs/gov/runs/*` claims; (b) every lease a run writes.
  (b) prunes build leases, which the clause forbids. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1,
  layer-memory:333 naming "run claims" beside the build's never-pruned tombstone. widens: none · relaxes: none
- **F3 — What does a run's `--landed` write on its build lease?** (a) `released`, the build's terminal
  tombstone written only by the release verb at Deploy or withdrawal; (b) `landed`, a tombstone. (b)
  refuses the build run after every spec run of this chain, which fails S1's hand-over for the very
  slug that needs it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, coordination.md:86-89
  releasing the build lease "at Deploy's item 9 and at any terminal status" of the build.
  widens: none · relaxes: none
- **F4 — Which cause refuses a stale queued claim?** I9 offers `offline` and `epoch-fence`. The refusal
  protects the epoch against a pruned lease, and the remote is reachable when it fires. RESOLVED (agent,
  2026-10-25, delegated): `epoch-fence`, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 16, scout A row 6, v2:780-781, v2:1163,
  layer-memory:325 and :333-334, research-cloud-headless P3 and S2.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: S7 says prune where it retires no named thing.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: consumes-from TOOL-dPlacedRequest-25,
  hands-off TOOL-dPlacedRequest-28, hands-off TOOL-dPlacedRequest-34, each the mirror of that
  promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-40.

## 10. Reuse audit

The seams extended are the claim reader's status set and verdict pass (`tools/unattended/
unattended.sh:2162`, `:2183`), the write table's classes and rows (`:2219`, `:2284-2301`), and
`TOOL-dPlacedRequest-1`'s offline queue; ages come from `TOOL-dPlacedRequest-17`'s observer clock and
the deleted ref's last record from `TOOL-dPlacedRequest-13`'s feed. `python tools/codebase-map/
reuse_lookup.py "release a claim with a terminal status and never delete it"` ranked `write_claim`,
`check_claim_writable` and the claim-push lock functions, all in the claim block above, and
`ts_release` (`tools/run-gates/run-gates.sh`, the turnstile, a different lease); no seam fits the
prune or the queued-claim age, and `git grep` finds no deletion of a `refs/gov` ref outside test
fixtures, agreeing with scout A's row 6. `python tools/memory-recall/query.py "when may a released or
terminal lease be pruned and what stops an epoch restart"` returned the brief's unit row, scout A's row 6,
v2's `[chain]` row and the packet's Items; none disagrees with source.

Recall terms used: tombstone released hand-over epoch prune queued-claim-days last-fetch closed root draw never deleted
