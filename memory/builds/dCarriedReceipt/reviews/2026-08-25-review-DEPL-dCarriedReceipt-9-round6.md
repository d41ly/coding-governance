# Pre-code review, round 6 — part 2 of 2, the receipt and reach units, DEPL-dCarriedReceipt-9..15

**Serves:** spec-audit DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15

**Reviewed:** all 15 specs plus the build README, against the round-5 fold at `1d19b58b` and the
reproduction record at `7ef2a60a`. **Base:** `7ef2a60a`.
**Harness:** four primed finder lenses over the fold diff (fold fidelity, fold collateral, citation
integrity, convergence), then batched default-refute skeptics, then one synthesis. Ten agents, all
returned. Sixteen confirmed entries arrived; deduplicated they are 12 distinct defects across both
parts, and 12 were refuted.
**Why two parts:** the Serves id list renders into one build-README row and 15 ids blow its entry
cap. That is DEPL-dCarriedReceipt-16; rounds 1, 4 and 5 split on the same boundary.

This record carries the convergence answer and the findings against units 9-15 and the build
README. Units 1-8 are part 1, `2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md`.

## Verdict: CLEAN WITH FIXES

Zero blockers, twelve defects, all of them stale prose with a written edit.

## The convergence question, answered

**Yes. The 15 specs describe one build, and the receipt converges.**

Round 4 said the specs described one vocabulary and one order but not one receipt. Round 5 said the
distance had closed from four seams to one field set — the `merged` row `cmd_apply` writes at
`:2417`, whose identities no spec stated. That field set is now closed, and closed properly:

- `-7` §8 F4 is RESOLVED to Direction A, with the reasoning pointed at rather than restated.
- `-7` S1 names the third channel and gives the row its field set: `source` and `commit`, neither
  identity.
- `-7` S9 carries the exemption by ROLE as its own fourth item, placed before the exactly-one
  refusal it would otherwise trip, and says why it reads `role` rather than `evidence`.
- `-13` S11 states the choice explicitly instead of inheriting it, and names F4 as the ruling.
- `-7` AC11 runs `update` over a `push-main` fixture and asserts the merged row does NOT refuse,
  with its RED arm staged by removing the `merged` arm. The exemption is observed, not assumed.

**And the ruling stopped resting on a reading.** B1, B2 and H2 were all derived from `govkit.py` and
two kit descriptors, never run. The fold's own follow-up commit reproduced them: a scratch repo,
`intake --kits push-main`, then `apply`, yielding six rows. The merged row for `.githooks/pre-commit`
carries `commit` and not `gov_oid` — exactly one of the two, on a receipt this tree's own kit
produces on a first apply. The same run corrected how H2 had been argued: four of six rows carry
`sha256` and `install.sums` is 333 bytes over those four, so the sidecar is non-empty for a normal
apply and the zero-byte failure is specific to `adopt` omitting the field. A round that both ratifies
a fork and then goes and runs the thing it ratified against is the behaviour this build wants, and it
is why the convergence answer can be yes rather than "yes on the reading we have".

Every row class `cmd_apply` produces now has a named writer and a stated field set somewhere in the
set, and `adopt` writes the same classes. What is left is bookkeeping: **six of the twelve defects
below are one document failing to carry a ruling another document already made.** That is a
different kind of problem from the one this loop opened with, and it is the kind that ends.

**No blockers.** Nothing below is an owner fork, nothing makes a criterion unbuildable, and nothing
stops a run at build time. The single High is a false argument in a spec that does not own the rule
it argues about.

## Did the round-5 fold hold?

**Yes, on every edit it declared, and it declared its own collateral again.** All three of B1's owed
items landed — `-13` S11 states the choice, `-7` AC11 observes the exemption, and the S9 sentence
Direction A itself flagged as its one follow-up was narrowed. The fold also found and fixed a defect
outside the finding set: `-13` §8 F5's mark read `RESOLVED (agent, 2026-08-25, round-4 fold)`, which
`TEMPLATE-SPEC` does not allow, so that mark had resolved nothing and left `-13` FORKED. All 39 marks
across the set now conform and `--plan` reads all 15 READY. And the commit message states plainly
what was still unreproduced at the time it was written, rather than letting a green record imply
otherwise.

**Two edits landed in one copy where the set holds two, and both are findings below.**

- **B1's S9 narrowing landed in `-7` and not in `-12`.** The fold's own `-7` §9 rev-6 entry records
  it: "S9's own 'not by `role` or by `evidence`' sentence is NARROWED rather than left standing
  beside its exception". `-12` §4 carries the same argument in stronger form, unedited, and `-12`
  lands FIRST. That is H1.
