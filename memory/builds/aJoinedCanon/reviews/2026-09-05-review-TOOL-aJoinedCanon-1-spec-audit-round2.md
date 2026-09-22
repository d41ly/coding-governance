**Serves:** spec-audit TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11

# Spec audit round 2 — aJoinedCanon

Tier-2 · node a · 2026-09-05 · a second pre-code pass over the whole eleven-unit spec set at rev-3, after the round-1 fold, before any unit opened and before owner scope approval. Round 1 returned BLOCKED with 2 blockers, 9 highs and 6 mediums; all seventeen were folded. This round was primed to hunt the fold rather than re-find them.

**ROUND 2** over eleven subjects, each pinned at the blob it was read at: [TOOL-aJoinedCanon-1](../spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md)@`2bc769096fd3` · [TOOL-aJoinedCanon-2](../spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md)@`3898ff554fff` · [TOOL-aJoinedCanon-3](../spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md)@`9c3f68c368c1` · [TOOL-aJoinedCanon-4](../spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md)@`2f7144f30f23` · [TOOL-aJoinedCanon-5](../spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md)@`eda6912ca0b0` · [TOOL-aJoinedCanon-6](../spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md)@`5af780e23ab8` · [TOOL-aJoinedCanon-7](../spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md)@`c8928799b428` · [TOOL-aJoinedCanon-8](../spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md)@`971638b93b26` · [TOOL-aJoinedCanon-9](../spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md)@`c62bc8bae565` · [TOOL-aJoinedCanon-10](../spec/2026-09-04-spec-TOOL-aJoinedCanon-10.md)@`2a7a5b4d8a5e` · [TOOL-aJoinedCanon-11](../spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md)@`aa5115c05ac5`.

## Verdict: BLOCKED

One finding says a unit cannot be built as its own design section describes it, and it is round 1's
own blocker B1, wearing a different unit number. B1 was ruled on and closed in `TOOL-aJoinedCanon-4`
with a hoist plus a witness-key-absent fixture. `TOOL-aJoinedCanon-3` writes the same awk block
three `order` steps EARLIER, places its arm against the same anchor, and never says the branch sits
outside the `SPEC_WITNESS_CUTOFF` guard — so the fix landed on the second unit to touch the block
and not on the first, and unit 4's hoist moves the acceptance accumulator, not unit 3's independent
§2 walk. An adopter arming `SCOPE_JOIN_CUTOFF` alone still gets an arm that never runs while its own
key reads as armed. That needs a design sentence in unit 3, not a build-pass repair.

The rest is repairable inside the specs, mostly one line each — but the distribution is the story.
Fifteen of the twenty-three distinct defects below are the fold's own work: a ruling applied to one
sibling and not to the sibling beside it (eight times), a revision-log entry claiming a conversion the
document only half carries (three times), two specs the fold commit `0787e7cb` never touched at all
(`TOOL-aJoinedCanon-2` and `TOOL-aJoinedCanon-5`, which round 1 cleared and which the build's new
rules therefore never reached), a ruled-on wrong line number corrected in one spec and left standing
in the other (once), and two rev-3 edits landing the same day in opposite directions (once). 15 of 23
is 65%, inside the 60–89% band round 1 measured across five builds. The fold is still the most
defect-dense operation in this build, and it is now measurably so on this build's own corpus.

The seven that are not the fold's doing are the ones worth the most: three criteria whose stated
failing case does not exist in the code they name.

## Review shape

| Raw | Confirmed | Refuted | Unverified | Precision |
|---|---|---|---|---|
| 46 | 40 | 6 | 0 | 0.87 |

Precision 0.87, up from round 1's 0.61, and nothing came back unverified. That jump is the priming
change round 1 recommended — the fan was handed the write sets as a table and this report's
predecessor — and it says the fan is now over-calibrated rather than under: at 0.87 the skeptics are
refuting almost nothing, which usually means the lenses stopped reaching for the hard half. Round 3
should widen scope, not tighten it.

The 40 confirmed collapse to **23 distinct defects**. The duplication is concentrated in the
citation class: four lenses independently found unit 6's three surviving line pins, four found unit
10's `Lines 22, 24 and 29`, four found unit 2's `:183`, three found unit 5's unconverted anchors.
That is a coverage artefact of handing every lens the same build rule to check against, and it is
cheap — the consolidation is stated per finding.

Two units drew no confirmed finding: none. Every one of the eleven has at least one.

## Severity as adjudicated here

Two severities here differ from the ones the fan assigned, both raised, both for consistency with
round 1's own rulings.

- **Raised to BLOCKER — B1, the nested guard in `TOOL-aJoinedCanon-3`.** The fan called it high. The
  owner ruled the identical defect a blocker on `TOOL-aJoinedCanon-4` in round 1, and grading the
  same shape lower on the unit that writes the block FIRST is how the class survives a second fold.
- **Raised to HIGH — H9, the three surviving pins in `TOOL-aJoinedCanon-6`.** Two lenses called it
  medium and two high. It goes high because one of the three sits inside an acceptance criterion and
  because the spec now asserts, in §4 and again in its rev-3 entry, a property of itself that is
  false — a later reader trusts the sentence instead of checking, which is strictly worse than the
  pin it was supposed to remove.

One severity is deliberately held DOWN. M2, unit 2's `:183` pins, is a plain offset with the clause
quoted verbatim beside every number; H10, unit 5's, is high because unit 4 does not merely shift its
anchor, it unindents the loop the whole placement argument rests on. Same rule broken, different
blast radius.

| Severity | Count |
|---|---|
| BLOCKER | 1 |
| HIGH | 10 |
| MEDIUM | 10 |
| LOW | 2 |

## The findings at a glance

