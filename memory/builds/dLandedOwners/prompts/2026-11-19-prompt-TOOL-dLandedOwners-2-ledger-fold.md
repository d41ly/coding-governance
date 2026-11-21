# Revision — dLandedOwners: TOOL-dLandedOwners-2 names its acceptance ledger

**Serves:** research TOOL-dLandedOwners-2

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries a defect unit 1's builder found in its own spec, which unit 2's spec shares, to the spec writer before unit 2's dispatch.

## The brief

### Goal
Unit 1's first build pass stopped because its spec's Files touched left out the acceptance ledger that closing the
spec needs (`memory/HYGIENE.md`, "Acceptance ledger"); see
`memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-divergence-1.md`. The spec
`memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-2.md` has the same gap. Close it before unit 2
is dispatched.

### Items
1. Add `memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-2-ledger.md` to section 4's Files
   touched, and add to section 7 every leg `python tools/check-spec-tokens.py --spec <path>` says that path trips.
2. Read the builder's other findings in that divergence record and unit 1's rev-3 revision-log line. Where one of
   them holds for this spec too (a fixture that copies a kit's modules no `policy fixtures` guard covers, a
   module already loaded that hides a refusal, a count of fixture lines that omits the guard-trace and count
   lines), fix it the same way; otherwise leave the spec as it stands.
3. Unit 1 is now built at `c5255c179`; where this spec cites `tools/policy/check_policy.py` by a line or a blob
   that unit 1 moved, re-ground the citation against HEAD.
4. Bump the rev and add one revision-log line naming this record.

### Acceptance
`bash tools/unattended/unattended.sh --plan dLandedOwners --paths` grades TOOL-dLandedOwners-2 READY;
`--check-specs dLandedOwners TOOL-dLandedOwners-2` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>`
and `check-spec-tokens.py --spec <path>` are clean.

### Gates
The spec-format and spec-token checks the role allows; no other gate.

### Non-goals
No change to the reader scan's design beyond what item 2 finds; no product code; no commit and no index render,
which the main loop does.
