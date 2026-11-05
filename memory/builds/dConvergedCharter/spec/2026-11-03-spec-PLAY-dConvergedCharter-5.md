# PLAY-dConvergedCharter-5 — adopters migrated onto the ranked charter and the loop by the walk that exists, each read migrated or put to the owner

**Status:** DEFERRED · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 6 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0479@8dc7a199 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md](../build/2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md) | research | PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

Gov's own governance and the shipped product are one body only if every adopter reaches the
converged release: "adopters receive partial stage contracts" (`gap-spine-04`, gap register :315).
The parents ship the content as upgrade steps, and dSafePassage's `update` already walks them
(`cmd_update`, `derive_pending_steps`, `run_step_walk`). This unit drives that walk for each adopter
the register holds and reads each one `migrated` or puts it to the owner, writing no engine code.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`0d1c1dda`: the register reader `read_adopter_rows` and its `registered` flag (DEPL-dShippedRelease-31
S2); `kits.adopters`, `adopter_reading.py read`, the `adopters` record and its `steps-pending` field
(DEPL-dShippedRelease-7 S7, S8); `kits.offer`, `offer.py run` (DEPL-dShippedRelease-16 S4); the
receipt's schema 5 (DEPL-dShippedRelease-25); `read_release_tags` (DEPL-dShippedRelease-3 S1); and
`raise_owner_item` with `OWNER_ITEM_KINDS` (TOOL-dWellOiledMachine-48 S1). The migration's content is
each parent's own `[[upgrade]]` rows: PLAY-dOrderedCharter-31 S4 (adopter rules into the overlay),
TOOL-dBoundRoles-19 (house files into the overlay), TOOL-dTotalRecall-20 (the record-kind aliases) and
dDeclaredLoop's loop kit.

- **S1** — The reading, `derive_migration_state(record, release)` in `tools/govkit/adopter_reading.py`,
  a pure function over one `adopters` record (DEPL-dShippedRelease-7 §4 "Data model"). It returns
  `migrated` when the record's `reading` is `read`, its `release` is `release` or later, and its
  `steps-pending` is empty; `pending <n>: <step ids>` when `steps-pending` holds any id;
  `unregistered` when its `reading` is `unregistered`; and `unverified` otherwise. A record at an
  earlier release with no step pending reads `pending 0: behind <release>`, never `migrated`, since
  the content of the release it lacks is not walked. Observed by AC1.
- **S2** — The verb, `python adopter_reading.py migration --release <tag>`. For each row of
  `read_adopter_rows(root)` it reads the row's record through `read_adopter_reading` (DEPL-dShippedRelease-7
  S7) and prints `migration — <key> · <state>`, then the summary `migration — <m> of <n> rows migrated ·
  <p> pending · <u> unregistered · <v> unverified`. A register with no row prints `migration — not
  graded: the register holds no row` and exits 2, since an empty population is no reading. Any other
  run exits 0: the verb reports, and unit 20's exit check grades. Observed by AC1 and AC3.
- **S3** — The walk, driven and never rebuilt. A row not `migrated` takes its route as
  `deploy.currency` says through `derive_adopter_route` (DEPL-dShippedRelease-7 S8): under
  `push-branches` a row whose `grant` is `branch-push` is offered through `offer.py run <key> --release <tag>`,
  whose `update --offer` walks that adopter's pending steps with `derive_pending_steps`
  (`tools/govkit/upgrade_steps.py:1886`) and `run_step_walk` (`:2036`); every other route records only,
  and the adopter's own `update` (`cmd_update`, `tools/govkit/govkit.py:9381`) walks the same rows when it
  pulls. `adopter_reading.py` gains no step, walk or receipt code. Observed by AC4.
- **S4** — The owner's turn. Each row that S2 reads `pending`, `unregistered` or `unverified` raises one
  owner item through `python owner_items.py raise adopter-unmigrated <build> --key "<key> <release>"`,
  the runtime kit found through `resolve_kit_dir("runtime", "owner_items.py", here)`, with the options its
  state offers: `register` and `wait` for `unregistered`, `offer` and `wait` for `pending`, `retry` and
  `wait` for `unverified`, the first recommended. `adopter-unmigrated` joins `OWNER_ITEM_KINDS`. A second
  run at one release is the mailbox's duplicate (TOOL-dWellOiledMachine-48 S1). An absent runtime kit
  prints `migration — owner item not raised: no runtime kit` and exits as S2 says. Observed by AC2.
- **S5** — The converged release, the one value every reading compares: the first `gov/v*` tag, in
  `read_release_tags` order, whose commit contains this build's landing merge on the default branch.
  Before such a tag exists the verb prints `migration — not graded: no release holds the converged
  commit` and exits 2. Observed by AC3.
- **S6** — The docs: `help/upgrade-steps.md` gains how an adopter is migrated (register, then the offer or its
  own `update`) and what `migration` prints; `WIRE-INTO-PROJECT.md` names the verb where an adopter's
  update is described. NOT OBSERVED by a criterion: prose, graded by the `docs` leg at the close.

