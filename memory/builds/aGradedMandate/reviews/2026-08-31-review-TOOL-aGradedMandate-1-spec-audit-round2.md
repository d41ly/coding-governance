**Serves:** spec-audit TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9

# aGradedMandate — spec audit of the folded unattended-kit units, ROUND 2

*Adversarial Tier-2 pass over the spec set as it stands after the round-1 fold, node `a`,
2026-08-31. This round judges the FIX: whether each rev-2 edit closed the finding it cites, and
whether the fold prose it added is true. Round-1 findings are not re-raised. Every claim below was
re-derived in this worktree against the driver (`tools/unattended/unattended.sh`), the gate leg
(`tools/unattended/check-unattended.sh`), the hygiene engine
(`tools/memory-tree/check-memory-hygiene.sh`), the rendered Skill and both protocol copies, at the
line numbers cited. One probe was EXECUTED — the `TOOL-aGradedMandate-1` S1 predicate over all 28
tracked `RUN.md` files — and its census is reproduced under R2. Severities are this report's
adjudication, not the finders' self-grading. Round 1:
`reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md`. Binding contract:
`memory/guides/UNATTENDED-PROTOCOL.md`. Method: `memory/guides/BUILD-METHOD.md`.*

**Range:** eight spec records, each pinned at the blob reviewed —
`spec/2026-08-31-spec-TOOL-aGradedMandate-1.md@052c0fb387314b75e4303d9a31e50e7ce4673113` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-2.md@9d77ea37bc33616eea6e91540cdc76162d5c78ce` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-4.md@226d853261aa5d3e8211610edcd46d7792747a08` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-5.md@42b4308f3f7a48f6ee1bea1bcff057a6ddd6e746` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-6.md@e2e976f310cb2256170e364b308e1fd38b39cc2c` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-7.md@78190f83db44160ad2cb01630a8e3f1b2feb8f53` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-8.md@02fb3c9c8fdadc7c0fdd954872578634621bf16d` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-9.md@13414c0617c2ab0e994bef66d973f74b07b7fa21`.
`TOOL-aGradedMandate-3` is RETIRED at rev-2 on round 1's BLOCKER F1 and is deliberately NOT a
subject; the fork it carried is parked in `memory/builds/aGradedMandate/RUN.md`.

**ROUND:** 2.

## Verdict: BLOCKED

Two blockers, five highs, three mediums, one low — eleven distinct defects. Both blockers are
fold-introduced, and both live in prose the fold wrote to close a round-1 finding.

`TOOL-aGradedMandate-5`'s replacement design splits the owed set on the ACT axis but leaves the
history side computing its complement on the KIND axis, so a single `rescope · item retire` row is
counted as owed AND as history and `--status` prints it twice. Section 4's sentence "the complement
rule is preserved on both axes" is not an omission — it is the instruction that produces the double
count, and AC3 is worded so that a row counted twice satisfies it.

`TOOL-aGradedMandate-1`'s new AC7 pins the probe's expected hits at three records and calls a fourth
"a finding, not a pass". Run over the tree, the predicate refuses 21 of 28 tracked `RUN.md`. The one
criterion the fold added to stop F9 recurring fires eighteen spurious findings on its first
execution, and the cheapest exit from it is to loosen it.

The dominant class round 1 named — *build to the Inventory, red a gate the spec's own §7 names* — is
GONE. That is the fold's real result and it should be said plainly: no finding in this round reds
`unattended kit gate`, `unattended skill wiring`, memory hygiene or the driver suite on the tree the
units ship with. The Inventory rows the fold added are, on the two units where a gate was at stake,
complete. What replaced that class is quieter and worse to catch: **criteria that cannot fail, and
design prose that contradicts its own Inventory.** Five of the eleven defects are one of those two
shapes.

**Review shape.** Raw 36, confirmed 27, refuted 9, unverified 0, precision 0.75. The 27 confirmed
findings collapse to 11 distinct defects. Convergence was heavy and is corroboration rather than
volume: four independent finders reported the `park_kinds_unowed` double count (R1), three the
unsatisfiable AC7 census (R2), four the un-refolded §10 (R4), four the rev-1 status headers (R11),
three the ungraded `PARK_ACTS_OWED` (R3), three the protocol's surviving "declared once" sentence
(R8). Each merged entry carries the strongest reachability argument its contributors offered, plus
this report's own re-derivation. Precision rose from 0.45 to 0.75 against a set half the size, which
is what a narrowed surface is supposed to do.

## What the fold closed

Stated because judging the fix is this round's job, and because a reader who sees only the table
below will mis-read a shorter list as a worse one.

- **F1 (BLOCKER)** — closed by retirement. `TOOL-aGradedMandate-3` is `WONTDO` at rev-2 with the
  fork and its five options parked in `RUN.md`. F3, F10, F11 and F13 die with it.
- **F2 (BLOCKER)** — closed. S1a refuses the `kind:act` member grammar outright and states the
  mechanism, so `check-unattended.sh:366-371` and `:1943-1951` are untouched and stay green. The
  design that replaced it carries R1 and R3, which is a different defect, not the same one.
- **F4** — closed. S2a spells the id join whole-token WITH range expansion, names the 18 live range
  lines, and states both failure directions.
- **F5, F14** — closed. `TOOL-aGradedMandate-6` S1a validates the commit before the blob read, and
  AC3b covers the mirror direction S3 promises.
- **F6, F8** — closed. `TOOL-aGradedMandate-2`'s Inventory now carries the protocol count sentence
  (check 16) and the example conf's `CORE_FLOOR` (`unattended.test.sh:1371`).
- **F12, F16** — closed. `TOOL-aGradedMandate-8` §5's size-ceiling claim is corrected and AC6
  narrowed to the shape half; `TOOL-aGradedMandate-4` drops AC5's orphaned shape clause and states
  the unvalidated-cutoff residual in §5 as a named residual.
- **F19** — closed. Both prose counts replaced with a name.
- **F7, F9, F15, F17, F18** — addressed but not closed. Each fold edit is the subject of a finding
  below: R9, R2 and R7, R10, R8, R5 respectively.

## Findings

| # | Sev | Site | One line |
|---|-----|------|----------|
| R1 | BLOCKER | `spec-TOOL-aGradedMandate-5.md` §4, AC3 | The complement stays on the KIND axis, so one `retire` row is counted as owed AND as history |
| R2 | BLOCKER | `spec-TOOL-aGradedMandate-1.md` §6 AC7 | AC7 expects 3 hits; the predicate refuses 21 of 28, so its own "fourth hit" clause fires 18 times |
| R3 | HIGH | `spec-TOOL-aGradedMandate-5.md` §2 S1/S1a, §4 | `PARK_ACTS_OWED` is a closed kit set the leg neither reads nor joins to any writer |
| R4 | HIGH | `spec-TOOL-aGradedMandate-5.md` §10 | §10 is un-refolded rev-1 prose telling the builder to do what S1a refuses |
| R5 | HIGH | `spec-TOOL-aGradedMandate-8.md` §6 AC7 | `grep -c 'retire' SKILL.md` returns 2 today — S6's only observation is green before S6 exists |
| R6 | HIGH | `spec-TOOL-aGradedMandate-4.md` §2 S3, §3 | `plan_state` returns one token; the section name S3 and AC1 require cannot be built inside §3 |
| R7 | HIGH | `spec-TOOL-aGradedMandate-1.md` §4 Migration | The rewritten census omits this run's own record, the only one it will actually close |
| R8 | MEDIUM | `spec-TOOL-aGradedMandate-5.md` §2 S5, AC6 | The protocol's "declared once … no second list" sentence stays false and no criterion sees it |
| R9 | MEDIUM | `spec-TOOL-aGradedMandate-4.md` §2 S6, AC5 | S6's "three carriers" is not the triple check 22 joins, and the sibling-cutoff claim is false |
| R10 | MEDIUM | `spec-TOOL-aGradedMandate-4.md` §4, §5 | "three arms" against a fold that added two more, in the counts the same fold wrote |
| R11 | LOW | `spec-TOOL-aGradedMandate-8.md` §3 · `-9.md` §3 | Status headers read `rev-1` over a rev-2 log, and the hygiene arm is one-directional |

---

### R1 — BLOCKER · `spec/2026-08-31-spec-TOOL-aGradedMandate-5.md` §4 Data model and Inventory, against §6 AC3

The rev-2 design replaces the refused `kind:act` grammar with a second constant,
`PARK_ACTS_OWED="retire supersede"`, and leaves `PARK_KINDS_OWED` holding bare kinds only (S1). §4
then states:

> The complement rule is preserved on both axes: absent from a set IS history, so there is still no
> second list to keep in step, and `park_kinds_unowed` keeps computing the history side by
> difference.

That sentence is false, and it is false BECAUSE of the mechanism it names. Read at the lines:

- `PARK_KINDS` (`unattended.sh:350`) holds `rescope`.
- `PARK_KINDS_OWED` (`:356`) does not, and S1 keeps it that way.
- `park_kinds_unowed` (`:3352`) computes `PARK_KINDS` minus `PARK_KINDS_OWED` at KIND granularity
  and therefore returns `proposal rescope dispatch review` — the whole `rescope` kind — before and
  after this unit.
- `verb_status` counts the owed rows at `:2618` over `kinds_re "$PARK_KINDS_OWED"`, which S3
  widens with the act arm, and the history rows at `:2628` over `kinds_re "$(park_kinds_unowed)"`,
  which nothing in this spec touches.

So a `rescope · item retire TOOL-… ` row matches BOTH alternations. `--status` prints
`· parked 1 · noted 1` for one row, and the two counts sum above the parked total. That is the
operator surface this unit exists to fix, reporting one retirement as an unanswered decision and as
a note simultaneously — the "two readers of one taxonomy disagreeing" defect S3 is written to
prevent, reproduced by the unit preventing it.

`park_kinds_unowed` appears in NO Inventory row, so a builder working from the Inventory has no
reason to open it, and §4 has actively told them it needs nothing.

AC3 cannot see it. It reads: *counts a retire row among the decisions the owner is owed and an add
row among the notes*. A retire row counted twice satisfies the first half and does not contradict
the second. The unit ships green against its own criteria with its deliverable wrong.

This is a blocker rather than a high for the same reason round 1's F2 was: building to the spec as
written produces a broken artifact, and the repair is not a missing inventory line but a design
decision the spec has not made — whether the history side subtracts owed ACTS as well as owed kinds,
or whether the notes alternation excludes `rescope · item (retire|supersede) ` positionally.

**Fix.** Add a CHANGED Inventory row for `unattended.sh:3352` `park_kinds_unowed` and specify the
history side as the complement over (kind, act) pairs: a `rescope` row is history only when its
first item token is outside `PARK_ACTS_OWED`. Rewrite §4's "preserved on both axes" sentence to say
which function does the subtracting on which axis — the sentence is load-bearing and is currently
the instruction that produces the defect. Extend AC3 with the negative half: the retire row is
counted in the owed count and NOT in `noted`, and `parked + noted` equals the total parked-row
count.

**Left-shift.** An arm in `tools/unattended/unattended.test.sh` that writes a fixture record holding
exactly one `rescope · item retire …` row, runs `--status`, and asserts the printed line carries
`parked 1` and NOT `noted`. Add its partition sibling: over a fixture holding one row of every
member of `PARK_KINDS`, assert `parked + noted` equals the row count — that arm gates the CLASS
(any future kind or act landing in both alternations or neither) rather than this instance. Both
fail today against the specified design, which is exactly why they are worth writing: stage the
break, confirm RED, unstage.

---

### R2 — BLOCKER · `spec/2026-08-31-spec-TOOL-aGradedMandate-1.md` §6 AC7, against §2 S1

AC7 was added by the fold to close F9. It requires the candidate predicate be run over every tracked
`RUN.md` before wiring, printing hits and near-misses, and then pins the answer:

> The expected hits are `memory/builds/aBoundedCeiling/RUN.md`,
> `memory/builds/aPrimedKeepalive/RUN.md` and `memory/builds/aThawedCorpus/RUN.md`; a fourth hit is
> a finding, not a pass.

I ran it. S1's predicate is: `review` rows whose ` · item ` subject equals the build slug, at least
one must exist, and the LAST must carry a terminal token from `CONVERGED` / `NON-CONVERGENT` /
`CEILING`. The subject join is EXACT — `review_counts` at `unattended.sh:3438` does
`if (item != subj) next`, and S3 commits the new reader to the same grammar in the same shape.

Over all 28 tracked `RUN.md`: **7 pass, 21 refuse.**

- **Pass (7)** — `aBoundedVerdict`, `aGroundedOrientation`, `aLexedStripper`, `aScouredKit`,
  `dFramedEntrypoint`, `dPromptedSeam`, `dScaffoldedMirror`.
- **Refuse on the terminal-token arm (2)** — `aBoundedCeiling`, `aPrimedKeepalive`.
- **Refuse on the "at least one exists" arm (19)** — `aBranchedMandate`, `aDeclaredBound`,
  `aDeclaredCeiling`, `aFusedCharter`, `aGradedMandate`, `aMeteredTurnstile`, `aPacedTurnstile`,
  `aPromptedMandate`, `aScannedThrottle`, `aSealedCaravan`, `aSiftedPlaybook`, `aThawedCorpus`,
  `aWalkedCorpus`, `cBriefedPilot`, `dCarriedReceipt`, `dClosedLexicon`, `dScriptedRepeat`,
  `dTieredTribunal`, `dUnstalledConvoy`.

`dCarriedReceipt` carries 19 review rows and `dTieredTribunal` and `dUnstalledConvoy` carry several,
all keyed on unit ids or suffixed handles rather than the bare slug — so the refusals are not merely
records with no review history. No reading of "hit" yields 3: would-block is 21, records carrying
any bare-slug review row is 9, records carrying review rows but no terminal slug row is 7. The
pinned set of three appears to be the terminal-token arm's two hits plus the live record — the
predicate minus its own first clause.

The consequence is not a wrong number in a document. AC7 says a fourth hit is a finding. Executed as
written it produces eighteen, and the builder's cheapest exit is to loosen or override the one
criterion the fold added to stop F9 recurring. A pinned expected value the tree contradicts is not a
style call, and no phase scoping rescues it: two of the three named records are `LANDED` while
twelve other `LANDED` records are omitted.

**Fix.** Restate AC7 from the measurement rather than from §3's two names plus the Migration
example: 21 hits over 28 tracked `RUN.md` with 7 passing, the passing set named, and the failure
condition changed from "a fourth hit" to "a hit outside the recorded set, or any hit on a
non-terminal record". State in the same bullet WHY a hit on a terminal record costs nothing — the
slug-subject closing-review convention postdates most tracked records and no verb re-closes them —
because that is the argument §4 is actually making and the probe exists to evidence it.

**Left-shift.** Not a gate: the population legitimately freezes at authoring time and a leg over it
would red honest landings (§3 already rules that out for exactly this reason). The check that
belongs here is procedural and is already in the charter — *run a candidate gate predicate over the
real tree before wiring it, and print hits AND near-misses*. AC7 is that rule correctly invoked and
then answered from memory instead of from the run. The durable left-shift is to make the AC demand
the probe's OUTPUT be pasted into the journal record and compared against a set the AC does not
pre-declare, so the criterion cannot be satisfied by a number nobody re-measured.

---

### R3 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-5.md` §2 S1/S1a and §4 Inventory

