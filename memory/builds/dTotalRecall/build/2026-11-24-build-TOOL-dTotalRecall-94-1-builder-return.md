**Serves:** journal TOOL-dTotalRecall-94
**Caused-by:** TOOL-dTotalRecall-94

# TOOL-dTotalRecall-94 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `ea222030e` from [2026-11-24-prompt-TOOL-dTotalRecall-94-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-94-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `94cb5885a`.

## Why

Spec rev-2 was built as written. The claims it makes about the tree that I probed held at the base, and AC1 to AC4 were all observed. Unit 90's AC3 answer falls on the first row of section 4's table, so no deviation record is owed and none was written. The commit holds the acceptance ledger, the CLOSED header, RUN.md and the regenerated index rows.

## Summary

All figures here are DERIVED 2026-11-24. The fences of specs 94, 93 and 90 were extracted verbatim into files under the scratch directory and sourced. `has_deviation_90` differs from spec 90's fence only in its first line's name, checked by `diff`. I ran no gate, suite, bar or selftest.

Criteria, all observed:
- AC1: over the build folder, `census` with `has_deviation` printed 89 census lines and no red line. File counts sum to 147 and probe counts to 147, which is the 150 records less 3 superseded. (DERIVED 2026-11-24)
- AC2: `census` with `has_deviation_90` printed 89 census lines and 72 red lines. Sorted, they are `diff`-equal to the 72 lines of `scan_foreign`, and `red census 59` is among them. (DERIVED 2026-11-24)
- AC3: over the fixture, `has_deviation` printed 2, 1, 1, 1 and 0 for units 59, 5, 89, 61 and 590, and 2 for unit 59 after the superseding record. `census` with `has_deviation_90` printed red for units 59, 61 and 89 alone, before and after, as did `scan_foreign`. (DERIVED 2026-11-24)
- AC4: the ledger quotes unit 90's AC3 answer beside the census lines of units 59 and 90. The row is the first, so no record is owed. `has_deviation` with the token `audit-89 id 28 ac3` printed 0 for unit 90 before and after. With no token it prints 1, so the zero can move. (DERIVED 2026-11-24)

Checks standing in for gates: these probes stand in for no leg of section 7. `memory hygiene`, `recall floor` and `recall floor arms` are owed to the close. The spec declares no new arm, so no RED-first observation is owed. The pre-commit hook's own staged checks passed. `gotchas.py --for-diff HEAD~1..HEAD` ran and needed no change: no ledger token is wrapped, no table cell holds a pipe, and the fixture and the census were each seen red on unit 90's probe.

Skipped: nothing timed out. The two censuses ran in the background beside each other, 238 s each, with no deviation record written during them. (DERIVED 2026-11-24)

Notes:
- The orientation card said unit 94 was DEFERRED. The spec was INPROGRESS at the base, so the card was stale. (DERIVED 2026-11-24, the pass)
- The `--brief` verb reported the brief already recorded and unchanged. I declared no path beyond the dispatched set.
- With no unit INPROGRESS after this close, `gen_build_index.py` derives the build as DEFERRED in LIVE.md, backlog/TOOL.md and the build README. It changes back when the next unit is flipped.

Ledger: C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-94-1-acceptance-ledger.md
