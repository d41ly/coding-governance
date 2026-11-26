**Serves:** journal TOOL-dTotalRecall-37
**Caused-by:** TOOL-dTotalRecall-37

# TOOL-dTotalRecall-37 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `d25e5c29e` from [2026-11-25-prompt-TOOL-dTotalRecall-37-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-37-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `0bb9f069c`.

## Why

Built to spec rev-7 and committed as one commit with the spec CLOSED in it. AC1, AC2, AC4 and AC5 were observed; AC3 was observed on the arm alone, over a scratch copy, and the whole `govkit selfcheck` run is owed to the close. One unstated change, a third plant, is recorded as deviation 1020.

## Summary

WHAT LANDED: `.gitattributes` names the four rendered workflow scripts `linguist-generated`, one line each. `tools/govkit/govkit.py` gains `check_generated_attributes`, called by `selfcheck` after `check_source_rows`, with `derive_home_ctx` and `read_attr_population` extracted. `tools/govkit/selftest.py` gains `check_generated_attribute_arms`, called after `check_benched_probe_arms`. The commit also holds the regenerated map and indexes, RUN.md, the acceptance ledger and deviation 1020.

DEVIATION 1020: a third plant, `render-token`, arms S2's finding on a `to` token gov cannot resolve. The spec's `New arm:` line named no plant for it. It shares the `generated-glob` run, so it adds no selfcheck run.

OBSERVED (all DERIVED 2026-11-25):
- AC1 and AC2: `git check-attr` over the fourteen .js files reads `set` on the four renders and `unspecified` on the other ten.
- AC3: `check_generated_attributes` and the new selftest helper were called as functions over a single-commit `git init` copy of `tools/` and the root files under %TEMP%, not the whole tree. With no line it names the four renders, and a `=true` line reads as unmarked. All seven checks passed: the glob, token and cut-line plants were each named, and the restored copy was silent with 4 and 4. This stands in for `govkit selfcheck`. The copy has been deleted. (DERIVED 2026-11-25, the pass)
- AC4: `code_record.py --dump` over the staged tree took 37.7 s, and again at HEAD after the commit. The four templates and six scripts each have an `f` line and the four renders have none; `renderShapeLine` sits under `tier2-review.template.js`. (DERIVED 2026-11-25, the pass)
- AC5: `eol_population` equals `read_attr_population(root, "eol")` over 16441 paths, and the argvs of every parsed descriptor are identical before and after the edit. (DERIVED 2026-11-25, the pass)
- The naming lexicon was run and read OK. The bug-class checklist was run over HEAD~1..HEAD; it led to no edit.

OWED TO THE CLOSE:
- AC3 through `python tools/govkit/govkit.py selfcheck` run whole, and the `govkit selftest` leg that carries the new arm.
- The rest of section 7's legs.
- RED-first for `New arm: tools/govkit/selftest.py`: `generated-glob` and `render-unmarked` under a one-direction compare, plus `render-token` with its finding removed.

DISCLOSURES:
- I ran `python code_record.py --check` directly once while waiting on the dispatch; it printed green. That is the `code record` leg's own command, so treat it as a probe and not as bar evidence.
- The `--dispatch` declaring the deviation record's path ran past its 300 s bound into the background and exited 0 after about nine minutes. It drew re-dispatch 88/186. It ran after the spec header was already CLOSED and after the record was staged, so it printed that it reserves nothing. (DERIVED 2026-11-25, the pass)
- The hook refused my `sleep 20` and `tail --pid` waits.