## 3. Non-goals (OUT)

- Registering an adopter. `remote`, `branch` and `grant` are facts of each adopter that no record in
  this tree holds, and `govkit.py register` (DEPL-dShippedRelease-31 S3) is the owner's verb; S4 puts
  each unregistered row to the owner.
- Any upgrade step. Each parent declares its own; this unit adds none and edits none, a landed row
  being frozen.
- The exit check that grades every adopter at the converged release: unit 20's, which reads S1.
- A new walk, a new offer mode or a receipt field: dSafePassage and dShippedRelease own them.
- Running a step in an adopter's tree from gov's cadence beyond what `kits.offer` already runs.

### Edges

- **hands-off** `PLAY-dConvergedCharter-20` — `steps-pending`, read through `derive_migration_state`'s states, which the widened exit check grades for every registered adopter, and S2's `migration` verb with its one row walk, which that unit's exit check extends with `--grade` rather than walking the register a second time
- **consumes-from** external — DEPL-dShippedRelease-31 (`read_adopter_rows`, `registered`), -7 (`adopter_reading.py read`, `steps-pending`, `derive_adopter_route`), -16 (`kits.offer`), -25 (schema 5) and -3 (`read_release_tags`), and TOOL-dWellOiledMachine-48 (`raise_owner_item`), each specced and unbuilt at base `0d1c1dda`
- **consumes-from** external — the migration content: PLAY-dOrderedCharter-31 S4, TOOL-dBoundRoles-19, TOOL-dTotalRecall-20 and dDeclaredLoop's loop kit, each a parent's own `[[upgrade]]` rows

## 4. Design

### Evidence

Read at `d8a12f04`; no product file differs from base `0d1c1dda`.

- `tools/govkit/adopters.toml:16-25` holds three rows with no `remote`, `branch` or `grant`, one with
  no `key`; under DEPL-dShippedRelease-31 S2 none is `registered`, so at landing every row reads
  `unregistered` until the owner runs `register` (scout D row 5).
- `derive_pending_steps` (`tools/govkit/upgrade_steps.py:1886`) is every row of the target commit's
  tree minus the ids the receipt records `applied`; `run_step_walk` (`:2036`) walks them. Both are
  dSafePassage's and CLOSED.
- `tools/govkit/adopter_reading.py` does not exist at base; DEPL-dShippedRelease-7 S7 creates it,
  and this unit adds one function and one verb to it.

### The states

