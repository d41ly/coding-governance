**Serves:** spec-audit TOOL-dMispairedQuote-3

# Spec audit round 2 — `TOOL-dMispairedQuote-3`, and the subject is the FOLD

*Node d, 2026-09-01, round 2. The subject of this round is the FOLD. Rev-2 is fresh prose nobody has
reviewed, written to close round 1's 5 blockers, 4 highs and 5 mediums, and the two bug classes this
repo's own checklist selects for a diff of this shape are `fold-text-is-unreviewed-surface` and
`amendment-leaves-its-other-half-standing`. Both were hunted first and both landed — one blocker
apiece. No code has been written; the spec is the PLAN and is audited as a design. Units 1 and 2 were
read as context and carry no finding of their own this round, though one finding below names a
collision that must be settled in one of them. Every surviving finding was re-derived in this
worktree against `tools/hooks/agent-cap.js` at BASE `d65da7ab`, against its shipped suite actually
run, against the whole tracked corpus actually swept, or against a gate actually run.*

Reviewed subject, pinned at the blob actually read:

- `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md@87154517637a8063ead1eefde2c23f0e2c9361de`

Context read, not reviewed: unit 1 at rev-3, unit 2 at rev-3, the build `README.md`, and round 1's
record over this unit.

Round 2.

## Verdict: BLOCKED

Two confirmed blockers, four highs and two mediums, presented as 8 rows over 18 confirmed findings.

**The fold is genuinely better than what it replaced, and this is worth saying before the bad news.**
The threaded selector became a dispatcher, which does not merely fix round 1's B1 — it dissolves the
census B1 was about. The property arm now reads a sha-pinned BASE blob instead of an in-tree copy,
which closes B2 as filed and takes the assertion-between-two-derived-values class off the board. The
`zero`-versus-`3` contradiction is gone. Unit 2 took the orphaned carrier half and is now rev-3. Nine
new names were consulted against the declaration and all nine answer OK — I re-ran every one. Six of
round 1's fourteen rows are closed properly.

**And both blockers are the same defect the fold was written to close.** Round 1's B3 said the unit's
only class-level guard lands never having been observed RED. Rev-2 answered it by extending AC10's
quantifier to name the property arm — and then specified a staging that cannot produce the RED it
demands, because nothing in the spec measures a tracked file that flips DENY-to-ADMIT under unit 1
alone, and round 1's own H2 measured that the corpus contains no instance of the class. I swept all
1265 tracked files against the hook myself: 42 deny, and they are 37 markdown records, 3 `.sh` test
files and the two `agent-cap.js` copies. Not one workflow harness. B3 is reworded, not closed. That
is blocker one.

Blocker two is the other named class, arriving through the fold exactly as the checklist predicts.
The fold made two independent repairs and did not check them against each other. S2's dispatcher
carries the bolded justification **"no rule function changes at all"**. S6's lexicon repair requires
`stripStrings` and `blankLiterals` to stop existing — and those two names are read from inside four
rule bodies at five lines, which I re-derived at `:84`, `:356`, `:681`, `:977` and `:1004`. Rename
them and S2's sentence is false and the implementer is back to hunting five reads, which is the
hand-kept census S2 exists to abolish and which round 1 measured wrong for two of the four rules —
including `:356` and `:1004`, both in this set. Keep them and S6's offender drain is zero and AC9's
figure is unreachable. Two sentences in one section specifying mutually exclusive designs, and the
cheaper reading silently restores round 1's B1.

**A third shape runs through the highs and is the real lesson of this round: the fold kept each
fix's headline and dropped its operative clause.** Round 1's H3 asked for "105 plus the three S6 arms
plus the S7 arm, with the expected number written into the criterion"; AC8 kept the 105 and dropped
the addition, so its floor now sits below the count unit 1's own AC7 already guarantees and cannot
fail. Round 1's M1 asked for a byte comparison "staged RED by perturbing one body"; S10 took the
comparison and AC10 left the byte arm out of its observed-RED quantifier — the same defect the fold
closed one row up, re-created one row down. Round 1's M3 asked for the `(n, why)` key AND the merge
order; S4 took the key. Round 1's H1 asked that arms assert the message rather than the exit code;
AC2 through AC5 do, and AC1 does not — and I reproduced AC1's own fixture denying through rule 2,
not the rule 3 it is labelled.

Round 1 closed with a warning that this build had twice produced a fold worse than what it replaced.
That did not happen here — this fold is better. What happened instead is subtler and is the thing to
carry into the next one: **every one of these six defects is a fix whose measurable half was
dropped.** The spec is now consistently good at naming the right repair and consistently poor at
keeping the clause that would let anyone tell whether the repair worked. That is the same complaint
round 1 filed as "the defect is never in the mechanism and always in what observes it", one level
further in.

