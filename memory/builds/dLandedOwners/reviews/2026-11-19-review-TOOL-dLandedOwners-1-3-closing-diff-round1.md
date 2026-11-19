**Serves:** diff-review TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3

# Closing diff review, round 1: dLandedOwners units 1 to 3, landed owners counted from build runs, module-constant reader keys and declared unscanned readers

Node `d` · 2026-11-19 · Tier-2 · on `branch/dLandedOwners` · adversarial fan through `tier2-review.js` (5 finder lenses, then 5 skeptic batches, then this synthesis). The diff closes ask TOOL-dTrackedAtlas-5 in the shipped policy kit (`tools/policy/check_policy.py`). Unit 1 widens `derive_landed_owners` into `derive_landed_builds`. Unit 2 teaches the reader scan a key passed through a module constant. Unit 3 adds `tools/policy/unscanned-readers.txt`, withheld from installs. Docs touched: `help/policy.md` and `tools/policy/README.md`.

**Reviewed range:** `51971579aed0c244f2d8b590dc4a79151d5806aa...b8297f70176502be8df21cfbc5366cbed3169b69`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high: the shipped predicate computes the right answer on every reachable path today. Five items are MEDIUM. One is a seam where `derive_run_kind` drops the `kit` its caller was given. Four are fixture gaps: the withholding of `unscanned-readers.txt`, the base intersection, the rotated run record and two arms of `derive_run_kind` each have no case that can go red. Four items are LOW: two doc inaccuracies, a git failure reported as untracked files, and a duplicated withheld set that drifted. All fold into the build before it closes.

## Review shape

Intensity **full** · raw **10** · confirmed **10** · refuted **0** · merged **0** · unverified **0** (0 uncertain) · precision **1.00**.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

The 10 confirmed findings collapse to **9 items**. The one merge is mine, made at write time: ids 1 (correctness) and 4 (seams) both describe `derive_run_kind` dropping `kit`. Each keeps its own binding grade, 1 LOW and 4 MEDIUM, and the item takes the higher.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 4 LOW** (9 items).

Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 5 LOW** (10 findings).

Every id keeps its bracketed binding grade. I re-grade none. The skeptic re-graded one finding (id 7, high to medium) before this synthesis, and that grade is binding.

No refuted findings and no same-address pairs were shown, so no twin is flagged.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified.
- **0** orphaned duplicate refutations demoted to unverified.
- **0** duplicate refutations counted as merged confirmations.
- **0** spurious verdicts discarded, **0** duplicates.
- Fixes on confirmed findings: **9** judged sound, **0** judged UNSOUND, **1** judged INSTANCE-ONLY (id 3), **0** none proposed, **0** NOT JUDGED.
- Severity on confirmed findings: **0** UNGRADED by the skeptic, **1** RE-GRADED by the skeptic (id 7).
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intent: no spec was supplied. `context` was the caller's statement, read beside the range's commit messages.
- Checklist: 38 items, acquired by the harness from `--for-diff 51971579aed0c244f2d8b590dc4a79151d5806aa..HEAD`, each assigned to one lens: security 8, correctness 8, seams 8, verification 7, intent 7.
- By design: the caller's byDesign.
- Refuted findings shown: 0. Same-address pairs shown: 0.

Every counter that must be zero is zero, so the run is complete. The security lens returned zero findings from a live run, which is evidence of absence within its checklist.

## MEDIUM

### M1. `derive_run_kind` drops the `kit` its caller was given (ids 1, 4)

