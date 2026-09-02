# TOOL-dRetiredFork-13 — the `KIT_REL` default reaches the remaining test and selftest surface

**Status:** OPEN · rev-2 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Apply the mechanism that already works. `tools/unattended/check-unattended.test.sh` retired 127
hand-repathed sites into a `KIT_REL` default and `adopt-unattended.test.sh` retired 28 more at gov
`662c0e9a`. Both are measured, both are proven at three prefixes, and the idiom has never been
applied to the other 32 shipped test and selftest files, which carry 259 of the ratchet's 656
recorded occurrences.

## 2. Scope (IN)

- **S1** — One line per file — `KIT_REL="${KIT_REL:-tools/<kit>}"`, or its Python equivalent — with
  every kit-path literal beneath it read through the variable, across the 32 remaining shipped
  test and selftest files.
- **S2** — `tools/unattended/check-playbook.test.sh` last, because its 37 sites are unblocked only
  by `TOOL-dRetiredFork-12`.
- **S3** — Per file, the equivalence proof `TOOL-aGradedDoorway-2` established: expanding `$KIT_REL`
  back to its default and removing the added line reproduces the pre-change file BYTE FOR BYTE, so
  this repo's behaviour cannot have changed.
- **S4** — At least three files RUN at a foreign prefix, not merely proven equivalent. An
  equivalence proof covers regression and says nothing about the new capability, which is the gap
  `TOOL-aGradedDoorway-2` recorded honestly and this unit must not repeat silently.
- **S5** — Re-baseline `tools/install-prefix-carried.txt` in the same landing.

## 3. Non-goals (OUT)

- Widening the ratchet's population. Measured and unnecessary: arm 2 already has NO test exclusion —
  its own source says so — and 259 of its 656 occurrences are already test/selftest rows. Only arm 1
  excludes them, and arm 1 is the root-spelling ban, not the ratchet.
- Files outside the shipped surface. `tools/lib/` is gov-internal and never travels.
- Non-test shipped CHECKERS. `tools/check-wiring.sh` is the measured case and it is NOT this unit's:
  `TOOL-dRetiredFork-8` S6 takes its own literals in its own landing. rev-1 was named as that
  sweep's owner by `TOOL-dRetiredFork-8` §3 while this population excluded it, so the work had no
  owner at all; the pointer is corrected on both sides.

## 6. Acceptance criteria

- **AC1** — For each touched file, expanding `$KIT_REL` to its default and removing the added line
  reproduces the file's bytes at `b0108f13` exactly.
- **AC2** — At least three touched suites RUN green at `scripts/<kit>` and at a repo-root prefix,
  with their assertion counts recorded and equal to the default-prefix run.
- **AC3** — Any suite NOT run at a foreign prefix is named in the acceptance ledger as unexercised,
  with the reason, so a green row is never misread as a verified one. Recorded in this build's acceptance ledger under `memory/builds/dRetiredFork/build/`.
- **AC4** — `bash tools/check-install-prefix.sh` reports a carried total strictly below 656, and the
  ratchet is re-baselined in the same commit.
- **AC5** — `bash tools/check-testsuite-counts.sh` exits `0`, with every touched suite still
  printing its executed assertion count.

## 7. Gates

`install-prefix (shipped surface)` · `testsuite counts (every bar self-test prints one)` · every touched kit's own self-test leg,
run on demand under `GATE_SELFTESTS=1` rather than added to the bar.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H4. rev-1's population excluded the non-test checkers that
  `TOOL-dRetiredFork-8` §3 deferred to it, so 39 literal sites had no owning unit. §3 now names the
  owner explicitly and the pointer is corrected on both sides.
