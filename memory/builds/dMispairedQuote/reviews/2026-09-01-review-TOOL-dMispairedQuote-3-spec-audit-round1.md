**Serves:** spec-audit TOOL-dMispairedQuote-3

# Spec audit round 1 — `TOOL-dMispairedQuote-3`, the unit promoted out of a NON-CONVERGENT exit

*Node d, 2026-09-01, round 1. The subject is the unit round 2 promoted: unit 1's mechanism corrects
which quote OPENS a literal, which un-hides every other character the old mispairing was blanking,
and three DENY-to-ADMIT moves were reproduced against unit 1 alone. Unit 3's answer is a union — keep
the three shipped views verbatim, give each rule a selector, evaluate every rule over both views. No
code has been written; the spec is the PLAN and is audited as a design. Units 1 and 2 were read as
context and carry no finding of their own this round, though two findings below name work that must
land in one of them. Every surviving finding was re-derived in this worktree against
`tools/hooks/agent-cap.js` at BASE `d65da7ab`, against its shipped suite actually run, or against a
gate actually run.*

Reviewed subject, pinned at the blob actually read:

- `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md@2c8ff5ddc747b8bd125d8e79735c8addfdce795c`

Context read, not reviewed: unit 1 at rev-3, unit 2 at rev-2, the build `README.md`, and both prior
spec-audit records.

Round 1.

## Verdict: BLOCKED

Five confirmed blockers, four highs and five mediums, presented as 14 rows over 20 confirmed
findings. The mechanism is right and the unit should exist; what is wrong is that its central
guarantee — *monotone in the DENY direction by construction* — is asserted by three sentences and
enforced by nothing that can fail.

**The guarantee has three independent holes and each one is sufficient on its own.** §2's S2 census
of which rule reads which view is WRONG for half the rules, so the selector it specifies does not
reproduce shipped behaviour (B1). §2's S7 names a reference — "the shipped hook" — that will not
exist in the tree after this unit lands, and the in-tree implementation an author would reach for
compares the union against its own shipped arm, which is `union(a, b) ⊇ b`, decided before any data
is read (B2). And §6's AC7, the only criterion demanding an observed RED, quantifies over "each S6
arm", which excludes S7 — so the class-level property lands never having been seen to fail (B3).
Three ways to write a check that cannot fail, in the unit whose whole product is a check.

The other two blockers are not about the mechanism. §7 lists `lexicon naming predicates` as a leg
this unit keeps green while §2 mandates four new top-level names, three of which the declaration
refuses; I appended them and measured the leg RED (B4). And round-2 blocker 8 had two halves — a
verdict half and a carrier half — of which unit 3 takes only the verdict half, leaving the carrier
correction in no unit's scope while unit 2 lands last still shipping the untrue ceiling sentence
(B5).

One thing this round should say plainly, because it is the third instance of the same shape in this
build: **the defect is never in the mechanism and always in what observes it.** Round 1 filed "no AC
in §6 can observe it" twice; round 2 filed it four times; this round files it in B1, B2, B3, H1, H2,
H3 and M1. The specs in this build are consistently better at designing a change than at designing
the thing that would notice the change was wrong.

## Review shape

- raw 42 · confirmed 20 · refuted 22 · unverified 0 · precision 0.48
- confirmed by severity, as adjudicated in this report: 5 BLOCKER · 4 HIGH · 5 MEDIUM, over 14 rows
- confirmed blockers: 5 · confirmed highs: 4

Precision fell from 0.57 to 0.48, just under the ~0.5 floor §8 names, on a fan that was NOT widened.
The reading is not that priming got worse: this spec is 200 lines against unit 1's 330, and a
smaller, cleaner subject with fewer moving parts gives a fixed lens fan fewer real targets while
costing it none of its appetite. The 22 refuted were, as in both prior rounds, readings of the spec
text alone; every survivor was re-derived against the binary, the suite or a gate. Per §8 the lever
here is scope, not agent count, and round 2's advice stands.

**Four rows fold more than one finding, and are marked in place.** `B1 (with #2, #31)` is one census
defect filed twice; `B4 (with #11, #22, #34)` is one lexicon defect filed three times with one fix;
`B5 (with #14, #35)` is one unowned-carrier defect filed twice; `M4 (with #28, #4-cost)` is the cost
half of a split finding. Merging them is honest — rows asserting one fix should not inflate the
count a convergence condition is measured on.

