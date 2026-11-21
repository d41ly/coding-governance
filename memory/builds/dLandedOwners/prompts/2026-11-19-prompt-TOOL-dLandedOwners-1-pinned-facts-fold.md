# Revision — dLandedOwners: unpinned figures in the specs of units 1 and 2

**Serves:** research TOOL-dLandedOwners-1 TOOL-dLandedOwners-2

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries a pass-leg red back to the spec writer.

## The brief

### Goal
The pass legs over `c3f402ac1` read the writing-practice leg red: its pinned-facts check names unpinned figures in
`memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-1.md` (the leg ceiling and the instrument's
measured cost, at its lines 44, 56, 231 and 271) and in
`memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-2.md` (the probe's file count, at its lines 143
and 144). Pin each one so the check reads them green.

### Items
1. Give every figure on those lines that the pinned-facts check grades a pin on its own line: the owning source as a
   `path:line` or `path#symbol` (the leg ceiling lives in `tools/gate-legs.json`), `PINNED` or `DERIVED` where the
   figure is a measurement this build made, or a code span opening and closing on that line.
2. Sweep both specs, and spec 3, for any other figure before a unit word with no pin on its line, and pin it the
   same way.
3. Add one revision-log line to each spec you touch, naming this record. Leave the rev token and every design
   statement as they stand.

### Acceptance
`python tools/playbook/writing_practice.py check` names no pinned-facts red
in any dLandedOwners spec; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>`
stay clean for each spec touched; `unattended.sh --plan dLandedOwners --paths` still grades all three READY.

### Gates
The spec-format, spec-token and writing-practice checks the role allows; no other gate.

### Non-goals
No design change; no product code; no commit and no index render, which the main loop does.
