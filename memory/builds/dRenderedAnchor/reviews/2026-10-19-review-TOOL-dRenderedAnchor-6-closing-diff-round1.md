**Serves:** diff-review TOOL-dRenderedAnchor-6

# Closing diff review, round 1: dRenderedAnchor unit 6, the receipt-aware harness citations

2026-10-19 · Tier-2 · on `branch/frosty-feistel-42acd4` · adversarial fan through `tier2-review.js`: 5 finder lenses, then 5 skeptic batches, then this synthesis. Base 05357638b is the landed tip of units 1-5. The unit adds `render_kit_cites` to `tools/lib/render-doc.sh`, inlines it with `derive_kit_paths` into `tools/workflows/check-protocol-parity.test.sh` and `tools/unattended/adopt-unattended.sh`, and adds the `PROTOCOL_PARITY_REPASS` re-run. The range also carries a manifest re-stamp of `memory/guides/SESSION-KICKOFF.md` and records.

**Reviewed range:** `05357638b6727a98ff603ffc6e62361890748533...0a6eff73e1a81f9841512dd9c5e7c4d8ab9229cb`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker.

One high stands. Under a junction-installed kit, the new cite derivation resolves the junction, so both rendered documents name the target repo's paths and the parity leg certifies them.

One medium stands. Receipt-held paths now reach a JS string literal and agent-run shell commands without the charset guard both renderers already apply to their other substituted values.

Four low items remain: a false "never re-runs" claim in the README, the script comment and the spec; a silent skip of the re-run; and two missing arms.

## Review shape

Intensity **full** · raw **10** · confirmed **10** · refuted **0** · unverified **0** (0 uncertain) · precision **1.00**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: **6 items**, 0 blocker, 1 high, 1 medium, 4 low. By raw confirmed finding: 0 blocker, 1 high (id 4), 2 medium (ids 1, 5), 7 low (ids 2, 3, 6, 7, 8, 9, 10).

Run integrity:
- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 8 judged sound, 2 judged UNSOUND (ids 1 and 8, whose corrected fixes are written below), 0 with none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED and 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

The run is complete.

Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages. Checklist: 13 items, each assigned to exactly one of 5 lenses (security 3, correctness 3, seams 3, verification 2, intent 2). By design: the caller's byDesign.

## Items

### H1 [HIGH]: under a junction-installed kit, the cite derivation follows the junction and renders the target repo's paths (id 4)

**Where:** the inlined `derive_kit_paths` python, `kit = pathlib.Path(sys.argv[1]).resolve()`, at `tools/workflows/check-protocol-parity.test.sh:293` and `tools/unattended/adopt-unattended.sh:401`. The canonical copy in `tools/lib/render-doc.sh` already held the line at base (:152).

**What is wrong:** `.resolve()` follows a junction. Both renderers find their own root with a logical walk, which `adopt-unattended.sh:55-61` states as the junction contract for "the install shape this fleet uses". `resolve_kit_dir` itself uses `absolute()  # never resolve()`. Before this diff the two renderers substituted the logical TOOLROOT. This diff is what first inlines the resolving line into them, so it makes the defect reachable here.

**Consequence:** A scratch probe built repo B with `.gov/workflows` and `.gov/hooks` as junctions to `T/tools/workflows` and `T/tools/hooks`. Run from B, `derive_kit_paths python3 .gov/workflows tpl` printed `tools/workflows/tier2-review.js` and `tools/hooks/agent-cap.js`. Neither path exists in B. The base rendered `.gov/workflows/...` and `.gov/hooks/...`, which do exist.
- `REVIEW-PROTOCOL.md` names dead paths: agent-cap.js 7 times and tier2-review.js twice.
- The Skill's `unattended-build.js` and `unattended-unit.js` citations name dead paths too.
- The Skill's `unattended-unit.js` stops matching the harness's logical `{{KIT_DIR}}/unattended-unit.js` hand-out, the pair PV-AC12 exists to keep as one answer.
- Check mode derives the same way, so the parity leg reports the dead render as in parity.

The path is narrow: it needs a junction install whose prefix differs from the target's.

