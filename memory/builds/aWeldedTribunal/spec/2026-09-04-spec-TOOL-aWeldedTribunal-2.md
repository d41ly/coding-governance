# TOOL-aWeldedTribunal-2 — a bounded array loses its bound when a later statement grows it

**Status:** CLOSED · rev-3 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` blesses a name bound to an array literal whose element count it can see,
and never looks at that name again. `const batches = []` counts zero elements, is blessed as
bounded, and a later `batches.push(…)` grows it to one entry per finding with the bound still
standing. Take the bound back when a later statement grows the array, the way the file already takes
it back on a bare reassignment.

## 2. Scope (IN)

- **S1** — A sweep over the code view that REMOVES a name from the bounded set when a later
  statement calls a GROWING method on it. The vocabulary is `push`, `unshift`, `splice` — the
  methods that can increase an array's length. `unshift` and `splice` are NEW verbs in this file;
  §4 says why the set is not the existing right-hand-side one.
- **S2** — The sweep runs AFTER both scan passes, beside the existing reassignment sweep, for that
  sweep's stated reason: a name accepted on pass 2 and taken back earlier would fall through to
  whatever pass 1 wrote.
- **S3** — A refusal reason keyed by name, in the shape the file already uses, so the operator is
  told the bound was taken back by a mutation rather than reading the generic fan-out sentence.
  Scoped to a name that HAD a bound, mirroring the reassignment sweep's `hadBound` guard: announcing
  that a bound was withdrawn from a name that never had one is that guard's own recorded defect.
- **S4** — Arms in `tools/hooks/agent-cap.test.sh` in both directions, asserting on the refusal TEXT
  and not only on the exit code. A criterion that checks non-zero alone cannot tell which rule
  fired, which is the defect the spec-audit found in rev-1's AC1.
- **S5** — The candidate predicate is run over the tracked tree before wiring, printing hits and
  near-misses. Done at rev-1 and recorded at
  `memory/builds/aWeldedTribunal/build/2026-09-04-build-TOOL-aWeldedTribunal-2-1-predicate-measurement.md`;
  it is what refuted rev-1's vocabulary.

## 3. Non-goals (OUT)

- **Deciding HOW MUCH a mutation grows an array by.** It cannot be decided from a line, and a
  partial answer is worse than a denial. Any growth call withdraws the bound outright.
- **Mutation through an alias.** `const b = batches; b.push(…)` is not tracked. This file tracks
  names, not values, and following an alias needs a data-flow model it does not have.
- **Index assignment and `length` writes.** `batches[i] = x` past the end, and `batches.length = n`,
  both grow an array and neither is in S1's vocabulary. A regex over `name[<expr>] =` would match
  every ordinary element write in the file, which is the false-denial direction. Named as a residual
  rather than implied away; a spelling that shows up in a real harness is a backlog row.
- **Widening the right-hand-side growth veto.** §4 explains that the two vocabularies answer
  different questions and must NOT share a source. Adding `unshift`/`splice` to the RHS veto is a
  change to a different rule that no criterion here covers.
- **The two loop shapes.** `TOOL-aWeldedTribunal-1` closes those, and this unit is sequenced after
  it for the reason §4 gives.

## 4. Design

### Why this unit is sequenced AFTER unit 1, and why the ordering is load-bearing

The row this unit closes claims the empty-literal blessing is independently exploitable. It is not,
and this was measured rather than argued. Four growth spellings were piped to the shipped hook:

| Shape | Shipped hook |
|---|---|
| `const batches = []` grown in `for (const f of allFindings)` | exit 2 |
| `const batches = []` grown in `allFindings.forEach(…)` | exit 2 |
| `let batches = []` then `batches = allFindings.map(…)` | exit 2 |
| `const th = []` grown in `for await (const f of allFindings)` | exit 0 |

Only the fourth escapes, and it escapes through the loop-walk hole, not through the literal
blessing. So an acceptance arm written against today's tree would go from RED to GREEN for unit 1's
reason and prove nothing about this one — the `staged-break-substitutes-a-synthetic-value` class,
one level up.

### THE TWO GROWTH VOCABULARIES ARE DIFFERENT, and rev-1 was wrong to share them

Rev-1 proposed reusing the file's existing right-hand-side veto,
`/\b(concat|push|flat|flatMap|fill|repeat)\s*\(|\.\.\./` at `agent-cap.js:759`, as the receiver
vocabulary, on the ground that two growth vocabularies in one file is
`two-answers-to-one-question`. The pre-wiring run refutes it:

| Set | Members | Hits over the tracked tree |
|---|---|---|
| the RHS veto applied to a receiver | `concat` `push` `flat` `flatMap` `fill` `repeat` | 44, including `ALL_LENSES.concat` |
| methods that GROW a receiver | `push` `unshift` `splice` | 42, and no lens array |

`concat`, `flat` and `flatMap` are NON-MUTATING: they return a new array and leave the receiver
exactly as long as it was. `fill` and `repeat` change contents or build a string, not a length.
Applying the RHS list to a receiver would take the bound back from `ALL_LENSES` — a shipped lens
array — on the strength of a `.concat` that changes nothing.

**They differ because they answer different questions.** The RHS one asks *can this expression
PRODUCE something bigger*, where `concat` qualifies. The receiver one asks *does this statement GROW
the array named*, where it does not. The two sets overlap on `push` alone. What they share is this
paragraph, not a constant.

### Data model

Beside the existing reassignment sweep:

```js
// A GROWTH CALL takes the bound back, exactly as a reassignment does. `const batches = []` counts
// zero elements and is blessed; a later `batches.push(...)` grows it to one entry per finding with
// the bound still standing (TOOL-aCandidStub-1). NOT the RHS veto's vocabulary: `concat`, `flat`
// and `flatMap` return a NEW array and grow nothing, and using that list here took the bound back
// from `ALL_LENSES` on a measured run over this tree.
const GROWS_RECEIVER = /\b([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g
```

### The one receiver at risk, and why no harness reds

`tools/workflows/drift-audit-code.js:275` binds `const indexed = []` and grows it at `:277`. Under
this sweep `indexed` loses its bound. Nothing fans over `indexed`: the fan at `:341` is over
`batches`, bound at `:338` from `indexed.length ? chunk(indexed, Math.ceil(indexed.length / MAX_VERIFIERS)) : []`,
whose two branches are a bounded split resolved through `boundedK` and an empty literal. Neither
branch depends on `indexed` being in the bounded set.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — one constant, one sweep beside the reassignment sweep.
- `tools/hooks/agent-cap.test.sh` — the arms of S4.

### Alternatives rejected

- **Bless an empty literal only when nothing grows it, decided at bless time.** Rejected: the scan
  is per-line and the growth may be a hundred lines below, so deciding at bless time means a third
  pass. The take-back sweep already exists and already runs after both passes.
- **Refuse an empty literal outright.** Rejected: `const out = []` followed by nothing is legal and
  common, and denying it would red innocent files.
- **Share one constant with the RHS veto.** Rejected on measurement; see above.

## 5. Production-readiness checklist

- security — this is the security surface; the change is strictly in the deny direction.
- perf / scale — one linear sweep over the code view, matching the existing reassignment sweep.
- a11y — N/A — a stdin CLI with no interface.
- i18n — N/A — the surface is JavaScript source.
- error / empty / loading states — N/A — the hook decides and exits.
- observability — S3's reason is a NEW message, so it needs its own arm asserting the text, or an
  edit to it strands the arm silently. That class is
  `memory/gotchas/arm-literal-strands-on-message-edit.md`.
- risks — false denial of a legal script, priced by S5's whole-tree run and AC4's baseline. Two
  residuals are named in §3: alias mutation and index/length writes.
- testing + left-shift gates — S4's arms. One arm per NEW verb, because a verb added to a rule
  without an arm is a rule change nobody voted for. The class is
  `memory/gotchas/concurrency-is-not-a-budget.md`.
- migration / rollback — none; one file, reverts cleanly.
- user docs — `tools/hooks/README.md` if it states the bounded-receiver forms; checked at fold time.

## 6. Acceptance criteria

- **AC1** — When a script binding `const batches = []`, growing it with a PLAIN VALUE at top level
  (`batches.push(f)`), and fanning with
  `await boundedParallel(batches.map((f) => () => agent(f.claim)), 5)` is piped to
  `node tools/hooks/agent-cap.js`, it exits `2` and the refusal names `batches` and the MUTATION.
  Today it exits `0`.
  **THE `agent()` CALL MUST SIT LEXICALLY INSIDE THE MAP RECEIVER'S PARENS.** That adjacency, not
  the presence of `.map` somewhere on the line, is what the opener walk reads: `fanoutFindings`
  judges only lines matching the `agent(` pattern at `agent-cap.js:851`, and `markedWhy` is read at
  exactly one site, `:918`, inside the `hit.kind === 'iter'` arm. A `push(` whose preceding text is
  `batches.push` does not match `ITER_CALL` at `:426`, so a criterion that puts the agent call in
  the push and the `.map` on another line reaches nothing. The fixture's bound must also resolve, or
  it reds under a different rule and hides the one being tested.
- **AC2** — When that same script's `push` is removed so the literal is never grown, the hook exits
  `0`. An empty literal is legal and must stay so.
- **AC2b** — When the growth is a `push` and the `.map` fan is on a SEPARATE line from the
  `agent()` call, the hook exits `0` — that shape is legal and must stay legal. This is the control
  that distinguishes AC1's mechanism from an over-broad predicate, and it is the shape rev-2's AC1
  wrongly asserted would be denied.
- **AC3** — One arm per NEW verb: the AC1 shape spelled with `unshift` and with `splice` each exits
  `2` naming the mutation.
- **AC4** — When each of the five tracked harnesses is piped to the hook, every one exits `0`,
  matching the baseline recorded in
  `memory/builds/aWeldedTribunal/build/2026-09-04-build-TOOL-aWeldedTribunal-2-1-predicate-measurement.md`.
  A predicate that reds the repo's own harnesses is not landable.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, every pre-existing arm still passes.
- **AC6** — When `tools/hooks/agent-cap.js` is read, `GROWS_RECEIVER` and the right-hand-side veto
  are SEPARATE constants and the comment on the first says why. Rev-1 demanded one shared source and
  was refuted by measurement; this criterion pins the corrected requirement rather than leaving the
  reversal implicit.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `agent-cap self-test` and
`agent-cap restatement self-test` legs, which are `subject = kit` in `tools/gate-legs.json` and are
therefore held as `ondemand` by `tools/run-gates/run-gates.sh:947` on the plain bar. `AGENTS.md`
records that no boundary sets `GATE_SELFTESTS` (owner, 2026-08-27) and that a DoD owes the full pair
for KIT work, which this is.


**The FULL PAIR, not half of it.** `AGENTS.md:488` spells the DoD command for KIT work as
`GATE_FULL=1 GATE_SELFTESTS=1`; `GATE_SELFTESTS=1` alone lifts the `ondemand` hold but leaves every
per-leg GUARD in force, so kit legs outside the touched directory stay held with no `skipped` line
saying which. Rev-2 cited the pair and prescribed one half of it.
## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The four-spelling reachability measurement in §4 was run
  against the shipped hook before writing, and is why this unit carries an order after unit 1.
- rev-2 · 2026-09-04 · folded the pre-wiring predicate run and spec-audit round 1 (H2, H7, H8).
  **The predicate run refuted rev-1's vocabulary**: `concat`, `flat` and `flatMap` are non-mutating
  and would have taken the bound back from `ALL_LENSES`. S1 is now `push`/`unshift`/`splice`, §4
  states why the two sets differ, and AC6 pins them as SEPARATE — the reverse of rev-1's AC5.
  **H2, high:** rev-1's AC1 could not reach this unit's mechanism at all. `markedWhy` is read at
  exactly one site, `agent-cap.js:918`, inside the `hit.kind === 'iter'` arm, and `push` is not in
  `ITER_CALL` — so rev-1's `boundedParallel(batches, 5)` line contains no `agent(` and its
  `batches.push` line was attributed to the enclosing loop, producing unit 1's denial. AC1 is
  rewritten onto a `.map` fan that reaches the iter arm. **H8:** rev-1 called its list "the one the
  file already uses"; the existing constant has six verbs and neither `unshift` nor `splice`. S1
  now names them as NEW and AC3 gives each its own arm. **H7:** §7 named the plain bar for
  `subject = kit` legs it holds; corrected to `GATE_SELFTESTS=1`.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (B1, M10). The loop exited NON-CONVERGENT at round
  2 — 17 defects against round 1's 16 — so this is the disposing fold and there is no round 3.
  **B1, blocker, and it is round 1's H2 recurring on the same criterion.** Rev-2's AC1 moved the fan
  to a `.map` but left the `agent()` call inside the `push`, and the reviewer REPRODUCED the
  consequence rather than arguing it: AC1's script exits 0 against the shipped hook AND against a
  copy patched with this unit's own take-back sweep, the sweep firing twice on `batches` and denying
  nothing, while a control with the agent call moved inside the map receiver went 0 to 2 carrying
  this unit's own reason text. A criterion green before and after a faithful build cannot be built
  against. AC1 is respelled onto `batches.push(f)` plus an inline
  `boundedParallel(batches.map((f) => () => agent(f.claim)), 5)`, states the adjacency requirement
  explicitly, and AC2b adds the legal-shape control. **M10:** §7 cited `AGENTS.md`'s full pair and
  prescribed half of it; corrected to `GATE_FULL=1 GATE_SELFTESTS=1`.

## 10. Reuse audit

The seam is the reassignment take-back sweep already in `tools/hooks/agent-cap.js`, which this unit
extends rather than duplicating: it is the file's existing answer to "a name that had a bound can
lose it", including its `hadBound` guard and its `markedWhy` reason map. Located by
`python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for loop shapes and
array literals"`, which ranked `capFindings` and `checkLiteralOpen` in that file. The growth
vocabulary is deliberately NOT shared with the file's existing RHS constant, and §4 records the
measurement that decided it — a reuse that was tried, tested and rejected.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