## Review shape

- raw 34 · confirmed 18 · refuted 16 · unverified 0 · precision 0.53
- confirmed by severity, as adjudicated in this report: 2 BLOCKER · 4 HIGH · 2 MEDIUM, over 8 rows
- confirmed blockers: 2 · confirmed highs: 4

Precision rose from 0.48 to 0.53, back over the ~0.5 floor §8 names, on a fan that was not widened.
The reading is the one round 1 offered in reverse: the fold added measurable claims — figures, counts,
a pinned sha, a named population — and measurable claims give a lens real targets instead of prose to
argue with. Every survivor was re-derived against the binary, the suite, the corpus or a gate; the 16
refuted were, as in all three prior rounds, readings of the spec text alone.

**Five rows fold more than one finding, and are marked in place.** Merging them is honest — rows
asserting one fix should not inflate the count M4's convergence condition is measured on. Row 2 folds
`#12`, `#20` and `#30`, one blocker filed three times. Row 4 folds `#3`, `#14`, `#23` and `#32`, one
floor defect filed four times. Row 5 folds `#4`, `#13`, `#21`, `#31` and `#18`, one lexicon
measurement filed four times plus its unowned-pin half. Row 1 folds `#28` and `#24`. Row 3, row 6,
row 7 and row 8 each carry one finding.

**Severities here are this report's adjudication, not the finders' filings, and two moved.** `#24`
was filed MEDIUM and is promoted into blocker row 1, because it is the same defect as `#28` and the
pair blocks the unit's central design decision. `#18` was filed MEDIUM and is subsumed into high row
5, because its fix is one edit set with the figure correction and filing it separately would price
one piece of work twice.

## What was re-derived, and how

Every figure and line anchor printed below was measured in this worktree at HEAD `47067d68`.
`git diff --stat d65da7ab..HEAD -- . ':!memory'` is **empty**, so every tracked file outside `memory/`
is byte-identical to BASE and the hook I ran IS the BASE blob.

| claim | how it was checked | result |
|---|---|---|
| the tracked corpus | `git ls-files \| wc -l` | 1265 |
| the at-risk population | every tracked file fed whole to the hook | **42 DENY** — 37 `.md`, 3 `.sh`, 2 `.js` |
| its composition | the 5 non-markdown members | both `agent-cap.js` copies, `agent-cap.test.sh`, `check-review-join.test.sh`, `check-verifier-fanout.test.sh` |
| whether any harness denies | all four `tools/workflows/*.js` fed to the hook | **all four exit 0** |
| the P1 verb census | `python tools/lexicon/lexicon.py --check` | `graded=1012 offenders=463`, `lexicon OK` |
| the two view offenders | `python tools/lexicon/lexicon.py --list` | `stripStrings:70` and `blankLiterals:601` in **BOTH** copies — 4 rows, 17 offender rows per copy |
| the nine new names | `--suggest` run on each | **all nine OK** — `render` and `run` are declared |
| the leg's RED condition | `tools/lexicon/lexicon.py:697` | `if len(unwaived) > pin:` — a FALL leaves the leg green |
| the pin | `.lexicon.conf:158` | `VERB_OFFENDER_PIN="463"`, declared shrink-only |
| the suite baseline | `bash tools/hooks/agent-cap.test.sh` | `---- 105 passed, 0 failed ----` |
| unit 1's floor | unit 1 spec `:241-242` | AC7 — "0 failed and a pass count **strictly above 105**" |
| landing order | the three status headers | unit 1 order 1 · unit 3 order 2 · unit 2 order 3, now rev-3 |
| AC1's own fixture | built verbatim and fed to the hook | exits 2 via **RULE 2** (`a verify/fan-out stage`), not rule 3 |
| `main()`'s rule order | `sed -n '1075,1170p'` | rule 2 `:1085` · rule 3 `:1105` · rule 1 `:1126` · rule 5 `:1157`, **unguarded** |
| the view reads inside rules | `grep -n` | `stripStrings` :84 :356 :1004 · `blankLiterals` :681 :977 · `renderCodeView` :355 |
| the printed truncations | `grep -n 'slice(0, 6)'` | :1091 · :1111 · :1129 · :1164 |
| the `addc6169` comment | `sed -n '287,312p'` | `:301-306`, INSIDE `renderCodeView`'s quote branch, ends "and so does this now" |
| `agent-cap self-test` | `tools/gate-legs.json` | ceiling **740** · `subject = kit` · `chunk = selftests` · guards `tools/hooks/`, `tools/lib/` |
| `lexicon naming predicates` | `tools/gate-legs.json` | `subject = repo` · guards include `tools/` and `.claude/` — this diff runs it |

