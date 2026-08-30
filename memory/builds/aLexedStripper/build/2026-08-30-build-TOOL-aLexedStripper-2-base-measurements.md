# BASE measurements and the rev-2 design proof — `TOOL-aLexedStripper-2`

**Serves:** journal TOOL-aLexedStripper-2

Node `a`, 2026-08-30, BASE `19d9b328`. Every verdict below is `node <hook> <<< {tool_name:Workflow,
tool_input:{script}}`, taking the exit code: `0` ADMIT, `2` DENY. The BASE column runs
`git show 19d9b328:tools/hooks/agent-cap.js`.

This record exists because §7 requires a gate's failing case to be OBSERVED before it is wired, and
because rev-1's design was refuted by measurement rather than by argument. The numbers are here so
the next reader does not have to re-derive them.

## 1. The false-positive class at BASE

A CORRECT five-element lens array, fanned through `boundedParallel(…, MAX_VERIFIERS)`. Only the
prose of one prompt differs. Every row SHOULD admit.

| prose contains | multi-line array | one-line array |
|---|---|---|
| a literal `...` | 2 DENY | 2 DENY |
| an unmatched `[` | 2 DENY | 2 DENY |
| an unmatched `]` | 2 DENY | 0 |
| an unmatched `)` | 2 DENY | 0 |
| an unmatched `}` | 2 DENY | 0 |
| an unmatched `(` | 0 | 0 |
| an unmatched `{` | 0 | 0 |
| two ASCII apostrophes | 0 | 0 |
| U+2019 apostrophes | 0 | 0 |
| an em dash | 0 | 0 |

Five spellings deny in the multi-line array, which is the shape every shipped harness writes.

**Two corrections to the records this build inherited.** `ABL-dPinnedVintage-4` attributes the
denial to two apostrophes eating a `)`, and the adopter's gotcha
`guard-blanks-quoted-strings-before-counting-brackets.md` prescribes U+2019 in place of ASCII `'`.
Both rows admit at BASE in both shapes, so the diagnosis is stale at 1.8 and the workaround
addresses nothing. And the round-1 spec audit reported that NO unmatched-`)` shape denies, having
run 17 one-line variants; the multi-line column refutes that, and the row survived into rev-2 with
its deciding array shape now named.

## 2. Why rev-1's design was withdrawn

Rev-1 said `fanoutFindings` should read `blankLiterals(script)`. Two shapes, both reproduced here,
say otherwise. Each is DENIED at BASE and ADMITTED under that reading.

| shape | BASE | rev-1's S1 |
|---|---|---|
| an unbounded fan below an unterminated backtick | 2 DENY | 0 ADMIT |
| an `agent(` inside a multi-line interpolation | 2 DENY | 0 ADMIT |

The first is `blankLiterals`' `let mode` at `agent-cap.js:506`, declared outside the per-line loop at
`:507`: one unmatched backtick blanks every later line, so rule 2 finds no fan-out site at all. The
second is that `blankLiterals` blanks interpolation bodies, and rule 5's per-line span view cannot
restore them for a rule whose walks are line-indexed.

Both were found by the round-1 spec audit and both were re-measured before folding rather than taken
on the report's word.

## 3. The rev-2 design, proven

`renderCodeView` prototyped against the shipped hook: line-aligned, interpolation bodies copied,
`${…}` nesting tracked, and a fail-closed branch when the scan ends inside a template literal.
29 shapes, one per acceptance criterion, BASE against prototype.

| criterion | shapes | result |
|---|---|---|
| AC1–AC4 prose must ADMIT | 20 | all pass; the five BASE denials become admits |
| AC5 six lenses must DENY | 1 | pass, unchanged |
| AC6a single-line interpolation must DENY | 1 | pass, unchanged |
| AC6b multi-line interpolation must DENY | 1 | pass, unchanged — the shape rev-1 would have opened |
| AC6c bounded fan inside an interpolation must ADMIT | 1 | pass, unchanged |
| AC7 unbounded fan below an unterminated backtick must DENY | 1 | pass, unchanged — the other shape rev-1 would have opened |
| AC8 nested template must ADMIT | 1 | pass — the fail-closed branch adds no false positive |
| AC9 prior escapes must stay DENY, correct harness stay ADMIT | 3 | pass, unchanged |

