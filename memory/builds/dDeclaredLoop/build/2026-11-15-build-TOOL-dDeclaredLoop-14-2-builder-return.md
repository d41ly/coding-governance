**Serves:** journal TOOL-dDeclaredLoop-14

# Builder return — TOOL-dDeclaredLoop-14, dispatch 2: the pass may not declare the shared DECISIONS record

## Why

DIVERGENCE: --dispatch refused the write set, and that refusal is binding. The spec makes this pass write memory/DECISIONS.md, which this project lists as a shared record no pass may declare. The refusal was check 49: "--dispatch declares a path overlapping a shared mutable record this project declares ... memory/DECISIONS.md against memory/DECISIONS.md". .unattended.conf sets SHARED_RECORDS="memory/DECISIONS.md memory/project/readme-contract.txt", and its comment says a concurrently dispatched pass "may not declare a write under SHARED_RECORDS at all".

Two places in the spec put that write in this pass. Section 4 "The Skill's row" says the Skill render's size row is raised and "memory/DECISIONS.md records the unit's row with the raise". Section 4 "Files touched" lists `memory/DECISIONS.md: the raise's row`. The raise cannot happen without that row: term 4 at the head of tools/template-size-limits.txt requires the unit's row in memory/DECISIONS.md "before or with the raise". Grep finds no row for TOOL-dDeclaredLoop-14 in memory/DECISIONS.md today.

The tree has an established route for this. Commit b443d7081, "records(aNimbleMend): the decision row for TOOL-aNimbleMend-11's size raise, ahead of the pass that makes it", landed the row in a records commit before the pass. Commit d11f2a018 put unit 5's decision row in its spec-writer commit.

What the spec would have to say:
- Section 4 "The Skill's row": the unit's decision row lands in memory/DECISIONS.md ahead of the pass, by the spec writer or the main loop. The pass then raises the row under term 4's "before" clause.
- Section 4 "Files touched": drop memory/DECISIONS.md.

Dispatch the unit again once that row is committed.

## Summary

I committed nothing for TOOL-dDeclaredLoop-14: `--dispatch` refused the write set because the spec tells this pass to write memory/DECISIONS.md, a record no pass may declare (details in `why`). I made no edits, and the tree is still clean at base b02214aaef84663f65c5cddeb81cbe4b4149ef2f, so no patch file was needed. The refused `--dispatch` wrote no row to RUN.md. I did not run `--brief`, because the dispatch refusal says stop and RUN.md already holds a brief row for this unit (it reads `brief · item TOOL-dDeclaredLoop-14` with hash ebc183d5298e). I did not run `gotchas.py --for-diff`, since there is no commit to check.

**One deviation record is owed at the rebuild.** `--check-refusal` should handle the item composition the way the engine already does. When the composition answers unarmed (exit 2), it reads gov's own `[[item]]` rows. It prints `loop: unarmed` only when the composition refuses (exit 1). The spec does not say this, so it needs a deviation record. I had planned it as memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-14-deviation-144.md.

**Checks that ran, all read-only, none a gate:**
- `lexicon.py --suggest` passed `derive_frontier`, `check_refusal`, `read_refusals`, `run_refusal_plant` and `check_frontier_plant` (py.function) and `write_refusal` (sh.function). This stands in for the `lexicon naming predicates` leg.
- A Python probe of the shipped loop definition's step.build and step.test items and the unit transition rows. It confirmed:
  - The shipped needs already chain item.build.base → item.build.unit-lease → item.build.unit-pass, so the `frontier-chain` plant needs no edit to the definition in memory.
  - The step's unit-forward item is item.build.acceptance.
- I read the code the spec relies on, and each claim holds:
  - In position.py: `derive_next_item`, `derive_instance_key`, `PLANTS`, `write_position_plant` and `main`.
  - In unattended.sh: `park`, `verb_propose`, `verb_plan`, `resolve_position_engine`, `VERB_REQUIRES`, `VERBS_SLUG`, the `gov:argv` loop and the dispatch.
  - check-unattended.sh checks 26, 27 and 52.
  - In the suite: `PARITY_ROWS`, `_rf_matrix` and `run_hostile_verb`. The suite runs the real tree's driver, so the engine resolves there and the one-line hostile form would be accepted.
  - runlog's `read_run_state` and `PARK_KINDS`, and drift-audit's `_RUN_PARK_KINDS`. The kind set is copied only in runlog/model.py and drift_report.py.
  - The `loop position fixtures` rows in gate-legs.json and selftest-budgets.txt, and the `principle.p24` row in core-pending.txt.

**Still owed at the close, unchanged from section 7:**
- The RED-first observation for both `New arm:` lines: the position.py frontier plants, and the unattended.test.sh `--refused` arms.
- `core meta-check` for AC8.
- A fresh price for the `loop position fixtures` budget row.
- The bar.
