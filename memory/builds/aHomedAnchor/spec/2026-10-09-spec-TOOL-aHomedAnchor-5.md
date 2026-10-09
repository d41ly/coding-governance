# TOOL-aHomedAnchor-5 — an adopter arm proves the render of `ANCHOR_SCOPE="local"`

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-1 · base 40a976d9 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aHomedAnchor-5-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aHomedAnchor-5-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close the closing review's HIGH id 28 and M9: spec TOOL-aHomedAnchor-1's AC6 was claimed and no
arm observes it.

## 2. Scope (IN)

- S1. `tools/unattended/adopt-unattended.test.sh` renders a fixture conf declaring `local` and hits
  the anchor sentence naming `local`, and renders an unrecognised value and hits `default-branch`.
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

The adopter's code: TOOL-aHomedAnchor-1 changed it.

### Edges

none

## 4. Design

The AUTH_PARAM arms' shape: a seeded host, a conf line replaced, a render, a hit on content.

### Files touched (estimate)

- `tools/unattended/adopt-unattended.test.sh`

## 5. Production-readiness checklist

- testing — AC1, AC2.

## 6. Acceptance criteria

- **AC1** — When `adopt-unattended.sh` renders a host whose conf declares `ANCHOR_SCOPE="local"`, the
  Skill reads `authorizes at this project's anchor, `local``.
  Red when: the `local)` case arm is removed.
- **AC2** — When the conf declares `ANCHOR_SCOPE="nearby"`, the Skill reads the `default-branch`
  anchor. Red when: an unrecognised value renders as itself.

## 7. Gates

`unattended skill wiring`

New arm: tools/unattended/adopt-unattended.test.sh · covers AC1 AC2 · a host conf declaring local, and one declaring a value outside the set · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from `memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md` HIGH id 28 with M9.

## 10. Reuse audit

The seam is the suite's `authconf` helper and its AUTH_PARAM arms. Recall terms used: `--terms
"adopt-unattended test authconf render ANCHOR_SCOPE AUTH_PARAM seed host Skill"`.