**29/29.** No verdict moved except the five false positives the unit exists to remove.

AC8 is the row worth keeping in view: a fail-closed branch on "ended inside a template literal" is
only safe because the nesting in S2 makes `` `a${`b`}c` `` balance. Without it that legal script
would end the scan in template mode and be denied, and the unit would have traded one false-positive
class for another.

## 4. A defect in this record's own harness, found and fixed

The first run of the verification script annotated every `BASE 2 -> prototype 0` transition as
`FAIL-OPEN!`. For the twenty prose rows that transition IS the fix, and the label would have made a
correct result read as twenty regressions. The verdict column was computed against the wanted value
and was never wrong, so nothing was mis-decided — but the annotation would have gone into this
record. It now fires only when the WANTED verdict is DENY. Noted because it is the
`fixture-passes-by-finding-nothing` family one step over: a harness whose reporting cannot
distinguish a fix from a regression is not reporting.

## 5. The corpus figures for `TOOL-aLexedStripper-1`

Recall and precision against stdlib `tokenize` NAME tokens, which is the exact set the tokenizer
approximates. Enumerated by `git ls-files '*.py'`, files that fail to tokenize skipped.

| corpus | current chain | candidate scanner |
|---|---|---|
| this repo, 46 files | recall 88.6% · precision 37.6% | recall 99.3% · precision 99.6% |
| `d41ly/incms` at `069f0459`, 1167 files | recall 97.5% · precision 39.0% | recall 99.5% · precision 99.3% |

Worst files under the current chain — this repo: `tools/lexicon/lexicon_conf.py` 55.6% recall,
`tools/codebase-map/selftest.py` 57.3%, `tools/lexicon/lexicon.py` 61.5%. inCMS:
`services/api/app/main.py` 18.8%, which is `ABL-bCandidLoupe-1`'s 81.3% loss.

12 files in this repo and 34 in inCMS lose more than 10% of their real identifiers. The adopter's
row says "24 .py files affected" and does not mention this repo at all.

## 6. The class is LATENT under this repo's own review harness

Two facts, measured after the fix landed, that change what this defect IS.

**The prose must be BACKTICKED.** The same lens array with its prompts written `"…"` or `'…'` admits
every row: `stripStrings` already blanks those, so the prose never reaches a counter. Only a
template literal survives to be read as structure — and a lens brief is always a template literal
when it is long enough to need one.

**`tools/workflows/tier2-review.js` is one style choice away from being denied**, and it is the
harness this build used for both spec-audit rounds and the closing review. Its `DIFF_LENSES` briefs
are SINGLE-QUOTED. Rewrite one of them as a template literal — the natural choice for prose that
long — and add ordinary punctuation:

| variant of the shipped harness | 1.8 | fixed |
|---|---|---|
| shipped, single-quoted brief | 0 | 0 |
| the same brief written backticked | 0 | 0 |
| backticked, with a literal `...` in it | **2 DENY** | 0 |
| backticked, with an unmatched `]` in it | **2 DENY** | 0 |

So this was never only a false-positive nuisance in a guard. It was a trap under every multi-agent
harness in the tree, disarmed per file by whether its author reached for a quote or a backtick, and
firing with a message about verifier arity that names nothing about quoting. An adopter session
reached the same conclusion independently about its own nine harnesses.

That is the strongest argument for the fix, and neither the adopter's row nor this build's first two
spec revisions had it. It was found by answering a peer session's question rather than by reviewing
the diff.

## 7. The adopter's standing exposure, measured on its own nine harnesses

Reported by the `aMendedTollgate` run in `d41ly/incms` after this record's §6, using the corrected
method: count backticked elements of the FAN RECEIVER, not any long backtick in the file. Six of its
nine committed workflow harnesses carry five backticked lens elements each; the other three carry
zero. All nine ADMIT today, which is itself the proof that no triggering punctuation is present in
those briefs right now.

