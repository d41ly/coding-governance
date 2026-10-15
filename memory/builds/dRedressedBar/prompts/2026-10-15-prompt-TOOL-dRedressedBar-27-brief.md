# Brief — dRedressedBar: hygiene check 23 green, this build's ledgers written and the base's foreign ledger lines fixed

**Serves:** research TOOL-dRedressedBar-27

## The prompt

> Fix them here

The owner's answer, 2026-10-15, to how this build handles the check 23 failures the base bar already carried in builds aSparedSpawn and aOrientedCast.

## The brief

### Goal
A full `bash tools/memory-tree/check-memory-hygiene.sh` at the build tip reds check 23 in three arms. (1) A CLOSED unit numbers an acceptance criterion no journal record evidences: TOOL-dRedressedBar-2, -4, -5, -7, -9, -11, -18 and -20 wrote no acceptance ledger. (2) An acceptance-ledger line is in neither legal form: TOOL-aSparedSpawn-10/AC9, -11/AC10, -13/AC11, -6/AC6, -6/AC8, -8/AC10, -8/AC6, -32/AC12. (3) A ledger answer shares no backticked token with its criterion: TOOL-aOrientedCast-22/AC7 and 29 aSparedSpawn entries. Arms 2 and 3 are byte-identical at the base `ebce889c7` (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-1-4-researcher.md`), so the base bar's `memory hygiene` leg was red on them too. Make check 23 pass with no waiver, by evidence.

### Items
1. **TOOL-dRedressedBar-27 — a records-only unit, order after unit 26.** No product code moves. Spec it as Tier-1 (records), with a scope item and an AC per arm.
   - **Arm 1:** one acceptance ledger per listed dRedressedBar unit, under `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal <unit id>`, one line per criterion in the OBSERVED or AMENDED form check 23 accepts. The readings come from what each unit's builder recorded: its commit body, its `Decided:` trailers and its return in `build/2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`. A criterion its builder did not observe is written as such (an AMENDED or an owed-at-close line in the legal form), never as an invented reading. Units 18's criteria are the rev the builder built against.
   - **Arms 2 and 3:** rewrite each listed foreign ledger line in place so it is in a legal form and shares a backticked token with its criterion, keeping its reading true to what that unit observed: read the unit's spec criterion and the ledger's own evidence before changing a word. A line whose observation cannot be reconstructed from the record is converted to the honest legal form check 23 accepts for an unobserved criterion, not given a token it did not earn. List every foreign line changed, before and after.
   - The check's legal forms, the token rule and any cutoff or grandfather keys are read from `tools/memory-tree/check-memory-hygiene.sh` check 23 and `.memory-tree.conf`; the spec cites them.
2. **The record:** the unit's own ledger evidences its ACs as usual.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 27 READY, ordered after unit 26. The spec names each of the 8 + 38 targets and an AC whose red half is today's check 23 output for that arm.

### Gates
`memory hygiene`

### Non-goals
- No product code, no checker change, no waiver or grandfather row added to make check 23 pass.
- No edit to any other part of the aSparedSpawn or aOrientedCast builds beyond the listed ledger lines.
- No merge to local main and no push without the owner's ask.