`PARK_ACTS_OWED` is a new CLOSED kit-owned set with a `--status` counter and a Definition-of-Done
predicate hanging off it, and nothing on the leg reads it, refuses it empty, or joins it to a writer.

The leg's own block comment states the criterion verbatim, at `check-unattended.sh:215-217`:

> The parked-kind taxonomy. Read here for the same reason the four above are: a set declared in the
> driver and graded nowhere is decoration, and this one has a counter and a Definition-of-Done
> predicate hanging off it.

Every sibling set is read through `core_of` with an unreadable-refusal: `AUTH_MODES` (`:196`),
`SECOND_ANCHOR_MODES` (`:213`), `PARK_KINDS_OWED` (`:219`), `RUNAWAY_CEILING` (`:221`),
`HALT_CODES_CORE` (`:225`), the core sets (`:228-230`). `PARK_KINDS_OWED` gets a second guard on top:
check 2's `pk_dead` loop at `:366-371` asserts every owed kind has a `park "$rel" <kind> ` call
site, and check 27's third loop at `:1948-1953` asserts the owed set is a subset of `PARK_KINDS`.
The spec's Inventory pins both of those ranges UNCHANGED and adds no leg row at all, so the new set
inherits neither. It does not even get the presence assertion `unattended.test.sh:3788` gives the
sibling constant.