§7's gate claims survive this check: the self-test leg really is `subject = kit` and `chunk =
selftests`, so it really is held off an ordinary bar, and the Definition of Done really does need
`GATE_FULL=1 GATE_SELFTESTS=1`. The 740 s ceiling is real and the measured 161 s is nowhere near it.

## Round 1's fourteen rows — closed, or reworded?

The mandate for this round is that a priorFinding is CLOSED by the fold rather than reworded. Six of
fourteen are closed. Here is each one.

| round-1 row | what rev-2 did with it | status |
|---|---|---|
| **B1** census wrong for 2 of 4 rules | replaced the selector with a DISPATCHER — a better fix than B1 asked for, because it dissolves the census rather than correcting it | CLOSED IN MECHANISM, **RE-OPENED BY S6** (row 1) |
| **B2** no obtainable baseline; in-tree tautology | S9 reads `git show <BASE>:tools/hooks/agent-cap.js` into a temp file, names the degradation class by name, AC6 writes the sha, AC11 specifies the skip | **CLOSED** |
| **B3** property arm lands never observed RED | AC10's quantifier extended to name it — and the staging it names cannot produce the RED | **REWORDED, NOT CLOSED** (row 2) |
| **B4** three of four names undeclared verbs | all names re-spelled; I ran `--suggest` on all nine and all nine answer OK | naming half **CLOSED**; the arithmetic and the pin move are not (row 5) |
| **B5** carrier half in no unit's scope | unit 2 bumped to rev-3; its S1 now carries the template-span exception and names unit 3 | **CLOSED** — and it produced row 8 |
| **H1** exit codes only; rules 2 and 5 unarmed | AC2-AC5 each assert "the message names …"; rules 2 and 5 get arms; S8 covers rule 5 | **CLOSED FOR FOUR OF FIVE** (row 6) |
| **H2** corpus holds no instance of the class | the population is now stated (42) — but the instances were never supplied | **NOT CLOSED** (row 2) |
| **H3** no pass-count floor | AC8 gained a floor, keyed to BASE rather than to the arms | **REWORDED, NOT CLOSED** (row 4) |
| **H4** `zero` and `3` for one measurement | §3, §4 and §5 all read `3`, and §5 says so explicitly | **CLOSED** |
| **M1** verbatim asserted, nothing compares | S10 + AC7 byte-compare each body against the BASE blob | mechanism **CLOSED**; the observed-RED clause was dropped (row 3) |
| **M2** rule 5's unguarded call site | S5 names the asymmetry and preserves it deliberately; AC5 covers `--only=join` | **CLOSED** |
| **M3** merge keys on `n` alone | S4 keys on `n` **and** `why` | key half **CLOSED**; the ordering half was dropped (row 7) |
| **M4** the property arm's cost unpriced | 140 s sweep and 161 s leg against the declared 740 s, in §4, §5 and §7 | cost half **CLOSED**; see the note below |
| **M5** §10's finding shapes wrong | §10 now states `{ n, line, why }` for three rules and `{ line, n }` for rule 1 | **CLOSED** |

One residual worth naming that no finder confirmed and that I therefore do not file as a row. M4 had
a second half — "state in S7 that the property arm is ONE arm … a single `ok`/`FAIL` line carrying the
flip count" — and S9 still says nothing about its output shape. It matters only because it interacts
with row 4: if the arm emits one `ok` per file, the suite's pass count jumps by 1265 and every floor
argument below changes shape. §4's Measured row implies one arm, since it reports the candidate suite
at 105. Settle it in S9 in one clause while fixing row 4.

## Findings

| # | Sev | Address | One line |
|---|---|---|---|
| 1 | BLOCKER | §2 S2 vs §2 S6 · §4 · §10 | the dispatcher's justification and the lexicon drain specify mutually exclusive designs |
| 2 | BLOCKER | §6 AC10 vs §2 S9 · §4 Measured | the property arm's demanded RED is over a population measured to contain no instance |
| 3 | HIGH | §6 AC10 vs §2 S10 | the byte arm is not in AC10's observed-RED quantifier — B3 re-created one row down |
| 4 | HIGH | §6 AC8 vs S8/S9/S10 · unit 1 AC7 | the pass floor sits below what the previous unit already guarantees |
| 5 | HIGH | §2 S6 · §4 Measured · §4 Files touched · §6 AC9 | `461` is unreachable — the leg grades both copies, so the value is `459`, and the pin move is unowned |
| 6 | HIGH | §6 AC1 vs AC2-AC5 | the one criterion that kept the exit code is the one whose fixture denies through another rule |
| 7 | MEDIUM | §2 S4 vs §5 observability | the merge key was taken and the merge ORDER dropped, so §5's promise is unsecured |
| 8 | MEDIUM | §2 S1/S10 vs §3 · unit 2 S4/AC3 | the byte-frozen body carries the comment unit 2 lands last to rewrite |

---

### 1 — BLOCKER — §2 S2, against §2 S6, §4 Data model and §10

*Folds finder findings `#28` and `#24`.*

