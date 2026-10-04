# Source synthesis — wave 1 of the review (aMendedFleet)

**Serves:** journal TOOL-aMendedFleet-1

Quoted below this preamble, its title demoted one heading level, from the session scratchpad file `A-synthesis.md`, which
the final report beside this record cites as `[A#n]`.

---
>
> ## Synthesis: coding-governance review at `ac65de998` (2026-10-04)
>
> **Inputs.** This synthesis draws on five lens reports in this scratchpad (`A-convergence.md`, `A-memory-tree.md`,
> `A-memory-recall.md`, `A-codebase-map.md`, `A-drift-audit.md`) and 63 adversarially verified findings.
>
> **Finding ids.** `[#n]` is the id of a verified finding. The lens reports number their own findings F1, F2 and so
> on, and those are not used here.
>
> **Verdict tally.** Of the 63 findings, 26 were confirmed and 37 partially confirmed. None was refuted in full and
> none was left uncertain. Where a finding was partially confirmed, this document uses the verifier's corrected
> claim. Several lens headlines did not survive verification; §4 lists every claim that was cut back.
>
> **Number provenance.** Every number below comes from a command run by a lens reviewer or a verifier. When the two
> disagreed, the verifier's figure is used.
>
> ---
>
> ## 1. Question 1: how the project converges, and whether its tooling does its job
>
> ### Overall verdict
>
> Work units converge. The system around them does not. The tooling does its local job: units close fast and the
> records stay honest about what shipped. It does not yet drive the whole repo toward a state that is green, triaged
> and current. Most of the signals that would show that already exist, but nothing consumes them.
>
> **What converges**
>
> - **Units close.** 785 of 850 spec files are CLOSED and 29 are WONTDO [#15]. Closed builds take a median of 1.5
>   days from opening to their last real touch, with p90 at 9.1 days [#3].
> - **Records are honest about product.** 1 of 763 closed specs has no product commit [#12].
> - **Ids do not collide across nodes.** There has been no cross-slug id collision across 4 nodes. Hygiene check 13
>   enforces this [#11].
> - **Merge conflicts on decisions are rare.** `DECISIONS.md` appears in only 4 recorded conflict merges, because
>   of the row driver [#24].
> - **The capped surfaces have stopped growing.** AGENTS.md went from 64,195 to 64,344 bytes since 09-01. The
>   template is 48,193 bytes against a 49,152-byte limit [#12].
> - **Review rounds now stop.** A declared rule (re-arm only on a strictly smaller count, `REVIEW_ROUNDS=1` since
>   09-14) has made round 3 and beyond rare [#4].
>
> **What does not converge**
>
> - **Remote CI has never been green.** It failed all 15 runs since 09-29. Every push run reds the same three legs.
>   The causes depend on the host, not on node a:
>   - `tools/govkit/matrix.py` decodes subprocess output with the cp1252 locale codec.
>   - A fixture leaks `__pycache__`.
>   - The lexicon template is checked out CRLF.
>
>   No record acknowledges the red. `DECISIONS.md:131` still routes an owed compensating check to the failing held
>   job [#1].
> - **The behaviour suites do not bind at push, and some are red.** 63 of 124 legs are held. The 61 that bind at
>   push are mostly declaration and record-shape checks. The scheduled CI run on 10-04 had 15 held suites red; some
>   of those may be environmental [#2].
> - **The backlog is not triaged.**
>   - 749 asks have been filed and 457 are live. 452 of the live asks have no severity [#8].
>   - Severity at filing is enforced only for asks filed on or after 2026-10-01 (V12) [#8].
>   - 54 live asks are cited by product source. In a sample of 5, 2 had already been fixed and were still OPEN. A
>     triage pass wrote KEEP rows on both after their fixes had landed [#59].
> - **LIVE.md lists work that has stopped.** About 15 of its 22 rows have had no build-folder commit in 29 days or
>   more, and 4 of those are DEFERRED by declaration [#3]. 8 rows have had no commit naming their slug since before
>   09-04, and 3 of those are INPROGRESS [#59]. LIVE.md has no last-touch column [#13].
> - **Writing goes mostly to records.**
>   - Records take 66% of the 1,105,738 churned lines [#6].
>   - The ratio of records-only commits to product-touching commits rose from 1.32 in August to 1.46 in September
>     and 1.47 in October [#6]. The records-only bucket includes design work: spec, fold and review commits [#16].
> - **Kit versions are hand-copied.** Each version is copied into up to 27 carrier files per kit. 147 commits
>   (about 4%) only move version markers [#5].
> - **Uncapped code doubles.** In about two weeks, unattended.sh went from 5,339 to 10,576 lines, gen_build_index.py
>   from 2,787 to 5,674, run-gates.sh from 1,917 to 3,425 and govkit.py from 9,005 to 12,741 [#7].
> - **Nobody measures adopter outcomes.** Whether governed code gets better is not measured anywhere, even though
>   adopters exist [#10].
>
> **Is the cost paid back?** It is paid back for unit closure, record integrity and collision-free ids. It is not
> paid back for main-branch health ([#1], [#2]), backlog triage ([#8]) or knowing what is live ([#3]). It is unknown
> for adopter code quality ([#10]).
>
> ### Verdict per kit
>
> | Kit | Verdict | Key numbers |
> |---|---|---|
> | **memory-tree** | **Partly.** The mechanics are sound. The memory is not on point. | **Works:** hygiene green in 49.8 s; `gen_build_index --check` clean in 3.7 s; 4 conflicts on `DECISIONS.md` [#24]; no cross-node id collision [#11]. **Fails:** status in LIVE.md is authored and stale (`aBatchedLintel` shows INPROGRESS although it landed on 08-03) [#13]; about 15 of 22 LIVE rows idle [#3]; 452 of 457 live asks unlabelled [#19]; 22 dated cutoffs and 155 kit-version bumps in under 3 months [#16]; memory/ is 46.7 MB, 88% of it in terminal builds, with no measured harm [#15]. |
> | **memory-recall** | **A good lookup for callers who already know the jargon. Its quality is not graded.** | **With strong terms** (n=16): P@1 0.750, hit@5 1.000, MRR 0.854. **With weak terms:** MRR 0.422, close to the no-terms MRR of 0.397 [#30]. **The floor** grades a records-only, no-terms configuration that the CLI never serves (0.8333). The real served path, terms plus fusion, is ungraded, and its fix has been blocked for a month [#26]. **Stale text:** archived charter snapshots fill alternate ranks for charter questions [#27]. **Output:** about 16 KB, 37 hits per answer [#29]. **Telemetry:** 1 hand-recorded open in 379 queries; 120 of 155 inferred opens are not in the shown list [#32]. **Recent work:** 43 commits since 09-06, none touching ranking [#34]. |
> | **codebase-map** | **Partly.** The ratchet works. The reuse and orientation half does not. | **Ratchet:** gate 3.8 to 3.9 s; baseline 69 to 39 keys, only renames added [#49]. **Replay** (335 phrases): hit@5 0.400, hit@10 0.454, any-hit 0.672, 102 unreachable. Shell is dark, and lexicon's shell parser would lift any-hit to 0.851 [#38]. **No miss signal:** seed coverage has a median of 0.12 for both hits and misses [#39]. **Output** is unbounded at 9 to 49 KB, and the median shortlist grew from 30 to 171 [#40]. **Dossiers:** 3 of 6 sampled carry false prose with no freshness check [#41]. **Workflow use:** tier2 `byDesign` has no caller, and 1 of 29 orientation cards mentions the map [#42]. |
> | **drift-audit** | **An honest instrument whose readings nobody acts on.** | **Honest:** 19 signals; 2 print DEAD PROBE instead of 0 [#62]; the base ref is printed with its sha [#63]. **Imprecise:** `run_records` is right on 2 of 12 hits, because 10 are protocol-derived LANDED [#51]; `readme_mechanism_drift` has 31 of 31 hits on CLOSED specs [#61]; pins are counts, not identities [#52]. **No consequence:** 6 report-only signals over pin and 0 asks cite them [#54]; no history [#55]; not on the kickoff card or at the unattended close; Tier 2 ran once (precision 0.86 and 0.92) and has no trigger [#60]. |
>
> **The push bar and CI.** These are not kits, but they decide whether the tooling as a whole works. A local GREEN
> means the bookkeeping is consistent on node a [#2]. It does not mean the kits behave, and it does not mean a clean
> machine agrees [#1].
>
> ---
>
> ## 2. Per-kit improvement plans
>
> Each plan is ranked by value over effort. Where a backlog ask or build already covers an item, the plan says so,
> because doing that item means executing a stalled ask, not filing a new one. A "Do not build" list follows each
> plan; it holds proposals the verifiers judged wrong, redundant or too costly.
>
> ### 2.1 memory-tree
>
> 1. **Add a last-touch column and a dormant split to LIVE.md** (high value, S) [#3] [#13] [#59].
>    - Compute it in `gen_build_index.py` from ONE `git log --format` pass, excluding sweep commits that touch more
>      than K build folders. Do not spawn one `--grep` per slug, because a git spawn costs about 751 ms on node a.
>    - Render ACTIVE and DORMANT rows against a declared `LIVE_DORMANT_DAYS`.
>    - [#3] and [#13] propose this independently, and drift-audit's [#59] wants the same column. Build it once.
> 2. **Render LANDED-UNCLOSED by reusing drift-audit's existing join of spec ids to product commits** (high, S)
>    [#13]. Drift already reports `non_terminal_specs_cited_by_product_source 2/29` [#13]. The drift lens hand-checked
>    both hits and found them true; no verified finding covers that check. Do not add a new mandatory `Unit:` trailer.
> 3. **Triage the backlog in bulk** (high, S) [#8] [#19] [#59].
>    - Auto-DEFER aged unlabelled asks with a generated disposition row.
>    - Re-arm a shrink-only pin on `backlog_asks_unlabelled`. The old ratchet was blanked at the 09-28 switch-over.
>    - Drop the KEEP rows, which are derivable as "OPEN plus a terminal build".
>    - Collapse `row_grammar`'s 8 "NOT MEASURED" lines into one "retired under builds mode" line.
>    - Do NOT add severity-at-filing. V12 already enforces it.
> 4. **Add a `--doctor <slug|path>` that prints every failing folder rule in one pass, plus a `--new-spec`
>    skeleton that satisfies every active cutoff** (high, M) [#23].
>    - This removes the cost of a new folder surfacing four rules over four bar cycles.
>    - Leave `--new-build`'s mandate semantics alone.
> 5. **Make generated views merge-neutral** (medium, S) [#14].
>    - Use `merge=ours` on LIVE.md, `ledger/*` and `gotchas/INDEX.md`. Check 9 already reds a stale render.
>    - Drop the Status column from month shards, so the "Frozen" claim becomes true. It is false today:
>      `4289f1b40` flipped a row a month later.
>    - Keep `merge=rows` on the backlog views.
>    - Caveat: the conflict data predates the switch-over. Since then, conflicts come mostly from version carriers,
>      which §3 theme E covers.
> 6. **Set a cutoff budget: a new `*_CUTOFF` must retire an old one** (medium, S) [#16]. This targets the 22 dated
>    rule switches directly. Batch format migrations onto kit versions rather than running one sweep each.
> 7. **Set a spec byte ceiling, reusing the template's high-water mechanism** (medium, S) [#4] [#6]. Specs have a
>    median of about 18 KB and no cap. While doing this, move the recurring spec-shape finding classes into
>    `check-spec-tokens.py` or hygiene check 12 [#4].
> 8. **Make the gotchas `--for-diff` output precise** (medium, S) [#21] [#25] [#45].
>    - Rank selected classes by anchor specificity: full path, then directory, then basename.
>    - Put classes that are both anchored and claimed by the touched dossier first.
>    - Use tiered output rather than a hard top-12 cut.
>    - Keep the universals for markdown diffs, because the inline-fence class applies there.
>    - Have check 19 report anchors that select zero paths. 39 of 314 do today.
> 9. **Make two small repairs** (low, S) [#20]. Report dead paths in non-terminal build READMEs as an advisory
>    signal (1 of 43 is dead today). Fix the dead `decisions/` pointer at `DECISIONS.md:5`.
> 10. **Add a `missing:<ID>` citation form with its own count** (low-medium, S) [#18]. This affects only citations
>     of ids that have no record; citing existing ids already works.
>
> **Do not build**
>
> - **Compaction that deletes `reviews/`** [#15]. It conflicts with charter §8's persisted Tier-2 corpus, and no
>   measured harm was shown.
> - **A `record_overhead_ratio` signal** [#16] [#6]. It would count design work as overhead.
> - **A mandatory `Unit:` commit trailer** [#13]. It adds another meta-gate.
> - **A new disposition verb** [#3]. DEFERRED and WONTDO already exist.
> - **"Reconciling" RUN LANDED against build status** [#3] [#13]. These are partial landings, not contradictions.
> - **An authored dossier `verified_at` stamp.** See §2.3.
>
> ### 2.2 memory-recall
>
> 1. **Exclude archived versioned snapshots of live docs from the corpus, and add a gold arm whose answer is a live
>    charter line** (high, S) [#27]. One glob, or a `RECALL_EXCLUDE` conf key, in `corpus_files`. Skip indexing
>    AGENTS.md: it is already in every session through CLAUDE.md.
> 2. **Schedule and build `aTunedCompass` unit 9, which unblocks units 2 and 3** (high, M) [#26] [#34].
>    - Grade the floor by importing `query.run_fusion` with terms, so the floor grades what the CLI serves.
>    - Get headroom from a naive-terms slice. That meets the owner's no-saturating-fixture ruling.
>    - Replace the literal `h=10 R=12` arm with a not-below arm.
>    - Close `TOOL-aWeighedCompass-16` as a duplicate of `TOOL-aProbedToolkit-10`.
>    - The build has been BLOCKED since 2026-09-05.
> 3. **Grow the gold set well beyond 16 questions before any ranking decision** (high, S-M) [#30] [#29] [#31].
>    - At n=16, the MRR deltas measured so far (0.02 to 0.03) are noise.
>    - The weak-term caller is a projection: 378 of 379 logged queries carried terms.
> 4. **Measure "answer used" offline** (medium, M) [#32]. Join each logged query's result ids and worktree to the
>    ids that the worktree's next commit, spec or READY card cites. No hook change is needed, and it supersedes
>    `TOOL-aWeighedCompass-11`. It is also the prerequisite for an alias harvest [#30].
> 5. **Label supersession; never demote it** (high value, S, because the work is in flight) [#28] [#22].
>    - Hand the 18 mined edges to `aGraftedHelix` unit 4 as a one-off backfill. That build was opened today, so it
>      is in flight, not stalled.
>    - Key each edge by (path, line), because 434 ids are anchored more than once.
>    - Partial edges ("for R2+R5", "narrows") are common. Demoting `TOOL-cBriefedPilot-21` would bury its R1/R3/R4
>      verdict.
>    - Demote only rotated backlog snapshots.
> 6. **Trim the output without losing recall** (medium, S) [#29]. Cut each snippet to its decisive line, or set
>    `--k 10` per source, or cut adaptively when the top score is strong. Do NOT ship a hard 5+3 default: weak-term
>    answers sit at ranks 9, 19 and 35, and logged opens have a median rank of 6.
> 7. **Make gotchas, map dossiers and guides first-class front-matter documents, and add an explicit exclusion rule
>    for generated views** (medium, S-M) [#31]. Today generated views escape the records arm only by accident, at
>    `extract.py:181`.
> 8. **Add `query.py --for-paths`, returning OPEN asks plus decisions that cite the touched paths, and point
>    `tier2-review.js`'s prior-art lens at `query.py`** (medium, S-M) [#35]. `gotchas.py --for-paths` already covers
>    gotchas, so extend that seam; do not duplicate it.
> 9. **Fix cache eviction** (low-medium, S) [#33]. Evict caches of deleted worktrees first, and order by last query
>    rather than last build. Keying by the current `corpus_digest` would share nothing: it hashes mtime, so it
>    differs per checkout.
> 10. **Delete the stale typed figures in the README and Skill** (low, S) [#36]. Point at the manifest counts. A
>     `--stats` flag does not exist. Change the Skill's miss advice to "re-query in the record's vocabulary, then
>     grep".
>
> **Do not build (yet)**
>
> - **A model2vec or dense serving arm** [#30]. It breaks the stdlib invariant and would be dark on node a, which
>   has no numpy. Measure it once with `bench.py` first.
> - **Chunk-arm-only-as-fallback** [#31]. It loses the gotcha rescue (strong hit@5 is 1.000 served vs 0.938 for
>   records alone).
> - **A PreToolUse Edit hook** [#35].
> - **Demoting all non-live records** [#22]. CLOSED specs hold most of the rationale.
>
> ### 2.3 codebase-map
>
> 1. **Wire `lexicon.parse_shell_defs` into `SYMBOL_EXTRACTORS` and drop `RECALL_DARK_LAYERS=".sh"`** (high, S-M)
>    [#38].
>    - This is ask `TOOL-aWeighedCompass-8`, OPEN since 2026-09-04. The parser landed one day later and removed its
>      blocker.
>    - Measured effect: unreachable phrases go from 102 to 35, any-hit from 0.672 to 0.851, hit@5 from 0.400 to
>      0.466.
>    - Fix the three stale "shell is dark" texts in the same change.
> 2. **Add a byte budget with a "cut N, rerun with `--budget 0`" line** (high, S) [#40].
>    - This is `TOOL-aProbedToolkit-9`, stalled for 31 days.
>    - Choose the default by grading `replay-phrases.py` at hit@budget. A plain top-30 cut today drops hit rate
>      from 0.672 to 0.540.
> 3. **Add `map_diff --by-design <range>`, byte-capped, that prints the touched dossiers' Constraints and Gaps; feed
>    it to `tier2-review` `byDesign` and to the unattended unit brief** (high, S) [#42]. `byDesign` has no caller
>    today. This is the §8 precision lever: feed reviewers what is by design.
> 4. **Derive dossier freshness instead of stamping it** (high, S-M) [#41].
>    - Compare each dossier's last commit with the newest commit on its `[paths].globs`.
>    - Report the result as an advisory drift signal with a shrink-only pin.
>    - Add a regex lint against typed population counts in dossier prose. This applies §7's own rule to the map.
> 5. **Inventory the steering surface** (medium, S) [#43] [#44].
>    - Add a `harness-hooks` inventory read from `.claude/settings.json`, failing closed.
>    - Restrict `git-hooks` to real hook names; today 3 of its 7 keys are not hooks.
>    - Claim `pre-commit`, `pre-push` and `drift-audit`.
>    - Move the `skill-engines` claim from the unattended dossier to session-kickoff, and glob
>      `skills/session-kickoff/*`.
>    - Execute `TOOL-aProbedToolkit-15` and `TOOL-aProbedToolkit-8` (separate code coverage from record coverage)
>      rather than filing new asks.
> 6. **Give `replay-phrases.py` a self-enforced `--floor`, plus a DoD line that any ranking change runs it**
>    (medium, S) [#50] [#39]. Keep it off the bar, per the owner ruling of 2026-08-23.
> 7. **Count `>>> canonical-copy` markers as install sites in `fan_in`, and add a join from legs to paths** (medium,
>    S) [#46].
>    - The most-installed seam currently shows "fan-in 3".
>    - Give `map_imports.py` a consumer or delete it.
> 8. **Generate a ≤1 KB card per feature from the toml fence, and move measured history out of the dossiers**
>    (medium, S-M) [#47]. Seven dossiers sit within 10% of the 20,480-byte cap.
> 9. **Assert that `baseline.toml` never gains a key against the base ref** (medium, S) [#49]. Today the shrink-only
>    property holds by discipline only.
> 10. **Build a miss signal, but measure its predictor first** (medium, M, *uncertain*) [#39]. Seed coverage is not
>     the predictor: absent capabilities score 0.17 to 0.25, higher than real hits.
>
> **Do not build**
>
> - **A rewrite that ranks on behavioural text** [#39]. With equal coverage, `reuse_lookup` (hit@5 0.400) already
>   matches naive BM25 (0.382). BM25's apparent lead came from shell coverage.
> - **A union of dossier-claimed gotchas into the checklist** [#45]. The checklist already over-selects.
> - **Auto-filled dossier `decisions`** [#48]. It conflates "mentioned" with "governs". Print candidates instead.
> - **A `kit-entrypoints` inventory, for now** [#43].
> - **Merging zero-claim dossiers back** [#47]. Move a few keys into them instead.
>
> ### 2.4 drift-audit
>
> 1. **Apply D12-i2 in `run_records_nonterminal_but_merged`** (high, S) [#51] [#17].
>    - Run `read_landing_commit`'s ancestry test against the base. Do NOT use `branch-sha`: it is written at
>      preflight, so every run would read LANDED on day one.
>    - The value drops from 12 to 2, both actionable.
>    - Give the residual an age column and make it the staleness bound for `TOOL-aReapedTicket-5`.
> 2. **Have the `drift-audit records` leg append one row per signal to a node-local
>    `<git-common-dir>/drift-history.tsv`** (high, S) [#55] [#63].
>    - Each row carries the sha, the base ref plus its sha, value, of, and a key hash, plus the fresh-file lexicon
>      arm.
>    - This is the prerequisite for "rising", for the lexicon kill rule, and for items 9 and 10.
> 3. **Fix the pins** (high, S then M) [#52].
>    - Lower `lexicon_verbs_declared_but_unused` from pin 3 to 0 today. That is one line.
>    - Then move the gateable stable-key signals to identity baselines, reusing `render_drift_offenders`' keys and
>      `baseline.toml`'s shape.
>    - `TOOL-dScaffoldedMirror-9` is the DEFERRED precedent for this.
> 4. **Re-arm `HANDKEPT` as a name-set comparison of the README table against `SIGNALS`, and drop the Skill's second
>    table** (medium, S) [#58]. Today the README omits 2 of 19 signals, and the Skill lists 6 of 19.
> 5. **Restrict `readme_mechanism_drift` to LIVE builds and re-seed its pin** (medium, S) [#61]. That leaves 4 hits.
>    Retire the signal if its precision stays below about 0.5.
> 6. **Retarget `dangling_pointers_in_own_ledger` to an adopter-declared auto-memory path, checking backticked
>    paths against `git ls-files`** (medium, S) [#56].
>    - Add a rule that a report-only signal DEAD for N readings is retired or filed as an ask [#62].
>    - Today's live catch: node a's install-prefix note names two files deleted by `e3d2cda9b`.
> 7. **Add `live_builds_without_activity` and `open_asks_cited_by_product_source`** (high, S-M) [#59].
>    - The second stays report-only until a sampled precision figure exists, because forward references make false
>      positives.
>    - Reuse `migrate_backlog.py`'s triage machinery; do not write a third ask parser.
> 8. **Group timeout retries by leg across all git dirs** (medium, S) [#53].
>    - Read the verdict files and `<i>.retry.leg`, not `gate-ledger.tsv`, which keeps one row per leg.
>    - Act on the reading now: `straggler-guard arms` was retried 9 times across 4 git dirs, and `brief-recorded`
>      failed after its retry at 648 s.
> 9. **Ship `TOOL-aProbedToolkit-18`, a records-only deliverable in the spec header, and grade shrink-only lists
>    against their low-water mark** (medium, M) [#57].
> 10. **Put a drift card line on kickoff and a BASE-to-HEAD drift delta on the unattended close** (high, S once item
>     2 exists) [#60] [#54]. Offer Tier 2 as a suggestion on the card; do not fan it out automatically.
> 11. **Add a report-only `remote_ci_red_streak` signal** (high, S) [#1]. Pair it with the three cheap leg fixes in
>     §3 theme A.
> 12. **Delete before syncing: retire or demote over-pin report-only signals nobody acts on** (low, S) [#54]. Print
>     `lexicon_marginal_offense_rate` without a pin label; its docstring says it has no pin.
>
> **Do not build:** a per-signal "owner action" governance field across 13 signals [#54] [#62].
>
> ### 2.5 Suggested order across kits (first ten moves)
>
> All ten are cheap, and most are already filed:
>
> 1. Fix the three CI legs and add the red-streak signal [#1].
> 2. D12-i2 in drift [#51].
> 3. The drift history TSV [#55].
> 4. The LIVE.md last-touch and LANDED-UNCLOSED columns [#3] [#13] [#59].
> 5. Bulk backlog triage [#8] [#19].
> 6. Kit-version `--fix` [#5].
> 7. Exclude snapshots from recall [#27].
> 8. Shell symbols in the map [#38].
> 9. A byte budget for `reuse_lookup` [#40].
> 10. `map_diff --by-design` into tier2 [#42].
>
> ---
>
> ## 3. Cross-cutting themes
>
> ### A. Detectors without consumers
>
> This is the largest gap, and the pattern is the same in every lens: the signal exists and nothing acts on it.
>
> - CI has been red 15 times out of 15, unrecorded [#1].
> - Held suites are red, with OPEN asks that carry no severity [#2].
> - 6 drift signals are over pin and no ask cites them [#54].
> - 452 asks are unlabelled [#8].
> - Nothing persists a drift reading [#55].
> - Drift never reaches the card or the close [#60].
> - The 08-30 Tier-2 review already wrote "the instrument is working — it is the response that is absent" [#54].
>
> **Fix pattern:** route existing detectors into sinks that already exist. Do not add detectors.
>
> - The inherited-red machinery already auto-files HIGH asks (`TOOL-aSightedSkeptic-11`) [#2]. Route the daily CI
>   held-job result into it.
> - The kickoff card and the unattended close summary are where drift readings should land [#60].
> - The three CI legs are cheap host-portability fixes [#1]:
>   - Add `encoding='utf-8'` in `matrix.py`.
>   - Stop the fixture leaking `__pycache__`.
>   - Set `eol=lf` on `tools/lexicon/*.template.md`.
>
>   Do them before any push-time CI check. A gate that is red for environmental reasons teaches people to use
>   `--no-verify`.
>
> ### B. The fixes are already filed and stalled
>
> A large share of the improvements above mean executing an existing ask:
>
> | Ask | What it would fix | Open since | Finding |
> |---|---|---|---|
> | `TOOL-aWeighedCompass-8` | shell visible to the map | 09-04 | [#38] |
> | `TOOL-aProbedToolkit-9` | output budget for `reuse_lookup` | 09-03 | [#40] |
> | `TOOL-aProbedToolkit-8` | separate code from record coverage in `map_diff` | 09-03 | [#44] [#49] |
> | `TOOL-aProbedToolkit-15` | unclaimed hooks and files | 09-03 | [#43] |
> | `TOOL-aProbedToolkit-10` and `TOOL-aWeighedCompass-16` (duplicates) | floor grades what the CLI serves | 09-03 / 09-04 | [#26] |
> | `TOOL-aWeighedCompass-11` | usage telemetry | 09-04 | [#32] |
> | `TOOL-aProbedToolkit-18` | records-only deliverables | 09-03 | [#57] |
> | `TOOL-aReapedTicket-5` | run-record staleness bound | 08-27 | [#51] |
> | `TOOL-aUnmannedHelm-2` | the dead ledger probe | 08-10 | [#56] |
> | `TOOL-aBoundedVerdict-29` and `DEPL-aHoistedPass-10` | version carriers | 08-19 / 09-05 | [#5] |
>
> `aTunedCompass` has been BLOCKED for a month on one SPECCED unit [#26].
>
> The backlog cannot rank (theme A, [#8]), so stalled high-value asks look the same as noise. Some OPEN asks are
> already fixed [#59]. Bulk triage plus the fixed-but-OPEN signal is what makes this list actionable.
>
> ### C. Two answers to one question
>
> The repo's own rule "one fact in one place" is broken by its tooling:
>
> - **Run state.** Drift's run-record terminal set disagrees with the unattended protocol's derived LANDED
>   ([#51], [#17]).
> - **Landed-ness.** LIVE.md ignores drift's spec-to-commit join [#13].
> - **Recall quality.** The recall floor grades a configuration the CLI refuses to serve [#26].
> - **Inventories and counts in prose.** Several surfaces state figures their sources contradict:
>   - the README and Skill signal tables [#58];
>   - recall's README scale figures [#36];
>   - the dossiers' typed counts [#41];
>   - `.lexicon.conf:20` "sh is DARK", two lines above its own shell parser declaration [#38].
> - **Kit versions.** One `version_from` constant is copied by hand into up to 27 carriers [#5].
>
> The fix is the same each time: derive, or gate the pair. For the version carriers, a `--fix` that writes every
> carrier from `version_from` is cheap and needs no new architecture [#5]. Since the switch-over, version carriers
> are also the main source of merge conflicts [#14].
>
> ### D. The system has no clock
>
> Nothing ages:
>
> - builds [#3] [#59];
> - asks, with a median age of 31 days and 108 at 45 days or more [#59];
> - drift readings, which are overwritten and not kept [#55];
> - the gate ledger, which keeps the last observation per leg, not a series [#53];
> - DEAD probes, which stay dead forever [#56] [#62].
>
> For unattended runs choosing work, this is the most damaging gap: idle residue reads as live work, so nodes spend
> passes on phantom claims [#59]. The cheapest clocks are a git-derived last-touch column [#3] and the history TSV
> [#55].
>
> ### E. Friction the tooling imposes on its own agents
>
> - **Learned traps.** Most of node a's learned traps concern the governance tooling itself. The 60% figure is
>   plausible but was not re-run [#5].
> - **Cost per new record.**
>   - A new folder surfaces its rules one bar cycle at a time [#23].
>   - 22 dated cutoffs make the required shape of a spec depend on its filename date [#16].
>   - The orphan-id rule pushes agents to paraphrase ids that have no record [#18].
> - **Version markers.** About 147 commits are marker bumps. The close-time "fix" `531db8c06` was a 31-file
>   version bump [#5].
> - **Bug-class checklist.** 48 of 94 classes for a mid-size diff is not a checklist anyone finishes [#21].
> - **Hygiene self-test.** It takes 10 to 35 minutes [#23].
> - **Required reading.** An unattended session owes about 181 KB of always-read guides [#7].
>
> The remedy is "a program writes what a program can compute": a `--fix` for carriers [#5], a `--doctor` for
> folders [#23], a cutoff budget [#16], and ranking for checklists [#21]. Watch that each remedy does not add a
> meta-gate of its own: [#13]'s trailer and [#16]'s ratio signal were rejected for exactly that reason.
>
> ### F. Precision claims rest on small or leaky instruments
>
> - The recall gold set has n=16, and its strong terms were written after reading the targets [#30].
> - Replay phrases leak vocabulary into both arms [#39].
> - Several drift true-positive rates come from samples of 2 to 5 ([#59], [#61]).
>
> Grow the instruments before tuning against them [#30]. Keep `replay-phrases.py` as the graded reference [#50].
> The lens headline that BM25 beats `reuse_lookup` dissolved once coverage was equalised [#39]: a warning about
> reading A/B results built on these instruments.
>
> ### G. The kits do not feed each other
>
> | Producer | Consumer that does not receive it | Finding |
> |---|---|---|
> | Dossier Constraints | reviewers (`byDesign` has no caller) | [#42] |
> | Dossier gotcha claims | `gotchas --for-diff` | [#45] |
> | Lexicon's shell parser | the map's symbol tier | [#38] |
> | Drift's spec-to-commit join | LIVE.md | [#13] |
> | Status and supersession in the memory tree | recall ranking | [#22] [#28] |
> | Map dossier prose, which can be false | recall, which serves it back as answers | [#41] |
> | Drift readings | kickoff and close | [#60] |
>
> Every integration on the plan lists is a join over data that already exists. None needs a new store.
>
> ### H. Telemetry is scoped to one git dir, but the product is many concurrent sessions
>
> - The retry signal reads only the per-worktree git dir [#53].
> - Drift's gate log dies with its worktree [#55].
> - Recall caches are keyed per worktree path and evict live siblings [#33].
> - Recall-opened attributes to the repo-wide last query across worktrees [#32].
> - Node-local auto-memory is unaudited and partly stale [#56] [#35].
>
> Fleet-level questions ("which leg retries everywhere?", "what did node d learn?") cannot be answered today.
>
> ### I. What the project lacks against its primary goal (Question 3, as far as the findings reach)
>
> 1. **A cross-node claim before landing.** Two nodes researched one question in parallel without knowing it
>    ("Neither knew about the other", `4f8073f30`) [#9].
>    - `aGraftedHelix`-1 specifies a CAS claim, but it is unpushed and was opened today.
>    - Cheaper interim step: push a README-only build branch at open, and have kickoff list `origin/branch/*` build
>      folders whose map keys overlap [#9].
> 2. **An outcome measure.** Nothing says whether governed code improves [#10]. Start by aggregating what runlog
>    already records per run (reds per close, time from open to land, findings per changed line), report-only,
>    before building a cross-repo ledger.
> 3. **A clean-machine green**, and behaviour suites that bind for the kits a change touches [#1] [#2]. Re-arming
>    self-tests at push reverses the 2026-08-23 owner ruling and needs a new one. The cheap half is routing CI
>    held-job reds into HIGH asks [#2].
> 4. **Liveness on work items and readings** (theme D).
> 5. **A blast-radius query for reviewers and unattended builders** [#46].
>
> ---
>
> ## 4. What did not survive verification
>
> No finding was refuted in full. These are the sub-claims and figures the verifiers refuted or corrected. Each is
> one line, and the corrected figure is the one used above.
>
> **Convergence and the bar**
>
> - [#1] The causes of the CI reds are not node-a state. They are host-environment and code defects: the
>   `matrix.py` codec, a `__pycache__` leak, a CRLF template.
> - [#1] "No record mentions it" is slightly overstated. `DECISIONS.md:131` routes a compensating check to the red
>   held job, without noting that the job is red.
> - [#2] The held suites are not the only behaviour tests. `transition-audit arms` and `govkit acceptance matrix`
>   bind at push.
> - [#2] Red legs are not all unlabelled. Inherited-red legs are auto-filed as HIGH asks; only the August and
>   September prose asks lack severity.
> - [#2] The proposal does not "keep" the owner ruling. Re-arming touched-kit self-tests reverses it.
> - [#3] The idle count is about 15 of 22, not 17, and 4 of those are DEFERRED by declaration.
> - [#3] [#13] "Status contradicts run records" is wrong. RUN LANDED next to a BLOCKED or DEFERRED build is a
>   partial landing.
> - [#4] "Review loops end only on budget or owner fiat" is refuted. A convergence stop rule exists (strictly
>   smaller since 08-20, `REVIEW_ROUNDS=1` since 09-14).
> - [#4] "TOOL-aScouredKit-1 reviewed 16 times" counts lens files from one or two waves.
> - [#4] The per-round confirmed means (15.0, 15.8, 17.4) and the pooled precision of 0.62 could not be
>   re-derived. Treat them as unverified.
> - [#5] "12% of commits only move markers" is wrong. About 147 commits (4%) are marker-only; 445 merely touch a
>   marker line.
> - [#5] "No single version source" is wrong. `kit.toml version_from` exists; the carriers are just not derived
>   from it.
> - [#8] "Require severity at filing" already exists (V12, `ASK_CUTOFF` 2026-10-01).
> - [#8] The pin moving 81, 89, 454 was a change of unit, not an upward drift.
> - [#11] `backlog_asks_contested` does not measure id collisions; check 13 does.
> - [#11] Two collisions exist outside the slug scheme: hygiene check numbers have collided across lineages, and
>   `DECISIONS.md` reuses ids within a session.
> - [#12] The caps stop growth but shrink nothing, and some were set at or raised to the current size.
>
> **memory-tree**
>
> - [#13] "Nothing links a commit to its unit" is wrong. Drift already joins spec ids to product commits.
> - [#13] The non-terminal spec count is 31, not 38.
> - [#14] All 75 recorded conflict merges predate the 09-28 switch-over. Since then, version carriers dominate.
> - [#14] The top conflict path is the authored `SESSION-KICKOFF.md`, at 44.
> - [#14] The backlog views are already `merge=rows`.
> - [#14] The regenerate driver was declined on purpose, not "withdrawn".
> - [#15] Recall noise from the archive is mostly legitimate: 16 of the 22 archive top-1 hits are the rotated
>   DECISIONS log.
> - [#15] No harm from the 88% terminal bytes was measured.
> - [#16] There were 155 memory-tree version bumps, not 147.
> - [#16] The "last bar failure was a records leg" evidence is stale. The failures of 10-01 to 10-04 are mostly
>   product and kit legs.
> - [#17] LANDED is already derived (D12-i2), and check 23 already excludes derived-LANDED records.
> - [#17] The proposed branch-sha rule would mark every run LANDED on day one.
> - [#18] Only citations of ids with no record are forced into prose. Citing existing ids works.
> - [#20] Only 1 of 43 cited paths in LIVE READMEs is dead.
> - [#20] `DECISIONS.md` rows are excluded by the append-only rule on purpose.
> - [#21] Not every universal is irrelevant to a records diff; the inline-fence class applies there.
> - [#22] Demoting all non-live records would bury CLOSED specs, which hold most of the rationale.
> - [#23] `--new-build` refusing without asks is by design (mandate scaffold, D12-a).
> - [#23] The "self-test last timed out" claim is stale. It now passes, in 10 to 35 minutes.
> - [#25] Gotcha anchor liveness is not gated. Check 15 does not cover `gotchas/`, and 39 of 314 anchors select
>   nothing.
>
> **memory-recall**
>
> - [#26] The "served ensemble 0.75" measured fusion without terms, which the CLI refuses. The real served shape is
>   ungraded and probably above the pin.
> - [#28] The flagship superseded example is a partial supersession (R2+R5 only). Label it; do not demote it.
> - [#28] `aGraftedHelix` is not stalled; it was opened today.
> - [#29] "Top 5 holds every answer" is true only for oracle-written strong terms. Weak-term answers sit at ranks
>   9, 19 and 35.
> - [#30] Q3 is in the weak pool, at rank 35. The weak misses are Q4, Q7 and Q12.
> - [#30] The README line quoted about dense arms concerns seed stability, not retrieval quality.
> - [#30] At n=16, the effect of lexical tweaks cannot be decided.
> - [#31] "Never beats the records arm" is false. Served hit@5 is 1.000 against 0.938 for records alone, thanks to
>   the gotcha rescue.
> - [#31] The MRR deltas are noise-level, and the gap is already filed.
> - [#33] Keying the cache by the current digest would share nothing, because the digest is mtime-based.
> - [#33] The impact is a rebuild of 6.5 to 15.5 s, not a correctness fault.
> - [#34] The selftest already has a 2,730 s ceiling and is held off the bar.
> - [#34] The last ranking change landed on 09-05, just before the window.
> - [#34] The diffstat depends on the base chosen.
> - [#35] Recall is used: 106 queries in the card window. The cards under-record it.
> - [#35] Path-scoped gotchas already exist and tier2 consumes them.
> - [#36] Grep is still slightly faster than a warm query. Only "small corpus" and "half the tree" are stale.
> - [#36] `--stats` does not exist.
>
> **codebase-map**
>
> - [#38] The shell work is already filed (`TOOL-aWeighedCompass-8`).
> - [#38] Its gain is mostly reach: hit@5 rises only 0.066, and the median rank worsens from 3 to 5.
> - [#38] 56,644 of the 95,973 shell lines are tests.
> - [#39] "`reuse_lookup` ranks worse than naive BM25" is refuted. With equal coverage it is 0.400 against 0.382;
>   BM25's lead came from shell files.
> - [#39] The `--converge` false positives are documented as by design.
> - [#40] "A top-30 cap costs almost nothing" is wrong today. It drops hit rate from 0.672 to 0.540.
> - [#40] The 60.6 KB answer did not reproduce; it measured 49 KB at HEAD.
> - [#44] The noisy `map_diff` coverage metric is already filed as `TOOL-aProbedToolkit-8`.
> - [#45] Unioning claimed gotchas grows an over-selecting list. Rank by the claim instead.
> - [#48] It is 14 of 16 empty-decisions dossiers, not 13.
> - [#48] Deriving `decisions` from cited ids conflicts with the pin's recorded rationale.
> - [#50] A floor on a guarded leg contradicts the 2026-08-23 owner ruling.
>
> **drift-audit**
>
> - [#53] `legs_retried_after_timeout` is live (value 3) in every worktree that has run a bar. It is dead only in
>   fresh worktrees and the primary.
> - [#53] The cited source (`gate-ledger.tsv`) holds one row per leg. The real data is 9 retries of `straggler-guard
>   arms` across 4 git dirs, plus `brief-recorded`.
> - [#54] Only `lexicon_marginal_offense_rate` cannot reach 0, and it is pinless by its docstring. The "over pin 0"
>   is a display artifact.
> - [#55] Readings are persisted in a degraded form: one overwritten text log per git dir, without the fresh-file
>   arm.
> - [#58] `shrink_only` is in the Skill table, so 5 of the 6 over-pin signals lack Skill guidance, not all 6.
> - [#60] "The state harness's default lenses never ran" is refuted. The aScouredKit statewave ran all five on
>   08-30.
