# TOOL-aWeldedTribunal-1 — one loop-header predicate, and it recognises `for await` and `do`-blocks

**Status:** OPEN · rev-1 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` decides whether an `agent()` call sits inside a loop by testing
`/\b(for|while)\s*\(/` against a line. Two ordinary JavaScript loop headers do not match it, and
both were measured at exit 0 carrying an unmarked thunk-array fan past the hook. Replace the five
copies of that regex with one predicate that recognises the shapes the ban was written to deny.

## 2. Scope (IN)

- **S1** — ONE module-level predicate, used at every site that asks "is this line a loop header".
  There are five such sites today and each holds its own copy of the regex, which is the
  `two-answers-to-one-question` class the checklist selects for this file.
- **S2** — The predicate recognises `for await (`. The current regex requires `for` followed by
  optional whitespace and then `(`; `for await (` puts an identifier between them.
- **S3** — The predicate recognises a `do`-block opener, `do {`. A `do { … } while (…)` block's
  opening line carries neither keyword, because its `while` sits after the closing brace.
- **S4** — Arms in `tools/hooks/agent-cap.test.sh` in BOTH directions: the two evasion shapes must
  DENY, and a set of legal scripts that are not loop headers must still ADMIT. A predicate widened
  without a negative arm denies innocent files silently.
- **S5** — The candidate predicate is run over the tracked tree before it is wired, printing hits
  AND near-misses, per the charter's §7 rule. Whatever it turns up is recorded in §9 of this file.

## 3. Non-goals (OUT)

- **Widening the ADMIT side.** `gov:sequential-agents` marks a loop as sanctioned, and the clause
  that admits one requires a strict `for (const x of <bounded identifier>)` header. A `for await`
  or `do`-block header does not match that clause and this unit does not make it match: a marked
  `for await` loop reaches the receiver clause and is DENIED there, which is the correct answer.
  `TOOL-dFoldedVerdict-4` widened the admit side deliberately and separately, and one closing diff
  carrying both widenings is unreviewable.
- **A braceless `do`.** `do out.push(await agent(f)); while (…)` has no brace for the `do {` arm to
  match. Named as a residual in §5 rather than closed here; it is not a spelling anybody writes.
- **Modelling regex literals.** Named in this file already as a standing residual of the lexed view.
- **The empty-literal blessing.** That is `TOOL-aWeldedTribunal-2`, sequenced after this unit.

## 4. Design

### Data model

One module-level constant beside the other scan constants:

```js
// A loop HEADER, in every spelling this file must recognise. `for await (` puts an identifier
// between the keyword and the paren; a `do {` block carries no keyword on its opening line at all,
// because its `while` sits after the closing brace. Both were measured at exit 0 carrying an
// unmarked thunk-array fan (TOOL-dFoldedVerdict-8).
const LOOP_HEADER = /\b(?:for(?:\s+await)?|while)\s*\(|\bdo\s*\{/
```

### Inventory

The five sites, each holding its own copy today, and what each asks:

| Site | Line today | What it asks |
|---|---|---|
| `checkSeqMarker` C5 | 705 | is the marked line a loop header at all |
| `checkSeqMarker` C6 | 710 | does the marked header carry more than one opener |
| `checkSeqMarker` nesting walk | 738 | is the enclosing block a loop |
| call-site braceless arm | 934 | is this `agent()` on a braceless loop header line |
| call-site brace walk | 944 | is the block still open above this line a loop |

Sites 705, 738, 934 and 944 take `LOOP_HEADER` directly. Site 710 counts occurrences and needs the
global flag, so it takes a second constant built from the same source rather than a second literal.

### Why widening the marker path is safe, checked rather than assumed

Sites 705, 710 and 738 sit on the `gov:sequential-agents` ADMIT path, so widening them lets two new
header shapes reach clauses that previously rejected them at the door. Both still end in a denial:

- A marked `do {` header passes C5, counts zero openers at C6, and fails C7's strict for-of match —
  denied, naming the for-of requirement.
- A marked `for await (const f of ALL)` passes C5, counts one opener, and fails the same strict
  match, because that regex requires `for` immediately followed by `(` — denied identically.

So no script that is denied today becomes admitted. The message changes for these two shapes and
nothing else does; S4's negative arms pin that.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — one constant added, five regex literals replaced.
- `tools/hooks/agent-cap.test.sh` — the arms of S4.

### Alternatives rejected

- **Widen each of the five copies in place.** Rejected: it leaves five answers to one question,
  which is the class this file's own checklist selects, and the next shape to be discovered has to
  be applied five times again.
- **Parse the script.** Rejected: this hook is a one-shot stdin CLI with no dependency budget, and
  the file's own history records that every previous attempt at more structure bought a new
  false-positive class.

## 5. Production-readiness checklist

- security — this IS the security surface. The hook is the only mechanical control against an agent
  burst, and the change is strictly in the deny direction.
- perf / scale — one extra alternation in a regex evaluated per line. No measurable cost.
- a11y — N/A — a stdin CLI with no interface.
- i18n — N/A — the surface is JavaScript source, not human language.
- error / empty / loading states — N/A — the hook decides and exits.
- observability — the denial message for the two new shapes is the existing loop-ban text; no new
  message is introduced, so no arm can strand on a message edit.
- risks — the one real risk is a FALSE DENIAL of a legal script. S4's negative arms and S5's whole-
  tree run are what price it. A residual: a braceless `do`, named in §3.
- testing + left-shift gates — S4's arms are the left-shift; the class is already named at
  `memory/gotchas/concurrency-is-not-a-budget.md`.
- migration / rollback — none. The change is one file and reverts cleanly.
- user docs — `tools/hooks/README.md` states the resolvable-bound grammar. The loop-header spelling
  set is not stated there today; if the fold finds that it is, it is updated in the same commit.

## 6. Acceptance criteria

- **AC1** — When a script whose fan is grown inside `for await (const f of allFindings) { th.push(() => agent(f.claim)) }`
  is piped to `node tools/hooks/agent-cap.js`, it exits `2`. It exits `0` today; this was measured
  before the unit was written.
- **AC2** — When the same fan is grown inside `do { th.push(() => agent(…)); i++ } while (i < n)`,
  the hook exits `2`. It exits `0` today, measured the same way.
- **AC3** — When `bash tools/hooks/agent-cap.test.sh` runs, every pre-existing arm still passes, so
  no legal script that was admitted becomes denied.
- **AC4** — When the shipped harness `tools/workflows/tier2-review.js` is piped to the hook, it
  exits `0`. That file is the repo's own review harness and the one this predicate class has
  falsely denied before.
- **AC5** — When `grep -c 'for|while' tools/hooks/agent-cap.js` is run over the loop-header sites,
  the five separate literals are gone and `LOOP_HEADER` is the single source.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — specifically the `agent-cap` self-test leg and the
`agent-cap restatement` leg, whose names are in `tools/gate-legs.json`. Both are read from that
manifest at emission time and not typed here as a list.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Both evasion shapes reproduced at exit 0 against the shipped
  hook before writing; the transcript of that measurement is in the build README's rules slot.

## 10. Reuse audit

The seam is `tools/hooks/agent-cap.js` itself and specifically its five existing loop-header
predicates, found by `python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for
loop shapes and array literals"`, which ranked `capFindings`, `checkLiteralOpen`,
`renderBlankedLiterals` and `resolveLiteralEnd` in that file. No new mechanism is introduced: this
unit consolidates a predicate the file already has five copies of.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