- **H1's skip rescoping reached three specs in round 5 and the README in this fold, but not `-7` §5
  or `-13` S7's own sequencing clause.** Two copies of the pre-H1 reading survive. That is L2.

**One fold edit is a verbatim carry of a finding's own error.** `-13` AC10's `sha256`-filter
enumeration says three call sites because round-5 H1's finding text said "all three call sites".
There are four. The fold applied the wording rather than re-deriving the count, which is the same
mechanism that produced round 5's blocker — M4's two-channel enumeration landed verbatim and the tree
had three. It is L4 here, and low rather than high only because the four sites are copies of one
expression.

**One fold edit inherited a wrong attribution from the review record that specified it.** Round 5's
Direction A text credited `-8` with keeping `block_sha256`; `-8` never mentions the field. The clause
went into `-7` S1 verbatim and is now the justification sentence for the ratified direction. That is
L3.

**And the fold created one new instance of a class it had just fixed.** Round 5's M2 was "`-13` AC6
does not name its fixture's role"; the fold fixed it in `-13` and left the identical shape in `-7`
AC10, which the same fold made role-sensitive by adding AC11. That is L1.

## This is the LAST round, and the loop had already arrived

The owner's instruction on 2026-08-25 was to stop converging after this round and get to building.
It costs nothing here, because the loop reached its own exit in the same breath: blockers went
3 (round 4) -> 1 (round 5) -> **0**, and the convergence question is answered YES for the first
time. The build method's loop is bounded by blockers, and there are none.

The twelve defects below are therefore folded and NOT re-reviewed. Every one has a written edit,
none opens a fork, none makes an acceptance criterion unbuildable, and none stops a run. Six of the
twelve are one document failing to carry a ruling another document already made -- which is the
cheap kind of wrong, and the kind that ends.

Rounds are recorded for every subject that still had an open loop. `-12` is the exception and it is
worth naming: H1 lands on `-12`, whose loop closed at round 5 with zero blockers, and `--review`
refuses a further round for a subject already terminal. So H1 is folded without a round, which is
exactly the tension `TOOL-dCarriedReceipt-2` was filed for.

## High

**H1 — `-12` §4 still argues that `-7` S9 CANNOT be scoped by role, which is the argument S9's new
arm rebuts, and `-12` is the spec a builder meets first.**
*Unit `-12` §4, ordering-table prose (:106-112). Against `-7` §2 S9 (:82, :105-110) and §8 F4
(:294-303). Provenance: this fold's own B1 narrowing.*

`-12` :107-111 reads: "That is precisely why `-7` S9 is scoped by FIELD PRESENCE rather than by
`role` or by `evidence`: an unattributed row carries neither field … Scope S9 by role instead and it
would have to know a classification that has not happened yet."

Both halves are now false, and `-7` says so in terms. S9 :82 reads "It is SCOPED BY FIELD PRESENCE,
in three arms, plus one exemption by ROLE", and :105-110 answers `-12`'s argument by name: "`role` is
on every row `apply` and `adopt` write, so the arm needs no later precondition to have run, while
`evidence` is `-13`'s field and is exactly what the in-loop skip keys on."

Verified in source rather than inferred: `role = row.get("role", "engine")` at `govkit.py:2973` is
read from the row itself, one line BEFORE `how = UPDATE_ROLE.get(role)` at `:2974`. A preamble arm
reading `role` needs no classification to have run, because `role` is stored, not derived.

The paragraph carrying this is the one `-12` itself flags as "load-bearing rather than arbitrary, and
the first is easy to get backwards", and `-12` is README step 2 while `-7` is step 3. So a builder
reads an emphatic argument that Direction A is impossible, then reads Direction A. This is not the
under-description class — it is not silence about the exemption, it is an assertion that the
exemption cannot exist.

**Edit.** Rewrite `-12` :108-111 to the narrowed reading. Replace "scoped by FIELD PRESENCE rather
than by `role` or by `evidence`" with *"scoped by FIELD PRESENCE rather than by `evidence`"*, and
replace "Scope S9 by role instead and it would have to know a classification that has not happened
yet" with *"Scope S9 by `evidence` instead and it would have to know a classification that has not
happened yet — `evidence` is `-13`'s field and is exactly what step 6 keys on. `role` is different:
it is on every row `apply` and `adopt` write and is read at `:2973` before the dispatch resolves at
`:2974`, which is why S9's one exemption by ROLE (`-7` §8 F4) needs no later precondition and does
not re-open this ordering."* Leave the "scope it by nothing" clause and the 41-row measurement
untouched — both are correct and neither is about `role`.

