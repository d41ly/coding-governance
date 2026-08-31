**Serves:** spec-audit TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

# Spec audit round 4 — the same seven units at rev-4, and the fork resolution attacked on its own terms

*Node a, 2026-08-31, round 4. Rounds 1, 2 and 3 returned BLOCKED with 7, 5 and 4 blockers. rev-4 is
not an amendment: round 3 proved that no test over a declined slash's span can classify it — without
a closure test there are false positives, with one there are false negatives on an identical shape —
so rev-4 RETIRES the leak test and resolves the fork in `TOOL-aPairedLexer-8` §8 F1 to option (c),
reporting AMBIGUITY. This round therefore aimed first at the resolution itself, on the five questions
the fork raises: whether the new condition catches every fail-open the retired tests were chasing,
whether the re-baselined `-6` AC6 verdict is correct, how large the false-deny class actually is when
measured rather than asserted, whether anything still references the retired machinery, and M2
agreement at rev-4.*

Reviewed at these blobs, all seven verified to match the pinned addresses at HEAD `20ae25b7`:
`memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-6.md@a0ccff020238` ·
`…-7.md@74004d4936cc` · `…-8.md@7b2f776ce447` · `…-9.md@262e172980e0` · `…-10.md@6ea040323f3b` ·
`…-11.md@f49583463fe7` · `…-12.md@d5bea51debf3`. Round: **4**.

## Verdict: BLOCKED

The counts sit here rather than on the heading, because that line's token is a closed set and a tally
appended to it turns a structural check into a semantic one.

**5 blockers and 3 highs stand, and BUILD-METHOD M4's convergence test FAILS.** M4 re-arms the loop
only when the confirmed-blocker count is strictly smaller than round 3's 4. It is not. Counted the
way rounds 2 and 3 counted — distinct defects by owner and mechanism, duplicate finder rows
consolidated rather than padded out — round 4 stands at **5 blockers over 24 upheld finder rows**.

**Both counting bases were computed, and they agree on the ruling.** The contested consolidation is
whether the two retirement non-folds (one in `-8`, one in `-6`) are one defect or two: they share a
mechanism but have different owners and need two separate edits, which is why this report counts them
as two. Merged into one, the total is **4**. Round 3's own precedent supports splitting — it counted
B1 and B2 as two blockers at the identical address (`-8` §2 S3) because the mechanisms differed,
while folding `-9` AC4 and AC7 into a single row because the mechanism was shared. Either way,
**5 ≥ 4 and 4 ≥ 4**, so the ruling does not depend on the contested call: **the loop STOPS, and every
standing blocker is PROMOTED and BUILT AS SPECCED.**

That ruling is stated plainly because its consequence is severe. Two of the five blockers below are
fail-opens — one measured DENY→ADMIT, one measured under-specification whose wrong branch permanently
degrades this repo's own Tier-2 review harness — and promoting them means they are resolved in the
BUILD rather than in a rev-5. They are not spec-prose defects that a builder can route around.

**The relocation rate, which round 3 named as the number to watch, is worse than the headline.** Of
round 3's four blockers, two are genuinely closed (B1 and B2, both dissolved by retiring the leak test
outright), one is closed (B4, restated as an honest builder obligation), and one is NOT closed but
RELOCATED WITHIN ITS OWN SECTION: round 3's B3 named `-9` AC4 *and* AC7, and rev-4 amended AC4 only,
while the amended AC4 acquired a fresh defect of its own. Round 3's H1 closed one of its four
addresses. Worse, **two of this round's five blockers did not exist before rev-4** — they are
properties of the new S2 and S3 text, authored by the edit that was supposed to close the fork. The
fold resolved the fork and left every consumer of the retired design standing.

## Review shape

Raw 32 · confirmed 25 · refuted 7 · unverified 0 · precision 0.78.

Adjudication on top of that: of the 25 confirmed rows, **24 are upheld and 1 is refuted here on a
run** (see "Refuted in adjudication" below), and **1 new high was raised by this round's own
measurement** while answering attack (a). The 24 upheld rows consolidate to 5 blockers and 2 highs;
with the new finding, 3 highs.

## The five attacks, answered

**(a) Is "declined slash plus a later slash on the same line" sufficient? PARTLY — and the miss is on
the side nobody was watching.** On the DECLINE side the condition is sufficient, and the hypothesis in
the brief is refuted: a declined slash whose leaked opener is the last thing on its line with no later
slash cannot occur in runnable JavaScript, because a regex literal cannot contain a line terminator,
so a mis-declined regex opener always has its closing slash on the same line. I built both spellings
of that shape and `node --check` rejects both with `SyntaxError: Invalid regular expression: missing
/`. A script that cannot parse cannot fan out, so admitting it is harmless.

