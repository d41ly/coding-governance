**Serves:** spec-audit DEPL-dSealedTally-1 DEPL-dSealedTally-5

# Spec audit round 3 — dSealedTally

Tier-2 · node d · 2026-09-04 · a re-audit of the two units the rev-3 fold amended, before either
opened for building.

**ROUND 3** over two subjects, each pinned at the blob it was read at:
[DEPL-dSealedTally-1](../spec/2026-09-04-spec-DEPL-dSealedTally-1.md)@`76854deec80f` ·
[DEPL-dSealedTally-5](../spec/2026-09-04-spec-DEPL-dSealedTally-5.md)@`3c0fba713d17`.

## Verdict: BLOCKED

Four blockers stand. Two of them are the fold's own damage rather than a bad idea: rev-3's edit to
`DEPL-dSealedTally-1` §6 swallowed AC6's bullet head, so the unit's only staged-break criterion now
names no subject and can be satisfied by mutating anything at all. The other two are mechanism.
`DEPL-dSealedTally-1` S2 moves the landing block whole, which carries the block's own
`unclaimed sources:` summary print above the verify-and-rollback pass and makes S4's stated purpose
unreachable by S2's literal instruction. `DEPL-dSealedTally-5` S1 threads a `--to <pin>` through the
real-root `run()` helper, which re-stamps the receipt at the pin while an existing arm still asserts
that receipt equals `rev-parse HEAD` — so the fix reds an arm and contradicts its own AC1. And
`DEPL-dSealedTally-5` AC5 asserts the constant 9, which a substring grep produced by counting five
`gov_run()` calls §3 declares out of scope; the strict figure is 4.

The shape of this round is the shape of the last one, one revision on. Round 2 said the fold
"rewrote prose against the round-1 report rather than against the code the prose now names". Rev-3
did that again and added a new failure mode: it rewrote §2 and §6 of `DEPL-dSealedTally-1` without
re-reading the bullets it landed between, leaving two structural corruptions — a missing AC head and
a scope item spliced through the middle of another. Nine of the fourteen defects below are in text
that did not exist at rev-2. None of them changes what a unit is for, and all fourteen repairs are
cheap.

## Review shape

| Raw | Confirmed | Refuted | Unverified | Precision |
|---|---|---|---|---|
| 43 | 26 | 17 | 0 | 0.60 |

The 26 confirmed findings deduplicate to the 14 defects below — four separate lenses filed the AC6
corruption, four filed the S4/S7 splice, three filed the stale §10 reuse audit. Each entry lists the
raw ids it absorbs so nothing is lost. Precision 0.60 is inside the healthy band; the refuted half
was mostly missing-detail complaints against sections that are deliberately terse, plus three claims
about `govkit.py` behaviour that did not survive reading the code.

## Findings

| # | Sev | Subject | Address | Defect |
|---|---|---|---|---|
| B1 | blocker | DEPL-1 | §6, line 157 | AC6 has lost its bullet head and its subject |
| B2 | blocker | DEPL-1 | §2 S2 / S4 | the moved block's summary print lands above the rollback pass |
| B3 | blocker | DEPL-5 | §2 S1 / §4 | the real-root receipt assertion is not re-pointed at the pin |
| B4 | blocker | DEPL-5 | §6 AC5 / §4 Inventory | the pinned population figure 9 is a substring miscount; it is 4 |
| H1 | high | DEPL-1 | §2, lines 34-39 | S7 is spliced through S4, orphaning S4's tail below it |
| H2 | high | DEPL-1 | §2 S7 / §6 | S7 has no acceptance criterion |
| H3 | high | DEPL-1 | §2 S4 / §6 | S4 has no acceptance criterion |
| H4 | high | DEPL-1 | §2 S1 / §4 Files touched | the return-shape change breaks the read-only preview, unbudgeted and ungraded |
| H5 | high | DEPL-5 | §3, non-goal 2 | the excluded population is still declared as the refuted "32 of the 74" |
| H6 | high | DEPL-5 | §4 Data model, Rollout, Files touched | one threading site declared, and the vetoed apply-at-pin priced |
| M1 | medium | DEPL-1 | §4 Files touched | budgets a deleted mechanism and the arm shape AC5 forbids |
| M2 | medium | DEPL-1 | §10 Reuse audit | still cites the call site §2 declares unreachable on a write run |
| M3 | medium | DEPL-1 | §2 S7 | the two empty-`restored` fallbacks state something false on a landed-only rollback |
| L1 | low | DEPL-1 | §4 Inventory | S1's safety sentence was severed mid-clause by the fold |

