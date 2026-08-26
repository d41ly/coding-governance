# agent-cap — the fan-out guard, and the grammar it enforces

A `PreToolUse` hook that bounds review fan-out at the tool call, where the rule actually gets broken.
The charter (`§8`) states the two rules; this file states the GRAMMAR the hook recognises, because a
grammar is implementation detail of one hook and does not belong in a ruleset every session reads.

## The two rules

- **The verify-stage TOTAL is whatever `agent-cap.js` resolves.** Batching grows the batch, never
  the agent count.
- **Concurrency is a SECOND bound, its own constant in the same file.** How many run at once is not
  how many exist; they are two rules.

## Wiring

The matcher is the exact pair `Workflow|Agent`. `Workflow` alone leaves direct spawns unguarded,
which is the configuration this hook was rewritten to stop shipping.

## What the hook DENIES, and how to satisfy it

- A raw `parallel(` / `pipeline(` primitive. Route through a bounded helper instead —
  `boundedParallel(thunks, 5)` or `boundedPipeline(items, 5, …)`, inlined, because workflow scripts
  cannot import. The line carries a `gov:bounded-fanout` marker.
- Any `agent(` fanned over a receiver the hook cannot PROVE bounded. The batching assignment carries
  a `gov:fixed-verifiers` marker, and EVERY top-level value branch of that assignment must qualify on
  its own — a marked line is admitted only when all of its branches do, never when the first one that
  matches does. A branch qualifies in one of three ways and no fourth: a bounded split, spelling
  `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)` with a `K` the hook can resolve; an array
  LITERAL whose element count it can count here; or an identifier it has already proven bounded,
  alone or followed by operations that cannot grow it. A branch it cannot delimit never qualifies, so
  an expression the hook cannot read lands on the deny side rather than being waved through.
- The marked DERIVATION receiver, which is the third form above and was undocumented until now. A
  marked assignment may derive its receiver from something already proven bounded — a `.filter()` or
  a `.slice()`, which cannot grow an array — and the bound is inherited. Mentioning a bounded name is
  not enough: the whole right-hand side is still vetoed if it can grow, and the derivation must be
  ROOTED on the bounded value rather than merely referring to one. Accepted only WITH the marker, so
  it stays a deliberate claim rather than something inferred from a name.
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
