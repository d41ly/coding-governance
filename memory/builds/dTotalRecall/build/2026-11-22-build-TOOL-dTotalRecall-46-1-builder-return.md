**Serves:** journal TOOL-dTotalRecall-46

# TOOL-dTotalRecall-46 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `254057fa6` from [2026-11-22-prompt-TOOL-dTotalRecall-46-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-46-build-brief.md), recorded whole; the pass tip is `63f283ddd`.

## Why

The spec says this pass only checks the parser unit 54 built at 74af3faa4 and writes no product code ("Files touched: none"). Every claim the spec makes about the current code held. The pass is one commit holding: the acceptance ledger; the spec's status moved from INPROGRESS to CLOSED (rev-7, 2026-11-22); RUN.md; and the files gen_build_index --write rewrote.

## Summary

Commit 63f283ddd (TOOL-dTotalRecall-46, Pass: TOOL-dTotalRecall-46 trailer, Co-Authored-By trailer) adds memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-46-1-acceptance-ledger.md and sets memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md to CLOSED. It also stages memory/builds/dTotalRecall/RUN.md and the files gen_build_index --write rewrote: memory/LIVE.md, memory/backlog/TOOL.md, memory/builds/dTotalRecall/README.md and the spec's records table. All of those paths were already declared. No product path changed.

The --brief verb reported the brief was already recorded and unchanged (3030fc142f8f).

**Generator side effect for the main loop to look at:** with no INPROGRESS spec left, gen_build_index changed the dTotalRecall build status from INPROGRESS to DEFERRED in LIVE.md and the build README. It also changed TOOL-dTotalRecall-27's row in memory/backlog/TOOL.md from INPROGRESS to DEFERRED, with its owner moving from -46 to -10. That output is generated and was committed as the brief asks.

**Checks that ran** (python -c probes of unit 54's parse_id_parts; they stand in for the memory-recall kit selftest arm test_id_parts_parse_under_each_tree_grammar and the hygiene ledger check, both run at the close):
- **AC1:** from the repository root, the call on TOOL-dTotalRecall-38 returned ('TOOL', 'dTotalRecall', 38). grep -c 'ID_RE' over inspect.getsource printed 0 and exited 1. In a scratch tree under the scratchpad (.memory-tree.conf with MEMORY_ROOT, FAMILIES="tooling:TOOL", RECALL_CITED_FAMILIES="ZED"), the call on ZED-aFoo-2 returned ('ZED', 'aFoo', 2).
- **AC2:** TOOL-aDrainedSluice-9b returned ('TOOL', 'aDrainedSluice', 9).
- **AC3:** ARCH-001, ABL-d119, TOOL-x and TOOL-dTotalRecall-38@rev-2 each raised ValueError whose message names the id.
- **Unit 63's AC2** (owed at this tip, run from tools/memory-tree/):
  - The cited-family call returned the tuple.
  - As a check that the probe can fail, the same call with alt=tree_lib._id_alternation(load_conf(tree)) raised ValueError.
  - The _id_alternation source count printed 0.
  - In git log --reverse, 74af3faa4 is at position 10986 and this pass commit at 11005, after the commit was made.
- **Unit 64's AC2:** ast.get_source_segment of parse_id_parts at 74af3faa4 and in the working file are equal (1083 characters each).

Units 63's and 64's results are recorded in the ledger under their own **Evidences:** blocks.

**Owed to the close:** every leg in §7 (memory hygiene, lexicon naming predicates, tier2-review self-test, recall floor, recall floor arms, build-index selftest, memory-recall kit selftest, drift-audit selftest, playbook render selftest, policy fixtures). §7 declares no New arm, so no failing-first observation is owed.

The pre-commit hook passed. gotchas.py --for-diff HEAD~1..HEAD exited 0 with 28 classes. I checked the relevant ones and none needed action:
- fixture-passes-by-finding-nothing: covered by the liveness control above.
- ledger-token-wrapped-across-a-line: every ledger line is single-line.
- record-without-serves: the ledger carries **Serves:**.
- pipe-in-a-code-span and inline-fence: neither appears.

No command was skipped.
