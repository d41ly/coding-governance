**Serves:** spec-audit TOOL-dSafePassage-72@rev-3 TOOL-dSafePassage-73@rev-3 TOOL-dSafePassage-74@rev-2 TOOL-dSafePassage-75@rev-2 TOOL-dSafePassage-76@rev-3 TOOL-dSafePassage-77@rev-3 TOOL-dSafePassage-78@rev-1 TOOL-dSafePassage-80@rev-4 TOOL-dSafePassage-81@rev-3 TOOL-dSafePassage-82@rev-3 TOOL-dSafePassage-83@rev-4

# Tier-2 spec audit: dSafePassage, units TOOL-dSafePassage-72 to -78 and -80 to -83, ROUND 1

*This is the round-1 adversarial audit, done before any code, of the eleven units dSafePassage added at its close, 2026-10-28.
Units 72 to 75 promote the HIGH findings of the closing diff review (`memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`).
Units 76 and 77 batch that review's mediums and lows by write set.
Units 78 and 80 to 83 repair the reds of the close's discovery bar (`C:/Users/DAILY-~1/AppData/Local/Temp/dsp-bar-83817478f.log`).
All eleven build at order 16, with 81 stated last.
Five finder lenses read the set, and a skeptic tried to refute each finding.
This report carries only what the skeptics confirmed, at the grade the skeptic bound, and it adds no finding and drops none.*

Reviewed: memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md@69f87f189727edc1e50a1fba1f929283da5d3d00, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-73.md@e94ebee1e082c10a9b187f1bfc85137c93082a2d, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md@a7139405456fe96281b0e6fbe64d84854f8dc49b, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-75.md@3ae3cd17efe062d33e1a0fb7d9c0284f695c60c8, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md@08ce7c3f05c2623037e2a215f70507dafa5665ea, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md@4ba5e9ae44ba207b670ee8b355d79a4897d25df4, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-78.md@ef1673c5980f73cb299b788a119d57228b4951a1, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md@ed18f7128b5a99a492591dc7942b09b73d506581, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-81.md@f5baf45b4fc975602070b8fe4a41a40e351a72d8, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md@12a7f26be3deff4c8a2654fd6a02a9c7407bb159, memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md@5ad147311c8ee247adefa05bb21a2a30b1dbcb25

ROUND: 1

## Verdict: CLEAN WITH FIXES

No finding is a blocker.
One HIGH, sixteen MEDIUM and sixteen LOW items stand, and each must be fixed in its spec before the unit builds.
The HIGH (item H1) concerns unit 77's tree-clean check against the dirty evidence file that unit 80 commits, and its fix needs a dispatch-order ruling.

## Review shape

