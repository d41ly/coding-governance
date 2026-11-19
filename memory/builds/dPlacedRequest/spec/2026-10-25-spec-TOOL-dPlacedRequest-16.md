# TOOL-dPlacedRequest-16 — a lease never deleted: a release is a hand-over or a terminal tombstone, the epoch rises for life, and only a run's tombstone is ever pruned

**Status:** INPROGRESS · rev-8 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0134@bacb3ef7 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-16-deviation-161.md](../build/2026-10-25-build-TOOL-dPlacedRequest-16-deviation-161.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-34 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-16-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-16-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-16-divergence-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-16-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

A lease's epoch must rise for its whole life, or a claim queued offline wins a unit another node has
already landed, at epoch 1 (gap-conc-13, research-cloud-headless P3 case 3). That holds only if a lease
is never deleted while a queued claim could race it, and if a released lease is told apart from a
finished one: a hand-over any node may take, or a terminal tombstone for a build or unit landed or
withdrawn, which refuses everything but a patch build's draw on its closed root's rework budget (the
layer-memory `[contract]`, v2:780-781, v2:1163). Today a terminal claim is "taken over by the slug's
next run and never deleted" (`tools/unattended/STOPS.template.md@be658f8fe45c:202`), the take being
the row `preflight:foreign-terminal` of `tools/unattended/unattended.sh#check_claim_writable`;
never-deleted holds by omission, and nothing queues a claim or prunes one.

## 2. Scope (IN)

- **S1** — The hand-over: the status `released` joins the reader's set
  (`tools/unattended/unattended.sh#read_claims`) with the verdict `released`, so a `released` record
  reads the class `foreign-released`, which joins `CLAIM_READS` beside `foreign-tombstone` and is read
  before the identity rows (§4 "The class order"). `--lease release <kind> <name> [<sub>]` without
  `--as` writes it, and every mode of the write table reads a `released` record as free: it takes it,
  parented on its tip, at its epoch plus one, whoever released it, its releaser included. Observed by
  AC1 and AC12.
- **S2** — A run's end hands its build's lease over: the driver's status writes of `landed` and
  `aborted` on a build lease write `released`: two in `tools/unattended/unattended.sh#verb_landed`, one
  each in `tools/unattended/unattended.sh#verb_abort`, `tools/unattended/unattended.sh#verb_preflight`
  and `tools/unattended/unattended.sh#write_settle_claim`. The run's own outcome stays in its run-state
  file, and `held` stays `held`. Only the `lease` verb's
  `--as landed` or `--as withdrawn` writes a build or unit lease terminal, at Deploy's release or a
  withdrawal. `--lease release` is total over its kind and its `--as` (§4 "The release outcomes", §8
  F5): a build or unit lease admits no `--as`, `landed` and `withdrawn`; a cadence `run` lease admits
  no `--as`, `landed` and `aborted`; every other pair, `--as aborted` on a build or unit lease and
  `--as withdrawn` on a run lease, prints `lease not written — --as <status> on a <kind> lease`, exits
  2 and writes nothing. Observed by AC2 and AC11.
- **S3** — The tombstone: a build or unit lease whose status is `landed` or `withdrawn`, and a `held`
  record whose first-parent chain reaches such a tombstone through `held` records only (a draw's hold,
  however many draws re-took it), read the class `foreign-tombstone`, which joins `CLAIM_READS` in the
  order §4 "The class order" states. The chain is read by one `git log --first-parent` over the
  fetched ref, stopping at the first record that is not `held`. Every mode but `beat` and `status`,
  which decline and announce it, refuses it as that section's column table states, the run columns'
  `preflight:foreign-terminal` take included, except `--lease acquire build <slug> --for draw`. A
  cadence `run` lease and a legacy `refs/gov/runs/*` claim keep today's terminal take. Observed by AC3
  and AC4.
- **S4** — The draw: `--for draw` over a tombstone writes `held` at the epoch plus one, parented on the
  tombstone. Over a draw's hold it refuses `live-holder` until the hold is stale by §8 F6's rule (§4
  "The draw"), then takes it the same way, parented on that hold, so S3's chain still reaches the
  tombstone. A write by the hold's own holder keeps
  `status: held`: a renew or re-acquire of a draw's hold writes `held`, never `live`.
  `--lease release build <slug> --as landed` writes the tombstone back at the same epoch, and it is the
  one release a draw's hold admits: a release without `--as`, or with any other, prints
  `lease not written — a draw's hold is released --as landed`, exits 2 and leaves the hold reading
  `foreign-tombstone`. `tools/unattended/unattended.sh#run_budget_draw` wraps the patch draw in that
  acquire and release on its closed root, so concurrent draws on one closed root serialise (§8 F7).
  Observed by AC4, AC11 and AC14.
- **S5** — The epoch for life: an acquisition of a ref the remote does not hold, whose ref this node's
  feed (`TOOL-dPlacedRequest-13`) names, reads the newest commit the feed holds for it. A build or unit
  tombstone there refuses `tombstone`; any other record makes the write a create parented on that commit
  at its epoch plus one, never at 1. Observed by AC5.
- **S6** — The queued claim's age: every successful lease read writes `<git-common-dir>/gov-last-fetch`
  with this node's time, atomically: the stamp goes to `gov-last-fetch.<pid>` in the same directory
  and `mv -f` replaces the file, so a reader sees the old stamp or the new one, never an empty or
  half-written file. `TOOL-dPlacedRequest-1`'s offline queue records it in the queued record's
  `last-fetch` key, and `write_gov_queue` refuses a queued write whose `last-fetch` is older than
  `leases.queued-claim-days` with the cause `epoch-fence`, removing it from the queue. When
  `gov-last-fetch` is absent or holds no ISO-8601 UTC second, the queued record's `last-fetch` reads
  `-`, as `TOOL-dPlacedRequest-1` writes it before this unit lands, and `write_gov_queue` refuses a
  `-` or unparsable `last-fetch` as `epoch-fence` too, removing the line: a claim that never read the
  remote is not pushed on a guess. A write it does
  not refuse is still a compare-and-swap on its recorded tip, so a claim queued after a release by a node
  whose last fetch preceded the lease yields on the moved tip, or is refused by age once the tombstone it
  would race could have been pruned. Observed by AC6, AC7, AC10 and AC13.
- **S7** — The prune: `unattended.sh --lease prune` prunes, through `remove_gov_ref` on the tip read
  (`TOOL-dPlacedRequest-11` S1), each cadence `run` lease and each legacy `refs/gov/runs/*` claim whose status
  is terminal and whose terminal commit `check_deadline_passed` reads older than
  `leases.queued-claim-days`. It never prunes a build or unit lease: naming one prints `prune refused —
  tombstone` and exits 1 with the ref unchanged. No other code path calls `remove_gov_ref` on a
  `refs/gov/leases/*` ref, and `write_gov_ref` refuses an empty source, so a failed commit build never
  becomes a deletion.
  Observed by AC8.
- **S8** — The stops guide's section 7 (`tools/unattended/STOPS.template.md@be658f8fe45c:171`,
  rendered to `memory/guides/UNATTENDED-STOPS.md`) gains the `released` and `foreign-tombstone` rows,
  the class order, the draw, the queued-claim age and the prune, and its sentence "a terminal claim is
  taken over by the slug's next run" is narrowed to cadence and legacy run claims. Observed by AC9.
