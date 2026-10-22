# TOOL-dSafePassage-9 — withdrawn hook fragments unwired, and an edited file gov stopped shipping kept as `retired-edited` and ordered

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0026@97d3c99b whole
**Carries:** node:policy-key.install.retired-edits

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |

<!-- /gen:spec-records -->

## 1. Goal

`update` stops leaving three adopter states silent. A hook fragment gov withdrew is taken out of the
adopter's settings, so the withdrawn hook stops running. A file gov no longer ships that the adopter
edited becomes a receipt state of its own, `retired-edited`, kept and ordered as
`install.retired-edits` says, never graded `patched` with no order and never `forked`. And a rendered
file the adopter edited since its last render is named and held with an order, never overwritten and
reported `re-rendered`. Today an adopter's edit to a file gov retired reads as patched with no order,
and a withdrawn hook stays wired (`gap-deploy-18`, closed by this unit). SA-2 moved all three into
this build: "move hook unwiring, retired-edit orders and stale-lock reclaim into dSafePassage".

## 2. Scope (IN)

- **S1** — Withdrawn hook fragments unwired. Under `update --write`, a receipt row whose path ends
  `.fragment.json` and whose verdict is `withdrawn` has its settings entry taken out through the
  target's own `settings-merge.py --unwire --fragment`, before any deletion `--write-withdrawals`
  makes, because `--unwire` reads the fragment. An unwire that fails, or one the target-code switch
  declines, leaves the entry wired, says so on one line, and withholds the fragment's deletion. When
  the same run rolls the row's kit back, the rollback wires again what this run unwired. Observed by
  AC1 and AC2.
- **S2** — The state of its own. Govkit's verdict-grid cell for a file the target changed and gov no
  longer ships, (`differs`, `absent`), answers `retired-edited` in place of `patched`. Under
  `--write` that row's receipt role is set to `retired-edited`, its other fields kept, and no run
  writes or deletes its bytes, `--write-withdrawals` included. On every later run the row's own role
  dispatches it. Observed by AC3 and AC4.
  **Readers:** by name: `VERDICT_GRID` in `tools/govkit/govkit.py`, read by `classify_row` and by
  selfcheck's arms 7g and 7i. by value: the verdict tally and line `_cmd_update` prints, and the
  verdict arms of `tools/govkit/selftest.py`, which read each row's verdict word through `verdict_of`.
- **S3** — The new state of S2 gains its own row in `UPDATE_ROLE`, the disposition `order`, and its
  own row in `UNLANDED_REASON`, so selfcheck arm 7g, whose known roles are built from
  `UNLANDED_REASON`, demands the dispatch row. Arm 7g's two completeness loops move into
  `derive_dispatch_gaps`, which selfcheck calls with the module's tables and a fixture calls with a
  copy, so the arm is seen to speak. Observed by AC5.
- **S4** — The order, as `install.retired-edits` says. Under `order`, the default, the row is graded
  the order: one outbox order is written for it by the writer the `withdrawn` arm uses today, and
  its line names the order. Under `keep`, no order is written, and the row is still named in
  update's report with the mode that kept it, never silent. Neither value grades the row `forked`.
  Observed by AC4, AC6 and AC7.
- **S5** — The edited render. A `rendered` row whose working file, cleaned by the target's own
  filters, is no longer the blob the receipt recorded at its last render is the verdict
  `render-edited`: named at update, its kit held back through `_add_held` so its regenerate does not
  run over the edit, and an outbox order written for it. It is never reported `re-rendered`. A row
  whose receipt recorded no render blob cannot prove an edit and is graded as today. Observed by AC8
  and AC9.
- **S6** — The policy key: one catalogue row for `install.retired-edits`, values `order` and `keep`,
  default `order`, with its summary and usage as the parent's catalogue clause requires, from v2's
  `[policies]` row (v2:1406). The value is read from the target's policy, since the choice is the
  adopter's. Observed by AC10.
