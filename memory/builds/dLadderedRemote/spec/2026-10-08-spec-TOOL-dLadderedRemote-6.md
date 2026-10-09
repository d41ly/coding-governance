# TOOL-dLadderedRemote-6 — the round-2 minors: the ban's lost defaults, variables and argv, and two small honesty fixes

**Status:** CLOSED · rev-2 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-7 TOOL-dLadderedRemote-8 TOOL-dLadderedRemote-9 |
| [2026-10-08-review-TOOL-dLadderedRemote-6-closing-diff-round3.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-6-closing-diff-round3.md) | diff-review | TOOL-dLadderedRemote-5 |

<!-- /gen:spec-records -->

## 1. Goal

Every item of the round-2 closing review, built as the one batch unit M4 prescribes. The record is
`memory/builds/dLadderedRemote/reviews/2026-10-08-review-TOOL-dLadderedRemote-5-closing-diff-round2.md`.
Its items N1 to N7 are this unit's scope.

## 2. Scope (IN)

- **S1** — N1, N2, N3 and N4, in `tools/check-remote-literals.sh` and its self-test. A `${...}`
  default matches whatever the parameter is. The UNQUOTED assignment form is graded in shell files
  only, by a second `git grep` over the shell population, so a Python or JS variable named like the
  remote is not a hit. The remedy shape admits flags between the verb and the name. A new shape
  catches the list form, a quoted verb followed by quoted arguments ending in the quoted name. The
  last-argument shape also closes on `]`. Every spelling gets a RED arm, every variable form gets a
  GREEN one, and the header names what stays invisible: a call wrapped across lines. Observed by AC1,
  AC2.
- **S2** — N5: the codebase-map selftest's `finally` leaves the environment variable the arm sets
  exactly as the arm found it, set or unset. NOT OBSERVED by a criterion: a fixture hygiene fix whose break needs a failing
  assert to show.
- **S3** — N6: `WIRE-INTO-PROJECT.md` names the three readers that take the observed branch only, and
  says the ladder is above. Observed by AC3.
- **S4** — N7: the pre-commit guard prints the refusal only when `GOV_DEFAULT_BRANCH` is unset, and
  reads its current branch from the full `symbolic-ref` with `refs/heads/` stripped. Observed by AC4.

## 3. Non-goals (OUT)

- A multi-line parser for wrapped calls. The header states the gap.
- Any other kit's comment or variable naming.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-5` — the widened ban and the guard this unit corrects
- **hands-off** `TOOL-dLadderedRemote-7` — the round-3 review's corrections to this unit's ban and runbook text

## 4. Design

The shell-only pass reuses the population with its own include list (`*.sh` and `.githooks/*`) and
appends its hits to the general pass's before the comment filter runs, so both share one filter and
one report.

### Files touched (estimate)

- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `tools/codebase-map/selftest.py`
- `WIRE-INTO-PROJECT.md`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`

## 5. Production-readiness checklist

- security: N/A — a lint and a hook message.
- perf / scale: one more `git grep` over the shell files; milliseconds.
- error / empty / loading states: unchanged.
- observability: the guard stops printing a refusal that changes nothing.
- risks: a widened shape could hit current code; it is run over the real tree before it is wired.
- testing: new RED and GREEN rows; a pre-commit arm for the tag named like the branch.
- migration: none.
- user docs: S3.

## 6. Acceptance criteria

- **AC1** — When the ban's self-test plants `${1:-origin}`, `${x-origin}`, `${x=origin}`,
  `remote.origin.url`, `git pull --ff-only origin`, `git fetch --quiet origin` and
  `["git", "fetch", "origin"]`, `check-remote-literals.sh` names each. Red when: removing the pattern
  for one leaves its line unnamed.
- **AC2** — When it plants `self.origin = origin` in a `.py` file and `const base = origin;` in a
  `.js` file, `check-remote-literals.sh` stays clean, and over the real tree it exits 0. Red when:
  either is named.
- **AC3** — When `WIRE-INTO-PROJECT.md` is read, its ladder bullet names `run-gates`, the codebase-map
  baseline and the playbook render as observed-only, and the branch-guard bullet says `above`.
  Red when: either is missing.
- **AC4** — When a primary tree holds a tag named `main` and commits on `main`,
  `.githooks/pre-commit` allows it; with two remotes and `GOV_DEFAULT_BRANCH` set it prints no
  `GOV_REMOTE` line. Red when: either fails.

## 7. Gates

`remote literals (kit code names no remote)` · `remote literals self-test` · `codebase-map kit selftest` · `push-main self-test` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/check-remote-literals.test.sh · covers AC1 AC2 · one pattern removed at a time · FLOOR_ASSERTIONS
New arm: .githooks/pre-commit.test.sh · covers AC4 · the guard reading `--short HEAD` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft, from the round-2 closing review.
- rev-2 · 2026-10-08 · §3 · the hands-off edge to `TOOL-dLadderedRemote-7`, the round-3 batch unit.

## 10. Reuse audit

Every item amends this build's own ban, guard and docs. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found nothing beyond them.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