- **S9** — The kickoff card: `skills/session-kickoff/manifest-check.sh#derive_claims_line` ranks
  `released` beside `terminal` in its closed verdict set and hides it under the same
  `CARD_CLAIMS_HIDE_S` rule (§8 F8). Observed by AC15.

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
- **consumes-from** `TOOL-dPlacedRequest-11` — `remove_gov_ref`, the one deletion form, which the prune calls; without it a prune would have to push an empty source
- **consumes-from** `TOOL-dPlacedRequest-17` — `read_first_seen` and `check_deadline_passed`, which judge a tombstone's prune age and a draw's hold's age over its renewing beat
- **hands-off** external — dWellOiledMachine's supervisor runs `--lease prune`
- **consumes-from** `TOOL-dPlacedRequest-25` — `derive_lease_renews`, through which the take of a `released` lease and the draw set `renews`, so each opens its tenure renewed
- **hands-off** `TOOL-dPlacedRequest-28` — S5's feed read of an absent ref, which that unit moves into `read_feed_lease_tip` for every create
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-40` — `--lease prune`, which that unit exempts from the id-less refusal so a headless supervisor prunes

## 4. Design

### The statuses

| status | verdict | written by | a later write |
|---|---|---|---|
| `live` | `live` or `stale` | acquire, renew, the run's holder writes | per the table |
| `held` | `held` | `--hold`, a draw, its holder's renew | per the table; a draw's hold, at any depth of re-takes, reads `foreign-tombstone` to all but its holder, and a draw takes it once stale |
| `released` | `released`, class `foreign-released` | `--lease release`, a run's end | taken by any mode, its releaser included, epoch plus one |
| `landed`, `withdrawn` on a build or unit lease | `terminal`, class `foreign-tombstone` | `--lease release --as` | refused `tombstone`, its writer included, but a draw |
| `landed`, `aborted` on a run lease or a legacy claim | `terminal` | the cadence verb, a legacy run | today's terminal take |

The `--claims` row keeps five fields; `released` and `terminal` are values of its status and verdict
columns.

### The release outcomes

| lease read | no `--as` | `--as landed` | `--as withdrawn` | `--as aborted` |
|---|---|---|---|---|
| build or unit, `live` and mine | `released` | `landed` | `withdrawn` | refused, exit 2 |
| build, a draw's hold and mine | refused, exit 2 | `landed`, the epoch kept | refused, exit 2 | refused, exit 2 |
| cadence `run`, `live` and mine | `released` | `landed` | refused, exit 2 | `aborted` |

Every refused pair prints one `lease not written —` line naming the pair and writes nothing, so no
release writes a status the statuses table above does not read (§8 F5).

### The class order

`check_claim_writable` reads a row's class in this order, the first step that holds deciding (§8 F9):

| step | the row read | its class |
|---|---|---|
| 1 | status `released` | `foreign-released` |
| 2 | a build or unit lease whose status is `landed` or `withdrawn` | `foreign-tombstone` |
| 3 | the identity rows, as today | `mine`, `same` |
| 4 | a draw's hold, by S3's chain | `foreign-tombstone` |
| 5 | any other row, as today | `foreign-<verdict>` |

So a releaser takes its own `released` lease at the epoch plus one, nobody revives a tombstone, and a
draw's holder reads its hold `mine`. A terminal cadence `run` lease or legacy claim stays
`foreign-terminal`. A `foreign-tombstone` cell refuses by its column's existing refusal, its line
carrying `tombstone`; the check numbers are the `fail` calls in
`tools/unattended/unattended.sh#check_claim_writable` (PINNED 2026-11-19).