**Severities here are this report's adjudication, not the finders' filings, and two moved.** Finding
`#4` was filed HIGH and is SPLIT: its artifact half (S7 names no obtainable baseline) is promoted
into blocker `B2`, because it is the same defect as `#32` and blocks the unit's only class guard;
its cost half is demoted into medium `M4`, because I measured the leg at roughly 200 s against a
declared ceiling of 740 in `tools/gate-legs.json` and there is no breach — the defect is unpriced
work, not a broken gate. Finding `#31` was filed BLOCKER and stays one, folded into `B1`.

## What was re-derived, and how

Every line anchor printed below was confirmed in this worktree at BASE `d65da7ab`:

| claim | how it was checked | result |
|---|---|---|
| which view each rule reads | `grep -n` over `tools/hooks/agent-cap.js` | `offendingLines` :84 · `fanoutFindings` :355 **and** :356 · `capFindings` :681 · `scanJoinFindings` :977 **and** :1004 |
| the four rule call sites | `sed -n` over `main()` | :1085 · :1105 · :1126 guarded by `ONLY === null`; :1157 **unguarded** |
| `--only` is a rule selector, not a view selector | `ONLY_RULES` at :1022 | closed set `["join"]` |
| rule 1's finding shape | :81 and :1130 | `{ line, n }` — no `why`; the formatter destructures `({ n, line })` |
| the suite's baseline | `bash tools/hooks/agent-cap.test.sh` | `---- 105 passed, 0 failed ----` |
| the four new names | `python tools/lexicon/lexicon.py --suggest <name>` | 3 of 4 refused: `strip`, `blank`, `union` are not declared verbs; only `render` is |
| the pin the leg grades against | `.lexicon.conf:158` | `VERB_OFFENDER_PIN="463"`, declared shrink-only |
| the leg's guard | `tools/gate-legs.json` | `lexicon naming predicates` guards `tools/`, `skills/session-kickoff/`, `.githooks/`, `.claude/` — this diff runs it |
| S7's DENY population, workflow half | all four `tools/workflows/*.js` fed to the hook as `Workflow` scripts | **all four exit 0** |
| the suite deploys to adopters | `tools/hooks/kit.toml:17-19` | `to = "{prefix}/hooks/agent-cap.test.sh"` |

## Findings

