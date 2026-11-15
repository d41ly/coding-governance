# TOOL-dDeclaredLoop-25 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-25

No merge bar, no self-test suite and no gate leg ran in this pass, and `splice.py check --selftest` was
not run. The criteria were observed on node `d` (win32), at rev-7 of the spec, by probes of the unit's
own code: `splice.py check` over the tree and each of its cases run alone by direct CLI from the loop
kit's folder, the `factory` case building its own scratch repository from the working tree that held
this diff; `loop_items.py check` over the tree and its `factory`, `repo-unresolved-need` and
`schema-absent` plants by direct CLI; `derive_new_item_row`, `check_row_owners` and
`core.check_kind_row` called through `python -c`; the step gate's class readers and the `stage` plant
called in process over a shared clone of HEAD holding this diff; and greps and a `json.load` over the
registries.

Owed to the close: every leg the spec's section 7 names, `core kinds`, `core meta-check`, `step-gate`
and `govkit selftest` among them, the new leg `loop splice check`, the gate run of
`step_gate.py --fixture --plant stage` with and without `--with-row`, and the RED-first observation of
both `New arm:` lines. The exit 2 path of a kit that does not resolve was not probed. The new leg's run
time was not read: its budget row is a proxy priced from the cases run alone, and the close re-prices it
from the leg itself.

**Evidences:** TOOL-dDeclaredLoop-25
- AC1 — `adopter-security-review` — `--plant between-test-deploy` exited 0 printing the R1 line from `testing` into `adopter-security-review` on `item.test.exit` and the R2 line from there into `deploying` on `item.adopter.security-review.exit`, and the splice table line; `check_splices` refuses a split row that survives the spliced table, and none did.
- AC2 — `removes` — `--plant removes` exited 1 naming the gov stage `step.test` excluded; `--plant reorders` exited 1 reading `step.deploy and step.test are not adjacent in order`; `--plant replaces` exited 1 naming the stage `step.test` with no `adopter` seat.
- AC3 — `before-plan` — `--plant before-plan` exited 1 reading `no gov stage precedes it`, and `--plant after-deploy` exited 1 reading `no gov stage follows it`.
- AC4 — `non-adjacent` — `--plant non-adjacent` exited 1 naming `step.build` and `step.deploy`; `--plant two-splices` exited 1 naming `step.adopter.security-review` and `step.adopter.second-review`.
- AC5 — `step-gate: RED stage:step.plan` — over a shared clone of HEAD holding this diff, the registry read through `step_gate.read_surface_classes` loaded the `stage` class; every class reader ran on the base side and again after `write_stage_plant` took the first `[[step]]` table out, the `drive` reader raising on neither, and the vanished set was `stage:step.plan` alone, witnessed by no row. The gate run of the fixture, its exit 1 and its exit 0 under `--with-row`, is owed to the close.
- AC6 — `gov-rename` — `--plant gov-rename` exited 0 printing `loop: re-point step.adopter.security-review · after step.verify → step.test` and an R1 line leaving `testing`.
- AC7 — `stale-pin` — `--plant stale-pin` exited 1 naming the pin as stale beside the split row's own pin.
- AC8 — `item.adopter.ghost.check` — `--plant exit-elsewhere` exited 1 naming the exit `item.test.exit`; `--plant exit-unwitnessed` exited 1 naming `item.adopter.security-review.exit`, which carries no witness; `--plant orphan-item` exited 1 naming `item.adopter.ghost.check`.
- AC9 — `splice.py:read_stage_members` — the criterion's grep over the classes registry printed the `stage` row naming `splice.py:read_stage_members`, `splice.py:write_stage_plant` and `pins.py:read_change_successors`.
- AC10 — `loop: splices composed · 0 splice(s)` — `splice.py check` over this repository exited 0 printing that line and nothing else (PINNED: the overlay holds no stage row at the pass).
- AC11 — `principle.p20` — the pending grep printed 0 (PINNED), `core.check_kind_row` returned no red and conforming for `kind.stage`, which `read_pending` no longer holds, and `json.load` read `principle.p16` and `principle.p20` in the `enforces` of `loop splice check`; the `core.py kinds` and `core.py meta-check` exits are owed to the close.
- AC12 — `factory` — `--plant factory` exited 0: the factory appended `step.adopter.demo` and `item.adopter.demo.exit` to the scratch's overlay, the commit landed, the scratch's `splice.py check` composed the stage, its `loop_items.py check` exited 0 counting one repository row (PINNED), and the same `core.py new stage demo` exited 2 naming `step.test` and `step.deploy`.
- AC13 — `Adding a stage of your own` — the heading grep over the loop help page printed the section heading, the usage grep printed the bare, `#check` and `#new` rows of `splice.py`, and `docs_leg.py --fingerprints` printed each against no page before the help page anchored them.