S2 is the fold's central decision and it carries a bolded justification: the three view NAMES every
rule already calls become one-line dispatchers, and **"no rule function changes at all"**. That
sentence is the whole argument for the dispatcher over the threaded flag — it is what buys the
abolition of the census round 1 measured wrong.

S6 is a different repair, made to close round 1's B4, and it says the two dispatchers "take the place
of the file's two existing verb offenders". `python tools/lexicon/lexicon.py --list` names those two
exactly: `stripStrings` at `:70` and `blankLiterals` at `:601`. So S6 can only happen if those two
names cease to exist. Re-derived at BASE, they are read from inside the rule bodies at five lines:

- `stripStrings` — `:84` (rule 1), `:356` (rule 2's `view.unterminated` fallback), `:1004` (rule 5's
  interpolation span view)
- `blankLiterals` — `:681` (rule 3), `:977` (rule 5)
- `renderCodeView` — `:355`, already `render`-led and the one view needing no respelling

Both horns are bad. **Rename**, and five in-rule lines change, S2's bolded sentence is false, and the
implementer must find all five reads — which is precisely the hand-kept census S2 exists to abolish,
and which round 1 measured wrong for two of the four rules. The two it missed were `:356` and
`:1004`, both in this set, and both on fallback branches where a missed read is a latent
`ReferenceError` on a rarely-taken path rather than a visible failure. **Keep the names**, and S6's
drain is zero, the pin does not fall, and AC9's figure is unreachable.

The rest of the spec points at the rename — §4's data model names the dispatcher `renderStrippedView`,
§10 consults nine new names and retains neither old one, AC9 pins a fallen figure — so the design is
recoverable by inference. What is not recoverable is the justification: an implementer who takes S2's
bold sentence at its word keeps the dispatchers named `stripStrings` and `blankLiterals`, and the
cheaper reading is the one that silently restores B1. One mitigation, which is why this is a blocker
about the spec and not a prediction of a shipped bug: AC9 pins a figure the keep-the-names reading
cannot produce, so the contradiction would eventually surface at the Definition of Done — as a
confusing red on a naming gate, three sections away from the sentence that caused it.

**Fix.** Decide it in S2 and say which. Either (a) the dispatchers KEEP the called names, the shipped
and lexed bodies take the new `render*` names, no rule body changes, S2's sentence stands as written,
and S6's pin-falls claim and AC9's figure are deleted because nothing drains; or (b) own the rename in
its own S-item that enumerates the five reads by line — `:84 · :356 · :681 · :977 · :1004` — restate
S2 as "no rule function's LOGIC changes; the only edit inside a rule body is the callee name", and
carry one AC per read asserting it resolves to the dispatcher. Do not leave both sentences standing.

**Left-shift gate.** The arm round 1 specified for B1, which the dispatcher made look unnecessary and
option (b) makes necessary again: an arm in `tools/hooks/agent-cap.test.sh` that greps each rule
function's body for every view call and asserts each one resolves to a dispatcher name — a census the
file keeps about itself, so the next repair cannot leave one read behind. It is the third round in
which a hand-kept view census has been wrong; per §7 the CLASS is what needs gating, not the
instance. The spec-level companion is a `TEMPLATE-SPEC` check: a scope item that renames an existing
top-level definition must enumerate its call sites by line, which converts "find all five" from a
memory task into a written, checkable list.

---

### 2 — BLOCKER — §6 AC10, against §2 S9 and §4 Measured

*Folds finder findings `#12`, `#20` and `#30`. This is round 1's B3, reworded.*

AC10 requires the S9 property arm, "staged against a tree carrying unit 1 WITHOUT this unit", to
FAIL. It even carries the reason in its own text: "a class-level guard that has never been observed
RED is §7's own could-not-fail shape". The clause is right. The staging it names cannot deliver it.

S9's arm ranges over tracked files only, comparing each file's verdict under the BASE blob against
its verdict under the built hook. For that arm to go RED on a unit-1-alone tree, some tracked file
must flip DENY-to-ADMIT under unit 1 alone. **Nothing in the spec measures that.** §4's Measured table
has exactly one unit-1-alone row — the three hand-written fixtures — and its whole-corpus row is
BASE-versus-candidate, reporting `0 flips to ADMIT` by construction. The one measurement that would
settle AC10 is the one measurement §4 does not take, in a table whose header states that every row was
run rather than estimated.