The writer side is equally unjoined. The act vocabulary's only other home is an inline closed-set
case arm in `verb_rescope` — `retire|supersede|add)` at `unattended.sh:3882` — so there is no
declaration to join against, and check 24 hardcodes act tokens a third time at `:1623`, `:1629` and
`:1635`. A typo (`supercede`) or a rename silently drops those rows back into history: the surfaced
count returns to what it was, the unit's whole purpose reverts, and `unattended kit gate`, the
driver suite and every AC in §6 stay green. That is the same silent-widening class the driver's own
header says `PARK_KINDS` was promoted to a declaration to close, and check 27's header carries the
recorded incident — the protocol declared `DECISION` for as long as it had instructed a run to park
one, and no verb wrote it.

Nothing in §3 withholds this. The non-goals cover new kinds and fields, a volume cap, and
`verb_rescope`'s refusals. S1a's own argument for a separate constant is that the SIBLING set has
exactly this protection.

**Fix.** Add an Inventory row for `check-unattended.sh` reading `PARK_ACTS_OWED` through `core_of`
with an unreadable-refusal in its siblings' shape, plus a dead-member arm asserting every member is
a first token `verb_rescope`'s act case can accept. Add an AC that sets a bogus member and observes
the named red — the red-fixture discipline S1a cites as its own justification. If the leg-side guard
is deliberately deferred, say so in §5 as a named residual the way the protocol states the unarmed
`review` shrink floor, rather than leaving the Inventory reading as full coverage.