**Fix (skeptic judged SOUND):** In the canonical `derive_kit_paths` in `tools/lib/render-doc.sh`, use `pathlib.Path(sys.argv[1]).absolute()` instead of `.resolve()`, as `resolve_kit_dir` already does. Re-inline it into both renderers; the parity row in `tools/lib/resolve-python.test.sh` then holds the copies byte-identical. Add an arm that builds a junction kit dir under a prefix that differs from the target's, and assert the protocol names the logical `<prefix>/workflows/tier2-review.js`.

**Left-shift gate:** the junction arm above, observed RED on `.resolve()`. Add a checklist entry under two-answers-to-one-question: "a canonical block that computes a kit or root path uses the same walk as every script that inlines it: `absolute()`, never `resolve()`." A grep in the resolve-python parity section that refuses `.resolve()` on `sys.argv` paths inside canonical render blocks would make that entry a gate.

### M1 [MEDIUM]: receipt-held paths reach a JS literal and agent-run shell commands without the renderers' charset guard (ids 1, 5)

**Where:**
- The applied values: `render_kit_cites` in `tools/workflows/check-protocol-parity.test.sh:415-421`, called at :479, and in `tools/unattended/adopt-unattended.sh:523`, called at :679. The canonical copy is in `tools/lib/render-doc.sh:280-285`.
- The guard that does not cover them: `check-protocol-parity.test.sh:457-466` (`case "$KITREL/$MTD" in *[!A-Za-z0-9._/+@-]*`), and `adopt-unattended.sh:535` and :590 for TOOL_ROOT and MEMORY_TREE_DIR.
- The sinks: `tools/workflows/unattended-build.template.js:557`, `const DRIVER = 'bash {{TOOL_ROOT}}unattended/unattended.sh'`, a JS string literal holding a shell command agents are told to "Run exactly". Also SKILL.template.md:159, `python {{TOOL_ROOT}}runlog/runlog.py record`.

**What is wrong:** A cite's value is `(resolve_kit_dir(home, anchor, kit)/anchor).relative_to(root)`. `resolve_kit_dir` accepts any receipt row whose `source` ends in `<home>/<anchor>` and whose `path` is an existing file inside the tree. So the directory part of the value comes from the receipt. The only filter is `derive_kit_paths`' `emit()` (`render-doc.sh:149-154`), which refuses tab, CR and LF and nothing else. `render_kit_cites` substitutes the value verbatim. Before this diff every `{{TOOL_ROOT}}` value in these two renders came from KITREL or TOOL_ROOT, which pass the charset guard. The guard's comment still says it covers every interpolated value. Spec §5's security claim ("applies only paths the resolver admits: inside the tree, existing") does not cover characters. Separately, the emitted value is `<row dir>/<anchor>`, which need not exist.

**Consequence:**
- Injection: one `.governance/install.json` row with `source` ending in `unattended/unattended.sh`, plus a file at `scripts/u';process.exit(7);'/unattended.sh`, rendered `const DRIVER = 'bash scripts/u';process.exit(7);'/unattended.sh'`. `node` on the result exited 7.
- Breakage without malice: a receipt row `{"source":"g/unattended/unattended.sh","path":"my tools/unattended/unattended.sh"}` rendered `const DRIVER = 'bash my tools/unattended/unattended.sh'`, a command the space splits.
- `--render` writes the render and `--check` diffs against the same render, so the gate meant to keep the harness byte-equal to its template stays green over the injected or broken bytes.

The effect is contained: the attacker needs write access to the committed receipt and the tree.

**Fix:** The skeptic judged id 1's own proposal UNSOUND. The fix below is that skeptic's correction, and it agrees with id 5's fix, which the skeptic judged SOUND.
- Use the scripts' existing path charset, `[A-Za-z0-9._/+@-]`, and check only the lines `render_kit_cites` applies.
- In `check-protocol-parity.test.sh`, after each `derive_kit_paths` call (:522 for `KIT_PATHS` and :602 for `_kp_after`), and in `adopt-unattended.sh` after :570, loop over `KIT_PATHS` with CRs dropped.
- For each line whose key matches `'{{TOOL_ROOT}}'?*`, run `case "$kv" in ''|*[!A-Za-z0-9._/+@-]*)`. On a hit, print a line naming the cite and its value in the existing refusal's wording, and exit 2 before anything is written.
- Leave the bare `{{TOOL_ROOT}}` line and the adopter-placeholder lines alone. Their values are phrases with spaces and backticks, so folding all of `KIT_PATHS` into the existing `case` would refuse every install.
- Add a section 2g / RA6 arm with a receipt-held path containing `'` and `;`, and another with a space. Observe both RED without the check.

