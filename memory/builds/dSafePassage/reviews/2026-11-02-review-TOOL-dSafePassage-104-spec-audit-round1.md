**Serves:** spec-audit TOOL-dSafePassage-104@rev-1

# Tier-2 review: round-1 spec audit of TOOL-dSafePassage-104

TOOL-dSafePassage-104 was adopted under UNATTENDED-PROTOCOL section 11. The close's bar on the landing merge 9f8812d80 reds in two places. Memory hygiene check 12 reds on TOOL-dSafePassage-103's consumes-from edge onto CLOSED TOOL-dSafePassage-8. The lexicon naming-predicates and lexicon-wiring legs red at `verb offenders 1212 over pin 1211` on 103's second nested `ask()` in `tools/policy/check_policy.py`, and that red shows on the branch too. 103's rev-3 edit, committed with 104's spec, names 8 in prose and keeps 103's two external edges. 104 lets `run_census_window_edge` and `run_census_source_receipt` call one module-level `ask`, and keeps the name because the pin is a two-sided equality.

Reviewed: memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md@f8089972e1a18b6de191f3cd19ab1eded4658bec
ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. Two items are MEDIUM, and both are acceptance criteria that cannot observe what they claim to observe: AC7's second probe and AC9. Four items are LOW and are wording or declaration defects. No two findings describe the same defect, so each finding is its own item. Fold the six fixes into the spec before the build starts.

Review shape: intensity full, raw 6, confirmed 6, refuted 0, unverified 0 (0 uncertain), precision 1.00. Adjudicated tally by item: 0 blocker, 0 high, 2 medium, 4 low. By raw confirmed finding: 0 blocker, 0 high, 2 medium, 4 low.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 0 | 0 | 0 | 0 | 0 | - |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

## Run integrity

- All 5 of 5 lenses returned, and none DIED.
- All 3 of 3 skeptic batches returned, and none DIED.
- No verdicts were demoted or discarded: 0 contradictory, 0 orphaned duplicate refutations, 0 spurious and 0 duplicates.
- All 6 fixes on confirmed findings were judged sound. None was judged UNSOUND, none was missing and none was NOT JUDGED.
- The skeptic left 0 confirmed findings UNGRADED and RE-GRADED 0.
- Unverified findings: 0 were answered UNCERTAIN and 0 had no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches were gov-skeptic, and synthesis was gov-synthesizer.
- Intent: no spec was supplied, and `context` was the caller's statement.
- Checklist: 17 items, each assigned to exactly one of 5 lenses (coherence 4, grounding 4, reuse 3, blast-radius 3, failure-envelope 3).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Every count is zero, so the run is complete. The reuse lens returned and found nothing, so its zero is real evidence that there are no reuse defects.

## Items

### MEDIUM 1: AC7's second probe reads HEAD, which the ledger cannot record honestly (finding 5)

- **Where:** section 6, AC7 (the second probe) and its fixture line.
- **What is wrong:** The probe is `git show --name-only --format= HEAD -- tools/`, run "at the build commit". The brief requires one pass commit that already contains the acceptance ledger, with each probe's output recorded in it.
  - Run before the commit, the probe reads the previous records commit (bfc894d06) and prints nothing. That is a red with nothing to do with S2.
  - Run after the commit, its output cannot go into that same commit unless the builder amends, and the spec never mentions amending.
  - The probe only sees the last commit. If the build is split across commits, an edit to `policy.py` in an earlier commit goes unseen. If the build commit is a merge, the probe sees only the combined-diff names.
- **Consequence:** A pass can certify a write set the probe never read. That is the opposite of its 'Red when'.
- **Fix (judged SOUND by the skeptic):** Read the write set from the tree the ledger is written against, not from HEAD.
  - Before the commit: `git diff --name-only HEAD -- tools/` plus `git ls-files --others --exclude-standard -- tools/` must print only `tools/policy/check_policy.py`.
  - After the commit, as a check owned by the main loop: `git diff --name-only 4467aa796 <build-commit> -- tools/`.
  - The criterion must name which of the two the ledger records.
