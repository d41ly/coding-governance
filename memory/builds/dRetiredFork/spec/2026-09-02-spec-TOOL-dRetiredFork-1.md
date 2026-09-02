# TOOL-dRetiredFork-1 — memory-tree arms `pop_guard` on check 6

**Status:** CLOSED · rev-3 · 2026-09-03 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-prompt-TOOL-dRetiredFork-1-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-1-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Absorb, verbatim, the two-line `pop_guard` arming NicoCares added to check 6 and has carried
privately as `nc carve-out 5/20`. gov arms `pop_guard` on checks 3, 4, 5, 8, 12, 21, 22 and 23 and
not on 6, so check 6 reports a clean zero over an empty population instead of refusing.

## 2. Scope (IN)

- **S1** — Paste NicoCares `scripts/check-memory-hygiene.sh:552-553` into
  `tools/memory-tree/check-memory-hygiene.sh` immediately after the `bad6` fail, using gov's own
  `pop_guard` helper and gov's message shape rather than nc's wording.
- **S1b** — Author check 6's PRECONDITION expression, because `pop_guard` does not refuse on an
  empty population. Measured: it takes four arguments at `tools/memory-tree/check-memory-hygiene.sh:199`
  and returns silently unless the FOURTH — the precondition count — is greater than zero (`:202`).
  It refuses on a MIS-SEGMENTED selector, not an empty one, deliberately, so a freshly scaffolded
  repo with no builds stays legal. None of the existing `PRE_*` expressions at `:206-216` covers
  check 6's `INDEX_SET`, which spans guides, ledger shards, build READMEs and map dossiers. The
  precondition is the un-segmented count of index-class files anywhere under `$M/`.
- **S2** — One arm in `tools/memory-tree/check-memory-hygiene.test.sh` that observes the refusal:
  stage a tree whose check-6 population is empty, confirm RED, unstage.
- **S3** — Bump `KIT_MEMORY_TREE_VERSION` and every marker `tools/check-kit-versions.sh` pairs
  against it, in the same commit.

## 3. Non-goals (OUT)

- Re-auditing which other checks want a `pop_guard`. Eight already have one; this unit closes the
  one an adopter measured, and a sweep is its own unit.

## 6. Acceptance criteria

- **AC1** — When check 6's population is empty AND its precondition count is non-zero, `bash
  tools/memory-tree/check-memory-hygiene.sh` refuses naming the mis-segmented selector, and the RED
  is observed before the arm is wired. An empty population with a zero precondition stays green,
  which is `pop_guard`'s contract and not a gap.
- **AC2** — When the tree is unchanged, the same command exits `0` and the check-6 verdict line is
  byte-identical to its pre-change output.
- **AC3** — When the version moves, `bash tools/check-kit-versions.sh` exits `0`.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `harness arms (fail branches armed or pinned)`.

## 8. Open questions

none - it absorbs a two-line arming VERBATIM onto a check whose eight siblings already
carry it, so the mechanism is the sibling's. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H9. rev-1's AC1 stated behaviour `pop_guard` does not have:
  it refuses on a mis-segmented selector, not an empty population, and returns silently on a zero
  fourth argument. S1b now authors the missing precondition and AC1 is restated in the helper's own
  terms, so the staged RED S2 requires is producible.
- rev-3 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.
