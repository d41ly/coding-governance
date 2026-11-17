# TOOL-dDeclaredLoop-6 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-6

No merge bar, no self-test suite and no gate leg ran in this pass, and `factories.py --selftest` was not
run. The criteria were observed on node `d` (win32), at rev-7 of the spec, by probes of the unit's own
code: each of the eleven plants run alone by direct CLI from the loop kit's folder, each building its
own scratch clone of the working tree that held this diff; `check-commands` and the slot refusal over
the tree; `core.check_kind_row` called through `python -c` on the five filled rows; and greps and a
`json.load` over the registries.

Owed to the close: every leg the spec's section 7 names, `core kinds` and `core meta-check` among them,
the two new legs `loop command conformance` and `loop factories fixtures`, and the RED-first
observation of the `New arm:` line, each `-hand` case staged in its scratch clone. The exit 2 path of a
kit that does not resolve was not probed. The fixture leg's run time was not read: its budget row is a
proxy priced from the plants run alone, and that proxy sits above the leg's manifest ceiling, which
the close reads from the leg itself.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
The `command-hand` plant of `tools/loop/factories.py`, whose planted defect is the staged break, exited 1 over
its scratch tree, its last line reading `factories: fixture · command-hand · gate loop command conformance
exit 1`; the leg over the tree read green at HEAD: RED observed.
The `hook-hand` plant of `tools/loop/factories.py`, whose planted defect is the staged break, exited 1 over
its scratch tree, its last line reading `factories: fixture · hook-hand · gate hook destinations (every
declared hook path ships) e`; the leg over the tree read green at HEAD: RED observed.
The `role-hand` plant of `tools/loop/factories.py`, whose planted defect is the staged break, exited 1 over
its scratch tree, its last line reading `factories: fixture · role-hand · gate roles catalogue exit 1`; the
leg over the tree read green at HEAD: RED observed.
The `workflow-hand` plant of `tools/loop/factories.py`, whose planted defect is the staged break, exited 1
over its scratch tree, its last line reading `factories: fixture · workflow-hand · gate roles catalogue exit
1`; the leg over the tree read green at HEAD: RED observed.

**Evidences:** TOOL-dDeclaredLoop-6
- AC1 — `kind.command` — `grep -cP '^kind\tkind\.(command|policy-key|hook|role|workflow)\t' tools/playbook/core-pending.txt` printed 0, and `core.check_kind_row` returned no red and conforming for each of `kind.command`, `kind.policy-key`, `kind.hook`, `kind.role` and `kind.workflow`; the `core.py kinds` exit is owed to the close.
- AC2 — `command-hand` — `--plant command-new` exited 0 ending `factory exit 0 · gate green`; `--plant command-hand` exited 1 naming `command.loop.hand`, its run naming no file git holds under the loop kit's folder.
- AC3 — `arm_mirror_parity` — `--plant policy-key-new` exited 0, the factory printing the `policy-check:` lines of `arm_schema`, `arm_shape`, `arm_summaries` and `arm_direction`, each with no finding, and no `arm_mirror_parity` line, the clone's porcelain holding the catalogue alone; `--plant policy-key-hand` exited 1, its `arm_shape` finding reading `fixture.hand: lacks the required field owner`.
- AC4 — `kind.stage` — the grep printed the pending row naming dDeclaredLoop, and the register's `kind.stage` row still carries an empty factory.
- AC5 — `hook-dest: ok` — `--plant hook-new` exited 0, the factory's own gate run printing a `hook-dest: ok` line naming `fixture-hook.fragment.json` and the clone's `git diff --cached --name-only` printing nothing; `--plant hook-hand` exited 1 on a `hook-dest: FAIL` line naming `fixture-hand.fragment.json`. No throwaway index directory was left in the system temp folder.
- AC6 — `role-hand` — `--plant role-new` exited 0 with `check_roles.py --write` green; `--plant role-hand` exited 1 on an R2 line, front-matter key `writes` missing.
- AC7 — `workflow-hand` — `--plant workflow-new` exited 0 with `check_roles.py` and `loop_lib.py --check` green; `--plant workflow-hand` exited 1 on an R8 line naming `gov-nobody`.
- AC8 — `principle.p16` — `json.load` of `tools/gate-legs.json` read `principle.p16` in the `enforces` of the three wrapped legs and the two new ones, each with `stage` `step.test`; the leg-row grep of the pending list printed 0; the `core.py meta-check` exit is owed to the close.
- AC9 — `dKeptSession` — the grep printed the `kind.preset` pending row naming dKeptSession, and the register's row reads that owner.
- AC10 — `factory-restores` — exited 1, the factory printing an `arm_shape` finding reading `fixture.bad: its own row refuses its default`, no `arm_mirror_parity` line, and the plant line reading `porcelain clean`.
- AC11 — `kinds.md` — after `render_playbook.py --reference`, the usage grep over the page printed 5 (PINNED, one usage line per kind), and its `kind.preset` section names dKeptSession.
- AC12 — `Making a new part` — the heading grep over the loop help page printed the heading, `factories.py` counts 14 (PINNED) in the govkit usage file, and `docs_leg.py --fingerprints` prints each of the seven factories rows (PINNED) against the loop help page.
- AC13 — `Bad_Slot` — the role factory over the tree exited 2 printing `refused · the slot 'Bad_Slot' is not [a-z][a-z0-9-]* · nothing written`, and `git status --porcelain` named no path the factory could write.
