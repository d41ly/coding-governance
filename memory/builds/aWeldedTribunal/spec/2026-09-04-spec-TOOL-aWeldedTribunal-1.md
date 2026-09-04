# TOOL-aWeldedTribunal-1 — one loop-header predicate, and it recognises `for await` and `do`-blocks

**Status:** OPEN · rev-2 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` decides whether an `agent()` call sits inside a loop by testing
`/\b(for|while)\s*\(/` against a line. Two ordinary JavaScript loop headers do not match it, and
both were measured at exit 0 carrying an unmarked thunk-array fan past the hook. Replace the five
copies of that regex with one predicate that recognises the shapes the ban was written to deny.

## 2. Scope (IN)

- **S1** — ONE module-level SOURCE for the loop-keyword set, used at every site that asks "is this a
  loop opener". There are SIX such sites today and each holds its own copy of the regex, which is the
  `two-answers-to-one-question` class the checklist selects for this file. Five take the predicate
  directly; `:710` and `:910` take siblings DERIVED from the same source, because one counts
  occurrences and the other matches a keyword TAIL rather than a header.
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

SIX sites, each holding its own copy today, and what each asks:

| Site | Line today | What it asks | Takes |
|---|---|---|---|
| `checkSeqMarker` C5 | 705 | is the marked line a loop header at all | `LOOP_HEADER` |
| `checkSeqMarker` C6 | 710 | does the marked header carry more than one opener | a global-flag sibling |
| `checkSeqMarker` nesting walk | 738 | is the enclosing block a loop | `LOOP_HEADER` |
| **opener walk** | **910** | **is this open paren a loop opener** | **a keyword-TAIL sibling** |
| call-site braceless arm | 934 | is this `agent()` on a braceless loop header line | `LOOP_HEADER` |
| call-site brace walk | 944 | is the block still open above this line a loop | `LOOP_HEADER` |

Site 710 counts occurrences and needs the global flag. **Site 910 was omitted from rev-1's inventory
and it is the one that cannot take `LOOP_HEADER` at all**: it is `/\b(for|while)\s*$/` tested against
the text BEFORE an opener position, so a pattern ending in `\(` or `do\s*\{` never matches there. It
needs a sibling anchored at end-of-text, `/\b(?:for(?:\s+await)?|while)\s*$/`, derived from the same
keyword source exactly as site 710's is.

### Why :910 is not cosmetic — a fail-open the header widening alone leaves open

`openersOf()` walks right-to-left. When `before` ends in `for await`, the `:910` predicate misses,
`hit` stays null, and the walk continues OUTWARD. If the next enclosing opener is a bounded
`.map(` / `.forEach(` receiver already in `ok`, the call-site arm returns at `:912-919` with no
finding and the loop arms at `:934` and `:944` are never reached. So widening only the header sites
leaves a second `for await` path admitted, and S1's "one source at every site" and AC5's single-
source claim would both be false after the change. The `do`-block spelling does not reach this site
— a `do {` opener is a brace, not a paren — so only the `for await` half is added here.

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
- **AC5** — When the same `for await` fan is reached through the OPENER walk rather than the brace
  walk — the shape where the next enclosing opener is a bounded `.map(` receiver already in `ok` —
  `node tools/hooks/agent-cap.js` exits `2`. This is the `:910` path, and without its own arm the
  brace-walk arm passes while this one stays admitted.
- **AC6** — When `grep -n 'for|while' tools/hooks/agent-cap.js` is run, the six separate literals are
  gone: `LOOP_HEADER` and the two siblings derived from it are the only carriers of the keyword set.

## 7. Gates

`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `agent-cap self-test` and
`agent-cap restatement self-test` legs, which are `subject = kit` in `tools/gate-legs.json` and are
therefore held as `ondemand` by `tools/run-gates/run-gates.sh:947` on the plain bar. `AGENTS.md`
records that no boundary sets `GATE_SELFTESTS` (owner, 2026-08-27) and that a DoD owes the full pair
for KIT work, which this is. The `agent-cap restatement` leg is `subject = repo` and does run on the
plain bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Both evasion shapes reproduced at exit 0 against the shipped
  hook before writing; the transcript of that measurement is in the build README's rules slot.
- rev-2 · 2026-09-04 · folded the pre-wiring predicate run and spec-audit round 1 (H3, H7).
  **The predicate run** over all eight tracked `*.js` found ZERO lines the widened predicate matches
  and the current one does not, so the widening denies nothing currently admitted. Recorded at
  `memory/builds/aWeldedTribunal/build/2026-09-04-build-TOOL-aWeldedTribunal-2-1-predicate-measurement.md`.
  **H3, high:** rev-1's inventory listed five sites and omitted `:910`,
  `if (/\b(for|while)\s*$/.test(before))`, which cannot take `LOOP_HEADER` because it matches a
  keyword TAIL. §4 now carries the sixth row, the derived sibling, and the fail-open that widening
  the header sites alone would leave open; AC5 gives the opener walk its own arm and the old AC5 is
  renumbered AC6. **H7:** §7 named the plain bar for `subject = kit` legs that
  `run-gates.sh:947` holds as `ondemand`; corrected to `GATE_SELFTESTS=1`, and the one leg that IS
  `subject = repo` is now distinguished rather than lumped in.

## 10. Reuse audit

The seam is `tools/hooks/agent-cap.js` itself and specifically its five existing loop-header
predicates, found by `python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for
loop shapes and array literals"`, which ranked `capFindings`, `checkLiteralOpen`,
`renderBlankedLiterals` and `resolveLiteralEnd` in that file. No new mechanism is introduced: this
unit consolidates a predicate the file already has five copies of.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
