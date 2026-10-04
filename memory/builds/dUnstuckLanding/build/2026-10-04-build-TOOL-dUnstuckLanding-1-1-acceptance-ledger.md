# TOOL-dUnstuckLanding-1 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-1

The census was assembled from three read-only historian passes, one per repository. Their reports
sat in the session scratchpad and are not tracked. The orchestrator then re-ran the two
observations the design rests on: the merge-after-abort read over every ABORTED record in all three
repositories, and the driver line reads. No gate leg was run in this pass.

**Evidences:** TOOL-dUnstuckLanding-1
- AC1 — `2026-10-04-build-TOOL-dUnstuckLanding-1-census.md` — the "The runs" section has a
  sub-section for each of gov, nc and inCMS. Since rev-2 (closing review M17), each one carries a run
  table with slug, code, stage, landing and abort on every row. That covers all 15 gov aborts across
  two tables, 13 in nc and 9 in inCMS. Every sha in those tables was checked with `git cat-file -e`
  in its own repository.
- AC2 — `git log origin/main` — for every ABORTED record (8 in gov, 13 in nc with one retired, and
  9 in inCMS with one retired), `git log <tip> --merges --grep=<slug>` found a merge naming the slug for
  29 of the 30. The 30th is nc `dBarredPostern`, whose work the historian traced to `23be1536`, a
  merge of another branch. The landed-later cells agree with those landings. One gov row was wrong at rev-1:
  aMeteredTurnstile's work merged at `3214f393`, before its abort, and it is corrected. The witness
  ancestry probe, which also read ON for all 30, is structural for a record read from the tip, so it
  is not evidence for this criterion (closing review H1).
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
