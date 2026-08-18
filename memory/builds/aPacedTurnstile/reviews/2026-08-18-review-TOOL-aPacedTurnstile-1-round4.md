# Narrow re-review of the T1 blocker fix — TOOL-aPacedTurnstile (units 1-7)

**Serves:** spec-audit TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7

**Date:** 2026-08-18 · **Tier:** 2 · **Streams:** tooling · **Base:** `fa1d848` · **Round:** 4
**Subject:** commit `fa1d848`, "TOOL-aPacedTurnstile: fold all 23 round-3 findings, blocker first",
read as the seven spec files now stand plus the build README. **Question asked:** did the round-3
T1/T2/T3 blocker fix — the two-form `tools/run-gates/gate-fingerprint.sh` contract — land WHOLE, in
every carrier the fix names and in the unit that owns the interface, and is the contract sound on
its own terms? **Narrow scope:** this pass read the TEXT `fa1d848` touched and the joins that text
participates in — the two-form contract attacked directly, defects the fold CREATED, and
fold-PARTIAL residue graded against the round-3 finding table T1..T23. It did NOT re-audit the set
at large. The five owner decisions settled at kickoff, the round-3 findings that closed cleanly
(re-verified only far enough to classify them), the round-3 refutations, and anything needing code
that does not exist yet were all out of scope, and a defect living entirely in text this fold did
not touch would not have been looked for.

## Verdict: CLEAN WITH FIXES

**The T1 blocker is closed, and it closed whole.** Every carrier the fix names carries it: `-5` S5
declares the two forms, `-5` §4 The fingerprint states the contract, `-5` §4 Files touched has the
rewritten row, `-5` AC17 arms both halves, `-7` S2b names the AT-A-REV form with its argument, `-7`
§4 Data model agrees, and `-1`'s kit-dir layout gloss was corrected. `-7` AC6b needed no edit and
got none — it grades the hook's observable behaviour, and its "computed AT THE RECORDED SHA" is
exactly the corrected join. Nothing in the set now calls the helper by the wrong form. The contract
is also sound when attacked directly: on a clean tree the porcelain component and the dirty-blob set
are empty in the no-argument form, the rev form supplies those same two components EMPTY rather than
omitting them, one implementation serialises all three, so the two forms hash byte-identical input
and yield one digest. `-5` S7's clean-at-start and tree-did-not-move preconditions do make every
value written into `gate-full-green` a value the rev form reproduces at the sha the record names.
The arity mismatch that round 3 said would return the blocker "in its most expensive form" is dead.

**The multi-carrier partial-fold pattern has NOT stopped.** That is the one question this pass was
run to answer and the answer is no. It recurred three times inside the fold that was written to end
it: T12's fix widened predicate 6's reason string in `-7` §4's decision table and in S2b, and did
not move it in AC6c, the criterion that asserts the literal (V1); T6's fix moved AC6d's arm into a
different harness and swept neither the scope item that enumerates this unit's arms nor the
files-touched table a builder derives the commit from (V4); T9's fix named four carriers in `-3` and
landed in three (V6). The build README's own blockers table, edited by this commit to record T1,
picked up a miscount in the caption three lines above the new row (V7).

**What HAS stopped is the pattern producing a blocker.** Rounds 2 and 3 each ended with a spec set
that had no green state — R1 left predicates 3-6 unreachable, T1 named a computation the owning
interface could not perform, and in both cases the repair required new interface design across
units. Nothing in this round is of that grade. V1 is the closest: two binding carriers of one reason
string disagree, so no implementation satisfies both documents, and the cheapest field repair
restores T12's original defect. But the direction of the correct edit is not in dispute — S2b, added
by this same fold, states the widened population in terms — and the whole repair is one literal and
one gloss inside one criterion. The remaining findings are completeness gaps inside otherwise sound
text: two in the new contract itself (its arm does not bind the rev ARGUMENT, V2; the precondition
the entire binding property rests on is nowhere defined, V3), and four scoping or record misses a
builder recovers from by reading one section further (V4, V5, V6, V7). The set is buildable. Fold V1
before build, and fold V2 and V3 with it — they are the two places where the new contract's own
guarantees are weaker than the prose claiming them.

One methodological note for whoever folds this. All three residues sit in fixes with three or more
carriers, and none sits in a fix with two. The mechanism is visible: the fold edits the section it is
reading, and the carrier it misses is always the one in a different section of the same file that
restates a literal or a file path. Sweeping a fix by grepping the changed literal across the file —
not by re-reading the finding's carrier list — is what would have caught V1, V4 and V6, and it is
cheaper than any of the three.