| column | its callers | over a tombstone, checks PINNED |
|---|---|---|
| `preflight`, `take-over` | `--preflight`, a take-over | check 107, exit 1 |
| `holder` | the run's own holder writes | check 108, exit 1 |
| `status` | `--hold`, S2's landing and abort writes, `--settle` | announced, exit unchanged |
| `lease` | the `--lease` verbs | `lease refused — tombstone`, exit 1; `--for draw` takes it |
| `beat` | `--beat` | declined, as today |

The status cell announces one line carrying `tombstone`, writes no lease commit and leaves the verb's
exit alone, as its non-writing rows do: a run must still close over its own `--as landed` tombstone.

### The draw

```
unattended.sh --lease acquire build dRoot --for draw   # tombstone -> held, epoch n+1
budget.py draw --build=dPatch …                        # the module derives the row's patch:dPatch cause
unattended.sh --lease release build dRoot --as landed  # held -> landed, epoch n+1
```

`run_budget_draw` makes the three calls in-process, the lease calls through `run_lease_verb`, on the
closed root `check_patch_peers` reads from `budget.py origin`; a build with no readable origin draws as
today. The draw runs only when the acquire exits 0 and its line is not a `queued` one; otherwise
`_bd_rc` is 2, `_bd_why` reads `budget: patch draw refused — ` and the acquire's line, which both
callers already relay, and nothing is drawn. With `RUN_CLAIMS` off the draw runs unguarded, as today.
The release runs after every draw answer; one that does not exit 0 prints its line and leaves the hold.

