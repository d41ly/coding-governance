**Serves:** diff-review TOOL-dTotalRecall-122 TOOL-dTotalRecall-8 TOOL-dTotalRecall-37 TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-122

# dTotalRecall — Tier-2 CLOSING DIFF review, round 3

*Node `d`, 2026-11-26. This round reviews the units built after round 2: TOOL-dTotalRecall-122 (round 2's minors), TOOL-dTotalRecall-8 (the code record under a bound it meets), TOOL-dTotalRecall-37 (its generated-code registration) and TOOL-dTotalRecall-123 (the map replay's noise rule and its second experiment). Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 4 spec documents supplied as `specs`, beside the range's commit messages. The checklist had 98 items, acquired by the harness from `--for-diff 146df78025b4f87a6a9449fe3225b5472f69a168..33706662ef0750552bf8820599bd2f204760f156`, each assigned to exactly one lens: security 20, correctness 20, seams 20, verification 19, intent 19. By design: 1 invariant from the checklist's by-design block.* (DERIVED 2026-11-26, the review)

**Range reviewed: `146df78025b4f87a6a9449fe3225b5472f69a168...33706662ef0750552bf8820599bd2f204760f156`**

**Round: 3.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER.
One item is HIGH: H1, tracked paths fed to ctags as `-L -` lines that ctags reads as options.
Eight items are MEDIUM and three are LOW.
Two MEDIUMs are checks that certify what they do not check: M1, the read allowlist still admits rg and git options that run commands, and M2, the `Decided:` check that compares counts instead of matching lines.
Two MEDIUMs are the new dossier anchors: M3, anchors replace path staleness instead of refining it, and M4, no gate resolves the committed anchors at HEAD.
Two MEDIUMs are the `playbook render selftest` leg after `code_record.py --selftest` joined it: M5, its guard, and M6, its budget row.
Two MEDIUMs are refusal branches no arm reaches: M7 in the replay scorer and M8 in `map_diff.py`.
I recommend folding H1 and M1 before the landing, each with a plant seen red first.
The rest can be folded or filed.

## Review shape

Intensity full, raw 14, confirmed 12, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.86.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 6 | 5 | 1 | 0 | 0 | 0 | 0.83 |
| verification | yes | 4 | 3 | 1 | 0 | 0 | 0 | 0.75 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 12 items (0 blocker, 1 high, 8 medium, 3 low).
Adjudicated tally by raw confirmed finding: 12 (0 blocker, 1 high, 8 medium, 3 low).
The two tallies agree because each confirmed finding is its own defect.
Every confirmed finding takes its binding grade.
Findings 8 and 12 were refuted and are not counted.
Neither refuted finding describes a confirmed defect, so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 9 judged sound (findings 4, 5, 6, 7, 9, 10, 11, 13, 14), 1 judged UNSOUND (finding 3), 2 judged INSTANCE-ONLY (findings 1, 2), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so those items carry the skeptic's class-level fix.
- The UNSOUND fix is replaced by the skeptic's corrected fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 2. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 98 class slugs handed; 231 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero, so this run is complete.

## HIGH

### H1. Tracked paths reach ctags as `-L -` lines, and ctags reads a leading `-` as an option (finding 2)

**Where:** `tools/playbook/code_record.py@63fe2576:400` (`read_ctags_defs`), lines 400-401.

**What is wrong:** `read_ctags_defs` runs ctags with `-L -` and writes the raw tracked paths from `git ls-tree` (line 283) to its stdin, one per line, with no prefix.
The ctags manual says of `-L` that "Options are also accepted in this input".
A tracked path that starts with `-` is therefore read as an option, not a file name.
Only the output side strips `./` (line 414).

**Consequence:** this runs only when the code-record policy value selects ctags (line 794) and the repo tracks such a path, so the path is narrow.
On it, repository content becomes ctags options: a file `--options=y.c` makes ctags load the copy written at lines 396-398 as an option file, and `-fZ.c` redirects the tag output.
That is option injection from an untrusted tree into a program the record trusts, at worst writing a file.
Established by reading; no ctags binary was installed, so it was not run.

**Grades:** 2 HIGH.

**Fix (the skeptic's class-level fix; the finder's is INSTANCE-ONLY):** prefix every `-L` line with `./`, and refuse any path holding `\n` or `\r`, or leave it to the builtin reader.
A git path can hold a newline, and with only the prefix the text after the newline arrives as an unprefixed line that ctags reads as an option.
Alternatively, pass the `./`-prefixed paths as argv instead of through `-L`.
The finder's proposal (write `./` + path, or refuse paths starting with `-`) cures the cited instance alone.

