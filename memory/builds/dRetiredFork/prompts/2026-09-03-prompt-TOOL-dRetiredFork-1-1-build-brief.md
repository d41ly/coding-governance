# Build brief — TOOL-dRetiredFork-1

**Serves:** journal TOOL-dRetiredFork-1

## What the unit is

gov arms `pop_guard` on checks 3, 4, 5, 8, 12, 21, 22 and 23 — and not on 6. So check 6 reports a
clean zero over an empty population instead of refusing. NicoCares found this and has carried the
two-line arming privately as `nc carve-out 5/20`.

## What this pass does

1. S1 — arm `pop_guard` on check 6, immediately after the `bad6` fail at
   `check-memory-hygiene.sh:508`, using gov's own helper and gov's message shape.
2. S1b — AUTHOR the missing precondition. `pop_guard` returns silently unless its FOURTH argument
   is greater than zero, and none of the existing `PRE_*` expressions covers check 6's `INDEX_SET`,
   which spans `LIVE.md`, `DECISIONS.md`, ledger shards, backlog shards, build READMEs, `RUN*.md`,
   guides and map dossiers. The precondition is deliberately UN-SEGMENTED: it asks what KIND of
   file exists, never where, exactly as `PRE_BINDABLE` does.
3. S2 — one arm in the self-test that OBSERVES the refusal: stage a tree whose check-6 population
   is empty while its precondition is non-zero, confirm RED, unstage.
4. S3 — bump `KIT_MEMORY_TREE_VERSION` and EVERY marker `check-kit-versions.sh` pairs against it,
   in the same commit. Measured earlier this run: there are SEVEN carriers, not the three
   `check-verdict-epoch.sh` names.

## The contract, so the arm is not written against the wrong behaviour

`pop_guard` refuses on a MIS-SEGMENTED selector, not an empty one. An empty population with a ZERO
precondition stays green — that is a freshly scaffolded repo and is legal. rev-2 folded exactly this
correction after round 1's H9; do not restate rev-1's premise.

## Acceptance

AC1-AC3, run rather than asserted, with the RED observed before the arm is wired.

## What this also owes

`tools/memory-tree/check-memory-hygiene.sh` is a WATCHED file in the kickoff manifest, so the
`last-audit` re-stamp is bundled into this commit.
