**Serves:** spec-audit TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-5 TOOL-dFoldedVerdict-6

# Spec audit round 1 — the six-unit spec set of dFoldedVerdict, six units authored by five agents in parallel

*Node d, 2026-09-01, round 1, attended work on `branch/folded-verdict-9c2e41` at BASE `adc0543c`. The lenses were primed on CROSS-SPEC AGREEMENT as the highest-yield axis, because the six units were authored in parallel by five agents and none read another: BUILD-METHOD M2 requires them to agree on scope, interface, ordering and acceptance, and a disagreement between two specs is a defect in exactly one document. Units 1, 2 and 3 are one mechanism split three ways and were read as a triple; units 5 and 6 share one author and one file and were read for the opposite failure, a handoff assumed rather than stated. A finding survives here only where it joins a spec sentence to a MACHINE — a leg name resolvable in `tools/gate-legs.json`, a parser arm, an awk program, a line citation, a ratified decision id — and every citation below was re-derived against the tree by the author of this record before it was graded. Where a claim could be reproduced by running something, it was: the `--rescope` invocation, the `check-arms.py --report` counts, the section-8 conf-key extractor, the `gov:kit unattended@` carrier population and `id_in` against aClosedDocket's executing roster were all executed rather than reasoned about.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-1.md@405def8eb92a` · `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md@a743d1dfa24b` · `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md@f6d695c0bb97` · `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-4.md@eb18795c1dad` · `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-5.md@0601731dd4df` · `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-6.md@0e56f7eb3ed7`. **ROUND 1.**

## Verdict: BLOCKED

One blocker stands after adjudication, and it is unusual in that the spec states the OPPOSITE of what the gate does. Unit 3's S5 act 2 writes a `--rescope --act supersede` row whose successor lives in another build, and the spec's stated reason for writing it — "without that row check 24 reds, this unit trades one red for another otherwise" — is inverted at source: the row is what CREATES the red. The successor arm at `tools/unattended/check-unattended.sh:1777-1781` reds unless the successor is a whole token of THAT record's own executing roster, which is `memory/builds/aClosedDocket/README.md`'s `gen:build-units` region and carries only `TOOL-aClosedDocket-1` through `-4`. A `dFoldedVerdict` id can never be in it. The record is at `phase: BUILDING`, so the `LANDED|ABORTED` skip does not apply, and `verb_rescope` membership-tests only the unit and never the successor — so the driver ACCEPTS the write, `park()` appends it to an append-only record, and no verb can remove it. AC9 as written is unsatisfiable and AC7's corpus-wide exit 0 fails with it.

Nine highs stand beside it, and they are not scattered. Read together, this set has one dominant failure and it is the same one the predecessor build reported five rounds running: **a scope item that names a deliverable no acceptance criterion observes.** Nine of the twenty items below are that shape, across five of the six units — the CEILING half of the state gate (H1), the illegal-disposition branch (H2), the mixed-exit rule that has no carrier at all (H3), the protocol sentence three specs hand to each other and nobody owns (H4), the kit version bump that three specs assign to three different units (H9), plus M1 through M5. The second cluster is newer and is a direct product of parallel authorship: **four criteria are pinned to observations that a SIBLING unit is required to invalidate before the criterion is evaluated** (H5, H6, L1, and the `--review` sentence in H4). Both clusters are cheap to close in a fold; neither is a design problem.

The set is otherwise strong. The design work in units 1 and 4 is careful and repeatedly correct at source — unit 1's Q3 enumerates the nine `gov:kit unattended@` carriers correctly and records that the ratified `TOOL-aClosedDocket-4` S6 named only eight, and unit 1's AC9 correctly refutes that same ratified spec's floor claim in both directions. The irony of this round is that unit 2 then reproduces BOTH errors its sibling had already diagnosed, one spec over. That is the parallel-authorship tax, stated exactly: the corrections exist in the build and did not reach the units that needed them.

## Review shape

- raw 45, confirmed 28, refuted 17, unverified 0, precision 0.62.
- confirmed by severity as ADJUDICATED in this report: **1 BLOCKER · 9 HIGH · 9 MEDIUM · 1 LOW**, over 20 reported items.
- confirmed blockers: 1.
- the 28 confirmed findings collapse into 20 items here. Every merge is named in the item's own header so the filing and this report stay reconcilable. The largest merge is B1, which arrived twice from two lenses, and H7, which arrived three times.
- no finding went unverified: every confirmed item survived a skeptic prompted to refute it, and the author of this record re-derived each one against the tree before grading.

Precision is measured over the whole raw population of 45 and is unaffected by the merging, which happens after grading. 0.62 on a pre-code spec audit of six parallel-authored units is in line with the predecessor build's tuned rounds and well above its round-1 figure.

## The findings

