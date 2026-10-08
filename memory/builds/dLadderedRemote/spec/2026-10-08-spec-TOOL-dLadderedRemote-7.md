# TOOL-dLadderedRemote-7 — the round-3 minors: the ban's last false positives, its honest header, and the runbook's full list

**Status:** INPROGRESS · rev-2 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6 TOOL-dLadderedRemote-8 TOOL-dLadderedRemote-9 |
| [2026-10-08-review-TOOL-dLadderedRemote-7-closing-diff-round4.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-7-closing-diff-round4.md) | diff-review | TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-5 |

<!-- /gen:spec-records -->

## 1. Goal

Every item of the round-3 closing review, built as the one batch unit M4 prescribes. The record is
`memory/builds/dLadderedRemote/reviews/2026-10-08-review-TOOL-dLadderedRemote-6-closing-diff-round3.md`.
Its items F1 to F5 are this unit's scope.

## 2. Scope (IN)

- **S1** — F1 and F3, in `tools/check-remote-literals.sh` and its self-test. The `${...}` default
  matches only a parameter-expansion head: a name, a digit or a special parameter, with an optional
  `[...]` subscript, then `:-`, `-`, `:=` or `=`. The last-argument shape closes on `)` only, as it did
  before unit 6; the argv-list shape already owns the list form. GREEN rows plant `let r=origin;` in a
  `.js` file, `x=origin` in a `.py` file, a JS template comparing `===origin` and a Python key list
  ending in the quoted name. Observed by AC1.
- **S2** — F2 and F5, in the same file and `.githooks/pre-commit`. The header names a flag's separate
  value as hiding the name. The merge dedupes on the whole line. The guard's comment says when the
  refusal is announced. Observed by AC2.
- **S3** — F4: `WIRE-INTO-PROJECT.md` names migrate-backlog and the straggler guard as taking the
  observed branch and only cross-checking `GOV_DEFAULT_BRANCH`. Observed by AC3.

## 3. Non-goals (OUT)

- Seeing past a flag's separate value. The header states the gap; a flag-value grammar per git verb
  is out of proportion to a lint.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-6` — the ban, guard and runbook text this unit corrects
- **hands-off** `TOOL-dLadderedRemote-8` — the round-4 review's corrections to this unit's ban and prose

## 4. Design

Each pattern change is run over the real tree before it is wired, and each GREEN row is observed RED
against a mutant that runs the shape it guards over every file.

### Files touched (estimate)

- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `.githooks/pre-commit`
- `WIRE-INTO-PROJECT.md`

## 5. Production-readiness checklist

- security: N/A — a lint, a comment and a runbook sentence.
- perf / scale: unchanged.
- error / empty / loading states: unchanged.
- observability: the ban reports every distinct hit line.
- risks: a narrowed shape could lose a spelling a RED row holds; the RED rows run unchanged.
- testing: four GREEN rows, each red under its mutant.
- migration: none.
- user docs: S3.

## 6. Acceptance criteria

- **AC1** — When the ban's self-test plants `let r=origin;` (.js), `x=origin` (.py), a JS `===origin`
  template and a Python key list, `check-remote-literals.sh` stays clean, while every RED row is still
  named. Red when: a mutant running the shell-only pass over every file names the `.js` row.
- **AC2** — When `check-remote-literals.sh` is read, its header lists a flag's separate value as
  invisible, and its merge dedupes on the whole line with `!seen[$0]++`, not on colon-split keys.
  Red when: either is missing.
  fixture: none on this node — a path holding a colon cannot exist on NTFS, so the collapse itself
  is reproducible only on a POSIX checkout, and this criterion observes the code instead.
- **AC3** — When `WIRE-INTO-PROJECT.md` is read, it names `migrate_backlog` and the straggler guard
  as observed-first readers. Red when: either is missing.

## 7. Gates

`remote literals (kit code names no remote)` · `remote literals self-test` · `push-main self-test`

New arm: tools/check-remote-literals.test.sh · covers AC1 · the shell-only pass run over every file · FLOOR_ASSERTIONS

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft, from the round-3 closing review.
- rev-2 · 2026-10-08 · §3 · the hands-off edge to `TOOL-dLadderedRemote-8`, the round-4 batch unit.

## 10. Reuse audit

Every item amends this build's own ban, guard and runbook text. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found nothing beyond them.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