| # | Sev | Address | One line |
|---|---|---|---|
| B1 | BLOCKER | §2 S2 (with #2, #31) | two of four rules read TWO views; a single selector does not reproduce shipped behaviour |
| B2 | BLOCKER | §2 S7 · §6 AC4 (with #32, #4-artifact) | "the shipped hook" names a file that will not exist; in-tree it is a set-inclusion tautology |
| B3 | BLOCKER | §6 AC7 (with #3) | AC7 quantifies over "each S6 arm", so the property arm lands never observed RED |
| B4 | BLOCKER | §7 · §2 S1/S4 · §10 (with #11, #22, #34) | three of four new names are undeclared verbs; the leg §7 claims goes measurably RED |
| B5 | BLOCKER | §5 user docs (with #14, #35) | round-2 blocker 8's carrier half is in no unit's scope, and unit 2 lands last |
| H1 | HIGH | §6 AC1-AC3 · S6 (with #7) | every criterion observes only an exit code; rules 2 and 5 have no arm at all |
| H2 | HIGH | §2 S7 · §4 Measured (with #21, #33) | the corpus contains zero instances of the class S7 certifies |
| H3 | HIGH | §6 AC5 (with #5) | "reports 0 failed" with no pass-count floor — the green-by-absence class |
| H4 | HIGH | §3 vs §4 Measured vs §5 risks (with #15) | one measurement stated as `zero` and as `3` in the same file |
| M1 | MEDIUM | §6 AC6 vs §2 S1 (with #26) | "verbatim is the whole point" is asserted and nothing compares the bodies |
| M2 | MEDIUM | §4 Data model vs §2 S3/S4 (with #27) | the published composition line is wrong for rule 5's deliberately unguarded call site |
| M3 | MEDIUM | §4 Data model (with #25) | the union keys on `n` alone, and one line legitimately carries several findings |
| M4 | MEDIUM | §5 perf (with #28, #4-cost) | S7's wall cost is unpriced and its output shape unbounded |
| M5 | MEDIUM | §10 (with #29) | the reuse audit's stated evidence is false for the rule §4 uses as its example |

---

### B1 — BLOCKER — §2 S2 (and §4 Data model, which carries no correction)

*Folds finder findings #2 and #31.*

S2 gives each rule "a `shipped` selector choosing which view it reads" — singular — and justifies
rule 5's inclusion solely by "it reads `blankLiterals` too, at `agent-cap.js:977`". Two of the four
rules read TWO views each:

- `fanoutFindings` reads `renderCodeView` at `:355` **and** `stripStrings` at `:356`, in the
  `TOOL-aLexedStripper-5` fallback keyed on `view.unterminated`. S2 names no read at all for this
  branch.
- `scanJoinFindings` reads `blankLiterals` at `:977` **and** `stripStrings` at `:1004`, building the
  `${…}` interpolation span view. S2 names only `:977`.

Both unnamed reads are `stripStrings` — the function unit 1 re-bases. A selector wired only to the
named read leaves BOTH union branches of those two rules computing their second view with the NEW
stripper, and for half the rules the union stops being monotone.

Two live denials at BASE travel through exactly those reads. Rule 2 exits 2 on a script whose
trailing unterminated template forces the fallback (`unterminated = true` verified), where the
line-2 fallback view is `const u = ` + a template carrying a quoted `//` and then
`await Promise.all(all.map((f) => agent(f.p)))` — under unit 1's template-span-emitted-whole rule
that view truncates at the un-hidden `//` and the fan is gone. Rule 5 exits 2 on a same-line
template containing a quoted `'http://x'` before a `${m[f.ref]}` span, whose ban match exists ONLY in
the `stripStrings`-built span view; `blankLiterals` returns the template blanked to nothing.

Round 2's blocker 8 named this channel for rule 1. It arrives in two more rules that neither unit 1
nor this spec names. The prior art is unit 1's own S2, which round 1's `F25` already forced to be
corrected on this exact census — "`stripStrings` has THREE consumers, not one" — and `:1004` is the
consumer S2 misses here.

**Fix.** Rewrite S2 to say the selector switches the whole VIEW SET a rule reads, and enumerate the
six (rule, view, line) pairs explicitly: `offendingLines`/`stripStrings`:84 ·
`fanoutFindings`/`renderCodeView`:355 + `stripStrings`:356 · `capFindings`/`blankLiterals`:681 ·
`scanJoinFindings`/`blankLiterals`:977 + `stripStrings`:1004. Add an S6 arm per unnamed read and an
AC for each.

**Left-shift gate.** An arm in `tools/hooks/agent-cap.test.sh` that greps the source for
`stripStrings(`, `renderCodeView(`, `blankLiterals(` inside each rule function's body and asserts
every occurrence is selector-parameterised — a census the file checks about itself, so the next
repair cannot silently leave one read behind. This is the third round in which a hand-kept view
census has been wrong; per §7 the class, not the instance, is what needs gating.

---

### B2 — BLOCKER — §2 S7 and §6 AC4

*Folds finder finding #32 and the artifact half of #4.*

S7 and AC4 both compare against "the shipped hook", and the spec names no source for it. After this
unit lands, `tools/hooks/agent-cap.js` IS the union hook. There is no `--shipped-only` flag —
`ONLY` is a RULE selector over the closed set `["join"]` at `:1022`, and `main()` unions
unconditionally under S3. The rule functions are not exported. `tools/hooks/agent-cap.test.sh` (915
lines) carries no git-pinned baseline arm to lean on, and §4's Files touched names neither a pinned
blob nor a vendored copy.

So the arm is unimplementable exactly as written, and the implementation an author holding
`stripStringsShipped` would reach for compares the union against its own shipped arm. That is
`union(a, b) ⊇ b` — a set-inclusion tautology decided before any data is read, and it arms cleanly.
This repo has the class named and recorded: `memory/gotchas/assertion-between-two-derived-values.md`,
whose stated fix is "assert against something declared INDEPENDENTLY of the thing under test".

It is worse in an adopter. `tools/hooks/kit.toml:17-19` deploys `agent-cap.test.sh` to
`{prefix}/hooks/agent-cap.test.sh`, where no BASE blob of this repo's hook exists. The arm there
either errors or passes vacuously, and §7's "a skip must announce itself" is unaddressed.

**Fix.** Name the reference in S7: `git show d65da7ab:tools/hooks/agent-cap.js` into the harness's
`mktemp -d` with the sha written into the arm, or a vendored `tools/hooks/agent-cap.shipped.js`
added to §4's Files touched AND to `kit.toml`. State the adopter behaviour explicitly — the arm
SKIPS with a printed reason naming what it could not find, never silently.

**Left-shift gate.** Two arms. One asserts the reference blob resolves and its sha equals the one
written in the spec, failing loudly rather than skipping when it does not. One asserts the reference
hook and the landed hook DISAGREE on at least one known input — a liveness assertion in §7's sense,
so a reference that silently degraded into a second copy of the subject reds instead of passing.

---

### B3 — BLOCKER — §6 AC7, against §2 S7

*Folds finder finding #3.*

AC7's quantifier is "each S6 arm". S7's property arm — the one §2 calls "the class", and the one
§4's alternatives table makes the whole reason a fixture set was refused — is not an S6 arm, so
nothing in §6 requires its failing case to have been observed.

AGENTS.md §7 is verbatim binding here: "A new gate is not landed until its failing case has been
observed" and "A gate you have only ever seen pass is an assertion about nothing." AC4 only ever
asserts the passing value (the count is 0). A property arm that enumerates the wrong set, compares
the hook to itself (see B2), or returns early on a read error is indistinguishable from a working
one — and with AC5 carrying no pass-count floor (H3), nothing else in §6 notices.

The unit's entire monotonicity guarantee therefore rests on one check that lands never having been
seen to red.

**Fix.** Extend AC7 to "each S6 arm AND the S7 property arm", and name the staging: revert ONE
rule's selector to the new view only — rule 2's fallback at `:356` is the cheapest — confirm the arm
reds and NAMES that rule, restore. Record the observation under
`memory/builds/dMispairedQuote/build/` exactly as the S6 arms are.

**Left-shift gate.** The generalisation, which this build has now earned: a hygiene-style check that
every AC introducing a new gate arm has a sibling AC demanding an observed RED for it. Round 2's
`#13` and this round's B3 are the same omission at one level up.

---

### B4 — BLOCKER — §7 Gates, against §2 S1/S4 and §10

*Folds finder findings #11, #22 and #34. Measured, not inferred.*

§7 lists `lexicon naming predicates` among the legs this unit keeps green. S1 and S4 mandate four
new top-level definitions whose leading tokens are `strip`, `blank`, `render` and `union`. Three are
outside `.lexicon.conf`'s closed VERBS table:

```
python tools/lexicon/lexicon.py --suggest stripStringsShipped
  -> `strip` is not in the declared table, and no row bans it by name.
python tools/lexicon/lexicon.py --suggest blankLiteralsShipped
  -> `blank` is not in the declared table, and no row bans it by name.
python tools/lexicon/lexicon.py --suggest union
  -> `union` is not in the declared table, and no row bans it by name.
python tools/lexicon/lexicon.py --suggest renderCodeViewShipped
  -> OK — leads with `render`, which the declaration carries.
```

Appending the four definitions to both tracked copies (S5 mirrors every byte, and the probe grades
`.claude/hooks/agent-cap.js` too) moves the leg from `graded=1012 offenders=463`, which prints
`lexicon OK` and exits 0, to `graded=1020 offenders=469` with no OK line and exit 1:
`lexicon: verb offenders 469 over pin 463`. That is +8 graded for 4 definitions × 2 copies and +6
offenders for 3 × 2 — so the arrow spelling `const union = (a, b) => …` is graded identically. Files
restored after measuring.

`VERB_OFFENDER_PIN="463"` at `.lexicon.conf:158` is declared shrink-only and the leg is sitting
exactly on its floor. The leg's guard is `tools/`, `skills/session-kickoff/`, `.githooks/`,
`.claude/`, so this diff runs it, and §7's Definition of Done is
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — the whole bar green.

**This is the third instance of the same shape in this exact file.** `.lexicon.conf:151-157` records
the second: the `dTieredTribunal` fold (`2114c912`) added three P1 offenders in
`.claude/hooks/agent-cap.js` and "landed on main without moving this pin, so the
`lexicon naming predicates` leg was RED on main". Unit 1 handled the identical exposure explicitly —
its §10 records the `--suggest` consult, records that the refused rev-1 spellings moved offenders 463
to 467, and its AC11 pins the leg. Unit 3 has no scope item raising the pin, no AC over the leg, and
a §10 recording only the reuse probe and the recall terms.

**Fix.** Re-spell the three to declared verbs — `scanStringsShipped` / `renderLiteralsShipped`, and
`addFindings` or `mergeFindings` in place of `union`, adjusting S4's wording — or add a scope item
raising `VERB_OFFENDER_PIN` to 469 with the six added offender names listed inline, per the raise
convention `.lexicon.conf` itself states and demonstrates at `:116-157`. A pin that records a number
and loses what bought it is the one thing that convention exists to prevent. Add an AC mirroring
unit 1's AC11, and record the `--suggest` consult for all four names in §10.

**Left-shift gate.** The gate exists and works; what is missing is the DoR step. Make the naming
consult a required §10 line for any spec whose scope names a new top-level definition, checkable by
the hygiene gate: a spec introducing a backticked `function <name>` or `const <name> =` in §2 must
carry a `--suggest` verdict for it in §10. That converts a rule people forget into a check that
fails.

---

### B5 — BLOCKER — §5 user docs, against unit 2's §2 and §4

*Folds finder findings #14 and #35.*

Round-2 blocker 8 had two halves. The VERDICT half — the `//` inside a quoted span inside a same-line
template must still deny — unit 3 takes, as S6's third arm and AC3. The CARRIER half — its fix text
explicitly required "correct unit 2's S1 replacement text to cover template-borne quoted spans" —
unit 3 does not take, and neither does anyone else.

Unit 3's §5 delegates it in one prose bullet: unit 2 "carries the prose, extended to name this unit's
shipped-view block". Unit 2 cannot receive that. Its §2 is S1-S8 and none names a shipped-view block;
its §1 states its carrier list is "DERIVED from unit 1's files-touched, not authored", and unit 1's
files-touched contains no `*Shipped` block; its §4 Files touched lists none; and its §4 states
plainly that "Every S-item has its own acceptance clause in §6, because an AC pinning one edit of
eight certifies coverage this unit does not have" — so unit 3's added obligation would land with no
S-item and no AC in the sibling it is delegated to. Unit 2 is still rev-2; the round-2 fold commit
`c45f1c08` touched units 1 and 3 only.

The consequence is the exact sentence round-2 blocker 8 wrote. Unit 1's S3 has since narrowed its own
claim to "**No view hands a consumer a raw line outside a template span**, and the template case is
closed by `TOOL-dMispairedQuote-3`". Unit 2's S1 still writes the unqualified "its line is still
blanked, so no view ever hands a consumer a raw line" into the shipped header, and unit 2's AC1 pins
that wording. Unit 3 does not make it true: it unions rule RESULTS and changes nothing about what
`stripStrings` emits inside a same-line backtick span. So the build ships a second untrue ceiling, in
the carrier written to fix the first one — which the build README lists as expected improvement 3.
`memory/gotchas/amendment-leaves-its-other-half-standing.md` is selected by anchor for this diff.

**Fix.** Either add a scope item to unit 3's §2 that owns the ceiling text and the dossier residual
for the union mechanism, listing `memory/map/features/agent-cap.md` in §4's Files touched with an AC
pinning the corrected wording; or state in unit 3's §5 that unit 2 takes a rev bump whose carrier
list unit 3 names, amend unit 2's S1 and AC1 to unit 1's qualified form with a revision-log entry,
and record the dependency in the build README's ordering. A promoted blocker with half its fix
unowned is not closed.

**Left-shift gate.** A hygiene-style check over promoted blockers: when a review's disposition
promotes a finding, every clause of its recorded fix text must be traceable to an S-item in some
unit of the build. The machinery is already there — the round-2 record names the blockers, the specs
name their S-items, and `gen_build_index.py --print-bindings` already reads every record's bytes.

---

### H1 — HIGH — §6 AC1-AC3 and S6, against §2 S2

*Folds finder finding #7.*

Every criterion in §6 observes a process exit code, and no arm or criterion exercises rule 2
(`fanoutFindings`) or rule 5 (`scanJoinFindings`) at all — S6's three shapes are two rule-3 and one
rule-1. `main()` runs rule 2 (`:1085`), then rule 3 (`:1105`), then rule 1 (`:1126`), then rule 5
(`:1157`), each exiting 2 on the first non-empty list.

An exit code cannot say which rule denied. AC1 and AC2 are multi-line `boundedParallel(…, 50)` shapes
whose map receivers rule 2 also judges, so both can pass on a rule-2 denial while rule 3's selector
is unwired. S2 puts four rules in scope; an implementer wiring rules 1, 2 and 3 and leaving rule 5's
span view on the new stripper satisfies AC1, AC2, AC3, AC5, AC6, AC7 — and very likely AC4, since H2
shows AC4's population contains no script of the class. Half of S2 can be skipped with the whole
acceptance set green.

**Fix.** Assert the stderr message, not the exit code. The harness already has the helper: `msg()` at
`agent-cap.test.sh:336`, under a header at `:332` reading "EVERY ARM HERE ASSERTS ITS OWN MESSAGE,
never the exit code". Pin each arm to its rule's own banner text — "a verify/fan-out stage", "a bound
is written here", "raw parallel()/pipeline()", "a ref-keyed verdict join". Add one S6 arm and one AC
per rule, including the two rule-2 and rule-5 scripts named in B1, and cover `--only=join`, whose
call site is the one not guarded by `ONLY === null`.

**Left-shift gate.** An arm asserting that every rule in `main()` has at least one `msg()`-shaped arm
naming its banner — derived from the source, not from a list, so a fifth rule added later reds until
it is covered.

---

### H2 — HIGH — §2 S7, §4 Measured (last row) and §6 AC4

*Folds finder findings #21 and #33.*

S7 assumes the tracked corpus contains instances of the class it asserts over. It does not. Of 1264
tracked files fed whole to `tools/hooks/agent-cap.js` at BASE, exactly 41 exit 2 and 1223 exit 0. The
1223 are structurally incapable of a 2→0 flip. The 41 are the two `agent-cap.js` copies, three
`*.test.sh` files and 36 markdown records, README/protocol prose and archived template snapshots.
Not one is a workflow script: I fed all four `tools/workflows/*.js` — the corpus unit 1's own build
rule calls "the real corpus this hook reads" — and every one exits 0. None of S6's three reproduced
shapes appears anywhere in the 41.

So AC4's "the count of files moving from exit 2 to exit 0 is 0" is a criterion 97% of its stated
population cannot fail, and the remaining 3% contains zero instances of the defect class. Run against
the tracked corpus alone, the property arm would not have caught ANY of the three DENY-to-ADMIT moves
that caused this unit to exist. That is `memory/gotchas/fixture-passes-by-finding-nothing.md`, which
`python tools/memory-tree/gotchas.py --for-diff d65da7ab..HEAD` selects for this very diff — and it
is §7's could-not-fail shape one level up from the fixture set §4's alternatives table already
refuses.

There is a second half. Round-2 blocker 1's left-shift column specified a DIFFERENT gate: a per-LINE,
per-VIEW delimiter-conservation property — "for every corpus line, assert that the count of unescaped
`(`, `)`, backtick and `//` occurrences a view emits is ≤ what HEAD's view emits" — and blocker 8 said
the same arm covers its case if it counts `//`. Unit 1 measured that population at 86217 lines across
140 files. §4's Alternatives rejected has four rows and none of them rejects that property. A
whole-file exit-code sweep over 41 denials was substituted for a per-line property over 86217 lines,
and the substitution is nowhere argued.

**Fix.** Carry the specified per-line, per-view conservation arm as S7's class arm — it needs no
whole-hook reference (which also relieves B2) and its population is every line of every tracked source
file — or add a row to §4's alternatives table recording the measurement that rejected it. Either
way, state AC4's DENY population size in §4's Measured table beside the 1263, and give the property
real instances by injecting the S6 shapes into corpus files before feeding them.

**Left-shift gate.** Make S7 report its OWN population — the count of files that reach exit 2 under
the reference — and red when it is 0 or falls below a pinned figure. §7 requires that liveness
assertion of any signal, and it is precisely what would have caught this.

---

### H3 — HIGH — §6 AC5

*Folds finder finding #5.*

AC5 is "reports 0 failed" and nothing else. The harness prints `---- $pass passed, $fail failed ----`
at `agent-cap.test.sh:914` and exits on `[ "$fail" = 0 ]` at `:915`. It reports 105 passed / 0 failed
at BASE — the exact baseline §4's Measured table already publishes.

So a suite in which the S6 arms and the S7 arm were written but never invoked, or whose corpus arm
returned before asserting, prints `0 failed` and satisfies AC5. That is the green-by-absence class
AGENTS.md §7 names and this repo's own memory records twice. AC7 partially covers the S6 arms by
demanding a RED observation, which is exactly why the uncovered S7 arm (B3) slips through here.

Unit 1's sibling criterion carries the floor this one drops: its AC7 reads "0 failed AND a pass count
strictly above 105, the count recorded at BASE". The fix is already written down one file over.

**Fix.** Restate AC5 as: `bash tools/hooks/agent-cap.test.sh` reports 0 failed AND a pass count of at
least 105 plus the three S6 arms plus the S7 arm, with the expected number written into the criterion.

**Left-shift gate.** A ratchet in the suite itself: a `PASS_FLOOR` constant the runner asserts against
its own final count, raised in the same commit that adds arms. That makes de-collection impossible to
land silently rather than merely discouraged.

---

### H4 — HIGH — §3 third non-goal, against §4 Measured and §5 risks

*Folds finder finding #15.*

Three statements about one measurement, in one file:

- §3: the new view's false positives "are measured at zero over the tracked corpus".
- §4 Measured: "1263 files, **0 flips to ADMIT**, 3 flips to DENY, all markdown records".
- §5 risks: "the union inherits BOTH views' false positives. Measured: 3 flips to DENY over 1263
  tracked files, every one a markdown review record and none a workflow script."

§5 reports the inherited false-positive count as 3 over the same corpus §3 calls zero. By unit 1's own
§3 definition — rule 1 denying a primitive written in a lens PROMPT is "a FALSE POSITIVE" — a newly
denied markdown review record IS a false positive. "None a workflow script" is a mitigation argument,
not a zero. The sentence licensing the entire non-goal is the one the spec contradicts elsewhere, and
a reviewer of the next round cannot tell whether the 3 are accepted false positives or claimed true
positives.

**Fix.** Pick one and say it once. Either restate §3 as "the new view adds 3 measured denials over the
tracked corpus, all markdown records, and reducing them is out of scope", or classify the 3 as true
positives in §5 and drop them from the risks bullet. Do not leave `zero` and `3` describing the same
1263-file run in two sections of one file.

**Left-shift gate.** Not gateable as prose. It joins the recurring-class checklist as: *a number
stated in one section and re-stated in another is two answers to one question* — the §6 "a value
stated in prose beside the source that OWNS it rots" rule applied within a single document. The
mechanical version is to publish the figure once, in §4's Measured table, and have every other
section point at it.

---

### M1 — MEDIUM — §6 AC6, against §2 S1

*Folds finder finding #26.*

S1 calls verbatim "the whole point" and §3's first non-goal exists to protect it, but nothing checks
it. AC6 asserts only that `grep -c 'function stripStringsShipped'` reports 1 and that the two file
copies diff empty. No criterion and no leg in §7 compares the three `*Shipped` bodies against the same
functions at BASE `d65da7ab`.

A `*Shipped` copy that drifts — reformatted, written from unit 1's corrected implementation by
mistake, or later tidied by someone reading three near-duplicate functions as dead weight — passes
every criterion in §6 while silently deleting the monotonicity guarantee, because the union's shipped
arm becomes a second copy of the new arm. H2's measurement shows the corpus property will not catch it
either.

**Fix and left-shift gate (the same thing here).** Add an arm that extracts each of the three
functions from the BASE blob and byte-compares it, modulo the name token, against its `*Shipped`
twin, with the pinned sha in the arm; stage it RED by perturbing one body. Without it S1 is a comment,
not a constraint. This shares the reference-blob machinery B2 needs, so the two fixes are one piece of
work.

---

### M2 — MEDIUM — §4 Data model, against §2 S3 and S4

*Folds finder finding #27.*

§4 publishes ONE composition line carrying the `ONLY === null ? … : []` guard, and S4 calls `union`
"one function … used by all four call sites". The four call sites do not share that shape:
`fanoutFindings` at `:1085`, `capFindings` at `:1105` and `offendingLines` at `:1126` are guarded;
`scanJoinFindings` at `:1157` is UNGUARDED, deliberately, because `--only=join` is a closed selector
(`ONLY_RULES = ["join"]` at `:1022`) whose entire purpose is to run that one rule.

Copying the published line onto rule 5's call site makes `--only=join` return `[]` and exit 0 for
every script. Nothing in the suite catches it: the rule-5 denial arms at `:71`, `:75` and `:79` run
unfiltered and still deny, and the one `--only=join` arm at `:107` asserts exit 0.
`tools/workflows/check-review-join.sh:94` drives the hook with `--only=join` over its whole
population, so the leg goes vacuously green — the vacuous-selector-over-an-empty-population class
`main()`'s own comment at `:1018-1021` names, and that `tools/check-wiring.sh:149` exists to catch in
`settings.json` but cannot catch inside the hook.

**Fix.** Split the composition rule in S3: rules 1-3 keep the `ONLY === null` guard, rule 5 unions
unconditionally, and §4 publishes both lines.

**Left-shift gate.** An arm asserting `--only=join` still DENIES a ref-keyed join after the union
lands, paired with one asserting `--only=join` exits 0 on a script carrying a raw `parallel(` and no
join. The pair is what distinguishes a working selector from a dead one.

---

### M3 — MEDIUM — §4 Data model, against §5 observability

*Folds finder finding #25.*

The union is keyed on `n` alone, on the premise that a line number identifies a finding. It does not.
`capFindings` pushes several findings at one `n`: the call-site pass is `while ((m = HELPERS.exec(l)))`
over every helper call on a line (`:721-746`), and the default-parameter pass (`:717`) and the marker
pass (`:752-772`) push independently at their own `i + 1`. §4 states no tie-break and its published
call order puts the NEW view first — `union(offendingLines(script), offendingLines(script, true))`.

On a collision a naive `n`-keyed merge keeps the new view's row and drops the shipped one, which
contradicts §5's "a finding reported from the shipped view carries that view's own explanation, which
is the message an operator sees today". That is mechanical, not cosmetic: the rule-3 arms all go
through `msg()`, which greps stderr for an exact needle, and `main()` prints only `slice(0, 6)`, so a
doubled list can push the shipped row out of the printed set and leave an operator without the line to
fix.

**Fix.** State the tie-break in §4 — shipped view wins a collision, shipped rows ordered first — and
key on `(n, why)` so two genuinely distinct findings at one line both survive.

**Left-shift gate.** An arm over a line carrying two helper calls asserting BOTH explanations reach
stderr, and one over a shipped-view finding at a line the new view also flags asserting the SHIPPED
`why` is the emitted text.

---

### M4 — MEDIUM — §5 perf / scale, against §2 S7

*Folds finder finding #28 and the cost half of #4.*

§5 prices only "every rule runs twice" and offers "the shipped suite's wall time is the observation" —
a measurement of a suite that does not contain S7. S7 is the expensive half and is unpriced.

Measured on node d, and the readings vary as this node's recorded AV tax predicts: one pass of the
hook over all 1264 tracked files is 62-99 s across runs, so two hooks is roughly 130-200 s, against a
shipped suite that currently runs in about 21 s and a `ceiling` of 740 declared for
`agent-cap self-test` in `tools/gate-legs.json`. That is roughly a tenfold growth in the leg and it is
stated nowhere. **It is not a breach** — this is why the finding is a medium and not the high it was
filed as: §7's cost-is-a-verdict rule is satisfied by 200 against 740. The defect is that the figure
was never taken.

The second half is the output shape. If the arm is written as one `check`/`js` call per file it emits
1263 `ok` lines and increments `pass` 1263 times, which blows up the pass count unit 1's AC7 pins as
"strictly above 105" and turns the suite's output into scrollback.

**Fix.** State in S7 that the property arm is ONE arm — it accumulates per-file verdicts and reports a
single `ok`/`FAIL` line carrying the flip count — and give §5 a measured wall figure against the
declared 740 s ceiling. Drive the corpus loop from a single process rather than one `node` plus one
python per file if the figure does not fit.

**Left-shift gate.** The ceiling already exists and the runner already reds on breach; what is missing
is the DoR habit of measuring a new arm before specifying it. Add the measured seconds to §4's
Measured table so the next revision can see the number move.

---

### M5 — MEDIUM — §10 Reuse audit

*Folds finder finding #29.*

§10 justifies the reuse decision on the claim that the file's rule-function signature "already carries
the finding shape (`{ n, line, why }`) the union keys on". One of the four does not. `offendingLines`
returns `{ line, n }` with no `why` — it is built by `.map((line, i) => ({ line, n: i + 1 }))` at
`:81` — and `main()`'s rule-1 formatter destructures only `({ n, line })` at `:1130`. The other three
rules do carry `why` (`:1085`, `:1111`, `:1008`).

The mechanism survives, because §4 pins the union key as `n`, which every finding does carry. What is
wrong is the reuse audit's published evidence for "the merge is four characters of selector and one
helper", and it is false for exactly the rule §4 uses as its worked example. A `union` written to the
published three-field shape reads `undefined` for every rule-1 row; since rule 1 is the one rule that
never prints `why`, a union that de-duplicates on the presence of `why`, or logs it, degrades silently
and no criterion in §6 notices.

**Fix.** Correct §10 to state the actual shapes — `{ n, line }` for rule 1, `{ n, line, why }` for
rules 2, 3 and 5 — and say in §4 that `union` reads `n` only and copies rows opaquely, so the missing
field is a non-issue by construction rather than by luck.

**Left-shift gate.** None warranted on its own; M3's `(n, why)` keying arm covers the mechanical
residue, and the §10 correction is prose.

## Exit condition for round 2

Round 1 sets the ceiling at **5 confirmed blockers**. Per BUILD-METHOD M4 the loop continues only on a
strictly falling confirmed-blocker count; a round 2 that does not come in under 5 stops the loop and
disposes every standing blocker rather than re-reviewing it.

Two notes for whoever writes the fold, because this build has now twice produced a fold that was worse
than what it replaced:

- **B1, B2, B3, M1 and H2 are one piece of work, not five.** All five are about the reference against
  which the union is proved monotone. Pinning the BASE blob once buys B2's baseline, M1's verbatim
  comparison and part of H2's population, and correcting the S2 census (B1) plus extending AC7 (B3)
  is then cheap. Fold them together or the fold will fix them independently and inconsistently.
- **`fold-text-is-unreviewed-surface` is selected for the fold diff by name.** Round 2 landed eight
  findings in sentences that did not exist at rev-1, four of them blockers. The rev-2 prose of this
  spec is the least-reviewed text in the build the moment it is written, and round 2 should hunt it
  first rather than re-reading rev-1.
