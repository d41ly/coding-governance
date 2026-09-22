---
slug: dPinnedHandoff
node: d
opened: 2026-09-22
streams: tooling
roster: TOOL
ids: TOOL-dPinnedHandoff-1 TOOL-dPinnedHandoff-2 TOOL-dPinnedHandoff-3
---

# dPinnedHandoff — three habits of the NicoCares handoff briefs, as spec shapes a machine reads

## The problem this build exists to solve

Three briefs from the NicoCares backend team were built from with no blockers. They sit in `d41ly/nc`
under `backend/`. Three of their habits have no gradeable home in this repo's spec format. The first
states what the builder does when a precondition turns out false. The second lists nearby, correct
files the builder must leave alone. The third writes acceptance as a grep a machine can run. Here
each one is prose or absent. Of 68 `consumes-from external` edges, 7 say what breaks without the
precondition and none is asked what the builder does. And 23 of 191 unit briefs carry a "do not
touch" line that no gate reads.

## Expected improvements

- A builder who finds an external precondition false has a declared disposition, not an improvised
  workaround.
- A commit that edits a path its unit froze reds on the next bar.
- An acceptance grep that already holds at the spec's base reds before any code is written.

## Detriments if this is not built

- The workaround class stays a reviewer's catch; the brief named it and our specs cannot.
- "Do not touch" stays unchecked prose inside pass briefs.
- The class `TOOL-aHonedRuleset-12` records, a criterion that cannot fail, stays open with no
  criterion shape a checker can run.

## Build-level rules

Dry run before wiring, the precedent `dGatedProse` set. Each unit runs its predicate over the whole
spec corpus and prints hits and near-misses before the arm gates anything. A predicate whose hits are
mostly innocent comes back to the owner, not into a gate.

Every arm this build adds grades SHAPE or a JOIN over git, and its own header says what it cannot see.

Order is sequential, 1 then 2 then 3. The units are separate mechanisms, but all three edit
`tools/memory-tree/SPEC-TEMPLATE.template.md`, so their write sets are not disjoint (M6). The
memory-tree kit's one version move for the build rides unit 3, the last unit to edit a kit file.

Items the source comparison ranked lower are not units here. That covers a sink table for secrets,
before/after contract tables, decision tables and the outbound handoff brief. Each is named as a
follow-up in the spec that meets it.

## Parked decisions

Sequencing against `dDerivedDocket`. That build's unmerged branch, HELD at the owner's instruction,
edits all five files this build touches, `tools/check-spec-tokens.py` and
`tools/memory-tree/check-memory-hygiene.sh` among them. Measured at `9b7e2de6`, it does not touch
check 12's edge arm, and its spec-tokens change adds a `hands-off` arm beside the joins these units
add. The overlap is adjacent insertions, not shared lines. Options: (a) build now and let whichever
lands second reconcile additively and re-ground per M7; (b) wait for `dDerivedDocket` to land.
Recommendation: (a). Waiting holds three small units behind a build with no release date, and the
second lander's reconcile is the same work either way. Owner's call.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dPinnedHandoff-1` | SPECCED | hygiene check 12: a `consumes-from external` edge carries an `If false:` clause |
| 2 | `TOOL-dPinnedHandoff-2` | SPECCED | a seventh spec-tokens join: a commit naming the unit touches no path its spec froze |
| 3 | `TOOL-dPinnedHandoff-3` | SPECCED | an eighth spec-tokens join: an `Invariant:` line runs, and cannot already hold at base |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node d · opened 2026-09-22 · streams tooling
ids TOOL-dPinnedHandoff-1 TOOL-dPinnedHandoff-2 TOOL-dPinnedHandoff-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dPinnedHandoff-1 — an external precondition says what the builder does when it is false](spec/2026-09-22-spec-TOOL-dPinnedHandoff-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-22 |
| [TOOL-dPinnedHandoff-2 — a commit naming a unit touches no path its spec froze](spec/2026-09-22-spec-TOOL-dPinnedHandoff-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-22 |
| [TOOL-dPinnedHandoff-3 — an acceptance grep runs, and cannot already hold at the spec's base](spec/2026-09-22-spec-TOOL-dPinnedHandoff-3.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-22 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-dPinnedHandoff-1 TOOL-dPinnedHandoff-2 TOOL-dPinnedHandoff-3.

Ids no `spec-audit` record has ever named: TOOL-dPinnedHandoff-1 TOOL-dPinnedHandoff-2 TOOL-dPinnedHandoff-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dPinnedHandoff-1` | no |
| 2 | `TOOL-dPinnedHandoff-2` | no |
| 3 | `TOOL-dPinnedHandoff-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
