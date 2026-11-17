# TOOL-dDeclaredLoop-31 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-31

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`d` (win32), at rev-4 of the spec, by probes of the unit's own code: `budget.py`'s new plants, the
transition writer's new plant and the table's moves run alone by direct CLI, each plant in its own
scratch repository; `derive_ending` called by a `python -c` probe; the driver's exhaustion park run
through a scratch probe over `position.py`'s plant; and `guard.py --staged` run in a scratch repository
holding a copy of the policy kit's guard. The five new shell functions and three new Python functions
each passed `lexicon.py --suggest`, and `lexicon.py --check` read OK. The driver's census, read through
`tools/memory-tree/check-arms.py#branches` and `tools/memory-tree/check-arms.py#scan_refusal_sites`,
is 330 branches PINNED and 5 sites PINNED, 335 PINNED at the raised ceiling; no new message meets a
family of `tools/unattended/unattended.families.txt`. The help anchors carry the fingerprints
`docs_leg.py --fingerprints` printed.

The `loop budget fixtures` row is re-priced from the direct readings, as deviation 313 records, and
its proxy now sits above that leg's hang-bound ceiling, which the close reads.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of each `New
arm:` line: the `ending` and `driver-exhausted` plants staged against the base module and driver, the
`any-unending` plant and the ending moves against the base table, the `descope-spent` plant against
the base writer, and the driver suite's new arms, the three new refusals' signatures and the
exhaustion park's refused and admitted resume, against the base driver.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant ending` with the base module, which has no `ending` verb exited
1, and 0 once restored: RED observed.
`python tools/loop/budget.py --fixture --plant driver-exhausted` with the base module and driver, which have
no exhausted read exited 1, and 0 once restored: RED observed.
`python tools/loop/loop_transition.py --fixture --plant descope-spent` with every function the unit's pass
changed in `tools/loop/loop_transition.py` swapped back to its pre-pass source exited 1, and 0 once restored:
RED observed.
`python tools/loop/loop_table.py check --selftest` with every function the unit's pass changed in
`tools/loop/loop_table.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-31
- AC1 — `descope` — `derive_ending` answered `land-green` over one CLOSED and one WONTDO unit, `descope` over one CLOSED and one INPROGRESS, `close-incomplete` over one INPROGRESS and over none, `park-for-owner` and `close-incomplete` each over all CLOSED, and `lap` raised naming `flow.on-exhausted`; `--fixture --plant ending` printed `loop: budget · ending · descope · spent 0/0 · open TOOL-tFix-1 · disposed continue`, then `ending · none · unfrozen 0/8` under the default value, and `held`; figures PINNED by the plant's policy file.
- AC2 — `--exhausted` — `--fixture --plant driver-exhausted` printed `held`: the build slug's second round exited 1 naming `end the build with --exhausted tPos`, `--exhausted` exited 0 leaving one `decision · item flow.on-exhausted · reason ending close-incomplete · spent 0/0 · open TOOL-tPos-1` row, a second call exited 0 printing the recorded ending and adding no row, and a further round and a second dispatch each exited 1 naming `the build's ending is close-incomplete, and only the owner raises flow.rework-budget`.
- AC3 — `unfrozen` — the same plant's first `--exhausted`, under the default budget, exited 1 through `fail 37` naming `unfrozen 0/10`, the run-state file's bytes unchanged; figures PINNED by the plant's three units.
- AC4 — `budget-exhausted` — the same plant's abort with no exhaustion row exited 1 naming `the record holds no exhaustion row`, the bytes unchanged; under `close-incomplete` with `TOOL-tPos-1` open and both items attested it exited 1 naming that unit, and after `--rescope --act defer` it exited 0 with `phase: ABORTED`, `halt-code: budget-exhausted` and `main` resolving.
- AC5 — `item.flow.on-exhausted` — a scratch probe over `position.py`'s plant under `park-for-owner` with a declared `LANDER` ran `--exhausted`, then `--handoff --code owner-decision` to `phase HELD · code owner-decision · until owner`; `--resume --keepalive-id k2` exited 1 through `fail 57` naming the item, the record unchanged, and once a committed disposition record read `continue` the same resume passed the guard and stopped at the probe repository's remote, which advertises no HEAD. The suite's take-over and the plain `owner-decision` resume are owed to the close.
- AC6 — `36 row(s)` — `loop_table.py check` printed `loop: table build · 36 row(s)`, PINNED, at exit 0; the five ending moves answered `building → incomplete`, a refusal from `landed`, `parked → testing`, `parked → incomplete` and `testing → building · backward`; `--fixture --plant any-unending` exited 1 naming `only a row entering @reentry`; `read_transition_rows` held E1 to E5, each `draws = "none"`; and `loop_transition.py --fixture --plant descope-spent` printed `held`, the backward move on `item.test.attribute`'s `code-miss` refused naming the spent budget and the descope recording `testing -> building` on `@any` with no draw row.
- AC7 — `flow.rework-budget` — `guard.py --staged` in a scratch repository holding no run-state file, with a raise from `"4+2"` to `"6+2"` staged, exited 1 naming `flow.rework-budget` and `not a live run's branch`; AC2's `--exhausted` printed `only the owner raises flow.rework-budget`.
- AC8 — `--exhausted` — `grep -c -- '--exhausted'` read 3 over the verbs template and its render, `grep -c 'unattended.sh --exhausted '` read 1 over the Skill template and its render, the render measured 10848 bytes PINNED CR-stripped, its size row's figure, and `docs_leg.py --fingerprints` named both new anchors before `help/loop.md` carried them.
