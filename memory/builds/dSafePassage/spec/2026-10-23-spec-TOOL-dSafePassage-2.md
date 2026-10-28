# TOOL-dSafePassage-2 — `update` walks the upgrade steps oldest first, and recovers what a killed run left

**Status:** CLOSED · rev-5 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0019@6e0cd313 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-2-deviation-115.md](../build/2026-10-23-build-TOOL-dSafePassage-2-deviation-115.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-2-deviation-116.md](../build/2026-10-23-build-TOOL-dSafePassage-2-deviation-116.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-2-deviation-117.md](../build/2026-10-23-build-TOOL-dSafePassage-2-deviation-117.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-2-deviation-118.md](../build/2026-10-23-build-TOOL-dSafePassage-2-deviation-118.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-2-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-2-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-26-prompt-TOOL-dSafePassage-2-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-2-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

`update` moves an adopter's files forward and has no way to move anything else: a moved conf key is
only reported, and an old shape stays (research, §2). TOOL-dSafePassage-1 gives the step row and
TOOL-dSafePassage-7 the contract a step runs under; this unit makes `update` walk every step between
a receipt's vintage and its target, oldest first, each skipped when its witness holds, the receipt
advancing per completed step, and a failed or killed step stopping the walk with the failure
recorded and the steps before it left applied. It also closes `gap-deploy-19`: a half-applied
`update` leaves the write lock behind, which an operator must `rm` by hand
(`tools/govkit/govkit.py:7421-7427`), and leaves staged paths the next run refuses as dirty
(`tools/govkit/govkit.py:7386-7391`). A lock a killed run left is reclaimed by the next once its
holder is dead, and the paths that run staged are read as gov's own staging.

## 2. Scope (IN)

- **S1** — The pending set. `derive_pending_steps(gov_root, receipt, to_commit)` in
  `tools/govkit/upgrade_steps.py` returns every step row TOOL-dSafePassage-1's `read_steps` reads at
  `to_commit`, in the order that reader returns them, which is the brief's S5 order (oldest
  introducing commit first along the default branch's first-parent line, then row order, unlanded
  rows last), minus every row the receipt's `steps` list records as `applied`. A row landed after
  `--to` is not in `to_commit`'s tree, so it is not read. A receipt with no `steps` list has every
  row pending. This unit derives no order of its own. §8 F1 says why the receipt's step record, and
  not its `gov_commit` alone, is the vintage. Observed by AC1.
- **S2** — The walk. `run_step_walk(gov_root, target, receipt_path, receipt, rows, to_commit)` takes
  each pending step in order through five moves, all spawns through `run_step_isolated`
  (TOOL-dSafePassage-7):
  1. its `witness`; exit 0 records the step `applied` and moves on, its `up` never spawned;
  2. an `attended` verdict (`needs-target = true`) records the step `failed` with the failure
     `attended: the step needs the target's code`, writes S5's order, and stops the walk;
  3. it records the step `failed` with the failure `interrupted: started <utc>, no exit recorded`,
     persisted before the spawn, so a walk killed with its step leaves the failure recorded;
  4. it runs the row's `resume` argv when the receipt held a `failed` row for the step when this walk
     began and `resume` is an argv, else its `up`; a non-zero exit records `failed` with
     `exit <rc>: <the last stderr line>` and stops the walk;
  5. it runs the `witness` again; exit 0 stages the step's writes (S11) and records `applied`,
     anything else records `failed` with `witness does not hold after up` and stops the walk.
  The steps before a stop stay `applied`, and no `down` runs. Observed by AC2, AC3, AC4 and AC5.
- **S3** — The receipt's progress. Each record goes through `set_step_state`, the one writer
  TOOL-dSafePassage-3 ships, into `_cmd_update`'s in-memory receipt and onto `receipt_path` in one
  atomic write, `gov_commit` unchanged. That on-disk state is the one the findings path already
  writes (`tools/govkit/govkit.py:12397-12405`). After each spawn the walk re-reads `schema` and
  `steps` from disk into the in-memory receipt, because a step may rewrite them, as
  `govkit/receipt-schema-4` does. The list's last `applied` row is the last completed step.
  Observed by AC3 and AC4.
