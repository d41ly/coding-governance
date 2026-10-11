# Acceptance ledger — TOOL-aHomedAnchor-1

**Serves:** journal TOOL-aHomedAnchor-1

Tier-2 · node a · 2026-10-09

The kit self-test suites were NOT run, by the owner's instruction. Every OBSERVED line below names
an arm of `tools/unattended/unattended.test.sh` observed through a SLICE: the suite's prologue plus
only this build's local-anchor block, at `d31d7bc9`, 45 assertions, `SLICE-PASS`, 8 min 50 s.

**Evidences:** TOOL-aHomedAnchor-1
- AC1 — `anchor-kind: local` — the slice's AC1 arm: a slug README on an unpushed branch preflights OK under local and the record names the anchor
- AC2 — `the remote advertises no tip for the branch this run is on` — the slice's AC2 arm, same fixture under published
- AC3 — `is not an ancestor of HEAD` — the slice's AC3 arm, a parentless base over the same tree
- AC4 — `built nothing` — the slice's AC4 arm, a recorded base equal to HEAD at --authorization
- AC5 — `may:` — the slice's AC5 arms: fail 78 and fail 89 name the local anchor, and a recipe README passes check 50
- AC6 — `adopt-unattended.sh` — this repo's render reads the anchor as local at TOOL-aHomedAnchor-3, and TOOL-aHomedAnchor-5's adopter-suite slice observes it in a seeded host