A draw's hold is stale when `check_deadline_passed` returns 0 over the hold's
`refs/gov/leases/<slug>/build`, its renewing beat and the seconds `read_lease_bound expiry` prints (§8
F6). The beat is the one the walk in `tools/unattended/unattended.sh#read_claims` already finds by
TOOL-dPlacedRequest-17 S2's rule, carried out as a nineteenth row field, `beat-sha`, after the eighteen
its header names (DERIVED from that list), so no second walk exists. A return of 1 or 2, a refused
bound or a `renews: -` beat refuses `live-holder`, as TOOL-dPlacedRequest-17 S3 never reads such a row
stale.

A patch build dying mid-draw leaves a hold that refuses every other mode until stale, when a later
draw takes it, parented on it; the closed root is never released free.

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
| `foreign-tombstone`, `foreign-released` | `CLAIM_READS` members | graded by leg check 52 |
| `tombstone` | refusal cause | none |
| `--for draw`, `--lease prune` | driver options | none |
| `gov-last-fetch` | node-local file | none |
| `beat-sha` | the claim row's appended field | none |
| `write_lease_prune` | shell function | `write`, OK |

### Migration

None for data. A legacy `refs/gov/runs/*` claim a run left `landed` or `aborted` keeps today's terminal
take, so the slug's next run migrates it onto a live build lease as `TOOL-dPlacedRequest-1` S4 states.
This unit and `TOOL-dPlacedRequest-1` land in one landing, so no build lease ever carries a run's
`landed` from a window between them.

### Rollout

Live with `RUN_CLAIMS`. In this repository a run that ends after the landing hands its build over, and
the next run of the slug takes the hand-over at the epoch plus one, as it took a terminal claim before.
The card's reader lands with the driver; an older card skips its claims cell over a `released` row.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the `released` status and verdict, the class order, the
  `foreign-tombstone` class and its refusals, the run's status writes, the draw, its staleness and its
  wrap in `run_budget_draw`, the `beat-sha` field, the epoch read from the feed, `gov-last-fetch`, the
  queued-claim age, `--lease prune`; the kit version is minted by the lander (TOOL-aMendedFleet-65; TOOL-dPlacedRequest-34 S59)
- `tools/unattended/unattended.test.sh`: the tombstone, draw, draw-wrap, prune and queued-claim arms;
  `GC_CELLS` gains one row per (`foreign-tombstone`, mode) and per (`foreign-released`, mode) over
  `CLAIM_MODES`' six modes, `lease` included. Each `foreign-tombstone` cell types its column's refusal
  from §4 "The class order", the ref `same`, its `status` cell exit 0 and `announced`; each
  `foreign-released` cell types S1's take, the ref
  `moved`, its `holder` cell refused as `foreign-terminal`'s; both `beat` cells `declined`.
  `tools/unattended/unattended.test.sh#seed_claim_row` and
  `tools/unattended/unattended.test.sh#seed_lease_row` each gain the two cases,
  a `landed` build lease and a `released` one, seeded under the reacher's own identity, so every cell
  also shows the class read before `mine`
- `help/loop.md`: the `verb:unattended.sh:--lease` usage anchor `TOOL-dPlacedRequest-1` adds, its
  fingerprint refreshed to the one the govkit kit's `docs_leg.py --fingerprints` prints once
  `--lease prune` and `--for draw` move the usage line; the card paragraph, that a `released` row
  shows as a `terminal` one
- `skills/session-kickoff/manifest-check.sh`: `derive_claims_line`'s verdict set and hide rule (S9)
- `skills/session-kickoff/manifest-check.test.sh`: the `released` seeds beside the seven-claim arm
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since its `watch:` line names
  `skills/session-kickoff/manifest-check.sh`
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass, since `write_lease_prune` is minted, so `gen_map.py --check` exits 0 after the
  pass; `TOOL-dPlacedRequest-34` S38 is the final re-check only