The real miss is on the ACCEPT side, and S3 cannot see it because S3 reports only on slashes it
DECLINES. `renderCodeView` sets `prev` to the closing quote after consuming a string, and a quote is
neither in `})]` nor a word character, so `"a" / 2` is ACCEPTED as a regex position. Measured:

```js
const x = "a" / 2; await parallel(D.map((d) => agent(d))); const y = "b" / 3
```

is valid JavaScript (`node --check` clean), and exits **0** against the shipped hook, against a copy
patched with `-8` S1+S2, and under the rev-4 ambiguity rule — while the bare
`await parallel(D.map((d) => agent(d)))` exits **2**. The first slash opens a "regex" that closes on
the second, blanking the raw primitive out of the view. There is no declined slash on that line, so
S3 announces nothing, `unterminated` stays false and `clean` stays true. This is raised as H3 below.

**(b) Is the re-baselined AC6 verdict correct? YES; the stated workaround is NOT.** The deny direction
is right and `-8` §8 corroborates it. But the one-character workaround `-8` §8 offers is false for the
class actually measured — see (c) and blocker B4.

**(c) How large is the false-deny class? It is decided by a sentence the spec does not contain, and
the two answers differ by the entire population.** I implemented S3's condition over this repo's own
tracked corpus under both readings:

| Reading of "a later slash" | tracked workflow scripts reporting AMBIGUITY |
|---|---|
| RAW line (any later `/` byte, comment introducer included) | **3 of 4** |
| code-mode TOKEN (slashes the scanner actually reaches) | **0 of 4** |

Under the raw reading the three are `tools/workflows/tier2-review.js:395`,
`tools/workflows/drift-audit-code.js:285` and `tools/workflows/drift-audit-state.js:297`, and in every
case the sole cause is one line of the hook's OWN mandated dialect:
`chunk(x, Math.ceil(x.length / MAX_VERIFIERS)) // gov:fixed-verifiers`. The declined division slash is
followed by the `//` of the marker comment that `fanoutFindings` requires on that same raw line. In
`tools/hooks/agent-cap.test.sh` the same shape appears in 4 arms of 111, of which exactly **one is an
ADMIT arm** (`rule2: bounded group count + marker → allow`, line 228); the other three already expect
a deny, so their exit codes do not flip.

So the measured cost is not "a legal script with two ordinary slashes on one line". It is the repo's
own mandated spelling, on the marked line of all three shipped harnesses, and the stated workaround
cannot reach it: `boundedBranch` requires the literal `Math.ceil(<id>.length / K)` and the marker rule
requires `gov:fixed-verifiers` on that same raw line, so neither "end the statement before the
ambiguous regex" nor "bind it to a name" is available.

**(d) Does anything still reference the retired machinery? YES, extensively — this is blockers B1 and
B2.** The rev-4 fold reached `-8` S3, S3-RETIRED and §8, and `-6` S3 and AC6, and stopped. Eight
clauses across the two documents still specify the retired opener set, leak set, extent test or
closure test.

**(e) M2 agreement at rev-4: FAILS on the interface axis and on the fork-state axis.** `-6` S1 spells
the interface "`TOOL-aPairedLexer-8` S3's LEAK report" five lines above `-6` S3 spelling it
"AMBIGUITY, not a leak" — one interface named twice, differently, inside one section. And `-6` §8, the
section M2 and M3 read to classify fork state, records the resolution "in the ADMIT direction" while
the criterion it names denies. Units 7, 11 and 12 hold no disagreement at rev-4; their only rev-4 diff
is the round-3 records row.

## Findings

Severity-ranked, blockers first. Each row names its address, the finder ids it consolidates, and the
consequence. Detail, fix and left-shift gate follow below.

