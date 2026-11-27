**Serves:** spec-audit TOOL-aPrunedIndex-17@rev-3 TOOL-aPrunedIndex-20@rev-1

# Tier-2 spec audit: TOOL-aPrunedIndex-17 rev-3 and TOOL-aPrunedIndex-20 rev-1, round 1

Provenance: a five-lens unit-spec review (finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer), run against the build aPrunedIndex on 2026-11-26.

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md@ca1d8aa0684bdfd0ae4e6615a3d07b65da33c32f, memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md@9e0d027b0515c7e60242571dd7be679e45563c2c

ROUND: 1

## Verdict: CLEAN WITH FIXES

No blocker or high item. 17 items: 8 medium and 9 low. By raw confirmed finding: 23, of which 0 blocker, 0 high, 10 medium and 13 low. Each medium item has to be folded into a spec revision before either unit builds.

Review shape: intensity full, raw 23, confirmed 23, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 8 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |

Run integrity:
- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 21 judged sound, 0 UNSOUND, 2 INSTANCE-ONLY (ids 4 and 11; each cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED, 3 RE-GRADED by the skeptic (ids 14, 15, 20).
- Unverified findings: 0 UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Preset: unit-spec. The lenses were coherence, grounding, reuse, blast-radius and failure-envelope.
- Intent: 6 spec documents were supplied as `specs`, as sibling context.
- Checklist: 18 items, split coherence 4, grounding 4, reuse 4, blast-radius 3, failure-envelope 3.
- By design: none supplied.
- Move check: no checked subject moved.
- Refuted findings shown: 0. Same-address pairs shown: 0. Twins flagged: none.
- Dispositions: unclassed refuse, 18 class slugs handed, 226 leg names read from tools/gate-legs.json.

Every lens and every skeptic batch returned, so the finding set is complete for this run.

## Medium

### M1. AC8's MONOTONE branch accepts an outcome its own Red-when rejects, and `--reset` writes before it refuses (ids 9, 20)

- **Where:** spec 17 section 6 AC8 (the MONOTONE branch and its "On green, also red when" clause) and section 2 S6. Spec 20 section 5 AC5 and S5 inherit it.
- **What is wrong:** derive-ceilings.py `cmd_write` runs `remove_reset_rows` first, at line 548. That step deletes the reset leg's non-ok rows from `<git-dir>/gate-run/*/*.leg`. The leg's row is then re-derived as the retained maximum R. At line 601, `prev[0] >= obs_secs` prints MONOTONE, names R and returns 1 without writing ceiling-evidence.txt. The tracked row therefore keeps its prior value, 106.0 at ceiling-evidence.txt:149.
  - AC8 calls this path benign ("writes nothing, and the evidence row stands").
  - AC8's Red-when then requires the row to read `<worst after>` or "the retained maximum the MONOTONE line names". Unless R happens to be 106, the row reads neither.
  - "Writes nothing" is false, because the killed readings are already gone from the retained run files.
  - The refusal also fires at R == W, not only when R is above W.
- **Consequence:** the likely close is a contended bar run whose retained reading of this leg sits at or above the worst-after reading. On that path AC8 reads a false red, the main loop writes neither row, and it opens the hand-off for a reason the spec never meant. Otherwise the builder resolves the contradiction ad hoc. Unit 20 AC5 inherits the same procedure.
- **Grades:** id 9 medium (binding). Id 20 medium: the finder graded it high and the skeptic re-graded it medium, because the error is a false red at the close and never certifies a wrong result. The synthesis keeps medium.
- **Fix (judged SOUND by the skeptic):**
  - After a MONOTONE refusal, require the node-a row to read its value as it stood before the call (106.0 today), not the retained maximum.
  - Say the refusal fires at R >= W.
  - Say in S6, AC8 and section 5 that `--reset` deletes the leg's non-ok rows from the retained run files before any refusal.
  - Fix spec 20 AC5's wording the same way.
  - Have the build probe this on a fixture git-dir: retain an ok reading at or above the observed value, run the spelled call, and confirm it exits 1, the file is unchanged and the killed rows are gone.
- **Left-shift:** add to the bug-class checklist under `criterion-asserts-what-its-own-command-cannot-show`. A criterion that names a tool's refusal path must quote the tool's refusal branch (file:line) and state the post-call state of every file the tool touches before that branch.

### M2. AC8's budget rule can write a row and then go red on the same path, and contradicts S6 (id 2)

- **Where:** spec 17 section 6 AC8 (the MONOTONE branch and the budget rule) against section 2 S6. Unit 20 AC5 reuses the rule.
- **What is wrong:** on the MONOTONE branch, AC8 still has the budget row rewritten by hand as 1.5 x max(worst after, the evidence row's value). AC8 is also red when the budget row exceeds 159. If the retained maximum is over 106, the hand-written budget is over 159, so AC8 goes red after a row was already written, while "On red, the main loop writes neither row". S6 says both rows come "from the worst reading on the built tree", which the max() rule contradicts.
- **Consequence:** one criterion gives two verdicts and leaves a written row on its red path. The path is narrow today (106.0 and 159 in the tracked files), but unit 20 carries the conflict forward.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** pick one answer, then align S6's "from the worst reading on the built tree" with it. The options are:
  - treat the MONOTONE branch as red and write neither row;
  - base the budget row only on the worst reading after, and drop "the larger of ... the evidence row's value";
  - drop the ">159" red on that branch.
- **Left-shift:** `two-answers-to-one-question` checklist entry. Every write a criterion orders must be placed after the last red test it can trip.

### M3. Unit 20 says the two units "may build concurrently", but their write sets overlap and the build order says otherwise (ids 3, 17)

- **Where:** spec 20 section 3 (the gov_tag.py non-goal) and section 4 Files touched, against the README gen:build-order (steps 6 and 7, both Parallel "no") and spec 17 section 4 Files touched and AC8.
- **What is wrong:** spec 20 says "The two write sets are disjoint, so the two units may build concurrently". They are not disjoint:
  - Both units list memory/map/generated/symbols.json, tools/run-gates/selftest-budgets.txt and tools/run-gates/ceiling-evidence.txt.
  - Both re-version the same two instruction_units extractors.
  - Spec 20's own edge and its AC5 need unit 17's AC8 to run first.
- **Consequence:** two concurrent builds would regenerate symbols.json against bases that each lack the other's functions, so they conflict at merge. If unit 20 lands first, unit 17's AC8 before-tree already holds the pool, so its 0.90 ratio and 106 s bound measure a different baseline from the one section 4 predicted. Unit 20's AC5 baseline then depends on commit order. (PINNED, 2026-11-26)
- **Grades:** id 3 medium, id 17 medium (binding).
- **Fix (judged SOUND by the skeptic):** strike the "may build concurrently" sentence. Instead, say the product-code files are disjoint, but symbols.json and the two run-gates rows are shared, so unit 20 builds after unit 17's build commit, as the README's build order says.
- **Left-shift:** `two-answers-to-one-question`. A spec sentence that asserts parallelism should be checked against the generated build-order table's Parallel column and against the intersection of the sibling specs' Files-touched lists. That is a candidate arm for `spec tokens (a spec's own names resolve)`.

### M4. Unit 17 still treats the pool as a conditional, unminted, external hand-off, though it is TOOL-aPrunedIndex-20 (ids 4, 19)

- **Where:** spec 17 section 1 (line 28), the section 3 non-goal (line 69), section 3 Edges (`**hands-off** external`, lines 80-82), section 4 (lines 140 and 222), and AC8's red clause (line 331: "opens the hand-off of section 3").
- **What is wrong:** rev-3 was committed after unit 20's spec. It still says the pool is a unit "the session owning this slug mints", which "AC8's readings at the close decide". Unit 20 is SPECCED, approved by the owner unconditionally, and declares `consumes-from TOOL-aPrunedIndex-17`.
- **Consequence:** there are two answers to whether the pool is owed. If AC8 is red, the main loop is told to open a unit that already exists, which risks a duplicate. If AC8 is green, unit 17 says the pool is not owed, yet unit 20 is built anyway. Because the bullet names `external`, the SPEC_HANDOFF_CUTOFF join in check-spec-tokens is skipped, so nothing grades whether the two edges match.
- **Grades:** id 4 medium, id 19 low (binding).
- **Fix (id 4 judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** name TOOL-aPrunedIndex-20 everywhere spec 17 speaks of the pool as a conditional or future hand-off: section 1 line 28, the section 3 non-goal at line 69, the Edges hands-off line, section 4 lines 140 and 222, and AC8's red clause at line 331. On red, AC8 then records its readings for unit 20 instead of opening a hand-off. (PINNED, 2026-11-26)
  - The finder's proposal cures the cited instance alone. It rewrites the hands-off edge to name `TOOL-aPrunedIndex-20` and fixes section 1, the Edges prose and AC8's red clause.
  - Id 19's fix (judged SOUND) is contained in the class fix: write the bullet as `**hands-off** `TOOL-aPrunedIndex-20`` naming `run_selftest`, and have AC8's readings feed unit 20's AC5.
- **Left-shift:** `amendment-leaves-its-other-half-standing` / `two-answers-to-one-question`. Have `spec tokens (a spec's own names resolve)` refuse a `hands-off external` edge when a sibling spec in the same build declares `consumes-from` that unit.

### M5. Unit 20's fallback CompletedProcess leaves stdout as None, so the kept grading line raises TypeError (ids 5, 13, 22)

- **Where:** spec 20 section 2 S1 and section 4 (the `run_plant_process` exception path), against section 5 AC3 and S3.
- **What is wrong:** S1 gives the fallback only `returncode=None` and an stderr. `subprocess.CompletedProcess` defaults stdout to None. tools/playbook/tag_bundle.py@8a284c47:401 computes `out = p.stdout + p.stderr`, and S3 keeps that line unchanged, so `None + str` raises TypeError inside run_selftest.
- **Consequence:** a literal build crashes on exactly the path S1 exists to soften. AC3 catches it at build time, so the cost is a red build and a rework.
- **Grades:** id 5 medium, id 13 low, id 22 low (binding).
- **Fix (judged SOUND by the skeptic):** have S1 and section 4 say the fallback is `subprocess.CompletedProcess(argv, None, stdout="", stderr=f"{type(exc).__name__}: {exc}")`.
- **Left-shift:** new class `fallback-leaves-a-graded-field-unset`. A spec that builds a synthetic result object must name every field its consumer reads.

### M6. AC7's rev-3 amendment left S5 asking for the retired before/after measurement (id 1)

- **Where:** spec 17 section 2 S5 (lines 47-48), against section 6 AC7 (lines 295-302).
- **What is wrong:** rev-3 changed AC7 to three interleaved A/B pairs on the one built tree, with A as HELD_PLANTS emptied. S5 still says the builder times the five plants "before and after the edit, back to back".
- **Consequence:** a builder following S5 repeats the two-block rounds that went red under a 0.041 to 0.324 s gauge swing. A reviewer grading S5 against AC7's ledger finds no before-edit reading and calls the scope unmet.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** rewrite S5 to match AC7 (three interleaved A/B pairs of the five plants on the built tree, A as HELD_PLANTS emptied, B as built, with a gauge beside each run), and add S5 to the rev-3 log line.
- **Left-shift:** `amendment-leaves-its-other-half-standing`. A revision that edits an AC must re-read the scope item that AC observes and list it in the revision log.

### M7. AC8 never pins "the built tree", so a concurrent unit 20 would have its saving credited to unit 17 (id 21)

- **Where:** spec 17 section 6 AC8 ("the parent of the unit's build commit"; "the built tree").
- **What is wrong:** the before-tree is pinned to the parent of unit 17's build commit. The after-tree is just "the built tree", run at the close. If unit 20's pool reaches the tip between unit 17's build commit and its close, the after-tree holds the pool and the before-tree does not.
- **Consequence:** AC8's 0.90 ratio and 106 s bound could go green on the pool's saving, and the rows would be rewritten on that basis. A red that should signal the hand-off is masked, and unit 20's AC5 compares against a moved baseline. (PINNED, 2026-11-26)
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** do any one of these:
  - define the after-tree as unit 17's build commit in a second detached worktree;
  - require that `git diff --name-only <parent> <after> -- tools/playbook/tag_bundle.py` prints nothing;
  - drop "may build concurrently" from unit 20 (see M3).
- **Left-shift:** new class `measurement-tree-left-unpinned`. Every A/B criterion must name both trees by commit.

### M8. Both specs name the base worktree with cmd.exe `%TEMP%`, which Git Bash does not expand (id 10)

- **Where:** spec 17 section 6 AC8 (`%TEMP%/pi17-base`, line 317) and spec 20 section 5 AC5 (`%TEMP%/pi20-base`, line 161).
- **What is wrong:** in Git Bash and in PowerShell, `%TEMP%` stays literal. `git worktree add --detach %TEMP%/pi17-base` therefore creates a nested worktree under a literal `%TEMP%/` directory inside the checkout.
- **Consequence:** an untracked worktree sits inside the repository during the timed readings. That breaks the scratch-location rule, and a careless cleanup could commit it or leave it behind.
- **Grade:** medium (binding).
- **Fix (judged SOUND by the skeptic):** spell the location in a form the shell expands and the probe policy allows, such as an absolute path under the session scratch directory or `"$TEMP"/pi17-base`, and use the same form in both specs.
- **Left-shift:** new class `cmd-syntax-in-a-bash-command`. A grep arm over spec command spans for `%[A-Z_]+%` fits beside `shell hygiene (a quoting hazard)`.

## Low

### L1. AC4's bounds contradict the column they claim to quote (ids 7, 12)

- **Where:** spec 17 section 6 AC4, against the section 4 spawn table (lines 120-121).
- **What is wrong:** AC4 says the counts must be "at most section 4's with column", then lists gc-predates 90 and released-rows 210. The column reads 86 and 207.
- **Consequence:** a count of 88 passes by one reading and fails by the other. AC4's Red-when fires only at the "without" value, so the verdict does not change in practice.
- **Grades:** id 7 low, id 12 low (binding).
- **Fix (judged SOUND by the skeptic):** either list 86 and 207, or keep 90 and 210 and say they are deliberate slack over section 4's 86 and 207.
- **Left-shift:** `two-answers-to-one-question`. A criterion that quotes a table must carry the table's figures or name its margin.

### L2. AC2 never probes `rev-parse --show-toplevel` (id 6)

- **Where:** spec 17 section 6 AC2, against section 4 Mechanism item 1 and S1.
- **What is wrong:** Mechanism item 1 holds both `--git-common-dir` and `--show-toplevel`. AC2's nine reads cover only the first, and AC3 probes only the `^{tree}` read.
- **Consequence:** a rule that drops `--show-toplevel`, or mis-holds it, would show only as a spawn count inside AC4's slack.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** add `rev-parse --show-toplevel` at the top (True) and at `tools/` (False) to AC2, giving eleven expected entries.
- **Left-shift:** new class `criterion-probes-half-the-rule`. Each held case a mechanism names should map to one AC probe.

### L3. AC6 counts one `seen-red` line per plant, but the ledgers hold eight (id 8)

- **Where:** spec 17 section 6 AC6, against the section 7 New arm lines.
- **What is wrong:** named-probe has two `seen-red` lines and gc-predates has three, which matches section 7 and the ledgers on disk.
- **Consequence:** the count the main loop must reconcile is stated two ways, and a literal reading collapses the separate breaks.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** state eight lines in all (one each for dead-versions, released-rows and released-cost, two for named-probe, three for gc-predates), or drop the sentence and point to section 7.
- **Left-shift:** `two-answers-to-one-question`.

### L4. AC8's cost line was never timed and is about half the real figure (id 11)

- **Where:** spec 17 section 6 AC8 "cost:" line. Spec 20 AC5's "under 11 minutes at a 0.21 s gauge" line has the same premise.
- **What is wrong:** "about 10 minutes at a 0.21 s gauge" multiplies a 106 s reading, taken at an unrecorded gauge, by six. At 0.21 s, section 4's own sums put the five plants at 223.6 s before the edit and 157.7 s after it, so six readings take at least about 19 minutes. At that gauge, AC8's 106 s bound cannot turn green. (PINNED, 2026-11-26)
- **Consequence:** the close's time budget is misjudged, and so is whether AC8 is reachable.
- **Grade:** low (binding).
- **Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** re-derive the cost in both specs from timed sums at a named gauge. For spec 17 AC8, use section 4's 223.6 s and 157.7 s plus the bundle-* plants. For spec 20 AC5, use unit 17's post-edit serial sum for the reverted tree plus a pooled estimate for the tip. Then either drop the 106 s premise from both, or name the gauge at which a 106 s reading is reachable. (PINNED, 2026-11-26)
  - The finder's proposal cures spec 17's line alone: about 3 x (223.6 s + bundle plants) + 3 x (157.7 s + bundle plants), roughly 20 minutes or more, with a note that at 0.21 s AC8 can only read red on its 106 s bound. (PINNED, 2026-11-26)
- **Left-shift:** new class `cost-estimate-not-derived-from-timed-figures`.

### L5. Unit 20 misses the twin plant runner in positional.py (id 14)

- **Where:** spec 20 section 2 S1-S2, section 3 and section 9 (Reuse audit).
- **What is wrong:** tools/playbook/positional.py@3bbaecc5:743-754 (`tags positional selftest`) runs gov_tag.py plants with the same lazy `subprocess.run` and the same `out = p.stdout + p.stderr`. The spec names it nowhere.
- **Consequence:** the two runners in one kit would split. One would pool and turn exceptions into FAIL rows, and the other would stay serial and still traceback. The record has a gap, but no wrong behaviour ships.
- **Grade:** low. The finder graded it medium and the skeptic re-graded it low, because the twin keeps its current behaviour and the brief scopes the unit to tag_bundle.py. The synthesis keeps low.
- **Fix (judged SOUND by the skeptic):** name positional.py#run_selftest in section 9, then choose one of:
  - (a) put `run_plant_process` and the pooled run where both selftests can import them (for example tag_bundle.py, in the same directory), and add positional.py to the files touched and the gates;
  - (b) record in section 3, with a reason, that the positional leg keeps its serial runner.
- **Left-shift:** new class `twin-runner-left-unnamed`. The reuse audit should grep for the call shape being changed (`--fixture --plant`), not only for the symbol.

### L6. Unit 20 cites a WONTDO, disproved ask as the owner of the bar-slot class (id 15)

- **Where:** spec 20 section 3 (last bullet, line 55) and section 9 (line 211).
- **What is wrong:** TOOL-aReapedSpinner-23 is WONTDO. Its row reads "THE DIAGNOSIS IN THIS ROW WAS WRONG AND A GREEN BAR DISPROVED IT".
- **Consequence:** four processes in one bar slot look tracked when no live record owns the risk.
- **Grade:** low. The finder graded it medium and the skeptic re-graded it low, because section 4 and the GATE_JOBS rejection already cover the risk. The synthesis keeps low.
- **Fix (judged SOUND by the skeptic):** drop the citation from sections 3 and 9. Either state the oversubscription as this unit's accepted risk (section 4's "What it cannot see" already holds it), or file a new ask and cite its id.
- **Left-shift:** new class `cites-a-closed-record-as-owner`. `spec tokens` could refuse a non-goal that hands a class to a WONTDO or DONE row.

### L7. Unit 17's reuse audit misses the `patch.object` precedent for swapping module attributes (id 16)

- **Where:** spec 17 section 4 Mechanism item 3 and section 10.
- **What is wrong:** `set_git_held` hand-writes a save, set and restore of `ti.read_git_stdout` and `ti.git`. tools/loop/guard.py@c55c8905:805 and tools/loop/budget.py@f7926144:1337-1339 do the same with `contextlib.ExitStack` and `unittest.mock.patch.object`. Section 10's grep only matches assignments, so it reports two prior instances.
- **Consequence:** a few repeated lines and an understated audit. Behaviour is the same either way.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** build the swap from `ExitStack` and `patch.object(ti, "read_git_stdout", held)` / `patch.object(ti, "git", held)`, following guard.py. Or keep the hand-written form, name the precedent in section 10 with the reason it was not taken, and widen section 10's grep to include `patch.object`.
- **Left-shift:** new class `reuse-audit-grep-misses-a-form`.

### L8. Unit 20's gate list omits `tags` and `edges` and drops unit 17's timing restriction (id 18)

- **Where:** spec 20 section 6 (Gates) leg line and the prose under it.
- **What is wrong:** unit 20 re-versions the same two instruction_units extractors as unit 17, but it omits `tags (the resolver's checks)` and `edges (every declared edge parses, is registered and resolves)`, both of which unit 17 section 7 owes. It also lists `instruction units selftest` and `instruction edits (manifest checks)` without unit 17's "owed at the close ... by no pass before it" restriction.
- **Consequence:** unit 20's close does not observe the leg that pays its re-version, and the sibling specs give opposite timing instructions. Both legs are unguarded, so a full bar still runs them.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** add the two legs to unit 20 section 6, and either carry unit 17 section 7's sentence on when the live-index legs are owed or say why unit 20 differs.
- **Left-shift:** new class `sibling-spec-gate-list-diverges`.

### L9. Unit 20 AC5's red clause "a row reads higher" is unscoped (id 23)

- **Where:** spec 20 section 5 AC5 (Red when).
- **What is wrong:** `derive-ceilings.py --write` re-derives every leg's node-a row (line 558), and those rows can only rise (lines 560-562). "A row" can therefore be read as any row of ceiling-evidence.txt.
- **Consequence:** a legitimate raise of an unrelated leg could turn AC5 red.
- **Grade:** low (binding).
- **Fix (judged SOUND by the skeptic):** scope the red to "the `tags bundle selftest` row of either file", and record the other legs' movement in the ledger, as unit 17's AC8 records the file's diff.
- **Left-shift:** new class `red-clause-unscoped`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=23 confirmed=23 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=10 low=13 agents=11 out-tokens=138932 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 2 S5 against section 6 AC7 | medium | medium | confirmed | Re-probed. `git diff 712c9fe17~1 712c9fe17` on spec 17 changes only the status header, the records table, AC7 and the rev-3 log line. S5 at blob ca1d8aa0 lines 47-48 still reads 'times the five plants before and after the edit, back to back'. AC7 at lines 295-302 now asks for interleaved A/B pairs on the one built tree, with A as HELD_PLANTS emptied. So the scope item and the criterion that observes it ask for different measurements. A builder who follows S5 repeats the two-block method that rev-3 retired. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (MONOTONE branch and budget rule) against S6 | medium | medium | confirmed | Read lines 322-335. On green, the MONOTONE branch (tools/run-gates/derive-ceilings.py@b8c1709f:606-611 returns 1 when prev[0] >= obs_secs and writes nothing) still has the budget row rewritten by hand as 1.5 x max(worst after, the evidence row's value). AC8 is then also red when the budget row exceeds 159. Line 330 says that on red neither row is written. Line 334 accepts a node-a row that reads the retained maximum the MONOTONE line names. So when that maximum is over 106, the hand-written budget goes past 159: one criterion gives two verdicts, and a row has already been written on its red path. S6 at lines 50-52 says both rows come 'from the worst reading on the built tree', which the max() rule contradicts. Today ceiling-evidence.txt:149 holds 106.0 and selftest-budgets.txt:146 holds 159, so the conflict fires only on a narrow path. Unit 20 AC5 reuses this rule. | sound | - | class:two-answers-to-one-question |
| 3 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 3 (gov_tag.py non-goal: 'may build concurrently') against README build-order and unit 17 section 4 Files touched / AC8 | medium | medium | confirmed | Spec 20 at blob 9e0d027b lines 48-49 says 'The two write sets are disjoint, so the two units may build concurrently'. Its own Files touched (lines 107-112) and unit 17's (lines 198-204) both list memory/map/generated/symbols.json, selftest-budgets.txt and ceiling-evidence.txt. The README build order lists step 6 (unit 17) and step 7 (unit 20), each with Parallel 'no'. Spec 20's own edge (line 59) and AC5 (line 159) need unit 17's AC8 to run first. Both specs re-version the same two instruction_units extractors (spec 17 lines 185-188, spec 20 lines 100-103). The 'disjoint' claim is false, and it contradicts the generated order. | sound | - | class:two-answers-to-one-question (PINNED, 2026-11-26) |
| 4 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 3 Edges (hands-off external), section 1, and AC8 'opens the hand-off' | medium | medium | confirmed | Spec 17 lines 80-82 declare 'hands-off external ... as a unit the session owning this slug mints ... AC8's readings at the close decide it', and line 331 has AC8 red 'open the hand-off of section 3'. Spec 20 lines 18-19 say it is that pool and the owner approved it. Its line 59 declares consumes-from TOOL-aPrunedIndex-17, and the README lists it as SPECCED at order 7. So the edge pair does not match, and AC8 red tells the main loop to open a unit that already exists. The fix cures only the lines it names. Spec 17 also frames the pool as a conditional future hand-off at line 28 (section 1), at line 69 (non-goal: 'handed off below, for the case where AC8's readings miss'), at line 140 ('whether it is owed') and at line 222, all in sections 1, 3 and 4. | instance | two-answers-to-one-question | class:two-answers-to-one-question (PINNED, 2026-11-26) |
| 5 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 2 S1 against section 5 AC3 | medium | medium | confirmed | The stdlib signature printed '(args, returncode, stdout=None, stderr=None)'. tag_bundle.py run_selftest computes 'out = p.stdout + p.stderr', and S3 keeps that grading line unchanged. Spec 20 S1 (lines 25-27) and section 4 (lines 75-78) set only returncode None and stderr. A build that follows that text gets stdout None, and None + str raises TypeError out of run_selftest, which is exactly what AC3 calls red. AC3 would catch it at build time, so the effect is contained. | sound | - | new:fallback-leaves-a-graded-field-unset |
| 6 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC2 against section 4 Mechanism item 1 / S1 | low | low | confirmed | Spec 17 at blob ca1d8aa0. Mechanism item 1 holds both `rev-parse --git-common-dir` and `rev-parse --show-toplevel` when a `.git` entry stands at repo. AC2's nine reads are --git-common-dir at the top and at tools/, HEAD^{tree}, worktree list, ls-tree, rev-parse <id>^{tree}, diff, hash-object and rev-parse <id> HEAD. None is --show-toplevel. AC3 probes only the ^{tree} read. A rule that drops or mis-holds --show-toplevel would surface only as a spawn count inside AC4's slack. That leaves the rule part-checked, but nothing wrong ships, so the grade is low. | sound | - | new:criterion-probes-half-the-rule |
| 7 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC4 against section 4 spawn table | low | low | confirmed | The spec 17 section 4 table reads gc-predates 152 -> 86 and released-rows 331 -> 207. AC4 says 'at most section 4's with column' and then lists gc-predates 90 and released-rows 210. A count of 88 passes by one reading and fails by the other, so the bound has two answers. The other three figures (20, 17, 31) match the table. | sound | two-answers-to-one-question | class:two-answers-to-one-question |
| 8 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC6 against section 7 New arm lines | low | low | confirmed | grep of the acceptance ledgers prints eight seen-red lines. Unit 1 has one (line 25), unit 2 two (lines 20-21), unit 3 two (lines 23-24, released-rows and released-cost), unit 4 one (line 20) and unit 10 two (lines 21-22). So named-probe has two and gc-predates three, which matches section 7's arms ('its two', 'its three'). AC6's 'one `seen-red` line per plant' contradicts both. | sound | - | class:two-answers-to-one-question |
| 9 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (MONOTONE branch and its 'On green, also red when' clause); inherited by spec 20 section 5 AC5 and S5 | medium | medium | confirmed | I read tools/run-gates/derive-ceilings.py cmd_write. `remove_reset_rows(gd, reset)` (line 548) runs first and deletes the reset leg's non-ok rows from the retained run files. Then `read_runs(..., reset)` re-derives rows[(name,node)] = max of the ok readings, R. At line 601, `if prev and prev[0] >= obs_secs` prints a MONOTONE line naming R and returns 1 before the evidence file is written. So the file keeps 106.0 (ceiling-evidence.txt:149), which is not R unless R is 106. AC8's 'On green, also red when ... row afterwards reads neither <worst after> nor the retained maximum the MONOTONE line names' therefore fires on the branch the prose calls benign. 'Writes nothing' is also false for the run files the deletion has already rewritten. The refusal also fires at R == W (>=), while AC8 says only 'above'. Spec 20 AC5 writes 'by the call ... unit 17's AC8 spells', so it inherits the procedure. The effect is contained to the close's bookkeeping of the row. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 10 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 ('a detached worktree ... under `%TEMP%/pi17-base`'); same text in spec 20 section 5 AC5 (`%TEMP%/pi20-base`) | medium | medium | confirmed | In the Bash tool, `echo %TEMP%/pi17-base` printed `%TEMP%/pi17-base` and `echo "$TEMP"` printed `C:\Temp`, so Git Bash leaves `%TEMP%` unexpanded. PowerShell does too, since it uses $env:TEMP. `git grep -n %TEMP%` finds spec-17.md:317 and spec-20.md:161. So `git worktree add --detach %TEMP%/pi17-base` resolves relative to the cwd and nests a worktree inside the checkout. That breaks the scratch-location rule, but the effect is contained. | sound | - | new:cmd-syntax-in-a-bash-command |
| 11 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 'cost:' line | low | low | confirmed | Both blobs match their pins. tools/playbook/tag_bundle.py@8a284c47:391-411 runs the 14 SELFTEST_ROWS one after another, and those rows include all five plants. At a 0.21 to 0.23 s gauge, section 4 puts the five alone at 223.6 s before the edit and 157.7 s after it, so six readings take at least 3x223.6 + 3x157.7, about 1144 s or 19 minutes. AC7 already gets this right: it charges about 19 minutes for three rounds of the same 381 s. The 106 s row at ceiling-evidence.txt:149 records no gauge, only 'other sessions working on the node'. So AC8's '10 minutes at a 0.21 s gauge' line is wrong, and its 106 s bound cannot be met at that gauge. The mistake sits only in a cost estimate, so it is low. | instance | - | new:cost-estimate-not-derived-from-timed-figures (PINNED, 2026-11-26) |
| 12 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC4 versus section 4's spawn table | low | low | confirmed | Spec 17 section 4 table, lines 120-121, reads gc-predates 152 -> 86 and released-rows 331 -> 207. AC4 says 'at most section 4's with column' and then quotes gc-predates 90 and released-rows 210. The quoted figures contradict the column they claim to quote. The impact is limited because AC4's Red-when only fires when a count stays at its 'without' value, so either bound gives the same verdict. That leaves it a text contradiction, low. | sound | - | class:two-answers-to-one-question |
| 13 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 2 S1 / section 4 (the run_plant_process fallback) | low | low | confirmed | I re-ran the probe. CompletedProcess(['x'], None, stderr='OSError: probe') prints stdout None, and then None + str raises TypeError. Spec 20 S1 describes the fallback only by returncode=None and its stderr. S3 keeps the grading loop, and tools/playbook/tag_bundle.py@8a284c47:401 computes out = p.stdout + p.stderr. A literal build would therefore traceback on the exact path S1 exists to soften. AC3 fakes OSError('probe') for released-rows, and its Red-when names a traceback escaping, so the build would go red and be reworked. That makes the defect contained. | sound | - | new:fallback-leaves-a-graded-field-unset |
| 14 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 2 S1-S2, section 3, section 9 (Reuse audit) | medium | low | confirmed | tools/playbook/positional.py@3bbaecc5:743-754 holds a run_selftest for the 'tags positional selftest' leg (tools/gate-legs.json@2cf8c282:4919). It uses the same lazy `if plant not in runs` plus subprocess.run of gov_tag.py --fixture --plant, and the same `out = p.stdout + p.stderr`. Neither spec names positional.py, and git grep over the build matched only older unit-1 records. The twin exists and spec 20 does not record it, so the runners would split. The section 9 sentence 'no shared width exists' is about the max_workers literal and is still true. The brief scopes this unit to tag_bundle.py, and the twin keeps its current behaviour. The consequence is therefore a gap in the record, not shipped wrong behaviour, which grades low. | sound | - | new:twin-runner-left-unnamed |
| 15 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 3 (last bullet) and section 9 | medium | low | confirmed | memory/builds/aReapedSpinner/BACKLOG.md:23, under '## Dispositions', reads 'WONTDO · TOOL-aReapedSpinner-23 · THE DIAGNOSIS IN THIS ROW WAS WRONG AND A GREEN BAR DISPROVED IT'. Its slot-charging idea survives only as an uncosted candidate inside the quoted original text. Spec 20 section 3 (line 55) says that ask 'names' the bar-slot class, and section 9 (line 211) cites it as such. So a closed, disproved ask is presented as the owner of a live class. The effect is confined to non-goal prose, since section 4 and the GATE_JOBS rejection already cover the four-process risk. Low. | sound | - | new:cites-a-closed-record-as-owner |
| 16 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 4 Mechanism item 3; section 10 | low | low | confirmed | Spec 17 Mechanism 3 (blob ca1d8aa0) does say set_git_held 'saves ti.read_git_stdout and ti.git, sets both ... and in its finally sets both back'. Section 10's grep `^\s*[A-Za-z_]+\.(git\|read_git\|read_git_stdout) = ` only matches assignments and reports two prior instances. Re-running `git grep -nE "mock\.patch\|patch\.object" -- 'tools/*.py' \| grep -v selftest` printed tools/loop/guard.py@c55c8905:805 and tools/loop/budget.py@f7926144:1337-1339, which use ExitStack plus unittest.mock.patch.object to swap a module attribute for a block, plus tools/loop/breakpoints.py@88b47bb0:549 and tools/loop/factories.py@a933fc7b:989. So the audit misses that precedent. Behaviour is the same either way, so this is cosmetic. | sound | - | new:reuse-audit-grep-misses-a-form |
| 17 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 3 (Non-goals), the gov_tag.py bullet; section 4 Files touched | medium | medium | confirmed | Unit 20 section 3 (blob 9e0d027b) says 'The two write sets are disjoint, so the two units may build concurrently.' But its Files touched lists memory/map/generated/symbols.json and the two run-gates files. Spec 17's Files touched (lines 198-204) lists the same three. The README's gen:build-order table has step 6 TOOL-aPrunedIndex-17 'no' and step 7 TOOL-aPrunedIndex-20 'no'. Spec 17 AC8 takes its before-tree from the parent of 17's build commit (line 316), so if 20 landed first that baseline would already hold the pool. The claim holds. The effect is limited to merge conflicts and the measurement baseline. | sound | - | class:two-answers-to-one-question |
| 18 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 6 (Gates) leg line and the prose under it | low | low | confirmed | Unit 20 section 6 lists instruction units selftest and instruction edits as owed for the same re-version of the instruction_units extractors. It leaves out `tags (the resolver's checks)` and `edges (...)`, and it carries no 'owed at the close ... by no pass before it' restriction. Spec 17 section 7 (lines 344-349) lists all four and gives them that restriction. gov_tag.py imports tag_bundle (line 122) and instruction_units (line 44), and the tags and edges legs in tools/gate-legs.json carry no guard, so a full bar still runs them. The two specs give inconsistent instructions, but the effect is contained. | sound | - | new:sibling-spec-gate-list-diverges |
| 19 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 3 Edges (hands-off bullet), section 3 concurrency non-goal, AC8 red branch | low | low | confirmed | `git log` shows 99ecfb62c (spec TOOL-aPrunedIndex-20) before 712c9fe17 (17 rev-3). Spec 17 lines 68-69 and 80-82 still say `**hands-off** external` 'as a unit the session owning this slug mints', and AC8's red branch (line 331) says it 'opens the hand-off of section 3'. Unit 20 exists, declares consumes-from TOOL-aPrunedIndex-17, and says the owner approved it on 2026-11-26. .memory-tree.conf SPEC_HANDOFF_CUTOFF says 'a bullet naming `external` has no sibling to join', so the join between the two specs is never graded. These are stale records that could mislead the close, with no effect on product behaviour. | sound | - | class:amendment-leaves-its-other-half-standing (PINNED, 2026-11-26) |
| 20 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 (the MONOTONE branch and its Red when), section 2 S6 | high | medium | confirmed | In tools/run-gates/derive-ceilings.py cmd_write, `removed = remove_reset_rows(gd, reset)` (line 548) deletes the reset leg's non-ok rows from the retained .leg files before anything else. The reset leg's row is then re-derived from the retained ok runs. In the observed block (601-612), `prev[0] >= obs_secs` prints 'MONOTONE. Nothing was written.' and returns 1 before ceiling-evidence.txt is written. So the tracked row keeps its prior value. Today that is line 149, `tags bundle selftest 106.0 ... (TOOL-aPrunedIndex-4 AC8)`, an out-of-band row. It is neither `<worst after>` nor, except by coincidence, the retained runner maximum the MONOTONE line names. Spec 17 lines 326-327 accept this path ('writes nothing, and the evidence row stands'), while lines 333-335 make it red. The retained run files are also changed on this path. The finder graded this high. I grade it medium because the error is a false red at the close, a contained procedural misfire, and it never certifies a wrong result. Unit 20 AC5 follows 17's procedure, so fixing 17 fixes both. | sound | criterion-asserts-what-its-own-command-cannot-show | class:criterion-asserts-what-its-own-command-cannot-show (PINNED, 2026-11-26) |
| 21 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md:section 6 AC8 ('the tree before the edit ... the parent of the unit's build commit', 'the built tree') | medium | medium | confirmed | I re-read spec 17@ca1d8aa0 AC8. It takes its before-tree from 'a detached worktree at the parent of the unit's build commit', and its after-tree is just 'the built tree', never pinned to a commit. AC8 runs 'at the close'. Spec 20@9e0d027b section 3 says 'the two units may build concurrently'. Its Edges and AC5 only order unit 20's AC5 after unit 17's AC8, so nothing stops unit 20's build commit, which adds the pool, from reaching the tip before unit 17 closes. The README build-order table (lines 93-94) lists both steps as 'Parallel: no', which contradicts unit 20's sentence. On that path, AC8's 0.90 ratio and its 106 s bound would measure the pool's saving and credit it to unit 17. The effect is contained: the readings are real readings of the tip, and it needs the concurrent path to happen. | sound | - | new:measurement-tree-left-unpinned (PINNED, 2026-11-26) |
| 22 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 2 S1, section 4 (the exception path) | low | low | confirmed | Spec 20 S1 sets returncode None and stderr on the exception path and says nothing of stdout. I re-ran the probe: CompletedProcess(['x'],None,stderr='e').stdout printed None. tools/playbook/tag_bundle.py line 401 has `out = p.stdout + p.stderr`, and S3 keeps that grading loop unchanged. A literal build would raise TypeError (None + str) inside run_selftest, the crash S1 exists to prevent. AC3, which expects 'OSError: probe' as the indented output, would catch it at build time, so the effect is contained. | sound | - | new:fallback-leaves-a-graded-field-unset |
| 23 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md:section 5 AC5 (Red when: 'a row reads higher after the write than before it') | low | low | confirmed | tools/run-gates/derive-ceilings.py cmd_write loops `for name, vals in runs.items()` (line 558) over every leg and keeps prev only when prev >= mx (lines 560-562). So every --write can raise other legs' node-a rows, and spec 17 AC8 says as much ('also re-derives the other legs' rows'). Spec 20 AC5's red clause reads 'or a row reads higher after the write than before it'. The sentence before it speaks of 'the two rows', which suggests the narrower meaning, but the red clause itself is unscoped. A builder could read it as any row of ceiling-evidence.txt and turn AC5 red over a legitimate raise of an unrelated leg. The ambiguity is real and its effect is small. | sound | - | new:red-clause-unscoped |
