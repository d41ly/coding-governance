# Blocker re-review of the round-2 fold — TOOL-aPacedTurnstile (units 1-7)

**Serves:** spec-audit TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7

**Date:** 2026-08-18 · **Tier:** 2 · **Streams:** tooling · **Base:** `6e45fb75` · **Round:** 3
**Subject:** commit `6e45fb7`, "TOOL-aPacedTurnstile: fold all 29 round-2 findings, blocker first",
read as the seven spec files now stand plus the build README. **Question asked:** did the round-2
blocker fix land WHOLE — in every carrier and in the unit that owns the interface it now calls —
and did the fold of the other twenty-eight findings break anything it touched? **Out of scope:**
the five owner decisions settled at kickoff, the round-2 findings that closed cleanly and were
re-verified only far enough to classify them, the eight raw findings round 2 refuted, and anything
requiring code that does not exist yet.

## Verdict: BLOCKED

The R1 blocker fix did NOT land whole. It landed in `TOOL-aPacedTurnstile-7` and nowhere else. `-7`
now states predicate 0 correctly — the recorded digest joined against a fresh fingerprint computed
AT THE RECORDED SHA, obtained by CALLING `TOOL-aPacedTurnstile-5`'s shipped
`tools/run-gates/gate-fingerprint.sh` rather than by reimplementing it — but `-5`, which owns that
helper, still declares exactly one digest, over the committed tree object plus the sorted porcelain
status lines plus the blob hashes of every dirty-or-untracked file that still exists. That is a
function of the live working tree. It takes no sha, and `-5` §4 Files touched spells it with no
argument, as "called by the runner and by `.githooks/pre-push`". The corrected predicate names a
computation the owning interface cannot perform. R19's fold gave the helper a name; nobody gave it
a signature.

That leaves a builder three readings and all three fail. Call the helper as specified and the
digest is taken at the pushed tip, predicate 0 fires on every push whose tree moved, and the scoped
path is unreachable — R1 restored verbatim. Reimplement an at-a-sha digest inside the hook and you
break the one sentence S2b adds in the same breath, and land the
two-implementations-silently-disagree class `-5` S5 exists to prevent, which fails toward FULL
forever. Add an at-a-sha mode to the helper — the right answer — and no spec declares it, no
criterion grades it, and unless it is specified to reproduce byte-for-byte what the runner stamps
on a clean tree, the two modes hash different input arities and predicate 0 mismatches
unconditionally. The set has no green state until `-5` moves. AC6b's control half, added by this
fold precisely to stop predicate 0 firing unconditionally, cannot be satisfied by the only
implementation `-5` currently declares.

The second theme is that multi-carrier fixes left residue, and two of them created new defects
inside the same commit. R10's fix promotes `tools/run-gates/run-gates.gov.test.sh` to its own gate
leg. That new leg is unaccounted for in four places: `-1` §4 Files touched still says the manifest
gains TWO new legs; `-1` S6 still justifies four `[[gate_leg]]` rows by a census that omits it;
`-1` S8's registry surgery is enumerated exhaustively and carries no `[[exempt_leg]]` row for it,
which is the one shape `tools/govkit/govkit.py` reds on for a manifest leg claimed by no descriptor
— at `-1`'s own single-commit landing, on a gate `-1` §7 lists and AC3 asserts green; and `-3` S2's
freshly corrected "73 rows" is 74 once the leg lands, on the arm R10 itself moved into that
harness. R17's fix froze a number R10's fix had already moved. That is R17's own defect class
reintroduced by another finding's fix, in the same commit.

The third theme is that the fold swept scope items and criteria but not the sections that summarise
them. `-3` alone of the four units carrying the gov harness never gained it in §7, §4 Files touched
or S8, so this unit's stated DoD cannot see its own headline criterion and S8 still assigns the
contiguity arm to the shipped canary that AC6 moved it out of. `-7` §5's user-docs line still reads
"all three carriers" against an S9 the fold rewrote to a MEASURED seven, two of them product files
an adopter receives. `-7` §8's ratified second fork still asks whether `tools/push-main.sh` should
force full on a retry, still answers YES for the lander, and still closes "Predicate 7 closes it" —
a predicate the renumbered table no longer has, in a document whose S2b and AC6c explicitly move
the mechanism off the lander. A ratified §8 answer is binding text by the build method; this build
has now been bitten by that class four times (R6 and R29 in round 2, both folded here, and this one
created by the fold itself).

Two smaller classes round out the list. Some new criteria grade against declarations that were
never made: `-5` AC15 grades "the declared retention bound" and no scope item, section or fork
declares a value, while the sibling pattern in `-4` S8 insists a bound be "a DECLARED value with
its reasoning beside it". And some new criteria name harnesses that cannot observe them: AC6d
asserts a header the runner wrote inside a suite whose own header line says the gate is stubbed so
the bar never runs, and AC9b asserts a guard comparison that `govkit.py` does not perform — a fact
`-7` S10's own new paragraph states verbatim, with no scope item and no files-touched row to build
it.

Counting: 1 BLOCKER, 3 HIGH, 8 MEDIUM, 11 LOW, against round 2's 1 / 9 / 15 / 4 and round 1's 5 /
25 / 13 / 1. Six of the twenty-three are the same defect reached by two lenses and three by three
lenses; they are kept separate, as rounds 1 and 2 kept theirs, because the lenses carry different
evidence and the fix lands in different files. Two raw findings were refuted and are listed at the
end. Nothing here challenges the architecture — the emitter, the turnstile, the chunking, the
read-side inversion and the deployable-kit boundary all survive a third reading. The fold closed
twenty-three of the twenty-nine round-2 findings outright and left no finding untouched, which is a
good commit; what it did not do is finish the one that mattered most.

## Findings

### T1 - BLOCKER - TOOL-aPacedTurnstile-7 §2 S2b, the CALLING sentence · §4 Data model

