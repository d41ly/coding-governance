# TOOL-dMispairedQuote-1 — one quote-opening decision, shared by every view in `agent-cap.js`

**Status:** CLOSED · rev-4 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-TOOL-dMispairedQuote-1-acceptance-ledger.md](../build/2026-09-01-build-TOOL-dMispairedQuote-1-acceptance-ledger.md) | journal | TOOL-dMispairedQuote-3 |
| [2026-09-01-build-TOOL-dMispairedQuote-1-staged-red.md](../build/2026-09-01-build-TOOL-dMispairedQuote-1-staged-red.md) | journal | — |
| [2026-09-01-prompt-TOOL-dMispairedQuote-1.md](../prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md) | research | TOOL-dMispairedQuote-2 |
| [2026-09-01-review-TOOL-dMispairedQuote-1-2-3-closing-diff-round1.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-3-closing-diff-round1.md) | diff-review | TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3 |
| [2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md) | spec-audit | TOOL-dMispairedQuote-2 |
| [2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round2.md) | spec-audit | TOOL-dMispairedQuote-2 |

<!-- /gen:spec-records -->

## 1. Goal

`agent-cap.js` reads three views of a workflow script and each one pairs a quote with the next quote
of the same kind on the line. An apostrophe in prose earlier on that line takes the pairing, and the
span blanked between the two carries the fan-out. All three rules are defeated by it, at exit 0. This
unit gives the file ONE decision about what opens a string literal, and applies it in all three.

## 2. Scope (IN)

- **S1** — Add `checkLiteralOpen(line, i)` and `resolveLiteralEnd(line, i)` to
  `tools/hooks/agent-cap.js`. A quote opens a string literal only where one may legally BEGIN.
  `checkLiteralOpen` skips whitespace backwards, then answers false when the character it lands on is
  `[A-Za-z0-9_$)\]\\]` — UNLESS the identifier ending there is a JavaScript keyword after which an
  expression may start. `LITERAL_OPENERS` holds ELEVEN members — `return case throw typeof
  instanceof new delete void yield await else` — and the three the fold first carried and round 2
  refuted are gone: `in`, `of` and `do` are ordinary English connectives, so a comment reading
  "one of 'em", "in 'ere" or "do 'em" made the apostrophe a legal opener and admitted the fan. The
  eleven that remain are a STATED residual with a fixture each, not a claim of closure, and every one
  of them admits at HEAD too, so none is a regression.
  `resolveLiteralEnd` returns the index of the unescaped partner on the same line, or `-1`
  when the quote does not open a literal or has no partner. Escapes are consumed two characters at a
  time, as every existing branch already does. Both names lead with a verb the lexicon declares —
  `check` and `resolve` — which §10 records the consult for.
- **S2** — `stripStrings` becomes one ordered pass over the line using `resolveLiteralEnd`, replacing
  the two independent `replace()` passes. It skips a same-line backtick span whole rather than
  scanning inside it, so template prose contributes no false opener. It does NOT blank template
  contents: rule 1's fail-closed ceiling for a primitive named inside a template is
  `TOOL-aLexedStripper-3`'s and is out of scope here. **`stripStrings` has THREE consumers, not one**
  — rule 1's `offendingLines:84`, and rule 2's fallback view at `fanoutFindings:356`, which
  `TOOL-aLexedStripper-5` reaches whenever a scan ends unterminated. S2 re-bases both.
- **S3** — A quote `resolveLiteralEnd` cannot pair is emitted as ORDINARY TEXT and the line stays
  blanked, EXCEPT inside a same-line template span, which S2 emits whole. **No view hands a
  consumer a raw line outside a template span**, and the template case is closed by
  `TOOL-dMispairedQuote-3` rather than by wording. This replaces rev-1's whole-line
  fail-closed, which round 1 reproduced as a fail-OPEN in two rules: `stripStrings` runs BEFORE the
  line-comment strip on purpose, so a raw line let a `//` inside a string truncate the view; and
  `joinCall` balances parens across lines, so a raw line re-admitted string and comment parens to the
  join. §4 carries both reproductions.