**Left-shift.** The dead-member arm IS the gate, and it closes the class rather than the instance:
every closed vocabulary this kit declares should be joinable to the code that writes it. Beside it,
an arm asserting the driver contains no second spelling of the act alternation — the same shape
`unattended.test.sh:3789` already uses to ban a second spelling of the kind alternation — which
would also catch check 24's three hardcoded copies. Observe both RED first.

---

### R4 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-5.md` §10 Reuse audit, against §2 S1a and §4 Inventory

§10 was not reconciled with the fold. It is rev-1 text and it survives verbatim, in the present
tense, in the section the DoR mandates a builder read for where the edit lands:

> The seam is `park_kinds_unowed` at `tools/unattended/unattended.sh:3348`, which already computes
> the history class as the COMPLEMENT of `PARK_KINDS_OWED` — so widening the owed set is the only
> edit the split needs … `kinds_re` at `:3340` … is the single site where the pair form has to be
> understood.
>
> The leg's both-directions taxonomy check at `check-unattended.sh:1943-1951` is the reader that
> would otherwise refuse the new member shape; it is extended rather than exempted.

Three statements, all now wrong, and one record giving two opposite instructions about the same leg
lines:

- **"widening the owed set is the only edit the split needs"** — rev-2 leaves `PARK_KINDS_OWED`
  alone and adds a separate constant plus arms in `dod_met` and `verb_status`.
- **"the pair form"** — S1a REFUSES the pair form outright, and §4 marks both `:366-371` and
  `:1943-1951` UNCHANGED. A builder following §10 rebuilds the widened member grammar round 1's
  BLOCKER F2 rejected, and reds check 2's `pk_dead` loop on this unit's own tree.
