# TOOL-aDistilledCharter-4 — every live citation of a charter section number is re-pointed

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-1 · base 6473ae38 · streams tooling+kickoff · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

v4.0 has no §1 to §16. Hooks, guides, kit READMEs, skills, code comments and gate messages cite
them, so after PLAY-aDistilledCharter-1 lands each of those names a section that no longer exists.
This unit re-points every live one to the v4.0 handle, the guide that now owns the rule, or the
tool that enforces it.

## 2. Scope (IN)

- **S1** — Every citation the rule map of 2026-10-09 lists under "prose that cites a section
  number", outside frozen records, is rewritten: a practice becomes its handle (`charter [land]`), a
  moved rule its guide, a gated rule its gate. Observed by AC1.
- **S2** — `.claude/rules/product.md` describes the v4.0 template rather than v3.0's single file
  under 48 KiB. Observed by AC1.
- **S3** — A rendered artifact whose template carries a citation is re-rendered from it, never
  hand-edited: `memory/guides/BUILD-METHOD.md` from `tools/memory-tree/BUILD-METHOD.template.md`,
  the lexicon Skill from `.lexicon.conf`. Observed by AC2.

## 3. Non-goals (OUT)

- `memory/DECISIONS.md`, `memory/builds/`, `memory/archive/` and the generated backlog views. They are
  frozen records and cite the charter as it was.
- `WIRE-INTO-PROJECT.md`. DEPL-aDistilledCharter-1 owns it whole.
- The gate that keeps it clean. TOOL-aDistilledCharter-3 adds it after this lands.

## 4. Design

The rule map's list is the starting population; `git grep -nE '§[0-9]+'` over the same surface is
the sweep that catches what the list missed. A bare `§<n>` citing the citing file's own sections is
left alone. Kit versions are not bumped here: every kit this unit touches moves once, after the last
unit of the build.

### Files touched (estimate)

`.githooks/pre-commit` · `.githooks/pre-push` · `README.md` · `.claude/rules/product.md` · `memory/guides/MERGE-BAR.md` · `memory/guides/SESSION-KICKOFF.md` · `memory/guides/BUILD-METHOD.md` · `tools/memory-tree/BUILD-METHOD.template.md` · `tools/memory-tree/README.md` · `tools/codebase-map/README.md` · `tools/gate-lint/README.md` · `tools/drift-audit/README.md` · `tools/hooks/README.md` · `skills/session-kickoff/MANIFEST-TEMPLATE.md` · `skills/session-kickoff/manifest-check.sh` · `tools/hooks/scratch-guard.js` · `tools/run-gates/run-selftests.sh` · `.lexicon.conf` · `.claude/skills/lexicon/SKILL.md`

## 6. Acceptance criteria

- **AC1** — When `git grep -nE '\b(charter|template|playbook|governance)(.s)?.{0,3}§[0-9]|§1 Landing|§16 R1'`
  runs over the population of TOOL-aDistilledCharter-3 §4, it prints nothing.
  Red when: a live citation survives.
- **AC2** — When the memory-tree dogfood render and the lexicon render are re-run, `git diff
  --exit-code memory/guides/BUILD-METHOD.md .claude/skills/lexicon/SKILL.md` exits 0.
  Red when: a rendered file was hand-edited away from its source.

## 7. Gates

`dead-path carriers (deleted files still named)` · `lexicon wiring` · `memory hygiene` · `kickoff-manifest ratchet` · `branch-guard self-test` · `manifest-check self-test` · `shell-hygiene selftest` · `agent-cap self-test` · `scratch-guard self-test` · `kit/dogfood doc parity` · `check-wiring self-test` · `verifier fan-out self-test` · `review-join self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `hook destinations self-test` · `lexicon naming predicates` · `straggler-guard arms` · `govkit acceptance matrix` · `run-selftests self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
