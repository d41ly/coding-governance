# TOOL-dUnstuckLanding-1 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-1

The census was assembled from three read-only historian passes, one per repository. Their reports
sat in the session scratchpad and are not tracked. The orchestrator then re-ran the two
observations the design rests on: the witness-ancestry probe over every ABORTED record in all three
repositories, and the driver line reads. No gate leg was run in this pass.

**Evidences:** TOOL-dUnstuckLanding-1
- AC1 — `2026-10-04-build-TOOL-dUnstuckLanding-1-census.md` — the "The runs" section has a
  sub-section for each of gov, nc and inCMS. Every gov row carries an abort sha or a landing sha in
  its evidence cell. The nc and inCMS sub-sections cite their landing commits and abort commits by
  sha.
- AC2 — `git log origin/main` — `git merge-base --is-ancestor <witness> <remote tip>` was run for
  every ABORTED record: 8 in gov, 13 in nc (one of them retired) and 9 in inCMS (one of them
  retired). All 30 read ON, and the merge each `git log <tip> --merges --grep=<slug>` found follows
  its abort commit. The probe is live: nc `a7e0eb03` and inCMS `eafbff4f4`, both known unmerged,
  read OFF.
- AC3 — `## Failure classes` — K1 to K6 each state per-repo counts, cite two or more instances, and
  name a root cause. K1's root causes are its five sub-shapes. K2's root cause is BUILD-METHOD M3's
  park rule. K3's is `refuse_if_terminal`. K4 to K6 each carry a **Root cause** line.
- AC4 — `unattended.sh` — every line the census cites was opened at BASE:
  - `:647` is `PHASES_TERMINAL="LANDED ABORTED"`.
  - `:2675-2690` is `refuse_if_terminal` with fail 26.
  - `:1160-1164` is `read_derived_phase`, which returns early unless the phase is LANDING.
  - `:7115` is `check_inherited_override`, and its fail 83 is at `:7148`.
  - `run-gates.sh:2385-2400` is the classifier's KF3 and comparator rules, and `:2373-2375` is the
    "Five recorded stops" header.