| # | Severity | Address | Consequence | Rows |
|---|---|---|---|---|
| B1 | blocker | `-8` §6 AC7, with §3 bullet 3 and §10 final ¶ | §2 retires the leak/closure test and §6 mandates building it; S3 ships with no criterion at all | 1, 9, 15, 20, 26, 29 |
| B2 | blocker | `-6` §4 ¶2, with §5 risks, §8, S1 and AC5 | Two mutually exclusive routing conditions for the central mechanism, in the document that consumes it | 3, 8, 10, 14, 23, 24, 30 |
| B3 | blocker | `-8` §2 S3, with §8 F1's cost ¶ | "A later slash" is undefined; the two readings differ by the entire measured population, and the ratified cost is priced on the wrong one | 2, 12, 21, 25, 28 |
| B4 | blocker | `-8` §2 S2, with §6 AC4's negative table | `of`, `await`, `yield` are legal identifiers; a measured DENY→ADMIT authored by the unit whose job is closing one | 19 |
| B5 | blocker | `-9` §6 AC7, with AC4's replacement name | AC7's exemption has a null referent, so AC7 cannot pass; round 3's B3 relocated, not closed | 4, 32 |
| H1 | high | `-10` §4, §5, AC7 | Three of four round-3 addresses unchanged, and AC4 asserts a correction git refutes | 5, 11 |
| H2 | high | `-6` §6 AC1 | AC1's fixture is denied by rule 2, so rule 1's fallback has no criterion and "all four rules" is observable for three | 6 |
| H3 | high | `-8` §3 bullet 1 and §5's ceiling-paragraph line | A measured fail-open on the ACCEPT side survives all seven units, unrecorded, against an explicit coverage claim | new |

---

### B1 — blocker — `-8` §6 AC7, with §3 bullet 3 and §10's final paragraph

**Address.** `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-8.md`, §6 AC7
(lines 116–120); §3 bullet 3 (line 61); §10 final paragraph (lines 192–194).

**The defect.** §2 S3 reads "No opener test and no closure test: see §8, where the fork is resolved and
both are refuted by measurement", and §8 F1 resolves to option (c). AC7 is byte-unchanged by rev-4 and
still requires exactly the refuted pair: "When a declined slash has a later slash on its line and an
opener still OPEN at the end of the span, the predicate reports a LEAK. When the opener CLOSES inside
the span it reports NO leak". Section 2 retires the test; section 6 mandates building it — for the
fourth consecutive round, in the one document whose rev-4 exists to close that fork.

Three consequences, each independently blocking. A builder implementing §6 rebuilds the closure test
whose false-negative class round 3 confirmed as B2. AC7's assertion "over all three measured false
positives named in S3" is a dangling reference — rev-4 deleted those three fixtures along with the
test, and S3 now names none. And AC7 is the ONLY criterion in the unit touching S3 (verified: AC1–AC6,
AC8 and AC9 all target the predicate, the tables, the seam or regression), so once AC7 is corrected,
**S3 — the ambiguity report the entire fork resolution rests on — ships at order 5 with no acceptance
criterion and nothing that can fail if a builder omits it.**

The same non-fold left §10's reuse audit asserting in the present tense that "S3's leak set includes
`/*` and `*/` for exactly that reason", which is the sole justification for the `TOOL-aLexedStripper-5`
citation. S3 has no leak set at rev-4, and `-6` S3 explicitly dropped `*/` as "a CLOSER the predicate
could never have reported" — round 3's confirmed finding, removed from `-6` and left standing here.
§3 bullet 3's "the leak report" is naming residue only; its substance is still correct.

**Fix.** Replace AC7 with the criterion the resolution actually owes, in S3's own vocabulary and in
both directions: through the `--selftest` seam (S6), a line carrying a declined slash and a qualifying
later slash reports AMBIGUOUS; a line carrying a declined slash and no later slash does not; both
scanners return the same answer for the same script. Assert positively on `-6` AC5's two-line `/*`
fixture and negatively on `tools/workflows/tier2-review.js:395`'s marker shape. Delete every
leak/no-leak word and the "three measured false positives" reference. Rewrite §10's closing paragraph
to cite `TOOL-aLexedStripper-5` for why a `/*` inside a regex literal is undecidable at all — which is
the premise of the DECLINE and of reporting ambiguity — not for a retired leak set. Reword §3 bullet 3
to "the routing of the AMBIGUITY report".

**Left-shift gate.** A retired-vocabulary leg over `memory/builds/*/spec/*.md`: when a spec declares
an `S<n>-RETIRED` block, every distinctive term that block retires (here `leak set`, `opener set`,
`leak report`, `closure test`) must not appear anywhere else in that spec or in any sibling spec that
cites it, outside the RETIRED block itself. Cheap, mechanical, and it reds on exactly this class. Stage
it RED against the pinned rev-4 blobs before wiring — it should report B1 and B2 on the current tree,
which is the observation that proves it can fail.

---

