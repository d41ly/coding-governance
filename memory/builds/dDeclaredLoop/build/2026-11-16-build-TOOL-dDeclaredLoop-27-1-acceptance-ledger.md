# TOOL-dDeclaredLoop-27 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-27

No merge bar, no self-test suite and no gate leg ran in this pass but the naming lexicon, and
`scenario.py check --selftest` was not run. The criteria were observed on node `d` (win32), at rev-4 of
the spec, by probes of the unit's own code: every plant of `scenario.py` run alone by direct CLI from the
loop kit's folder, each building its own scratch repository; `select` and `check` run as subprocesses in
a scratch built by `build_scenario_base` from this tree's kits with the `two-builds` overlay committed; the
factory's `scenario-new` and `scenario-hand` plants by direct CLI, each in its own snapshot clone; the
register's factory verb over the working tree; `check_kind_row` through `python -c`; the `field` and
`default` plants of `loop_transition.py`, the `rename` plant of `composition.py` and the `steps` plant of
`position.py` by direct CLI, each still held; and greps of the pages and the usage register.

Owed to the close: every leg the spec's section 7 names, `core kinds`, `core meta-check`, `tags (the
resolver's checks)`, `loop transition record`, `loop position fixtures`, `loop factories fixtures`,
`govkit selfcheck` (the subject pin row was written by hand in the generator's sorted place),
`codebase-map coverage + freshness`, `help page commands` and `docs` among them; the new leg
`loop scenario fixtures` and `loop stage coverage` for its stage claim; AC12's first two readings on the
built tree, whose HEAD holds the pack only once this commit lands; and the RED-first observation of both
`New arm:` lines. The new leg's run time was not read: its budget row is a proxy priced from the plants
run alone, and the close re-prices it from the leg itself.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/scenario.py --fixture --plant conflict` with the later scenario winning under refuse exited
1, and 0 once restored: RED observed.
The `scenario-hand` plant of `tools/loop/factories.py`, whose planted defect is the staged break, exited 1
over its scratch tree, its last line reading `factories: fixture · scenario-hand · gate loop scenario fixtures
exit 1`; the leg over the tree read green at HEAD: RED observed.

**Evidences:** TOOL-dDeclaredLoop-27
- AC1 — `select` — in the scratch, `select --fact entry=feature --fact design-only=true` printed `scenario.feature scenario.design-only`, `select` with no fact printed `scenario.feature`, and `select --fact entry=patch` printed `scenario.patch`, each exit 0 with its `loop: facts` line.
- AC2 — `two-builds` — `--plant two-builds` printed `read — scenario=scenario.feature · 0 activated` for `tFix` and `read — scenario=scenario.feature+scenario.adopter.mobile · 1 activated` for `tFix2` (PINNED), each from `position.py` run as a subprocess in the scratch, then `held`, exit 0.
- AC3 — `drops-stage` — `--plant drops-stage` printed `check` exit 1 naming `scenario.adopter.drops`, `item.test.adopter.exit-own`, the fixed row `item.test.exit` and `principle=principle.p20`; `reorders-stage` exit 1 naming `scenario.adopter.reorders`, `field step` and `principle=principle.p20`; `replaces-stage` exit 1 naming `scenario.adopter.replaces`, `step.test` and `owned`; each `held`.
- AC4 — `conflict` — `--plant conflict` printed `select` exit 1 naming `scenario.adopter.a`, `scenario.adopter.b`, `item.test.adopter.device-farm` and `actor`, and the `record` out of `none` exit 2 with the commit count unchanged, then `held`.
- AC5 — `conflict-ordered` — `--plant conflict-ordered` printed `loop: settled · item.test.adopter.device-farm:actor:scenario.adopter.b:scenario.adopter.a` from `select`, and the `record` exit 0 with its `Gov-Transition` trailer ending `scenario-settled=item.test.adopter.device-farm:actor:scenario.adopter.b:scenario.adopter.a`, then `held`.
- AC6 — `bad-default` — `--plant bad-default` printed `select` exit 1 naming `flow.scenario-default` and `"nowhere"`, the policy kit's refusal relayed through the scenario composition; `default-excluded` exit 1 printing `flow.scenario-default = patch names no composed scenario`; each `held`.
- AC7 — `scenario-new` — `factories.py --fixture --plant scenario-new` exited 0 with `gate loop scenario fixtures green` and the clone's pack holding `scenario.trial` with every S3 key; `scenario-hand` exited 1 with `loop: refused · scenario.hand · entry step.nowhere is no gov step`; `core.py new scenario adopter --extends none --admit entry=x --entry step.plan` exited 2, the porcelain unchanged.
- AC8 — `then` — `--plant then` printed the second trailer ending `scenario=scenario.feature+scenario.adopter.b`; `mid-step-switch` printed `· 1 activated` before the move and `· 2 activated` after it (PINNED); `derived-field` printed `record` exit 2 with `--field scenario is derived`; each `held`.
- AC9 — `then-cycle` — `--plant then-cycle` and `--plant extends-cycle` each refused naming `scenario.adopter.a` and `scenario.adopter.b` in one cycle line, then `held`.
- AC10 — `Choosing a build's scenario` — the grep in `help/` printed the heading; the grep of `tools/govkit/usage.toml` printed the bare, `#select` and `#check` rows; the grep of `help/overlay-rows.md` for `--rows -` printed a line.
- AC11 — `loop scenario fixtures` — `json.load` read `principle.p16` and `principle.p8` in the leg's `enforces`; `check_kind_row` answered no red and `conforms` for `kind.scenario`; the grep of `tools/playbook/core-pending.txt` for the kind's row counted 0 (PINNED). The `core.py kinds` and `core.py meta-check` exits are owed to the close.
- AC12 — `scenarios composed` — `check` in the scratch printed `loop: scenarios composed · 6 scenario(s) · 1 repository` (PINNED), gov's five beside the plant's one; `gov_tag.py show scenario.design-only` exited 0 naming `tools/loop/scenarios.toml` once the pack was staged. The reading on the built tree is owed to the close.
