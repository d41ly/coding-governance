# TOOL-dLadderedRemote-8 — the round-4 minors: two restored ban spellings and four exact sentences

**Status:** CLOSED · rev-2 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6 TOOL-dLadderedRemote-7 TOOL-dLadderedRemote-9 |
| [2026-10-08-review-TOOL-dLadderedRemote-8-closing-diff-round5.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-8-closing-diff-round5.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

Every item of the round-4 closing review, built as the one batch unit M4 prescribes. The record is
`memory/builds/dLadderedRemote/reviews/2026-10-08-review-TOOL-dLadderedRemote-7-closing-diff-round4.md`.
Its items N1 to N4 are this unit's scope. Each change is the smallest that closes its item, because
the last two rounds each found an escape the previous narrowing made.

## 2. Scope (IN)

- **S1** — N1 and N3, in `tools/check-remote-literals.sh` and its self-test. A new shape catches the
  quoted name as a list's last element directly inside a call, `, "<name>"])`, which a bare key list
  never is. The `${...}` head admits an optional `!`. Two RED rows. Observed by AC1.
- **S2** — N2: the header names a path holding a colon as mis-split by the comment filter, a false
  RED and never a missed hit, and the merge comment claims only whole-line dedupe. Observed by AC2.
- **S3** — N4: the runbook says the two observed-first readers let the pin choose when nothing is
  observed; the skill's remote bullet names the `.` and unknown-name rungs; the govkit row's comment
  counts two interpolated values. Observed by AC2.

## 3. Non-goals (OUT)

- Splitting `git grep` output on NUL. A colon in a path costs a false RED, which is the safe
  direction, and the header now says so.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-7` — the narrowed ban and the runbook text this unit corrects
- **hands-off** `TOOL-dLadderedRemote-9` — the round-5 review's corrections to this unit's shape and sentences

## 4. Design

### Files touched (estimate)

- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `WIRE-INTO-PROJECT.md`
- `skills/session-kickoff/SKILL.md`
- `tools/govkit/govkit.py`

## 5. Production-readiness checklist

- security: N/A — a lint and four sentences.
- perf / scale: unchanged.
- error / empty / loading states: unchanged.
- observability: the header states the colon-path behaviour.
- risks: the new shape could hit current code; it runs over the real tree before it is wired.
- testing: two RED rows, each red with its pattern removed.
- migration: none.
- user docs: S3.

## 6. Acceptance criteria

- **AC1** — When the ban's self-test plants `subprocess.run(["git", "remote", "show", "origin"])` and
  `r=${!ref:-origin}`, `check-remote-literals.sh` names both, every GREEN row stays clean, and the real
  tree reads clean. Red when: removing the new shape or the `!` leaves its row unnamed.
- **AC2** — When `check-remote-literals.sh`, `WIRE-INTO-PROJECT.md`, `skills/session-kickoff/SKILL.md`
  and the govkit row are read, each carries its S2 or S3 sentence. Red when: one is missing.

## 7. Gates

`remote literals (kit code names no remote)` · `remote literals self-test` · `scratch-guard self-test` · `govkit selftest` · `manifest-check self-test` · `lexicon naming predicates` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/check-remote-literals.test.sh · covers AC1 · one pattern removed at a time · FLOOR_ASSERTIONS

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft, from the round-4 closing review.
- rev-2 · 2026-10-08 · §3 · the hands-off edge to `TOOL-dLadderedRemote-9`, the round-5 batch unit.

## 10. Reuse audit

Every item amends this build's own ban and prose. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found nothing beyond them.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