I swept the corpus myself rather than rely on the filing. Feeding all 1265 tracked files whole to the
hook reproduces the spec's own figure exactly — **42 DENY** — and the composition is the problem:

- 37 markdown records (review records, protocol prose, archived template snapshots)
- 3 `.sh` files — `tools/hooks/agent-cap.test.sh`, `tools/workflows/check-review-join.test.sh`,
  `tools/workflows/check-verifier-fanout.test.sh`
- 2 `.js` files — the two copies of `agent-cap.js` itself

**Not one `tools/workflows/*.js` harness.** I fed all four directly and every one exits 0. Round 1's
H2 measured the same population one file smaller (41 of 1264) and recorded that the arm "would not
have caught ANY of the three DENY-to-ADMIT moves" — the three reproduced shapes are synthetic
fixtures, and §4's Files touched adds no tracked fixture that would put one into the corpus. There is
a second reason the 42 cannot help: a whole-file exit-code comparison cannot flip a file that carries
any OTHER denial, and the two `agent-cap.js` copies and the three `*.test.sh` files are dense with
them.

So AC10's property clause quantifies over an event nothing has measured and round 1 measured as
having no instance. Two outcomes, both bad, and §7 rules on both: the arm lands never having been
observed RED — "A gate you have only ever seen pass is an assertion about nothing" — or the builder
improvises an undocumented staging to make the criterion pass, which is this repo's
`staged-break-substitutes-a-synthetic-value` class. In the unit whose entire product is a check, and
whose §4 alternatives table refuses a fixture set precisely because §7 says gate the CLASS, the
class-level guarantee then rests on S8's five hand-written fixtures.

