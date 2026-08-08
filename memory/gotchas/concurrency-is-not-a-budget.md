---
name: concurrency-is-not-a-budget
description: a per-item verify fan-out passes a concurrency cap and still spawns one agent per finding
kind: class
universal: false
---

# Concurrency is not a budget

## Symptom

A multi-agent review is written with a cap-N helper, the cap hook allows it, every fan-out line is
marked, and the run still spawns one agent per finding. `boundedParallel(thunks, 5)` bounds how many
run AT ONCE; N findings still spawn N agents, five at a time. The transcript looks disciplined and
the token bill does not.

The tell is arithmetic, not style: if the agent count is a function of the item count, there is no
budget. `chunk(items, 5)` — five items per group — is the same defect in a helper's clothing: 70
findings buys 14 skeptics.

## Where it bit

Twice in one repository, one session apart.

- Upstream (inCMS), six consecutive reviews of one spec: 79 / 54 / 48 / 37 agents, ~36 M subagent
  tokens. The rule already said CONSOLIDATE; `boundedParallel(…, 5)` was read as the cap.
- Here, 2026-08-09. A bespoke closing-review workflow with a verify stage of
  `all.map((f) => () => agent(...))` — 47 agents and 3.65 M subagent tokens on the wave before it —
  written in a repo that already SHIPPED a batched harness, by a session that had read the protocol
  at kickoff. Re-run batched, the same review cost 9 agents and 0.81 M tokens.

The second one is the interesting one. The rule existed, in prose, in a file the session had read.
Prose lost.

## The fix

Bound the group COUNT, never the group size:

```js
const MAX_VERIFIERS = 5
const batches = chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) // gov:fixed-verifiers
```

Gated by `tools/hooks/agent-cap.js`, which denies an `agent(` reached through an iteration construct whose
receiver it cannot see is bounded — a marked bounded split, or an array literal small enough to count
in the source. `tools/workflows/check-verifier-fanout.sh` applies the same predicate to the committed
harnesses by delegating to that hook.

The enforcement point matters more than the predicate. The offending script was an inline `script`
string on a `Workflow` tool call and was never a file, so a gate over `tools/**/*.js` would have
covered four already-compliant harnesses and zero of the observed failures. Put the check where the
source actually passes through.
