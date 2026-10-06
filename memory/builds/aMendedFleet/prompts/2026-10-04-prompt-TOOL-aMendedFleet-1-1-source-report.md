# Source report — the final two-wave review (aMendedFleet)

**Serves:** journal TOOL-aMendedFleet-1

Quoted below this preamble, its title demoted one heading level, from the session scratchpad file `FINAL-report.md`, the
report the run mandate names. `[A#n]` cites the wave-1 synthesis beside this record; `[B#n]` cites
wave-2 findings whose lens reports were not copied.

---
>
> ## coding-governance: final review report
>
> Reviewed at `ac65de998` (main tip) on 2026-10-04. Read-only. This report merges two waves of review.
>
> - **Wave 1** produced 63 verified findings, cited `[A#n]`: 26 confirmed and 37 partially confirmed. Its synthesis is `A-synthesis.md`.
> - **Wave 2** produced 47 verified findings, cited `[B#n]`: 14 confirmed, 32 partially confirmed and 1 refuted ([B#16]). The lens reports are `B-integration.md`, `B-orchestration.md`, `B-quality-outcomes.md`, `B-context-economy.md` and `B-state-of-the-art.md`.
>
> Where a finding was only partially confirmed, this report uses the verifier's corrected claim. Every figure came from a command a reviewer or verifier ran. I re-ran six checks today, and the results agree with the findings:
>
> - Remote CI: 15 runs between 2026-09-29 and 2026-10-04, 10 push and 5 scheduled, and all 15 failed.
> - `grep write_ask_views tools/unattended/unattended.sh` returns nothing, so main still lacks the dropped code.
> - `TOOL-dUnstuckLanding-17` and `-25` are CLOSED, and `-26` is filed HIGH, all on `origin/branch/unattended-build-closing-f90fd9`, which is 35 commits ahead of `origin/main`.
> - The aBlindedTrial scratch root holds 0 files in 3,950 directories.
> - `AGENTS.md` is 64,344 B and 586 lines. The unattended Skill is 88,481 B.
> - All the asks named below are OPEN. None of the new proposals is already filed: a grep for `omitClaudeMd`, `escape ratio`, `szz`, `prompt-audit` and `project_doc_max_bytes` across the repo returns nothing.
>
> ---
>
> ## Read this first
>
> **The most severe item is live data loss on main.** Merge `01c22e155` (10-01) resolved a conflict by taking one side, and in doing so dropped `TOOL-dMendedRecall-2` and `-3`, two CLOSED units from node d. Main still lacks that code. The restore (`TOOL-dUnstuckLanding-25`) and the gate that would have caught the loss (`TOOL-dUnstuckLanding-26`, HIGH) both exist only on node d's unlanded branch [B#11].
>
> **Decisions needed from you:**
>
> 1. **Land node d's built fixes.** Land `TOOL-dUnstuckLanding-25` and `-17`, and decide where `-26` runs [B#11] [B#14].
> 2. **Choose one by-design source.** Make aGraftedHelix-3's gated invariants the only by-design source, and drop the by-design half of [A#42] before either is built [B#2].
> 3. **Two one-time acts on node a.** Run `claude update`, because the PATH CLI is 2.1.178. Register `gov-resume-tick` [B#40] [B#13].
> 4. **Later: whether to reverse owner ruling D11-c**, which keeps landing as a direct push, so that a remote ruleset can bind unattended landings [B#41].
>
> ---
>
> ## Q1. How the project converges, and whether its tooling does its job
>
> ### Verdict
>
> **Units converge; the system does not.** A unit closes fast and its record tells the truth about what shipped. The repo as a whole does not converge toward green, triaged and current. Signals that would show this already exist, and nothing consumes them ([A] theme A).
>
> **Wave 2 adds three gaps that wave 1 could not see from inside one run.**
>
> - **Runs are blind to each other until they land.** That blindness has already cost shipped work [B#10] [B#11].
> - **Nobody knows whether the code gets better.** It is now measurable with one script [B#18].
> - **Context is the binding cost.** It is spent mostly on the governance itself [B#28] [B#29] [B#30].
>
> **Each kit does its local job and feeds almost nothing into the stages that would use it.**
>
> - When a build began, the existing CLIs printed about 80 ids. The build later cited 3 to 5 of them [B#3].
> - The open asks that target the very files a build edits reach no stage at all [B#1].
>
> ### The numbers that matter
>
> | # | Figure | Source |
> |---|---|---|
> | 1 | 785 of 850 specs are CLOSED. Closed builds take a median of 1.5 days from open to last real touch (p90 9.1 days). | [A#15] [A#3] |
> | 2 | Remote CI failed 15 of 15 runs since 09-29 (re-checked today). 63 of 124 legs are held off the push bar. | [A#1] [A#2] |
> | 3 | 452 of 457 live asks carry no severity. About 15 of the 22 rows in LIVE.md have had no build-folder commit for 29 days or more. | [A#8] [A#3] |
> | 4 | 80 of 191 merges since 09-01 had real textual conflicts. A definition-level replay flags 3 merges in 34 days as dropping code: 1 confirmed loss, 1 documented rebuild and 1 unverified. | [B#11] |
> | 5 | A full bar (no self-tests) took 188 to 561 s on 09-21 to 09-24, and 1,254 to 2,158 s on 10-02 to 10-04. 19 of 50 recorded bars were RED. | [B#14] [B#24] |
> | 6 | Escape ratio: 116 of 297 product fixes (0.39) repaired code that had already reached main. The median escape age is 3.2 days. August to September is flat: 0.38 against 0.41, p = 0.525. | [B#18] |
> | 7 | `AGENTS.md` is 64,344 B and 586 lines, about 3× Anthropic's 200-line guidance. It loads into every session and into each of the 2,239 workflow agents run since 09-04. | [B#28] [B#29] |
> | 8 | An unattended start owes about 239 KB of whole-file reads before any code. The unattended contract went from 61,440 B in one file on 09-01 to 135,207 B in four files. | [B#30] [B#31] |
> | 9 | Production code grew from 2.78 MB to 7.10 MB in 33 days. 51.2% of its bytes are comments or docstrings. | [B#32] |
> | 10 | Of the ids each tool printed at a build's base, the build later cited 3 of 35 and 5 of 35 from recall, 0 of 36 and 0 of 32 from reuse, and 0 of 10 from the map. This is a citation proxy, not a relevance label. | [B#3] |
> | 11 | 58 and 37 live asks targeted files that aWindowedPass and aSightedSkeptic edited. The builds cited 0 and 1 of them. | [B#1] |
> | 12 | The out-of-process resume tick is not registered on node a. One run sat 13.3 h with no driver call. | [B#13] |
>
> ### What is working and must be kept
>
> - **Enforcement at the tool call through hooks.** agent-cap, scratch-guard, gate-guard and stop-guard fire in sidechains and under skip-permissions. This makes a prose diet safe. Their effect is unmeasured: the guard hooks log no denials [B#36] [B#47].
> - **The evidence-to-rule loop of aBlindedTrial.** A blinded, frozen, permutation-tested trial changed a rule, and practice followed: spec-audit records fell from 140 to 6. Keep the habit, and fix where its instrument lives [B#20] [B#46] [B#19].
> - **Committed, pre-declared keys at every stage.** These are:
>   - the `--dispatch` write sets, 576 rows with a median of 7 paths, enforced at commit;
>   - the spec "Files touched" section, present in 136 of 137 recent specs;
>   - the spec §10 probes, present in 580 of 850 specs.
>
>   Every integration below joins over these [B#9] [B#17].
> - **Slug-scoped ids.** No cross-slug collision has occurred across 4 nodes [A#11].
> - **Drift-audit's honesty about its own probes.** It prints DEAD PROBE rather than a reassuring 0 [A#62].
>
> ---
>
> ## Q2(a). Per-kit improvements, ranked
>
> Each list is ranked by value over effort. "Filed" names the ask that already covers an item; doing that item means executing a stalled ask, not filing a new one.
>
> ### memory-tree
>
> | Rank | Change | Value / effort | Ids | Filed |
> |---|---|---|---|---|
> | 1 | **Make the asks feed usable.** Each `gen_build_index --asks` row gains three things: the `pointer` that `backlog.py:296` already parses, a summary cut to 160 B, and a `--path` filter. Rank by severity, then recency, and cap the result: 26 of the 58 hits target `unattended.sh` or `govkit.py`. Point `REVIEW-PROTOCOL.md:188-190` and `tier2-review.js:480` at the filtered call. | high / S | [B#1] | no |
> | 2 | **LIVE.md gets a last-touch column, a dormant split and a LANDED-UNCLOSED render.** Compute them in one `git log` pass, and reuse drift's existing join of spec ids to product commits. | high / S | [A#3] [A#13] [A#59] | no |
> | 3 | **Bulk triage with generated dispositions.** Auto-DEFER aged unlabelled asks and evidence-free KEEP rows. Dispose of the fixed-but-OPEN asks this review found: `TOOL-aUnblockedFleet-7` is fixed by dUnstalledConvoy-38, and `-8` by dDerivedDocket-27 for profiled repos. | high / S | [A#8] [A#59] [B#16] [B#21] | partly |
> | 4 | **Make the gotchas output precise, and record what it catches.** Rank classes by anchor specificity and cut in tiers. Add a `classes` column to tier2's committed appendix now, so hit counts accrue: today 37 of 98 finder findings carry a C\<n\> label and 0 survive into committed records. Retire zero-hit classes once the counts exist. | high / S | [A#21] [B#4] | no |
> | 5 | **`--doctor <slug>` plus a `--new-spec` skeleton, and a cutoff budget.** A new `*_CUTOFF` must retire an old one. | medium-high / M | [A#23] [A#16] | no |
> | 6 | **Merge-neutral generated views.** Use `merge=ours` on LIVE.md, `ledger/*` and `gotchas/INDEX.md`. | medium / S | [A#14] | no |
>
> ### memory-recall
>
> | Rank | Change | Value / effort | Ids | Filed |
> |---|---|---|---|---|
> | 1 | **Exclude archived versioned snapshots of live docs from the corpus.** One glob or one conf key. | high / S | [A#27] | no |
> | 2 | **Build aTunedCompass unit 9, so the floor grades the path the CLI actually serves** (terms plus fusion). Close `TOOL-aWeighedCompass-16` as a duplicate of `TOOL-aProbedToolkit-10`. | high / M | [A#26] | yes, BLOCKED since 09-05 |
> | 3 | **Grow the gold set from the committed spec §10 probes.** There are 111 candidate questions, and each node writes them in its own vocabulary. Label each with the foreign ids its build later cited. First drop the ids the probe itself returned: 164 of 458 cited ids sit in §10, and 78 sit only there. Hand-check the labels and report hit@10 only. | high / S-M | [A#30] [B#5] | no |
> | 4 | **Label supersession through a one-off aGraftedHelix unit-4 backfill**, keyed by (path, line). Never demote a superseded record. | high / S | [A#28] | in flight |
> | 5 | **Trim output adaptively.** Do not ship a hard top-5 cut: weak-term answers sit at ranks 9, 19 and 35. | medium / S | [A#29] | no |
> | 6 | **Drop `query.py --for-paths`.** The structured asks join (memory-tree item 1) answers that question better than BM25 does. | removes work | [A#35] [B#1] | — |
>
> ### codebase-map
>
> | Rank | Change | Value / effort | Ids | Filed |
> |---|---|---|---|---|
> | 1 | **Wire the lexicon's shell parser into the symbol tier.** Unreachable phrases go from 102 to 35, and any-hit from 0.672 to 0.851. | high / S-M | [A#38] | `TOOL-aWeighedCompass-8`, OPEN since 09-04 |
> | 2 | **Add a byte budget** with a "cut N, rerun with `--budget 0`" line, and grade the default at hit@budget. | high / S | [A#40] | `TOOL-aProbedToolkit-9`, OPEN since 09-03 |
> | 3 | **Derive dossier freshness, as one signal.** Compare a dossier's last commit with the newest commit on its globs. Print it at the close for BASE..HEAD as "touched, not refreshed", report-only: 23 of 84 feature touches refreshed their dossier. | high / S-M | [A#41] [B#7] | no |
> | 4 | **Delete `map_diff --converge`, its sink and the "closing loop" prescriptions.** The prescriptions are in `README.md:37`, `WIRE-INTO-PROJECT.md:495` and `reuse-lookup.agent.md:62`. The sink was last written 09-13, and all 19 of its rows are collisions. | removes code / S | [B#7] | no |
> | 5 | **Inventory the steering surface.** Add a harness-hooks inventory. Restrict `git-hooks` to real hook names. | medium / S | [A#43] [A#44] | `TOOL-aProbedToolkit-15` and `-8` |
> | 6 | **Drop the by-design half of `map_diff --by-design`.** Dossiers claim invariants by id instead of restating them. | removes work | [A#42] [B#2] | — |
>
> ### drift-audit
>
> | Rank | Change | Value / effort | Ids | Filed |
> |---|---|---|---|---|
> | 1 | **Apply D12-i2 in `run_records_nonterminal_but_merged`, which takes it from 12 hits to 2. Lower `lexicon_verbs_declared_but_unused` from pin 3 to 0.** | high / S | [A#51] [A#52] | `TOOL-aReapedTicket-5` |
> | 2 | **Add `remote_ci_red_streak`, and fix the three CI legs.** The legs are the cp1252 codec in `matrix.py`, the `__pycache__` fixture leak, and `eol=lf` on the lexicon templates. | high / S | [A#1] | no |
> | 3 | **Add a history TSV appended by the records leg.** The kickoff card reads its last row, which costs 0 s; a fresh drift run costs about 32 s. The close prints the BASE..HEAD delta. | high / S | [A#55] [A#60] | no |
> | 4 | **Add an escape-ratio report outside the seconds tier, run monthly or on demand.** Requirements: classify by landing, filter version and stamp lines, and print n, a 95% interval and the DIRECT share. Never claim an effect from a single-repo before/after. Keep it off the card: at about 150 fixes a month the interval is about ±0.08. | high / S | [B#18] [B#26] | no |
> | 5 | **Retire or demote report-only signals over pin that nobody acts on.** Add a rule for signals that read DEAD for N readings. Restrict `readme_mechanism_drift` to LIVE builds. | medium / S | [A#54] [A#62] [A#61] | no |
> | 6 | **Report gate yield per leg as a mode over `runlog.py journal --producer gates`, sharing one parser with retry grouping.** In 50 bars, 41 of the 61 always-run legs never went red. | low-medium / S | [B#24] [A#53] | no |
>
> ---
>
> ## Q2(b). Cross-integration architecture
>
> ### Four principles
>
> 1. **One key per stage, and the key is a committed path set.** Every stage already holds one before it acts: the entrypoints at kickoff, "Files touched" at spec, the `--dispatch` write set at a build pass, and BASE..HEAD at review and close [B#9] [B#17].
> 2. **Only committed data may rank or gate.** Node-local telemetry (`review-lenses/`, `recall/`, `orientation/`, `runlog/`) may report, never rank. Two nodes at one sha then get the same context ([A] theme H) [B#9].
> 3. **Existing commands, spelled once.** `gotchas.py --for-paths|--for-diff` and `gen_build_index.py --asks --path` stay two commands, written once in BUILD-METHOD. SKILL Step 4 and the workflow prompts point there.
>    - **Why not a single carrier.** Folding the asks into `gotchas.py` would couple the class catalogue to the backlog fold, at 2.6 s against 0.25 s. It would also add a second block for `tier2-review` to cut out [B#3].
>    - **Why it matters.** SKILL is at 18,407 of 18,432 bytes, so collapsing Step 4 is also what makes room for anything new [B#3].
> 4. **Everything at the close is report-only.** It is a disposition list routed into existing sinks, the close summary and the backlog, never a new gate ([A] theme A).
>
> ### What each stage should receive
>
> | Stage | Key | Today | Proposed |
> |---|---|---|---|
> | Session card | none | Node, tree, LIVE count and 5 recent subjects. | Add one line from the last drift-history row [A#55] [A#60]. Add one overlap line built from unmerged remote refs [B#10]. Add a NOTE when the PATH CLI is older than the running session [B#40]. |
> | Kickoff / DoR | pointer-map entrypoints | Three prose paragraphs: a dossier read by hand, `gotchas --for-paths`, and a recall query. | `gotchas --for-paths` and `asks --path` over the same entrypoints. Recall stays keyed by question. Step 4 becomes a pointer [B#3] [B#1]. |
> | Spec | "Files touched" | `reuse_lookup` and recall, recorded in §10. | Unchanged, plus an overlap check of "Files touched" against unlanded remote refs [B#10]. The §10 lines become recall's gold set [B#5]. |
> | Build pass | `--dispatch` write set | The checklist runs on HEAD~1..HEAD after the commit. | Unchanged until ranking exists. Then the driver hands the unit a budgeted top-N for its dispatch set. Run one build first to measure whether it cuts checklist-fix commits [B#6] [A#21]. |
> | Review (tier2) | BASE..HEAD at an immutable sha | 48 of 94 classes for a mid-size diff. `byDesign` is usually "none supplied". The asks feed is unusable. | A ranked, budgeted checklist. `byDesign` comes from aGraftedHelix-3's invariants. `asks --path` covers the diff's paths. The appendix keeps the classes. One machine shape line carries severities and output tokens [B#1] [B#2] [B#4] [B#23]. |
> | Close and land | BASE..HEAD, plus the merge parents | The Definition of Done proves a map probe ran. The lander runs the bar. | A report-only block listing three things: touched-file open asks for disposition, dossiers touched but not refreshed, and the drift delta. `--close` renders the runlog record itself. `push-main --prepare` runs a definition-level both-parents check [B#1] [B#7] [A#60] [B#15] [B#11]. |
> | Unattended preflight and resume | slug plus declared writes | A local-only single-live check. The tick is reported at INFO. | The overlap probe runs at preflight. The tick check becomes loud. The launching CLI version is recorded, and the resume path compares against it. The history legs run in RANGE mode [B#10] [B#13] [B#40] [B#14]. |
>
> ### Feedback loops
>
> Each loop is a join over data that already exists. None needs a new store.
>
> | Loop | Committed data joined | Where it closes | State today |
> |---|---|---|---|
> | Review → gotcha (left-shift) | Review finding to a new class | the catalogue | **Working.** 7 builds added 5 classes [B#9]. |
> | Findings → class ranking and retirement | appendix `classes` column × the catalogue | gotchas ordering and zero-hit retirement | **Broken.** The label is dropped at `tier2-review.js:1064-1070` [B#4]. |
> | Asks ↔ edits | BACKLOG `→ path` × BASE..HEAD | close disposition, then triage | **Missing.** 37 to 58 asks per build are never surfaced [B#1]. |
> | Invariants → reviewers | gated invariant records × review refutations | skeptic precision | **In flight** (aGraftedHelix-3) [B#2]. |
> | Edits → map freshness | dossier last commit × glob commits × BASE..HEAD | close list, then dossier refresh | **Missing.** 27% of touches refresh their dossier [B#7] [A#41]. |
> | Spec probes → recall grade | §10 question and terms × later-cited ids | recall bench | **Missing.** 111 probes are unread [B#5]. |
> | Fixes → outcome | fix commits × blame × first-parent landings | monthly report, then rule changes | **Missing** [B#18]. |
> | Runs → fleet record | the runlog record committed at close | a glob across nodes | **Skipped.** 6 of 9 runs since 09-14 have no record [B#15]. |
> | Review cost → §8 re-audit | machine shape line × `diff --shortstat` | lens and agent counts | **Missing.** No record carries cost [B#23]. |
> | Human labels → skeptics | about 30 owner labels × `review_replay.py` | lens retune | **Never done** [B#44]. |
>
> ---
>
> ## Q3. What the project lacks against its primary goal
>
> The primary goal is that many nodes, running unattended, produce better code. Ranked by value toward that goal:
>
> | Rank | Gap | Value | Effort | What it replaces or removes | Evidence |
> |---|---|---|---|---|---|
> | 1 | **Main can lose shipped work in a reconcile, and no push-binding check notices.** Execute `TOOL-dUnstuckLanding-26` as a definition-level check: names a parent added that vanish from the merge. When it fires, require a `superseded: <name> -> <successor>` line. Land the `-25` restore. | high | S | Mechanizes the prose rule at `AGENTS.md:133`. A line-level version would have demanded a 368-line list for one documented rewrite. | [B#11] |
> | 2 | **No clean-machine green.** Fix the three CI legs. Route the scheduled held-job reds into the existing HIGH auto-file. | high | S | Nothing new. It is the prerequisite for any remote control. | [A#1] [A#2] |
> | 3 | **Runs are blind to each other until they land.** Add an overlap probe over unmerged remote refs that joins "Files touched" with the diff. Ignore version-marker-only edits, age out abandoned refs, and announce rather than refuse. | high | S | It widens the local-only `check_single_live` and extends aGraftedHelix-2's card. A slug-keyed claim cannot see two slugs on one subject. | [B#10] [A#9] |
> | 4 | **No outcome reading.** Add the monthly escape ratio, and a review shape line carrying severity and cost. | high | S | It supersedes wave 1's "aggregate runlog" idea, because runlog sees only unattended runs. | [B#18] [B#23] [A#10] |
> | 5 | **Context is the binding cost.** The parts:<br>• an `omitClaudeMd` worker type for read-only review and drift agents, about 25K tokens each at the measured ratio;<br>• a trim of the repo wrapper in `AGENTS.md`;<br>• the unattended Skill cut to a router;<br>• a Codex size warning. | high | S-M | Removes the 88.5 KB paraphrase of the protocol, a duplicate node registry and repeated catalogs. Closes `TOOL-aScouredKit-23`. | [B#28] [B#29] [B#30] [B#38] [B#39] |
> | 6 | **The unattended harness and its authority are unpinned.** Record the CLI version at preflight and compare it on resume. Register the tick. Switch to `--permission-mode auto` once the CLI is at least 2.1.281. | high | S, then L | Replaces the INFO-level tick line and bypass mode on a bare Windows host. | [B#40] [B#13] [B#41] |
> | 7 | **No experiment discipline and no standing eval.** Commit instruments to the build folder. Run the vague-brief P-versus-S arm that decides §1's spec. Later, build an eval from history whose briefs come from owner prompts. | high | M-L | May shrink the §1 Tier-2 spec, which is 19 KB at the median, to a 3.2 KB plan: the trial measured the plan at 1.1× the cost of building directly, against 12.3× for the full spec route. | [B#19] [B#43] [B#20] |
> | 8 | **Review precision has never been checked against a human.** | medium | S (one owner hour) | May let a lens or verify agents be cut. | [B#44] |
> | 9 | **History legs set the bar's floor.** Land `-17` RANGE mode, which is already built. | medium-high | S | Stops closing bars from re-grading immutable history. | [B#14] |
> | 10 | **Version-minting churn.** Write the carriers with `--fix`, then mint versions at the lander. | medium | M | Removes version-only conflict hunks (71 of 146 in `5cb052dab`), re-bump commits and a per-spec obligation. | [B#12] [A#5] |
> | 11 | **Adopters get no test-adequacy guidance.** Add the AC id(s) to the existing `New arm:` grammar. Defer mutation work, and when it comes, limit it to legs under 60 s. | low-medium | S | Nothing. One grammar token. | [B#27] [B#45] |
>
> ---
>
> ## Roadmap
>
> There are 25 items. "Owner" marks a step that needs you. Everything else an agent can do.
>
> ### Now: cheap, mostly executing filed or already-built work
>
> 1. Fix the three CI legs, and add `remote_ci_red_streak` [A#1].
> 2. Land node d's `TOOL-dUnstuckLanding-25` (the restore) and `-17` (RANGE mode). Execute `-26` as a definition-level check in `push-main --prepare` and pre-push. **Owner** [B#11] [B#14].
> 3. On node a, run `claude update` and register `gov-resume-tick`. **Owner** [B#40] [B#13].
> 4. Correct the agent-instructions kit:
>    - Next to the byte count `adopt-agent-instructions.sh:138` already prints, announce when the file exceeds 32,768 B.
>    - Fix the "nothing extra" row at `README.md:19`.
>    - Stamp both environment claims.
>    - Fix the stale reason at `AGENTS.md:14`.
>
>    [B#38] [B#35]
> 5. Record on aGraftedHelix that its invariants are the one by-design source. **Owner** [B#2].
> 6. Make the asks feed usable with `pointer`, the summary and `--path`, and repoint the two carriers [B#1].
> 7. Run the bulk backlog triage:
>    - Dispose of `TOOL-aUnblockedFleet-7` and `-8`.
>    - Close `TOOL-aReplayedCard-9` WONTDO, unless the tokens-to-READY baseline (median +66.7K tokens and 6.7 min over 23 sessions) shows orientation is worth a matrix.
>
>    [A#8] [A#59] [B#16] [B#21] [B#34]
> 8. In `tier2-review`, add the appendix `classes` column, and one byte-stable shape line with severity counts and output-token spend [B#4] [B#23].
> 9. Adopt one rule: an experiment's instrument and its result rows are committed to its build folder, never left under `%TEMP%`. Then file the vague-brief arm as a HIGH ask that gates §1 [B#19] [B#22].
> 10. Execute the stalled kit asks:
>     - drift: D12-i2 and the pin change;
>     - recall: the snapshot exclusion;
>     - map: shell symbols and the reuse budget.
>
>     [A#51] [A#52] [A#27] [A#38] [A#40]
>
> ### Next
>
> 11. LIVE.md: the last-touch column, the dormant split and LANDED-UNCLOSED [A#3] [A#13] [A#59].
> 12. The drift history TSV, the card line that reads its last row, and the close delta [A#55] [A#60].
> 13. The cross-run overlap probe at `--preflight` and on the card, folded into [A#9]'s interim step [B#10].
> 14. A `gov-worker` agent type with `omitClaudeMd`, for tier2 and drift finders and skeptics only.
>     - Restart the session once after committing it.
>     - A/B one tier2 run on precision and first-turn tokens, using a tokens-to-READY report mode over runlog's extractor.
>
>     [B#29] [B#34]
> 15. The first step of the charter diet:
>     - Trim the `AGENTS.md` wrapper.
>     - Move the 8,587 B merge-bar slot into a guide.
>     - Run `/doctor prompt-audit`.
>     - Port the Skill-only ordering into the protocol, then cut the unattended Skill to a router of 10 KB or less.
>
>     [B#28] [B#39] [B#30]
> 16. The version carrier `--fix` (`TOOL-aBoundedVerdict-29`, `DEPL-aHoistedPass-10`). Then mint versions in `push-main --prepare`, and delete the per-branch bump obligation [A#5] [B#12].
> 17. The close-time report-only block: touched-file asks, stale dossiers, and the runlog record rendered by `--close`/`--abort` [B#1] [B#7] [A#41] [B#15].
> 18. The monthly escape-ratio report in drift-audit [B#18] [B#26].
> 19. One owner-labelled calibration of about 30 review findings, scored through `review_replay.py`. **Owner** [B#44].
> 20. Gotchas ranking and its tiered budget. Delete `map_diff --converge` [A#21] [B#7].
>
> ### Later
>
> 21. Unattended authority. Switch to `--permission-mode auto` once the CLI is at least 2.1.281. Stage 2 is a non-admin run credential plus a GitHub ruleset; it needs green CI and a reversal of D11-c. **Owner** [B#41] [A#1].
> 22. Recall quality: aTunedCompass unit 9, and the gold set grown from de-contaminated §10 probes [A#26] [A#30] [B#5].
> 23. Run the vague-brief trial. Then build a standing eval from history, briefed from owner prompts, with a measure that cannot saturate [B#19] [B#43].
> 24. A `/goal` spike in an interactive session. If it holds, delete the idle-wake schedule and register/release-task, and keep resume-tick and stop-guard [B#42].
> 25. Path-scoped rules for editing areas, and a budgeted pre-build checklist in unit prompts. Do this only after items 14, 15 and 20 have been measured [B#39] [B#37] [B#6].
>
> ---
>
> ## Do not build
>
> - **A second by-design pipeline** (`map_diff --by-design` feeding `byDesign`) [A#42] [B#2].
> - **`query.py --for-paths`** [A#35]. The structured asks filter replaces it [B#1].
> - **Folding the asks into `gotchas.py` as a block**, or a new single context carrier [B#3].
> - **A line-level merge-drop check that demands superseded-line lists** [B#11].
> - **An overlap probe on every `--dispatch`** [B#10]. Remote refs are not refetched per pass.
> - **A per-build memo store for the history legs** [B#14]. RANGE mode already stops the re-grading.
> - **A comment-share gate.** It conflicts with the recorded ANNOTATION-STYLE A1-A2 ruling [B#32].
> - **Per-kit byte caps on code** [B#31].
> - **Retiring the per-file guide caps in favour of a per-activity token figure** [B#31]. Keep the caps, and add a review rule that a split is accepted only if the parent names when to read the new file.
> - **A per-leg `break` fixture field and runner** [B#25]. The held self-tests already stage breaks; make the daily held job green instead.
> - **Retiring declarations legs because their reds are "self-referential"** [B#33]. Execute `TOOL-aDeferredBar-13` instead.
> - **Path-scoping rules tied to running commands**, such as the merge bar, or a line-count cap on the charter [B#39].
> - **An authored `CLAUDE_CLI_FLOOR` constant** [B#40]. Derive the version from the launching session instead.
> - **Refusing preflight when the tick is not registered** [B#13]. Announce it.
> - **Executing `TOOL-aUnblockedFleet-7` and `-8`** [B#16]. Both are fixed in code.
> - **An escape-ratio line on the kickoff card** [B#18].
> - **A periodic adherence sampler that auto-files violations** [B#22]. Re-grade the three concentrated units once, with a skeptic, before anything else.
> - **A general experiment framework before a second experiment exists**, or coverage and mutation kits before an outcome reading justifies them [B#19] [B#27].
> - **A new §7 traceability line** [B#27]. It duplicates `New arm:`.
> - **A central merge queue, a fleet dashboard or an automatic work picker** (orchestration lens).
> - **Wave 1's "do not build" lists stand** ([A] §2).
>
> ## What to delete or demote
>
> 1. **`map_diff --converge`, its sink and its three "closing loop" prescriptions** [B#7].
> 2. **The 164 to 312 KB `--asks --json` instruction** in `REVIEW-PROTOCOL.md:188-190` and `tier2-review.js:480` [B#1].
> 3. **The unattended Skill's paraphrase.** Cut it from 88,481 B to a router [B#30].
> 4. **From the `AGENTS.md` wrapper:** the second node registry (`:154-156` disagrees with `:62-67`), the repeated command catalog, and the dated measurement history in the merge-bar section [B#28] [B#39].
> 5. **Present-tense counts in code comments**, for example `unattended.sh:4017` and `:4023`, in one ANNOTATION-STYLE A4 sweep [B#32].
> 6. **Stale OPEN asks:** `TOOL-aUnblockedFleet-7` and `-8`, and `TOOL-aReplayedCard-9` [B#16] [B#21].
> 7. **The dead `.git/gate-timings.tsv`**, last written 08-20 and superseded by the ledger [B#14].
> 8. **Report-only drift signals over pin that nobody acts on, and probes DEAD for N readings** [A#54] [A#62].
> 9. **Once replaced:**
>    - the per-spec version-bump obligation [B#12];
>    - the Skill's "Record the run" paragraph [B#15];
>    - the idle-wake and register-task machinery, if the `/goal` spike holds [B#42].
>
> ---
>
> ## What wave 2 claimed and verification cut back
>
> - [B#16] is refuted. The same-clone lander-marker and turnstile races are mitigated in code, by dUnstalledConvoy-38 and dDerivedDocket-27.
> - [B#3] The "about 53 KB pack" sums tools that no single stage receives together. The 8 to 10 KB pack size is an unmeasured estimate.
> - [B#5] About a third of the "later-cited" ids in spec §10 come from the probe's own output. The set is usable only after those are removed.
> - [B#6] The pre-build checklist is 76 to 94% of the post-commit list. 7 of the 9 checklist-fix commits come from one build.
> - [B#7] `--converge` having no caller is documented, by design.
> - [B#10] The aGraftedHelix overlaps are spec estimates only. Several of the named shared files overlap only in version-marker lines.
> - [B#11] Line-level loss counts overstate. A definition-level replay flags 3 merges, not 9.
> - [B#12] Main never published a duplicate version: 149 first-parent values, 0 repeats. The harm is churn.
> - [B#13] 4 of the 5 "manual" resumes were releases of HELD runs, which the tick skips by design.
> - [B#14] The "stale timing cache" claim is wrong: the scheduler reads the ledger.
> - [B#15] The run record has been a mandated Skill step since 09-14. Runs skip it.
> - [B#18] Adopters land mostly by direct commit, so the escape ratio is validated on this repo only.
> - [B#22] The 13% adherence figure is one unverified LLM reading.
> - [B#24] Of the 80 "never red" legs, 38 never ran in that series.
> - [B#28] The 31.8% core figure is one reviewer's classification.
> - [B#29] `omitClaudeMd` is safe only for read-only agents, and is unproven through Workflow.
> - [B#31] Per-file caps did bound growth. Only the summed budget failed.
> - [B#32] With a strict marker set, history is 28 to 34% of comment bytes, not 71 to 85%.
> - [B#39] The Vercel result concerns a passive docs index, not rule adherence.
> - [B#41] Stage 1's "deny pushes to main" would disable the kit's own landing. Auto mode needs CLI 2.1.281 or later.
> - [B#42] In `-p` sessions, `/goal` delivers check-ins only at the end of a turn.
> - [B#43] Briefing from the spec would saturate again.
>
> **Corrections to wave 1:**
>
> - The aGraftedHelix-1 CAS claim is pushed, not unpushed [A#9]. It is keyed by slug and carries no paths.
> - [A#42]'s by-design half is superseded by [B#2].
> - [A#35] is superseded by [B#1].
> - [A#60]'s card line must read a persisted row rather than run drift, which takes about 32 s, at SessionStart.
>
> ## Still uncertain
>
> - **The token ratio.** It was measured at 0.395 tokens per byte on task briefs only. At 4 bytes per token, `AGENTS.md` is about 16K tokens rather than 25K. So the monthly saving from item 14 is between 36M and 57M tokens, as an upper bound, because only read-only agents switch.
> - **Whether CLI 2.1.178 omits the stop-guard's `background_tasks` field** [B#40].
> - **Whether any of the 23 "violated" acceptance criteria are real defects** [B#22].
> - **Whether the e2e840d08 loss of `parse_push_class` was deliberate** [B#11].
> - **Whether a pre-build checklist reduces fixup commits** [B#6].
> - **Whether `/goal` covers the silent-background case in practice** [B#42].