| # | Sev | Unit | Address | The defect |
|---|---|---|---|---|
| B1 | blocker | `TOOL-aJoinedCanon-3` | §2 S4, §6 | round 1's blocker, unfixed in the sibling that writes the block first |
| H1 | high | `TOOL-aJoinedCanon-3` | §4, §7, §2, §6 | §4 states a version-bump obligation its own file table, scope and criteria all omit |
| H2 | high | `TOOL-aJoinedCanon-4` | §2 S1 and S7, §6 AC10 | the entire author-facing half can ship absent with AC1–AC11 green |
| H3 | high | `TOOL-aJoinedCanon-1` | §2 S1/S2/S7, §6 AC8 | the grammar the arm grades is observed only by a byte-compare of two unmoved files |
| H4 | high | `TOOL-aJoinedCanon-11` | §2 S6, §6 | a scope item with no criterion at all, and no `Observed by` tag either |
| H5 | high | `TOOL-aJoinedCanon-6` | §2 S6, §6 AC8 | the named mitigation for a 25.4% false-red rate is graded by a sameness compare |
| H6 | high | `TOOL-aJoinedCanon-9` | §6 AC1 | the stated failing case does not exist, and the invocation is not a real verb |
| H7 | high | `TOOL-aJoinedCanon-7` | §6 AC6, §7 | AC6 claims an equality neither the suite nor the leg performs |
| H8 | high | `TOOL-aJoinedCanon-2` | §2 S1, §6 AC5 | the criterion is driven by the record's own anchors, not by the pointer it stands for |
| H9 | high | `TOOL-aJoinedCanon-6` | §6 AC7, §10, §4 | three line pins survive a fold whose log says it converted every one |
| H10 | high | `TOOL-aJoinedCanon-5` | §4, §2 S1b | no citation sweep reached it, and unit 4 restructures the block it argues from |
| M1 | medium | `TOOL-aJoinedCanon-1` | §3, §4 | three numbers wrong at base, one of them a round-1 ruling corrected only in unit 4 |
| M2 | medium | `TOOL-aJoinedCanon-2` | §2 S3, §4, §6 AC3 | four pins into the template pair, in a spec the rules sweep never touched |
| M3 | medium | `TOOL-aJoinedCanon-10` | §3 first non-goal | the sweep skipped the one section holding a number that is wrong today |
| M4 | medium | `TOOL-aJoinedCanon-11` | §7 leg list | script paths where leg names belong, and `verdict epoch` missing entirely |
| M5 | medium | `TOOL-aJoinedCanon-9` | §7 closing paragraph | a leg is hidden from the join on grounds unit 7 deletes two `order` steps earlier |
| M6 | medium | `TOOL-aJoinedCanon-9` | §2 S1 and S9, §6 | one third of the F1 adopter deliverable has no observer and no documented check |
| M7 | medium | `TOOL-aJoinedCanon-11` | §6 AC4 | the whole-tree green cannot fail for the reason the criterion gives |
| M8 | medium | `TOOL-aJoinedCanon-11` | §4 "The probe that cannot move" | the header amendment it prescribes is false of its own file before it is written |
| M9 | medium | `TOOL-aJoinedCanon-8` | §3 Edges | the worked example is contradicted by unit 10's rev-3, folded the same day |
| M10 | medium | `TOOL-aJoinedCanon-8` | §2 S10 | `Observed by AC11` is false for half of what S10 declares |
| L1 | low | `TOOL-aJoinedCanon-9` | §4 | a count of a population unit 8 changes one `order` step earlier |
| L2 | low | `TOOL-aJoinedCanon-8` | §4 Alternatives rejected | `render_edges` is at `:1016`, not `:1013` |

---

## Blockers

