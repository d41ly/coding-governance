**Serves:** spec-audit TOOL-dMispairedQuote-3

# Spec audit round 3 — `TOOL-dMispairedQuote-3`, and the subject is again the FOLD

*Node d, 2026-09-01, round 3. The subject of this round is the FOLD: rev-3 is fresh prose nobody has
reviewed, written to close round 2's 2 blockers, 4 highs and 2 mediums. The two bug classes this
repo's checklist selects for a diff of this shape are `fold-text-is-unreviewed-surface` and
`amendment-leaves-its-other-half-standing`, and both were hunted first. Both landed, and this time
they landed in the same place: **each of this round's two blockers is the repair that closed one of
round 2's two blockers.** No code has been written; the spec is the PLAN and is audited as a design.
Units 1 and 2 were read as context and carry no finding of their own, though both blockers name a
collision that has to be settled in one of them. Every surviving finding was re-derived in this
worktree against `tools/hooks/agent-cap.js` at BASE `d65da7ab`, against a gate actually run, or
against the fold's own diff actually read.*

Reviewed subject, pinned at the blob actually read:

- `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md@ce46aa62478b8b1289ff253dab1b24bbeec9ff45`

Context read, not reviewed: unit 1 at rev-3, unit 2 at rev-3, and rounds 1 and 2 over this unit.

Round 3.

## Verdict: BLOCKED

Two confirmed blockers, two highs and two mediums, presented as 6 rows over 12 confirmed findings.
Round 2 confirmed 2 blockers and set this round's ceiling at 2. Two is not strictly fewer than two,
so **the loop does not re-arm** and this is its exit — the disposition is at the bottom of this
record and it is binding, not advisory.

**What the fold got right, first, because it is more than last round.** Round 2's blocker 1 was a
real contradiction between two rev-2 sentences and rev-3 resolves it the harder and better way: S2
now says "**No rule's LOGIC changes**", owns the rename in five places, and enumerates the five reads
by line. Round 2's blocker 2 was a property arm sweeping a population with no instance of its class,
and rev-3 gives it real instances by shipping a fixture set. Round 2's row 3 is closed outright —
AC10's observed-RED quantifier now covers S10's byte arm and names the perturbation. Round 2's row 5
asked for `.lexicon.conf` in Files touched and got it, with the pin move owned in S6 rather than
merely asserted. Round 2's row 6 relabelled AC1 to rule 2 on a measurement rather than on the cap-50
in the fixture. That is four of eight rows moved substantively, and the two blockers among them were
moved by design changes rather than by rewording.

**And both of this round's blockers are those same two repairs.** S2's rename needed a check that the
rename actually happened, so the fold added AC12: `grep` the hook for the two old tokens and report
nothing. The hook carries sixteen occurrences of those tokens and only seven of them are the
definitions and in-rule reads S2 enumerates; the other nine are comments, and one of those comments —
`agent-cap.js:305` — sits INSIDE the body S1 freezes verbatim and AC7 byte-compares against the BASE
blob. AC7 and AC12 cannot both pass. That is blocker one, and it is the exact question round 2's row
8 asked and rev-3 did not answer: whether the byte comparison covers comments. An unanswered
ambiguity became a contradiction.

Blocker two is the fixture set. S9's fixtures are declared SHIPPED and land under `tools/hooks/`,
which is a kit home whose descriptor claims files by a literal include list — so `govkit selfcheck`
reds on every tracked file no rule claims. I staged one probe file there and ran the leg: one FAIL,
by name. That leg is `subject = repo` with no guard, so it reds on the ORDINARY bar the moment the
directory is tracked, not at the Definition of Done. A tracked rule-5 fixture also enters
`review-join ban`'s population, which is every `.js` under `tools/` and has no harness-marker filter.
Neither leg appears in §7, neither remedy appears in §4, and the cheap escape — ignoring the
fixtures — puts the population back where round 2's blocker found it.

**The lesson of this round is not that the fold was careless.** It was the most careful fold in this
build: it took the harder option on both blockers and it measured AC1 instead of arguing about it.
The lesson is narrower and it is why the loop is ending here rather than running a fourth time.
**Every repair in this build has been checked against the finding it answers and against nothing
else.** AC12 was checked against S2 and not against AC7 two bullets above it. The fixture set was
checked against S9's population and not against the two repo-subject gates that enumerate the
directory it lands in. That is the same failure at one more level of remove than round 2's "the
headline survived and the measurable half did not", and no further round of the same review closes
it, because the defect is in what the fold is compared against, not in how well it is written.

## Review shape

