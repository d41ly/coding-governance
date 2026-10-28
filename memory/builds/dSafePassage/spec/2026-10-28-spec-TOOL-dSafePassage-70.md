# TOOL-dSafePassage-70 — a rollback killed after the schema step's down resumes: the reverse walk persists nothing on a receipt already below schema 4, and stops only at the down that lowers it

**Status:** CLOSED · rev-1 · 2026-10-28 · node d · Tier-2 · base 717bf240 · streams tooling · order 8 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-35

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-70-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-70-ledger.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-71 |
| [2026-10-28-prompt-TOOL-dSafePassage-70-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-70-build-brief.md) | journal | — |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-35's build measured a rollback killed after `govkit/receipt-schema-4`'s down and
before the stamp, over rows shaped as the shipped ones, as unresumable. The re-run of the same
`update --rollback --to A --write` exits 2 with
`govkit: a receipt at schema 3 has no steps to record 'fx/s2' in`, because move 3 of
`run_reverse_walk` persists `down interrupted:` on a receipt the killed schema down already lowered.
Past that refusal, the `LOWERED_STOP` test would stop the walk at its first row. This unit gives the
reverse walk one rule for that receipt: a row's records are written only where the receipt can hold
them before its down, and the walk stops only at the down that took the receipt below schema 4. A
re-run from that state then downs again each row whose witness still holds, records nothing, and
finishes to the stamp. It carries TOOL-dSafePassage-35's S19 and AC17 (id 42 of the round-1 audit
of units 15 to 26), moved here on 2026-10-28.

## 2. Scope (IN)

- **S1** — The rule. In `run_reverse_walk` (`tools/govkit/upgrade_steps.py:1485-1571`), each row reads
  `held = test_steps_recordable(receipt)` after move 1's witness re-read and move 2's attended test,
  before move 3. Move 3's `write_step_record` of `down interrupted: ...` (`:1539-1541`) runs only
  where `held` is true. The `LOWERED_STOP` test (`:1549-1550`) fires only where `held` is true, the
  re-read after the down reads `test_steps_recordable` false, and the row is not the last. The
  records after the down are already guarded by `recordable` (`:1546-1547`, `:1562-1563`,
  `:1567-1568`) and keep that guard. So on a receipt below schema 4 when the walk starts, every
  down runs and is judged as on a schema-4 receipt, writes no row, and returns its verdict in
  `downs` (TOOL-dSafePassage-18 S2), and the walk reaches its last row. `update` then moves the
  file rows and stamps, as after any unstopped reverse walk (`tools/govkit/govkit.py:10944-10952`).
  The docstring of `run_reverse_walk` (`:1487-1512`) states the rule, and the module's
  reverse-walk paragraph (`:83-92`) says the `down interrupted:` failure is persisted where the
  receipt can hold it. Observed by AC1 and AC2.
- **S2** — The plant, TOOL-dSafePassage-35's S19 moved here. The `rollback-update` family of
  `python3 "tools/govkit/upgrade_steps.py" fixture` gains `schema-step-kill-shipped-rows`, a member
  of `ROLLBACK_UPDATE_SCHEMA_PLANTS` (`:2598`). Its scratch gov is `build_update_gov`'s
  (`:3221-3274`) with targets `t` and `t2`, schema-3 receipts and the steps `fx/s1` and `fx/s2`.
  `fx/s2` has the floor row's shape: it declares `reverted = "down-exit"` and its witness always
  holds (`s2.witness-always`, `:2469`), as `lib/python-floor-3.15` reads the node
  (`tools/govkit/steps.toml:33-37`). `fx/s1`'s witness holds while `s1.txt` is absent
  (`s1.witness-absent`, `:2466`), so the forward walk applies it by its witness alone and writes no
  before-image. `build_update_gov` gains a keyword `down_exit`, the slugs whose row it renders with
  `reverted = "down-exit"` through `render_fixture_row` (`:2628`). Both targets are updated A to B
  and committed. `t2`, the twin, is rolled back to A uninterrupted. `t` is killed once the schema
  step's down has renamed schema 3 into place (`schema.block-after`), then re-run with the same
  command. The plant shares the `schema-step-kill-before-stamp` branch (`:3826-3870`), with its own
  down-line expectation, and also prints how many times `fx/s2`'s and `fx/s1`'s downs ran on `t`.
  Observed by AC1.
