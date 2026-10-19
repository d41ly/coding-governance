# Skeptic return: run C, batch 4

**Serves:** research PLAY-dClosedLoop-1

Dispatch 195's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-36-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- C5-F16: confirmed medium
  Neither cl-dClosedLoop-0383 ("the derived-READY hand-off") nor cl-dClosedLoop-0384 ("the design index") names `design.handoff` or `design.overlap` (catalogue rows at v2:1158-1159, owned by dIndexedDesign). No other clause names either key. stage0-leads:155-156 agree. The only effect is that flow-steps:200 lists both under Design's policies.
- C5-F23: refuted
  At flow-steps:188 the Needs cell is "`design.overlaps`, where `design.streams` holds for the build". The only edge is to `design.overlaps`, and the second name is a policy condition, so stage0-leads:13's "cycle" is a parser artifact. The design map keeps item and policy-key as separate namespaces. `build.scope` is also both an item (flow-steps:237) and a key, and cl-0407 grades the check "by its value" with no ambiguity.
- C5-F18: confirmed low
  `review.build.when` (v2:1208, dScopedBuild) is named by no clause, and cl-dClosedLoop-0402 reads only "the closing review recorded". flow-steps has no item that reads the key either.
- C5-F5: confirmed medium
  cl-dClosedLoop-0406 hard-codes "in hunks under `retrofit.drain-cap`" and "claiming … under `retrofit.claim-cap`". No clause names `retrofit.drain` or `retrofit.claim-on-touch`. The preset row at v2:1571 gives velocity `carry` (header at v2:1345: velocity | standard | strict | guarded). retrofit:404-406 defines the `file` and `off` arms.
- C5-F17: refuted
  The ancestor clause cl-dClosedLoop-0115 (dDeclaredLoop, upstream of dScopedBuild through dIndexedDesign) already covers this. It gives one rework budget per build with "every repetition drawing on it, a route back, a fix pass…". It also makes "`flow.route-backs` the per-item early limit past which that item's loop ends non-converging and its open work goes to asks". The engine applies both to cl-0410's fix passes, so P39's single budget holds.
- C5-F15: refuted
  dTrueNorth's own clauses close both gaps when it lands:
  - gap-design-13 ("Nothing joins a design clause to the spec"): cl-dClosedLoop-0002 builds the carries join with its reds, and cl-dClosedLoop-0003 has memory hygiene "refusing a chain build's spec in progress while its build's coverage is red".
  - gap-build-07 ("never gated"): cl-dClosedLoop-0004 joins the deviation population "at the commit … and at the close … seen red on a planted revision after a pass with no record".
  - cl-0398 and cl-0412 only add the policy-keyed exits, so no gate is missing when dTrueNorth lands.
- C5-F12: confirmed medium
  cl-dClosedLoop-0419 is only "a derived runbook" and cl-dClosedLoop-0414 only "kit release notes", with no red case. final-questions:220 and 225 and research-final-help:129 say so, and final-questions [folded] (382-404) does not fold it. cl-dClosedLoop-0489 then migrates "the agent runbook … its reference half generated", so two builds derive the same document.
- C5-F11: confirmed medium
  None of `landing.order`, `deploy.runs`, `deploy.currency`, `kits.cadence`, `kits.host`, `kits.watch-cadence` or `commits.squash` appears in any clause. cl-dClosedLoop-0422 says only "landings ordered through the landing queue". The P21 row at v2:1705 relies on that clause. flow-steps:407 does say "ordered by `landing.order`", but no clause carries it. cl-0437 builds `commits.squash`'s three values without naming the key.
- C5-F3: confirmed medium
  The terminals conflict:
  - cl-dClosedLoop-0423: "a core red the landing merge introduced stops that build from closing (foundations K1)". Foundations:369-377 reads that as the build being unable to exit "until the red is fixed or excepted".
  - flow-steps:369 (`deploy.core`): "red → a patch build through the entry-point table's post-close row, and the close waits for its filing".
  - layer-flow:326-328 routes the same red through the post-close row.
- C5-F20: confirmed low
  cl-dClosedLoop-0430 reads "an update `kits.offer` offers runs neither in the adopter's tree … the adopter's own run of both". The pair (`adopt` and `test.seed`) is named only in cl-dClosedLoop-0427, and the hash pins the clause text alone.