## Findings

### V1 - HIGH - TOOL-aPacedTurnstile-7 §6 AC6c, against §4 The decision, table row 6 · §2 S2b

- **Claim:** T12's fix had three carriers and landed in two. §4's decision table row 6 now emits the
  widened reason `a merge tip the record does not cover`, and S2b states the widened population, but
  AC6c still requires `.githooks/pre-push.test.sh` to observe the retired literal `a reconcile merge
  is not covered by the record`, and still glosses the population as "the shape
  `tools/push-main.sh` produces when it reconciles and retries" — the narrow reading S2b was
  rewritten in this same commit to reject. The fold had AC6c open when it did this: it edited that
  criterion to add the negative-half control, and edited the string a hundred lines above in the same
  file. The reason strings are not decoration here. AC4 says so in terms — the string is part of the
  criterion because predicate 1 also yields `GATE_FULL=1`, so the flag alone cannot tell the arms
  apart — and every other criterion's string (AC2, AC3, AC4, AC6, AC6b) matches its table row
  exactly. This row is the only mismatch in the set. §9's rev-7 entry then claims "the reason string
  names the real condition", which is true of the table and false of the criterion.
- **Impact:** there is no implementation that satisfies both binding carriers. A builder implementing
  §4's table prints the widened string and AC6c reds; a builder implementing AC6c prints a string §4
  says the hook does not print, and an operator reading `a reconcile merge is not covered by the
  record` on a first-attempt landing — which S2b and §4 now agree is the ORDINARY case here, since
  every landing on this repo is a merge — is told a retry happened that never did. That is the
  over-firing-that-reads-as-caution failure the whole predicate-0/predicate-6 thread exists to stop.
  The cheapest field repair is to weaken whichever side is noticed second, and the side most likely
  to be weakened is the table row, which restores T12 verbatim: a row whose reason string
  mis-describes its own population. The narrow gloss compounds it — a builder reading AC6c writes an
  arm that only ever exercises the push-main retry shape, leaving the ordinary case graded by nothing
  but the new control.
- **Fix:** in AC6c, replace the asserted reason with `a merge tip the record does not cover`, and
  replace the em-dash gloss with the population S2b now states — a merge tip whose second parent is
  not an ancestor of the recorded green, of which the push-main reconcile retry is one instance.
  Leave the negative half as written. Then re-read §9's rev-7 T12 clause, which is only true once
  AC6c moves, and grep the file once for every table reason string against its criterion; only this
  row diverges today.
