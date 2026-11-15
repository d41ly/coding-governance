**Serves:** journal TOOL-dDeclaredLoop-25

# Builder return — TOOL-dDeclaredLoop-25, dispatch 2: the stage plant makes the drive class refuse, exit 2, where AC5 needs a RED

## Why

DIVERGENCE: S6 and AC5 can't both hold. In rev-6, S6's step-gate plant `write_stage_plant` stages "a clone's definition holding every [[step]] table but the first". AC5 needs `python tools/govkit/step_gate.py --fixture --plant stage` to exit 1 and print `step-gate: RED stage:step.plan`.

With step.plan taken out, the `drive` class's reader raises on the tip side. The call chain: `tools/playbook/render_playbook.py#read_drive_members` -> `#read_drive_reference_rows` -> `tools/playbook/instruction_units.py#read_drive` -> `render_playbook.py#read_drive_rows` -> `loop_lib.read_workflow_order` -> `check_loop`, which raises `the step step.plan is missing`. `read_drive_rows` documents that refusal: "a loop definition that does not read refuses, naming it". A raising reader is a step-gate REFUSAL, exit 2 (govkit selftest's `reader-raises` case), not a RED, exit 1. So the gate exits 2 where AC5 needs 1. The `[dSP-10] step-gate fixture stage` arm in `tools/govkit/selftest.py#check_step_gate_fixture` would newly go red: it reads the class ids from the registry, and its bare run needs exit 1 matching `^step-gate: RED stage:\S`.

Probe that shows it: in a `git clone --shared` of HEAD under %TEMP%, I took the first `[[step]]` table out of tools/loop/loop.toml, read the classes with `step_gate.read_surface_classes`, and called every class reader in process. All 15 shipped classes but `drive` returned members. `drive` raised `Refusal: the drive section sorts by the loop definition, which does not read: .../tools/loop/loop.toml: the step step.plan is missing`. Any plant that makes a gov step tag disappear trips `check_loop` the same way, so the fault is in the design, not in this one plant.

The spec has to choose, in S6, AC5 and §8 F7, one of:
- (a) `read_drive_rows` treats a definition that does not read as no order, as it already treats a loop kit it cannot find. This changes the playbook kit's documented refusal, so that kit's help page needs updating too.
- (b) The `stage` class's fixture case is admitted at exit 2, with the drive refusal named, in `check_step_gate_fixture`. This weakens AC5 and S6's "armed by that row alone".
- (c) A different source for the class's members whose removal leaves `check_loop` passing, if one exists.

Also, F7 says "a gov stage tag absent at the tip ... reds the gate". In fact the gate refuses (exit 2) instead of going red. A landing is still stopped, but the class's own red is never observed.

Two more checks failed, so the next revision should cover them too:
1. §5 "what keeps each touched registry green" gives `tools/govkit/usage.toml` only the three `script:{prefix}/loop/splice.py` rows. That file also says "a registered class with no row here is a finding", so the new `stage` step-gate class also needs a `[[class]] class = "stage"` row (`usage = "none"`, as unit 24's `item` class has) to keep the `docs` leg green.
2. §5 has this unit bump `KIT_PLAYBOOK_RENDER_VERSION` once. The branch reads 1.38 and origin/main now reads 1.40. Unit 24 moved the playbook kit's bytes without a bump, and this dispatch's task says the bump is owed once, after the last move, at the close. The spec should say whether this unit bumps or leaves it to the close; it should not do both.

Every other claim I probed held against the tree:
- kinds.toml `kind.stage`, still pending, and its core-pending row.
- `core.py#run_new`, `#run_kinds` and `#check_kind_row`.
- overlay_rows `#read_kind_schema`, `#check_row_owners` and `#read_kind_source`. No `stage` namespace row exists, so the gov side composes as [].
- `loop_lib.py#check_program` and `#check_loop`, and `loop_items.py#read_composition`, `#run_new`, `#run_factory` and `#build_scratch_tree`.
- The build rows of `loop.toml`, including B12, `testing` on `item.test.exit` `recorded` to `deploying`.
- `loop_table.py#ROW_KEYS`, `loop_parents.py#read_policy_kit`, and `policy.resolve('instructions.exclude', root, 'HEAD')`, which reads [].
- `build_records.py#read_changes`, whose records carry `Unit`, `Successor` and `id`, and `design_lib.py#derive_pin_hash`.
- The `item` class row in surface-classes.toml and `pins.py#read_change_successors`.
- SHARED_RECORDS, which names memory/DECISIONS.md and memory/project/readme-contract.txt; this unit needs neither.

## Summary

I committed nothing and changed nothing in the worktree. `git status` is clean at base aa47ebbe8, so there was nothing to restore and no patch file. I did not run --dispatch or --brief: a divergence leaves no write set to declare, and the first dispatch's builder return records that RUN.md already holds this unit's brief row.

What ran:
- The spec's claims about current code, checked against the tree with greps and reads.
- A probe of the step gate's class readers. It ran in a `git clone --shared` of HEAD under %TEMP%/s25, which I have since removed, with the first `[[step]]` table taken out of tools/loop/loop.toml. I loaded the classes with `step_gate.read_surface_classes` and called each reader in process. The `drive` reader raised the loop definition's `the step step.plan is missing` refusal. This shows that AC5's `step_gate.py --fixture --plant stage` would exit 2 (REFUSED) instead of 1, and that govkit selftest's `[dSP-10] step-gate fixture stage` arm would newly go red. It stands in for the `step-gate` and `govkit selftest` legs on this one case. No gate itself ran.
- `tools/lexicon/lexicon.py --suggest <name> --as py.function` for every planned name, extracted helpers included. All 21 returned OK, which stands in for the `lexicon naming predicates` leg on those names.
- `docs_leg.py --fingerprints`, to see the anchor form the help page needs for the three `script:` rows of tools/loop/splice.py: `script:tools/loop/<file>[#verb] <fp8>`, as on help/loop.md.

What did not run:
- `gotchas.py --for-diff`, because there is no commit to run it over.
- The step gate fixture itself, the kit epoch leg and every section 7 leg. These belong to the close once the spec is revised.

Notes for the next dispatch:
- The companion write set is unchanged from the first return. Add `tools/govkit/usage.toml` for the `stage` class row and a deviation record numbered 255 if the revision does not cover that row.
- Leave `tools/playbook/render_playbook.py` out unless the spec keeps the version bump in this unit.

Paths:
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/render_playbook.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/govkit/selftest.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/govkit/usage.toml
