---
slug: aBlindedTrial
node: a
opened: 2026-09-20
streams: tooling+playbook
roster: TOOL
ids: TOOL-aBlindedTrial-1
authorized-by: prompt
---

# aBlindedTrial — does speccing and auditing before code buy code quality, measured on a blinded trial

## The problem this build exists to solve
Every Tier-2 unit in this repo pays for a spec, an adversarial spec audit and a fold before its
first line of code, and adopters inherit the same rule through the template's §1. Nobody has
measured what that ceremony buys. The owner's standing impression is that sessions often spec after
building, that specs are abstract, and that nothing checks whether code follows them. Two of those
three are answerable from the tree; the third needs a controlled comparison, which has never been
run.

## Expected improvements
- A measured answer to "spec-first or build-first", per token spent, on tasks shaped like this
  repo's own work.
- The retrospective figures — how often the order is honoured, how often the audit precedes code,
  how concrete a spec is — derived by command, not recalled.
- Evidence on which to keep, narrow or drop the §1 design-pass rule in the template.

## Detriments if this is not built
- The most expensive step of every Tier-2 unit keeps running on faith.
- If it buys nothing, adopters keep paying for it; if it buys a lot, the sessions that skip it keep
  shipping worse code and nobody can say so with a number.

## Build-level rules
- **This unit reports; it does not fix.** A template or method change is a follow-up unit with its
  own spec, never a rider on an evaluation.
- **Every arm works in a scratch cell under the sanctioned temp root, never in this tree.** A cell is
  its own git repository holding the brief and the fixtures; an arm may read nothing outside its
  cell.
- **The acceptance suite is hidden, written from the brief alone, and FROZEN by hash before any arm
  runs.** Its author never sees an implementation; its verifier re-tags any test that asserts more
  than the brief pins.
- **Judges are blind.** Reviewers see a script under a code name and the brief, never the cell, the
  spec or the plan.
- **Every number in the record names the command or file that derives it.** A figure with no
  derivation is not written.
- **Concurrency stays inside the review protocol's bound.** One task's arms run at a time, spec-first
  replicates sequentially, and the audit is the shipped `tier2-review.js` harness.

## Parked decisions
None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBlindedTrial-1` | 1 | a retrospective over every spec in the tree (order, audit-before-code, concreteness, adherence) plus a prospective blinded trial: three tasks × three arms × three replicates, graded by a frozen hidden suite, blind adversarial review, adherence judges and per-arm token cost |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-09-20 · streams tooling+playbook
ids TOOL-aBlindedTrial-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBlindedTrial-1 — spec-first versus build-first, measured on a blinded trial](spec/2026-09-20-spec-TOOL-aBlindedTrial-1.md) | 1 | 1 | INPROGRESS | rev-2 | 2026-09-20 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aBlindedTrial-1.

Ids no `spec-audit` record has ever named: TOOL-aBlindedTrial-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBlindedTrial-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