- **S3** — The docs. The rollback section of `help/upgrade-steps.md` says, under a new bullet
  **After a kill past the schema step**, that a rollback killed after `govkit/receipt-schema-4`'s down
  leaves the receipt at schema 3 with no `steps`. The same command again witness-probes every step,
  runs the down again of each whose witness still holds, records nothing, since the receipt has no
  `steps`, and moves the files and the stamp. Its record names the schema step
  `skipped (nothing applied)`. The "What runs, in what order" bullet (`:223-232`) says a step is
  marked `down interrupted: ...` before its down where the receipt holds `steps`, and the fixture
  block (`:267-273`) gains the plant's line. Observed by AC3.

## 3. Non-goals (OUT)

- The forward walk below schema 4. TOOL-dSafePassage-15's `persist` is unchanged.
- A progress marker so a re-run skips rows already downed. TOOL-dSafePassage-35 §8 F2 accepted the
  idempotent second down, which is TOOL-dSafePassage-19 S4's own design.
- A re-run record equal to the twin's on the schema step's line. No verdict of the killed run
  survives the kill (TOOL-dSafePassage-19 S4), and the schema step's witness cannot hold at schema 3
  (`tools/govkit/steps/receipt_schema_4.py:75-78`).
- A suffix on a verdict the receipt cannot hold, as the forward walk's `NOT_RECORDED_SUFFIX`.
  TOOL-dSafePassage-18 S2 returns that verdict as `rolled-back`, and the record compare of AC1 rests
  on it.
- The `schema-step-kill-before-stamp` plant and its expectations, which stay as they are.

### Edges

- **consumes-from** `TOOL-dSafePassage-35` — S19 and its criterion AC17 (id 42), moved here on 2026-10-28, with S20's reading of the idempotent second down and §8 F2's ruling on it, which this unit's AC1 observes

Read and closed, so named here rather than joined: TOOL-dSafePassage-2's `run_step_reread` and
`write_step_record`; TOOL-dSafePassage-4's `run_reverse_walk`, `derive_reverse_steps` and
`update --rollback`; TOOL-dSafePassage-62's receipt written before the forward walk, which the
fixture's A-to-B update runs through; TOOL-dSafePassage-16's `test_steps_recordable` and its refusal
in `set_step_state`; TOOL-dSafePassage-17's `derive_down_verdict`; TOOL-dSafePassage-18's
`LOWERED_STOP` and verdict list; TOOL-dSafePassage-19's `schema.block-after` kill and the twin
compare; and TOOL-dSafePassage-33's no-record branch. The edge join counts CLOSED specs
(`tools/memory-tree/check-memory-hygiene.sh:2717-2720`, `:2928-2931`), and a CLOSED spec cannot
take the matching `hands-off` line.

## 4. Design

### The rule, derived from the code

Move 3 persists `down interrupted:` before the spawn so that a killed down leaves its row marked for
the re-run (TOOL-dSafePassage-4 S4). Below schema 4 no row can hold that mark: `set_step_state`
refuses (`tools/govkit/upgrade_steps.py:837-840`), and the field's absence is the record
(TOOL-dSafePassage-18 S1). The forward walk answers the same question by asking
`test_steps_recordable` at each persist and writing nothing where it fails (`persist`, `:1374-1381`).
S1 gives move 3 the same question.

`LOWERED_STOP` exists because a down that lowers the receipt before the last row leaves the later
downs unrecordable (TOOL-dSafePassage-18 S3). That reason holds for the down that changed the
answer. A walk that starts below schema 4 has no record to lose: every down in it is unrecordable
from its first row, and a re-run re-probes each witness (TOOL-dSafePassage-19 S4). A down never
raises the schema, so `held` is true for every row before the first lowering, and false for every
row of a walk that starts below schema 4. Keying the stop on `held` makes it fire exactly at the
down that lowered the receipt.

