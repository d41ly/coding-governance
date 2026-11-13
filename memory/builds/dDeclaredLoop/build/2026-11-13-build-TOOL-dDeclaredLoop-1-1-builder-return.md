**Serves:** journal TOOL-dDeclaredLoop-1

# Builder return — TOOL-dDeclaredLoop-1, dispatch 1: a divergence, nothing built

## Why

DIVERGENCE: spec section 2 (S2, S4) and section 4 ("The moved table, and the step each workflow serves", "The readers, re-pointed") describe a roles catalogue that carries no `step` key, and the code now carries one. PLAY-dOrderedCharter-21 (commit e542b6367, 2026-11-09) landed after the spec's base ed497191 and after its rev-4 re-ground at 462d20f35 (e542b6367 is not an ancestor of 462d20f35). It added `step` to every `[[workflow]]` row of tools/roles/workflows.toml, to `WORKFLOW_KEYS` and a `STEP_NAMES` vocabulary (entry, plan, design, build, test, deploy, review, none) graded by R6 in tools/roles/check_roles.py, plus a reader, tools/playbook/load_sets.py#read_role_step.

Building S2 as written would mint a second `step` per workflow in tools/loop/loop.toml that states the same fact in a different vocabulary and with different values for four of the ten workflows:
- orient: roles `entry`, spec `none`
- spec-review: roles `review`, spec `step.design`
- closing-review: roles `review`, spec `step.build`
- research: roles `plan`, spec `none`

That is the shape the spec's own Alternatives section rejects for `stage` ("two spellings of one order"), and which of the two is authoritative is a design choice, not a builder's.

What the spec would have to say:
1. S2 and section 4's table: whether the roles `step` key moves into the loop definition with `stage`, stays in roles as the one home with the loop row carrying only `order`, or both stay with a stated join; and which value wins for the four rows above, including whether `entry` and `review` have a loop spelling, since neither is one of the five gov steps and S3 refuses any `step` that is not a declared step tag or `none`.
2. S4 Readers and section 4's readers table: tools/playbook/load_sets.py#read_role_step reads `step` from the roles catalogue and is unnamed; if the key moves it is a reader to re-point, and tools/roles/adopt-roles.test.sh already holds an arm grading "missing key 'step'".
3. S4's `git grep -l workflows.toml` population is no longer seven files: tools/playbook/load_sets.py, tools/playbook/instruction_units.py and tools/playbook/render_playbook.py now name it. S9 covers render_playbook.py#read_drive_rows only; the fixture in tools/playbook/instruction_units.py (`DRIVE_WORKFLOWS`, which writes `stage = 5` and `stage = 7` into a fixture roles catalogue to exercise that sort) is unnamed and would need re-pointing with S9.
4. Section 4 Files touched omits tools/roles/adopt-roles.test.sh, which section 7's second `New arm:` line re-points, and whichever playbook files items 2 and 3 add.

Nothing was written: no product edit, no `--dispatch`, no `--brief`, so RUN.md is untouched, the tree is clean at base and no patch file exists.

## Summary

No commit; the tree is clean at base e40eb7649. I stopped before the first write, so no `--dispatch` or `--brief` ran and there is nothing to restore.

Checks that ran, all read-only and standing in for no gate:
- `git merge-base --is-ancestor`, showing e542b6367 is outside the rev-4 re-ground commit 462d20f35.
- `git show ed497191:tools/roles/check_roles.py`, showing `WORKFLOW_KEYS` held no `step` at the spec's base.
- `git grep` over `tools/` for readers of `stage`, `step` and `workflows.toml`.
- Whole reads of tools/roles/workflows.toml, tools/roles/check_roles.py and tools/roles/adopt-roles.sh.

Spec claims that still hold, so a revised spec can keep them:
- `tools/loop/` does not exist.
- tools/playbook/core.py has a `meta-check` verb, and tools/playbook/core-pending.txt holds the `principle.p1` row for dDeclaredLoop that S7 deletes.
- tools/playbook/render_playbook.py#read_drive_rows still sorts by the roles `stage` integer (S9).
- tools/roles/kit.toml `requires` is `["kickoff-manifest", "memory-tree"]`.
- tools/playbook/namespaces.toml already names `{prefix}/loop/loop.toml` as the `step` namespace's source (unit 18).

Not run and still owed to the close once the unit is built: both section 7 `New arm:` RED-first observations (tools/loop/loop_lib.py, tools/roles/adopt-roles.test.sh), the legs section 7 lists, and the bar.

The SubagentStart orientation card still reads this unit as DEFERRED and not buildable, while the spec header reads INPROGRESS. The card looks stale; a re-dispatch may hit scratch-guard on routed paths until it is refreshed.
