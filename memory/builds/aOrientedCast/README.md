---
slug: aOrientedCast
node: a
opened: 2026-10-11
streams: tooling+kickoff+playbook
status: INPROGRESS
roster: TOOL+KICK+PLAY
ids: KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8
authorized-by: prompt
---

# aOrientedCast — every agent is handed a rendered role, and the main loop delegates

## The problem this build exists to solve

Attended sessions skip the kit's oriented workflows: specs are written inline from half-settled
orientation, and every agent prompt is freeform, so each handoff restates or forgets the build's
scope. aRoutedQuill makes code wait for a specced unit, but nothing decides who writes the spec, the
code or the review, or what that agent is told. The harnesses' role texts are string literals in
JavaScript the owner cannot adjust. The owner's prose is the mandate, recorded under
[prompts/](prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md).

## Expected improvements

- Every agent prompt is a role block the owner edits plus a task block rendered from the card.
- Spec writing, spec review, building and closing review run only in their role agents.
- An attended code build runs the same harness pipeline an unattended one does.
- Adopters get all of it through a normal `govkit update`.

## Detriments if this is not built

- Attended builds keep writing specs inline from half-oriented sessions.
- Each handoff keeps restating the build in freeform prose, so agents drift off its scope.
- Role text stays buried in harness code that only a build can change.

## Build-level rules

- **Classification (M2)**: eleven units, MISSING at open, one mechanism each.
- Layered on aRoutedQuill's card route, write gate, subagent hand-off and push leg: reused, never
  re-specced. BASE includes its landing.
- aScoutedSeam owns the reuse-scout's content and its kickoff opt-in. This build ships only that
  role's catalogue slot and handoff wiring, and edits no reuse file under `tools/codebase-map/`.
- Owner rulings of 2026-10-11: native agent types, superseding aReplayedCard's ruling of 2026-09-13
  that no agent definition is wired for use; role agents drop the charter where the CLI honours it;
  enforcement from landing with no warn phase; the kit is an adopter default.
- The two enforcement units build last, so no pass of this run meets a gate it has not finished.
- The catalogue does not exist yet, so this run's own spec and build briefs are written by hand.
- One kit-version bump per touched kit, after that kit's last unit.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aOrientedCast-1` | the role catalogue: one agent-definition file per role, with gov's front-matter grammar and its checker |
| 2 | `KICK-aOrientedCast-1` | the card's `## task` gains To-do and Reuse, and `--card --append` refuses an empty task field |
| 3 | `TOOL-aOrientedCast-2` | the handoff renderer: a role's block plus a task block from the card, brief and spec, into a prompt file |
| 4 | `TOOL-aOrientedCast-3` | the catalogue renders `.claude/agents/<name>.md`, trimmed of the charter where the CLI honours it |
| 5 | `TOOL-aOrientedCast-4` | the build harnesses take their role text and agent type from the catalogue |
| 6 | `TOOL-aOrientedCast-5` | the review harness takes its role text and agent type from the catalogue |
| 7 | `KICK-aOrientedCast-2` | the attended router: kickoff's hand-back for a code build drives the harness pipeline |
| 8 | `PLAY-aOrientedCast-1` | the charter: agents are handed rendered roles, and the main loop delegates |
| 9 | `TOOL-aOrientedCast-6` | the write gate admits a spec write only from the spec-writer role, a product write only from the builder |
| 10 | `TOOL-aOrientedCast-7` | the spawn guard refuses an Agent or Workflow call that carries no rendered handoff |
| 11 | `TOOL-aOrientedCast-8` | the kit is an adopter default, wired at install |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 0 unit(s) · node a · opened 2026-10-11 · streams tooling+kickoff+playbook
ids KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
