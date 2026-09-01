# TOOL-dFoldedVerdict-4 — `agent-cap` admits a strictly sequential awaited `agent()` under a marker that names a bound

**Status:** SPECCED · rev-4 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md) | spec-audit | TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-5 TOOL-dFoldedVerdict-6 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` denies an `agent(` call inside any loop body, unconditionally, while
`TOOL-cBriefedPilot-21` ratified `parallelism route: none`. A harness that dispatches per unit
therefore has no legal shape: bounded-parallel is permitted by the hook and forbidden by the
verdict, and sequential is required by the verdict and forbidden by the hook. This unit adds a third
marker to the hook's whitelist — a claim whose shape is checked, like its two siblings — so that a
STRICTLY SEQUENTIAL awaited call over a receiver the hook already proves bounded is admitted, and
every evasion the loop ban was written for stays denied.

This build is its own live instance of the cost, and the instance is dated rather than argued. Its
spec set holds six units, so dispatching them takes a fan over a six-element list, and that shape is
refused today. Reproduced on node `d`, 2026-09-01, against the hook at `adc0543c`: one script naming
a five-element `UNITS` literal and routing it through `boundedParallel` exits 0, and the same script
with a sixth element exits 2, naming `UNITS` as a receiver the file does not show to be bounded. The
strictly sequential form the ratified verdict actually requires — a `for … of` over that same list
whose body reads `out.push(await agent(promptFor(u)))` — exits 2 at every list length, naming a loop
body. So this build's six specs were dispatched by hand across five agents rather than by a harness,
which is the concrete thing this unit removes.

## 2. Scope (IN)

*Every symbol in `tools/hooks/agent-cap.js` is named below by its DECLARATION, never by a line
number. This unit inserts a constant above `FIXED_MARK` and a predicate inside `fanoutFindings`, so
every line number in that file at or below the constant moves under its own diff; a pin here would
be stale the moment the unit is built. The rev-1 draft carried them throughout, and rev-2 removed
every one whose file this unit touches.*

- **S1** — A third marker constant declared beside `FIXED_MARK`, spelled
  `gov:sequential-agents`, written as a line comment on the LOOP HEADER line and carrying a bound
  token immediately after it.
- **S2** — A predicate inside `fanoutFindings` that admits an
  `agent(` occurrence in a loop body when, and only when, all eight clauses of §4 hold. Every clause
  that does not hold is a REFUSAL naming which one, in the convention `markedWhy` already applies to
  a refused `gov:fixed-verifiers` assignment.
- **S3** — The bound is resolved by `boundedK` and by nothing else.
  No second resolver, no second constant, no environment read.
- **S4** — The loop's iteration source must be a bare identifier already in the `ok` set that
  `fanoutFindings` builds for `.map`-style receivers. The marker's bound alone does not admit
  anything: it is the author's claim, and `ok` is the shape check that stops the claim being made
  falsely, exactly as `chunk(x, Math.ceil(x.length / K))` is for `gov:fixed-verifiers`.
- **S5** — New arms in `tools/hooks/agent-cap.test.sh`: the shapes that must now be ADMITTED, and one
  arm per refusal clause, each observed RED before the predicate is written.
- **S6** — The no-regress PROPERTY arm in `tools/hooks/agent-cap.test.sh` — the one whose green line
  reads `no-regress: no denial lost against BASE` — gains a
  CLASS-SCOPED ratification: a denial the BASE hook made and this hook does not is ratified only
  when deleting every `gov:sequential-agents` token from that file's bytes restores the denial. It
  needs no path list and no `GOV_BASE_SHA` bump. The arm reports the ratified count and REDS when it
  is zero, so the ratification branch cannot go unexercised and pass by never running.
- **S7** — Two fixtures under the arm's own `nrfix` population: one marked bounded sequential loop
  (the ratified path) and one unmarked braceless loop (the lost path), so neither branch of S6 is
  graded over an empty set.
- **S8** — `tools/hooks/README.md` gains the third marker's spelling and grammar. It OWNS the marker
  grammar; the charter delegates to it at `coding-governance-agents.template.md:244` and must not be
  touched.
- **S9** — `tools/workflows/REVIEW-PROTOCOL.template.md:125` — the sentence beginning
  `Everything else is denied` — is amended in the TEMPLATE, and
  `memory/guides/REVIEW-PROTOCOL.md:125` is regenerated from it by
  `bash tools/workflows/check-protocol-parity.test.sh --render`, never hand-edited.
- **S10** — `.claude/hooks/agent-cap.js` is rewritten byte-identically from `tools/hooks/agent-cap.js`
  in the same commit, and `KIT_AGENT_CAP_VERSION` moves with EVERY tracked carrier of the
  `gov:kit agent-cap@` marker. That population is DERIVED and is not listed here; §4's third trap
  records why the rev-1 draft's "both copies" was an undercount.
- **S11** — Two dossier sentences that go false, both amended in place and both named by their TEXT
  rather than by a line number, because this unit's own edits move the lines under them: the
  `Both markers are CLAIMS whose shape is checked` sentence in `memory/map/features/agent-cap.md`,
  and the `denies an agent() in any loop body` clause in `memory/map/features/unattended.md`. The
  rev-1 draft pinned that second one at `:49`; the clause is at `:50-51` and `:49` is the preceding
  sentence, so the citation is dropped rather than corrected.
- **S12** — Two sentences of the `TWO SHAPES HERE ARE FORCED RATHER THAN CHOSEN` header comment in
  `tools/workflows/unattended-build.js`: the one saying this hook `refuses an agent() inside ANY loop
  body, unconditionally`, and the one saying its whitelist `names no marker for the case`. The
  numbered items below them describe shapes this unit does NOT change and are left alone — the rev-1
  draft's `:41-58` range reached both.
- **S13** — One backlog row in `memory/backlog/TOOL.md` for the two loop spellings §3 declares out,
  minted with this build's slug at build time.

## 3. Non-goals (OUT)

- **`for await (` and `do { … } while ( )` are OUT.** Both admit the UNMARKED thunk-array evasion
  today, measured at `adc0543c` by piping each shape to `node tools/hooks/agent-cap.js`: a
  `for await (const f of allFindings) { th.push(() => agent(f.claim)) }` exits 0, and the same body
  inside a `do { … } while (i < allFindings.length)` exits 0. The brace walk inside `fanoutFindings`
  tests `/\b(for|while)\s*\(/` against the line whose brace opened the
  block; `for await (` does not match it, and a `do {` line carries neither keyword because the
  `while` sits after the closing brace. Closing that is a widening of the DENY side, which is a
  different change from this unit's widening of the ADMIT side, and mixing the two makes one closing
  diff unreviewable. S13's backlog row carries it.
- Rewriting `tools/workflows/unattended-build.js` into a per-unit loop. Its `ordered` list comes from
  `--plan` and is not a receiver this hook can size, so this unit does not by itself make a per-unit
  loop over it legal — only a loop over a bounded GROUPING of it, or over a bounded stage literal.
  That rewrite is a separate unit and a separate decision.
- Raising, lowering or re-siting `MAX_VERIFIERS` or `MAX_LENSES`. `tools/check-playbook-parity.sh`
  carries five `PAIRS` rows, and FOUR of them resolve their owning half with
  `^const MAX_LENSES = <int>` or `^const MAX_VERIFIERS = <int>` in this file. Both declaration lines
  keep their exact shape. The fifth row owns the hook matcher and reads `.claude/settings.json`, not
  this file; the rev-1 draft said all five read this file, and re-reading the `PAIRS` block at source
  on 2026-09-01 says otherwise.
- Editing `coding-governance-agents.template.md`. It already delegates marker spellings and the
  resolvable-bound grammar to `tools/hooks/README.md` at `:244`, so no charter edit is owed, and the
  template is size-gated and parity-pinned.
- Touching `renderShippedLine`, `renderShippedView` or `renderShippedBlanks`. The BYTE arm in
  `tools/hooks/agent-cap.test.sh` — the one whose green line reads
  `no-regress: the three renderShipped* bodies are the BASE bytes` — compares those three bodies
  against their BASE counterparts and reds on any drift.
- Making `tools/hooks/agent-cap.test.sh` print the `PASS ($n assertions)` shape. It sits in
  `memory/project/testsuite-count-waivers.txt`, that registry is shrink-only, and a suite that starts
  complying without its row being drained reds `testsuite counts (every bar self-test prints one)`.

## 4. Design

### Data model

The marker is a LINE COMMENT on the loop header, carrying one bound token:

```js
const MAX_VERIFIERS = 5
const batches = chunk(units, Math.ceil(units.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const out = []
for (const g of batches) { // gov:sequential-agents MAX_VERIFIERS
  out.push(await agent(promptFor(g)))
}
```

The bound token is either an integer literal or an identifier, and it is resolved by `boundedK`
against the same `consts` map `fanoutFindings` already builds from `intConsts(code)`. One resolver,
three consumers, per `TOOL-aNumeralWarden-1`'s standing rule that a bound is resolved wherever it is
written.

### Inventory

Eight clauses. An `agent(` occurrence at code line `i`, starting at column `c`, whose enclosing
construct is a loop, is ADMITTED when every one of these holds, and REFUSED naming the first that
does not.

| # | Clause | Read from | Why |
|---|---|---|---|
| C1 | the enclosing loop header line `h` is located | `code` | the braceless branch, the one whose refusal reads `agent() in a braceless loop body`, puts `h = i`; the brace walk immediately below it already computes `h` and is refactored to return it |
| C2 | `lines[h]` — the RAW line — contains `gov:sequential-agents` | `lines` | both views break their scan on `two === '//'`, so a marker is invisible in `code`; `FIXED_MARK` is read from `raw` for the same reason inside `scan` |
| C3 | the marker is followed by a bound token `T` | `lines[h]` | a bare marker admits concurrency one with an unbounded total, which is the owner's stated refusal |
| C4 | `boundedK(T, consts)` is true | `code` | S3 — the marker's number is checked, never trusted |
| C5 | `code[h]` matches `/\b(for\|while)\s*\(/` | `code` | the SHAPE is read from the literal-blanked view, so a marker sitting inside a quoted string on a line that is not really a loop header blesses nothing |
| C6 | `code[h]` iterates a bare identifier in `ok` | `code` | the marker's bound is a claim; `ok` is what makes the total real |
| C7 | the text of `code[i]` before column `c`, right-trimmed, ends `await` | `code` | AWAIT-ADJACENCY on THIS occurrence, not "the line contains await" |
| C8 | no `=>` and no `\bfunction\b` between the loop opener and column `c` | `code` | a deferred call is a thunk array, which is the evasion the ban exists for |

A ninth condition is judged after the per-line pass rather than inside it: **exactly one admitted
occurrence may resolve to any one loop header `h`.** Two awaited calls in one marked body spend
twice the bound, so the marker would name a number the loop does not obey. Grouping the admitted
candidates by `h` and refusing every member of a group larger than one costs one map and one sweep,
and it makes the bound a SPAWN count rather than an iteration count.

Nested loops fail closed with no extra clause. The brace walk stops at the first enclosing
`for`/`while`, so an inner loop must carry its own conforming marker and its own bounded receiver;
an unmarked inner loop inside a marked outer one is refused at the inner header.

Two things the clauses CANNOT distinguish, stated rather than left to be discovered.

- **A marker inside a TEMPLATE literal, on a script whose view scan does not terminate.** Both full
  views drop template contents, so a `for (` written inside one reaches neither `code` array and C5
  refuses it. The `view.unterminated` fallback at the head of `fanoutFindings` does not: it is
  per-line, leaves backticks alone, and would read template text as code. That is the residual
  `TOOL-aLexedStripper-4` and `TOOL-dMispairedQuote-4` already carry for every other rule in this
  file, inherited unchanged rather than widened, and C6 still demands a bounded receiver inside the
  same text.
- **A loop whose body calls a function that itself spawns.** No rule in this file has ever followed a
  call, and this one does not either. The marker's bound is over `agent(` occurrences the file can
  SEE.

Two shapes fail CLOSED that a reader might expect to pass, and both have a one-line workaround. A
C-style `for (let i = 0; i < n; i++)` names no bare identifier for C6 to size and is refused; write
the `of` form over the bounded receiver. An arrow function declared inside the body BEFORE the call
trips C8; hoist it above the loop.

### Migration

None. Every currently tracked script keeps its verdict, because no tracked file carries the new
marker until this unit writes one. Measured at `adc0543c` over the 69 tracked files whose text
contains `agent(`: 36 are denied by the BASE hook at `d65da7ab`, and of those exactly two print a
loop-body finding at all — `tools/hooks/agent-cap.test.sh` and
`memory/builds/aLexedStripper/reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-7-closing-diff-round2.md`.
Both also print at least one NON-loop finding in the same block (`agent() fanned over \`D\`` and
`Array.from()` for the first, `agent() fanned over \`all\`` for the second), so no tracked file's
denial rests on a loop finding alone and none can flip to ADMIT by this change on its own.

### Rollout

The property arm's disposition is the item most likely to block the Definition of Done, and it is
decided here rather than at build time.

The no-regress property arm pipes every tracked file plus the `nrfix` fixtures to the BASE
hook at `GOV_BASE_SHA` (defaulted `d65da7ab`, which resolves in this tree) and then to this hook; a
file the BASE denies and this hook admits is a LOST denial and fails the suite.

The rev-1 draft claimed that arm would red the moment any tracked file carried a marked loop, and
that is FALSE. Measured on 2026-09-01 by piping each carrier this unit edits to the hook at
`adc0543c`: `tools/hooks/README.md`, both protocol copies and `memory/map/features/agent-cap.md` are
already denied on a RULE 3 finding, the one reading that a bound is written here which the file
cannot resolve, and this unit does not touch that rule — so their denial survives whatever loop they
carry. `memory/map/features/unattended.md` and `tools/workflows/unattended-build.js` exit 0 today, so
they have no denial to lose. `tools/hooks/agent-cap.test.sh` is denied on six findings and not one of
them is a loop finding: five read `agent() fanned over` a receiver and one reads `Array.from()`. So
no tracked file in this repo can produce a ratified loss, the ratified count over tracked files is
ZERO, and S7's marked fixture is the ONLY source of ratifications here as well as in an adopter's
tree. That makes S7 load-bearing rather than defensive, which is the correction: without it the
`R == 0` guard below reds this unit's own commit.

The disposition is a CLASS-SCOPED rule, not a path list and not a base bump:

> A lost denial is RATIFIED when, and only when, deleting every occurrence of the
> `gov:sequential-agents` token from that file's bytes and re-running THIS hook restores exit 2.

It is self-checking. A path list goes stale silently and a base bump discards every denial the BASE
made for reasons unrelated to this unit, which is the whole point of the arm. Deletion is a
substring replacement of the marker token with a neutral one, never a line deletion: the residual
`//` and whatever else the line carried stay, so the strip can only remove a CLAIM and cannot
introduce code.

Three properties this rule has, said plainly.

- It fails on every loss NOT attributable to a marker, which is the guarantee that matters.
- It CANNOT tell a correct blessing from an over-broad one. If a clause is written wrongly and the
  marker admits more than it should, the loss is still marker-attributed and is still ratified. What
  bounds that is the per-clause arms of S5, not this arm.
- It reds when the ratified count is ZERO, because a ratification branch that never runs is a branch
  whose green says nothing. S7's marked fixture is what keeps that count non-zero, in this tree and
  in an adopter's alike, per the measurement above.

The reported line becomes `population N scanned, D denied at BASE, R ratified by marker, L denial(s)
lost`, and the arm exits non-zero on `L > 0`, on `D == 0` (the existing vacuity guard), or on `R == 0`.

### Files touched (estimate)

| Path | What |
|---|---|
| `tools/hooks/agent-cap.js` | the marker constant, the eight clauses, the one-call sweep, the refusal strings, the version constant and its `gov:kit` marker |
| `.claude/hooks/agent-cap.js` | byte-identical mirror, required by the two-destination rule in `tools/hooks/kit.toml` |
| `tools/hooks/scratch-guard.js` | its `gov:kit agent-cap@` marker alone; the version constant on that line is scratch-guard's own and does not move |
| `.claude/hooks/scratch-guard.js` | the same one-line marker edit, in the wired copy |
| `tools/hooks/agent-cap.test.sh` | the ADMIT arms, one arm per refusal clause, the no-regress ratification and its two `nrfix` fixtures |
| `tools/hooks/README.md` | the third marker's spelling and grammar |
| `tools/workflows/REVIEW-PROTOCOL.template.md` | the `Everything else is denied` sentence |
| `memory/guides/REVIEW-PROTOCOL.md` | RENDERED from the template, never hand-edited |
| `memory/map/features/agent-cap.md` | `Both markers are CLAIMS` becomes three |
| `memory/map/features/unattended.md` | `denies an agent() in any loop body` becomes the marked form |
| `tools/workflows/unattended-build.js` | the header comment claiming the refusal is unconditional |
| `memory/backlog/TOOL.md` | S13's row for `for await (` and `do … while` |

Three traps in that list. `tools/check-agent-cap-restatement.sh` scans every tracked `*.md` outside
`^memory/(builds|archive|gotchas|backlog)/`, so five of the touched documents are in its population
and none of the new prose may put a bound word adjacent to a digit adjacent to one of its nouns —
write "a bound this file resolves" and "the file constant", never a numeral. And
`.lexicon.conf` pins `VERB_OFFENDER_PIN="461"` against a measured 461, so any new top-level function
here must lead with a declared verb; `resolveLoopHeader` and `checkSequentialMark` both pass
`python tools/lexicon/lexicon.py --suggest`.

The third trap was found while verifying this fold and is the same class the round-1 audit filed as
M8 against a sibling. **S10's version bump is not a two-file edit.** `tools/check-kit-versions.sh`
DERIVES the carrier population as `git grep -lE "gov:kit agent-cap@" -- '*.js'` and asserts every
member equals `KIT_AGENT_CAP_VERSION` — and `tools/hooks/scratch-guard.js` and
`.claude/hooks/scratch-guard.js` each carry that marker on their own `KIT_SCRATCH_GUARD_VERSION`
line, because scratch-guard ships inside the same kit entry. Measured 2026-09-01: the marker has four
tracked carriers and this unit's Files-touched table names two of them. That checker's own comment
records the identical mistake being made before — a prior build moved the kit in both agent-cap copies
and left both scratch-guard copies behind, which is why the population became derived in the first
place. So no count of that population is written anywhere in this spec, S10 names the derivation, and
AC17 reads it from `git grep` rather than from a sentence.

### Alternatives rejected

- **A bare marker with no bound.** Refused by the owner, and correctly: concurrency one over 500
  items is 500 agents, and the ceiling this rule enforces is the verify-stage TOTAL.
- **The bound alone, with no bounded-receiver clause.** This is the shape the owner ruling names
  literally, and it FAILS OPEN on exactly the quantity the rule exists to bound: a marker reading
  `gov:sequential-agents 5` over `allFindings` would be admitted while spawning one agent per
  finding. Failing open here is worse than the current refusal, so C6 is not optional.
- **A blacklist of thunk-array spellings.** The receiver whitelist exists because provenance is
  undecidable from a line (`TOOL-aBatchedTribunal-1`), and the same argument applies one construct
  over: `th.push(() => agent(g))` and `out.push(await agent(g))` differ in deferral, not in origin.
- **Restructuring a call into a helper the loop invokes.** Refused at `TOOL-dBriefedPass-4`'s park:
  it is textually indistinguishable from the evasion the rule names, and passing a checker by
  indirection is worse than not passing it.
- **Bumping `GOV_BASE_SHA` past this build.** It discards every denial the BASE made, which is the
  arm's entire content, and it has to be done again on the next build that touches a loop.

## 5. Production-readiness checklist

- security — this is a guard against agent fan-out; the change WIDENS what it admits, so the whole
  risk of the unit is the fail-open direction, and C6 through C8 plus the one-call sweep are that
  control. No credential, network or write surface is touched.
- perf / scale — the added work is one map lookup per `agent(` occurrence and one grouping sweep at
  the end; the arm whose green line reads `quadratic budget: 8000 literals on ONE line` still binds
  and must stay under the ceiling that arm declares.
- a11y — N/A — a `PreToolUse` hook has no user interface.
- i18n — N/A — the marker is an ASCII token in source comments.
- error / empty / loading states — a script with no `agent(` occurrence, a marked loop with no body,
  and a marker on a line the views disagree about all reach the refusal path rather than an
  exception; `runBothViews` already turns a throw in one view into a fall-through and a throw in both
  into a denial.
- observability — every refusal names its clause and the token it could not resolve, in the
  `markedWhy` convention; the suite's per-arm `ok`/`FAIL` lines and the no-regress arm's four-number
  summary are the only outputs anyone reads.
- risks (concurrency, data-loss, rollback hazards) — the real hazard is a clause written loosely
  enough to bless a thunk array, which the no-regress arm ratifies rather than catches; rollback is a single revert
  because the marker is additive and no tracked script depends on it.
- testing + left-shift gates — one arm per clause, both no-regress branches armed, and the failing case of
  the new predicate observed RED by staging before it is written.
- migration / rollback — none needed; no tracked file carries the marker before this unit.
- user docs — `tools/hooks/README.md` is the user-facing grammar and is S8; the protocol pair is S9.

## 6. Acceptance criteria

- **AC1** — When the existing fixture `rule2: loop-built thunks → deny` in
  `tools/hooks/agent-cap.test.sh` is run, it still exits 2, and so do
  `bypass: a braceless for-of body → deny` and `bypass: a braceless while body → deny`.
  Witness: `bash tools/hooks/agent-cap.test.sh`.
- **AC2** — When a script binding `const MAX_VERIFIERS = 5`, then
  `const batches = chunk(units, Math.ceil(units.length / MAX_VERIFIERS)) // gov:fixed-verifiers`,
  then `for (const g of batches) { // gov:sequential-agents MAX_VERIFIERS` with
  `out.push(await agent(promptFor(g)))` in its body, is piped to `node tools/hooks/agent-cap.js`, it
  exits 0. Arm name: `rule2: a marked sequential loop over a bounded receiver → allow`.
- **AC3** — When the same script names a four-element array literal as the receiver instead of a
  bounded split — the stage-list shape — it exits 0. Arm name:
  `rule2: a marked sequential loop over a lens literal → allow`.
- **AC4** — When the marked loop iterates `allFindings`, a name the hook does not show to be bounded,
  it exits 2 with stderr naming `gov:sequential-agents` and that identifier. Arm name:
  `seq: an unbounded receiver under the marker → deny`.
- **AC5** — When the marker carries no bound token at all, it exits 2 with stderr saying the marker
  names no bound. Arm name: `seq: a bare marker names no bound → deny`.
- **AC6** — When the marker carries a bound the file cannot resolve — an identifier bound by an
  `<expr> || <int>` right-hand side, and separately a `.length` expression — it exits 2 naming the
  token it could not resolve. Arm names: `seq: an or-bound K → deny` and `seq: a .length K → deny`.
- **AC7** — When the marker carries an integer literal above the file constant, it exits 2. Arm name:
  `seq: a bound above the cap → deny`.
- **AC8** — When the marked loop body reads `th.push(() => agent(g))`, it exits 2 with stderr naming
  the deferral. Arm name: `seq: a thunk deferral inside a marked loop → deny`.
- **AC9** — When the marked loop body reads `th.push(agent(g))` — a collected promise, not an awaited
  call — it exits 2 with stderr naming the missing `await`. Arm name:
  `seq: a collected promise inside a marked loop → deny`.
- **AC10** — When the marker text appears inside a single-quoted string on a line that is not a loop
  header once literals are blanked, and a real unmarked loop sits below it, the script exits 2. Arm
  name: `seq: a marker inside a quoted string blesses nothing → deny`.
- **AC11** — When a marked loop body holds two awaited `agent(` calls, it exits 2 with stderr naming
  both line numbers. Arm name: `seq: two awaited calls in one marked loop → deny`.
- **AC12** — When `bash tools/hooks/agent-cap.test.sh` runs, its no-regress property line reads
  `population <n> scanned, <d> denied at BASE, <r> ratified by marker, 0 denial(s) lost` with `r`
  greater than zero, and the suite exits 0.
- **AC13** — When the `nrfix` fixture holding an UNMARKED braceless loop is present and the braceless
  branch of `fanoutFindings` — the one whose refusal reads `agent() in a braceless loop body` — is
  deleted as a staged break, the property arm prints
  `FAIL no-regress: a denial the BASE hook made is gone` naming that fixture; the break is unstaged
  and the run repeated green. Recorded as a staged-red note under
  `memory/builds/dFoldedVerdict/build/`.
- **AC14** — When the ratification strip in the no-regress property arm of
  `tools/hooks/agent-cap.test.sh` is staged to a
  no-op, `bash tools/hooks/agent-cap.test.sh` reports the marked `nrfix` fixture as a LOST denial and
  the suite fails; unstaged, it passes. Recorded in the same staged-red note.
- **AC15** — When `bash tools/workflows/check-verifier-fanout.sh` runs over the committed harnesses,
  it exits 0; `grep -c 'gov:sequential-agents' tools/workflows/REVIEW-PROTOCOL.template.md` and the
  same grep over `memory/guides/REVIEW-PROTOCOL.md` each return at least one; and
  `bash tools/workflows/check-protocol-parity.test.sh` reports parity between the two. The greps are
  the half with a failing case. Parity compares the template against its render, so it passes
  byte-identically whether or not S9's sentence was ever amended, and asserting parity alone would be
  a criterion that cannot fail on the absence of the change it grades (round-1 M4).
- **AC16** — When `bash tools/check-agent-cap-restatement.sh` runs after the five markdown carriers
  are edited, it exits 0 and `tools/agent-cap-restatement-waivers.txt` gains no row.
- **AC17** — When `grep -c 'gov:sequential-agents' tools/hooks/README.md` runs, it returns at least
  one; the value in `KIT_AGENT_CAP_VERSION` DIFFERS from the value the same constant held at this
  unit's pre-image, read with
  `git show <pre-image sha>:tools/hooks/agent-cap.js`; every path
  `git grep -lE 'gov:kit agent-cap@' -- '*.js'` names carries the NEW value; and
  `bash tools/check-kit-versions.sh` exits 0. Movement is asserted separately and against the
  pre-image because that checker grades AGREEMENT — it is satisfied at a version nobody bumped, so it
  can witness the carriers being consistent and never that the bump happened.
- **AC18** — When `diff tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` runs after the commit,
  it reports no difference, and the same `diff` over the two `scratch-guard.js` copies also reports
  none.
- **AC19** — When `python tools/lexicon/lexicon.py` runs, its `P1 verb` line reports `offenders=461`
  or fewer, so no new function name raised the pin.
- **AC20** — When the pass is complete, `grep -n 'gov:sequential-agents'` returns a hit in each of
  `memory/map/features/agent-cap.md`, `memory/map/features/unattended.md` and
  `tools/workflows/unattended-build.js`; the same grep for `Both markers are CLAIMS` over
  `memory/map/features/agent-cap.md` returns no line, so the falsified sentence is GONE rather than
  contradicted beside itself; and `grep -n 'for await' memory/backlog/TOOL.md` returns a row whose id
  begins `TOOL-dFoldedVerdict-`. This is the only witness S11, S12 and S13 have, and each of the
  three gates a reader would expect to cover them is blind here: no `codebase-map` leg reads dossier
  PROSE, `check-agent-cap-restatement.sh` keys on a bound word beside a digit rather than on these
  sentences, and `workflow script syntax` parses the script instead of reading its header
  (round-1 M3).

## 7. Gates

Every leg named here resolves in `tools/gate-legs.json`.

- `agent-cap self-test` — the unit's own suite. It carries `subject: kit` and `chunk: selftests`, so
  it is HELD on a default bar; a Definition of Done for this unit owes
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, or the suite run standalone as
  `bash tools/hooks/agent-cap.test.sh`. It is NOT the unattended kit's suite and the standing owner
  instruction forbidding `tools/unattended/*.test.sh` does not reach it.
- `verifier fan-out` — delegates to this hook over the committed workflow harnesses; the gate that
  proves the predicate did not start denying a shipped script.
- `verifier fan-out self-test`
- `review-protocol parity (kit vs dogfood)` — S9's render, asserted.
- `agent-cap restatement` and `agent-cap restatement self-test` — the five markdown carriers.
- `review-join ban (no ref-keyed join)` — rule 5 shares this file and must stay green.
- `workflow script syntax` — S12 edits a workflow script's header.
- `kit version markers` — S10's paired bump.
- `govkit selfcheck` and `install-prefix (shipped surface)` — no new tracked file appears under
  `tools/hooks/`, so both must stay at zero unclaimed.
- `codebase-map coverage + freshness` — S11's dossiers.
- `memory hygiene` — this spec and its records.
- `lexicon naming predicates` — AC19's pin.

New gate added: none. The predicate is enforced at the tool call by the hook itself and on the bar by
`verifier fan-out`, which already delegates to it rather than re-implementing it.

## 8. Open questions

- **F1 — the marker spelling.** RESOLVED (owner, 2026-09-01): `gov:sequential-agents`, carrying its
  bound as `gov:sequential-agents(5)`. `gov:sequential-agents` reads as what it claims and matches the
  `gov:` prefix both siblings use. `gov:sequential-fanout` would pair with `gov:bounded-fanout` but a
  sequential dispatch is not a fan-out, and `gov:one-at-a-time` says nothing about the bound.
  Recommendation: `gov:sequential-agents`. Whatever is chosen is written once in the hook and read
  everywhere from that constant, so this decides prose and not structure.
- **F2 — the one-call-per-marked-loop sweep.** RESOLVED (agent, 2026-09-01): land it here. It is
  what turns the marker's number from an
  ITERATION bound into a SPAWN bound, and without it a body holding two awaited calls spends twice
  what the marker claims. It costs a two-pass restructure of the `lines.forEach` sweep that builds
  `bad`. The alternative is to land the eight clauses now and file the
  sweep as a backlog row, which leaves a stated fail-open of exactly 2x in the shipped rule.
  Recommendation: land it here — a stated fail-open in the guard's own admission path is the thing
  this unit exists to avoid.
- **F3 — the `denies an agent() in any loop body` clause in `memory/map/features/unattended.md`.**
  RESOLVED (agent, 2026-09-01): amend it here, as a rewrite of the clause and never as an appended
  negation. Deferring a false claim to a compression pass is how it survives the build that
  falsified it. Its sentence explains why
  `tools/workflows/unattended-build.js` has the two shapes it has, and those shapes do not change in
  this unit; only the absolute `denies an agent() in any loop body` goes false. Amending one clause
  here risks the append-a-negation-beside-the-text-it-contradicts class, and deferring it to unit 6's
  compression pass risks a false claim surviving the build that falsified it.
  Recommendation: amend it here, as a rewrite of the clause rather than an appended sentence, and let
  unit 6 compress whatever survives.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft, authored against BASE `adc0543c` on node `d`.
- rev-2 · 2026-09-01 · folded the round-1 spec audit, and re-verified every citation at source while
  doing it. **M3** — added AC20, the only witness S11, S12 and S13 had. Each gate a reader would
  expect to cover those three is blind to them, and AC20 says which and why. **M4** — AC15 gained a
  pair of greps for `gov:sequential-agents` in both protocol copies. Parity compares a template
  against its own render, so it passes byte-identically whether or not S9's sentence was amended, and
  it was the only criterion touching S9. **The ordinal class**, filed as L1 against a sibling and
  reaching this spec throughout: every line number pinned into a file this unit's own diff moves
  is replaced by a content anchor. S1, S2 and S3 pinned `agent-cap.js` below the constant this unit
  inserts; C2 and F2 pinned its interior; S6, AC13, AC14 and two §3 bullets named test-file arms by
  ordinal, and those arms are now named by the line they print. §2 states the convention once.
- rev-2, continued — four corrections the audit did not file, found by re-deriving its citations.
  `memory/map/features/unattended.md:49` was simply WRONG: the `denies an agent() in any loop body`
  clause is at `:50-51`. `memory/builds/dBriefedPass/RUN.md:29` in §10 is the `## Parked` HEADING; the
  park entry this unit answers is `:63`. §3 claimed all five of `check-playbook-parity.sh`'s `PAIRS`
  rows read this file; four do, and the fifth reads `.claude/settings.json`. And the largest one:
  **AC17 named two `gov:kit agent-cap@` carriers where `check-kit-versions.sh` DERIVES four**, adding
  both `scratch-guard.js` copies — the identical undercount the audit filed as M8 against a sibling,
  and the identical one that checker's own comment records a prior build making. The count is deleted
  rather than corrected, S10 names the derivation, the Files-touched table gains both copies, and
  AC17 now asserts MOVEMENT against the pre-image because that checker grades AGREEMENT and is
  satisfied at a version nobody bumped. §4's Rollout also claimed a tracked marked loop would red the
  no-regress arm; measured on 2026-09-01, no tracked carrier can, which promotes S7 from defensive to
  load-bearing. §1 gained this build's own denied six-unit spec fan as dated evidence.
- rev-2, refusals and rulings, recorded rather than left silent. **M5 as filed does not reach this
  unit.** It addresses a sibling's `kit.toml` rows and Skill sentence; verified at source,
  `tools/hooks/kit.toml` already declares `README.md` as an engine file to `{prefix}/hooks/README.md`,
  S8 adds no destination and no new tracked file under `tools/hooks/`, and AC17 observes the README's
  content directly rather than inferring it from an adopter check. **The owner ruling that
  `KIT_UNATTENDED_VERSION` moves once on unit 6 does not reach S10.** That is a different kit with a
  different constant and a disjoint carrier set: `check-kit-versions.sh` holds the two as separate
  blocks, and this spec claims only `KIT_AGENT_CAP_VERSION`, whose carriers no other unit in this
  build touches. **The owner ruling that the marker must NAME A BOUND the hook resolves** was already
  the rev-1 design and is unchanged — S1, C3, C4, AC5 and the first Alternatives-rejected bullet each
  carry it, and a bare marker is refused rather than treated as concurrency one.
- rev-3 · 2026-09-01 · reordered to order 5 by the build's own ordering fix. No scope change: this unit touches no protocol carrier, and it moved only because the section-7 split had to precede the units that add protocol bytes to a render already at EXACTLY `GUIDE_CAP_BYTES`.

- rev-4 · 2026-09-01 · the fork sweep. F1, F2 and F3 marked; the spec is no longer FORKED. **F1**
  is the owner's, taken 2026-09-01: the marker is `gov:sequential-agents` and it carries its bound as
  `gov:sequential-agents(5)`. It becomes permanent grammar in `tools/hooks/README.md` and in every
  adopter's copy of the hook, which is why it went to the owner rather than being picked here.
  **F2** — the one-call-per-marked-loop sweep lands in this unit rather than as a backlog row: it is
  what turns the marker's number from an ITERATION bound into a SPAWN bound, and shipping without it
  would leave a stated 2x fail-open inside the guard's own admission path. **F3** — the false
  `denies an agent() in any loop body` clause in `memory/map/features/unattended.md` is rewritten
  here, not appended to and not deferred to unit 6's compression pass, because a claim deferred to a
  compression pass is a claim that survives the build which falsified it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "admit a sequential awaited agent call inside a loop body
under a marker naming a bound"` ranked `boundedParallel` (`tools/workflows/tier2-review.js`, fan-in 3,
SEAM) first and then `boundedBranch` and `boundedK`, both in `tools/hooks/agent-cap.js`, together with
the `agent-cap.topLevelArgs` affordance seam. The seam this unit EXTENDS is therefore inside the file
it changes and is named twice by the probe: `boundedK` in `tools/hooks/agent-cap.js` is the bound
resolver S3 reuses without adding a second one, and the `ok` receiver set built by the two
`lines.forEach(scan)` passes in the same file is the bounded-receiver proof C6 reuses without adding a
second one. Verified against source at `adc0543c` rather than taken from the probe: `boundedK` accepts
an integer literal or an identifier bound by a bare `const <name> = <int>` and rejects an
`<expr> || <int>` binder, and `intConsts` invalidates a name that is later reassigned. No new seam is
created and none of the three shipped harnesses changes shape.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap deny every loop body
containing agent() and what would a marker that names a bound have to check" --terms "agent-cap
fan-out marker gov:fixed-verifiers boundedK loop body sequential thunk evasion verifier arity
parallelism route bounded receiver"` — 38 hits, of which the deciding ones were
`memory/builds/dBriefedPass/RUN.md:63` (the park entry this unit answers — the `decision` row opening
`tools/hooks/agent-cap.js denies any agent() inside a loop body unconditionally`; the rev-1 draft
cited `:29`, which is the `## Parked` HEADING and not the row),
`memory/builds/aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md:81` (the marker
as an unchecked bypass, and why a marker on the call line was removed) and
`memory/archive/DECISIONS.2026-08-10.md:49` (`TOOL-aBatchedTribunal-1c`, why the predicate is a
whitelist and not a blacklist).
