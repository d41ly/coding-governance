**Serves:** journal TOOL-dTotalRecall-90
**Caused-by:** TOOL-dTotalRecall-90

# TOOL-dTotalRecall-90 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `c1203e18c` from [2026-11-24-prompt-TOOL-dTotalRecall-90-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-90-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `84c9a0821`.

## Why

The spec built as written and no check of it against the tree diverged. All seven labelled lines, both red reads, all seven guards and the fixture counts match §4's pins. No record is owed, and the spec header is CLOSED in the pass commit.

## Summary

TOOL-dTotalRecall-90 is committed as 84c9a0821, on base c1203e18c. It adds the acceptance ledger C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-90-1-acceptance-ledger.md, closes the spec header, commits RUN.md, and re-renders README.md, LIVE.md and backlog/TOOL.md. It touches no product code and writes no deviation record.

Checks run: §4's five fences verbatim, with unit 81's first bash fence sourced and the strings files taken from units 82, 83 and 84's own heredocs. They ran at the base and again at the tip with the same output. (DERIVED 2026-11-24, the pass)
- AC1: the block printed seven lines, one per label. `s1-67` read 1 at 56390bab8cce, `s1-59` 1 at 206422580b73, `s1-46` 0 at 254057fa6d5b. `live-59`, `live-62`, `live-46` and `live-64` read 0, 1, 1 and 0 at 653bed738685. The red reads printed `s1-999 red 999 no pass commit` and a line opening `s1-bad red no blob at` (DERIVED 2026-11-24).
- AC2: the grep named this ledger alone. Each `s1-*` line agrees with the S1 in its unit's ledger and with unit 74's lines. The decisions are spec 82's second row, spec 83's third and spec 84's second, and none owes a record. All seven guards printed 0. With the token `spec changed at`, units 70 and 83 printed 1 each, so the probe is seen both ways (DERIVED 2026-11-24).
- AC3: over a scratch folder `has_deviation` printed 0 with the ledger alone, 1 with the first record, 1 with a superseding second record, and 2 with the Supersedes line taken out (DERIVED 2026-11-24).
These probes stand in for no gate.

Owed to the close: §7's legs `memory hygiene`, `recall floor` and `recall floor arms`. The unit declares no new arm, so no RED-first observation is owed. The staged pre-commit checks passed at the commit. `gotchas.py --for-diff HEAD~1..HEAD` ran: each ledger token sits on one line, no table cell holds a pipe, and the zero-reading guards were seen non-zero, so nothing needed a change. No command was skipped.

For the caller:
- Units 93, 94, 95 and 100 read this ledger. Its `s1-bad` line leaves out spec 999's path, because spelling that path in a record made the index list a phantom id 999 for this build. It was caught before the commit and the index re-rendered. A later ledger quoting a read of spec 999 should leave it out too. (DERIVED 2026-11-24, the pass)
- The index now reads the build DEFERRED, and ask TOOL-dTotalRecall-27 likewise. No unit is INPROGRESS between this commit and the next flip, so no action is needed.
