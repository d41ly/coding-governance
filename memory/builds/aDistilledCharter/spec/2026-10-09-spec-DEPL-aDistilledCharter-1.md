# DEPL-aDistilledCharter-1 — the runbook adopts v4.0: section 2, the fleet claim and the re-tag step

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-1 · base 6473ae38 · streams deployer · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

`WIRE-INTO-PROJECT.md` tells an agent how to wire gov into a project. At BASE it describes v3.x: the
charter's kit blocks by section number with counts already stale, and a node registry the adopter
fills itself. This unit rewrites those passages for v4.0 and adds the one step an existing adopter
owes to take fleet tags.

## 2. Scope (IN)

- **S1** — Every passage naming a v3.x charter section or kit-block count names the v4.0 section
  instead, with no count. Observed by AC1.
- **S2** — A section-2 passage: the adopter's rules are one line each in `[charter] adopter_rules`,
  and the render refuses a continuation line. Observed by AC2.
- **S3** — A nodes passage: a new node claims its tag once in gov with `--claim-node`; an existing
  adopter re-tags by deleting its wrapper's `## Node registry`, removing `node-table` from
  `drop_blocks`, and re-rendering, after which old slugs stay valid under the collision grep.
  Observed by AC2.

## 3. Non-goals (OUT)

- Running the re-tag in any adopter.
- The runbook's other chapters.

## 4. Design

### Files touched (estimate)

`WIRE-INTO-PROJECT.md`

## 6. Acceptance criteria

- **AC1** — When `grep -nE '§[0-9]+' WIRE-INTO-PROJECT.md` runs, no hit names a charter section;
  hits name the runbook's own sections or a frozen history note. Red when: a charter section is
  cited by number.
- **AC2** — When `grep -n 'adopter_rules\|--claim-node' WIRE-INTO-PROJECT.md` runs, both print.
  Red when: either step is missing.

## 7. Gates

`playbook parity` · `govkit runbook parity` · `dead-path carriers (deleted files still named)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
