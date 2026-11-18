**Serves:** journal TOOL-dDeclaredLoop-6

# Builder return — TOOL-dDeclaredLoop-6, dispatch 1: the policy-key factory's own policy check is always red on mirror parity

## Why

DIVERGENCE: §2 S4, §4 "The factory contract" and "What a factory leaves to its caller", §5 security, and AC3/AC10 with the policy-key-new plant cannot all hold. As written, the policy-key factory writes only the catalogue and then runs the whole `policy check`, and that check is always red on the factory's own key. Its arm_mirror_parity compares the working-tree `.governance/policy.json` with `policy.render_mirror(repo, "HEAD")`. That render includes the new working-tree catalogue row, and the mirror does not have it. Observed in a snapshot clone through `core.py new policy-key fixture.knob ...`: arm_shape and every other arm were green, then `arm_mirror_parity · 1 finding(s)` printed `fixture.knob: differs from the render at HEAD; run: python <this kit>/policy.py mirror --write`. So the factory exits 1 and restores every time, and AC3's "policy check is green" can never be observed. The fix is not mine to choose. `.governance/policy.json` is listed in tools/policy/guarded-paths.txt, so having the factory run `policy.py mirror --write` as a held renderer would write a guarded file. That widens the write surface beyond §5's "writes the catalogue, never .governance/policy.toml", which is the build method's veto 3. The spec has to say which way to go: (a) the policy-key factory runs `policy.py mirror --write` as a held renderer of `.governance/policy.json`, with §5 and the write surface re-priced; or (b) the mirror becomes the caller's in §4's table, and the factory's gate is narrowed to arms that read the catalogue alone (arm_shape, arm_schema, arm_summaries), with AC3 and the policy-key-new outcome rewritten to match. One companion gap belongs in the same revision. `check-hook-destinations.sh` grades only tracked `*.fragment.json` (`git ls-files`), so the hook factory's own innermost gate run never reads the fragment it just wrote. My build had the hook-new plant stage the files (`git add -A`) and run the gate again, which went green over 14 fragments. The spec should either state that limit in S5 or §4's "WHAT check-commands DOES NOT CHECK", or say the factory stages its files. Everything else in rev-6 held when probed against the tree.

## Summary

Nothing was committed, and the working tree is back at base 2b1d84b. The only change left is the dispatch row that `unattended.sh --dispatch` itself staged in `memory/builds/dDeclaredLoop/RUN.md`; I left it for the caller.

The work in progress is saved as a patch: C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/TOOL-dDeclaredLoop-6.patch. It holds:
- the new `tools/loop/factories.py`: the five factories, `check-commands`, the eleven plants and `--selftest`, with every function name checked against the lexicon's suggest verb;
- the five filled kind rows in `tools/playbook/kinds.toml`, with the preset row naming dKeptSession;
- the edits to `tools/playbook/core-pending.txt`: five kind rows and three leg rows deleted, and the preset row's arming build set to dKeptSession;
- the edits to `tools/gate-legs.json`: three `enforces` keys placed before `stage`, and the two new legs, each ending in `"stage": ["step.test"]`.

The rest of the declared write set was never started: registry, pins, budget row, usage, help, README, kit.toml, kinds.md, map, manifest stamp, ledger and the spec status.

Checks that ran. These are probes of the unit's own CLI over snapshot clones and stand in for no gate:
- `check-commands` over the tree exited 0 printing `unarmed` across 30 descriptors.
- AC13's slot refusal exited 2 naming `Bad_Slot`, with nothing written.
- `command-new` exited 0. `command-hand` exited 1 naming `command.loop.hand`.
- `role-new` exited 0, with `check_roles` reporting 0 defects. `role-hand` exited 1 naming R2.
- `workflow-new` exited 0, with `check_roles` and `loop_lib.py --check` green. `workflow-hand` exited 1 naming R8.
- `hook-new` exited 0 after its files were staged and the gate ran again. `hook-hand` exited 1 naming `tools/hooks/fixture-hand.fragment.json`.
- `policy-key-hand` exited 1 naming the missing `owner`.
- `factory-restores` exited 1, and the clone's `git status --porcelain` was clean.
- `policy-key-new` exited 1 on arm_mirror_parity; this is the divergence.
- An in-process `core.check_kind_row` returned no red, and conforming, for all five rows.

Rough timings, PINNED 2026-11-15 on node d: a snapshot clone takes about 18 s, a policy check about 25 s and a hook gate about 40 s.

Owed to the close when the unit is rebuilt: every §7 leg, including `core kinds` and `core meta-check`, and the `loop factories fixtures` arm's RED-first observation.

Of the four budgets the task named: no shell file is touched, so refusal ceilings and families are not reached, and no shared record was in the write set.