- C5-F1: confirmed high
  The receipt never gets the fields the currency watch needs:
  - No clause carries a release tag or source remote. cl-dClosedLoop-0020 makes schema 4 "gaining `steps`", and cl-dClosedLoop-0435 makes schema 5 gain only `superseded`, `deprecations` and `prior_commit`.
  - layer-expansions:438 had placed "the release tag, the source remote" in schema 4.
  - Today's code at `tools/govkit/govkit.py:49` is `RECEIPT_SCHEMA = 3`, and line 8020 writes `"gov_source": str(root)`, a local path.
  - `kits.currency` (layer-expansions:454) reads gov's remote tag list with "unreachable → unverified, never green". With no source remote it has nothing to reach, so S4 reads unverified. gap-deploy-12 is carried by no clause.
- C5-F9: confirmed medium
  `maintain.host`, `maintain.cadence`, `maintain.events`, `maintain.reading-admission` and `observability.run-record` are named by no clause. cl-0443, 0445 and 0447 are bare phrases, and stage0-leads:129-130 shows run-record with no writer and no reader. One sub-claim is weaker than stated: layer-expansions:232 already limits `release-verify-failed` to "when integrations is installed", so the missing stand-in is a partial gap only.
- C5-F2: confirmed low
  The walker graded it high; the rubric grades it low (wording).
  - The wording defect is real: cl-dClosedLoop-0448 calls it "the memory's dead pointers", but `tools/check-dead-paths.sh:2` covers "nothing outside `memory/`".
  - The high consequences do not hold. The clause absorbs the script and keeps its merge-bar leg (owner NP-22, night-pass:755: "so a dead path still blocks a merge"). The script is an `[[exempt]]` row at `tools/govkit/registry.toml:242`, so no adopter install ever carried it, and no core-only install loses it.
- C5-F8: confirmed medium
  cl-dClosedLoop-0449 (dTendedCadence) delivers "Maintain and the Loop Review … as cadence steps". The items `loop.lease` to `loop.record` (layer-expansions:253-262) and `record-kind.loop-review` (design-map:290) belong to dCalibratedLens, a descendant, and cl-0460 builds the Loop Review again.
- C5-F7: confirmed medium
  cl-dClosedLoop-0460 fixes "the weekly Loop Review", and `review.loop.cadence` (v2:1213) is named by no clause. The `budgets.*` half is weaker: cl-0015, 0041 and 0064 read `budgets.enforce` and `budgets.pinned`, and cl-0461's "caps re-derived" is in substance the `budgets.*` row's default.
- C5-F6: refuted
  Re-derivation cannot be applied directly:
  - It is `loop.propose`'s ("re-derives the caps"), whose only route is `loop.file`, into Plan's triage and "the owner's breakpoint" (layer-expansions:260-261).
  - The `budgets.*` row (v2:1217) makes each cap's value "the owner's".
  - The ancestor cl-dClosedLoop-0116 makes "raising the budget the owner's alone".
  - cl-dClosedLoop-0118 reads "a raise of a loop bound … as a loosening that waits for the owner".
- C5-F4: refuted
  - cl-dClosedLoop-0392 already makes `check-playbook` "Design's pack" in dIndexedDesign, long before convergence.
  - Fates:151 marks it RESHAPED into that pack.
  - cl-dClosedLoop-0488 runs "every part in the fates table at its fate" as convergence's exit check, so a builder who retired the leg under cl-0486 would turn that check red.
  - The code facts hold: the leg argv is `{prefix}/unattended/check-playbook.sh`, and the recorders are at unattended.sh:29-30.
- C5-F22: confirmed low
  cl-dClosedLoop-0488's population leaves out `memory/` and root dotfiles. Fates:210 has "hand-written guides | RETIRED", and fates:158 covers `.unattended.conf`. A surviving guide or conf matches no file in the population.
- C5-F21: confirmed medium
  cl-dClosedLoop-0438 proposes "the house file's efforts as `roles.effort.*` values" for the owner "to rule once" (flow-roles-adoption:264). cl-dClosedLoop-0495 later folds "a repository's efforts … into the `roles.effort.*` policy keys … with an upgrade step". Nothing in cl-0495 reads a prior ruling or a declined row.
- C3-F23: confirmed low
  No clause from 0238 to 0261 mentions gap-mem-11's records or gap-mem-12's follow-through test. Searching all clauses for follow-through, ANNOTATION-STYLE or `note` finds only cl-0241's grammar. layer-memory:1226 also gives gap-mem-12's threshold to dTotalRecall, not to the owner dLinkedLibrary.
- C5-F10: confirmed medium
  A search of every clause for the five signals, `reading-tree` or the remote-CI signal finds only cl-0277, the two lexicon signals. gap-maint-09, 10 and 11 (gap-register:427-429) are owned by dTendedCadence and carried nowhere.