### B1 — round 1's blocker, unfixed in the sibling that writes the block first

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md` §2 S4, against
§6 (no criterion). Consolidates 1 confirmed finding.

**Defect.** S4 places the new §2-item arm "after the acceptance-witness arm, whose last statement
prints `acceptance bullets naming no backticked witness`", and never says OUTSIDE the enclosing
guard. That print sits INSIDE `if (wcut != "" && fdate != "" && fdate >= wcut) {`, so the position
S4 describes is satisfied by a nesting that makes this arm's population the INTERSECTION of
`SCOPE_JOIN_CUTOFF` and `SPEC_WITNESS_CUTOFF`. No criterion observes independence.

**Why it is real.** Verified at source: `tools/memory-tree/check-memory-hygiene.sh:1020` opens the
guard, `:1048` is the print S4 names as its anchor, and the guard does not close until `:1049`.
`tools/memory-tree/.memory-tree.conf.example:39` ships `SPEC_WITNESS_CUTOFF=""`, so an adopter who
arms `SCOPE_JOIN_CUTOFF` alone gets an arm that never executes while its own key reads as armed.
AC1–AC5 and AC7–AC10 all drive fixtures in a scratch tree whose conf pins `SPEC_WITNESS_CUTOFF`, so
a nested arm passes every one of them. Unit 4's order-4 hoist does not repair this: the hoist moves
the `acc` acceptance accumulator, and unit 3's is an independent §2 item walk.

**Fix.** Say in S4 what unit 4's S3 now says: the branch sits outside the `wcut` guard and carries
only its own liveness test. Then add unit 4's AC7 in this unit's numbering — a post-cutoff fixture
with an unjoined §2 item, in a scratch tree whose conf declares `SCOPE_JOIN_CUTOFF` and declares NO
`SPEC_WITNESS_CUTOFF`, still reds.

**Left-shift.** The gate for the class, and it would have caught both instances: extend
`tools/memory-tree/check-memory-hygiene.test.sh` with a one-cutoff-at-a-time matrix — for each
cutoff key the engine reads, build a scratch conf arming that key ALONE, blank every other, and
assert the key's own red fixture still reds. Any arm that has silently inherited a neighbour's guard
fails immediately, in every adopter shape rather than only in this repo's fully-armed fixture conf.
The declaration half belongs to `TOOL-aJoinedCanon-5`, which is already building a preconditions
field: require it to name every `-v <name>cut` guard on the awk path the arm sits on.

---

## Highs

### H1 — §4 states a version-bump obligation that the file table, the scope and the criteria all omit

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md` §4 Files touched, against §2 and §6.
Consolidates 1 confirmed finding.

**Defect.** §4 states "The commit also owes a `gov:kit memory-tree@` version bump in EVERY carrier"
and §7 names `kit version markers`, but the Files-touched table has no version-carrier row, none of
S1–S7 declares the bump, and none of AC1–AC10 runs `tools/check-kit-versions.sh` or
`tools/memory-tree/check-verdict-epoch.sh`.

**Why it is real.** Verified. `grep -rl 'gov:kit memory-tree@'` over `tools/` and `memory/guides/`
returns carriers the table does not list, among them `tools/check-kit-versions.sh`,
`tools/memory-tree/adopt-memory-tree.sh`, `HYGIENE.template.md` and `memory/guides/BUILD-METHOD.md`.
Units 1 (S8), 6 (S8) and 8 (S10) each carry this as a scope item; unit 3 alone does not — round 1's
H4 fix was applied to unit 6 and not swept sideways. One correction to the failure attribution: an
unbumped constant leaves `kit version markers` GREEN, because every carrier still agrees; it is
`verdict epoch` that reds, since this unit changes the engine.

**Fix.** Add a bookkeeping scope item naming the constant plus every `gov:kit memory-tree@` carrier,
with the set derived by `grep -rl` at build time rather than counted in prose; give the Files-touched
table its row; add a criterion asserting both scripts exit 0 on the landing commit, with the
constant-untouched case as the observed red.

**Left-shift.** A check-12 arm joining §4 to §6: a spec whose §4 Files-touched table names a file
matching the engine set `check-verdict-epoch.sh` already computes must carry a §6 criterion naming
`check-verdict-epoch.sh`, or a §7 waiver saying why not. This is the same join the build is already
building for scope items, applied to the one obligation every engine-touching unit owes.

### H2 — unit 4's entire author-facing half can ship absent with every criterion green

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md` §2 S1 and S7, against §6 AC10 and §7.
Consolidates 2 confirmed findings.

**Defect.** S1 is the `Red when:` paragraph in `SPEC-TEMPLATE.template.md` — the only thing that
ever tells a spec author to write the clause this unit's arm grades. S7 is a sentence in HYGIENE
item 12 plus a `KIT_MEMORY_TREE_VERSION` bump. AC10 is `kit-dogfood-parity.test.sh --check`, a
render-and-byte-compare that is equally green when NEITHER half moved, and it is explicitly scoped
to the `TEMPLATE-SPEC.md` / `SPEC-TEMPLATE.template.md` pair, so it cannot reach the HYGIENE pair at
all. No criterion greps any rendered file for the marker text, the HYGIENE sentence, or the version.

**Why it is real.** Verified: AC1–AC7 and AC11 drive the six fixtures, AC8 the hoist, AC9 the example
conf, AC10 the parity compare. Nothing else. Under the ratified 2026-09-06 cutoff the arm grades
zero live specs at landing, so the template paragraph is the ONLY thing a post-cutoff author meets —
and it is the half with no observer. This is round 1's H9 class, which the owner raised to HIGH and
which unit 3 closed with AC9 in the same fold; unit 4 did not get the sweep. §7 states the version
obligation outright ("a new arm changes the engine's verdicts, so `KIT_MEMORY_TREE_VERSION` must
move in the same landing") with nothing in §6 behind it.

**Fix.** Add unit 3's AC9 in this unit's numbering: after the render, a grep for `Red when:` over
`memory/TEMPLATE-SPEC.md` returns non-zero against the pre-change count recorded in §4's Inventory
table, and a grep over `memory/HYGIENE.md` item 12 finds the added sentence. Add unit 6's AC12: on
the landing commit `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
both exit 0, with the two new `Red when:` branches landed on an untouched constant as the observed
red. Restate AC10 as the sameness check it is, the way unit 3's AC6 now does.

**Left-shift.** One arm covers H2, H3, H4, H5 and H8 together: in check 12, a §2 scope item whose
own text names a file in the doc pair set may not be observed SOLELY by a criterion whose body
matches the parity/byte-compare family. The predicate is greppable — the criterion cites
`kit-dogfood-parity` or `--check` and nothing that reads content — and it fires on exactly the shape
five specs in this set committed independently.

### H3 — the grammar the arm grades is observed only by a byte-compare of two files that need not have moved

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §2 S1, S2 and S7, against §6 AC8.
Consolidates 1 confirmed finding.

**Defect.** S1 (the `## REV_SCOPE_CUTOFF` grammar section), S2 (the two §9 skeleton example lines)
and S7 (the HYGIENE check-12 paragraph) are observed only by AC8, the doc-pair byte-compare, whose
own text concedes it grades whether both halves moved together rather than what they say.

**Why it is real.** Verified: AC1–AC6 are fixtures, AC7 the corpus green, AC9 the verdict epoch,
AC10 check-arms, AC11 the manifest, AC12 the notice, AC13 the example conf. Nothing greps the
rendered template for `- rev-<N> · <date> · <scope> · <what moved>`, for the reworked `rev-2`
skeleton line, or for the HYGIENE sentences. Same aggravator as H2: this unit's cutoff means the arm
grades zero specs at landing, so the ungraded text is the whole author-facing product.

**Fix.** Add a content criterion beside AC8, derived against a pre-change count recorded in §4: after
the render, a grep for the rev-line grammar over `memory/TEMPLATE-SPEC.md` and a grep for the check-12
sentences over `memory/HYGIENE.md` each return non-zero, and the skeleton's `rev-2` example carries a
scope token. Restate AC8 as a sameness check.

**Left-shift.** H2's arm.

### H4 — a scope item with no criterion at all, in the unit whose §4 names the trap twice

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §2 S6, against §6. Consolidates 1
confirmed finding.

**Defect.** S6 — the `base` bullet in `memory/TEMPLATE-SPEC.md` and its twin gain the resolution rule
and NAME the cutoff, with the kit version marker moved in every carrier — has no §6 criterion, and
unlike S1, S5 and S7 it carries no `Observed by` tag either. AC8 is scoped to check 12's catalog
entry in `memory/HYGIENE.md` plus the HYGIENE pair's byte parity, and says nothing about the template
pair or the version marker.

**Why it is real.** Verified: AC1–AC3 and AC5–AC6 are fixtures and engine, AC4 the corpus green, AC7
check-arms, AC8 the HYGIENE entry, AC9 the example conf. The traps are real in this tree and this
spec's own §4 cites both of them — `TOOL-aSiftedFork-5` and backlog row `TOOL-dSettledRoster-4`, the
twice-missed marker.

**Fix.** Add a criterion that reads the `base` bullet after the render and asserts it names
`BASE_RESOLVE_CUTOFF` and the resolution rule, against S2's recorded pre-change absence; and a second
asserting `bash tools/check-kit-versions.sh` exits 0 with the constant advanced by this diff, in the
shape unit 6's AC12 already uses.

**Left-shift.** H2's arm, plus the narrower one this build is already funding: unit 3's mechanism
makes an `Observed by` tag mandatory per scope item. Make the ABSENCE of the tag a red rather than a
silence, so a scope item cannot decline to answer.

### H5 — the named mitigation for a measured 25.4% false-red rate is graded by a sameness compare

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md` §2 S6, against §6 AC8. Consolidates 1
confirmed finding.

**Defect.** S6 puts the token rule in the HYGIENE pair and is tagged "Observed by AC8". AC8 is
`kit-dogfood-parity.test.sh` being green, proving `HYGIENE.template.md` carries the same bytes — a
sameness compare that is green when the rule was never written into either half.

**Why it is real.** Verified, and this one is load-bearing rather than documentary. §4 names S6 as
the notation answering arm B's measured 25.4% corpus / 18.2% newest-cohort containment failure —
the thing an author is supposed to follow instead of arguing with a red bar. The one mitigation of a
gate the spec itself expects to red on correct ledgers ships with no observation that can fail, in
the unit whose §5 risks row concedes that a gate manufacturing work on correct ledgers gets waived.

**Fix.** Add the content half AC8 lacks, as unit 3's AC9 does: after the edit, a grep for the token
rule under `## Acceptance ledger` in `memory/HYGIENE.md` returns non-zero against the pre-change
count of 0. Keep AC8 as the pair-parity leg it actually is.

**Left-shift.** H2's arm.

### H6 — a criterion whose stated failing case does not exist, and whose invocation is not a real verb

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §6 AC1, against §2 S4. Consolidates 1
confirmed finding.

**Defect.** AC1 rests on `python tools/govkit/govkit.py --selfcheck` redding a key that is declared
in `.memory-tree.conf` and in no `kit.toml` config key list. Two defects. `--selfcheck` is not a
subcommand; it exits with `govkit: unknown subcommand '--selfcheck'`. And the real verb,
`govkit.py selfcheck`, exits 0 today while `.memory-tree.conf` declares eighteen keys —
`ACCEPTANCE_LEDGER_CUTOFF`, `ARMS_FLOORS`, `FORK_MARK_CUTOFF`, `REVIEW_VERDICT_CUTOFF`,
`SPEC10_EVIDENCE_CUTOFF`, `TOMBSTONE_ROOTS` and twelve more — that appear in none of
`tools/memory-tree/kit.toml`'s four key lists.

**Why it is real.** Verified by running both. `govkit.py`'s only config-list arm is check 7, which
grades `requires_if` `when_any_key_set` entries and nothing else; `tools/check-kit-placeholders.py`
reads only `placeholders`. So S4's `[config]` half ships with no working observer at all — AC4 covers
only the `placeholders` half. This is the could-not-fail shape the build exists to remove, inside the
build that names it.

**Fix.** Rewrite AC1 so its observation is one the tooling actually makes. If the intent is that the
declaration is REACHED, grade it directly: a `python -c` over `tools/memory-tree/kit.toml` asserting
both keys appear in a `[config]` list, with the deletion of one row as the observed red. If the
intent is `requires_if` resolution, say which condition names the key. Either way, state in §4 that
no existing gate joins a conf key to a descriptor's lists, because that absence is what S4 buys
against.

**Left-shift.** Add the missing arm to `govkit.py selfcheck` itself: every key a kit's shipped
`.memory-tree.conf` / `.example` declares must appear in that kit's `[config]` lists or in a named
exemption. Eighteen live instances today, so run the predicate over the tree and print hits and
near-misses before wiring it — per charter §7, and because eighteen may hide a legitimate class the
exemption list needs to name.

### H7 — AC6 claims an equality that neither the suite nor the leg performs

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md` §6 AC6, and §7's `New arm:` line.
Consolidates 1 confirmed finding.

**Defect.** AC6 asserts that `FLOOR_ASSERTIONS` "equals the arm total the suite actually executes and
the suite compares the two". Neither comparison exists. `tools/check-spec-tokens.test.sh:127` is
`if [ "$total" -lt "$FLOOR_ASSERTIONS" ]` — a floor. `tools/check-testsuite-counts.sh`'s `compliant()`
asserts only that the file prints the agreed `PASS ($n assertions)` shape, pins a non-zero
`^FLOOR_ASSERTIONS=[0-9]+$`, and mentions the variable somewhere; it never compares the pin to the
count.

**Why it is real.** Verified against both files, including that `FLOOR_ASSERTIONS` appears in the test
suite only at its declaration (`:15`, currently 12) and in the `-lt` test. Landing the eight new arms
with the floor left at 12 passes both the suite and the leg, so "the eight added arms cannot be
stranded silently" is untrue and §7's only observer of the floor advance certifies nothing.

**Fix.** Rewrite AC6 to observe the advance directly and against a break: read `FLOOR_ASSERTIONS`
before and after, assert it rose by eight, and stage the break — delete one added arm with the floor
left raised and confirm the `-lt` test reds. Drop the equality claim, or make raising the suite to an
equality an explicit scope item with its own observed red.

**Left-shift.** The class gate is one line in `tools/check-testsuite-counts.sh`: have `compliant()`
compare the pinned `FLOOR_ASSERTIONS` to the `n` in the file's own `PASS ($n assertions)` output and
red on inequality. That turns the floor into the equality every spec in this corpus already assumes
it is, across every suite the leg covers rather than this one.

### H8 — the criterion standing in for the pointer is driven by the record's own anchors

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md` §2 S1, against §6 AC5. Consolidates 1
confirmed finding.

**Defect.** S1 requires M4 to gain "a pointer at `memory/gotchas/fold-text-is-unreviewed-surface.md`".
AC5 grades that `gotchas.py --for-diff` SELECTS that record — which is driven by the record's own
derived anchors, and those name `memory/guides/BUILD-METHOD.md` already. AC5 is therefore green
because unit 2 touches that file at all, whether or not the pointer is ever written.

**Why it is real.** Verified: the record anchors `memory/guides/BUILD-METHOD.md` at its own lines 51
and 70. AC1 grades the table's five rows, the §4 and §8 row contents and the transitivity sentence,
and stops. §3 also asserts "M4 points at that record" while refusing to restate its practices, so the
pointer is load-bearing in two sections and observed in none — the H7/H9 class of round 1, inside the
unit that ships the fold procedure.

**Fix.** Add a criterion that reads M4 at HEAD and asserts the string
`fold-text-is-unreviewed-surface` appears in the procedure block, red before the edit; or extend AC1
to require the pointer alongside the rows. Re-word AC5 to say what it observes — that this diff's
checklist selects the record.

**Left-shift.** A `gotchas/` class record for "a criterion that grades a retrieval/selection result
is green on the inputs the retrieval already had, not on the edit under test". It is the same
false-observer shape as the byte-compare family and it will keep recurring wherever a spec grades a
tool's output instead of the tree.

### H9 — three line pins survive a fold whose log says it converted every one

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md` §6 AC7 and §10, against §4 Data model and
the §9 rev-3 entry. Consolidates 4 confirmed findings.

**Defect.** §4 states "Every anchor into this engine is cited by its own source text rather than by
line number, because units 1, 3 and 4 all edit this file at a lower `order`", and rev-3's log claims
the citation rule "moved every anchor into `check-memory-hygiene.sh` … off line numbers and onto
source text". Three pins survive: AC7's `check-memory-hygiene.sh:1526`, and §10's `:1495` and
`:1508-1516`.

**Why it is real.** All three verified correct at base — `:1495` is `declare -A ALFORM`, `:1508-1516`
is the label walk, `:1526` is the `check 23 measured NO unit` printf — which is exactly the problem:
they are live numbers in a file three lower-`order` units insert into first. The fold moved §2 and §4
and left §6 and §10 standing, so the spec asserts a property of itself that is false in two of its own
sections. AC7 is the sharp end: its only anchor for the announce-line shape is a number a sibling
moves before this unit builds. No exemption is recorded for §10, the way unit 10's rev-3 records one
for its §8.

**Fix.** Convert all three — AC7 to the printf's own text `memory-hygiene: check 23 measured NO unit`,
§10 to `declare -A ALFORM` and the `while IFS="\t" read -r _lt _lseq _luid _llab` walk it already
names by variable list — and amend the rev-3 entry to describe what was actually converted.

**Left-shift.** The gate for the whole citation class, and it covers H10, M1, M2, M3 and L2 as well:
a `tools/check-spec-citations.py` arm that extracts every `<path>:<line>` citation from a spec under
`memory/builds/*/spec/`, and reds when that path appears in the §4 Files-touched table of a sibling
spec in the same build at a lower `order`. Pure structure, no source parsing, and it is the build
README's rule 6 stated as a predicate rather than as a request. A second, cheaper leg: red on a
citation whose line number does not exist in the file at HEAD.

### H10 — no citation sweep reached unit 5, and unit 4 restructures the block it argues from

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md` §4 "Where it goes, and why that placement
is not arbitrary", §2 S1b, and AC6's figure line. Consolidates 3 confirmed findings.

**Defect.** Six line pins and two byte baselines into files lower-`order` siblings edit first:
`check-memory-hygiene.sh:1020-1048` and `:1039`, `SPEC-TEMPLATE.template.md:183`,
`memory/TEMPLATE-SPEC.md:85` and `:80`, and "against 16,913 B and 16,906 B today".

**Why it is real.** All verified accurate at base and stale by construction at build time — but
`:1020-1048` is worse than stale. Unit 4 at order 4 HOISTS that exact block, unindenting the loop out
of the `wcut` guard, so §4's placement argument — that instructional prose above an author's first
bullet is read with `lab` empty inside that guard — is verified against a structure that does not
exist at order 5, and the spec never says to re-verify it. Git shows the cause plainly: the round-1
fold commit `0787e7cb`, which ADDED the two build rules this violates, touched nine of the eleven
specs and skipped units 2 and 5 — the two units round 1 cleared. The rules were written after the
sweep's scope was set, and nobody re-ran it over the cleared pair.

**Fix.** Convert every anchor to literal text: the accumulator is the block under
`# ---- acceptance witnesses:`, the regex is the line matching `AC[0-9]+[a-z]?`, the fold clause is
`Review corrections fold in here; bump the header rev and log it in §9.`, the writing rules are the
`## Writing rules` heading (AC6 already does this correctly with its `sed -n` range), and the existing
DERIVED instance is the `order` bullet. Drop the two byte baselines or mark them derived-at-build-time,
since AC4 already derives the pair. Add one sentence saying the placement analysis must be re-verified
against the loop unit 4 hoists.

**Left-shift.** H9's citation checker for the pins. For the hoist, the build-level habit worth
gating is narrower and belongs in `BUILD-METHOD`: a unit whose design argument rests on the SHAPE of
code a lower-`order` sibling restructures must say so and name the re-verification step, which is a
`gotchas/` class record and a §10 checklist line, not a machine check.

---

## Mediums

### M1 — three numbers wrong at base, one of them a round-1 ruling corrected in the other spec only

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §3 Non-goals first bullet, and §4 The arm.
Consolidates 2 confirmed findings.

**Defect.** `check-memory-hygiene.sh:1173` for the Tier-1 cut (it is `:1172`); `memory/HYGIENE.md:299`
for the ledger's AMENDED form (`:299` is the OBSERVED form, AMENDED is `:300`); and
`memory/guides/BUILD-METHOD.md:207` labelled "M7 step 4" (`:207` is step 3, `**This file, whole.**`).

**Why it is real.** Verified — the file's only `hdr ~ /Tier-1/` match is line 1172. Two of the four
anchors the §3 non-goal offers as "Verified at writing time" evidence do not say what the spec says
they say. And round 1's M4 adjudicated this exact anchor, recorded that three specs gave three
different numbers, and its Fix reads "Correct unit 4 AC5 AND unit 1 §4 to `:1172`". Commit `0787e7cb`
corrected unit 4 and did not correct unit 1. Unit 1 is `order` 1, so these are not stale — they are
simply wrong, in the spec the whole chain builds from.

**Fix.** Cite the cut as `if (hdr ~ /Tier-1/) next`, the AMENDED form by its ledger line text, and the
sub-spec step as `4. The CURRENT sub-spec, whole`.

**Left-shift.** H9's citation checker, second leg — red on a `path:line` citation whose line does not
carry the identifier the same sentence quotes. Plus the process half, which is the real lesson: a fold
that closes a review finding should be verified by re-running the finding's own check against every
address the finding names, not against the one the fold happened to open.

### M2 — four pins into the template pair, in a spec the rules sweep never touched

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md` §2 S3, §4 Files touched and Alternatives
rejected, §6 AC3. Consolidates 4 confirmed findings.

**Defect.** `SPEC-TEMPLATE.template.md:183` and `memory/TEMPLATE-SPEC.md:183` for the fold clause,
plus `line 138` for the pathless `BUILD-METHOD M4` precedent. Unit 1 at `order` 1 adds a
`## REV_SCOPE_CUTOFF` explainer of roughly fourteen lines plus two skeleton lines to the same file,
and every explainer in that file sits above the skeleton at `:160`, so all four numbers shift before
unit 2 builds at `order` 2.

**Why it is real.** All four verified correct at base. Unit 2's rev-3 log is one of two that record no
citation conversion, and `0787e7cb` does not touch this file — same cause as H10. Held at medium
rather than high because S3 quotes the clause verbatim beside the number and AC3's real observation
is two `grep -c` calls, so a builder is inconvenienced rather than misdirected.

**Fix.** Drop the `:183` from S3 and AC3 and let the quoted clause be the anchor. Replace `line 138`
with the §10 bullet's own sentence, `BUILD-METHOD M7's regrounding step 5 re-runs the query FROM that
line`.

**Left-shift.** H9's citation checker.

### M3 — the sweep skipped the one section holding a number that is wrong today

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-10.md` §3 Non-goals, first bullet. Consolidates 4
confirmed findings.

**Defect.** "Lines 22, 24 and 29 of both halves say 'its three siblings', 'Those three' and 'the four
cutoffs'". Verified in both halves: `Those three` is on line 23. Line 24 reads "section canons and the
check must pick one for every spec it grades" and carries no count.

**Why it is real.** Wrong at base, before any sibling moves the file, and the other two pins go stale
once five lower-`order` units re-render the pair. Unit 10's rev-3 states "§1, §2 and §4 now cite the
shared write set by literal text rather than by line number" and grants §8 an explicit exemption with
a reason — §3 got neither, which is the neighbour-left-standing shape. The bullet's whole job is to
hand a named follow-up backlog row the exact sites it must fix, so the row inherits an address that
never pointed at its quoted phrase.

**Fix.** Drop the three numbers and keep the three phrases, which are already quoted verbatim and are
unique in the file. Correct the rev-3 entry to say §3 was converted too.

**Left-shift.** H9's citation checker, both legs.

### M4 — script paths where leg names belong, and `verdict epoch` missing entirely

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §7 leg list, against §4 Files touched and
the §9 rev-3 entry. Consolidates 3 confirmed findings.

**Defect.** §7 opens "Leg names are read from `tools/gate-legs.json`, never from a list typed here"
and then lists `tools/check-kit-versions.sh` and `bash tools/run-gates/run-gates.sh` — neither is a
name in that manifest; the leg is `kit version markers`. `verdict epoch (kit version dates the
engine)` appears nowhere in the spec, though S2 adds a new verdict-bearing arm to the engine. And the
same bullet still says "the seven-carrier version marker" after rev-3's log claims the count "is
derived with `grep -rl` instead of pinned at seven" — true of §4, false of §7.

**Why it is real.** Verified against `tools/gate-legs.json:128`, which declares the leg as
`kit version markers` with `tools/check-kit-versions.sh` as its argv. `tools/check-spec-tokens.py`
excludes §7 tokens by shape — a leg name has no slash and no leading dot — so a path contributes no
graded leg name, and the obligation is invisible to the only join that grades §7. No criterion in
§6 observes the version bump either; AC8 reaches only the HYGIENE pair. The `SPEC_LEGLINE_CUTOFF`
half of the fan's claim is discounted: that arm is dated 2026-09-06 and this spec's filename date is
2026-09-04, so unit 7's arm never reaches it. The manifest mismatch and the unfolded literal stand on
their own.

**Fix.** Replace the script path with `kit version markers`, add `verdict epoch (kit version dates the
engine)`, delete "seven-carrier" in favour of §4's `grep -rl` derivation, move the whole-bar
invocation out of the leg list into the DoD sentence, and add a criterion asserting both legs exit 0
on the landing commit with the constant-untouched case as the observed red.

**Left-shift.** Extend `TOOL-aJoinedCanon-7`'s own arm, which is already resolving §7 tokens: red when
a §7 token resolves as a filesystem path that IS the argv of a manifest leg, with the remedy naming
the leg. That is the one case where a path is provably the wrong spelling of a name the manifest
already has, so it is zero-false-positive by construction.

### M5 — a leg is hidden from the join on grounds unit 7 deletes two `order` steps earlier

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §7, final paragraph of the leg list.
Consolidates 2 confirmed findings.

**Defect.** `kit/dogfood doc parity` is kept out of the backticked leg list because "its name carries
a `/`, which `tools/check-spec-tokens.py` treats as a path and does not resolve" — a checker behaviour
`TOOL-aJoinedCanon-7` removes at `order` 7, before this unit builds at `order` 9.

**Why it is real.** Verified: unit 7's S4 change 2 resolves a token that IS a manifest name BEFORE the
`NOT_A_LEG` shape exclusions, its §4 identifies `kit/dogfood doc parity` as the single manifest name
containing a `/` (confirmed — it is the only one of 93), and its AC5 observes that name graded rather
than skipped. So unit 9 ends up hiding a real leg from the very join unit 7 exists to widen, for a
limitation that no longer exists, and tells its builder something false about the checker.

**Fix.** Move the leg into the backticked list and delete the paragraph, noting that unit 7's
resolve-first change makes the slash-carrying name resolvable. If this unit may land before unit 7,
state the dependency on `order` explicitly rather than on a checker behaviour scheduled to change.

**Left-shift.** No machine check fits a prose justification. This is the fifth build rule, and it
generalises the one round 1 wrote: **no unit justifies a decision by a behaviour a lower-`order`
sibling changes** — the same rule as the pinned literal, one level up from a number. Add it to the
build README and to the §10 checklist this build's diff will carry.

### M6 — one third of the F1 adopter deliverable has no observer and no documented check

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §2 S1 and S9, against §6. Consolidates 1
confirmed finding.

**Defect.** S1 requires the shipped example conf's `READINESS_ROWS` comment to state that the value is
the ADOPTER's to change and to name the one edit that changes it; S9 names that comment as the first
of three parts of the tailoring path. AC9 observes the no-overwrite part, AC10 the README part.
Nothing observes the comment. AC1 is tagged (S1, S4) but observes only that the key resolves in the
govkit descriptor's config lists — the declaration, not the comment beside it.

**Why it is real.** Verified, and §7 names compensating manual steps for AC9, AC10 and AC7
specifically and none for the comment, in a spec meticulous enough to write three. §5's user-docs row
makes it load-bearing in the spec's own words: under F1 the README and the example's comment ARE the
adopter tool the ruling required, so a missing sentence is a missing deliverable — and the part an
adopter reads first, in their own conf, is the ungraded one.

**Fix.** Extend AC10 to the second file, or add a criterion asserting that after the edit the
`READINESS_ROWS` comment in `tools/memory-tree/.memory-tree.conf.example` names the per-project
property and the edit that changes it, in the same grep shape AC10 already uses on the README.

**Left-shift.** H2's arm, widened once: the doc-pair set it guards should include
`.memory-tree.conf.example`, since a comment in the shipped conf is adopter-facing documentation with
exactly the same silent-omission profile as the template pair.

### M7 — the whole-tree green cannot fail for the reason the criterion gives

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §6 AC4. Consolidates 1 confirmed finding.

**Defect.** AC4 says a green whole-tree run proves "the 22 grandfathered specs across
`aBatchedTribunal`, `aDrainedSluice`, `aRelaxedShard`, `aUnmannedHelm` and `cSettledDocket` are not
redded". §4 sets the cutoff strictly ahead of every committed spec filename date and S2 restricts the
population to non-terminal specs, so nothing is graded at all and the run is green whether either
exemption works or not.

**Why it is real.** Verified empirically: all nine unresolvable `base` values in the tree appear ONLY
on CLOSED specs, so S2's terminal-status conjunct excludes every bad base on its own. AC4's green
survives a broken cutoff comparison and reds only if BOTH exemptions fail. No criterion anywhere
exercises a pre-cutoff bad base — AC1 grades a post-cutoff red, AC3 the terminal exemption, AC6 the
off-state. A criterion that manufactures confidence in an unexercised guard, in the unit whose §4
names "the could-not-fail shape this unit exists to close".

**Fix.** Reword AC4 to what it can observe — the run stays green and the arm emits no sentinel,
because no tracked spec reaches the cutoff. Move the grandfathering claim onto AC3, or add a
temporary-lowering observation in the shape of unit 3's AC8: lower the cutoff, watch it red naming the
22, revert before the commit.

**Left-shift.** This is `TOOL-aJoinedCanon-1`'s zero-population notice doing a second job, and it
should be made a rule rather than a courtesy: any criterion whose proof is "a whole-corpus run stays
green" must be accompanied by the arm's own announced population count, so a green with population
zero is visibly distinct from a green with population 22. The arm already has to print the notice —
the criterion just has to read it.

### M8 — the header amendment it prescribes is false of its own file before it is written

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §4 "The probe that cannot move", against
§6 and §7. Consolidates 1 confirmed finding.

**Defect.** The stderr decision rests on "the script's contract is that anything on stdout is a
hygiene regression". The engine already breaks that in four places, and the prescribed amendment —
"stdout carries findings and stderr carries announced skips" — is falsified by one of them
(`check 23 HELD under --staged` is an announced skip printed on stdout today) and contradicts units 1,
3, 6 and 8, whose announcements are stdout by design.

**Why it is real.** Verified: the header does claim it, and `:154`, `:1303`, `:1405` and `:1526` are
non-finding stdout announcements at base. Unit 1's AC12 pins its zero-population line as stdout on an
exit-0 run, and unit 8's AC12 copies the `HELD under --staged` shape. So the spec directs the builder
to write a false sentence into a shipped header and puts one announcement class in a different stream
from every sibling's, leaving a leg-log reader two conventions for one event class.

**Fix.** Either put the skip line on stdout in the sibling shape and drop the contract claim, or make
the amendment the true one: stdout carries findings AND named announcements, and the exit status
carries the verdict. Name the four existing announcements as the evidence and say which sibling units
add more.

**Left-shift.** A self-test arm asserting the engine's header claim against its own behaviour: run the
checker on a clean tree, assert exit 0, and assert that whatever it printed is announcement-shaped
(`memory-hygiene: ` prefix, matched against the declared announcement set) rather than finding-shaped.
A header that says "anything printed is a regression" then reds on its own green run, which is the
honest way to keep a header from drifting away from its file.

### M9 — the worked example is contradicted by unit 10's rev-3, folded the same day

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §3, Edges block, the
`hands-off TOOL-aJoinedCanon-10` bullet. Consolidates 1 confirmed finding.

**Defect.** "Unit 10 is Tier-1 and carries no `### Edges` block, so this edge has no reciprocal" is
false: unit 10's own rev-3 added an `### Edges` block whose single bullet is
`consumes-from TOOL-aJoinedCanon-8`, self-described as the reciprocal of this very bullet.

**Why it is real.** Two rev-3 folds landed the same day and moved in opposite directions, both under
round 1's M2. The first live instance of the new grammar now has a reciprocal, so the spec presenting
it as the worked example of the S14 skip is wrong about its own example. The silence conclusion
survives on the other ground — S14 keys on the graded population and a Tier-1 spec is `next`-ed at
`if (hdr ~ /Tier-1/) next` before it registers — which is the half worth keeping.

**Fix.** Rewrite to the surviving reason: unit 10 DOES declare the reciprocal, and the pair is still
silent because unit 10 is Tier-1 and therefore outside the graded population S14 tests against.

**Left-shift.** This is what unit 8's own arm is for, so make it grade the build rather than the spec
text: the reciprocal check should run over the build's spec set at `--check` time, which turns "is
there a reciprocal" from a sentence a fold can invalidate into a derived answer. Until then, a fold
that edits an `### Edges` bullet must re-read the sibling it names — a `gotchas/` class record, since
this is the second cross-spec contradiction the build has produced.

### M10 — `Observed by AC11` is false for half of what S10 declares

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §2 S10. Consolidates 1 confirmed finding.

**Defect.** S10 bundles two obligations — re-measuring `ARMS_FLOORS` with `check-arms.py --report`,
and bumping `KIT_MEMORY_TREE_VERSION` in every marker carrier — and names AC11 as the observer of
both. AC11 runs only `check-arms.py --check` and `--report`.

**Why it is real.** Verified: `KIT_MEMORY_TREE_VERSION` appears in the spec only at S10 and the leg
names only in §7; no criterion names `check-kit-versions.sh`, `check-verdict-epoch.sh` or the
constant. §7 does list both legs and does state that `kit version markers` reds if a carrier is left
behind, so real coverage exists on the bar — that narrows the impact but not the defect. S10 asserts a
join to AC11 that is false for half its content, which is round 1's H9 class: the missing join
announces itself, the false one reads as coverage.

**Fix.** Split S10's version half into its own criterion — both scripts exit 0 with the constant
advanced and every `grep -rl 'gov:kit memory-tree@'` carrier moved — or amend the pointer to name AC11
for the floors and the new criterion for the version.

**Left-shift.** H1's §4-to-§6 join arm, plus one narrower rule inside unit 3's own mechanism: a scope
item's `Observed by` tag may name a criterion only if that criterion's text names the file or command
the scope item names. Cheap string containment, and it kills the false-observer class rather than
the missing-observer one.

---

## Lows

### L1 — a count of a population unit 8 changes one `order` step earlier

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §4, the paragraph beginning "The arm adds
no `fail` call site". Consolidates 1 confirmed finding.

**Defect.** "check 12 has exactly one" `fail` call site — true at base, and unit 8 at `order` 8 adds
three `fail 12` branches and re-measures `ARMS_FLOORS` before this unit builds at `order` 9.

**Why it is real.** The conclusion survives — this unit's own diff still adds no call site — but the
premise is stale by one step and the same paragraph uses it to assert that `ARMS_FLOORS` and the
harness-arms leg are unmoved. The paragraph even acknowledges that four sibling units edit the file
first while pinning a count of that file's population.

**Fix.** Drop the count. Say the arm prints into check 12's existing collected stream and adds no
`fail` call site of its own, and that whether the `ARMS_FLOORS` pair moves is derived with
`python tools/memory-tree/check-arms.py --report` before and after. Unit 11's AC7 is the model: assert
the reported pair is unchanged across a before-and-after `--report` and name no literal.

**Left-shift.** Round 1's M6 arm, still unbuilt and now earning its keep a third time: a check-12 warn
when a §4 body carries a spelled-out or digit count immediately followed by `carriers`, `legs`, `arms`
or `rows` and the same paragraph names no command that derives it.

### L2 — `render_edges` is at `:1016`, not `:1013`

**Address.** `spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §4 Alternatives rejected, the generated
build-edges bullet. Consolidates 2 confirmed findings.

**Defect.** `tools/memory-tree/gen_build_index.py:1013` is cited for `render_edges`; the definition is
at `:1016`, and `:1013` is the closing `return "\n".join(out)` of the preceding function.

**Why it is real.** Verified at HEAD and at base `750ca0ca`. The bullet's companion pins are right —
`GEN_REGIONS` at `:85-86`, `rosters` at `:661` — which rules out a whole-file offset and makes this a
single wrong number rather than a stale base. `gen_build_index.py` is in no unit's write set, so
nothing will shift it: the citation is wrong now and stays wrong. Low, because the symbol name beside
it makes the miss one grep deep — but it is the recorded ground for NOT extending the region
machinery, so a reader following it lands on an unrelated return statement.

**Fix.** Cite `def render_edges(build: dict)` by name, as the rest of the bullet already cites
`GEN_REGIONS`, or correct the number.

**Left-shift.** H9's citation checker, second leg — the identifier-at-the-cited-line check catches
exactly this and nothing else.

---

## What the hunt found and did not find

The prompt named six hunts and all six produced findings, which is one more than round 1.

- **A §2 item with no §6 criterion** — H4 (no criterion and no tag), M6, and H1 as the version-bump
  variant.
- **A criterion naming no observation, or one that cannot fail** — H2, H3, H5, H6, H7, H8, M7, M10.
  This is now the largest class in the build, eight of twenty-three, and every instance is a spec
  written to close that class committing it.
- **§2 against §3** — M9, the Edges contradiction.
- **§4 Design against §7 Gates** — H1, M4, M10.
- **What must be true of existing code for §4 to work that §4 never says** — B1 (the enclosing
  cutoff guard), H6 (no gate joins a conf key to a descriptor list), H7 (the suite compares a floor,
  not an equality), M8 (the header contract the engine already breaks four times).
- **Whether a record already decided this** — M1 is round 1's own M4 ruling, applied to one of the two
  specs it named. M9 is two rev-3 folds under round 1's M2 landing in opposite directions.

**Every line-number and text-anchor citation in this report was checked against source rather than
taken.** Correct as cited: `check-memory-hygiene.sh:1020` (the `wcut` guard), `:1039`, `:1048`,
`:1172` (`if (hdr ~ /Tier-1/) next`, the file's only match), `:1495` (`declare -A ALFORM`),
`:1508-1516`, `:1526`; `check-spec-tokens.test.sh:15` and `:127`; `gate-legs.json:128`
(`kit version markers`); `.memory-tree.conf.example:39` (`SPEC_WITNESS_CUTOFF=""`);
`memory/TEMPLATE-SPEC.md:22`, `:29`, `:80`, `:85`, `:183`; `SPEC-TEMPLATE.template.md:138` and `:183`.
Wrong as cited by the spec that cites them: `check-memory-hygiene.sh:1173` (unit 1),
`memory/HYGIENE.md:299` (unit 1), `BUILD-METHOD.md:207` labelled step 4 (unit 1),
`TEMPLATE-SPEC.md:24` for "Those three" (unit 10, it is `:23`), `gen_build_index.py:1013` (unit 8, it
is `:1016`). Two invocations were run rather than read: `govkit.py --selfcheck` is not a subcommand,
and `govkit.py selfcheck` exits 0 today with eighteen undeclared conf keys in the tree.

Unit 3's eleven converted text anchors were the newly checkable surface this round, and they hold —
the conversion is correct where it was performed. The defect is never a bad conversion; it is a
conversion that stopped at a section boundary.

## The fold, measured

Round 1's claim was that a fold creates 60–89% of the next round's confirmed findings. On this
build's own corpus it is **15 of 23, or 65%**, by these five shapes:

| Shape | Count | Instances |
|---|---|---|
| A ruling applied to one sibling, not to the sibling beside it | 8 | B1, H1, H2, H3, H4, H5, H8, M10 |
| A rev-3 log claiming a conversion the document only half carries | 3 | H9, M3, M4 |
| A spec the sweep never reached | 2 | H10, M2 |
| A ruled-on defect corrected in one of the two specs it named | 1 | M1 |
| Two folds landing the same day in opposite directions | 1 | M9 |
| Not fold-attributable — present at rev-2, never ruled on | 8 | H6, H7, M5, M6, M7, M8, L1, L2 |

The dominant shape is not carelessness inside a fold; it is **scope**. Fourteen of the fifteen are a
fold that was correct about the address it was given and never asked which siblings shared the
defect — M9, where two folds moved in opposite directions, is the only one that is not. Round 1 said
this in prose — "the same fix, sideways" — and it did not happen, because a finding's Address field
names one file and the fold followed it.

That is the one process change worth more than any of the twenty-three fixes below it: **a fold
closes a finding by re-running the finding's own predicate over the whole spec set, not over the
address the finding names.** For this round that is nearly free — the citation checker in H9's
left-shift covers H9, H10, M1, M2, M3 and L2; the doc-pair observer arm in H2's covers H2, H3, H4, H5
and M6; the `Observed by` containment rule in M10's covers M10 and H8. Three predicates, thirteen of
the twenty-three, and each of them is a grep over eleven files.

## What round 3 should look like

Narrower, and later. Precision 0.87 with zero unverified says the fan is now returning what it is
primed to return; another pass at the same priming will mostly re-derive this report. The higher-value
sequence is: fold this round with the three predicates above rather than twenty-three edits, run the
predicates, and only then re-review — a round 3 that reads a spec set no predicate can fault is
worth a fan, and one that reads a set with fifteen known instances still in it is not.

Three items belong to the owner rather than to a build pass. B1 is the population question round 1
already ruled on once, and the ruling now has to be applied to `TOOL-aJoinedCanon-3` before anything
in this chain opens. H6 needs a decision on whether `govkit selfcheck` gains the conf-key-to-descriptor
arm at all, since eighteen live instances say the absence may be deliberate. And M5 is the fifth
build rule — no unit justifies a decision by a behaviour a lower-`order` sibling changes — which is a
README edit, not a spec edit, and should land before round 3 reads anything.
