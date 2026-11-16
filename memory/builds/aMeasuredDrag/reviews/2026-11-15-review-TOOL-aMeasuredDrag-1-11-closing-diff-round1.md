**Serves:** diff-review TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11

# aMeasuredDrag — Tier-2 review of the cumulative diff landing on main, round 1

Provenance: finders gov-diff-reviewer (5 lenses), skeptic batches gov-skeptic, synthesis gov-synthesizer. ROUND 1.

Range: a0a1892de069cd2299ba162d885ac283cfa81010...3d03a15950b02963aba40f2a9d1f6fa55133d361

## Verdict: CLEAN WITH FIXES

No blocker and no high. Six items stand: five medium and one low. They hold seven raw confirmed findings: six medium and one low. Every item is a gap in verification or a narrow spurious-red path. None gives a wrong verdict on a reachable path, and each needs a fix and a gate.

Review shape: intensity full, raw 7, confirmed 7, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00. Tally by item: 6 items (blocker 0, high 0, medium 5, low 1). Tally by raw confirmed finding: 7 (blocker 0, high 0, medium 6, low 1). Findings 2 and 6 describe one defect and make one item.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Intent: neither `specs` nor `context` was supplied. The lenses had only the range's commit messages as intent.

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 4/4 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 5 judged sound, 1 judged UNSOUND (id 6), 1 judged INSTANCE-ONLY (id 1), 0 with no proposal, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (id 5, low to medium).
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Checklist: 128 items from `--for-diff a0a1892de069cd2299ba162d885ac283cfa81010..HEAD`, split security 26, correctness 26, seams 26, verification 25, intent 25. By design: 3 invariants from the checklist's by-design block.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin is flagged.

The zero counts for security and correctness come from lenses that all returned. They rest on generic briefs and commit-message intent only, and do not prove absence beyond what those lenses read.

Line references are blob-pinned (`<path>@<blob8>:<line>`) at the reviewed sha 3d03a159.

## Items

### 1. [MEDIUM] Arm 1m cannot tell a memo hit from a re-probe — ids 2, 6

- **Where:** tools/run-gates/run-gates.test.sh@e33c90b2:569 (arm 1m, lines 541-571), against the export at tools/run-gates/run-gates.sh@33b623a2:3571-3572.
- **What is wrong:** TOOL-aMeasuredDrag-11 exists so that no leg re-probes the launcher. Arm 1m is its only lasting gate. The arm checks that the leg's memo has no sentinel, and that the launcher the leg resolved (`_mlaunch`) equals memo line 2 (`_mml`) and runs. On a memo hit the resolver prints PYBIN. On a miss the probe loop runs over the same GOV_PYTHON and PATH and prints that same PYBIN. Both assertions compare two values that are both derived from PYBIN, so the arm passes either way. A probe at 3d03a159 confirmed it: a memo with an empty version line caused 1 `-I -c` probe and printed the same launcher, and a well-formed memo caused 0. resolve-python.test.sh e2 builds its memo by hand, so it never checks what the bar actually exports.
- **Consequence:** the export could swap the GOV_PYTHON and PATH fields, drop the version, or drift from the block's `_rp_re` layout. A leg could also inherit a different PATH. Either way every bash leg would quietly re-probe, at about 176 ms per resolution by the spec's figure, and every gate would stay green. The cost is time, never a wrong verdict.
- **Grades:** 2 medium, 6 medium (binding).
- **Fix:** the skeptic judged id 2's fix SOUND and REJECTED id 6's. The fix below is the skeptic's corrected fix for id 6, plus id 2's sound alternatives.
  - Set GOV_PYTHON, for both the scratch bar and the leg, to a counting wrapper script. The wrapper appends a line to a counter file and then execs the real `$PYBIN`.
  - leg.sh truncates the counter after the runner's own probe and before it calls resolve_python, then records what the counter holds.
  - Assert the counter stayed empty, alongside the existing launcher-equality check.
  - Sound alternatives from id 2: require zero ` -I -c ` lines in a `bash -x` trace of resolve_python. Or assert that memo line 1 matches `^[0-9]+\.[0-9]+$` at or above the floor, and that lines 3 and 4 equal the leg's own GOV_PYTHON and PATH.
  - Stage it red by swapping the GOV_PYTHON and PATH fields in the export line, or by replacing PY_MM with "" at tools/run-gates/run-gates.sh@33b623a2:3571. The counter must fill and 1m must go red.