- **Left-shift gate:** Add a spec-lint check that reds when an acceptance criterion whose output the ledger records reads `HEAD` (as in `git show ... HEAD`) while the brief commits the ledger in the same pass. This is the class test-oracle-read-from-a-historical-sha. Where no gate fits, add it to the bug-class checklist.

### MEDIUM 2: AC9 pins no main sha and never checks that `ask#2` is gone (finding 6)

- **Where:** section 6, AC9; section 4, 'Where the reds come from' (lines 108-112); Edges, bullet 3.
- **What is wrong:**
  - AC9 assumes main is still at 2a6f39756, the parent of 9f8812d80, but its fixture never names that sha.
  - AC9 checks only that the offender count equals the pin. On main, `.lexicon.conf` reads `VERB_OFFENDER_PIN="1212"`; on the branch it reads `"1211"`.
  - AC9's 'Red when' is "the merge still carries ask#2", but nothing checks for `ask#2` directly.
  - The spec says nothing about main moving before the landing merge, whether by gaining or losing an offender or by re-measuring the pin.
- **Consequence:** If main gains an offender, AC9 reds, and section 3's ban on pin moves leaves no remedy. If main loses an offender while the merge still carries `ask#2`, the count returns to 1211 and AC9 passes while its own red condition holds.
- **Fix (judged SOUND by the skeptic):**
  - Name main's sha in AC9's fixture: either 2a6f39756, or "main at the prepared merge, recorded".
  - Add the absence check AC4 already uses, run on the merge: `python tools/lexicon/lexicon.py --offenders` prints no `tools/policy/check_policy.py verb ask#2` line.
  - State that a main move which shifts the merge's count is a hand-back to the main loop, not a pin move by this unit.
- **Left-shift gate:** Add a spec-lint check that every criterion run on a merge names the base sha in its fixture. Also add a checklist entry: a count-equals-pin criterion must pair with a direct absence check of the offender it names.

### LOW 1: S3's claim that `derive_answer` stays out of the symbol tier has no criterion (finding 1)

- **Where:** section 2 S3, and section 6 AC7 and AC8.
- **What is wrong:** S3 says the nested `derive_answer` stays out of the symbol tier and cites AC8 as the check. Section 4 rejects a module-level `derive_answer`. But AC8 checks only that `gen_map.py --check` exits 0 and that the `"id": "ask"` count is 1, and AC7 greps only for `def ask`.
- **Consequence:** A build that hoists `derive_answer` to module level and regenerates the map passes AC1-AC9. The result is a second public symbol for one caller, which is exactly what the spec rejected. The effect is contained, with no wrong result.
- **Fix (judged SOUND by the skeptic):** Use either of these:
  - Add to AC8: `git grep -c -e '"id": "derive_answer"' -- memory/map/generated/symbols.json` prints nothing and exits 1.
  - Add to AC7: `git grep -n -e '^def derive_answer' -- tools/policy/check_policy.py` prints nothing.
  - Either one reds when `derive_answer` is module-level.
- **Left-shift gate:** Add a spec-lint check that every "Observed by ACn" claim in section 2 names a symbol or path that also appears in ACn's probe text.

### LOW 2: Section 7 says every other leg is reached only through the `tools/` guard, which is false (finding 2)

- **Where:** section 7 Gates, paragraph 2.
- **What is wrong:** The section says: "Every other leg the estimate trips is reached only through the broad `tools/` guard." In `tools/gate-legs.json`, 76 of 148 legs carry no guard. One of them is `policy check` (`python {prefix}/policy/check_policy.py`), which runs the very module S2 edits on every change, and section 7 does not list it.
- **Consequence:** The section's reasoning disagrees with the manifest, and a reader underestimates which legs exercise the edited module. The gate verdict does not change.
- **Fix (judged SOUND by the skeptic):** Add `policy check` to section 7's list, noting that it imports and runs the edited `check_policy.py`. Reword the sentence to: "every other leg the estimate trips is either unguarded or reached through the broad `tools/` guard."
- **Left-shift gate:** Add a spec-lint check that compares section 7's leg list against the legs in `tools/gate-legs.json` whose argv names a path in the files-touched estimate.