- **Where:** `tools/policy/check_policy.py@782ffc07:532` (calls at 532-533), caller at `tools/policy/check_policy.py@782ffc07:642`.
- **What is wrong:** `derive_landed_builds(repo, builds, kit)` resolves the memory-tree kit from `kit` (`load_tree_lib_or_refuse(kit)` at 594, `load_run_readers(kit)` at 616). It then calls `derive_run_kind(repo, b, x, conf, families)` at 642 with no kit. `derive_run_kind` calls `load_tree_lib_or_refuse()` and `load_run_readers()` with no argument, so both default to the module's own `KIT`. Half 2 therefore resolves the memory-tree kit from two roots in one call.
- **Consequence:** The modules themselves come from `sys.modules`, which the earlier `load_run_readers(kit)` filled, so the computed answer does not change today. With a kit copy whose memory-tree differs from `KIT`'s, which is what the fixtures pass, two things can go wrong. A Refusal can fire naming `KIT`'s location when `kit`'s resolves. Or a module missing from the copy is hidden by `sys.modules`. Both break the docstring's promise that each miss is a Refusal naming where the resolver looked from `kit`. The `kit-modules-absent` case cannot catch it, because it refuses at 616 first. `resolve_kit_dir` and the existence check also re-run once per candidate base.
- **Grades:** id 1 LOW (binding), id 4 MEDIUM (binding). id 4's skeptic weighed that the dropped value will mislead the next change at the one place it decides where the modules come from, so the item is MEDIUM.
- **Fix (judged SOUND by the skeptic, both ids):** Give `derive_run_kind` a `kit` parameter, or pass in the already-loaded `(tree_lib, gbi, backlog, row_grammar)`. Thread `kit` from 642, and load the modules once per `derive_landed_builds` call, not once per base.
- **Left-shift gate:** Add a `policy fixtures` case that passes a kit copy whose memory-tree resolves while `KIT`'s is made unresolvable (or a copy missing one `RUN_READER_MODULES` file after `KIT`'s loaded), and expects the Refusal to name the copy's location. Record the class `kit-argument-dropped-at-an-inner-call` in the bug-class checklist: a function that takes a resolution root must thread it to every callee that resolves.

### M2. Nothing checks that `unscanned-readers.txt` stays withheld from installs (id 5)

- **Where:** `tools/policy/kit.toml@da41b1f1:35`.
- **What is wrong:** This diff adds `unscanned-readers.txt` to the `project-owned` include, so installs withhold it. No fixture checks this. `run_legacy_withheld_install` (`check_policy.py@782ffc07:1640-1665`) filters its plan rows and applied-target rglob on `policy.LEGACY_LIST` only. The install-target stray check (1515) and the descriptor check (2911-2923) also name `LEGACY_LIST` only. The `RD_CASES` fixtures write the list straight into a kit copy and never go through an install.
- **Consequence:** If the include is removed or undone by a later edit, every case stays green. Every adopter install would then ship gov's own row naming `memory/builds/dClosedLoop/...`. Once that adopter lands an owner called `dClosedLoop`, reader coverage reports a false "not a tracked file" red. The README's claim that the list is withheld goes unchecked.
- **Grade:** MEDIUM (binding).
- **Fix (judged SOUND by the skeptic):** Extend `legacy-homes-withheld-install` to run the same two checks over `UNSCANNED_LIST`: exactly one `ORDER [project-owned]` plan row for it, and no such file in the applied target. Then remove the entry from `kit.toml` in a probe and watch the case go red.
- **Left-shift gate:** Drive the withheld-install case from the `project-owned` includes in `kit.toml` instead of a hand-named constant, so every withheld file is checked by the `policy fixtures` leg the moment it is declared.

### M3. No carried-run case can fail on half 2's base intersection (id 7)