## Medium

**M4 — `-13` §4's Data model still says every written row carries `sha256`, `gov_oid`, `oid` and
`evidence`, which the same fold declared false for S11's two synthesized classes.**
*Unit `-13` §4 Data model (:183-186). Against §2 S5 (:59-63) and §2 S11 (:151-153). Provenance: this
fold's own S5 and S11.*

§4:183-186, untouched by the fold, reads: "Each written row carries the receipt shape `apply` already
produces at `:2458-2460` — `path`, `role`, `kit`, `version`, `sha256`, `source`, `commit` — plus
`-7`'s `gov_oid` and `oid`, `-9`'s `carry`, and this unit's `evidence`. `evidence` takes exactly
`\"apply\"`, `\"vintage-match\"`, `\"pinned\"` or `\"unattributed\"`."

The fold then wrote two sentences that contradict it, both in normative scope items. S5 (:61-63):
"S11's two synthesized classes do not — `apply` gives neither the `attributes` row at `:2350` nor the
merged row at `:2417` a `sha256`, and `adopt` matches that — so neither appears in `install.sums`."
S11 (:151): "Neither synthesized class carries `evidence`, and neither carries `gov_oid` or `oid`."

Four fields §4 declares universal are absent from two of the four classes the unit writes, and
`evidence` gains a fifth state — key absence — that §4's closed enumeration excludes. Taken
literally, §4 puts the synthesized rows into `install.sums`, which S5 forbids by name. Source and the
reproduction agree with S5 and S11, not with §4.

The appositive "the receipt shape `apply` already produces at `:2458-2460`" does scope the sentence
for a careful reader, and that is why this is medium rather than high. But §4 is the unit's data
model and the place a builder reads the row shape from, and conflating absent-`evidence` with
`evidence: "unattributed"` is precisely the destructive reading S7 spends a paragraph closing off.

**Edit.** Scope §4's first sentence and point at S11 for the rest: *"Each DESTINATION row — the rows
S1–S7 describe, built from `resolve_entry`'s two channels — carries the receipt shape `apply` already
produces at `:2458-2460` … and this unit's `evidence`. S11's two synthesized classes carry none of
`sha256`, `gov_oid`, `oid` or `evidence`; S11 states each absence and why, and this table does not
restate them."* Then amend the enum sentence to *"`evidence` takes exactly `\"apply\"`,
`\"vintage-match\"`, `\"pinned\"` or `\"unattributed\"` on every row that carries it, and is ABSENT
on S11's two classes — absence is the fifth state and is NOT a synonym for `\"unattributed\"`, which
is what S7's skip keys on."*

## Low

**L4 — `-13` AC10 names three of the FOUR sites applying the `sha256` filter, and the omitted one is
the sidecar write that runs on every clean `update`.**
*Unit `-13` §6 AC10 (:350-353). Provenance: round-5 H1, whose finding text said "all three call
sites".*

AC10's folded predicate: "one line per row that carries a `sha256` — the filter the writer at
`:2828-2830` applies, `cmd_check`'s join re-applies at `:1551` and `cmd_update` re-applies at
`:3117-3119`."