| `reading` | `release` | `steps-pending` | State |
|---|---|---|---|
| `read` | the converged release or later | empty | `migrated` |
| `read` | any | one or more ids | `pending <n>: <ids>` |
| `read` | earlier | empty | `pending 0: behind <release>` |
| `unregistered` | — | — | `unregistered` |
| `unverified`, or no record | — | — | `unverified` |

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_migration_state` | function, `tools/govkit/adopter_reading.py` | `py.function`, OK by `--suggest` |
| `migration` | verb of `adopter_reading.py` | none |
| `adopter-unmigrated` | member of `OWNER_ITEM_KINDS` | none |
| `migration-done`, `migration-pending`, `migration-behind`, `migration-unregistered`, `migration-empty` | `--fixture --plant` cases | none |

### Migration

None: the verb reads records and raises items. An adopter migrates when its update walks the
parents' rows, which is today's `update`.

### Rollout

Live at landing, gov-side only: `tools/govkit/` never ships. The first run lands when the converged
release is cut, and every row reads `unregistered` until the owner registers it.

### Files touched (estimate)

- `tools/govkit/adopter_reading.py`: S1, S2, S3, S4, S5, the fixture plants
- `tools/govkit/usage.toml`: one `[[usage]]` row for the `migration` verb
- `tools/runtime/owner_items.py`: `adopter-unmigrated` in `OWNER_ITEM_KINDS`
- `help/upgrade-steps.md`, `WIRE-INTO-PROJECT.md`: S6

### Alternatives rejected

- **A migration walker of its own.** The clause says "the walk that exists", and `update --offer`
  already runs every pending step a row's grant admits; a second walker is the second answer
  `[one-fact]` refuses.
- **Reading `migrated` from the adopter's `steps_unapplied`.** That count is the adopter's own
  (DEPL-dShippedRelease-7 S6) and no remote read reaches it; `steps-pending` is gov's figure over the
  committed receipt, the one a gov-side reading can make.
- **A migrated adopter as one at gov's tip.** An adopter installs from release tags under
  `install.from: release-tag`, so a commit no tag names is one no adopter can reach.

## 5. Production-readiness checklist

- security — the verb reads committed receipts through `load_committed_receipt` under an emptied
  environment (DEPL-dShippedRelease-7 §4) and pushes only through a row's own `branch-push` grant; it
  holds no credential and prints no remote's userinfo.
- perf / scale — one bounded remote read per registered row, three rows at base.
- error / empty / loading states — an empty register and a missing converged release each exit 2 as
  not graded; an unreadable remote reads `unverified` and is put to the owner.
- observability — one line per row and one summary line; each owner item names the key and release.
- risks — every row reads `unregistered` until the owner registers it, so the clause's migration
  completes only on the owner's act; S4 puts it to the owner rather than reading the empty set green.
- testing — the plants of §6 over a local register and a stub runtime kit.
- migration — none, §4.
- user docs — `help/upgrade-steps.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python adopter_reading.py --fixture --plant migration-pending` runs, a registered row
  whose record holds one pending step id prints `migration — <key> · pending 1: <id>` and no `migrated`
  line; under `--plant migration-done` the same row with none pending prints `migrated`, and under
  `--plant migration-behind` a row at an earlier release prints `pending 0: behind`.
  Red when: the planted adopter with a step pending reads as migrated.
- **AC2** — When `--plant migration-unregistered` runs over a register whose one row has no `remote`,
  the row prints `unregistered` and the stub runtime kit records one `adopter-unmigrated` raise keyed
  `<key> <release>` with options `register` and `wait`; a second run records no new raise.
  Red when: an unregistered row is skipped silently, or raised twice.
- **AC3** — When `--plant migration-empty` runs over an empty register, and when the verb runs with no
  tag holding the converged commit, each exits 2 printing `not graded`.
  Red when: an empty population prints a summary of zero rows and exits 0.
- **AC4** — When a registered row under a planted `.governance/policy.toml` setting
  `deploy.currency = "push-branches"` and holding `grant = "branch-push"` reads `pending`, the verb's
  route calls `offer.py run <key> --release <tag>` once, which a stub offer records; under
  `deploy.currency = "pull-and-watch"` it calls none.
  Red when: the verb walks a step itself, or offers a row whose grant is `read`.
- **AC5** — When `govkit.py update --to <release> --write` runs over a scratch adopter installed from
  the `release-0` fixture, and `migration` then reads it through a local register row, it prints
  `migrated`.
  Red when: a parent's step is left pending after the walk, so the release's content never reached it.
  cost: a full `update` walk, minutes.
  fixture: `tools/govkit/fixtures/release-0/` and a local bare repository under `%TEMP%/<short-name>`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `upgrade-walk` · `docs` · `recall floor arms` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · `adopter_reading.py --fixture` under each migration plant, its failing case a pending row read migrated · none

## 8. Open questions

- **F1 — What the unit does with a row the owner has not registered.** All three rows at base are
  unregistered, and the clause migrates adopters. Options: (a) read it `unregistered` and raise one owner
  item naming `register`; (b) leave it out of the reading, so the population is the registered rows
  alone; (c) register it from what the tree holds. (b) reads zero rows as done, the empty population
  `[gate]` refuses, and (c) needs a remote, branch and grant no record holds, a write surface the
  unit's tier does not price. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — One owner item kind or one per state.** Options: (a) one kind, `adopter-unmigrated`, its
  options by state; (b) `adopter-unregistered` and `adopter-pending` apart. One adopter can move
  between states at one release, and (b) would then hold two open items for one question.
  RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What "the converged commit" names for an adopter.** Options: (a) the first release tag whose
  commit holds this build's landing; (b) the landing commit itself. Under the default
  `install.from: release-tag` an adopter cannot install a commit no tag names (DEPL-dShippedRelease-25
  S3), so (b) is a state no adopter can reach. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 5, `gap-spine-04`, scout D's row for 0479
  and its disagreement 2, and the spec brief's I7.
- rev-2 · 2026-11-04 · §3 · the hands-off edge to PLAY-dConvergedCharter-20 names S2's `migration` walk,
  which that unit's S5 extends with `--grade`, mirroring the consumes-from edge PLAY-dConvergedCharter-20
  rev-5 wrote when it folded `2026-11-04-review-PLAY-dConvergedCharter-11-spec-audit-round1` finding 24;
  this unit's S2 and its exit codes are unchanged.

## 10. Reuse audit

The seams driven are `cmd_update` (`tools/govkit/govkit.py:9381`), `derive_pending_steps`
(`tools/govkit/upgrade_steps.py:1886`) and `run_step_walk` (`:2036`), through DEPL-dShippedRelease-16's
`update --offer`; the seam extended is DEPL-dShippedRelease-7's `adopter_reading.py`, whose record
already carries `steps-pending`. `python tools/codebase-map/reuse_lookup.py "report every adopter migrated
with no upgrade step pending"` ranked `read_steps`, `read_step_states`, `run_step_walk`,
`run_step_isolated` and `derive_reverse_steps`, each the walk this unit drives and none a reading of an
adopter; no seam at HEAD reads an adopter, since `adopters.toml` is a name ban (scout D row 5). Scout D's
row holds at HEAD; its disagreement 2 (DEPL-dShippedRelease-31's stale line citations) does not touch a
seam this unit cites.

Recall terms used: `python tools/memory-recall/query.py "how are adopters migrated by the update walk and read as having no step pending" --terms "adopters register registered steps-pending update walk derive_pending_steps kits.offer receipt migration"`