- **Where:** `tools/policy/check_policy.py@782ffc07:631` (`bases[b] & {base read from each landing merge's RUN.md}`).
- **What is wrong:** `build_carried_repo` writes `RUN.md` exactly once, as `RC_RUN.format(base)` on branch `run`. Every `RC_CARRIED` sub-case with a merge (`carried-landed`, `spec-run-landed`, `base-unresolved`) therefore reads the same base from the merge's `RUN.md` as from the record at L. `run-unlanded` has no merge.
- **Consequence:** If the intersection were dropped (for example `{read_run_base(...) for h in merges[b]}` without `bases[b] &`), every sub-case would still pass. A build would then read landed whenever any first-parent merge touched its `RUN.md`, including one that landed an earlier or different run. That widens which keys get graded, and the fixture leg would certify the predicate anyway. The shipped code is correct today.
- **Grade:** MEDIUM (binding; the finder graded high, the skeptic re-graded medium because the shipped code is correct and only the guard is missing).
- **Fix (judged SOUND by the skeptic):** Add an `RC_CARRIED` sub-case, for example `landing-other-base`, expecting 0 graded keys. Land one run through a `--no-ff` merge carrying base B1, then commit `RUN.md` with base B2 directly on main with no merge, so L's record carries B2 while the only landing merge carries B1. Confirm it goes red with the intersection removed before relying on it.
- **Left-shift gate:** Add a mutation pass to the `policy fixtures` leg's own self-check for each new predicate conjunct: stub the conjunct and require at least one case to go red.

### M4. The rotated run record `RUN.LANDED.<8 hex>.md` has no fixture (id 8)

- **Where:** `tools/policy/check_policy.py@782ffc07:483` (`RUN_RECORD`).
- **What is wrong:** `RUN_RECORD` accepts `RUN.LANDED.<8 hex>.md`, and the docstring, `help/policy.md` and the kit README say a rotated record counts. `build_carried_repo` only ever writes `memory/builds/bPlanted/RUN.md`. `RUN.LANDED` appears only in the three prose lines.
- **Consequence:** If the rotated alternative in the regex broke, or a rotated record's base stopped being read, a build whose live `RUN.md` was rotated away would read unlanded and its keys would go ungraded. Every case would still pass. The current code is correct.
- **Grade:** MEDIUM (binding).
- **Fix (judged SOUND by the skeptic):** Add an `RC_CARRIED` sub-case such as `rotated-landed`, expecting 1 graded key. After the landing merge, rename `RUN.md` to `RUN.LANDED.<8 hex>.md` on main in a plain commit. Confirm the case goes red when `RUN_RECORD` is narrowed to `^RUN\.md$`.
- **Left-shift gate:** Require each alternative of a record-name regex the predicate reads to be planted by at least one `policy fixtures` case, checked by the same per-conjunct mutation pass as M3.

### M5. Two arms of `derive_run_kind` have no failing case (id 9)

- **Where:** `tools/policy/check_policy.py@782ffc07:554` (the TERMINAL-disposal arm) and `tools/policy/check_policy.py@782ffc07:570` (the all-units-specced roster arm).
- **What is wrong:** No fixture `BACKLOG.md` holds a status row, so the disposal arm at 554 never runs. `carried-landed` has no `BACKLOG.md` and answers "build" through the early return at 556. `spec-run-landed` leaves the unit 2 spec out of the base, so it only ever answers "spec". No case reaches the roster with every unit specced, so the final "build" at 570 never runs.
- **Consequence:** If disposal reading broke (say `row.cls` compared to the wrong value), or the roster comparison inverted for the all-specced case, a build run would read as a spec run and not land. Its keys would go ungraded, and the fixture leg would still pass.
- **Grade:** MEDIUM (binding).
- **Fix (judged SOUND by the skeptic):** Add two `RC_CARRIED` sub-cases, each expecting 1 graded key. (a) The `spec-run-landed` repository plus a status row disposing TOOL-bPlanted-9 in `BACKLOG.md` at the base. (b) An open ask with both roster units' specs present at the base. Watch each go red with its arm stubbed to answer "spec".
- **Left-shift gate:** Extend the `harness arms (fail branches armed or pinned)` discipline to `derive_run_kind`'s return arms, so each return is either reached by a `policy fixtures` case or pinned with a reason.

## LOW

### L1. A failed `git ls-files` reads as "not a tracked file" (id 3)