- **S7** — The fixture, `tools/govkit/fixtures/retired_edits.py`: `--plant <case>` builds a scratch
  gov and an installed target, stages one case, runs `update --write`, and prints each verdict line,
  each order, each settings entry and each receipt role it observed beside what the case expects;
  `--stub <name>` runs the same case over a copy of govkit with one named mapping stubbed, which is
  how each red the clause names is seen. Observed by AC1 to AC9.
- **S8** — The docs: a page `help/update-edits.md` saying what `update` does with an edited file gov
  stopped shipping under each value of the key, with an edited render, and with a withdrawn hook,
  and its line in `help/README.md`. Observed by AC11.

## 3. Non-goals (OUT)

- Deleting an edited file gov stopped shipping. `delete` was dropped from the key by the owner's
  FK-1-4 with FK-3-1, "Drop delete and refuse (Recommended)", because it lost edits.
- A receipt schema bump. S2 adds a role value and no row field, and `RECEIPT_SCHEMA`'s rule bumps on
  a new per-role row field (`tools/govkit/govkit.py:49`); the schema-4 bump is TOOL-dSafePassage-3's.
- A row that returns from `retired-edited` to its old role once the adopter reverts its edit. It is
  reported `withdrawn` and keeps its role until the operator's next `apply`; §4 "### What it does not
  check" names it.
- The stale-lock reclaim SA-2 also moved here: TOOL-dSafePassage-2's.
- The forwarders a moved surface keeps: TOOL-dSafePassage-6's.
- Fixing an edited render for the adopter. The order says how; the adopter resolves it.

### Edges

- **consumes-from** external — dGroundRules' policy file, its catalogue (`cl-dClosedLoop-0007`) and its reader (`cl-dClosedLoop-0008`, `read_policy_key`); without them the key reads its default, `order`, and S6 has no catalogue to join

## 4. Design

### The verdict grid and the dispatch

In `tools/govkit/govkit.py`:

| Where | Today | After |
|---|---|---|
| `VERDICT_GRID[("differs", "absent")]` (`:8425`) | `"patched"` | `"retired-edited"` |
| `UPDATE_ROLE` (`:8478-8503`) | no row for the state | `"retired-edited": "order"` |
| `UNLANDED_REASON` (`:405-421`) | no row for the state | `"retired-edited"`: the target edited a file gov no longer ships, so gov keeps the target's bytes and orders it |
| arm 7g (`:2729-2762`) | two inline loops | `derive_dispatch_gaps(update_role, unlanded_reason, landable_roles, grid)` returning the same messages, byte for byte |

`retired-edited` is deliberately not in `ROLE_KINDS`: like `adopter-owned` (`:416-420`), it reaches a
receipt only through `update`, so arm 3b refuses a descriptor that spells it. It is not in
`RAW_WRITE_VERDICTS` or `TOUCHING_VERDICTS` (`:8439-8455`), so arm 7i's no-clobber assertion holds over
the new cell structurally and the row's kit is not verified for a write it never made.

`check` and `check-receipt.py` already grade a non-engine row by existence or not at all
(`govkit.py:5472-5480`, `tools/run-gates/check-receipt.py:90`), so neither reds on the new role.

### The write loop

One arm sits before the write loop's `a["how"] != "table"` guard (`:10518`), for the verdicts in a new
`ORDERED_VERDICTS = ("retired-edited", "render-edited")`, so both a first-time engine row and a row
already carrying the role reach it:

1. `read_retired_edits_mode(target)` reads `install.retired-edits` once per run through the parent's
   reader, `read_policy_key` (`cl-dClosedLoop-0008`), over the target's policy, default `order`. A
   value outside `order` and `keep` is a refusal naming the key and both values, and holds the row's
   kit. The render-edited verdict ignores the mode: it is always ordered.
2. Under `order`, `write_row_order(outbox, kind, row, to_commit, body)` writes
   `.governance/outbox/update-<kind>-<slug>.md`, `<slug>` from `render_order_slug`, with `kind`
   `retired-edited` or `render-edited`. It is the `withdrawn` arm's writer (`:10760-10768`), extracted
   at this second caller, and the `withdrawn` arm calls it for its own order with bytes unchanged.