| # | Sev | Unit | Address | One line |
|---|---|---|---|---|
| B1 | BLOCKER | 3 | §2 S5 act 2 · §4 · AC9 | the cross-build supersession row REDS check 24 rather than clearing it, permanently and on another build's record |
| H1 | HIGH | 1 | §6, all of AC1-AC12 | no criterion drives a CEILING round, though S3 makes the flag required there and S5 rewrites its success line |
| H2 | HIGH | 2 | §2 S3 · S10 fixtures · §6 | the illegal-disposition-VALUE refusal has neither a fixture nor a criterion |
| H3 | HIGH | 3 | §2 S4 · §4 Inventory · §5 | the mixed-exit rule is required to be "written down" and no file in scope carries it |
| H4 | HIGH | 1, 2, 5, 6 | u1 §2/§4/§5 · u2 N7 · u5 N2 · u6 N1 | the protocol's `--review` sentence goes false and no unit owns it; unit 5 then copies it verbatim into a new pair |
| H5 | HIGH | 3 | §6 AC1 · §2 S1 | AC1 pins the pre-unit-2 check-2 message, and unit 2 replaces that sentence at order 2 |
| H6 | HIGH | 6 | §4 anchor table · §6 AC5 | the section-8 conf-key tripwire is pinned at 29 keys; unit 2 is required to make it 30 |
| H7 | HIGH | 3 | §2 S5 · §4 command block | the one load-bearing invocation spells `--unit` where the parser takes `--item`, and is refused before writing |
| H8 | HIGH | 2 | §2 S11 · §6 AC7 · §4 files | raises a one-sided arms floor from 101 to 102 against an actual 169, and calls that proof |
| H9 | HIGH | 1, 2, 5 | u1 Q3 · u2 §7 · u5 §4 | the kit version bump has no owning scope item, and three specs name three different owners |
| M1 | MEDIUM | 1 | §6 vs §2 S5, S8a | nothing observes the FOLD success sentence, which is the unit's one user-visible outcome |
| M2 | MEDIUM | 1 | §2 S8 · §6 AC7 | the two suite call sites S8 names as deliverables have no criterion over the file |
| M3 | MEDIUM | 4 | §2 S11, S12, S13 · §6 | three prose carriers the unit FALSIFIES have no criterion; no gate reads sentence content |
| M4 | MEDIUM | 4 | §2 S9 · §6 AC15 | the only criterion touching the protocol pair is a parity check that passes whether or not the change happened |
| M5 | MEDIUM | 5 | §2 S7, S8 · §6 | the `kit.toml` rows and the Skill sentence have no criterion, and the adopter cannot cover them |
| M6 | MEDIUM | 2 | §6 AC8 | infers project-conf presence from check 22, which joins the project conf in one direction only |
| M7 | MEDIUM | 2 | §2 S7 vs u1 N1 | the `:317` aggregate is handed over and left in neither of the two states the spec accounts for |
| M8 | MEDIUM | 2 | §7 `kit version markers` | "the eight carriers" — there are nine, and unit 1 already diagnosed this exact undercount |
| M9 | MEDIUM | 3 | §10 · §4 provenance | two claims about prior records the records do not support, one of them reversed in direction |
| L1 | LOW | 2 | §6 AC11 | pins "check 2 branch 2", which the unit's own S6a renumbers to branch 3 |

---

### B1 — BLOCKER — the cross-build supersession REDS check 24, permanently, on another build's record

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md` §2 S5 act 2, §4 "The supersession, which is two acts", §6 AC9. *(Filed twice by two lenses; merged here.)*

**The defect.** S5's act 2 writes `--rescope aClosedDocket --act supersede ... --successor TOOL-dFoldedVerdict-3` into `memory/builds/aClosedDocket/RUN.md`. Check 24's third arm extracts every `item supersede <id> -> <succ>` and reds unless `id_in "$rs_now" "$rssucc"`, where `rs_now` is bound to THAT record's own build README `gen:build-units` region. Verified: `memory/builds/aClosedDocket/README.md`'s units region carries exactly `TOOL-aClosedDocket-1` through `-4`, `id_in` in `tools/unattended/lib-unattended.sh:37` is a whole-token match, and `memory/builds/aClosedDocket/RUN.md` is at `phase: BUILDING`, so the `LANDED|ABORTED` skip does not apply. A cross-build successor can never be a member. The spec's stated reason for the act is therefore inverted: the row does not clear a red, it creates one.

**Why it is a blocker and not a high.** `verb_rescope` membership-tests only the unit and never the successor, so the driver ACCEPTS the write; `park()` appends to an append-only record; no verb can remove it. The failure is on ANOTHER build's landed-adjacent record, it is permanent from the commit that writes it, and only a second hand edit could clear it. AC9 ("reports no check 24 failure for that record") is unsatisfiable as specced and AC7's corpus-wide exit 0 fails with it. The prior art settles the direction: `TOOL-dUnstalledConvoy-6` built this arm, and its own comment reads that a supersession which never landed its replacement is a retirement wearing a better name. `--act supersede` is a WITHIN-build mechanism and no record sanctions a cross-build successor.

**Fix.** Replace act 2 with `--act retire`, whose row carries no ` -> ` and therefore never reaches the successor arm; name `TOOL-dFoldedVerdict-3` in `--reason` instead. The RETIRE arm's `grep -qE "item (retire|supersede) $rsid"` is satisfied either way. State in §4 that check 24 has no cross-build supersession shape and that this is the reason. Rewrite AC9 to assert BOTH check-24 arms by name over that record. If a true cross-build supersession record is wanted, it is its own unit against `tools/unattended/check-unattended.sh:1776` with its own backlog row, not a scope item here.

**Left-shift gate.** `verb_rescope` in `tools/unattended/unattended.sh` should membership-test `$succ` against the same roster check 24 reads, and refuse at write time — a driver that accepts a write its own merge bar will red forever is the guard-shares-nothing-with-the-thing-it-guards shape. Add the refusal arm in `tools/unattended/check-unattended.test.sh` and let `check-arms.py` force it. That converts a permanent unremovable red into an immediate, correctable refusal.

---

### H1 — HIGH — the CEILING half of the state gate ships unobserved

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-1.md` §6, all of AC1-AC12, against §2 S3 and S5.

**The defect.** Verified by reading §6 in full: AC1 and AC5 drive NON-CONVERGENT, AC3 and AC4 drive CONVERGING, AC2 is a closed-set refusal, and AC6 through AC12 are gate, usage and arms observations. Not one criterion produces a CEILING round. Yet S3 makes the flag REQUIRED at CEILING, S5 replaces the CEILING success sentence at `tools/unattended/unattended.sh:3969` (confirmed present at source, and it still ends "The run promotes and lands anyway"), and §8's Q2 turns entirely on whether `fold` is legal there.

