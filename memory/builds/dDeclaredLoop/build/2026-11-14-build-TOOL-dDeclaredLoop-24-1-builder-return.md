**Serves:** journal TOOL-dDeclaredLoop-24

# Builder return — TOOL-dDeclaredLoop-24, dispatch 1: the composition read refuses an uncommitted install's first render

## Why

DIVERGENCE: spec section 2 S3 and section 4 "The composition read" (and AC12 and the section 5 testing list along with them). The spec says derive_kind_composition answers None only when the kind's schema file is missing from the root. Otherwise it reads gov's rows with `git show HEAD:<namespace source>`. After a fresh `govkit apply`, the source is on disk and staged but not committed, because apply stages and never commits before the playbook adopter renders. In that state the read raises: instruction_units.run_git raises LevelError, and render_delta_report turns it into a Refusal, so the render is REFUSED.

I probed this in a clone under %TEMP%. I gave kind.item a schema row, added a minimal tools/loop/item-schema.toml and pointed the item namespace source at the loop definition. Then I ran a default `govkit apply` into a fresh target and called render_delta_report on it. It printed: `the delta report is unreadable: git show HEAD:tools/loop/loop.toml failed: fatal: path 'tools/loop/loop.toml' exists on disk, but not in 'HEAD'`. Control: the same target with the schema line removed returned 4 delta lines and no refusal.

A default install holds both the playbook and loop kits. So this unit as written would refuse the first render of every default install. It would also newly red govkit selftest's "OC8 AC4 a default apply into a scratch target exits 0" arm (`govkit selftest` is a section 7 gate).

To fix it, the spec has to say what derive_kind_composition answers when the namespace source is missing at HEAD but present on disk. The choices I see:
- (a) None, as for a missing schema, so the first render composes no item row;
- (b) zero gov rows;
- (c) read gov's rows from the working tree instead of HEAD.

It also needs an acceptance criterion that runs a render over an install that is not yet committed, and section 5 should name the OC8 AC4 default-apply arm. Choosing among these is a design call, so I wrote no code.

Two smaller points for the same revision:
1. The new leg runs in the `selftests` chunk, so it needs a row in tools/run-gates/selftest-budgets.txt. That file is not in Files touched. Unit 17's leg went red for the same missing row and needed a red-fix commit.
2. The record-version rule as written only compares the pinned hash with the recomputed one. If someone changes a record kind's fields and re-pins the hash without bumping the version, the check stays green. To catch that, the rule would have to compare against the row at a base.

## Summary

Nothing written, declared or committed. `--dispatch` and `--brief` were not run: the brief is already in RUN.md from the earlier "briefed and in progress" commit. The worktree is clean at base fc31a0016, so there was no product edit to save as a patch. The scratch clone, the target and the log under %TEMP% were deleted.

What I checked:
- Read memory/guides/BUILD-METHOD.md, the brief and spec rev-4 in full.
- Checked the spec's claims against current code: tools/playbook/overlay_rows.py, row_checks.py, overlay.py, render_playbook.py read_kind_rows and render_delta_report, core.py kinds, meta-check and new, tools/loop/loop_lib.py, loop_witness.py, loop_table.py, tools/govkit/step_gate.py, docs_leg.py, usage.toml, surface-classes.toml, registry.toml, tools/playbook/fixtures/row_kind.py, tools/run-gates/selftest-budgets.txt, tools/check-install-prefix.sh and the policy catalogue.
- Ran the naming lexicon's suggest verb on every name in the spec's Inventory, plus run_compose and read_memory_tree. All are OK.
- Ran gotchas.py --for-paths over the planned write set.

The probe that found the divergence: a git clone of HEAD under %TEMP% with kind.item given a schema, the item namespace source changed and a minimal item-schema.toml added. Then intake and a default `govkit apply` into a fresh target, and render_delta_report called on that target, which refused. The control, the same target without the schema row, did not refuse. This probe stands in for govkit selftest's OC8 AC4 default-apply arm, which I did not run.

The other items I checked hold at HEAD and need no change:
- principle.p2, p16, p20 and p24 all have principle rows.
- The test-step needs chain merge, select, verdict supports AC6 and AC9.
- record-kind.acceptance and record-kind.disposition are the only typed kinds any item returns, and no gov input names a record kind.
- The compose JSON can carry the composed rows.
- The usage-row fingerprint is computed the way docs_leg does it.

No gate, suite or bar ran. No section 7 criterion and no new arm's RED-first observation was run. All are still owed once the spec is revised and the unit is dispatched again.