```
for n, row in enumerate(rows, 1):
    move 1: a row recorded nowhere or rolled-back runs its witness, skipped where it does not hold
    move 2: an attended row stops the walk
    held = test_steps_recordable(receipt)                      # S1
    move 3: if held: write_step_record(... "down interrupted: ..." ...)
    move 4: the down, its re-read; recordable = test_steps_recordable(receipt)
    a non-zero down: recorded where recordable, stop
    if held and not recordable and n < len(rows): stop(row, LOWERED_STOP)     # S1
    move 5: derive_down_verdict, recorded where recordable (unchanged)
```

| Receipt before the down | After the down | Row | At HEAD | After this unit |
|---|---|---|---|---|
| schema 4 | schema 4 | any | move 3 persisted, the verdict recorded | the same |
| schema 4 | below 4 | the last | move 3 persisted, no record, `rolled-back` | the same |
| schema 4 | below 4 | not the last | `LOWERED_STOP` | the same |
| below 4 | below 4 | any | move 3 refuses and `update` exits 2 | no record, the verdict in `downs`, the walk goes on |

### The plant's rows

| Row | Shape | Forward walk A to B | Twin's rollback | Re-run on `t` |
|---|---|---|---|---|
| `govkit/receipt-schema-4` | the copied schema step | up, `applied` | down, `rolled-back` | witness fails at schema 3, `skipped (nothing applied)` |
| `fx/s1` | witness holds while `s1.txt` is absent | `applied` via its witness, no image | down by its exit, `rolled-back` | witness holds, downed again, `rolled-back` |
| `fx/s2` | `reverted = "down-exit"`, witness always holds | `applied` via its witness | down by its exit, `rolled-back` | witness holds, downed again, `rolled-back` |

Each second down writes nothing. `write_from_before_image` returns at once with no image
(`:715-717`), and the fixture step's down writes only its own reports beside the target. That is why
the re-run's receipt and target bytes can equal the twin's, while its record differs on one line.

### Inventory

Minted: the plant `schema-step-kill-shipped-rows` of the `rollback-update` family, which
TOOL-dSafePassage-35's inventory named and never built; and the keyword `down_exit` of
`build_update_gov`. Neither is a lexicon surface: the surfaces are `function`, `type`, `file` and
`constant`, by `python tools/lexicon/lexicon.py --suggest down_exit --as py.param` on 2026-10-28.
No function, conf key, gate leg, policy key or receipt field is minted. No `raise Refusal` site is
added, so `BRANCH_PIN` (`tools/govkit/refusal_join.py:41`) does not move.

### Migration

None. No recorded value changes. A receipt below schema 4 carries no step row before or after.

### Rollout

Live at landing, at order 8 beside TOOL-dSafePassage-35. Both write
`tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and `help/upgrade-steps.md`, so M6
sequences them: this unit builds after 35, whose S20 reading it observes.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **A walk-start flag, read once before the loop.** It gives the same verdicts on every reachable
  path, since a down never raises the schema. It is a second reading of the receipt beside the one
  each row already makes, and the forward walk asks per persist.
- **Delete the `LOWERED_STOP` test.** The re-run would then pass, and `schema-step-early` would down
  `fx/s1` over a receipt `fx/s2` lowered, recording nothing of it. AC2 is that case.
- **Skip every down on a receipt below schema 4.** A row whose witness holds would print
  `skipped (nothing applied)` while its effect is on disk. It contradicts move 1's rule and §8 F2 of
  TOOL-dSafePassage-35.
- **Lift the receipt back to schema 4 before the walk.** It writes a schema the rollback is taking
  away, and the stamp would have to take `steps` out a second time.
- **Refuse, naming the state.** The kill would then have no resume, which is the defect.

## 5. Production-readiness checklist

- security: no new spawn, argv, path or input. The downs run are the ones a schema-4 receipt's
  rollback already runs, under the isolation contract.
- perf / scale: none; one predicate call per row.
- error / empty / loading states: a down that fails on a receipt below schema 4 still stops the walk
  with its finding and writes nothing, and the next run re-probes.
- observability: each down prints its `step <id> · ...` line and its verdict reaches the run's record,
  as at schema 4.
- risks: a receipt never lifted to schema 4 whose rollback reaches a row with a holding witness now
  downs that row, where HEAD refused with exit 2. That is the treatment move 1 already gives a row
  recorded nowhere on a schema-4 receipt.
- testing: the plant through the arm of §7, and the `schema-step-early` row as the other side of the
  rule.
- migration: none.
- user docs: `help/upgrade-steps.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant schema-step-kill-shipped-rows`
  runs, it exits 0 with no `rollback-update: FAILED` line. It prints that the re-run exits 0, that
  its receipt's bytes equal the twin's, and that the target's bytes outside `.governance/outbox/`
  equal the twin's. It prints that the re-run's record equals the twin's line for line except two:
  the `started` line, which carries times, and the schema step's line, which reads
  `down govkit/receipt-schema-4: skipped (nothing applied)` where the twin's reads `rolled-back`. So
  `down fx/s2: rolled-back`, `down fx/s1: rolled-back`, the `files:` line and
  `gov_commit: moved to <A8>` equal the twin's. It also prints that `fx/s2`'s and `fx/s1`'s downs
  each ran twice on `t`.
  Red when: move 3 persists on the schema-3 receipt, so the re-run exits 2 naming
  `a receipt at schema 3 has no steps to record 'fx/s2' in`; or `LOWERED_STOP` fires on a receipt
  already below schema 4, so the re-run stops at `fx/s2`; or a second down changes a byte the twin
  does not hold.
  cost: about a minute, three scratch repositories.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant schema-step-early`
  runs, it exits 1 printing `step fx/s2 · STOPPED · receipt below schema 4 before the last down`,
  and `fx/s1`'s down does not run. This is TOOL-dSafePassage-18's AC3, green at HEAD, kept as the
  other side of S1's rule.
  Red when: the `LOWERED_STOP` test is deleted rather than keyed on `held`, so the walk downs `fx/s1`
  over the receipt `fx/s2` lowered.
