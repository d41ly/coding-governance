# DEPL-dShippedRelease-4 — the deploy engine: `deploy.current` to `deploy.close`, `deploy.unlease` and the mailbox it closes

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 10 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0415@032149c3 whole
**Carries:** node:item.deploy.current
**Carries:** node:item.deploy.mandate
**Carries:** node:item.deploy.notify
**Carries:** node:item.deploy.snapshot
**Carries:** node:item.deploy.unlease
**Carries:** node:item.deploy.close
**Carries:** node:record-kind.comparison

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-5 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-4-deviation-41.md](../build/2026-10-30-build-DEPL-dShippedRelease-4-deviation-41.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-4-deviation-42.md](../build/2026-10-30-build-DEPL-dShippedRelease-4-deviation-42.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

A build's Deploy step today ends at the push: `--close` runs before it and `--landed` writes a
terminal claim after it, so nothing runs on the landed tree, the lease goes terminal before the work
is done, and nothing closes a mailbox. This unit builds the core Deploy engine: the items around the
landing, `deploy.unlease` closing each of a build's leases with a terminal tombstone and never
deleting it, the mailbox copied into the build folder before its ref is pruned, and `deploy.close`
recording the transition. "The deploy engine" here is the core `deploy.*` items only: v1's promotion
engine became DEPL-dShippedRelease-6 and -15 (scout A disagreement 15, fork 9).

## 2. Scope (IN)

- **S1** — The walk, `run_deploy_items(slug, sha, root, before, after)` in `tools/loop/deploy_items.py`
  (pin C1), reached as `unattended.sh --deploy run <slug> [<sha>] [--to-land]`. Its order is derived:
  `read_items(step="step.deploy")` through `order_by_needs` (TOOL-dDeclaredLoop-12), never typed here.
  `--to-land` walks up to, and not through, `item.deploy.land`; with no flag it walks from the item
  after `item.deploy.land` to `item.deploy.close`. An item on a `[[stand-in]]` row prints `stand-in
  <owner>` and the walk goes on. Each item runs through its own `--deploy <item>` verb; every item is
  idempotent, so a re-run or a second node's run resumes by re-running. The first non-zero exit stops
  the walk with that exit, 3 meaning held and not failed. `<sha>` defaults to `read_landing_commit`
  (`tools/unattended/lib-unattended.sh:1688`). Observed by AC1.
- **S2** — `deploy.current`, `unattended.sh --deploy current <slug>` over `run_deploy_current`. It reads
  `read_policy_value("verdict.tree", root)`. Under `prepared-merge` the subject is HEAD and the verdict
  stands when HEAD's first parent is the tip the remote advertises and `python verdict_backends.py read
  --sha <subject>` answers `GREEN` for that tree. Under `build-tip` the subject is the prepared merge's
  second parent and the tip is not compared. It writes a `comparison` record through S3 and exits 0
  for `current`, 1 for `stale`, whose route is row B17, back to Test. Observed by AC2.
- **S3** — The `comparison` record: one commit at `refs/gov/comparison/<sha>` by `build_gov_commit` and
  `write_gov_ref`, header `gov-comparison <sha>`, keys `sha`, `tree`, `verdict-tree`, `tip`, `mode` and
  `result`; a ref, because a tracked record would change the tree it compares (§8 F1). Its row in
  `tools/memory-tree/record-kinds.toml` is §4 "The kind row". Observed by AC2, AC12.
- **S4** — `deploy.mandate`, `unattended.sh --deploy mandate <slug>` over `run_deploy_mandate`. It reads
  `read_policy_value("autonomy", root)`. Under `plan-only` it runs `check_authorization`
  (`tools/unattended/unattended.sh:3927`), today's stand-in for `plan.exit`'s ratification while
  `item.plan.exit` sits on a stand-in row; a patch or repeat build answers through
  `check_patch_ratified` (TOOL-dPlacedRequest-21 S6). Under `three-gates` and `every-stage` it requires
  `check_owner_disposition` for the gate before `item.deploy.mandate` (TOOL-dDeclaredLoop-19 S6).
  Exit 0 with the witness printed, 1 naming what is missing. Observed by AC3.
- **S5** — `deploy.notify`, `unattended.sh --deploy notify <slug> <sha>` over `run_deploy_notify`. The
  `landed` notice rides the landing push (TOOL-dWellOiledMachine-60 S2, S3), so this is a held-id
  check: for each dependent it finds a `landed` message whose subject is `landing <slug>` and body
  `<sha>`, through `read_mailbox`, on any of the build's mail refs. All found prints `notify — <sha8> ·
  already posted`; a missing one is built by `--mail landing <slug> <sha>` and pushed by
  `write_gov_ref`, which an attended landing and a `notice — none` push need. Observed by AC4.
- **S6** — `deploy.snapshot`, `unattended.sh --deploy snapshot <slug>` over `run_deploy_snapshot`: it
  runs TOOL-dPlacedRequest-2 S5's `--card --follow` at the terminal state in the session's own tree; an
  equal snapshot is a no-op and a card store with no `build-folder` selected writes none. The commit
  that writer makes rides S7. Observed by AC5.
- **S7** — The records landing (pin C3), `run_records_landing <slug> <sha>` in `unattended.sh`. It
  stages the mailbox copies and, where S11 finds the close due, the transition's folder copy, commits
  one records-only commit `records(<slug>): landing records for <sha8>` with a `Pass: none` trailer,
  and lands it by `$LANDER --prepare --slug <slug>` and `$LANDER --land --slug <slug>`, so it is gated
  as any landing. Nothing bypasses the lander. A landing's records commit runs no `deploy.*` item, so
  it raises no second landing record. Nothing to carry prints `records — nothing to land` and exits 0.
  The tree must be clean and on a branch holding `<sha>`, else exit 2 naming which. Observed by AC5, AC7.
- **S8** — The closer, `run_unlease <slug> --as landed|withdrawn` in `unattended.sh`, shared interface
  I10, the one body under `life.unlease` and `deploy.unlease`: TOOL-dWellOiledMachine-58 S9's writer
  check, unit leases, mailbox and build lease, moved rather than copied. A lease already terminal
  counts as done and a missing mail ref counts as done. Under `--as landed` each unit and build lease
  is written `landed` through `--lease release … --as landed`; the mailbox's `mailbox-message` records
  are written first, an undisposed message titled `<id> — undisposed at close`, and every ref is pruned
  only after S7 and only when `git cat-file -e <advertised tip>:<copy>` finds each copy on the default
  branch, exit 3 otherwise. Then the build lease: the mailbox closes before the tombstone (pin C5,
  deviation 41), because TOOL-dWellOiledMachine-58 S5 needs a live lease to prune. Under `--as
  withdrawn` the order and the copies are that spec's, with no records landing. Observed by AC6, AC7.
- **S9** — `deploy.unlease`, `unattended.sh --deploy unlease <slug> <sha>`, every write under
  `GOV_DOOR_VERB=deploy.unlease`, runs `run_unlease <slug> --as landed`. `DOOR_CLOSING_VERBS` in
  `tools/memory-tree/gov_record.py` gains `deploy.unlease`, as TOOL-dWellOiledMachine-58 S6 hands this
  build. The tombstone stays: `--lease prune` refuses a build or unit lease
  (TOOL-dPlacedRequest-16 S7), and a queued claim replayed against it is refused `tombstone`
  (TOOL-dPlacedRequest-16 S3, S6). Observed by AC6, AC8.
- **S10** — `--landed`'s terminal write ends (pin C4). In `verb_landed` the in-place arm's status write
  (`tools/unattended/unattended.sh:6381-6384`) and the primary arm's (`:6632-6635`) write no status:
  the lease stays live until `deploy.unlease`, so a killed supervisor's build can be taken over and
  closed. The verb prints `next: --deploy run <slug>` instead. `--settle`'s write (`:7199`) is
  unchanged, an attended hand-off running no walk. The reader `read_claims` and `--claims` need no
  change: `live` ages to `stale` as any live lease does, which is the route a take-over takes. Observed
  by AC9.
- **S11** — `deploy.close`, `unattended.sh --deploy close <slug> <sha>` over `run_deploy_close`, I10. It
  runs three terms, each one function in `deploy_items.py`: `check_unleased` (`--claims` reads the
  build lease and each unit lease terminal, and no ref under `refs/gov/mail/<slug>/` remains),
  `check_released`, and `check_core_settled`, which runs `read_core_settlement`
  (DEPL-dShippedRelease-13 S9) and adds no rule. All holding, it records the transition by `python
  loop_transition.py record --build <slug> --from deploying --item item.deploy.close --outcome pass
  --witness <sha>`, row T10, the record minting under the build's claim ref (`layer-memory.md:325-326`)
  and landing through S7 unless its copy is already on the default branch. `[--release-outcome <o>]`
  adds that outcome as a `--field`, the "release outcome" flow-steps:446 puts on the transition. Any
  term failing prints `close — <slug> · held · <term> · <why>`, exit 3, and records nothing.
  `check_released` reads the landing record's `closes`: `at-landing` and `at-landing-maintain-owns`
  hold; `after-release-verifies` reads held, printing the value, until DEPL-dShippedRelease-5 S7 gives
  the term that value's arm over `read_hold_answers`. Observed by AC10.
- **S12** — `--close` and `deploy.close` stay two acts (scout A disagreement 2). `--close` grades the
  Definition of Done on the graded merge before the push, and commits LANDING. `deploy.close` runs
  after the push and `deploy.unlease` and records the transition. Neither calls the other, and neither
  name is spelled for the other in any message. `check_close_due(slug, sha)` is S11's second and third
  terms alone, which S7 asks to decide whether the transition rides the one commit (§8 F3). Observed
  by AC10.
- **S13** — The red landing's wait. S11 held on `check_core_settled` with `open · filed` declares
  `python waits.py declare core-settled <sha> <slug> --on refs/gov/core-verdict/ --seconds <n>
  --outcome owner-item`, `<n>` the `flow.wait-ceiling` hours less the time since the landing record; a
  `core-settled` row joins `WAIT_KINDS`, its `wake` `--deploy close <slug> <sha>`, run under
  TOOL-dWellOiledMachine-18 S4's cadence lease because the build holds no lease by then. A wake with
  the term still open re-declares with the remaining seconds. Past the deadline the sweep raises the
  owner item: an exception under `core.exceptions`, or the budget raised. Observed by AC11.
- **S14** — The items armed: `item.deploy.current`, `.mandate`, `.notify`, `.snapshot`, `.unlease` and
  `.close` take their witnesses, and their `[[stand-in]]` rows leave `tools/loop/loop.toml`, including
  the `item.deploy.close` row TOOL-dDeclaredLoop-13's table names. The core Deploy items each gain an
  `[[adapter]]` row at `point.command-adapters` in `tools/runtime/points.toml`, `class = "idempotent"`,
  `run` their `--deploy` verb, so the supervisor runs them through TOOL-dWellOiledMachine-6 S8: this
  unit's six and `deploy.record`, `deploy.distill` and `deploy.core`. Observed by AC12.
- **S15** — The docs: `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, states the order after the last `--prepare` (`--deploy run <slug>
  --to-land`, `--close`, `--land`, `--landed`, `--deploy run <slug>`) and the difference of S12;
  `tools/unattended/STOPS.template.md`, rendered to `memory/guides/UNATTENDED-STOPS.md`, states the
  lease's life past `--landed`; `help/deploy.md` states the items. `KIT_UNATTENDED_VERSION` moves.
  NOT OBSERVED by a criterion: prose, read by the memory hygiene leg at the close.

**Build-run preconditions**: TOOL-dWellOiledMachine-58 (the door, `--unlease`), -60 (the landing
notice), -18 (`waits.py`), -6 (command adapters), TOOL-dPlacedRequest-1, -11, -16 (the lease verbs and
tombstones), -2 (the card snapshot), -21 (`check_patch_ratified`), KICK-dKeptSession-5 and -39
(`read_mailbox`, `mailbox-message`), TOOL-dDeclaredLoop-3, -12, -13, -19 (the transition writer, item
rows, stand-ins, gates), TOOL-dWitnessedBar-6 (`verdict_backends.py`), DEPL-dShippedRelease-1, -2, -13.

## 3. Non-goals (OUT)

- `deploy.parents` and `deploy.land`: DEPL-dShippedRelease-11 and -12. `deploy.record`, `deploy.distill`,
  `deploy.core`: units 1, 2 and 13, which this unit only calls.
- `deploy.released` and the release arm: DEPL-dShippedRelease-5, whose exit 3 under `whole-close` stops
  the walk before `deploy.snapshot`, and whose S7 gives `check_released` its `after-release-verifies` arm.
- Promotion, adapters and environments: DEPL-dShippedRelease-6 and -15.
- `deploy.recommend`: TOOL-dDeclaredLoop-22. The landing review's term: DEPL-dShippedRelease-14.
- The take-over verb itself, which is TOOL-dPlacedRequest-1's; the killed-supervisor case is observed
  by DEPL-dShippedRelease-5, on this unit's walk.
- Enforcing the walk at the lander. `--land` does not read a comparison record: the walk's order is
  the procedure, and the lander stays as DEPL-dShippedRelease-12 leaves it.
- The `--settle` verb's `landed` write, and the `aborted` writes at `:6770` and `:7620`.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing`, whose `closes` field `check_released` reads, and `set_landing_field`
- **consumes-from** `DEPL-dShippedRelease-13` — `read_core_verdict` and `read_core_settlement`, which `check_core_settled` runs
- **hands-off** `DEPL-dShippedRelease-14` — `run_unlease` and the close terms, to which that unit adds `check_landing_review`
- **hands-off** `DEPL-dShippedRelease-5` — `run_unlease`, the close verb its wake runs, and `check_released`, to which that unit adds the `after-release-verifies` arm
- **consumes-from** external — the parent units §2 lists, each specced and unbuilt at this base
- **hands-off** external — the two asks of §8 F4 and F5, on TOOL-dPlacedRequest-16 and TOOL-dWellOiledMachine-58
- **hands-off** `DEPL-dShippedRelease-56` — `run_deploy_items`, whose stop rule that unit gives one exception (review id 74)
- **hands-off** `DEPL-dShippedRelease-58` — S14's adapter rows and S15's order, which that unit completes (review id 2)
- **hands-off** `DEPL-dShippedRelease-59` — `run_records_landing`, whose exit 5 that unit routes (review id 3)
- **hands-off** `DEPL-dShippedRelease-68` — `run_deploy_close` and the tombstone, past which that unit lands the late copy (review id 73)
- **hands-off** `DEPL-dShippedRelease-69` — `run_unlease` and `check_unleased`, which that unit teaches a carry-forward landing (review id 75)
- **hands-off** `DEPL-dShippedRelease-78` — `deploy.current` and `run_deploy_close`, which the minors batch repairs (review ids 5, 22, 34, 40, 79, 105)

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `--close` commits LANDING on the graded merge (`write_close_commit`, `tools/unattended/unattended.sh:10703-10719`),
  and it says why a landing needs no record of its own: `:6354-6357`. `DOD_CORE` (`:868`) holds
  `keepalive-reaped` and `records-current`, which TOOL-dDeclaredLoop-11 maps to `item.deploy.unlease`
  and `item.deploy.record`; both are graded before the landing they name (`:11615-11619`), so they
  stay `--close`'s and this unit adds no DoD item.
- `--landed` writes `landed` at `:6383` (in-place) and `:6634` (primary). `read_claims` admits four
  statuses (`:2162`).
- `verb_landed`'s in-place arm stages nothing and writes one log line (`:6371`).
- A bar's verdict can be re-read by tree (`gate-verdict/<tree hash>`, TOOL-dWitnessedBar-4). In-place
  `--close` commits on top of the graded merge, so `deploy.current` runs before `--close`, on the
  merge the bar graded. `--to-land` is that order.

### The kind row

```toml
[[record-kind]]
name = "comparison"
tag = "record.comparison"
layer = "layer.flow"
home = "refs/gov/comparison/*"
id-rule = "<compared sha>"
schema = { form = "header", source = "tools/loop/deploy_items.py:COMPARISON_FIELDS", fields = [
  "sha", "tree", "verdict-tree", "tip", "mode", "result"] }
writer = "unattended.sh --deploy current"
readers = []
readers-none = "the route reads the verb's exit; the record is its witness"
lifecycle = "append-only"
check = "deploy items"
```

### The one commit

```
core · record · distill · recommend · [landing review] · notify · [released] · snapshot
  → unlease: mail copies written · close due? transition copy written
             → ONE records commit, landed through the lander
             → copies confirmed on the default branch → refs pruned → unit and build tombstones
  → close: terms graded again; the transition's copy already on the default branch → closed
```

Where the close is not due at that commit, because a release, a red landing or a review holds it, the
transition's copy cannot exist yet, and `deploy.close` lands it alone when its terms hold. That is
the one case of a second records commit, deviation 42.

The transition written before `check_unleased` holds is a real ordering: for the seconds between S7
and the tombstones the default branch says `landed` with the lease live. A kill there leaves a build
a second node finishes by the same walk, every step idempotent, and `deploy.close` re-grades all three
terms on that walk.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_deploy_items`, `run_deploy_current`, `run_deploy_mandate`, `run_deploy_notify`, `run_deploy_snapshot`, `run_deploy_close`, `check_unleased`, `check_released`, `check_core_settled`, `check_close_due` | functions, `deploy_items.py` | `py.function`, each answered OK by `--suggest` at `5d1c82ac` |
| `COMPARISON_FIELDS` | module constant | `py.constant`, screaming |
| `run_unlease`, `run_records_landing` | shell functions, `unattended.sh` | `sh.function`, OK |
| `--deploy run`, `current`, `mandate`, `notify`, `snapshot`, `unlease`, `close` | driver verbs | none |
| `refs/gov/comparison/<sha>` | ref namespace | none |
| `core-settled` | `WAIT_KINDS` member | none |

### Migration

A build landed before this unit has a terminal claim and no record: `--deploy run` on it exits 1 at
`deploy.record`'s `read_landing_outcome`, and no walk owes it. A build in flight at this unit's landing
lands with a live lease and runs the walk, or its operator runs `--lease release build <slug> --as landed`.

### Rollout

Live at landing for `RUN_CLAIMS` on. `RUN_CLAIMS` off keeps `--landed` as today, with no lease to hold
and every `--deploy` write refusing dark, and the walk prints `deploy — dark: RUN_CLAIMS is off`.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1 to S5, S11, S12
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/loop/loop.toml`: S14
- `tools/unattended/unattended.sh`: S1's verb, S6, S7, S8, S9, S10, `KIT_UNATTENDED_VERSION`
- `tools/unattended/unattended.test.sh`: the status arms S10 moves
- `tools/memory-tree/gov_record.py`: `DOOR_CLOSING_VERBS`
- `tools/memory-tree/record-kinds.toml`: the `comparison` row
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`: the generated region
- `tools/runtime/waits.py`: the `core-settled` row
- `tools/runtime/points.toml`: S14's adapter rows
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S15
- `tools/unattended/STOPS.template.md`, rendered to `memory/guides/UNATTENDED-STOPS.md`: S15
- `help/deploy.md`: S15

### Alternatives rejected

- **A second closer beside `life.unlease`.** Rejected by `[reuse]`: two bodies for one sequence, the
  drift being who prunes before whom. Test: TOOL-dWellOiledMachine-58 S9 already holds the sequence.
- **`--landed` releasing the lease as TOOL-dPlacedRequest-16 S2 has it.** Rejected by pin C4 and the
  clause cl-dClosedLoop-0508: a hand-over at `--landed` leaves no holder for the post-landing items.
  Test: the killed-supervisor case, a `released` lease being free to any node with no build to finish.
- **Pruning on a local copy.** Rejected by pin C3: a copy in a worktree that dies is gone with the ref.
  Test: S8's `cat-file` probe of the advertised tip.
- **A comparison record in the build folder.** Rejected: it changes the tree it compares, so
  `deploy.current` would read itself stale. Test: S2's own tree comparison.
- **A typed item order in `deploy_items.py`.** Rejected by `[derive]`: the needs graph is the order.
  Test: `order_by_needs` over the rows TOOL-dDeclaredLoop-12 ships.

## 5. Production-readiness checklist

- security — every lease and mail write goes through the door under `GOV_DOOR_VERB=deploy.unlease`;
  the writer check of S8 refuses a session that does not hold the build lease. The records commit
  carries only `memory/builds/<slug>/` paths and is graded by the hook. Copied mail bodies are records
  that sessions wrote; `mailbox-message` keeps each in one fenced block, read as data.
- perf / scale — one extra landing per build, on the docs path where `GATE_DOC_PATHS` declares it; one
  bounded fetch per item.
- error / empty / loading states — a mailbox with no ref counts as done; a build with no dependents
  has no notice; a held close exits 3, not 1.
- observability — one `<item> —` line per verb; `close — held` names the term.
- risks — a live lease past `--landed` with no walk ages to `stale` and is announced at other slugs'
  `--preflight`; `next:` is what prevents it. The window of §4 "The one commit".
- testing — `deploy_fixture.py` over a bare remote and two clones, with a stub bar.
- migration — §4.
- user docs — `help/deploy.md` and the two guides.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-walk` runs `--deploy run <slug> <sha>` with a
  planted `needs` edge that swaps two items, the printed item order follows the planted graph, an item
  on a planted `[[stand-in]]` row prints `stand-in`, and a stub exit 3 stops the walk with exit 3; a
  re-run from the top reaches the end.
  Red when: the order is typed, or a held item reads as a failure or as done.
- **AC2** — When `python deploy_fixture.py --case engine-current` runs `--deploy current` on a green
  prepared merge, it exits 0 and `refs/gov/comparison/<sha>` reads `result current`; after a planted
  tip move it exits 1 reading `stale`; with `.governance/policy.toml` planted `verdict.tree = "build-tip"`
  the moved tip reads `current` and `mode build-tip`.
  Red when: a verdict for another tree reads current, or `build-tip` still compares the tip.
- **AC3** — When `python deploy_fixture.py --case engine-mandate` runs `--deploy mandate` under each of
  `autonomy` `plan-only`, `three-gates` and `every-stage` planted, `plan-only` exits 0 on a reachable
  authorization and 1 on none; the other two exit 1 with no disposition record and 0 with one.
  Red when: an owner gate is passed by the plan's authorization alone.
- **AC4** — When `python deploy_fixture.py --case engine-notify` runs `--deploy notify` after a landing
  whose push carried the notice, it prints `already posted` and writes no ref; with the notice planted
  absent it posts one, and a second run posts none.
  Red when: a repeated post makes a second message for one SHA.
- **AC5** — When `python deploy_fixture.py --case engine-records` walks a planted build, the default
  branch gains one records-only landing holding the snapshot, the copies and the transition's copy, and
  `git for-each-ref refs/gov/landing` counts one ref; a second walk lands nothing.
  Red when: a records commit raises a landing record, or a copy reaches the tree outside the lander.
- **AC6** — When `python deploy_fixture.py --case engine-mailbox` plants a build unleased with an
  undisposed message, its copy titled `undisposed at close` is on the default branch before the ref
  goes, and with the records landing planted to refuse, `--deploy unlease` exits 3 with the ref still
  on the remote and the build lease still live.
  Red when: the ref is pruned before its marked copy is on the default branch, the clause's second case.
- **AC7** — When `python deploy_fixture.py --case engine-order` records the ref writes of a passing
  `--deploy unlease`, every mail prune precedes the build lease's tombstone, and `--as withdrawn` on a
  second planted build runs no records landing.
  Red when: the tombstone precedes a prune, so the door refuses it.
- **AC8** — When `python deploy_fixture.py --case engine-tombstone` runs `--deploy unlease` and then
  replays a queued claim through `--lease flush`, the replay prints `tombstone`, `--lease acquire build
  <slug>` is refused, `--lease prune` naming the build lease exits 1, and the ref still resolves.
  Red when: a queued claim lands on an unleased build, the clause's first case, or a ref is deleted.
- **AC9** — When `python deploy_fixture.py --case engine-landed` runs `--landed` on a landed run,
  `--claims` reads `live` and not `landed`, and the verb prints `next: --deploy run`; after the planted
  age `--lease take-over build <slug>` on the second clone succeeds and its walk reaches `deploy.close`.
  Red when: `--landed` writes a terminal status, pin C4.
- **AC10** — When `python deploy_fixture.py --case engine-close` runs `--deploy close` with each of
  `check_unleased`, `check_released` and `check_core_settled` planted false in turn, it exits 3 naming
  that term and writes no transition; with all true it records row T10; a `--close` run in the same
  fixture writes no `deploy.close` transition; a planted red with no filing and a planted filed red not
  yet green each exit 3 naming `check_core_settled`.
  Red when: a build closes past a false term, or the two acts share a name in a message.
- **AC11** — When `python deploy_fixture.py --case engine-red-wait` holds the close on a filed red,
  `python waits.py sweep` wakes it on a planted `core-verdict` ref and re-declares with fewer seconds;
  past the deadline one owner item is raised.
  Red when: a spurious wake restarts the clock, or the wait raises twice.
- **AC12** — When `python supervise.py --check-adapters` and `python record_kinds.py --check` run at the
  pass, each exits 0 with the nine `deploy.*` adapter rows and a `comparison` row; `grep -c
  'item = "item.deploy.' loop.toml` counts no row for this unit's six items.
  Red when: a command item has no adapter, so the supervisor cannot run it.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `unattended kit gate` · `push-main self-test` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit version markers` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC10 AC11 · the `engine-` cases, the failing case `engine-mailbox` staged against `run_unlease` with its copy probe removed · none

New arm: tools/unattended/unattended.test.sh · covers AC9 · the status read after `--landed` on both lander modes, staged against the base driver, which writes `landed` · none

## 8. Open questions

- **F1 — Where does the `comparison` record live?** Options: (a) a ref keyed by the compared SHA; (b) a
  build-folder record, committed; (c) a field on the landing record. (b) changes the tree it compares,
  and (c) does not exist yet, since a stale comparison never lands. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3. widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the ref namespace
  `refs/gov/comparison/` and the `--deploy` verbs of this unit's items
- **F2 — What grades the records that reach the tree after a landing?** Options: (a) one records-only
  commit through the lander, gated as any landing; (b) a direct push; (c) no tree copy. (b) is a
  bypass and (c) fails TOOL-dWellOiledMachine-58 S5, which needs each copy under the build folder.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, pin C3, scout A's fork 2. widens: none · relaxes: none
- **F3 — Can the transition's folder copy always ride that one commit?** Under `after-release-verifies`
  with `close-only`, on a red landing and under an open review, the close follows `deploy.unlease` by
  days, so no transition exists at the commit. Options: (a) the copy rides the commit when S12's
  `check_close_due` holds, and lands alone otherwise; (b) two commits always; (c) hold the unlease until
  the close, against `flow-steps.md:88-89`'s "the build stays open after `deploy.unlease`". Pin C3
  states one commit and is true of (a)'s default path alone, so a deviation names the rest. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3, deviation 42. widens: none · relaxes: none
- **F4 — Does the lease stay live past `--landed`?** Options: (a) yes, `--landed` writes no status, pin
  C4; (b) TOOL-dPlacedRequest-16 S2's `released`. (b) contradicts cl-dClosedLoop-0508. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 1. Ask for dPlacedRequest, filed by the main loop:
  TOOL-dPlacedRequest-16 S2 leaves `tools/unattended/unattended.sh:6383` and `:6634` to dShippedRelease,
  whose build lease goes terminal at `deploy.unlease`; accept S2 no longer lists those two lines and a
  fixture run's lease reads `live` after `--landed`. widens: none · relaxes: none
- **F5 — How does `life.unlease` share a body?** TOOL-dWellOiledMachine-58 S9 writes `withdrawn`, exits
  early on a `landed` tombstone with a message that goes stale here, and its acceptance at `:288`
  asserts `not-closing-verb` for this name (scout A disagreement 8). Options: (a) move the body to
  `run_unlease --as`, the early exit reading `already closed`; (b) a second body. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3, `[reuse]`. Ask for dWellOiledMachine, filed by the main loop:
  TOOL-dWellOiledMachine-58 S9 and its acceptance are read through `run_unlease --as withdrawn`, and
  the `deploy.unlease` case of `not-closing-verb` moves to a name still outside the tuple; accept
  `door_fixture.py` green at the landing of DEPL-dShippedRelease-4. widens: none · relaxes: none
- **F6 — In which order do the clause's two acts run?** Clause wording puts tombstones first; S5 of
  TOOL-dWellOiledMachine-58 needs a live lease to prune. Options: (a) mailbox, then tombstone; (b) a
  door exception. (b) widens the door. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, pin C5,
  deviation 41. widens: none · relaxes: none
- **F7 — How far does "the deploy engine" reach?** Options: (a) the core `deploy.*` items; (b) v1's
  promotion engine as well. v2 split that into two later clauses. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 1, cl-dClosedLoop-0416 and -0425. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 4, flow-steps:84-90 and :434-446, pins C1,
  C3, C4 and C5, shared interface I10, and scout A's row and disagreements 1, 2, 5, 7, 8, 14 and 15.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 56, 58, 59, 68, 69, 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are TOOL-dWellOiledMachine-58 S9's closer (moved to `run_unlease`), `verb_landed`
(`tools/unattended/unattended.sh:6316`), `check_authorization` (`:3927`) and `write_close_commit`'s
commit shape (`:10703`). `python tools/codebase-map/reuse_lookup.py "close a build's leases with
tombstones and copy its mailbox into the build folder before pruning"` returned name-stem neighbours
(`build`, `build_commit`, `before`), so the shipped seams are the ones scout A read, and every closer
is a parent spec. Scout A's row holds at `5d1c82ac`, with three corrections: the in-place write's call
sits at `:6383` inside `:6381-6384`, a second `landed` write sits at `:6634`, and `read_claims` admits
its status set at `:2162`. The recall probe's hits were this build's scout record and
TOOL-dPlacedRequest-16's scout; neither disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a build's lease closed after landing and what happens to its mailbox" --terms "tombstone lease unlease mailbox prune closing verbs landed terminal status take-over claim"`