- raw 19 · confirmed 12 · refuted 7 · unverified 0 · precision 0.63
- confirmed by severity, as adjudicated in this report: 2 BLOCKER · 2 HIGH · 2 MEDIUM, over 6 rows
- confirmed blockers: 2 · confirmed highs: 2
- precision rose across the three rounds — 0.48, 0.53, 0.63 — over a shrinking raw count, which is
  what a hardening surface is supposed to look like and is worth recording against §8's own
  "past ~25 agents returns diminish" tuning note.

## What was re-derived, and how

Every figure and anchor below was measured in this worktree, and the working file's hash equals the
pinned blob `ce46aa62`, so the spec read is the spec pinned.

| claim | how it was checked | result |
|---|---|---|
| the two old tokens' occurrences | `grep -n` over the hook | **16** — 2 definitions, 5 in-rule reads, **9 comments** |
| where the definitions are | the same grep | `:70` and `:601` |
| the five in-rule reads | the same grep | `:84` `:356` `:681` `:977` `:1004` — S2's list is right |
| the nine comment occurrences | the same grep | `:247` `:257` `:259` `:266` `:277` `:305` `:970` `:990` `:1001` |
| `renderCodeView`'s span | `grep -n '^function'` plus `sed -n '344,352p'` | `:287`-`:348` |
| whether `:305` is inside it | `sed -n '300,310p'` | **yes** — it names `stripStrings` and ends "and so does this now" |
| unit 2's assignment to that comment | unit 2 §2 S4 and §6 AC3 | rewrites it; the phrase must be ABSENT |
| landing order | the three status headers | unit 1 `order 1` · unit 3 `order 2` · unit 2 `order 3` |
| unit 1's suite floor | unit 1 §6 AC7 at `:241-242` | "0 failed and a pass count strictly above 105" |
| the P1 verb census | `python tools/lexicon/lexicon.py --check` | `graded=1012 offenders=463`, `lexicon OK` |
| the drainable rows | `python tools/lexicon/lexicon.py --list` | **4** — both names at `:70`/`:601` in BOTH copies |
| the pin | `.lexicon.conf:158` | `VERB_OFFENDER_PIN="463"`, shrink-only |
| what the js probe grades | `tools/lexicon/lexicon.py:109-117` | `function NAME` and `const\|let\|var NAME = (…) =>`; `let VIEW_MODE` is ungraded, indented consts are not |
| the tracked corpus | `git ls-files \| wc -l` | **1266** — §4's Measured row says 1265 |
| the printed truncation | `grep -n 'slice(0, 6)'` | `:1091` `:1111` `:1129` `:1164`, all four rules |
| `main()`'s rule order | `sed -n` over `:1080`-`:1168` | fan-out `:1085` before cap `:1105`, so AC1's relabel holds |
| govkit check 7i's predicate | `tools/govkit/govkit.py:1599-1622` | per-file, skips only `kind = "flat"`; `tools/hooks/kit.toml` declares no `kind` |
| that home's claim rules | `tools/hooks/kit.toml` | seven literal `[[files]]` includes, no `**`, and its own comment says selfcheck reds on any unclaimed file |
| any exemption covering it | `tools/govkit/registry.toml` | none under `tools/hooks` |
| the red itself | staged one probe `.js` under `tools/hooks/`, ran the leg, restored | **1 FAIL**, naming the file; `git status` clean afterwards |
| that leg's scope | `tools/gate-legs.json` | `govkit selfcheck` — `subject = repo`, **no guard** |
| `review-join ban`'s population | `tools/workflows/check-review-join.sh:55-56` | every `^tools/.*\.js$`, cached AND others, minus a 4-path SELF_EXCLUDE, **no marker filter** |
| `verifier fan-out`'s population | `tools/workflows/check-verifier-fanout.sh:44-53` | same population, but skips a file with no `export const meta` |
| that gate's own precedent | `tools/workflows/check-verifier-fanout.sh:32-35` | its fixtures live under `mktemp -d` because "a fixture that lands in the repo would otherwise make the merge bar permanently red" |
| §7's self-test claims | `tools/gate-legs.json` | `subject = kit` · `chunk = selftests` · guard `tools/hooks/` · ceiling **740** — every §7 claim holds |
| memory hygiene | `bash tools/memory-tree/check-memory-hygiene.sh` | exit 0, one reported-not-gated check-16 note unrelated to this build |
| **the fold itself** | `git diff 47067d68 HEAD` over the spec | S1, S4, S10 and §3's last non-goal are **untouched** |

That last row is the one to read twice. It is how the priorFinding table below is answered from bytes
rather than from the revision log, and it is what disproves the revision log's own count line.

## Round 2's eight rows — closed, or reworded?