- `tools/unattended/STOPS.template.md`: section 7
- `memory/guides/UNATTENDED-STOPS.md`: its render
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
  compare-and-swap on the tip it read and refuses every build or unit lease; a patch draw is denied
  unless its acquire took the hold.
- perf / scale — the prune is one read and one delete per prunable ref; the epoch read from the feed is
  one `awk` and one `cat-file` per absent ref.
- error / empty / loading states — a queued write refused by age leaves the queue and names its cause;
  an absent ref the feed never named is a plain create.
- observability — every refusal names `tombstone`, `live-holder` or `epoch-fence` and the ref; a
  refused draw relays the acquire's line.
- risks — a node whose feed never named a pruned run lease restarts its epoch at 1, safe only because no
  queued claim outlives the prune age.
- testing — the probes of §6 and the suite arms of §7.
- migration — none for data (§4).
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7, and `help/loop.md`, which anchors the
  unattended driver's verbs beside its `--claims` paragraph: this unit refreshes the `--lease`
  anchor's fingerprint and says how the card shows a `released` row.

## 6. Acceptance criteria

- **AC1** — When session `s1` runs `--lease release build tFix` over its live lease at epoch 3 and session
  `s2` on a second fixture clone runs `--lease acquire build tFix`, the acquire exits 0 and the origin's
  lease reads `status: live`, `epoch: 4`, its parent the `released` commit; when `s1` itself acquires
  instead, the same holds. This is the clause's hand-over that some node can take.
  Red when: a hand-over is refused, or taken at the same epoch, its releaser's acquire included.
  fixture: two scratch clones of one bare origin, `RUN_CLAIMS=on`, each with a fleet user.
- **AC2** — When a fixture run's `--landed` writes its claim, the origin's build lease reads `released`,
  and `--preflight` of the same slug by a new keepalive takes it at the epoch plus one.
  Red when: a run's landing tombstones its build.
- **AC3** — When `--lease release build tFix --as landed` has run, `--lease acquire build tFix` by its
  writer and by another session and `--lease take-over build tFix` each exit 1 printing `tombstone`;
  `--preflight tFix` exits 1 printing `UNATTENDED check 107 FAILED` and `tombstone`. The origin's
  lease is unchanged throughout. This is the clause's terminal tombstone acquired for anything but a draw.
  Red when: any mode but the draw takes a tombstone, its writer included, or a column refuses one
  without the word `tombstone`.
- **AC4** — When `--lease acquire build tFix --for draw` runs over that tombstone at epoch 5, the lease
  reads `held` at epoch 6, and `--lease release build tFix --as landed` restores `landed` at epoch 6. A
  second draw holds it at epoch 7; its holder's `--lease renew build tFix` writes `status: held` and
  `renews: no`, and another session's `--for draw` exits 1 printing `live-holder`. With the feed
  sighting of the epoch-7 opener planted past `leases.expiry-hours` and the renew's left fresh, that
  draw takes the hold at epoch 8, parented on it, and the record reads `status: held` with the class
  `foreign-tombstone` for a third session; with the epoch-8 opener's sighting removed from the feed, a
  draw exits 1 printing `live-holder`. With the epoch-8 hold planted stale, `--lease take-over build
  tFix` and a plain `--lease acquire build tFix` each exit 1 printing `tombstone`, the origin unchanged.
  Red when: a draw's hold reads free at any depth, a renew turns a hold `live`, a holder's `renews: no`
  beat keeps a dead hold alive, or two draws hold one root at once.
  figure: epochs PINNED by the planted tombstone; `renews: no` DERIVED by `derive_lease_renews`.
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
- **AC10** — When `<git-common-dir>/gov-last-fetch` is deleted before an offline `--lease acquire
  build tOff`, the queued record reads `last-fetch: -`; with the origin restored, `--lease flush`
  prints `lease refused — epoch-fence`, removes the line and writes no ref. With the file planted
  `garbage`, the same holds.
  Red when: a claim queued with no recorded fetch is pushed, or the flush exits on the value.