**Left-shift gate:** a `code_record.py --selftest` arm with a ctags stub that echoes its `-L` lines, over tracked paths `-fZ.c` and one holding a newline, asserting every line arrives `./`-prefixed and the newline path is refused; seen red with the prefix removed.

## MEDIUM

### M1. The read allowlist still counts rg and git calls that run commands as reads (finding 1)

**Where:** `tools/workflows/replay_scorer.py@9b34dbfc:1191` (`check_read_call`), lines 1191-1192 and 1349-1354.

**What is wrong:** S10 of TOOL-dTotalRecall-122 was meant to be the class-level fix: answer False for a read program's or a git read's writing option.
The diff refuses only `git --output` and the `find` write options.
A probe at 33706662 returned True for `rg --pre rm x .`, `rg --pre=rm x`, `git grep -Orm x`, `git grep --open-files-in-pager=rm x`, `git -c core.pager="rm a.py" log` and `git --config-env=core.fsmonitor=X status`.
The `GIT_OPTS_WITH_ARG` skip in `derive_segment_program` lets the `git -c` and `--config-env` forms through.
The docstring's gap list names none of these.
The new gotcha `memory/gotchas/read-allowlist-admits-a-writing-option.md` says the class is gated by map-transcript.

**Consequence:** a lens can delete or change files with these calls before its first act and still be scored as reading.
The map replay's bytes-before-first-act number is then inflated and can flip the term.
The gotcha's claim misleads the next change into trusting the check.
The effect is limited to that one replay term.

**Grades:** 1 MEDIUM.

**Fix (the skeptic's class-level fix; the finder's is INSTANCE-ONLY):** refuse `rg --pre` and `--pre=`, `git grep -O` and `--open-files-in-pager`, and `git -c` and `--config-env` before the subcommand.
Also refuse any segment whose leading `VAR=value` assignment sets a git or tool hook variable (`GIT_EXTERNAL_DIFF`, `GIT_PAGER`, `PAGER`, `GIT_CONFIG_*`, `GIT_SSH*`).
Also refuse git's `--ext-diff` and `--textconv` on read subcommands.
The finder's proposal (the rg, git grep and `git -c`/`--config-env` refusals only) cures the cited instance alone.

**Left-shift gate:** one map-transcript case per refused option and variable, each seen red with its refusal removed; the gotcha's gated claim stands only once those cases exist.

### M2. The `Decided:` check compares counts, so a `Decided :` trailer hides a decision git never reads (finding 3)

**Where:** `tools/lib/commit_trailers.py@ae056cd6:407` (`check_message_decisions`), with the same line at :405 in the memory-tree and unattended copies.

**What is wrong:** the check counts lines opening with exactly `Decided:` and compares that count with the `Decided:` lines in `git interpret-trailers --parse` output (`len(kept) >= len(said)`).
Git normalises `Decided :` to `Decided:` in its parse.
So a `Decided : x` trailer in the final block makes up for a real `Decided:` line above the block.
The probe `check_message_decisions('s\n\nDecided: lost - why\n\nPass: none\nDecided : kept\n')` returned `('ok', '1 decision(s), each in the final trailer block')`.
Git's parse of that message holds only `Pass: none` and `Decided: kept`.
The docstring's WHAT IT DOES NOT CHECK does not name this gap.

**Consequence:** the decision `lost - why` is invisible to every reader of the key, and `unattended --check-commit` (check 49) admits the commit.
Reaching it needs the unusual `Decided :` spelling plus a misplaced decision, so the effect is contained.

**Grades:** 3 MEDIUM.

**Fix (the skeptic's corrected fix; the finder's was judged UNSOUND):** match each said line one to one against git's parsed `Decided` values, using the key case-insensitively with whitespace allowed before the colon.
A said value matches a parsed value equal to it, or one that starts with it followed by a space, because git joins a folded continuation onto the value.
Remove each matched value from a multiset, and refuse naming the first said line with no match.
Add a `_DECISIONS_FIXTURE` case for `Decided : kept` expecting refused, and one folded `Decided:` trailer expecting ok, in all three copies.

**Left-shift gate:** the two `_DECISIONS_FIXTURE` cases above, the folded one seen to refuse under a plain-equality match and the `Decided :` one seen to pass under the count compare.

### M3. A dossier's `symbols` anchors replace its path staleness, so lexicon reads fresh when its own engine changes (finding 4)