- **Claim:** the blocker fix restated predicate 0 as a join at the RECORDED sha but did not land in
  the unit that owns the digest. S2b in the same breath says the hook computes it "by CALLING
  `TOOL-aPacedTurnstile-5`'s shipped `tools/run-gates/gate-fingerprint.sh`, never by reimplementing
  the digest". `-5` S5 and `-5` §4 define that helper as one digest over the committed tree object
  plus the porcelain status lines plus the blob hashes of every dirty-or-untracked file that still
  exists — a function of the WORKING TREE at invocation, with no sha argument anywhere in `-5` (no
  parameter, no rev, no sha placeholder; §4 Files touched describes it only as S5's digest, "called
  by the runner and by `.githooks/pre-push`"). `-1`'s kit layout says the same thing a third time:
  shipped as its own executable because the hook "must compute the same one". Invoked from a
  pre-push hook, that helper computes at the pushed tip. The corrected text names a computation the
  owning interface cannot perform, and the mechanism it prescribes is the tip join round 2 called a
  blocker.
- **Impact:** all three readings available to a builder fail. Call the shipped helper as specified
  and the digest is taken at the tip, predicate 0 fires on every push whose tree moved, the scoped
  path is unreachable and predicates 3-6 are dead code again — R1 restored verbatim. Reimplement an
  at-a-sha digest in the hook and you break S2b's own sentence and land the
  two-implementations-disagree class both specs warn about, which fails toward FULL forever. Add an
  at-a-sha mode to the helper — the right answer — and no spec declares it; unless that mode is
  specified to reproduce byte-for-byte what the runner stamps on a CLEAN tree (empty porcelain
  component, empty dirty-blob set: the digest is over three inputs, two of which do not exist at a
  bare sha), the two modes hash different input arities, predicate 0 mismatches unconditionally,
  and the blocker returns in its most expensive form. The set has no green state until `-5` moves,
  because AC6b's control half cannot be satisfied by the only implementation `-5` currently
  declares.
- **Fix:** edit `-5` S5 and §4 The fingerprint to declare the helper's two modes explicitly — the
  default working-tree digest the runner stamps, and an at-a-rev mode the hook calls — with the
  binding statement that on a clean tree the two produce the SAME value, the porcelain and
  dirty-blob components being empty and the rev mode supplying them empty rather than omitting
  them. Add the mode to `-5` §4 Files touched. Then narrow `-7` S2b's CALLING sentence to name that
  mode with its argument, and correct `-1`'s layout gloss, which currently says the hook computes
  "the same one".
- **Confirmed because:** `-5` §2 S5 and §4 The fingerprint declare one digest over the committed
  tree object plus the porcelain lines plus the dirty-blob hashes — a working-tree function with no
  rev/sha/argument anywhere in the file — and §4 Files touched describes
  `tools/run-gates/gate-fingerprint.sh` only as "called by the runner and by `.githooks/pre-push`",
  while `-7` S2b, §4 Data model, table row 0 and AC6b all require a fresh fingerprint "computed AT
  THE RECORDED SHA" from that same helper: an at-a-rev mode no spec declares and that neither Files
  touched table carries.

### T2 - HIGH - TOOL-aPacedTurnstile-7 §2 S2b, predicate 0 · §4 Data model

- **Claim:** R1's fix landed in `-7` alone. Predicate 0 now joins the recorded digest against a
  fresh fingerprint computed AT THE RECORDED SHA, computed by CALLING
  `tools/run-gates/gate-fingerprint.sh` — but `-5` S5 and `-5` §4 define that helper as one digest
  over the committed tree object, the sorted porcelain status lines, and the blob hashes of every
  dirty-or-untracked file that still exists: a function of the LIVE working tree, with no sha
  argument and no mode that computes at an arbitrary commit. `-5` was edited by this same fold
  (R19) to give the helper a name, and was not extended to give it the parameter the corrected
  predicate now requires. The two files also disagree on what predicate 0 observes: `-7` states
  flatly "It does NOT detect a dirty working tree", while under `-5`'s definition every call
  includes the porcelain and dirty-blob components, so any push from a dirty tree yields a
  different digest and predicate 0 fires.
- **Impact:** `-7`'s builder has no callable interface for the join the blocker fix specifies, and
  the two paths of least resistance are the two failures both specs already name — call the helper
  with no argument, which is the pushed-tip join round 2 called a blocker, or reimplement the
  digest with a sha parameter, which is the two-answers-to-one-question class S5 exists to prevent.
  AC6b's control half is the arm that would catch it and it is fixture-built, so it can be
  satisfied by a fixture whose working tree is clean while the shipped hook is not.
- **Fix:** extend `-5` S5 and §4 to define the helper's invocation contract — a sha argument
  selecting the tree object to digest, with the working-tree component EMPTY when a sha is
  supplied, which is what makes the recomputation equal the value written under S7's clean-at-start
  precondition, and the no-argument form staying the runner's live-tree digest. Add the argument to
  `-5`'s Files touched row for `gate-fingerprint.sh`, spell the same two-form call in `-7` S2b, and
  either drop or qualify `-7`'s "It does NOT detect a dirty working tree" so it is true of the form
  the hook actually calls.
- **Confirmed because:** `-5` S5 and §4 The fingerprint define the helper with no argument and no
  sha-selected form anywhere in the file, while `-7` S2b and §4 Data model require a fresh
  fingerprint computed at the recorded sha obtained by CALLING it. Round 2's R1 fix text only asked
  `-7` to restate the join and R19 only asked for a name, so the invocation contract was never
  specced — and under `-5`'s live-tree definition `-7`'s flat "It does NOT detect a dirty working
  tree" is false, since porcelain and dirty blobs are digest components.

### T3 - HIGH - TOOL-aPacedTurnstile-5 §2 S5 · §4 The fingerprint

- **Claim:** the same defect seen from the owning side. The R1 fix moved predicate 0's join to a
  fresh fingerprint computed at the recorded sha, but `-5` — which owns the helper — still defines
  exactly one digest, over the committed tree object, the sorted porcelain status lines, and the
  blob hashes of every dirty-or-untracked file that still exists, with no sha parameter and no
  definition of the working-tree half at a sha other than HEAD. `-5` §4 Files touched spells the
  helper as "called by the runner and by `.githooks/pre-push`" with no argument. Under the only
  definition the set carries, a fresh call from the hook at push time reads the CURRENT worktree's
  porcelain and dirty blobs, so `-7`'s new sentence is false and §4's exhaustive gloss — "a
  hand-edited record or an object store rewritten under that sha" — omits the population it will
  actually fire on.
- **Impact:** the one interface both specs insist must have exactly one implementation cannot
  express the operation the blocker's fix requires, so the builder must invent the sha semantics —
  and the natural invention reproduces R1's shape in miniature: predicate 0 fires on every push
  made from a tree with any dirty or untracked file, forcing full and taking the scoped path away
  on exactly the pushes predicates 3 and 4 exist to admit. It fails toward FULL, so no arm reds;
  AC6b's control is satisfiable only on a clean push tree, which no fixture is told to build. R19
  named the missing identifier; the fold gave the name and left the signature.
- **Fix:** in `-5` S5, give the helper a required sha argument and state the working-tree half's
  scope in one sentence — the porcelain and dirty-blob components apply only when the argument is
  the current HEAD; at any other sha the digest is that sha's tree object alone. Cite that sentence
  from `-7` S2b and §4 Data model, and add to AC6b's control the precondition that the push tree is
  clean, so the criterion cannot be graded on a fixture that hides the case.
- **Confirmed because:** `-5` S5 and §4 The fingerprint define exactly one digest over the three
  named components with no sha parameter, and §4 Files touched spells the helper with no argument —
  yet `-7` §2 S2b, §4 Data model and AC6b all require a fresh fingerprint computed at the recorded
  sha and assert the predicate does not detect a dirty working tree, which is false under the only
  definition the set carries.

### T4 - HIGH - TOOL-aPacedTurnstile-1 §2 S8, registry surgery · §4 Files touched · §6 AC3

- **Claim:** S8's registry surgery is enumerated exhaustively and is all deletions plus one
  addition: add the entry, delete three exempt path rows and the two exempt-leg rows naming
  run-gates, correct one `why`, add the id to `[selection].default`. The new gov-only leg S1
  creates is deliberately NOT a descriptor `[[gate_leg]]` row — S6 keeps the count at FOUR and
  withholds the file from the payload — so it is a manifest leg claimed by no descriptor.
  `tools/govkit/govkit.py` reds on exactly that: a gate leg claimed by no descriptor and carried by
  no `[[exempt_leg]]` must red until a declaration says whether an adopter receives it.
- **Impact:** `python tools/govkit/govkit.py selfcheck` reds at `-1`'s own landing, on a gate named
  in `-1` §7 and asserted green by `-1` AC3 — and §4 Rollout mandates ONE commit, so there is no
  green state. It is the mirror image of the round-1 blocker the same S6 sentence was written to
  prevent. The settled precedent sits right beside it: the memory-recall gov-only split carries an
  `[[exempt_leg]]` row for each of its two legs, with the same pin-copied-from-another-corpus
  reason S1 cites.
- **Fix:** add to S8 the `[[exempt_leg]]` row for the gov-only harness with its reason, mirroring
  the two memory-recall rows; carry it in §4 Files touched's registry row, which currently reads
  "five rows deleted", and in AC3.
- **Confirmed because:** `-1` S8 enumerates add-entry, delete three exempt path rows and the two
  exempt-leg rows naming run-gates, correct one `why`, add the id to `[selection].default` — no
  `[[exempt_leg]]` row for the gov-only harness — while `govkit.py` fails for exactly that case and
  S6 keeps the descriptor at four rows. AC3 demands selfcheck exit 0 at a landing §4 Rollout
  mandates as one commit, and the registry's existing recall-floor pair is the shape S8 omits.

### T5 - MEDIUM - TOOL-aPacedTurnstile-7 §8, second fork, the RESOLVED line

- **Claim:** the fold deleted the non-integer-lag row and renumbered the reconcile-merge row to 6,
  and moved its derivation off the lander onto the tip's shape — in S2b, §4's table and AC6c. §8's
  ratified answer was not swept: it is still headed "Whether `tools/push-main.sh` should force full
  on a retry", still answers YES about the lander's behaviour, and still ends with a pointer to
  predicate 7. There is no predicate 7; the table now runs 0-6, and AC6c explicitly moves the
  grading out of the lander's suite because the hook needs no channel from it.
- **Impact:** a ratified §8 answer is binding text by the build method — round 2's own Refuted list
  rests on that premise — and this is the third occurrence in this build of a §8 resolution
  surviving the fold that invalidated it (R6 in `-5` and R29 in `-3`, both corrected in this same
  commit). A builder reading §8 looks for a predicate the table does not carry, and reads an
  obligation on `tools/push-main.sh` that S2b's fold explicitly removed — the lander now keeps only
  the end-to-end arm.
- **Fix:** rewrite the resolution to the answer the fold actually took: the lander forces nothing
  and exports nothing; the hook derives the reconcile-merge shape from the commit it is handed, as
  predicate 6, and `tools/push-main.test.sh` keeps only the end-to-end observation. Re-title the
  fork accordingly and log the line in §9.
- **Confirmed because:** §8's second fork is untouched by the fold — still headed as a question
  about `tools/push-main.sh`, still answering YES about the lander, still closing on predicate 7 —
  while the §4 table now runs 0-6 with the reconcile-merge row at 6, S2b states the lander exports
  nothing and the hook derives the shape from the tip, and AC6c moves the grading out of
  `tools/push-main.test.sh`.

### T6 - MEDIUM - TOOL-aPacedTurnstile-7 §6 AC6d, against §2 S8 and §10 Reuse audit

- **Claim:** AC6d closes R21 by asserting the forced-full reason lands in the record header,
  "asserted in `.githooks/pre-push.test.sh` against the header the runner wrote, not against the
  hook's stdout". That suite has never run the runner: its own header line says the gate is stubbed
  via `GOV_GATE_CMD` so the bar never actually runs, every arm in it passes a stubbed gate command,
  and §10 leans on exactly that — "the hook's test already stubs the gate, so the forcing arms need
  no new harness". No runner runs there, so no runner-written header exists to assert against.
- **Impact:** the cheap implementation is a stub that echoes its own environment into a file the
  arm then reads, which certifies test code rather than the runner and leaves R21's actual gap
  open: `-5` S2 declares the forced-reason key, `-5` AC1 reads the header for the run id alone, and
  `-5` S10's canary pins the MANIFEST key set, so nothing in the set observes the runner writing
  that key. The durable half of S5 still ships unbuilt, which is the finding AC6d was added to
  close.
- **Fix:** either move the header assertion to `tools/run-gates/run-gates.evidence.test.sh`, where
  the runner is really driven through `GATE_LEGS` so it never re-enters the real bar and where `-5`
  owns the header, leaving the hook's suite to assert only that the reason is exported; or keep it
  in the hook's suite and say in S8 and §10 that this one arm drives the REAL runner under
  `GATE_LEGS` — the harness claim in §10 is false for it as written.
- **Confirmed because:** AC6d demands the reason be asserted in `.githooks/pre-push.test.sh`
  against the header the runner wrote, but that suite's own header line says the gate is stubbed so
  the bar never actually runs, all ten arms pass a stub gate command and the file never references
  `run-gates` or `GATE_LEGS`, and `-7` §10 rests on exactly that stubbing — so no runner-written
  header exists there, and no `-5` criterion observes that key either.

### T7 - MEDIUM - TOOL-aPacedTurnstile-3 §2 S2 and §4 Inventory — the 73-row count

- **Claim:** R17's fix froze a new number that R10's fix had already moved. S2 now says the reorder
  commit sees 73 rows — 70 at base plus `-1`'s adopter e2e, `-1`'s wiring check and `-4`'s
  turnstile suite, "The three take `e2e`, `wiring` and `selftests` respectively". But R10's fold
  makes `-1` S1 create a FOURTH build-added leg, `tools/run-gates/run-gates.gov.test.sh`, which S1
  states "is its own gate leg", which `-1` §7, `-6` §7 and `-7` §7 all list as a bar command, and
  whose assertion counter `-1` S11 provisions at birth. It is added by `-1`, sequenced first, so it
  is in the manifest at the reorder commit and no later pass picks it up — the exact argument S2
  makes about the other three.
- **Impact:** the manifest holds 74 rows at the reorder commit, not 73, and the gov-only leg has no
  chunk assigned by any spec. AC6's UNCONDITIONAL every-leg-carries-a-chunk assertion — the arm
  R29's corrected §8 resolution now names as the sole protection — reds at the build's last commit
  on exactly the leg S2's enumeration omits. That is the defect R17 was folded to prevent,
  reintroduced by R10's fix inside the same commit.
- **Fix:** restate S2's count as 74 and name the chunk `run-gates.gov.test.sh` takes (`selftests`
  is its natural home), or drop the arithmetic entirely in favour of "every leg in the manifest at
  this commit" and list only which chunk each build-added leg takes, sourced from the siblings'
  files-touched tables rather than from a figure. Update §4 Inventory's own restatement of 73 in
  the same edit.