**Left-shift gate:** the 2g/RA6 arms above. Add a checklist entry: "a new channel that feeds a substituted value into a template passes the same charset guard as the values already substituted there; a guard comment that says 'every interpolated value' is re-read when a channel is added."

### L1 [LOW]: the README, the script comment and the spec say `--tracked-only` never re-runs, but it re-runs after restoring a deleted tracked harness (ids 3, 6, 7, 10)

**Where:** `tools/workflows/README.md:68` ("`--tracked-only` creates nothing, so the regenerate's two derivations agree and it never re-runs"), the comment at `tools/workflows/check-protocol-parity.test.sh:600-601` ("under --tracked-only nothing is created"), and spec TOOL-dRenderedAnchor-6 §4 (:193-194). All three are new in this diff.

**What is wrong:** The `--tracked-only` skip at `check-protocol-parity.test.sh:532-535` fires only when the live copy is absent AND untracked (`[ ! -e "$LIVE" ] && ! check_tracked "$LIVE"`). The comment just above it (:529-531) says a tracked copy someone deleted is still rendered. PAIRS (:94-98) includes `$KITREL/tier2-review.js`, `unattended-build.js` and the drift-audit harnesses. Take a tracked `tier2-review.js` deleted from the worktree:
1. The first derivation cannot see it, because `resolve_kit_dir` keeps a receipt row or probe only when the file exists. `derive_kit_paths` drops the cite (the `continue` at :310).
2. The write loop (:583-593) recreates the file.
3. The second derivation at :602 does see it, so `_kp_after != KIT_PATHS` and the run re-runs itself under `PROTOCOL_PARITY_REPASS` (:603-607).

This happens in a renamed install and in gov's own tree.

**Consequence:** None in behaviour. The re-run converges and renders the right citation. A probe confirmed it: an RA6-style layout (kit at `scripts/rh`, four receipt rows) was committed, then `scripts/rh/tier2-review.js` was deleted. `--render --tracked-only` printed the five "rendered" lines, then "this render wrote a file a template's citation resolves to, so the citations moved; rendering once more", then the five lines again, with rc=0. The three carriers state a guarantee the code does not give. A later change built on it would rest on a false premise, for example dropping the re-run guard under `--tracked-only`, or treating a re-run line in govkit's captured stage-1 output as a fault.

**Fix (skeptic judged SOUND for all four ids):** Restate all three carriers to match the code: "`--tracked-only` creates only a live copy this install already tracks. On a tree that holds every rendered harness, the two derivations agree and it does not re-run. A tracked harness deleted from the worktree is recreated, and then the run re-runs once, like a fresh render." Optionally add an arm to the RA6 layout: commit the render, delete the tracked harness, run `--render --tracked-only`, then assert the re-run line appears exactly once and the following check mode reads in parity.

**Left-shift gate:** the optional arm above, which makes the documented behaviour tested. Add a checklist entry: "a doc or comment that says a path 'never' happens names the condition that guarantees it, checked against every skip condition it depends on, or names the arm that would fail."

### L2 [LOW]: an inherited `PROTOCOL_PARITY_REPASS` suppresses the re-run silently and exits 0 over a render the run knows is stale (id 2)

**Where:** `tools/workflows/check-protocol-parity.test.sh:604`, the guard `[ -z "${PROTOCOL_PARITY_REPASS+set}" ]`, and `exit 0` at :609.