**Impact.** A build that wires the gate to NON-CONVERGENT only, or that leaves the ceiling sentence claiming promotion after recording a fold, passes AC1 through AC12 unchanged. Q2's chosen answer becomes a decision nobody can witness, and unit 2's clause 3 inherits the hole because it sets its needs-a-disposition flag for CEILING too. AC10 does not close it — it only asserts `check-unattended.sh`'s status is unchanged from BASE.

**Fix.** Two criteria, both on the scratch fixture AC7 already uses, so neither depends on the suite the owner has instructed not to run. One drives a subject to `RUNAWAY_CEILING` rounds with no `--disposition` and observes the absent-at-exit refusal naming the state CEILING. One records `--disposition fold` at CEILING and observes the rewritten success sentence in stdout. CEILING is reachable from a fixture: `review_state` at `unattended.sh:3859-3866` returns it once `n+1 >= RUNAWAY_CEILING` with shrinking counts, so this is a coverage hole and not an unobservable state.

**Left-shift gate.** Gateable and worth gating: a spec-format arm that joins §2 to §6 on CLOSED-SET STATE TOKENS. Every ALL-CAPS state name a §2 item names as a precondition (`CONVERGING`, `CONVERGED`, `NON-CONVERGENT`, `CEILING`) must occur at least once in §6. It is an awk join over one document, it has a failing case that can be staged, and it catches this whole item's class rather than this instance. Home: `tools/memory-tree/check-memory-hygiene.sh`'s spec-conformance block, beside check 12.

---

### H2 — HIGH — the illegal-disposition VALUE refusal has neither a fixture nor a criterion

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §2 S3 and S10's fixture list, unrepresented in §6.

**The defect.** S3 makes an out-of-set disposition VALUE in a record its own refusal, distinct from an absent one, on the express ground that reading it as absent would report the wrong cause; §4's outcome table carries the row. S10's fixture list enumerates fold-only, unlabelled, promote-short, promote-with-id, blank cutoff and malformed cutoff — no illegal-value fixture. §6's AC1-AC11 never exercise it either: AC1 covers absent, AC3 covers a malformed CUTOFF (a different branch), AC4 and AC5 cover fold and promote.

**Impact.** The one branch S3 exists for is the only clause-3 outcome with neither an arm nor a criterion. A build that folds the illegal value into the absent-disposition message satisfies every criterion while reporting the wrong cause on exactly the record class — a hand-edited one — that unit 3 is about to create. AC11 itself records that awk-composed messages sit outside `check-arms.py`'s population, so the arms gate cannot compensate.

**Fix.** Add an AC pairing a fixture whose terminal row reads `disposition promoted` (or any non-member) against the leg, observing a refusal that names the file, the subject and the illegal value, textually distinct from AC1's absent-disposition message. Add the matching fixture to S10's list.

**Left-shift gate.** Documented check, because the awk-composed message is outside `check-arms.py` by construction and that is recorded. Add to the spec-audit checklist: *every outcome row in a spec's §4 outcome table has a named fixture in the fixture list AND a numbered criterion; a row with neither is a branch nobody will observe.* The §4 table is already a machine-readable markdown table, so this becomes gateable the moment a fixture list is given a stable shape — worth a backlog row.

---

### H3 — HIGH — the mixed-exit rule is required to be written down and no file in scope carries it

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md` §2 S4, with §4 "Inventory" and §5 user-docs.

**The defect.** S4 requires the mixed-exit rule to be "written down" precisely because a rule discovered per record is a rule nobody applies next time. Verified by grepping the whole build for "mixed": the rule appears only in S4, its §4 discussion, its alternatives, and inside the disposition-source block that lands in `memory/builds/dMispairedQuote/RUN.md`. §4's Inventory table lists four paths and assigns none of them S4. AC1-AC11 never observe it. §5's user-docs row routes it to "§8 Q2", which asks only whether the protocol should sanction the provenance form of a source-suffixed key and recommends one sentence admitting a source-suffixed line — nothing about mixed exits. Units 5 and 6, the protocol and Skill units, never mention it.

**Impact.** The rule's only durable home becomes the per-record provenance block, which is exactly the burial S4 forbids. The build can complete every criterion with the rule existing nowhere a future exit's operator would read it, and the next mixed exit re-decides it from scratch.

**Fix.** Name a carrier in S4 and add a criterion over it — either a sentence in the protocol's verb or review section, owned by unit 5 or 6 with a matching scope item there, or a row in `memory/gotchas/` — plus an AC that greps the chosen file for the rule after the pass. If the owner wants it deferred, make S4 a non-goal with a backlog row instead of a scope item. A scope item with no carrier is worse than an honest deferral, because it reads as covered.

**Left-shift gate.** Same join as H1's, in its second direction: every §2 scope item must name at least one path that appears in §4's Inventory or Files-touched table. That is a machine-checkable table-to-table join over one document with an obvious failing case, and it catches H3, M3 and M5 together.

---

### H4 — HIGH — the protocol's `--review` sentence goes false, no unit owns it, and unit 5 copies it verbatim into a new pair

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-1.md` §2, §4 Files touched and §5 User docs; `...-2.md` N7; `...-5.md` N2; `...-6.md` N1. *(Filed twice from two directions; merged.)*

**The defect.** `memory/guides/UNATTENDED-PROTOCOL.md`'s `--review` bullet states that at the exit every blocker still standing is promoted to a unit rather than parked, and enumerates the verb's refusals as exactly three. Unit 1's S3 makes `fold` a legal exit disposition and adds three new refusals, so both halves of that sentence go false. Unit 1 §5 says user docs are none owed, its Files-touched table lists only `unattended.sh` and `unattended.test.sh`, and grep confirms the spec never names the protocol document at all. Unit 2's N7 explicitly assigns that sentence to unit 1. Unit 3 writes records only; unit 4's subject is `agent-cap`. Unit 5's N2 moves §7's bullets VERBATIM and forbids rewording; unit 6's N1 puts the new carrier out of subject.