**Where:** `tools/codebase-map/map_lib.py@fe64906d:1625` (`measure_dossier_staleness`), lines 1624-1626.

**What is wrong:** for any anchored dossier, `stale = now != then and (scope is None or stale)` throws away the path-ancestry result whenever the anchored hashes match.
`memory/map/features/lexicon.md@82706bc8` claims `tools/lexicon/*`, `check-placeholders.sh`/`.test.sh` and its kit.toml entry.
It anchors only `read_defs_at` and `extract_text` in `tools/lexicon/extract_code.py`, a byte-identical copy of the shared `tools/lib` block that the dossier's body never mentions.
The codebase-map selftest pins this behaviour: it asserts `behind == 1 and not stale` when an unanchored change lands.
Spec S12 asks for this literally ("stale only when an anchored definition's hash differs"), but the regression is this diff's.

**Consequence:** `map_diff.py --stale-dossiers`, drift-audit's `dossiers_older_than_their_paths` and unattended's range list stop reporting lexicon when `lexicon.py`, `canon.py` or `check-placeholders.sh` change.
Only an edit to two generic extraction functions it does not describe marks it stale.
The signals are advisory (drift_report marks it gateable False), so the effect is contained.

**Grades:** 4 MEDIUM.

**Fix (judged sound by the skeptic):** apply anchors only to the anchored file.
For a path the anchors name, use the hash comparison; for every other claimed path, keep the commit-ancestry rule, so a dossier is stale when an anchored hash moved or a non-anchored claimed path is behind.
Alternatively, anchor lexicon.md to definitions in the lexicon kit's own engine.

**Left-shift gate:** a codebase-map selftest arm where a second claimed file moves and the anchored dossier reads stale, replacing the arm that pins `not stale`.

### M4. No gate resolves the committed anchors at HEAD, and one unresolved anchor kills the whole dossier report (finding 5)

**Where:** `tools/codebase-map/map_diff.py@3a42e03d:394` (`main`), lines 389-395.

**What is wrong:** if any anchor key reads None at HEAD, `main` returns 1 before any row is measured.
Nothing in a gate reads `paths.symbols` or `read_anchor_hashes`: not `test_codebase_map.py`, not `check_gate_coverage.py`, not the code record leg, and no leg in gate-legs.json runs `--stale-dossiers`.
lexicon.md's anchors point into a parity copy of `tools/lib/extract_code.py`, so renaming `read_defs_at` or `extract_text` in the canonical file breaks them silently.
The exit 1 itself is what spec S12 asks for; the missing HEAD check is the gap.

**Consequence:** after such a rename, `drift_report.build_stale_dossiers` (`drift_report.py:3596-3600`) turns rc != 0 into one DEAD PROBE for all 34 dossiers.
`unattended.sh print_stale_dossiers` prints its DEAD PROBE line for every run's range.
The stderr line names the key, but no gate turns red.
The path is narrow and the signal advisory, so the effect is contained.

**Grades:** 5 MEDIUM.

**Fix (judged sound by the skeptic):** the `codebase-map coverage + freshness` leg runs `read_anchor_hashes` at HEAD and fails on a None key.
Separately, consider reporting an unresolved anchor as that one dossier's row (stale, with a note) instead of failing the whole report.

**Left-shift gate:** the HEAD-resolution check inside `codebase-map coverage + freshness`, seen red by planting an anchor on a function HEAD does not define.

### M5. The `playbook render selftest` leg now runs the code record selftest, but its guard omits `{prefix}/policy/` (finding 6)

**Where:** `tools/playbook/adopt-playbook.sh@b739293c:593`, lines 584-593; the guard in `tools/gate-legs.json@4b03b6e5` ("playbook render selftest").

**What is wrong:** the diff appends `code_record.py --selftest` to the leg.
That selftest commits `.governance/policy.toml` fixtures (`code_record.py:1248-1251`), and `read_policy_value` (`policy_value.py:88-94`) spawns `tools/policy/policy.py get --explain` against them.
It also reads blobs through memory-tree.
The leg's guard lists `{prefix}/playbook/`, seven memory-tree files, `{prefix}/lexicon/`, the kit.toml entry and the charter template, but no `{prefix}/policy/`.
`py_reads.py --guards` refuses this leg as not Python, so the guard is hand-kept and the diff did not touch it.
The sibling `code record` leg's derived guard does include policy/, but it runs only `--check` over the live tree.