- **Left-shift gate:** class `assertion-between-two-derived-values`. Every new memo or cache arm in the run-gates suite must assert that the work was skipped (a spawn counter or a trace count), not only that the output matches. Add this to the checklist entry for the class.

### 2. [MEDIUM] A relative GOV_PYTHON enters the launcher memo and goes dead in a leg that changes directory — id 1

- **Where:** tools/lib/resolve-python.sh@522ccfe2:41-45, and every inline resolver copy of it. The export is at tools/run-gates/run-gates.sh@33b623a2:3572.
- **What is wrong:** the GATE_RESOLVED_PY shortcut assumes the resolved answer depends only on GOV_PYTHON, PATH and the floor. It also depends on the working directory. Take a relative GOV_PYTHON such as `.venv/Scripts/python`. The bar resolves it at the repo root, and the loop prints the override as given (line 66). The bar then puts that relative string in the memo as PYBIN. A leg that changes into a fixture or temp directory gets the relative path back from the memo, which skips both the run check and `[ -x ]`.
- **Consequence:** before this change, such a leg's resolver fell through to python3, python or py and found a working launcher. Now `"$PY" ...` exits 127, and the leg goes red for a reason unrelated to its subject. This is a spurious red, not a false green. The path is narrow, because help/python-floor.md shows an absolute path.
- **Grades:** 1 medium (binding).
- **Fix:** the skeptic judged the finder's fix INSTANCE-ONLY. The class-level fix is below.
  - Absolutize at export time, or export no memo. In run-gates.sh, before the export, compute PYBIN_ABS:
    - PYBIN itself when it starts with `/` or a drive letter;
    - otherwise, when it contains a slash, `$(cd "$(dirname "$PYBIN")" && pwd)/$(basename "$PYBIN")`;
    - otherwise `$(type -P "$PYBIN")`.
  - Put PYBIN_ABS in the memo only when it is non-empty and absolute. Otherwise unset GATE_RESOLVED_PY.
  - Add resolve-python.test.sh arms for a relative launcher with resolve_python called from another directory, and for a bare-name launcher with `.` on PATH.
  - The finder's proposal cures the cited instance alone. That proposal allowed a memo for an absolute path or a bare name; its literal `*/*` case would still export relative paths. A bare name is also cwd-dependent when PATH holds `.` or an empty component, and such a PATH passes the byte-for-byte PATH check.
- **Left-shift gate:** class `inherited-env-retargets-a-check`. Extend the python-resolver leg (`python resolver (behaviour + inline parity + idiom ban)`) to fail when any memo producer can export a non-absolute launcher.

### 3. [MEDIUM] The run-gates assertion floor was not raised for arm 1m — id 3

- **Where:** tools/run-gates/run-gates.test.sh@e33c90b2:289 (`FLOOR_ASSERTIONS=450`).
- **What is wrong:** TOOL-aMeasuredDrag-11 adds two assertions in arm 1m (`n=$((n+1))` twice), and neither is gated on HAVE_TIMEOUT. FLOOR_ASSERTIONS stays at 450, and the floor ledger gains no dated line. Its last entry is still TOOL-aNimbleMend-15's 440 -> 450. The same diff did raise run-gates.gov.test.sh from 17 to 18 for G8, so the convention was known.
- **Consequence:** the floor is a lower bound counted on hosts that skip the timeout arms, and 1m runs on every host. If arm 1m were deleted or skipped early, the count would still clear 450. The canary would stay green with the only integration check of the memo export gone. Today the arm runs, so the effect is contained.
- **Grades:** 3 medium (binding).
- **Fix** (judged SOUND by the skeptic): raise FLOOR_ASSERTIONS to 452. Add the ledger line "450 -> 452, TOOL-aMeasuredDrag-11: arm 1m's two, neither gated. Counted off the arm."
- **Left-shift gate:** class `floor-left-below-the-arms-it-guards`. Extend `testsuite counts (every bar self-test prints one)` to go red when a diff adds ungated `n=$((n+1))` lines to a suite without moving that suite's floor constant.