So the accurate statement is sharper than "passing by luck on the quoting". Six of the nine already
LOST the quoting coin flip and are held up only by the second coincidence — the absence of an
ellipsis or a stray bracket in English prose, which is the most likely edit anyone ever makes to a
lens brief.

**Both repos' canonical harness is accidentally the safe one.** Here it is
`tools/workflows/tier2-review.js`, safe because its briefs are single-quoted. There it is
`tier2-review-indexed.js`, one of the three at zero. In each tree the most-invoked review path is
the one that happens not to be exposed, surrounded by siblings that are. That is worth stating
because it explains why the class survived this long in two repos at once: the harness everybody
runs is the harness that never fails.

Method note, recorded because it cost a wrong answer here first: a sweep that injects into any long
backticked span returns a clean grid that means nothing. §6's first pass over gov's four harnesses
did exactly that and read 0/0 everywhere; the injection had landed outside the lens array. Inject
into an element of the array that is the fan receiver, or do not run the sweep.

## 8. Why one grid row disagreed, and what it reveals

The adopter's grid and this record's disagreed on ONE row: an unmatched `)` in backticked lens prose.
This record had it denying; theirs had it admitting, at the same version, both measured honestly.
Reconciled against the adopter's own installed 1.6:

| prose | elements with `key: "x", prompt:` | elements with `prompt:` only |
|---|---|---|
| clean | 0 | 0 |
| unmatched `)` | **2 DENY** | 0 |
| unmatched `]` | 2 DENY | 2 DENY |
| literal `...` | 2 DENY | 2 DENY |
| a balanced `( )` pair | 0 | 0 |
| unmatched `)` at the very END of the prose | 0 | 0 |

**The variable is COMMA DENSITY, not the version and not the line shape.** A stray `)` drives
`topLevelArgs`' depth negative; from there every later comma is counted at top level instead of
being skipped, so the element count inflates past `MAX_LENSES`. How far it inflates depends on how
many commas FOLLOW the stray bracket — which is how many fields each lens object has, and where in
the array the prose sits:

| fields per element | prose in element 0 | in element 2 | in element 4 |
|---|---|---|---|
| 1 (`prompt` only) | 0 | 0 | **2** |
| 2 (`key` + `prompt`) | **2** | **2** | **2** |
| 3 | **2** | **2** | **2** |
| 4 | **2** | **2** | **2** |

So a single-field lens array is denied only when the prose is in the LAST element, and a two-field
one is denied wherever the prose sits. Real harnesses carry at least a key and a brief, so real
harnesses are in the second regime — the adopter's prompt-only fixture UNDERSTATED its own exposure,
and so would any minimal reproduction.

That also explains why an unmatched `(` never denies: it drives the depth the other way, and an
under-count still satisfies `<= MAX_LENSES`. And why a `)` at the very end of the prose is harmless:
no comma follows it inside the element.

Both grids were correct. Neither fixture was wrong. The disagreement was worth chasing because `)`
is far commoner in English prose than `]`, and the answer is that ordinary parenthetical writing IS
dangerous in any lens object with more than one field.

The adopter re-ran every row and confirmed it, then checked its own lens arrays rather than assuming:
`readopt-specreview.js:136` opens `{ key: 'claims-vs-source',`, `pinnedvintage-specreview.js:179`
opens `{ key: 'verbs-as-shipped',`, `drift-audit-code.js:137` opens `{ slug: 'dead-code',`. All six
of its exposed harnesses are multi-field, so all six sit in the right-hand column where an unmatched
`)` denies from ANY element.

**Three corollaries, and the third is the one no author could hold in their head.** Openers are safe
and closers are not, because an under-count still satisfies the cap. A closer at the very END of an
element's prose is harmless, because no comma follows it — so `see the table)` admits and
`the table), then stop` denies. And real lens elements are multi-field, so the dangerous regime is
the one every harness is actually in.

**The method rule this cost twice, stated as an instruction rather than an anecdote:** match the
fixture to the population — same field count, same element position — or the grid honestly describes
a different program. Two independent sessions each produced a clean, correct grid about a shape
neither of them had.

## 9. The class this build kept hitting: a clean result that means nothing

Six instances across two sessions in one night, three of them ours. They are one class in two
directions, and both survive reading, which is why neither reviewer nor author catches them.