- **Confirmed because:** `-3` S2 reads 73 rows and enumerates exactly three build-added legs, and
  §4 Inventory repeats the figure — but `-1` S1, folded in the same commit, creates
  `tools/run-gates/run-gates.gov.test.sh` and calls it its own gate leg, added first in the order,
  so the manifest holds 74 and that leg is assigned no chunk by any spec while `-3` AC6 asserts
  unconditionally that every leg in `tools/gate-legs.json` carries one. Below HIGH because S2's
  leading clause is count-free and normative, so only a builder assigning from the enumeration is
  misled.

### T8 - MEDIUM - TOOL-aPacedTurnstile-1 §4 Files touched, the `tools/gate-legs.json` row

- **Claim:** S1 now creates `tools/run-gates/run-gates.gov.test.sh` and says it "is its own gate
  leg", but the files-touched row for the manifest was left at its pre-fold wording: "two argv
  repoints, TWO new legs — the adopter e2e and the wiring check". One file states three new legs
  and two.
- **Impact:** the files-touched table is what a builder derives the commit's edits from, so the
  gov-only leg's manifest row is the half of R10's split most likely to be skipped — and it is the
  half every other unit depends on, since `-3` AC6, `-6` AC12 and `-7` AC9 all name that harness as
  their arms' home and `-1` §7 lists it as a gate. It is also the row `-3` S2's chunk arithmetic
  reads.