Intensity full, raw 40, confirmed 35, refuted 5, unverified 0 (0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 12 | 11 | 1 | 0 | 0 | 0.92 |
| reuse | yes | 5 | 3 | 2 | 0 | 0 | 0.60 |
| blast-radius | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |
| failure-envelope | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |

Adjudicated tally by item: 33 items, of which 0 BLOCKER, 1 HIGH, 16 MEDIUM and 16 LOW.
Adjudicated tally by raw confirmed finding: 35 findings, of which 0 BLOCKER, 1 HIGH, 16 MEDIUM and 18 LOW.
The two LOW items that merge findings are L1 (ids 5 and 21) and L2 (ids 6 and 22).
Four defects were found by two lenses at different binding grades, so each became two items, cross-referenced below: ids 16 and 35, ids 3 and 40, ids 29 and 9, ids 30 and 20.
Four findings were re-graded by the skeptic: 17 (medium to low), 24 (medium to low), 28 (high to medium) and 37 (low to medium).
Every item follows its binding grade.

## Run integrity

- Lenses 5/5 returned, 0 DIED.
- Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 33 judged sound, 2 judged UNSOUND (ids 14 and 35, where the skeptic's corrected fix is written below), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 4 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: no spec was supplied, and `context` was the caller's statement.
- Checklist: NONE swept, because it is absent. A zero count is not evidence that the project's recurring bug classes are absent.
- By design: the caller's byDesign.
- Move check: no checked subject moved.

## HIGH

### H1. 77's tree-clean check refuses the walk on the evidence file 80 has yet to commit (id 35)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md`, §2 S3, §6 AC5 to AC8, and §4 Rollout.
- **What is wrong:** S3's `check_tree_clean` stops the leg with exit 2 on any dirty tracked path outside the leg's three own files. The build worktree already holds such a path: `tools/run-gates/ceiling-evidence.txt`, the close's uncommitted evidence, which TOOL-dSafePassage-80 S4 commits. The dispatch order builds 77 before 80. 77's own S5 and S8 edits to `BACKLOG.md` and `help/upgrade-steps.md` also lie outside `own`.
- **Consequence:** Every upgrade-walk run from 77's build until 80 lands exits 2 before it measures anything. That covers AC6, AC7, AC8 and the bar leg. The leg's message says 'commit or stash them'. Following it either commits 80's evidence under 77 or stashes or discards it, and 80 §3 forbids re-creating that evidence by hand or by any `--write` run. The 7177 s reading would be lost.
- **Fix (finder's fix judged UNSOUND, so this is the skeptic's corrected fix):** State in 77 §4 Rollout that 77 builds after 80, whose S4 commits `tools/run-gates/ceiling-evidence.txt`, and that 77's walk ACs run only after its own non-leg edits are committed. Narrow `check_tree_clean` to the engine files the walk takes from HEAD, for example `git status --porcelain --untracked-files=no -- tools/govkit tools/lib` minus `own`, and never the whole tree. Add S7 tree-clean grader rows in which a dirty file under `memory/` and a dirty `tools/run-gates/ceiling-evidence.txt` each return `[]`. The build observes those rows red against the as-written predicate.
- **Related:** M8 (id 16) is the same predicate's over-reach, graded MEDIUM.
- **Left-shift gate:** add a bug-class checklist entry, "a dirty-tree refusal names its population as the paths the check reads, never the whole tree, and ships a grader row for an unrelated dirty file". Add a spec-template check that a unit's Rollout names every sibling whose uncommitted output its ACs run over.

## MEDIUM

### M1. 80 and 82 stage the watched `tools/gate-legs.json` with no last-audit re-stamp (id 1)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md` §4 Files touched and §7 Gates. The same gap is in TOOL-dSafePassage-82 §4 Files touched and §7.
- **What is wrong:** `.githooks/pre-commit` runs `manifest-check --staged`. That check refuses a commit that stages a watched path, and `tools/gate-legs.json` is watched by `memory/guides/SESSION-KICKOFF.md`:6, unless the same commit re-stamps `last-audit`. Neither spec lists `memory/guides/SESSION-KICKOFF.md`, the §B re-audit, or the `kickoff-manifest ratchet` leg. 83 S4 assumes its own advance is the only one.
- **Consequence:** The pass commits of 80 and 82 are refused at pre-commit. To land them, the builder has to make an unscoped edit to a file 83 owns, and no criterion observes that edit.
- **Fix (judged sound):** Add `memory/guides/SESSION-KICKOFF.md` to the Files touched of 80 and 82, with an S-item that re-stamps `last-audit` after re-reading the §B claims that `gate-legs.json` feeds, as every earlier commit touching `gate-legs.json` did. Add `kickoff-manifest ratchet` to both §7 lines. Say in 83 §4 Rollout that `last-audit` will already have moved twice before 83 runs.
- **Left-shift gate:** have the spec-writer derive each unit's Files touched through `manifest-check`'s WATCH list, so that a watched path in scope pulls in SESSION-KICKOFF.md and the ratchet leg.

### M2. 80 commits node-d readings tagged node `a`, and AC5 locks the tag in (id 2)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md` §2 S4, the §3 non-goal on the node column, and §6 AC5.
- **What is wrong:** The three evidence rows were taken on node d over a tree with a 3.15 floor, which node a cannot run (RUN.md:16 records that node a resolves only 3.14.6). They were written under a `GOV_NODE=a` override. §3 says the readings were taken on node a, and AC5 goes red if a row names another node.
- **Consequence:** The build commits false provenance, and its own criterion pins it. `derive-ceilings.py` refuses a defaulted `--observed` node precisely because a wrong tag is 'a false claim about provenance'. Seconds are unaffected.
- **Fix (judged sound):** Correct §3 to name node d. Have S4 carry the rows as node d, through an owner-ruled `--reset` of the three rows (monotone refusal blocks a re-run of `--write --observed`) or through a §3 ruling that states the mislabel. Change AC5's red-when so it no longer requires node `a`.
- **Left-shift gate:** have `derive-ceilings.py --write --observed` refuse a `GOV_NODE` whose resolved Python cannot satisfy `tools/lib/python-floor.txt`.

### M3. 77 AC6 expects one hit of the phrase where a correct build leaves two (id 3)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md` §6 AC6.
- **What is wrong:** AC6 requires `git grep -c -F "is absent at release-0" -- tools/govkit/upgrade_walk.py` to print 1. The phrase occurs at :23 (module docstring), :145 (the Stop in `write_plant_edits`) and :847 (the Stop in `check_inject`). S6 removes only :847.
- **Consequence:** The criterion cannot pass on a correct build unless the builder deletes the docstring's accurate exit-2 cause.
- **Fix (judged sound):** Count only Stop sites, for example `git grep -c -F 'is absent at release-0")' -- tools/govkit/upgrade_walk.py` prints 1, or state that the expected count is 2 and name the docstring line.
- **Related:** L16 (id 40) is the same defect, found by another lens and bound LOW.
- **Left-shift gate:** the spec-writer runs every grep-count AC at base and records the base count beside the expected count.

### M4. 76 S9 adds the required-`<to>` sentence without removing the default-to-HEAD clause (id 4)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md` §2 S9, the §4 'The pages' row for `help/python-floor.md`, and §6 AC9.
- **What is wrong:** S5 makes `<to>` required outside gov. The page row only adds a sentence and does not say 'in place of'. AC9 checks only that the new phrase is present. Nothing removes `help/python-floor.md`:75-76, which says that when `<to>` is left out it defaults to the target's `HEAD`.
- **Consequence:** A build that passes AC9 can ship a page telling adopters both that `<to>` is required and that it defaults to HEAD.
- **Fix (judged sound):** Have the S9 row replace the existing default clause at `help/python-floor.md`:75-76. Add a negative grep to AC9, for example `git grep -n -F "defaults to the target's" -- help/python-floor.md` prints nothing.
- **Related:** L15 (id 34) covers the stale usage line at :74.
- **Left-shift gate:** add a checklist entry saying that a help-page row which changes a contract carries an 'in place of' clause and a negative grep for the retired text.

### M5. 72 AC2 is green at base because govkit already refuses `a:b` (id 11)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §6 AC2 and §4 'One answer to one question'.
- **What is wrong:** `govkit.py`:1244-1246 refuses `dest[1] == ":"`, so `a:b` is refused at base. AC2's probe prints `True a/b` at HEAD. Its red-when line and §4's 'misses an alternate data stream `a:b`' are both false. `ab:c` and `x/a:b` pass at base.
- **Consequence:** AC2 passes whether or not S2 is built, and no criterion exercises the colon-anywhere tightening that F1(a) ruled for govkit's destinations.
- **Fix (judged sound):** Replace `a:b` in AC2's list, and in AC1's for symmetry, with a colon past index 1, such as `ab:c` or `x/a:b`. Correct the §4 sentence to name that form.
- **Left-shift gate:** a spec-audit check that each AC's red case is run at base and recorded red. An AC observed green at base is refused.

### M6. 72's escape probe, run red at base, writes to the drive root and an admin share (id 12)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §4 'Observed at base' (UNC row), §6 AC3 and its note, and the §7 New arm (observed RED at base).
- **What is wrong:** The §4 row says the UNC form resolves to `C:\localhost\c$\x.txt`. At base, `check_contained` returns `\\localhost\c$\x.txt`, and the rooted form returns `C:\rooted.txt`. `write_from_before_image` then calls `cur.write_bytes`, and AC3's probe catches only `us.Refusal`.
- **Consequence:** The required RED-at-base observation can go wrong three ways. As a standard user it dies with PermissionError, which is red for the wrong reason. Elevated, it writes to `C:\` and over SMB to the admin share, outside the scratch directory the stray scan watches. Either way it opens a network share.
- **Fix (judged sound):** Correct the §4 UNC row to `\\localhost\c$\x.txt`. In AC3 and the arm, check the rooted and UNC forms through `read_image_paths` and `check_contained` alone, which write nothing, and keep `write_from_before_image` for the `..\` form, whose escape stays inside the scratch tree. Alternatively, have the probe catch every exception and record its type, so a base run reads red without writing.
- **Left-shift gate:** add a checklist entry saying that a probe observed red at base never calls a write path with an input that can escape the scratch tree.

### M7. 76 AC7's grep cannot see the sixth argument at the wrapped govkit calls (id 14)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md` §6 AC7.
- **What is wrong:** The clause `git grep -n "run_step_walk(" -- tools/` shows no call passing a sixth argument. Both govkit.py calls wrap, and `to_commit)` sits alone at :9455 and :11727, lines the grep never prints.
- **Consequence:** A build that drops the parameter but leaves `to_commit` at a caller passes AC7, and every `update --write` then raises TypeError at run time.
- **Fix (finder's fix judged UNSOUND, so this is the skeptic's corrected fix):** Keep the single-line grep, which covers `selftest.py`:4448 and the `FIXTURE_WALK_CHILD` string at `upgrade_steps.py`:3407. Add a `python -c` check that parses `govkit.py` and `selftest.py` with `ast` and asserts that every Call whose func ends in `run_step_walk` has `len(args)+len(keywords) == 5`. Also parse the `FIXTURE_WALK_CHILD` string with `ast.parse` and apply the same assertion to it.
- **Left-shift gate:** add a checklist entry saying that an arity criterion is an AST check, never a line grep, and covers callers embedded in string fixtures.

### M8. 77's tree-clean check refuses on any tracked edit, not only engine edits (id 16)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md` §2 S3 and §5 risks.
- **What is wrong:** §5 says the leg exits 2 'on a local run over uncommitted engine edits'. S3 refuses any modified tracked path outside the three own paths, including records, help pages and run-gates evidence, none of which the walk reads.
- **Consequence:** A held run in a mid-build tree with any bookkeeping edit reports `nothing measured`. This worktree has one such edit now, and 83 §3 records 65 uncommitted ledger edits at writing. `run-gates.sh` still runs the legs on a dirty tree.
- **Fix (judged sound):** Narrow `own` to the inverse: refuse only modified paths the walk's clone or engine could read. Or state in §5 and the help page that any tracked edit refuses the leg, and add a `tree-clean` grader row for a dirty `memory/` file so the chosen rule is pinned.
- **Related:** H1 (id 35) is this predicate's collision with 80's evidence file, graded HIGH. A single narrowing cures both.
- **Left-shift gate:** the H1 checklist entry covers this class.

### M9. 80's cost finding omits the nightly held CI run its budget row enrolls (id 18)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md` §3 'Finding for the owner' (Who pays it) and §2 S5.
- **What is wrong:** The finding says remote CI does not pay for the leg. `remote-ci.yml` builds its daily held matrix from `run-selftests.sh --list`, which reads `selftest-budgets.txt`. S5's row therefore enrolls `upgrade-walk` at a bound of 10770 + 10770 = 21540 s, over the 21000 s cap, so it runs platform-bounded on hosted windows-latest every day.
- **Consequence:** The owner rules on an incomplete cost picture: up to about 5.8 h of extra daily CI. A runner about 3x slower than node a is killed at the cap, and the nightly schedule reds.
- **Fix (judged sound):** Add the nightly held job to 'Who pays it', naming `remote-ci.yml`'s held-plan population and this row's run bound (21540 s bound, capped at 21000 s, platform-bounded). Either keep the row and accept that cost, or hold the row out of the scheduled matrix by the mechanism the file offers, as an owner choice.
- **Left-shift gate:** have `run-selftests.sh --list` (or a check over `selftest-budgets.txt`) flag a new row whose bound exceeds the remote cap, so a budget row cannot land platform-bounded unnoticed.

### M10. 80's budget row puts upgrade-walk into foreign-prefix parity, which it does not honour (id 28)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md` §2 S5, §7 Gates, and §4 'The budget row'.
- **What is wrong:** `foreign-prefix parity (every self-test at three prefixes)` takes every row `run-selftests.sh --list` prints and requires each to print the FOREIGN_PREFIX_PROBE marker, unless the row is declared in WHOLE_RUN or GOV_LAYOUT. `upgrade_walk.py` does not honour the probe, and the spec never names the leg.
- **Consequence:** Every bar running the held legs reds that leg as 'an undeclared whole run'. Otherwise it runs three walks of about 7177 s each, past its own 7500 s ceiling. This unit sets out to turn one held leg green, and as written it turns another red.
- **Grade:** the finder graded this high. The skeptic bound medium because the failure is loud on the bar, not a silent wrong result.
- **Fix (judged sound):** Name `foreign-prefix parity (every self-test at three prefixes)` in §7, and add a scope item that settles the row's place in its population. Either `upgrade_walk.py` honours `FOREIGN_PREFIX_PROBE=1` by stopping after its first subject-touching case and printing `foreign-prefix-probe: stopped after 1 arm`, or the row gets a GOV_LAYOUT or WHOLE_RUN declaration in `tools/run-gates/foreign-prefix.gov.test.sh`, its cost weighed against the 7500 s ceiling. Run `bash tools/run-gates/foreign-prefix.gov.test.sh --plan` with the row staged, and show that upgrade-walk is classified and not red.
- **Left-shift gate:** have foreign-prefix parity's `--plan` run in the fast tier whenever `selftest-budgets.txt` is staged, so an unclassified row reds at commit.

### M11. Five specs mint Python top-level names without the symbols.json regeneration or the map leg (id 29)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §4 Inventory / Files touched and §7. The same gap is in -73, -76, -77 and -82.
- **What is wrong:** 72 (`derive_contained_rel`), 73 (`test_up_unrecorded`), 76 (`read_git_dir`, `derive_gov_root`), 77 (four `upgrade_walk.py` functions) and 82 (the floor step program's `main`) add names that `memory/map/generated/symbols.json` maps. None lists that file or names `codebase-map coverage + freshness` in §7. Only 81 regenerates the map, and it builds last.
- **Consequence:** The pre-commit codebase-map gate refuses the first commit of 72 and each later sibling's, unless each pass writes a file outside its declared write set. M6 sequences passes by write set, and this shared write set is undeclared.
- **Fix (judged sound):** Add `memory/map/generated/symbols.json` to Files touched in 72, 73, 76, 77 and 82, and `codebase-map coverage + freshness` to their §7 lines. Each pass runs `python tools/codebase-map/gen_map.py --write` in the same commit, as 81 §4 Rollout already does. Correct 81's claim that it alone moves the map.
- **Related:** L9 (id 9) is the Files-touched half, found by another lens and bound LOW.
- **Left-shift gate:** a spec-audit check that a spec whose Files touched holds a `.py` under a mapped path also lists `symbols.json` and the map leg.

### M12. 81 §7 omits `lexicon wiring`, a leg its offenders turned red (id 30)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-81.md` §7 Gates.
- **What is wrong:** `lexicon wiring` runs `adopt-lexicon.sh --check` on every bar and re-runs `lexicon.py` against the pin this unit moves. It was red at the discovery bar on the same 1281-over-1212 count, and 82 §3 assigns it to 81. 81 §7 names only `lexicon naming predicates`.
- **Consequence:** A leg this build turned red belongs to no unit's gate list. Its other arms (the canon-overlay arm, `check_skill`) go unobserved until the close bar.
- **Fix (judged sound):** Add `lexicon wiring` to 81's §7 line, with a sentence saying its failing case is the discovery bar's red at 83817478f and that the main loop observes it green at the tip, as for the naming leg.
- **Related:** L10 (id 20) is the same omission, found by another lens and bound LOW.
- **Left-shift gate:** a close-time check that every leg reported `GATE FAIL` in the discovery bar log is named in some unit's §7.

### M13. 83 S1 moves spec headers without re-rendering the build README, so hygiene check 9 reds (id 31)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md` §2 S1, §4 Files touched, and AC6.
- **What is wrong:** S1 bumps the rev and moves the header date of CLOSED specs 5, 11 and 26. The `gen:build-units` block in `memory/builds/dSafePassage/README.md` renders those fields. The README is not in Files touched, and AC6 watches hygiene checks 12 and 23 but not check 9 (`gen_build_index.py --check`).
- **Consequence:** The `memory hygiene` leg this unit exists to turn green stays red, while AC6 still passes.
- **Fix (judged sound):** Add `memory/builds/dSafePassage/README.md` to Files touched, with `gen_build_index.py --write` run in the pass commit. Extend AC6 so the hygiene run also prints no `HYGIENE check 9` line.
- **Left-shift gate:** have a records unit's AC observe the whole `check-memory-hygiene.sh` exit, not a chosen subset of its checks.

### M14. 72's link walk raises OSError or ValueError on unnameable segments instead of refusing (id 36)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §2 S4, the §4 'One answer to one question' pseudocode, and §5 error states.
- **What is wrong:** The S4 walk calls `test_path_linked` on every prefix, and that function catches only FileNotFoundError. `a?b` and `a|b` raise `OSError [WinError 123]`, and an embedded NUL raises ValueError. `derive_contained_rel` lets these names through, and §5 names only the absent and dangling cases.
- **Consequence:** A tampered or corrupt image crashes `read_image_paths` with a traceback inside the reverse and forward walks. Step programs catch only Refusal, so a down or up dies with a traceback recorded as its failure, on exactly the hostile input this boundary exists for.
- **Fix (judged sound):** In S4, wrap each prefix test so that any OSError or ValueError from the lstat raises the same Refusal, naming rel and the segment (for example 'does not read as a path on this node'). Keep `test_path_linked`'s contract unchanged for its other callers. Extend AC3's escaping forms with `a?b/x.txt` and `'a' + chr(0) + 'b'`, each raising a Refusal and writing nothing.
- **Left-shift gate:** add a checklist entry saying that a containment boundary's AC table includes OS-illegal names and an embedded NUL.

### M15. 72's predicate admits an empty or root-only path as the target root (id 37)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §2 S1 and §6 AC1.
- **What is wrong:** `derive_contained_rel` returns `.` for `''`, `.` and `a/..`, so `check_contained` hands back the target root itself. AC1's tables hold none of these inputs.
- **Consequence:** A tampered image listing one of them passes containment. The down then calls `unlink` or `write_bytes` on the target directory and dies with an OSError instead of a refusal. govkit, now sharing the predicate, also passes `''`. No data is lost.
- **Grade:** the finder graded this low. The skeptic bound medium because the shared boundary admits a path that names no file, and a crash follows.
- **Fix (judged sound):** Have `derive_contained_rel` return None where the normalised form is `.`. Add `''`, `.` and `a/..` to AC1's escaping list, and to AC2's list only if govkit must refuse them too.
- **Left-shift gate:** the M14 checklist entry extends to empty and root-normalising inputs.

### M16. 76 S3's index read of the before-image has no parse-failure branch (id 39)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md` §2 S3 and §4 'S2 and S3: the kill windows'.
- **What is wrong:** S3 reads the killed down's paths from `git show :<image path>` through `read_image_paths`, which calls `json.loads(...)["paths"]` with no except. The spec names only the case where the index holds no image. It is silent on a blob that does not parse or lacks `paths`, such as an LFS pointer, a clean-filtered form or a truncated older image.
- **Consequence:** After a kill, every re-run of the rollback dies with a JSONDecodeError or KeyError traceback, and the row stays `down interrupted` with nothing naming the cause. Today `paths=[]` goes through, so this stuck re-run is new with S3.
- **Fix (judged sound):** State the parse-failure branch: an index image that does not parse, or lacks `paths`, is a Refusal that names the image and tells the operator to stage the restored paths by hand. It is never a traceback and never a silent `[]`. Route the index read through the same parse-and-contain function the working-tree read uses, with the source passed in. Add a kill-after-down-stage variant whose staged image is replaced by non-JSON, and observe that run red as a traceback before the fix.
- **Left-shift gate:** add a checklist entry saying that every read of adopter-controlled JSON names its malformed-input Refusal in §5.

## LOW

### L1. 81 and 83 each claim the last landing slot of order 16 (ids 5, 21)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md` §4 Rollout, against 81 §4 Rollout and 82 §4 Rollout.
- **What is wrong:** 83 says it is 'the last pass of the order', with 81 built first. 81 says its pass is 'the last of order 16 to be built'. 82 builds before both 'because -81 states it is the last'.
- **Consequence:** The dispatch order is ambiguous, and one spec's stated reason for its position becomes false. Today neither order breaks check 9, because 81 touches no watched path and 83 touches no Python name.
- **Fix (judged sound):** Make one statement in both specs. The task context places 81 last, so amend 83 §4 Rollout to 'after 72 to 78, 80 and 82, before 81' and keep its AC5 count reasoning. Alternatively, 83 builds after 81 and 81's Rollout says it is last among the code passes, with 83 following.
- **Left-shift gate:** a spec-audit check that order-N specs agree on a single total order, with at most one claimant per slot.

### L2. 74 S1's 'pass over `want`' crashes if taken literally, and AC3's grep matches the natural rewrite (ids 6, 22)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md` §2 S1 and §6 AC3.
- **What is wrong:** S1 says `for i in hits` 'becomes a pass over `want`', but the loop calls `want.discard(i)` (`upgrade_steps.py`:971-974). Iterating `want` directly raises 'Set changed size during iteration'. The natural copy, `[i for i in want if i in held]`, matches AC3's `in want if` grep.
- **Consequence:** A literal build crashes, which AC1 catches. A correct comprehension rewrite reds AC3 for the wrong reason. The grep checks a substring, not the removal of the raw-text test.
- **Fix (judged sound):** Spell the pass in S1, for example `for i in want & held:`. Make AC3's first pattern the raw-text test itself, `git grep -n -F "f'\"{i}\"' in text" -- tools/govkit/upgrade_steps.py` prints nothing, together with the existing `parsed only where` check.
- **Left-shift gate:** add a checklist entry saying that a removal AC greps the removed expression, never a substring that correct replacement code may contain.

### L3. 77 AC9 is green at HEAD and does not observe the ask's close (id 7)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md` §6 AC9 (S5).
- **What is wrong:** `BACKLOG.md`:7 and :16 already hold the TOOL-dSafePassage-79 ask row and its `DEFERRED · … until TOOL-dSafePassage-77` line.
- **Consequence:** S5 reads as observed while the build does nothing for it. The `closes TOOL-dSafePassage-79` flip goes unchecked.
- **Fix (judged sound):** Drop AC9, or have it observe the close: after 77 closes, the BACKLOG row reads closed, or the ask index lists 79 as closed by TOOL-dSafePassage-77.
- **Left-shift gate:** the M5 base-red check covers this class.

### L4. 82 misstates `--list` as clone-free and assigns two timed-out legs to 83 (id 8)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md` §6 AC4 and the first two non-goals of §3.
- **What is wrong:** AC4 says the listing mode 'builds no clone', but `upgrade_walk.py`:911 calls `build_release_tree`, which clones unconditionally at :173. 77:218 itself says the clone takes about a minute. §3 gives `routed commits name a specced unit` and `spec tokens` to 83, but 83 §1 and §3 and 80 S6 and S7 place them in 80.
- **Consequence:** A builder budgets AC4 as instant when it takes about a minute and touches git, and looks in 83 for ceiling work that lives in 80.
- **Fix (judged sound):** In AC4, say the listing mode builds the pinned clone but applies no target and runs no case. In §3, say the two timed-out legs are TOOL-dSafePassage-80's.
- **Left-shift gate:** none fits; add a checklist entry saying that a leg-ownership sentence cites the owning unit's S-item.

### L5. 72, 73, 76, 77 and 82 omit `symbols.json` from Files touched (id 9)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §4 Files touched, and the same in 73, 76, 77 and 82.
- **What is wrong:** Each mints top-level Python definitions, and none lists `memory/map/generated/symbols.json`. Only 81 claims it.
- **Consequence:** Each pass is refused at commit until it regenerates a file its scope does not name, and two units claim one artifact without saying so.
- **Fix (judged sound):** Add `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write` in the same commit, to the Files touched of 72, 73, 76, 77 and 82, as 81 does.
- **Related:** this is the Files-touched half of M11 (id 29), which carries the gate-line half and the MEDIUM grade. One edit cures both.
- **Left-shift gate:** as M11.

### L6. 77's missing-key Stops are unobserved, and its gate line omits install-prefix (id 10)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md` §2 S1 and S2 (the missing-key Stops) and §7 Gates.
- **What is wrong:** S1 and S2 make a missing `order` or `needle` a Stop at row read, but no AC and no S7 grader row feeds such a row. S3's `own` set and S7's grader inputs spell `tools/govkit/...` literals inside `upgrade_walk.py`, which `tools/check-install-prefix.sh` refuses, yet §7 omits that leg.
- **Consequence:** A build that silently defaults a missing key passes every criterion. The unit's gate line misses a leg its own design turns red.
- **Fix (judged sound):** Add a grader row or an AC that feeds a fixture row without `order` or `needle` and expects exit 2 naming the row. Add `install-prefix (shipped surface)` to §7, or spell the own set from `upgrade_walk.py`'s own location (HERE), as the leg's remedy names.
- **Left-shift gate:** add a checklist entry saying that every Stop named in §5 has an AC or grader row that triggers it.

### L7. 72 S1 credits `ntpath.isabs` with catching the rooted `\x` form (id 13)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §2 S1.
- **What is wrong:** On Python 3.13 and later, `ntpath.isabs('\\Windows\\x')` is False. The rooted form is refused only because the folded form passes `posixpath.isabs`.
- **Consequence:** Behaviour is unaffected. A later editor who drops the backslash fold, believing the ntpath arm guards the rooted form, reopens it.
- **Fix (judged sound):** Reword S1: `ntpath.isabs` covers the UNC and drive-absolute forms, and the rooted `\x` form is caught by `posixpath.isabs` on the folded form.
- **Left-shift gate:** none fits; the M14 AC table (with the rooted form in it) pins the behaviour.

### L8. 76 AC4's `retired-step` plant exits 0, against the family's exit contract (id 15)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md` §6 AC4.
- **What is wrong:** The plant's final run is a held refusal, but AC4 expects exit 0. `upgrade_steps.py`:101-103 and :4685-4686 document exit 1 for a refusing plant, and :4902 sets `rc = 1`.
- **Consequence:** A builder who follows the convention reds AC4, and one who follows AC4 breaks the documented contract.
- **Fix (judged sound):** Have AC4 expect exit 1 for `retired-step`, as for the other refusing plants. Or name the docstring edit (`upgrade_steps.py`:101-103, :4684-4686) the plant needs.
- **Left-shift gate:** none fits; add a checklist entry saying that a new plant's expected exit is checked against the family docstring.

### L9. 78 AC1 is green at base and does not run the block S1 edits (id 17)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-78.md` §6 AC1 and §4 'The probes' (walk probe).
- **What is wrong:** The walk probe runs its own `git init` and loads no `selftest.py`, and §4 records it printing True for all three cases at 83817478f. Its red-when describes an edit to the probe, not to the product.
- **Consequence:** AC1 is dead weight. S1 is still observed through AC2's grep and the staged-red New arm.
- **Grade:** the finder graded this medium. The skeptic bound low because S1 remains observed elsewhere.
- **Fix (judged sound):** Point AC1 at the edited block, for example by running `check_step_walk`'s three-case block alone through an import of `selftest.py`, or by extracting it with `ast`, so the observation flips with S1. Or drop AC1 and let the New arm's staged-red selftest observation carry S1.
- **Left-shift gate:** as M5.

### L10. 81 §7 omits `lexicon wiring` (id 20)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-81.md` §7 Gates.
- **What is wrong:** The leg failed at base on `verb offenders 1281 over pin 1212`, S6's pin move turns it green, and 82 §3 assigns it to 81. 81 never names it.
- **Consequence:** The unit can close without anyone observing `lexicon wiring` green.
- **Fix (judged sound):** Add `lexicon wiring` to §7's leg line and to the observation in AC7 or AC8.
- **Related:** M12 (id 30) is the same omission, bound MEDIUM. One edit cures both.
- **Left-shift gate:** as M12.

### L11. 82's floor step program imports govkit instead of using the step seam (id 24)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md` §8 F1 (b) resolution, the §4 'The install-prefix shapes' row 'A step row's program', and S3.
- **What is wrong:** The program calls `gk.resolve_kit_dir` and `gk.resolve_bash`, which means importing `govkit.py`. The existing seam is different. `fanout_cap.py`'s `load_steps` loads `upgrade_steps.py` by path, because the runner's `-I` drops the step's directory from `sys.path`, and `upgrade_steps.py` already defines both functions (:293, :347), which govkit only re-binds. `receipt_schema_4.py` documents the rule 'imports nothing from govkit'.
- **Consequence:** A builder writes a third import shape for step programs. It is heavier, it contradicts the isolation contract, and it fails under `-I` without a `sys.path` insert. Once that insert exists, the behaviour works.
- **Grade:** the finder graded this medium. The skeptic bound low because the defect is a divergent import shape, not a wrong result.
- **Fix (judged sound):** Rewrite F1 (b), the §4 row and S3. The program loads the step module by path, as `fanout_cap.py`'s `load_steps` does, then calls `STEPS.resolve_kit_dir("lib", "python-floor.sh", GOV)` and `STEPS.resolve_bash(script)`. Alternatively, it carries the inline `resolve_kit_dir` block under the resolve-python parity table, as `fanout_cap.py` does. Cite `fanout_cap.py` in §10 as the seam extended. Add to AC6 a run of the program under `run_step_isolated` (as 75's AC2 does) that expects verdict ok, so the isolated `-I` launch is observed.
- **Left-shift gate:** a lint over `tools/govkit/steps/*.py` that refuses `import govkit`.

### L12. 78's non-goal files as an ask the help sentence 76 already replaces (id 25)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-78.md` §3, last non-goal.
- **What is wrong:** 78 calls the `help/upgrade-steps.md`:184 sentence 'recommended as an ask of its own'. 76 rev-2 already builds it (S9, the §4 pages row, AC9).
- **Consequence:** There is a possible duplicate ask, or an open ask left misleading after 76 lands.
- **Fix (judged sound):** Rewrite the non-goal as "The page's 'Until the deployer runs steps itself' sentence (help/upgrade-steps.md:184) is TOOL-dSafePassage-76 S9's, which replaces it." Drop the 'recommended as an ask' clause.
- **Left-shift gate:** none fits; add a checklist entry saying that a spec revised after a sibling's hand-off re-reads its own non-goals.

### L13. 74's `derive_introduced` change also reaches `shims.py`, unnamed and unmeasured (id 27)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md` §2 S2 and §4 'What the parse costs'.
- **What is wrong:** S2 names two inheriting readers. A third, `tools/govkit/shims.py`:330 (`resolve_shim_landing`), also inherits the change.
- **Consequence:** A single-quoted shim id is now found where it read empty before. The shims kit changes with no AC and no cost reading, although the change agrees with shims.py's own docstring.
- **Fix (judged sound):** Add `shims.py`:330 to S2 as a third reader. Either add an AC2 row (a single-quoted `[[shim]]` id committed on a scratch gov reads its committing sha) or state in §3 why it needs none. Add the shim walk to §4's parse-count table, or say it is unmeasured.
- **Left-shift gate:** have the spec-writer list callers with `git grep -n '<fn>('` for every function whose behaviour changes.

### L14. 72 S2 leaves govkit's stale docstring and an unused `import ntpath` (id 33)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md` §2 S2.
- **What is wrong:** After the test moves into `derive_contained_rel`, `demand_contained_dest`'s docstring (`govkit.py`:1238-1243) still states the old rule, and `import ntpath` (:38) has no remaining code use.
- **Consequence:** Cosmetic: stale prose and an unused import.
- **Fix (judged sound):** Have S2 rewrite the docstring to say the decision is `upgrade_steps.derive_contained_rel`'s and that a colon anywhere is refused (§8 F1), and drop the unused `import ntpath` from `govkit.py`.
- **Left-shift gate:** an unused-import check over `tools/govkit/*.py` in the fast tier.

### L15. 76 leaves the optional-`<to>` usage spelling at `help/python-floor.md`:74 (id 34)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md` §2 S5 and S9, and §4 'The pages'.
- **What is wrong:** S5 changes the usage lines in `python_floor.py` and `python-floor.sh`. The page row rewrites only :75-76, so :74 still reads `python-floor.sh down 3.12 <target> [<to>]`.
- **Consequence:** Cosmetic: the page shows `<to>` as optional one line above the sentence that says it is required.
- **Fix (judged sound):** Widen the `help/python-floor.md` row of §4 'The pages' to cover `:74-76`, so the usage spelling matches `[<to>, required outside gov]`.
- **Related:** M4 (id 4) covers the default clause at :75-76.
- **Left-shift gate:** as M4.

### L16. 77 AC6's count of 1 is red on a correct build (id 40)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md` §2 S6 and §6 AC6.
- **What is wrong:** The phrase occurs three times at base (:23, :145, :847). S6 removes only :847, so a correct build leaves 2.
- **Consequence:** Only the criterion is affected: AC6 reds on a correct build, or the builder edits the docstring unasked.
- **Fix (judged sound):** Have AC6 count the Stop literals, for example `git grep -c -F -e 'is absent at release-0")' -- tools/govkit/upgrade_walk.py`, or add to S6 that the docstring at :23 is reworded.
- **Related:** M3 (id 3) is the same defect, bound MEDIUM. One edit cures both.
- **Left-shift gate:** as M3.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=40 confirmed=35 refuted=5 unverified=0 blocker=0 high=1 medium=16 low=18 agents=11 out-tokens=301877

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md:section 4 Files touched; section 7 Gates (and the same gap in TOOL-dSafePassage-82 section 4 Files touched and section 7) | medium | medium | confirmed | Re-probed. .githooks/pre-commit:238-239 runs manifest-check.sh --staged. In manifest-check.sh:1779-1788 C5s fails when `git diff --cached` touches a WATCH path and the staged last-audit blockstamp equals HEAD's. SESSION-KICKOFF.md:6 lists tools/gate-legs.json in the watch list. 80's Files touched (gate-legs.json, ceiling-evidence.txt, selftest-budgets.txt) and 82's (gate-legs.json and others) both omit memory/guides/SESSION-KICKOFF.md. Neither spec mentions last-audit, and neither §7 names kickoff-manifest ratchet. Only 83 touches the file. The four earlier gate-legs.json commits each staged SESSION-KICKOFF (grep -c printed 1 for each). As written, the pass commits of 80 and 82 are refused at pre-commit. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md:section 2 S4; section 3 non-goal on the node column; section 6 AC5 | medium | medium | confirmed | 80 S4 (:44) says the rows were written 'under GOV_NODE=a'. Its §3 (:66) says 'The readings were taken on node `a`'. The working-tree diff of ceiling-evidence.txt shows all three new rows tagged `a`, and one is 'timed by date over this worktree at 83817478f'. That tree carries tools/lib/python-floor.txt = 3.15. RUN.md:16 records that node a resolves only 3.14.6, and no later record says node a was provisioned. This host runs Python 3.15.2, and every spec header reads node d. The file's existing node-d rows are this build's own. derive-ceilings.py:565-569 refuses a defaulted --observed node because a wrong tag is 'a false claim about provenance'. AC5 then locks the `a` tag in. The ceiling check reads seconds only, so the effect is contained to the provenance record. | sound | - |
| 3 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 6 AC6 | medium | medium | confirmed | grep printed three hits in upgrade_walk.py: :23 (the docstring's exit-2 list), :145 (the Stop in write_plant_edits) and :847 (the Stop in check_inject). `git grep -c` printed 3. S6 removes only the check_inject path test, and no S-item touches the docstring. That docstring line stays accurate after S6, since write_plant_edits still raises the cause. A correct build therefore leaves the count at 2, and AC6's 'prints 1' cannot pass unless the builder deletes accurate documentation. | sound | - |
| 4 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 2 S9; section 4 'The pages' help/python-floor.md row; section 6 AC9 | medium | medium | confirmed | help/python-floor.md:75-76 reads 'left out, `<to>` defaults to the target's `HEAD`, so the down always grades bytes at a commit.' 76's §4 pages row for this page cites ':75-76' but, unlike the schema row at :204, has no 'in place of' text. AC9 greps only for the presence of 'is required in an adopter' and has no negative grep for the old default clause. A build that appends the sentence passes AC9 and leaves the page contradicting itself for adopters. | sound | - |
| 5 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md:section 4 Rollout | low | low | confirmed | 83 §4 Rollout (:282) says 'Order 16, the last pass of the order' with -81 built first. 81 §4 Rollout says 'This unit's pass is the last of order 16 to be built'. 82 says it builds 'before TOOL-dSafePassage-81 and -83'. So two units claim the last slot. 81's Files touched holds no watched path (.lexicon.conf, govkit py files, symbols.json, push-main.test.sh, python_floor.py), so either order leaves check 9 unaffected and the conflict is only in the prose. | sound | - |
| 6 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md:section 6 AC3 | low | low | confirmed | 74 AC3 requires that `git grep -e "in want if" -e "parsed only where"` print nothing. S1 says 'for i in hits becomes a pass over want'. At upgrade_steps.py:971-974 the loop calls want.discard(i), so iterating want directly needs a copy or a filter, and `[i for i in want if i in held]` is a natural spelling that trips AC3. Other spellings such as `held & want` or `list(want)` avoid it, so a red is likely but not certain. AC3 checks a substring, not the removal of the raw-text test. | sound | - |
| 7 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 6 AC9 (S5) | low | low | confirmed | BACKLOG.md:7 already holds the TOOL-dSafePassage-79 ask row with the AC9 phrase. :16 already reads 'DEFERRED · TOOL-dSafePassage-79 · until TOOL-dSafePassage-77'. AC9 (77:252-254) therefore passes on the unbuilt tree and cannot go red. The 77 header carries `closes TOOL-dSafePassage-79`, and nothing observes that close. | sound | - |
| 8 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md:section 6 AC4; section 3 first two non-goals | low | low | confirmed | 82:360 says 'The listing mode runs no case and builds no clone.' upgrade_walk.py:911 calls build_release_tree(..., with_target=not listing), and that function runs `run_git(root, "clone", ...)` at :173 with no condition. 77:218 itself says 'the clone `--list` makes, about a minute'. 82 §3 (:95-96) gives `routed commits name a specced unit` and `spec tokens` to 83, while 83:22-23 says their ceiling raises are TOOL-dSafePassage-80's, and 80 S6 and S7 raise them. | sound | - |
| 9 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 4 Files touched (and the same in 73, 76, 77 and 82) | low | low | confirmed | I read the Files touched (estimate) lists. 72 names upgrade_steps.py, govkit.py, selftest.py and help/upgrade-steps.md. 73 names upgrade_steps.py, selftest.py and help. 76 names 11 files and 77 names four. 82 names 20. None of them lists memory/map/generated/symbols.json. 81 does, at :401 with S4 at :36. Each of 72, 73, 76 and 77 mints top-level functions (derive_contained_rel, test_up_unrecorded, read_git_dir, derive_gov_root and others). .githooks/pre-commit:280 runs the codebase-map gate whenever a .py file is staged, and it fails on a STALE artifact. symbols.json maps `check_contained` and has 30 upgrade_walk.py hits, and earlier build commits f8f919882, dfcef45a7 and 7c51ef25f each carried it. The list is only an estimate, so the cost is a scope omission, not a behaviour change. | sound | - |
| 10 | coherence | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 2 S1 and S2 (the missing-key Stops); section 7 Gates | low | low | confirmed | 77 S1 (:28-29) and S2 (:37) make a missing `order` or `needle` a Stop, and §5 restates it. The S7 grader table lists only order-kind, arm-needle, tree-clean and case-counts. AC1 to AC10 never feed a row that lacks either key, so a silent default passes every criterion. The second half also holds. S3's own set and the S7 tree-clean input spell tools/govkit/... literals inside upgrade_walk.py. tools/check-install-prefix.sh:564 refuses a tracked file that spells a kit path, and 82's table lists upgrade_walk.py:199 (`tools/policy/adopt-policy.sh`) as a finding of that leg. 77's §7 gate line has no install-prefix leg. | sound | - |
| 11 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 6 AC2; section 4 'One answer to one question' | medium | medium | confirmed | govkit.py:1244-1246 refuses `len(dest) > 1 and dest[1] == ":"`, so `a:b` is already refused at base. I ran AC2's probe at HEAD and it printed `True a/b`, so the criterion is green before the unit is built. Its red-when line ('`a:b` is returned, as at base') is false, and so is §4 :113 ('the second misses an alternate data stream `a:b`'). In the same run `ab:c` and `x/a:b` were NOT refused at base, so the colon-anywhere tightening is unexercised. | sound | - |
| 12 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 4 'Observed at base' UNC row; section 6 AC3 and its note; section 7 New arm (observed RED at base) | medium | medium | confirmed | The base check_contained (upgrade_steps.py:1040-1045) tests only PurePosixPath and `:`, then returns `Path(target) / rel`. My probe joined C:\Users\x\c1\target with `\\localhost\c$\unc.txt` and got `\\localhost\c$\unc.txt`, not the `C:\localhost\...` the §4 row states. The rooted form gave C:\rooted.txt. write_from_before_image (:1125-1144) plans the entry, because now is None and after is None, and then calls `cur.write_bytes(was)`. AC3's probe catches only us.Refusal. A base run, which the [dSP-72] arm's 'observed RED at base' requires, therefore either raises PermissionError or, elevated, writes to C:\ and to the admin share outside the scratch directory, where the stray scan never looks. `icacls C:\` shows Authenticated Users with only (AD) on the root. AC3's note that these forms 'resolve onto the node's own drive' misstates the UNC case. | sound | - |
| 13 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 2 S1 | low | low | confirmed | On Python 3.15.2 I ran `[ntpath.isabs(x) for x in bad]` and got `[False, False, True, False, True, False, False, False, False, False]`, so `\Windows\x` reads False. S1 (:33-34) lists 'a rooted `\x`' under ntpath.isabs, but that form is caught only by posixpath.isabs on the folded form. Behaviour is unaffected and only the wording misleads. | sound | - |
| 14 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 6 AC7 | medium | medium | confirmed | `git grep -n "run_step_walk(" -- tools/` prints govkit.py:9454 and :11726 ending at `_src_pending,` and `_sw_pending,`. Lines 9455 and 11727 hold `to_commit)` alone, which the grep never prints. So AC7's second clause cannot see the sixth argument at either govkit caller. The signature clause and the govkit suites would still catch a leftover call later, which contains the effect. The AST option in the fix is unsound as a replacement for the grep. The fourth caller, upgrade_steps.py:3407 (`us.run_step_walk(..., to)`), sits inside the FIXTURE_WALK_CHILD string literal (:3383), so ast.Call never sees it, whereas today's grep does. Grepping with -A1 for `to_commit)` alone would also miss any other wrapped argument name. | unsound | - |
| 15 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 6 AC4 | low | low | confirmed | 76 AC4 (:303-308) has the retired-step plant exit 0, although its final run is `update --rollback --to A --write` exiting 2 with a held refusal. upgrade_steps.py:101-103 says 'a refusing `rollback-update` plant 1', :4685-4686 says '1 for a refusing plant whose refusal held', and :4902 sets `rc = 1` in the refusing-plant branch. The AC and the module's exit contract disagree, and the spec names no docstring edit. | sound | - |
| 16 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 2 S3; section 5 risks | medium | medium | confirmed | 77 S3 (:39-44) returns every path that `git status --porcelain --untracked-files=no` lists outside the three own paths, and main raises Stop (exit 2) on any of them. Nothing limits it to engine files, yet §5 says only 'on a local run over uncommitted engine edits'. `git status --porcelain --untracked-files=no` here prints ` M tools/run-gates/ceiling-evidence.txt`, and 83 :76-79 records 65 uncommitted ledger edits at writing. run-gates.sh:5694-5703 only withholds the full-green stamp on a dirty tree; it still runs the legs. So upgrade-walk would red with 'nothing measured' over edits the walk never reads. | sound | - |
| 17 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-78.md:section 6 AC1; section 4 'The probes' (walk probe) | medium | low | confirmed | Spec 78 lines 167-168 say the probes load no tools/govkit/selftest.py. The walk probe calls `git init` itself (line 187) and drives upgrade_steps.run_step_walk directly. §4 'Measured at writing time' (line 264) records it printing True for all three cases at 83817478f, before any build, so AC1 cannot fail on S1. Its 'Red when' describes an edit to the probe, not to the product. Graded low because S1 is still observed: AC2 greps the exact edited literals, including 'case == "escaping" or "fx/x" in refused', and the New arm at line 370 is staged red against the no-git-init block. AC1 is dead weight, not a lost observation. | sound | - |
| 18 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md:section 3 'Finding for the owner' (Who pays it); section 2 S5 | medium | medium | confirmed | remote-ci.yml builds the held matrix from `run-selftests.sh --list` (line ~206), and run-selftests.sh reads its population from selftest-budgets.txt (BUDGETS at :47, read_population at :937). So S5's row enrolls upgrade-walk in the daily cron job ('23 4 * * *'). ceiling-margin.txt's first row is 120 TAB 1.0, so bound = 10770 + max(120, 10770) = 21540. The cap is 360*60 - 600 = 21000, so the entry is platform_bounded. Spec 80's 'Who pays it' (lines 86-90) says only that remote CI sets no GATE_SELFTESTS and that a default bar is not slowed. It never mentions this nightly cost. | sound | - |
| 19 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md:section 8 F1 (resolved b); section 4 'The install-prefix shapes' step-row row; section 6 AC6 | medium | - | refuted | The premise is false on re-probe. resolve_step_argv (tools/govkit/upgrade_steps.py:1389-1390) rewrites a leading `python` to `[sys.executable, "-I", ...]`, so a `python` step argv never depends on PATH or the Store stub. The schema row already uses this shape (steps.toml:16-18). A fake named `python` first on PATH therefore cannot answer the floor step. The wrapper then runs python-floor.sh preflight through bash, whose resolver honors GOV_PYTHON. 75's arm and its AC2 still separate kept from stripped GOV_PYTHON. | unsound | - |
| 20 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-81.md:section 7 Gates | low | low | confirmed | Spec 81's §7 leg line names `lexicon naming predicates` but not `lexicon wiring`. grep finds no 'lexicon wiring' anywhere in spec 81. The bar log at lines 1005-1009 shows `GATE FAIL  lexicon wiring` with `lexicon: verb offenders 1281 over pin 1212`, and spec 82 line 94 assigns that leg to -81. | sound | - |
| 21 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md:section 4 Rollout | low | low | confirmed | Spec 81's Rollout reads 'This unit's pass is the last of order 16 to be built'. Spec 83's Rollout reads 'Order 16, the last pass of the order. TOOL-dSafePassage-72 to -78, -80, -81 and -82 build first'. Spec 82's Rollout says it builds before -81 'because -81 states it is the last of order 16 to build', then that -83 follows 82. The three statements contradict each other about the final pass. | sound | - |
| 22 | grounding | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md:section 2 S1; section 6 AC3 | low | low | confirmed | upgrade_steps.py:963 is `hits = [i for i in want if f'"{i}"' in text]`. Lines 971-974 run `want.discard(i)` inside the loop. Spec 74 S1 says '`for i in hits` becomes a pass over `want`', and iterating `want` while discarding from it raises RuntimeError. AC3 greps 'in want if', which the natural `[i for i in want if i in held]` rewrite would match. The effect is contained, because AC1 would catch the crash. | sound | - |
| 23 | reuse | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 4 'One answer to one question', S1/S2, AC7 | medium | - | refuted | The evidence does not fully reproduce. Simulating check_path_inside's body with posixpath returns False (refused) for '..\x', '\Windows\x' and '\\srv\s', because the backslashes are replaced before isabs and the '../' test. Only drive or colon forms and 'a\..\..\x' pass. Those divergences fit the predicate's actual job, which is a bool filter that keeps a pathspec git would reject out of ls-files and diff (govkit.py:6630-6645, :6965-6974). On POSIX git takes 'C:\x' or 'a:b' as an in-tree filename, so passing them is right. The comment there says the receipt-row refusal is demand_contained_dest's, and 72 does unify that. So 72's 'one answer' covers the refusal question, not this filter. The proposed fix would also make legal POSIX git paths holding a colon or backslash read as absent from the index. That is the false-absent that F5's comment at :6639 guards against. | unsound | - |
| 24 | reuse | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-82.md:section 8 F1 (b) resolution, section 4 'The install-prefix shapes' row 'A step row's program', S3 | medium | low | confirmed | Spec 82's §4 row (line 177) and F1(b) (lines 436-438) have the program call gk.resolve_kit_dir and gk.resolve_bash, so it imports govkit. upgrade_steps.py already defines resolve_kit_dir (:293, inline gated copy) and resolve_bash (:347), and govkit.py:147 only re-binds them. The existing step seam, fanout_cap.py's load_steps (:42-55), loads upgrade_steps by path because the runner's -I drops the step's own directory from sys.path (resolve_step_argv :1390 confirms -I). receipt_schema_4.py also imports only upgrade_steps. Graded low: calling the re-bound function through govkit still hits the same _BASH cache, so behaviour works once a sys.path insert is added. The defect is a divergent, heavier import shape, not a wrong result. | sound | - |
| 25 | reuse | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-78.md:section 3, last non-goal | low | low | confirmed | 78 spec lines 77-79 still say the help/upgrade-steps.md:184 sentence 'is not one of this brief's items; recommended as an ask of its own'. 76 already builds it: line 96 (S9), line 204 (the §4 pages row replacing 'Until the deployer runs steps itself'), line 340 (AC9 greps it to nothing) and lines 393-395 (rev-2 cites the 78-1 spec-writer prompt as the hand-off). The non-goal is out of date. The only effect is a possible duplicate ask, so this is low. | sound | - |
| 26 | reuse | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 10 (S1 seam), section 2 S1 | low | - | refuted | This is a preference (case 6). S1 (76 lines 32-34) sets the shape: `git -C <target> rev-parse --absolute-git-dir`, 'run under `build_step_env` as `read_target_repositories` runs it'. `build_step_env` (upgrade_steps.py:1354) is a module-level callable. It builds a new dict from STEP_ENV_KEEP only, so no hook-exported GIT_DIR gets through, and it also forces an empty hooksPath and credential helper. The spec names the pattern and the env seam, and the builder can do both. The §10 wording 'reuses ... the call' is loose about the nested closure at :1443, but it names no wrong design. The proposed `build_tree_git_env` would only be a different, weaker env choice. | unsound | - |
| 27 | reuse | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md:section 2 S2, section 4 'What the parse costs' | low | low | confirmed | `git grep -n 'derive_introduced(' -- tools` printed shims.py:330 (`derive_introduced(root, ref, [rel], "shim", [shim_id])` inside resolve_shim_landing), plus upgrade_steps.py:861 and :907 and selftest.py:3090. 74 S2 (lines 31-33) says 'Both readers inherit it' and names only read_steps and read_retired. `grep -n shim` over spec 74 prints nothing. The shim landing derivation changes with no AC and no cost reading. The change agrees with shims.py's own docstring ('exactly that id, never a substring search'), so the effect is contained to unnamed and uncovered behaviour. Low. | sound | - |
| 28 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-80.md:section 2 S5; section 7 (Gates); section 4 "The budget row" | high | medium | confirmed | foreign-prefix.gov.test.sh:29-35 takes as its population every row `run-selftests.sh --list` prints. run-selftests.sh:703-716 resolves an empty-argv row from the manifest and prints it `ok`, and gate-legs.json gives upgrade-walk argv `python {prefix}/govkit/upgrade_walk.py`. run_row (:568-577) reds a probe-kind row that prints no marker: 'an undeclared whole run'. The kind is whole only for WHOLE_RUN entries (:315), and GOV_LAYOUT (:264-266) names only `govkit selftest`. `git grep FOREIGN_PREFIX` over upgrade_walk.py prints nothing; the only govkit site is selftest.py:5136. S5 adds the row with an empty argv (80 line 213, 'argv-empty' at :285), and §7 (line 403) does not name the foreign-prefix leg. So the leg reds, or hangs at three runs of about 7177 s. The failure is loud on the bar, not a silent wrong result, so medium rather than high. | sound | - |
| 29 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 4 Inventory / Files touched; section 7 (also TOOL-dSafePassage-73, -76, -77 and -82, same sections) | medium | medium | confirmed | symbols.json lists top-level functions of upgrade_steps.py, upgrade_walk.py and python_floor.py (check_contained, check_plant_rows, read_down_population and build_step_env all present). .githooks/pre-commit:280 runs the codebase-map gate whenever a .py file is staged. A grep for symbols.json, codebase-map coverage or gen_map counted 0 in specs 72, 73, 74, 75, 76, 77, 78, 80, 82 and 83, and 11 in 81 only. Specs that mint top-level functions (72, 73, 76, 77, 82) would have their commits refused unless they regenerate a file outside their declared write set. The failure is loud and the cure is mechanical, so medium. | sound | - |
| 30 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-81.md:section 7 (Gates) | medium | medium | confirmed | The bar log line 1005 prints `GATE FAIL  lexicon wiring  (exit 1)`, with 'THE DECLARATION DOES NOT GRADE ... lexicon.py exited 1'. A grep for 'lexicon wiring' over specs 80 to 83 matches only 82:94, which assigns the leg to 81. 81's §7 (line 508) names `lexicon naming predicates` but not `lexicon wiring`. A red leg this build caused belongs to no unit's gate list, and its other arms go unobserved until the close bar. | sound | - |
| 31 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-83.md:section 2 S1; section 4 Files touched; AC6 | medium | medium | confirmed | 83 S1 (lines 27-33) bumps the rev and moves the header date of specs 5, 11 and 26. The README's gen:build-units rows read `CLOSED \| rev-11 \| 2026-10-27` (5), `CLOSED \| rev-4 \| 2026-10-26` (11) and `CLOSED \| rev-11 \| 2026-10-27` (26). Files touched (lines 288-302) omits memory/builds/dSafePassage/README.md. AC6 checks hygiene checks 12 and 23 and MANIFEST check 9, never HYGIENE check 9, which check-memory-hygiene.sh:1483-1491 grades with `gen_build_index.py --check`. So the memory hygiene leg stays red while AC6 passes. | sound | - |
| 32 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-74.md:section 2 S2; section 4 "What the parse costs" | low | - | refuted | duplicate of id=27: the same missing third caller, shims.py:330 calling derive_introduced with table `shim`, which 74 S2 and §4's cost table leave out. I re-probed it with the same git grep. | sound | - |
| 33 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 2 S2 | low | low | confirmed | I grepped tools/govkit/govkit.py for `ntpath`. The only code use is line 1246, inside the test S2 replaces. Line 38 is the import, and lines 1242 and 6598 are docstring prose. The docstring at 1238-1243 still states the old rule ('A drive letter counts as absolute'). Spec 72 S2 (lines 37-42) names neither the docstring nor the import. The effect is cosmetic: stale prose and an unused import. | sound | - |
| 34 | blast-radius | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 2 S5 / S9; section 4 "The pages" | low | low | confirmed | `git grep -n "\[<to>\]" -- tools help` printed help/python-floor.md:74 plus python-floor.sh:6 and :45 and python_floor.py:5. Spec 76 S5 names only the last three. The §4 pages row (spec-76.md:205) rewrites only `:75-76`. Line 74 of the page still reads `python-floor.sh down 3.12 <target> [<to>]`, one line above the new sentence. The mismatch is cosmetic. | sound | - |
| 35 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 2 S3 (and section 6 AC5-AC8, section 4 Rollout) | high | high | confirmed | Spec 77 S3 (lines 42-48) makes check_tree_clean refuse with exit 2 on every tracked dirty path outside the leg's three files. `git diff --stat` shows tools/run-gates/ceiling-evidence.txt dirty right now. 80 S4 commits that file, and 80 §3 forbids recreating it by hand or by any --write run. Dispatch order puts 77 before 80: 77 builds after 76, and 82 builds after -72..-78 and -80. AC6 (expects a plant Stop), AC7 (expects exit 0) and AC8 run in the build worktree, so each would exit 2 on the dirty-tree check before measuring. The leg's message, 'commit or stash them', points the builder at 80's evidence. 77's own S8 and S5 edits to help/upgrade-steps.md and BACKLOG.md lie outside `own` as well. run-gates.sh runs the leg over the working tree, so any unrelated dirty file, a memory record for example, also turns the leg red. FIX: unsound as exemplified. The proposed narrowing to `git status -- tools/` still lists tools/run-gates/ceiling-evidence.txt, so it does not cure the named instance. Only the alternative (sequence 80 first) does. | unsound | - |
| 36 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 2 S4 / section 4 'One answer to one question' pseudocode / section 5 error states | medium | medium | confirmed | I re-probed from scratch dir verify-b. us.test_path_linked raised `OSError [WinError 123]` on 'a?b' and 'a\|b', and `ValueError lstat: embedded null character` on 'a\x00b'. upgrade_steps.py:1416-1424 catches only FileNotFoundError. derive_contained_rel (spec 72 §4 pseudocode) does not reject these names, so the S4 walk raises out of check_contained. fanout_cap.py:221-225 catches only Refusal. Spec 72 §5 names only the absent and dangling cases. The result is a traceback instead of a named refusal, and the effect is contained. | sound | - |
| 37 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-72.md:section 2 S1 / section 6 AC1 | low | medium | confirmed | posixpath.normpath('') and normpath('a/..') both print '.'. The 72 pseudocode returns that form, and check_contained returns target/'.' = the target root. The S4 walk passes it, because the root is a directory with no link and the loop then ends. In write_from_before_image (upgrade_steps.py:1128-1142), a '.' entry with before None reaches `cur.unlink` on the target directory, which dies with an OSError and no Refusal. AC1's escaping list (spec-72.md:226) holds no '', '.' or 'a/..'. The effect is a crash on tampered input with no data loss, so it is contained. | sound | - |
| 38 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 2 S1 / section 4 'S1: two refusals' / section 5 error states | medium | - | refuted | The premise is false on re-probe: the fail-open read_git_dir is not reachable to a write. Every step spawn goes through run_step_isolated. That calls check_target_local_config (upgrade_steps.py:1703, 'found = check_target_local_config(target)') before spawning anything. check_target_local_config reaches read_target_repositories, which runs the same `git -C <target> rev-parse --absolute-git-dir` under build_step_env (:1495). Its git helper (:1444-1450) raises Refusal on any non-zero exit, and the caller turns that into a refusal: 'nothing was spawned'. So on a dead git, a dubious-ownership refusal under GIT_CONFIG_GLOBAL=devnull, or a corrupt repo, the step child that would write the before-image never runs. The parent-side read_image_paths only reads and stages. No hook plant passes through the lexical-only fallback. | sound | - |
| 39 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-76.md:section 2 S3 / section 4 'S2 and S3: the kill windows' | medium | medium | confirmed | read_image_paths (upgrade_steps.py:1909-1919) calls json.loads(...)["paths"] with no except. run_reverse_walk calls it at :2128 with no catch around it. Spec 76 S3 (lines 45-50) and §4 (lines 159-161) name only the 'index holds none' branch. An index blob that does not parse, or lacks `paths`, would raise a JSONDecodeError or KeyError traceback on each re-run of the rollback. Today, paths=[] goes through after a killed down, so this stuck re-run is new with S3. The image is committed adopter content. The effect is contained: the operator can unstage it by hand. | sound | - |
| 40 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-77.md:section 2 S6 / section 6 AC6 | low | low | confirmed | `git grep -n -F "is absent at release-0" -- tools/govkit/upgrade_walk.py` printed three lines: :23 (module docstring), :145 and :847. S6 removes only :847, and no scope item touches :23. AC6's `git grep -c` would print 2 on a correct build. Only the criterion is affected, not shipped behaviour. The proposed `is absent at release-0")` pattern matches only the two Stop literals, which leaves 1 after S6. | sound | - |
