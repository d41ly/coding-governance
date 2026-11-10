---
slug: aGuardedEffort
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
ids: TOOL-aGuardedEffort-1 TOOL-aGuardedEffort-2
---

# aGuardedEffort — the spawn guard refuses a role spawn or a harness call at a level the session model's profile does not give

## The problem this build exists to solve

`aProfiledEffort` gave the effort policy a profile per model, and the dispatch carriers tell a
session to pass its model id to the resolver and the resolved level on every spawn. Nothing checks
that it did. A session that omits the model runs every role at the default tables' level, and only
the `agent` line shows it afterwards. That is ask `TOOL-aProfiledEffort-6`, and this build is its
gate. The owner's words are in `prompts/`.

## Expected improvements

- A direct role spawn at a level its model's profile does not give is refused at the tool call.
- A harness call whose `efforts` differ from the profile's stage levels is refused the same way.
- The refusal names the level expected and the verb that prints it.

## Detriments if this is not built

- A Fable session that forgets the model argument keeps running builders at `high`, silently.
- The profile system stays a convention a session can forget.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: `tools/hooks/agent-cap.js` is a
  shipped kit file and the guard refuses tool calls.
- The session's model is read from the transcript the hook payload names; the payload carries none.
- Where no model can be read the call is admitted with one stderr line (owner, 2026-11-10).
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: the owner declined one, 2026-11-10.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aGuardedEffort-1` | the spawn guard compares an `Agent` call's `effort` and a `Workflow` call's `efforts` with the levels the session model's profile gives, and refuses a difference |
| 2 | `TOOL-aGuardedEffort-2` | promoted from the closing review: round 1's two highs, five mediums and two lows, batched |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aGuardedEffort-1 TOOL-aGuardedEffort-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGuardedEffort-1 — the spawn guard refuses a role spawn or a harness call at a level the model's effort profile does not give](spec/2026-11-10-spec-TOOL-aGuardedEffort-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aGuardedEffort-2 — rule 8 grades an unset stage at the level of the role the call names, and the closing review's arms land](spec/2026-11-10-spec-TOOL-aGuardedEffort-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-11-10 |
<!-- /gen:build-units -->

Records: 10 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aGuardedEffort-1 TOOL-aGuardedEffort-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aGuardedEffort-1` | no |
| 2 | `TOOL-aGuardedEffort-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