The mandate for this round is that a priorFinding is CLOSED rather than reworded. Four of eight are
closed. Round 1's fourteen rows are not re-tabulated: round 2 established that its residue is carried
entirely by these eight, and nothing in rev-3 reaches past them.

| round-2 row | what rev-3 did with it | status |
|---|---|---|
| **1** BLOCKER — dispatcher justification vs lexicon drain | took option (b): S2 owns the rename, enumerates the five reads by line, and restates the claim as "no rule's LOGIC changes" | **CLOSED** — and its new check is this round's row 1 |
| **2** BLOCKER — property arm over a population with no instance | S9's population gains a shipped fixture set, seeded by the three reproductions | mechanism **CLOSED** — and the fixture set is this round's row 2 |
| **3** HIGH — byte arm outside AC10's quantifier | AC10 now reads "each arm from S8, the property arm from S9 **and** the byte arm from S10", and names the one-byte perturbation | **CLOSED** (the "names which body drifted" clause was not taken; noted below, not filed) |
| **4** HIGH — pass floor below what the previous unit guarantees | the comparator moved from "at least" to "STRICTLY GREATER"; the baseline the row was about stayed 105 and the addition was again dropped | **REWORDED, NOT CLOSED** (row 3) |
| **5** HIGH — `461` unreachable, pin move unowned | pin half **closed**: S6 lowers the pin explicitly and `.lexicon.conf` joins Files touched. Figure half: the number was retyped and given a new explanation that does not produce it | **HALF CLOSED** (row 4) |
| **6** HIGH — AC1 keeps the exit code, and its fixture denies through another rule | relabelled to **Rule 2** on a measurement, with the reason; the message clause the four siblings carry was attached to the BASE observation, not to the candidate's criterion, and S8's label was not touched | **HALF CLOSED** (row 6) |
| **7** MEDIUM — merge key taken, merge ORDER dropped | S4 is byte-identical to rev-2 | **NOT ADDRESSED** (row 5) |
| **8** MEDIUM — byte-frozen body carries the comment unit 2 lands last to rewrite | S1, S10 and §3's last non-goal are byte-identical to rev-2; AC12 was added and makes the unanswered question a contradiction | **NOT ADDRESSED, AND ESCALATED** (row 1) |

**The revision log's count line is wrong, and it is checkable.** The rev-3 entry opens "folded
spec-audit round 2 over this unit: 2 blockers, 4 highs, 2 mediums", then enumerates two blockers and
four highs and names no medium. The diff confirms why it names none: neither medium's carrier moved a
byte. A fold log that counts a fix nobody made is the same defect class as an acceptance criterion
that observes nothing, one document over, and it is the reason this table had to be built from the
diff rather than read out of §9.

## Findings

| # | Sev | Address | One line |
|---|---|---|---|
| 1 | BLOCKER | §6 AC12 vs §6 AC7 · §2 S1/S2/S10 | the fold's new totality check and its byte-freeze cannot both pass |
| 2 | BLOCKER | §2 S9 · §4 Files touched vs §7 | the shipped fixture set reds two unguarded repo-subject legs the spec never names |
| 3 | HIGH | §6 AC8 vs unit 1's AC7 · §4 Measured | the pass floor is entailed by the previous unit's landing and observes no arm of this one |
| 4 | HIGH | §2 S6 · §4 Measured · §6 AC9 | `461` is two offenders above the arithmetic, and the new explanation explains a different number |
| 5 | MEDIUM | §2 S4 vs §5 observability | the merge ORDER is still unstated, so §5's operator promise is unsecured |
| 6 | MEDIUM | §2 S8 vs §6 AC1 | AC1 was relabelled on a measurement and S8 still carries the disproved label |

---

### 1 — BLOCKER — §6 AC12, against §6 AC7 and §2 S1/S2/S10

*Folds finder findings `#1`, `#6` and `#12`. This is round 2's row 8, arriving through the fold with a
new other half — `fold-text-is-unreviewed-surface` over a sentence that did not exist at rev-2.*

AC12 is new at rev-3 and it is the only check S2's census-free argument now rests on: run
`grep -n 'stripStrings\|blankLiterals' tools/hooks/agent-cap.js` and it must report **nothing**.

The file carries **sixteen** occurrences. Two are the definitions at `:70` and `:601`. Five are the
in-rule reads S2 enumerates at `:84`, `:356`, `:681`, `:977` and `:1004` — that list is correct and I
re-derived it. The remaining **nine are comments**: `:247` `:257` `:259` `:266` `:277` `:305` `:970`
`:990` `:1001`. S2 prescribes the mechanic as "one global substitution of two tokens", which rewrites
all nine.