- **AC11** — When the holder runs `--lease release build tFix --as aborted` over its live build lease
  and `--lease release run maintain 2026-10 --as withdrawn` over its live cadence lease, each exits 2
  printing `lease not written` and the origin is unchanged; `--as landed`, `--as withdrawn` and no
  `--as` on the build lease, and `--as aborted` on the run lease, write the status §4 "The release
  outcomes" names. Over a draw's hold, `--lease release build tFix` and `--lease release build tFix
  --as aborted` each exit 2, the lease still reads `foreign-tombstone` for another session, and that
  session's `--lease acquire build tFix` exits 1 printing `tombstone`.
  Red when: a release writes a status no row of §4's statuses table reads, or a plain release of a
  draw's hold frees the closed root.
- **AC12** — When a probe derives `CLAIM_READS` by `CLAIM_MODES` from `tools/unattended/unattended.sh`
  and the cells `GC_CELLS` types, as the GH19 arm does, and compares them with `comm -3`, it prints
  nothing, and `CLAIM_READS` names `foreign-tombstone` and
  `foreign-released`.
  Red when: a class this unit adds has a mode with no typed outcome.
- **AC13** — When a probe that sources `unattended.sh` in a scratch clone runs S6's stamp write 200
  times in a background loop beside a loop of 200 offline `--lease acquire build tOff` queue writes in
  that clone, over a `gov-last-fetch` holding a valid stamp before the loops start, no queued record
  reads `last-fetch: -`, and `grep -c '> *"[^"]*gov-last-fetch"'` over `tools/unattended/unattended.sh`
  prints 0.
  Red when: a reader catches the file truncated, so a valid queued claim is dropped as `epoch-fence`.
  fixture: one scratch clone whose origin is renamed away, so every acquire queues.
- **AC14** — When a probe that sources `unattended.sh` in a scratch clone calls `run_budget_draw tPatch
  re-dispatch u1` for a patch build `tPatch` of `tFix`, tombstoned at epoch 5, `_bd_rc` reads 0, one
  draw row is written, and the origin's `refs/gov/leases/tFix/build` log reads, newest first, `landed`
  at epoch 6, `held` at epoch 6, then the epoch-5 tombstone. With another session's fresh draw hold
  on `tFix`, the call sets `_bd_rc` 2, `_bd_why` naming `live-holder`, and moves no row or lease; with
  the origin renamed away, `_bd_why` names `queued` and no row is drawn. With `RUN_CLAIMS=off` it
  draws and no lease ref moves.
  Red when: a patch draw runs without a hold on its closed root, or a refused or queued acquire draws.
  fixture: none in the tree today; the arm plants `tPatch` with `scenario.patch` and `parents: tFix`.
  figure: the epochs are PINNED by the planted tombstone.
- **AC15** — When the card fixture's remote carries a `released` claim `sRel` with a beat two hours old
  and a `released` claim `rRelOld` three days old beside its seven claims, `manifest-check.sh --card
  --write` writes a `claims —` cell whose head counts nine on the remote, `sRel`'s row sorted beside
  `vLanded`'s `terminal` row, `rRelOld` hidden, and no `claims — skipped:` line.
  Red when: a `released` row blanks the cell, or one older than `CARD_CLAIMS_HIDE_S` is shown.
  figure: nine is DERIVED from the seeds; `CARD_CLAIMS_HIDE_S` is one day, PINNED 2026-11-19.
- **AC16** — When `--settle tFix` runs after a fixture run's own `--lease release build tFix --as
  landed`, it exits 0, prints one line carrying `tombstone`, and the origin's lease is unchanged.
  Red when: the status column refuses a run's own tombstone, so the run cannot close.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `docs` · `codebase-map coverage + freshness` · `manifest-check self-test`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC10 AC11 AC12 AC13 AC14 AC16 · the GC_CELLS rows for `foreign-tombstone` and `foreign-released` and the hand-over, tombstone, draw, draw-wrap, epoch, queued-claim and prune arms, staged by restoring `preflight:foreign-terminal`'s take for a build lease, by classing the new rows after `mine`, by drawing past a refused acquire and by cutting the age refusal · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14, and each covered criterion's own probe is the observation at landing
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC15 · the two `released` seeds beside the seven-claim arm, staged by dropping `released` from `derive_claims_line`'s verdict set · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `tools/memory-tree/tree_lib.py#STATUS_TOKENS`. Observation, 2026-10-25: the tuple holds
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
- **F5 — What does `--lease release` write for a pair the statuses table has no row for: `--as aborted`
  on a build or unit lease, `--as withdrawn` on a run lease, and any release of a draw's hold but
  `--as landed`?** (a) Refuse each with exit 2, writing nothing; (b) map each onto a row, `aborted` on a
  build as `released`, `withdrawn` on a run as `aborted`, and any release of a hold as `landed`. (b)
  writes a status the caller did not name, and on a hold whose root was withdrawn it would write
  `landed`. RESOLVED (agent, 2026-11-19, delegated): (a), rung 3, the charter's deny-by-default at the
  write boundary; a plain release of a draw's hold then leaves the hold, which a later draw takes.
  widens: none · relaxes: none