**Impact.** The binding contract every run reads keeps stating promotion as the only disposition and omits three new refusals, in BOTH byte-identical halves — which check 10 can never see, by its own header, since it compares the two copies to each other and says nothing about whether either is TRUE. Worse: the sentence sits inside the range unit 5 moves verbatim into a brand-new byte-compared pair that unit 6 then excludes from compression, so the build ends by copying a falsified sentence into a fresh pair nothing revisits. This is the producer-less handoff in its purest form — N7 hands a carrier to a unit that owns no carriers.

**Fix.** Give the sentence one owner. Either add it to unit 1 §2 with a §6 criterion (unit 1 is order 1, so it lands before unit 5's move), or add a scope item to unit 5 amending that one bullet during the move and carve the exception explicitly out of its N2. Then correct N7 to name whichever unit takes it, and cite the line by SECTION rather than by a line number the move will invalidate.

**Left-shift gate.** A cross-spec arm, and this build is the argument for building it: any `N`-item in one spec that assigns work to a named sibling unit must be matched by a scope item in that sibling naming the same path. It is a grep join across the six spec files of one build, it has an obvious failing case, and it catches the single class this parallel-authored set produced most. Home: a new arm in the memory-tree spec-conformance block, scoped to specs sharing a build folder.

---

### H5 — HIGH — AC1 pins a message unit 2 replaces two units earlier, on the reproduce-before-writing gate

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md` §6 AC1, and §2 S1.

**The defect.** AC1 pins the pre-unit-2 check-2 message — one record named, with "the counts 2 and 1" — but this unit is order 3, after unit 2 replaces that sentence. Unit 2 states the consequence twice: its §4 Migration says outright that it changes the sentence the red carries, from a shortfall claim to an absent-disposition refusal, and its AC1 names both `memory/builds/dBriefedPass/RUN.md` and `memory/builds/dMispairedQuote/RUN.md` for recording no disposition. The "counts 2 and 1" wording belongs to the pre-cutoff shortfall message, which unit 2's S7 keeps only for records the cutoff does not grade. Unit 3's own Rollout says it runs after units 1 and 2, so AC1's pinned message and S1's "confirm the message" cannot both be satisfied as worded.

**Impact.** The reproduce-before-writing gate cannot pass. A builder taking AC1 literally either reports unit 2 as having broken the leg, or waives the observation and skips S1's "is the red actually true" check — which is the ONE control on inventing a disposition to clear a gate. That is why this grades HIGH rather than MEDIUM: the criterion that fails is the integrity control, not a coverage nicety.

**Fix.** Restate AC1 against the message unit 2 ships at this unit's pre-image, and keep §4's verbatim quote under an explicit "at BASE `adc0543c`" label with a second row for the post-unit-2 message, so the reproduction step has a target that exists when it runs.

**Left-shift gate.** Documented check, and it is the second-largest class in this round: *a criterion that quotes an observation must state WHICH image it was taken at, and a spec at order N may not pin a BASE observation that a sibling at order < N is scoped to change.* Add to the spec-audit checklist and to the build's regrounding step. Partially gateable — a spec's §6 quoting a literal that a lower-ordered sibling's §2 declares it edits is a grep join across one build's spec set, the same machinery H4 asks for.

---

### H6 — HIGH — the compression pass's only section-8 tripwire is calibrated against a number a sibling must move

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-6.md` §4 anchor table (conf-key row) and §6 AC5. *(Filed twice; merged.)*

**The defect.** AC5 pins the section-8 conf-key extractor at "exactly what it yielded at BASE" and spells the expected value as 29 keys. Reproduced with the leg's own extractor — `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'` over `memory/guides/UNATTENDED-PROTOCOL.md`, first table cell, backticked ALL-CAPS, `sort -u` — and BASE does yield exactly 29, so the figure is right for BASE. But unit 2's S12 is unconditional IN-scope at order 2, and it must be: check 22 joins `.unattended.conf.example`, the section-8 table and the project conf, so `DISPOSITION_CUTOFF` has to be added to that table. Unit 2's F3 refuses option C outright, so the row lands before unit 6 runs under every recommended path. At unit 6's evaluation the extractor yields 30.

**Impact.** A criterion that is false by construction at the moment it is graded. A correct compression fails AC5; the literal remedy — restore what BASE yielded — is to delete a sibling's mandatory row, which reds check 22 instead. The likelier outcome is that the builder silently adjusts the number, which destroys the only property AC5 has: that a reworded anchor is caught by a count nobody may edit. The spec's own anchor table proves the author tracked sibling-induced anchor movement for one row (the verb bullets, annotated as moving to the new carrier at order 5) and missed it for this one.

**Fix.** State AC5's expectation relationally — "the extractor yields the same key set as this unit's pinned pre-image, measured after `TOOL-dFoldedVerdict-2` lands" — and record the observed number in the build record at §4 method step 1 rather than pinning 29 in the spec. §4's table row takes the same edit.

**Left-shift gate.** Same gate as H5, and this is the strongest argument for it: a compression pass whose one machine tripwire is a literal count is exactly where a stale pin does the most damage. Beyond that, the durable form is the one the charter already states — a count of a derived population is not written in prose. AC5 should DERIVE its expectation at run time from the pre-image, not carry it.

---

### H7 — HIGH — the one load-bearing invocation is spelled with a flag the parser does not accept

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md` §2 S5 and the §4 command block. *(Filed three times by three lenses; merged.)*

**The defect.** The invocation spells `--unit TOOL-aClosedDocket-4`. Verified at source: the arg loop binds `--item` to `PK_ITEM` at `tools/unattended/unattended.sh:4781` and `--unit` to `BR_UNIT` at `:4783`, which only `--brief` reads; the dispatch at `:4852` passes `$PK_ITEM` as `verb_rescope`'s third positional; the driver's own header at `:14` spells it `--rescope <slug> --act <...> --item <id>`. Reproduced: running the command exactly as S5 writes it returns `UNATTENDED check 48 FAILED — --rescope --unit is not id-shaped by the driver's own spelling … (none)`. Grep for a second `--unit)` arm or alias returns none.

**Impact.** As written, PK_ITEM is empty and the verb refuses before writing anything. S5 calls this half not optional and §4 says check 24 reds without the row, so the spec's one load-bearing invocation cannot run. The trap is worth recording: `verb_rescope`'s own refusal TEXTS call the parameter `--unit` while the parser takes `--item`, so the spec copied the message rather than the parser, and the same misspelling appears in `TOOL-dUnstalledConvoy-5`'s AC1 — it reads as a house spelling rather than an error.

**Fix.** Spell it `--item TOOL-aClosedDocket-4`, matching the driver header. Add one sentence to §4 noting that the driver's `fail 48` texts name a flag the parser does not accept, so a reader who copies the refusal is misled. Note that B1's fix changes `--act supersede` to `--act retire` in the same command; both edits land together.

**Left-shift gate.** Real and cheap: `verb_rescope`'s refusal strings should name the flag the PARSER accepts. A gate leg is available — the arms harness already reads those messages, so a check that every flag name appearing in a refusal string occurs as a `case` arm in the same script's parser is an awk pass over one file with a stageable failing case. That kills the class, which has now produced the same error in two builds.

---

### H8 — HIGH — a one-sided floor raise is presented as proof that a new branch is armed

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §2 S11, §6 AC7, and the §4 Files-touched row for `.memory-tree.conf`.

**The defect.** S11 moves `ARMS_FLOORS` for `tools/unattended/check-unattended.sh` from `101:100` to `102:101`, and AC7 makes that raise the proof that S6's new branch is both counted and armed. Verified by running the tool: `check-arms.py --report` shows that file at **169 branches / 161 armed** against floors 101/100, and `tools/memory-tree/check-arms.py:288` reds only on `got[i] < want[i]` — one-sided minimums. Raising a minimum from 101 to 102 against an actual 169 cannot fail and proves nothing about any new branch.

**Impact.** A criterion that cannot fail on the absence of the change it grades — the shape this repo names explicitly, and the one this build exists to remove. Worse as a cross-spec matter: this build has ALREADY corrected it. Unit 1's AC9 records at source that the ratified `TOOL-aClosedDocket-4` AC9 asserted the opposite in both directions and is false, and unit 5's N6 independently measures the same file and concludes no floor moves. Three siblings, two answers, and the wrong one is the ratified one being carried forward.

**Fix.** Delete S11 and the `.memory-tree.conf` row from Files-touched. Rewrite AC7 to assert what actually grades the new branch: `check-arms.py --check` exits 0 AND `--report` shows the branch and armed counts both risen by the number added, with the new `fail 2` branch listed ARMED on its own message signature. Cite unit 1's AC9 so the corrected reading is recorded once for the build.

**Left-shift gate.** The generalisable form: a criterion whose predicate is a floor, cap, ceiling or minimum must state the MEASURED value beside the floor, so a reader can see the slack. Add to the spec-audit checklist. It is not gateable in general, but the specific instance is: `check-arms.py` could WARN when a declared floor sits below half the measured count, which turns a decorative floor into a visible one.

---

### H9 — HIGH — the kit version bump has no owning scope item, and three specs name three different owners

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-5.md` §4 Files touched (no §2 item); `...-1.md` §8 Q3; `...-2.md` §7.

**The defect.** Unit 5's Files-touched lists `tools/unattended/unattended.sh` and every `gov:kit unattended@` marker as "the version bump", while S1-S10 contain no item scoping it, and AC7 only asserts `tools/check-kit-versions.sh` exits 0 — which that script satisfies by AGREEMENT at 1.14, never by movement, since its comparator asserts markers equal `KIT_UNATTENDED_VERSION`. Meanwhile unit 1's Q3 defers the bump to "the build's last landing unit", which is order 6, whose N5 forbids touching any script; and unit 2's §7 asserts the opposite as fact, that the bump is the build's and belongs to order 1, with no producer before it.

**Impact.** No unit in the set owns the bump. Either it does not happen, or one unit edits a shipped driver with no scope item authorizing it. BUILD-METHOD M2 makes a disagreement between two specs a defect in exactly one document, and here there are three documents and three answers.

**Fix.** Give the bump one owning scope item in exactly one unit; add a criterion there that the version DIFFERS from 1.14 and that `check-kit-versions.sh` exits 0. Cite the carrier population from source rather than restating it (see M8). Correct unit 1's Q3 and unit 2's §7 to point at whichever unit takes it.

**Left-shift gate.** Same cross-spec arm as H4: a deliverable named in one spec's Files-touched with no §2 item in that spec, and no §2 item in any sibling, is an ownerless deliverable. A grep join over one build's spec set. Separately, `tools/check-kit-versions.sh` cannot distinguish "bumped in step" from "never bumped" — a DoD that requires a bump should assert movement against the pre-image, not agreement.

---

### M1 — MEDIUM — nothing observes the FOLD success sentence

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-1.md` §6, against §2 S5 and S8a.

**The defect.** `tools/unattended/unattended.sh:3968`'s NON-CONVERGENT echo hard-codes the promotion sentence — confirmed at source, it ends with every blocker still standing being PROMOTED — and S5 exists to split it. AC1 observes only the row in `RUN.md` and says so explicitly, not by reading the source; AC7 pins the literal PROMOTED on the promote call only; AC8's `check-arms` grades fail-branch coverage, not success text. S8a's "a second arm covers the fold sentence" lives in `unattended.test.sh`, which AC7 states may not be run under the standing owner instruction, and no criterion witnesses it.

**Impact.** S5's stated defect — that the driver would refuse a fold and then tell the run it had promoted — is the unit's one user-visible outcome and it ships ungraded. A commit that adds the flag and the row while leaving the echo hard-coded to the promotion sentence passes AC1 through AC12.

**Fix.** Add an AC: a successful `--disposition fold` on a NON-CONVERGENT round prints a sentence naming the fold and NOT containing the literal PROMOTED, observed in the stdout of the same scratch-fixture invocation AC1 already makes.

**Left-shift gate.** Documented check: *where a scope item's stated defect is user-visible TEXT, at least one criterion must observe that text in stdout.* Add to the spec-audit checklist. The general principle already sits in the charter — a check that exercises the change, never an assertion — and this is its spec-time form.

---

### M2 — MEDIUM — the suite call sites S8 names as deliverables have no criterion

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-1.md` §2 S8 and §6 AC7.

**The defect.** S8 names two concrete deliverables by line — `tools/unattended/unattended.test.sh:4468` and `:4475`, both NON-CONVERGENT after S3 and therefore refusals — and §5 calls them the live risk. AC7 then witnesses the two SEQUENCES by direct invocation on a scratch fixture and explicitly not by the suite, so it observes the driver and never the suite file. AC8's `check-arms` scan forces arms for NEW fail branches only, and it matches branch message text rather than call correctness, so the test file gets touched but the two stale calls are not graded.

**Impact.** A commit that never touches `unattended.test.sh` satisfies every criterion while leaving two calls the shipped driver now refuses — a red that surfaces on whichever node next runs the suite, which is exactly the node that did not write it.

**Fix.** Add an AC over the file TEXT, runnable without executing the suite: `grep -n -- '--disposition' tools/unattended/unattended.test.sh` returns hits at the two call sites S8 names, and the PROMOTED assertion below them is unchanged. A static observation was available and cheap, so this is a closable gap rather than a cost of the do-not-run instruction.

**Left-shift gate.** Documented check, and a useful one under the standing owner instruction: *when a suite may not be RUN, its file is still a deliverable and is graded by grep.* A criterion may not cite the do-not-run instruction as a reason to observe nothing.

---

### M3 — MEDIUM — three prose carriers the unit falsifies have no criterion, and no gate reads sentence content

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-4.md` §2 S11, S12, S13, unrepresented in §6.

**The defect.** Three scope items have no acceptance criterion: the two dossier sentences at `memory/map/features/agent-cap.md:75` and `memory/map/features/unattended.md:49`, the `tools/workflows/unattended-build.js:41-58` header comment, and the backlog row for the `for await` and `do-while` holes. §6's AC1-AC19 never name a map file, a workflow header, or `memory/backlog/TOOL.md`. AC16 runs `check-agent-cap-restatement.sh`, whose header states it only hunts a bound word adjacent to a digit in markdown; AC17 greps only `tools/hooks/README.md`.

**Impact.** These are the three prose carriers the unit falsifies. I read `tools/codebase-map/test_codebase_map.py`: freshness is a byte-compare of generated artifacts and coverage grades claimed keys — neither reads dossier sentence content, and `workflow script syntax` parses the script. So all three can be skipped silently, leaving the map asserting that both markers are CLAIMS and that the hook denies an `agent()` in any loop body after the change that makes both false, with the declared out-of-scope evasions unrecorded.

**Fix.** One criterion covering all three: after the pass, `grep -n 'gov:sequential-agents'` returns a hit in each of the two dossiers and the workflow header, the falsified sentence is gone from `agent-cap.md`, and `grep -n 'for await' memory/backlog/TOOL.md` names the new row under this build's slug.

**Left-shift gate.** The §2-to-§4-Inventory join from H3 catches this at spec time. At code time the durable form is different and worth a backlog row: the codebase-map dossiers have coverage and freshness gates but no gate on PROSE truth, and this is at least the second build to falsify a dossier sentence with every map leg green. A candidate is a marker-adjacency arm — a dossier sentence quoting a hook's behaviour carries the marker spelling it describes, so a rename reds.

---

### M4 — MEDIUM — the only criterion touching the protocol pair is a parity check that cannot fail on the change's absence

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-4.md` §2 S9 and §6 AC15.

**The defect.** S9 amends the "Everything else is denied" sentence in `tools/workflows/REVIEW-PROTOCOL.template.md` (verified at `:125`, with the identical line at `memory/guides/REVIEW-PROTOCOL.md:125`). AC15 asserts `check-verifier-fanout.sh` exits 0 and that `check-protocol-parity.test.sh` reports parity between template and render. Parity is a template-versus-render comparison, so it passes byte-identically whether or not the sentence was ever amended. AC16's restatement gate keys on a bound word next to a digit, not on this sentence, so nothing else covers S9.

**Impact.** A criterion that cannot fail on the absence of the change it is meant to grade. The protocol pair keeps stating that every loop-body `agent()` is denied, in both copies — which is the shared-error class unit 6's own S1 documents as having already produced four live defects in the sibling protocol.

**Fix.** Add an observation with a failing case, on AC17's shape: `grep -c 'gov:sequential-agents'` returns at least one in each of `tools/workflows/REVIEW-PROTOCOL.template.md` and `memory/guides/REVIEW-PROTOCOL.md`, AND the parity check is green. The PAIR of observations, not parity alone.

**Left-shift gate.** Documented check with a sharp wording, because this is the third instance of the shape in this set: *a parity, byte-compare or freshness check is never evidence that a CONTENT change happened. It proves two copies agree, including on being wrong.* The gates themselves already say so in their own headers; the checklist item makes a spec author read it.

---

### M5 — MEDIUM — the kit.toml rows and the Skill sentence have no criterion, and the adopter check cannot reach them

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-5.md` §2 S7 and S8, unrepresented in §6.

**The defect.** S7 (the `kit.toml` `[[files]]` and `[[lf_pin]]` rows) and S8 (the `SKILL.template.md:9` sentence naming both carriers) have no criterion. Verified: `tools/unattended/adopt-unattended.sh` contains ZERO references to `kit.toml` — it hard-codes `PROTO_SHIP`/`PROTO_REL` and `PBT_SHIP`/`PBT_REL` at `:183-190` — so AC6's adopter `--check` cannot cover S7. Nor does the bar: govkit's per-file arm is satisfied for the kit half by the existing `include = "**"` engine rule in `tools/unattended/kit.toml`, and its surface globs do not reach `memory/guides`, so a missing rendered `[[files]]` row reds nothing. AC1-AC12 never name `kit.toml`, and never run govkit selfcheck or install-prefix, both of which are named only in §7. AC6 grades the render's BYTES, not S8's sentence.

**Impact.** The install of the new pair can be green in gov while the kit ships undeclared to adopters, and the Skill can keep telling a reading agent that `UNATTENDED-PROTOCOL.md` is the one binding contract after the verbs have left it.

**Fix.** Two criteria: the govkit selfcheck leg exits 0 with the new destination declared and unique; and `grep -n 'UNATTENDED-VERBS'` returns a hit in both `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md`, with the adopter's `--check` green over the regenerated render.

**Left-shift gate.** Real and narrow: `tools/unattended/adopt-unattended.sh` hard-codes the paths its own `kit.toml` declares, so the two can drift silently. Either the adopter reads the descriptor, or a check asserts that every `[[files]]` destination in `tools/unattended/kit.toml` appears in the adopter script. The second is a ten-line awk join with a stageable failing case. Backlog row either way.

---

### M6 — MEDIUM — AC8 infers project-conf presence from a check that joins in one direction only

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §6 AC8.

**The defect.** AC8 infers from a green check 22 that `DISPOSITION_CUTOFF` is present in `.unattended.conf`. Verified at source: check 22 grades the example conf against the section-8 table in BOTH directions, but the PROJECT conf in one only — `proj_extra` at `tools/unattended/check-unattended.sh:1311` is keys the project declares that the table does not document — and its own inline comment says an optional key the project never sets is not a fault.

**Impact.** A commit that adds the key to `.unattended.conf.example` and the section-8 table but forgets `.unattended.conf` passes AC8, passes check 22, and passes the whole bar — while S5's blank-cutoff path grandfathers every record and the new predicate grades nothing. The unit lands inert with a green gate, which is the green-by-absence shape it exists to remove. §4's cutoff subsection never states the join's direction.

**Fix.** Replace AC8's inference with a direct observation — `grep -n '^DISPOSITION_CUTOFF=' .unattended.conf` returns the declared date — and keep check 22 as the criterion for the example-conf and section-8 halves only, saying explicitly that it cannot observe the project declaration.

**Left-shift gate.** The gate's own header already states its direction, which is the correct design; the failure is a spec author inferring past it. Documented check: *a criterion may not infer PRESENCE from a green gate whose header states it grades a different direction or population.* Where a criterion cites a gate, it cites the arm.

---

### M7 — MEDIUM — the `:317` aggregate is handed over and left in neither state the spec accounts for

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §2 S7, against unit 1's N1.

**The defect.** Unit 1's N1 explicitly hands unit 2 the aggregate text at `:317` that says a subject exited without promoting. S7 enumerates only the three clause-3 messages plus the unreadable-BASE one and never says whether that outer `fail 2` sentence changes; grep over unit 2 finds no other reference to it. The live line reads `review loops that ran past the ceiling, stalled without recording it, or exited without promoting`. After S2 and S3 a record can red for recording NO disposition or an ILLEGAL one, neither of which is any of those three things.

**Impact.** Either the aggregate keeps a sentence that is false once folds are legal, reporting the wrong cause under a header S3 exists to make precise; or it is reworded and strands the arm. Verified: `check-arms.py --report` lists `check 2 branch 2` at line 317 as ARMED on that literal alone, and no scope item in S9 or S10 updates that arm, so a rewording sends the branch unarmed-and-unpinned and reds `harness arms`. Unit 2's own AC11 also relies on the literal. The handoff lands in neither state the spec accounts for.

**Fix.** S7 states explicitly whether `:317` is reworded. If it is, name the assertion in `tools/unattended/check-unattended.test.sh` that must move in the same commit and add an AC over it. If it is not, say so and record why the sentence stays true.

**Left-shift gate.** The arms gate already catches the rewording half — it reds on an unarmed branch — so the durable left-shift is the spec-time half: *an `N`-item handing a line to a sibling must be answered by a scope item in that sibling that names the same line, in one of exactly two states: changed with its arm, or unchanged with a reason.* Same cross-spec arm as H4.

---

### M8 — MEDIUM — "the eight carriers" — there are nine, and the sibling spec already diagnosed this exact undercount

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §7, the `kit version markers` bullet. *(Filed three times; merged.)*

**The defect.** Measured on this tree, `gov:kit unattended@` has NINE live carriers: the constant plus a same-line marker in `tools/unattended/unattended.sh:42`, `tools/unattended/check-unattended.sh:40` and `tools/unattended/check-pass-order.sh:29`; the three `tools/unattended/*.template.md` files; and the three renders `memory/guides/UNATTENDED-PROTOCOL.md`, `memory/guides/PLAYBOOK-TEMPLATE.md` and `.claude/skills/unattended/SKILL.md`. Unit 2 §7 says eight.

**Impact.** `tools/check-kit-versions.sh` loops all three shell files and asserts both the constant and the same-line marker, so `check-pass-order.sh` is inside the population unit 2 undercounts. A builder bumping from this bullet leaves it behind and reds `kit version markers`. The bullet is not idle prose — it also owns a conditional bump. And unit 1's Q3 enumerates all nine and records that omitting `check-pass-order.sh` is PRECISELY the error the ratified `TOOL-aClosedDocket-4` S6 made, so the sibling spec reproduces the miscount unit 1 diagnosed. Unit 5 then adds carriers, so the figure is wrong in a second direction by the time a bump lands.

**Fix.** Delete the count and point at unit 1's §8 Q3 enumeration, or at `git grep -l 'gov:kit unattended@'` over the three trees. Do not restate the number in a third place.

**Left-shift gate.** The charter already gates this in principle — no count of a derived population is written in prose — and this is the second build to break it on the same population. Gateable: an arm that finds a spelled-out cardinal or digit within a short window of the literal `gov:kit unattended@` in any tracked markdown, and reds. Narrow, cheap, has a failing case, and it fires on both offending specs today. Home: beside `tools/check-kit-versions.sh`, which already owns the population.

---

### M9 — MEDIUM — two claims about prior records the records do not support, one of them reversed

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-3.md` §10 Reuse audit (last paragraph) and §4 "The provenance block, and the precedent it copies". *(Filed twice; merged.)*

**The defect.** §10 describes the `TOOL-dMispairedQuote-7` row as the row that records this build's supersession of the ratified predecessor. Verified at `memory/backlog/TOOL.md`: the row's own text records the OPPOSITE relation — it is SUPERSEDED BY that predecessor — and it names no `dFoldedVerdict` id anywhere. Separately, §4 cites `memory/builds/aGroundedOrientation/RUN.md:11` for the `landed-anchor-source:` precedent; that key is at `:17`, and `:11` is the `## Run facts` heading. §4 and §10 both carry the bad line number.

**Impact.** A reader checking the supersession chain from §10 finds a row pointing the other way and concludes the chain is recorded when it is not. And after S5 flips the predecessor to WONTDO, that row's successor pointer names a WONTDO unit: unit 3's Inventory edits no backlog file, and unit 2's S13 edit of the same row is scoped to the two rows that unit answers rather than to the successor pointer. So the backlog's only route from the measured defect to its fix goes stale in the same commit that fixes it.

**Fix.** Correct the §10 sentence to what the row says. Add an explicit item — in unit 3's S5 or unit 2's S13, but in exactly one — repointing that row's successor at the `dFoldedVerdict` ids that answer it, and name `memory/backlog/TOOL.md` in the owning unit's Inventory. Fix the `aGroundedOrientation/RUN.md` citation to `:17`.

**Left-shift gate.** Documented check for the direction half — *a reuse-audit sentence describing a prior record quotes it, rather than paraphrasing its relation* — since paraphrase is where the reversal happened. The line-number half is gateable and probably should be: a check that a `path:NNN` citation in a spec resolves to a line whose content matches a quoted token, wherever the spec quotes one. That is a real gate with a failing case, and this round found two stale citations by hand.

---

### L1 — LOW — AC11 pins the branch ordinal that the unit's own S6a renumbers

**Address.** `memory/builds/dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md` §6 AC11.

**The defect.** AC11's corroboration names `check 2 branch 2` as the ARMED aggregate branch. Verified today: `check-arms.py --report` lists check 2 branch 1 at line 251 and branch 2 at line 317. S6 puts the new `DISPOSITION_CUTOFF` refusal beside the `:251` refusal, i.e. above 317, and S6a states the consequence itself — the pinned ordinals move from 9, 10, 11 to 10, 11, 12. So the aggregate becomes branch 3, and the spec performs the renumber in one scope item while pinning the pre-renumber ordinal in a criterion.

**Impact.** A criterion stale by construction. A builder checking AC11 literally reads the new cutoff refusal and either fails a correct change or accepts the wrong branch as evidence. Low, because the report prints the message text beside the ordinal and a careful reader recovers immediately.

**Fix.** Drop the branch number and corroborate on the literal: `--report` lists the branch whose signature begins "review loops that ran past the ceiling" as ARMED, whatever ordinal it holds after the insertion.

**Left-shift gate.** Documented check, same family as H5 and H6: *a criterion never pins an ORDINAL into a list the same unit inserts into.* Name the row by its content. This is the cheapest of the four ordinal or count pins this round found and the clearest statement of the rule.

## What this round says about the build

Three classes account for eighteen of the twenty items, and each has a different cure.

**The scope item with no criterion — nine items, five units.** This was the single largest finding category across five rounds on the predecessor build, and it is the largest here. The cure is mechanical and is proposed above twice: a table-to-table join inside one spec (§2 items against §4 Inventory) and a grep join across one build's spec set (an `N`-item's named sibling must carry a matching scope item). Both are awk over markdown with obvious failing cases. Neither exists today, and this build is now the second consecutive one to pay for their absence.

**The criterion pinned to a pre-image a sibling invalidates — four items.** This class is NEW and it is a direct product of parallel authorship: five agents each pinned to BASE `adc0543c` and none could see what a lower-ordered sibling would change under them. H5 and H6 are the expensive ones because both land on the unit's only real tripwire. The cure is a rule the build method can carry without any tooling: a criterion states the image its observation was taken at, and a spec at order N may not pin a BASE observation a sibling at order less than N is scoped to change. The regrounding step is where it belongs.

**The count typed beside a population the tree owns — two items, and one of them is a repeat.** M8 is the sharper of the two, because unit 1's Q3 diagnoses the identical undercount in the ratified predecessor and unit 2 reproduces it one spec over. The charter already forbids this and the fix is a narrow, cheap gate that would red both specs today.

One observation about method, offered because it was visible from outside. The corrections this build most needed already existed INSIDE it — unit 1's Q3 had the carrier count right and unit 1's AC9 had the floor claim right — and they did not reach units 2 and 5. Parallel authorship bought speed and cost cross-reading, exactly as expected; what it did not buy is a step where the specs are read against each other before they are ratified. That step is this record. It found one blocker and nine highs in a set whose individual units are, on their own, well-argued.
