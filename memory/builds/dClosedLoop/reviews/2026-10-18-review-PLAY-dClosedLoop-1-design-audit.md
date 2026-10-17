**Serves:** spec-audit PLAY-dClosedLoop-1

# Tier-2 review: the whole-design audit of dClosedLoop's architecture v2 and gap register

Provenance: a Tier-2 spec audit at full intensity, run on 2026-10-18. It is the audit the owner declared at kickoff and step 4 of the owner's convergence order ("Execute on The PM-10 ownership table, The chain reordering, and The review declared at kickoff"). ROUND 1. Five lenses ran (finders gov-spec-reviewer), then five skeptic batches (gov-skeptic), then synthesis (gov-synthesizer). The audit read both subjects whole, as one architecture spec, with the layer and design records as context. It asked seven questions: consistency, the principles, the chain, the catalogue, P28, [owed] and [open], and the gap register.

Reviewed: memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@535c0e058def094389bfb236b85b0a877b067037, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@9a05621f429d0277ed1110fbb212fc098a8dbb8f

## Verdict: CLEAN WITH FIXES

No finding is a blocker. Six findings are high, in six items.

The design is not yet in full shape, and the high items show where. Three step builds route through mechanisms that only a descendant builds: dRankedPlan's RC-9 fallback needs an owner breakpoint (H1), and every step's `*.recommend` and `*.reason` items need dCalibratedLens (H2). dOrderedCharter's P28 check reads only recall-kit imports, while the core already depends on drift-audit and on shell-resolved optional kits (H3). Its move of the id grammar leaves the verdict-epoch gate scanning the old file (H4). The convergence fold empties two policy homes whose existing readers no row re-points (H5). A malformed policy file fails open to defaults that loosen strict and guarded postures (H6).

Fix these in v2, and in the register where it is named, before any chain build writes unit specs from its row. Most medium items are typed populations that should be derived by query, contracts that name one reader of a class, and text that still states a superseded answer.

Review shape: intensity full, raw 34, confirmed 33, refuted 1, unverified 0 (0 uncertain), precision 0.97. Adjudicated tally: by item, 0 blocker, 6 high, 16 medium, 6 low (28 items); by raw confirmed finding, 0 blocker, 6 high, 19 medium, 8 low (33 findings).

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |

Run integrity: lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0 contradictory verdicts were demoted to unverified, 0 orphaned duplicate refutations were demoted, 0 spurious verdicts were discarded, and there were 0 duplicates. Fixes on confirmed findings: 31 judged sound and 2 judged unsound (ids 7 and 11, whose skeptic-corrected fixes are written below), with 0 none proposed and 0 not judged. Severity: 0 ungraded, 5 re-graded by the skeptic (ids 17, 21, 25, 29, 31). No lens notes were supplied, so every lens ran on the kit's generic brief. Intent: 18 spec documents supplied as sibling context. Checklist: 17 items over 5 lenses. By design: the caller's byDesign. Move check: no checked subject moved. The run is complete. Id 27 was refuted (the M7 reader clause was misread) and is not reported.