- **S4** — The walk inside `update`. On a read-only run the preview block
  (`tools/govkit/govkit.py:10223-10233`) prints each pending step as `would walk` and spawns
  nothing, its witness included, because a read-only `update` writes no byte. On `--write` the walk
  runs after the HOLD REGION END marker (`tools/govkit/govkit.py:11197`) and before the re-render
  block (`tools/govkit/govkit.py:11202`), so steps meet the new vintage's files and the renders,
  hook wiring and per-kit verify that follow meet the migrated tree. It runs only while the run has
  no finding at that point, and only on a run with no `--kits` scope; otherwise it prints
  `steps: not walked` with the reason and the pending count. A stopped walk is a finding, so the
  `gov_commit` stamp is withheld (`tools/govkit/govkit.py:12397`). The per-kit verify rollback runs
  no `down`. One summary line prints every count, zeros included:
  `govkit update — steps: <n> pending · <a> applied · <s> skipped · stopped at <id|none>`.
  Observed by AC6.
- **S5** — The attended order. An `attended` stop writes
  `.governance/outbox/update-attended-step-<slug>.md`, the slug from `render_order_slug`
  (`tools/govkit/govkit.py:5735`), naming the step id, its resolved `up` argv, why it is attended,
  and that the next `update --write` skips the step once its witness holds. Observed by AC5.
- **S6** — The lock names its holder. `take_write_lock` (`tools/govkit/govkit.py:7409-7432`) adds
  `host` to the record it writes. `describe_write_lock` prints it, and its refusal's remedy names
  the reclaim in place of a hand `rm`. Observed by AC7.
- **S7** — The reclaim. On `FileExistsError` the take calls `write_reclaimed_lock(lock, record)`,
  which reads the holder with `read_lock_holder` and judges it with `check_holder_dead`: `dead` when
  the lock's `host` is this host, or absent, and the process-monitor census
  (`tools/process-monitor/census.py:260-281`) holds no row with that pid, or holds one created after
  the lock's `started`, a reused pid; `live` when a row with that pid was created before it;
  `unknown` when the census refuses, the host differs or the lock is unreadable. Only `dead` is
  reclaimed, holding a guard file `<lock>.reclaim` taken with `O_EXCL`: the holder of the guard
  re-reads the lock, and only bytes equal to the ones it judged dead are unlinked and the lock
  re-made with `O_EXCL`. A guard whose own holder is dead is cleared and that call refuses busy, so
  no call both clears a guard and takes one. `live` and `unknown` refuse as today. The reclaim
  prints one line naming the dead holder. Observed by AC7 and AC8.
- **S8** — The staging journal. Every call in `_cmd_update` and `land_through_index`
  (`tools/govkit/govkit.py:8958`) that writes the target's index first appends one JSON line to
  `.governance/outbox/.update.lock.staged`, the path and the blob oid it is about to stage, or
  `null` for a deletion. `release_write_lock` (`tools/govkit/govkit.py:7435-7446`) unlinks it with
  the lock. When S7 reclaims a dead holder, its journal is handed to `demand_claimed_paths_clean`
  (`tools/govkit/govkit.py:7321-7391`), and `dirty_claimed_paths` reads a claimed path whose only difference is index against HEAD, and whose
  index state equals the journal's last line for that path, as gov's own staging, the same oid
  comparison its third carve-out makes (`tools/govkit/govkit.py:7113-7116`). Observed by AC9.
- **S9** — The fixtures. `python3 "tools/govkit/upgrade_steps.py" fixture walk|lock|update [--plant <case>]`
  observes S1 to S8 in scratch repositories under `%TEMP%`; `update` copies this checkout's
  `govkit.py`, `upgrade_steps.py` and the census module into a scratch gov, as
  `tools/govkit/selftest.py:1711-1745` builds its scratch govs. Every plant is listed in §4
  "Inventory". Observed by AC1 to AC9.
- **S10** — The docs. `help/upgrade-steps.md` gains a section "What `update` does with steps": the
  order, the skip, a stopped walk, the attended order, and what the next run does after a kill.
  Observed by AC10.