### 4. [MEDIUM] Nothing tests check_tree's new `tags` switch on either side — id 4

- **Where:** tools/playbook/instructions_edit.py@7638c707:539. The switch is at :502 and the `if tags:` branch at :528-532. The write path at :300 relies on the default `tags=True`.
- **What is wrong:** TOOL-aMeasuredDrag-4 adds `check_tree(root, candidate=None, tags=True)`. The write path keeps the tag checks through the default, and the check verb drops them with `tags=False`. The only tag arm (lines 1058-1063) calls `run_tag_check` directly. Nothing asserts ` · tags · ` or `cites retired` through check_tree or through the write path. G8 checks only the leg manifest. AC1 was one scratch probe, which is not a gate.
- **Consequence:** the default could flip to False, or line 300 could pass `tags=False`. Writes would then be admitted without tag checks at the write boundary, and the instruction-edits selftest would stay green. A retired or unregistered tag would reach the tree and be caught only later, by the bar's tags leg.
- **Grades:** 4 medium (binding).
- **Fix** (judged SOUND by the skeptic): add a fixture arm that plants a retired-tag citation and runs it through `check_tree(root, {rel: candidate})`. Assert that it comes back red with ` · tags · ` or `cites retired`, and that `run_check` over the same tree does not report it. Stage it red by changing the default to `tags=False`.
- **Left-shift gate:** class `rule-stated-with-no-check-that-fails`. `instruction edits selftest` should carry one arm per value of every new mode switch on a write-boundary function.

### 5. [MEDIUM] Nothing tests pre-commit's rewritten template-size trigger — id 5

- **Where:** .githooks/pre-commit@f1da4472:203 (the `st_template` case pattern in the st_list loop), and the guard at :307.
- **What is wrong:** TOOL-aMeasuredDrag-10 replaced `git diff --cached --name-only -- coding-governance-agents.template.md` with a case pattern over the staged list once. pre-commit.test.sh never mentions `coding-governance-agents.template.md`, `check-template-size` or `st_template`; its only "template" hits are `git init --template=`. No other test drives the hook with the template staged. The unit's evidence was one scratchpad probe (u10probe.sh). The memory, wiring, codebase-map and policy triggers do have arms.
- **Consequence:** a typo in the case arm or its guard would silently stop the template-size leg at commit time, and the branch-guard self-test would stay green. The bar's template-size leg still catches an oversize template at push time, so the effect is contained.
- **Grades:** 5 medium. The finder graded it low and the skeptic medium. Medium binds because the untested trigger is new code that can stop a commit-time check without anything going red.
- **Fix** (judged SOUND by the skeptic): add a pre-commit.test.sh arm that stages coding-governance-agents.template.md with a stub check-template-size.sh that prints a marker, and assert that the marker appears. Add a control that stages some other file and assert that the marker is absent. Stage it red by misspelling the case pattern.
- **Left-shift gate:** class `rule-stated-with-no-check-that-fails`. `branch-guard self-test` should carry one trigger arm per leg the hook dispatches. Have the suite list the hook's case arms and go red on any arm no test stages.

### 6. [LOW] Spec §7 claims full AC5 coverage, but the export-after-digest order has no lasting gate — id 7

