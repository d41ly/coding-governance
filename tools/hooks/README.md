# agent-cap — the fan-out guard, and the grammar it enforces

A `PreToolUse` hook that bounds review fan-out at the tool call, where the rule actually gets broken.
The charter (`§8`) states the two rules; this file states the GRAMMAR the hook recognises, because a
grammar is implementation detail of one hook and does not belong in a ruleset every session reads.

## The two rules

- **At most 5 agents in a verify stage, TOTAL.** Batching grows the batch, never the agent count.
- **At most 5 running at once.** Concurrency is a separate bound from the total; they are two rules.

## Wiring

The matcher is the exact pair `Workflow|Agent`. `Workflow` alone leaves direct spawns unguarded,
which is the configuration this hook was rewritten to stop shipping.

## What the hook DENIES, and how to satisfy it

- A raw `parallel(` / `pipeline(` primitive. Route through a cap-5 helper instead —
  `boundedParallel(thunks, 5)` or `boundedPipeline(items, 5, …)`, inlined, because workflow scripts
  cannot import. The line carries a `gov:bounded-fanout` marker.
- Any `agent(` fanned over a receiver the hook cannot PROVE bounded. The batching assignment carries
  a `gov:fixed-verifiers` marker and must spell `chunk(x, Math.ceil(x.length / K))` or
  `splitInto(x, K)`, with `K` an integer literal ≤5 or an identifier bound to one.
- Any `K` it cannot resolve to an integer ≤5. It RESOLVES a bound wherever it is written — the call
  site, a helper's default parameter, or a `gov:bounded-fanout` slice width — and the burden is on
  the fan-out.

An array LITERAL of ≤5 elements — the finder-lens fan — passes unmarked and needs no helper.

## Direct spawns are COUNTED, not parsed

A direct `Agent` spawn carries no script for the hook to read, so it is counted instead: five per
user prompt, claimed as atomic slots. That count is the only enforcement reaching a fan-out made
outside a workflow script, which is why the matcher must name both tools.

`AGENT_CAP` in the environment is REFUSED, not honoured — the bound is a file constant. A ready-made
harness that satisfies every rule above ships at `tools/workflows/tier2-review.js`.