- **Fix:** change the row to "two argv repoints, THREE new legs — the adopter e2e, the wiring check
  and the gov-only harness (S1)", and check the same count against `-3` S2.
- **Confirmed because:** `-1` §2 S1 creates the gov-only harness and says it is its own gate leg,
  and S11 gives it a counter and a floor of its own at birth so it never needs a waiver row, while
  §4 Files touched still spells the manifest row as two new legs. The same file states three and
  two, and `-3` S2's arithmetic reads the stale figure.

### T9 - MEDIUM - TOOL-aPacedTurnstile-3 §7 Gates, §4 Files touched, and §2 S8

- **Claim:** R10's fix moved AC6 into `tools/run-gates/run-gates.gov.test.sh`, and three of the
  four carriers swept their supporting text with it — `-1` §7, `-6` §7 plus §4 Files touched, and
  `-7` §7 all gained the gov harness. `-3` did not. Its §7 gate list still reads canary plus
  evidence plus five others and never names the gov harness; §4 Files touched still has only a
  `run-gates.test.sh` row for S8's arms; and S8 itself still reads "canary arms for chunk
  contiguity", assigning to the shipped canary the one arm AC6 just moved out of it. §4 Data model
  repeats it: "asserted by a canary arm".
- **Impact:** this unit's stated DoD cannot see its own headline criterion — AC6 is graded by a
  command §7 does not run, the same shape R9 found in `-1` §7. Meanwhile S8 and AC6 disagree on
  which file the contiguity arm lands in, so a builder working from §2 writes it back into the
  shipped canary and re-creates the red-on-arrival R10 named.
