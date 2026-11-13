# TOOL-dDeclaredLoop-1 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-1

No merge bar and no self-test suite ran in this pass, and no gate leg but the naming lexicon, which
the builder role allows and which exited 0. The criteria were observed through the unit's own
commands over the working tree where a command is no leg's argv, through the loop reader's
`--fixture --plant <case>`, through `python -c` probes that call the changed functions, and through
a scratch repository holding a copy of the roles kit and the loop kit side by side, where the
adopter's `--scaffold` and a probe of `check_roles.check_roles` stand in for the two roles legs. The
pass base is `9667ba4c`.

Owed to the close: the `roles catalogue` leg (AC3's first command), the `roles render wiring` leg
(AC4's own command), the `loop definition` leg (AC1's first command, a leg's argv since this pass
named it in the manifest), the `core meta-check` leg (AC10's second command), and the RED-first
observation of each `New arm:` line of the spec's section 7: `tools/loop/loop_lib.py`,
`tools/roles/adopt-roles.test.sh` and `tools/playbook/instruction_units.py`.

**Evidences:** TOOL-dDeclaredLoop-1
- AC1 — `bash adopt-loop.sh --check` — exited 0 and printed the steps `step.plan`, `step.design`,
  `step.build`, `step.test`, `step.deploy` in that order and one `loop: workflow` line for each row of
  the moved table, each with the order, step and reach word that table gives it. The adopter runs
  `loop_lib.py --check`, whose own argv is the new leg's and the close's to observe.
- AC2 — `read_workflow_order` — the `git grep` for a `stage = ` or `step = ` row in the roles
  catalogue printed nothing, and `roles_lib.read_workflow_order` over the roles kit returned `orient`
  1, `reuse` 2, `spec-write` 3, `spec-review` 4, `build` 5, `closing-review` 6, `gate-bar` 7, and
  `research`, `handoff` and `bookkeeping` 0.
- AC3 — `python tools/roles/check_roles.py` — NOT RUN: it is the `roles catalogue` leg's command. Observed in its place,
  by a probe calling `check_roles.check_roles`: no defect over the working tree, and no defect over
  the scratch copy of the two kits unplanted. There, with `stage = 3` planted on the `spec-write`
  row, one line `R6 — entry 3 (spec-write) has an unknown key 'stage'`; with the `handoff` row taken
  out of the loop definition, one line `R6 — the workflow 'handoff' has no [[workflow]] row in the
  loop definition, so no loop row places it`; with a row named `ghost` added there, one R6 line
  naming it; and with the `build` row's step taken out, one R6 line holding `the loop definition
  does not read` and `(build) carries no step`.
- AC4 — `bash tools/roles/adopt-roles.sh --check` — NOT RUN: it is the `roles render wiring` leg's command. Observed in
  its place over the scratch copy through `--scaffold`, which runs the same `render_skill`: exit 0
  unplanted; with `order = 9` planted on the `spec-write` row of the loop definition, exit 1 saying
  the heading `## Stage 3 — spec-write` says stage 3 but the order of the entry spec-write is 9 in
  the loop definition; a definition placing no workflow, a definition that does not read, and a
  copy with no loop kit each exited 2 on one line. Over the working tree `--scaffold` exited 0 and
  rewrote the Skill's one reworded sentence.
- AC5 — `python tools/roles/handoff.py stage-efforts build` — printed the JSON it printed before the first edit, byte
  for byte, and `render_agents.py --check` exited 0.
- AC6 — `--plant missing-step` — `reordered` exited 1 on `the step step.test is out of order: row 3 is
  step.build's place`; `missing-step` exited 1 on `the step step.deploy is missing`; `bad-step` exited
  1 on `workflow row 5 (build) step 'step.ship' is neither a declared step tag nor none`; `bad-reach`
  exited 1 on `workflow row 4 (spec-review) reach 'revew' is not one of entry review`.
- AC7 — `STEP_NAMES` — the `git grep -l` listed all four files, and `git grep -n -e "in its stage order" -e "STEP_NAMES" -- tools/roles/ help/roles.md`
  printed nothing.
- AC8 — `memory/map/features/` — the four greps each found their line: the dossier's `kits = ["loop"]`, the leg
  `"loop definition"`, the link in `help/README.md` and the registry's `id = "loop"`.
- AC9 — `python tools/playbook/instruction_units.py drive --list` — its lines equal, line for line and in order, the lines captured before the
  first edit, and `drive --check` exited 0. The fixture's new plant, `fixture --plant drive-order`,
  run alone, exited 0 on both expectations: the build row before the gate-bar row at the shipped
  orders, and the gate-bar row first with the two orders swapped.
- AC10 — `loop definition` — the manifest row carries `enforces` holding `principle.p1`, no `guard`,
  and the argv `python {prefix}/loop/loop_lib.py --check`, and `core-pending.txt` holds no
  `principle.p1` row. `core.py meta-check` NOT RUN: it is the `core meta-check` leg's command.
  Observed in its place: a probe calling `core.run_meta_check` over the working tree returned 0, its
  last line reading `meta-check · green`, and no line named the leg or a stale row.
- AC11 — `read_role_step` — the criterion's `load_sets.py check` command, its three `--reader` flags and `--reach`, printed the lines it printed before the first edit, byte for byte:
  reach units ending `.review` for the spec reviewer, `.plan` for the researcher, and no reach line
  for the orienter.

Beyond the criteria: the install-prefix ban's `--list` mode named three lines once a kit directory
named `loop` existed, each spelling that word as a path segment, in `tools/playbook/README.md`,
`tools/playbook/tag_index.py` and `tools/govkit/upgrade_steps.py`; the pass declared the three paths
in a second `--dispatch`, respelt the lines, and the same mode then printed `clean`. The record is
deviation 14. Also: `docs_leg.py --list` over a scratch copy anchors `entry:loop` and the kit's two
script rows on `help/loop.md`, and the run-gates kit's guard-gap derivation, called as a probe,
names no leg whose import closure gained the loop reader.
