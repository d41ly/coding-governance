# TOOL-dDeclaredLoop-26 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-26

No merge bar, no self-test suite and no gate leg ran in this pass, and `composition.py --selftest` was
not run. The criteria were observed on node `d` (win32), at rev-6 of the spec, by probes of the unit's
own code: every plant of `composition.py` run alone by direct CLI from the loop kit's folder, each
building its own scratch repository; the `field`, `default`, `pre-spec`, `backward-rows` and
`skip-backward` plants of `loop_transition.py` by direct CLI; the `idempotent`, `steps` and
`status-line` plants of `position.py` and its `--check-refusal` by direct CLI; and reads of the
manifest row, the pending file and the help page.

Owed to the close: every leg the spec's section 7 names, `core meta-check`, `loop transition record`,
`loop position fixtures`, `codebase-map coverage + freshness` and `help page commands` among them, the
new leg `loop composition fixtures`, `loop stage coverage` for the row's stage claim (deviation 266),
and the RED-first observation of both `New arm:` lines. The new leg's run time was not read: its budget
row is a proxy priced from the plants run alone, and the close re-prices it from the leg itself.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/composition.py --fixture --plant rename` with the position engine reading the tip, the
move's pin ignored exited 1, and 0 once restored: RED observed.
`python tools/loop/loop_transition.py --fixture --plant field` with the derived `composition` field accepted
as given exited 0, and 0 once restored: not reddened by this break, so not observed.
`python tools/loop/loop_transition.py check --selftest` with the derived `composition` field accepted as given
exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-26
- AC1 — `read_step_composition` — `--plant rename` printed `loop: fixture · pin after C2 · <C1's sha8> · pinned`, C1 the first move's commit; `loop: fixture · composition at the pin · item.design.decompose True · item.design.regroup False`, read through a scratch worktree at C1; and `loop: fixture · position reads · composition@<C1's sha8> · pinned` from `derive_position` over the plant; then `· rename · held`, exit 0.
- AC2 — `derive_carried_witnesses` — the same plant printed `loop: fixture · move at C2 · composition=<C2's sha8> · C2 <C2's sha8>` and `loop: fixture · carry · <the decompose move's sha8> under item.design.regroup`, with no `item-ended` order filed.
- AC3 — `read_tag_policy` — `--plant policy-rename` printed `review.breakpoints ['item.design.decompose']` before the move at C2 and `review.breakpoints ['item.design.regroup'] · loop-policy-renamed-review.breakpoints-item.design.decompose.md` after it, then `held`, exit 0.
- AC4 — `loop-item-ended-tFix-item.design.decompose` — `--plant ended` and `--plant split` each printed `loop: order · .governance/outbox/loop-item-ended-tFix-item.design.decompose.md` at the move at C2, the outbox holding that one order, and `loop: fixture · carry · item.design.regroup carried: False`; each ended `held`, exit 0.
- AC5 — `derive_composition_revision` — `--plant rename` printed `loop: fixture · channels · trailer <C2's sha8> · log <C2's sha8>`, both equal to the first eight hex digits `derive_composition_revision` answered before the move.
- AC6 — `composition` — `--plant unpinned` printed `loop: fixture · pin · <HEAD's sha8> · unpinned` over the hand-written move, `loop: fixture · next move · composition=<HEAD's sha8>` for the move recorded after it, and `loop: fixture · orders · 0 order(s)` (PINNED), then `held`, exit 0.
- AC7 — `item-ended` — `grep -n "next step boundary" help/loop.md` found the opening line of the section `When a build moves to a newer composition`, which names the `composition` field, the `item-ended` order and the `policy-renamed` order.
- AC8 — `loop composition fixtures` — `json.load` read `principle.p8` in the row's `enforces` and `step.test` in its `stage`, its last key; a grep of `tools/playbook/core-pending.txt` for the tag's row counted 0 (PINNED). The `core.py meta-check` exit is owed to the close.
- `field` — `loop_transition.py --fixture --plant field` printed `loop: unanswered · --field composition is derived: the writer sets it to the commit HEAD names, so it is never given`, then the plain move's trailer ending `· composition=<sha8>` and the check's `0 finding(s)` (PINNED), exit 0.