- **Fix:** add `bash tools/run-gates/run-gates.gov.test.sh` to §7, add a files-touched row for it
  naming AC6's arms, and reword S8 and §4 Data model's "canary arm" to put the every-leg and
  contiguity assertions in the gov-only harness while leaving the fixture-driven arms in the
  shipped canary, matching AC6/AC6b.
- **Confirmed because:** `-3` §7 lists the canary, the evidence suite, the testsuite counter, the
  codebase-map test, hygiene, govkit selfcheck and playbook parity and never names the gov harness,
  which AC6 makes the sole home of this unit's headline assertion; §4 Files touched carries only
  the `run-gates.test.sh` row; and S8 plus §4 Data model still put contiguity in the canary. `-1`,
  `-6` and `-7` all gained the gov harness in this fold; `-3` alone was not swept.

### T10 - MEDIUM - TOOL-aPacedTurnstile-7 §6 AC9b, against §2 S10 and §4 Files touched

- **Claim:** AC9b asserts that when `python tools/govkit/govkit.py selfcheck` runs,
  `tools/memory-tree/kit.toml`'s declared guard for the parity leg names `memory/guides/`, "and a
  fixture reverting it to the narrow spelling reds". No such comparison exists: selfcheck's
  descriptor/manifest join reads the leg NAME only, and its guard pass classifies pathspecs from
  gov's own `tools/gate-legs.json`. S10's own new paragraph says so verbatim — govkit's selfcheck
  joins descriptor gate legs to the manifest by NAME only and never compares the two guards. No
  scope item builds the arm, §4 Files touched carries no `tools/govkit/govkit.py` or
  `tools/govkit/selftest.py` row, and neither deferred unit covers it (`-9` defers guard
  COMPLETENESS in general; `-11` is the requires-edge and default-selection arm).
- **Impact:** R7's fold closed the descriptor half in text and left its observation unbuildable, so
  AC9b's second clause cannot pass and the SHIPPING carrier of the hole is graded by nothing. This
  is the R11-R13 shape — an obligation named in prose with no scope item and no arm that can fail —
  reintroduced by the fix for a different finding, in the section the README's largest-risk claim
  rests on.
- **Fix:** either add the selfcheck arm as a scope item in S10 with `tools/govkit/govkit.py` (or
  its selftest) in §4 Files touched — a join of each descriptor's declared `[[gate_leg]]` guard
  against gov's manifest row for the same leg name — or restate AC9b as what an existing gate can
  observe (kit.toml's guard for that leg names `memory/guides/`, asserted in the memory-tree kit's
  own suite) and file the join as the follow-up R7 recommended.
- **Confirmed because:** AC9b demands selfcheck red on a fixture reverting kit.toml's parity-leg
  guard, but S10's own closing sentence says selfcheck joins descriptor gate legs to the manifest
  by name only and never compares the two guards — confirmed in the code, whose descriptor join
  reads the leg name and whose guard pass classifies only gov's own manifest pathspecs. No scope
  item adds the join, §4 Files touched carries kit.toml but no govkit row, and neither deferred
  unit covers it, while the README rests the build's largest risk on AC9b arming the shipping
  carrier.

### T11 - MEDIUM - TOOL-aPacedTurnstile-1 §2 S1 · §4 Files touched, against `-3`'s inventory

- **Claim:** R10's fix makes the gov harness its own gate leg, which is a THIRD leg `-1` adds to
  `tools/gate-legs.json`. `-1` §4 Files touched still reads two argv repoints and TWO new legs, and
  `-3` S2 and its inventory, rewritten in the same commit for R17, count `-1`'s two plus `-4`'s one
  and state 73 rows at the reorder commit, naming the chunk for exactly three legs. The manifest
  holds 70 today, so the reorder commit holds 74.
- **Impact:** R17 reintroduced by the R10 fix, landing on the arm R10 moved: the gov harness's own
  leg is the one leg with no chunk assigned, and AC6 — the unconditional every-leg-carries-a-chunk
  assertion that now lives INSIDE that harness — reds on it at the build's final commit. `-3`'s
  reorder is sequenced last, so no later pass picks it up, and the cheapest field repair is again
  to weaken AC6.
- **Fix:** correct `-1` §4's manifest row to THREE new legs and name the gov harness among them. In
  `-3` S2, the inventory paragraph and §4 Files touched, state 74 and name the chunk the gov
  harness takes — `selftests`, beside the other harness arms.
- **Confirmed because:** `-1` §4 Files touched still spells the manifest row as two new legs while
  S1 adds a third; `-3` S2, its Inventory paragraph and its §4 Files touched row all say 73 rows at
  the reorder commit and name exactly three build-added legs. With the gov harness the figure is 74
  and a fourth leg is unnamed. S2's binding quantifier still covers it, so the AC6 red is possible
  rather than certain.

### T12 - MEDIUM - TOOL-aPacedTurnstile-7 §2 S2b predicate 6 · §4 The decision, row 6 · §6 AC6c

- **Claim:** R15's prescribed re-derivation replaced "any `push-main` retry after the first" with
  "the pushed tip is a merge whose second parent is not an ancestor of the recorded green", but
  every description of the row kept the old population: S2b calls it the shape a `push-main`
  reconcile retry produces, the reason string still says a reconcile merge is not covered by the
  record, and AC6c grades only that shape. The predicate as written matches ANY merge tip whose
  second parent is not an ancestor of the recorded green — which on this repo is the ordinary
  landing shape, since every build landing on the default branch is a merge commit, whenever the
  recorded green was not earned on that exact branch head.
