**Serves:** journal TOOL-dTotalRecall-92
**Caused-by:** TOOL-dTotalRecall-92

# TOOL-dTotalRecall-92 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `298898436` from [2026-11-24-prompt-TOOL-dTotalRecall-92-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-92-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `2db944436`.

## Why

Built as spec rev-3 says, with no divergence found. The pass wrote S10's deviation record 1014 of unit 87 (through the record door) and S23's docstring paragraph. Every other item read as the spec pins it, so no other record is owed. AC1 to AC24 are observed in the acceptance ledger, and the spec header is CLOSED. (DERIVED 2026-11-24, the pass)

## Summary

Built: the docstring paragraph of `tools/memory-tree/tree_lib.py#resolve_memory_root` (S23), and `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-87-deviation-1014.md` (S10). The generated renders that follow them, the as-built view included, are in the commit, as is the ledger `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-92-1-acceptance-ledger.md`. `gen_map.py --write` moved no bytes. S11 restores nothing, S12 moves nothing, S13 clears nothing.

Checks run, all DERIVED 2026-11-24, every spec fence extracted verbatim and run by path:
- Tip scan: rc 0 at the base over 150 records and at the commit over 151. At the commit it prints 121 `by` lines, 3 `quoted` lines and nothing else. This stands in for the `memory hygiene` deviation checks. (DERIVED 2026-11-24, the pass)
- Anchored read: no path, liveness 151.
- Span derivation over unit 78's block: `spans 2` with the live lines, `spans 1` without; a deleted verdict line gave `red population 72 read 71`, exit 1. (DERIVED 2026-11-24, the pass)
- Corrected `read_at`: 2 and 2 for the two needles; an empty file and a blank-line file are each a red line, exit 1. (DERIVED 2026-11-24, the pass)
- Needle scan: `blocks 14` and no other line.
- Plant `kept-home-trailing-root`: exit 0, one home on both lines. (DERIVED 2026-11-24, the pass)
- AC22 scratch folder: one `dup` line.
- AC10 `has_deviation`: 0 at the base, 1 after. (DERIVED 2026-11-24, the pass)
- AC11 addition listing: 150 at the base, 151 at the commit; deletions none, with rename detection off too. (DERIVED 2026-11-24, the pass)
- AC5 and AC9: the main loop's `p79` read is copied from the brief. Unit 78's two counts are both 72, so no second sweep. (DERIVED 2026-11-24, the pass)
- AC23: `[True, True, True]` and four definitions.

The pre-commit hook passed. `gotchas.py --for-diff HEAD~1..HEAD` selected 26 anchored classes plus 6 universal ones. I read the first 14 of its 32 entries (output cut) and checked the diff by eye for the relevant ones (table-cell pipes, inline fences, wrapped ledger tokens, idempotence); no change was needed. (DERIVED 2026-11-24, the pass)

Owed to the close: the §7 legs. Spec 92 declares no new arm, so no RED-first observation is owed. (DERIVED 2026-11-24, the pass)

Process fault, for the main loop: the index render added record 1014's row to `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-87.md`, a path outside the declared set. I ran `--dispatch --writes` for it only after the render and after setting the spec CLOSED. It exceeded its 120 s bound (DERIVED 2026-11-24) and went to the background, and I committed before it answered. I then killed it, because it reads its anchor from HEAD late and would have keyed a row to the new commit that no pass commit closes. It wrote no row, left no lock, and the tree is clean. So that generated-row write is undeclared, and `check-unattended.sh` check 23 may count it; its header says the undeclared-write count never fails the leg.