Grepped `"sha256" in` across the source: four sites. `:2829` (`cmd_apply`'s sidecar write), `:1551`
(`cmd_check`'s `want_pairs` join), `:3118` (`cmd_update` under `if r.problems:` at `:3115` — the run
that HAD findings) and `:3129` (`cmd_update`'s clean re-stamp, after `receipt["gov_commit"] =
to_commit` at `:3126`). The two `cmd_update` expressions are byte-identical, and the omitted one is
the routine path: `:3117-3119` runs only when the update reported problems, `:3128-3130` runs on
every successful update and produces the sidecar an adopter actually ends up holding.

An enumeration presented in an acceptance criterion as the complete set of places the filter lives,
naming the exceptional write and dropping the normal one, is the could-not-be-checked shape this
build files against elsewhere. S5's new "so neither appears in `install.sums`" depends on all four
agreeing, and a filter changed at three trips both `r.fail` arms at `:1552-1555`.

**Edit.** In AC10 replace "and `cmd_update` re-applies at `:3117-3119`" with *"and `cmd_update`
re-applies at BOTH its sidecar writers — `:3117-3119` on a run that had findings and `:3128-3130` on
the clean re-stamp — four sites in all, and a filter changed at three of them reds `cmd_check`'s join
at `:1552-1555`"*.

**L5 — `-9` §10 still summarises the derivation as reading the receipt after this fold rewrote S3 to
take a sequence of pairs.**
*Unit `-9` §10 Reuse audit (:415-419). Against §2 S3 (:41-48). Provenance: this fold's own M4 edit.*

S3 now reads: "`alpha` is DERIVED, never authored, and the derivation takes a SEQUENCE OF PAIRS
rather than a receipt, because it has two callers." §10:415, untouched, still reads "`alpha`
therefore reads the receipt, which is the only record of what was taken".

Round 5 read §10 as already correct and filed M4 against S3 alone; after the fold the polarity is
reversed and the two sentences answer one question two ways. §9 rev-7 records M4's motive precisely:
"a builder read it and wrote a helper taking receipt rows, which `adopt` has none of" — and §10:415
is the surviving sentence with that reading. The paragraph self-corrects two clauses later by naming
both callers and `adopt`'s planned pairs, which contains the damage and keeps this low, but does not
remove the contradiction. Same one-sentence-left-behind shape M4 itself filed, one document over.

**Edit.** In §10 (:415) replace "`alpha` therefore reads the receipt, which is the only record of
what was taken" with *"`alpha` therefore reads what its CALLER supplies rather than re-resolving the
descriptors — the receipt from `cmd_update`, since it is the only record of what was taken, and the
run's own planned pairs from `adopt`, which has no receipt yet (S3)"*, leaving the rest intact.

**L6 — `-14` S4's new `not-run` state is unscoped, where §5 and AC6 both bound it to CLAIMED kits.**
*Unit `-14` §2 S4 (:49-53). Against §5 observability (:150-152), §5 perf (:142-143), §5 security
(:140-141) and §6 AC6 (:192-197). Provenance: round-5 M5, first option taken.*

The fold declared the state in the scope item that owns it. S4 now reads "Such a kit is printed once
as `not-run` and counted under its own tally", where "such a kit" resolves to the preceding
sentence's "A kit the run did not touch" — unbounded. Everywhere else it is bounded: §5 observability
says "one `not-run` line per CLAIMED kit the run did not touch", §5 perf says "per untouched claimed
kit", §5 security says "It stays bounded to kits the receipt claims", and AC6's fixture "claim[s]
three kits".

A builder implementing S4 as written prints a `not-run` line for every registry entry the target does
not claim. `cmd_update` already prints exactly those at `:3027-3032` as "available (not installed)",
with a paragraph explaining why `update` does not touch them — two answers to one question, in the
output of the verb built to end silent partial installs.

Second, smaller: AC6 says "the tally NAMES the other two kits as `not-run`", while §5 splits the two
outputs — a `not-run` LINE per kit and a `not-run` COUNT among five tallies. AC6 is satisfiable under
a loose reading of "tally", but one output now has two spellings.

**Edit.** In S4 change "Such a kit is printed once as `not-run`" to *"A CLAIMED kit the run did not
touch is printed once as `not-run` and counted under its own tally; an unclaimed registry entry is
not one of these — `cmd_update` already prints it as `available (not installed)` at `:3027-3032`, and
a second line about the same kit is two answers to one question."* In AC6 change "the tally names the
other two kits as `not-run`" to *"the other two claimed kits each print one `not-run` line and the
`not-run` tally reads 2"*.

**L7 — the build README's architecture paragraph carries no trace of the merged-row exemption this
fold ratified.**
*Build README (:40-59). Against `-7` §8 F4 (:294-303), §2 S1 (:45-49) and §2 S9 (:95-100).*

Grepped: the README contains zero occurrences of "merged". The fold edited this paragraph — :53-55
took round-5 L3's skip-ordering correction — and ratified, in the same commit, the only design
decision this round produced. The paragraph still opens "A receipt row … carries **two identities**"
and closes "`oid != gov_oid` **is** the local-delta predicate, so no stored flag can go stale behind
it", with no row class carved out of either.

That sentence is not incidental to the ruling; it is why Direction B was discarded. The round-5 fork
resolution turns on it: Direction B "makes a whole row class read as carrying a local delta forever,
which does not fail an acceptance criterion but falsifies a ratified sentence", the sentence being
README :55-56. Direction A protects it by leaving the merged row with NEITHER identity, so the
predicate is undefined there rather than permanently true. A reader of the architecture of record
cannot tell that a row class sits outside the two-identity model at all — and this paragraph already
carries its other carve-outs by name, since role `forked` is spelled out as report-only and the
unattributed state as "no `commit`, no `gov_oid`".

The README's `deps` cell, its landing-order step 5 and its skip ordering were all brought forward by
this fold. The architecture paragraph was the one place it edited without carrying the ruling in.

**Edit.** After :55's clause, insert: *"One row class sits outside that model by construction. Where
gov owns a BLOCK inside a file the target owns — role `merged` — there is no whole-file gov blob to
hash, so the row carries neither identity, the delta predicate has no operands, and its drift is the
block hash's business. It is exempt from the integrity preamble by ROLE, which is the one place that
preamble is not scoped by field presence (`-7` §8 F4)."* No line citations, keeping the README's
architecture prose free of source pins as its own L3 edit established.

---

## What the fold got right

- **B1's three owed items all landed, and one of them landed better than asked.** The record said an
  acceptance criterion should observe the exemption; the fold put it in `-7` rather than `-13`, on
  the reasoning that the refusal and the exemption are `-7`'s and `-7` lands two steps earlier, so a
  criterion firing only at `-13` would leave `-7` landing an unarmed exemption. That is the right
  call and the record did not make it.
- **The one follow-up Direction A left open was paid in the same pass.** S9's "not by `role` or by
  `evidence`" sentence was narrowed and given a reason, rather than left standing beside its own
  exception. It is only H1 because a second copy lived in `-12`.
- **It reproduced its own ruling.** B1, B2 and H2 had all been argued from source reading. The
  follow-up commit ran `intake` then `apply` against a scratch repo, put the six-row table on the
  record, confirmed B2, and CORRECTED how H2 had been argued — `install.sums` is 333 bytes over four
  rows on a normal apply, so the zero-byte failure is specific to `adopt`, not general. A fold that
  goes and falsifies its own supporting argument is the behaviour §7 asks for.
- **It said what it had NOT established.** The commit message states that no arm, gate or
  `refusal_join.py` branch has observed the refusal either way, and names `-7` AC11 as the first
  thing the build owes. A green record that declines to imply coverage it does not have.
- **It found and fixed a defect outside the finding set.** `-13` §8 F5's mark used a third field
  `TEMPLATE-SPEC` does not allow, so it resolved nothing and left `-13` FORKED. All 39 marks now
  conform and `--plan` reads 15 READY.
- **Five specs and the README moved sequentially rather than in parallel**, because the round-4
  dispatch declarations never closed (`TOOL-dCarriedReceipt-3`). An unprovable disjointness got
  sequenced instead of assumed, which is why this round has no fold-collision findings at all.
- **`-13` S11 points at source literals rather than re-typing key sets**, and `-13` S5 states the
  `install.sums` split once beside F5 rather than in both places. Both are the form this build
  prefers, applied without being asked.

## What remains unverified

- **The merged-row refusal has still never been RUN.** The reproduction observed the row SHAPE that
  would trip it — `commit` present, `gov_oid` absent — on a receipt this tree's own kit produces.
  It did not observe a refusal, because `-7` S9 does not exist yet. Direction A's exemption is an
  unexercised design decision, and `-7` AC11 is the first thing its build owes. A gate whose failing
  case has never been staged is an assertion about nothing, and this one is specified rather than
  observed.
- **The AC13/AC14 fixture family exists only as a `-13` §4 estimate.** Round 5 flagged this and it is
  unchanged. Several findings across the last two rounds turn on which fixture a criterion runs over,
  and the answer is currently in a section headed "(estimate)". No `seed` rule is named there while
  AC14 needs an unattributed `seed` row. This resolves when the arms are written, not before.
- **No acceptance criterion observes the four-producer set as a set.** M1's fix makes `-7` S1 name
  all four, and the reproduction record shows all four on one receipt, but nothing asserts that a
  future `cmd_apply` change adding a fifth producer reds anything. The receipt row-class population
  is documented, not gated.
- **`-7` AC11's exit-0 claim depends on `-2` landing first, and that dependency is not stated in
  `-7` §3.** M3's edit adds it. Until then the criterion is correct and its precondition is recorded
  only for the other fixture.
- **The inCMS figures — 41 unattributable rows, 13 `project-owned`, 11 carried — are carried forward
  from `-9` §4 and `-13` §4 and were not re-measured this round.** They are load-bearing in `-12`'s
  "scope it by nothing" argument and in S7's disposition-deletion count. No finding depends on them
  and none contradicts them.
- **`-13` §4's `sha256` narrowing was verified in prose but not against a carried row.** F5 says the
  field hashes the target's bytes; the reproduction ran `push-main`, which produces no `eol` or
  `relocate` row, so the case where gov's blob and the target's bytes differ is still unobserved.