- **Confirmed because:** `fa1d848` rewrote §4's decision row 6 to `a merge tip the record does not
  cover` while §6 AC6c still asserts `a reconcile merge is not covered by the record` and still
  carries the push-main reconcile-retry gloss, in the same commit that rewrote S2b to reject exactly
  that narrow reading. AC4 makes the reason string load-bearing, so the two binding carriers cannot
  both be satisfied. Three lenses reached this independently and the skeptic confirmed each.

### V2 - MEDIUM - TOOL-aPacedTurnstile-5 §6 AC17, the arm for §2 S5's two-form contract

- **Claim:** AC17 does not falsify a rev form that IGNORES its rev argument, which is the failure
  mode its own text claims to close. Both invocations it names are at HEAD: no argument on a clean
  tree, and `HEAD` as the rev argument. Consider an implementation that computes the tree object at
  HEAD unconditionally and uses the argument count only to decide whether to include the porcelain
  and dirty-blob components. On a clean tree the two invocations are equal, so half one passes. Made
  dirty, the no-argument form gains a porcelain component and the two differ, and the rev form is
  unchanged from its clean-tree value because HEAD did not move — so half two passes, including its
  "rev form unchanged" clause. Both halves are green and the argument is dead. AC17's stated
  reasoning names this hazard exactly ("the equality alone is satisfied by a rev form that ignores
  its argument") and then arms only the worktree-reading half of it. No assertion anywhere in the
  seven specs invokes the helper at a rev whose tree DIFFERS from HEAD's, which is the only
  invocation that binds the parameter.
- **Impact:** the argument-ignoring form is precisely the shape that restores round 2's R1.
  `.githooks/pre-push` calls the helper at the recorded sha, which is normally an ancestor of the
  pushed tip; under an argument-ignoring helper the hook gets the digest at the tip, predicate 0
  fires on every push whose tree moved since the recorded green, the scoped path is unreachable and
  predicates 3-6 are dead code. It fails toward FULL, so no leg reds and nothing on the bar notices.
  `-7` AC6b's control is the only other arm in the region; it is fixture-built and catches this only
  if the fixture's stored fingerprint is sourced independently of the helper under test, which no
  criterion says — and which AC17 is the natural place to make unnecessary.
- **Fix:** add a third invocation to AC17 — on a clean tree with at least two commits whose trees
  differ, the helper at `HEAD~1` must DIFFER from the helper at `HEAD`, and must equal the
  no-argument form measured with that rev checked out clean. One extra assertion in
  `tools/run-gates/run-gates.evidence.test.sh`, and the only one in the set that binds the argument
  rather than the components.
- **Confirmed because:** AC17 invokes the helper only at HEAD in both forms, so the
  compute-at-HEAD-unconditionally implementation passes the equality half on a clean tree and the
  difference half including its unchanged-rev-form clause on a dirty one; a grep of all seven specs
  finds no criterion invoking the helper at a rev whose tree differs from HEAD's, leaving the hazard
  AC17's own text names unarmed.

### V3 - MEDIUM - TOOL-aPacedTurnstile-5 §2 S7 and §2 S2's CLEAN-at-start key, against §2 S5 · §6 AC13

- **Claim:** the new binding property is exactly as strong as S7's clean-at-start precondition, and
  nothing in the set defines CLEAN. S5 argues that S7 refuses to write `gate-full-green` unless the
  tree was clean at start, so every recorded digest is one the rev form reproduces at the sha it
  names. That inference holds only if CLEAN means precisely `git status --porcelain` empty — the same
  predicate the fingerprint's own porcelain component is computed from, untracked files included. S7
  says only "the tree was CLEAN when the run started"; S2's header key says only "whether the tree
  was CLEAN at start"; AC13 grades "the working tree is DIRTY at the start" and never says what a
  dirty fixture must carry. The helper is now its own executable printing only a digest, so the
  runner must compute cleanliness separately, and a builder writing the obvious pair of
  `git diff --quiet` checks — an idiom that ignores untracked files — satisfies every word of S7 and
  AC13 with untracked files present.
- **Impact:** under that reading the runner writes `gate-full-green` from a tree whose fingerprint
  carries a non-empty porcelain component (a `??` line) and a non-empty dirty-blob set. The rev form
  CANNOT reproduce that digest at any sha, because both components are empty by construction.
  Predicate 0 then mismatches on every subsequent push, forces full forever, and prints `the record
  describes a different tree` — the blocker returned in the unconditional-mismatch-that-reads-as-
  caution form AC17 exists to prevent. AC17 cannot see it, because AC17 grades the helper and this is
  a runner-side definition; AC13 cannot see it, because an untracked-only fixture is not mandated.
  §4's own note that this repo's ignore rules cover the python bytecode dirs confirms
  untracked-but-unignored files DO move the fingerprint, so the two definitions select genuinely
  different populations.
- **Fix:** in S7, define the clean-at-start precondition as the same predicate the fingerprint's
  porcelain component uses — `git status --porcelain` empty, untracked included — in one clause, and
  say so beside the S5 binding property that depends on it. Give AC13 a second fixture whose only
  dirtiness is an untracked, unignored file; that is the fixture that separates the two definitions,
  and no criterion in the set contains it today.
- **Confirmed because:** S5's new binding property rests on S7's refusal, but S7, S2's header key and
  AC13 all say only CLEAN/DIRTY, and nothing in the set equates that to the `git status --porcelain`
  predicate §4 defines the fingerprint's own component from (untracked included) — so a diff-only
  clean check records a digest carrying a `??` porcelain line that the rev form can never reproduce.

### V4 - MEDIUM - TOOL-aPacedTurnstile-7 §6 AC6d, against §2 S8 · §4 Files touched

- **Claim:** T6's fix was taken by moving AC6d's header assertion out of `.githooks/pre-push.test.sh`
  and into `tools/run-gates/run-gates.evidence.test.sh` — the right harness, since that one actually
  drives the runner. The move landed in the criterion alone. S8, the scope item that enumerates this
  unit's arms, still covers only `.githooks/pre-push.test.sh` ("one arm per forcing predicate, one
  arm proving the scoped path actually scopes, one proving the no-halt export, and one asserting the
  lag constant"), and §5's testing bullet still summarises it as "S8's arms, one per forcing
  predicate". §4 Files touched has a `.githooks/pre-push.test.sh` row and NO row for the evidence
  suite. The file belongs to `TOOL-aPacedTurnstile-5`, whose own §4 row for it reads "S9's arms", so
  a cross-unit edit made at `-7`'s commit is recorded in neither unit.
- **Impact:** §4 Files touched is what a builder derives the commit's edits from — T8's own argument
  — so the one arm that observes the runner writing the forced-full reason into the header can be
  skipped without contradicting any scope item or table row, which reopens R21, the gap AC6d exists
  to close, while every criterion in `-7` still reads green. This is a builder-scoping gap rather
  than a blind DoD: §7 already ends with the full bar, and the evidence suite is a leg on it, so
  AC6d IS executed by this unit's stated gates once the arm is written. The cost is an unbuilt arm,
  not an invisible red.
- **Fix:** add a `tools/run-gates/run-gates.evidence.test.sh` row to `-7` §4 Files touched naming
  AC6d's arm, note that it lands in `-5`'s suite because `-5` owns the header, extend S8 with that
  one arm, and correct §5's testing bullet. Consider naming the cross-unit arm in `-5` §4's row for
  that suite too, so the file has one owner statement rather than two units editing it silently — as
  `-3` S9 now does for the kickoff guide.
- **Confirmed because:** `fa1d848` moved AC6d's assertion into
  `tools/run-gates/run-gates.evidence.test.sh` while `-7` S8 still enumerates only
  `.githooks/pre-push.test.sh` arms and §4 Files touched has no evidence-suite row, and `-5` §4's row
  for that same file reads only "S9's arms" — the identical shared-file ownership gap this fold
  narrowed in `-3` S9 for the kickoff guide. Two sub-claims raised alongside it were corrected: §7
  does list the full bar and therefore does reach the suite, and §7's `kit-dogfood-parity.test.sh`
  entry predates this fold.

### V5 - LOW - TOOL-aPacedTurnstile-7 §6 AC9b, against §2 S10 · §4 Files touched

- **Claim:** T10 is closed in the criterion's text and left open in the build instruction. AC9b now
  demands that `bash tools/memory-tree/kit-dogfood-parity.test.sh` assert that
  `tools/memory-tree/kit.toml`'s declared gate-leg guard for this leg names `memory/guides/`, with a
  fixture reverting it to the narrow spelling as the control. That suite reads no `kit.toml` today
  and never has — its own header declares its whole contract as the two documents this kit SHIPS,
  rendered for this install, equalling the two documents this repo RUNS ON, and the only `kit.toml`
  readers in the tree are `tools/govkit/govkit.py`, `tools/govkit/selftest.py` and the descriptors
  themselves. So the arm is a new TOML-parsing capability inside a bash document-differ. S10 still
  scopes this unit to closing the hole in the two DECLARATION carriers and builds no arm, and §4
  Files touched carries a `tools/memory-tree/kit.toml` row but no row for the suite AC9b now names.
- **Impact:** the shape AC9b's own new paragraph says it is repairing — an obligation named in prose
  with no criterion that can fail, the R11-R13 shape — survives one level down: the criterion CAN
  fail, but nothing tells the builder to write the arm, and the files-touched table is the section a
  builder derives edits from. The shipping carrier of the guard hole then ends up closed in
  `kit.toml` with nothing observing it, which is the half `-7` S10 says must not be left open, and
  `TOOL-aPacedTurnstile-12` explicitly does not cover it. Low rather than medium because AC9b is
  binding and names the file, the assertion and the control fixture, and §7 already listed that suite
  before the fold — so nothing is unreachable.
- **Fix:** add the arm to S10 as a stated obligation ("and the memory-tree kit's suite gains an
  assertion over its own descriptor's guard for this leg, with a narrow-spelling fixture as the
  control") and add the matching §4 Files touched row. If a bash documents-parity suite is the wrong
  host for a TOML read, point AC9b at `python tools/govkit/selftest.py` instead — T10's fix text
  offers it — and repoint §7 with it.
- **Confirmed because:** `-7` S10 says the hole has two carriers and both are closed here, scoping
  only the `tools/gate-legs.json` and `tools/memory-tree/kit.toml` declaration edits with no arm, and
  §4 Files touched carries a `kit.toml` row but none for `kit-dogfood-parity.test.sh`, whose header
  declares a two-document parity contract and which reads no `kit.toml`.

### V6 - LOW - TOOL-aPacedTurnstile-3 §4 Data model, the contiguity sentence

- **Claim:** T9's fix named four carriers — §7, §4 Files touched, S8, and §4 Data model's "canary
  arm" wording — and landed in three. §4 Data model still reads "Chunks are required to be CONTIGUOUS
  in gov's own manifest, asserted by a canary arm". AC6 now places the contiguity assertion in
  `tools/run-gates/run-gates.gov.test.sh`, and S8 was rewritten in this same fold to say so
  explicitly and to record why the earlier assignment was wrong. `-3` §9's rev-6 entry lists §7, §4
  Files touched and S8 and does not claim §4 Data model, so the omission is unrecorded as well as
  unfixed.
- **Impact:** §4 Data model is the section that states the contiguity requirement as a design
  property, and it is the sentence a builder reaches first. Left unqualified it points at a harness
  by an unqualified noun while AC6, AC6b, S8, §7 and the Files-touched row all name the harness by
  path. The severity stays LOW because the sentence is under-specified rather than wrong — this file
  also calls the gov-only harness "the GOV-ONLY canary" in S2 and in rev-6, and the sentence already
  scopes itself to "gov's own manifest" — so the residue is ambiguity, not the misdirection that
  would export a red-on-arrival assertion into the shipped canary.
- **Fix:** reword to name the harness — "...asserted in `tools/run-gates/run-gates.gov.test.sh`
  (AC6), because gov's six declared chunk names are gov's corpus" — and while there, stop using the
  bare word "canary" for both harnesses in this file, since S8 and AC6b already distinguish the
  SHIPPED canary from the gov-only one by name. One clause, and it is T9's last carrier.
- **Confirmed because:** `fa1d848`'s diff to `-3` touches §7, §4 Files touched and S8 only; §4 Data
  model still reads "asserted by a canary arm" although round 3's fix text said in terms to reword
  "S8 and §4 Data model's 'canary arm'", and §9's rev-6 entry lists the three it swept without
  claiming this one.

### V7 - LOW - build README, the blockers table and its caption · the per-unit audit column

- **Claim:** the fold added a `T1 | -5, -7` row to the blockers table and did not sweep the sentence
  that introduces it. The caption still reads "Five from round 1, then one from round 2:" above a
  table that now holds seven rows across three rounds, and the new row is placed BEFORE `R1`, so the
  table reads F1-F5, T1, R1 — round 3 ahead of round 2.
- **Impact:** cosmetic against a builder, and no criterion or gate observes it. But this is the record
  an owner reads to learn what the build got wrong, the caption is now a factual miscount, and it is
  the same multi-carrier miss the paragraph a few lines above it declares to be this build's
  recurring defect — created by the fold that declares it.
- **Fix:** change the caption to "Five from round 1, one from round 2, one from round 3:", and move
  the `T1` row below `R1` so the table runs in round order. Adding `T1` to `-5`'s and `-7`'s audit
  cells in the unit table is worth doing at the same time, though that column already omitted round
  2's `R1` from `-7` before this commit, so it is a pre-existing thinness rather than fold damage.
- **Confirmed because:** the fold's diff added the `T1 | -5, -7` row while leaving the caption as
  unchanged context, so "Five from round 1, then one from round 2:" now sits above seven rows
  spanning three rounds, with T1 (round 3) placed above R1 (round 2).

## Refuted

- `-5` S5's empty-on-any-failure sentinel making predicate 0's equality join fail OPEN (empty equals
  empty, so a doubly-failed fingerprint reports agreement) — killed as a pre-existing property of the
  sentinel rather than something this fold created or worsened, and one whose realisation needs a run
  that failed at both ends AND a record written from it, which S7's failed-nothing precondition
  already blocks on the write side. Worth a follow-up on the helper's sentinel; not a finding against
  this fold.
- `-5` §2 S9's four-item arm enumeration not covering AC17 — killed: S9 has been an incomplete
  enumeration since rev-5 (AC15's sweep arm and AC16's redaction arm sit outside it too), AC17 is
  binding and names its own harness, and grading a two-revision-old enumeration style against this
  fold's addition would charge the fold for a defect it inherited.
- `-5` §2 S1's `GATE_RUN_KEEP=5` not saying whether the constant is source or environment — killed as
  speculative: the declaration says "a DECLARED constant", `-5` S10 pins the manifest key set, and no
  criterion in the set is satisfiable by an environment-overridable reading that a source reading
  fails. A real ambiguity, but one with no demonstrated wrong outcome.
- `-7` §5's user-docs bullet saying "seven at this base" and "deliberately NOT a count restated here"
  in one sentence — killed: the parenthetical is an as-measured aside inside a bullet whose binding
  instruction is the measurement, and T13/T16/T23's fix text offered both spellings. Untidy, not
  wrong.
- Two further raw findings naming `-3` §4 Data model's "canary arm" and `-7` AC6d's unswept carriers
  were folded into V6 and V4 rather than carried separately; they are duplicates from a second lens,
  not independent defects.
