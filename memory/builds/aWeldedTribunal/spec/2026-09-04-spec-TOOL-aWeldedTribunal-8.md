# TOOL-aWeldedTribunal-8 — close the four rows whose defect the tree no longer has

**Status:** CLOSED · rev-2 · 2026-09-04 · node a · Tier-1 · base 9b5ae688 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 |

<!-- /gen:spec-records -->

## 1. Goal

Four of the eleven rows the owner named describe a defect that is already fixed. Close them against
the work that fixed them, with the evidence on the row, so the next run does not re-triage them. A
fifth row, reached through one of the seven live ones, closes as a DUPLICATE rather than as a fixed
defect — the difference is stated because the two are not interchangeable and S5 says which.

## 2. Scope (IN)

- **S1** — `TOOL-dScrubbedConduit-2` — already reads `CLOSED`. No edit; recorded here so the owner's
  count of eleven reconciles against a list of ten.
- **S2** — `TOOL-dScaffoldedMirror-22` → `CLOSED`, against `dSealedTally`.
- **S3** — `TOOL-aGroundedOrientation-4` → `CLOSED`, against the same fix. One defect, two rows.
- **S4** — `TOOL-aFlaggedScaffold-4` → `CLOSED`, against `DEPL-dRetiredFork-4`.
- **S5** — `TOOL-aScouredKit-25` → `CLOSED` as a **DUPLICATE of `TOOL-aFlaggedScaffold-3`**, which
  is what its own text instructs and which is NOT the same as closing it against
  `TOOL-aWeldedTribunal-6`. `TOOL-aFlaggedScaffold-3` STAYS OPEN: its claim — `govkit update` cannot
  LAND a source gov ships — survives unit 6 by unit 6's own first non-goal, which reports and does
  not land. The tail says `TOOL-aWeldedTribunal-6` adds the REPORT and that the landing verb is
  still open, so two rows with identical headlines do not end at opposite statuses. This row is a
  DEDUPE, not a fixed defect, and §1 describes it that way.
- **S6** — Each closure names the file, the line and the commit or unit that fixed it. A closure
  citing nothing is a status flip, and a later reader has no way to tell it from a guess.

## 3. Non-goals (OUT)

- **Rebuilding any of them.** There is nothing to change. `--landed` already writes both facts
  together after every check; `git_pathspec` already exists with the exact remedy the row proposed.
- **Auditing the rest of the backlog.** The population is the owner's eleven plus the one row that
  routes through them.
- **Touching `TOOL-dRatifiedSeam-2` or `TOOL-dTieredTribunal-28`.** Both name the same `--landed`
  ordering defect and are therefore also stale, but neither is in the owner's list and closing rows
  nobody asked about widens a records diff past what anyone reviewed. Named here so the next run
  finds them already identified: filed as a backlog note at fold time.

## 4. Design

### The evidence, per row

| Row | Claim | Tree today |
|---|---|---|
| `TOOL-dScrubbedConduit-2` | `check-playbook.sh` exits 1 on the fixture prefix | row already reads `CLOSED` at `memory/backlog/TOOL.md:206` |
| `TOOL-dScaffoldedMirror-22` | `--landed` writes `phase: LANDED` above the check that refuses | `tools/unattended/unattended.sh:2444-2446` writes `landed-anchor` then `phase` immediately before `stage_or_fail`; the reason is at `:2425` |
| `TOOL-aGroundedOrientation-4` | same defect, observed on a second build | same lines |
| `TOOL-aFlaggedScaffold-4` | `govkit apply` blows the 32 KiB argv on renormalize | `git_pathspec` at `tools/govkit/govkit.py:3724` uses `--pathspec-from-file=-` with `--pathspec-file-nul`, plus a subcommand allowlist and an empty-list refusal |
| `TOOL-aScouredKit-25` | `govkit update` cannot land a new source | a DUPLICATE of `TOOL-aFlaggedScaffold-3` (`memory/backlog/TOOL.md:303` says close it against that one). That row STAYS OPEN — its claim survives unit 6, which reports and does not land |

Every row in that table was verified by reading the named file at the named line, not by reading a
commit message.

### Why this is one unit and not five

The act is one edit to one shared mutable record. Splitting it into five would put five passes on
`memory/backlog/TOOL.md`, which M6 clause 3 forbids running together anyway, and would give a
records-only change five review surfaces.

### Files touched (estimate)

- `memory/backlog/TOOL.md` — four status flips and their evidence tails.

## 5. Production-readiness checklist

N/A — Tier-1, records only. The one cross-cutting concern that applies is the merge one: this unit
writes a shared mutable record, so it runs alone and reconciles additively per the charter's §1.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'TOOL-dScaffoldedMirror-22 · OPEN' memory/backlog/TOOL.md` runs, it
  returns zero, and the row reads `CLOSED` with the `tools/unattended/unattended.sh:2444-2446`
  citation in its tail.
- **AC2** — The same for `TOOL-aGroundedOrientation-4`, `TOOL-aFlaggedScaffold-4` and
  `TOOL-aScouredKit-25`.
- **AC3** — When `bash tools/run-gates/run-gates.sh` runs the memory-tree hygiene legs, the row
  grammar and status vocabulary checks stay green over the edited rows.
- **AC4** — When each closure tail in `memory/backlog/TOOL.md` is read, it names a file and a line
  or a unit id. No closure is a bare status flip.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the memory-tree hygiene legs, which own row grammar and the
status vocabulary, named in `tools/gate-legs.json`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Every row in §4's table verified against the file and line it
  names before this spec was written.
- rev-2 · 2026-09-04 · folded spec-audit round 2 (H5). **H5, high:** rev-1 closed
  `TOOL-aScouredKit-25` "against `TOOL-aWeldedTribunal-6`", reversing what that row's own text says.
  `memory/backlog/TOOL.md:303` instructs closing it against `TOOL-aFlaggedScaffold-3`, which is still
  OPEN at `:16` and which NO unit of this build closes — its claim, that `update` cannot LAND a new
  source, survives unit 6 by unit 6's own first non-goal. Rev-1's tail would therefore have named a
  fix that did not happen and left two rows with identical headlines at opposite statuses, which is
  the stale-row harm this unit exists to remove, inverted. S5, §1 and §4's fifth row now describe a
  DEDUPE and say `TOOL-aFlaggedScaffold-3` stays open. Unit 6's §3 had this right and unit 8 quoted
  the same source and reversed it.

## 10. Reuse audit

N/A — Tier-1, and §10 is required of a Tier-2 spec. Recorded anyway because the finding is worth
carrying: the closure evidence came from `python tools/memory-recall/query.py`, whose top hits were
`memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` and that build's acceptance
ledger, which is how the `--landed` fix was located without reading the driver end to end. No seam
is extended by this unit because it writes no code.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