3. `render_retired_edited_line(row, mode, order_path)` returns the row's report line, the order's
   path under `order` and `kept, no order (install.retired-edits = keep)` under `keep`, and the loop
   prints it. The tally counts the verdict word.
4. A first-time engine row has its `role` set to `retired-edited`; its `path`, `source`, `commit`,
   `gov_oid` and `kit` stay, so later runs classify it from the same fields. The role change moves no
   byte, so a rollback leaves it, as the existing `role-recorded` branch leaves its role (`:9771`).

The order's body says gov no longer ships the file, that the copy carries the target's edit, that
nothing was deleted, and that deleting the file once the edit has moved lets the next `update` close
the row.

### The edited render

In the classification loop, inside the hold region (`:9659-11197`), before the cap that turns a
`rendered` row's `diverged` or `stale` into `re-rendered` (`:10001-10002`):
`check_render_edited(target, row)` runs `git hash-object --path=<path>` over the working file, the
same cleaning `measure_rendered_rows` stamped the row's `oid` with (`:9107-9115`), and is true when a
recorded `oid` differs from it. True makes the verdict `render-edited`, calls `_add_held` for the
row's kit, so the held-kit decline (`:11272-11277`) keeps its regenerate from running, and sends the
row to the ordered arm above. The working file is read rather than the index entry, because a
regenerate may leave its output unstaged and an index read would then call an untouched render
edited (`:9090-9093`).

### The withdrawn fragment

In the `withdrawn` arm (`:10741-10778`), for a row whose path ends `.fragment.json`, before any
`unlink`: when the target-code switch is on, `remove_wired_fragments(target, rows, [path], "update",
cause="withdrawn")` takes the entry out. That function (`:6180-6193`) gains the `cause` parameter for
its line, `unwired by the rollback` or `unwired, gov no longer ships it`, and returns the fragments it
unwired; its rollback call (`:11685`) prints what it prints today. The switch read,
`os.environ.get("GOVKIT_RERENDER") != "0"` (`:11227`), moves above the write loop, unchanged, so the
arm reads the one value the wiring step reads. A fragment this run unwired is recorded per kit, and a
rollback of that kit calls `run_fragment_merges` (`:6109-6177`) over it after its files are restored,
so the entry comes back with the bytes.

### What it does not check

A `retired-edited` row whose target later reverts its edit grids to `withdrawn` and is reported only,
keeping its role, until `apply` re-records it. A render whose receipt row carries no `oid`, as a
receipt older than DEPL-dRemeasuredRender-1 does, is never called edited. A hook entry the adopter
wired by hand, with no fragment row in the receipt, is never unwired.

### The fixture

`tools/govkit/fixtures/retired_edits.py` builds a scratch gov holding one kit, an engine file, a
rendered file with a `[[regenerate]]` argv, a hook fragment and a `settings-merge` entry, by copying
`tools/govkit/govkit.py` into it as `check_update_safety` does (`tools/govkit/selftest.py:1728-1737`),
installs a target from it, stages the case, and runs `update --write`. A `--stub` run loads the scratch
copy as a module, sets the stubbed name, and calls its `main`, so the break is staged in the copy and
never in the tree.