**The FIXTURE direction — a probe that cannot reach the mechanism.**

| # | the clean result | what it actually described |
|---|---|---|
| 1 | rev-1's §4 fixtures for over-strip rows 3 and 4 | the identifier sat BEFORE the marker, so nothing could be lost |
| 2 | the adopter's four ADMIT rows against 1.6 | its lens prompts were single-quoted, so the prose never reached the counter |
| 3 | the adopter's `)` grid | a one-field element, where the class needs a comma after the stray bracket |
| 4 | the adopter's first swallow sweep | injected into any long backtick rather than into the fan receiver |
| 5 | this run's refutation of closing-review blocker 2 | four fixtures with the fan on a different line from the quote |
| 6 | this run's first gov harness sweep | same as 4, and it read 0/0 and nearly shipped as an all-clear |

**The CLAIM direction — a correction that does not reach its sibling.** The adopter's: a phrase grep
returns zero while a sibling three lines down restates the same fact in its own words, so the
correction lands on one copy and the other survives. Their generalisation is the better one and is
recorded here in their words: **grep the SUBJECT of a claim, not its wording.**

**Why it is one class.** Both produce a result that is honest, reproducible, and about a population
nobody meant to measure. Neither leaves a symptom: the fixture passes, the grep is empty, the sweep
is green. The only defence either session found is to state the population first and check the probe
reaches it — same field count, same element position, same line, same file set — before believing a
null result. A null result is a claim and owes the same evidence a positive one does.

**And the most expensive instance was not a fixture at all.** Closing-review round 1 prescribed
deleting `renderCodeView`'s block-comment branch. This run shipped the smaller repair instead —
widening the unterminated flag — and it PASSED everything: all 29 acceptance shapes, the 99-arm
suite, and the blocker harness written for round 1. Round 2 then measured the one shape it cannot
reach. A repair that passes every test you have is indistinguishable from a correct one until
somebody builds the test you did not, which is the argument for taking a review's prescribed fix
rather than the cheaper one that satisfies its evidence.

## 10. The first full bar came back RED, and what the seven legs were

`GATE_FULL=1 GATE_SELFTESTS=1` on `addc6169`: **RED, 7 of 86**. Recorded because a build record that
only ever shows greens is not evidence of a bar, and because two of the seven are worth more than
their fix.

**Four attributable to this build.**

| leg | what it caught |
|---|---|
| `memory hygiene` check 21 | the measurements record wrote `**Serves:** build …`, and `build` is not a record KIND — the set is spec-audit / diff-review / journal / research. The closing review's Serves also named `TOOL-aLexedStripper-7`, a BACKLOG row rather than a unit, so no spec H1 defines it |
| `build README slot contract` | a new build README naming no row in `readme-contract.txt` "would escape the contract by existing" |
| `drift-audit records` | `non_terminal_specs_cited_by_product_source` grew 2 → 6, because the four specs were still SPECCED while the code already cited them |
| `install-prefix (shipped surface)` | see below |

**The install-prefix red is the ceiling-provenance class in a third disguise, and worth keeping.**
The waiver exempting `REGEN_CMD` is keyed by LINE NUMBER — `tools/codebase-map/map_lib.py:1244`. This
build's rewrite moved that line to 1387, the key stopped matching, and the leg red on a line nobody
touched, naming the exempted line rather than the stale key. A waiver keyed by POSITION expires
silently on any edit above it. Same shape as a ceiling derived from a cache-hit run and a fixture
that cannot reach its mechanism: a correct-looking artifact whose validity depends on a condition it
does not record.

**Three are contention, and all three say so in their own output.** `manifest-check self-test` timed
out at 4370 s, `check-wiring self-test` at 2320 s, and `run-gates evidence` failed after printing
`SKIP — the kill at 50s landed during startup (a full run here measured 125s) — the run never
reached its header, so the crash case went UNEXERCISED rather than failing`. The node carried a
second session's full bar and roughly 110 live processes throughout; an adopter session measured 89%
of one leg's wall clock as waiting rather than computing. The first two are ceilings sized on a quiet
machine. The third is different and harder: a fixture whose validity depends on wall-clock ORDERING,
which no ceiling raise can fix.

