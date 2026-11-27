**Serves:** diff-review TOOL-aAnsweredPark-1

# Closing diff review, round 1: TOOL-aAnsweredPark-1, the position engine's owner-decision interrupt

Tier-2 · 2026-11-25 · on `branch/nervous-mayer-a90301` · adversarial fan through `tier2-review.js`: 5 finder lenses (`gov-diff-reviewer`), 3 skeptic batches (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The diff spans 17 files, +950/−47 (PINNED 2026-11-25). A parked `decision` row of a run-state file now settles only by its own tracked disposition record. Only an open decision row, or a hold while `phase` reads `HELD`, interrupts. Every line ref below is pinned to the blob at the reviewed sha `9981f34e`.

**Reviewed range:** `3d6c1702afb6c2e86638785950d80657a187192c...9981f34e05da975039caf7e93af774310d7f623b`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. Three items are MEDIUM. M1 is an answered question that cannot be raised again in the same words, because the driver's park no-ops still match answered rows. M2 and M3 are conditions of the settle rule that no arm can turn red. The two LOW items are an arm's missing phases and a contradictory ledger paragraph. The shipped settle rule and hold rule are judged correct in M2, M3 and L1.

## Review shape

Intensity **full** · raw **6** · confirmed **5** · refuted **1** · merged **0** · unverified **0** (0 uncertain) · precision **0.83**.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

No two confirmed findings describe one defect, so the 5 confirmed findings form **5 items**. Ids 4, 5 and 6 share a class and not a defect.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 3 MEDIUM · 2 LOW** (5 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 3 MEDIUM · 2 LOW** (5 findings).

Every id keeps its bracketed binding grade, and I re-grade none.

No twin flag is raised. Refuted id 2 concerns a row whose item opens with a space, which the row pattern does not count. It is not the defect of any confirmed finding.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **3/3** returned, **0 DIED**.
- **0** contradictory verdicts were demoted to unverified, and **0** orphaned duplicate refutations were demoted to unverified.
- **0** duplicate refutations were counted as merged confirmations.
- **0** spurious verdicts were discarded, and **0** duplicates were found.
- Fixes on confirmed findings: **3** judged sound (ids 3, 4, 5), **1** judged UNSOUND (id 1), **1** judged INSTANCE-ONLY (id 6), **0** none proposed, **0** NOT JUDGED. An INSTANCE-ONLY fix cures the cited instance and leaves its class standing.
- Severity on confirmed findings: **0** UNGRADED by the skeptic, **0** RE-GRADED by the skeptic.
- Unverified findings: **0** answered UNCERTAIN by a skeptic, **0** with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 31 items, acquired by the harness from `--for-diff 3d6c1702afb6c2e86638785950d80657a187192c..HEAD`. Each was assigned to exactly one of 5 lenses: security 7, correctness 6, seams 6, verification 6, intent 6.
- By design: the caller's byDesign.
- Refuted findings shown: 1. Same-address pairs shown: 0.
- Dispositions: unclassed values are refused. 31 class slugs were handed, and 226 leg names were read from `tools/gate-legs.json`.

Every integrity count is zero where it must be, so the run is complete. The zero yield of the seams and intent lenses is evidence for those lenses' shares only.

No finding on this list was run end to end by a skeptic. Id 1 was read from the code, and ids 4, 5 and 6 were judged from source. The finder of ids 4, 5 and 6 did run in-memory mutants.

## MEDIUM

### M1 — a question asked again in the same words after its answer is settled in advance (id 1)

- **Where:** `tools/loop/position.py@edc79dc3:697`, where the tag is built from the row's timestamp alone, and lines 703-708, where a record settles by that tag. The driver halves are `tools/unattended/unattended.sh@9b83204c:17645` (`verb_park`, lines 17645-17652) and `tools/unattended/unattended.sh@9b83204c:9592` (the `--exhausted` ending, lines 9592-9595).
- **What is wrong:** The driver's two park writers skip a write when a matching row already stands. `--park` compares `decision · item <i> · reason <r>` with the timestamp stripped, and on a match prints `decision already parked, unchanged`, writes nothing and returns 0. `--exhausted` keeps the first `flow.on-exhausted` row. Neither asks whether the standing row is answered. At base this was safe, because every owed decision row interrupted for the life of the run. This diff closes an answered row, so the no-op now matches a row that no longer interrupts, and no new row or tag is written.
- **Consequence:** After a row is answered, the same item and reason parked again, or a raised budget spent a second time, raises no owner-decision interrupt. The run may answer `act` with a question it has just raised unanswered, while the driver reports success and the docs say "A newly parked decision stops the run". The effect is contained: it needs an identical item and reason, the question already carries an owner answer, and a caller that goes on to `--handoff` reaches phase `HELD`, which interrupts. A bare `--park` has no such backstop.
- **Fix (the finder's proposal was REJECTED by the skeptic; this is the skeptic's corrected fix):** Keep both no-ops for replay, and keep the first ending as recorded. Where the matching row is already answered, the driver must say so instead of reporting plain success. `--park` prints that the row is answered and that a new question needs a different reason. `--exhausted` prints that the standing row is answered and that a new owner question goes through `--handoff --code owner-decision`. State the same limit in the `position.py` docstring, in `help/loop.md` and in `tools/loop/README.md`, beside "A newly parked decision stops the run". File the driver half as an unattended-kit ask.
- **Left-shift gate:** For the driver half, add an arm to the suite behind the `unattended kit gate` leg. It parks an item and reason, stages an `answered` record for the row's tag, parks the same item and reason again, and expects the output to say the row is answered. The same arm for a second `--exhausted` covers the sibling.

### M2 — no arm feeds the build filter or the malformed filter a record it would reject (id 4)

- **Where:** `tools/loop/adapt.py@42ad9fb5:237` (`read_newest_dispositions`). The arms are `FX_PARKED` at `tools/loop/position.py@edc79dc3:313` and `run_parked_plant`.
- **What is wrong:** Spec S1 says a row settles only by a well-formed record of the same build, and says AC1 to AC3 observe it. `FX_PARKED` holds only `(tag, word, reason)` triples. `run_parked_plant` writes every one through `write_disposition` under `FX_SLUG`, a validating door. Each record is therefore well-formed and of this build. The reader walks every build's records, and the tag names no build, so line 237 is the only enforcement of both conditions. Dropping `r["build"] != build or`, and separately dropping `r["malformed"] or`, left both new plants `held`.
- **Consequence:** If the build filter regresses, another build's `answered` record of the same second settles this build's open decision. If the malformed filter regresses, a malformed record can settle one. Either breaks the invariant that only the owner's answer settles a row, and the leg stays green. The current code is correct, so this is a contained coverage gap.
- **Fix (judged SOUND by the skeptic):** Add two `FX_PARKED` variants, each owing `awaiting` with T. `other-build` writes T `answered` with a reason under a second build slug and stages it. `malformed` stages a T record with a doubled field or a Channel outside the closed set. Extend the plant's tuple and its assertion that a record is read under its tag, since these records must not be read and must have no `read —` line. Observe each variant red with its own filter dropped.
- **Left-shift gate:** The `loop position fixtures` leg carries both variants. For the class, spec section 7 should name one staged break per condition an S clause states, so an S clause whose condition has no break is visible at review.

### M3 — no arm shows that the newest record wins by date and number (id 5)

- **Where:** `tools/loop/adapt.py@42ad9fb5:240`, the hand-written fold that replaced the base's `max()`.
- **What is wrong:** Only `other-word` in `FX_PARKED` puts two records on one tag. They are n=1 and n=2 on one date, so path order, lexical order and the real `(date, n)` key all choose the second. Replacing the comparison with `True` (last read wins) or with a lexical compare of `r["id"]` left both plants `held`. AC3's red condition, that an older `answered` record outranks the newer one, is observed only against first-wins. No loop fixture names a `disposition-<n>` of 10 or more.
- **Consequence:** Records are read in path order, so `disposition-10` is read before `disposition-2`. A regression to last-read or lexical order lets an older `answered` -2 outrank a later `withdrawn` -10. A re-opened owner decision then reads as settled and the gate stays green. The current key is correct, so this is a contained test gap.
- **Fix (judged SOUND by the skeptic):** Add a variant whose T records are n=2 `answered` and n=10 `withdrawn`, owing `awaiting` with T. Pad with records of other tags, or write the file names directly. The skeptic notes that the plant's per-tag checks tolerate the padding. Observe the variant red under both mutants above.
- **Left-shift gate:** The `loop position fixtures` leg carries the variant. For the class, an arm on a newest-record rule feeds records whose read order and lexical order both disagree with the key.

## LOW

### L1 — the hold rule is exercised on `BUILDING` and `HELD` only (id 6)

- **Where:** `tools/loop/position.py@edc79dc3:722`, the rule, with its variants at `tools/loop/position.py@edc79dc3:313`.
- **What is wrong:** The rule is that a hold interrupts only while `phase` reads `HELD`. The variants plant `BUILDING` (`hold-resumed`) and `HELD` (`hold-live`, `hold-passed`), and the base fixture writes `phase: BUILDING`. Changing the predicate to `!= "BUILDING"` left both plants `held`. The motivating state is dBoundRoles at `18ba9d38`, `phase: SPECCING` with a stale hold. No arm plants it, and AC10 calls only `read_open_decisions`.
- **Consequence:** A predicate that still interrupts on `SPECCING`, or with no phase, passes the leg. The shipped `== "HELD"` is correct, the mutant is implausible, and AC6's stated red conditions are met.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Keep the `BUILDING` variant. Add two variants beside it, one with `phase: SPECCING` and one with no phase fact. Each carries the same hold facts and owes `act` with none. The finder's proposal, to plant `SPECCING` in `hold-resumed` or add it as a second variant, cures the cited instance alone. It moves the blind spot and leaves the absent phase uncovered.
- **Left-shift gate:** The `loop position fixtures` leg carries both variants.

### L2 — the acceptance ledger says the arms were not observed, then records both as observed (id 3)

- **Where:** `memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md@483d6e2c:23`.
- **What is wrong:** The paragraph under "Owed to the close" lists the RED-first observation of `parked-decisions` and `parked-kinds` as owed and ends "Neither was observed in this pass". The two `seen-red` lines beneath it, added by `9981f34e`, record both as observed at `ace7f1ee`. The paragraph was not edited with them, and the file does not say they came later.
- **Consequence:** A reader of the close cannot tell from the ledger whether the two arms are still owed. No behaviour changes.
- **Fix (judged SOUND by the skeptic):** Reword the paragraph so that only the legs of section 7 stay owed, and say the two arms were seen red afterwards at `ace7f1ee`.
- **Left-shift gate:** No leg reads this prose. The class is on the checklist already, as `amendment-leaves-its-other-half-standing`, and this instance can be added to its record.

review-shape kind=diff-review round=1 intensity=full at=synth raw=6 confirmed=5 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=3 low=2 agents=9 out-tokens=41690 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/loop/position.py@edc79dc3:697 | medium | medium | confirmed | Read, not run end to end. verb_park (tools/unattended/unattended.sh@9b83204c:17645-17652) compares item and reason with the timestamp stripped, against every decision row. On a match it prints 'already parked, unchanged', writes nothing and returns 0. run_exhausted (9592-9595) likewise keeps any standing row. read_open_decisions settles a row by its timestamp tag alone, so after an answer the same park yields no new tag and no interrupt. At base every owed decision row interrupted for the run's life, so this diff made the no-op unsafe. The spec and the BY DESIGN list do not cover re-asking; the by-design flow.on-exhausted item covers only that it needs its own record. The effect is contained: it needs an identical item and reason, the question already carries an owner answer, and the usual --handoff puts the phase at HELD, which interrupts. The fix is judged unsound. For --exhausted, read_exhausted_row takes the newest row (tail -n 1) and --close, --resume and the budget read use it, so appending a second row can replace the recorded ending and reverses the stated rule that the first ending stands. For --park, the no-op exists so post-compaction recovery can replay a step. Appending after an answer turns each replay into a new open question that stops the run. The docs part is right but leaves the driver reporting success. | unsound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 2 | correctness | tools/loop/position.py@edc79dc3:222 | high | - | refuted | PRE-EXISTING. I ran both regexes on the same rows. The base PARKED_ROW `... Z (\S+) · item (\S+)` and the new DECISION_ROW both match item 'a' and both return None for ' a' and ' '. At base derive_interrupts skipped such a row and raised no interrupt, so the build answered `act` with an open spaced-item row exactly as now. The driver's park and check_verb_flag are untouched by this diff. The ordinal shift is not a separate defect: the engine prints and looks up tags from the same count, so counted rows stay consistent. The proposed regex would count a spaced item. | sound | - | - |
| 3 | correctness | memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md:23 | low | low | confirmed | Read the ledger and the diff ace7f1eec..9981f34e0. The second commit only appended two seen-red lines. The paragraph directly above them, under 'Owed to the close', still lists the RED-first observation of both arms as owed and says 'Neither was observed in this pass'. 'In this pass' can be read as true of the builder pass, but the heading presents as outstanding what the next lines discharge, and the file does not say they came later. Wording only, no behaviour. The proposed rewording removes the contradiction, which occurs only here. | sound | - | class:amendment-leaves-its-other-half-standing |
| 4 | verification | tools/loop/adapt.py@42ad9fb5:237 | medium | medium | confirmed | Judged from source; no plant was run. FX_PARKED in position.py holds only (tag, word, reason) triples. run_parked_plant writes every one with write_disposition(repo, FX_SLUG, FX_IDS[0], tag, word, 'terminal', ...), a validating door, so each record is of FX_SLUG and well-formed. read_records walks builds/*/build, so the build filter and the malformed filter at tools/loop/adapt.py@42ad9fb5:237 are the only enforcement for a tag that names no build. No variant feeds either filter a record it would reject, so dropping either leaves both plants held. A grep of adapt.py finds no other fixture for malformed or foreign-build records. Spec S1 states both conditions and says AC1 to AC3 observe it, but those plants do not. The filters existed at base, but this diff adds the function, the owner-decision consumer and the arms that claim S1. Current code is correct, so the effect is a contained coverage gap. The fix covers both unexercised conditions; the plant's tuple and its 'record read under its tag' assertion must also be extended for these variants (a record not read, no read line), which is part of adding them. read_record marks a doubled field or an out-of-set Channel as malformed, so the variant is constructible. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 5 | verification | tools/loop/adapt.py@42ad9fb5:240 | medium | medium | confirmed | Judged from source; I did not re-run the mutants. Only `other-word` in FX_PARKED puts two records on one tag. write_record allocates n=1 and n=2 on one day, and read_records sorts by path, so last-read, lexical stem and (date, n) all pick the second record. The diff replaced the base's max() with a hand-written fold, and no loop fixture names a disposition-<n> with n of 10 or more. AC3's red condition, 'an older `answered` record outranks the newer one', is therefore observed only against first-wins. Because `-10` sorts before `-2`, a lexical or last-read regression would settle a re-opened decision with the leg green. The current key is correct, so this is a contained test gap. On the fix: with -2 `answered` and -10 `withdrawn`, both mutants pick -2 and answer `act`, so the variant goes red. The plant's dict-per-tag checks tolerate padding records of other tags. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 6 | verification | tools/loop/position.py@edc79dc3:313 | low | low | confirmed | Judged from source. The hold variants plant only BUILDING (`hold-resumed`) and HELD (`hold-live`, `hold-passed`), and the base fixture writes `phase: BUILDING`. A `!= "BUILDING"` predicate gives the same result on all of them. AC10 calls read_open_decisions alone, so the incident's SPECCING with a stale hold is exercised nowhere. The shipped `== "HELD"` is correct, the mutant is implausible, and AC6's stated red conditions are met, so this is low. On the fix: replacing BUILDING with SPECCING only moves the blind spot to `!= "SPECCING"`, and neither option covers the absent phase that the finding itself names. | instance | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