One of those nine is fatal. `renderCodeView` spans `:287`-`:348`, and `:305` reads:

> `// The measured case is an apostrophe inside a regex literal, /won't/. `stripStrings``

S1 freezes that body verbatim as `renderShippedView`, and S10 and AC7 require it to equal its
counterpart in the BASE blob **byte-for-byte**. So: rename it and AC7 reds, along with the verbatim
guarantee that is this unit's entire safety argument. Leave it and AC12 reds, on a build that did
exactly what S2 specifies. AC12 greps the same file the frozen body lives in, so there is no scoping
escape, and "byte-for-byte" forecloses reading "body" as executable-code-only.

Three further facts make this worse than an ambiguity.

**The blind rename produces false statements.** Eight of the nine comments describe the shipped
per-line blanker, not a dispatcher. `:259` — "`stripStrings` (line 70) blanks" — becomes a sentence
about a function at a line that no longer holds it. `:266` — "`blankLiterals` cannot be that view" —
becomes an assertion about a dispatcher that blanks nothing. A global `sed` converts documentation
into fiction, silently, on a file whose comments are its recorded provenance.

**AC7 has no extraction contract even before the comments.** The frozen bodies necessarily carry new
signature lines (`function renderShippedLine(line) {` where BASE has `function stripStrings(line) {`),
so "compared byte-for-byte with its counterpart" already presumes a definition of which lines
constitute the body and whether the signature is in it. No S-item supplies one. Round 2's row 8 asked
for exactly this clause — "either answer works, but it must be written, because AC7 is unanswerable
without it" — and rev-3 answered it with a criterion that contradicts it instead.

**Unit 2 lands last on the same six lines.** Unit 2's S4 is assigned to rewrite the `:301`-`:306`
comment and its AC3 requires "and so does this now" to be ABSENT; unit 2 is `order 3` against this
unit's `order 2`. So at unit 3's Definition of Done that occurrence must still exist — and after unit
3 lands it exists twice, once in each copy of the body, with nothing saying which copy unit 2 edits.

The implementer's cheapest exit is to quietly narrow or drop AC12, which restores the hand-kept census
S2 exists to abolish and which has now been measured wrong in three consecutive rounds.

**Fix.** Four clauses, and this fold is terminal, so all four have to land together.

1. Settle the extraction contract in S10 and AC7 in one sentence: the byte comparison covers the
   EXECUTABLE lines of each body, signature and comments excluded, and name how the arm delimits them.
2. Restate AC12 over that same scope. Grep with comment lines stripped, or better, drop the
   grep-for-absence entirely and assert the property S2 actually wants: **each of the five reads at
   `:84` `:356` `:681` `:977` `:1004` resolves to a dispatcher name.** That is what round 2's row-1
   left-shift asked for, it does not depend on prose, and no grep-for-absence can give it.
3. Add one S-item listing the nine comment occurrences by line, saying which are rewritten by hand and
   which stay. They describe the shipped per-line blanker; a global substitution makes them untrue,
   and `:990`/`:1001` sit inside rule 5 where S2 permits only a callee-name edit.
4. Say in §3 that comment prose naming the old views is out of this unit's scope and belongs to unit
   2's carrier list, and add to §3 that unit 2's list is re-derived against the post-unit-3 file,
   naming which carriers now exist twice and which copy each correction lands on. Extend whatever
   replaces AC12 to `.claude/hooks/agent-cap.js` too, since S7 mirrors every byte and that is the copy
   the tool call actually runs.

**Left-shift gate.** Two, and the second is the one this build has now earned three times over.
In `tools/hooks/agent-cap.test.sh`, an arm that derives each rule function's view calls from the
source and asserts every one resolves to a dispatcher — a census the file keeps about itself, so the
next repair cannot leave a read behind and no criterion has to enumerate them by hand. And the
binding-level check round 2 already proposed, which would have caught this at planning time:
`gen_build_index.py --print-bindings` already reads every record's bytes, so it can red when two units
in one build claim the same file region with contradictory verbs — one freezing what another is
assigned to rewrite.

---

### 2 — BLOCKER — §2 S9 and §4 Files touched, against §7's gate list

*Folds finder finding `#13`. This is `fold-text-is-unreviewed-surface` over the repair that closed
round 2's second blocker.*

S9's fixture set is new at rev-3 and it is a good idea: it is what gives the property arm an instance
of the class it guards. It is declared SHIPPED, §4 places it "beside" `tools/hooks/agent-cap.test.sh`,
and shipping it means tracking it. Three shipped legs enumerate the directory it lands in and the spec
names none of them.