### B2 — blocker — `-6` §4 ¶2, with §5's risks line, §8, S1 and AC5

**Address.** `…-spec-TOOL-aPairedLexer-6.md`, §4 paragraph 2 (lines 53–59); §5 risks (line 78); §8
(lines 121–122); §2 S1 (line 31); §6 AC5 (line 101).

**The defect.** rev-4 rewrote `-6` S3 and AC6 and left the rest of the document describing the retired
design. §4 still states the routing condition as "A declined `/` with a later `/` on the same line and
an opener strictly between them was a regex, and everything between leaked", and still concludes
"Ordinary division does not match … so it does not route" — the exact opener/extent test `-8` S3 now
refuses ("there is no opener set") and `-8` §8 refuted by measurement. A builder implementing §2 and a
builder implementing §4 build different mechanisms, for the CENTRAL mechanism of the fork resolution.

The contradiction is verdict-bearing, not cosmetic. AC6's own subject — two ordinary divisions on one
line — DENIES under S3's rule and ADMITS under §4's, so the criterion that RECORDS the re-baseline
passes or fails depending on which section the builder reads. And AC6's only stated justification is a
cross-reference to §4 ("§4 names the class of legal script that now does"), which is dangling and
inverted: §4 names no such class and asserts the reverse.

Three further clauses carry the same non-fold, and they are one edit, not four. §8 — the section M2
and M3 read for fork state — still reads "AC6 decides the precision question the audit raised, in the
ADMIT direction, and the extent-scoped condition in §4 is what makes that answer available", against
an AC6 that is now a DENY and an extent condition that no longer exists. §5's risks line still bounds
the precision cost with "The extent-scoped condition in §4". S1 still consumes "`TOOL-aPairedLexer-8`
S3's LEAK report" five lines above S3 saying the report is AMBIGUITY and not a leak. AC5 still requires
its arm be "Table-driven over the opener set, one row per opener" — a build instruction to enumerate a
set the same commit deleted, so the criterion is unbuildable as written even though its `/*` fixture
still denies for the right reason.

**Fix.** Rewrite §4 ¶2 to CITE `-8` S3's condition rather than restate it, and to NAME the class of
legal script that now denies, which is what AC6 and the rev-4 log both promise §4 does. Delete the
`args.n / args.total` example and the "Ordinary division does not match" sentence. Rewrite §8 to:
"none — the precision question is decided by `TOOL-aPairedLexer-8` §8 F1, in the DENY direction, and
AC6 records the cost that decision carries"; the word ADMIT must not survive in that section. Repoint
§5's risks line at `-8` §8 F1's resolution. Change S1 to "AMBIGUITY report". Drop AC5's opener-table
sentence and keep its fixture as a single row demonstrating the condition is opener-agnostic.

**Left-shift gate.** Two legs. First, the retired-vocabulary leg from B1 covers S1 and AC5 directly.
Second, a fork-state consistency check: when a spec's §8 states a resolution direction (ADMIT / DENY)
and names a criterion, the named criterion's own text must state the same direction. That is a
two-line grep pair and it reds on `-6` today.

---

### B3 — blocker — `-8` §2 S3, with §8 F1's cost paragraph

**Address.** `…-spec-TOOL-aPairedLexer-8.md`, §2 S3 (lines 39–41); §8 F1, the paragraph beginning
"The cost is real and is named rather than discovered".

**The defect.** S3's whole trigger is that a declined slash's line "also carries a later slash". The
spec never says whether that later slash is a raw character, a slash TOKEN the scanner reaches in code
mode, or a `//` comment introducer — and no criterion anywhere in the seven pins any answer. Both
scanners `break` on `//` (`agent-cap.js:302` and `:621`), so an implementer scanning as-they-go and an
implementer doing a raw lookahead get opposite answers on the same line.

The two readings differ by the entire population over this repo's own corpus. I implemented S3's
condition over the four tracked workflow scripts, walking them with the scanner's own mode machine:

```
tools/workflows/check-workflow-syntax.js  RAW=0  TOKEN=0
tools/workflows/drift-audit-code.js       RAW=1  TOKEN=0   L285
tools/workflows/drift-audit-state.js      RAW=1  TOKEN=0   L297
tools/workflows/tier2-review.js           RAW=1  TOKEN=0   L395
```

