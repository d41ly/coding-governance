# TOOL-aWindowedPass-6 — an amend of a committed pass is refused without a widening the close would not honour

**Status:** OPEN · rev-1 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aWindowedPass-6-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-6-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`--check-commit` reopens a dispatch row whose pass commit is HEAD, so `git commit --amend` on a pass
commit is graded rather than refused as "no open pass". But when that amend stages an undeclared
path, the refusal says the pass "has not committed" and prints a `--dispatch` widening. That widening
anchors at the commit the amend replaces, so check 23 never honours it, and the close still counts the
write. This unit makes the amend refusal say what is true and offer only a repair the close honours.
Promoted from the closing diff review's round 2 (HIGH id 8, with its MEDIUM twin id 4).

## 2. Scope (IN)

- **S1** — For a unit whose matching rows are all reopened rows (its pass commit is HEAD), an undeclared
  staged path is refused with a closed-pass message: an amend cannot widen a committed pass's
  declaration, so unstage the path, or commit it as a new commit after a fresh `--dispatch`. The
  message carries no `--dispatch` command line. Observed by AC1.
- **S2** — An amend that stays inside the declaration is still admitted, and a records commit after a
  pass commit, naming the unit in its subject with no trailer, is still not asked for one. Observed
  by AC2.

## 3. Non-goals (OUT)

- Making check 23 honour a row anchored at an orphaned commit: the anchor is the window's start, and a
  window starting at a commit outside the history is not a window.

### Edges

none

## 4. Design

The open-row set already tags each row `o` (open) or `O` (reopened because its pass commit is HEAD).
The trailer loop keeps that tag when it unions a unit's declarations, and chooses the refusal by it: a
unit with any `o` row keeps the open-pass message and its `--dispatch` repair; a unit whose rows are
all `O` gets the closed-pass message.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Anchoring the widening at HEAD's parent.** `--dispatch` takes its anchor from HEAD by design, and
  a second anchor rule for one verb is two answers to one question.

## 5. Production-readiness checklist

- security — N/A: a commit-time refusal's wording and repair.
- perf / scale — unchanged: the tag rides the row set already computed.
- error / empty / loading states — a unit with no matching row keeps the no-open-pass refusal.
- observability — the closed-pass message names each path and both legal repairs.
- risks — none beyond the amend path.
- testing — arms for a stray-path amend, an in-declaration amend and a records commit after a pass.
- migration — none.
- user docs — the verb carrier's `--check-commit` entry names the amend case.

## 6. Acceptance criteria

- **AC1** — When an amend of a pass commit stages an undeclared path, `--check-commit` exits 1 with
  `cannot widen a committed pass` and its output carries no `--dispatch` command line.
  Red when: the reopened row takes the open-pass message.
- **AC2** — When the amend stays inside the declaration, `--check-commit` exits 0; when a records commit
  after the pass names the unit with no trailer, `--check-commit` exits 0.
  Red when: the reopened row is graded as open for a message with no trailer.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/unattended.test.sh · stray-path amend, in-declaration amend, records commit after a pass · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from closing review round 2 ids 8 and 4.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse amending a committed pass commit that adds an undeclared path"`
ranked unrelated symbol definitions and printed that `.sh` layers have no extractor. Extended by hand:
`verb_check_commit`'s own `o`/`O` row tags and its open-pass refusal, which this unit splits by tag.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
