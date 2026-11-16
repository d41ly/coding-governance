**Serves:** journal TOOL-dDeclaredLoop-62

# Builder return — TOOL-dDeclaredLoop-62, dispatch 1: unit 61 extended parallel-append instead of adding the plant 62's rev-3 joins

## Why

DIVERGENCE: unit 61 (bbb9e82c2) changed things that the rev-3 spec of TOOL-dDeclaredLoop-62 still describes the old way. I checked tools/loop/budget.py, .gitattributes, help/loop.md and selftest-budgets.txt at HEAD 52961e46. Two of the changes are design claims, not counts, so the task's rule sends them back to the spec writer.

(1) Spec §4 "The plant" and S2: on `side`, the sketch has `parallel-append` draw TOOL-<fx>-2, and it also says the plant's "budget_state, rows and third-draw checks" stay "unchanged". Unit 61 made `parallel-append` draw the same item on both sides: tools/loop/budget.py#run_budget_plant draws TOOL-<fx>-1 on main and on side, then checks `rows == [... TOOL-<fx>-1 · 1/4] * 2` with two different draw ids. Both statements cannot hold at HEAD. Following the sketch breaks the unchanged checks, and keeping 61's checks departs from the sketch. §4 and S2 should say that the shared branch keeps 61's same-item side draw (TOOL-<fx>-1) for `parallel-append`. Only `parallel-append-uneven` draws TOOL-<fx>-2 then TOOL-<fx>-3 on side. S2's phrase "each on its own item" should be limited to the new case.

(2) Spec §5 "dependency": it says 61's S4 "adds the plant `parallel-append-identical` ... whichever of the two lands second joins its case to the shared branch". Unit 61 took the other option (its §8 option (b)). It added no `parallel-append-identical` plant: it extended `parallel-append` itself and added a new `draw-id-rows` plant. §5 should name 61's extended `parallel-append` and `draw-id-rows` as what landed, and drop the joining clause.

(3) Stale figures. These would have been allowed as a deviation record, but I list them here so the revision fixes them all at once. §4 Evidence and the §5 re-derive command say PLANTS holds 16 keys; HEAD has 17. §5 risks say the direct-CLI readings sum to 224 s with the row at 336; HEAD's `loop budget fixtures` row reads 226 s and 339 for seventeen plants, so S4's re-price starts from 226 s / 339. §5 quotes help/loop.md as "two byte-identical rows are kept once"; 61 reworded it to "Union keeps two byte-identical rows once, and the draw id is what keeps two parallel draws apart". The claim is still true, but the quote is stale.

These still hold: the comment above the transition line is .gitattributes lines 109 to 113 and the transition line is 114, with the five-line text the spec quotes; `write_budget_rows` opens the file in append mode and its writers are `record_draw` and `loop_transition.py#write_transition`; `build_records.py#write_record` writes with mode `x`; `merge-rows.py` `_ROW_RE` matches bullets only; the leg's ceiling is 300; VERB_OFFENDER_PIN is 1215; SESSION-KICKOFF's watch line names none of the three files.

## Summary

No commit; the tree is clean at base 52961e46. I made no product edit, so there is no patch to save. I did not run the `--brief` record verb either, because it would have left uncommitted changes with nothing to commit them in.

Checks run: the spec's §5 sweep commands at HEAD (the PLANTS count, the merge drivers in .gitattributes, VERB_OFFENDER_PIN, the `loop budget fixtures` budget row), plus reading the plant code in tools/loop/budget.py, the comment above the transition line, help/loop.md, 61's closed spec and the ceiling in tools/gate-legs.json. These are readiness checks before building. They stand in for no gate and observe none of AC1 to AC3.

What the main loop needs from the spec writer is in `why`: §4 "The plant" and S2 must keep 61's same-item side draw for `parallel-append`, §5 "dependency" must stop naming `parallel-append-identical`, and the figures should be refreshed to 17 plants, 226 s and 339.

Still owed at the close once a later dispatch builds the unit: the §7 New arm on tools/loop/budget.py covering AC2 and AC3, observed RED and then GREEN.

Relevant files: C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-62.md and C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/loop/budget.py
