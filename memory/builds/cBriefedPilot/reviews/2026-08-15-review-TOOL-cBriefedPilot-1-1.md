**Serves:** spec-audit TOOL-cBriefedPilot-1..22  <!-- inferred: an M4 pass its header scopes to 22 specs -->

## Verdict: CLEAN WITH FIXES

**M4 spec audit · cBriefedPilot · 2026-08-15 · node c · 22 specs · base 709d260**

## What this pass audited, and what it did not

The 22 conforming specs under `memory/builds/cBriefedPilot/spec/`, read AS DESIGNS. Three prior passes
had already worked this set on other axes: a nine-agent design panel (51 findings, 47 folded, 4
rejected on measured evidence), a three-lens cross-read for M2 agreement, format conformance and
buildability (31 findings, 18 applied), and an M3 fork sweep on 2026-08-15 (seven forks resolved,
unit 5 PARKED, unit 15 left FORKED on unit 21's verdict token). Format conformance is GREEN —
hygiene check 12 and `gen_build_index.py --check` both pass — and no format defect is reported here.

This pass hunted the axis none of them examined: whether a builder handed one of these specs can
determine what to build, and whether what they would build is the thing the design intends. 41 raw
findings; 12 survived skeptical refutation; deduplicated to **10 distinct defects** (three separate
raw findings turned out to be the same unit-19 acceptance criterion, and one unit-3 finding appears
below at a lower severity than it was raised, because the refutation of it was partly right).

**Zero blockers.** Every finding below is closed by a spec edit before any code is written. The set
is dominated by three classes: a scope item placed where its own mechanism cannot execute (unit 3),
a record that has no owner unit (units 20, 21, README), and an acceptance criterion that is false
against the tree (unit 19). Four HIGH, six MEDIUM.

---

## 1 · HIGH · unit 3 — refusal 1 is placed in a block where it can never fire

**Claim.** Unit 3's refusal 1, "the verb is not `--preflight`", is scoped by S2 and §4 into
`verb_preflight`'s precondition block, which is entered only when the verb IS `--preflight`. AC4
meanwhile requires the behaviour from the other verbs.

**Evidence.** `spec/2026-08-14-spec-cBriefedPilot-3.md` S2 opens "five refusals, each validated in the
precondition block ABOVE the write barrier" and lists as item 1 "the verb is not `--preflight`". §4
"Why validation sits above the write barrier" repeats it — "The five refusals join that block" — and
§10's reuse audit names "`verb_preflight`'s precondition block" as the seam all five join. Verified at
source: that block is `tools/unattended/unattended.sh:800-830`, inside `verb_preflight`, reached only
via the dispatch's `--preflight) verb_preflight "$SLUG" "$KID" ;;`. AC4 reads "When `--waive` is
passed to a verb other than `--preflight`, THAT VERB refuses."

**Consequence.** A builder following S2, §4 and §10 writes a `fail` branch inside `verb_preflight`
testing `[ "$verb" != "--preflight" ]`. It is dead code, and `check-arms.py` requires every `fail`
branch be armed by a positive assertion naming its own failure text — no arm can drive an unreachable
branch, so either `harness arms` reds or the branch is pinned into
`memory/project/unarmed-branches.txt` and S7's `ARMS_FLOORS` raise counts a branch that never runs.
AC4's actual behaviour is then built by nobody, and the ordering guarantee the whole design rests on —
"one branch, not a convention" — is absent from the tree.

There is a second, sharper wrinkle the spec does not reach. The dispatch loop at
`unattended.sh:1001-1016` **exits inside the loop** for two verbs: `--plan) shift; verb_plan …; exit $?`
and `--phase) … verb_phase …; exit $?`. So a post-loop guard — the obvious constructible home for
refusal 1 — is never reached by `--waive … --plan <slug>` or by `--plan <slug> --waive …`. Those two
verbs would silently accept and discard a waiver pair, which is exactly the "a verb reachable mid-run
is a place the run could answer its own question" hazard §4 rejects the `--waive` verb over.

**Edit.** In unit 3's S2, split the block: refusals 2-5 join `verb_preflight`'s precondition block;
refusal 1 is a guard in the argv dispatch, evaluated *inside* the parse loop's `--plan` and `--phase`
arms as well as after the loop, so no verb can exit past it while a waive pair is accumulated. Amend
§4's sentence to "The four remaining refusals join that block", and add the dispatch to §10's seam
list as a fifth extended seam.

---

## 2 · HIGH · unit 3 / README / unit 10 — the ordering branch is spelled two incompatible ways

**Claim.** The single mechanism the design says carries the whole ordering guarantee is stated one way
in unit 3 and a stricter, incompatible way in the master overview and in unit 10.

**Evidence.** `README.md` "The waiver, end to end": "**The ordering guarantee is one branch, not a
convention.** `--waive` is accepted by `--preflight` alone and only while no run-state file exists."
`spec/2026-08-14-spec-cBriefedPilot-10.md:62` repeats the same shortened rule: "alone and only while
no run-state file exists, so after preflight there is no verb that could take an answer".
`spec/2026-08-14-spec-cBriefedPilot-3.md` §4 states the actual rule with its disjunct: "accepted by
`--preflight` alone, and only while no run-state file exists **or the requested set matches the
recorded one**", and S2 refusal 2, S5 and AC5 all depend on that second clause.

**Consequence.** BUILD-METHOD M2's cross-read rule says a disagreement of this shape is a defect in
exactly ONE document and forbids building the intersection. Built to the README, unit 3's S5
idempotence and AC5's "byte-identical preflight re-run over a live record" are unsatisfiable and a
resumed run cannot re-issue the Skill's own step-C command line. Built to unit 3, the README and unit
10 state a refusal the driver does not have, and unit 10 §4's argument that no verb can take a late
answer no longer follows from the branch it cites.

**Edit.** Correct the README's sentence and unit 10 §4's echo to unit 3's rule: "`--waive` is accepted
by `--preflight` alone, and only while no run-state file exists or the requested set equals the
recorded one." Unit 3 is the document that is right; the two echoes are the defect.

---

## 3 · HIGH · unit 20 — S3 closes the residual row the M3 sweep deliberately preserved

**Claim.** Unit 20's S3 closes EVERY `TOOL-cBriefedPilot-*` backlog row, which includes row 23 — the
newline injection residual unit 1's fork resolution filed rather than absorbed.

**Evidence.** Unit 20 S3: "`memory/backlog/TOOL.md`: every `TOOL-cBriefedPilot-*` row to its terminal
token". `memory/backlog/TOOL.md:57`: "`TOOL-cBriefedPilot-23 · OPEN · a newline in an --override or
--abort reason forges a second parked line, because park() writes it verbatim into a region with a
line grammar. Unit 3 closes it for --waive only; the shared refusal was vetoed out of unit 1`."
Confirmed at source: `park()` at `unattended.sh:995` is `printf '\n%s %s · item %s · reason %s\n' … >> "$1"`,
a verbatim append into a line-grammar region, and unit 3's refusal 5 is scoped to `--waive`. Unit 20
is rev-2, dated 2026-08-14 — it predates the 2026-08-15 sweep that minted row 23.

**Consequence.** A builder following S3 literally marks row 23 CLOSED or WONTDO in the same commit as
the honest closures. The only record of a reproduced, still-open injection hole in `park()` goes
terminal with no work done — and it is now a worse hole than when it was filed, because after unit 3
the forged second line can be a well-formed `waiver · item <handle> · reason <text>` line that check
17 will accept and grade. The M3 veto that preserved the row is undone by the records unit.

**Edit.** S3 gains an exemption clause: "every `TOOL-cBriefedPilot-*` row to its terminal token EXCEPT
`TOOL-cBriefedPilot-23`, which stays OPEN — it is the residual unit 1's §8 filed when the shared
newline refusal was vetoed, and unit 3 closes only the `--waive` half." Add a matching AC beside AC4
observing that row 23 is still OPEN after this unit lands.

---

## 4 · HIGH · units 21 and 20 — the parallelism verdict has no record owner

**Claim.** Units 15 and 21 both delegate the parallelism verdict's `memory/DECISIONS.md` row and
backlog row to unit 20, and unit 20's scope claims neither.

**Evidence.** `spec/2026-08-14-spec-cBriefedPilot-21.md:33` §3: "**Any row in `memory/DECISIONS.md` or
`memory/backlog/TOOL.md`.** Unit 20 derives both from this recording."
`spec/2026-08-14-spec-cBriefedPilot-15.md:98-99` §4: "The backlog row and the `memory/DECISIONS.md`
row are unit 20's to derive — writing either here would duplicate a later…". Unit 20's S4 enumerates
exactly three DECISIONS rows (the registry is a kit constant and not a conf key; a waiver is taken at
preflight and nowhere else; the contract names zero handles) — none about parallelism. S5 files
exactly one NEW backlog row, the F4 read budget. S3 only closes this build's existing rows, and
closing `TOOL-cBriefedPilot-21` writes its terminal token, not its answer — the row text is the
question. Grepping unit 20 for `parallel` or for `21` outside S6's check-count arithmetic returns
nothing.

**Consequence.** On branch B — a legitimate outcome, and per P2 a likely one — the most expensive
finding in the build (a whole Tier-2 research unit answering "can an unattended run parallelize a
build pass at all") exists only as a dated recording under `memory/builds/cBriefedPilot/build/`.
`memory/DECISIONS.md` and `memory/backlog/TOOL.md` — the two surfaces M5's recall probe and the next
build's grounding read first — carry nothing, and the question re-opens at the next design pass with
the measurement lost. That is precisely the failure P2 spent a research unit to prevent.

**Edit.** Unit 20 S4 gains a fourth DECISIONS row for unit 21's verdict token, and S5 gains a second
new backlog row carrying the per-route "one thing that would have to change" from unit 21's recording.
Both are stated as conditional on the token, so branch A and branch B each have a home. Name unit 21
in unit 20's front-matter dependency line, which today reads `all`.

---

## 5 · MEDIUM · unit 19 — AC1's second clause is false against the tree

*(Raised independently three times in this pass, as `u19-ac1-unrunnable-grep`, `bump-grep-collides`
and `bump-ac-unsatisfiable`. One defect.)*

**Claim.** Unit 19's AC1 requires that no occurrence of `1.4` survive outside `memory/`, which is
false for reasons this unit cannot change.

**Evidence.** `spec/2026-08-14-spec-cBriefedPilot-19.md:89` AC1: "verified by
`grep -rn \"unattended@1\.5\|KIT_UNATTENDED_VERSION=1\.5\"` returning the six files in §4's table and
no occurrence of `1.4` surviving outside `memory/`". Measured with `git grep -n '1\.4' -- ':!memory/'`,
five legitimate hits remain outside this unit's six-file scope:

| Path | Occurrence |
|---|---|
| `tools/hooks/agent-cap.js:52` | `const KIT_AGENT_CAP_VERSION = '1.4' // gov:kit agent-cap@1.4` |
| `.claude/hooks/agent-cap.js:52` | the deployed-verbatim copy of the same line |
| `WIRE-INTO-PROJECT.md:212` | an adopter measured at memory-tree "kit 1.4" |
| `tools/unattended/unattended.sh:135` | a timing comment, "~1.4s of CPU" |
| `tools/unattended/check-unattended.sh:146` | the same timing comment |

**Consequence.** The last unit of the build ends on an acceptance criterion that fails on a correctly
completed unit. A builder running it literally either stalls hunting a bump that is already complete,
or edits `agent-cap.js` to make the grep clean — which breaks the same-line marker/constant pair
`tools/check-kit-versions.sh:46-50` asserts, desynchronises the `.claude/` copy from the `tools/`
original, and reds `kit version markers` with nobody present. Dropping the clause quietly instead
loses the only stated check that no unattended spelling was missed.

**Edit.** Scope AC1's second clause to the kit's own tokens: "and
`git grep -n \"unattended@1\.4\|KIT_UNATTENDED_VERSION=1\.4\"` returns nothing." Both spellings are
unique to this kit; the timing comments and `agent-cap`'s constant fall outside them by construction.

---

## 6 · MEDIUM · unit 18 — §1's own count is left wrong in the section this unit rewrites

**Claim.** Unit 18 edits two of protocol §1's bullets and fixes the analogous count defect one file
over, but leaves §1's "Three properties" standing over four bullets.

**Evidence.** Verified in both halves of the pair: `memory/guides/UNATTENDED-PROTOCOL.md:19` and
`tools/unattended/PROTOCOL.template.md:19` read "Three properties, all mechanical:" and are followed
by FOUR bullets — asserted · reachable · SHAPE · ROSTER. Unit 18's S12 rewrites the fourth of those
bullets ("§1's roster bullet stops reading opt-in by presence"), AC9 greps `Opt-in by presence` to
zero, and §4's file table lists §1 as taking three separate edits. One file over, S9 and AC8 fix the
mirror-image defect: "the `verb_resume` comment at `tools/unattended/unattended.sh:909` says the
authored region carries five facts against the protocol's seven" (confirmed at `:909`).
`spec/2026-08-14-spec-cBriefedPilot-16.md` §8 RESOLVED makes the standard explicit — an index that
omits its own bullet is "the same class as the driver comment saying five facts where the protocol
pins seven — a defect unit 18 is already fixing in this build".

**Consequence.** The build ships its own count-versus-enumeration standard, applies it to a comment in
the driver, and leaves the binding contract's first enumeration off by one in the exact section this
unit is rewriting. Unit 22's arms D and E join §3 and §4 only, so no leg will ever red on it. A reader
who counts three and stops has stopped before the roster bullet — the bullet P3 makes mandatory.

**Edit.** Add to S12: "the §1 preamble reads *Four properties, all mechanical*." Extend AC9 with a
second clause observing that §1's stated count equals the number of bullets that follow it, in both
halves of the pair.

---

## 7 · MEDIUM · README — the M2 classification block is stale and no unit re-derives it

**Claim.** The master overview still says eighteen units are MISSING with no conforming spec, while
all twenty-two conforming specs exist.

**Evidence.** `README.md:40-42`: "Four units are READY and specced: units 2, 3, 9 and 10 … The other
eighteen are MISSING: declared as backlog rows, no conforming spec yet", and the Units table's `State`
column repeats MISSING on eighteen rows. The `spec/` directory holds twenty-two conforming files and
the README's own generated region at `:293-319` links all twenty-two. `README.md:49` — "**Next
action.** Spec unit 1, then unit 21" — is stale for the same reason. Unit 20's S1-S6 covers dossiers,
backlog rows, `memory/DECISIONS.md` and `AGENTS.md`; it does not touch the README, and
`gen_build_index.py` rewrites only the generated region between the markers.

**Consequence.** BUILD-METHOD M7 step 2 sends a regrounding or post-compaction run to read the build's
authored record whole, and M2's Act rule says MISSING → author the spec. A run that trusts the README
re-authors specs that already exist — which M2 names as "how a spec set stops agreeing with itself" —
or, reading the table instead, re-opens the units the 2026-08-15 sweep resolved. Nothing gates README
prose, so this survives a green bar indefinitely. Under an unattended run there is nobody to notice.

**Edit.** Re-derive the classification block and the `State` column against the tree in the same commit
as unit 7's roster edit — READY for the resolved units, FORKED for unit 15, and the recorded park for
unit 5 — and replace the "Next action" line. Add the re-derivation to unit 20's scope as a new S, so
it happens again at close rather than once by hand.

---

## 8 · MEDIUM · unit 3 — the empty-waive re-preflight is unstated

*(Raised as a BLOCKER wedge and refuted; reinstated at MEDIUM. The refutation was right that this is
recoverable and that the block is scoped to `--waive`-carrying invocations by inference. It is the
inference, and the unwritten recovery, that remain.)*

**Claim.** Refusal 2 is defined as "a run-state file already exists AND the requested set differs from
the recorded one", and nothing states what an EMPTY requested set does — which is the ordinary shape
of the pre-close re-preflight.

**Evidence.** `spec/2026-08-14-spec-cBriefedPilot-3.md` S2 refusal 2 and AC5, which covers exactly two
cases, byte-identical and DIFFERING. `spec/2026-08-14-spec-cBriefedPilot-5.md` §4 makes a second
`--preflight` mandatory before every `--close`, and source confirms why: `splice` has exactly one call
site, `unattended.sh:846`, so `--preflight` is the only writer of the generated region that
`records-current` diffs. Unit 10's S4 carries the confirmed pairs into "the preflight invocation" —
singular; no spec tells the agent to repeat the pairs on a later one.

**What the refutation established, and is correct about.** Refusals 1, 3, 4 and 5 all presuppose a
`--waive` pair, so the block is necessarily scoped to an invocation carrying one — refusal 1 read
unscoped would make every `--status` refuse. AC4 spells refusal 1 with "when `--waive` is PASSED",
AC5 spells refusal 2 with "when a DIFFERING set is re-run", and §4's ordering sentence has `--waive`
as its grammatical subject. So the correct reading is available, and even under the wrong reading the
refusal is above the write barrier, leaves the file byte-identical, and names itself.

**Residual consequence.** The safe reading is reachable only by inference across four sibling clauses,
and the recovery from getting it wrong — re-invoke `--preflight` with the recorded handles, which
passes refusal 2 as a matching set — is written in no spec and in no Skill step. Unit 10 S4 hands the
pairs to one invocation. A run that takes the literal reading is refused at the re-preflight, cannot
refresh the generated region, and meets an unmet `records-current` at `--close` with nobody present;
it spends an override on an item that is telling the truth about nothing.

**Edit.** One clause in S2 refusal 2: "the comparison runs only when the invocation carries at least
one `--waive` pair; an invocation naming no handle leaves the recorded set untouched and is not a
refusal." Add an AC observing a re-preflight with no `--waive` over a live record carrying two
waivers. In unit 10's S6, add that a re-preflight after compaction re-issues the recorded pairs.

---

## 9 · MEDIUM · unit 13 — check 17's selector never meets a line the driver wrote

**Claim.** Check 17's waiver selector is exercised only against hand-authored fixture lines, which is
the cross-component gap `TOOL-aStandingWrit-8` already names and unit 13's §10 does not cite.

**Evidence.** Unit 13 S1 selects "every line carrying the parked waiver grammar ` waiver · item `
followed by ` · reason `", and S7 puts every arm in `tools/unattended/check-unattended.test.sh` with a
hand-authored committing fixture. Unit 3's S6 arms all live in the other self-test,
`tools/unattended/unattended.test.sh`. `memory/backlog/TOOL.md:24`: "`TOOL-aStandingWrit-8 · OPEN · the
unattended kit has driver arms, leg arms and Skill-parity arms and ZERO arms that run the driver and
THEN the leg over the same tree; one cross-component fixture would have caught both halves
disagreeing`". Unit 13 §10 cites four seams — check 13's blob read, the per-file loop, `park()`'s kind
discriminator, check 13's comment — and not this row.

**What limits the severity.** The grammar is fixed by existing source, not spelled twice: `park()` at
`unattended.sh:995` already writes `printf '\n%s %s · item %s · reason %s\n'`, and unit 3's S3 only
supplies a new kind token into that shape. So a divergence needs an edit to `park()` itself.

**Residual consequence.** S4's git join is the half that is genuinely unproven end to end. It reads
"the whole line, byte for byte" out of the first committed blob, and whether that line exists in that
blob depends entirely on unit 3's S4 placement — `park()` after `set_fact`, before `stage_or_fail` —
which no arm in unit 13's set exercises. If the two disagree, both self-tests stay green and check 17
selects nothing: the repo's own `vacuous-selector-empty-population` class, silent by construction,
landing on the one check the owner bought at Tier 2 under P1.

**Edit.** Unit 13 S7 adds one arm whose waiver line is PRODUCED by invoking
`unattended.sh --preflight <slug> --keepalive-id <id> --waive <handle> --reason <text>` inside the
fixture and then committing, rather than hand-written, and anchors AC4 (the silent-when-present arm)
and the S4 join arm on that line. Cite `TOOL-aStandingWrit-8` in §10 as the row this arm partially
retires.

---

## 10 · MEDIUM · units 3 and 6 — unit 3's five check numbers are unallocated, and unit 6's is absolute

**Claim.** Unit 3 adds five `fail` branches and assigns none of them a check number, while unit 6
hard-states 37 from an arithmetic that counts only unit 4.

**Evidence.** `spec/2026-08-14-spec-cBriefedPilot-3.md` S2 lists five refusals, §4's file table says
"five refusals", S7 raises `ARMS_FLOORS` "by the number of branches this unit adds", and AC6 says each
is observed RED — no check number appears anywhere in the spec. Unit 4's S2 claims 34 and shows its
work: "the driver spells 1 through 33, 35 and 36". Unit 6's S4:22 claims "check number 37 — the next
free number after unit 4 takes 34, which is the driver's only gap today", and AC2 and AC5 both name
"check 37" as a specific observable. Measured against `tools/unattended/unattended.sh`, `fail` is
spelled 1-33, 35 and 36, so 34 is the only gap and 37 is the next free — *before* unit 3's five
branches exist. Unit 6's own rev-2 log states the `ARMS_FLOORS` move relatively "as every sibling that
raises the same floor already states it: units 3 and 4 add six branches to this file ahead of this
unit, so the absolute pair this spec named was stale before it could be read" — the same reasoning,
applied to the floor and not to the check number four lines above it.

**What limits the severity.** Number reuse is the driver's norm, not a hazard: measured, `fail 4`
appears 3×, `fail 9` 4×, `fail 10` 5×, `fail 20` 4×. And the one row in
`memory/project/unarmed-branches.txt` is check 9 ordinal 1 at `:551`, above `verb_preflight`, so
unit 3's branches cannot move it.

**Consequence.** Unit 3 lands first. A builder numbering its five refusals the way units 4 and 6 both
did — measure the gaps, take the next free — takes 37-41, and unit 6's stated number is consumed and
its arithmetic false at the moment it is read. Unit 6's AC5 ("the check-37 branch is observed RED with
its arm in place and its branch removed") then names an ambiguous branch, and AC2 ("`--plan` refuses
with check 37") can be satisfied by the wrong one. This is the same staleness unit 6's rev-2 already
caught once for the floor and left standing for the number.

**Edit.** Name the five numbers in unit 3's S2 — "the five refusals take check numbers 37 through 41;
34 is unit 4's and is the driver's only gap today" — and restate unit 6's S4 relatively, the way its
own `ARMS_FLOORS` sentence already is: "the next free number after units 3 and 4 have taken theirs,
measured against the driver at the time this unit is built", with AC2 and AC5 naming that number
rather than a literal.

---

## Findings I believe the skeptics refuted correctly

I re-derived the load-bearing source claim behind each refutation that turned on one, and found none
refuted wrongly on the merits. Three are worth recording because they were close, or because the
refutation itself is a fact the build should keep:

- **The `State` column "outside the markers" (unit 7).** Raised three times independently, by three
  different agents, and refuted three times on the same correct ground: §8's resolution names the
  outcome in its own rationale ("the column it REMOVES is a third spelling of a state already derived
  twice") and Option A's body says "or is dropped". The refutations are right that the instruction is
  determinate to a builder who reads §8 whole. But a sentence that three careful readers construed as
  unbuildable is a sentence worth one edit anyway. **Suggested, not a finding:** delete the stale
  conditional from S6 ("under the recommended Option A the `State` column moves outside the markers,
  under Option B the table is enclosed as authored") and replace it with the resolved instruction —
  the marker pair encloses the plan columns; `State` is dropped. Cost: one line. It is the cheapest
  defect-shaped thing in the set and it is not a defect.

- **Unit 13's `core_of` vs the effective set.** Refuted on a source claim I verified:
  `check-unattended.sh:64-83` shows `core_of` parsing a `KEY="…"` line out of `$DRIVER`, and the leg
  composing `PHASES="$PHASES_CORE $PHASES_EXTRA"` at `:82-83`. `DIRECTIVES_EXTRA` is a conf key and is
  not a shape `core_of` can match, so "the effective set, read through the same `core_of` parse arm A
  uses" is coherent and describes the only construction available. Correct refutation.

- **Unit 2's init-line arm discriminator.** Refuted with the observation that "read but never assigned
  in this file" separates a conf key from a kit constant with no hardcoded key list. Verified: every
  global the finding named as indistinguishable is assigned in the driver (`M` at `:64`, `PHASES_CORE`
  at `:73`, `ROSTER_OPEN` at `:94`, `TB` at `:273`, and so on), while a conf key the driver reads and
  does not default-init is by construction never assigned — which is exactly what aborts it under
  `set -u`. Correct refutation, and the discriminator is worth carrying into unit 2's builder note.

One finding below appears in both lists by my own choice: **the empty-waive re-preflight** (§8 above)
was refuted as a BLOCKER wedge and I have reinstated it at MEDIUM. The refutation is right that the
wedge does not hold and that the correct reading is inferable. It is wrong only in treating "inferable
from four sibling clauses" as equivalent to "written", on the one branch this design says carries its
whole ordering guarantee.

## What a further pass would and would not buy

**This set is hardened.** 41 raw findings collapsed to 10 distinct defects and no blockers, against a
spec set that has already absorbed a nine-agent panel, a three-lens cross-read and a fork sweep. The
refutation rate is the tell: 29 of 41 died against source, and the three most-repeated findings in
this pass (the `State` column, the unit-19 grep, the unit-3 check numbers) were each raised by
multiple agents converging on the same three sentences — which is what a corpus looks like when the
remaining surface is small enough that independent readers keep landing on it.

REVIEW-PROTOCOL says to stop once a synthesis calls a design clean. **This one does.** A further
design pass over these 22 specs would manufacture noise: the ground that is left is authorial
preference over resolved forks, re-litigation of the five owner decisions, and wording-precision
complaints about sentences whose meaning is fixed three paragraphs down. Four of the refutations above
are already that shape.

What a further pass *would* buy, and the only thing it would: nothing here has been read by a builder
who then tried to build it. Eight of the ten findings are of the form "the spec's own mechanism cannot
execute where the spec puts it" or "an acceptance criterion is false against the tree" — the class
that surfaces on contact with the file, not on contact with another reader. The next real signal comes
from unit 1 and unit 2 landing, not from an eleventh lens. Fold these ten edits, and build.