- C3-F15: confirmed medium
  gap-mem-23 is owned by dTotalRecall, but the touch-drop is wired by cl-dClosedLoop-0407 (dScopedBuild, a descendant), which calls `drop_touched_exemptions`. No dTotalRecall clause mentions it. In the working tree `--drop-affordance-exempt` appears only in `tools/codebase-map/map_diff.py` and its README.
- C2-F1: confirmed blocker
  `cl-dClosedLoop-0093` is missing:
  - Parsing [chain] gives 495 ids, and the one missing number is 0093.
  - v2:1707 `| P23 | cl-dClosedLoop-0093 |` is the only occurrence of the id.
  - [clause-ids] says "Retired: none".
  - walk:893 and walk:1081 still list "claims keyed and trusted by key and source".
  - stage0-leads:201 reads 496 clauses.
  - The design's own K5 rule (v2:1679) turns red on "an id no clause carries", and P23 has no enforcing clause.
- C3-F28: confirmed medium
  v2:1713 names only cl-0178 for P29. P29 (v2:866-881) also covers verifiers, answered calls, false facts and "Recall: recall is re-verified once, by the orientation scout at entry". cl-0196, 0197 and 0198 carry three of those rules but sit in no row, and no clause carries the recall re-verification.
- C4-F4: confirmed medium
  flow-steps:81 gives `entry.intake` "orientation scout … the intake entry the scout writes". Against it stand the same record's amendment at flow-steps:796 ("`entry.intake` is a hook"), its Owner note at flow-steps:99, layer-roles:414 ("| hook | `entry.intake` |") and cl-dClosedLoop-0282 (the prompt-submit hook).

- cl-dClosedLoop-0265 dMindYourWords: holds
- cl-dClosedLoop-0069 dFairHearing: holds
- cl-dClosedLoop-0096 dDeclaredLoop: holds
- cl-dClosedLoop-0154 dKeptSession: defect
  - **CS4-F1: The policy namespaces' purposes are reviewed under a key no ancestor of dKeptSession registers**
  - **Address:** architecture-v2 [chain] cl-dClosedLoop-0154
  - **Class:** K6
  - **Severity:** medium
  - **Evidence:**
    - cl-0154: "the policy namespaces' purposes, reviewed".
    - project-map:660-666: an existing node is reviewed "under `memory.map-purpose: review` (PM-5)" by "the unit that adds its namespace's purpose field".
    - v2:1248: `memory.map-purpose` is owned by dTotalRecall.
    - dKeptSession's parents are dDeclaredLoop and dPlacedRequest, and dTotalRecall is neither its ancestor nor its descendant.
    - project-map:668 covers only "Builds after dTotalRecall".
    - project-map:657 still names dDeclaredLoop as the owner of the policy namespace's purpose.
  - **Consequence:** A dKeptSession spec carrying the clause has no review rule and no ask route, and it may land before the key exists.
  - **Fix:** Name `memory.map-purpose` in cl-0154 with a stand-in until dTotalRecall lands, or move the review to cl-0227's reviewers. Correct project-map:657.
- cl-dClosedLoop-0196 dFurnishedOrders: holds
- cl-dClosedLoop-0405 dScopedBuild: holds
- cl-dClosedLoop-0077 dFairHearing: holds
- cl-dClosedLoop-0415 dShippedRelease: defect
  - **CS4-F2: `deploy.unlease` is built without its mailbox close, and no clause carries copy-before-prune**
  - **Address:** architecture-v2 [chain] cl-dClosedLoop-0415
  - **Class:** K1
  - **Severity:** medium
  - **Evidence:**
    - cl-0415 builds `deploy.unlease` "closing each of a build's leases with a terminal tombstone" and says nothing of the mailbox.
    - flow-steps:376's item "closes its mailbox".
    - flow-steps:55-59: "every message still on its mailbox ref, disposed or not, is copied into the build folder, and the undisposed ones are marked … Only then is the ref pruned".
    - Searching all clauses for mail together with prune, copy or unlease finds nothing. cl-0143 says only "kept in the build's transition log".
  - **Consequence:** A builder of the clause may never close the mailbox, or prune the ref without copying, and lose undisposed messages. `life.unlease` has the same gap.
  - **Fix:** cl-0415 adds the mailbox close, with copy-before-prune and undisposed messages marked. Plant a build with an undisposed message, unlease it, and see the copy in the folder and the ref pruned only after it.

- **Read outside the list above:** none. I parsed the copy's [chain] into `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c4/clauses.tsv` and wrote nothing else.
