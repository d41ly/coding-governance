# Acceptance ledger — TOOL-aHomedAnchor-4

**Serves:** journal TOOL-aHomedAnchor-4

Tier-1 · node a · 2026-10-09

Observed twice: by hand in a throwaway repo before the commit, and through a slice of
`.githooks/pre-commit.test.sh` holding only the new block, 2 passed, 0 failed.

**Evidences:** TOOL-aHomedAnchor-4
- AC1 — `--check` — a staged .unattended.conf printed WIRING RAN --check from the stand-in
- AC2 — `--check` — an unrelated staged file ran the stand-in zero times; the slice counts one run across both commits
