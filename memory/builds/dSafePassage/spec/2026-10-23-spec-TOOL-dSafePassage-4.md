# TOOL-dSafePassage-4 — down steps in reverse, and the recorded rollback that lifts the downgrade refusal

**Status:** DEFERRED · rev-5 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0021@ad0db541 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-4-deviation-130.md](../build/2026-10-23-build-TOOL-dSafePassage-4-deviation-130.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-4-deviation-131.md](../build/2026-10-23-build-TOOL-dSafePassage-4-deviation-131.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-4-deviation-132.md](../build/2026-10-23-build-TOOL-dSafePassage-4-deviation-132.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-4-deviation-133.md](../build/2026-10-23-build-TOOL-dSafePassage-4-deviation-133.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

There is no way back across versions today. `update` refuses any `--to` that is not a descendant of
the receipt's commit, "A DOWNGRADE IS NOT AN UPDATE" (`tools/govkit/govkit.py:7463-7482`), and the
only rollback that exists runs inside one run, per kit, on a green-to-red verify
(`tools/govkit/govkit.py:11509` onward), with no reach into anything an upgrade step changed. This
unit closes `gap-deploy-17`. Down steps run in reverse, each tolerating the partial state a killed up
left, under a recorded rollback the operator asks for by name, `update --rollback`, which lifts the
downgrade refusal for a rollback only and is never run on its own after a failure.

## 2. Scope (IN)

- **S1** — The flag. `parse_args` (`tools/govkit/govkit.py:13632-13727`) gains `--rollback`, a bool
  passed to `cmd_update` and `_cmd_update`, and USAGE's `update` line
  (`tools/govkit/govkit.py:13596`) gains `[--rollback]` with one sentence on what it does. It does
  nothing without `--to`, and `--rollback` with `--kits` is a refusal, since a rollback moves the
  whole receipt. Observed by AC6.
- **S2** — The vintage. `check_rollback_vintage(root, base_commit, to_commit, reverse_rows)` sits in
  `govkit.py` beside `demand_forward_vintage`, and under `--rollback` it is called in that
  function's place (`tools/govkit/govkit.py:9231`). It refuses a receipt with no `gov_commit`, a
  `--to` that is not an ancestor of `gov_commit`, and an empty reverse set when `--to` equals
  `gov_commit`. `demand_published_vintage` still runs. Without `--rollback`, `demand_forward_vintage`
  refuses as today, its remedy naming `update --rollback --to <rev>` in place of "re-install
  deliberately". Observed by AC6.
- **S3** — The reverse set. `derive_reverse_steps(gov_root, receipt, to_commit)` in
  `tools/govkit/upgrade_steps.py` reads the rows with TOOL-dSafePassage-1's `read_steps` at gov's
  `HEAD` and returns every row whose introducing commit is not an ancestor of `to_commit`, an
  `unlanded` row included, and which the receipt's `steps` list records as `applied` or `failed`, or
  does not record at all. The order is the reverse of the order `read_steps` returns, which is the
  walk order, so `govkit/receipt-schema-4`, the steps file's first row, is downed last, after every
  other applied step, as its own down requires (TOOL-dSafePassage-3). A receipt row whose id
  `read_steps` does not return is named and refused before any down, since its down argv is no
  longer declared. Observed by AC1 and AC4.
- **S4** — The reverse walk. `run_reverse_walk(gov_root, target, receipt_path, receipt, rows)` takes
  each row in that order, all spawns through `run_step_isolated` (TOOL-dSafePassage-7):
  1. a row recorded `rolled-back`, or recorded nowhere, runs its `witness` first, and one whose
     witness does not hold is skipped, since nothing of it is applied;
  2. an `attended` verdict stops the reverse walk with the order TOOL-dSafePassage-2's
     `write_attended_order` writes, naming the `down` argv;
  3. the row's state is kept and its `failure` set to `down interrupted: started <utc>, no exit
     recorded`, persisted before the spawn;
  4. it runs the `down`; a non-zero exit sets `failure` to `down exit <rc>: <the last stderr line>`
     and stops;
  5. it runs the `witness`; exit 0 sets `failure` to `witness still holds after down` and stops;
     anything else stages the down's writes and records `rolled-back`, with no `failure`. The writes
     are the paths the step's before-image listed, read before the down's spawn because the down
     takes the image away, and the image's own path, each staged as TOOL-dSafePassage-2's S11
     stages an up's, with its staging-journal line first.
  A row recorded `failed`, the state a failed or killed up leaves, runs its `down` like an
  `applied` one: the down is what tolerates the partial state. Progress goes through the
  writer `set_step_state` TOOL-dSafePassage-3 ships and the hand-off of TOOL-dSafePassage-2's S3, so a
  down that rewrites the receipt, as `govkit/receipt-schema-4`'s down does, is re-read after its
  spawn. Observed by AC1, AC2, AC3 and AC4.
- **S5** — The rollback inside `update`. Under `--rollback` and no `--write`, the preview block
  (`tools/govkit/govkit.py:10223-10233`) prints each reverse row as `would roll back` and spawns
  nothing. Under `--rollback --write`, the reverse walk runs after that block and before the
  pre-write snapshot (`tools/govkit/govkit.py:10296`), so every down meets the tree its up left and
  no file row moves before the downs. A stopped reverse walk ends the run there, with its findings,
  `gov_commit` unmoved. A complete one hands over to the write loop, which moves the file rows to
  `--to` as it moves them for any `--to`; TOOL-dSafePassage-2's forward walk does not run. On a clean
  run the stamp sets `gov_commit` to `--to` and keeps the `schema` the downs left: the re-stamp at
  `tools/govkit/govkit.py:12407` never raises a receipt by itself (TOOL-dSafePassage-3's S5), and
  under `--rollback` it never raises one a down lowered. Observed by AC5.
- **S6** — The record. `write_rollback_record` writes
  `.governance/outbox/update-reverted-<from8>-<to8>.md` when a `--rollback --write` run begins,
  naming `from`, `to` and the time, and rewrites it before the run returns with each down's verdict,
  the file-row counts the run prints, and whether the stamp moved. A rollback killed partway leaves
  the record of what it began. This record and the receipt's `rolled-back` rows are what "recorded"
  means: the reason the refusal gives, that "nothing afterwards records it happened", no longer
  holds. Observed by AC5.
- **S7** — Never on its own. `run_reverse_walk` has one caller, `_cmd_update` under `--rollback`. A
  stopped forward walk, the per-kit verify rollback and `apply` run no `down`. Observed by AC3 and
  AC7.
- **S8** — The docs. `help/upgrade-steps.md` gains a section "Rolling back": when to use
  `update --rollback --to <rev>`, what it runs and in what order, that a failed `update` never
  rolls back by itself, the record it leaves, and that a file gov added after `--to` is a withdrawal
  `--write-withdrawals` decides, as for any `update`. Observed by AC8.

## 3. Non-goals (OUT)

- The forward walk, the pending order, the lock reclaim and the attended order: TOOL-dSafePassage-2.
  This unit reverses the order and reuses the order writer.
- Each step's `down` argv and its tolerance of a partial up: the row's author's, under
  TOOL-dSafePassage-1's grammar. The schema step's own down: TOOL-dSafePassage-3.
- The isolation contract: TOOL-dSafePassage-7.
- Byte-identity of a rollback to release-0 over every declared step, and the rollback from a killed
  walk's state over that tree: TOOL-dSafePassage-5's `upgrade-walk` leg.
- A rollback across a `[[retired]]` row, which brings back an entry the registry no longer holds:
  TOOL-dSafePassage-1's succession. This unit lifts no registry refusal.
- Un-installing an entry the receipt gained after `--to`. It stays claimed, and its files read as
  withdrawals, deleted only under `--write-withdrawals`.
- A `--kits`-scoped rollback, and a rollback of `apply` or `adopt`.
- Any policy key. This unit reads none.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — `read_steps` and the order it returns, the `down` and `witness` keys, and the before-image each down restores from; without them there is no down to run
- **consumes-from** `TOOL-dSafePassage-2` — `write_attended_order`, the receipt hand-off, the staging journal, and the `failed` rows a killed or failed walk leaves
- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state` and the `rolled-back` state, and the schema step whose down restores schema 3 and runs last, after every other applied step's down
- **consumes-from** `TOOL-dSafePassage-7` — `run_step_isolated` for each down, and its `attended` verdict
- **hands-off** `TOOL-dSafePassage-5` — the rollback over the release-0 tree, from a whole walk and from a killed one, compared byte for byte with release-0, the outbox directory where the rollback record lives left out of that comparison as the lock's directory is
- **hands-off** `TOOL-dSafePassage-17` — the reverse walk judging a down by the row's declared rule, or by its exit where no before-image exists, the repair of finding 51
- **hands-off** `TOOL-dSafePassage-18` — the reverse walk writing no row once a down leaves the receipt below schema 4, the repair of finding 2
- **hands-off** `TOOL-dSafePassage-19` — the stamp and the record of a rollback past the schema step, and its re-run after a kill, the repair of finding 52
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built
- **hands-off** `TOOL-dSafePassage-39` — move 3 rewriting an `applied` row with its `via` kept, and recording an unrecorded row whose witness holds and whose image is absent with `via` `witness`, the repair of finding 23 of the spec audit of units 27 to 35
- **consumes-from** `TOOL-dSafePassage-43` — `DOWN_STOP_PREFIXES`, from which moves 3, 4 and 5 build their failure texts, and the writer rule that admits them on an `applied` row; without it the writer refuses this unit's own stop rows
- **hands-off** `TOOL-dSafePassage-49` — AC4 read with each stop text the `down-fails` and `witness-stays` plants leave opening with an entry of `DOWN_STOP_PREFIXES`, and TOOL-dSafePassage-43's AC3 observed at this unit's pass; move 3 on a `rolled-back` row whose witness holds recording it `applied`; and this unit's order moved to 3 by that unit's §8 F1, so it builds after TOOL-dSafePassage-43 and TOOL-dSafePassage-7, findings 11, 1, 2 and 19 of the spec audit of units 43 to 46

## 4. Design

### Data model

The reverse walk changes only `state` and `failure` of rows TOOL-dSafePassage-3's schema holds:

| Row before | Down result | Row after |
|---|---|---|
| `applied` or `failed` | spawned, exit 0, witness does not hold | `rolled-back`, no `failure` |
| `applied` or `failed` | before the spawn returns | same state, `failure` `down interrupted: …` |
| `applied` or `failed` | exit non-zero | same state, `failure` `down exit <rc>: …` |
| `applied` or `failed` | exit 0, witness holds | same state, `failure` `witness still holds after down` |
| `rolled-back`, or none | witness does not hold | unchanged, skipped |
| `rolled-back`, or none | witness holds | as an `applied` row |

A reverse walk re-run after a stop resumes at the row it stopped at, because every row after it in
reverse order reads `rolled-back` and its witness no longer holds.

The record, `update-reverted-<from8>-<to8>.md`:

```
# update --rollback <from8> -> <to8>
started <utc> · finished <utc>|not finished
down <id>: rolled-back | skipped (nothing applied) | STOPPED <failure>
files: wrote <n> · moved <n> · deleted <n> · withheld <n> · conflicts <n>
gov_commit: moved to <to8> | not moved, <why>
```

### The order of one rollback run

1. The ordinary preconditions, the lock and its reclaim included (TOOL-dSafePassage-2, S6 to S8).
2. `check_rollback_vintage` in `demand_forward_vintage`'s place; `demand_published_vintage`.
3. The grading every `update` does, against `--to`.
4. Read-only: the preview, then return.
5. `write_rollback_record`, begun.
6. `run_reverse_walk`. A stop finishes the record and returns with the findings.
7. The pre-write snapshot, the write loop, re-render, hook wiring and the per-kit verify, as for
   any `--to`.
8. The stamp: `gov_commit` = `--to`, `schema` as left. The record, finished.

Downs run before the file rows move back because each up ran after its file rows moved forward
(TOOL-dSafePassage-2, S4): the reverse walk meets the tree each up left, and the rows return after.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `derive_reverse_steps`, `run_reverse_walk` and
`write_rollback_record`; the fixture families `rollback` and `rollback-update`. Plants of
`rollback`: `after-kill`, `after-fail`, `down-fails`, `witness-stays`, `unrecorded`, `partial-to`
and `callers`. Plants of `rollback-update`: `refused`, `read-only`, `descendant`, `scoped` and
`no-base`. In `govkit.py`: `check_rollback_vintage`, the `--rollback` flag, the record name
`update-reverted-<from8>-<to8>.md` and the `would roll back` preview line. Each function name passes
the `py.function` cell (`python3 tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for
all four, 2026-10-23). No conf key, no gate leg, no policy key.

### Migration

None. A receipt with no `steps` list has no recorded row, so every reverse row is witness-probed,
and a rollback to before `govkit/receipt-schema-4` ends with that step's down.

### Rollout

Live at landing, reached only through `--rollback`. Within order 2 it builds last, after
TOOL-dSafePassage-7 and TOOL-dSafePassage-2, the three sharing `tools/govkit/upgrade_steps.py`.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Roll back on a failed walk.** The clause forbids it: never run on its own after a failure. An
  operator reading the failure decides.
- **A `rollback` verb of its own.** It would duplicate every precondition and the write loop that
  `update` already runs for an arbitrary `--to`; a flag narrows `update` instead.
- **"One revert of the adopter's update commit"**, the research's reading of reversibility. `update`
  never commits (research §2, step 14), so there is no commit to revert, and a revert reaches
  nothing a step wrote outside tracked files.
- **The record as a receipt field.** The schema step's down restores schema 3, so a field there
  would be unwritable by the run it records, and a byte-identical rollback leaves no room for one.

## 5. Production-readiness checklist

- security: the lift is exactly one refusal under one flag; `demand_published_vintage`, the dirty
  precondition and the lock still hold, and every down runs under TOOL-dSafePassage-7's contract.
  The record sits in `.governance/outbox/`, where `update`'s orders already go.
- perf / scale: per reverse row, one or two witness spawns and one down. No figure is pinned.
- error / empty / loading states: nothing to roll back is a refusal naming why; a stopped reverse
  walk ends the run before a file moves, its record saying where it stopped.
- observability: one line per down and verdict, the record, and the run's ordinary counts.
- risks: the write loop meets an older `--to` here for the first time in normal use, and its
  comment at `tools/govkit/govkit.py:11190-11193` already records sources absent at an older vintage;
  AC5's fixture is the observation, and TOOL-dSafePassage-5 widens it to release-0. A down that does
  not tolerate a partial up stops the reverse walk with its exit recorded, the safe direction.
- testing: the two fixture families; the arm joins `tools/govkit/selftest.py` (§7), and each new
  refusal branch is reached there, as `govkit refusal join` requires.
- migration: none; §4 "Migration".
- user docs: `help/upgrade-steps.md`, S8.

## 6. Acceptance criteria

The `rollback` family reuses the `walk` family's scratch gov of TOOL-dSafePassage-2, commits A to C
and steps `s1` to `s4`, each `down` taking away the file its `up` writes, built under `%TEMP%`.

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback` runs, it walks the
  target from A to C, then reverse-walks to A: it prints the downs of `s4`, `s3`, `s2`, `s1` in that
  order, each row reads `rolled-back`, the target's tracked bytes equal their bytes before the walk,
  and it exits 0; `--plant partial-to` reverse-walks to B and downs only `s4` and `s3`.
  Red when: the downs run in walk order, or a step introduced at or before `--to` is downed.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant after-kill`
  runs, the walk is killed after `s3`'s up writes its first file, and the reverse walk downs `s3`
  from its `failed` row, then `s2` and `s1`; the target's bytes equal their bytes before the walk,
  and it exits 0.
  Red when: a `failed` row is skipped, so the killed up's first file stays.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant after-fail`
  runs, `s3`'s up exits 1 and the walk stops with no `down` canary present; only the explicit
  reverse walk that follows downs `s3`, `s2` and `s1`, and it exits 0.
  Red when: any down runs before the reverse walk is called.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant down-fails`
  runs, `s3`'s down exits 1: `s4` reads `rolled-back`, `s3` keeps its state with a `failure` naming
  `down exit 1`, `s2` and `s1` are not downed, and it exits 1; the fixture repairs the down and the
  re-run resumes at `s3`. `--plant witness-stays` makes `s2`'s down exit 0 leaving its file, and
  `s2` keeps `applied` with `witness still holds after down`. `--plant unrecorded` blanks `s2`'s
  receipt row with its file present, and its down runs.
  Red when: the reverse walk continues past a failed down, records `rolled-back` while the witness
  holds, or skips an unrecorded step whose witness holds.
- **AC5** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update` runs, a scratch
  gov's `govkit.py update --target <t> --rollback --to A --write` over a target updated from A to B,
  whose step `s1` is applied, downs `s1` before the write loop's first line, returns the file rows
  to A's bytes, writes `gov_commit` = A with the `schema` the downs left, and leaves
  `update-reverted-<from8>-<to8>.md` naming `s1` as `rolled-back` and `gov_commit: moved`; it exits
  0. `--plant read-only` prints `would roll back` for `s1` and spawns nothing.
  Red when: the file rows move before the downs, the stamp re-sets `RECEIPT_SCHEMA`, or no record
  is left.
- **AC6** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant refused`
  runs, `update --to A --write` without `--rollback` refuses, the message naming
  `update --rollback --to`; `--plant descendant` refuses `--rollback` to a descendant of the
  receipt's commit, `--plant scoped` refuses `--rollback --kits`, and `--plant no-base` refuses a
  receipt with no `gov_commit`; each exits 1 naming its reason.
  Red when: a downgrade passes without the flag, or the flag lets a forward move or a scoped run
  through.
- **AC7** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant callers` runs,
  it parses `upgrade_steps.py` and `govkit.py` with `ast`, finds one call of `run_reverse_walk`,
  inside `_cmd_update`, and exits 0; a planted module text calling it from a second function exits 1
  naming that call.
  Red when: a second caller exists, or the probe finds none and passes.
- **AC8** — When `git grep -n -e "update --rollback" -e "update-reverted" -e "never rolls back" -- "help/upgrade-steps.md"`
  runs, the "Rolling back" section names all three, and
  `python3 tools/govkit/govkit.py --help` prints the `update` line with `[--rollback]`.
  Red when: the section or the USAGE flag is missing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the self-test calls `upgrade_steps.py fixture` for the `rollback` and `rollback-update` families with every plant and asserts each exit, named line and the byte comparison, each failing case staged by its plant · none

## 8. Open questions

- **F1 — What makes a rollback "recorded".** Options: the receipt alone, its `rolled-back` rows; a
  receipt field naming the rollback; an outbox record beside the receipt rows. The schema step's down
  takes the `steps` field away, so a rollback to before it leaves no row, and a new receipt field
  is TOOL-dSafePassage-3's and would break the byte-identical rollback TOOL-dSafePassage-5 asserts.
  RESOLVED (agent, 2026-10-23, delegated): the outbox record plus the rows, on rung 3; the record is
  begun before the first down, so a killed rollback is recorded too. widens: none · relaxes: none
- **F2 — How the operator asks for a rollback.** Options: a new verb; a flag on `update`; an
  automatic rollback when a walk fails. The third fails the clause's "never run on its own after a
  failure" (veto 1); a new verb is a second public surface carrying the same preconditions.
  RESOLVED (agent, 2026-10-23, delegated): `update --rollback --to <rev>`, on rung 3, a scope flag
  that narrows `update` the way `--write-withdrawals` does. widens: none · relaxes: none
- **F3 — Downs before or after the file rows move back.** Options: before, against the tree the ups
  left; after, against `--to`'s files. TOOL-dSafePassage-2 runs each up after the file rows move
  forward, so only "before" gives each down the tree its up produced. RESOLVED (agent, 2026-10-23,
  delegated): before, on rung 3. widens: none · relaxes: none
- **F4 — The parent, dGroundRules, is unbuilt.** RESOLVED (agent, 2026-10-23, delegated): this unit
  reads no key of `.governance/policy.toml` and calls no policy reader, so `cl-dClosedLoop-0007` and
  `cl-dClosedLoop-0008` bind nothing here; the build run re-grounds against the landed parent before
  its first pass, and an interface the parent lands that this unit should read is an M2 amendment.
  widens: none · relaxes: none
- **F5 — Names spelled by a sibling.** The `rolled-back` state and the writer `set_step_state` are
  TOOL-dSafePassage-3's, the `down` key TOOL-dSafePassage-1's, written concurrently. RESOLVED (agent,
  2026-10-23, delegated): this spec spells them as the brief's S1 and S4 fix them; the M2 cross-read
  before the first code pass binds any difference, fixed in whichever document is wrong with a rev
  bump. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-17`, `TOOL-dSafePassage-18`, `TOOL-dSafePassage-19`, `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-39`; no other section moved.
- rev-4 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-43`; no other section moved.
- rev-5 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 43 to 46, written by the disposal stage: `TOOL-dSafePassage-49`; no other section moved.

## 10. Reuse audit

The seams extended are `demand_forward_vintage` (`tools/govkit/govkit.py:7463-7482`), whose refusal
the flag lifts and whose ancestry test `check_rollback_vintage` reverses, and `_cmd_update`'s own
write loop, which already grades an arbitrary `--to` (`tools/govkit/govkit.py:11190-11193`), so the
file half of a rollback is the ordinary run and not a second one. The reverse order is
TOOL-dSafePassage-1's `read_steps` order reversed, and the reverse walk reuses `run_step_isolated`,
`write_attended_order`, the receipt hand-off and the staging journal of TOOL-dSafePassage-2 and
TOOL-dSafePassage-7. The record follows the outbox orders `update` already
writes, `update-rollback-<kit>.md` (`tools/govkit/govkit.py:11937`). `reuse_lookup.py "run steps down
in reverse to roll back a downgrade"` ranked `run`, govkit's `step` (a phase-line printer,
`tools/govkit/govkit.py:98`), `run_arms`, `run_git` and the runlog model: none reverses a step, so
the hits are name matches and agree with source in having no reverse walk. The recall probe found
the research's candidate E (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-research-supersession.md`,
§4), which names "a rollback mode that lifts :7178 for a recorded rollback only", today's
`demand_forward_vintage`, and DEPL-dCarriedReceipt-14, the per-kit verify rollback this unit leaves
as it is.

Recall terms used: `python tools/memory-recall/query.py "how does govkit refuse a downgrade and roll back an update across versions" --terms "downgrade refusal rollback down steps reverse receipt vintage ancestor recorded partial killed"`