- **"the single site"** — false independently of the fold. `dod_met`'s `parked-decisions-surfaced`
  arm at `unattended.sh:3226` open-codes its own alternation with
  `printf '%s' "$PARK_KINDS_OWED" | tr ' ' '|'` and never calls `kinds_re`. That is S2's own target
  and the Inventory lists it as changing, so the spec knows about the site its §10 says does not
  exist.

Minor, noted here rather than as its own row: §10's line citations have drifted. `park_kinds_unowed`
is at `:3352` and `kinds_re` at `:3344`, not `:3348` and `:3340`.

**Fix.** Rewrite §10's last two paragraphs to the shipped design. The seams are `park_kinds_unowed`
(`:3352`) for the history axis and the TWO owed-alternation sites — `kinds_re` at `:3344`, called by
`verb_status` at `:2618`, and the inline `tr ' ' '|'` at `:3226` inside the
`parked-decisions-surfaced` predicate. `check-unattended.sh:366-371` and `:1943-1951` are untouched
by construction because `PARK_KINDS_OWED` keeps bare kinds, and S1a says why. Delete the "extended
rather than exempted" sentence outright. Refresh the two line numbers.

**Left-shift.** No gate reaches a stale §10, and one that graded spec prose against source line
numbers would be a maintenance tax with a worse failure mode than the defect. The check that belongs
here is a fold-procedure one worth adding to `memory/guides/BUILD-METHOD.md`: **a fold that changes a
unit's DESIGN re-reads that unit's §10 in the same pass, because the reuse audit is the section
written earliest and the one no acceptance criterion can observe.** Round 1 raised this class twice
(F16, F17) in different sections; this is its third instance and the first where the stale prose
re-opens a closed blocker.

---

### R5 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-8.md` §6 AC7

AC7 is the fold's answer to F18 — S6 had no criterion, and two other units discharge their user-docs
obligation onto it. It reads:

> `grep -c 'retire' .claude/skills/unattended/SKILL.md` inside the `--rescope` paragraph is at least
> 1, which is the only observation S6 has.