- **Impact:** a first-attempt merge landing forces a full run and prints a reason that
  mis-describes why, so the operator reads it as a retry that never happened; and the saving §1
  exists for is silently lost on the landing shape this repo actually uses. Nothing grades the
  negative — no criterion asserts an ordinary merge landing whose second parent IS covered stays
  scoped — so the over-firing looks like caution, which is the failure mode `-5` S5 and R1 both
  name.
- **Fix:** state the row's real population in S2b and widen the reason string to name a merge tip
  the record does not cover; add the negative half to AC6c — a merge tip whose second parent IS an
  ancestor of the recorded green runs WITHOUT the full-run flag — so the row cannot fire
  unconditionally.
- **Confirmed because:** §4 row 6 is the broad shape predicate while S2b glosses it as the
  reconcile retry shape and the reason string still names a reconcile merge; `git log --merges` on
  the default branch shows every landing here IS such a merge, so the row fires on ordinary
  landings whenever the recorded green is not exactly the second parent. AC6c grades only the
  positive half, unlike AC6b, which in this same fold gained an explicit control precisely because
  a one-sided criterion is satisfied by a predicate that fires unconditionally — the identical hole
  is left open on predicate 6.

### T13 - LOW - TOOL-aPacedTurnstile-7 §5 Production-readiness checklist, the user-docs bullet

- **Claim:** R8's fix made S9's carrier population MEASURED and named seven carriers, and AC7 was
  rewritten to grade all seven. §5's user-docs bullet still reads "S9, across all three carriers of
  the retired claim" — the pre-fold count, in the section a builder grades the docs line against.
- **Impact:** exactly the carrier class this fold is folding — R24 was raised in `-5` because §5 is
  the checklist a builder reads and it contradicted the scope item. Here §5 re-authorises the
  enumeration of three that R8 found leaves four carriers stating a guarantee this unit deletes,
  two of them product files every adopter receives and one of them the domain-rules checklist gov's
  own reviewers grade against.
- **Fix:** change the bullet to name the measured population — seven at this base, including two
  product files and the build-method template pair — or simply drop the count and point at S9.
- **Confirmed because:** §5's user-docs bullet still reads "all three carriers of the retired
  claim" and the fold's diff shows §5 untouched, while S9 now measures the population and AC7
  enumerates seven carriers at this base. Bounded harm, because AC7 rather than §5 is the binding
  criterion and it names all seven, so this is a stale count in the checklist rather than a defect
  a passing implementation could carry.

### T14 - LOW - TOOL-aPacedTurnstile-5 §6 AC15, against §2 S1 and §8 first fork

- **Claim:** R6's fix asked for two things — the corrected resolution, and, if the sweep's bound is
  a real decision, a statement of it with a criterion. The criterion landed; the bound did not.
  AC15 grades run directories older than "the declared retention bound" against a fixture carrying
  more than the bound, but no scope item, section or fork declares a value. S1 says only "bounded
  by a sweep"; §8's corrected resolution says only "bounded by a sweep that runs after the verdict
  is written". AC15's own body then implies a bound of 2 by asserting the current one and its
  predecessor remain, which is a third, undeclared number.
- **Impact:** the criterion is not falsifiable as written — a builder picking any bound satisfies
  it, and one picking a bound above the fixture's size satisfies it by finding nothing, the class
  this build names elsewhere. The sibling pattern is explicit that a bound must be declared with
  its reasoning: `-4` S8 requires a bounded wait to be a DECLARED value with its reasoning beside
  it, not an unnamed number. `-5`'s is an unnamed number.
- **Fix:** declare the retention bound in S1 as a named constant with its reasoning beside it, in
  `-4` S8's shape, and make AC15 read against that constant rather than against "the declared
  retention bound" plus a separate predecessor clause — the two must be the same number or the
  criterion grades two different designs.
- **Confirmed because:** `-5` S1 says only that retention of older run dirs is bounded by a sweep
  that runs after the verdict file is written, and §8's corrected first fork repeats that wording;
  no numeric bound appears anywhere in the build, yet AC15 grades against the declared bound and
  separately pins the current one and its predecessor. Low-stakes residue of a conditional fix —
  the criterion is not vacuous, since the predecessor clause fixes a floor of 2 — but it names a
  declaration that does not exist.

### T15 - LOW - TOOL-aPacedTurnstile-7 §8 second fork, the RESOLVED line, and §9 rev-6

- **Claim:** R20's fix deleted the non-integer-lag row and renumbered the reconcile-merge row from
  7 to 6, and §4's table now carries "Seven rows, not eight" with no predicate 7. The ratified §8
  answer still closes by pointing at predicate 7, and the rev-6 log line repeats the number in the
  present tense.
- **Impact:** the R6/R29 class — a ratified §8 answer naming a mechanism the rest of the file no
  longer carries — recreated by this fold in the same document that corrected it in two siblings.
  §8 answers are binding text by the build method, so a builder resolving the retry question
  follows the pointer to a row that does not exist, and the revision log tells a reader the file
  says something it does not.
- **Fix:** repoint the §8 resolution to predicate 6 and restate the rev-6 log line in the numbering
  the file now uses — the reconcile-retry row is derived from the tip's SHAPE and becomes predicate
  6; the non-integer-lag row is deleted.
- **Confirmed because:** §4's table now runs 0-6 and says seven rows not eight, and S2b spells the
  reconcile-merge row as predicate 6, but §8's second RESOLVED line and §9's rev-6 entry both still
  name predicate 7. A genuine stale cross-reference in binding ratified text, LOW because the
  resolution paragraph describes the reconcile-merge mechanism in full beside the pointer, so the
  row it means is unambiguous.