| `--plant` | Stages | Expected |
|---|---|---|
| `fragment-withdrawn` | gov stops shipping the fragment | the settings entry gone, the fragment file kept, the `withdrawn` order written |
| `fragment-withdrawn --write-withdrawals` | the same, with the flag | the entry gone, then the file gone |
| `fragment-withdrawn --rerender-off` | the same, the switch off | the entry and the file kept, one line naming the switch |
| `fragment-rollback` | the same, and the kit's check made to red | the entry wired again after the rollback |
| `edited-gone` | the target edits the engine file, then gov stops shipping it | verdict `retired-edited`, the order written, the receipt role `retired-edited`, the bytes kept under `--write-withdrawals` |
| `edited-row` | a receipt row already carrying the role | verdict `retired-edited` and the order, no `forked` line |
| `keep` | `edited-row` under `keep` | the row's line naming `keep`, no order |
| `render-edited` | the target edits the rendered file | verdict `render-edited`, the kit held back, the order written, the edit's bytes kept |
| `render-clean` | an unedited render, gov's template moved | `re-rendered`, as today |
| `dispatch-gap` | `derive_dispatch_gaps` over a copy of `UPDATE_ROLE` lacking the row | one message naming the role |

The stubs: `forked` sets the role's dispatch row to the `forked` row's disposition; `report-omits`
makes `render_retired_edited_line` return nothing; `today` makes `check_render_edited` return false.
A plant exits 0 when every observation matches its case and 1 otherwise.

### Inventory