### LOW 3: Section 10 presents a selection of reuse_lookup's neighbours as its ranking (finding 3)

- **Where:** section 10, the reuse_lookup paragraph (lines 410-412).
- **What is wrong:** The section names four neighbours as the ranking: refusal 25, Refusal 16, build_fixture 6 and run_fixture 2. Re-running the probe prints a different order: refusal 25 (SEAM), fixture 22 (SEAM), Refusal 16, DesignRefusal 6, build_fixture 6, resolve_compare_base 4, load_policy 3, and so on, with run_fixture in 14th place.
- **Consequence:** Only the reuse-audit record is off. None of the omitted candidates turns a policy Refusal into a compared value, so the "None fits" verdict holds.
- **Fix (judged SOUND by the skeptic):** Either say the listed neighbours are a selection, or list the top entries in printed order, each with its "none fits" reason.
- **Left-shift gate:** Add a checklist entry requiring a probe's output to be quoted in printed order, or explicitly labelled a selection.

### LOW 4: The files-touched estimate omits records the close will write (finding 4)

- **Where:** section 4, "Files touched (estimate)" (lines 244-251).
- **What is wrong:** 103's build commit 02030bc97 has the same shape of change, and it also wrote the unit's own spec and `memory/backlog/TOOL.md`. This estimate leaves out:
  - 104's own spec (the status flip and the `gen:spec-records` re-render).
  - The ledger's path. The estimate describes the ledger but gives no backticked path, so `read_files_touched` in `tools/unattended/unattended.sh` cannot see it.
  - `memory/backlog/TOOL.md` (line 551, the TOOL-dSafePassage-14 row, whose next-unit cell reads TOOL-dSafePassage-104).
