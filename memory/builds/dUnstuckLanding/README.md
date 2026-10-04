---
slug: dUnstuckLanding
node: d
opened: 2026-10-04
streams: tooling
roster: TOOL
ids: TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2 TOOL-dUnstuckLanding-3 TOOL-dUnstuckLanding-4 TOOL-dUnstuckLanding-5 TOOL-dUnstuckLanding-6 TOOL-dUnstuckLanding-7 TOOL-dUnstuckLanding-8 TOOL-dUnstuckLanding-9 TOOL-dUnstuckLanding-10 TOOL-dUnstuckLanding-11
authorized-by: prompt
---

# dUnstuckLanding — unattended runs that close themselves, and a verb for the ones that do not

## The problem this build exists to solve

Unattended runs reach their close and stop there. The two causes the owner names are a red bar the
run did not cause, inherited from the default branch or from another build, which the run does not
resolve itself, and a closing decision the run hands back to an owner who is not there. The run then
writes `ABORTED`, the work lands later with the owner present, and the record says `ABORTED`
forever. A terminal that is false about what happened makes every later reader wrong. The owner's
prompt is recorded verbatim under `prompts/`.

## Expected improvements

- A census of closing-time failures across this repo, inCMS and NicoCares, each one cited.
- A design that lets a run close unattended through an inherited red and a closing decision.
- A separate, truthful record shape for a run that was interrupted and then landed attended.
- Implementation asks a later run can take, each with a `seen` locator and an `accept` clause.

## Detriments if this is not built

- Runs keep ending `ABORTED` over work that landed, so the record contradicts git.
- Each inherited red keeps costing an owner turn the mandate was meant to remove.
- Deferred closing decisions keep leaving builds with no status anyone can act on.

## Build-level rules

- **Research and design only.** The prompt asks to "research and design"; no kit file changes in
  this build. Each mechanism the design chooses is filed as an ask in this build's `BACKLOG.md`
  with its `SEV` and `KEEP` rows, so that a later run can take it.
- Classified at kickoff (M2): both units MISSING. Unit 1 is the census and unit 2 the design,
  sequenced 1 then 2, because the design is only as good as the evidence under it.
- The census reads the other two repositories and never writes to them.
- `Tier-1` per unit, because both units write only memory-tree records. The closing diff review is
  still owed, under the `diff-reviewed` directive.

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dUnstuckLanding-1` | 1 | the closing-time failure census across gov, inCMS and NicoCares |
| 2 | `TOOL-dUnstuckLanding-2` | 1 | the design: unattended closes through inherited reds and closing decisions, plus attended-landing verbs |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node d · opened 2026-10-04 · streams tooling
ids TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2 TOOL-dUnstuckLanding-3 TOOL-dUnstuckLanding-4 TOOL-dUnstuckLanding-5 TOOL-dUnstuckLanding-6 TOOL-dUnstuckLanding-7 TOOL-dUnstuckLanding-8 TOOL-dUnstuckLanding-9 TOOL-dUnstuckLanding-10 TOOL-dUnstuckLanding-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dUnstuckLanding-1 — the closing-time failure census across gov, inCMS and NicoCares](spec/2026-10-04-spec-TOOL-dUnstuckLanding-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-2 — the design: unattended closes through inherited reds and closing decisions, plus attended-landing verbs](spec/2026-10-04-spec-TOOL-dUnstuckLanding-2.md) | 2 | 1 | CLOSED | rev-1 | 2026-10-04 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dUnstuckLanding-1` | no |
| 2 | `TOOL-dUnstuckLanding-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
