**Serves:** journal TOOL-dTotalRecall-117
**Caused-by:** TOOL-dTotalRecall-117

# TOOL-dTotalRecall-117 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `ce1c2095e` from [2026-11-25-prompt-TOOL-dTotalRecall-117-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-117-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `07486a8f8`.

## Why

Built to spec rev-1. No divergence from the spec. Two paths the spec did not list were declared by --dispatch and recorded in deviation 1016.

## Summary

`tools/memory-tree/build_records.py#write_new_record` now derives the content key through `read_key_fields`, the one reader for both the rendered text and each listed record. The key holds the build, unit, title, cause, edge lines and fields. A listed record whose header refuses to read has no key, so it is never `exists`; at the call's own path it is the standing refusal. The door-header plant went from 12 to 20 cases, the suite literal and the door's docstrings follow, and the gotcha `content-key-omits-a-supplied-input` and its INDEX row are in. The spec header is CLOSED. (DERIVED 2026-11-25, the pass)

Checks run, each standing in for the gate named:
- AC1: `python build_records.py --fixture --plant door-header` printed `PASS door-header — 20 cases`, rc 0 (DERIVED 2026-11-25). It stands in for the door-header arm of `memory-hygiene self-test`. In a scratch copy of tools/ with the old key put back, exactly the unit, title, cause, edge, no-edge, build and typed cases failed, each printing `exists` (DERIVED 2026-11-25). The scratch copy is removed.
- AC2 and AC3: a scratch-seed probe. The altered title raised ValueError `already holds the record` and the first record's bytes stood. A CRLF copy still replayed `exists`. A second `**Caused-by:**` line was refused and never `exists` (DERIVED 2026-11-25).
- AC4: the grep printed 0 (DERIVED 2026-11-25).
- AC5: `gotchas.py --check` named no finding of the new file. After the commit, `row_grammar.py --check-relations 3d6c1702a` printed 1 near match, 1 satisfied, and no line naming the file (DERIVED 2026-11-25).
- AC6: the literal prints 20. FLOOR_ASSERTIONS is unchanged because no assertion was added. The shell-role row stays at 3750, because the one edited line is a literal and the measure is code lines, so no widen record was owed (DERIVED 2026-11-25). The `sh_hygiene.py` measure itself was not run; the portability leg observes it.
- The lexicon accepted `read_key_fields`. The pre-commit hook passed, coverage and staged hygiene among it.

Deviation 1016: `tools/memory-tree/README.md` stated the old key, which S1 made false, so it was corrected. `memory/map/features/row-grammar.md` claims the new gotcha class, because an unclaimed class reds coverage.

The bug-class checklist over HEAD~1..HEAD was run and needed no further edit. The relevant classes (`staged-break-runs-stale-bytecode`, `append-without-an-idempotence-key`, the README half of `a-folded-field-leaves-its-row-shape-docs-behind`) were already handled.

Owed to the close: the section 7 legs, and the `New arm:` RED-first observation of the `door-header` literal in `tools/memory-tree/check-memory-hygiene.test.sh`. Nothing was skipped. (DERIVED 2026-11-25, the pass)