Round 1 wrote the clause that closes this — H2's fix said "give the property real instances by
injecting the S6 shapes into corpus files before feeding them", and B3's fix named a staging that
works (revert ONE rule's dispatch, confirm the arm reds and NAMES that rule). Neither clause appears
in any S-item or AC at rev-2.

**Fix.** Three edits, all small. Add a Measured row for the corpus swept under unit 1 ALONE and
publish the DENY-to-ADMIT count it produces; if it is zero, say so in the table, because that is the
finding. Extend S9's swept population with the five S8 fixture scripts and the three reproduced
shapes as synthetic corpus members, so the property has real instances and can be observed RED, and
re-point AC10 at that population. And take round 1's alternative staging as the cheap
belt-and-braces: reverting one rule's dispatch must red the arm and NAME that rule.

**Left-shift gate.** The liveness assertion §7 requires of every signal, which round 1 specified for
this exact arm and rev-2 did not adopt: the property arm reports its OWN population — the count of
files reaching exit 2 under the reference — and REDS when that count is zero or below a pinned figure.
An arm that sweeps a corpus containing no instance of its class then says so instead of printing a
reassuring pass. The spec-level companion, which this build has now earned twice over: a
`TEMPLATE-SPEC` check that every AC demanding an observed RED names the staging that produces it, so
"it FAILS when staged" can never again be written without a stated way to stage it.

---

### 3 — HIGH — §6 AC10, against §2 S10 and §4

*Folds finder finding `#2`. This is B3 re-created one row down.*

AC10's quantifier is "each arm from S8 **and** the property arm from S9". S10's byte arm — the arm
this fold introduced, to close round 1's M1 — is not in it.

The fold closed B3 for the S9 arm and re-opened the identical defect for the new S10 arm in the same
sentence. Nothing else in §6 notices: AC7 only ever asserts the passing value (the bodies are equal),
and AC8's floor cannot fail for reasons row 4 gives. A byte arm that extracts the wrong function,
matches nothing, or returns early on a read error passes identically to a working one.

Round 1's M1 carried the missing clause verbatim — "stage it RED by perturbing one body" — and that
clause did not survive into the fold. Unlike row 2's arm, this RED is trivially obtainable: change one
character inside one `renderShipped*` body and the comparison must fail. So this is a pure omission
rather than a measurement problem, which is why it is a high and not a second blocker.

**Fix.** Extend AC10 to "each arm from S8, the property arm from S9 **and the byte arm from S10**",
and name the perturbation: change one character inside one `renderShipped*` body, confirm the arm reds
and NAMES which of the three bodies drifted, restore. Record the observation under
`memory/builds/dMispairedQuote/build/` with the others. The "names which body" clause is worth its
words — a byte arm reporting only "unequal" over three functions costs the reader the diff.

**Left-shift gate.** The generalisation round 1 already proposed and this round earns a second time: a
hygiene-style check that every S-item introducing a new gate arm has a sibling AC demanding an
observed RED for it, derived from the spec's own S-items rather than from a hand-kept list. Round 1's
B3 and this row are the same omission at one level up, and a hand-written quantifier that must
enumerate every arm is a census — the same shape row 1 is about.

---

### 4 — HIGH — §6 AC8, against §2 S8/S9/S10 and unit 1's AC7

*Folds finder findings `#3`, `#14`, `#23` and `#32`. This is round 1's H3, reworded.*

AC8 asks for "0 failed and a pass count of at least 105, the count measured at BASE". I ran the suite:
`---- 105 passed, 0 failed ----`. The number is right and the baseline is two units too early.

Unit 3 is order 2 and lands on top of unit 1, whose own AC7 already demands "a pass count **strictly
above 105**, the count recorded at BASE" — I read it at unit 1 `:241-242`. So at unit 3's landing the
tree already guarantees more than 105 by a criterion in force from the previous unit, before unit 3
writes a single arm. Unit 3 then adds at least seven of its own: S8's five fixtures, S9's property arm
and S10's byte arm. A tree in which every one of those seven was written but never invoked, or
de-collected later, still prints well over 105 and satisfies AC8. The harness exits on the fail count
alone (`agent-cap.test.sh:914-915`), so a de-collected arm set lands green under AC8, AC7 and AC11
together.

Round 1's H3 spelled the fix in terms — "at least 105 plus the three S6 arms plus the S7 arm, with the
expected number written into the criterion" — and the fold kept the 105 and dropped the addition. The
criterion rewritten to prevent green-by-absence still permits it, which is §7's own "a de-collected
file can't fail".

One corroboration from the spec's own text, which I derived while checking this and which makes the
row worse. §4's Measured table reports the candidate's suite as "105 passed / 0 failed, **the same
count as BASE**". A unit adding seven arms cannot measure the same count as BASE. Either the row was
taken before the arms existed, or the arms are not counted — and both readings are the defect AC8 was
rewritten to catch, published in the spec's own evidence table. That row also violates unit 1's AC7 on
its face, since 105 is not strictly above 105.

**Fix.** Two edits. Restate AC8 with the arithmetic and the literal: unit 1's landed pass count, plus
S8's five arms, plus S9's one, plus S10's one, with the expected integer written into the criterion.
And correct §4's Measured row to the count the built candidate actually produces, which cannot be 105.

**Left-shift gate.** Round 1's left-shift, which is still the right one and is now overdue: a
`PASS_FLOOR` constant in `tools/hooks/agent-cap.test.sh` that the runner asserts against its own final
count and that each arm-adding commit raises. That makes de-collection impossible to land silently
rather than merely discouraged, and it moves the floor with the suite instead of with a number typed
into a spec — which is §6's "a value stated in prose beside the source that OWNS it rots", applied to
an acceptance criterion.

---

### 5 — HIGH — §2 S6, §4 Measured, §4 Files touched and §6 AC9

*Folds finder findings `#4`, `#13`, `#21` and `#31` (the figure) and `#18` (the unowned pin move).*

S6 measures the `lexicon naming predicates` leg moving from `offenders=463` to `461`, §4 publishes the
461, and AC9 pins "the measured value is 461". The figure is not reproducible from the corpus, and the
reason is the mirror the same spec mandates.

Measured here: `--check` reports `P1 verb graded=1012 offenders=463` against `VERB_OFFENDER_PIN="463"`
at `.lexicon.conf:158`. `--list` shows `stripStrings` and `blankLiterals` as P1 offenders in **both**
tracked copies — `tools/hooks/agent-cap.js:70`/`:601` and `.claude/hooks/agent-cap.js:70`/`:601`, four
rows, not two. S7 mirrors every byte, so both copies move together. Nothing is added back: I ran
`--suggest` on all nine new names and all nine answer OK, and the js probe grades only `function NAME`
and `const|let|var NAME = (...) =>`, so the module-level `let VIEW_MODE` is not graded at all.

463 − (2 names × 2 copies) = **459**. Not 461. And 461 is not the other reading either: keeping both
names alive leaves 463. The value is produced by neither design, so AC9 fails on a conforming build
whichever way row 1 is decided.

The doubling is not a subtle property of the leg — it is measured twice already in this build's own
records. Round 1's B4 appended four definitions to both copies and recorded "+6 offenders for 3 × 2".
Unit 1's §10 records two refused names moving offenders 463 to 467. The fold answered a finding whose
evidence contained the doubling by retyping a single-copy count.

S6's phrasing is wrong on its own terms too. "The file's two existing verb offenders" — each copy
carries **17** P1 verb offender rows, 34 across the pair, and this unit drains 2 of them.

**The pin move is the second half, and nothing owns it.** S6 says "the pin FALLS". `lexicon.py:697`
reds only on `len(unwaived) > pin`, so a FALL leaves the leg green with the pin untouched at 463. AC9
asks for offenders "no greater than `VERB_OFFENDER_PIN`" plus a measured value — neither clause
observes the pin itself, so a tree in which the pin never moved satisfies AC9 completely. §4's Files
touched does not list `.lexicon.conf`, the only file a fall could be written into. That file carries a
documented convention that every pin move is recorded inline with what bought it, downward moves
included, and an unmade fall loses that record and leaves the ceiling four offenders above the corpus.

**Fix.** Re-measure after row 1 decides the naming, and write the real value into S6, §4's Measured row
and AC9, showing the arithmetic as two names across the two copies S7 mirrors. Restate S6's phrase as
"two of the file's seventeen verb offenders per copy". Add `.lexicon.conf` to §4's Files touched, and
give AC9 the equality clause: `VERB_OFFENDER_PIN` reads the new measured value and the conf carries the
drain entry naming the two definitions that left, per the convention the file states and demonstrates
at `:116-157`. Consider dropping the exact integer from AC9 in favour of `offenders <=
VERB_OFFENDER_PIN` plus the drain COUNT, so the criterion survives a corpus that moves for unrelated
reasons between now and landing.

**Left-shift gate.** Two, both cheap. A `TEMPLATE-SPEC` check that a spec claiming a pin MOVE lists
that pin's file in §4's Files touched — the mechanical form of "a claimed edit with no file is not an
edit". And the generic one this build keeps re-earning: a figure a spec publishes about a leg must be
re-derived by running the leg, not typed from a prior record. The measurement here takes under a
second; what made it wrong was that nobody ran it.

---

### 6 — HIGH — §6 AC1, against AC2-AC5

*Folds finder finding `#15`. This is round 1's H1, applied to four of five criteria.*

Round 1's H1 said every criterion observes only an exit code and the fix is to assert the stderr
message. Rev-2 applied it to AC2, AC3, AC4 and AC5 — each now reads "the message names …". AC1 still
reads "exits 2 … it exits 0 … it exits 2", and AC1 is the criterion for the FIRST reproduced move.

I built AC1's fixture exactly as it is written — `const re = /it's` + a backtick + `don't/` above a
multi-line `boundedParallel(L.map((g) => () => agent(promptFor(g))), 50)` — and fed it to the hook.
It exits 2, and the message is:

```
BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item.
  L3: L.map((g) => () => agent(promptFor(g))),
```

That is **rule 2**, not the rule 3 AC1 is labelled. `main()` runs `fanoutFindings` at `:1085` before
`capFindings` at `:1105`, so rule 2's denial short-circuits and rule 3 never runs on this fixture.

The consequence is precise. Under unit 1 alone the backtick reaches `renderCodeView`'s mode switch
and both rules admit, so an implementer who wires rule 2's dispatcher and leaves rule 3's unwired
satisfies all three of AC1's clauses: exit 2 with unit 3 (rule 2's shipped pass), exit 0 with unit 1
alone, exit 2 at BASE. The fold's own stated fix for H1 was "AC1-AC5 are per-rule and name the
expected message"; the first reproduced move is the one it did not reach.