**`govkit selfcheck` reds first, and I reproduced it rather than argued it.** I created one probe
`.js` under `tools/hooks/`, staged it, ran the leg's own argv, and got:

```
govkit: entry 'agent-cap' has 'tools/hooks/fixtures/probe-round3.js' under its home and no file rule
claims it — a file added inside a kit whose includes are a literal list is otherwise invisible to
the surface predicate, which is depth-1
govkit: per-file claim: 1 unclaimed file(s) under a non-flat home
```

One FAIL, by name. The tree was restored and `git status` is clean. Every precondition holds:
`tools/govkit/govkit.py:1599-1622` skips only `kind = "flat"` entries and `tools/hooks/kit.toml`
declares no `kind`; that descriptor's seven `[[files]]` includes are a literal list with no `**`, and
its own comment at `:32` already says "selfcheck reds on any tracked file here no rule claims"; and
`tools/govkit/registry.toml` carries no exemption under `tools/hooks`. In `tools/gate-legs.json` the
leg is `subject = "repo"` with **no guard**, so it reds on the ORDINARY bar the moment the directory
is tracked — not at the Definition of Done, and on every other session's bar as well as this one's.

**`review-join ban (no ref-keyed join)` reds second.** `tools/workflows/check-review-join.sh:55-56`
builds its population from `git ls-files --cached --others --exclude-standard -- '*.js'` filtered to
`^tools/.*\.js$`, minus a SELF_EXCLUDE naming only its own three files and `tools/hooks/agent-cap.js`.
There is **no harness-marker filter** — it feeds every match to the hook with `--only=join`. S8 says
"Rule 5 gets one too", so this unit ships a fixture that is a ref-keyed join by design. That leg is
also `subject = "repo"` and unguarded. `--others` means the red arrives before anything is staged.

`verifier fan-out` is the near miss worth stating precisely, because it is the half the spec could
still get wrong: `check-verifier-fanout.sh:44-53` builds the same population but scans a file only
when it exports `const meta`. A plain fixture is skipped — but the spec nowhere states that its
fixtures lack that marker, so the exemption is luck rather than design. That same file records the
precedent in-source at `:32-35`: today's fixtures live under `mktemp -d` because "a fixture that lands
in the repo would otherwise make the merge bar permanently red". This unit proposes to do the thing
that comment exists to prevent.

§7 lists neither `govkit selfcheck` nor `review-join ban`, and §4's Files touched lists neither
`tools/hooks/kit.toml` nor either workflow gate. So a build that follows this spec lands a red
ordinary bar with the remedy unstated — and the remedy is a genuine spec decision, not an oversight
the implementer can improvise, because "shipped" needs `[[files]]` rules with destinations and those
destinations decide what adopters receive. The cheap escape is worse: ignoring the fixtures takes the
population local-only, adopters who copy-install the kit never receive it, and the property arm is
back to a corpus with no instance of its class, which is round 2's blocker restored exactly.

**Fix.** State the fixtures' full contract in S9 rather than "a directory the arm globs": the path,
that they are TRACKED, and the declarations that keep the bar green. Then pick one of two routes and
write it down.

- **Declare them.** Add `tools/hooks/kit.toml` to §4 Files touched with one `[[files]]` rule per
  fixture — a `**` include is the alternative and changes what adopters receive, so decide it
  explicitly — or a `[[exempt]]` in `tools/govkit/registry.toml` with its reason. Add the directory to
  SELF_EXCLUDE in both `tools/workflows/check-review-join.sh` and
  `tools/workflows/check-verifier-fanout.sh`, and list both files in §4.
- **Or give the fixtures a non-`.js` extension.** That sidesteps both JavaScript gates and the lexicon
  probe in one decision, which also disposes of half of row 4, and is probably the cheaper answer.
  S9's arm feeds file CONTENT to the hook, so the extension is not load-bearing for the property.

Either way, add `govkit selfcheck` and `review-join ban (no ref-keyed join)` to §7.

**Left-shift gate.** An arm asserting that every path the property arm globs is claimed by a kit file
rule and excluded by both JavaScript gates, so the next fixture directory cannot land silently red.
The spec-level companion, which this build has now earned: a `TEMPLATE-SPEC` check that a scope item
introducing a TRACKED file under a kit home names that kit's descriptor in §4 Files touched.

---

### 3 — HIGH — §6 AC8, against unit 1's AC7 and §4 Measured

*Folds finder findings `#3` and `#7`. This is round 2's row 4 and round 1's H3 — the same defect,
reworded twice.*