**Consequence:** an edit confined to `tools/policy/` (its `get --explain` output, or its refusal) skips this leg or reuses its stale green.
The code record's AC8 refusal arms and ctags-value fixtures that depend on it then go unrun.

**Grades:** 6 MEDIUM.

**Fix (judged sound by the skeptic):** add `{prefix}/policy/` to the leg's guard in `tools/playbook/kit.toml` and re-render gate-legs.json.
Also add the memory-tree modules `ti.load_memory_tree` loads, or derive the guard from the same closure the `code record` leg uses.

**Left-shift gate:** derive this leg's guard from the closure of the Python entry points its script runs, so `gate-leg conformance` reds when a guard misses a kit one of them spawns.

### M6. The `playbook render selftest` budget row and ceiling evidence were not re-measured after the code record arms joined it (finding 7)

**Where:** `tools/run-gates/selftest-budgets.txt@ffa0dcf2:109`; `tools/run-gates/ceiling-evidence.txt:124`.

**What is wrong:** the budget row still reads `60 · worst of 8 readings 10s, x1.5`, and the ceiling evidence still reads 1.5 from 2026-09-24.
The diff appended `code_record.py --selftest` (adopt-playbook.sh:585-594), which builds about ten scratch git repositories with roughly 26 build, commit and verb steps.
The builder's return (`memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-8-1-builder-return.md:37`) says the suite now takes "about 73 s here" and that the evidence row "is stale at 1.5 s".

**Consequence:** the suite already exceeds its 60 s cost budget, a verdict `run-selftests.sh` reads.
On a loaded node a red or timeout names the playbook render suite, not the code record arms that caused it.
The 300 s hang ceiling still holds, so the effect is contained.

**Grades:** 7 MEDIUM.

**Fix (judged sound by the skeptic):** run `bash tools/playbook/adopt-playbook.sh --selftest` under the bar's timing (measure-legs, `derive-ceilings.py --observed`), and rewrite the budget row and the ceiling evidence from the new readings.

**Left-shift gate:** `every held leg is budgeted, every budget row resolves` reds when a leg's script changes in a range that leaves its budget row and evidence row untouched.

### M7. Two of the three branches of the replay scorer's run-count refusal have no arm (finding 10)

**Where:** `tools/workflows/replay_scorer.py@9b34dbfc:1471`, lines 1469-1473; the arm `check_map_noise_arm` at line 2305.

**What is wrong:** the refusal `if len(sent) > 1 or rest or want < 2:` is new in this range.
`check_map_noise_arm` plants a dropped run and two different dispatched counts, so only `len(sent) > 1` fires.
No case has one shared count the audit count does not divide (`rest`), and none declares one run (`want < 2`).
Spec 123 AC2 names both cases, and the spec says the arm covers AC2.
A mutant with the condition cut to `if len(sent) > 1:` still printed `ok map-noise` with rc 0.

**Consequence:** if the branch is lost, a manifest dispatching 5 runs over 2 audits is scored on 2 runs per audit and the fifth silently drops, the partial-set red AC2 names.
A one-run manifest reaches `statistics.variance` on one value and crashes with StatisticsError instead of a Refusal.
The effect stays inside the scorer's refusal path.

**Grades:** 10 MEDIUM.

**Fix (judged sound by the skeptic):** add two cases to `check_map_noise_arm`.
(a) A two-audit manifest with both `dispatched` set to 5: `check_refused` names 'dispatched 5' and 'over 2 audit(s)'.
(b) Both arms with `dispatched` 1 over one audit: the same refusal.
Re-run the in-memory mutant and confirm map-noise turns FAIL.

**Left-shift gate:** `harness arms (fail branches armed or pinned)` grades each disjunct of a refusal condition, so a disjunct no arm reaches reds.

### M8. No test runs `map_diff.py`'s exit 1 for an anchor HEAD does not define (finding 11)

**Where:** `tools/codebase-map/map_diff.py@3a42e03d:394`, lines 389-395; `test_anchored_dossier_staleness` in `tools/codebase-map/selftest.py`.

**What is wrong:** spec 8 AC9 requires that "a key HEAD's a.py does not define exits 1 naming it".
`test_anchored_dossier_staleness` stops at line 1624, where `read_anchor_hashes` returns None, and never calls `main`.
In the selftest, `md.main()` is called only at lines 250 and 259, the latter asserting rc == 2 for a refusal.
The test's docstring (1573-1574) says main turns the None into exit 1, but nothing asserts it.
`does not define` appears only in the docstrings, the README and the print.

