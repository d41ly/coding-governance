**Serves:** spec-audit TOOL-aPrunedIndex-4@rev-4 TOOL-aPrunedIndex-10@rev-1
**Caused-by:** TOOL-aPrunedIndex-4

# aPrunedIndex — spec audit of units 4 and 10, round 1

*2026-11-26. A Tier-2 adversarial pass over spec 10 (the unit that fixes the closing review's four lows), with spec 4 at rev-4 audited beside it. Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md@dc4e20bb0a9ec7b985e911b89aedcaa51cd345ef, memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md@f7ce08e2e4e4490469542255f9bc144674595ad7

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker or high stands.
By item: 0 blocker, 0 high, 6 medium, 5 low, 11 in all.
By raw confirmed finding: 0 blocker, 0 high, 7 medium, 8 low, 15 in all.
Item 2 holds two medium findings and one low, and item 1 holds one medium and one low.
Spec 10 needs these fixes before it is built.
The main ones: AC2 cannot tell a lambda from a def, the gate line drops spec 4's legs and its owed-at-close rider, and the new ask duplicates PLAY-dClosedLoop-21.

The review shape is intensity full, raw 16, confirmed 15, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 5 | 4 | 0 | 1 | 0 | 0 | 1.00 |
| grounding | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses 5/5 returned, 0 died. Skeptic batches 4/4 returned, 0 died.
- 0 contradictory verdicts demoted, 0 orphaned duplicate refutations demoted, 1 duplicate refutation counted as a merged confirmation (id 5, a duplicate of id 7), 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 13 judged sound, 1 judged UNSOUND (id 1), 1 judged INSTANCE-ONLY (id 10), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 ungraded by the skeptic, 1 re-graded (id 7, medium to low).
- Unverified: 0 uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Preset unit-spec: coherence, grounding, reuse, blast-radius, failure-envelope.
- Intent: 4 spec documents supplied as sibling context.
- Checklist: 29 items over 5 lenses (coherence 6, grounding 6, reuse 6, blast-radius 6, failure-envelope 5).
- By design: none supplied.
- Move check: no checked subject moved.
- Refuted findings shown 0, same-address pairs shown 0, twins flagged 0.
- Dispositions: unclassed refuse, 29 class slugs, 226 leg names.

## Medium

### 1. Spec 10 never states that its gov_tag.py edit re-versions the instruction_units extractors, and never measures the re-parse (ids 11, 7)

- **Where:** spec 10 section 3 (the tag_index closure non-goal), section 4 (no Migration subsection).
- **What:** gov_tag.py is in instruction_units' import closure (`derive_module_closure` prints it). S2 to S4 edit it, so `instruction_units:extract_unit` and `extract_repo` take new versions. Section 3 speaks only of tag_index's closure. The brief (lines 46-48) accepts this cost and says the main loop measures it at the close on the private copy. The spec carries neither the statement nor a criterion or ledger line for the measurement.
- **Consequence:** every node pays an unstated, unmeasured re-parse. The live index gains one more set of rows that will go dead, which is the detriment this build exists to remove.
- **Grades:** id 11 medium (binding). Id 7 low (binding; the skeptic re-graded it from medium because the tag_index claim is true and the re-parse already happens at each routed_commits landing).
- **Fix (judged SOUND by the skeptic, both ids):** add a Migration line under section 4: "gov_tag.py is in instruction_units' import closure, so this edit re-versions instruction_units:extract_unit and extract_repo; the cost is accepted, and the main loop measures the re-parse at the close on the private copy, in the ledger." Add an AC or a ledger line owed at the close for that measurement. Id 11's gate-list half is carried by item 2's fix.
- **Left-shift:** a spec-tokens check that, for every file under Files touched, derives which extractor closures it sits in and requires the spec to name each re-versioned extractor.

### 2. Spec 10's section 6 gate line is not spec 4's section 7 leg line carried over: legs missing, and the owed-at-close rider dropped (ids 6, 10, 13)

- **Where:** spec 10 section 6 Gates (line 221), against section 4 Files touched and AC8, and section 3's last non-goal.
- **What:** the line names nine legs. It leaves out `every held leg is budgeted, every budget row resolves` and `leg ceilings clear their evidenced maximum`, though AC8 may rewrite selftest-budgets.txt and ceiling-evidence.txt. It also leaves out `tags (the resolver's checks)`, which runs the edited gov_tag.py, plus `instruction edits (manifest checks)` and `edges (every declared edge parses, is registered and resolves)`. It lists `instruction units selftest` with no rider. That leg's `statements` plant calls `load_resolver()`, which opens the node's live index. Section 3 says every observation runs in a fixture's scratch repository, which is not true of that gate. Timing never names `derive-ceilings.py --write` as the source of the evidence row.
- **Consequence:** the unit can be green on its named legs while the bar reds on a row AC8 rewrote. All of these legs are subject `repo` with no guard, so the spec-tokens guard join cannot catch the omission. A builder running section 6 from the worktree opens the live 12.6 GB index and writes rows at a new `instruction_units:*` version before the owner's go holds. The closing review was not clean (the owner answered "Fix lows first"), so the go does not hold yet.
- **Grades:** id 6 medium, id 10 medium, id 13 low (all binding; id 13 is conditional on AC8's rule firing, and the full bar still runs every leg).
- **Fix:** for id 10 the skeptic judged the finder's fix INSTANCE-ONLY. The class-level fix, which this item adopts: carry over spec 4's section 7 leg line in full for the files the two units share. That adds the budget and ceiling legs, and all four live-index legs (`tags (the resolver's checks)`, `instruction edits (manifest checks)`, `edges (every declared edge parses, is registered and resolves)`, `instruction units selftest`) under spec 4's rider: owed at the close once the go holds, by no pass before it. The finder's proposal (add the two budget legs, plus `tags` and `instruction edits` marked owed at the close) would cure only the cited instance. Id 6 (SOUND): narrow section 3's sentence to the observations in section 5, not the gates in section 6. Id 13 (SOUND): in Timing, state that the evidence row is written by `python tools/run-gates/derive-ceilings.py --write`, following spec 4 AC8.
- **Left-shift:** class `hand-named-gate-list-green-while-the-bar-reds` has recurred. A spec-tokens arm should map each Files-touched path to the `repo`-subject legs that read it and refuse a section 6 line that omits one. A second arm should require the owed-at-close rider on any leg tagged as opening the live index.

### 3. AC2 cannot tell a lambda from a def (id 1)

- **Where:** spec 10 section 5 AC2, which observes section 2 S2.
- **What:** AC2 is red when "the lambda stays bound". Its three commands (`grep -nw commit_texts` prints nothing, `grep -cw write_commit_texts` prints 10, lexicon `--suggest` answers OK) all pass on a bare rename, `write_commit_texts = lambda files: ...  # noqa: E731`. AC3 catches only a NameError.
- **Consequence:** S2's main change, a nested `def` the naming leg can grade, is never checked. A lambda-only rename lands green and `_python_defs` stays blind to the helper.
- **Grade:** medium (binding).
- **Fix (the skeptic judged the finder's fix UNSOUND; this is its corrected fix):** add to AC2 that `grep -c 'def write_commit_texts(' tools/playbook/gov_tag.py` prints 1 and `grep -cE 'commit_texts *= *lambda' tools/playbook/gov_tag.py` prints 0. Keep the 10-line count for the call sites.
- **Left-shift:** class `criterion-asserts-what-its-own-command-cannot-show`. A self-review checklist line: for each red-when clause, name the command output that turns red on it.

### 4. The new ask duplicates PLAY-dClosedLoop-21 and points at a different seam (id 9)

- **Where:** spec 10 section 2 S5, and the `closed-over-an-unaudited-spec-revision` row of the section 4 asks table.
- **What:** PLAY-dClosedLoop-21 (memory/builds/dClosedLoop/BACKLOG.md:15) already asks that the `specs-audited` term at `--close` count a unit as audited only when a spec-audit record pins its current revision. Spec 10 files a new ask for a new CLOSED refusal in the build index, with a new waiver, and never names that ask. Asks 5, 6, 8 and 9 each carry "the same class's gate is asked by ..., so one gate closes both"; this row has no such link.
- **Consequence:** two open asks for one gate, at two different seams. Someone building the new ask would add a second refusal in gen_build_index.py and leave the existing term (check-unattended.sh, `read_spec_audit_ids`) and its `--override specs-audited` still not pin-aware.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** either drop the second ask and name PLAY-dClosedLoop-21 in section 3 as the ask for L4's class, or file it in asks 5 to 9's shape with "the same class's gate is asked by PLAY-dClosedLoop-21, so one gate closes both". In that case its accept text extends the `specs-audited` term (pin-aware, waived by the existing `--override specs-audited`). AC7's expected summary follows the chosen option.
- **Left-shift:** a backlog check that refuses a new ask whose class already has an open ask elsewhere unless the row names it.

### 5. Filing two ask ids touches generated records the spec does not list, and `memory hygiene` is not a gate (id 12)

- **Where:** spec 10 section 2 S5, section 4 The asks and Files touched, section 6.
- **What:** two new ids change memory/backlog/TOOL.md (generated, "do not hand-edit"), the README's `ids:` line and gen:build-index region, and the aPrunedIndex row of memory/LIVE.md. The filing of asks 5 to 9 (b17cf2020) touched all four files. Files touched names only BACKLOG.md of these. `memory hygiene`, whose check 9 byte-compares those regions, is absent from section 6.
- **Consequence:** a builder edits BACKLOG.md alone, the renders go stale and the bar reds on a leg the spec never named. The same re-render clears the README's "moved past its audited revision" line that section 3 counts on for L4.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** list memory/builds/aPrunedIndex/README.md (new ids on `ids:`, gen regions re-rendered), memory/backlog/TOOL.md and memory/LIVE.md under Files touched, all regenerated by `python tools/memory-tree/gen_build_index.py --write`. Add `memory hygiene` to section 6. Have AC7 also require `gen_build_index.py --check` to be clean.
- **Left-shift:** a spec-tokens arm: a spec that files backlog ids must list the generated renders and `memory hygiene`.

### 6. AC8's no-move check diffs two whole shared files, so a main merge reds it (id 14)

- **Where:** spec 10 section 5 AC8, and section 4 Timing.
- **What:** `git diff --exit-code b15bee51 -- tools/run-gates/selftest-budgets.txt tools/run-gates/ceiling-evidence.txt` covers both whole files. 46 commits touched them in the week to 2026-11-26, and this build line merges origin/main into run branches (dcb75b59e, ad02f1a6a, fbeb537b0).
- **Consequence:** after a reconcile merge, AC8 reds on the no-move branch though this unit moved no row. Once that red is expected, it stops catching a `tags bundle selftest` row that did move.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** scope the check to that leg's rows. Compare `git show b15bee51:tools/run-gates/selftest-budgets.txt | grep '^tags bundle selftest'` with the same grep on the current file, and likewise for ceiling-evidence.txt. Or diff against the merge-base with the default branch, restricted to that row.
- **Left-shift:** class `a-merge-of-the-default-branch-read-as-additions`. A spec-tokens arm that flags `git diff` against a fixed sha over a file other units also write.

## Low

### 7. The new README cost sentence still understates the ceiling by up to half (ids 8, 15)

- **Where:** spec 10 section 2 S1, and section 4 "L1, the README sentence".
- **What:** the clause "one seek per released pair against the trees plus a scan of `dirty_path` for each pair no tree holds" drops a factor. `remove_released_rows` (tag_index.py 877-884) runs two DELETE statements, one filtering on (path, blob) and one on blob alone, and each has a `dirty_path` half. `dirty_path` is keyed (worktree, path) with no blob index. A pair no tree holds costs two tree seeks and two `dirty_path` scans. The code comment says "each EXISTS's dirty half"; the sentence drops "each".
- **Consequence:** the README states half the code's ceiling, repeating at half scale the understatement L1 was opened to fix. Prose only; the order of growth is unchanged.
- **Grades:** id 8 low, id 15 low (binding).
- **Fix (judged SOUND by the skeptic, both ids):** write "two seeks per released pair against the trees, and up to two scans of `dirty_path` for each pair no tree holds", or the comment's own form, "a seek against the trees per released pair and per released blob, plus a scan of `dirty_path` for each that no tree holds". Keep AC1's second probe substring in step with the chosen wording.
- **Left-shift:** a bug-class checklist entry: a cost sentence that mirrors a code comment must keep the comment's quantifiers.

### 8. AC7 reads a cut summary cell, so a correct ask can fail it (id 2)

- **Where:** spec 10 section 5 AC7, and section 4 The asks.
- **What:** AC7 looks for class names in the `Summary` column of `gen_build_index.py --asks`, which `render_summary_cell` (backlog.py 1656-1684) cuts at about 70 characters and ends with `…`. The table says only what each ask "names", not that the class leads.
- **Consequence:** an ask that leads with the review id or the 54-name count fails AC7. The failure reads as a missing SEV row, which is AC7's stated red cause.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** require each ask's text to open `THE CLASS <class> ...` as asks 5 to 9 do, or have AC7 read `--json`, which keeps the full text.
- **Left-shift:** a checklist entry: a criterion never greps a truncated render.

### 9. Spec 4 gives two ranges for one prototype time, and spec 10 quotes one of them (id 3)

- **Where:** spec 4 section 6, AC1 cost and AC8 cost; spec 10 section 4 Timing.
- **What:** AC1 says "19 s to 35 s", AC8 says "17 to 35 s", and spec 10 quotes the second. Unit 4's ledger line 11 measured 46 s. (PINNED, 2026-11-26)
- **Consequence:** cosmetic in a frozen spec, but spec 10 builds its timing rule on the figure and a reader cannot tell which one is pinned.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** this audit of spec 4 at rev-4 records the mismatch (here). In spec 10 Timing, cite the measured 46 s from unit 4's ledger, as AC6 already does. (PINNED, 2026-11-26)
- **Left-shift:** class `two-answers-to-one-question`. Its existing gate ask covers it.

### 10. Spec 4 AC8's "after the last unit" clause is left standing (id 4)

- **Where:** spec 10 section 2 S6, section 4 Timing and section 5 AC8, against spec 4 section 6 AC8.
- **What:** spec 4 AC8 takes its reading "after the last unit of the build is built". Spec 10 adds a later unit that lengthens `gc-predates` and, when the spread rule does not fire, keeps the d5288a92d reading. It never says this supersedes spec 4's clause. The budget row's "after aPrunedIndex's five plants" stays true, because spec 10 adds steps, not plants.
- **Consequence:** the two specs disagree about which reading the row stands on. Cosmetic.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** in spec 10 Timing, say that when the rule does not fire the rows keep spec 4's d5288a92d reading as the build's final figure. Have the ledger record that this replaces spec 4 AC8's "after the last unit" clause for unit 10.
- **Left-shift:** class `amendment-leaves-its-other-half-standing`.

### 11. "No skipped line" in step 7 and AC4 can never fail on its own (id 16)

- **Where:** spec 10 section 4 "L3, the two steps" step 7, and section 5 AC4.
- **What:** `run_gc` (gov_tag.py 199-207) prints skipped lines only after `remove_dead_versions` returns. So when the refusal holds, no skipped line can appear. "What the steps do not check" names only the counts as non-discriminating.
- **Consequence:** a reader counts it as a second independent check. Cosmetic.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** drop "no skipped line" from step 7 and AC4, or name it in "What the steps do not check" beside the counts, as implied by the refusal.
- **Left-shift:** class `criterion-asserts-what-its-own-command-cannot-show`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=16 confirmed=15 refuted=0 merged=1 unverified=0 blocker=0 high=0 medium=7 low=8 agents=10 out-tokens=113472 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 5 AC2 (observes section 2 S2) | medium | medium | confirmed | Spec 10 AC2 (blob f7ce08e2) has three checks: `grep -nw commit_texts` prints nothing, `grep -cw write_commit_texts` prints 10, and the lexicon --suggest answers OK. Its red-when says 'the lambda stays bound'. In the tree, tools/playbook/gov_tag.py@c22d4773:1365 is `commit_texts = lambda files: ...  # noqa: E731`, and `grep -cw commit_texts` printed 10. So a rename alone, `write_commit_texts = lambda files: ...`, would also give 10 and nothing for the old name. Neither grep nor the lexicon check can tell a lambda from a def. AC3 only catches a NameError. The def that S2 requires is never observed. The effect is contained, so medium. | unsound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 5 AC7 / section 4 The asks | low | low | confirmed | I ran `gen_build_index.py --asks --build aPrunedIndex --all`. Every Summary cell came back cut with an ellipsis at about 70 characters, e.g. `THE CLASS two-answers-to-one-question EARNED A GATE AT ITS SECOND…`. render_summary_cell in tools/memory-tree/backlog.py@77180b59:1656-1684 cuts at the cap and appends `…`. Spec 10's section 4 table only says what each ask's text 'names'. The phrase 'in the row shape of asks 5 to 9' does not clearly require the text to open with `THE CLASS <class>`. A correct ask that leads with the review id or the 54-name count could push the class name past the cut and fail AC7. That only makes the check fragile, so low. | sound | - | new:criterion-greps-a-truncated-render |
| 3 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md:section 6 AC1 cost vs AC8 cost | low | low | confirmed | Spec 4 at blob dc4e20bb gives two ranges for the gc-predates prototype: AC1 cost reads `19 s to 35 s for the prototype` and AC8 cost reads `17 to 35 s for gc-predates`. Spec 10's Timing section quotes `17 to 35 s`. Unit 4's acceptance ledger line 11 records 46 s. So the set holds two figures for one measurement, and neither is the measured one. It changes no behaviour, so low. | sound | two-answers-to-one-question | class:two-answers-to-one-question (PINNED, 2026-11-26) |
| 4 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 2 S6 / section 5 AC8 vs spec 4 section 6 AC8 | low | low | confirmed | Spec 4's AC8 (blob dc4e20bb) takes its reading 'after the last unit of the build is built'. Spec 10 S6, section 4 Timing and AC8 add a later unit that lengthens gc-predates. Where the spread rule does not fire, they keep the existing rows: 'Otherwise neither row moves, and the ledger says so'. Nowhere does spec 10 say it supersedes spec 4 AC8's 'after the last unit' clause, so that clause is left standing and stale. One part of the claimed impact is overstated. selftest-budgets.txt:146 reads 'at d5288a92d ... after aPrunedIndex's five plants'. Spec 10 adds steps, not plants, so the row text stays true. The disagreement between the specs is still real but cosmetic, so low. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 5 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 3 Non-goals (import closure bullet) / section 5 | low | - | refuted | duplicate of id=7. It raises the same omission: spec 10 never states that the gov_tag.py edit re-versions the instruction_units:* extractors, and it drops the brief's promise that the main loop measures that cost at the close. I re-read the brief at lines 46-48 and it says exactly what the finding quotes. Spec 10's section 3 discusses only tag_index's closure, and the only instruction_units text in the spec is the gate name in section 6. | sound | - | - |
| 6 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 3 (last non-goal) and section 6 Gates | medium | medium | confirmed | Spec 10 section 6 lists `instruction units selftest`. In tools/gate-legs.json that leg runs `instruction_units.py fixture`. run_fixture runs every plant, and the `statements` plant's arm_statements (line 1761) calls load_resolver(), which resolves root from KIT_DIR's own repository (`rev-parse --show-toplevel`) and then calls ti.load_index(root) and ti.load_view (lines 743-747). That is the live index, not a fixture copy. Spec 4 at blob dc4e20bb, section 3 lines 65-68, names this leg among those that open the live index. Its section 7 line 288 defers them to the close, once the go holds. Spec 4 section 3 says the go depends on a clean closing review, and that review confirmed four lows. Spec 10 carries no such deferral, and its section 3 last bullet says every observation runs in a fixture's scratch repository. My closure probe confirmed that gov_tag.py is in instruction_units' closure, so the view would load at a new version. The effect is contained: one premature open or write of the live index, against a standing rule. | sound | - | new:gate-list-drops-the-owed-at-close-rider |
| 7 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 3 (the tag_index closure non-goal) and section 4 (no Migration subsection) | medium | low | confirmed | From tools/playbook I ran import_walk.derive_module_closure('instruction_units.py', ['.', '../memory-tree', '../lib']). It printed a closure that includes gov_tag.py, tag_bundle.py, tag_index.py and routed_commits.py, so spec 10's S2 edit to gov_tag.py re-versions the instruction_units:* extractors. The brief at lines 46-48 accepts that cost and says 'The main loop measures it at the close on the private copy'. Spec 10 states neither the re-version nor any criterion or ledger line for that measurement. Its section 3 discusses only tag_index's closure, and AC8 times only the gc-predates plant. The tag_index claim in section 3 is true, so the gap is an omission, not a false statement. The re-parse also already happens at every routed_commits landing. The consequence is an unstated and unmeasured cost with no behaviour change, so I grade it low. | sound | - | new:closure-edit-re-versions-an-unnamed-extractor |
| 8 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 2 S1 and section 4 'L1, the README sentence' | low | low | confirmed | I read blob 4d1a9ef3 at lines 877-884. remove_released_rows runs two DELETE ... FROM released statements, and each has an `OR EXISTS (SELECT 1 FROM dirty_path d ...)` half. dirty_path's key is (worktree, path), from the schema at line 115, and it has no blob index. A pair no tree holds at its path costs one dirty_path scan in the first statement. If it is still in released, it costs a second tree seek on blob and a second scan when no tree holds its blob. The ponytail comment at line 877 says 'each EXISTS's dirty half', and spec 10's replacement sentence drops the 'each', so it understates the code by up to a factor of two. The order of growth is unchanged and the error is prose only. | sound | - | new:cost-prose-drops-the-comments-quantifier |
| 9 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 2 S5; section 4 "The asks" table, row `closed-over-an-unaudited-spec-revision` | medium | medium | confirmed | memory/builds/dClosedLoop/BACKLOG.md:15 holds PLAY-dClosedLoop-21, an ask that the specs-audited term at --close read a unit as audited only when a spec-audit record pins its current revision. Line 43 is its SEV row, which names the build index's past-pin line. Spec 10 line 149 files `closed-over-an-unaudited-spec-revision` with a new build-index CLOSED refusal and a new waiver, and never names that ask. Asks 5, 6, 8 and 9 in aPrunedIndex/BACKLOG.md each end with 'the same class's gate is asked by TOOL-dPlacedRequest-N, so one gate closes both'; this row has no such link. tools/unattended/check-unattended.sh@5e139505:1326-1327 states the has-ever-named gap. The consequence is a duplicated, divergent ask in the backlog, contained to records. | sound | - | new:ask-filed-without-its-open-twin |
| 10 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 6 Gates leg line, against section 4 "Files touched (estimate)" and AC8 | medium | medium | confirmed | Spec 10's section 6 line (line 221) names nine legs. It leaves out `every held leg is budgeted, every budget row resolves`, `leg ceilings clear their evidenced maximum` and `tags (the resolver's checks)`. Yet section 4 lines 170-171 list selftest-budgets.txt and ceiling-evidence.txt as touched, and gov_tag.py is edited. gate-legs.json shows all three legs with subject repo and guard None. Spec 4 at dc4e20bb, section 7, names all of them for the same files and carries the owed-at-close rider. | instance | hand-named-gate-list-green-while-the-bar-reds | class:hand-named-gate-list-green-while-the-bar-reds |
| 11 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 3 (the tag_index cut-line bullet), section 4 Files touched, section 6 | medium | medium | confirmed | Lines 46-48 of the brief say gov_tag.py is in instruction_units' closure, that this edit re-versions the instruction_units:* extractors, and that the main loop measures the cost at the close. Spec 10 section 3 (lines 46-49) covers only the tag_index:* re-versioning, and no AC or ledger line records the instruction_units re-parse. Section 6 lists `instruction units selftest` with no rider. Spec 4 section 3 lists it among the legs that open the live index, and its section 7 makes all four such legs owed at the close only. Section 6 also leaves out `tags (the resolver's checks)` (gov_tag.py check), `instruction edits (manifest checks)` and `edges (...)`. | sound | - | new:closure-edit-re-versions-an-unnamed-extractor |
| 12 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 2 S5, section 4 'The asks' and 'Files touched (estimate)', section 6 | medium | medium | confirmed | `git show b17cf2020 --stat` (the filing of asks 5-9) touched memory/LIVE.md, memory/backlog/TOOL.md, aPrunedIndex/BACKLOG.md and README.md. memory/backlog/TOOL.md line 1 reads 'generated by tools/memory-tree/gen_build_index.py --write — do not hand-edit'. The README's ids: line and LIVE.md's id count (10) would both change with two new ids. Spec 10 section 4's Files touched lists only the two tools/playbook files, BACKLOG.md, the ledger and the two budget files. The `memory hygiene` leg (repo, no guard) is absent from section 6. | sound | - | new:files-touched-omits-generated-renders |
| 13 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 4 Timing and Files touched, section 6 | low | low | confirmed | Spec 10 at blob f7ce08e2, line 221, gives section 6 as nine legs. Neither `every held leg is budgeted, every budget row resolves` nor `leg ceilings clear their evidenced maximum` is among them, though lines 170-171 have the unit editing selftest-budgets.txt and ceiling-evidence.txt when AC8's rule fires. Both legs exist in tools/gate-legs.json at lines 3747 and 3773. Spec 4 at dc4e20bb lists both at line 286, and lines 271-272 name `derive-ceilings.py --write`. Spec 10 Timing (lines 161-162) points to the render only indirectly, through 'by unit 4's AC8 method', and never names it. The edit is conditional and the full bar still runs every leg, so this is low. | sound | - | class:hand-named-gate-list-green-while-the-bar-reds |
| 14 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 5 AC8 (and section 4 Timing) | medium | medium | confirmed | AC8 at line 211 runs `git diff --exit-code b15bee51 -- tools/run-gates/selftest-budgets.txt tools/run-gates/ceiling-evidence.txt`. That covers both whole files and filters no row. I re-ran the finder's git log over the week from 2026-11-19 on those two paths and it printed 46. Among them are the merges dcb75b59e, ad02f1a6a and fbeb537b0, which brought origin/main into run branches. So a reconcile merge before the close makes AC8 red on the no-move branch even though this unit moved no row. The wrong red is contained to the criterion, which fits medium. | sound | a-merge-of-the-default-branch-read-as-additions | class:a-merge-of-the-default-branch-read-as-additions |
| 15 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 4 'L1, the README sentence' (and S1) | low | low | confirmed | tools/playbook/tag_index.py, lines 877-884, runs two DELETE...EXISTS statements. Each has a dirty_path half, one filtering on (path, blob) and one on blob alone. The comment at line 877 reads 'each EXISTS's dirty half scans `dirty_path` once per pair no tree holds'. dirty_path's only key is PRIMARY KEY(worktree, path) at line 114. A pair that neither tree half holds therefore pays two dirty_path scans. The spec's clause at line 86 says 'a scan' per pair, half the ceiling. Line 105 adds a tree_path_blob index, so the blob-only tree half is also a seek, which makes two tree seeks per pair. The error is in prose only, so low. The fix's wording matches the code and keeps AC1 in step. | sound | - | new:cost-prose-drops-the-comments-quantifier |
| 16 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md:section 4 'L3, the two steps' step 7, and section 5 AC4 | low | low | confirmed | In tools/playbook/gov_tag.py#run_gc (lines 199-207), the loop that prints the skipped lines comes after `ti.remove_dead_versions` returns. In run_collect (lines 1060-1068), the skipped list is taken from stdout captured before the TagError. When the refusal holds, no skipped line can appear, so 'no skipped line' in step 7 (line 121) and AC4 (line 190) is implied by the refusal and can never fail on its own. The 'What the steps do not check' paragraph (lines 134-136) names only the counts. The overstated coverage is cosmetic. | sound | criterion-asserts-what-its-own-command-cannot-show | class:criterion-asserts-what-its-own-command-cannot-show |