- **Where:** `tools/policy/check_policy.py@782ffc07:760`.
- **What is wrong:** When the `git ls-files` over the declared paths fails, `policy.run_git` returns None. The `or ""` turns that into `tracked == {""}`, so every declared graded row is reported as "is declared read at <path>, which is not a tracked file" instead of as a git failure.
- **Consequence:** A git read failure (a locked index, a bad repo state) produces confident findings that the declared files are untracked. That misdirects whoever reads the red, and it is inconsistent with `derive_landed_builds`, which turns a failed git read into a Refusal. The result is still red, so nothing wrong is certified.
- **Grade:** LOW (binding).
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Make one helper that runs git and raises `policy.Refusal` naming the read when `run_git` returns None. Use it for the `ls-files` at 760 and for the reads it gates: `derive_scanned_files`' `ls-files` over `CODE_PATHSPECS` and its `rev-parse --show-prefix`. Keep `or ""` only where empty output is valid. The finder's proposal (check None separately at 760 and raise a Refusal naming that read) cures the cited instance alone.
- **Left-shift gate:** A `policy check` lint that reds `run_git(...) or ""` outside an allow-list of reads where empty output is valid.

### L2. `help/policy.md` says "runs of spaces" where the code splits on any whitespace (id 2)

- **Where:** `help/policy.md@b502511c:170`.
- **What is wrong:** The user page says a row of `unscanned-readers.txt` is "split on the first two runs of spaces". `read_unscanned_readers` uses `line.split(None, 2)`, which splits on any whitespace, tabs included, and `tools/policy/README.md` says "whitespace".
- **Consequence:** An author following the user page may put a tab in a path. The code then cuts the path at the tab, and the row is reported as not tracked or accepted at a different path. A tab inside the reason survives `maxsplit=2`, so the effect is near zero.
- **Grade:** LOW (binding).
- **Fix (judged SOUND by the skeptic):** Change `help/policy.md:170` to "split on the first two runs of whitespace (spaces or tabs)".
- **Left-shift gate:** Bug-class checklist entry: a row grammar is stated in one place and the other docs point to it, never restate it.

### L3. The govkit fixtures' hand-copied withheld set misses `unscanned-readers.txt` (id 6)

- **Where:** `tools/govkit/shims.py@e70d5f7e:428`, `tools/govkit/fixtures/stale_edges.py@a14d44cb:44`, `tools/govkit/fixtures/retired_edits.py@2688653e:138`.
- **What is wrong:** All three copy the policy kit as an install-shaped tree with `shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt")`, which mirrors `kit.toml`'s withheld set. This diff withheld `unscanned-readers.txt` but did not add it to these lists.
- **Consequence:** The copies now hold a file a real install never holds, so the fixtures stop matching the install shape they stand in for. None of the three runs reader coverage or `check_policy`, so no behaviour changes today.
- **Grade:** LOW (binding).
- **Fix (judged SOUND by the skeptic):** Add `"unscanned-readers.txt"` to the three ignore lists. Better, derive the list from the `project-owned` includes in `kit.toml`, so the withheld set lives in one place.
- **Left-shift gate:** One shared helper that reads `kit.toml`'s withheld includes, and a `govkit selfcheck` arm that reds a literal `ignore_patterns(... "legacy-homes.txt" ...)` restatement.

### L4. The module docstring still defines landed the old way (id 10)

- **Where:** `tools/policy/check_policy.py@782ffc07:20` (lines 20-21).
- **What is wrong:** The header says `arm_reader_coverage` reds a key "whose owner build has landed, every spec in its build folder terminal at the landed revision". This diff edited the same sentence (it gained the module-constant clause) but left the predicate unit 1 replaced. `help/policy.md` and the kit README were updated.
- **Consequence:** No behaviour changes. A reader trusting the header would expect `dDeclaredLoop` and `dSafePassage`, which have DEFERRED specs, not to be graded, yet `check_reader_coverage('.')` names both as landed owners. That misleads the next change to the arm.
- **Grade:** LOW (binding).
- **Fix (judged SOUND by the skeptic):** Restate the clause to match `derive_landed_builds`, for example "whose owner build has landed by derive_landed_builds (every spec terminal at the landed revision, or a build-kind run record with a first-parent landing merge, TOOL-dLandedOwners-1)".
- **Left-shift gate:** Bug-class checklist entry (an amendment leaves its other half standing): when a predicate is replaced, grep every prose restatement of it, module headers included.