- **Where:** memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-11.md@ac1fa7c9:252. The ordering it should guard is at tools/run-gates/run-gates.sh@33b623a2:3566-3572.
- **What is wrong:** §7 says the new run-gates.test.sh arm covers AC5. AC5 has two red cases: the unset placed after the resolution, and the export placed before the REUSE_DIGEST assignment. Arm 1m goes red only for the first. Its header says it does not check the export-after-digest order (tools/run-gates/run-gates.test.sh@e33c90b2:541-547). No suite greps `export GATE_RESOLVED_PY`. Today the order is correct: lines 352, 353, 3566 and 3572.
- **Consequence:** the digest subshell hashes every `GATE_*` name not on its skip list, and GATE_RESOLVED_PY is not on that list. If the export moved above the digest, a direct bar's key would carry the name and a push bar's would not, because pre-push drops it. That would bring back the direct-versus-push reuse-key split that TOOL-aSparedSpawn-33 closed. No gate would go red. The cost is lost verdict reuse, not a wrong verdict.
- **Grades:** 7 low (binding).
- **Fix** (judged SOUND by the skeptic): correct the §7 line so the arm claims only the unset half of AC5. Gate the ordering half too. Add an arm to run-gates.test.sh, or to the G-series in run-gates.gov.test.sh, that runs AC5's grep over the runner. It goes red unless the unset, PYBIN, digest and export lines appear in that order. Watch it go red by moving the export line above the digest.
- **Left-shift gate:** class `observed-by-claim-no-arm-discharges`. `spec tokens (the pass's own spec)` or a sibling check should require every "covered by arm X" claim in a spec's §7 to name an arm whose staged red matches each red case of the criterion.