Every hit is the same line and the same cause: `Math.ceil(<id>.length / MAX_VERIFIERS)) //
gov:fixed-verifiers`, where the declined division slash is followed by the `//` of the marker comment
that `fanoutFindings` requires on that same raw line and `boundedBranch` (`agent-cap.js:220`) requires
in that exact literal form. Under the raw reading, all three of this repo's shipped harnesses — the
Tier-2 review harness the charter mandates included — route both views to the distrusted per-line
fallback on every run, permanently. Under the token reading, none do.

**§8's ratified cost statement is priced on the wrong reading, and this is the second half of the
defect.** It names the class as "a legal script with two ordinary slashes on one line" and prescribes
"end the statement before the ambiguous regex, or bind it to a name" — a one-character workaround
referencing a regex the named class by definition does not contain, and one that is structurally
unreachable for the measured class, since the marker rule forbids moving either the division or the
comment off that line. M3 ratified option (c) against this sentence. The vetoes that produced (c) are
unaffected — (a) and (b) remain fail-open regardless of how large the cost is — so the RESOLUTION
survives; the recorded COST does not. Also unstated: `fanoutFindings` picks the view once for the whole
script (`view.unterminated ? lines.map(...) : view.code`), so one ambiguous line demotes all four
rules, not its own line.

**Fix.** State the subject explicitly in S3 at the token level, and give the comment opener its own
arm: a declined slash makes its line ambiguous when a later `/` on that line is a slash token reached
in code mode, or is a `/*` block-comment opener, and NOT when it is a `//` line-comment introducer or
sits inside a string, template or comment. That reading is the safe one and it was checked against
every case in this review — `tier2-review.js:395` admits, `-6` AC5's two-line fixture reports, `-6`
AC6's two divisions still deny. Then restate §8's cost paragraph against the measured population,
citing the three harness lines, replace the one-character claim with the real remedies (`splitInto(x,
K)`, or splitting the statement), and say the ambiguity is script-scoped rather than line-scoped.

**Left-shift gate.** Pin `tools/workflows/tier2-review.js:395`'s exact shape as an ADMIT arm and `-6`
AC5's two-line `/*` fixture as a DENY arm in `tools/hooks/agent-cap.test.sh`, in the same commit,
staged RED first. That pair is the discriminator: it fails under the raw reading and passes under the
token reading, so it cannot be satisfied by an implementation that picked the wrong one. Add a
standing leg that runs the hook over every tracked `tools/workflows/*.js` and reds if any tracked
harness is denied by the hook that governs it — the repo's own harnesses failing their own guard is a
condition no one should have to notice by hand.

---

### B4 — blocker — `-8` §2 S2, with §6 AC4's negative table

**Address.** `…-spec-TOOL-aPairedLexer-8.md`, §2 S2 (the closed keyword set); §6 AC4.

**The defect.** Three members of the closed keyword set — `of`, `await`, `yield` — are CONTEXTUAL
keywords in JavaScript and are legal identifiers. S2's guard rejects only a preceding `.`, word
character or dollar sign, so a variable literally named `of` satisfies it and opens a regex span over
live code. This is a fail-open authored by the unit whose §5 names over-recognition as the direction
S2 exists to prevent.

Measured, not argued. For each of the three keywords I built:

```js
const of = list.length
const z = of / 2; parallel(items.map(f)); const w = 9 / 3
```

`node --check` accepts all three. Against the shipped hook each exits **2**. Against a copy of
`tools/hooks/agent-cap.js` patched with exactly S1+S2 as written — the trailing code text tested
against the closed set, the guard rejecting only `.`, a word character or `$` — each exits **0**. Both
scanner sites were patched (2 sites), and the patched file is `node --check` clean. The regex span
opens after the bare identifier, runs to the `/` before `3`, and blanks the raw `parallel(` out of the
view; the slash was ACCEPTED rather than declined, so S3 reports nothing and the four rules never fall
back. A raw primitive is still ADMITTED after all seven units land.