AC8's amended floor is "0 failed and a pass count STRICTLY GREATER than 105". Unit 1's AC7 at
`:241-242` already requires "0 failed and a pass count strictly above 105, the count recorded at
BASE", and unit 1 is `order 1` while this unit is `order 2`. The two sentences are the same bar. AC8
is therefore entailed by the previous unit's landing and observes nothing about any of this unit's
seven arms: S8's five, S9's one, S10's one could all be written and never invoked, or de-collected
later, and AC7, AC8 and AC11 stay green together. The harness exits on the fail count alone, so a
de-collected arm set lands green.

AC8's own justification is keyed to a number that no longer exists when AC8 is evaluated: "A unit
adding S8's five arms plus S9 and S10 cannot leave the count where it was" is true and is an argument
for an arithmetic the criterion does not contain. Round 1's H3 asked for the addition. Round 2's row 4
asked for the addition and named the terms. The fold moved the comparator and dropped the addition
both times. A criterion rewritten twice to prevent green-by-absence still permits it.

§4's Measured row was relabelled — "shipped suite, candidate WITHOUT this unit's new arms | 105 passed
/ 0 failed, the same count as BASE" — and the relabel names which ARMS are excluded without saying
which unit's CODE is in the tree. Under the reading that matches the landing order, a candidate
carrying unit 1 carries unit 1's arms and cannot report the same count as BASE without violating unit
1's AC7 on its face.

**Fix.** Write the arithmetic and the literal into AC8: unit 1's landed pass count, plus 5 for S8,
plus 1 for S9, plus 1 for S10, with the expected integer stated. If the integer genuinely cannot be
fixed before the build, "at least 7 above the count this tree reports immediately before this unit's
arms are added" is still a criterion an unwired arm fails, and it is better than a number keyed to the
wrong unit. Correct §4's Measured row to the count the built candidate produces, or say in the row
that the measurement is unit-3 code on BASE with neither unit's arms present.

**Left-shift gate.** Round 1's, round 2's, and now round 3's: a `PASS_FLOOR` constant in
`tools/hooks/agent-cap.test.sh` that the runner asserts against its own final count and that each
arm-adding commit raises. It makes de-collection impossible to land silently rather than merely
discouraged, and it moves the floor with the suite instead of with a number typed into a spec — which
is §6's "a value stated in prose beside the source that OWNS it rots", applied to an acceptance
criterion. Three rounds have now asked for it in prose. Prose is not what fixes it.

---

### 4 — HIGH — §2 S6, §4 Measured and §6 AC9, against §2 S9 and §10

*Folds finder findings `#2`, `#8`, `#14` and `#17`. This is round 2's row 5, whose figure half came
back with a new explanation instead of a new measurement.*

Measured here at BASE: `--check` reports `P1 verb graded=1012 offenders=463` and `--list` shows
exactly **four** drainable rows — `stripStrings` and `blankLiterals` at `:70`/`:601` in BOTH
`tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js`, which S7 mirrors byte for byte. S6 bolds
that "**Every name this unit introduces leads with a verb the lexicon declares**", §10 records nine
`--suggest` consults all answering OK, and unit 1's two helpers answer OK as well. A build honouring
S6 therefore drains 4, adds 0, and measures **459**. S6, §4 and AC9 all say **461**.

Rev-3's new reconciliation is the part that has to go: "It is NOT `463 - 4`: the candidate also adds
definitions the leg grades, and `graded` moves 1012 to 1032." `offenders` is a count of OFFENDING
definitions and is a subset of `graded`. Conforming additions move the denominator and leave the
numerator alone. The sentence explains a number nobody disputed and does not touch the one in
question.

The `graded` figure does not close either. The probe grades `function NAME` and
`const|let|var NAME = (…) =>`; `let VIEW_MODE` is ungraded. §2 and §10 between them introduce ten
definitions per copy where BASE has three, so +7 per copy and +14 for the pair, plus unit 1's +2 per
copy is +18 — landing on 1030, not 1032. Both gaps are 2, in the same direction, which is what a pair
of unenumerated definitions looks like: one per copy, and offenders.

So one of two things is true and neither is acceptable as written. Either 461 is wrong, and AC9's
exact equality reds a conforming build at 459 while `VERB_OFFENDER_PIN` sits two above the corpus.
Or 461 is right, two definitions this unit introduces are verb offenders, S6's bolded universal is
false, §10's nine consults do not cover them, and lowering the pin to 461 ratchets two unattributed
offenders into the corpus permanently — with no drain entry, which `.lexicon.conf`'s own convention
requires and demonstrates at `:116-157`. AC9 forbids exactly that in its own last clause: "no headroom
this unit did not earn."