---

### B1 — blocker · `DEPL-dSealedTally-1` §6, between AC5 and AC7 (line 157)

*Absorbs raw ids 1, 15, 26, 35.*

The rev-3 AC5 rewrite swallowed AC6's bullet marker and its whole opening clause. A grep for bullets
matching `^- \*\*AC` over the file returns AC1, AC2, AC3, AC4, AC5, AC7 — there is no AC6 bullet.
Line 157 is a bare indented fragment, "`tools/govkit/govkit.py`, the AC1 arm FAILS, recorded as an
observed staged break.", glued under AC5, whose own sentence already ended at line 156 on "the guard
has no hostile input to catch." At `d0c9bd4f` the lost head read: "**AC6** — When the `snap_rows`
append is removed by mutation in a scratch copy of".

The half that survived says an arm must go red. The half that was lost is WHAT gets mutated, which
is the load-bearing part of a staged break —
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md` records exactly that. As written, the
criterion is satisfiable by breaking any constant in the file. §5 leans on it ("S6's arm is the
left-shift; it fails before the change"), §7's DoD leans on it, and the charter's own
non-negotiable — a new gate is not landed until its failing case has been observed — is now
unspecified for this unit. AC7's arm-count delta of 6 is also stated against a criteria list with
five readable entries.

**Fix.** Restore AC6 as its own bullet with an explicit mutation subject, along the lines of "AC6 —
When the `snap_rows` append, or the `origin == landed` restore branch, is removed by mutation in a
scratch copy of `tools/govkit/govkit.py`, the AC1 arm FAILS, recorded as an observed staged break."
Re-check that AC5 ends at its own sentence and that AC7's delta matches the restored count.

**Left-shift gate.** A new numbered check in `tools/memory-tree/check-memory-hygiene.sh`: in any
tracked spec's §6, every `**ACn**` reference in the file resolves to a bullet head, the sequence is
gapless from AC1, and no non-bullet, non-continuation line follows a bullet block at bullet indent.
The same predicate run over §2's `**Sn**` catches H1 in the same pass. Run the candidate over the
whole `memory/builds/` tree before wiring it, printing hits AND near-misses — this defect class has
already produced two live instances in one file.

---

### B2 — blocker · `DEPL-dSealedTally-1` §2 S2 and S4 (and §4 Inventory)

*Absorbs raw id 24.*

S2 says the landing block "MOVES to sit between the write loop's end and `written_paths = ...` at
`tools/govkit/govkit.py:6806`", with no exception. The block's own summary print is part of it: the
landing loop ends at 7185 and 7187-7195 prints `unclaimed sources: {len(_landed_new)} landed` plus
one `landed <path>` line each. `written_paths` is at 6806 and the verify-and-rollback loop begins at
6808, so under the literal instruction that summary renders BEFORE any rollback can run.

That defeats S4 by placement. S4's stated purpose is that a rolled-back landing is removed from
`_landed_new` "so the summary does not report a landing that was undone" — but the summary has
already printed. The operator sees `unclaimed sources: 1 landed` and `landed <path>` for a file the
run then deletes, and the only later output is the rollback report. No section says the block splits,
and no AC reads stdout. Grepping all five dSealedTally specs, `_landed_new` appears only in this one,
so no sibling unit covers the print either.

**Fix.** Amend S2 and the §4 Inventory to say the block SPLITS: the decision-and-write half moves to
6806, above `written_paths = ...`, while the `unclaimed sources:` tally and its per-path lines at
7187-7195 STAY below the verify-and-rollback pass so they render the post-rollback `_landed_new`. Add
the split to §4 Files touched, and give it a criterion — the `landed <dest>` line is absent from the
AC1 run's stdout.

**Left-shift gate.** Extend the AC1 arm in `tools/govkit/selftest.py` to assert on stdout, not only
on the filesystem: after a forced-fail landed-only rollback, `unclaimed sources: 0 landed` and no
`landed <dest>` line. That is a regression gate for the CLASS "the run's summary reports an action
the run undid", which reaches every future verb that prints a tally beside a rollback.

---

### B3 — blocker · `DEPL-dSealedTally-5` §2 S1 and §4 (Data model, Files touched)

*Absorbs raw id 30.*

Threading `--to <pin>` through `run(*args)` makes every real-root `update --write` re-stamp the
receipt at the pin: `govkit.py:5670-5674` resolves `to_commit` from `--to`, and 7239 sets
`receipt["gov_commit"] = to_commit`. But `tools/govkit/selftest.py:583-587` asserts that
`rec["gov_commit"]` equals the stdout of `git -C <govroot> rev-parse HEAD`, and `govroot` at line 385
is `HERE.parents[1]` — the real checkout, not a scratch repo. It is reached through
`run("update", "--target", str(up), "--write")` at line 577, which carries no inline `--to` and is
therefore squarely in the group S1 pins.

On the detached `--no-ff` merge AC1 is measured on, PIN != HEAD by the unit's own premise. So the fix
itself reds the arm "and re-stamps the receipt at the new commit", and AC1's "it exits 0" is
contradicted by S1's own mechanism. Worse, the failure presents as a wrong-looking receipt assertion
rather than a vintage refusal, so a builder reads it as a new defect instead of as fallout.

**Fix.** Add a scope item: every arm comparing a real-root receipt's `gov_commit`, or a row's
`commit`, against `rev-parse HEAD` of `govroot` is re-pointed at the resolved pin. Enumerate that
population in §4 Inventory the way the `--to` population is enumerated — measured, with the command
spelled — and budget it in Files touched. Give it an AC so a future arm written against HEAD reds.

**Left-shift gate.** An arm in `tools/govkit/selftest.py` asserting that the count of `rev-parse HEAD`
comparisons against `govroot` is zero, or equals a declared pinned number, so the next arm added
against the moving ref fails at the bar rather than on the next detached head.

---

### B4 — blocker · `DEPL-dSealedTally-5` §6 AC5 and §4 Inventory (rows at lines 78, 84-85)

*Absorbs raw ids 2, 43.*

The replacement figure is a substring miscount. A `grep -c` for `run(.*"--to"` over
`tools/govkit/selftest.py` returns 9 because it also matches five `gov_run(...)` calls at 2721, 2736,
2739, 2745 and 2751, which drive a SCRATCH gov checkout — the first group §3 declares out of scope.
The strict count of `run()` calls carrying an inline `"--to"` is 4, at 3685, 3716, 3728 and 3747,
measured with a pattern anchored on a non-identifier character before `run(`. The full 13 `"--to"`
argument tokens split 4 in `run()`, 5 in `gov_run()` and 4 in `run_in_gov()`; `selftest.py` is
byte-identical between base `0f19429a` and HEAD, so the base figure is 4 too.

AC5 therefore asserts a constant that is wrong by 2.25x and that names, almost exactly, the group §3
excludes. An arm computing the figure strictly reds at base on a correct implementation. An arm
reproducing the spec's loose grep passes while counting two helpers, and so cannot detect a widening
confined to `run()` — the one thing AC5 exists to catch. This is rev-2's H2 defect recurring one
revision later: a number produced by an unstated method, sold as a measured one.

**Fix.** Correct the Inventory row to 4, state the measuring command that excludes `gov_run` and
`run_in_gov`, and restate AC5 as "the number of `run()` invocations carrying their own inline
`--to` is 4", with the arm computing it by that anchored pattern.

**Left-shift gate.** A memory-hygiene check over spec §4 Inventory tables: every integer cell carries
an adjacent runnable measuring command, and the check EXECUTES it and compares. That is the gate this
document has now needed twice — it turns "a number typed beside the thing it counts" into a leg that
reds, which §7 already asks for and nothing yet enforces on specs.

---

### H1 — high · `DEPL-dSealedTally-1` §2, lines 34-39

*Absorbs raw ids 4 (first half), 14, 27, 39.*

The rev-3 insertion put S7 through the middle of S4. S4 ends mid-clause at line 35 on "so the summary
does not report", S7's body follows at 36-38, and S4's tail "a landing that was undone." sits
orphaned at line 39 BELOW S7's own closing sentence, indented as if it belonged to it. The scope list
also reads S1-S2-S3-S4-S7-S5-S6.

§2 is the section a builder works from top-down. As it stands S4's second consequence — the
`_landed_new` removal, the mechanism B2 turns on — reads as a truncated fragment, and S7 reads as
ending in a sentence fragment that is part of its own requirement. A reader cannot tell which of the
two items owns the removal.

**Fix.** Rejoin S4 into one bullet ending "…so the summary does not report a landing that was
undone." and move the S7 bullet whole to below S6, where its number puts it.

**Left-shift gate.** Covered by B1's bullet-structure check, with the orphan-continuation clause: no
line at bullet indent that is neither a bullet head nor an indented continuation of the bullet above
it, and `**Sn**` heads in ascending order.

---

### H2 — high · `DEPL-dSealedTally-1` §2 S7, no corresponding item in §6

*Absorbs raw id 3.*

S7 is a declared IN-scope item with no acceptance criterion. No AC names the `removed <path>` verb,
and none names the conditioning of the "was restored to the index entry it had" sentence that
`govkit.py:6941-6945` emits. AC1 grades only that the report is REACHED, "rather than a traceback",
never its verb.

So the fold's own fix ships ungraded. Every criterion stays green while the rollback report keeps
printing `restored  <dest>` for a file it deleted and keeps claiming an index entry was restored for a
path that never had one — precisely the defect round 1's L1 raised.

**Fix.** Add a criterion over the AC1 arm's captured report: it contains `removed <dest>`, does NOT
contain `restored  <dest>`, and omits the index-entry sentence when every rolled-back entry has
`origin == "landed"`.

**Left-shift gate.** See H3 — one check covers both.

---

### H3 — high · `DEPL-dSealedTally-1` §2 S4, no corresponding item in §6

*Absorbs raw id 4 (second half).*

No AC names `written_paths`, the closing tally, `_landed_new`, or the `unclaimed sources: N` summary
at `govkit.py:7190`. AC1-AC4 cover absence, staging, the index and the receipt; AC5 covers
containment; AC7 counts arms. A declared scope item ships wholly ungraded, so a rolled-back landing
can still be counted by the summary and still be classified untouched by the closing tally with the
whole bar green.

**Fix.** Add a criterion asserting that after the AC1 rollback the run's landed summary lists no
rolled-back destination and the closing tally does not report it untouched.

**Left-shift gate.** A memory-hygiene check pairing §2 with §6: every `**Sn**` in a spec's Scope is
named by at least one criterion in §6, or the spec states in-line why it is deliberately ungraded.
This is the highest-value gate in this report — two of seven scope items in one unit are currently
ungraded, and the check is a join over text the specs already structure.

---

### H4 — high · `DEPL-dSealedTally-1` §2 S1 and §4 Files touched (line 109)

*Absorbs raw ids 16, 25.*

S1 changes `derive_unclaimed_candidates` to return `(dest, eid)` PAIRS. Its one live consumer is the
read-only preview at `govkit.py:6276-6282`, which iterates `for _p0 in _pv_land` and prints
`govkit update —   would land {_p0}`. After the shape change every preview line prints a tuple
instead of a path — in the verb's read-only DEFAULT, which is the whole safety story §5 tells.

The regression lands green. `tools/govkit/selftest.py:5140` asserts only the count line
(`unclaimed sources: 1 landed`), never a per-path preview line. And §4's ~80-line budget for
`govkit.py` names no edit at 6276: it still lists "the preview-widened `touched_kits`", the mechanism
rev-3's own §9 says it deleted.

**Fix.** State in S1 that the 6276 call site unpacks the new shape; replace "the preview-widened
`touched_kits`" in §4 Files touched with "the return-shape change and its surviving consumer"; add a
criterion asserting the preview still prints a bare path.

**Left-shift gate.** An arm in `tools/govkit/selftest.py` asserting the preview's per-path line
matches `would land <path>` with no bracket or quote character in it. A print-shape assertion on
operator-facing output is the class of gate this whole unit keeps needing and does not have.

---

### H5 — high · `DEPL-dSealedTally-5` §3 Non-goals, second bullet (lines 52-54)

*Absorbs raw ids 6, 18.*

The non-goal still reads "32 of the 74 do", while §4 Inventory (lines 82-85) states that figure was a
LINE count "wrong by about 2.5x" and puts the argument count at 13. The document declares the
excluded population twice with numbers it itself calls refuted, and the refuted one leads the section
a reader opens first for scope boundaries. This is the exact figure rev-3's H2 fold existed to remove,
left standing in the half that defines scope. Nothing in §6 grades which invocations were left alone,
so no run catches it.

**Fix.** Rewrite the bullet to the measured figures: 13 `--to` argument tokens exist, of which 4 are
in real-root `run()` calls and 9 in the scratch-gov helpers, and none is re-pointed. Point at the
Inventory row rather than restating a second count.

**Left-shift gate.** Covered by B4's measuring-command check, plus a narrower one worth having on its
own: no spec states the same population size twice with different integers. A grep for repeated
"N of the M" shapes inside one file, compared pairwise, is cheap and would have caught this.

---

### H6 — high · `DEPL-dSealedTally-5` §4 Data model (line 66), Rollout (line 115), Files touched (lines 119-120)

*Absorbs raw ids 7, 13, 33.*

Three passages in §4 describe the shape round 2 refuted. Data model says the pin is "threaded through
the `run(*args)` helper alone". Rollout says "The pin is threaded at one helper, so a future edit
widening it is visible in one place". Files touched budgets "the `--to` threading through `run(*args)`"
and "the apply-at-pin change for S4".

All four claims are contradicted by §2. S1 requires threading BOTH `run()` at line 69 AND the direct
`subprocess.Popen` at 2627 — verified as a real-root `update --write` outside `run()` — and states
that leaving the latter unpinned makes AC1 unreachable. S4 explicitly FORBIDS apply-at-pin: "pinning
it would add a public surface to a product verb — M3 veto 2, which is an owner turn this run cannot
take", and replaces it with a fixture receipt rewrite. §4's stated safety property, "visible in one
place", is simply false with two sites, and its own Inventory row already names both — so §4
contradicts itself as well as §2.

A builder sizing the work from §4 prices an edit the scope section vetoes as an owner turn, and
rebuilds the narrow fix that leaves the 2627 call unpinned. No criterion counts threading sites, so
nothing reds on the divergence.

**Fix.** Rewrite Data model to name both sites; change Rollout's "one place" to name the two, or state
why two is the floor; rewrite Files touched as: the resolution and its refusal, the conditional
`--to` threading in `run(*args)` at 69, the same threading at the direct `Popen` at 2627, the
post-`apply` `gov_commit` rewrite for S4, the liveness arm, and the AC5 counting arm.

**Left-shift gate.** An arm asserting the count of real-root pin-injection sites in
`tools/govkit/selftest.py` equals a declared constant, so a third real-root invocation added later
reds instead of quietly running unpinned. Pair it with B4's counting arm — they are the same
instrument aimed at two populations.

---

### M1 — medium · `DEPL-dSealedTally-1` §4 Files touched (lines 109-113)

*Absorbs raw ids 10 (first half), 20.*

The `govkit.py` budget still names "the preview-widened `touched_kits`", the rev-2 mechanism rev-3
deleted. The `selftest.py` budget's fourth item is "the containment mutation" — but AC5 now requires
the opposite arm shape, a monkeypatch recording `demand_contained_dest`'s `where` argument, and states
in its own text why a mutation arm is invalid: "Deleting the call is not the observation: an arm built
that way cannot fail for the right reason." The AC2 passing-check arm is budgeted nowhere.

Unlike a stale line number this names the ARM SHAPE, so §4 instructs the builder to write the arm §6
refuses. It is round 2's H1 finding re-entering through the design section.

**Fix.** Rewrite the `selftest.py` budget to the arms AC1-AC5 actually need — the staged-RED arm, the
passing-check arm, the index assertion, the receipt-row assertion, and the `demand_contained_dest`
monkeypatch recording its `where` argument — and replace the `touched_kits` item per H4.

**Left-shift gate.** Not gateable as prose-vs-prose. Fold it into this repo's §10 recurring-class
checklist as a documented check: after any spec fold, re-read §4 Files touched against the amended §2
and §6, because the budget is the section a fold never revisits. Round 2 and round 3 have both
confirmed a defect there.

---

### M2 — medium · `DEPL-dSealedTally-1` §10 Reuse audit (lines 203-204)

*Absorbs raw ids 10 (second half), 28, 41.*

§10 still says the unit "reuses the read-only classifier `derive_unclaimed_candidates` at 6276 for S1
rather than deriving the landed set twice" — the exact citation rev-3's B1 fold struck. §2 S1 says of
that line: "it sits inside `if not write:` and the branch returns at 6285, so a `--write` run never
reaches it", which I confirmed in the source. So the document asserts and denies the same seam in two
sections, and the stale answer sits where a later pass looks for prior art.

The clause's second half is false too. Grepping `derive_unclaimed_candidates` in `govkit.py` returns
one definition at 6203 and one call at 6276; the landing block re-walks `(kits or claimed)`,
`resolve_entry` and the four refusals inline. The function's own comment at 6270 — "ONE
IMPLEMENTATION, TWO CALLS" — is already false in the shipped tree, and with S1's new call added a
`--write` run does derive the landed set twice.

**Fix.** Cite the FUNCTION, not the dead call site: "it reuses the classifier
`derive_unclaimed_candidates`, defined at `tools/govkit/govkit.py:6203`, by adding a write-path call
rather than deriving the landed set twice", and record that the reuse costs a return-shape change
affecting the preview consumer (H4). While there, correct the 6270 comment.

**Left-shift gate.** A memory-hygiene check that every `path:line` citation in a tracked spec resolves
to a line that still exists, and — where the spec quotes the identifier at that line — that the
identifier is still there. It cannot catch a semantically stale citation, and its header should say
so, but it catches the whole class of line numbers that moved.

---

### M3 — medium · `DEPL-dSealedTally-1` §2 S7 and §4 Migration

*Absorbs raw id 29.*

S7 conditions only the order's "was restored to the index entry it had" sentence. It never says the
two empty-`restored` fallbacks must also become conditional, and both key on `if not restored`:
`govkit.py:6946` writes "(nothing to restore: every path this kit owns was refused before it was
written)" into `update-rollback-<eid>.md`, and 6956 prints "ROLLED BACK · (no path restored)".

By requiring landed paths to print under a separate verb, S7 GUARANTEES `restored` is empty for
exactly the fixture AC1 and S6 construct — "a kit whose ONLY change is a landed source". So this
unit's own central scenario writes an operator order stating the path was refused before it was
written, when it was written and then deleted. The outbox order is the operator's only durable record
of a delete in a repository gov does not own. S7 exists to stop the report contradicting what
happened, and as specified it produces two new contradictions in the one class the unit adds.

**Fix.** Extend S7: both fallbacks fire only when `restored` AND the new `removed` list are empty, and
the report enumerates `removed <path>` lines beside the `restored <path>` ones. Add a criterion
asserting the AC1 run's order file contains a `removed ` line and does not contain "nothing to
restore".

**Left-shift gate.** Same arm as H2's — one assertion over the captured order file covers both. Worth
generalising into the repo's recurring-class checklist as "a report's fallback branch states a fact,
not an absence": any `if not <list>` message that asserts WHY the list is empty must be re-read
whenever a sibling list is added.

---

### L1 — low · `DEPL-dSealedTally-1` §4 Inventory, paragraph at lines 85-87

*Absorbs raw id 22.*

The sentence justifying S1's empty withdrawal set is broken mid-clause: "For S1 the empty set is safe
in the name a kit that turns out not to need a baseline, and baselining a kit the run does not touch
costs one `run_kit_check` and grades nothing wrongly." The clause "safe in the name a kit" has no
parseable predicate — the direction was lost when rev-3 struck the preceding rev-2 sentence, which the
paragraph flags two lines up ("Rev-2 added … it is struck"). Only "It cannot MISS a kit" at line 87
still carries the argument, so a reader auditing the one deliberate imprecision in S1 has to
reconstruct it.

**Fix.** Restore the clause, along the lines of "the empty set is safe in the direction it errs: it
can only NAME a kit that turns out not to need a baseline".

**Left-shift gate.** None proposed. This is a prose-repair class no cheap predicate reaches without
false positives, and the B1 bullet-structure check does not see mid-paragraph damage. It belongs in
the fold checklist alongside M1.

## What the refuted half was

Seventeen findings did not survive the skeptic. Three claimed `govkit.py` behaviour that reading the
code disproved. The rest were missing-detail complaints against sections that are deliberately terse —
a spec is not required to restate its kit's contract — plus several that re-reported round 2's
already-folded findings as if they still stood. No refuted finding is carried forward as a caveat.

Nothing was left unverified: every raw finding either survived a skeptic or was refuted by one.

## What this round says about the fold

Nine of the fourteen defects are in text rev-3 wrote, and two of those are structural corruption
rather than a wrong claim — an AC head deleted by a neighbouring edit, and a scope item inserted
through the middle of another. That is a new class for this build: rounds 1 and 2 found bad
mechanisms, round 3 finds a bad EDIT. The cheapest counter is the bullet-structure check proposed
under B1, because it is the one gate here that would have caught both corruptions before the commit
that made them, and it costs a single pass over files the hygiene gate already reads.

The second theme is unchanged from round 2 and worth stating once more: the fold rewrote §2 and §6
and did not revisit §4 or §10. Four of the fourteen defects are stale design or budget prose left
behind an amended scope. Until §4 Files touched is re-derived rather than re-read, that will recur.