AC4 cannot catch it. Its five negative rows are `obj.in / 2`, `x.of / 2`, `m.delete / 2`, `p.new / 2`
and `r.case / 2` — every one a `.member` form, so the table exercises only the member-access direction
of a guard that has two. `-8` §3's "not full JavaScript lexing" non-goal does not withhold this: it
covers the DIVISION direction only ("after an identifier, a number or a closing bracket, `/` stays
DIVISION").

**Fix.** Drop `of`, `await` and `yield` from the closed set — they are the least valuable rows, and
AC3's positive table pins `return`, `typeof`, `case`, `throw` and `yield`, so only `yield` needs
re-covering — or require in S2 that the keyword not be the target of a declaration or assignment. Add
a NEGATIVE row to AC4 for a BARE identifier named `of`, with its measured tip verdict of `2`, so the
table covers both directions of the guard rather than one.

**Left-shift gate.** Two. First, one AC4 negative row per contextual keyword in the set, in the bare
form, asserted at `2`. Second — and this one generalises past this build — make
`tools/hooks/agent-cap.test.sh` run `node --check` over every fixture it feeds the hook, failing the
arm if the fixture does not parse. A fail-open can only be claimed on runnable JavaScript, and this
gate would have refuted one of this round's own finder rows automatically (see below).

---

### B5 — blocker — `-9` §6 AC7, with AC4's replacement name

**Address.** `…-spec-TOOL-aPairedLexer-9.md`, §6 AC7 (lines 105–106); §6 AC4 (lines 91–95); against
§2 S2c (line 40).

**The defect.** Round 3's B3 named AC4 AND AC7. rev-4's own log records folding it by amending AC4
only, and AC7 is untouched: it still excepts "any this unit's **sibling** re-baselines by name". S2c
and the new AC4 perform the admit-to-deny flip of `rule3: an exposed const resolves the cap and the
script admits` **at this unit**, not at a sibling, so the exception has a null referent and covers no
arm. AC7 therefore demands that the very arm AC4 requires to flip stay green. §2 and §6 of one
document require opposite things about one shipped arm for the fourth round running, and AC7 as
written cannot pass, so unit 9 cannot go green as specced.

Compounding it, the amended AC4 acquired a fresh defect while closing the old one. Its prescribed
replacement name — "a binding visible only to the distrusted view does not resolve a cap" — states
`TOOL-aPairedLexer-10` S1's mechanism, not the cause that fires here. Re-derived against the real
code: `blankLiterals` (`agent-cap.js:609-668`) emits nothing while in `tmpl` mode, so for the arm at
`agent-cap.test.sh:952` the paren-safe view's `code` is `["const t = `","","",""]` and the
`boundedParallel(...)` call-site line is BLANK. That is S2b's "cannot show it AT ALL" deny, which is
exactly the argument `-9`'s own AC5 makes three lines later for the structurally identical
block-comment twin. Unit 10's rev-4 AC4 now only OBSERVES the re-baseline, so nothing downstream
corrects the title, and the arm would ship permanently named after a mechanism that does not fire on
it. AC4 asserts no denial MESSAGE either, so an exit-code comparison cannot tell the two causes apart.

**Fix.** Change AC7's exception to "except the arm S2c re-baselines by name". Re-cut AC4's replacement
name onto S2b's actual cause — the paren-safe view cannot show the call site, so the cap is
unresolvable — require the denial message to name that ambiguity (the same message AC5 prescribes for
the block-comment arm), and state the arm's new title verbatim so `-10` AC4 can assert it unchanged.

**Left-shift gate.** A cross-reference resolver over the spec set: any AC clause of the form "except
… by name" must resolve to a name that appears in the same document, and any clause attributing an act
to a unit must name a unit whose own scope section claims that act. Both are greppable and both red on
`-9` and `-10` today. Separately, convert every deny-expecting arm in `agent-cap.test.sh` from the
exit-code-only `js` helper to the existing `msg` helper, so an arm that denies for a NEW reason fails
instead of passing — the suite already has the mechanism; it is simply not used here.

---

### H1 — high — `-10` §4, §5 and AC7

**Address.** `…-spec-TOOL-aPairedLexer-10.md`, §4 opening paragraph; §5 testing bullet; §6 AC7.

**The defect.** rev-4's revision log claims the attribution high was folded across "§4, §5, AC4 and
AC7", and the amended AC4's own text asserts that "§4 and §5 are corrected the same way". Git refutes
both: `git diff 7bf53d65 20ae25b7 -- …-10.md` touches only the status line, the round-3 records row,
AC4, AC6 and the rev-4 log. §4 still opens "S3 is a deliberate behaviour change to a shipped arm and
is called out as one"; §5 still reads "S3 re-baselines an arm rather than deleting it"; AC7 still
excepts "the one S3 re-baselines by name" — all against S3's own "This unit inherits the inversion and
does not repeat it". Three of the four addresses round 3 confirmed are unchanged, and the document now
makes a checkable false statement about its own fold.

**Why high and not blocker.** `-10`'s AC7 does not have `-9`'s structural failure. By the time unit 10
runs (order 9), the arm has already been flipped and renamed by unit 9 (order 8), so it is green in
its re-baselined form BEFORE this unit and green after it. AC7's exception is vestigial rather than
contradictory, and AC7 can pass. What remains is stale attribution and a false self-claim — a
records-accuracy defect that misleads a reader without stopping a builder.

**Fix.** Rewrite §4's paragraph to attribute the inversion to `TOOL-aPairedLexer-9` S2c at order 8,
keeping only the rationale here, and to say the arm ALREADY denies when this unit lands while S1 would
independently produce the same verdict by a different cause. Change §5's bullet to "S4's two
directions; the arm `-9` S2c re-baselines is not re-baselined again here". Change AC7's exception to
name the `-9` arm, or delete it. Correct AC4's claim, and add a §9 line recording that the rev-4 log
overstated the fold.

**Left-shift gate.** A revision-log honesty check: when a spec's revision log names sections it
folded, `git diff <prev-rev-sha> <this-rev-sha> -- <spec>` must contain a hunk inside each named
section. This is fully mechanical from the status line's rev number and the commit history, and it
reds on `-10` today. It is the highest-value gate in this report, because a fold that lies about
itself defeats every subsequent audit that trusts the log instead of re-reading the file.

---

### H2 — high — `-6` §6 AC1, against S2 and AC4

**Address.** `…-spec-TOOL-aPairedLexer-6.md`, §6 AC1.

**The defect.** AC1's fixture — a phantom span wrapping "a raw `parallel(D.map(...))`" — is denied by
RULE 2, not rule 1. Measured: `const r = await parallel(D.map((d) => agent(d)))` exits 2 with rule 2's
message, "a verify/fan-out stage spawns one agent per item", because `fanoutFindings` runs before
`offendingLines`. Only a receiver with no per-item `agent()` — `parallel(thunks)`, or
`pipeline(files, s1, s2)` — reaches rule 1's message. AC1 asserts nothing but the exit code, so it is
satisfied by the same rule AC4 pins, and AC4's claim that "AC1–AC4 are one arm per RULE" is false for
rule 1, leaving rule 1's fallback with no criterion at all.

This matters mechanically rather than cosmetically. `offendingLines` (L91) and `fanoutFindings` (L363)
each call `renderCodeView` separately, so a builder can wire the dirty signal into one call's return
and leave the other blind — passing AC1 and AC4 with rule 1 still blind. That is precisely the
one-consumer-widened defect rev-1 shipped and this unit was promoted to fix, and S2's "All four rules,
or the fix is the defect it was promoted for" would then be observable for three.

**Fix.** Restate AC1's fixture with a receiver rule 2 does not flag (`await parallel(thunks)` or
`pipeline(files, s1, s2)`), and make each of AC1–AC4 assert the DENIAL MESSAGE that identifies its
rule rather than the exit code alone. Four criteria that all exit 2 cannot demonstrate one arm per
rule.