One narrowing, in fairness to the fold: `lexicon.py:697` reds only when offenders EXCEED the pin, so a
459 outcome leaves the leg GREEN and fails AC9 rather than redding the bar. That bounds the blast
radius; it does not make the criterion satisfiable.

**And the fold created a second exposure it did not join.** The lexicon corpus is every tracked file
and `.lexicon.conf:23` declares `js:js-regex:probe`, so S9's tracked fixture directory — new at rev-3
— is GRADED. The 461 was measured "with the candidate in both copies", on a tree that predates the
fixtures. This repo already records the class: `memory/gotchas/pin-copied-from-another-corpus.md`. The
corpus has moved underneath the figure once already — `git ls-files` reports 1266 today against §4's
1265 — which is the general form of the same problem.

**Fix.** Show the arithmetic in S6 as `463 − 4 drained + N introduced` rather than as a bare pair of
measured totals, and name the definitions behind any N above zero. State in S6 and S9 whether
fixture-script identifiers are inside or outside "every name this unit introduces", and why — if they
must define nothing the probe grades, write that as the constraint and give it an arm. Then either
re-measure over a tree that carries the fixture directory and publish that figure in S6, §4's Measured
row and AC9, or keep 461 and name the two permitted offenders by identifier so a third cannot arrive
under the same number. Consider replacing AC9's exact integer with `offenders <= VERB_OFFENDER_PIN`
plus the drain COUNT of 4, so the criterion survives a corpus that moves for unrelated reasons before
landing — which it demonstrably does. Add the `.lexicon.conf` drain entry to AC9 as round 2 asked;
rev-3 kept the number and dropped that clause.

**Left-shift gate.** A `TEMPLATE-SPEC` check that a spec publishing a figure about a gate leg names
the command AND the tree state it was measured on. The defect here is a number measured on one tree
and pinned against another, twice, and a figure with no stated corpus cannot be re-derived by the next
reader — which is the only thing that would have caught it in round 2.

---

### 5 — MEDIUM — §2 S4, against §5 observability

*Folds finder finding `#5`. This is round 2's row 7, unaddressed: S4 is byte-identical to rev-2 and
the revision log counts it as folded.*

S4 states the merge key `(n, why)` and no ordering, and no criterion in §6 observes a merge collision:
AC1-AC5 are single-fixture single-message arms, AC6 and AC10 observe exit codes and REDs, AC7 and AC12
observe bytes and greps. S3's own description — run lexed, flip, run shipped, merge — puts lexed rows
first.

Widening the key makes the exposure worse rather than better, which is the part worth keeping. Under
an `n`-only key a colliding pair had one row displace the other; under `(n, why)` both survive, so a
colliding line contributes two rows to the printed list. All four rules print only `slice(0, 6)` —
verified at `:1091`, `:1111`, `:1129` and `:1164` — so on a script with several findings the shipped
row can be pushed out of the printed set. §5 then promises what the design does not secure: "a finding
reported from the shipped pass carries that view's own explanation, which is the message an operator
sees today." If the row is not printed, the operator does not see it. No non-goal covers this — §3
excludes regex modelling, view removal, false-positive reduction and unit 2's carrier list.

**Fix.** State the tie-break in S4 beside the key: shipped-pass rows are emitted first, so a collision
cannot push the status-quo explanation out of the six printed.

**Left-shift gate.** The arm rounds 1 and 2 both specified and neither fold took: over a line carrying
two helper calls, assert both explanations reach stderr; over a line both views flag, assert the
SHIPPED `why` is in the emitted text. The pair distinguishes a merge that preserves the
operator-facing message from one that merely does not crash.

---

### 6 — MEDIUM — §2 S8, against §6 AC1

*Folds finder finding `#9`. This is `amendment-leaves-its-other-half-standing` in its textbook form —
one fixture, two rule labels, in one document.*

AC1 was relabelled at rev-3 from rule 3 to **Rule 2** on a measurement, with the mechanism stated:
`main()` runs `fanoutFindings` before `capFindings`, which I re-verified at `:1085` and `:1105`. S8
describes the same fixture — "the backtick-inside-a-regex script above a multi-line cap-50 call" — and
still labels it "**(rule 3)**". The revision log names the AC1 relabel explicitly and S8 was not
touched.

S8 is where the arm inventory is stated, so with the stale label it claims two rule-3 arms and one
rule-2 arm; the true split is one rule-3 arm (AC2) and two rule-2 arms (AC1, AC4). An implementer
budgeting coverage per rule from S8 believes rule 3 is doubly covered when the shape they wrote for it
can never reach rule 3. S8's closing claim — "Rule 5 gets one too, so no rule is covered only by the
property" — does survive the correction, so this is a misleading census rather than a coverage hole,
which is why it is a medium.