**Consequence:** if `if unheld: return 1` is deleted or reordered, `--stale-dossiers` reads a dossier anchored on a removed function as fresh or stale with exit 0, and every arm stays green.

**Grades:** 11 MEDIUM.

**Fix (judged sound by the skeptic):** in the same git fixture, run `map_diff.py --stale-dossiers` as a subprocess, or call `md.main()` with argv patched, over a dossier whose symbols are `a.py::gone`.
Assert exit 1 and stderr containing 'anchors a.py::gone, which HEAD does not define'.
Stage it red by deleting `return 1`.

**Left-shift gate:** `harness arms (fail branches armed or pinned)` reds on a new `return 1` branch no arm reaches.

## LOW

### L1. The drift-audit README still defines `dossiers_older_than_their_paths` by commit ancestry alone (finding 9)

**Where:** `tools/drift-audit/README.md@685a7a52:159`.

**What is wrong:** the row defines the signal as "a commit touching a path the dossier claims is not an ancestor of the dossier's own last commit", and names only shallow clones and untouched paths as DEAD PROBE.
After this diff an anchored dossier is graded by definition hashes (M3), and an anchor HEAD does not define turns the whole signal into DEAD PROBE (M4).
The codebase-map README and map_diff's docstring were updated; this README was not.

**Consequence:** a reader of the drift report misreads a fresh anchored dossier, or an anchor-caused DEAD PROBE.
Only documentation is affected.

**Grades:** 9 LOW.

**Fix (judged sound by the skeptic):** extend the row: anchored dossiers (`[paths].symbols`) read stale only when an anchored definition's hash moved, and an unresolved anchor makes the probe answer DEAD PROBE.

**Left-shift gate:** `kit/dogfood doc parity` extended to pair each drift-audit signal row with the docstring of the producer it reads, so a producer's semantic change without the row reds.

### L2. No arm checks the first experiment's pinned noise figure 15.46 (finding 13)

**Where:** `tools/workflows/replay_scorer.py@9b34dbfc:1378` (`measure_rise_noise`); `check_map_verdict_arm` at line 2233.

**What is wrong:** spec 123 AC3's last sentence pins `measure_rise_noise` over the first record's six pairs at 15.46.
The string 15.46 appears nowhere under tools/ or skills/.
`check_map_verdict_arm` exercises only `derive_map_verdict` boundary sets.
`check_map_noise_arm` does pin `noise 5.65685` and `4.16333`, so a change to `NOISE_FACTOR` or the pooling would already red.

**Consequence:** only the first experiment's figure is left unjoined to its recorded pairs.
The gap is contained to a record figure.

**Grades:** 13 LOW.

**Fix (judged sound by the skeptic):** add the six pinned pairs to `check_map_verdict_arm` and assert `round(measure_rise_noise(pairs), 2) == 15.46`.
Stage it red by setting `NOISE_FACTOR` to 1.

**Left-shift gate:** `spec tokens (a spec's own names resolve)` extended so a numeric figure an acceptance criterion pins must appear in an arm.

### L3. The map replay verdict record omits the variances its spec says it carries (finding 14)

**Where:** `memory/builds/dTotalRecall/build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-verdict.md@f0873600:82`, section "The terms".

**What is wrong:** spec 123 §4 "The routes" says the record carries "the second experiment's own variances", and §5 says "the record carries the variances".
The section gives the per-run counts, the noise 7.0993 and the verdict, but no variance.
Recomputed with `statistics.variance` over the listed counts: without [5.3, 1.5, 2.8], sum 9.6; with [42, 6.7, 4.7], sum 53.4.
2*sqrt(63/5) = 7.0993, matching the printed noise.

**Consequence:** the measured spread that was to replace §4's rough two-run estimate, for the owner's decision on ask TOOL-dTotalRecall-111, is missing.
The with-map arm's audit-1 variance of 42 dominates the noise, and the record never says so.
The verdict is unaffected: the rise of -1.4 loses at any noise.

**Grades:** 14 LOW.

**Fix (judged sound by the skeptic):** add one line under "The terms" with each arm's sample variance per audit and their sums: without 5.3, 1.5, 2.8 (sum 9.6); with 42, 6.7, 4.7 (sum 53.4).
Add a sentence noting that audit 1's with-arm spread dominates the 7.0993 noise.

**Left-shift gate:** a bug-class checklist entry: a record whose spec names a figure it carries is checked for that figure before its commit.

## Refuted findings (not counted)

