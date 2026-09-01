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
- An `agent(` inside a `for (const x of <identifier>)` body. This is the ONE loop shape the hook
  admits, and only under `gov:sequential-agents(<K>)` written as a line comment on the LOOP HEADER.
  It exists because a ratified `parallelism route: none` verdict forbids the bounded PARALLEL fan the
  hook permits, while the hook forbade the strictly sequential dispatch that verdict requires — a
  harness iterating a build's units sat in the gap and could not be written at all.
  EVERY clause below must hold and the refusal names the first that does not. The marker is read
  from the RAW header line, since both code views break their scan on `//`. It carries a bound token,
  and that token resolves through the same `<K>` definition every other consumer uses. The header
  matches a STRICT `for (const|let|var <name> of <identifier>)` in the literal-blanked view — read as
  a whole from the `for (` itself, never as the first `of <name>)` on the line, and a `while` is
  refused outright because it has no iteration source this scan can size. That identifier must
  already be in the hook's proven-bounded set, which is what makes the marker's number real rather
  than asserted. The call is directly preceded by `await`, and no `=>` or `function` sits between the
  header and it, because a deferred call is a thunk array.
  THREE MORE conditions bound the TOTAL rather than the shape, and each of them was a working bypass
  before it existed. A header line carrying more than one loop opener is refused, because this scan
  cannot tell which loop the call belongs to. The marked loop may have NO enclosing loop, marked or
  not — an outer loop multiplies the bound by a count nothing here can size, and it is never
  evaluated on its own because no `agent(` line is attributed to it. And a script may carry only ONE
  marked loop: the sweep bounds a single body and relates no two headers, so two honest markers
  multiplied or summed with every other clause satisfied.
  Finally, exactly ONE awaited call may resolve to any one header, counted per OCCURRENCE and not
  per line — five calls on one line contributed a single entry once, which turned the bound into a
  line count.
- The marked DERIVATION receiver, which is the third form above and was undocumented until now. A
  marked assignment may derive its receiver from something already proven bounded — a `.filter()` or
  a `.slice()`, which cannot grow an array — and the bound is inherited. Mentioning a bounded name is
  not enough: the whole right-hand side is still vetoed if it can grow, and the derivation must be
  ROOTED on the bounded value rather than merely referring to one. Accepted only WITH the marker —
  spelled `gov:fixed-verifiers`, on the assignment line — so it stays a deliberate claim rather than
  something inferred from a name. Every top-level branch of that right-hand side is judged on its own
  text, and the chain after a bounded root must CONSUME to a close: a tail this file cannot delimit
  is refused rather than assumed shrink-only.
- Any `K` it cannot resolve to an integer ≤5. It RESOLVES a bound wherever it is written — the call
  site, a helper's default parameter, or a `gov:bounded-fanout` slice width — and the burden is on
  the fan-out.

- A REF-KEYED VERDICT JOIN. A review harness that joins each finding to its skeptic verdict on a
  `file:line` STRING loses findings to echo drift, and COLLAPSES two findings at one location so both
  inherit whichever verdict landed last. The class has no runtime signal — a mis-keyed harness reports
  a clean bill. Three spellings are refused: an object or Map literal indexed by a `.ref` string,
  `.get`/`.set`/`.has`/`.delete` called on one, and the retired `verdictByRef` identifier in any
  position. Key the join on the integer id the orchestrator assigns before the skeptic sees the
  finding. This rule reads the literal-blanked view, so a mention inside a string is not a hit, and a
  REGEX literal is — which is why a gate holding the ban table excludes itself from its own
  population.

## Running ONE rule

`--only=<rule>` narrows the hook to a single rule, over a closed set whose only member today is
`join`. Anything outside the set is REFUSED with the set named, rather than silently matching
nothing. It exists so a file gate can share this predicate instead of re-implementing it.

**A WIRED command must never carry it.** `--only=join` in `.claude/settings.json` would turn the cap
rules off with no diff and a hook that still looks wired. `tools/check-wiring.sh` asserts its absence.

An array LITERAL of ≤5 elements — the finder-lens fan — passes unmarked and needs no helper.

## Direct spawns are COUNTED, not parsed

A direct `Agent` spawn carries no script for the hook to read, so it is counted instead: five per
user prompt, claimed as atomic slots. That count is the only enforcement reaching a fan-out made
outside a workflow script, which is why the matcher must name both tools.

`AGENT_CAP` in the environment is REFUSED, not honoured — the bound is a file constant. A ready-made
harness that satisfies every rule above ships at `tools/workflows/tier2-review.js`.