**What is wrong:** The guard is false whenever the variable is set, including to an empty string. If the two derivations differ under that guard, control reaches `exit 0` with no line saying the citations moved. This is the degradation-known-but-unreported class: the run knows its render is stale and reports success. A probe with `export PROTOCOL_PARITY_REPASS=` took the skip branch.

**Consequence:** Inside the guarded child the derivations normally agree, so the branch is reachable only through a variable leaked from a caller's environment. The run that wrote a stale protocol and harness prints only its "rendered" lines and exits 0. The next `--check` reports DRIFT, so nothing wrong is certified, but the operator meets it later as an unexplained DRIFT from a different invocation.

**Fix (skeptic judged SOUND):** Under the guard, when `_kp_after != KIT_PATHS` and the re-run is suppressed, print one line saying the citations moved and `PROTOCOL_PARITY_REPASS` suppressed the re-run, and exit non-zero (1 or 2) instead of 0. Optionally test the guard as `[ "${PROTOCOL_PARITY_REPASS:-}" != 1 ]`, so an inherited empty value does not disable it.

**Left-shift gate:** an arm that exports `PROTOCOL_PARITY_REPASS=` before a render whose citations move, and asserts a non-zero rc plus the suppression line. Add a checklist entry under degradation-known-but-unreported: "a guard that suppresses a corrective step prints why and exits non-zero when the step was needed."

### L3 [LOW]: RA6-1 throws away the render's output and rc, so the re-run announcement and exit-status pass-back have no assertion (id 8)

**Where:** `tools/workflows/unattended-build.test.sh:2288`, `run_layout "$R6" scripts/rh --render >/dev/null`. The behaviours it leaves unchecked are the "rendering once more" line and `exit $?` at `check-protocol-parity.test.sh:605-606`.

**What is wrong:** Spec S4 adds both behaviours. RA6-1 checks only the rendered file's counts (:2290-2292) and a later check-mode run (:2293-2295). A search of `tools/` for "rendering once more", "citations moved" and `PROTOCOL_PARITY_REPASS` finds no test that asserts either.

**Consequence:** If someone removed the announcement, or changed `exit $?` to `exit 0`, RA6-1 would stay green. A re-run that fails after the parent already wrote stale-citation renders would then report success to govkit or the operator. The effect is contained, because a later check-mode run would read DRIFT.

**Fix:** The skeptic judged the finder's proposal UNSOUND. The fix below is the skeptic's correction.
- Capture the `--render` output. Assert that "rendering once more" occurs exactly once and that rc=0.
- Cover the exit-status pass-back with a separate staged run in which only the child fails. For example, point the parity script's python at a wrapper that exits non-zero when `PROTOCOL_PARITY_REPASS` is set, so the child's derivation exits 2.
- Assert that the parent's `rc=` line carries the child's status (rc=2), not rc=0.
- Observe that assertion RED with `exit $?` changed to `exit 0`, then GREEN restored, and raise `FLOOR_ASSERTIONS` by the added sites.

**Left-shift gate:** the staged child-failure arm above. Add a checklist entry: "an arm that runs a mode whose printed line or exit status the spec defines captures both; `>/dev/null` on such a run is a review flag."

### L4 [LOW]: the new no-python and failed-derivation refusals have no arm, and the parity script now needs python where it did not (id 9)

**Where:** `tools/workflows/check-protocol-parity.test.sh:514` (`_cite_py=$(resolve_python) || exit 2`) and :521-522 (exit 2 on a failed `derive_kit_paths`), and `tools/unattended/adopt-unattended.sh:569-570`. All are new in this diff.

**What is wrong:** No arm in `unattended-build.test.sh` or `resolve-python.test.sh` runs either script with python stubbed out or with a failing derivation. The 9009-stub arms in `resolve-python.test.sh` (:58, :72) exercise only `resolve_python` itself. Spec S6 records the branch as NOT OBSERVED because it "needs a PATH emptied of every launcher". It is cheap to stage: put first on PATH a directory of `python3`/`python`/`py` stubs that exit 9009, like the MS-Store stub. This is also a behaviour change. At base, the only python use before the by-design arm was the tolerant MTD probe (`resolve_python 2>/dev/null && ...`, base :451), and the `_bd_py ... || exit 2` exit (base :420) ran only when `MTD_SKIP` was empty. So on an install without the memory-tree kit the base script ran with no python, and it now exits 2 unconditionally.

