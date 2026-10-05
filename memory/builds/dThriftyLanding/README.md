---
slug: dThriftyLanding
node: d
opened: 2026-10-05
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-7 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 TOOL-dThriftyLanding-13
---

# dThriftyLanding — a doc-only push runs only the legs that read what it changed

## The problem this build exists to solve

Every push through `tools/push-main.sh` pays the bar the pre-push hook picks, and the owner saw a
one-line doc edit pay the same as a code landing. Measured over this clone's 15 gated pushes: the
scoped bar ran 54 legs to the full bar's 61, because only 7 of the 61 that are not held carry a
guard. One unguarded leg, `unattended kit gate`, takes 222 s alone and sets the wall either way.
Every build landing is a merge, which forces the full bar outright. The prompt is in `prompts/`.

## Expected improvements

- A push whose every changed path is in the declared doc class skips each leg that declares the doc
  paths it reads and reads none of the changed ones. The hook's decision line names that.
- A doc-only build landing is no longer forced to the full bar by its merge commit alone.
- A full green earned in one worktree satisfies the push boundary in the primary tree.
- Adopters receive the mechanism through the shipped hook, the runner and the deployer, opt-in.

## Detriments if this is not built

- A one-line doc push keeps paying 4 to 10 minutes of bar for verdicts it cannot move.
- The scoped bar stays nearly the full bar, so the push boundary's saving is only on paper.

## Build-level rules

- Safe by default: a leg that declares no `doc_reads` runs; an empty doc class is no doc class.
- The doc class is read at R, the remote tip, never from the tree being pushed.
- Every predicate that forces the full bar still forces it, except the merge-parent one on a
  doc-only push; the lag bound of 10 is the owner's and does not move.
- Reuse first: the guard pass, `read_policy_key`, `check_green_record`, the `subject` floor.
- Every new refusal or skip is observed RED on a staged break before it lands.
- No self-test suite runs inside a pass; the flagged bar runs once, at the close.
- Classified at kickoff (M2): all six MISSING; authored and built inline, in order.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dThriftyLanding-1` | 2 | the runner reads a leg's `doc_reads`, and under `GATE_DOCS_BASE` skips a leg none of whose doc paths moved |
| 2 | `TOOL-dThriftyLanding-2` | 2 | the full-green stamp is shared through the common git dir, so any worktree's green serves every push |
| 3 | `TOOL-dThriftyLanding-3` | 2 | the pre-push hook classifies a doc-only push against `GATE_DOC_PATHS` read at R and hands the runner its docs base |
| 4 | `TOOL-dThriftyLanding-4` | 2 | the deployer carries `doc_reads` from a kit descriptor to an adopter's manifest, above the runner floor |
| 5 | `TOOL-dThriftyLanding-5` | 2 | gov declares its doc class and the `doc_reads` of its bar legs, in the manifest and the descriptors |
| 6 | `TOOL-dThriftyLanding-6` | 1 | the run-gates README, the runbook, the charter's merge-bar section and the gate-env notes state the mechanism |
| 8 | `TOOL-dThriftyLanding-8` | 2 | promoted from the closing review's id 1: the runner's docs read walks a merged side branch |
| 9 | `TOOL-dThriftyLanding-9` | 2 | promoted from the closing review's id 22: the hook's doc-only read walks a merged side branch |
| 10 | `TOOL-dThriftyLanding-10` | 2 | promoted from the closing review's id 5: govkit's policy pattern sees a quoted multi-path value |
| 11 | `TOOL-dThriftyLanding-11` | 2 | promoted from the closing review's id 10: the policy selftest grades every spelling of a doc class |
| 12 | `TOOL-dThriftyLanding-12` | 2 | promoted from the closing review: round 1's twelve mediums and six lows, batched |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 11 unit(s) · node d · opened 2026-10-05 · streams tooling
ids TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-7 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12
ids TOOL-dThriftyLanding-13

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dThriftyLanding-1 — the runner skips a leg whose declared doc reads did not move](spec/2026-10-05-spec-TOOL-dThriftyLanding-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-2 — a full green earned in any worktree serves every worktree's push](spec/2026-10-05-spec-TOOL-dThriftyLanding-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-3 — the push boundary recognises a doc-only push and scopes its bar to it](spec/2026-10-05-spec-TOOL-dThriftyLanding-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-dThriftyLanding-4 — the deployer carries a leg's doc reads to an adopter's manifest](spec/2026-10-05-spec-TOOL-dThriftyLanding-4.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-dThriftyLanding-5 — gov declares its doc class and what its bar legs read of it](spec/2026-10-05-spec-TOOL-dThriftyLanding-5.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-6 — the carriers state how a doc-only push is scoped](spec/2026-10-05-spec-TOOL-dThriftyLanding-6.md) | 6 | 1 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-dThriftyLanding-8 — the runner's docs mode sees a doc path touched on a merged side branch](spec/2026-10-05-spec-TOOL-dThriftyLanding-8.md) | 8 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-9 — the hook's doc-only classification sees code touched on a merged side branch](spec/2026-10-05-spec-TOOL-dThriftyLanding-9.md) | 9 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-10 — govkit's policy-key scan sees a quoted multi-path value](spec/2026-10-05-spec-TOOL-dThriftyLanding-10.md) | 10 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-11 — the policy selftest grades every spelling of a doc class](spec/2026-10-05-spec-TOOL-dThriftyLanding-11.md) | 11 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-dThriftyLanding-12 — the closing review's batched minors, round 1](spec/2026-10-05-spec-TOOL-dThriftyLanding-12.md) | 12 | 2 | CLOSED | rev-2 | 2026-10-05 |
<!-- /gen:build-units -->

Records: 24 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dThriftyLanding-1` | no |
| 2 | `TOOL-dThriftyLanding-2` | no |
| 3 | `TOOL-dThriftyLanding-3` | no |
| 4 | `TOOL-dThriftyLanding-4` | no |
| 5 | `TOOL-dThriftyLanding-5` | no |
| 6 | `TOOL-dThriftyLanding-6` | no |
| 8 | `TOOL-dThriftyLanding-8` | no |
| 9 | `TOOL-dThriftyLanding-9` | no |
| 10 | `TOOL-dThriftyLanding-10` | no |
| 11 | `TOOL-dThriftyLanding-11` | no |
| 12 | `TOOL-dThriftyLanding-12` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
