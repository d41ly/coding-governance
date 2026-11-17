# TOOL-dDeclaredLoop-50 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-50

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-4 of the spec, by the loop definition's own CLI over the working tree: `loop_lib.py --fixture
--plant` for the two new plants, and for `witness-actor-listed`, the plant that reads clean, which runs
the whole `--check` read over the shipped definition and stands in for `loop_lib.py --check`, the
`loop definition` leg, which the role hook refused this pass; `git grep` and the `tomllib` probes the
criteria spell; and `check` of `loop_table.py`, `loop_items.py`, `loop_checklist.py` and `splice.py`,
which the hook admitted and which each exited 0. The re-run of the spec's section 5 sweep at the base
of this pass matched every figure it states but the driver's refusal ceiling, 340 PINNED where it reads
335 PINNED, which this pass does not touch (deviation 503); the definition read 61 PINNED items, 40
PINNED command rows, all tag-derived, and reads 67 PINNED, 45 PINNED and 45 PINNED after it; the
lexicon offender pin stays at 1215 PINNED, no function minted; `docs_leg.py --fingerprints` still
anchors `script:tools/loop/loop_lib.py` at `8a025e56` on `help/loop.md`; `gen_map.py --write` changed no
file.

Owed to the close: every leg the spec's section 7 names, `loop_lib.py --check` among them, and the
RED-first observation of its `New arm:` line, the `step-none-outside-review` and `review-step-named`
plants against a `check_program` that admits `none` on every row and a review row at any step.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_lib.py --selftest` with every function the unit's pass changed in
`tools/loop/loop_lib.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-50
- AC1 — `item.review.trigger` — the clean-reading plant exited 0 with no `loop: refused` line, printing `loop: program review · 6 PINNED item(s) · item.review.trigger item.review.pin item.review.report item.review.cost item.review.dispose item.review.fold` and one `loop: item` line per review row, five naming `command:review.<name>` and the fold row `role:gov-spec-writer`; the `git grep` for a bare or path-shaped actor printed nothing and exited 1.
- AC2 — `step-none-outside-review` — the plant exited 1 printing `the item item.plan.place step 'none' is not step.plan`; `review-step-named` exited 1 printing `the item item.review.pin step 'step.design' is not none`.
- AC3 — `review-step-named` — `grep -c` counted 1 PINNED line in `help/loop.md` and 1 PINNED in `tools/loop/README.md`; `grep -n "loop: program review" help/loop.md` printed the example line; the `git grep` for the bare two-segment span printed nothing.
- AC4 — `item.plan.record` — `loop_table.py check` exited 0 with no `loop: refused` line, printing `loop: owed item.review.dispose · plan-revision · dRankedPlan` and `loop: stand-in item.review.dispose · dDeclaredLoop`; the routes probe run in `tools/loop` printed `transition item.plan.record item.review.fold item.review.trigger item.review.dispose 6`.
