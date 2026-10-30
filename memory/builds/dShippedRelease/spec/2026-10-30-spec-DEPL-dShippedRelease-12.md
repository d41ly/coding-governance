# DEPL-dShippedRelease-12 — the landing queue, the landing turn, and the lander's outcome record

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 6 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0422@c488c531 whole
**Carries:** node:item.deploy.land
**Carries:** node:policy-key.landing.order

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md](../build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md) | research | DEPL-dShippedRelease-11 DEPL-dShippedRelease-27 DEPL-dShippedRelease-30 |
| [2026-10-30-build-DEPL-dShippedRelease-12-deviation-121.md](../build/2026-10-30-build-DEPL-dShippedRelease-12-deviation-121.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

Landing order among verified builds is undefined, the first landing silently stales the others'
verdicts, and no queue exists: the turnstile is a host semaphore `push-main.sh` never takes
(`gap-flow-08`). This unit builds the queue, ordered as `landing.order` says, and one landing turn at
a time across nodes, taken by compare-and-swap. It also closes `gap-deploy-09`'s gated half: exit 0
covers three landings and exit 1 many refusals, so a reader must scrape lines, and the lander now
writes one outcome record by SHA.

## 2. Scope (IN)

- **S1** — The queue, `refs/gov/landing-queue/<branch>`, one ref whose commits are its entries, each
  built by `build_gov_commit` and written by `write_gov_ref` (TOOL-dPlacedRequest-11 S1, S2) with the
  keys `slug`, `tree`, `sha` and `fleet-tag`. `write_queue_entry` appends one when a build first
  reaches `deploy.land`, unless one for that slug and tree is present; a lost compare-and-swap
  re-reads and retries once. Chain position is the only order: no clock is read (§8 F3). Observed by
  AC1.
- **S2** — The order, `derive_landing_queue(root)` in `tools/loop/deploy_items.py`, under
  `read_policy_value("landing.order", root)`, the literal call the reader-coverage arm counts. An
  entry is skipped, keeping its place, while `read_parent_state` (DEPL-dShippedRelease-11) reads its
  slug `landed`, `withdrawn` or `superseded`, while a parent of it is not `landed`, or while its
  build lease reads neither `live` nor `held` in `--claims`. The values are §4 "The values".
  Observed by AC2, AC3 and AC4.
- **S3** — Admission, `check_landing_admitted(build, root)` and `python deploy_items.py admit --slug
  <slug>`, exit 0 admitted, 3 not yet, naming the head and the value. `owner-orders` raises the
  `landing-order` item once per build through `raise_owner_item` (TOOL-dWellOiledMachine-48 S1), a row
  of `OWNER_ITEM_KINDS`, options `land-next` and `hold`, recommended `hold`, and admits only a build
  whose item disposes `land-next`. Observed by AC3 and AC4.
- **S4** — The turn. `write_landing_turn acquire|release` in `tools/push-main.sh` runs `unattended.sh
  --lease acquire run landing <branch>` before `:967` and before `check_claim_push_clear`, outside the
  marker window, and `--lease release run landing <branch>` with no `--as`, a hand-over, in the EXIT
  trap. The trap splits, EXIT alone releasing, since `INT` and `TERM` resume over a push in flight
  (`:214`). A refused acquire exits 5, nothing pushed. Observed by AC5 and AC6.
  **Readers:** by name: `tools/push-main.sh`'s trap at `:217` · by value: `tools/push-main.test.sh`'s
  trap cases, which read the marker's removal and keep it.
- **S5** — The fence (§8 F1). The landing push under `--slug` gains a fourth lease: `--lease fence run
  landing <branch>`, TOOL-dPlacedRequest-15 S2's act generalised past `build`, prints a beat, and the
  atomic push carries `--force-with-lease=<turn ref>:<turn tip>` and `<beat>:<turn ref>` beside
  TOOL-dWellOiledMachine-60 S3's refspecs, so a stale holder's push is rejected whole. Observed by AC7.
- **S6** — The lander's admission. `cmd_land` and the attended landing given `--slug` run
  `check_landing_admitted` first and exit 5 on 3. With `RUN_CLAIMS` off, as the `--lease` verb reports
  it, with no `--slug`, or with no loop kit beside the lander, each prints one `push-main: no landing
  turn — <why>` line and lands as before.
  `tools/push-main.sh`'s header states exit 5. Observed by AC8.
- **S7** — The outcome record (I8). `write_landing_outcome` writes
  `<git common dir>/gov/landing-outcome/<sha>` on every exit past argument parsing: `class`,
  `landing_prior_tip`, `allow`, `bar`, `remote-before` and `remote-after`. The classes are §4 "The
  classes". `landing_prior_tip` is `R` at `:956` or `was` at `:1127`, the tip before the push, since
  `<current default>..HEAD` is empty once pushed. Exit codes keep their meanings. Observed by AC9.
- **S8** — The reader, `read_landing_outcome(sha, root)` in `tools/loop/deploy_items.py` and `python
  deploy_items.py outcome <sha>`. Where the local record is absent, on a second node, it derives from
  the remote: the SHA on the tip reads `landed-ungated`, with `landing_prior_tip` the SHA's first
  parent; neither present reads `nothing-pushed`. Observed by AC10.
- **S9** — The item armed. `run_deploy_land(build, root)` and `python deploy_items.py land --build
  <slug>` enqueue, admit, run the lander with `GOV_PUSH_MAIN_MAX_RETRIES=1` and route by class per §4.
  The `[[stand-in]]` row for `item.deploy.land` leaves `tools/loop/loop.toml`. A `WAIT_KINDS` row
  `landing-turn` (TOOL-dWellOiledMachine-18 S7), `on` the queue ref and the turn ref, wake none,
  outcome `owner-item`, deadline `leases.expiry-hours`. Observed by AC11.
- **S10** — The key. The `landing.order` row (`tools/policy/catalogue.toml:180`) gains `summary` and
  `usage`, values and default untouched, and `policy.py lists --write` drains it from
  `tools/policy/unsummarised-keys.txt`. Observed by AC12.
- **S11** — The docs: `help/loop.md` gains the queue, the turn and the classes. NOT OBSERVED as
  behaviour: prose.

## 3. Non-goals (OUT)

- The landing record, which reads the outcome: DEPL-dShippedRelease-1.
- `deploy.core` and the post-merge bar: DEPL-dShippedRelease-13.
- The notice and the beat in the push: TOOL-dWellOiledMachine-60 and TOOL-dPlacedRequest-15, the two
  refspec sets S5 joins.
- Plan priority. Its field is dRankedPlan's, outside this build's closure (§8 F4).
- The turnstile. It is a host semaphore (`tools/run-gates/run-gates.sh:1467`) and stays untouched.
- `gap-deploy-09`'s adapter half, routing a class to an item: the record is the interface, and each
  route is the reader's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-11` — `read_parent_state`, without which the queue could admit a build whose parent has not landed
- **hands-off** `DEPL-dShippedRelease-1` — `read_landing_outcome` and `landing_prior_tip`, the class and the tip the landing record copies
- **hands-off** `DEPL-dShippedRelease-27` — `landing_prior_tip`, from which `carries` reads its range
- **consumes-from** external — TOOL-dPlacedRequest-1 (`--lease`, `derive_lease_ref`), -11 (`write_gov_ref`, `build_gov_commit`), -15 (the fence, the atomic push), -18 (the cadence segment), TOOL-dWellOiledMachine-18 (`WAIT_KINDS`), -48 (`raise_owner_item`), -60 (the landing push), TOOL-dDeclaredLoop-12 and -13 (the item row, `[[stand-in]]`), each specced and unbuilt at this base, so each is a build-run precondition
- **hands-off** `DEPL-dShippedRelease-51` — `landing_prior_tip`, the recorded base of a landing review (review id 29)
- **hands-off** `DEPL-dShippedRelease-58` — `run_deploy_land`, the program under `--deploy land` (review id 2)
- **hands-off** `DEPL-dShippedRelease-59` — `check_landing_admitted` and `write_queue_entry`, which that unit gives the records rule (review id 3)
- **hands-off** `DEPL-dShippedRelease-70` — `read_landing_outcome`'s no-record branch, which that unit reads by containment (review id 76)
- **hands-off** `DEPL-dShippedRelease-71` — `derive_landing_queue` and `run_deploy_land`, which that unit gives a written exit (review id 77)
- **hands-off** `DEPL-dShippedRelease-72` — `check_landing_admitted`'s exits, which that unit reads deny by default (review id 78)
- **hands-off** `DEPL-dShippedRelease-78` — the turn, the classes and the race fixtures, which the minors batch repairs (review ids 21, 35, 44, 49, 79, 80, 106)

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `cmd_land` is `tools/push-main.sh:952`: tip `:956`, carry check `:962`, marker `:967`, push `:978`,
  landed path `:981-983`, marker removal `:988`; attended push `:1128`, `was` `:1127`.
- `:981` and `:982` exit without passing `:988`, and `:956-957` before it, so only the trap sees every
  path; the trap is `:217` and resumes on `INT` and `TERM` on purpose (`:213-216`).
- `derive_push_failure` is `:262`, returning `refused`, `unreachable`, `unchanged` or `race`.
- `write_claim` refuses while `push-main-active` exists (`tools/unattended/unattended.sh:2415`) and
  the hook clears verdict files on every push (`.githooks/pre-push:494`), hence S4's placement.
- TOOL-dPlacedRequest-1 S6: `acquire` refuses `tombstone` on a foreign terminal lease, so a release
  `--as landed` would stop the next node; a hand-over has no `--as` (pin C11's form).
- A bar runs 16 to 65 minutes (`tools/push-main.sh:231-233`), and `leases.expiry-hours` defaults to
  24.
- The default's input has no home: TOOL-dPlacedRequest-1's `witness` is the progress witness and
  TOOL-dWitnessedBar-4 S6 puts `tree` on `test.exit`'s transition, so no cross-node reader of a
  verified tree exists, which S1's entry supplies.

### The values

| `landing.order` | Order over unskipped entries | Reason printed |
|---|---|---|
| `first-verified` | chain order | none |
| `plan-priority-then-first-verified`, the default | chain order | `landing.order: plan-priority-then-first-verified reads first-verified — no plan priority in this tree`, on every run |
| `owner-orders` | none; a build is admitted only by its `landing-order` item's `land-next` | the item's id |

### The classes

| Class | Test | Exit | `deploy.land`'s route |
|---|---|---|---|
| `landed-gated` | remote-after holds the SHA, remote-before did not, the allow record names it and the bar record is a real bar | 0 | `item.deploy.core` |
| `landed-ungated` | as above, with no such allow record, or a bar record reading a stub | 0 or 4 | `item.deploy.core`, recorded ungated |
| `nothing-pushed` | remote-before held the SHA | 0 | `item.deploy.core`, recorded as held |
| `refused` | nothing reached the remote and a check refused, a race included | 1 | `transition`, to Test |
| `unreachable` | a failed probe, after no refusal | 1 | held, as `stale-remote` is |
| `held` | the queue or the turn stopped it before any push | 5 | `awaiting` |
| `argument` | exit 2, keyed by no SHA, so the verb reads the exit and no record | 2 | an ask on the adapter |

`held` is a seventh class beside I8's six. flow-steps:437 says the queue admits a landing, and an
admission that says no is neither a refusal nor a failure, so routing it to `refused` would re-enter
Test for nothing.

### The turn, in order

```
check_landing_admitted → exit 5 if not
write_landing_turn acquire → exit 5 if refused
loop attempts:
  fence (build lease, mail ref, turn) → beat, chain, turn beat
  touch "$marker"; check_claim_push_clear; clear verdict files
  git push --atomic … <branch refspec> <beat>:<lease> <chain>:<mail> <turn beat>:<turn ref>
  write_landing_outcome
EXIT trap: rm marker; write_landing_turn release
```

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_landing_queue`, `check_landing_admitted`, `read_landing_outcome`, `run_deploy_land` | functions, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at `5d1c82ac` |
| `write_landing_turn`, `write_landing_outcome`, `write_queue_entry` | functions, `tools/push-main.sh` and the module | `sh.function`, OK by `--suggest`; `write_queue_entry` also `py.function` |
| `admit`, `outcome`, `land` | verbs of `deploy_items.py` | none |
| `refs/gov/landing-queue/<branch>` | ref namespace | none |
| `landing-turn`, `landing-order` | wait kind, owner-item kind | none |
| `landing_prior_tip` | record field | none |

The turn's ref needs no name of its own: `derive_lease_ref run landing <branch>`.

### Migration

None for a repository with `RUN_CLAIMS` off, which lands exactly as before, saying so. The outcome
directory is new, untracked, local and pruned with the verdict files.

### Rollout

Live at landing, under the default order. `refs/gov/landing-queue/` joins the namespaces
TOOL-dWellOiledMachine-58's door does not cover, as `refs/gov/waits/` is: it carries no authority.

### Files touched (estimate)

- `tools/push-main.sh`: S4, S5, S6, S7
- `tools/push-main.test.sh`: the arms of §7
- `tools/loop/deploy_items.py`: S1, S2, S3, S8, S9
- `tools/loop/loop.toml`: S9
- `tools/unattended/unattended.sh`: S5's act generalised
- `tools/runtime/waits.py`, `tools/runtime/owner_items.py`: `landing-turn`, `landing-order`
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S10
- `help/loop.md`: S11

### Alternatives rejected

- **The turnstile's FIFO.** Rejected on its own evidence: `tools/run-gates/run-gates.sh:1467` keys on a
  host directory and cannot order two nodes.
- **Ordering by a timestamp on each lease.** It needs a clock two nodes agree on, and
  TOOL-dPlacedRequest-17's declared clock judges deadlines, not order; a chain on one ref needs none.
- **Releasing the turn only inside the atomic push.** A failed landing still needs a separate release,
  so the trap must exist either way, and a release in the push fights TOOL-dWellOiledMachine-60 S4's
  rule that the landing push releases nothing.
- **A short turn bound of this unit's own.** It needs a value no catalogue row owns; the fence makes a
  stale holder harmless, so the bound is only how long the others wait.
- **`tools/deploy/landing_queue.py`, scout B's home.** Pin C1 rejects a new core kit.

## 5. Production-readiness checklist

- security — a queue entry carries a slug, a tree and a sha; it grants nothing. The turn's fence
  means a stale holder cannot land, and `owner-orders` defaults to `hold` on silence.
- perf / scale — one bounded fetch of two refs per admission; the queue's chain grows by one commit a
  landing, read from its tip back to the oldest unlanded entry.
- error / empty / loading states — an empty queue admits its only entry; a failed fence or a lost
  acquire exits 5 and pushes nothing; a local record absent derives from the remote.
- observability — the reason line on every default run; the `held` class names the head; the outcome
  record holds both remote readings.
- risks — a node dying between its push and its trap holds the turn until `leases.expiry-hours`, 24
  hours by default, and every other landing waits; the `landing-turn` wait raises an owner item then.
  Since `take-over` refuses a live lease, nothing shorter is safe to automate, and the fence keeps a
  revived holder from landing.
- testing — fixtures with one bare remote and two clones, per §6.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant two-enqueue` runs, two clones appending at
  once to one bare remote, both entries land on the ref in one chain and a repeat of a slug and tree
  adds none.
  Red when: an append is lost, or an order depends on a timestamp.
- **AC2** — When `--plant queue-first-verified` runs under a committed
  `landing.order = "first-verified"`, the second-queued build exits 3 from `admit` and the first exits 0; after the
  first lands the second exits 0.
  Red when: queue position does not decide admission.
- **AC3** — When the fixture has no policy file, `admit` orders as chain order and prints the line
  `landing.order: plan-priority-then-first-verified reads first-verified — no plan priority in this tree`.
  Red when: the default admits silently, or orders by anything else.
- **AC4** — When `--plant owner-orders-no-order` runs under `landing.order = "owner-orders"`, a queued
  build with no disposition, `admit` exits 3 and exactly one `landing-order` item exists after a second
  run; with `land-next` disposed it exits 0; with `hold` it exits 3.
  Red when: an `owner-orders` landing is admitted with no order, the clause's second seen-red case.
- **AC5** — When `--plant two-nodes-one-turn` runs, two clones running `bash push-main.sh --land --slug`
  at once against one bare remote, exactly one holds the turn and pushes, and the other exits 5 having
  pushed nothing; after the first's exit the turn reads released and the second lands.
  Red when: two nodes hold one turn, the clause's first seen-red case.
- **AC6** — When `--plant turn-released-on-failure` runs, a landing that exits 1 at the carry check, at
  a race, and at exit 4, the turn reads released in each; when `INT` arrives mid-push the turn is not
  released until the process exits.
  Red when: a failed landing keeps the turn, or a signal frees it under a live push.
- **AC7** — When `--plant stale-holder` runs, a turn taken over between one clone's fence and its push,
  that push is rejected whole: neither the branch nor the build lease moves.
  Red when: a stale holder lands.
- **AC8** — When `bash push-main.sh --land --slug fx` runs in a fixture with `RUN_CLAIMS` off, or with
  no loop kit beside it, it prints `no landing turn —` naming why and lands as before.
  Red when: an adopter without the kit is refused, or the skip is silent.
- **AC9** — When a fixture drives each class, `python deploy_items.py outcome <sha>` prints `landed-gated`
  with a real bar, `landed-ungated` with a stub, `nothing-pushed` on a re-push, `refused` on a planted
  red, `unreachable` on a dead remote and `held` on exit 5; `landing_prior_tip` equals the tip read
  before the push on each landed class.
  Red when: two classes share one reading, or the prior tip is the landed SHA.
- **AC10** — When the record is deleted, `outcome <sha>` on a landed SHA prints `landed-ungated` and the
  SHA's first parent.
  Red when: a second node cannot read a landing, or reads it gated with no evidence.
- **AC11** — When `python loop_lib.py --check` and `python loop_table.py check` run, each exits 0 with
  `item.deploy.land` no `[[stand-in]]` row; `python deploy_items.py land --build fx` maps each class to
  the route of §4.
  Red when: the item stays a stand-in, or a class has no route.
- **AC12** — When `python tools/policy/policy.py get landing.order` runs with no policy file it prints
  `plan-priority-then-first-verified`; `grep -c "landing.order" unsummarised-keys.txt` prints 0; and
  `git grep -c 'read_policy_value("landing.order"'` over the loop kit prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.

## 7. Gates

`push-main self-test` · `policy fixtures` · `policy check` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 AC4 AC9 AC10 AC11 · its `--selftest` over a bare remote and two clones, its failing case `owner-orders-no-order` · none
New arm: tools/push-main.test.sh · covers AC5 AC6 AC7 AC8 · two clones against one bare remote, its failing case two holders of one turn · none

## 8. Open questions

- **F1 — How the turn fences and when it is released.** Options: (a) a fourth lease in the atomic push
  fences, the EXIT trap releases on every path; (b) a separate write after the landing and no fence;
  (c) release inside the atomic push. (b) lets a holder taken over land anyway. (c) needs the trap
  regardless and contradicts TOOL-dWellOiledMachine-60 S4. RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 3. widens: none · relaxes: none
- **F2 — How long a dead holder stalls the queue.** Options: (a) `leases.expiry-hours`, the lease's
  own staleness, with an owner item at that deadline; (b) a shorter constant; (c) a new policy key.
  (c) trips veto 2 outside the grant, and (b) is a value no reader can tune, for a wait the fence has
  already made safe. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, flow-steps:437's own bound.
  widens: none · relaxes: none
- **F3 — First verified across nodes.** Options: (a) position in one compare-and-swap chain, an entry
  appended when a build with a current verdict first reaches `deploy.land`; (b) a node-stamped time;
  (c) the declared clock. (b) is exposed to skew, and (c) judges deadlines, not order. A build verified
  earlier and arriving later queues later, which is the one thing (a) does not see. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — The default before dRankedPlan (C7).** Options: (a) `plan-priority-then-first-verified` reads
  `first-verified` with a recorded reason, on every run; (b) add dRankedPlan as a parent; (c) refuse
  the default. (b) changes the closure the packet pins, and (c) stops every landing. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3, pin C7, recorded as deviation 121. widens: none · relaxes: none
- **F5 — Where the outcome lives.** Options: (a) a local record by SHA in the common dir, with the
  remote as a second node's reading; (b) a ref; (c) lines on stdout. (c) is what `gap-deploy-09`
  refuses, and (b) moves every refusal to the remote. RESOLVED (agent, 2026-10-30, delegated): (a),
  rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 12, `gap-flow-08`, `gap-deploy-09`,
  flow-steps:437, :479-482, coordination:194-195, scout B's row, disagreements 8, 10, 11 and §4, and
  the spec brief's I8 and pin C7.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 51, 58, 59, 70, 71, 72, 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `--lease acquire run landing <branch>` (TOOL-dPlacedRequest-1 S5, S1), the
fence act and atomic push (TOOL-dPlacedRequest-15, TOOL-dWellOiledMachine-60), `write_gov_ref`,
`derive_push_failure` and the EXIT trap (`tools/push-main.sh:262`, `:217`), and `WAIT_KINDS`.
`python tools/codebase-map/reuse_lookup.py "order concurrent landings across nodes by compare and
swap"` ranked name-stem hits (`read_landing_commit`, `scan_landing_nodes`, `resolve_compare_base`);
none orders anything. The compare-and-swap shape is `write_claim`
(`tools/unattended/unattended.sh:2396`) and `write_red_ref` (`tools/run-gates/post-merge.sh:275`),
read at source, and `write_gov_ref` absorbs both; no queue exists. Scout B's row holds at source, with these corrections:
pin C1 replaces its `tools/deploy/landing_queue.py`, I8's six classes gain `held`, and its trap note
misses that `INT` and `TERM` resume, so the release must sit on EXIT alone.

Recall terms used: `python tools/memory-recall/query.py "how are landings ordered across nodes through a landing queue and turn" --terms "landing queue landing-turn landing.order compare-and-swap lander outcome class gap-flow-08 gap-deploy-09 first-verified"`
