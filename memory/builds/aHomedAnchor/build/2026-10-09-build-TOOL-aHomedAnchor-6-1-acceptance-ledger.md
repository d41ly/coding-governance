# Acceptance ledger — TOOL-aHomedAnchor-6

**Serves:** journal TOOL-aHomedAnchor-6

Tier-2 · node a · 2026-10-09

Observed through the same driver-suite slice as TOOL-aHomedAnchor-1, at `d31d7bc9`, 45 assertions,
`SLICE-PASS`. The suite was not run, by the owner's instruction. S8 and S9 are not observed by an
arm: an initialisation and prose, read in the closing review. M3 and M9 are closed by
TOOL-aHomedAnchor-3 and TOOL-aHomedAnchor-5.

**Evidences:** TOOL-aHomedAnchor-6
- AC1 — `the BASE came from the local anchor` — the asks: arm prints fail 71's local clause
- AC2 — `no build README at the pinned BASE` — an uncommitted README under local reads fail 6, and the generic fail 16 is absent
- AC3 — `authorization-reachable — met` — the honest local record reads met at its preflight base
- AC4 — `is not an ancestor of the base this history derives` — present for the orphan base, absent for the unit-only ancestor
- AC5 — `base:` — the re-preflight over the retired record pins the new HEAD and not the old base
- AC6 — `spec-audit — not owed` — a run-branch SPEC_AUDIT_DEFAULT opts nothing in
- AC7 — `the record pins none` — the take-over --resume refuses a record with no base line