- **F6 — Who reads a draw's hold stale, when TOOL-dPlacedRequest-17 S3 keeps `held` out of its age
  verdict?** (a) This unit judges it with `check_deadline_passed` and `read_lease_bound expiry`, aging
  the renewing beat TOOL-dPlacedRequest-17's walk finds on the hold's chain; (b) the same, aging the
  hold's tip; (c) a hold never expires. RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; it is the
  beat every other lease ages by (one rule, TOOL-dPlacedRequest-17 F5), (b) lets a holder's plain
  `renews: no` beat keep a dead hold alive, (c) blocks every later draw for a dead holder.
  widens: none · relaxes: none
- **F7 — Where is the patch draw wrapped, and what does an acquire that does not take the hold do?**
  (a) `run_budget_draw`, an acquire that refuses, queues or prints `lease not written` refusing the
  draw, and with `RUN_CLAIMS` off the draw unguarded (TOOL-dPlacedRequest-1 F2); (b)
  `tools/loop/budget.py`, which holds no lease seam; (c) the draw made anyway. RESOLVED (agent,
  2026-11-19, delegated): the driver's run_budget_draw, a non-zero acquire refusing the draw, rung 3;
  deny by default, and the only call site that already holds a claim read. widens: none · relaxes: none
- **F8 — How does the card show a `released` row, its verdict set closed at `live held unknown stale
  terminal`?** (a) Ranked beside `terminal` and hidden by the same `CARD_CLAIMS_HIDE_S` rule; (b)
  shown at any age; (c) left an unreadable line. RESOLVED (agent, 2026-11-19, delegated): (a), rung 3;
  (b) keeps every landed build on every card, (c) blanks the claims section after every landing.
  widens: none · relaxes: none
- **F9 — Where do the new classes sit against the identity rows `mine` and `same`?** (a) A released
  record and a true tombstone before them, a draw's hold after, a tombstone refused by each column's
  existing refusal carrying `tombstone`; (b) all after; (c) all before. RESOLVED (agent, 2026-11-19,
  delegated): (a), rung 3; (b) lets a releaser renew at the same epoch and a writer revive its
  tombstone, (c) leaves a draw's holder unable to renew or release its hold; the status column
  announces a tombstone, exit unchanged, so a run closes over its own. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 16, scout A row 6, v2:780-781, v2:1163,
  layer-memory:325 and :333-334, research-cloud-headless P3 and S2.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: S7 says prune where it retires no named thing.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: consumes-from TOOL-dPlacedRequest-25,
  hands-off TOOL-dPlacedRequest-28, hands-off TOOL-dPlacedRequest-34, each the mirror of that
  promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-40.