**Left-shift gate.** The same `msg`-helper conversion named under B5, applied to `-6`'s four arms: a
rule-attribution arm asserts the rule's message. Add one arm per rule that would go green only if that
rule's own fallback is wired, and stage each RED against a build with only the other three wired.

---

### H3 — high — `-8` §3 bullet 1 and §5's ceiling-paragraph line — RAISED BY THIS ROUND

**Address.** `…-spec-TOOL-aPairedLexer-8.md`, §3 non-goals bullet 1; §5's user-docs line ("the
dossier's ceiling paragraph is narrowed to what actually remains"); and the ceiling paragraph itself
at `tools/hooks/agent-cap.js:283-289`.

**The defect.** This is the answer to attack (a) and it refutes the claim, made in one of this round's
own confirmed rows, that the resolution misses no leak shape. It misses one — on the ACCEPT side,
where S3 by construction cannot look, because S3 reports only for slashes it DECLINES.

`renderCodeView` sets `prev` to the closing quote after consuming a string. A quote is neither in
`})]` nor a word character, so the guard at `agent-cap.js:305` treats a following `/` as a REGEX
position. Measured:

```js
const x = "a" / 2; await parallel(D.map((d) => agent(d))); const y = "b" / 3
```

`node --check` clean. Exit **0** against the shipped hook, **0** against the S1+S2 patch, and 0 under
the rev-4 ambiguity rule — while the bare primitive alone exits **2**. The first slash opens a "regex"
that closes on the second, blanking the raw `parallel(` out of the view. No slash on that line is
declined, so S3 announces nothing, `unterminated` stays false and `clean` stays true.

