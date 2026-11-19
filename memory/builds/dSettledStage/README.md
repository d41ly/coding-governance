---
slug: dSettledStage
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
ids: TOOL-dSettledStage-1 TOOL-dSettledStage-2
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 2 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dSettledStage-1 TOOL-dSettledStage-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSettledStage-1 — the lander commits a dirty-then-staged change only when the stage holds a diff](spec/2026-11-19-spec-TOOL-dSettledStage-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dSettledStage-2 — a commit after a stage nothing tested is gated: a fifth shell-hygiene mode](spec/2026-11-19-spec-TOOL-dSettledStage-2.md) | 2 | 2 | SPECCED | rev-2 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSettledStage-1 TOOL-dSettledStage-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSettledStage-1` | no |
| 2 | `TOOL-dSettledStage-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