- **Consequence:** The overlap probe and check 23 both see a smaller write set than the build and close write. Nothing ships wrong, because AC7 filters to `tools/` and the overlap probe is advisory.
- **Fix (judged SOUND by the skeptic):** Add these to the estimate:
  - `memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md` (the status flip, and the records-region re-render by `gen_build_index.py`).
  - `memory/builds/dSafePassage/build/2026-11-02-build-TOOL-dSafePassage-104-ledger.md`.
  - `memory/backlog/TOOL.md` (the TOOL-dSafePassage-14 row's next-unit cell, re-rendered at the close).
- **Left-shift gate:** Add a spec-lint check that every files-touched estimate names the unit's own spec, its ledger path as a backticked token, and the backlog file of any row that names the unit.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=6 confirmed=6 refuted=0 unverified=0 blocker=0 high=0 medium=2 low=4 agents=9 out-tokens=74746

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 2 S3 / section 6 AC7, AC8 | low | low | confirmed | In blob f8089972, S3 (line 48) says the nested derive_answer stays out of the tier and cites AC8 as the check. Section 4 also rejects a module-level derive_answer. AC8 only checks that `gen_map.py --check` exits 0 and that the `"id": "ask"` count is 1. AC7 only greps `def ask`. If the builder moved derive_answer to module level and regenerated the map, both criteria would still pass, and AC6 only checks the scenario values. `git grep -n derive_answer` over symbols.json and tools/ printed nothing, and check_policy.py currently has only the two nested `def ask():` at lines 4206 and 4238. So S3's 'Observed by AC8' points at a criterion that cannot observe it. The effect is contained: one extra public symbol, with no wrong result. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 7 Gates, paragraph 2 | low | low | confirmed | I read tools/gate-legs.json with python. The `policy check` leg has no guard key, and its argv is `python {prefix}/policy/check_policy.py`, which runs the module S2 edits. The leg is missing from section 7's list. 76 of 148 legs carry no guard, so the sentence 'Every other leg the estimate trips is reached only through the broad `tools/` guard' is false. Section 7 itself already lists the unguarded `codebase-map coverage + freshness` and `memory hygiene` legs. The gate verdict does not change; only the section's reasoning is wrong. | sound | - |
| 3 | grounding | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 10, the reuse_lookup paragraph | low | low | confirmed | The spec at blob f8089972 (verified with git rev-parse), lines 410-412, says reuse_lookup 'ranked name-stem neighbours' and names four: refusal 25, Refusal 16, build_fixture 6, run_fixture 2. I re-ran the same reuse_lookup command and it printed this order: refusal 25 SEAM, fixture 22 SEAM, Refusal 16, DesignRefusal 6, build_fixture 6, resolve_compare_base 4, load_policy 3, then a group at fan-in 2, with run_fixture 14th. So the four named are a selection, and the spec presents them as the ranking. None of the candidates it leaves out turns a policy Refusal into a compared value, so the 'None fits' verdict still holds. Only the record is off. | sound | - |
| 4 | blast-radius | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 4 "Files touched (estimate)" | low | low | confirmed | Spec lines 244-251 list check_policy.py, symbols.json, 103's spec, the README, and an unnamed ledger ('under the build's own build-records folder', with no backticked path). `git show --name-only --format= 02030bc97` (103's build commit, the same shape of change) printed memory/backlog/TOOL.md, the README, RUN.md, the 103 ledger, the 103 spec, symbols.json and tools/policy files. That shows the close writes the unit's own spec and the backlog too. memory/backlog/TOOL.md:551 holds the TOOL-dSafePassage-14 row, and its next-unit cell reads TOOL-dSafePassage-104. tools/unattended/unattended.sh:3503-3527 (read_files_touched) extracts only backticked path tokens under '### Files touched', so the unnamed ledger and the missing paths are invisible to it. The declared write set is therefore smaller than the real one. The effect is contained: the overlap probe is advisory, and nothing ships wrong. | sound | - |
| 5 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 6 AC7 (second probe), with its fixture line | medium | medium | confirmed | I read spec blob f8089972e. AC7's second probe is `git show --name-only --format= HEAD -- tools/`, run "at the build commit". Brief lines 17-28 require one pass commit that already contains the acceptance ledger, with one line per AC giving the probe and what it printed. So the probe can't be recorded honestly. Run before the commit, it reads the previous records commit. Run after, its output can't go into that same commit unless the builder amends, which the spec never mentions. AC5, AC6, AC8 and AC7's first probe read the working tree, which is the same before and after the commit, so only this probe has the problem. The effect stays inside the ledger's honesty and AC7's write-set check, so medium. | sound | test-oracle-read-from-a-historical-sha |
| 6 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-02-spec-TOOL-dSafePassage-104.md:section 6 AC9; section 4 'Where the reds come from' (lines 108-112); Edges bullet 3 | medium | medium | confirmed | I re-ran the evidence. `git show 9f8812d80 -s --format='%h %p'` printed `9f8812d80 2a6f39756 4467aa796`. main:.lexicon.conf:327 reads `VERB_OFFENDER_PIN="1212"` and the branch's :335 reads `"1211"`. AC9 (spec lines 351-357) checks only that there is no `over pin` line and no `UNDER pin` line, and lexicon.py 3280-3293 compares the count to the pin and nothing else. Its 'Red when: the merge still carries ask#2' is never checked directly. AC9's fixture names no main sha; 2a6f39756 appears only in the section 9 revision log. The spec also never says what happens if main's offender count moves before the merge. The impact is contained: AC4 already checks that ask#2 is absent at the build commit, and the false pass needs main to drop an offender. So medium, not blocker. | sound | - |
