**Serves:** journal TOOL-dTotalRecall-118
**Caused-by:** TOOL-dTotalRecall-118

# TOOL-dTotalRecall-118 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `ee5987930` from [2026-11-25-prompt-TOOL-dTotalRecall-118-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-118-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `8e9ad3d6d`.

## Why

Spec rev-1 is built as written. AC1 to AC4 are observed, the spec is CLOSED in the pass commit, and the bug-class checklist was run over the commit with nothing left to act on.

## Summary

`tools/runlog/memory_measure.py#check_memory_word` now counts a word that resolves to the memory root itself, in the main worktree and in a linked one. The module and function docstrings say so. The five `root-` plants and their `FIXTURE_CASES` names are in. `tools/runlog/selftest.py` has the dropped memory block back, with `test_memory_dtr118_root` after it and `ASSERTION_FLOOR` at 1724 (DERIVED 2026-11-25). `symbols.json` is re-rendered. The ledger is C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-118-1-acceptance-ledger.md.

Checks run; they stand in for the `runlog selftest` leg on this unit's code:
- AC1: a probe over `derive_read_channel` answered read, shell, read, shell, None, and None for the other tree. Before the edit, all five calls answered None (DERIVED 2026-11-25).
- AC2: the five CLI plants read 400 on read, 350 on shell, 300 on read, 250 on shell, and 0 for the sibling, each over one agent. With both equalities cut in a scratch copy of the kit, the four counting plants read zero (DERIVED 2026-11-25).
- AC3: the grep printed 10, and the restored block equals `ffa0dcf2d^1`'s byte for byte, nine arms (DERIVED 2026-11-25).
- AC4: the grep printed the raise line and the matching floor. The new arm, imported alone, made 10 checks with no failure, and `parse_floor_raise` read 1711 and 1724 (DERIVED 2026-11-25).
- The naming lexicon's `--suggest` accepted the new arm's name. Its `--measure` printed `VERB_OFFENDER_PIN` at 1437, equal to the conf (DERIVED 2026-11-25). The pre-commit hook passed.

Owed to the close:
- The RED-first observation of `test_memory_dtr118_root` on the old `check_memory_word`.
- The first run of the nine restored arms inside the suite; only their bytes were compared here.
- The section 7 legs. (DERIVED 2026-11-25, the pass)

One imprecise claim in the spec, which changes nothing built. Section 4 says the restored arms are what the 1711 already counts. The raise line counts seven of the nine, so the checks of `test_memory_dtr43_paths` and `test_memory_dtr53_paths` sit above the floor. The floor is lower than it could be but refuses nothing wrongly; the ledger and a `Decided:` trailer name it. (DERIVED 2026-11-25, the pass)

No gate, suite or bar was run and no command was skipped. No path outside the declared write set was written, and the brief was already recorded unchanged.
