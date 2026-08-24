# TOOL-dUnstalledConvoy-27 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-27

Five arms in `.githooks/pre-push.test.sh`, cases 19 to 23. The red-first run applied the ARMS ALONE
and left the hook untouched, so the hook under test was the one committed at `835e1c7e` — a boundary
that parses three fields from the stamp and has no eighth predicate.

## The arms, and the break each one was observed against

| case | red-first verdict |
|---|---|
| 19 a switch-OFF record offered for a switch-ON push → FULL | RED — `scoped gate on main push … full green be18d7d9 is 1 commit(s) back, within 10` |
| 20 the forcing reason names the switch | RED — same line; there was no forcing reason to name |
| 21 a record with NO switch key reads as OFF | RED — the absent key was read as covering everything |
| 22 a switch-ON record satisfies a switch-OFF push | **passes without the mechanism** |
| 23 CONTROL — a switch-ON record satisfies a switch-ON push | **passes without the mechanism** |

## The two that pass either way, and why they are still here

Both assert that the boundary chooses SCOPED, and before this unit the boundary chose SCOPED for
every one of these cases — so neither can red on the pre-fix hook. They are not evidence the
predicate works; they are evidence it does not fire where it must not.

That direction is the expensive one. The tempting predicate here is EQUALITY — record and run
agree — and it looks identical to coverage on arms 19 through 21. It differs exactly on 22 and 23,
where a record that covered MORE is offered for a push that needs less, which is every adopter's
ordinary push. An equality implementation would force a full run there and delete the whole saving
`TOOL-dUnstalledConvoy-26` was built to give, at the one boundary it was measured for.

## What predicate 8 does NOT do

It never makes a run smaller. Every predicate in that block forces and none scopes, which is the
asymmetry the block's own header states: it can be wrong in one direction only. Predicate 8 keeps
that property — the switch-ON push with a switch-OFF record is the only pair it fires on.

It also does not decide where this repository SETS the switch. That is
`TOOL-dUnstalledConvoy-28`, and until it lands the hook reads whatever the environment carries.
