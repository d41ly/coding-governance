**Serves:** journal TOOL-dTotalRecall-10

# TOOL-dTotalRecall-10 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `32d4c2e81` from [2026-11-22-prompt-TOOL-dTotalRecall-10-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-10-build-brief.md), recorded whole; the pass tip is `d735e47b9`.

## Why

TOOL-dTotalRecall-10 is built as its spec (rev-3) says. Before any write I checked every precondition the spec names against the tree, and each one held: derive_heading_seg, scan_unfenced, extract_doc, PLANTS, build_tags_fixture, run_plant, run_check, run_plant_rows, and AC3's at-HEAD exit 2 with "no plant 'repeat-heading'". Every path the commit holds was in the declared dispatch set, apart from RUN.md and the ledger, which the brief excepts. So there was no divergence to report.

## Summary

TOOL-dTotalRecall-10 is committed as d735e47b9 on top of base 32d4c2e81. The subject names the unit and the commit ends with the Pass and Co-Authored-By trailers. The same commit flips the spec header to CLOSED, dated 2026-11-23.

**What changed**
- `tools/playbook/tag_index.py`: new `derive_anchor(heading, seen)`, written as the spec's section 4 shows it. It calls `derive_heading_seg`, and a repeated fold searches for the smallest free `-n` from 2. An empty fold comes back empty and is never added to `seen`. `extract_doc` now creates one `seen` per document and derives each segment through it, keeping its skip of an empty segment.
- `tools/playbook/gov_tag.py`: the `repeat-heading` plant is added to `PLANTS`, with a `REPEAT_GUIDE` constant. The fixture builder adds `memory/guides/REPEAT.md`. The plant rebuilds, prints the sections line (read through `ti.read_rows` over the loaded view, in line order) and the line `doc.repeat#findings-2` serves, then runs `check`.
- `tools/playbook/adopt-playbook.sh`: the two `repeat-heading $_tk|0|...` rows are added to the tag-resolver block, plus a comment saying what they check and what they do not.
- Records and generated files: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-10-1-acceptance-ledger.md`, `RUN.md`, and the output of `gen_map.py --write` (`symbols.json`) and `gen_build_index.py --write` (`LIVE.md`, `backlog/TOOL.md`, the build README, the spec's generated records table).
- With no unit at INPROGRESS any more, the build index now shows the dTotalRecall build as DEFERRED in `LIVE.md` and the README, and TOOL-dTotalRecall-27 as DEFERRED, advanced by TOOL-dTotalRecall-100. That is the generator's own output, not a hand edit.

**Checks run in this pass** (fixtures and probes only; no gate, suite or bar ran)
- AC1: the criterion's `python -c` probe printed `['findings', 'findings-2', 'findings-2-2', 'm5-recall-and-reuse']`.
- AC2: a probe printed `findings findings` for two fresh `seen` sets, and `'' ''` for `—` derived twice, with `seen` left empty.
- AC3 and AC4: `python gov_tag.py --fixture --plant repeat-heading --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new`, run from `tools/playbook`, exited 0. It printed `sections findings findings-2 findings-2-2`, `findings-2 serves the second findings` and `tags: green · 0 red`, and no line naming `doc.repeat#findings`. This stands in for the `playbook render selftest` leg's two new rows.
- Staged break: with `extract_doc` set back to `derive_heading_seg` alone, the plant exited 1 and printed `sections findings findings findings-2`. The file was restored from a scratch backup.
- AC5: a scratch probe at `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/ac5_probe.py` read the 14519 tracked `.md` files under `memory/` through `tree_lib.unfenced_lines`. It found 24 files whose plain folds repeat, 0 files holding two equal anchors, and 0 empty folds. This also supports the spec's claim that the `doc` rows the `tags` leg reads are unchanged.
- The lexicon check `--suggest derive_anchor --as py.function` said OK.
- `gotchas.py --for-diff HEAD~1..HEAD` listed 31 classes. I went through the relevant ones: the plant's fixture does trigger the rule, the staged break is the one the spec names, every ledger token sits on one line, no heredoc or inline fence was written, and the arm rows split on `|`, so an empty last field does not shift the others. None needed a change.
- The pre-commit hooks passed, including hygiene check 23 on the ledger.
- No command timed out or was skipped.

**Owed at the close (main loop)**
- The `New arm:` for `tools/playbook/adopt-playbook.sh` (covers AC3 and AC4): the two `repeat-heading` rows of the tag-resolver block, run by the `playbook render selftest` leg. Each needs to be seen RED-first on the staged break (`extract_doc` folding with `derive_heading_seg` alone), then green once restored, and recorded as a seen-red line.
- The spec's legs on the spec's gates section: `playbook render selftest`, `govkit acceptance matrix`, `policy fixtures` and `tags (the resolver's checks)`.
- AC1, AC2 and AC5 are checked by no leg; this pass's probes are their only check.