There is a second half of round 2's row 6 still standing. AC1's message clause is scoped to the BASE
run — "at BASE this fixture denies through the verifier-arity rule, naming `agent() fanned over`" —
while AC2 through AC5 assert the message on the CANDIDATE run. AC1's own criterion clause is still
three exit codes and no message, which is what round 2's row 6 was filed to fix.

**Fix.** Relabel S8's first arm "(rule 2)" with the one-clause reason AC1 now carries, and add that
rule 3's only arm is AC2's regex-borne `)` shape. Give AC1's candidate run the message clause its four
siblings have.

**Left-shift gate.** The arm round 2 proposed for its row 6 and this row re-earns: assert that every
rule in `main()` has at least one message-asserting arm naming its own banner text, derived from the
source rather than from a list, so a sixth rule added later reds until it is covered. The harness
already has the helper — `msg()` in `tools/hooks/agent-cap.test.sh` — under a header written after a
retired arm passed on a fixture that tripped a different rule. That is this exact trap, and it has now
appeared in a criterion, in a scope item, and once in the suite itself.

## Not filed

Four observations that no finder confirmed or that are too small to be rows, recorded because the
disposition below is terminal and nobody reviews the final fold.

- **S9's output shape is still unstated**, which round 2 also flagged and did not file. If the
  property arm emits one `ok` per file the suite's pass count jumps by more than 1200 and every floor
  argument in row 3 changes shape. Settle it in S9 in one clause while fixing row 3.
- **AC10's "names which body drifted" clause was not taken.** AC10 now covers the byte arm and names
  the perturbation, which is the substantive half; a byte arm reporting only "unequal" over three
  functions costs the reader the diff. One clause, while §6 is open anyway.
- **AC12 is placed between AC10 and AC11**, and the revision log runs rev-1, rev-3, rev-2. Neither
  breaks a TEMPLATE-SPEC rule. Both are the signature of a criterion appended at the end of a fold
  without re-reading its neighbours, which is precisely how row 1 happened: AC12 was checked against
  S2 and never against AC7 two bullets above it.
- **§4's corpus figure is already stale** — 1265 in the spec, 1266 tracked today. Harmless in itself,
  and the general form of row 4's second half.

## Exit — the loop does not re-arm, and the disposition

Round 1 confirmed 5 blockers. Round 2 confirmed 2 and set this round's ceiling at 2. This round
confirms **2**. `BUILD-METHOD.md` M4 re-arms the loop only on a confirmed-blocker count STRICTLY
SMALLER than the one before, and 2 is not smaller than 2, so **this is the exit**. There is no round
4, and per M4 every blocker still standing is DISPOSED here rather than parked, waived or
re-reviewed.

**Both blockers are FOLDED, not promoted.** Each is a defect in a document this review read, each has
a fix written above in terms the implementer can execute without a new mechanism, and both terminate.
Neither needs a capability this build lacks. Concretely:

- **Row 1** folds into S1, S2, S10, §3 and §6 — the extraction contract, AC12 restated over call sites
  rather than file text, the nine comment occurrences enumerated with a per-line disposition, and the
  unit-2 hand-off made per-copy. Rows 1 and 6 both touch §6 and should be one pass.
- **Row 2** folds into S9, §4 Files touched and §7 — the fixtures' declaration contract, or the
  non-`.js` extension that disposes of it and of half of row 4 at once. Decide the extension FIRST:
  everything else in rows 2 and 4 is downstream of it.
- Rows 3 and 4 are one pass over §6 and §2 S6. Rows 5 and 6 are one clause each.

**The fold that closes this loop is unreviewed by construction, and that is the risk to state plainly
rather than dress up.** Three rounds have now shown the same pattern: each repair is checked against
the finding it answers and against nothing else, and the next round's blockers are in the repair. The
mitigation is not another round of the same review — M4 forecloses it and it would find the same class
again. It is the two left-shifts above that convert this build's recurring census problems into arms
the suite keeps about itself: the per-read dispatcher assertion in row 1, and the `PASS_FLOOR`
constant in row 3. Both are small, both are in `tools/hooks/agent-cap.test.sh`, and both have now been
asked for by every round of this audit. Build them in this unit rather than recommending them again.

**One thing to carry to the build README's build-level rules slot**, because it outlives this unit:
this build's own record shows that a spec's acceptance criteria have never once been re-read against
each other after a fold. Row 1 is what that costs. A fold pass that ends by reading §6 top to bottom
as a set — not as a list of answered findings — is a five-minute step and it would have caught row 1,
the AC12 placement and row 6 in one sitting.