- **S4** — `renderCodeView`'s code-mode quote branch calls `resolveLiteralEnd`. An unpairable quote
  keeps the branch's existing behaviour — emit the character, advance one. The flag's CODE is
  untouched; **its VALUE is not**, and saying otherwise was round 2's finding 18: the shipped branch
  SKIPS a mispaired span, so a backtick inside one never reaches the mode switch, and refusing the
  mispairing feeds it. The flag is false at BASE and true after, for a regex literal carrying both an
  apostrophe and a backtick. The consequence is bounded by `TOOL-dMispairedQuote-3`, not by this
  scope item.
- **S5** — `blankLiterals`' quote branch calls `resolveLiteralEnd` on the same terms. This also
  removes its run-to-end-of-line swallow, which is the defect `addc6169` fixed in `renderCodeView`
  and left here, named as out of scope by that round's own review record.
- **S6** — Every byte of S1 to S5 is mirrored into `.claude/hooks/agent-cap.js`, the wired copy.
- **S7** — `KIT_AGENT_CAP_VERSION` moves to `1.10`, and so does EVERY `gov:kit agent-cap@` marker.
  There are FOUR tracked carriers, not the one line rev-2 named: both `agent-cap.js` copies and both
  `scratch-guard.js` copies, each carrying `gov:kit agent-cap@1.9` on a line whose own constant is
  `KIT_SCRATCH_GUARD_VERSION`. `check-kit-versions.sh` derives that population and asserts every
  carrier agrees, so bumping one of four reds the leg. It grades FORM only and has no bump rule, so
  new engine bytes shipped at `1.9` red nothing and an adopter cannot tell a patched engine from the
  one they hold.
- **S8a** — Regenerate `memory/map/generated/symbols.json`. `agent-cap.js` contributes 23 rows today
  and S1 adds two top-level definitions to a file under `tools/`, which `map_extractors` scans.
- **S8** — `TOOL-aLexedStripper-5` was CLOSED on the argument that the fallback view "IS the shipped
  behaviour, so it cannot regress in either direction". S2 re-bases that view, so the argument stops
  holding. Record a `memory/DECISIONS.md` row superseding that clause — the log is append-only and
  the closed record is not rewritten — and keep `-5`'s own legal fixture green on both sides.
- **S9** — Regression arms in `tools/hooks/agent-cap.test.sh`, each staged RED against the tip before
  it lands, covering the CLASS in all three rules AND in both directions:
  the apostrophe-shares-the-line shape for rule 1 (regex literal, double-quoted string, block
  comment, template literal, loose `'em` prose), for rule 2, and for rule 3 at a MULTI-LINE call
  site, which is the shape every shipped harness uses and which rev-1's three rule-3 probes all
  missed. Each carries a control with the apostrophe removed. The ADMIT direction is armed too: a
  legal `log('parallel(') // we don't allow it`, a `return`/`case`/`throw` string naming a primitive,
  and `-5`'s regex-with-a-backtick fixture, each asserted at exit 0 — and rule 3 gets an ADMIT case
  of its own, a legal multi-line `boundedParallel(x, 5)`, because rev-2's rule-3 group asserted only
  denials and a fixture group that cannot fail in one direction is §7's could-not-fail shape.
  **The keyword clause is fixtured over its DECLARED SET, not sampled**: one arm per member of
  `LITERAL_OPENERS`, each a block comment ending in an apostrophe-word above a raw `parallel(`,
  asserting the verdict measured for that member. Adding a member then adds its fixture.
- **S10** — This unit does not land without `TOOL-dMispairedQuote-3`. Its mechanism un-hides
  delimiters as well as fan-outs, and unit 3 is the property that bounds it.

## 3. Non-goals (OUT)

- `TOOL-aLexedStripper-3` — rule 1 denying a primitive written inside a lens PROMPT. That is a
  FALSE POSITIVE and widening rule 1's blind spot needs fixtures in both directions. S2 deliberately
  leaves the ceiling where it is.
- `TOOL-aLexedStripper-4` — `blankLiterals`' `let mode` sitting outside the per-line loop, so one
  unterminated template blanks every later line. A different defect in the same function; S5 touches
  the quote branch and not the mode.