- rev-5 · 2026-11-19 · §4 Files touched · §7 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`: finding 24 (H6), the kit version is the lander's to mint; finding 4 (M3), the unattended.test.sh arm cites README rule 8 and owes its clean reading to PLAY-dClosedLoop-14. §7 also names `scratch-guard self-test`, `tier2-review self-test`, `policy fixtures`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-6 · 2026-11-19 · §2 S6, S7 · §3 Edges · §6 AC10 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 29 (M12), an absent or unparsable
  `gov-last-fetch` records `last-fetch: -`, which the flush refuses as `epoch-fence`, observed by AC10;
  finding 28 (H4), the prune goes through `remove_gov_ref`, with the consumes-from edge to
  TOOL-dPlacedRequest-11 mirroring its hands-off.
- rev-7 · 2026-11-19 · §2 S1 to S4, S6 · §4 · §5 · §6 AC4, AC11 to AC13 · §7 · §8 F5 · §10 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 18 (H2), the tombstone class holds
  over the whole chain of draws and a holder's renew keeps `held` (AC4); findings 2 and 19 (M2),
  `--lease release` is total over kind and `--as`, refusing every pair no status row reads and every
  release of a draw's hold but `--as landed` (§4 The release outcomes, §8 F5, AC11); finding 15
  (M6), `foreign-released` joins `CLAIM_READS` and `GC_CELLS` types both new classes (AC12); finding
  21 (M9), `gov-last-fetch` is replaced atomically (AC13); finding 16 (M7), the `--lease` anchor is
  refreshed and §7 names `docs`; finding 17 (M8), the map is regenerated in this pass; finding 9
  (L3), §10 names `remove_red_ref`.
- rev-8 · 2026-11-19 · §1 · §2 S1 to S4, S8, S9 · §3 Edges · §4 · §5 · §6 AC1, AC3, AC4, AC14, AC15 · §7 ·
  §8 F1, F6 to F9 · §10 · folds `2026-11-19-prompt-TOOL-dPlacedRequest-16-divergence-brief`, the rulings
  on the builder's DIVERGENCE of run `wf_8d80f1b3-f05`: F6 the hold's staleness (AC4), F7 the draw's
  wrap in `run_budget_draw` (AC14), F8 the card (AC15), F9 the class order (AC1, AC3); line citations
  become `path#symbol` or blob-pinned. A later ruling: the status column announces a tombstone, exit
  unchanged (§4, S3, §5, F9, AC3, AC16).

## 10. Reuse audit

The seams extended are the claim reader's status set, verdict pass and walk
(`tools/unattended/unattended.sh#read_claims`), the write table's classes and rows
(`tools/unattended/unattended.sh#check_claim_writable`), the patch draw's claim read
(`tools/unattended/unattended.sh#run_budget_draw`, beside `check_patch_peers`), the card's claims reader
(`skills/session-kickoff/manifest-check.sh#derive_claims_line`), and `TOOL-dPlacedRequest-1`'s offline
queue; ages come from `TOOL-dPlacedRequest-17`'s observer clock and its walk, and the deleted ref's
last record from `TOOL-dPlacedRequest-13`'s feed. `reuse_lookup.py` on the draw's lease and the card's ranking found name-stem neighbours only
(`build`, `claims`); both seams were found by reading. `python tools/codebase-map/
reuse_lookup.py "release a claim with a terminal status and never delete it"` ranked `write_claim`,
`check_claim_writable` and the claim-push lock functions, all in the claim block above, and
`ts_release` (`tools/run-gates/run-gates.sh`, the turnstile, a different lease); no seam fits the
prune or the queued-claim age. One deletion of a `refs/gov` ref exists outside test fixtures:
`remove_red_ref` (`tools/run-gates/post-merge.sh#remove_red_ref`) deletes `refs/gov/bar-red` on the
remote by pushing an empty source under a lease, found by `git grep -n 'PM_PUSH_SRC=""'`; unit 11 makes
it `remove_gov_ref`, the seam S7's prune calls. Scout A's row 6 missed it. `python tools/memory-recall/query.py "when may a released or
terminal lease be pruned and what stops an epoch restart"` returned the brief's unit row, scout A's row 6,
v2's `[chain]` row and the packet's Items; none disagrees with source. A second query on the draw's
hold ranked DEPL-dShippedRelease-47 first, an open ask for a one-commit `--lease draw`, left to its unit.

Recall terms used: tombstone released hand-over epoch prune queued-claim-days last-fetch closed root draw hold renewing beat