Measured on the unedited render: `grep -c 'retire' .claude/skills/unattended/SKILL.md` returns **2**,
before S6 is written. The hits are `SKILL.md:139` ("the retired bytes stay exactly as the previous
run left them") and `SKILL.md:504`, which is the invocation line
`--act retire|supersede|add` — and line 504 sits INSIDE the `--rescope` bullet, which spans roughly
`:499-513`. The paragraph qualifier does not rescue the criterion, because the pre-existing hit is
in the paragraph. Uppercase `RETIRE` at `:500` and `retiring` at `:512` do not match
case-sensitively, so the paragraph has exactly one matching line today: the one that was always
there.

So S6's only observation is green before S6 exists, and AC7 says so in its own words. The retirement
sentence can silently not ship — which is the defect F18 raised, reproduced by the fix for F18. The
sibling criteria are not vacuous by contrast: `pieces-complete` (AC1), `not retired` (AC2),
`gotchas.py` (AC3) and `--verdict FAIL` (AC4) each return 0 on the current render, which is what a
falsifiable criterion looks like. `TOOL-aGradedMandate-5` §5 discharges its user-docs obligation
here explicitly, so the dependency is live.

**Fix.** Anchor AC7 on bytes S6 must INTRODUCE rather than on a word the file already carries: grep
the render for the phrase the new sentence brings in — the owner's turn, `PARK_ACTS_OWED`, or
"surfaced" inside the `--rescope` paragraph — and record the measured pre-edit count of 0 beside it,
so the criterion is observably falsifiable. Record the pre-edit `grep -c 'retire'` value of 2 in §5
as the reason the obvious spelling was rejected. Spell the paragraph scope as a runnable selector
(awk between the `--rescope` bullet and the next one) rather than as a parenthetical no command
implements.

**Left-shift.** Gate the CLASS, in the kit's own leg rather than in the spec: `check-unattended.sh`
already reads the rendered Skill for the directive join, so a third assertion over the same file
costs one comparison and survives the build — assert the `--rescope` paragraph names the surfaced
split, the same way check 16 asserts the protocol's count sentence. And the procedural rule this
instance argues for, worth stating in the review protocol: **a grep-shaped acceptance criterion is
not accepted until its pre-edit count has been measured and written down.** A criterion whose
current value nobody ran is an assertion about nothing, which is this repo's own recorded defect
class one artifact over.

---

### R6 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §2 S3, against §3 Non-goals

S3 requires a `DOD_OUT` message "naming each thin unit and which of the three sections is empty,
since `plan_state` already knows which". It does not — not in any form a caller can read.

`plan_state` is at `unattended.sh:1593`. Its per-section map `seen["scope"]` / `seen["acc"]` /
`seen["gates"]` is built inside the awk program and consumed inside the `END` block, which prints
the bare word `THIN` and exits. The map never leaves. Its only caller is `verb_plan` at `:1977`,
which receives one token. So S3's premise is true only INTERNALLY, and the grade the caller gets
cannot name the empty section that S3's message and AC1 both require.

§3 forbids the natural repair: *No change to `plan_state` itself.* That non-goal is load-bearing
well beyond this unit — the function body is SLICED out of the shipped bytes and graded against a
case table by both `tools/unattended/unattended.test.sh:3677` (`slice_fn plan_state`) and the
cross-kit `tools/memory-tree/marker-contract.test.sh:218`, so widening its output ripples into a
contract this kit keeps deliberately unshared, and the function's own header says the slicing is why
constants may not be defined outside it.

That leaves one route: a second section-emptiness derivation beside `plan_state`. §4's Inventory
prices it nowhere (no `plan_state` row, no new helper row), §10 denies it exists ("Nothing new is
derived"), and it is a second spelling of the M2 THIN rule — the two-answers-to-one-question defect
`lib-unattended.sh`'s own header exists to prevent.

**Fix.** Pick one and say so in §2. Either add an S-item widening `plan_state`'s output to
`THIN <section>` — with the matching Inventory row, the narrowed non-goal ("no change to the
three-section PREDICATE"), and the two sliced harnesses named as the blast radius — or drop the
section name from S3 and AC1 and state in §5 that the message names the unit only, because the grade
is a single token by design. The second is the smaller change and is probably right; the point is
that the spec currently promises the first while forbidding it.

**Left-shift.** If the output widens: an arm in `marker-contract.test.sh` asserting the two readers
still agree on the GRADE after the token gains a suffix, since that harness is the one that would
discover the divergence last. If it does not: an arm asserting the `DOD_OUT` message names the unit
and no section, so a later contributor cannot quietly reintroduce the section name by re-deriving it
beside the function.

---

### R7 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-1.md` §4 Migration

The fold rewrote §4's Migration to correct round 1's F9, and the rewritten census — a section that
advertises itself as "Stated rather than assumed" — is wrong in the one direction that matters:

> The one live record in the tree is `memory/builds/aThawedCorpus/RUN.md`, and it WOULD BLOCK.

There are two live records, and the omitted one is this run's own.
`memory/builds/aGradedMandate/RUN.md` is tracked, sits at `phase: FOLDING`, and carries exactly one
review row: `review · item aGradedMandate-specs · reason verdict BLOCKED · blockers 2`. The subject
join is exact (`unattended.sh:3438`, `if (item != subj) next`), so `aGradedMandate-specs` does not
satisfy a join on `aGradedMandate` and the S1 term returns no row at all — the same failure
`aThawedCorpus` gets, on the record that will actually reach `--close`. `aThawedCorpus` is at
`LANDING` with `--close` already run; `aGradedMandate` is the more live of the two by phase.

Whether this unit blocks its own build depends on whether the closing round happens to park a row
keyed on the bare slug. Seven records in the corpus do exactly that, so the block is not certain —
which is precisely why it belongs in the Migration section as a stated dependency rather than as an
accident. `TOOL-aGradedMandate-2` §4 handles the identical situation correctly one file over: *This
build is its own first subject and must satisfy it.* Unit 1 says nothing.

**Fix.** Add the run's own record to §4 Migration with its measured row, and state which side gives:
either S1 accepts a subject PREFIXED by the slug — with the false-positive boundary spelled out,
since `aGradedMandate-specs` and a hypothetical `aGradedMandateFoo` are different risks — or the
spec records that this build's closing loop must park a `review` row whose subject is the bare slug
before `--close`. Say it in the spec, not in the run's head.

**Left-shift.** Fold it into R2's probe: the AC7 census already enumerates every tracked record's
verdict under the predicate, so requiring the census to flag any record at a NON-TERMINAL phase
makes this instance fall out of the probe automatically rather than depending on a human noticing
which records are live. That is the one arm of AC7 worth keeping strict, and it is the arm that
would have caught this.

---

### R8 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-5.md` §2 S5 and §6 AC6

S5 owns the protocol fact-3 correction outright after the fold deleted `TOOL-aGradedMandate-8` S5 —
which is the right resolution of F17. But the edit is scoped to "fact 3's kind enumeration and its
surfaced sentence", and the sentence immediately after those two, in the same block, is the one this
unit falsifies. `memory/guides/UNATTENDED-PROTOCOL.md:193` and `tools/unattended/PROTOCOL.template.md:193`,
byte-identical:

> Membership is declared once, in the driver's `PARK_KINDS_OWED`, and `history` is the COMPLEMENT —
> absent from that set IS history, so there is no second list to keep in step.

After S1 there are two declarations, and a `rescope retire` row is surfaced while absent from
`PARK_KINDS_OWED`. Both clauses become false, in the BINDING contract, on the exact property a
reader consults it for. A future reader who follows it adds a kind to `PARK_KINDS_OWED` expecting
the complement to follow, and gets R1.

Nothing observes it. AC6 greps `of eight kinds` and checks the surfaced sentence's members — neither
reaches `:193`. AC5's byte-identity leg is true before the edit, true after it, and true if neither
copy moves; over a false sentence it proves only that both copies are wrong identically. No check in
`check-unattended.sh` joins that prose to either constant: check 27 is driver-internal and check 16
parses only the DoD count sentence.

The driver's own twin IS covered — the Inventory's `PARK_KINDS_OWED` row reads "UNCHANGED, and its
header says why the acts live apart", which reaches `unattended.sh:396-398`'s "MEMBERSHIP IS DECLARED
HERE AND NOWHERE ELSE … That is the whole reason it is one constant and not two". So the protocol is
the single carrier left asserting the old invariant. While that header is being rewritten, §4's
Alternatives-rejected should also engage the recorded ruling at `unattended.sh:383-390` — the merge
that deliberately converged two names for this one fact — because reversing it is the argument this
fold owes, and "kinds and acts are different things" is not that argument.

**Fix.** Extend S5 and the `PROTOCOL.template.md` §2 Inventory row to name the `:193` sentence
explicitly: membership is declared on two axes, kinds in `PARK_KINDS_OWED` and acts of `rescope` in
`PARK_ACTS_OWED`, and history is the complement on both. Extend AC6 with a grep asserting the
replacement names both constants and states which axis each governs, so the correction is OBSERVED
rather than left to a byte-identity check that cannot see it.

**Left-shift.** Extend check 27 — or a sibling — to join fact 3's surfaced sentence to the two
constants it describes, the same both-directions join the leg already runs on `PARK_KINDS` against
the `park()` call sites. That closes the class round 1 opened as F17 and this round re-finds one
sentence lower: a prose statement of a declared set's membership, sitting beside the set, with no
machine joining them. Check 16 already gates exactly this shape one section further down the same
document, so the pattern is in the file and needs copying, not inventing.

---

### R9 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §2 S6, against §6 AC5

S6 is the fold's answer to F7 and it mis-maps its own gate. S6 names THREE carriers —
`.unattended.conf`, `tools/unattended/.unattended.conf.example`, and the driver's conf-default init
block — and AC5 says green "with the new key declared in all three carriers, which is what check
22's three-way key join asserts".

Check 22 (`check-unattended.sh:1228-1256`) joins three populations and the driver's init block is
not among them:

- `doc_keys` — the FIRST table cell of `UNATTENDED-PROTOCOL.md` §8;
- `ex_keys` — `^[A-Z_]+=` in `tools/unattended/.unattended.conf.example`;
- `proj_extra` — `^[A-Z_]+=` in `$ROOT/.unattended.conf`, one direction only.

So the carrier check 22 actually requires — the protocol §8 row — is not one of S6's three, and the
init block it does name is invisible to the check. A builder who declares the key in S6's three and
skips the protocol row reds check 22 in both directions at once: the example key arrives
"undocumented in the protocol" and the project key "set by this project and undocumented".

S6's supporting claim is false as measured, too: *Both sibling cutoffs are carried in all three.*
`unattended.sh:289` defaults `UNITS_REGION_CUTOFF` only. `LANDED_ANCHOR_CUTOFF` is defaulted at
`check-unattended.sh:118` and appears nowhere in `unattended.sh` — because the LEG reads it and the
driver does not. Which file defaults a key follows which file reads it, and S6 states the opposite
as a pattern to copy.

Impact is narrower than the two errors suggest, and that is why this is a medium: §4's Inventory DOES
carry the `PROTOCOL.template.md` §8 / `UNATTENDED-PROTOCOL.md` §8 row, and AC5's binding clause is
"stays green". A builder working the Inventory lands correctly. But the spec's stated mapping of its
own scope item to its own gate is wrong on two verified counts, in the section a reader consults to
understand WHY four carriers are owed.

**Fix.** Rewrite S6 as FOUR carriers — project conf, example conf, the `unattended.sh:289` init
block (because the DRIVER reads this key, unlike `LANDED_ANCHOR_CUTOFF`), and the protocol §8 table
row — and re-point AC5 at what check 22 asserts: example-against-table in both directions plus
project-conf-against-table in one. Replace the sibling-cutoff sentence with the measured split and
the rule behind it.

**Left-shift.** Check 22 already gates three of the four carriers; the ungated one is the init
block, and its failure mode is loud (`set -u` aborts the driver), which AC7 now covers. The
worthwhile addition is a fourth arm to check 22 asserting every key in the example conf that the
DRIVER reads is defaulted in the driver's init block — derived by grepping `${KEY:-` or `$KEY` in
`unattended.sh`, not by a hand-kept list. That would have caught this mapping error mechanically
and closes the class for the next conf key.

---

### R10 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §4 Inventory and §5

The fold added AC6 (a fixture BOTH structurally broken and thin, to observe S2's ordering
requirement) and AC7 (the driver run with the key unset under `set -u`). It did not update the two
places that count the arms those criteria need.

§4's Inventory row for `unattended.test.sh` still reads: *a thin-and-CLOSED arm, a thin-but-
grandfathered arm, a fat arm.* §5's testing line still reads: *three arms, each observed RED first.*
AC7 says in its own words "verified by an arm in `unattended.test.sh`", and AC6's fixture — one unit
whose spec is MISSING plus one CLOSED-and-thin unit — is a distinct fixture from the thin-and-CLOSED
arm already listed. No reading reconciles them.

Both criteria were added because nothing observed the thing they observe: AC6 is the only observer
of S2's ordering, AC7 the only observer of S6's `set -u` default. A builder working from the
Inventory builds three arms, and both are again omissible. This is the derived-count-in-prose class
the charter bans outright, inside the fold that was supposed to close the omission.

**Fix.** Add the ordering fixture and the unset-key arm to the Inventory row, and move §5's figure
to five — naming AC6's fixture shape explicitly, so the ordering assertion lands on the MESSAGE
(missing-unit reported, THIN not reported) rather than on the verdict, which both faults would
produce identically.

**Left-shift.** The general rule is already in the charter — no count of a derived population is
written in prose — and it is unenforceable inside a spec record, where the population legitimately
freezes at authoring time. The enforceable version is narrower and worth adopting for this build's
remaining folds: **when a fold adds an AC, it edits the Inventory row for the file that AC names, in
the same edit.** That is a two-line rule for `BUILD-METHOD.md`'s fold section, and it is the same
discipline R4 argues for from the §10 side.

---

### R11 — LOW · `spec/2026-08-31-spec-TOOL-aGradedMandate-8.md` line 3 and `spec/2026-08-31-spec-TOOL-aGradedMandate-9.md` line 3

Both records carry `**Status:** SPECCED · rev-1` while each §9 logs a substantive `rev-2 ·
2026-08-31 · round-1 fold` entry — unit 8's deleting S5, halving S6, correcting the §5 size claim,
narrowing AC6 and adding AC7; unit 9's replacing the §3 prose count. Units 1, 2, 4, 5 and 6 were all
bumped to rev-2, and unit 3 to `WONTDO · rev-2`. Unit 7 is legitimately rev-1 in both places. These
two are the only mismatched records in the set.

Nothing catches it, and the mechanism is worth stating because it is a genuine one-directional gate.
`check-memory-hygiene.sh:919` fires on `if (!seen || hrev + 0 > mx)` — the header rev is reported
only when it is ABSENT from §9 or GREATER than the maximum logged there. With `hrev = 1` present and
`mx = 2`, the arm is silent. A header that LAGS its own log is invisible to the bar by construction.

The consequence is already on disk: `memory/builds/aGradedMandate/README.md`'s generated units table
renders units 8 and 9 as `rev-1` at rows 89 and 90, telling every later reader — a rev-currency
question, a round-3 review pinning blobs by rev, `TOOL-aGradedMandate-2`'s own reasoning about "an
audit at the unit's current rev" — that these two were never folded.

**Fix.** Bump both status headers to `rev-2`.

**Left-shift.** One comparison in that same hygiene arm: red when the header rev is BELOW the §9
maximum as well as above it. The arm's own comment records that closing the range in the other
direction changed 0 of 22 in-scope specs when it was measured, so the cost of the symmetric closure
is likely a handful of records and a fixture. That is the both-directions rule this repo applies to
every other declared population, applied to the one place it is currently half-applied — and it
should be raised as its own backlog row against the memory-tree kit rather than smuggled into this
build, because it grades a population no unit here owns.

## What this pass did NOT cover

Stated so a green row is never misread as a verified one.

- **`TOOL-aGradedMandate-2`, `-6` and `-7` drew no confirmed finding.** For `-2` and `-6` that is a
  judgement on their folds specifically: F4, F6 and F8 are closed in `-2` (S2a spells the
  whole-token-plus-range join, and both missing Inventory carriers are added), and F5 and F14 in
  `-6` (S1a validates the commit before the blob read, AC3b covers the mirror direction). Their
  UNFOLDED surface was re-read but not re-audited to round-1 depth, because round 1 already covered
  it at the same blobs for `-7`. `-7` was unchanged by the fold and remains the only record in the
  set whose one cross-unit claim was correctly written the first time.
- **`TOOL-aGradedMandate-3` was not reviewed.** It is `WONTDO` at rev-2 on round 1's BLOCKER F1 and
  is out of scope by construction. Its fork is parked in `RUN.md` and is an owner question.
- **No finding grades whether a unit's IDEA is right.** Same scope as round 1: whether each spec
  describes the code it names, whether its criteria observe its scope, and whether building to its
  Inventory lands green. Whether `specs-audited` or the retirement split should exist at all is an
  owner question and is untouched.
- **The refuted 9 are not re-litigated.** They divided between re-reports of round-1 findings the
  fold had already closed and findings whose reachability collapsed against a stated non-goal.
- **One probe was executed; nothing else was.** R2's census ran S1's predicate over all 28 tracked
  `RUN.md` and its full result is reproduced above. No gate leg, no driver suite and no `--status`
  invocation was run — R1's double count is derived from reading `unattended.sh:2618`, `:2628` and
  `:3352`, not from observing the printed line. A builder repairing R1 should observe it before
  fixing it, per the same rule R2 invokes.