**Consequence:** Today the refusal works. Nothing guards it: an edit that turns `|| exit 2` into `|| :` would bring back the dead-path renders this unit retires, and every suite would stay green. The finder could not observe the branch, because the role hook refused the check-mode probe as a suite-shaped run.

**Fix (skeptic judged SOUND):** Add an arm to the RA6 layout. Make a scratch bin directory holding `python3`, `python` and `py` scripts that `exit 9009`, and unset `GOV_PYTHON`. Run the fixture's parity script and `adopt-unattended.sh --check` with `PATH="$stubbin:$PATH"`. Assert rc=2 and the `resolve_python` reason line for each. Observe it RED with `|| exit 2` replaced by `|| :` in each script.

**Left-shift gate:** the stub-PATH arm above. Add a checklist entry: "every new exit-2 refusal ships with an arm observed RED on its staged break; NOT OBSERVED is accepted only where the stage truly cannot be built, and the 9009 stub PATH always can."

review-shape kind=diff-review round=1 intensity=full at=synth raw=10 confirmed=10 refuted=0 unverified=0 blocker=0 high=1 medium=2 low=7 agents=11 out-tokens=154338

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/check-protocol-parity.test.sh:479 | medium | medium | confirmed | The claim holds against the code. derive_kit_paths' emit() (render-doc.sh:149-154) refuses only tab, CR and LF. A cite's value is (resolve_kit_dir(home, anchor, kit)/anchor).relative_to(root), and resolve_kit_dir accepts any receipt row whose `source` ends in <home>/<anchor> and whose `path` is an existing file inside the tree. That makes the directory part receipt-controlled, and nothing checks its characters. render_kit_cites (check-protocol-parity.test.sh:415-421, called at :479; adopt-unattended.sh:523, called at :679) substitutes that value verbatim. The diff also bypasses a guard both scripts already keep for this purpose. check-protocol-parity.test.sh:457-466 refuses a KITREL/MTD outside [A-Za-z0-9._/+@-] because 'Both values land inside a single-quoted JS string in the harness and inside a shell command an agent runs'. adopt-unattended.sh:535 and :590 apply the same charset to TOOL_ROOT/MEMORY_TREE_DIR. Before this diff the {{TOOL_ROOT}} values in these two renders came only from KITREL/TOOL_ROOT, which pass that guard. The new KIT_PATHS channel reaches the same JS literal and shell commands with no charset check. --render writes the render and --check diffs against the same render, so parity stays green. The impact is contained: the attacker must be able to write the committed receipt and tree. A non-malicious space or quote in a renamed kit dir hits it too, which is the case the existing guard was written for. So it is a real defect of contained effect: medium. | unsound | - |
| 2 | security | tools/workflows/check-protocol-parity.test.sh:604 | low | low | confirmed | At check-protocol-parity.test.sh:604, `[ -z "${PROTOCOL_PARITY_REPASS+set}" ]` is false whenever the variable is set, including to an empty string. If `_kp_after != KIT_PATHS` under that guard, control reaches `exit 0` at :609 with no line saying the citations moved. The only output is the earlier 'rendered' lines, so the run knows its render is stale and reports success. Normally that branch is unreachable: the guarded child derives KIT_PATHS over files the parent already wrote, so its two derivations agree. It is reachable only when PROTOCOL_PARITY_REPASS leaks in from the caller's environment. The next --check run does report DRIFT, so nothing wrong is certified. The real effect is an unreported, misattributed degradation on a narrow path: low. | sound | degradation-known-but-unreported |
| 3 | correctness | tools/workflows/README.md:68 | low | low | confirmed | The claim holds. At check-protocol-parity.test.sh:535 the --tracked-only skip fires only when `[ ! -e "$LIVE" ] && ! check_tracked "$LIVE"`, and the comment just above it says a tracked copy that was deleted is still rendered. PAIRS (lines 94-98) includes $KITREL/tier2-review.js, unattended-build.js and the drift-audit harnesses, so a tracked harness that was deleted gets recreated by the write loop. The first derive_kit_paths could not see it: resolve_kit_dir keeps a receipt row only when `hit.is_file()`, and the probe fails too. The second derivation at :602 does see it. That makes _kp_after differ from KIT_PATHS, and the re-run at :604-607 fires. Even in an un-renamed layout the probe adds a new line after the write, so KIT_PATHS differs there as well. The sentence added at README.md:68 ('--tracked-only creates nothing ... it never re-runs') and the comment at :600-601 are therefore false. Rendering is still correct, so the harm is limited to misleading prose: low. | sound | - |
| 4 | seams | tools/workflows/check-protocol-parity.test.sh:293 | high | high | confirmed | The `kit = pathlib.Path(sys.argv[1]).resolve()` line was already in the canonical derive_kit_paths at the base (render-doc.sh:152). This diff is what first inlines it into the two harness renderers (check-protocol-parity.test.sh:293, adopt-unattended.sh:401), which before rendered the logical TOOLROOT. So the diff makes the defect reachable from these renderers. adopt-unattended.sh:55-61 states the junction contract: the kit-dir walk is logical, and junction installs are 'the install shape this fleet uses'. resolve_kit_dir also says `absolute()  # never resolve()`. I reproduced it in a scratch dir: B/.gov/workflows is a junction to T/tools/workflows, both B and T have .git, and the template cites {{TOOL_ROOT}}workflows/tier2-review.js. Running `derive_kit_paths python .gov/workflows tpl` from B printed `{{TOOL_ROOT}}workflows/tier2-review.js<TAB>tools/workflows/tier2-review.js`, which is the target's layout and does not exist in B. Before this diff the plain TOOL_ROOT gave .gov/workflows/tier2-review.js. Check mode derives the same way, so the parity leg certifies the dead render as in parity. It is a wrong result, but only on a junction install whose prefix differs from the target's, so high. | sound | two-answers-to-one-question |
| 5 | seams | tools/workflows/check-protocol-parity.test.sh:460 | medium | medium | confirmed | I read the code and the claim holds. In tools/workflows/check-protocol-parity.test.sh the charset refusal at ~460 tests only "$KITREL/$MTD". KIT_PATHS is derived later, at ~520. render() then calls render_kit_cites before the {{TOOL_ROOT}} substitution, and render_kit_cites in tools/lib/render-doc.sh:280-285 splices each value into the template unchecked. derive_kit_paths' emit() refuses only tab, CR and LF. resolve_kit_dir accepts any receipt row whose source ends in <home>/<anchor> and whose path is an existing file inside the root with no '..' part, so a path containing a space or a quote passes. tools/workflows/unattended-build.template.js:557 has `const DRIVER = 'bash {{TOOL_ROOT}}unattended/unattended.sh'`, which is a cite home/file shape, so it now takes the receipt value. At the base, every value reaching that literal was TOOLROOT, derived from the charset-checked KITREL. The diff therefore opens a path around the guard, and the guard's comment still says it covers every interpolated value. Check mode renders the same bytes, so the leg reports parity. The path is narrow: it needs a hand-edited receipt plus an existing file at the odd path. The effect is contained to a rendered harness whose driver command breaks, so medium. | sound | - |
| 6 | seams | tools/workflows/README.md:68 | low | low | confirmed | The skip at check-protocol-parity.test.sh (the --tracked-only branch) needs `[ ! -e "$LIVE" ] && ! check_tracked "$LIVE"`, so a tracked live copy deleted from the worktree is still rendered. The render-mode write loop then copies it into place. PAIRS has $KITREL/tier2-review.js, and REVIEW-PROTOCOL.template.md cites {{TOOL_ROOT}}workflows/tier2-review.js. The first derivation finds no such file: the receipt row needs hit.is_file(), and the probes are <kit>/workflows and <kit>/../workflows. So it emits no line for that cite. After the write, the second derivation does emit it, _kp_after != KIT_PATHS, and the script re-runs. That happens in a renamed install and also in gov's own tree, where the re-run is benign. So 'creates nothing ... never re-runs' is false in both the new README text (tools/workflows/README.md:68, which the base did not have) and the new comment at ~601. The behaviour itself is correct, so the defect is documentation only: low. | sound | - |
| 7 | verification | tools/workflows/README.md:68 | low | low | confirmed | The claim is false, and the path that disproves it is reachable. check-protocol-parity.test.sh:535 skips a pair under --tracked-only only when the live copy is absent AND untracked, so a tracked copy someone deleted is still rendered and written by the loop at :586-593. PAIRS (:94-98) includes $KITREL/tier2-review.js, and the template cites {{TOOL_ROOT}}workflows/tier2-review.js (REVIEW-PROTOCOL.template.md:34,202). resolve_kit_dir (:236-272) accepts a receipt row or a probe only when hit.is_file() / (cand/anchor).is_file(). So when that harness is deleted, the first derivation cannot resolve it, derive_kit_paths drops it (the `continue` at :310), and KIT_PATHS leaves it out. After the write, _kp_after does include it, the two differ, and :603-606 re-runs. Despite that, README.md:68, the comment at :601 and spec §4 :193-194 all say --tracked-only never re-runs. The re-run converges and does no harm, so the only consequence is a false statement in the docs and the comment: low. | sound | - |
| 8 | verification | tools/workflows/unattended-build.test.sh:2288 | low | low | confirmed | unattended-build.test.sh:2288 runs `run_layout "$R6" scripts/rh --render >/dev/null`, which discards both the output and the rc= line. Searching tools/ for 'rendering once more', 'citations moved' and PROTOCOL_PARITY_REPASS finds no test that asserts the announcement line or how the exit status is passed back. RA6-1 checks only the rendered file's counts (:2290-2292) and a later check-mode run (:2293-2295). If someone removed the announcement, or changed `exit $?` at :606 to `exit 0`, RA6-1 would stay green. Today's behaviour is correct, and a later check-mode run would read DRIFT, so the effect is contained: this is a coverage gap, low. | unsound | - |
| 9 | verification | tools/workflows/check-protocol-parity.test.sh:514 | low | low | confirmed | I checked the code. check-protocol-parity.test.sh:514 (`_cite_py=$(resolve_python) \|\| exit 2`) and :521-522 (derive_kit_paths failure, exit 2) are new in this diff, and so are adopt-unattended.sh:569-570. I grepped unattended-build.test.sh and resolve-python.test.sh and found no arm that runs either script with python stubbed out or with a failing derivation. The 9009 stub arms in resolve-python.test.sh (lines 58 and 72) exercise only resolve_python itself. Spec S6 (line 46) records the branch as NOT OBSERVED. The behaviour-change claim also holds. At base, the only python use before the by-design arm was the tolerant MTD probe (`resolve_python 2>/dev/null && ...`, base :451). The `_bd_py ... \|\| exit 2` exit (base :420) ran only when MTD_SKIP was empty. So on an install without the memory-tree kit the base script ran with no python, and it now exits 2 unconditionally. The effect is contained: today the refusal works, and the only cost is that nothing guards it against a later regression. Low. | sound | - |
| 10 | intent | tools/workflows/README.md:68 | low | low | confirmed | The README line ('`--tracked-only` creates nothing, so the regenerate's two derivations agree and it never re-runs') is added by this diff, and so is the script comment at check-protocol-parity.test.sh:601. The skip at :532 fires only when TRACKED_ONLY=1 AND the live copy is absent AND `! check_tracked`. The comment right above it (:529-531) says a tracked copy somebody deleted is still rendered. The write loop at :583-588 then copies it into place. Take $KITREL/tier2-review.js, which is in PAIRS, tracked and deleted. In the first derivation resolve_kit_dir skips its rendered receipt row (it requires `hit.is_file()`), and both probes miss. That raises LookupError, so derive_kit_paths emits nothing for the citation. After the write, the file exists, the second derivation emits it, `_kp_after != KIT_PATHS`, and the run re-runs itself through PROTOCOL_PARITY_REPASS. Both carriers therefore state a guarantee the code does not give. No wrong render results, so the defect is documentation only. | sound | - |
