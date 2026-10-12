---
slug: aOrientedCast
node: a
opened: 2026-10-11
streams: tooling+kickoff+playbook
roster: TOOL+KICK+PLAY
ids: KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21
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

- **Classification (M2)**: eleven units MISSING at open, a twelfth added by the M2 cross-read; one
  mechanism each.
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
- Owner rulings of 2026-10-13, the second addendum under `prompts/`: roles cite section 1 rule tags,
  agents carry the rendered Protocols section whole, and an inline stand-in needs a run that cannot
  spawn agents and an owner waiver. Its five units are MISSING at the resume, and their briefs are
  written by hand because the handoff renderer refuses until the first of them lands.
- The owner's third addendum, the same day: every agent a turn dispatches or receives is shown with
  its effort, model, unit, prompt, ids, outcome and authority, kept in a per-build ledger, and
  enforced by extending format-guard. The build reconciles from local main, never waiting on origin.

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
| 12 | `TOOL-aOrientedCast-9` | the unattended Skill and verbs pass the renderer's `roles` to every harness call (M2 cross-read) |
| 13 | `TOOL-aOrientedCast-10` | every role runs at a declared effort level, read from one owner-editable config (owner addendum) |
| 14 | `TOOL-aOrientedCast-11` | a role agent runs no gate or self-test beyond its allowlist, and the hooks enforce it (owner addendum) |
| 15 | `TOOL-aOrientedCast-12` | the roles render selftest budget row carries an empty argv column, and a prose argv is refused (review H1, M1) |
| 16 | `TOOL-aOrientedCast-13` | a gate allowlist may name a leg a target lacks without redding the catalogue (review H2) |
| 17 | `TOOL-aOrientedCast-14` | the hooks scan every launcher option and anchor on the project dir (review M2, M3) |
| 18 | `TOOL-aOrientedCast-15` | the remaining review minors, batched (review M4, M5, L1, L2, L3) |
| 19 | `TOOL-aOrientedCast-16` | a role cites section 1 rule tags, and its agent type carries those rules and the rendered Protocols section (addendum 2) |
| 20 | `TOOL-aOrientedCast-17` | a role declares when it is mandatory and where its output goes, and the kit prints the charter's roster lines (addendum 2) |
| 21 | `TOOL-aOrientedCast-18` | the playbook renders a derived role-roster placeholder from the roles kit's roster (addendum 2) |
| 22 | `PLAY-aOrientedCast-2` | the charter's `[roles]` rule and its generated Agent roles section (addendum 2) |
| 23 | `TOOL-aOrientedCast-19` | an inline stand-in for a role needs a dated owner waiver row (addendum 2) |
| 24 | `TOOL-aOrientedCast-20` | the roles kit derives each agent's dispatch and return lines, and appends them to a generated per-build agent ledger (addendum 3) |
| 25 | `PLAY-aOrientedCast-3` | the charter's `agent` and `returned` micro-formats, mandatory for every agent a turn dispatches or receives (addendum 3) |
| 26 | `TOOL-aOrientedCast-21` | format-guard refuses a final message that omits an agent line for an agent its turn dispatched or received (addendum 3) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 23 unit(s) · node a · opened 2026-10-11 · streams tooling+kickoff+playbook
ids KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9
ids TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [KICK-aOrientedCast-1 — the card's task gains To-do and Reuse, and a READY body lands only with every task field filled](spec/2026-10-11-spec-KICK-aOrientedCast-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aOrientedCast-1 — the role catalogue: one owner-editable agent definition per role, the workflow table, and the checker that keeps them agreeing](spec/2026-10-11-spec-TOOL-aOrientedCast-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-2 — the handoff renderer: a role's constant block and a task block rendered from the card, the brief and the unit, into one prompt file](spec/2026-10-11-spec-TOOL-aOrientedCast-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-3 — the role catalogue renders native agent types, trimmed of the charter](spec/2026-10-11-spec-TOOL-aOrientedCast-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-4 — the build harnesses spawn their stage agents as catalogue roles](spec/2026-10-11-spec-TOOL-aOrientedCast-4.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-5 — the review harness spawns each stage as the role its caller names](spec/2026-10-11-spec-TOOL-aOrientedCast-5.md) | 5 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [KICK-aOrientedCast-2 — the attended router: after kickoff's go, `/build` drives a code build through the harness pipeline](spec/2026-10-11-spec-KICK-aOrientedCast-2.md) | 6 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-9 — the unattended Skill and verbs pass the renderer's `roles` to every harness call](spec/2026-10-11-spec-TOOL-aOrientedCast-9.md) | 6 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-8 — the roles kit is an adopter default: installed, rendered and reported at install and update](spec/2026-10-11-spec-TOOL-aOrientedCast-8.md) | 7 | 2 | CLOSED | rev-4 | 2026-10-11 |
| [PLAY-aOrientedCast-1 — the charter: every agent is handed a rendered role, and the main loop delegates](spec/2026-10-11-spec-PLAY-aOrientedCast-1.md) | 8 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-10 — every role runs at its declared effort, from one owner-editable policy file](spec/2026-10-11-spec-TOOL-aOrientedCast-10.md) | 8 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aOrientedCast-6 — the write gate admits a spec write only from the spec-writer role and a product write only from the builder role](spec/2026-10-11-spec-TOOL-aOrientedCast-6.md) | 9 | 2 | CLOSED | rev-3 | 2026-10-12 |
| [TOOL-aOrientedCast-7 — the spawn guard refuses an Agent or Workflow call that carries no rendered handoff](spec/2026-10-11-spec-TOOL-aOrientedCast-7.md) | 10 | 2 | CLOSED | rev-4 | 2026-10-12 |
| [TOOL-aOrientedCast-11 — a role agent runs no gate, and the write gate's hook refuses one](spec/2026-10-11-spec-TOOL-aOrientedCast-11.md) | 11 | 2 | CLOSED | rev-2 | 2026-10-12 |
| [TOOL-aOrientedCast-12 — a budget row is four fields, and an argv column that reads as prose is refused](spec/2026-10-12-spec-TOOL-aOrientedCast-12.md) | 12 | 1 | CLOSED | rev-3 | 2026-10-12 |
| [TOOL-aOrientedCast-13 — a gate allowlist may name a leg the target lacks, marked optional](spec/2026-10-12-spec-TOOL-aOrientedCast-13.md) | 13 | 2 | CLOSED | rev-2 | 2026-10-12 |
| [TOOL-aOrientedCast-14 — the role gate reads past every launcher option, and both role arms find the session's checkout](spec/2026-10-12-spec-TOOL-aOrientedCast-14.md) | 14 | 2 | CLOSED | rev-4 | 2026-10-12 |
| [TOOL-aOrientedCast-15 — the closing review's minors: oracles that rot, readers that disagree, a verdict over a broken index](spec/2026-10-12-spec-TOOL-aOrientedCast-15.md) | 15 | 2 | CLOSED | rev-4 | 2026-10-12 |
| [TOOL-aOrientedCast-16 — a role cites section 1 rule tags, and its agent carries those rules with the Protocols and Facts sections](spec/2026-10-13-spec-TOOL-aOrientedCast-16.md) | 16 | 2 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-aOrientedCast-17 — a role declares when it is mandatory and where its output goes, and the kit prints the charter's roster lines](spec/2026-10-13-spec-TOOL-aOrientedCast-17.md) | 17 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-aOrientedCast-18 — the role roster, derived into the charter by the roles kit's own verb](spec/2026-10-13-spec-TOOL-aOrientedCast-18.md) | 18 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-aOrientedCast-19 — an inline stand-in for a role declares itself through its handoff, and needs a dated owner waiver row](spec/2026-10-13-spec-TOOL-aOrientedCast-19.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-13 |
| [PLAY-aOrientedCast-2 — the charter's `[roles]` rule and its generated Agent roles section](spec/2026-10-13-spec-PLAY-aOrientedCast-2.md) | 20 | 2 | OPEN | rev-1 | 2026-10-13 |
<!-- /gen:build-units -->

Records: 41 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7
TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 PLAY-aOrientedCast-2 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `KICK-aOrientedCast-1`, `TOOL-aOrientedCast-1` | yes |
| 2 | `TOOL-aOrientedCast-2` | no |
| 3 | `TOOL-aOrientedCast-3` | no |
| 4 | `TOOL-aOrientedCast-4` | no |
| 5 | `TOOL-aOrientedCast-5` | no |
| 6 | `KICK-aOrientedCast-2`, `TOOL-aOrientedCast-9` | yes |
| 7 | `TOOL-aOrientedCast-8` | no |
| 8 | `PLAY-aOrientedCast-1`, `TOOL-aOrientedCast-10` | yes |
| 9 | `TOOL-aOrientedCast-6` | no |
| 10 | `TOOL-aOrientedCast-7` | no |
| 11 | `TOOL-aOrientedCast-11` | no |
| 12 | `TOOL-aOrientedCast-12` | no |
| 13 | `TOOL-aOrientedCast-13` | no |
| 14 | `TOOL-aOrientedCast-14` | no |
| 15 | `TOOL-aOrientedCast-15` | no |
| 16 | `TOOL-aOrientedCast-16` | no |
| 17 | `TOOL-aOrientedCast-17` | no |
| 18 | `TOOL-aOrientedCast-18` | no |
| 19 | `TOOL-aOrientedCast-19` | no |
| 20 | `PLAY-aOrientedCast-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