**One pre-existing repair rather than a waiver.** `memory/builds/aGradedDoorway/build/…-s3-cost-split.md`
carried no `Serves:` line and predates this build's BASE, so check 21 was red for every session, not
just this one. The binding line was added rather than left for the next run to trip over.

## 11. "It was contention" is a hypothesis, and two of them were tested

§10 called three RED legs contention artifacts. Two of those were killed at a ceiling, which means
they produced NO verdict at all — so "it would have passed" was a story, not a measurement, and it is
exactly the reassuring story a killed leg invites. An adopter session put the principle better than
this record had: **a green earned with ceilings OFF rests on strictly more evidence than a run where
a ceiling fired, because the legs a ceiling kills are precisely the ones nobody has measured.**

So both were re-run directly, unbounded.

| leg | in the bar | run unbounded |
|---|---|---|
| `check-wiring self-test` | killed at 2320 s, no verdict | **76 passed, 0 failed, exit 0** |
| `manifest-check self-test` | killed at 4370 s, no verdict | **PASS, 62 assertions, exit 0** |

That converts an assertion into a result for BOTH: neither leg has a defect, and both ceilings were
breached on a node carrying a second session's full bar and roughly 110 live processes. The bound is
what failed, not the thing bounded — and that is now measured rather than assumed, which is the whole
difference between this paragraph and the one §10 first wrote.

**The third RED is a different animal and no ceiling raise reaches it.** `run-gates evidence` kills a
nested run at a fixed 50 s expecting to catch it mid-run, and under load a full run took 125 s, so
the kill landed during startup and the crash case went unexercised. Its validity depends on
wall-clock ORDERING rather than on a budget. It announced its own skip, which is more than the two
ceilings did — a killed leg says nothing at all, and silence is the failure mode this repo's own
liveness rule exists to prevent.

**Why this belongs in a build record about two scanners.** The same shape has now appeared five ways
in one night: a ceiling derived from a run whose cache was alive, a waiver keyed to a line number,
a fixture that cannot reach its mechanism, a repair that passes every test that exists, and a leg
killed before it could answer. Each is an artifact whose validity depends on a condition it does not
record, and each reads as a result.

## 12. Both review loops exited NON-CONVERGENT

Moved here from the build README when that file was registered under the slot contract, which closes
the heading set at five. The narrative is the record's job; the README's is to be readable.

**The spec audit.** Round 1 confirmed 2 blockers, round 2 confirmed 2. The count did not strictly
fall, so M4 STOPS the loop and PROMOTES every surviving blocker to a unit — `-5` and `-6` are those
two. Round 1 refuted `-2`'s central design; round 2 then found that the FOLDS introduced two new
defects, one per unit, each moving a verdict in the direction its own §1 forbids. That is the loop
working. What it could not do is converge in two rounds, and the method says stop rather than keep
paying.

**The closing review.** Round 1 confirmed 2, round 2 confirmed 2, so it stopped too. M4 promotes
every blocker still STANDING and none stood: both were fixed and each fix is measured, so the
promotion set was empty. Recorded because an empty promotion looks identical to a skipped one.

**One round-1 finding was REFUTED by measurement** and did not survive into rev-2: the claim that no
unmatched `)` in lens prose denies at BASE. It denies in the multi-line array, which is the shape
every shipped harness writes; the report had run 17 one-line variants only.

**And one refutation of mine was WRONG**, which is the more useful half. Closing round 1's second
blocker was recorded refuted with a stated mechanism, on four fixtures. The mechanism was false and
the fixtures were the wrong shape — the verdict only moves when the fan sits on the SAME line as the
quote. Round 2 supplied one that does. That is the same fixture-shape error an adopter session made
three times the same night and that this build had warned them about, made here, in a review of a
security guard.

Precision was 0.28, 0.29, 0.65 and 0.69 across the four rounds. The two spec-audit rounds sit far
under the ~0.5 the charter names; the two diff-review rounds clear it. On this evidence the closing
review was worth more per agent than the spec audit, and the cheapest instrument of all was a peer
session asking whether a mechanism was really the mechanism.