- Finding 8 (seams, `tools/playbook/code_record.py:968`): `--check` reusing held facts cannot catch a wrong facts row under an unchanged version key. Refuted: spec TOOL-dTotalRecall-8 AC5 requires that reuse. Not a twin of any confirmed finding.
- Finding 12 (verification, `tools/playbook/code_record.py:968`): the `code record` leg's red branch is unreachable outside the selftest. Refuted: an uncommitted edit to the assembly or render code reds it once a row exists for HEAD's tree. Not a twin of any confirmed finding.

review-shape kind=diff-review round=3 intensity=full at=synth raw=14 confirmed=12 refuted=2 merged=0 unverified=0 blocker=0 high=1 medium=8 low=3 agents=11 out-tokens=111679 trigger=- shape=- efforts=- role-sha=-
review-round round=3 limit=- prior=- count=1 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/replay_scorer.py:1191 | medium | medium | confirmed | I re-ran the probe on the worktree's check_read_call, using the runlog extract module. `rg --pre rm x .`, `rg --pre=rm x`, `git grep -Orm x`, `git grep --open-files-in-pager=rm x`, `git -c core.pager="rm a.py" log` and `git --config-env=core.fsmonitor=X status` all return True. `git diff --output=x` and `find . -delete` return False. check_read_call itself was already in the base, but this diff's S10 (spec TOOL-dTotalRecall-122 §2) was meant to be the class-level fix: "answers False for a read program's or a git read's writing option". The new gotcha memory/gotchas/read-allowlist-admits-a-writing-option.md tells the reader to read each admitted program's manual and claims the class is gated by map-transcript. The diff added only git --output and the find options, so rg is still an admitted program with an option that runs a command, and its docstring gap list does not mention it. The class fix this diff claims is incomplete. That is in scope, and it misleads the next change. The effect is limited to the map replay's bytes-before-first-act term, so medium. | instance | read-allowlist-admits-a-writing-option | class:read-allowlist-admits-a-writing-option |
| 2 | security | tools/playbook/code_record.py:400 | high | high | confirmed | tools/playbook/code_record.py is new in this diff. Line 400 runs ctags with `-L -` and line 401 feeds it the raw `want` keys, one per line with no prefix. Line 414 strips `./` only on the output side. The keys are tracked paths from git ls-tree (line 283), which can start with `-`. Universal/Exuberant ctags documents that options are also accepted in -L input, so a tracked file `--options=y.c` makes ctags load the copy written at line 396-398, which is repo content, as an option file. A path like `-fZ.c` would redirect the tag output. This is reachable only when the policy selects ctags (line 794) and the repo tracks such a path, so the path is narrow. The consequence is option injection from an untrusted tree, at worst writing a file, so high on the rubric. I could not run it because no ctags is installed. | instance | - | new:path-list-input-read-as-options |
| 3 | correctness | tools/lib/commit_trailers.py:407 | medium | medium | confirmed | check_message_decisions is new in this diff (TOOL-dTotalRecall-122 S9). Line 407 compares only `len(kept) >= len(said)`. I ran the cited probe from tools/lib and it returned ('ok', '1 decision(s), each in the final trailer block'). `git interpret-trailers --parse` on the same message prints only `Pass: none` and `Decided: kept`, so git normalised `Decided :` to `Decided:` and the decision above the block went uncounted. The check therefore certifies a decision that git never reads. Reaching this needs an unusual `Decided :` spelling in the final block plus a misplaced decision, so the effect is contained: medium. | unsound | - | class:trailer-parse-reads-only-the-final-block |
| 4 | seams | tools/codebase-map/map_lib.py:1625 | medium | medium | confirmed | map_lib.py:1624-1626 (this diff) sets `stale = now != then and (scope is None or stale)` for any dossier listed in anchors, so the path-ancestry result `bool(behind)` is thrown away whenever the anchored hashes match. memory/map/features/lexicon.md:55-65 claims tools/lexicon/*, check-placeholders.sh/.test.sh and the kit.toml entry, but anchors only extract_code.py::read_defs_at and ::extract_text. Those functions belong to the copied shared extraction block, and the dossier's body never mentions them. So an edit to lexicon.py, canon.py, check-placeholders.sh and so on leaves the dossier reading fresh. Spec S12 literally asks for this ('stale only when an anchored definition's hash differs'), but the consequence is a real regression that this diff introduced. Lexicon's freshness in --stale-dossiers, drift_report.build_stale_dossiers and unattended's VERIFYING print stops tracking its own engine. Those signals are advisory: drift_report marks it gateable False, so the effect is contained to medium. | sound | - | new:refinement-replaces-the-rule-it-refines |
| 5 | seams | tools/codebase-map/map_diff.py:394 | medium | medium | confirmed | map_diff.py:389-395 (this diff) returns 1 before measure_dossier_staleness runs if any anchor key reads None at HEAD. I grepped tools/ for read_anchor_hashes and paths.symbols. Outside map_diff, map_lib.parse_dossier and the fixture arm in codebase-map/selftest.py:1611, nothing reads them. test_codebase_map.py, check_gate_coverage.py and code_record.py never resolve the committed anchors, and gate-legs.json has no leg that runs --stale-dossiers. The anchors point into tools/lexicon/extract_code.py, a parity copy of tools/lib/extract_code.py, so renaming read_defs_at or extract_text in the canonical file would kill the whole report. drift_report.py:3596-3600 then turns rc!=0 into one DEAD PROBE for the entire signal, and its stderr line does name the key. No gate goes red. The exit-1 behaviour itself is what spec S12 asks for, but the missing HEAD-resolution check is a real gap. The path is narrow and the signal is advisory, so medium. | sound | - | gate:codebase-map coverage + freshness |
| 6 | seams | tools/playbook/adopt-playbook.sh:593 | medium | medium | confirmed | adopt-playbook.sh:584-593 (this diff) adds `code_record.py --selftest` to the `playbook render selftest` leg. That selftest commits .governance/policy.toml fixtures (code_record.py:1248-1251), and read_policy_value (policy_value.py:88-94) spawns tools/policy/policy.py `get --explain` against them. The leg's guard in gate-legs.json lists {prefix}/playbook/, seven memory-tree files, {prefix}/lexicon/, the kit.toml entry and the charter template, but no {prefix}/policy/. This diff did not touch that guard in kit.toml. The sibling `code record` leg added in this diff does guard {prefix}/policy/, but it only runs --check over the live tree, not the selftest's refusal and ctags-value fixtures. So an edit confined to tools/policy/ skips the leg that arms those cases. | sound | held-suite-guard-misses-a-sibling-kit | class:held-suite-guard-misses-a-sibling-kit |
| 7 | seams | tools/run-gates/selftest-budgets.txt:109 | medium | medium | confirmed | This diff adds `code_record.py --selftest` as the last command of tools/playbook/adopt-playbook.sh (lines 585-594). The range did not change tools/run-gates/selftest-budgets.txt: line 109 still reads `playbook render selftest\t60\t\tworst of 8 readings 10s, x1.5`. ceiling-evidence.txt:124 still reads 1.5 from 2026-09-24, and that file's only change in the range is the new `code record` row. The builder's own return contradicts both figures. memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-8-1-builder-return.md:37 says the suite now takes "about 73 s here" and that the evidence row "is stale at 1.5 s". So the selftest already costs more than its 60 s budget row, a cost verdict read by run-selftests.sh. The leg's 300 s hang ceiling still holds, so the effect is contained to the cost budget, its evidence, and which suite gets blamed. | sound | budget-row-not-remeasured-after-added-arms | class:budget-row-not-remeasured-after-added-arms |
| 8 | seams | tools/playbook/code_record.py:968 | medium | - | refuted | The mechanics are as described: check_code_record (code_record.py:955-993) passes read_held_facts into build_derivation, and with no code_tree row it writes and prints `derived and cached`. But that fact reuse is what the spec requires. Spec TOOL-dTotalRecall-8 AC5 makes `a warm run re-parses unchanged blobs` a RED condition and requires a parse count of 1 after one edited file. S8's check is the cached text against a re-resolution over the facts cache. So the check being unable to catch a wrong facts row under an unchanged version key is the specified design, not a defect this diff introduced against its intent. The interpreter case was offered only as an example and is not established: the version key at code_record.py:255-258 hashes code_record.py, extract_code.py, the policy value and the ctags version. Nobody showed that a Python upgrade changes extract output for any blob in this tree. | unsound | - | - |
| 9 | seams | tools/drift-audit/README.md:159 | low | low | confirmed | tools/drift-audit/README.md:159 is unchanged in the range. It still defines the signal only as "a commit touching a path the dossier claims is not an ancestor of the dossier's own last commit" and names only shallow clones and untouched paths as DEAD PROBE. drift_report.py:3577-3600 reads `map_diff.py --stale-dossiers --json`. This diff's map_lib.measure_dossier_staleness grades an anchored dossier by its anchor hashes (`stale = now != then and (scope is None or stale)`), and map_diff.main now returns 1 when HEAD does not define an anchor, which drift_report turns into DEAD PROBE (`gave no answer`). The codebase-map README and map_diff's docstring were updated; the drift-audit README was not. Only documentation is affected. | sound | a-folded-field-leaves-its-row-shape-docs-behind | class:a-folded-field-leaves-its-row-shape-docs-behind |
| 10 | verification | tools/workflows/replay_scorer.py:1471 | medium | medium | confirmed | replay_scorer.py:1469-1473 is new in this range: the base has no `rest or want` refusal. check_map_noise_arm (2305-2330) plants three cases: counts [2,6] and [2,6,1,7] with dispatched alike, one dropped candidate (which the per-case `n != want` refusal catches), and arms[0].dispatched=5 against 4, so sent={4,5} and only `len(sent) > 1` fires. No case has one shared count that the audit count does not divide, and none has want < 2. Spec 123 AC2 (line 294) names 'declares over two audits a count they do not divide', and line 341 says the arm covers AC2. So two of the three disjuncts are never exercised, and cutting them leaves the arm green. The effect stays inside the scorer's refusal path. | sound | liveness-negative-from-another-population | class:refusal-branch-with-no-arm |
| 11 | verification | tools/codebase-map/map_diff.py:394 | medium | medium | confirmed | map_diff.py:389-395 (the `unheld` print and `return 1`) is new: `unheld` does not appear in the base. In selftest.py, md.main() is called only at lines 250 and 259, and the 259 call asserts rc == 2 for a refusal. test_anchored_dossier_staleness stops at line 1624 with `gone["x"][0] == {"a.py::gone": None}` and never calls main, though its docstring (1573-1574) says main turns that None into exit 1. Grepping for 'does not define' finds only the docstring, the README, the print and the test docstring, never an assertion. Deleting `return 1` would let every arm stay green. | sound | - | class:refusal-branch-with-no-arm |
| 12 | verification | tools/playbook/code_record.py:968 | medium | - | refuted | The red branch is reachable outside the selftest. check_code_record (code_record.py:955-992) reads the HEAD tree's code_tree row and re-derives with the current working-tree code_record.py and extract_code.py. read_held_facts reuses only per-blob facts keyed by (blob, lang, version); the cross-file assembly and rendering run fresh. So once a row exists for HEAD's tree, for example from an earlier gate run at the same commit, an uncommitted edit to the assembly or render code that does not bump the version makes row[0] != d['text'], and the leg prints RED and exits 1 at line 984. That is the drift the leg exists to catch. The finding's central claim, that only the hand-corrupted row can make it red, is false. Spec S8 asks for what the code does: re-derive, compare the bytes to the cached text, red on any difference. Reusing held facts is the incremental design. | unsound | liveness-negative-from-another-population | - |
| 13 | verification | tools/workflows/replay_scorer.py:1378 | low | low | confirmed | There is no `15.46` anywhere under tools/ or skills/ in .py or .sh files. check_map_verdict_arm (replay_scorer.py:2233) only exercises derive_map_verdict boundary sets, yet spec §7 says map-verdict covers AC3, and AC3's last sentence pins measure_rise_noise over the first record's six pairs at 15.46. That clause has no check behind it. measure_rise_noise is new in this range: it does not exist at base. The finding overstates its impact, though. check_map_noise_arm (2305) pins `noise 5.65685` and `4.16333`, so changing NOISE_FACTOR or how the variance is pooled would already turn map-noise red. What stays unjoined is only the first experiment's figure against its recorded pairs. That gap is contained to a record figure, so low. | sound | - | class:rule-stated-with-no-check-that-fails |
| 14 | intent | memory/builds/dTotalRecall/build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-verdict.md:82 | low | low | confirmed | Spec 123 says in §4 'The routes' that the record carries 'the second experiment's own variances', and §5 observability says 'the record carries the variances'. The record's 'The terms' section has the per-run counts, noise 7.0993 and the verdict, and grepping it for varian or standard finds nothing. I recomputed with statistics.variance over the listed counts. Without gives [5.3, 1.5, 2.8], sum 9.6. With gives [42, 6.7, 4.7], sum 53.4. 2*sqrt(63/5) = 7.0993, which matches the printed noise. The record was written in this range. The verdict is unaffected, so this is a documentation gap against the spec: low. | sound | - | new:record-omits-a-figure-its-spec-names |
