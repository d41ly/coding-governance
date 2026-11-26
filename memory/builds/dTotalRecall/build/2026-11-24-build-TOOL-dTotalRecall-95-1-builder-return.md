**Serves:** journal TOOL-dTotalRecall-95
**Caused-by:** TOOL-dTotalRecall-95

# TOOL-dTotalRecall-95 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `5d0ce047a` from [2026-11-24-prompt-TOOL-dTotalRecall-95-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-95-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `a3c73bc04`.

## Why

Spec rev-2 could be built as written; its cited code, its key table, and the records of units 74, 83, 90 and 93 were checked against the tree before the first edit, and AC1 and AC2 are both observed. (DERIVED 2026-11-24, the pass)

## Summary

TOOL-dTotalRecall-95 is built and CLOSED. It changes no product code; it adds the acceptance ledger and closes the spec. No deviation record is owed, so none was written.

**AC1:** the section 4 fences and spec 93's `has_deviation` were extracted verbatim and sourced. The four fixture runs printed the section 4 pins (DERIVED 2026-11-24):
- First: the `key59 missing` line naming the fixture's 591, then `key59 1 0`. (DERIVED 2026-11-24, the pass)
- Second: the same `missing` line, then `key59 2 1`.
- Third: `key59 1 1` alone.
- Fourth: `key59 red the probe failed` alone.

**AC2:** run over memory/builds/dTotalRecall/build both before and after the ledger was written (DERIVED 2026-11-24):
- `key59` printed `key59 0 0`, and `has_deviation` for unit 59 with the string printed 0. (DERIVED 2026-11-24, the pass)
- The tokenless `--paths` run listed the roster record 591 and 1. (DERIVED 2026-11-24, the pass)
- The `Caused-by` grep over unit 59's records listed nothing; over the fixture it listed 592, so it can find a match. (DERIVED 2026-11-24, the pass)
- Extra probes: a raising probe over the build folder printed the red line, and an empty folder printed `key59 0 0`.

No path is handed to TOOL-dTotalRecall-89.

**Checks:** these probes are the unit's acceptance observations and stand in for no gate. No bar, suite, leg or selftest was run by hand; the pre-commit hook's own checks passed. The section 7 legs `memory hygiene`, `recall floor` and `recall floor arms` are owed to the close, and no new arm or RED-first observation is owed. (DERIVED 2026-11-24, the pass)

**After the commit:** `gotchas.py --for-diff HEAD~1..HEAD` selected 29 classes (DERIVED 2026-11-24). I read the relevant ones against the diff (unwrapped ledger tokens, a fixture seen both ways, the Serves line) and none needed a change. No command was skipped for its bound, the brief was already recorded unchanged, and the tree is clean.

RUN.md and the files `gen_build_index.py --write` rewrote (memory/LIVE.md, memory/backlog/TOOL.md, the build README and the spec's records table) are in the commit. With no unit INPROGRESS, the build and ask TOOL-dTotalRecall-27 now derive as DEFERRED until the next unit is flipped.

C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-95-1-acceptance-ledger.md
