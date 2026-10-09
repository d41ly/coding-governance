# TOOL-aHomedAnchor-3 — re-render the unattended Skill from its template

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-1 · base 40a976d9 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close the closing review's HIGH id 7, and M3 with it: the committed Skill was hand-edited, so it
still names `published` where this repository's conf now declares `local`, and the wiring leg reds.

## 2. Scope (IN)

- S1. `.claude/skills/unattended/SKILL.md` is re-rendered by `tools/unattended/adopt-unattended.sh`
  from its template and this repository's conf. Observed by AC1.

## 3. Non-goals (OUT)

Any template text change: the template is right, the copy is stale.

### Edges

none

## 4. Design

The adopter is the only writer of the rendered Skill. Run it, commit what it writes.

### Files touched (estimate)

- `.claude/skills/unattended/SKILL.md`

## 5. Production-readiness checklist

- security — N/A — a render of committed inputs.
- testing — AC1.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs at this unit's commit, it
  exits 0 and the Skill reads `authorizes at this project's anchor, `local``.
  Red when: the copy is hand-edited again instead of rendered.

## 7. Gates

`unattended skill wiring` · `unattended skill size` · `check-wiring self-test` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from `memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md` HIGH id 7.

## 10. Reuse audit

The seam is the adopter's own render, `tools/unattended/adopt-unattended.sh`; no existing seam fits
anything else. Recall terms used: `--terms "adopt-unattended render SKILL.template.md ANCHOR_SCOPE
skill wiring check out of sync placeholder"`.