review-shape kind=diff-review round=1 intensity=full at=synth raw=7 confirmed=7 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=6 low=1 agents=10 out-tokens=102876
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | seams | tools/lib/resolve-python.sh@522ccfe2:41 | medium | medium | confirmed | The fix's prose rule (memo only for an absolute path or a bare name) cures the cited relative-with-slash instance. The literal case it sketches lists */*, which matches relative paths with a slash, so taken literally it would still export them. More important, a bare name is cwd-dependent too when PATH holds a relative entry ('.' or an empty component), and that PATH passes the byte-for-byte PATH check unchanged. So 'bare name is safe' leaves another instance of the class. The class-level cure is to put only an absolute launcher in the memo. | instance | inherited-env-retargets-a-check | class:inherited-env-retargets-a-check |
| 2 | verification | tools/run-gates/run-gates.test.sh@e33c90b2:569 | medium | medium | confirmed | I read tools/run-gates/run-gates.test.sh@e33c90b2:541-571. Arm 1m checks only two things: the leg's memo does not contain the sentinel, UNSET or 'NO LEG RAN', and the launcher the leg resolved equals memo line 2 and runs. When the memo misses (fields swapped, an empty PY_MM, or PATH changed after export), the regex or equality check at tools/lib/resolve-python.sh@522ccfe2:42-44 fails and the loop runs. With the same GOV_PYTHON and PATH it prints the same PYBIN the bar printed at tools/run-gates/run-gates.sh@33b623a2:353. Both assertions still pass. The arm's own header lists what it does not check and stops at the digest ordering; nothing in the arm tests that the leg skipped its probe, which is the unit's whole purpose. So a regression that silently removes the optimisation stays green. The consequence is lost performance with no wrong result, so medium. | sound | - | class:assertion-between-two-derived-values |
| 3 | verification | tools/run-gates/run-gates.test.sh@e33c90b2:289 | medium | medium | confirmed | In tools/run-gates/run-gates.test.sh, arm 1m (lines 541-571) runs `n=$((n+1))` twice, both outside any HAVE_TIMEOUT gate. FLOOR_ASSERTIONS is still 450 at line 289. The diff's hunks in this file add only arm 1m and the resolver block, and no floor line, so the last ledger entry is still TOOL-aNimbleMend-15's 440 -> 450. The floor at line 4312 is a lower bound, so deleting or skipping arm 1m would still clear 450 and the canary would stay green. That is a real gap, but it is contained: today the arm runs and still catches a regression. | sound | floor-left-below-the-arms-it-guards | class:floor-left-below-the-arms-it-guards |
| 4 | verification | tools/playbook/instructions_edit.py@7638c707:539 | medium | medium | confirmed | The diff adds `check_tree(root, candidate=None, tags=True)` and the `if tags:` branch (instructions_edit.py lines 502 and 528-532). The base had no such parameter: its line 535 called `check_tree(root)`. The write path at line 300 relies on the default, and run_check at line 539 passes tags=False. I grepped the module's fixture. `run_tag_check` is called only at line 1062, directly, and neither ' · tags · ' nor 'cites retired' is asserted through check_tree or the write path. The unit's acceptance ledger confirms that AC1 was a one-off scratch probe and that G8 checks only the leg manifest. Nothing in the suite pins either side of the new switch, so a flipped default or a tags=False at line 300 would drop the write-boundary tag check and the selftest would stay green. The effect is contained, because the bar's tags leg still catches it later. | sound | - | class:rule-stated-with-no-check-that-fails |
| 5 | verification | .githooks/pre-commit:203 | low | medium | confirmed | At the base, the template-size trigger was `git diff --cached --name-only -- coding-governance-agents.template.md` (base line 274). This diff replaced it with the `st_template` case pattern (.githooks/pre-commit, the st_list loop) and the `[ -n "$st_template" ]` guard, so the untested trigger is new in this diff. I grepped .githooks/pre-commit.test.sh and found no match for `coding-governance-agents.template.md`, `check-template-size` or `st_template`; its only 'template' hits are `git init --template=`. No other test drives the hook with the template staged. So a typo in that case arm, or in its guard, would silently stop the commit-time leg while the self-test stays green. The bar's template-size leg still catches an oversize template at push, so the effect is contained: medium. | sound | - | class:rule-stated-with-no-check-that-fails |
| 6 | intent | tools/run-gates/run-gates.test.sh@e33c90b2:569 | medium | medium | confirmed | Arm 1m (tools/run-gates/run-gates.test.sh@e33c90b2:562-570) asserts that `_mlaunch` (what the leg's resolve_python printed) equals `_mml` (line 2 of the inherited memo) and that it runs. On a hit the block prints BASH_REMATCH[3], which is PYBIN. On a miss the probe loop runs over the same GOV_PYTHON and PATH and returns at the first usable candidate, which is normally that same PYBIN. Both paths print the same string, so the arm cannot tell a memo hit from a re-probe. Nothing else exercises the runner's real export at run-gates.sh (`export GATE_RESOLVED_PY=...`) against the block's `_rp_re` layout. A drift in that layout would make every leg re-probe while every gate stays green. The cost is lost time, never a wrong verdict: medium. | unsound | assertion-between-two-derived-values | class:assertion-between-two-derived-values |
| 7 | intent | memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-11.md:252 | low | low | confirmed | Checked against the code. Spec §7 line 252 says the new run-gates.test.sh arm covers AC5. AC5 (spec lines 229-232) names two red cases: the unset placed after the resolution, and the export placed before the digest. Arm 1m (tools/run-gates/run-gates.test.sh@e33c90b2:540-570) only goes red when the `unset GATE_RESOLVED_PY` line is deleted, and its header says outright: 'WHAT THIS DOES NOT CHECK: that the export follows the toolchain digest, which is the spec's grep over the runner.' No suite grep-checks `export GATE_RESOLVED_PY`. The other GATE_RESOLVED_PY hits in the test files are only the resolver-block copies. The impact holds too. The digest subshell (tools/run-gates/run-gates.sh@33b623a2:3534-3565) reads `compgen -e` in direct mode and hashes any `GATE_*` name not on its skip list, and GATE_RESOLVED_PY is not on that list. So if the export at :3572 moved above `) && REUSE_DIGEST=` at :3566, a direct bar's key would carry the name and a push bar's would not, and no gate would catch it. Today the order is correct (352, 353, 3566, 3572), so nothing misbehaves now. The defect is a spec line that overclaims coverage plus a missing lasting guard, and a regression would only cost verdict reuse, not give a wrong verdict. That makes it low. | sound | - | class:observed-by-claim-no-arm-discharges |
