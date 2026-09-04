# Build brief — TOOL-dRatifiedSeam-1

**Serves:** journal TOOL-dRatifiedSeam-1

Tier-2 · node d · 2026-09-03 · order 2 · streams tooling

## The defect, read from the code rather than from the ruling

`tools/workflows/unattended-build.js` stage 2 spawns a sidechain agent whose prompt says: *"Run the
shipped harness as a Workflow — not as direct Agent spawns — with `scriptPath:
tools/workflows/tier2-review.js`"*. A sidechain agent holds neither `Workflow` nor `Agent`; the
capability is ABSENT, not policed. So the instruction is unfollowable, the stage never completes,
and BUILD is unreachable through the harness.

The stage agent that met this searched the deferred registry three times, refused to fabricate a
verdict, wrote nothing, and returned the impossible CONVERGING-with-0-blockers pairing. It was
right on every count, and its refusal is the reason this unit exists rather than a mystery to
diagnose.

## F1 is resolved by the runtime, not by preference

The spec asked whether the AUDIT stage belongs in the harness at all, and recommended keeping it
with the caller supplying the result. Reading the code makes a better answer available: **the
harness IS a workflow script**, and the script runtime provides `workflow({scriptPath}, args)` for
running another workflow inline as a sub-step. The spawn does not need to leave the harness — it
needs to stop being delegated to an agent that cannot perform it. The script itself sits in the
context where the tool exists.

Nesting is one level only, and this harness is invoked at the top by the main loop, so the one
level is available and is spent here.

**No harness in this repo calls `workflow()` today** — `grep` over `tools/workflows/*.js` returns
nothing. This is the first, which is a reason to observe it end to end rather than to assume it.

## What that costs, and it is not nothing

`AUDIT_SCHEMA` currently binds the AGENT's return. With no agent in that position there is no
schema to enforce, so S2's requirement — an absent verdict must never read as a pass — moves from
a schema to an explicit check on what `workflow()` returns. That is arguably stronger: a schema on
an agent is a retry prompt, and an explicit check is a refusal. It is also a change the spec did
not anticipate, so it is recorded here rather than smuggled in.

## The trap to avoid

S2's inverse. A stage that cannot complete is at least LOUD. A stage that completes with a
fabricated verdict is silent, and silent is worse. Whatever replaces the agent must keep the
property that an absent or non-integer blocker count REFUSES rather than defaulting to zero —
`unattended.sh` emits CONVERGED only on a count of 0, so a null read as 0 would make every
degraded audit look clean.
