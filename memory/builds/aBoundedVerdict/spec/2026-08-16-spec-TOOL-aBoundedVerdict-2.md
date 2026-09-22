# TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads

**Status:** CLOSED · rev-9 · 2026-08-20 · node c · Tier-2 · base 098bebd9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md](../build/2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md) | research | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 |
| [2026-08-16-review-TOOL-aBoundedVerdict-1-2.md](../reviews/2026-08-16-review-TOOL-aBoundedVerdict-1-2.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 |
| [2026-08-16-review-TOOL-aBoundedVerdict-1.md](../reviews/2026-08-16-review-TOOL-aBoundedVerdict-1.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 |
| [2026-08-19-review-TOOL-aBoundedVerdict-1-2.md](../reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-11 TOOL-aBoundedVerdict-12 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-14 TOOL-aBoundedVerdict-15 TOOL-aBoundedVerdict-16 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 |
| [2026-08-20-review-TOOL-aBoundedVerdict-1-round2.md](../reviews/2026-08-20-review-TOOL-aBoundedVerdict-1-round2.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 |
| [2026-08-20-review-TOOL-aBoundedVerdict-1.md](../reviews/2026-08-20-review-TOOL-aBoundedVerdict-1.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |
| [2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md](../reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |
| [2026-08-21-review-TOOL-aBoundedVerdict-1-round4.md](../reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round4.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |
| [2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md](../reviews/2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-22 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 TOOL-aShardedFloor-4 |

<!-- /gen:spec-records -->

## 1. Goal

A run that cannot finish reaches exactly one non-landing terminal, and that terminal carries no
machine-legible reason: the free-text abort reason is parsed by nothing, and the kind field the
helper already writes is read by nothing. Give the abort verb a required halt code over a kit-owned
vocabulary, and give that vocabulary readers, so an owner returning to a stopped run learns why it
stopped without reading prose.

## 2. Scope (IN)

- **S1** — a kit-owned core halt vocabulary in the driver, one member per halt site this build's
  research actually enumerated, and no member invented for symmetry: the review loop reached its
  RUNAWAY CEILING with the subject not clean — rev-5's re-reading of a member that used to name a
  routine cap refusal, and now names a backstop whose being reached is itself a defect
  (`TOOL-aBoundedVerdict-1` S1a); a fork survived the method's vetoes with no resolution the mandate
  delegates; a unit awaits owner scope approval the mandate does not supply; a unit is blocked on an
  EXTERNAL PREREQUISITE, which is a different owner turn from an unapproved scope and is the case
  `TOOL-aBoundedVerdict-3` S1 routes here; a unit's acceptance or gates could not be derived; the
  repository state at start was outside what the mandate reaches; a gate is red and its fix lies
  outside the mandate's scope.
- **S2** — `--abort <slug> --reason <text> --code <CODE>`, with the code REQUIRED and validated
  against the effective vocabulary. An unlisted code is refused naming the legal set.
- **S3** — the code is recorded as an AUTHORED FACT through the existing fact writer, not buried in
  the reason prose, so a reader is a field read rather than a parse. It is therefore a NEW fact, and
  S7 moves the region's fact pin wherever it is spelled rather than leaving the spec silently in
  breach of it. **No ordinal and no count appears anywhere in this spec.** The pin's value, and the
  ordinal the code takes, are READ AT BUILD TIME out of the carriers S7 enumerates: the pin's history
  across those carriers is non-monotone, so a number written into a spec is a number that was true
  once, and this spec has already carried three wrong ones. The justification is the protocol's own
  membership test — nothing in the tree derives the code, and only the run knows it — and the shape: a
  halt code is a per-run SINGLETON that three readers read by key, which is what a fact is for. **The
  in-tree precedent is exact**: the fact recording the roster frozen at landing is a singleton written
  by a TERMINAL verb, which is the same shape this code has. A tracked sibling spec declined a new
  fact and added a park KIND instead, and that remains the right answer for append-only history; it is
  the wrong answer for a singleton nobody would grep a region to recount. `TOOL-aBoundedVerdict-1`
  takes the park-kind route for exactly that reason, so this build uses both shapes deliberately.

  **This unit is the pin's ONLY mover in this build.** `TOOL-aBoundedVerdict-21` would have been the
  second and is PARKED: the fix its own blocker needs is refused by that unit's §3 Non-goal, so there
  is no sibling mover to sequence against, no shared carrier list to split, and no "one apart"
  arithmetic anywhere in S7.

  **The ratified decision row is partly stale, and this spec says which part.** `memory/DECISIONS.md:68`
  is the append-only, owner-ratified row for this unit. What SURVIVES is the decision itself — a
  validated halt CODE, never a new phase, ratified by the owner — and its three measurements: nothing
  outside the kit reads the phase, a new terminal is unwritable without a producer verb, and a
  non-terminal one wedges the next preflight. What does NOT survive is its final clause, which pins
  the code to an ORDINAL: true at the base, false at HEAD, and the exact reason this spec now states
  none. The row is append-only so it is never edited; a superseding row that DROPS the ordinal rather
  than re-spelling it is the BUILD's to commit at landing and is not in this unit's write set. A
  builder who greps the decision log and finds the ordinal reads this bullet as the correction.
- **S4** — two new `.unattended.conf` keys, spelled here rather than described, in the shape the
  existing `PHASES_EXTRA` / `DOD_EXTRA` / `CORE_FLOOR` trio already sets:
  - `HALT_CODES_EXTRA` — OPTIONAL, empty legal, the project's appended members.
  - `HALT_FLOOR` — REQUIRED, a single integer, the shrink-only size of the kit's core set. Undeclared
    or malformed is a refusal, not a defaulted value, matching how the existing floor key behaves.

  Both are added to the adopter's seed conf as well as this repo's, because the seed is what a real
  adopter copies and a gate-required key missing from it reds the unattended leg's first check on
  install with no gate here noticing. Rev-2 asserted both were named and named neither, which is the
  defect round 1 raised, restated rather than fixed.
- **S5** — three readers, because a vocabulary with no reader is decoration and this kit says so
  about its own phase writer: `--status` names the code on its single line; `--resume` names it and
  states that the run is finished rather than resumable; and a new leg check asserts that every
  tracked run-state file whose phase is the aborted terminal carries a code in the effective
  vocabulary.
- **S6** — the wrap-up gains the code, so the one turn the owner gets opens with why the run stopped.
  It lands in the PROTOCOL's wrap-up rows, which are already in this unit's write set, and NOT in the
  build method's derivation table — F3 recommends leaving the method alone on its own pointer rule,
  and rev-2 pre-applied that recommendation to the files list while leaving the scope item pointing
  at the method. If F3 is resolved the other way, `memory/guides/BUILD-METHOD.md` and its kit
  template join Files touched, and the manifest re-stamp and read-path clauses apply with them.
- **S7** — the region's FACT PIN moves, in every place it is spelled, because one new authored fact
  makes every count statement about that region stale at once. It has moved before and left a stale
  reader at every move — which is the argument for enumerating the carriers rather than trusting a
  builder to find them. **No count appears below.** Read the live value out of the protocol at build
  time; the carriers do not agree with each other today, so the protocol pair is the source and the
  rest are followers.
  - `memory/guides/UNATTENDED-PROTOCOL.md` — the count sentence introducing the authored region, and
    the numbered enumeration beneath it, which gains the code as one more entry.
  - `tools/unattended/PROTOCOL.template.md` — the same sentence and the same enumeration in the
    SHIPPED template. The leg byte-compares the shipped template against the installed copy
    (`check-unattended.sh` check 10), so these two move together or that check reds.
  - `tools/unattended/unattended.sh` — the resume path's comment about the authored region, which
    carries its own count statement, is stale at HEAD, and is read by no gate at all.
  - `memory/map/features/unattended.md` — TWO count statements: one in the run-state-split paragraph,
    one in the Gaps section's re-derivation note. That dossier's own prose says dossier prose is
    ungated, so nothing there catches a carrier left behind either.

  Nothing counts the facts, so no leg catches a missed carrier. AC8 is the assertion that closes that
  hole, and it asserts AGREEMENT across these paths rather than any value.
- **S8** — the protocol's phase and verb sections, the conf's key table, the adopter's seed conf, the
  rendered Skill, and the kit version SITES — which Files touched enumerates BY PATH rather than
  calling them "the constant", because they are several sites across two kits and naming one is how
  a half-bumped version ships.
- **S10** — the REVIEW VERDICT vocabulary gets the same treatment as the halt vocabulary, because it
  is the same defect one document over and this unit's title is the promise to fix it. Measured over
  the tracked review corpus at this spec's base: 18 distinct `## Verdict` lines, 5 leading tokens, 32
  records with no verdict line at all, 2 where `Verdict` is a section heading rather than a verdict,
  and **zero** carrying the literal clean token the method names as the loop's only exit. That is a
  motivating measurement, not a target — re-derive it with
  `git ls-files 'memory/builds/*/reviews/*.md'` and read each file's first line. So the vocabulary the
  method states in prose is read by nothing and written consistently by no one.

  **The set is CLOSED and has exactly three members: `CLEAN`, `CLEAN WITH FIXES`, `BLOCKED`** — the
  three `memory/guides/BUILD-METHOD.md:103` already states in prose, which is the floor and not a
  starting point. **The canonical owner is the MEMORY-TREE kit**: `memory/HYGIENE.md` check 5 and
  `tools/memory-tree/check-memory-hygiene.sh` enforce record grammar, and the build method is rendered
  by that kit, so the set lives where the records live.

  S10 makes a member a REQUIRED LINE of a review record, adds it to a NEW hygiene check, and
  `TOOL-aBoundedVerdict-1`'s `--review` verb accepts exactly that set.

  **Two corrections made at build time, because the files say otherwise.** First, NOT the first line:
  check 21 already owns a review record's head with its `**Serves:**` binding line, and every record
  in the corpus puts the verdict below it. So the rule is that the record carries exactly one
  `## Verdict: <member>` line, position-independent, which is what the corpus already does and what
  the build method's own wording approximates. Second, NOT check 5: that check is a recording-FILENAME
  grammar, and hanging a content assertion off it would make a structural check read as a semantic one
  to everybody who did not write it — the hazard this repo states as a rule about gate headers. A new
  check number is the cheap option here and this repo says so in as many words: the leg is named
  `memory hygiene` with no count in its name, and the codebase-map coverage assert and the drift leg
  signal both key on `tools/gate-legs.json`, which does not move for a new CHECK. It costs an
  `ARMS_FLOORS` bump, an arm per new `fail` site, and an entry in `memory/HYGIENE.md`.

  **The forward-only SELECTOR is PICKED, and it is the pattern already in the conf:** a dated cutoff
  key, set strictly ahead of every committed review record, so nothing landed is retroactively red and
  no record is rewritten. The alternative was the grandfather registry, which is for files kept under
  historical NAMES and is the wrong instrument for a content rule. This is the same instrument
  `TOOL-aBoundedVerdict-4` S6 chose for the same reason one document over, which is the argument for
  it rather than a coincidence. **That is a duplication, and it is STATED rather than resolved**: the two homes
  sit in independently installable kits and neither may import the other
  (`TOOL-aBoundedVerdict-4`'s spec records why at `:120-123`), so the set is spelled twice on purpose.
  The drift is ARMED and not left to prose — ONE row in the cross-kit case table
  `tools/memory-tree/marker-contract.test.sh` carries, the same harness `TOOL-aBoundedVerdict-4` S2
  extends and for the same reason. One harness, no new gate leg, and `TOOL-aBoundedVerdict-1`'s AC3 is
  satisfied by that row rather than by an unobservable claim of byte-identity.

  **Check 5 keeps its number.** It is today a recording-file NAME grammar, and S10 extends the SAME
  check to the record's first line. Minting a new check number is the alternative, and it moves the
  hygiene leg's declared check count for no gain, so it is refused.

  **Forward-only**: no retrofit of the existing corpus, for the reason §3 already gives about existing
  records. **One thing S10 does not settle, stated rather than hidden:** WHICH selector makes check 5
  forward-only over that corpus. Check 5 already carries a grandfather registry
  (`memory/project/legacy-files.txt`) and `TOOL-aBoundedVerdict-4` S6 declares a conf CUTOFF key for
  check 12; either serves and both already exist in this kit, so no new mechanism is needed. Picking
  between them is the builder's call inside S10's write set, and AC13's green-over-the-real-tree arm
  is what forces the pick to be made rather than assumed.

  S10's write set is `memory/HYGIENE.md` (check 5's grammar),
  `tools/memory-tree/HYGIENE.template.md` (the shipped source of that document),
  `tools/memory-tree/check-memory-hygiene.sh`, and `tools/memory-tree/check-memory-hygiene.test.sh`.
  All four are in Files touched and AC13 is the observable. Rev-5 declared none of them and rev-6
  claimed to have added them without doing so; rev-8 actually does.
- **S9** — the three documented CALL SITES of the abort verb gain the new required argument, and one
  arm asserts they cannot silently stop carrying it. No existing gate joins a documented invocation
  to the driver's argument set — the adopter check, the protocol parity check and the kickoff-engine
  check are all copy-parity or literal-string tests — so without this the full bar stays green while
  every documented invocation is missing a required argument.

## 3. Non-goals (OUT)

- **No new phase member, terminal or otherwise, and no move of the core phase floor or the terminal
  set.** This is the unit's central design decision and the owner ratified it against the
  measurements. A phase added to the core set is refused by the driver's own guard with a message
  naming two verbs that cannot write it; added as non-terminal it wedges the next run's preflight
  forever; and the protocol's phase list is joined to the driver's by no gate, so either drifts
  silently.
- No code on the landed terminal. A landing needs no reason.
- No code on a park. Parking is unit 5's mechanism and a park is not a halt.
- No retrofit of existing terminal records BEYOND the ones §4 enumerates. The population is the
  records §4 enumerates AT BUILD TIME, re-derived by the command §4 gives rather than capped at a
  number here: it grows every time any run aborts, and it has grown repeatedly while this spec was
  open. Every record that command finds is migrated by this unit's commit, ARCHIVED records included.
  A blanket no-retrofit rule was the rev-3 position and rested on a population that was zero at the
  old base and is not at this one.
- No claim that the code is trustworthy. The run writes it, as it writes every other authored fact,
  and the protocol's boundary section already states what that is worth.

## 4. Design

### Data model

The vocabulary is a driver constant, read by the leg the same way the leg already reads the core
phase and Definition-of-Done sets from the driver rather than restating them. The effective set is
the core set plus the project's declared extras, composed the way the phase set already is.

The size pin gets its own conf key rather than a third field on the existing floor. The rationale
rev-1 gave for that — that a three-field value is dropped in silence — is FALSE and was refuted
against source: the existing key's parser matches a three-field value on its reject arm first and
fires a named refusal saying it wants two integers separated by a colon, a guard added precisely
because a malformed value once disarmed both pins. The decision survives on the grounds that
actually hold: the floor key is a two-field contract whose malformed-value guard is written for
exactly two fields, so widening it means editing that guard and its arm, while a separate key costs
one conf line, one entry in the leg's required-key loop, and no change to a working refusal.

| Fact | Written by | Read by |
|---|---|---|
| the phase | the terminal producers | every in-kit reader, all on the terminal binary |
| the halt code | the abort verb | `--status`, `--resume`, the new leg check, the wrap-up |
| the free-text reason | the abort verb, through the park helper | a human, and the bypass-flag grep |

The three coexist deliberately. The code is for a machine and for a glance; the reason is for the
owner and stays free text, because a code set that tried to carry the specifics would grow without
bound.

### Inventory

Each core member exists because the research found a real site that reaches it, and each names the
owner turn it needs:

| Code | Reached from | The owner turn it names |
|---|---|---|
| review budget exhausted | unit 1's RUNAWAY CEILING, not its ordinary exit — the convergence predicate promotes a residual blocker to a unit and never halts | the convergence rule failed to terminate; read the round sequence and decide whether the ceiling or the predicate is wrong |
| fork unresolvable | the method's vetoes 2 and 3, and a scope fork | decide the fork |
| awaiting scope approval | a unit at the awaiting-approval status that is NEITHER reachable at the pinned base NOR authored by this run — the residual `TOOL-aBoundedVerdict-3` S1's three cases do not cover, reached when a spec arrives on the run's own branch from elsewhere | approve or amend the scope |
| blocked on an external prerequisite | a unit whose status names a prerequisite outside the run | clear the prerequisite |
| acceptance underivable | the kickoff engine's fifth interactive exit | supply the acceptance check, or split the unit |
| precondition unmet | the kickoff engine's first three interactive exits | repair the repository state |
| gate red out of scope | a red gate whose fix the mandate does not reach | authorise the fix, or widen the mandate |

The mapping is the unit's real content. A code set that did not correspond one-to-one with the
enumerated exits would be a vocabulary invented ahead of its callers, which is what the phase
vocabulary already is.

### Migration

**The population is RE-DERIVED AT BUILD TIME and is not a number in this paragraph.** Every tracked
run-state file that claims the aborted terminal and carries no code fact is a live subject for AC4's
leg check, so each one reds the merge bar the day that check lands. Enumerate it with:

```bash
git ls-files 'memory/builds/*/RUN*.md' | xargs grep -l '^phase: ABORTED'   # then read each for a code fact
```

**Archived records are NOT exempt, and this is the answer rather than an open question.**
`check-unattended.sh` selects `memory/builds/<slug>/RUN(.<PHASE>.<blob8>)?.md` — the live record PLUS
every rotated one, widened at kit 1.6 so that checks 9, 13 and 15 quantify over both. A per-file
check added by this unit therefore sees an archived `RUN.ABORTED.<blob8>.md` like any other file, and
exempting them would take a special case in the new check with no reason behind it while leaving the
bar green over records the leg already reads everywhere else.

The disposition is a RETROFIT, enumerated rather than waived. Each code is READ FROM THAT RECORD'S OWN
PARKED TEXT and never invented. The table is that reading as measured on 2026-08-20; a record the
command above finds and this table does not name is migrated the same way, by the same rule:

| record | the code, and the phrase in its own parked text that gives it |
|---|---|
| `memory/builds/aMeteredTurnstile/RUN.md` | `gate red out of scope` — aborts "at the landing boundary because the merge bar cannot pass on this host", the canary correctly refusing to certify what it could not observe, landing handed to the owner |
| `memory/builds/aWalkedCorpus/RUN.md` | `gate red out of scope` — "origin/main is RED on two of its own merge-bar legs", and raising another build's shrink-only pin "is a SCOPE decision a standing mandate does not delegate" |
| `memory/builds/cBriefedPilot/RUN.md` | `fork unresolvable` — "WHAT I REFUSED TO DECIDE: whether 16 of 22 units is a landable build. That is a scope decision, reserved to the owner by M3 and not delegated" |
| `memory/builds/dClosedLexicon/RUN.md` | `fork unresolvable` — "REFUSED TO DECIDE ... all three are scope calls the standing mandate does not delegate" |
| `memory/builds/aBoundedVerdict/RUN.ABORTED.fc79c21d.md` | `gate red out of scope` — the record NAMES the member: "the fix is outside this mandate's authority, which is exactly the gate-red-out-of-scope case" |
| `memory/builds/aDeclaredBound/RUN.ABORTED.08aaae74.md` | `fork unresolvable` — "neither live blocker is mine to resolve. The first is a SCOPE question ... M3 reserves a fork whose options differ in what gets built to the owner" |

`aDeclaredBound`'s record is the only one with two readings, and the choice is recorded here rather
than left to the builder: it ALSO spent the review round cap. `review budget exhausted` is not it,
because S1 re-read that member to name the RUNAWAY CEILING — a backstop whose being reached is itself
a defect — and that run reached the ordinary round cap instead. Its own text names the surviving
blocker as a scope fork, so that is the code.

Two properties of the migration, unchanged since rev-4:

- It is a DATA migration performed by this unit's commit, not a driver verb. The driver refuses to
  move a terminal record on purpose and nothing here changes that refusal. Adding a code fact to a
  record that is ALREADY terminal is not the act `memory/builds/aBoundedVerdict/RUN.ABORTED.fc79c21d.md`
  records refusing, which was writing a TERMINAL onto another node's live run.
- No waiver registry, no cutoff, no enumeration file: a registry would need a path, a grammar and a
  reader, which is more machinery than the rows it would hold. The rows are the table above and AC4a.

The corpus therefore DOES exercise the new check, which is better than rev-2's position: the red arm
has live subjects as well as fixtures in `tools/unattended/check-unattended.test.sh`, rather than
fixtures alone.

### Rollout

The verb's new required argument is a breaking change for every caller, and rev-1's claim that the
existing gates enforce the update was verified FALSE. There are three documented call sites, not
two: the Skill template and its render, the protocol template and its installed copy, and the
kickoff engine. Every gate over them is a copy-parity or literal-string test — the adopter check
compares the render against its template and conf, the leg compares the shipped protocol against the
installed one, and the kickoff check asserts two literal strings and an exit count. **No gate joins a
documented invocation to the driver's argument set.** So all three could keep omitting the argument
with the full bar green, and the first unattended run to follow the Skill would meet a refusal on
the one exit that exists for a run which cannot proceed.

S9 is the rollout, and it has teeth: the three sites are an explicit scope item, and a source-level
arm asserts that every tracked file spelling the abort invocation also spells the code argument.

### The kickoff engine's size budget

S9 edits `skills/session-kickoff/SKILL.md`, which rides a HARD gate leg no other unit in this build
touches and which this spec's §7 did not name. **No byte figure for that file appears here.** The
INVOCATION moved at the merge base and the ceiling is no longer a positional: `tools/gate-legs.json`'s
argv is now `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` with no number, and
the limit is DECLARED in `tools/template-size-limits.txt`. That leg prints the file's size, its limit,
the bytes under and the percentage on every run, so the builder measures through the leg's own argv
and no number is carried in this paragraph — the numbers rev-4 carried here had already moved by the
time this fold was written, which is the whole argument.

The edit is the code argument on the one abort line plus a code named on each code-bearing exit —
tens of bytes, not a rewrite — and it fits with room left over. **The finding is that nothing in the
spec knew a margin existed at all**, and the fix is that AC9 now re-measures it rather than asserting
it.

### Alternatives rejected

- **A new terminal phase plus a producer verb.** What the owner first asked for. Measured cost: each
  new terminal needs its own producer, each producer's refusal branch needs an armed assertion in a
  leg that took eighteen minutes to run on the probe host, the core floor moves, and the protocol's
  prose phase list drifts from the driver's with no gate joining them. Rejected by the owner on those
  measurements.
- **A non-terminal halt phase.** Writable today with a three-line diff, and it wedges the fleet: the
  record counts as live forever, so the next run's preflight is hard-blocked and resume tells every
  future session to carry on. Reproduced.
- **A reason-code convention with no validation.** Costs nothing — appending one to a real tracked
  run-state file leaves both gates green, which is exactly the problem. A convention nothing checks
  is a convention that is followed until the first hurry.
- **Reusing the park helper's kind field as the vocabulary.** Tempting: the field exists and is
  already distinct per call site. Rejected because the kind describes the LINE's grammar, not the
  run's disposition, and overloading it would put two meanings on the field whose single meaning was
  itself the product of a review finding.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the vocabulary, the verb, and the resume path's stale fact-count
comment) · `tools/unattended/check-unattended.sh` and its sibling ·
`tools/unattended/unattended.test.sh` · `.unattended.conf` ·
`tools/unattended/.unattended.conf.example` — the seed a real adopter copies, which nothing
validates against the required-key set · `tools/unattended/kit.toml` ·
`tools/unattended/PROTOCOL.template.md` and the installed protocol (the verb section, the phase
section, and the fact pin with its enumeration) · `tools/unattended/SKILL.template.md` and the
rendered Skill · `skills/session-kickoff/SKILL.md` (the exits' abort disposition names the code) ·
EVERY run-state record §4's migration table enumerates, re-derived at build time by §4's command ·
`memory/map/features/unattended.md` (BOTH of its fact-count statements) ·
`tools/unattended/check-unattended.sh`'s own header check COUNT, which S5 moves by one and which no
gate observes — `TOOL-aBoundedVerdict-1` moves it again, so the two units state their moves one apart
rather than both writing the same number. That header comment is the ONLY carrier of that count: the
charter's gate-suite enumeration it used to be paired with no longer exists, because the legs are
single-sourced from `tools/gate-legs.json` now, and `AGENTS.md`'s body is generated between
`gov:playbook` markers — a hand-edit there reds the playbook parity leg and a template edit is
outside this unit · S10's four carriers: `memory/HYGIENE.md`,
`tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/check-memory-hygiene.sh` and
`tools/memory-tree/check-memory-hygiene.test.sh` · `memory/guides/SESSION-KICKOFF.md` (the manifest
re-stamp; `.unattended.conf`, `skills/session-kickoff/SKILL.md` and
`tools/memory-tree/check-memory-hygiene.sh` are all on its watch list) · the KIT VERSION sites, which
are never "the constant": for the UNATTENDED kit, `KIT_UNATTENDED_VERSION=` and its same-line
`gov:kit` marker in BOTH `tools/unattended/unattended.sh` and
`tools/unattended/check-unattended.sh`, the `gov:kit` marker in
`tools/unattended/PROTOCOL.template.md` and in `tools/unattended/SKILL.template.md`, and the
re-rendered `.claude/skills/unattended/SKILL.md` that `tools/check-wiring.sh` compares against the
tracked copy — all of them forced by `tools/check-kit-versions.sh`; and for the MEMORY-TREE kit that
S10 edits, `KIT_MEMORY_TREE_VERSION=` in `tools/memory-tree/check-memory-hygiene.sh` plus the
`gov:kit memory-tree@` marker on every tracked `tools/memory-tree/*.template.md`, a population that
gate DERIVES rather than lists.

## 5. Production-readiness checklist

- security — N/A as a surface, but the code is a run-authored field and the spec says so where a
  reader could otherwise mistake it for evidence.
- perf / scale — N/A. One extra field read per record per leg run.
- a11y — N/A.
- i18n — the codes are identifiers, not prose, and are not translated.
- error / empty / loading states — an undeclared extras key, an empty effective set, an unlisted
  code, and a missing code are four distinct refusals. An empty effective vocabulary must refuse
  rather than accept everything, on the same rule the phase set already follows.
- observability — S5 is the whole point of the unit; without a reader this is the decoration the
  protocol warns about, and §3 says so.
- risks — the real risk is vocabulary rot: a code nobody can reach, or a halt with no code that
  fits. §8 carries both as forks.
- testing + left-shift gates — the leg check plus an arm per refusal branch. The left-shift for the
  wrong-lever risk is the one-to-one mapping table in §4: a future code with no enumerated site is
  visibly a new row with an empty middle column.
- migration / rollback — §4's migration paragraph; rollback removes the required argument, and
  records written with a code stay readable because the field is additive.
- user docs — the protocol's verb and conf tables, and the rendered Skill.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --abort <slug> --reason r` runs with no code,
  it refuses naming the legal set, and the record is unchanged. Asserted on the on-disk effect.
- **AC2** — When the code is outside the effective vocabulary, the verb refuses; when it is a
  project extra declared in `.unattended.conf`, it is accepted. Both arms in
  `tools/unattended/unattended.test.sh`.
- **AC3** — When a run aborts with a code, `bash tools/unattended/unattended.sh --status <slug>` and
  `--resume <slug>` both name it, and resume states the run is finished rather than resumable.
- **AC4** — When a tracked run-state file claims the aborted terminal and carries no code fact,
  `bash tools/unattended/check-unattended.sh` reds naming the file. No exemption clause and no
  waiver: every record §4's migration enumerates at build time is migrated by this unit, so the check
  is green over the real tree on the day it lands, and both arms also live in
  `tools/unattended/check-unattended.test.sh` fixtures.
- **AC4a** — When each record §4's migration table names is read after the migration, it carries the
  code that table reads out of its own parked text: `gate red out of scope` in
  `memory/builds/aMeteredTurnstile/RUN.md`, `memory/builds/aWalkedCorpus/RUN.md` and
  `memory/builds/aBoundedVerdict/RUN.ABORTED.fc79c21d.md`; `fork unresolvable` in
  `memory/builds/cBriefedPilot/RUN.md`, `memory/builds/dClosedLexicon/RUN.md` and
  `memory/builds/aDeclaredBound/RUN.ABORTED.08aaae74.md`. And
  `bash tools/unattended/check-unattended.sh` is green over the whole tracked population RE-DERIVED at
  build time by §4's command, ARCHIVED records included — a record that command finds and the table
  does not name is migrated the same way BEFORE this criterion is claimed.
- **AC5** — When the core vocabulary shrinks below its declared floor,
  `bash tools/unattended/check-unattended.sh` reds; when the floor key is absent or malformed, it
  refuses rather than passing with the pin disarmed.
- **AC6** — When the leg reads the vocabulary, it reads it from the driver, asserted as the
  COMPLEMENT rather than as a prefix grep: the leg's only reference to the vocabulary is the
  `core_of` helper call taking the key as its argument, and no member token appears in
  `tools/unattended/check-unattended.sh` under a word-anchored grep of the members themselves. The
  prefix alternation rev-1 proposed cannot distinguish a member from an unrelated identifier, and
  `TOOL-aBoundedVerdict-1` lands a constant whose name that alternation would have matched.
- **AC7** — When every tracked file spelling the abort invocation is greped, each also spells the
  code argument — all three documented call sites — and the arm that asserts it lives in
  `tools/unattended/unattended.test.sh`.
- **AC8** — When the region's fact count is extracted with `sed -nE` from each carrier S7 enumerates
  — `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/PROTOCOL.template.md`,
  `tools/unattended/unattended.sh` and `memory/map/features/unattended.md` — every carrier yields
  exactly ONE token and all carriers yield the SAME token. The criterion asserts AGREEMENT and never
  a value, and it is anchored PER CARRIER on that carrier's own sentence rather than on a list of the
  numerals that happen to be stale today:

  ```bash
  for f in memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/PROTOCOL.template.md \
           tools/unattended/unattended.sh memory/map/features/unattended.md; do
    printf '%s => ' "$f"
    sed -nE 's/.*(exactly|carries) ([[:alpha:]]+|[0-9]+) facts.*/\2/p;
             s/.*[^[:alnum:]]([[:alpha:]]+|[0-9]+) of them, enumerated.*/\1/p' "$f" \
      | sort -u | tr '\n' ' '; echo
  done
  ```

  A carrier printing NOTHING is a carrier whose sentence stopped matching, and that reds as loudly as
  a disagreement. That is the failure the rev-3 and rev-4 patterns each walked into in turn: an
  alternation of VALUES stops matching the moment the pin moves past its longest listed word, returns
  zero hits, and reads as green over a stale pin — the criterion failing in exactly the way it exists
  to prevent. Run over the tree before the edit this prints DISAGREEING tokens, so the criterion is
  red by construction today and its failing case has been observed rather than imagined.
  **What it does not check:** it does not count the protocol's numbered enumeration, so it cannot
  catch an entry added without the count being moved. S7's edit does both in one pass; this criterion
  catches a carrier LEFT BEHIND, which is the failure that has actually happened at every move.
- **AC9** — When `skills/session-kickoff/SKILL.md` is edited,
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` is green — no positional; the
  ceiling is declared in `tools/template-size-limits.txt` — re-measured rather than assumed.
- **AC10** — When the Skill and protocol are re-rendered,
  `bash tools/unattended/adopt-unattended.sh --check` reports in sync with no surviving placeholder
  shape, and `bash tools/check-kit-versions.sh` is green with both unattended constants moved.
- **AC11** — When any NEW `fail` branch exists, it is armed in that gate's sibling test or pinned in
  `memory/project/unarmed-branches.txt` with its reason, and `python tools/memory-tree/check-arms.py
  --check` exits 0. `ARMS_FLOORS` moves only where `--report` shows the measured counts grew.
- **AC12** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.
- **AC13** — When a review record's first line is outside the closed verdict set,
  `bash tools/memory-tree/check-memory-hygiene.sh` reds naming the file; when it is a member, the
  check is green — both arms in `tools/memory-tree/check-memory-hygiene.test.sh` fixtures, and green
  over the real tree, which is what forces S10's forward-only selector to be chosen rather than
  assumed. The cross-kit agreement row does NOT land here and this criterion does not grade it: the
  row in `tools/memory-tree/marker-contract.test.sh`'s case table asserts that the hygiene gate and
  `TOOL-aBoundedVerdict-1`'s `--review` verb accept the same set, and that verb does not exist on the
  day this unit lands — this unit is sequenced ahead of it. So the armed form of S10's duplication is
  claimed by that unit, whose Files touched names the harness and whose own criterion grades the row;
  this unit ships the SET and states the duplication, and the drift arm arrives with the second
  reader. A criterion graded on a file its spec does not admit editing is the defect this same review
  round found twice elsewhere in this build. And `bash tools/memory-tree/check-verdict-epoch.sh` is green,
  which requires `KIT_MEMORY_TREE_VERSION` to move in the same commit because check 5's verdicts
  changed.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/adopt-unattended.test.sh` · `tools/check-kit-versions.sh` ·
`tools/check-template-size.sh skills/session-kickoff/SKILL.md` — the hard leg on the kickoff engine,
whose ceiling is declared in `tools/template-size-limits.txt` and whose headroom the leg itself
prints · `skills/session-kickoff/manifest-check.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` and `tools/memory-tree/check-memory-hygiene.test.sh` —
S10 edits check 5's grammar, and this unit also edits two files under the memory root and grows a
read-path member · `tools/memory-tree/check-verdict-epoch.sh` — the constant that DATES the engine's
verdicts must move when they do, and S10 moves them ·
`tools/memory-tree/marker-contract.test.sh` — the cross-kit case table that carries S10's
verdict-set agreement row ·
`python tools/memory-tree/corpus_ids.py --report` for the read-path share ·
`python tools/memory-tree/check-arms.py` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`python tools/codebase-map/test_codebase_map.py` · `python tools/drift-audit/drift_report.py
--check` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — what does a run do when no code fits?** Options: add a catch-all member, which is a hole
  that will swallow the vocabulary within a few runs; require the project to declare an extra, which
  stalls a run at the moment it is trying to stop; or refuse to abort, which is the worst of the
  three. Recommendation: no catch-all, and the unclassifiable case aborts under the closest code with
  the specifics in the free-text reason — with the mismatch itself worth a backlog row when it
  happens.
  RESOLVED (agent, 2026-08-20, delegated): as recommended — NO catch-all member. The
  unclassifiable case aborts under the closest code with the specifics in the free-text reason, and
  the mismatch earns a backlog row when it is first hit. Mechanism-only. The two alternatives are
  strictly worse and the spec already says why: a catch-all is a hole that swallows the vocabulary,
  and requiring a fresh project declaration stalls a run at the moment it is trying to stop.
- **F2 — does the leg assert the code is REACHABLE, not merely legal?** A member no verb can produce
  is the phase vocabulary's disease. A reachability assertion would grep the callers for each member.
  Recommendation: not in this unit. The one-to-one table in §4 is the human-readable form of the same
  claim, and a grep-based reachability check over prose callers is the kind of predicate this repo
  has found vacuous twice.
  RESOLVED (agent, 2026-08-20, delegated): NOT in this unit. Mechanism-only, and the richer option
  is discarded by this repo's own rule against a predicate it cannot arm: a grep over prose callers
  is the vacuous-selector class, and §4's one-to-one table already carries the claim in the form a
  reader can check. Recorded as a limit of the leg rather than dropped silently.
- **F3 — does the wrap-up row in the build method make this a cross-kit change?** The wrap-up
  derivation lives in the memory-tree kit's rendered method document, so S6 moves a memory-tree
  carrier for an unattended-kit reason. Options: put the row there anyway, since the method already
  points at the unattended protocol for exactly this kind of fact; or leave the method alone and let
  the code reach the owner through the protocol only. Recommendation: leave the method alone —
  its own rule is that a fact stated in it and in a carrier it points at is a defect in it.
  RESOLVED (agent, 2026-08-20, delegated): LEAVE the build method alone. Mechanism-only, and the
  alternative is refused by the method's own stated rule rather than by preference — M9's wrap-up
  row already derives from the authored record, and the halt code lands in that record, so the
  owner reaches it through a carrier the method already points at. No cross-kit change.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records that the owner ratified the code-over-phase decision
  against the measured cost of both, so §3's central non-goal is a decision and not an omission.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. The set-level blocker: the code is an
  EIGHTH authored fact in a region the binding protocol pins at seven, which rev-1 neither named nor
  moved while a tracked sibling spec answered the identical question the other way by name. S3 now
  argues the fact shape on the protocol's own membership test and on the singleton-versus-history
  distinction, and S7 moves the pin in all four places it is spelled — including a driver comment
  that was already stale at five. The rollout claimed two callers under enforcing gates; there are
  three and no gate joins any of them to the argument set, so S9 and AC7 replace the claim. Added
  the seventh member for a unit blocked on an external prerequisite, which
  `TOOL-aBoundedVerdict-3` routes here and the six-member set excluded. Added the kickoff engine's
  measured size budget and its hard gate leg, the adopter's seed conf, the map dossier's fact count,
  and the manifest re-stamp. The floor-key rationale rested on a false claim about the existing
  parser and is restated on grounds that hold. AC6's prefix grep would have broken under the unit
  that lands after this one and is replaced by the complement assertion.
- rev-3 · 2026-08-16 · folded round 2. S4 asserted "Both keys are NAMED in the design" and named
  neither — round 1's finding restated rather than fixed — so both are now spelled, with which is
  required and which optional. The migration's exemption, its registry and its enumeration all
  answered a question the tree does not ask: the measured population of codeless aborted records is
  ZERO, both tracked run-state files being landed, and the recording the enumeration would have gone
  into is read by no gate. The pin's dossier statement is TWO statements, not one, and the completeness
  grep as written misses the bare-numeral form. The wrap-up scope item still pointed at the build
  method after the files list had already dropped it on this spec's own recommendation; it now lands
  in the protocol and says what changes if the fork resolves the other way. The awaiting-approval
  member had lost its last routing site to the stall unit's three cases and is narrowed to the
  residual they leave. Added the hygiene gate and the read-path reporter to §7, and the leg's own
  check count to Files touched, sequenced against the other unit that moves it.

- rev-4 · 2026-08-17 · M7 REGROUND onto the new merge base, and the most affected spec. BLOCKER: the
  migration said the population of codeless aborted records was zero; at the new base it is ONE, a
  named tracked record that this unit's own leg check would have redded the bar on at landing — it is
  now a stated one-record retrofit rather than a claim of nothing to do. The authored-region pin moved
  from seven to eight under the spec, so the halt code is the NINTH fact, not the eighth, and the
  in-tree precedent is now exact: the eighth fact is a singleton written by a terminal verb. The
  completeness grep is rewritten NUMBER-AGNOSTIC — the two-value alternation would have returned
  nothing while two carriers still said eight, the criterion failing exactly as it exists to prevent.
  The kickoff size leg lost its positional; the ceiling now lives in a declared limits file.
- rev-5 · 2026-08-19 · widened by the close-path audit's medium 24 and by `TOOL-aBoundedVerdict-1`'s
  rev-6 reversal. Two changes, no removals. **S10 is new**: the review VERDICT vocabulary is the same
  defect as the halt vocabulary one document over — measured at 18 distinct verdict lines, 5 leading
  tokens, 32 records carrying none, and zero carrying the token the method calls the loop's only exit —
  so this unit, whose title is about a vocabulary something reads, takes it. Forward-only, on §3's
  existing no-retrofit reasoning. **The first core halt member is re-read**: it used to name unit 1's
  cap refusal, and unit 1 no longer has a cap; it now names the runaway ceiling, whose being reached is
  itself a defect, and the owner turn it names changes with it — the old wording would have told a
  returning owner to re-scope a unit when the real question is whether the convergence predicate
  terminated. The member is NOT removed, so the shrink-only floor does not move.

- rev-7 · 2026-08-20 · M3 fork sweep, before any code. F1, F2 and F3 RESOLVED under the delegated
  rule; all three were mechanism-only and all three took the spec's own recommendation, F2 because the
  richer option is an unarmable predicate and F3 because the build method's own rule refuses it. §8's
  first non-blank line is now the machine-legal `none` form. **Also repaired: rev-6 had no §9 entry.**
  The status header was bumped to rev-6 and §4:92 explains what rev-6 added, but the revision log
  stopped at rev-5 — a rev bump whose only record is the number in the header is the change nobody can
  audit, and it is the same class as a fork mark that never landed. What rev-6 added, recovered from
  §4: the three carriers rev-5 did not declare.

- rev-8 · 2026-08-20 · folded the M4 spec audit's 2026-08-20 round — three blockers, and every one of
  them was a stale MEASUREMENT still being treated as a fact. **B1**: §4's migration said there were
  four tracked run-state files with one codeless ABORTED record, while §3 capped the retrofit at
  "exactly one" and AC4 forbade both an exemption and a waiver — so a builder obeying §3 would have
  landed a leg check that reds the bar over every record §3 told it to leave alone. The population is
  now RE-DERIVED by a command, the records are enumerated in a table with each code read out of that
  record's own parked text, §3's cap points at that table instead of at a number, and the question
  nobody had answered — are the two archived `RUN.<phase>.<blob8>.md` records exempt — is answered
  NO, from the leg's own selector, which has quantified over archived records since kit 1.6.
  **B2 and L4**: S7 instructed an edit of numerals that exist in no carrier (`eight`→`nine`, a "NINTH
  entry", a driver comment said to read FIVE) and Files touched said "the seven-fact pin", so the pin
  move would silently not have happened while S3 in the same spec said every ordinal had been deleted.
  S7 is now a numeral-free list of carrier PATHS with each site's role, and so is Files touched. The
  audit's brief listed the map dossier as no longer a carrier; it still holds TWO count statements at
  HEAD, so it stays in the list — dropping a live carrier is how this pin went stale three times.
  **B3**: S10 asserted that rev-6 "adds them to Files touched and gives S10 its own acceptance
  criteria" and NEITHER had happened — no memory-tree carrier was in Files touched and no AC mentioned
  a verdict token. The false self-claim is deleted, the four carriers are declared, AC13 is the red/green
  criterion over hygiene check 5, and `check-verdict-epoch.sh`, the hygiene sibling test and the
  marker-contract harness join §7. **H1**: AC8's "number-agnostic" alternation stopped at `ten` while
  the pin reads past it, so it returned zero hits and read GREEN over a stale pin — the failure its own
  text says it was rewritten to prevent, one word later. It now extracts one token per carrier and
  asserts the tokens are EQUAL, anchored on each carrier's own sentence; the predicate was run over the
  real tree during the fold and prints disagreeing tokens, so its failing case has been observed.
  It also states what it does not check. **H2**: S3 said this build "moves the pin exactly once" against
  a README that had been corrected to name two movers; with `TOOL-aBoundedVerdict-21` PARKED there is
  exactly one mover again, and S3 says which and why rather than counting. **H3**: the verdict token set
  was demanded byte-identical to "the one -2 defines" while -2 enumerated no member and named no source.
  S10 now enumerates `CLEAN`, `CLEAN WITH FIXES`, `BLOCKED`, names the memory-tree kit as canonical
  owner, and replaces the unobservable byte-identity claim with a row in the cross-kit case table
  `TOOL-aBoundedVerdict-4` S2 already extends — one harness, no new gate leg. **H4**: Files touched
  instructed an edit to `AGENTS.md`'s gate-suite bullet, which no longer exists and sits inside a
  generated `gov:playbook` region besides; that carrier is deleted and the leg's own header comment is
  named as the only one. **H22**: `memory/DECISIONS.md:68` is now cited in S3, which states that the
  decision and its three measurements survive and the ORDINAL clause does not, and that the superseding
  row is the build's to commit rather than this unit's to write. Two fixes offered a choice and both took
  the narrower option: check 5 is EXTENDED rather than renumbered (a new number moves the hygiene leg's
  check count for nothing), and S10 stays in this unit rather than splitting into its own (a split needs
  an id, a spec and a roster edit to fix a false sentence). Not folded by choice: the byte figures for
  the kickoff engine's size budget were deleted for the same reason as everything else here — the leg
  prints size, limit and headroom on every run, and the numbers rev-4 wrote had already moved.

- rev-8 · 2026-08-20 · **written BEFORE this unit's code, because two of S10's instructions do not
  survive contact with the files they name** — and the method's rule is that a divergence changes the
  spec first. (1) "the FIRST line of a review record" is already check 21's, which requires the
  `**Serves:**` binding line there; every record in the corpus puts the verdict below it. The rule is
  now one `## Verdict: <member>` line, position-independent. (2) check 5 is a recording-FILENAME
  grammar; a content assertion under its number would make a structural check read as a semantic one,
  which is the gate-header hazard this repo states as a rule. S10 takes a NEW check number, which this
  repo's own trap calls the cheap option — the leg's name carries no count and `tools/gate-legs.json`
  does not move for a new check, so the cost is an arms floor, an arm per new fail site, and a
  `memory/HYGIENE.md` entry. (3) The forward-only selector, left open by the fold, is PICKED: a dated
  cutoff key, the instrument the conf already carries four times and the one the sibling unit chose
  hours earlier for the same shape of problem. The grandfather registry was the alternative and is for
  files kept under historical NAMES, which is a different question.

- rev-9 · 2026-08-20 · **built. The pin was worse than S7 described, and S7 was already the part of
  this spec that expected the worst.** Read live at build time, the four carriers disagreed THREE WAYS
  AT ONCE: the protocol pair said eleven, the driver's own resume comment said seven, the map dossier
  said seven. Nothing counts facts, so no gate had ever compared them. All four now say twelve.
  **AC8 then caught my own edit**, which is the best thing that happened in this pass: the dossier
  printed NOTHING, because I had written "carries / twelve facts" across a line break and the
  extraction is line-based. That is exactly the case AC8 says reds as loudly as a disagreement — a
  carrier whose sentence stopped matching — and it fired on the person who wrote it.
  **A `fail` message cannot contain a command substitution and still be armable.** Both new abort
  refusals ended `Legal codes: $(halt_codes)`, and the arms gate signs a branch with the LITERAL source
  text of its `fail` call, so the substitution became part of the signature and no runtime arm could
  ever match it. Bound to a name, with only a plain interpolation after the sentence. Same family as
  the recorded positional trap, third instance this build has hit.
  **The migration was DERIVED and not copied, which is what AC4a asks, and the derivation held.** The
  population was re-derived at build time with an assertion that would have caught a record another
  node added — twenty-five commits arrived from `origin/main` during this run — and each code was read
  out of that record's own parked text. All six matched the table. The one that deserved the scrutiny
  is `dClosedLexicon`: its reason reads as review NON-CONVERGENCE, which would suggest the ceiling
  member, but the CAUSE of the halt was a refused scope decision (ship weakened, cut scope, or land
  the remainder), and reading it as the kit's runaway ceiling would be anachronistic — that ceiling did
  not exist when the run stopped. `fork-unresolvable` stands.
  **What migrating an ARCHIVED record costs, since nothing else says it.** A rotated record is named
  `RUN.<phase>.<blob8>.md` from its own blob hash, so editing its bytes leaves a name that no longer
  reproduces from its content, and nothing verifies that pair. It is BENIGN and the protocol says why:
  the name exists so two records with the same content cannot collide, not as an integrity check, and
  a later edit cannot reintroduce a collision. Recorded because a reader who assumes the name is a
  checksum would conclude otherwise.
  **A newly REQUIRED conf key has THREE seeds, not two**, and the third is the one that bites: this
  repo's own conf, the adopter's seed conf, and the leg test's fixture conf. Omitting the third redded
  every conforming-tree arm in that suite at once, which is the "a gate-required key missing from the
  seed reds the first check on install" hazard happening inside the test written to catch it. The
  fixture value is DERIVED from the shipped driver like its two siblings, because a literal floor in a
  fixture goes stale the moment a member is added.
  **All six new refusals were OBSERVED against the real tree before being armed** — floor undeclared,
  floor malformed, vocabulary below floor, vocabulary empty, aborted record with no code, code outside
  the vocabulary — and the record-level pair carries a CONTROL, without which every arm could be
  passing on a check that reds on any aborted record at all.
  **One id citation was caught before it landed.** The conf comment first read `TOOL-aBoundedVerdict-2`,
  and `tools/unattended/.unattended.conf.example` is product source under `tools/`, so it would have
  taken the non-terminal-citation drift signal from 2 to 3 and broken a shrink-only pin. Paraphrased.
  This is the cross-unit rule this build states, and it is easy to break while writing a comment about
  the unit itself.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "terminal phase for a run that cannot continue"` returns
the unattended conf and the driver and no third seam, which is consistent with the research finding
that no reader of the phase exists outside the kit. Three existing seams are extended rather than
duplicated: the driver-side core-set constant with the leg reading it through the same helper that
already reads the phase and Definition-of-Done sets; the authored-fact writer, unchanged; and the
conf's required-key loop. The one seam deliberately NOT reused is the existing two-field size floor,
for the parse reason §4 gives.

Recall terms used, recorded for the reground: halt code abort terminal phase vocabulary shrink-only
floor run-state authored fact status resume reader unattended driver conf declaration.