### T16 - LOW - TOOL-aPacedTurnstile-7 §5 user-docs line (fold-completeness lens)

- **Claim:** R8's fix rewrote S9's carrier population from three to a MEASURED seven and swept §4
  Files touched and AC7 with it. §5's checklist line was not swept and still enumerates three.
- **Impact:** the same half-closure and the same section as R24, whose whole argument was that §5
  is the checklist a builder grades a line against, so a §5 line contradicting a scope item sits in
  the half that gets read. A builder grading user docs against three carriers edits `AGENTS.md`,
  the playbook template and the runner header and stops — leaving the two domain-rules bullets, the
  build-method pair and the kickoff guide, precisely the four-carrier miss R8 raised. AC7 would
  catch it, but only if the builder reaches §6 rather than closing on §5.
- **Fix:** change the line to name S9's measured carrier set — seven at this base — each with AC7's
  negative-plus-positive pair.
- **Confirmed because:** §5's checklist line still reads "across all three carriers of the retired
  claim" while S9, rewritten by R8's fold, measures seven and §4 Files touched plus AC7 both
  enumerate all seven. An unswept carrier of R8's fix, LOW rather than MEDIUM because the line
  points at S9 and AC7 — the graded criterion — carries the measured population per carrier.

### T17 - LOW - TOOL-aPacedTurnstile-3 §2 S9, the exclusive-ownership sentence

- **Claim:** S9 still ends "This unit owns that file for this build" of
  `memory/guides/SESSION-KICKOFF.md`. R9's fold added four path spellings in that file to `-1` S10
  and to `-1` §4 Files touched; R8's fold added the safety-property statement in the same file to
  `-7` S9 and to `-7` §4 Files touched. Three units now edit a file one of them claims exclusively.
  `-2` §3's non-goal is the correct narrow form and now disagrees with `-3` itself: it defers only
  that file's gate-command block.
- **Impact:** the exclusive-ownership sentence is the set's only statement about who may touch that
  file, and it is now false. A builder on `-1` or `-7` reading it either skips their edit — `-1`'s
  is the `watch:` pathspec whose omission fails the kickoff ratchet, which R9 established makes
  `-1`'s mandated single commit land red — or overrides a binding spec sentence with no record of
  why.
- **Fix:** narrow S9's ownership claim to the gate-command BLOCK, in `-2` §3's wording, and name
  the other two edits (`-1`'s path repoints, `-7`'s safety-property sentence) as belonging to those
  units.
- **Confirmed because:** `-3` S9 still claims the file for this build, while `-1` S10 and its §4
  row mandate four path spellings there including the manifest-audit `watch:` line, and `-7` S9
  plus its §4 row mandate the safety-property sentence — three units editing a file one claims
  exclusively, and `-2` §3's narrower form now disagrees with `-3`. LOW because S9's own first
  clause scopes its edit to the gate-command block and `-1`'s builder is told twice, with the
  red-commit consequence spelled out, to make its edit.

### T18 - LOW - TOOL-aPacedTurnstile-7 §2 S5, the parenthetical justification

- **Claim:** S5 justifies passing the forced-full reason through the environment partly because the
  first draft's alternative would have been cleared by the record's start-of-run reset in any case.
  R6's fold removed that reset: `-5` §8's corrected resolution is now per-run directories with
  nothing cleared at start, and `-5` S1 says nothing clears the record at the START of a run.
- **Impact:** a live cross-reference to a mechanism the sibling deleted in the same commit. Minor
  on its own, but it is the reasoning AC6d rests on, so a reader checking why the reason must ride
  the environment is sent to a design that no longer exists — and the sentence reads as though `-5`
  still resets, which is the belief R6 exists to remove.
- **Fix:** drop the clause or replace it with the reason that survives: the record's format and
  writer belong to `-5`, so the hook declares the value and `-5` S2's key list carries it.
- **Confirmed because:** `-7` S5 still cites the record's start-of-run reset while `-5` S1 now
  states nothing clears the record at the start of a run and §8's corrected resolution reads
  "per-run directories, nothing cleared at start" — the fold's own R6 fix in `-5` falsified a
  sentence in `-7` the fold left untouched. Consequence-free rationale for a rejected alternative,
  so it costs a reader's confidence rather than a build decision.

### T19 - LOW - TOOL-aPacedTurnstile-1 §2 S6, the "FOUR, not five" justification

- **Claim:** S6 was not touched by the fold and still justifies its four `[[gate_leg]]` rows with
  "only the two repointed legs plus S7's adopter e2e and its `--check` exist when this unit lands".
  After R10's split, a fifth leg — the gov-only harness — also exists at this unit's landing; it is
  correctly absent from kit.toml because it is withheld from the payload, but the stated reason is
  now an incomplete census rather than the real rule.
- **Impact:** the count stays right by accident. A reader reconciling S1's new leg against S6 finds
  the enumeration does not account for it and cannot tell whether the omission is deliberate
  withholding or an oversight — and the same census is what `-1` §4 Files touched and `-3` S2 both
  got wrong.
- **Fix:** restate the reason as the rule rather than the census: four rows because those are the
  legs the kit SHIPS; the gov-only harness is a bar leg here and is withheld from the payload by
  the file rules this item writes.
- **Confirmed because:** `-1` S6 is unchanged by the fold and still justifies four rows by a census
  of the legs that exist at landing, while S1, added by the fold, creates the gov-only harness and
  calls it its own gate leg — so a fifth leg does exist at landing and the census is incomplete
  even though the row count stays correct.

### T20 - LOW - TOOL-aPacedTurnstile-7 §8, second fork, the RESOLVED line (fold-broke lens)

- **Claim:** the fold deleted the non-integer-lag row, renumbered the reconcile predicate from 7 to
  6, and moved the mechanism out of the lander into the hook — AC6c grades it in the HOOK's suite,
  not the lander's, because the hook derives the fact from the commit it is handed. §8's ratified
  resolution is untouched: it still poses the question as whether `tools/push-main.sh` should force
  full on a retry, answers YES for the lander, and closes on a predicate this document no longer
  has.