**Fix.** Add the message clause to AC1 in the same shape as its four siblings: "and the message names
the CALL SITE bound". The harness already has the helper — `msg()` at `agent-cap.test.sh:336`, under a
header stating that every arm there asserts its own message and never the exit code, written after a
retired arm passed on a fixture that tripped a different rule. This is the same trap, in a criterion
rather than an arm.

**Left-shift gate.** An arm asserting that every rule in `main()` has at least one `msg()`-shaped arm
naming its own banner text, derived from the source rather than from a list, so a sixth rule added
later reds until it is covered. Round 1 proposed it for H1 and it remains unbuilt; this row is what
its absence costs.

---

### 7 — MEDIUM — §2 S4, against §5 observability and §4

*Folds finder finding `#16`. This is round 1's M3, half taken.*

M3 asked for two things: key the merge on `(n, why)`, AND state the tie-break — shipped rows win a
collision and are ordered first. S4 takes the key and states no ordering. S3's description — run one
rule under `lexed`, flip to `shipped`, run again, and merge — puts lexed rows first, which is the
order M3 warned against.

Widening the key makes this worse rather than better, which is the part worth noticing. Under the old
`n`-only key a colliding pair had one row displace the other; under `(n, why)` both survive, so a
colliding line now contributes two rows to the printed list. All four rules print only `slice(0, 6)`
— verified at `:1091`, `:1111`, `:1129` and `:1164` — so on a script with several findings the shipped
row can be pushed out of the printed set. §5's observability bullet then promises something the design
does not provide: "a finding reported from the shipped pass carries that view's own explanation, which
is the message an operator sees today". If that row is not printed, the operator does not see it.

