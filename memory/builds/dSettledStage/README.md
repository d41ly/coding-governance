---
slug: dSettledStage
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
ids: TOOL-dSettledStage-1 TOOL-dSettledStage-2 TOOL-dSettledStage-3 TOOL-dSettledStage-4
---

# dSettledStage — the lander commits only what staging actually changed

## The problem this build exists to solve

Landing 12764ec21 aborted before its bar. `run_regen` left `.governance/instructions.lock` dirty by
line endings only, `git add -A` normalised it back to the committed bytes, and the regen
`git commit` found nothing to commit and failed. Four sites in `tools/push-main.sh` share the shape:
a dirty `git status --porcelain` gates a `git add -A` and a commit, with nothing checking that the
staging left a diff. The owner's prompt is recorded verbatim under `prompts/`.

## Expected improvements

- A landing whose regenerated outputs differ from the index only in line endings reaches the bar.
- The mint, gov-first and merge-fold sites take the same check, so none of them aborts or rewrites
  HEAD on an empty stage.
- The class is gated, so a new dirty-then-stage commit site cannot land unseen.

## Detriments if this is not built

- Every Windows landing that regenerates an unpinned path can abort, at the cost of a re-run.
- The next dirty-then-stage site is written the same way, because nothing names the class.

## Build-level rules

- Classified at kickoff (M2): both units MISSING. Tier-2, a shipped-kit edit. Unit 1 precedes unit 2,
  because unit 2's gate is green only on the tree unit 1 fixes.
- No spec audit: the owner answered "go, no audit" (2026-11-19).
- Units run no gates. The RED-first observation of each new arm is the main loop's, at the close.

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSettledStage-1` | 2 | the lander commits a dirty-then-staged change only when the staged diff is non-empty, at all four sites, with an EOL-only arm |
| 2 | `TOOL-dSettledStage-2` | 2 | the dirty-then-stage commit class gated: a gate-lint scan, else a gotcha class claimed in a dossier |
| 3 | `TOOL-dSettledStage-3` | 2 | a failed stage refuses: `write_staged_change` answers 2 and every caller aborts on it (closing review item 1, promoted) |
| 4 | `TOOL-dSettledStage-4` | 2 | the stage scan's gaps closed and arm 43's liveness (closing review items 2 to 6, promoted) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dSettledStage-1 TOOL-dSettledStage-2 TOOL-dSettledStage-3 TOOL-dSettledStage-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSettledStage-1 — the lander commits a dirty-then-staged change only when the stage holds a diff](spec/2026-11-19-spec-TOOL-dSettledStage-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dSettledStage-2 — a commit after a stage nothing tested is gated: a fifth shell-hygiene mode](spec/2026-11-19-spec-TOOL-dSettledStage-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dSettledStage-3 — a failed stage refuses: the lander's stage helper answers 2 and every caller aborts on it](spec/2026-11-19-spec-TOOL-dSettledStage-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dSettledStage-4 — the stage scan reads past a quoted substitution, every git global option and a stager's wrappers, and arm 43 proves its shape](spec/2026-11-19-spec-TOOL-dSettledStage-4.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 14 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSettledStage-1 TOOL-dSettledStage-2 TOOL-dSettledStage-3 TOOL-dSettledStage-4.

Ids whose spec moved past its audited revision: none — 0 of 4 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSettledStage-1` | no |
| 2 | `TOOL-dSettledStage-2` | no |
| 3 | `TOOL-dSettledStage-3` | no |
| 4 | `TOOL-dSettledStage-4` | no |

A step's `Parallel` yes means its units share an order; BUILD-METHOD M6 still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md`, `2026-11-19-prompt-TOOL-dSettledStage-2-pass-legs-fix.md` and 4 more under prompts/ |
| reviews | `2026-11-19-review-TOOL-dSettledStage-1-2-closing-diff-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-19-build-TOOL-dSettledStage-3-red-fix-2.md`, `2026-11-19-build-TOOL-dSettledStage-2-red-fix-1.md` |
| logs | `2026-11-19-build-TOOL-dSettledStage-4-1-acceptance-ledger.md`, `2026-11-19-build-TOOL-dSettledStage-3-1-acceptance-ledger.md` and 3 more under build/ |
| card ref | `refs/gov/builds/dSettledStage/card` |
<!-- /gen:build-routes -->
