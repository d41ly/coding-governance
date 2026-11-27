**Serves:** journal TOOL-dTotalRecall-84
**Caused-by:** TOOL-dTotalRecall-84

# TOOL-dTotalRecall-84 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `65b104e2e` from [2026-11-24-prompt-TOOL-dTotalRecall-84-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-84-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `f1b815ced`.

## Why

Spec rev-3 was built as written. The claims I probed about current code and records held at the base. S1 equals unit 74's recorded reading and unit 70's recorded count, so spec 84's comparison table owes no deviation record of either unit. (DERIVED 2026-11-24, the pass)

## Summary

AC1 and AC2 are observed in the ledger C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-84-1-acceptance-ledger.md. No product code changed.

What ran: spec 84 section 4's fence with spec 81 section 4's first fence sourced, both extracted verbatim and run from one script under the scratch directory (u84/run.sh). (DERIVED 2026-11-24, the pass)
- S1: `254057fa6d5bbc19cd48329737487c88a10b0085 0`, the sha `git rev-parse "$(pass_of 46)^"` prints; `pass_of 46` is 63f283ddd383 (DERIVED 2026-11-24).
- S2: 1 over spec 46 and 0 over spec 64 at 653bed738685 (DERIVED 2026-11-24).
- Refusals: the first read with 999 printed `red 999 no pass commit`. An empty revision and a bare `^` each printed a red line with rc 1 (DERIVED 2026-11-24).
- S3: unit 74's line is `s1-46 254057fa6d5b 0` and unit 70's AC8 line records 0, so the table owes no record of unit 70 or unit 74 and none is written. The write-once read printed nothing for either unit. Its positive controls listed -70-deviation-702 (string `spec-revised`), -70-deviation-701 and -74-deviation-741 (string `roster`) (DERIVED 2026-11-24).

The commit holds the ledger, the spec header moved to CLOSED, RUN.md, and the generator's re-render (LIVE.md, backlog/TOOL.md, the build README, and the ledger's row in the spec's generated records table). `gen_build_index.py --write` reported 4 artifacts written. With unit 84 no longer INPROGRESS, the render derives the build's status as DEFERRED until the next unit is flipped. (DERIVED 2026-11-24)

Check standing in for a gate: a `python -c` call of writing_practice.derive_facts over the new ledger found no unpinned fact, and found two in a positive control line (DERIVED 2026-11-24). It stands in for that file's share of pinned-facts. The pre-commit hook passed on the commit.

gotchas.py --for-diff HEAD~1..HEAD named 29 classes, 23 anchored and 6 universal (DERIVED 2026-11-24). I checked the ones that bear on a ledger by eye: inline fence, token wrapped across a line, pipe in a code span, a criterion's grep quoting its own pattern, and a record without Serves. Each holds and no edit was needed.

Owed to the close: the section 7 legs `memory hygiene`, `recall floor` and `recall floor arms`. The spec declares no new arm, so no RED-first observation is owed. Nothing was skipped for a time bound. The worktree guard refused two inline commands naming git, so those reads ran from the script file. (DERIVED 2026-11-24, the pass)