- Modelling regex literals. Section 4 records the test that rejected it.
- A fail-closed that substitutes a different rendering for a line. Section 4 records the two blockers
  that rejected it, and §5 states the residual accepted in its place.
- Any change to what rules 1, 2 or 3 DECIDE. This unit changes only what they can SEE.

## 4. Design

The file holds three string views and each has its own quote handling: `stripStrings` (rule 1's view
and rule 2's fallback, two regex passes), `renderCodeView` (rule 2, an ordered per-line scan),
`blankLiterals` (rule 3, an ordered scan with a block-comment mode). They disagree about what a quote
is, which is why the same apostrophe defeats them in three different ways and why one repair has now
twice fixed one of them.

### Data model

`resolveLiteralEnd(line, i)` is the whole contract. It answers one question — where does the literal
opening at `i` end, if one opens there — and every view asks it instead of walking the line itself.

```js
function checkLiteralOpen(line, i) {
  let p = i - 1
  while (p >= 0 && (line[p] === ' ' || line[p] === '\t')) p--
  if (p < 0) return true
  if (!/[A-Za-z0-9_$)\]\\]/.test(line[p])) return true
  const word = /([A-Za-z_$][\w$]*)$/.exec(line.slice(0, p + 1))
  return word !== null && LITERAL_OPENERS.has(word[1])
}
```

In valid JavaScript a string's opening quote is never GLUED to the character that ends an expression,
and never follows a bare word that is not a keyword. `don't`, `won't`, `it's`, `y'all` and `run 'em`
are all refused by that rule; `return 'x'`, `case 'y':` and `throw 'z'` are admitted by the keyword
clause. The predicate does not depend on which construct the prose sits in, which is why it reaches a
block comment and a template literal as well as a regex.

### Alternatives rejected

Six candidates were built as patched copies of the shipped hook and measured against a 21-case rule-1
corpus, three probes each for rules 2 and 3, eleven probes for the two round-1 blockers, the shipped
suite, and every tracked file in this repo fed to both hooks. Scores are the rule-1 corpus.

| candidate | rule 1 | rule 2 | rule 3 | the test that rejected it |
|---|---|---|---|---|
| model regex literals in `stripStrings` | 16/21 | ADMIT | ADMIT | `W2`, `W3`, `W4`, `W6` — a block comment, a template literal and mid-line prose carry the same apostrophe and no regex, and all four still admit |
| the opener rule alone, no fail-closed | 20/21 | ADMIT | ADMIT | `W6` — `/* run 'em */` puts the apostrophe after a space, and a prev-character-only rule reads that as a legal opener |
| opener + whole-line fail-closed, `stripStrings` only | 21/21 | ADMIT | ADMIT | `R2` — `renderCodeView` carries the same mispairing and rule 2 still admits an unbounded receiver |
| the above plus `renderCodeView` | 21/21 | DENY | ADMIT | `R5`, `R6` — `blankLiterals` carries it too, and rule 3 admits a declared bound of 50 |
| the above plus `blankLiterals` (rev-1's design) | 21/21 | DENY | DENY | **round 1's two blockers**, both reproduced: `B26` and `B27` below |
| **whitespace-skipping opener with the keyword clause, no fail-closed** | **21/21** | **DENY** | **DENY** | chosen |

**`B26`, reproduced.** `stripStrings` is called BEFORE the line-comment strip, deliberately
(`agent-cap.js:69`), and `offendingLines:84` then does `stripStrings(line).split('//')[0]`. Under a
whole-line fail-closed, `const u = 'http://x'; const re = /won't/; await parallel(all.map(f))` returns
raw, the `//` inside the string truncates the view, and the `parallel(` after it is gone: HEAD DENIES,
rev-1's design ADMITS. The other direction reproduces too — `log('parallel(') // we don't allow it`
becomes a newly DENIED legal script.

**`B27`, reproduced.** `capFindings` reads a call site through `joinCall`, which balances parens
forward across lines. Given the sanctioned helper definition, a multi-line
`boundedParallel(` whose argument line carries an apostrophe and a quoted `)` returns raw under a
fail-closed, the join closes early inside the string, `topLevelArgs` yields one argument, and the call
falls through to the helper's DEFAULT of 5. A declared cap of **50** is ADMITTED where HEAD denies,
and the control with the apostrophe removed denies at both.

Both are one mistake: **a fail-closed that hands back a RAW line is a fail-OPEN with respect to any
consumer that reads across the line boundary.** The chosen candidate has no such fallback — an
unpairable quote is text, the line stays blanked, and delimiters keep the structure the consumer
walks.

### Inventory

| measurement | result |
|---|---|
| rule-1 shape corpus | 21/21, against 14/21 at HEAD |
| rules 2 and 3 probes | 6/6, against 3/6 at HEAD |
| blocker probes, both directions | 11/11, against 10/11 at HEAD |
| shipped suite at BASE | 105 passed / 0 failed, unchanged |
| tracked `.js` `.sh` `.py` fed line-by-line to both rule-1 predicates | 140 files, 86217 lines, 15603 blank differently, 5 flips to DENY, **0 to ADMIT** |
| every tracked file fed whole to both hooks, with unit 3 | 1263 files, 3 flips to DENY, **0 to ADMIT** |

The five line-level flips are all payload lines in `tools/hooks/agent-cap.test.sh` — shell
single-quoted JSON carrying escaped double quotes — and every one moves toward DENY. The three
file-level flips are markdown review records, never workflow scripts, and also move toward DENY.
**Rev-2 printed 4319 and 0 flips here and both were wrong**: they were measured with a superseded
predicate, which round 2's finding 11 caught by re-deriving the row from the block §4 publishes. The
numbers above come from lifting the predicate out of the candidate file rather than retyping it.

### Files touched (estimate)

| file | why |
|---|---|
| `tools/hooks/agent-cap.js` | S1 to S5, S7 |
| `.claude/hooks/agent-cap.js` | S6, verbatim mirror |
| `tools/hooks/agent-cap.test.sh` | S9 |
| `memory/DECISIONS.md` | S8 |

## 5. Production-readiness checklist

- security — this IS the security surface. Measured in both directions: the inventory table above is
  the evidence, and the one ADMIT-direction move is accounted for by name.
- perf / scale — one linear pass per line replacing two regex passes. The hook already runs per tool
  call and the script is bounded by what a caller sends.
- a11y — N/A — a stdin/stderr hook with no interface.
- i18n — N/A — the predicate is over ASCII source syntax, not over prose language.
- error / empty / loading states — unchanged. `main()` exits 0 on unparseable stdin, which S1 to S7
  do not touch.
- observability — unchanged. Every denial keeps the existing per-rule stderr explanation.
- risks — **two residuals, both stated rather than closed, and both wider than rev-2 said.**
  (a) `resolveLiteralEnd` opener-tests only the OPENING quote, so the shape needs ONE apostrophe in a
  legal opener position before the fan-out and ANY unescaped quote of the same kind after it — not
  one on each side, which was rev-2's understatement and round 2's finding 15. (b) The keyword
  clause: prose whose last word before the apostrophe is one of the eleven `LITERAL_OPENERS` members
  still mispairs. Neither is a regression — both admit at HEAD too — and S9 fixtures every member of
  the declared set so the leak is recorded rather than assumed away. Named here, in the dossier by
  `TOOL-dMispairedQuote-2`, and as backlog rows.
- testing + left-shift gates — S9. **The `agent-cap self-test` leg is NOT on an ordinary bar**: its
  manifest entry is `chunk = "selftests"`, `subject = "kit"`, and the runner holds every such leg
  unless `GATE_SELFTESTS=1`, which `GATE_FULL=1` does not lift. This unit's Definition of Done is
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and saying "already on the bar"
  was round 2's finding 13.
- migration / rollback — none beyond S7's version bump. The file is deployed verbatim and a revert is
  a file revert.
- user docs — `TOOL-dMispairedQuote-2` carries the prose. Not this unit.

## 6. Acceptance criteria

- **AC1** — When the three reported probes run against `tools/hooks/agent-cap.js`, all three exit 2;
  the third is `const re = /won't/; const r = await parallel([() => agent('a'), () => agent('b')])`
  and exits 0 today.
- **AC2** — When the same fan-out is preceded on its line by `"don't"`, `/* don't */`,
  `` `don't` `` or `/* run 'em */`, each exits 2 through rule 1's `offendingLines`.
- **AC3** — When `const re = /won't/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)`
  runs, it exits 2 — rule 2's `renderCodeView` sees the `agent(` the apostrophe used to hide.
- **AC4** — When a MULTI-LINE `boundedParallel(` call declares a cap of 50 and its argument line
  carries an apostrophe and a quoted `)`, it exits 2, and so does the control with the apostrophe
  removed — rule 3's `joinCall` still balances and `capFindings` still reads the 50.
- **AC5** — When `const u = 'http://x'; const re = /won't/; await parallel(all.map(f))` runs it exits
  2, and when `log('parallel(') // we don't allow it` runs it exits 0. Both directions of `B26`.
- **AC6** — When `TOOL-aLexedStripper-5`'s own legal fixture runs — a regex literal containing a
  backtick above a bounded fan — it exits 0 both before and after this change.
- **AC7** — When `bash tools/hooks/agent-cap.test.sh` runs, it reports 0 failed and a pass count
  strictly above 105, the count recorded at BASE.
- **AC8** — When each DENY-DIRECTION arm from S9 is staged against the tip WITHOUT the fix, it
  FAILS. The quantifier is scoped: S9's ADMIT-direction arms and controls pass at the tip by
  construction, and demanding a RED from them was round 2's finding 9. The observation is recorded
  under `memory/builds/dMispairedQuote/build/` — NOT `reports/`, which hygiene check 4's
  build-folder whitelist forbids.
- **AC12** — When the keyword sweep runs — one arm per member of `LITERAL_OPENERS` above a raw
  `parallel(` — every member's verdict matches the one S9 records, and the three dropped English
  connectives each exit 2.
- **AC9** — When `diff .claude/hooks/agent-cap.js tools/hooks/agent-cap.js` runs, it is empty, and
  the suite's own two-copy parity arm passes.
- **AC10** — When `git grep -c 'gov:kit agent-cap@1.10'` runs over the four tracked carriers it
  reports 1 for each, `KIT_AGENT_CAP_VERSION` reads `1.10`, and `bash tools/check-kit-versions.sh`
  exits 0.
- **AC11** — When `python tools/lexicon/lexicon.py --suggest checkLiteralOpen` and the same for
  `resolveLiteralEnd` run, both answer OK, and the `lexicon naming predicates` leg exits 0 with
  `offenders` no higher than `VERB_OFFENDER_PIN`.

## 7. Gates

- `agent-cap self-test` — `tools/hooks/agent-cap.test.sh`, the leg that owns this file.
- `lexicon naming predicates` — `subject = repo`, guarded on `tools/` and `.claude/`, so this diff
  runs it and its shrink-only `VERB_OFFENDER_PIN` binds.
- `verifier fan-out` — `tools/workflows/check-verifier-fanout.sh`, which delegates to this hook.
- `agent-cap restatement` — `tools/check-agent-cap-restatement.sh`.
- `kit versions` — `tools/check-kit-versions.sh`, for S7's constant and its marker.
- `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

- **F1 — how far does the repair reach: one view, two, or all three?** Rule 1 is where the report
  landed, but rules 2 and 3 read their own views and carry the same defect. Options: `stripStrings`
  only; `stripStrings` and `renderCodeView`; all three.
  RESOLVED (agent, 2026-09-01, delegated): all three. This is a FACT-QUESTION and the probe that
  decides it is stated: run the same mispairing shape against each rule's own verdict. The
  observation can produce a negative — rule 3 could have been immune, as it is to `/* don't */`,
  which it blanks. It was not: `R5` and `R6` admit a declared bound of 50 at HEAD and deny under the
  chosen candidate. Fixing two of three views would leave the class open one rule over, which is §7's
  gate-the-instance shape.
- **F2 — what does a view hand back when it cannot pair a quote?** Options: the raw line
  (rev-1's design); a differently-rendered line; nothing special, the quote is text and the line
  stays blanked. RESOLVED (agent, 2026-09-01, delegated): the third. Another FACT-QUESTION, decided
  by a probe that could have produced a negative and did: round 1 reproduced the raw-line option as a
  DENY-to-ADMIT move in rule 1 and again in rule 3, and the whole point of the option was to be
  fail-closed. The cost of the third option is the balanced-loose-quote residual §5 names, which is
  a precision loss and not a structural one.

## 9. Revision log

- rev-4 · 2026-09-01 · CLOSED. Folded the closing diff review's F1 and F2, both fail-opens this unit introduced and both reproduced: `checkLiteralOpen` copied the whole line prefix per quote, so 8000 literals on one line took 33.8 s and a hook that times out is NON-BLOCKING (now 83 ms, a backward identifier walk); and a throw in the corrected views exited 1, which is also non-blocking, before the shipped pass could run. A third residual was named — an apostrophe after an operator — filed as `TOOL-dMispairedQuote-8` and fixtured. Suite 150 passed / 0 failed.
- rev-1 · 2026-09-01 · initial draft, written after the five-candidate measurement in §4.
- rev-3 · 2026-09-01 · folded spec-audit round 2, which exited NON-CONVERGENT at 4 blockers against
  a ceiling of 2. Per BUILD-METHOD M4 the loop STOPPED and every standing blocker was disposed:
  **1, 8 and 17 PROMOTED** to `TOOL-dMispairedQuote-3`, because bounding what the corrected views
  un-hide needs a mechanism this unit does not have; **24 FOLDED** by narrowing `LITERAL_OPENERS`
  from fourteen members to eleven and fixturing the set rather than a sample of it. The nine highs
  folded here: the corrected inventory numbers (11), the held self-test leg (13), the four
  kit-version carriers (25), the `symbols.json` regen (26), AC8's forbidden write target and
  unsatisfiable quantifier (10, 9), the moved `unterminated` VALUE (18), the widened residual (15),
  and rule 3's missing ADMIT case (2). The disposition could not be recorded with the driver's
  `--disposition` flag: the rendered Skill documents it and `unattended 1.14` refuses it, which is
  parked in `RUN.md` and filed as a backlog row.
- rev-2 · 2026-09-01 · folded spec-audit round 1 (`2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md`),
  2 blockers and 6 highs. Deleted rev-1's whole-line fail-closed after reproducing both blockers
  against a patched hook (`B26`, `B27`); replaced it with a whitespace-skipping opener carrying a
  keyword clause, which needs no fallback. Renamed both new functions to declared verbs (F22).
  Named `stripStrings`' third consumer (F25). Added S7's version bump (F39), S8's supersession of
  `TOOL-aLexedStripper-5`'s cannot-regress clause (F32), ADMIT-direction arms in S9, and F2 to §8.
  Moved AC8's RED observations out of `RUN.md` (F21). Replaced §5's "no case moved" assertion with
  §4's measured inventory.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "strip string literals from a line of javascript before scanning
it for a call"` ranks `stripStrings`, `blankLiterals`, `offendingLines` and `renderCodeView` — all four
in `tools/hooks/agent-cap.js`, all fan-in 0. The seam this unit extends is `renderCodeView`, the
newest and most correct of the three views: it already does the ordered single pass the other two
approximate, and `resolveLiteralEnd` is the decision lifted out of it so the other two can ask the
same question. No new file and no new module. `memory/map/features/agent-cap.md` is the dossier.

Naming consult, per the same obligation applied to identifiers rather than to seams:
`python tools/lexicon/lexicon.py --suggest checkLiteralOpen` and `--suggest resolveLiteralEnd` both
answer OK; the rev-1 spellings `opensLiteral` and `literalEnd` were both refused, and appending them
to both copies moved `offenders` from 463 to 467 against a shrink-only pin.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap.js blank string literals
per line instead of lexing the script, and what was decided about the unpaired quote repair" --terms
"agent-cap stripStrings renderCodeView blankLiterals unpaired quote fan-out fail-open template
literal regex literal line-aligned view rule 1 raw primitive"` — 31 hits. The three that bind:
`TOOL-aLexedStripper-3` and `-4`, both OPEN and both named in §3 as out of scope, and `-5`, whose
ratified cannot-regress clause S8 supersedes.