The shipped ceiling paragraph asserts the opposite coverage: "a regex is recognised only after a token
that cannot end an expression — an operator, an opening bracket, a comma, a colon, a semicolon, or
start of input." A closing quote is none of those, and a string CAN end an expression. `-8` §3's
residual statement is likewise incomplete — it names only the DIVISION direction — while §3 goes on to
claim "`TOOL-aPairedLexer-6` is what makes it announce itself — using S3", which is not true for this
shape.

**Why high and not blocker.** The seven units never promised to close this residual, and the fix is a
scope and records sentence rather than a redesign. But the set makes an explicit and incomplete
coverage claim, and §5 promises the ceiling paragraph will be narrowed "to what actually remains", so
shipping it unrecorded is a real defect against this build's own bar.

**Fix.** Correct the ceiling paragraph at `agent-cap.js:283-289` to state the accept side accurately —
a `/` after a closing QUOTE is also taken as a regex position, and that is a residual. Add a `-8` §3
bullet naming the residual explicitly, so it is recorded rather than discovered. If it is to be closed
rather than recorded, the fix is one character in the guard set: add `'` and `"` to `'})]'`.

**Left-shift gate.** Add the fixture above to `agent-cap.test.sh` as an arm asserting the recorded
behaviour, so a future change to the guard set is observed rather than silent. Then generalise: an arm
that walks the guard set itself and asserts, for each character class that can END an expression
(identifier, number, `)`, `]`, `}`, `'`, `"`, backtick), that a following `/` is treated as DIVISION —
so the class is gated, not the instance.

---

## Refuted in adjudication

One confirmed row is refuted here on a run, and it is recorded rather than dropped because the
relocation discipline this build runs on depends on knowing which findings did not survive.

**The "fall-through leak" row** claimed two fail-open shapes: `if (a) /x` + backtick and `const p = /x`
+ backtick, each with a raw `parallel(D.map(...))` between two such lines, balanced so `unterminated`
stays false. Both are **SyntaxError** under `node --check` — `Invalid regular expression: missing /` —
because a JavaScript regex literal cannot contain a line terminator, so a slash the scanner accepts at
a regex position must find its closer on the same line or the source does not parse. A script that
cannot parse cannot fan out, so admitting it is not a reachable fail-open. The row's underlying
instinct was right and its mechanism was wrong; the correct version is H3 above, which reaches the
same conclusion on VALID JavaScript through the guard set rather than through the fall-through branch.

That refutation is also the argument for B4's second gate: a `node --check` leg over every fixture in
`agent-cap.test.sh` would have caught this automatically, rather than costing a skeptic pass.

## What the fold DID close

Stated so the direction of travel is legible and the loop-stop is not read as "nothing improved".

- Round 3's **B1** (the `/*` leak that could never be reported) and **B2** (the closure test's false
  NO-LEAK on a balanced opener pair) are both genuinely CLOSED, dissolved by retiring the leak test
  outright rather than patched. The fork resolution itself is sound: options (a) and (b) remain
  fail-open regardless of the cost dispute in B3, so option (c) survives its own cost being
  mis-priced.
- Round 3's **B4** (`-10` AC6's fixture passing against the shipped tip) is CLOSED, restated as a
  requirement the builder must verify, with dropping S2 named as the honest outcome if no
  discriminating fixture exists. That is the right shape for a criterion that has now failed three
  fixtures.
- `-6` AC6's re-baseline verdict is CORRECT. The fixture genuinely denies once the design lands, and
  recording the cost as a re-baseline rather than leaving an admit control that cannot fail is the
  better of the two available answers.
- Units 7, 11 and 12 hold no disagreement at rev-4 and were not the source of any finding this round.

## Notes for the build

The loop stops here, so these are build obligations rather than audit items.

The five blockers are not one class. B1, B2 and B5 are non-folds — text the rev-4 edit should have
reached and did not — and they are resolved by editing, with the retired-vocabulary and
cross-reference gates above making the class un-repeatable. B3 and B4 are different: they are defects
the rev-4 edit AUTHORED, in new S2 and S3 text, and both are fail-opens or fail-open-adjacent. Build
those two first and stage each one's gate RED before wiring it, because they are the two that a build
"as specced" would otherwise ship.

The single highest-leverage gate in this report is H1's revision-log honesty check. Four rounds of
this audit have each had to diff the specs against their own revision logs to discover what was
actually folded, and in this round the log was wrong. A gate that compares a fold's claim to its diff
removes that cost permanently and is perhaps twenty lines.