review-shape kind=diff-review round=1 intensity=full at=synth raw=10 confirmed=10 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=5 low=5 agents=11 out-tokens=65920 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/policy/check_policy.py:532 | low | low | confirmed | Observed in tools/policy/check_policy.py: derive_run_kind (line 525) calls load_tree_lib_or_refuse() at 532 and load_run_readers() at 533 with no argument, so both default to KIT. derive_landed_builds(repo, builds, kit) calls load_tree_lib_or_refuse(kit) at 594 and load_run_readers(kit) at 616, then calls derive_run_kind at 642 with no kit. So the file-existence check in half 2 runs a second time against KIT's memory-tree, not the caller's. This contradicts the docstring's claim that misses are resolved "from `kit`". The modules themselves come from sys.modules, which the earlier load_run_readers(kit) call filled, so the computed answer does not change. The only effects are a Refusal naming the wrong location, or a miss that never surfaces, and both need a kit argument whose memory-tree differs from KIT's. In practice that is a fixture path. The effect is contained, so low. | sound | - | new:kit-argument-dropped-at-an-inner-call |
| 2 | correctness | help/policy.md:170 | low | low | confirmed | help/policy.md lines 169-170, added in this diff, say a row is "split on the first two runs of spaces". read_unscanned_readers uses line.split(None, 2), which splits on any whitespace, and both its docstring and tools/policy/README.md:527-528 say "whitespace". The user page therefore states the rule differently from the code and the kit README. The behaviour only diverges if a tab appears in the key or the path, because a tab inside the reason survives maxsplit=2. That makes this a documentation inaccuracy with almost no effect, so low. | sound | - | class:two-answers-to-one-question |
| 3 | correctness | tools/policy/check_policy.py:760 | low | low | confirmed | policy.run_git (tools/policy/policy.py:333-340) returns None on a nonzero exit or OSError. At check_policy.py:760, which is new in unit 3 and not in the base, `(... or "").split("\0")` turns that None into tracked == {""}. Every declared graded path then fails `path not in tracked` and is reported as "not a tracked file" instead of as a failed git read. derive_landed_builds turns a failed read into a Refusal. The result is still red, so nothing wrong is certified, only misattributed. That makes it low. | instance | - | class:staged-break-substitutes-a-synthetic-value |
| 4 | seams | tools/policy/check_policy.py:532 | medium | medium | confirmed | derive_landed_builds(repo, builds, kit) calls load_tree_lib_or_refuse(kit) at line 594 and load_run_readers(kit) at line 616. derive_run_kind (line 525) takes no kit and calls load_tree_lib_or_refuse() and load_run_readers() with the default KIT at lines 532-533, so the kit it was given is dropped. The imports themselves come back from sys.modules, which were loaded from `kit` first. So in practice the dropped kit causes two things. The existence check and resolve_kit_dir run a second time against KIT's location, once per candidate base. A spurious Refusal can fire when KIT's memory-tree does not resolve but kit's does. In production kit == KIT, and gov's own KIT resolves in the fixtures, so the effect is contained. It is still a real seam defect that will mislead the next change, so medium. | sound | - | new:kit-argument-dropped-at-an-inner-call |
| 5 | seams | tools/policy/kit.toml:35 | medium | medium | confirmed | This diff adds `unscanned-readers.txt` to the `project-owned` include in tools/policy/kit.toml (line 35). Nothing checks that it stays withheld. run_legacy_withheld_install (check_policy.py:1640-1665) filters its plan rows and its applied-target rglob on policy.LEGACY_LIST only. The install-target stray check at check_policy.py:1515 filters on LEGACY_LIST only. The descriptor check at check_policy.py:2911-2923 looks for a project-owned rule naming LEGACY_LIST only. The RD_CASES fixtures (check_policy.py:3172-3225) write the list straight into a kit copy and never go through an install. Grepping tools/ finds no other test of the withholding. So if the include is removed, every case stays green, and the README and docstring claim that the list is withheld goes unchecked. The adopter consequence the finder describes needs that regression and a landed owner, so the effect is contained. | sound | - | class:rule-stated-with-no-check-that-fails |
| 6 | seams | tools/govkit/shims.py:428 | low | low | confirmed | All three ignore lists read `shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt")`: tools/govkit/shims.py:428, tools/govkit/fixtures/stale_edges.py:44 and tools/govkit/fixtures/retired_edits.py:138. None was updated when this diff withheld `unscanned-readers.txt`, so the copied policy kit now carries it. Grepping those three files shows none of them runs reader coverage or check_policy, so no behaviour changes. The only result is that the duplicated withheld set has drifted from kit.toml. | sound | - | class:two-answers-to-one-question |
| 7 | verification | tools/policy/check_policy.py:631 | high | medium | confirmed | I checked this at b8297f70. In build_carried_repo (check_policy.py ~3095-3140), RUN.md is written exactly once, as RC_RUN.format(base) on branch `run`, and then merged with --no-ff, or with --ff-only for run-unlanded. Every RC_CARRIED sub-case that has a merge therefore reads the same base from the merge's RUN.md as from L's record. If line 631 were replaced by `{read_run_base(...) for h in merges[b]}` without `bases[b] &`, every sub-case would produce the same result, so the leg cannot fail on the intersection. The predicate is new in this diff (the base has no derive_landed_builds or RUN_RECORD). The shipped code is correct today. The gap is that the fixture does not guard the intersection, so its effect is contained, which grades medium rather than high. | sound | - | class:rule-stated-with-no-check-that-fails |
| 8 | verification | tools/policy/check_policy.py:483 | medium | medium | confirmed | RUN_RECORD (line ~483, new in this diff) accepts `RUN.LANDED.<8 hex>.md`, and the docstring at 578, help/policy.md:150 and README.md:490 document it. A git grep at b8297f70 finds RUN.LANDED only in those three prose lines. build_carried_repo writes only RC_FOLDER/RUN.md. The rotated route therefore has no fixture that can go red, for example if the regex were narrowed to ^RUN\.md$. The proposed fix works. With RUN.md renamed on main after the landing merge, the runs list at L holds only the rotated record. The merges log on the RUN.md path still finds the landing merge, whose RUN.md carries the same base, so the case grades 1 key. Narrowed to ^RUN\.md$, runs is empty and the case grades 0, so it goes red. The current code is correct and the gap is contained. | sound | - | class:rule-stated-with-no-check-that-fails |
| 9 | verification | tools/policy/check_policy.py:554 | medium | medium | confirmed | At b8297f70, derive_run_kind (check_policy.py:525-570) is called only from derive_landed_builds:642. Its only fixture coverage is build_carried_repo/RC_CARRIED (lines 3091-3140). In every case except spec-run-landed, no BACKLOG.md is written, so the function takes the early return at line 556 and answers "build". spec-run-landed writes RC_ASK with no status row and leaves the unit 2 spec out of the base, so it always answers "spec". No case writes a status row, so the TERMINAL-disposal branch at line 554 never runs. No case reaches the roster with every unit specced, so the final "build" at line 570 is never reached. A mutation of either arm would leave the fixture leg green. The diff added this code, so the gap is in scope. The effect is limited to under-grading keys in a corner case, which makes it medium. | sound | - | class:rule-stated-with-no-check-that-fails |
| 10 | intent | tools/policy/check_policy.py:20 | low | low | confirmed | At b8297f70, lines 20-21 of check_policy.py still define landed as 'every spec in its build folder terminal at the landed revision'. The derive_landed_builds docstring (lines 573-589) says a build also lands through a build-kind run record with a first-parent landing merge. This diff edited that same sentence and left the stale predicate. git grep shows this is the only stale instance in tools/, help/ and README.md. It changes no behaviour, since it is header prose only, so it is low. | sound | - | class:amendment-leaves-its-other-half-standing |