Minted: the verdicts `retired-edited` and `render-edited`; the role `retired-edited` and its
disposition `order`; the constant `ORDERED_VERDICTS`; the functions `derive_dispatch_gaps`,
`read_retired_edits_mode`, `write_row_order`, `render_retired_edited_line` and
`check_render_edited` in `govkit.py`, and `run_fixture` and `main` in the fixture module; the
`cause` parameter of `remove_wired_fragments`; the order names `update-retired-edited-<slug>.md` and
`update-render-edited-<slug>.md`; the fixture flags `--plant`, `--stub`, `--write-withdrawals` and
`--rerender-off`. Naming cells: each minted function passes `py.function`
(`tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for all seven). Owned node:
`policy-key.install.retired-edits`, the catalogue row of S6.

### Migration

Additive for every receipt in the field: no row carries the new role until a run sets it, and the
cell change only renames a verdict that wrote nothing before. A target whose edited retired files
read `patched` today reads `retired-edited` on its next run and receives an order, which is the gap
closing.

### Rollout

Live at landing in gov's own deployer. The deployer never travels, so an adopter meets it on its
next `update`. `govkit.py` is also written by TOOL-dSafePassage-6 and TOOL-dSafePassage-10, so the
three passes sequence rather than run concurrently (M6).

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/fixtures/retired_edits.py` (new)
- `tools/govkit/selftest.py`
- `help/update-edits.md` (new)
- `help/README.md`

The catalogue row also goes into the catalogue file `cl-dClosedLoop-0007` defines, whose path the
build run re-grounds against the landed parent (§8 F4) and adds to this unit's `--dispatch --writes`.

### Alternatives rejected

- **Marking the row `forked`.** A fork is gov's copy derived from the target's, reported in both
  directions and written in neither, with no order (`UNLANDED_REASON["forked"]`, `:414-415`); the
  clause says never `forked`, and the owner's AP-28 says never graded as a fork.
- **Re-rendering an edited render and keeping the edit as a conflict candidate.** The regenerate
  writes under the kit's own authority with no three-way (`KIT_WRITING_DISPOSITIONS`, `:8522-8541`),
  so the edit would be lost before any merge could see it. §8 F2.
- **Holding only the edited row while the rest of the kit renders.** The regenerate argv is keyed on
  the kit, not on a row, so standing back from one row does not stand back from the argv
  (`:8528-8536`).
- **A second order writer per verdict.** The `withdrawn` arm's writer is extracted at its second
  caller, as the clause asks, rather than copied.

## 5. Production-readiness checklist

- security: no new write path into the target beyond the outbox order writer `update` already uses; every path stays under `update`'s containment check (`:10501-10511`); an unwire runs the target's own `settings-merge.py` under the same switch that already gates target-side code.
- perf / scale: one `git hash-object` per `rendered` row with a recorded `oid`, and one `settings-merge.py --unwire` per withdrawn fragment, each per run.
- error / empty / loading states: an unknown key value refuses and holds the kit; a failed unwire keeps the entry and the file and says so; a render with no recorded `oid` is graded as today and the line does not claim an edit.
- observability: every new verdict prints its row line with its order's path or the mode that kept it; the held kit prints the `HELD BACK` line it prints today.
- risks: a `retired-edited` row stays in that role after a revert (§4 "### What it does not check"); a target whose renders carry no `oid` gets no edit detection until a render re-stamps them.
- testing: the fixture plants and stubs of §4, run by AC1 to AC9 and by the new selftest arm (§7).
- migration: additive; §4 "### Migration".
- user docs: `help/update-edits.md` and its `help/README.md` line (S8).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/fixtures/retired_edits.py" --plant fragment-withdrawn` runs, it
  exits 0, its observations showing the fragment's settings entry gone, the fragment file still
  present and the `withdrawn` order written; with `--write-withdrawals` the entry is gone first and
  the file after; with `--rerender-off` both stay and one line names the switch.
  Red when: the arm deletes the fragment before unwiring it, or a withdrawn fragment's entry stays
  wired with the switch on.
- **AC2** — When `python "tools/govkit/fixtures/retired_edits.py" --plant fragment-rollback` runs, it
  exits 0, its observations showing the entry unwired during the run and wired again after the kit's
  rollback.
  Red when: a rollback restores the kit's files and leaves the unwired entry out.
- **AC3** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-gone` runs, it exits
  0, its observations showing the verdict `retired-edited`, one `update-retired-edited-` order, the
  receipt row's role `retired-edited` and the edited bytes still present with `--write-withdrawals`
  passed.
  Red when: the cell still answers `patched`, so no order is written.
- **AC4** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-row` runs, it exits 0
  with the verdict `retired-edited` and its order; with `--stub forked` it exits 1, its observations
  showing no order and the row graded as a fork.
  Red when: the role's dispatch row maps to the `forked` disposition, or the stub run exits 0.
- **AC5** — When `python "tools/govkit/fixtures/retired_edits.py" --plant dispatch-gap` runs, it exits
  0, its observation the one message naming `retired-edited` that `derive_dispatch_gaps` returns over
  the copy, and `derive_dispatch_gaps` over the module's own tables returns none.
  Red when: `UNLANDED_REASON` carries no row for the state, so arm 7g never asks for its dispatch row.
- **AC6** — When `python "tools/govkit/fixtures/retired_edits.py" --plant keep` runs, it exits 0, the
  row's line naming `keep` and no order written; with `--stub report-omits` it exits 1.
  Red when: `keep` makes the row silent in update's report.
- **AC7** — When `git grep -n -e "update-withdrawn-" -- tools/govkit/govkit.py` runs after the pass,
  the only writer of an outbox order for a row's verdict is `write_row_order`, and the `withdrawn`
  arm's order bytes on the `fragment-withdrawn` plant equal those the arm writes at `3708a705`.
  Red when: a second order writer is copied in for the new verdict.
- **AC8** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-edited` runs, it
  exits 0, its observations showing the verdict `render-edited`, the kit's `HELD BACK` line, one
  `update-render-edited-` order and the edited bytes unchanged; with `--stub today` it exits 1, the
  row reported `re-rendered` and the edit overwritten.
  Red when: an edited render is still capped at `re-rendered` and its kit's regenerate runs over it.
- **AC9** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-clean` runs, it exits
  0 with the row `re-rendered` and no order.
  Red when: an unedited render whose output was left unstaged reads as edited.
- **AC10** — When `git grep -n -e "install.retired-edits"` runs over the catalogue file the parent
  lands, the key's row carries the values `order` and `keep`, the default `order`, a summary and a
  usage.
  Red when: the key lands with no summary or usage, which `cl-dClosedLoop-0007`'s schema refuses.
  fixture: the catalogue's path is the parent's, re-grounded at the build run (§8 F4).
- **AC11** — When `git grep -n -e "retired-edited" -- help/` runs, it finds the page and its line in
  the help index.
  Red when: the state ships with no page under `help/`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC9 · a new arm runs the fixture module over every plant of §4 and over the three stubs, asserting each exit · none

## 8. Open questions

- **F1 — Whether the new state is a verdict, a role, or both.** The clause asks for "a receipt
  state of its own" with "its own update-role and unlanded-reason rows". Options: a verdict only,
  re-derived each run from the grid; a role only; the cell's verdict on the first run and the role
  recorded from then on. A verdict only has no role row for arm 7g to demand. RESOLVED (agent,
  2026-10-23, delegated): both, rung 1, the clause naming the verdict-grid cell and the role rows
  together. widens: none · relaxes: none
- **F2 — What "held" means for an edited render.** Options: (a) the kit held back through
  `_add_held`, so its regenerate never runs over the edit; (b) the regenerate runs and the edited
  bytes are restored after it; (c) the regenerate runs and the edit is kept as a conflict
  candidate. (b) writes over the adopter's file and then reverses itself inside one run, and (c)
  loses the edit, since the regenerate has no three-way. RESOLVED (agent, 2026-10-23, delegated):
  (a), rung 3, the one option that never writes over the edit, and the seam the hold region already
  grades. widens: none · relaxes: none
- **F3 — The index or the working file for "edited since its last render".** Options: the target's
  index entry, as `classify_row` reads OURS; the working file cleaned by `git hash-object --path`, as
  `measure_rendered_rows` stamped the row. The index lags an unstaged render (`:9090-9093`) and would
  call an untouched render edited. RESOLVED (agent, 2026-10-23, delegated): the working file, rung 2
  in effect, AC9's `render-clean` plant being the observation that would show the index reading
  wrong. widens: none · relaxes: none
- **F4 — The parent is unbuilt.** The catalogue row of S6, the target's policy file and its reader
  are dGroundRules' (`cl-dClosedLoop-0007`, `cl-dClosedLoop-0008`), and none has landed. RESOLVED
  (agent, 2026-10-23, delegated): rung 1, v2's `[chain]` puts dGroundRules before this build; the
  build run re-grounds this spec against the landed parent first, spelling the catalogue file and the
  reader's call as the parent ships them. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seams extended are all in `tools/govkit/govkit.py`: the verdict grid (`:8419-8429`), the role
dispatch `UPDATE_ROLE` (`:8478-8503`) and `UNLANDED_REASON` (`:405-421`), whose completeness arm 7g
(`:2729-2762`) is extracted rather than copied; the `withdrawn` arm's outbox order (`:10741-10778`),
extracted into `write_row_order` at its second caller; `remove_wired_fragments` (`:6180-6193`) and
`run_fragment_merges` (`:6109-6177`), reused for the unwire and its rollback; the hold region and
`_add_held` (`:9659-9670`); and the render stamp `measure_rendered_rows` (`:9081-9122`), whose `oid`
the edit test compares against. `reuse_lookup.py "unwire a hook fragment from the settings file"`
ranked `run_fragment_merges` and the six wired hooks of the `harness-hooks` inventory, which is the
seam taken; `reuse_lookup.py "write an outbox order for a file gov no longer ships"` ranked generic
writers (`write`, `write_text`, `write_record`) and no order writer, because the `withdrawn` arm's is
inline, which is why S4 extracts it. Where a record and the source disagree: the supersession
research cites the edited-withdrawn cell at `govkit.py:8048` and `:8078` and the hook wiring at
`:11062-11127`; at `3708a705` they sit at `:8425` and `:11437-11474`, and the unwire it cites at
`:11304` is the rollback call at `:11685`. The recall probe found the clause, the research's surface
table, DEPL-dCarriedReceipt-11's "`withdrawn` stops deleting silently", and the owner's FK-1-4 ruling
keeping `keep` with a planted case.

Recall terms used: `python tools/memory-recall/query.py "what does update do with an adopter-edited file gov stopped shipping, and does a withdrawn hook stay wired" --terms "retired-edited withdrawn verdict grid patched outbox order unwire fragment settings-merge re-rendered forked"`