- **S11** — The step's writes, staged. `update` stages what it writes and never commits (research,
  §2, step 14), and a step's writes are no exception. After a step's witness holds, the walk stages
  every path the step's before-image lists, the image TOOL-dSafePassage-1's helpers write at
  `.governance/steps/<entry>/<slug>.before.json`, and the image itself: `git add` for a path
  present, `git rm --cached` for one the step took away, each preceded by its S8 journal line. A
  step that writes no image, such as `govkit/receipt-schema-4`, whose one write is the receipt,
  stages nothing here; the receipt is staged where `update` stages it today. Observed by AC6.

## 3. Non-goals (OUT)

- The step row's grammar, its reader, `introduced` and how it is filled, `resume`'s spelling, and the
  `[[retired]]` rows `update` reads: TOOL-dSafePassage-1.
- The receipt's `steps` field, `RECEIPT_SCHEMA = 4`, the writer, and how the schema step's own row
  lands while the field does not exist yet: TOOL-dSafePassage-3.
- The isolation contract and the `attended` verdict: TOOL-dSafePassage-7.
- Down steps and any rollback: TOOL-dSafePassage-4. A failed walk never runs one.
- `update` on gov's own tree and gov's source-mode receipt: TOOL-dSafePassage-8. The refusal of the
  gov checkout as a target (`tools/govkit/govkit.py:9167-9168`) is untouched here.
- The release-0 walk, its kill-after-first-write and k-th-step-fails arms, and the byte-identity of
  the converged tree over every declared step: TOOL-dSafePassage-5's `upgrade-walk` leg.
- A step phase timeout, and a walk on a `--kits`-scoped run (§8 F3).
- An unreadable lock, a lock from another host, and a census that cannot run: each stays a refusal an
  operator clears, because none of them proves the holder dead.
- Any policy key. This unit reads none.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — `read_steps` and the order it returns, the `witness`, `up` and `resume` keys, the before-image whose paths the walk stages, and `tools/govkit/upgrade_steps.py` with its import from `govkit.py`; without them there is no row to walk
- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, the one writer of the `steps` field it owns, and the schema step whose up rewrites the receipt; without it no progress row has a schema to land in
- **consumes-from** `TOOL-dSafePassage-7` — `run_step_isolated` and its `attended` verdict; without them a step would spawn on the node's whole environment
- **hands-off** `TOOL-dSafePassage-4` — `write_attended_order`, the receipt hand-off, the staging journal, and the `failed` rows a killed or failed walk leaves for a down to tolerate
- **hands-off** `TOOL-dSafePassage-8` — `run_step_walk` and `derive_pending_steps`, whose source-mode branch that unit adds, with the walk's `witness does not hold after up` stop and its lock reclaim, run on gov's own tree in the lander's prepared merge
- **hands-off** `TOOL-dSafePassage-11` — the walk that runs the floor step's row in its place and stops when that step fails
- **hands-off** `TOOL-dSafePassage-5` — the walk over the release-0 tree, killed after each step's first write and made to fail at each step in turn, its converged tree compared byte for byte
- **hands-off** `TOOL-dSafePassage-15` — the walk asking the step record's precondition before each record, so a schema-3 receipt reaches the schema step, the repair of finding 1
- **hands-off** `TOOL-dSafePassage-19` — the post-spawn re-read dropping a key the receipt on disk no longer holds, part of the repair of finding 52
- **hands-off** `TOOL-dSafePassage-22` — the reclaim reading its clock before the census, the repair of finding 16
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built
- **hands-off** `TOOL-dSafePassage-33` — recording a row the forward walk's first move applies by witness alone with the mark that says so, the repair of finding 40 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-40` — move 1's evidence read, the walk-start record and the row's before-image path, and the `kill-after-up` walk plant, the repair of finding 29 of the spec audit of units 27 to 35

## 4. Design

### Data model

A progress row, in the brief's S4 shape: `{"id", "introduced", "state"}`, `state` one of `applied`,
`failed` or `rolled-back`, a `failed` row adding `"failure"`. This unit writes the first two
states and these failures:

| Failure text | Written at |
|---|---|
| `attended: the step needs the target's code` | move 2 |
| `interrupted: started <utc>, no exit recorded` | move 3, before the spawn; a walk that returns replaces it |
| `exit <rc>: <the last stderr line>` | move 4 |
| `witness does not hold after up` | move 5 |

The lock record, one JSON object, gains one key:

```
{"pid", "verb", "started", "started_utc", "host"}
```

A lock written before this unit has no `host`, and is judged on this host, since the lock lives in
the target's working tree.

A journal line: `{"path": "<target-relative path>", "oid": "<blob oid>" | null}`, one per staging
call, a step's own writes included (S11), in call order; the last line for a path wins.

### The pending order

The order is TOOL-dSafePassage-1's, read once per run by `read_steps` at `to_commit`, and this unit
re-derives none of it: a second ordering beside the reader's would be two answers to one question.
Reading at `to_commit`, never at gov's working tree, is what keeps a row landed after `--to` out of
an older walk. A progress row's `introduced` is the reader's derived value, `unlanded` included.

### The receipt hand-off

The receipt on disk is the hand-off between govkit and a step. The walk persists before each spawn
and re-reads after it, so a step never meets a receipt older than the walk's record, and govkit
never stamps over a field a step wrote. A step may change only `schema` and `steps` in the receipt;
those are the two keys re-read.

### The reclaim and the census

The census is the process-monitor kit's, loaded from the sibling kit directory through govkit's own
`resolve_kit_dir` (`tools/govkit/govkit.py:197-235`), the way `load_process_monitor` loads it
(`tools/run-gates/measure_legs.py:998-1009`). govkit runs only from gov's checkout
(`tools/govkit/registry.toml:480-482`), so the kit is there. A row's creation time is `now - age_s`.
`check_holder_dead` reads a pid as the same process when its row was created no later than two
seconds after the lock's `started`, since `age_s` is whole seconds; a pid reused inside that window
reads `live`, which refuses, the safe direction.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `derive_pending_steps`, `run_step_walk`,
`read_lock_holder`, `check_holder_dead`, `write_reclaimed_lock`, `read_staging_journal`,
`write_staging_line` and `write_attended_order`; the fixture families `walk`, `lock` and `update`.
Plants of `walk`: `witness-holds`, `fail-k`, `kill-step`, `resume`, `attended` and `not-pending`.
Plants of `lock`: `lock-dead`, `lock-live`, `lock-reused`, `lock-foreign-host`, `lock-unreadable`,
`lock-race` and `guard-dead`. Plants of `update`: `read-only`, `scoped`, `update-fail`, `kill-walk`
and `kill-walk-edit`. In `govkit.py`: the lock record's `host` key, the
journal path `.governance/outbox/.update.lock.staged`, the guard path `<lock>.reclaim`, the order
`update-attended-step-<slug>.md`, and the `steps:` summary line. Each function name passes the
`py.function` cell (`python3 tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for
all eight, 2026-10-23); `take_` and `demand_` are outside the declared verbs, so this unit mints
neither). No conf key, no gate leg, no policy key.

### Migration

Additive. A receipt with no `steps` list walks every step up to `--to`, the first being
`govkit/receipt-schema-4`, which creates the field. A lock written by an older govkit has no `host`
and is judged here; an older govkit meeting a new lock reads its `pid` and `started` as before.

### Rollout

Live at landing in `update --write`. Within order 2 it builds after TOOL-dSafePassage-7 and before
TOOL-dSafePassage-4, the three sharing `tools/govkit/upgrade_steps.py`. Every scratch gov a
self-test arm builds copies `upgrade_steps.py` beside `govkit.py`, the seam TOOL-dSafePassage-1
lands; the `update` fixture also copies the census module, and a scratch gov without it reads every
holder `unknown`.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Pending keyed on `gov_commit` alone**, every step introduced after the receipt's commit: a
  scoped run or an `apply` moves `gov_commit` without walking, and the steps it passed would never
  run. §8 F1.
- **A walk that rolls back on failure.** The clause leaves the earlier steps applied, and
  `cl-dClosedLoop-0021` says a rollback never runs on its own after a failure.
- **Reclaim by lock age**, as the claim-push lock breaks on a deadline
  (`tools/unattended/unattended.sh:2325-2330`): a long `update` would lose its lock while alive.
  The pid with its creation time is the proof `measure_legs.py` uses for its own dead owners
  (`tools/run-gates/measure_legs.py:1467-1493`).
- **Reading `read_process_created` from `measure_legs.py`.** It is Windows-only and needs that
  module's `ctypes` table; the census answers on both platforms.
- **Predicting the killed run's staging** from gov's blobs at `--to`: the three-way arm, the carry
  needles and the pin block would each need a second implementation of the write loop. The journal
  records what was staged instead.
- **A per-row receipt flush in the write loop**, so carve-out 3 alone clears the killed run's paths:
  a verify rollback killed partway would leave rows naming bytes the index no longer holds.

## 5. Production-readiness checklist

- security: no new spawn path; every step argv runs through TOOL-dSafePassage-7's contract. The
  journal and the guard sit beside the lock under `.governance/outbox/`, the directory the lock
  already writes. The dirty precondition is widened only by an exact oid the dead holder journaled
  before staging it, so an operator's own staged edit, a different blob, stays dirty.
- perf / scale: one `read_steps` per run; each pending step costs two witness spawns, one up and
  one staging call per path its image lists. A receipt recording every step costs no spawn. The
  census runs only when a lock already exists. No figure is pinned.
- error / empty / loading states: no pending step prints the summary line with `0 pending`; a census
  refusal, an unreadable lock and a foreign host each refuse with the reason; a scoped or
  already-red run prints `steps: not walked` and its reason.
- observability: one line per step and verdict, the summary line, the reclaim line, and the
  attended order.
- risks: `_cmd_update` is thousands of lines long, so each local this unit adds takes a `_sw_`
  prefix (`memory/gotchas/a-new-local-collides-in-a-long-function.md`). A step line printed
  `applied` before a verify rollback reverts that kit's files is still true of the step
  (`memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md`). An index write added to
  `_cmd_update` later without a journal line is read dirty after a kill, the safe direction; AC9's
  set comparison is what finds it.
- testing: the three fixture families; the arm joins `tools/govkit/selftest.py` (§7), and each new
  refusal branch is reached there, as `govkit refusal join` requires.
- migration: additive; §4 "Migration".
- user docs: `help/upgrade-steps.md`, S10.

## 6. Acceptance criteria

The fixtures build their repositories under `%TEMP%`. The `walk` family's scratch gov carries commit
A, commit B introducing steps `s1` and `s2`, a side branch introducing `s3` merged at M, and commit
C introducing `s4`; each step writes one file into the target through TOOL-dSafePassage-1's
before-image helper, and its witness tests that file.

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk` runs from a receipt at A
  to `--to` C, it prints `s1`, `s2`, `s3`, `s4` in that order, each `applied`, the receipt's `steps`
  lists them so, and it exits 0; `--plant not-pending` adds a step introduced after C and one the
  receipt records `applied`, and neither spawns.
  Red when: the walk re-orders the rows `read_steps` returns, so `s3` does not take M's place, or a
  step outside the pending set runs.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant witness-holds` runs
  with `s2`'s file already in the target, `s2` prints `skipped (witness holds)`, its `up` canary is
  absent, its row reads `applied`, and the run exits 0.
  Red when: an `up` runs over a step whose witness holds.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant fail-k` runs with
  `s3`'s `up` exiting 1, the run stops: `s1` and `s2` read `applied`, `s3` reads `failed` with a
  `failure` naming `exit 1` and its stderr line, `s4`'s canary and every `down` canary are absent,
  and the run exits 1.
  Red when: the walk continues past the failure, rolls back an earlier step, or records no failure.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant kill-step` runs,
  `s3`'s `up` writes its first file and blocks, and the fixture kills the walk's process and the
  step's; the receipt then reads `s2` as the last `applied` row and `s3` `failed` with an
  `interrupted:` failure. The re-run walk completes and its target and receipt bytes equal those of
  an uninterrupted walk's, and `--plant resume` shows the re-run spawning `s3`'s declared `resume`
  argv in place of its `up`; both exit 0.
  Red when: the pre-spawn row is not persisted, so the kill leaves no failure, or the re-run skips
  `s3`, or a `resume` argv is ignored.
- **AC5** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant attended` runs with
  `s2` declaring `needs-target = true`, the walk stops before spawning `s2`, its row reads `failed`
  with the `attended:` failure, the outbox order `update-attended-step-<slug>.md` names `s2` and
  its argv, and the run exits 1; the fixture then runs `s2`'s `up` by hand, and the re-run walk
  skips `s2` by its witness and applies `s3` and `s4`.
  Red when: an attended step spawns, or the re-run cannot pass it.
- **AC6** — When `python3 "tools/govkit/upgrade_steps.py" fixture update` runs, the scratch gov's
  `govkit.py update --target <t> --write` prints each step line after the write loop's lines and
  before the re-render block's, the summary reads `2 pending · 2 applied · 0 skipped · stopped at
  none`, the receipt's `gov_commit` moves, and `git diff --cached --name-only` in the target names
  each step's file and its before-image; `--plant read-only` prints `would walk` twice with no
  canary; `--plant scoped` prints `steps: not walked` with the pending count; `--plant update-fail`
  exits 1 with `gov_commit` unmoved, `s1` `applied`, `s2` `failed`, the file rows landed and no
  `down` canary.
  Red when: the walk runs before the file rows land, on a read-only or scoped run, a stopped walk
  lets the stamp move, or a step's write is left unstaged.
- **AC7** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-dead` runs
  over a lock whose pid names a process the fixture started and let exit, the take prints the
  reclaim line naming that pid and holds a lock naming its own, its record carrying `host`;
  `lock-reused`, a live pid created after the lock's `started`, reclaims the same
  way; `lock-live`, `lock-foreign-host` and `lock-unreadable` each refuse with the holder described,
  the remedy naming the reclaim. `lock-dead` and `lock-reused` exit 0, the other three exit 1.
  Red when: a live holder is reclaimed, a reused pid reads live, or a dead one is never reclaimed.
- **AC8** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-race` runs,
  two processes reclaim one dead lock at once and exactly one holds the lock afterwards, the other
  refusing busy; `--plant guard-dead` leaves a `.reclaim` guard whose holder is dead, and the first
  take clears it and refuses busy, the second reclaims.
  Red when: both racers proceed, or a call clears a guard and takes the lock in one go.
- **AC9** — When `python3 "tools/govkit/upgrade_steps.py" fixture update --plant kill-walk` runs,
  `update --write` is killed while its first step blocks; the paths in the staging journal
  `.update.lock.staged` beside the lock then equal the set `git diff --cached --name-only` names in
  the target, and a re-run `update --write` reclaims the lock, passes the dirty precondition and
  converges to the bytes of an uninterrupted run, exiting 0. `--plant kill-walk-edit` stages a
  different blob at one journaled path after the kill, and the re-run refuses naming that path as
  dirty.
  Red when: an index write in the write loop journals nothing, so the sets differ, or a journaled
  path's different blob is read as gov's staging.
- **AC10** — When `git grep -n -e "would walk" -e "update-attended-step" -e ".update.lock.staged" -- "help/upgrade-steps.md"`
  runs, the section "What `update` does with steps" names all three.
  Red when: the section is missing or names none of them.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · the self-test calls `upgrade_steps.py fixture` for the `walk`, `lock` and `update` families with every plant and asserts each exit and named line, each failing case staged by its plant · none

## 8. Open questions

- **F1 — What "a receipt's vintage" is for a step.** Options: the receipt's `gov_commit`, every step
  introduced after it; the receipt's own `steps` record, every step up to `--to` it does not record
  `applied`. The final stamp moves `gov_commit` on a `--kits`-scoped run too
  (`tools/govkit/govkit.py:12440`), and `apply` writes it fresh, so under the first a step those
  runs passed never runs, which fails the clause's "walking every step". RESOLVED (agent, 2026-10-23,
  delegated): the step record, on rung 3. For a receipt every walk has written, the two sets are
  equal; they differ only where `gov_commit` moved without a walk, and there the second walks what
  the first strands. widens: none · relaxes: none
- **F2 — Whether a read-only `update` probes witnesses.** Options: spawn each witness and print its
  verdict; list each pending step as `would walk` and spawn nothing. USAGE says `update` "writes no
  byte" read-only (`tools/govkit/govkit.py:13608`), and a witness is step code over the
  target. RESOLVED (agent, 2026-10-23, delegated): spawn nothing, on rung 3; the preview names the
  pending set, and `--write` is where the witness is read. widens: none · relaxes: none
- **F3 — A `--kits`-scoped run.** Options: walk the in-scope kits' steps; walk nothing and print the
  pending count. Walking a subset runs a later step before an earlier one out of scope, against the
  clause's "oldest first", so veto 1 discards it. RESOLVED (agent, 2026-10-23, delegated): walk
  nothing, on rung 3; F1's pending rule walks them at the next unscoped run. widens: none · relaxes:
  none
- **F4 — The staged half of `gap-deploy-19`.** The clause names the lock; the gap names the lock and
  the staged paths. Options: reclaim the lock only, leaving staged paths an operator clears; restore
  the killed run's pre-write snapshot, which would also undo an operator's edit staged after the
  kill; the staging journal of S8, an exact oid per staged path. RESOLVED (agent, 2026-10-23,
  delegated): the journal, on rung 3, the most capable option the vetoes leave: it closes the gap,
  adds no surface beyond the lock's own directory, and keeps an operator's different blob dirty.
  widens: none · relaxes: none
- **F5 — The parent, dGroundRules, is unbuilt.** RESOLVED (agent, 2026-10-23, delegated): this unit
  reads no key of `.governance/policy.toml` and calls no policy reader, so `cl-dClosedLoop-0007` and
  `cl-dClosedLoop-0008` bind nothing here; the build run re-grounds against the landed parent before
  its first pass, and an interface the parent lands that this unit should read is an M2 amendment.
  widens: none · relaxes: none
- **F6 — Names spelled by a sibling.** The row reader, `resume`'s values and the writer
  `set_step_state` are TOOL-dSafePassage-1's and TOOL-dSafePassage-3's, written concurrently; this
  spec was cross-read against both drafts on 2026-10-23, and the progress row's `introduced` for a
  step not yet landed reads `unlanded` in TOOL-dSafePassage-1 and `null` in TOOL-dSafePassage-3, a
  difference this unit only carries through. RESOLVED (agent, 2026-10-23, delegated): this spec
  spells the keys as the brief's S1, S4 and S5 fix them; the M2 cross-read before the first code pass binds any difference,
  fixed in whichever document is wrong with a rev bump. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-15`, `TOOL-dSafePassage-19`, `TOOL-dSafePassage-22`, `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the hands-off `TOOL-dSafePassage-8` that unit's
  consumes-from already declared, so the reciprocity join of hygiene check 12 holds; no other
  section moved.
- rev-4 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-33`; no other section moved.
- rev-5 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-40`; no other section moved.

## 10. Reuse audit

The seams extended are govkit's write preconditions: `take_write_lock`, `describe_write_lock` and
`release_write_lock` (`tools/govkit/govkit.py:7394-7446`), `dirty_claimed_paths`' third carve-out
(`tools/govkit/govkit.py:7113-7116`), and `_cmd_update` between its HOLD REGION END and its re-render
(`tools/govkit/govkit.py:11197-11202`). Process liveness reuses the process-monitor census,
`scan_processes` (`tools/process-monitor/census.py:260-281`), loaded as `load_process_monitor` loads
it. The guard follows the break-guard of TOOL-aGraftedHelix-37
(`memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-37.md`, S1 and S2), with
liveness where that lock uses a deadline. `reuse_lookup.py "walk ordered upgrade steps between two
vintages, skipping a step whose witness holds, advancing a receipt per step"` ranked `skipped`,
`walk` (`corpus_ids.py`), govkit's `step` (a phase-line printer over its reserved `STEPS` tuple,
`tools/govkit/govkit.py:98`), `vintage`
and `map_from_receipt` (`census.py` of govkit): none walks a step, and `step` is a name match, not a
seam. `reuse_lookup.py "reclaim a stale write lock whose holder process is dead"` ranked
`check_claim_push_lock_stale` (`tools/unattended/unattended.sh:2325`), which judges by deadline, and
did not rank `read_process_created` or the census, which this unit found by reading
`measure_legs.py`; that is where the hits and the source disagree. The recall probe found the shape
audit's H4 (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-b.md`),
whose fix this clause is, and DEPL-dCarriedReceipt-12, which landed the lock.

Recall terms used: `python tools/memory-recall/query.py "how does update walk upgrade steps, record progress in the receipt and recover a lock a killed run left" --terms "upgrade step walk witness receipt steps vintage stale lock reclaim pid killed resume"`
