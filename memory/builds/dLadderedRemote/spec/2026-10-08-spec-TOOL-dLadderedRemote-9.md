# TOOL-dLadderedRemote-9 — the round-5 minors: argv lists followed by more arguments, and three exact sentences

**Status:** CLOSED · rev-1 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6 TOOL-dLadderedRemote-7 TOOL-dLadderedRemote-8 |

<!-- /gen:spec-records -->

## 1. Goal

Every item of the round-5 closing review, the round at which the diff review exits. The record is
`memory/builds/dLadderedRemote/reviews/2026-10-08-review-TOOL-dLadderedRemote-8-closing-diff-round5.md`.
Its four items are this unit's scope, built from this spec as written.

## 2. Scope (IN)

- **S1** — item 1, in `tools/check-remote-literals.sh` and its self-test. The list-in-call shape
  becomes a list opened right after `(` or `,` whose last element is the quoted name, whatever
  follows the list. One RED row plants `subprocess.run(["git", "remote", "show", "origin"], check=True)`.
  Observed by AC1.
- **S2** — items 2 and 4, in the same header. It states that a comment line in a path holding a colon
  is not skipped, a false RED, and that only a path holding `:<digits>:` followed by a comment leader
  can hide a hit. It also states that a key list or tuple passed into a call whose last element is
  the name is a hit, cleared by hoisting it into a named constant. Observed by AC2.
- **S3** — item 3: `WIRE-INTO-PROJECT.md` says the pin cross-checks only when the observed HEAD
  carries the conf, that otherwise the pin chooses (the straggler guard: else `main`), and that
  `migrate_backlog.py` refuses with neither. Observed by AC2.

## 3. Non-goals (OUT)

- A further review round. The diff review exited at round 5 by M4's strictly-smaller rule.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-8` — the list-in-call shape and the sentences this unit corrects

## 4. Design

### Files touched (estimate)

- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `WIRE-INTO-PROJECT.md`

## 5. Production-readiness checklist

- security: N/A — a lint and three sentences.
- perf / scale: unchanged.
- error / empty / loading states: unchanged.
- observability: the header states two more behaviours.
- risks: the widened shape could hit current code; it runs over the real tree before it is wired.
- testing: one RED row, red with the shape reverted to unit 8's.
- migration: none.
- user docs: S3.

## 6. Acceptance criteria

- **AC1** — When the ban's self-test plants `subprocess.run(["git", "remote", "show", "origin"], check=True)`,
  `check-remote-literals.sh` names it, every GREEN row stays clean, and the real tree reads clean.
  Red when: unit 8's shape is restored and the row goes unnamed.
- **AC2** — When `check-remote-literals.sh` and `WIRE-INTO-PROJECT.md` are read, each carries its S2 or
  S3 sentence. Red when: one is missing.

## 7. Gates

`remote literals (kit code names no remote)` · `remote literals self-test`

New arm: tools/check-remote-literals.test.sh · covers AC1 · the shape reverted to unit 8's · FLOOR_ASSERTIONS

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft, from the round-5 closing review.

## 10. Reuse audit

Every item amends this build's own ban and runbook text. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found nothing beyond them.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
