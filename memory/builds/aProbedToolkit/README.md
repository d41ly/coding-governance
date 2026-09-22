---
slug: aProbedToolkit
node: a
opened: 2026-09-03
streams: tooling
roster: TOOL
ids: TOOL-aProbedToolkit-1 TOOL-aProbedToolkit-2 TOOL-aProbedToolkit-3 TOOL-aProbedToolkit-4 TOOL-aProbedToolkit-5 TOOL-aProbedToolkit-6 TOOL-aProbedToolkit-7 TOOL-aProbedToolkit-8 TOOL-aProbedToolkit-9 TOOL-aProbedToolkit-10 TOOL-aProbedToolkit-11 TOOL-aProbedToolkit-12 TOOL-aProbedToolkit-13 TOOL-aProbedToolkit-14 TOOL-aProbedToolkit-15 TOOL-aProbedToolkit-16 TOOL-aProbedToolkit-17 TOOL-aProbedToolkit-18
authorized-by: prompt
---

# aProbedToolkit — are the four knowledge kits still earning their keep, measured in four real repos

## The problem this build exists to solve
`memory-tree`, `memory-recall`, `lexicon` and `codebase-map` are graded only where every one of them
is present and configured: this repo. That is the single configuration which cannot exercise the
adopter paths, and `TOOL-dPromptedSeam-1` already recorded the consequence for one kit. Nobody has
run the four against the trees that actually carry them — `incms/main` (6347 files, kits forked under
`scripts/`), `nicocares-package` (1879), `swydee` (133, two kits at the repo root and 53 minor
versions behind) — and compared what they REPORT against what those trees actually hold. A kit that
reports green over a population it cannot see is indistinguishable from one that works, which is this
tree's own `vacuous-selector-empty-population` class applied to the kits that catalogue it.

## Expected improvements
- A per-kit verdict grounded in measurement rather than in the dogfood tree's own green bar.
- The defects that only appear at another install prefix, another corpus size, or no conf at all.
- A ranked recommendation list, so the next kit unit is chosen on evidence instead of on feel.

## Detriments if this is not built
- The kits keep being graded where they cannot fail, and adopters keep receiving green legs that
  grade nothing.
- Fixes an adopter already made stay in that adopter's fork, and gov keeps shipping the defect.
- Retirement candidates keep costing bar seconds and reader attention with no measured return.

## Build-level rules
- **Scratch clones only.** Every run is against a `git clone --local` under `/tmp/kite`. No kit is
  invoked inside `C:/projects/*`, so a kit that writes cannot damage a working tree.
- **Ground truth is derived independently, and BEFORE the kit is asked.** A kit's own count is the
  thing under test; grading it against itself is the assertion-between-two-derived-values class.
- **A green exit is not evidence.** Every green is followed by "over what population?", and a run
  whose population is empty is recorded as a finding, not as a pass.
- **This unit reports; it does not fix.** A cross-kit fix is Tier 2 by the manifest's own tier rule
  and cannot ride an evaluation. Every defect leaves a repro command and a backlog row instead.
- **Adopter forks are read as EVIDENCE, not as drift.** Where incms diverged from a shipped file,
  the first question is what they found that gov has not.

## Parked decisions
None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aProbedToolkit-1` | 1 | run every installed verb of the four kits in four scratch clones, grade the output against independently derived ground truth, and rank the defects and recommendations |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-09-03 · streams tooling
ids TOOL-aProbedToolkit-1 TOOL-aProbedToolkit-2 TOOL-aProbedToolkit-3 TOOL-aProbedToolkit-4 TOOL-aProbedToolkit-5 TOOL-aProbedToolkit-6 TOOL-aProbedToolkit-7 TOOL-aProbedToolkit-8 TOOL-aProbedToolkit-9 TOOL-aProbedToolkit-10 TOOL-aProbedToolkit-11 TOOL-aProbedToolkit-12 TOOL-aProbedToolkit-13
ids TOOL-aProbedToolkit-14 TOOL-aProbedToolkit-15 TOOL-aProbedToolkit-16 TOOL-aProbedToolkit-17 TOOL-aProbedToolkit-18

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aProbedToolkit-1 — grade the four knowledge kits against four real repos](spec/2026-09-03-spec-TOOL-aProbedToolkit-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-03 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aProbedToolkit-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aProbedToolkit-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