No criterion observes emitted text at a collision. AC2-AC5 assert messages on single-finding fixtures.

**Fix.** State the merge ORDER in S4 alongside the key: shipped-pass rows are emitted first, so a
collision cannot push the status-quo explanation out of the six printed. Add one AC over a line
carrying two helper calls asserting BOTH explanations reach stderr, and one over a line both views
flag asserting the shipped `why` is in the printed set.

**Left-shift gate.** The arm round 1 specified: over a line carrying two helper calls, assert both
explanations reach stderr; over a line both views flag, assert the SHIPPED `why` is the emitted text.
The pair distinguishes a merge that preserves the operator-facing message from one that merely does
not crash.

---

### 8 — MEDIUM — §2 S1 and S10, against §3's last non-goal and unit 2's S4/AC3

*Folds finder finding `#25`. This is `amendment-leaves-its-other-half-standing`, arriving through the
fold that closed round 1's instance of it.*

S1 freezes `renderCodeView` verbatim as `renderShippedView`, and S10/AC7 byte-compare that body
against the BASE blob. That body contains a comment at `agent-cap.js:301-306` — inside the quote
branch, not above the function — ending:

> `stripStrings` needs a matching PAIR before it blanks anything, and so does this now.

Unit 2's S4 is assigned to rewrite exactly that comment, and unit 2's AC3 requires the phrase "and so
does this now" to be ABSENT. Unit 2 is order 3 and lands LAST.

After unit 3 lands, that sentence exists twice — once in the lexed copy, once in the byte-frozen one.
Unit 2 then either edits both, which reds unit 3's byte arm because the frozen copy no longer equals
the BASE blob, or edits one, which leaves the sentence standing in the other and makes AC3's absence
clause ambiguous about scope. Unit 3's §3 raises this hand-off — "unit 2 is sequenced last so it
describes what both code units actually did" — and settles the prose half while leaving the per-copy
question unstated. Nothing in unit 3's §3 or §5, and nothing in unit 2's S4 or §9, says the carrier
set became per-copy.

One defence is not available: the sentence is not accurate in the frozen copy either. It describes the
shipped pairing, which is the thing unit 1 corrects, so "it is true where it is frozen" does not hold.

**Fix.** Two clauses. Say in S1/S10 whether the byte comparison covers comments or only executable
code — either answer works, but it must be written, because AC7 is unanswerable without it. And add to
§3 that unit 2's carrier list is re-derived against the post-unit-3 file, naming which carriers now
exist twice and which copy each correction lands on, with S4's comment as the live instance.

**Left-shift gate.** A binding-level check, and the machinery exists: `gen_build_index.py
--print-bindings` already reads every record's bytes, so it can assert that no two units in one build
claim the same file region with contradictory verbs — one freezing what another rewrites. A build that
byte-freezes a region a later unit is assigned to edit should red at planning time, not at the
landing where one of the two acceptance criteria has to give.

## Exit condition for round 3

Round 1 set the ceiling at 5 confirmed blockers. This round confirms **2**. Per BUILD-METHOD M4 the
loop re-arms only on a strictly falling confirmed-blocker count, and 2 < 5, so **round 3 is
permitted**. Its ceiling is 2. A round 3 that does not come in under 2 stops the loop and disposes
every standing blocker — folding what belongs in a document it read, promoting what needs a mechanism
this build lacks — rather than re-reviewing it.

Three notes for whoever writes the next fold.

- **Rows 1 and 5 are one piece of work, and rows 2, 3 and 4 are another.** Row 1 decides the naming;
  row 5's figure cannot be computed until it is decided, so fixing row 5 first guarantees fixing it
  twice. Rows 2, 3 and 4 are all "which arms must be seen to fail, and what counts them" — one pass
  over §6 settles all three, and settling them separately is how AC8 came to be keyed to the wrong
  baseline in the first place.
- **The failure mode of this fold was dropping operative clauses, not misunderstanding findings.**
  Six rows here are a round-1 fix whose headline survived and whose measurable half did not. Before
  committing rev-3, re-read each round-1 and round-2 fix text and check the clause containing the
  NUMBER, the STAGING or the ORDER actually appears in the new prose. That is a five-minute pass and
  it would have caught rows 3, 4, 6 and 7 outright.
- **`fold-text-is-unreviewed-surface` is selected again for the rev-3 diff.** Both blockers this
  round are in sentences that did not exist at rev-1, and one of them — row 1 — is a collision between
  two rev-2 sentences that were each written to close a different round-1 finding. Two independently
  correct repairs that contradict each other is the specific hazard of folding a five-blocker round in
  one pass, and rev-3 folds two more.
