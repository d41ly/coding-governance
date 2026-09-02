# TOOL-dRetiredFork-1 — memory-tree arms `pop_guard` on check 6

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Absorb, verbatim, the two-line `pop_guard` arming NicoCares added to check 6 and has carried
privately as `nc carve-out 5/20`. gov arms `pop_guard` on checks 3, 4, 5, 8, 12, 21, 22 and 23 and
not on 6, so check 6 reports a clean zero over an empty population instead of refusing.

## 2. Scope (IN)

- **S1** — Paste NicoCares `scripts/check-memory-hygiene.sh:552-553` into
  `tools/memory-tree/check-memory-hygiene.sh` immediately after the `bad6` fail, using gov's own
  `pop_guard` helper and gov's message shape rather than nc's wording.
- **S2** — One arm in `tools/memory-tree/check-memory-hygiene.test.sh` that observes the refusal:
  stage a tree whose check-6 population is empty, confirm RED, unstage.
- **S3** — Bump `KIT_MEMORY_TREE_VERSION` and every marker `tools/check-kit-versions.sh` pairs
  against it, in the same commit.

## 3. Non-goals (OUT)

- Re-auditing which other checks want a `pop_guard`. Eight already have one; this unit closes the
  one an adopter measured, and a sweep is its own unit.

## 6. Acceptance criteria

- **AC1** — When check 6's population is empty, `bash tools/memory-tree/check-memory-hygiene.sh`
  refuses naming check 6, and the RED is observed before the arm is wired.
- **AC2** — When the tree is unchanged, the same command exits `0` and the check-6 verdict line is
  byte-identical to its pre-change output.
- **AC3** — When the version moves, `bash tools/check-kit-versions.sh` exits `0`.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit versions` · `arms (fail branches armed or pinned)`.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