- **Impact:** a ratified §8 answer is binding text by the build method, and this build has already
  been bitten twice by exactly this class, both folded in this same commit. A builder reading §8
  puts the forcing in `tools/push-main.sh`, which §4 Files touched does not list and which the hook
  cannot see — and a reader auditing the table for the named predicate finds nothing.
- **Fix:** restate the resolution in the hook's terms and against the current numbering: the hook
  derives the reconcile shape from the tip it is handed, predicate 6 closes it, and the lander's
  suite keeps only the end-to-end observation AC6c assigns it.
- **Confirmed because:** §8's second fork still reads as a lander question answered YES and closing
  on predicate 7, and the fold's diff contains no hunk for that section, while §4's table now ends
  at row 6 and S2b plus AC6c put the mechanism in the hook. LOW because S2b's "derived from the
  tip's SHAPE and not from the lander" paragraph contradicts it loudly enough three sections up.

### T21 - LOW - TOOL-aPacedTurnstile-5 §6 AC15 (fold-broke lens)

- **Claim:** AC15 grades run directories older than the declared retention bound, but nothing in
  the set declares one. S1 says only "bounded by a sweep that runs AFTER the verdict file is
  written"; §8's corrected resolution repeats the phrase with no value. R6's fix said in terms that
  if the sweep's bound is a real decision it should be stated and given a criterion — the criterion
  landed, the declaration did not.
- **Impact:** the criterion is satisfied by any bound the builder picks, including one so large the
  record grows without practical limit, which is the failure AC15 was added to prevent; and the
  only concrete floor it carries — the current one and its predecessor remain — is an implicit
  bound of 2 stated in a criterion rather than in scope. The tree's settled pattern is the
  opposite: `-4` S8 makes its wait bound a DECLARED value with its reasoning beside it, not an
  unnamed number.
- **Fix:** declare the bound in S1 with its reasoning beside it in one line, have §8's resolution
  ratify that value, and let AC15 grade against it by name rather than against the declared bound
  in the abstract.
- **Confirmed because:** S1 and §8's corrected first fork both bound retention by a sweep with no
  number anywhere in the file, so AC15's "declared retention bound" names a declaration that does
  not exist. LOW rather than MEDIUM because any declared constant still bounds growth and AC15's
  fixture grades whatever the builder declares — the gap is an unmade decision, not an
  unsatisfiable arm.

### T22 - LOW - TOOL-aPacedTurnstile-3 §7 Gates, against §6 AC6

- **Claim:** the fold moved AC6 — this unit's central unconditional assertion — into
  `tools/run-gates/run-gates.gov.test.sh`, but §7's gate list was not updated and still names only
  the shipped canary and the evidence suite among the run-gates harnesses. `-1`, `-6` and `-7` all
  added the gov harness to their §7 in the same commit; `-3`, whose criterion moved, did not.
- **Impact:** the unit's stated DoD cannot see the harness carrying its own headline criterion, the
  same shape as R9, whose §7 could not see the reds its own rollout produced. AC6 lands in the
  build's LAST commit, so a DoD run of `-3`'s listed gates would report green with the
  every-leg-carries-a- chunk assertion never executed.
- **Fix:** add `bash tools/run-gates/run-gates.gov.test.sh` to `-3` §7.
- **Confirmed because:** `-3` AC6 now names the gov harness as the command that runs it, but §7
  lists the canary, the evidence suite, the testsuite counter, the codebase-map test, hygiene,
  govkit selfcheck and playbook parity, with no gov harness and no full bar, while `-1`, `-6` and
  `-7` all carry it in their §7. The push boundary still runs that leg, so the cost is a late
  signal rather than a wrong verdict.

### T23 - LOW - TOOL-aPacedTurnstile-7 §5 user-docs line (fold-broke lens)

- **Claim:** R8's fix replaced S9's enumeration of three carriers with a MEASURED population of
  seven and updated S9, §4 Files touched and AC7 accordingly. §5's user-docs line still enumerates
  three.
- **Impact:** §5 is the section a builder grades the readiness line against — the same reason R24
  was raised against this build's other §5 line and folded in this same commit. A builder checking
  documentation coverage against §5 stops at three and leaves the four the fold added, two of which
  (`parallel-coding-governance.domain-rules.md` and `tools/memory-tree/BUILD-METHOD.template.md`)
  are product an adopter receives.
- **Fix:** change the line to name the measured population rather than a count — S9, across every
  carrier the measured search selects — so it cannot go stale against S9 again.
- **Confirmed because:** §5's user-docs line is untouched by the fold and still reads "all three
  carriers of the retired claim" while S9, §4 Files touched and AC7 were all rewritten in that
  commit to a measured population of seven, two of them product. Round 2's R8 named S9, §4 and AC7
  and not §5, so this is a genuine leftover carrier of the fixed defect.

## Refuted

- `-7` §6 AC6b's control half not saying how the fixture's STORED fingerprint is produced — killed
  as premature: the criterion states two independently-sourced sides (a record on disk versus a
  value the hook derives) and the assertion-between-two-derived-values hazard is real but is a
  property of the fixture an implementation has not written yet; T1's fix, which declares the two
  helper modes and their clean-tree equality, is what makes the fixture's stamp specifiable at all,
  so raising it separately would grade a design decision this set has not yet been given the
  vocabulary to make.
- `-7` §4 Files touched's `.githooks/pre-push.test.sh` row and §5's testing bullet still
  summarising S8's pre-fold arm list — killed: both are summaries pointing at S8, which carries the
  three new obligations in full (the edit-time integer-lag arm, the executed assertion counter,
  AC6d's header arm), and neither is a graded criterion; the same class is already recorded where
  it has teeth, at T13/T16/T23, where §5 restates a COUNT a builder can grade against rather than a
  pointer.
