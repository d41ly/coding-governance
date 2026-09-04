# TOOL-aWeldedTribunal-2 — a bounded array loses its bound when a later statement grows it

**Status:** OPEN · rev-1 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` blesses a name bound to an array literal whose element count it can see,
and never looks at that name again. `const batches = []` counts zero elements, is blessed as
bounded, and a later `batches.push(…)` grows it to one entry per finding with the bound still
standing. Take the bound back when a later statement mutates the array, the way the file already
takes it back on a bare reassignment.

## 2. Scope (IN)

- **S1** — A sweep over the code view that REMOVES a name from the bounded set when a later
  statement calls a growth method on it. The growth vocabulary is the one the file already uses for
  a right-hand side: `push`, `concat`, `unshift`, `splice`, `fill`, `flat`, `flatMap`.
- **S2** — The sweep runs AFTER both scan passes, beside the existing reassignment sweep, for that
  sweep's stated reason: a name accepted on pass 2 and taken back earlier would fall through to
  whatever pass 1 wrote.
- **S3** — A refusal reason keyed by name, in the shape the file already uses, so the operator is
  told the bound was taken back by a mutation rather than reading the generic fan-out sentence.
  Scoped to a name that HAD a bound, mirroring the reassignment sweep's `hadBound` guard: announcing
  that a bound was withdrawn from a name that never had one is that guard's own recorded defect.
- **S4** — Arms in `tools/hooks/agent-cap.test.sh` in both directions.
- **S5** — The candidate predicate is run over the tracked tree before wiring, printing hits and
  near-misses, and the result is recorded in §9.

## 3. Non-goals (OUT)

- **Deciding HOW MUCH a mutation grows an array by.** It cannot be decided from a line, and a
  partial answer is worse than a denial. Any growth call withdraws the bound outright.
- **Mutation through an alias.** `const b = batches; b.push(…)` is not tracked. This file tracks
  names, not values, and following an alias needs a data-flow model it does not have. Named as a
  residual in §5 rather than implied away.
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
blessing. The first is caught by the loop ban, the second by the iteration-receiver clause, the
third by the reassignment sweep. So an acceptance arm for THIS unit written against today's tree
would go from RED to GREEN for unit 1's reason and prove nothing about this one — the
`staged-break-substitutes-a-synthetic-value` class, one level up. Acceptance here is therefore
measured on a tree where unit 1 has already landed, and AC1 states the shape that isolates it.

### Data model

Beside the existing reassignment sweep:

```js
// A MUTATION takes the bound back, exactly as a reassignment does. `const batches = []` counts
// zero elements and is blessed; a later `batches.push(...)` grows it to one entry per finding
// with the bound still standing (TOOL-aCandidStub-1). The vocabulary is the one the marked-branch
// veto already uses for a right-hand side, so there is one growth answer in this file.
const GROWS_RECEIVER = /\b([A-Za-z_$][\w$]*)\s*\.\s*(?:push|concat|unshift|splice|fill|flat|flatMap)\s*\(/g
```

The sweep walks the code view, and for each match removes the name from `ok` and, when the name had
a bound, records the reason.

### Why the vocabulary is shared and not re-listed

The file already vetoes a marked right-hand side that can grow, with
`/\b(concat|push|flat|flatMap|fill|repeat)\s*\(|\.\.\./`. Two growth vocabularies in one file is
the `two-answers-to-one-question` class. The fold derives both from one source; `repeat` and the
spread are RHS-only forms with no receiver, so the receiver pattern names the subset that has one
and the source records why the two differ rather than leaving a reader to guess.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — one constant, one sweep beside the reassignment sweep.
- `tools/hooks/agent-cap.test.sh` — the arms of S4.

### Alternatives rejected

- **Bless an empty literal only when nothing grows it, decided at bless time.** Rejected: the scan
  is per-line and the growth may be a hundred lines below, so deciding at bless time means a third
  pass. The take-back sweep already exists and already runs after both passes.
- **Refuse an empty literal outright.** Rejected: `const out = []` followed by nothing is legal and
  common, and denying it would red innocent files — the exact failure the charter's
  run-it-over-the-real-tree rule exists to catch.

## 5. Production-readiness checklist

- security — this is the security surface; the change is strictly in the deny direction.
- perf / scale — one linear sweep over the code view, matching the existing reassignment sweep.
- a11y — N/A — a stdin CLI with no interface.
- i18n — N/A — the surface is JavaScript source.
- error / empty / loading states — N/A — the hook decides and exits.
- observability — S3's reason is a NEW message, so it needs its own arm asserting the text, or an
  edit to it strands the arm silently. That class is `memory/gotchas/arm-literal-strands-on-message-edit.md`.
- risks — false denial of a legal script. Residual named in §3: mutation through an alias is not
  tracked.
- testing + left-shift gates — S4's arms; the class is `memory/gotchas/concurrency-is-not-a-budget.md`.
- migration / rollback — none; one file, reverts cleanly.
- user docs — `tools/hooks/README.md` if it states the bounded-receiver forms; checked at fold time.

## 6. Acceptance criteria

- **AC1** — When a script binding `const batches = []`, growing it with `batches.push(() => agent(f))`
  inside a construct unit 1 has already taught the hook to deny, and handing it to
  `boundedParallel(batches, 5)` is piped to `node tools/hooks/agent-cap.js`, the refusal names
  `batches` and the MUTATION, not the loop. That is what distinguishes this unit's mechanism from
  unit 1's, and it is the reason the arm is phrased on the message rather than the exit code.
- **AC2** — When a script binds `const batches = []` and never grows it, `node tools/hooks/agent-cap.js`
  exits `0`. An empty literal is legal and must stay so.
- **AC3** — When `bash tools/hooks/agent-cap.test.sh` runs, every pre-existing arm still passes.
- **AC4** — When `tools/workflows/tier2-review.js` and every other tracked harness is piped to the
  hook, each exits `0`. This is S5's whole-tree run, kept as an acceptance criterion because a
  predicate that reds the repo's own harnesses is not landable.
- **AC5** — When the growth vocabulary in `tools/hooks/agent-cap.js` is read, the receiver form and
  the right-hand-side form derive from one source rather than two literals.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `agent-cap` self-test and restatement legs, named in
`tools/gate-legs.json` and read from there.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The four-spelling reachability measurement in §4 was run
  against the shipped hook before writing, and is why this unit carries an order after unit 1.

## 10. Reuse audit

The seam is the reassignment take-back sweep already in `tools/hooks/agent-cap.js`, which this unit
extends rather than duplicating: it is the file's existing answer to "a name that had a bound can
lose it". Located by `python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for
loop shapes and array literals"`. The growth vocabulary is likewise an existing constant in the same
file and is shared rather than re-listed.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
