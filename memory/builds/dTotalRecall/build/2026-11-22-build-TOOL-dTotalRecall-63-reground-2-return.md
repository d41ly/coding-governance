**Serves:** research TOOL-dTotalRecall-63

# TOOL-dTotalRecall-63 second re-ground over units 5, 54 and 38 as built — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-2-spec-writer.md), in substance.

- Folded to rev-4 at base `94e17798`; `check-spec-tokens.py --spec`, `--check-specs`, hygiene check 12 and `writing_practice.py check pinned-facts` exit 0.
- §1: unit 54's `parse_id_parts` takes a keyword-only `alt` and unit 38 made most callers pass one, so a rebuild onto `_id_alternation` moves only the default-family readers (`drift_report.py#_parse_slug`, `check-recall.py#derive_probe_labels`, `query.py#measure_answer_used`, unit 45's readers).
- Its §4 now holds both sides of the distinguishing case, run in a scratch tree declaring a cited family; §3 and AC2 pin unit 54's pass commit `74af3faa4`; §7 names unit 54's arm by symbol.
- AC2 fixed: it read `git log` newest first, so a correct order read red; it reads `--reverse` now.
- AC1 still opens red, as designed; no fork, no new function, leg, arm or class row; every edge already has its mirror.

## Unit 46 waits for units 63 and 64

Decided by the main loop: unit 46's own re-check runs after units 63 and 64 are built, since both passes amend spec 46's text and a re-ground first would move the text their amendments replace.