Coverage against the seven questions:
- (1) Consistency: M2, M3, M4, M5, M10, L1, L3 and L4.
- (2) The principles: M4 (P7, P18), H3 and M7 (P28), H5 and M6 (P10), H6 (the guard and [floor]), M14 (P15) and M15 (P22).
- (3) The chain: H1, H2, H4, H5, M1, M3, M6, M8, M9, M12, M13, M16, L5 and L6.
- (4) The catalogue: H6, M8, M10, M11, L2 and L3.
- (5) P28: H3 and M7.
- (6) [owed] and [open]: M3 and L4.
- (7) The gap register: M2 (gap-spine-07's evidence) and M12 (gap-mem-13 narrowed by its owner row). No confirmed finding names a duplicated, orphaned or twice-owned gap.

## High

### H1. dRankedPlan's RC-9 fallback depends on a breakpoint only a descendant builds (id 1)

Where: v2 [chain] row dRankedPlan (the RC-9 fallback), against row dCalibratedLens and flow-steps [breakpoint].

What is wrong: under `plan.ratification: request`, dRankedPlan's `plan.exit` "falls back to an owner breakpoint" (RC-9). Breakpoints are built by dCalibratedLens, which descends from dRankedPlan through dTendedCadence. The breakpoint resolves as `run.on-owner-question` says, which is dBoundRoles's key. Under that key's default, the supervisor (dWellOiledMachine) resolves it. dRankedPlan's ancestors are dDeclaredLoop, dTotalRecall, dWitnessedBar, dOrderedCharter, dFairHearing and dGroundRules, and none of the three builds is among them. The re-cut lists only `entry.intake` as dRankedPlan's tolerance (recut:184, 364), because "owner breakpoint" is prose, not a backticked citation, so the ancestor probe cannot see it.

Consequence: dRankedPlan can land with no breakpoint mechanism. `plan.exit` then either cannot exit or exits unratified, or dRankedPlan hand-builds a second breakpoint, against dCalibratedLens's "one mechanism". Under the default `best-effort-recorded`, the stand-in for the owner's ratification is the supervisor's choice, not the owner's.

Fix (judged sound): choose one. (a) Put a minimal owner item, held until the owner's disposition record and ignoring `run.on-owner-question`, into dDeclaredLoop's transition table, and have dCalibratedLens generalise it into breakpoints. (b) State in dRankedPlan's row that its fallback is an owner item that only the owner's disposition record witnesses, built in dRankedPlan and absorbed by dCalibratedLens. In either case, add a row to the re-cut's [reconciled-order] for the prose citation, or extend the ancestor probe to cover prose mechanisms. Both options implement RC-9 without changing it.

Gate: extend the reconciliation probe so that every mechanism a row's text depends on, prose included, resolves to an ancestor or a declared tolerance.

### H2. Every step's recommend and reason items belong to a build that lands after the steps (id 32)

Where: v2 [chain] rows dRankedPlan (the RC-9 clause), dIndexedDesign, dScopedBuild and dShippedRelease, against dCalibratedLens's ownership (PM-12).

What is wrong: RC-9 gives a fallback for one item whose owner lands late, `entry.intake`. The class is wider. PM-12 made every step's `*.recommend` and `*.reason` items dCalibratedLens's, and each is on its step's main path: `plan.lease` held routes to `plan.recommend` (flow-steps:122), and the same holds for design, build, test and deploy. dCalibratedLens's parents are dTendedCadence and dFairHearing, so it lands after dRankedPlan, dIndexedDesign, dScopedBuild, dShippedRelease and dTendedCadence. v2:1170 calls the stage-exit recommendation dCalibratedLens's and gives no fallback. recut:184 has no row for any `*.recommend` item.

Consequence: between each step build's landing and dCalibratedLens's, `next` names an item that no landed code implements. The transition engine refuses transitions it lacks, so Plan, Design, Build, Test and Deploy cannot exit, and the chain's own dogfooded builds stall in that window.

Fix (judged sound): apply RC-9's pattern to the whole class. Either each step build ships a stub `*.recommend`/`*.reason` that records "recommendation not installed" and routes to `*.exit` or the owner gate, which dCalibratedLens later drains, or the items' owner lands before the first step build. Extend the reconciliation probe to walk each item's Then routes to the route target's owner, not just backticked citations, and see it red on `plan.lease` to `plan.recommend`.

Gate: the route-walking reconciliation probe, red on any main-path route to an item whose owner is neither the build nor an ancestor and that has no declared stub.

### H3. The P28 check reads recall imports only, but the core also depends on drift-audit and shell-resolved optional kits (id 9)

Where: v2 [chain] row dOrderedCharter (the check that the core never depends on an expansion or an optional component, M8); [principles] P28.

What is wrong: the check's population is the names a core memory-tree module imports from the recall kit, and nothing else. The tree has other core-to-optional edges that no row moves, wraps or names. gen_build_index.py:1695-1707 resolves drift-audit and runs `import drift_report` under LIVE_LANDED_UNCLOSED. memory-tree/kit.toml's requires_if row says that render "refuses by name before writing anything, with no degraded mode", and layer-instruction:242 places drift-audit and runlog in Observability, an expansion. Shell edges exist too: push-main.sh:732 (lexicon), unattended.sh:1268 (drift-audit), unattended.sh:14056 (runlog) and check-verdict-epoch.sh:176 (memory-recall's extract.py). No design record owns the drift_report edge.

Consequence: if the predicate covers every core-to-optional edge, it reds on gen_build_index.py the day dOrderedCharter lands, and no row owns the fix. If it is scoped to the recall names, it reports P28 green while the LIVE.md render refuses outright when drift-audit is absent, a gate certifying what it does not check.

Fix (judged sound): in dOrderedCharter's row, derive the population from every edge from a core kit to a non-core kit: Python imports, `resolve_kit_dir <kit>` calls in shell, and `requires_if` rows in kit.toml. Name an owning unit for each edge found: gen_build_index.py's drift_report import, push-main.sh's lexicon merge-loss call, unattended.sh's drift-audit and runlog calls, and check-verdict-epoch.sh's read of extract.py. Each edge either moves into the core or becomes a declared optional slot with a named fallback. Run the planted-import probe seen red, plus a planted `resolve_kit_dir` edge seen red.

Gate: a core-independence check whose population is every edge kind (import, shell resolution, requires_if), with one planted red per kind.

### H4. Moving the id grammar into memory-tree leaves the verdict-epoch gate scanning the old file (id 10)

Where: v2 [chain] row dOrderedCharter (moving `grammar_for`, `anchor_at`, `repo_root` and `recall_conf.resolve` into memory-tree).

What is wrong: the row names the import consumers of the moved names, but not the consumers that read memory-recall's extract.py by path. check-verdict-epoch.sh:62-68 scans extract.py because the grammar behind checks 13-16 lives there, and :176-180 builds a hand-listed DELEGATES set with no other grammar module. migrate_backlog.py:2805-2818 (seed_recall_kit) and merge-rows.test.sh:440, 734, 1724, 1789 and 1848 build fixtures by copying only extract.py and recall_conf.py.

Consequence: after the move, a grammar change no longer moves the verdict epoch. The gate prints clean with the constant untouched, the defect its own comment records measuring before (5 orphans became 9 under a clean print). Cached verdicts of checks 13-16 go stale on that path. The fixtures stop supplying the grammar that memory-tree modules now import from their own kit.

Fix (judged sound): add a unit to dOrderedCharter's move. It puts the moved module into check-verdict-epoch.sh's scan set, re-points migrate_backlog.py's seed_recall_kit and merge-rows.test.sh's fixture copies, and runs a `git grep -l 'extract.py\|recall_conf.py' -- tools/memory-tree` consumer inventory. Prove the scan-set change with a staged break: change one anchor pattern in the moved module on a scratch copy and see check-verdict-epoch.sh red.

Gate: a module move carries a by-path consumer inventory (scan sets, fixture copies), not only an import inventory.

### H5. The convergence fold empties two policy homes whose existing readers no row re-points (id 13)

Where: v2 [chain] row dConvergedCharter (the reader inventory, H6), with row dGroundRules and the [policies] preamble (RC-3, M7).

What is wrong: the fold moves `.githooks/gate-env.sh`'s keys and `tools/roles/house/policy.toml`'s `[effort]`/`[gates]` into `.governance/policy.toml`. Its by-value reader inventory names `transition_audit.read_modes`, govkit's gap checks, kit.toml's `*_keys`, the kit-placeholders leg and the agent-cap parser, and nothing else. It leaves out the four copies of `read_policy_key` (pre-push:1303, push-main.sh:404, post-merge.sh:168, unattended.sh:9380) and `roles_lib.load_policy` with its callers check_roles.py:355, handoff.py:480 and render_agents.py:123. dGroundRules's row only extends `read_policy_key`'s contract and re-points nothing. Chain-order review M7 named these readers, but no design record re-points them.

Consequence: once INHERITED_RED, INHERITED_RED_MAX_AGE and GATE_POST_MERGE move, pre-push finds no key and silently takes `land` (pre-push:1330-1340), and post-merge returns at once on an empty GATE_POST_MERGE. An adopter that set `park` lands inherited reds, and a declared post-merge verdict stops running, with no red either way. The roles readers read effort from a folded file. Keeping these four copies beside a fifth reader is also against P10's "one reader".

Fix (judged sound): extend dConvergedCharter's reader inventory, and RC-3's population in [policies], with every by-value reader of the two homes: the four `read_policy_key` copies and their callers (`read_policy_at`, `classify_docs`, `run_post_merge`, unattended's inherited-red read), and `roles_lib.load_policy` with its three callers. Either re-point them to dGroundRules's reader, read at the landed revision, in the fold's own unit, or have them read both homes keyed by commit, as `read_modes` does. Probe: fold INHERITED_RED=park in a scratch clone and run `.githooks/pre-push --decide` across the fold commit, which should read `land` until the re-point lands. The key-list half of this (GATE_DOC_PATHS and the other unlisted keys) is M5.

Gate: a retirement inventory derived by key value over the tree, red on any reader of a folded key that still reads the old home.

### H6. A malformed policy file fails open to defaults that loosen the guard (id 26)

Where: v2 [chain] row dGroundRules (the H4 clause); [floor].

What is wrong: the H4 clause treats a malformed file exactly like an absent one: every key falls to its catalogue default with a recorded reason. The owner's RC-1, as recut:144 records it, covers only the absent file, so the malformed case is v2's own choice. Neither the row nor [policies] says what happens to a key that is present with a value outside its allowed set.

Consequence: in a `strict` or `guarded` repository, one syntax error or truncated file silently restores hook bypass (`hooks.bypass` refused to allowed), `with-hooks-report` core bypass, warn-only leases and owner-free promotion. That loosens the guard without an owner choice, which [presets] says must never happen as a side effect. A typo such as `leases = "refuze"` has no specified outcome.

Fix (judged sound): split the absent file, where defaults are correct, from the malformed file and the out-of-set value. Those two must fail closed: refuse the push or landing gate and name the line, or read the last valid landed revision, but never use defaults. Add a planted-malformed-file arm in a strict repository that is red when any guard-bearing key reads looser than strict.

Gate: a reader-contract check with one planted input per failure class (absent, malformed, missing key, out-of-set value), each with its stated outcome.

## Medium

### M1. dGroundRules's no-reader arm is either red at its own landing or vacuous (id 2)

Where: v2 [chain] row dGroundRules, its last clause (the no-reader arm, H4).

What is wrong: the arm is "red when a key owned by a build that lands before dDeclaredLoop has no reader". By the Owner column, dOrderedCharter owns 12 keys, dFairHearing 3 and dGroundRules none, and both owners land after dGroundRules. The row does not scope the population to landed builds or define a reader, and its own generic default-reading reader would satisfy the arm.

Consequence: read literally, the arm is red at dGroundRules's landing and again at dOrderedCharter's. Read with the generic reader counted, it certifies coverage it never checks.

Fix (judged sound): restate the arm so its population is the keys whose Owner build has landed, read from a landed-builds record. Define a reader as a call site that consumes the key's value, excluding the policy reader's own default path. Name its seen-red probe: a key planted with Owner set to a landed build and no consumer reds, and the same key with an unlanded Owner stays green.

Gate: checklist entry: every arm states its population's scope in time and is seen red and seen green.

### M2. P1, [policies] and gap-spine-07 still put the policy schema in the loop kit (ids 3, 14)

Where: v2 [principles] P1 (v2:499-500); v2 [policies] opening paragraph (v2:690-691); gap register gap-spine-07, Evidence (register:211).

What is wrong: RC-1 moved the policy file, schema and reader to dGroundRules (v2:1160, and [policies]' own last sentence: "The file, its schema and its reader are dGroundRules's (RC-1)"). P1 still says the new loop kit owns "the policy schema". [policies] still says keys are "validated by the loop kit's schema". gap-spine-07 still cites "dDeclaredLoop's schema and its one reader".

Consequence: the spec gives two answers to where the schema lives. A builder of dGroundRules, or of gap-spine-07's fix (owned by dDeclaredLoop), may put a second schema in the loop kit, against P10's "one policy file, one reader, one guard". The P16 registry would register P1 against the wrong build.

Fix (judged sound): amend P1 to give the policy schema to dGroundRules, with the loop kit keeping the stage contracts and extending the schema. Change [policies]' first sentence to "validated by dGroundRules's schema". Re-cite gap-spine-07's evidence as "dGroundRules's schema and reader, extended by dDeclaredLoop's registry check". Do not re-argue RC-1.

Gate: checklist entry: an owner decision that moves a node updates every principle, section and gap that names the node's old home.

### M3. No row renders the preset and its overrides into the charter (id 4)

Where: v2 [front-door] (v2:667-668) and [presets] Rules (v2:898-900); [owed] "dOrderedCharter's policy consumers" (v2:1254-1258).

What is wrong: [front-door] puts "the repository's current preset and overrides" in the charter, and [presets] says the charter renders the preset's name and only the keys that differ from it. No chain row has that unit. dOrderedCharter's charter list stops at the project block, before presets exist. dDeclaredLoop builds the presets and their completeness check, with no charter render. dConvergedCharter renders protocols and templates, not the preset line. [owed] marks this consumer answered by RC-1, which supplies only the file, schema and reader.

Consequence: the charter ships without its posture line, and nothing reds it.

Fix (judged sound): add to dDeclaredLoop's row "the charter's preset section rendered through dOrderedCharter's renderer, the preset's name and the keys that differ from it, seen red on a planted override". Re-state the [owed] item: RC-1 answers the file, schema and reader, and dDeclaredLoop answers the preset render.

Gate: every acceptance stated outside [chain] must resolve to a clause in some row; a section-to-row join reds on an acceptance no clause implies.

### M4. P7 and P18 state as fixed what catalogue keys make switchable (id 5)

Where: v2 [principles] P7 (v2:518) and P18 (v2:544), against [policies] `review.blocks`, `run.on-owner-question`, `design.forks` and the [presets] table.

What is wrong: P7 says "every review that runs blocks", yet `review.blocks` allows owed-only and none, and velocity ships owed-only. P18 says "No build parks on an unresolved fork", yet `run.on-owner-question` allows park-item and park-build (strict ships park-item), and `design.forks` allows preference-forks-park. P16 makes principles fixed, with policies tuning only inside them. layer-flow:63-65 already qualifies the review rule with `review.blocks`.

Consequence: dOrderedCharter's meta-check registers each principle with its enforcing checks. A check written from the principle text reds the shipped velocity and strict presets, and a check written from the catalogue leaves the principle untrue.

Fix (judged sound): reword P7 to "a review that runs blocks as `review.blocks` says, every review by default", the form layer-flow already uses. Reword P18 to "by default no build parks; `run.on-owner-question` and `design.forks` let an owner choose to park". The owner's FR-4 and FL-R1 answers stand as given.

Gate: a principle-versus-catalogue check: each principle names the keys that tune it, and no shipped preset value contradicts the principle's text.

### M5. The gate-env legacy-homes list is typed, wrong, and misses four owner keys (ids 11, 18)

Where: v2 [policies] head paragraph (v2:694); [chain] row dGroundRules (the legacy homes on a shrink-only list, M4, M7) and row dConvergedCharter (the fold of "the legacy homes dGroundRules lists", v2:1175).

What is wrong: the list names `.githooks/gate-env.sh`'s keys as INHERITED_RED, INHERITED_RED_MAX_AGE and GATE_POST_MERGE. The file assigns GOV_KITROOT (90), INHERITED_RED (103), INHERITED_RED_MAX_AGE (104), GATE_DOC_PATHS (108), GATE_WSL_MIRROR_DEFAULT (113) and GATE_WSL_PARITY_RUNS (114). GATE_POST_MERGE is assigned nowhere in it, though pre-push:1621 reads it from the file. post-merge.sh:219-229 also reads GOV_GATE_CMD, GOV_PYTHON and GATE_SELFTESTS from it. GATE_DOC_PATHS decides which legs a push skips. GATE_WSL_PARITY_RUNS is a trust threshold set by owner rulings F1 and F2. [policies]' head folds "gate-env.sh's keys" unqualified, while dConvergedCharter folds only what dGroundRules lists, so the head and the two rows disagree.

Consequence: the shrink-only list either reds at its own landing over keys already assigned, or never covers them. GATE_DOC_PATHS and the WSL parity threshold stay owner policy outside the one policy file after the chain is done, against P10.

Fix (the finder's fix for id 11 was rejected; this is the skeptic's correction, and it agrees with id 18's sound fix): in dGroundRules's row, derive the population from the file by query: every `^[A-Z_][A-Z0-9_]*=` line in .githooks/gate-env.sh, the keys its header documents (GOV_GATE_CMD, GOV_BRANCH_GATE_CMD), and the keys its readers parse from it (GATE_POST_MERGE, read at pre-push:1621; and every key a `read_policy_key` call reads). Mark each key either an owner policy that dConvergedCharter folds (INHERITED_RED, INHERITED_RED_MAX_AGE, GATE_POST_MERGE, GATE_DOC_PATHS, GATE_WSL_PARITY_RUNS) or a mechanic that stays (GOV_KITROOT), and say which applies to GATE_WSL_MIRROR_DEFAULT. Keep GATE_POST_MERGE as declared but unassigned, as gap-deploy-02 records. The build plants a row and sees the list red, and sees it green on today's file. GATE_CMD is not a key of this file: it belongs to .unattended.conf.

Gate: a shrink-only list's population is derived by query from the file it guards, never typed.

### M6. dConvergedCharter's reader inventory omits the readers of the homes it empties (id 19)

Where: v2 [chain] row dConvergedCharter (the reader inventory by value, H6).

What is wrong: this is the reader half of H5, graded medium by its own finder and skeptic and kept as its own item because items merge within one grade only. Beyond H5's readers, it adds tools/run-gates/held_halves.py, which parses the GATE_WSL keys from gate-env.sh. v2 mentions `read_policy_key` only once, in dGroundRules's "extending `read_policy_key`'s contract", and names none of the copies or the roles readers.

Consequence: after the fold, pre-push, push-main.sh, post-merge.sh, unattended.sh and held_halves.py still parse gate-env.sh, and check_roles.py, handoff.py and render_agents.py still read house/policy.toml. Each reads an empty or stale home, or the old homes stay, leaving two policy homes and defaults the owner did not set.

Fix (judged sound): add to dConvergedCharter's inventory by name and file: .githooks/pre-push:1303, tools/push-main.sh:404, tools/run-gates/post-merge.sh:168 and tools/unattended/unattended.sh:9380 (`read_policy_key`), tools/run-gates/held_halves.py, and roles_lib.load_policy with check_roles.py, handoff.py and render_agents.py. Derive the inventory by key value over the tree rather than typing it. Plant the folded key in the old home only and see each reader's test red. H5's fix covers the same re-point.

Gate: the H5 retirement inventory.

### M7. The P28 check misses path probes, dynamic loads and shell routes into the recall kit (ids 17, 31)

Where: v2 [chain] row dOrderedCharter (the core-never-depends-on-an-optional-component check, M8 clause).

What is wrong: the population is "derived by `git grep`" over imports and "seeded red on a planted import". Core code also reaches memory-recall by other routes. gotchas.py:183-184 gates check 18 on the file probe `(mod.GRAMMAR_DIR / "extract.py").is_file()`, and gotchas.py is not on the row's module list. migrate_backlog.py:2813-2817 resolves the kit with `audit.resolve_recall_kit()` and copies its modules into a fixture. backlog.py:1791 calls `resolve_kit_dir("memory-recall", ...)`, and check-verdict-epoch.sh:176 resolves the kit in shell. A planted plain import proves only the plain-import shape; `__import__` and `importlib` loads are unexercised (corpus_ids.py:1145 records an earlier staged break of that kind in a comment).

Consequence: the check can certify "never depends" while a core check still degrades when recall is absent. Both skeptics graded this medium, not high, because the live non-import routes degrade with a named report (gotchas.py:1112 prints "NOT resolved") rather than silently. H3 is the separate, high defect of the non-recall edges.

Fix (judged sound for both): define the population as every route by which a core file reaches an optional kit: Python imports found by AST at any depth, `__import__` and `importlib` loads, path resolution of the kit's directory (`resolve_kit_dir("memory-recall"…)`, `resolve_recall_kit()`, `GRAMMAR_DIR / "extract.py"`), file copies of its modules, and shell references. Name gotchas.py:183, corpus_ids' GRAMMAR_DIR and migrate_backlog.py:2816 as readers the move rewrites. Plant the shipped shapes as reds: a deferred `import extract as EX` inside a function, `__import__("extract")`, a `(X / 'extract.py').is_file()` probe and a `resolve_kit_dir memory-recall` call in a .sh. On a scratch clone with tools/memory-recall removed, gotchas' check 18 must still resolve ids. check-verdict-epoch.sh's path use is either moved or registered as an optional slot.

Gate: the H3 core-independence check, with one planted red per route shape.

### M8. Re-pointing REVIEW_ROUNDS drops its runaway bound and names no reader (id 20)

Where: v2 [chain] row dCalibratedLens ("`REVIEW_ROUNDS` re-pointed at them"); [policies] `review.design.round-count`.

What is wrong: .unattended.conf:111 sets REVIEW_ROUNDS, and unattended.sh:774-783 refuses it at or above RUNAWAY_CEILING=8. The catalogue allows `review.design.round-count` any count. The row names none of the key's readers (16 non-memory files reference it). REVIEW_ROUNDS is also a kit conf key, so dGroundRules's shrink-only list and dConvergedCharter's fold reach it too.

Consequence: under `fixed-count`, a count of 8 or more is valid by the catalogue but refused by today's driver; if the re-pointed reader drops the refusal, the runaway ceiling fires before the declared bound. check-unattended.sh's parse (1850-1872, 2652), unattended-build.js and its template, and the PROTOCOL and VERBS templates keep reading the conf key. Three rows act on one key with no single owner of its fold.

Fix (judged sound): give `review.design.round-count` allowed values below the ceiling (1 to 7), or name the ceiling as a pair rule. In dCalibratedLens's row, name REVIEW_ROUNDS's readers: unattended.sh:779-783, check-unattended.sh:1850-1872 and 2652, tools/workflows/unattended-build(.template).js, and the PROTOCOL and VERBS templates. Have that row retire the conf key and take it off dGroundRules's legacy list, so one row owns its fold.

Gate: a catalogue check that every key replacing a legacy key carries the legacy key's bounds, and a one-owner-per-legacy-key check across rows.

### M9. Moving the map_lib names breaks the codebase-map gate and its adopter copies (id 22)

Where: v2 [chain] row dOrderedCharter ("`compute_coverage` moved to `tools/lib` ... with `map_lib.resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions` beside it").

What is wrong: the row names no consumer, re-export or re-copy. Consumers call through the `m.` alias: gen_map.py:164, map_diff.py:112, selftest.py (524-539, 965-968, 1588-1617), test_codebase_map.py:141/161/165 and test_codebase_map.template.py:141/161/165. adopt-codebase-map.sh:207 copies the template into every adopter.

Consequence: without re-exports, gov's codebase-map leg breaks, as do selftest.py, gen_map.py and map_diff.py. An adopter's installed gate breaks when its map_lib is updated without the template, and stays broken until the adopter re-runs the adopter script. The skeptic notes the adopter path is narrower than first stated, since an adopter holds its own map_lib copy.

Fix (judged sound): in dOrderedCharter's row, list the consumers: test_codebase_map.template.py:141,161,165 and its copy tools/codebase-map/test_codebase_map.py (gate-legs.json:817), selftest.py, gen_map.py, and map_diff.py for drop_touched_exemptions. Owe either map_lib re-exports for one release or a rewrite plus a re-copy into adopters through govkit's update. Run the map leg after the move, before landing.

Gate: a module move carries a consumer inventory that includes templates copied into adopters.

### M10. A preset-named file reads catalogue defaults, not the preset's values (id 25)

Where: v2 [chain] row dGroundRules (the H4 clause), against [presets] Rules.

What is wrong: the reader reads a key the file does not carry as its catalogue default. [presets] says the effective policy is the preset's assignment with the repository's overrides applied. dDeclaredLoop builds the presets, and no row changes the one reader's missing-key rule to consult the named preset.

Consequence: a repository with `preset = "strict"` or `guarded` and no override for `hooks.bypass`, `core.bypass`, `leases` or `verdict` reads `allowed`, `with-hooks-report`, `warn` or `local-hook`. Presets change nothing they do not also override. The finder graded this high; the skeptic graded it medium because [presets] states the intended rule, so it is a contradiction between two places in the spec, not a missing rule.

Fix (judged sound): in dGroundRules's row, state the resolution order: an override in the file, then the named preset's value, then the catalogue default only when the file names no preset or the preset system has not landed. Name dDeclaredLoop's row as the build that adds the preset step to the one reader. Add an arm red when a strict-named file with no override reads `hooks.bypass` as anything but `refused`.

Gate: a resolution-order check per shipped preset: a file naming only the preset reads every key as the preset's value.

### M11. The hooks' JSON mirror has no regeneration, pinning or absence rule (id 28)

Where: v2 [chain] row dGroundRules ("its JSON mirror"); [policies] head ("mirrored to JSON for the hooks").

What is wrong: the H4 and landed-revision contract names only the TOML reader. The hooks read policy through the JSON mirror, and nothing says when it is regenerated, whether it is pinned to the landed revision, or what a hook does when it is absent or stale. The walkthrough (lines 35 and 126) attached a parity leg to the mirror, and v2 does not carry it.

Consequence: after a policy change lands, a hook can enforce an old or working-tree value, or crash on an absent mirror, while the TOML reader says otherwise.

Fix (judged sound): extend the H4 clause to every reader of the class, the TOML reader and the mirror's consumers. Pin the mirror to the same landed revision, restore the walkthrough's parity leg, and state the hook's behaviour on an absent or stale mirror (fail closed, or fall back to the TOML reader). See the parity leg red on a hand-edited mirror.

Gate: a derived artifact carries a parity leg, seen red on a hand edit.

### M12. dTotalRecall's `record` row narrows gap-mem-13 to in-build mints (id 29)

Where: v2 [chain] row dTotalRecall (the `record` clause, v2:1165) and its Gaps owned cell (gap-mem-13).

What is wrong: the row says `record` "mints ids under the build's claim or lease", the in-build case only. gap-mem-13 (register:154) and layer-memory [contract] (320-334) name every filer outside a build (the owner, `entry.place`, a surfaced idea, an expansion, the supervisor) minting under an ask family's counter ref advanced by a leased compare-and-swap, with a claimant key and no prune of `refs/gov/claims/*`. None of that is in the row.

Consequence: a builder working to the row leaves out-of-build asks minting from the local clone, and two clones that have not fetched each other mint one ask id, the defect gap-mem-13 exists to close. The finder graded this high; the skeptic graded it medium because the row's first clause is "the memory contract" and its Gaps owned cell lists gap-mem-13, whose text spells out the fix.

Fix (judged sound): add to dTotalRecall's row the ask-family counter ref advanced by a `--force-with-lease` push for every filer outside a build, the claimant key on every claim commit, and slug claim refs never pruned. The acceptance is a two-clone concurrent mint seen red against today's local-only `check_slug_claimed`.

Gate: a gap-to-row join: each owned gap's fix clauses must appear in its owner row's Planned units.

### M13. The id-mint path has no unreachable-remote outcome (id 30)

Where: v2 [chain] rows dDeclaredLoop ("offline behaviour") and dTotalRecall (the `record` mint); [policies] `leases.offline`.

What is wrong: offline behaviour is specified for lease acquisition only (coordination.md:96-98, v2:719 and 953). Minting rests on compare-and-swap pushes (`entry.claim`'s claim ref and the ask-family counter). flow-steps.md:76 gives `entry.claim` three outcomes (claimed, claimed under another key, lease refused), none for an unreachable remote. layer-memory has no offline rule.

Consequence: under the default `leases.offline: warn`, an offline session filing an ask or claiming a slug either blocks every record write, contrary to `warn`, or mints locally and collides on reconnection, breaking id uniqueness. The builder picks one.

Fix (judged sound): give the mint path an explicit unreachable-remote outcome tied to `leases.offline`, for example refuse the mint and queue the ask unminted, keyed by content, to be minted by compare-and-swap on reconnection, never minting a local id. Add it to `entry.claim`'s closed outcome set. Probe with the remote made unreachable.

Gate: checklist entry: every remote compare-and-swap write names its unreachable-remote outcome in its closed outcome set.

### M14. RC-9's fallback drains for every harness, but Codex has no prompt-submit event (id 33)

Where: v2 [chain] row dWellOiledMachine ("the prompt-submit hook writing each owner prompt ...", "RC-9's fallback drained"), against `runtime.harnesses`.

What is wrong: the intake witness hangs on the prompt-submit event, and the fallback drains globally once that hook lands. Codex is a registered adapter (layer-runtime:821), and its events are PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd (layer-runtime:242, 794-799). The spec does not say what writes intake on a harness without the event.

Consequence: after the drain, an attended Codex session writes no intake record, so `plan.exit` under the default `plan.ratification: request` has no ratification witness and its builds cannot leave Plan. P15's claim that any harness can drive gov fails at the first step. Contained because the default harness is claude-code.

Fix (judged sound): make the fallback per harness. A harness adapter's capability table declares whether it carries prompt-submit. Where it does not, the fallback stays in force (an owner breakpoint witnessed "intake not installed") or the adapter's launch input writes intake. The drain removes the fallback only for adapters that declare the event. A planted Codex-shaped adapter must still reach `plan.exit`.

Gate: a harness-capability check: every mechanism tied to a harness event is either declared by each registered adapter or has a per-adapter fallback.

### M15. Builds in flight across the RC-9 drain lose their witnesses (id 34)

Where: v2 [chain] rows dRankedPlan (the RC-9 fallback, v2:1169) and dWellOiledMachine ("Plan's ratification and the placement dispositions re-pointed to the intake record, RC-9's fallback drained", v2:1167).

What is wrong: builds whose `plan.exit` was witnessed "intake not installed", and whose placement disposition sits in the claim commit (v2:1163), may still be open, or derived from history, when the readers are re-pointed to the intake record. The re-cut's RC-9 lines (135, 142, 184, 265) say nothing about them.

Consequence: position is derived from witnesses every time (P22). A re-pointed reader that knows only the intake kind can re-derive those builds as unratified or unplaced and send them back to Plan, or a drain that deletes the fallback reader leaves their history unreadable. Limited to builds crossing one landing.

Fix (judged sound): state the migration. Either the re-pointed readers accept both witness kinds for builds whose `plan.exit` predates the hook, keyed by the landing that drained the fallback, or the drain backfills a marked intake-equivalent record for each such build. Run a probe over a build that crosses the boundary, seen red without the rule.

Gate: checklist entry: every drain of a fallback names how witnesses written under the fallback stay readable.

### M16. Adding kit.toml for govkit and lib pulls both into every kit glob (id 23)

Where: v2 [chain] row dShippedRelease ("a `kit.toml` for govkit and lib, today's kits reviewed", v2:1172).

What is wrong: neither descriptor exists today. Consumers glob `*/kit.toml`: regen.py:110, check-kit-placeholders.py:81, run-gates.sh:1432, check-hook-destinations.sh, render_playbook.py and govkit.py's descriptor checks (20 files outside tests). Neither the row nor gap-mem-27 (register:168) says how a gov-internal lib descriptor stays out of the installable-kit population, though the Facts call tools/lib gov-internal and carried inline.

Consequence: a red at landing, or tools/lib offered or validated as an installable kit, unless each consumer changes or the descriptor's shape excludes it.

Fix (judged sound): in dShippedRelease's row, name the `*/kit.toml` consumers listed above. Declare how a non-installable descriptor such as lib is marked, and how each consumer treats it. Run each consumer's leg on a tree with both descriptors.

Gate: a new descriptor in a globbed population carries the glob's consumer inventory.

## Low

### L1. The [chain] heading says fifteen builds; the table has sixteen (ids 6, 12, 24)

Where: v2 [chain] section heading (v2:1156, "## [chain] The chain: fifteen builds, final rosters").

What is wrong: the table has 16 build rows, the revision log (v2:431) records dGroundRules as "a sixteenth build", and the re-cut's critical-path instrument asserts 16. The count is typed, not derived, and the two statements disagree.

Consequence: a reader or a count check that trusts the heading under-counts the chain by dGroundRules, the build that lands first. Nothing reads the heading today, so the effect is cosmetic.

Fix (judged sound for all three): retitle it "[chain] The chain: sixteen builds, final rosters", or drop the typed count so the table is the only answer.

Gate: checklist entry: no typed count beside a table that carries the count.

### L2. The preset completeness rule is not decidable from the text (id 7)

Where: v2 [presets] Rules ("every presettable key", v2:901) and the presets table.

What is wrong: `preset` is a catalogue key (v2:701) that is neither on the never-touch list (v2:907-909) nor assigned by any preset. Strict's `tests.landing-levels` cell, "every declared level" (v2:1029), is not a subset of the allowed unit, integration, e2e and performance (v2:798). Strict's `maintain.fixes` cell, "reap and regenerate only; the rest filed as asks" (v2:1060), is prose, not named fixes from v2:829.

Consequence: dDeclaredLoop's completeness check, built from the text, either reds every shipped preset or needs exemptions the spec does not state.

Fix (the finder's fix was rejected; this is the skeptic's correction): add `preset` to [presets]' never-touch list. Write strict's `maintain.fixes` cell as "reap, regenerate stale" and drop "the rest filed as asks", since strict's `maintain.on-breach: red-leg` already governs the rest. For `tests.landing-levels`, either write strict's cell as "unit, integration, e2e, performance" or add an `every-declared` value to the catalogue row's allowed values and use it, whichever matches the owner's intent. Moving "the rest filed as asks" into `maintain.on-breach` would contradict strict's own red-leg value.

Gate: the completeness check itself, run over the spec's tables: every preset cell is a value its catalogue row allows, and every key is either assigned or on the never-touch list.

### L3. Velocity's prose says nothing refuses, but its column ships refusing values (id 8)

Where: v2 [presets] "The four shipped presets", velocity (v2:917-919).

What is wrong: velocity is described as "Everything warns or records, nothing refuses but the floor". Its column ships `runtime.hook-failure: closed` (v2:995), `runtime.secret-scan: value-gate` (v2:1001) and `instructions.legacy: shrink-only` (v2:1097). All three are refusing values, and none is among [floor]'s four invariants (v2:1125-1130).

Consequence: an owner who picks velocity for "no refusals" still gets fail-closed hooks and secret-value refusals. The values themselves are unaffected.

Fix (judged sound): reword velocity to "everything the posture governs warns or records; the floor, fail-closed hooks, the secret value gate and shrink-only ratchets still refuse".

Gate: checklist entry: a preset's prose is checked against its column's refusing values.

### L4. Answered [owed] items still pose their questions as open (id 15)

Where: v2 [owed] items "Kit confs beside the policy file", "dOrderedCharter's policy consumers", "The tooling order" and "The `next` verb now lands with Runtime" (v2:1242-1258).

What is wrong: each opens with "State, 2026-10-18: answered ..." but its body still asks the question in the present tense. "Kit confs" ends "Whether those confs fold into the policy file is undecided." "dOrderedCharter's policy consumers" offers two options, and RC-1 chose neither (it chose dGroundRules). "The tooling order" ends "The re-cut weighs both orders." The `next` item still offers both orders.

Consequence: a reader or a recall hit on the body sees a decided question as open, and may re-open it or act on a rejected option. The State line does carry the decision.

Fix (judged sound): reduce each answered item's body to the decision and its record (RC-1, RC-3/H6, RC-4, M3), or move the original question under a "was:" clause, so no answered item states its question in the present tense. M3 also corrects the consumers item's state.

Gate: checklist entry: marking an item answered rewrites its body in the same edit.

### L5. dOrderedCharter and dTotalRecall plan the same artifact twice (id 16)

Where: v2 [chain] rows dOrderedCharter (v2:1161) and dTotalRecall (v2:1165), Planned units.

What is wrong: dOrderedCharter has three duplicate pairs:
- "each practice's reach per step rendered as step-scoped units (IW-2)" appears twice.
- "the section-tag grammar and its resolver" sits beside "the tag grammar, its namespace registry ... with one resolver".
- "the instruction registry and the ladder" sits beside "the instruction-unit registry (per unit: tag, level, ...)".

dTotalRecall plans the auto-memory remainder against `memory.load-budget` at session start twice.

Consequence: counted one unit per clause, each pair plans one thing twice. A builder would most likely merge them, so the effect is redundancy in the plan.

Fix (judged sound): merge each duplicate pair into one clause, keeping the fuller wording.

Gate: checklist entry: one artifact, one clause per row.

### L6. The 32 KiB charter budget ignores the existing AGENTS.md and template size rows (id 21)

Where: v2 [front-door] ("The whole charter fits ... Codex's 32 KiB", v2:669) and [chain] row dOrderedCharter ("the charter held inside 32 KiB"; budgets "extending `template-size-limits.txt`").

What is wrong: tools/template-size-limits.txt already caps AGENTS.md at 20480 bytes (:85) and the charter template at 49152 (:48), which is above the 32 KiB v2 promises. v2 names neither row. AGENTS.md is 16732 bytes, leaving 3748. The re-founded charter adds the core principles (the [principles] text alone is 12661 bytes), the decision principles, the drive section, the preset line and the level-0 envelope.

Consequence: check-template-size is likely red at dOrderedCharter's landing. The finder graded this medium. The skeptic graded it low because the limits file lets an owner-mandated build raise a measured row under its four conditions (lines 16-23), and dOrderedCharter plans its own 32 KiB hold.

Fix (judged sound): in dOrderedCharter's row, name the AGENTS.md 20480 row and the template's 49152 row. Either project the re-founded charter's size and owe the raise, or state that the 32 KiB bound replaces both rows and put that change to the owner. Measure the rendered charter at its first unit against both the existing row and 32768.

Gate: a budget a spec promises is reconciled against the size-limit rows that already cover the file.

## Left-shift

Every confirmed finding maps to a gate or a checklist entry.

The gates:
- A reconciliation probe that walks prose dependencies and item routes to their owner's ancestry (H1, H2).
- A core-independence check over every edge kind, with one planted red per route shape (H3, M7).
- A move or retirement inventory derived by consumer, by path and by key value. It covers scan sets, fixtures, adopter templates and globbed populations (H4, H5, M6, M9, M16).
- Populations derived by query, never typed (M1, M5, L1).
- A policy-reader contract check with one planted input per failure class and per preset, applied to every reader of the class (H6, M10, M11).
- A preset check against the catalogue and the principles (M4, L2, L3).
- A gap-to-row join (M12).

The checklist entries:
- An owner decision updates every principle, section, gap and [owed] body that names the old answer (M2, M3, L4).
- Every remote write names its unreachable-remote outcome (M13).
- Every fallback names its per-harness scope and how its witnesses migrate (M14, M15).
- A legacy key keeps its bounds and has one owner (M8).
- A budget reconciles with the existing limits (L6).
- One artifact, one clause (L5).

review-shape kind=spec-audit round=1 intensity=full at=synth raw=34 confirmed=33 refuted=1 unverified=0 blocker=0 high=6 medium=19 low=8 agents=11 out-tokens=217710

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dRankedPlan row (RC-9 fallback), against dCalibratedLens's row and flow-steps [breakpoint] | high | high | confirmed | Both blobs match their pins. v2:1169 dRankedPlan (parents dDeclaredLoop and dTotalRecall) says that under `plan.ratification: request`, `plan.exit` 'falls back to an owner breakpoint' (RC-9). Walking the Parents column gives dRankedPlan's ancestors as dDeclaredLoop, dTotalRecall, dWitnessedBar, dOrderedCharter, dFairHearing and dGroundRules. None of them is dCalibratedLens, dBoundRoles or dWellOiledMachine. dCalibratedLens (v2:1174, parents dTendedCadence and dFairHearing, and dTendedCadence descends from dRankedPlan) builds 'breakpoints placeable at any item boundary ... reviews and owner gates one mechanism'. It also owns `autonomy` (v2:708) and `review.breakpoints` (v2:784). flow-steps:425-430 resolves an owner breakpoint as `run.on-owner-question` says, and that key is dBoundRoles's (v2:772). Its default is the supervisor's recorded choice. The re-cut lists only `entry.intake` as dRankedPlan's tolerance (recut:184 and 364), so the breakpoint dependency on a descendant goes unnoticed. The claim is true and reachable, and it will mislead whoever builds dRankedPlan. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules row, its last clause (the no-reader arm, H4) | medium | medium | confirmed | v2:1160's last clause is 'an arm red when a key owned by a build that lands before dDeclaredLoop has no reader, its population derived from the catalogue's Owner column by query (H4)'. By the Owner column, dOrderedCharter owns 12 keys, dFairHearing owns 3 and dGroundRules owns none. Both of those builds have dGroundRules as their only parent, so they land after the arm does. The row does not scope the population to builds that have landed, and it does not define what counts as a reader. The same row's generic default-reading reader would satisfy the arm trivially. recut:144 states the intent ('an arm reds on a root-owned key with no reader'), but the row text leaves the arm either red at its own landing or vacuous. | sound | fixture-passes-by-finding-nothing |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P1; [policies] opening paragraph; gap register gap-spine-07 Evidence | medium | medium | confirmed | Re-read: v2:499-500 P1 says 'A new loop kit owns WHAT ... and the policy schema'. v2:690-691 [policies] says 'validated by the loop kit's schema'. The same paragraph ends 'The file, its schema and its reader are dGroundRules's (RC-1)', and v2:1160 has dGroundRules's row saying the schema was 'moved from dDeclaredLoop'. In the register, line 211 (gap-spine-07's Evidence) still cites 'dDeclaredLoop's schema and its one reader'. Two answers to where the schema lives stand in the spec set. | sound | amendment-leaves-its-other-half-standing |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[front-door] and [presets] Rules (the charter renders the preset and its overrides); [owed] 'dOrderedCharter's policy consumers' | medium | medium | confirmed | [front-door] (v2:667-668) puts 'the repository's current preset and overrides' in the charter. [presets] (v2:898-900) says the charter renders the preset's name and the keys that differ from it, and v2:691 says policy is 'rendered into the charter'. I split every chain row's Planned units at ';' and searched the clauses for preset, posture and override. dOrderedCharter's charter list stops at the project block and has no preset clause. dDeclaredLoop builds the presets and their completeness check, with no charter render. dConvergedCharter renders protocols and templates from policies, not the charter's preset line. No other row matched. The [owed] item 'dOrderedCharter's policy consumers' (v2:1254-1258) names the charter's preset render among the consumers, yet it is marked answered by RC-1, and RC-1 supplies only the file, schema and reader. | sound | - |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P7 and P18, against [policies] `review.blocks`, `run.on-owner-question` and `design.forks`, and the [presets] table | medium | medium | confirmed | v2:518 P7 says 'every review that runs blocks', and v2:544 P18 says 'No build parks on an unresolved fork'. v2:601-602 P16 says principles are fixed and policies only tune inside them. Against that: `review.blocks` allows owed-only and none (v2:844), and velocity ships owed-only (v2:1080). `run.on-owner-question` allows park-item and park-build (v2:772), and strict ships park-item (v2:1006). `design.forks` allows preference-forks-park (v2:706). layer-flow:63-65 already qualifies the review rule with '(`review.blocks`)'. This is a contradiction in the text, not a re-argument of FR-4 or FL-R1. A principle check written from the text would red the shipped presets. | sound | two-answers-to-one-question |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] section heading | low | low | confirmed | v2:1156 reads '## [chain] The chain: fifteen builds, final rosters'. The table has 16 build rows (I counted rows starting '\| d' in the chain table and got 16). v2:431 says 'a sixteenth build, dGroundRules'. The mismatch is cosmetic. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[presets] Rules ('every presettable key') and the presets table | low | low | confirmed | v2:701 makes `preset` a catalogue key. The never-touch list at v2:907-909 omits it, and the presets table has no `preset` row, yet v2:901 says every shipped preset assigns every presettable key. Strict's `tests.landing-levels` cell (v2:1029) is 'every declared level', which is not a subset of the allowed unit, integration, e2e and performance (v2:798). Its `maintain.fixes` cell (v2:1060) is 'reap and regenerate only; the rest filed as asks', which is prose rather than named fixes from v2:829. The fix is unsound on two counts. First, it offers to move 'the rest filed as asks' into `maintain.on-breach`, but strict sets that key to red-leg (v2:1061), not file-ask, so the move would contradict strict's own row. Second, rewriting 'every declared level' as all four levels may change its meaning for a repository that declares fewer levels. | unsound | - |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[presets] 'The four shipped presets', velocity | low | low | confirmed | v2:917-919 says velocity is the preset where 'Everything warns or records, nothing refuses but the floor'. In the same file, v2:995 gives velocity `runtime.hook-failure` closed, v2:1001 gives it `runtime.secret-scan` value-gate and v2:1097 gives it `instructions.legacy` shrink-only. The catalogue rows (v2:761, 767, 861) show these are refusing values. None of them is in the [floor] section (v2:1125-1130), which lists only four invariants. So the prose misstates what velocity enforces. The values themselves are unaffected, so the effect is cosmetic. | sound | two-answers-to-one-question |
| 9 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter row (the check that the core never depends on an expansion or an optional component, M8); [principles] P28 | high | high | confirmed | dOrderedCharter's row (v2:1161) bases the core-never-depends-on-an-expansion check on names a core memory-tree module imports from the recall kit, and nothing else. The tree has other edges. gen_build_index.py:1695-1707 resolves drift-audit and runs `import drift_report` under LIVE_LANDED_UNCLOSED. memory-tree/kit.toml's requires_if row for drift-audit says the render 'refuses by name before writing anything, with no degraded mode'. layer-instruction:242 puts runlog and drift-audit in Observability, an expansion. The shell edges reproduce: push-main.sh:732 (lexicon), unattended.sh:1268 (drift-audit), unattended.sh:14056 (runlog) and check-verdict-epoch.sh:176 (memory-recall extract.py). A grep for drift_report across the design records finds no record that owns the edge. P28 (v2:615-622) says the core never depends on an optional component or an expansion. Built as written, the check either reds with no row owning the fix, or certifies P28 over a subset of the edges. | sound | - |
| 10 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter row (moving the id grammar's `grammar_for`, `anchor_at` and `repo_root`, and `recall_conf.resolve`, into memory-tree) | high | high | confirmed | check-verdict-epoch.sh:62-68 says it scans memory-recall's extract.py because the grammar behind checks 13-16 lives there, and records a measured clean print over a changed grammar. At :176-180 it resolves `_recall=.../extract.py` and builds a hand-listed DELEGATES set that holds no other module for the grammar. migrate_backlog.py:2805-2818 seed_recall_kit copies only extract.py and recall_conf.py. merge-rows.test.sh:440, 734, 1724, 1789 and 1848 do the same. The dOrderedCharter row (v2:1161) moves grammar_for, anchor_at, repo_root and recall_conf.resolve into memory-tree and names the import consumers. It names neither the verdict-epoch scan set nor the fixture copies. Once the grammar sits in a new memory-tree file that is not in DELEGATES, a grammar change passes the gate with a clean print. That is a check certifying what it does not check, on the narrow path of a grammar change. | sound | - |
| 11 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] preamble; [chain] dGroundRules row (legacy homes on the shrink-only list, M4, M7) and dConvergedCharter row (the fold of 'the legacy homes dGroundRules lists') | medium | medium | confirmed | Grepping .githooks/gate-env.sh for assignments prints GOV_KITROOT(90), INHERITED_RED(103), INHERITED_RED_MAX_AGE(104), GATE_DOC_PATHS(108), GATE_WSL_MIRROR_DEFAULT(113) and GATE_WSL_PARITY_RUNS(114). There is no GATE_POST_MERGE line, although pre-push:1621 reads that key from the file. Lines 105-112 document GATE_DOC_PATHS as read by pre-push at R, and GATE_WSL_PARITY_RUNS as the trust threshold set by owner rulings F1 and F2. The dGroundRules row (v2:1160) lists only INHERITED_RED, INHERITED_RED_MAX_AGE and GATE_POST_MERGE. dConvergedCharter (v2:1175) folds only 'the legacy homes dGroundRules lists'. A grep across memory/builds/dClosedLoop for GATE_DOC_PATHS or GATE_WSL_PARITY prints only the v2 row match and review records, so no design record covers these keys. The proposed fix is unsound: as its example of a header-documented key it names GATE_CMD, but the header (gate-env.sh:59-66) documents GOV_GATE_CMD and GOV_BRANCH_GATE_CMD. GATE_CMD belongs to .unattended.conf, so the fix would add a key the file does not own. | unsound | - |
| 12 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] heading | low | low | confirmed | v2:1156 reads '## [chain] The chain: fifteen builds, final rosters'. A python count of the lines starting with '\| d' between ## [chain] and ## [open] printed 16. v2:431 records dGroundRules as 'a sixteenth build'. The typed count is wrong, and only a reader of the heading is affected. | sound | - |
| 13 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] row dConvergedCharter (the reader inventory, H6) with row dGroundRules and the [policies] preamble (RC-3, M7) | high | high | confirmed | `git grep 'read_policy_key() {'` prints four copies: pre-push:1303, push-main.sh:404, post-merge.sh:168 and unattended.sh:9380. pre-push:1330-1340 maps an empty INHERITED_RED to land with 'no INHERITED_RED is declared ... kit default land applies'. pre-push:1621-1622 reads GATE_POST_MERGE and GATE_DOC_PATHS from the gate-env blob at R. load_policy is called at check_roles.py:355, handoff.py:480 and render_agents.py:123. dConvergedCharter's inventory (v2:1175) names only read_modes, govkit's gap checks, kit.toml *_keys, the kit-placeholders leg and the agent-cap parser. dGroundRules (v2:1160) only extends read_policy_key's contract and re-points nothing. Chain-order review M7 (lines 157-166) named these readers, but no design record re-points them; the grep finds them only in v2:1160, recut:151 and the reviews. If the fold moves the keys as written, pre-push silently falls back to land, and post-merge goes dark with no red. That consequence is real on the adopter path where park is set or a post-merge verdict is declared. This is not a duplicate of id=11, which concerns the key list; this finding concerns the readers. | sound | - |
| 14 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P1 and the [policies] preamble; gap register gap-spine-07 Evidence | medium | medium | confirmed | v2:499-500 (P1) gives 'the policy schema' to the new loop kit. v2:690 says 'validated by the loop kit's schema'. Gap-register:211, gap-spine-07, cites 'dDeclaredLoop's schema and its one reader'. Yet v2:696-697 says 'The file, its schema and its reader are dGroundRules's (RC-1)', and the dGroundRules row (v2:1160) builds the schema 'moved from dDeclaredLoop'. The spec contradicts itself and cites a seam the chain does not build. That risks a second schema in the loop kit, against P10. | sound | - |
| 15 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[owed] items 'Kit confs beside the policy file', 'dOrderedCharter's policy consumers', 'The tooling order', 'The `next` verb now lands with Runtime' | low | low | confirmed | I checked the pinned blob (hash-object gives 535c0e05). At v2 lines 1242-1258 each item opens with 'State, 2026-10-18: answered ...' but its body still asks the question in the present tense. 'Kit confs' ends 'Whether those confs fold into the policy file is undecided.' 'dOrderedCharter's policy consumers' ends 'The re-cut moves the policy file, schema and reader into dOrderedCharter, or orders those units after dDeclaredLoop.' RC-1 chose neither: it chose dGroundRules. 'The tooling order' ends 'The re-cut weighs both orders.' The `next` item ends 'The re-cut either orders ... or lands its `next` unit first.' The State line does carry the decision, so this is only stale prose, which makes it low. | sound | - |
| 16 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] rows dOrderedCharter and dTotalRecall (Planned units) | low | low | confirmed | I re-ran the count on v2:1161. 'each practice's reach per step rendered as step-scoped units' appears twice, at the head of the row and in the IW-2 clause near its end. 'tag grammar' appears twice: 'the section-tag grammar and its resolver' and 'the tag grammar, its namespace registry ... with one resolver'. 'the instruction registry and the ladder' sits beside 'the instruction-unit registry (per unit: tag, level, ...)'. In v2:1165, 'load-budget' appears twice: 'held to `memory.load-budget` and reported at session start' and 'the auto-memory's remainder reported against `memory.load-budget` at session start'. Counted one unit per clause, each pair plans one thing twice. A builder would most likely merge them, so the effect is redundancy in the plan, which makes it low. | sound | - |
| 17 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter row (the check that the core never depends on an expansion or an optional component, M8) | high | medium | confirmed | v2:1161 bounds the core-independence check to 'every name a core memory-tree module imports from the recall kit ... the population derived by `git grep` and seeded red on a planted import'. It names backlog, corpus_ids, merge-rows, transition_audit and gen_build_index. On re-probe, gotchas.py:183-184 gates check 18 on the file `(mod.GRAMMAR_DIR / "extract.py").is_file()` and returns 'the id grammar lives in the memory-recall kit, which is not installed beside this one'. That is a path probe, not an import, and gotchas.py is not on v2's list. migrate_backlog.py:2813-2817 resolves the kit with audit.resolve_recall_kit() and copies extract.py and recall_conf.py into its fixture. An import-only population therefore misses both, and the check could pass while a core check still degrades without recall. The degradation is named rather than silent (gotchas.py:1112 reports 'NOT resolved'), so the effect is contained: medium, not high. | sound | retirement-inventory-misses-readers-by-value |
| 18 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules row (the legacy homes on a shrink-only list) and the [policies] head paragraph | medium | medium | confirmed | dGroundRules' row (v2:1160) lists only gate-env.sh's `INHERITED_RED`, `INHERITED_RED_MAX_AGE` and `GATE_POST_MERGE` on the shrink-only list. On re-probe, .githooks/gate-env.sh assigns GOV_KITROOT (line 90), INHERITED_RED (103), INHERITED_RED_MAX_AGE (104), GATE_DOC_PATHS (108), GATE_WSL_MIRROR_DEFAULT (113) and GATE_WSL_PARITY_RUNS (114). GATE_POST_MERGE matches no line in the file at all. post-merge.sh:219-229 reads GOV_GATE_CMD, GOV_PYTHON and GATE_SELFTESTS from it. The [policies] head (v2:694) folds 'gate-env.sh's keys' with no qualifier, while dConvergedCharter (v2:1175, clause 12) folds only 'the legacy homes dGroundRules lists'. The head and the two rows disagree, and keys such as GATE_DOC_PATHS fall outside both the list and the fold. | sound | - |
| 19 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter row (the reader inventory by value, H6) | medium | medium | confirmed | dConvergedCharter's inventory (v2:1175, clause 12) is: transition_audit.read_modes, govkit's conf-key gap checks, kit.toml's `*_keys`, the kit-placeholders leg and the agent-cap parser. On re-probe, `read_policy_key()` is defined in four places: .githooks/pre-push:1303, tools/push-main.sh:404, tools/run-gates/post-merge.sh:168 and tools/unattended/unattended.sh:9380. tools/run-gates/held_halves.py reads the GATE_WSL keys. load_policy is used in roles_lib.py, check_roles.py, handoff.py and render_agents.py, which read house/policy.toml. Both of those homes are emptied by the same fold. v2 mentions read_policy_key only once, in dGroundRules' 'extending `read_policy_key`'s contract', and names none of the four copies or the roles readers. Once the fold lands, those readers would read a stale or empty home. | sound | retirement-inventory-misses-readers-by-value |
| 20 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dCalibratedLens row ('`REVIEW_ROUNDS` re-pointed at them') and [policies] `review.design.round-count` | medium | medium | confirmed | On re-probe, .unattended.conf:111 is REVIEW_ROUNDS="1". unattended.sh:774 sets RUNAWAY_CEILING="8", and :783 refuses REVIEW_ROUNDS at or above it. v2:787 gives `review.design.round-count` the allowed values 'a round count', with no upper bound. v2:1174 says only '`REVIEW_ROUNDS` re-pointed at them' and names no reader; 16 non-memory files reference REVIEW_ROUNDS. No dClosedLoop build record mentions the runaway ceiling. REVIEW_ROUNDS is also a kit conf key, so dGroundRules' rule 'every kit conf key the retrofit does not convert' and dConvergedCharter's fold reach it too. That gives three rows with no single owner of its fold. | sound | - |
| 21 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[front-door] ('The whole charter fits … Codex's 32 KiB') and [chain] dOrderedCharter ('the charter held inside 32 KiB'; 'budgets … extending `template-size-limits.txt`') | medium | low | confirmed | On re-probe, AGENTS.md is 16732 bytes against its row `AGENTS.md 20480` (template-size-limits.txt:85), and the template row is 49152 (:48), above the 32 KiB v2:669 promises. v2 says only 'budgets extend `template-size-limits.txt`' (line 208) and 'the charter held inside 32 KiB' (v2:1161), and names neither row. The re-founded charter carries 'the core principles, fixed' (v2:663) on top of today's text, so crossing 20480 is plausible. Two things contain the effect. The file lets a run of an owner-mandated build raise a measured-file row under its four conditions (lines 16-23). dOrderedCharter also plans its own 32 KiB hold, which covers the template row's slack. The defect is an unreconciled cap that would surface as a red gate at landing, so I grade it low. | sound | - |
| 22 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter row ('`compute_coverage` moved to `tools/lib` … with `map_lib.resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions` beside it') | medium | medium | confirmed | v2 is at blob 535c0e05. Its dOrderedCharter row (v2:1161) moves `compute_coverage` to tools/lib with `resolve_compare_base`, `derive_baseline_additions` and `drop_touched_exemptions` beside it, and names no consumer, re-export or re-copy. Running git grep outside memory/ found these consumers: gen_map.py:164, map_diff.py:112, selftest.py (524-539, 965-968, 1588-1617), test_codebase_map.py:141/161/165, and test_codebase_map.template.py:141/161/165. All of them call through `m.`, the map_lib alias. adopt-codebase-map.sh:207 is `cp "$HERE/test_codebase_map.template.py" "$GATE"`. One part is overstated: an adopter that has the gate installed also holds its own copy of map_lib, so its gate breaks only when map_lib is updated without the template. The gov-side break and the unnamed adopter path are real. | sound | - |
| 23 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease row ('a `kit.toml` for govkit and lib, today's kits reviewed') | medium | medium | confirmed | The dShippedRelease row (v2:1172) adds 'a `kit.toml` for govkit and lib, today's kits reviewed'. Neither descriptor exists today: `ls tools/*/kit.toml \| wc -l` printed 17, and tools/govkit/kit.toml and tools/lib/kit.toml are absent. Every consumer the finding cites matches the glob it quotes: regen.py:110 `*/kit.toml`, check-kit-placeholders.py:81 `*/*/kit.toml`, and run-gates.sh:1432 `"$_rg_tool"/*/kit.toml`. The same git grep, tests excluded, printed 20 files. Neither the row nor gap-mem-27 (register:168) says how a gov-internal lib descriptor is kept out of the installable-kit population. | sound | - |
| 24 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] heading | low | low | confirmed | `grep -nE '^## \[chain\]'` on v2 printed `1156:## [chain] The chain: fifteen builds, final rosters`. v2:431 says 'a sixteenth build, dGroundRules, lands ahead of both roots'. The heading's count is one short. | sound | - |
| 25 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules (H4 clause) against [presets] Rules | high | medium | confirmed | The H4 clause of dGroundRules (v2:1160) reads 'each key read as its catalogue default ... when the file is absent, malformed or missing the key'. [presets] Rules says 'The effective policy is the preset's assignment with the repository's overrides applied'. The two disagree for any key a preset assigns. The dDeclaredLoop row builds 'the named presets and their completeness check ... each shipped preset loaded', but no row changes the one reader's missing-key rule to consult the named preset. Built literally, a strict repository with no override reads `hooks.bypass` as `allowed` (v2:712 against the presets table). I grade it medium rather than high: [presets] states the intended rule, so the defect is a contradiction between two places in the spec, not a missing rule. | sound | - |
| 26 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules (H4 clause); [floor] | high | high | confirmed | v2:1160 treats a malformed file exactly like an absent one: catalogue default plus a recorded reason. The owner's RC-1, as the re-cut records it (recut.md:144), says only that the reader 'reads a key's default when the file is absent'. Extending that to a malformed file is v2's own choice, not an owner decision. The defaults loosen strict and guarded postures, `hooks.bypass` from refused to allowed and `core.bypass` from never to with-hooks-report. [presets] says loosening must never be a side effect. Neither the row nor [policies] specifies what happens to a value outside its allowed set. The path is narrow, a malformed landed file, and the consequence is a guard loosened without the owner's choice, so I grade it high. | sound | - |
| 27 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules (M7 clause: "the reader extending `read_policy_key`'s contract") | medium | - | refuted | The finding misreads what the reader extends. The clause reads 'the reader extending `read_policy_key`'s contract, read at the landed revision, never from the working tree, parsed and never sourced (M7)', and recut.md:151 confirms that M7 is about legacy homes and that revision and non-sourcing contract. tools/push-main.sh:399-403 describes the contract the same way: 'AS COMMITTED AT THE LANDED TIP ... Never the working tree'. Nothing in v2 says the TOML file is parsed by the KEY=value line function. The probe of the shell function on TOML shapes shows only that the function cannot parse TOML, which no row proposes. The TOML grammar and the reader's test classes are unit-level detail, absent by design until the chain build writes its specs. | unsound | - |
| 28 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules ("its JSON mirror"); [policies] head | medium | medium | confirmed | In v2 the mirror appears only at v2:691 ('mirrored to JSON for the hooks') and v2:1160 ('its JSON mirror'). v2 has two 'parity' hits, at 1161 and 1175, and both are about renderers, not the policy mirror. The walkthrough at lines 35 and 126 attaches the mirror to a parity leg, and v2 never carries that leg. The H4 and landed-revision contract names only the reader, so the hooks' read path has no rule for when the mirror is regenerated, how it is pinned, or what a hook does when the mirror is stale or absent. The effect is contained to hook enforcement drifting from the TOML reader. | sound | - |
| 29 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall (the `record` clause) and its Gaps owned cell (gap-mem-13) | high | medium | confirmed | v2:1165 (blob 535c0e05 verified) gives dTotalRecall 'the one `record` write command, which mints ids under the build's claim or lease'. Grepping v2 for compare-and-swap, claimant, ask family and refs/gov/claims finds nothing in the row. layer-memory [contract] (lines 320-334) says every ask minted outside a build, by entry.place, the owner, a surfaced idea, an expansion or the supervisor, mints under its family's claim ref. That ref is a counter advanced by a leased compare-and-swap, slug claim refs are never pruned, and 'dTotalRecall owes both refs (gap-mem-13)'. gap-register:154 says the same. So the row narrows its own owned gap and contradicts the contract it summarises. I grade it medium, not high, for three reasons: the row's first clause is 'the memory contract'; the same row's Gaps owned cell lists gap-mem-13, whose text spells out the fix; and the omission also leaves the row's clause-counted unit total short. | sound | - |
| 30 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dDeclaredLoop ("offline behaviour") and dTotalRecall (`record` mint); [policies] `leases.offline` | medium | medium | confirmed | Offline behaviour is defined only for lease acquisition. coordination.md:96-98 says an offline acquisition is recorded locally, pushed by compare-and-swap on reconnection, and yields if it loses. walkthrough C4 and v2:719/953 cover `leases.offline` alone. Grepping layer-memory for offline or unreachable printed nothing. flow-steps.md:76 gives `entry.claim` three outcomes: claimed, claimed under another key, and lease refused. None covers an unreachable remote. The ask-family counter's mint is also a compare-and-swap push with no offline rule. So under the default `warn`, the mint path either blocks or mints a local id, and the spec does not say which. | sound | - |
| 31 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter (the core-never-depends-on-an-optional-component check, M8 clause) | high | medium | confirmed | v2:1161 defines the P28 check's population as 'derived by `git grep` and seeded red on a planted import (M8)'. In the tree, the deferred imports (backlog.py:1796, gen_build_index.py:5002, merge-rows.py:262, transition_audit.py:178/708) are textual `import` lines that a grep would catch, and the row names those modules. corpus_ids.py:1145's `__import__` is a comment recording a staged break, not live code. Other routes into memory-recall do exist and are neither imports nor in the population: backlog.py:1791 `resolve_kit_dir("memory-recall", ...)` and check-verdict-epoch.sh:176's shell `resolve_kit_dir ... memory-recall`. The planted red proves only the plain-import shape. The check would therefore certify 'never depends' while dynamic, importlib and shell routes go unchecked. Both live non-import routes degrade gracefully when the kit is absent, so the consequence is contained: medium, not high. | sound | staged-break-substitutes-a-synthetic-value |
| 32 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dRankedPlan (RC-9 clause), dIndexedDesign, dScopedBuild and dShippedRelease against dCalibratedLens's ownership (PM-12) | high | high | confirmed | flow-steps.md:122 routes `plan.lease` 'held → `plan.recommend`'. Lines 123-124, 172-173, 220, 280-281 and 345 give every step's recommend and reason items to dCalibratedLens. In v2 [chain] (1169-1174), dCalibratedLens's parents are dTendedCadence and dFairHearing. It therefore lands after dRankedPlan, dIndexedDesign, dScopedBuild and dShippedRelease. v2:1170 even says 'the stage-exit recommendation being dCalibratedLens's (PM-12)' and gives no fallback. recut.md:184's reconciliation table lists only `entry.intake` as a dRankedPlan tolerance, with no row for any *.recommend item. Between those landings, each step's main path routes to an item no landed build implements. RC-9's own pattern shows the design treats this as a defect needing a fallback. | sound | - |
| 33 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine ("the prompt-submit hook writing each owner prompt ...", "RC-9's fallback drained") against `runtime.harnesses` | medium | medium | confirmed | layer-runtime.md:242 and 794-799 list Codex's events: PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd. Codex has no prompt-submit event. Codex is a registered adapter (layer-runtime:821) and `runtime.harnesses` selects among adapters (v2:764). v2:1167 drains RC-9's fallback once the prompt-submit hook lands, with no per-harness condition. flow-steps.md:71's `entry.intake` says no intake means 'no request mandate exists', and flow-steps.md:125's `plan.exit` under the default `plan.ratification: request` needs the intake record. A Codex-attended build thus has no ratification witness after the drain. The default harness is claude-code, which keeps this contained: medium. | sound | - |
| 34 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dRankedPlan (RC-9 fallback) and dWellOiledMachine ("Plan's ratification and the placement dispositions re-pointed to the intake record, RC-9's fallback drained") | medium | medium | confirmed | v2:1163 keeps the placement disposition in the claim commit 'until dWellOiledMachine's intake kind lands (RC-9)'. v2:1169 records the fallback witness as 'intake not installed'. v2:1167 re-points Plan's ratification and the placement dispositions to the intake record and drains the fallback. recut.md's RC-9 lines (135, 142, 184, 265) say nothing about builds whose dispositions or plan.exit predate the drain. P22 (v2:561-564) requires a recorded disposition whose facts are checked, with position derived from witnesses. A re-pointed reader that knows only the intake kind will not find those builds' dispositions. The spec leaves this migration unstated. The effect is limited to builds in flight across one landing. | sound | - |
