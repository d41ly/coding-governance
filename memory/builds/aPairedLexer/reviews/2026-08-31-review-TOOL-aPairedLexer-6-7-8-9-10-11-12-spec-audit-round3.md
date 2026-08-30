**Serves:** spec-audit TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

# Spec audit round 3 — the same seven units at rev-3, and the convergence ruling

*Node a, 2026-08-31, round 3. Rounds 1 and 2 returned BLOCKED with 7 and 5 blockers; every round-2
finding was folded into a rev-3 of the spec that owned it. Round 2's own load-bearing observation was
that its predecessor's fold INTRODUCED three of its five blockers, so this round aimed first at the
two largest rev-3 edits — the `--selftest` seam moving from `TOOL-aPairedLexer-6` to
`TOOL-aPairedLexer-8` S6, and the leak predicate gaining a closure test — and asked of each fold
whether it CLOSED its finding or merely RELOCATED it. A parallel fan of primed finder lenses over the
seven specs, the two scanners they change, the extractor the seventh changes, the build README's
authored roster, `memory/guides/BUILD-METHOD.md` M2, and the shipped suite they inherit, then
skeptics prompted to REFUTE each finding against the source at the pinned base. Every behavioural
claim below was re-derived in the synthesis pass: an exit code measured by piping a real `Workflow`
payload into the real `tools/hooks/agent-cap.js`, a span computed against the fixture's own byte
indices, or a Python value printed by calling the real `map_lib` helper. Prose-only arguments were
refuted, as in round 2.*

Reviewed subjects, each pinned at the blob actually read:

- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-6.md@8db24b5a98a1`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-7.md@9f09eacaf35e`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-8.md@605d4e6ce31e`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-9.md@48d8d0c54ac0`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-10.md@eb2f0ffcf2f2`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-11.md@d91bcf1d2219`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-12.md@3c2ae1b3f3c5`

Round 3.

## Verdict: BLOCKED

The counts sit here rather than on the heading, because that line's token is a closed set and a tally
appended to it turns a structural check into a semantic one.

**4 blockers, 2 highs and 1 medium stand.** Measured the way round 2 measured its own: distinct
defects, one row per address-and-fix, duplicate finder rows consolidated rather than padded out.
Round 2 stood at 5 distinct blocking defects over 10 rows; round 3 stands at 4 over 7. Both measures
fell, and by the same counting method, so **BUILD-METHOD M4's convergence test is satisfied — 4 is
strictly smaller than 5 — and the loop RE-ARMS for a round 4 rather than stopping.** That ruling is
stated plainly because its opposite was live: at 5 or above the loop stops, every standing blocker is
promoted, and two of the four below would then have been built as specced into a shipped fail-open.

**Convergence is not the same as health, and the direction of travel is the reason.** Two of round
2's five blockers are genuinely closed. Two are RELOCATED rather than closed — B1's closure test
traded a false-positive class for a false-negative class of the same defect, and H3's fold moved
unit 9's §2/§6 contradiction one clause over instead of removing it. And one blocker below did not
exist before rev-3: unit 8 S3's new span extent is narrower than every sibling statement of the same
rule, which is a defect the fold authored. The relocation rate is the number to watch in round 4, not
the headline count.

**Review shape:** raw 30, confirmed 16, refuted 14, unverified 0, precision 0.53. The 16 confirmed
findings consolidate into the 7 adjudicated rows below; each row names the finder ids it absorbs.
Four independent finders reported unit 9's AC4 contradiction and three reported unit 8's span extent
— the clustering is again a signal about how reachable these defects are from a cold read. Precision
fell from 0.64 to 0.53, which is the expected shape for a third pass over a narrowing surface: the
easy defects are gone and more of what the lenses now propose is argument rather than measurement.
Per §8, that is a signal to tighten scope before adding agents in round 4, not to add lenses.

## What the fold DID close

Stated first because it is real, and because a promoted build should not re-do it.

- **B3 — the member guard's subject.** Unit 8 S2 now states that the guard's SUBJECT is the running
  code text, not a bare trailing word and not a line prefix, and that `^` means start of INPUT. Both
  fail-open readings round 2 measured are named and excluded in the text a builder implements.
  Closed.
- **B4 — unit 6's fixture discipline.** §4 now carries the discipline paragraph and states the rule
  in the direction unit 6 actually needs it: every arm here needs a slash `-8` DECLINES, because a
  `return`-position trigger is DISSOLVED two steps earlier. AC5's fixture (`if (a) /x[/*]y/`) uses a
  post-`)` slash and complies. The attack that the paragraph was prose beside criteria still naming
  the wrong trigger did not survive: AC1–AC4 name a declined-slash span, not a return-position one.
  Closed.
- **H5 — unit 6 AC6's precision control.** The control now has a later slash on its line
  (`const rate = done / total; log(\`tick\`); const inv = total / done;`), so `-8` S3's leak test can
  fire on it and the control can fail. Closed as written — though B3 below turns that same fixture
  into a second problem.
- **H2 — unit 12's ceiling-2 inversion.** AC4's claim that ceiling 2 inverts into a raised `MapError`
  rather than retiring is TRUE, and was measured rather than read: on
  `export const U = /^https?:\/\//, ALSO = 1;`, `render_comment_free` today returns
  `'export const U = /^https?:\\/\\'` and `_has_top_level_comma` is `False` on it, while the same
  helper on the untruncated line is `True`. Modelling regexes removes the truncation, the guard sees
  the comma, and `enumerate_exports` raises. The declared new failure mode is the real one. Closed.
- **M2 agreement across the seven.** Every rev-3 status header reads `SPECCED · rev-3 · node a ·
  Tier-2 · base 72dff924 · streams tooling`, orders 5 through 11 are contiguous and unique, and the
  generated `gen:build-units` columns agree with all seven. The single M2 surface still disagreeing
  is the README's AUTHORED roster row, M1 below.

## Findings

Severity-ranked, blockers first. Each row names its address, the finder ids it consolidates, the fix,
and a left-shift gate.

| # | Sev | Address | Defect |
|---|---|---|---|
| B1 | blocker | `-8` §2 S3 — the span's END | The `/*` leak the fold was told to keep can never be reported, and `-6` AC5 cannot go green |
| B2 | blocker | `-8` §2 S3 — a BALANCED opener pair | The closure test answers NO LEAK on a span that blanks live code; a raw primitive stays ADMITTED after all seven units land |
| B3 | blocker | `-9` §6 AC4 + AC7, against §2 S2c | Two clauses of one spec require opposite verdicts for one shipped arm; AC4 also depends on a unit sequenced after it |
| B4 | blocker | `-10` §6 AC6 — the replacement fixture | The only criterion pinning S2 passes against the SHIPPED tip, with the whole unit unimplemented |
| H1 | high | `-10` §6 AC4 + AC7, and §4 + §5 | S3 hands the re-baseline to `-9`, but four other clauses still attribute it here and demand a second rename |
| H2 | high | `-6` §2 S3 + §6 AC5 — the leak SET | `*/` is a closer; the owning predicate can never report it, so its required table row cannot fail |
| M1 | medium | `memory/builds/aPairedLexer/README.md:75` | The authored roster still credits the seam to the unit at order 7, two steps after the unit that now owns it |

---

### B1 — blocker — `-8` §2 S3, where the candidate span ENDS

*Consolidates finder ids 17, 11, 26. Against `-6` §6 AC5 and `-6` §4.*

S3 bounds the leak scan "from the declined slash to the next slash on the same line". A `/*` opener
IS a slash first, so a block-comment opener can never lie strictly inside that span.

Measured on unit 6 AC5's own fixture. In `if (a) /x[/*]y/.test(s)` the slash indices are `[7, 10,
14]`: the declined slash is at 7, and the next slash on the line is index 10 — the `/` that is both
the character-class member and the first byte of the `/*` opener. S3's span is therefore `"/x[/"`.
Nothing is open at its end, so the closure test reports NO leak, `-6` S1/S2 never set `dirty`, and
AC5's "the hook exits `2`" cannot pass. This is not fixture-specific: any `/*` after the declined
slash either IS the next slash or sits behind an earlier one.

The consequence is not a red arm only. Fed to the hook at the tip — a real `Workflow` payload,
`tool_input.script` — the full AC5 fixture with a raw `await parallel(D.map((d) => agent(d)))`
between its two regex lines exits **0**, while the same primitive alone exits **2**. The primitive is
blanked out of the view and stays admitted after all seven units land.

`-6` §4 words the same predicate a third way — "a later `/` on the same line and an opener strictly
between them", existential, under which the `/*` at column 10 IS strictly between 7 and 14. Two units
that exist so one predicate answers once now word its extent differently, and the narrower wording is
in the section that OWNS the predicate, which is the one a builder implements.

**Fix.** In S3, state the span end as the class-aware regex-close walk both scanners already run
(track `[`/`]`, skip `\` escapes, an unterminated walk yields NO span), or as end-of-line, and delete
the "to the next slash" clause. Round 2's B1 prescribed end-of-line and named this fixture among the
true leaks that must still report; the wider extent still reports NO leak on all three measured false
positives, since each opener closes before end of line. Add the `/x[/*]y/` row to AC7 so the narrow
reading cannot be re-derived. Re-word `-6` §4 to CITE `-8` S3 rather than restate it.

**Left-shift gate.** Add a `tools/hooks/agent-cap.test.sh` arm for this exact fixture and stage it
RED first, per §7's "a new gate is not landed until its failing case has been observed". Structurally:
`-8` AC7's negative/positive table and `-6` AC5's opener table must be driven from ONE declared opener
list, so a row that the predicate cannot observe reds instead of passing as a passenger.

### B2 — blocker — `-8` §2 S3, a balanced opener pair inside the span

*Consolidates finder id 18. Against `-6` §1, `-6` AC1 and `-6` AC6.*

The new closure test reports NO leak when the declined span carries a BALANCED opener pair. But that
span still blanks the live code between the two openers, so the B1 fold traded a false-positive class
for a false-negative class of the same defect.

Measured. The script

```
const MAX = 5
if (a) /x`; parallel(D.map(f)); `y/.test(s)
```

exits **0** at the tip; the same `parallel(D.map(f));` with no declined regex exits **2**. Nothing is
open at the end of the span under either the narrow or the wide reading, so S3 answers NO LEAK, `-6`
S2 never routes it, and the raw primitive is silently admitted.

This is not an edge case the unit tolerates — it is `-6` §1's own motivating defect, verbatim: "Two
mis-lexed backticks balance, `unterminated` stays false, `clean` stays true, and a raw `parallel(`
between them is blanked out of the view". `-6` AC1 requires the balanced shape too, since an
unbalanced one would leave `unterminated === true` and the existing fallback would already deny — so
AC1 is unpassable as well.

And the shape is structurally identical to `-6` AC6's precision control (division, closed template,
division), which the spec REQUIRES to stay at exit 0. One predicate input class, two required
answers. That is the part no amount of re-wording S3 dissolves: it is a decision, not a bug.

**Fix.** S3 must state the balanced-pair case explicitly and pick one of two answers, in the spec
rather than in the builder's head:

1. Report a LEAK whenever the span-as-code scan blanked non-whitespace content. Then re-cut `-6` AC6's
   control, which under that rule denies, and price the precision cost against the measured
   population — 0 hits across this repo's tracked `.js`.
2. DECLARE the balanced-pair residual as a named ceiling in `-6` §3, with an AC row pinning the
   admit, so the decline announces itself as a known gap instead of going silent.

Option 2 is the smaller change and is consistent with `-8` §3's existing residual paragraph; option 1
is the one that actually closes `-6` §1's motivating defect. The spec set has to say which.

**Left-shift gate.** Whichever answer is chosen, pin BOTH members of the pair as suite arms in the
same commit — the balanced-span fixture and `-6` AC6's control — so a future widening cannot move one
without reddening the other. If option 2 is taken, the ceiling belongs in
`memory/map/features/agent-cap.md`'s gap list with the fixture inline, so the admit is documented
coverage rather than an unrecorded blind spot.

### B3 — blocker — `-9` §6 AC4 and AC7, against §2 S2c

*Consolidates finder ids 2, 10, 20, 27.*

The H3 fold added S2c — "S2b FLIPS the shipped arm `rule3: an exposed const resolves the cap and the
script admits` from ADMIT to DENY, at THIS unit's step … The arm is re-baselined HERE" — and left AC4
exactly as rev-2 wrote it: "its verdict is whatever `TOOL-aPairedLexer-10` re-baselines it to, and
this unit does not change it alone."

§2 and §6 of one document require opposite things about one shipped arm. That is the defect round 1
found at 16/6 and round 2 found again at this unit's AC5, reintroduced one clause over by the fix for
H3 — the third round running.

The flip is real and lands here. `blankLiterals` on that arm's script (`agent-cap.test.sh:952`, which
opens `const t = \`` unterminated) leaves the `boundedParallel(…)` call-site line BLANK in the
paren-safe view, which is precisely S2b's "cannot show it AT ALL" DENY condition, while the arm ships
expecting exit 0. Over the 89 shipped `js` arms it is the only exit-0 arm with a blind call site, so
S2c's single-arm claim is correct and AC4 is the clause that is wrong.

Two further consequences, both load-bearing. AC4 defers to a unit that refuses the deferral: `-10` S3
at rev-3 says the arm is "ALREADY re-baselined by `TOOL-aPairedLexer-9` S2c … This unit inherits the
inversion and does not repeat it." And AC4 is a dependency on a unit sequenced AFTER this one — `-9`
is order 8, `-10` is order 9 — which is a BUILD-METHOD M2 cross-read violation on its ordering axis,
verbatim: "no sub-spec depends on a unit sequenced after it". AC7's escape covers only arms "this
unit's SIBLING re-baselines by name", which by S2c is not this one, so AC7 as written cannot pass
either. No spec in the set states the arm's expected verdict, name or message at unit 9's step. Unit
9 cannot go green as specced, and a builder following AC4 would implement S2b so as not to flip it.

**Fix.** Rewrite AC4 to assert the flip at THIS unit's step: the arm DENIES after this unit, with
S2b's ambiguity message rather than a width, under a replacement name this spec STATES. Change AC7's
exception from "any this unit's sibling re-baselines by name" to "the arm S2c re-baselines by name".

**Left-shift gate.** Machine-checkable and cheap: a spec-lint leg that parses every spec's `order`
from its status header, greps its §6 for sibling unit ids, and reds when a criterion names a unit
whose order is greater than its own. That is the M2 ordering axis as a gate rather than a review
item, and it would have caught this row in all three rounds.

### B4 — blocker — `-10` §6 AC6, the rev-3 replacement fixture

*Consolidates finder ids 19, 28.*

AC6 exists to make S2 non-optional. Its rev-3 fixture — real `const K = 7`, bare `K = args.width`,
prose `const K = 5` inside the mis-lexed span — passes against the SHIPPED tip, with neither S1 nor
S2 implemented.

Measured, not argued. Built as §6 prescribes:

```
const t = `an unterminated template literal
const K = 5
const K = 7
K = args.width
const L = [{a:1},{a:2}]
await boundedParallel(L.map((x) => () => agent(x)), K)
```

The tip exits **2** with `the cap argument at the boundedParallel() CALL SITE is \`K\`, which this
file cannot resolve to an integer at or under 5` — verbatim the denial AC6 demands. Control: deleting
only the `K = args.width` line changes the message to `resolves \`K\` to 7, above the 5-agent cap`,
which isolates the cause to `intConsts`' existing bare-reassignment sweep (`agent-cap.js:167-175`).
That sweep runs per view and deletes `K` from the clean view and the fallback alike.

AC6's own stated mechanism is false on both halves. Neither view binds `K`, so "both views bind, S1
keeps the max" does not hold; and S2's sweep pattern `\b(?:const|let|var)\s+(\w+)\s*=` cannot match a
bare `K = args.width` at all, so S2 is not the thing that deletes the name even in principle. Round-1
finding 10 is open on its third fix, and this attempt is strictly worse than round 2's: that one
passed with S1 alone, this one passes with nothing.

**Fix.** Use no bare reassignment — any bare `K = …` visible to either view deletes the name from
both. Use two DECLARATIONS instead: a clean-view `const K = args.width || 500` (matched by
`intConsts`' `orBound` arm, bound to no integer and not swept), plus the prose `const K = 5` inside a
CLOSED template so the call site survives `_bl.code` under `-9` S2b. State the criterion on the
denial MESSAGE — `orBound`'s fallback-form wording, which only S2's sweep can produce — rather than
on the exit code, and state BOTH the S1-alone verdict and the S1+S2 verdict, since the harness
compares exit codes and an unstated pre-verdict is how this criterion keeps being satisfiable by
absence. Verify the chosen fixture against `intConsts` before pinning it; this is the third fixture
this criterion has had and the second that was never run.

**Left-shift gate.** The general rule is §7's, and it is what all three attempts skipped: a new arm
is not landed until its failing case has been observed. Concretely for this suite — every AC that
pins a behaviour change states the measured verdict at the BASE as well as the expected verdict after
the unit, and a spec-lint leg reds on an AC naming an expected exit code with no base-verdict clause.
`-6`'s ACs already carry that clause ("at the tip it exits `0`"); the convention exists and simply is
not enforced.

### H1 — high — `-10` §6 AC4 and AC7, and §4 and §5, against §2 S3

*Consolidates finder ids 5, 12.*

The rev-3 fold reached §2 and stopped. S3 now says the arm is already re-baselined by `-9` and that
this unit "inherits the inversion and does not repeat it", but four other clauses still say
otherwise:

- §4 — "S3 is a deliberate behaviour change to a shipped arm … Under S1 the clean view binds nothing
  there, so the name is deleted and the script denies … The arm is not deleted, it is inverted."
- §5's testing line — "S3 re-baselines an arm rather than deleting it."
- AC4 — requires the arm's "replacement name states that a binding visible only to the distrusted
  view does not resolve a cap", which is S1's reason, not the reason the arm actually denies after
  `-9`. S2b denies because the paren-safe view cannot show the call-site line at all (measured
  blank), so the arm no longer exercises S1's mechanism and AC4 asks for a second rename onto a cause
  that is not firing.
- AC7 — "except the one S3 re-baselines by name" is now a null reference, because S3 re-baselines
  nothing.

The practical damage is a criterion that observes nothing. At unit 10's step the arm already denies,
produced by its predecessor, so AC4 certifies a state it did not cause — and the arm is effectively
renamed twice with no spec stating what it is called or expects between the two units. Behaviour for
unit 10 is genuinely pinned by AC1, AC3 and AC5, which is why this is a weak criterion rather than an
unbuildable one.

**Fix.** Pick ONE owner of the arm's name and message. Either `-9` S2c specifies both and `-10` AC4
asserts them unchanged, or `-10` S3 performs an explicit second re-baseline (verdict unchanged,
reason narrowed) and AC7 names it. Then give AC4 an observation unique to unit 10 — the denial
message naming `K` as unresolvable is unit 10's, not unit 9's. Correct §4 and §5 in the same edit;
they are the copies that will otherwise be read as the spec.

**Left-shift gate.** Same lint as B3, one predicate wider: red when two specs in one build both claim
to re-baseline the same named suite arm, or when zero do while an AC7-style exception clause names
one. The arm titles are string literals in `agent-cap.test.sh`, so the check is a grep of quoted arm
names against the spec set — no parsing needed.

### H2 — high — `-6` §2 S3 and §6 AC5, the leak SET

*Consolidates finder ids 3, 21.*

S3 declares the leak set as "the openers a declined span can carry into code mode: a backtick, a
quote, `/*` and `*/`", and AC5 demands the arm be table-driven over that set, "one row per opener".
But `-8` S3 defines a leak as a CLOSURE failure — "it leaked only if a construct is still OPEN at the
end of that span" — and `*/` is definitionally a closer. It opens nothing, so no span containing one
can end with it open.

Measured: the second line of unit 6's own AC5 fixture, `if (a) /z[*/]w/.test(s)`, reports leak=false
under both the literal and the class-aware span reading, while the first line is the one that
reports. The `*/` row therefore passes only as a passenger of the `/*` row, and the harm it was
listed for — a regex-borne `*/` closing a real block comment early and exposing commented-out text as
live code — happens while the scanner is in COMMENT mode, where no declined slash is ever evaluated.
`blankLiterals`' block branch only tests `two === '*/'`, and `renderCodeView`'s block-comment branch
was deleted by `TOOL-aLexedStripper-5`. Unreportable by construction, in a build whose folded
findings are repeatedly "a criterion that could not fail".

**Fix.** Either reduce `-6` S3 to the OPENERS (backtick, quote, `/*`) and say in §4 why a closer needs
no row — the line that OPENED the span is the line that reports — or extend `-8` S3 to also report a
leak when a span CLOSES a construct the scan had open, and give `-8` AC7 that second direction
explicitly. The first is the smaller change and matches what the predicate can actually observe.

**Left-shift gate.** The shared-list gate named under B1 covers this too, and this is the row that
shows why it is the right shape: one declared opener list, consumed by `-6` AC5's table and `-8`
AC7's table, so a member with no reachable observation reds at the point it is declared rather than
shipping as a green row that certifies nothing.

### M1 — medium — `memory/builds/aPairedLexer/README.md:75`, the authored Units table

*Consolidates finder ids 15, 30. Against `-8` §2 S6.*

The order-7 row still reads "`TOOL-aPairedLexer-6` … a DECLINED slash announces itself to BOTH views,
through that predicate, plus the test seam (round-2 D3)", while the order-5 row for
`TOOL-aPairedLexer-8` (line 73) names only the predicate. The B2 fold moved the `--selftest` seam to
`-8` S6 — "the test SEAM, moved here from `TOOL-aPairedLexer-6` because this unit lands FIRST" — with
its own AC9, and `-6` §9 records the same move.

BUILD-METHOD M2 makes this table load-bearing: "The roster is the build README's authored Units table
where one exists." So the document a builder classifies from still describes the backwards-pointing
unit boundary B2 was raised to remove. The generated order/tier/rev columns and all seven status
headers agree at rev-3; this authored row is the one M2 surface left disagreeing.

**Fix.** Move the "plus the test seam" clause from the order-7 row to the order-5 row.

**Left-shift gate.** Derive over author, per §5 and §12. The generated `gen:build-units` block already
carries each unit's title from the spec itself; the authored table's Mechanism column is a hand-kept
second copy of prose the specs own, and it is the only part of the roster that can rot this way.
Delete the column and let the generated table carry the mechanism, or render the whole roster. There
is then nothing to keep fresh and this class is structurally impossible rather than gated.

## What was attacked and held

Recorded so round 4 does not re-spend on it.

- **`-8` S3's closure test on the three declared false positives.** Division with a closed
  single-quoted string, division with a closed block comment, and division with a closed template all
  report NO leak under both the narrow and the wide extent. The B1 fold's stated purpose is achieved;
  B1 and B2 above are about what it stopped reporting, not about what it kept.
- **`-6` §4's fixture-discipline paragraph.** It constrains AC1 through AC5 in substance — every one
  of them triggers on a slash `-8` declines, not on a return-position span. The attack that it was
  prose beside criteria naming the wrong trigger did not survive contact with the criteria.
- **`-12` AC4's ceiling-2 inversion.** Verified by running `map_lib` directly, as recorded above.
- **`-11` and `-7` at rev-3.** No confirmed finding. `-11`'s trigger is named literally and its
  view-pair statement matches `-9` S1; `-7`'s start-of-input rule is consistent with `-8` S2's
  corrected `^` clause.
- **M2 agreement across the seven.** Headers, orders, revs and the generated columns all agree; only
  M1's authored row does not.

## Notes for round 4

Two things about the fold, offered because the loop re-arms and the same mistake is available again.

Round 3's blockers cluster on exactly two edits — the closure test and the re-baseline hand-off — and
both were introduced BY a fold, not survived by one. The pattern across three rounds is that a
targeted amendment reaches §2 and stops, leaving §4, §5 and §6 stating the superseded position. Both
B3 and H1 are that shape, and B3 is that shape for the third consecutive round. A rev-4 that amends
§2 should re-read §4, §5 and §6 of the same document as part of the same edit, and the two spec-lint
legs named under B3 and H1 exist to make that mechanical instead of remembered.

The other one is a decision, not a defect: B2 asks the spec set to choose between precision and a
declared ceiling, and neither answer is available to a builder from the current text. That choice is
the owner's, and it should be made before the rev-4 edit rather than during it.