- **AC3** — When `git grep -n -F "After a kill past the schema step" -- help/upgrade-steps.md` runs,
  it prints the new bullet, and
  `git grep -n -F "fixture rollback-update --plant schema-step-kill-shipped-rows" -- help/upgrade-steps.md`
  prints the fixture line.
  Red when: the page still says nothing of a re-run from a receipt the schema step's down lowered.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · a `check_step_rollback` row running the `rollback-update` plant `schema-step-kill-shipped-rows`, tagged `dSP-70`, its failing case staged by move 3's `held` guard taken out of a working copy · none

AC2's case is already the `schema-step-early` row of `check_step_rollback`
(`tools/govkit/selftest.py:3905-3906`), so no arm is added for it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft: TOOL-dSafePassage-35's S19 and AC17 moved here with the reverse
  walk's rule that makes them buildable, from that unit's second build pass, by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-35-4-spec-writer.md`.

## 10. Reuse audit

The seam extended is `run_reverse_walk`'s own record guard: the `recordable` reading TOOL-dSafePassage-18
put after each down (`tools/govkit/upgrade_steps.py:1543`), asked once more before move 3, as the
forward walk's `persist` asks it (`:1374-1381`). The plant extends the `rollback-update` family's
`schema-step-kill-before-stamp` branch (`:3826-3870`), and its rows reuse `FIXTURE_WALK_STEP`'s
`witness-always` and `witness-absent` switches (`:2465-2469`) and `render_fixture_row`'s `reverted`
(`:2628`). The arm is a row of `check_step_rollback`'s table (`tools/govkit/selftest.py:3860-3933`).
`python tools/codebase-map/reuse_lookup.py "resume a rollback killed after the schema step lowered the receipt below schema 4"`
ranked `step`, `read_steps`, `read_step_states`, `derive_reverse_steps` and `set_step_state`,
name-token matches; `derive_reverse_steps` and `set_step_state` are this path's, and none is a rule
for a walk that starts below schema 4, so no existing seam fits beyond the guard named above. The
recall probe ranked TOOL-dSafePassage-18's spec and ledger first, whose `schema-step-kill` re-run
starts at schema 4 because that kill lands before the rename, and TOOL-dSafePassage-19, whose
re-run downs nothing because its rows' witnesses fail after their downs.

Recall terms used: `python tools/memory-recall/query.py "what does the reverse walk do when the receipt is already below schema 4 at a rollback's re-run after a kill" --terms "reverse walk rollback re-run kill schema-3 receipt lowered stop down interrupted persist witness idempotent second down"`
