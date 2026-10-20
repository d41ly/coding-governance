**Serves:** spec-audit PLAY-dClosedLoop-1

# Whole-design walk, run C: by clause, the chain in five build ranges

Run C walked the 495 clauses of architecture-v2's `[chain]` in the sealed copy, each clause read against the records that settle it. The slicing is by clause, in five contiguous ranges of the chain's builds. Walker 1 took dTrueNorth to dOrderedCharter (cl-0001 to cl-0067). Walker 2 took dFairHearing to dKeptSession (cl-0068 to cl-0165). Walker 3 took dBoundRoles to dMindYourWords (cl-0166 to cl-0278). Walker 4 took dWellOiledMachine and dWitnessedBar (cl-0279 to cl-0368). Walker 5 took dRankedPlan to dConvergedCharter (cl-0369 to cl-0496). Four skeptics judged every walker finding in batches against the sealed copy, and each also re-walked a sample of clauses the walkers had passed. The synthesizer merged the nine returns into this report.

Subjects (round 1): memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md@418fc28cd47de2822db04eac3b86b7ca32bc7c31, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md@1888108d8da6848d19fb7cebb5f0446115ede751, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@b2dc2bca27f017876a1d64dd4976d3d4b27cb7ff, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99baf25aff315499fff75802dc3955, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md@027870b06e2c5808f196f4b15c515759be1821d3, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d0d0600136c20fd3fa22707b1abf1, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md@9f71f3d8e3b4b7ce34de6eaca7e4d8b2617e25ba, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md@01191e8514e8de36c304b9666462a016b9ae6598, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@460f54f6029a31c8104945ebac3a09de69b2d0af, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md@19388061eefc1757f9d215fe21222c17df8e3c5a, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md@e29e16d7bdb16df243611f6556fd3867d628b269, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md@b863d10c4aef7b07b306908108896d4d7433a6ca, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md@e61a5385821e344f6c1f1def5f0c989d1d5b517c, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview.md@c705dfd0c158de05379a6fad9299262fdeaf7e3d, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb39652a06061e8003caba48e618608b6a, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@c0731e8012bb22ee09323c0666a60424acacba55, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md@4976ef59117706e725b6a55e315daf125c9467d0, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md@57668e157e4100899208a3f2748c821db8346122, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md@e1906ced6ff9f3cc715719f752bb081bdd6d6924, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md@87a43459f2da84bd898f98a7c293b733c7f4f8ae, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@727ac3275eedf14ac37799f3fcefb12e70bf65a3, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md@d5c9c48072ea05c225c936617706d3de7973d499, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md@1254230e9a3acbc991a5585c8b1df561ecdcebb3, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md@e6948cd9cfa0e92958ac235c7db140e6bc1dba76, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md@3df38b0db51dfb353bdfc85f7905c5d8cc25dfef, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-state.md@ac95fcc269b34b03c5aef82161a86ea19274d378, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md@c679e0036b167f235a50b939224b8353b567e9ea, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md@ff10212477bcf48c713763c474e7e83637654236, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md@4dcb6aac62ce575704a32b75606c3a6dd5a5c2f8, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md@bc4c57e94062eb8dc81432d52b5347592661defd, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md@779d0f66eae7bc532e824af5d3530a7c3620f178, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md@5b0cb48caa25afe7b971262fd24b58a283b2030a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md@1cd205c67945e28c07bb39868cb18088419128c9, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md@ea3fa8ddee7804e6e80add05244c2560291b270e, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md@3655e28ccc77a0f592f0741b98281c8fbfe01f49, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md@1a192df98ba1010a56e646ca81451087395f7b49, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md@4f5e5809f6963500318ddc148fdfbaad02a87635, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md@ee6a9c11f18b693385636d30271b376f1037d865, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-population.md@015612d5b05d7bfcf12311a8306b87cd256a91c8, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-skeptic.md@94dfe381fe5f69d118d78fc913069a979c54873a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md@281a9b9526fcbb6a693c77c08925f9486e5e29ff, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md@7d11112ecee1c951389e70b057d2d33b4b1cdf88, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md@97edc2cf70309578889275494a710fddaf6f09fb, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md@35ef3eee6cc3285680e0ecae47668fb2dc3b8045, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md@07ce17290998aeb22b366cd27f11df0fa7b1558f, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md@a0c305c114b455f44977f4ecb7beee0d07483c53, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md@1720bf7555d336f9f8f1412bf7af7ed8ad0f2891, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b44c773093d661eb911f30c36f753254f, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md@6475aa368904b5a8cb8fb84a21382f9dd6958766, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md@c3c92f39e71a0ed06d6455e1f248ac50a05bcf60

## Verdict: BLOCKED

Eleven findings are critical: C2-F1 (blocker, c5), C1-F1 (c3), C1-F2 (c1), C1-F3 (c1), C1-F5 (c3), C2-F2 (c2), C3-F13 (c3), C3-F17 (c3), C4-F1 (c2), C4-F2 (c1) and C5-F1 (c2). A high finding counts as critical here only where its walker or skeptic tagged a rubric consequence. C3-F14 and C4-F3 are high with no such tag, so they sit under High. The run raised 108 findings: 95 confirmed and 13 refuted. The confirmed findings are 1 blocker, 12 high, 64 medium and 18 low. Five of the confirmed findings (CS1-F1, CS2-F1, CS3-F1, CS4-F1 and CS4-F2) were raised by the skeptics themselves, on clauses the walkers had passed as holding. No second skeptic judged those five.

## Critical

### C2-F1 — Clause `cl-dClosedLoop-0093` is missing, so P23 is enforced by a clause that does not exist and gap-orient-05 is carried by no clause
- **Address:** architecture-v2 [chain], dDeclaredLoop row, between cl-dClosedLoop-0092 and cl-dClosedLoop-0094; architecture-v2 [enforcement], row P23
- **Class:** K5, c5
- **Severity:** blocker
- **Evidence:** [enforcement] (v2:1707) reads `| P23 | cl-dClosedLoop-0093 |`, the id's only occurrence. [chain] carries 495 distinct ids, 0093 is the one number missing, and [clause-ids] says "Retired: none". The walk record still lists "claims keyed and trusted by key and source" in dDeclaredLoop's roster (walk:893, walk:1081). P23 lets a claim be acted on only when its stored key recomputes equal and its weakest source is not agent-typed. dDeclaredLoop owns gap-orient-05 ("Claims carry no freshness keys"), and only cl-0092's "each claim's key and verdict printed" touches claim keys.
- **Consequence:** dTrueNorth's carries join and Stage 0's K5 go red on an id no clause carries. No dDeclaredLoop spec builds the trust-by-key rule, so the card, the position engine and every claim reader act on stale or agent-typed claims, the failure gap-orient-05 measured (4 of 17 run claims disagreed).
- **Fix:** Restore cl-dClosedLoop-0093, "claims keyed and trusted by key and source", between 0092 and 0094. Give it its seen-red arm: a planted claim whose key no longer recomputes, and one whose weakest source is agent-typed, are each re-derived and never acted on.
- **Skeptic:** confirmed blocker. Parsing [chain] gives 495 ids with 0093 the only gap, v2:1707 is the id's only occurrence, Stage 0 read 496 clauses on the working tree, and the design's own K5 rule (v2:1679) reds an id no clause carries.

### C1-F1 — The unit registry leaves out `required-by`, so the missing-unit refusal has nothing to read
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0039, read with cl-dClosedLoop-0041
- **Class:** K6, c3
- **Severity:** high
- **Evidence:** layer-instruction R-A lists the unit row's fields, including "`required-by`: the roles and items that require it, which R-C's 'too little' refusal reads", and systems [design-instruction-writing] lists `required-by` and `enforced-by`. cl-0039's field list copies R-A item for item except `required-by`, and [chain] has no hit for `required-by` at all. cl-0041 and cl-0015 still refuse "a load set missing a required unit".
- **Consequence:** The P27 load-set check has no declared list of required units, so it stays green over nothing or the builder invents the field. adopter-instructions item 6's exclusion refusal ("one another active unit requires") has nothing to read either.
- **Fix:** Add `required-by` and `enforced-by` to cl-0039's fields, and make cl-0041 read `required-by`. Plant a red: a unit named in `required-by` that is missing from a load set.
- **Skeptic:** confirmed high (c3). cl-0039 copies R-A (layer-instruction:383-393) except `required-by`, and no clause registers it.

### C1-F2 — Re-founding the charter breaks the roles kit's reader of the section-1 rule tags
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 (also cl-0042 and cl-0043)
- **Class:** K10, c1
- **Severity:** high
- **Evidence:** layer-instruction R-B requires that retiring a section number re-points its readers in the same unit, naming `roles_lib.py`'s `SECTION_ONE_RE` and the harness prompts that grade by section number. R-D reds a numbered heading. `tools/roles/roles_lib.py:61` is `SECTION_ONE_RE = re.compile(r"^## 1\. ")`, and lines 193-205 raise R0 when there are neither section-1 rule tags nor `## §<n> — ` headings. No [chain] clause carries the re-point; the only `roles_lib` clause is dConvergedCharter's `load_policy`.
- **Consequence:** The level-0 charter has no `## 1.` heading and cl-0042's grammar reds one, so every role render fails with R0 and dOrderedCharter cannot land green.
- **Fix:** In cl-0032, re-point `SECTION_ONE_RE` and the roles `rules:` join to the practice units' tags in the same unit, along with the harness prompts that grade by section number. Prove it with a role render on the re-founded charter.
- **Skeptic:** confirmed high (c1). layer-instruction:438-440 requires the same-unit re-point, no clause carries it, and the roles render legs are on the bar (`gate-legs.json`: "roles render wiring", "roles render selftest").

### C1-F3 — Three guard-bearing `tags.*` keys owned by dOrderedCharter have no reader, so cl-0014's arm goes red when it lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049 (also cl-0040 and cl-0059)
- **Class:** K4, c1
- **Severity:** high
- **Evidence:** The v2 catalogue (v2:1220-1223) gives `tags.slice`, `tags.retired-cites` and `tags.bare-refs` the Owner dOrderedCharter. systems [design-tags] uses them for `gov tag show`'s leaf slice, the `retired` check and the `resolves` check. None of the three appears in any clause. cl-0049 names only "one resolver (`gov tag show`, `where`, `refs` and `check`) … the `tags` leg pack". cl-0014 is "an arm red when a key whose Owner build has landed has no reader".
- **Consequence:** At dOrderedCharter's landing, dGroundRules' own arm goes red on three keys. If the build lands anyway, `refuse-new` on retired cites and the `never`/`unique` bare-reference rules exist only as catalogue values.
- **Fix:** In cl-0049, name the `resolves` check under `tags.bare-refs`, the `retired` check under `tags.retired-cites` and `gov tag show`'s slice under `tags.slice`, each value with its planted case.
- **Skeptic:** confirmed high (c1). None of the three keys appears in any clause, so cl-0014's arm reds at dOrderedCharter's landing.

### C1-F5 — dGroundRules retires an adopter's `FANOUT_CAP` before any upgrade step exists, silently raising a lowered limit
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0016
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** cl-0016 retires "agent-cap's slot ledger … with `.agent-cap.conf`", and v2:1003 retires `FANOUT_CAP` into `runtime.agents-in-flight`, whose default is 6 (v2:1089). P38 requires an upgrade step, but the step kind (cl-0018) and the first step (cl-0028) arrive in the child dSafePassage. `tools/hooks/agent-cap.js:68-72` honours a repo-lowered `FANOUT_CAP` in a tracked `.agent-cap.conf`.
- **Consequence:** An adopter that set `FANOUT_CAP=2` updates and is held to the default of 6. Its own limit is loosened with no step, order or warning.
- **Fix:** In cl-0016, translate a present `FANOUT_CAP` into `runtime.agents-in-flight`, or hold the conf as a read legacy home, until dSafePassage ships the step. Plant `FANOUT_CAP=2` and check it still caps at 2.
- **Skeptic:** confirmed high (c3). No clause translates an adopter's lowered value.

### C2-F2 — Two of `flow.on-exhausted`'s endings lead to states the transition table does not have
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0116 (with cl-dClosedLoop-0098 and cl-dClosedLoop-0100)
- **Class:** K2, c2
- **Severity:** high
- **Evidence:** cl-0116 gives `park-for-owner` and `close-incomplete` ("closing the build incomplete with its branch and records kept"). flow-steps [transitions] (fs:617-654) refuses any transition the table lacks, has no row from an open state on budget exhaustion, and lists no incomplete or parked-for-owner terminal. Its only parked state, `paused`, is reached only by `life.request`. cl-0100 builds only the declared terminals, and P20 requires a build to end in one. The strict preset sets `park-for-owner` (v2:1452), and cl-0328 also speaks of "a parent ending incomplete".
- **Consequence:** A build that exhausts its budget under `close-incomplete`, or parks under strict's `park-for-owner`, asks for a transition the engine refuses. cl-0118's termination check finds no terminal, and the scenario ends with no terminal and no witness.
- **Fix:** Add rows that cl-0098 and cl-0100 carry: any open state → `incomplete` (terminal) on the exhaustion record, and any open state → `parked-for-owner` with the owner's disposition as its exit. Seed cl-0116's planted endings from those rows.
- **Skeptic:** confirmed high. The ending is real and the table has no row for it.

### C3-F13 — The map's losing replay has no loss conditions
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0228
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** project-map [test] (pm:699-702): "The map loses, and is not built, if any of these holds: the recall of the known set rises by less than the twin runs' difference plus 5 items; the median of existence searches per lens falls by less than one; the bytes read before the first act rise by more than the map's own bytes". cl-0228 says only "the replay with the map and without at its first unit … so a losing map is never built". cl-0253 extends the same undefined test to code.
- **Consequence:** "Losing" is undefined, so the replay certifies the map whatever it scores, and the routed loss path never runs.
- **Fix:** Carry the three loss conditions, and the twin runs they compare against, in cl-0228 and in cl-0253's extension.
- **Skeptic:** confirmed high.

### C3-F17 — The reuse scout's acceptance re-runs the benchmark with no threshold
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0239
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] (lm:717-718): the acceptance "re-runs aScoutedSeam's 24-case benchmark against the built index and entries, and must meet M1c's 16". research-scoutedseam-apply measured m1c at 8/12 on the held-out set. cl-0239 re-runs the benchmark and its twelve held-out cases with no bar.
- **Consequence:** The acceptance passes at any score, so a house index that loses to today's 13/24 checklist scout ships.
- **Fix:** Put the pass bar in cl-0239, on the tuning set and on the 12 held-out cases.
- **Skeptic:** confirmed high.

### C4-F1 — The unattended-kit dissolve retires the supervisor's own seam and removes the tick that hosts it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0306
- **Class:** K10 (a migration across a drain), c2
- **Severity:** high
- **Evidence:** cl-0306 retires "`resume-tick.sh` and the `RESUME_SCHEDULE_*` task … with an adopter's hand-registered resume task removed". cl-0284 says the opposite: "the supervisor: `resume-tick.sh` grown, started and restarted by the node tick". layer-runtime [supervise] (357-371) keeps the OS-scheduled `gov-resume-tick` registration as what starts the supervisor, refuses a run host without it at preflight, and retires only `RESUME_SCHEDULE_*`. Fates rows 145-146 mark `resume-tick.sh` RESHAPED into the supervisor and `RESUME_SCHEDULE_*` RETIRED. `tools/unattended/README.md:211,218` shows that `gov-resume-tick` is the hand-registered resume task.
- **Consequence:** The upgrade step deletes the supervisor's script and the node tick that starts and restarts it. Every run host then fails preflight, and the `host` fixture cannot pass. A crashed or rebooted supervisor never comes back, so unattended builds stop short of a terminal.
- **Fix:** In cl-0306, retire only `RESUME_SCHEDULE_*` and resume-tick's `--dangerously-skip-permissions` launch. Keep `resume-tick.sh` as the supervisor's seam (cl-0284), and keep the `gov-resume-tick` registration as the node tick, re-pointed rather than removed.
- **Skeptic:** confirmed high. cl-0306 contradicts cl-0284 and layer-runtime [supervise].

### C4-F2 — The shared bash resolver accepts only MINGW or MSYS, which refuses every bash on Linux
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0364
- **Class:** K10 (a trust boundary and portability), c1
- **Severity:** high
- **Evidence:** cl-0364 accepts a candidate "only once it runs and answers `uname -s` as MINGW or MSYS … and a refusal in place of any fall-back", with no Windows scope, while claiming to keep the existing resolvers' contracts. away-pass [p4-compat] (line 174) puts Windows with Git-Bash and Linux at tier 1, and cl-0315 plans for Linux nodes. The existing resolvers accept by run probe, not by MINGW: `tools/govkit/govkit.py:1138` runs `-c :`, and `tools/run-gates/profile_bar.py:282` runs `test -f`.
- **Consequence:** On any Linux node `uname -s` prints `Linux`, so every gov launch site refuses. The bar, the hooks and the lander cannot run there, so builds cannot land from a tier-1 platform.
- **Fix:** Scope the MINGW/MSYS acceptance to a Windows host (`os.name == 'nt'`). Elsewhere, accept a candidate that runs and meets the bash floor, and add a Linux arm to the staged-break fixture.
- **Skeptic:** confirmed high.

### C5-F1 — The receipt never gains the release tag and source remote that the currency watch reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0435
- **Class:** K6, c2
- **Severity:** high
- **Evidence:** layer-expansions:438 put "the release tag, the source remote" in receipt schema 4, and `kits.currency` (layer-expansions:454) joins the receipt to gov's remote tag list, with "unreachable → unverified, never green". After the schema renumbering, cl-0020 gives schema 4 only `steps`, and cl-0435 gives schema 5 only `superseded`, `deprecations` and `prior_commit`. No clause carries a release or source field. Today `tools/govkit/govkit.py:49` is `RECEIPT_SCHEMA = 3`, and line 8020 writes `"gov_source": str(root)`, a local path.
- **Consequence:** gap-deploy-12, which dShippedRelease owns, is closed by no unit. cl-0417's currency watch has no installed release to count from. In S4 (an adopter two releases behind) the currency record reads unverified, and `currency.on-behind` never fires.
- **Fix:** Add `release` and `source_remote` to cl-0435's schema-5 fields, and name `kits.currency` as their reader. Plant a receipt with no release tag and see it red.
- **Skeptic:** confirmed high.

## High

### C3-F14 — Renaming the Serves kind `journal` to `log` ships with no adopter alias step
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0231 (with cl-dClosedLoop-0229)
- **Class:** K10
- **Severity:** high
- **Evidence:** memory-plan [integration] and [migration] (memory-plan:293, 297, 331) require dTotalRecall's adopter upgrade steps to include "the `journal` alias", and read the `journal` kind through it. cl-0229 renames the kind. cl-0231's steps list the scaffold verbs, the README front-matter grading and the retag step, but no alias.
- **Consequence:** After an update, an adopter's records carrying `**Serves:** journal` fail the Serves grading or lose their kind, against P38. gov itself holds 1,443 such records (memory-plan:125).
- **Fix:** Add the `journal` alias upgrade step to cl-0231, seen on a planted adopter record with `Serves: journal`.
- **Skeptic:** confirmed high. The count is 1,443, not the walker's 1,436, which does not change the finding.

### C4-F3 — The default load is replayed through a hook channel smaller than the map, and no clause carries the owed cap measurement
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0301 (also cl-dClosedLoop-0290)
- **Class:** K10
- **Severity:** high
- **Evidence:** cl-0301 has the session-start hook load "the card and the map by default … at a compaction", and `memory.map-budget` defaults to 32k. night-pass-two (line 401) says the harness keeps 10,000 characters of hook context and "past them text is silently lost". v2 [owed] gives the level-0 map as 31,203 of 32,768 B, and owes the compact and resume hooks' output cap "measured with a 32 KiB map" (night-pass [p5-compaction] item 4). layer-runtime (line 1022) lists "the card's size check". Neither cl-0290 nor cl-0301 carries the measurement or the size check.
- **Consequence:** After a compaction the map is cut to about a third of its size, and nothing reports it. gap-orient-18's fix ships without restoring the map, and the session works from a partial map it does not know is partial.
- **Fix:** Add to cl-0301 the owed measurement of the hook channel's cap against a 32 KiB map, and a size check that routes the over-cap remainder through an instruction-file channel or fails red. Add the card's size check to cl-0290.
- **Skeptic:** confirmed high.

## Medium

### C1-F6 — The inventory of by-path readers for the moved grammar misses readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0048
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0048 builds "from an inventory of every reader of `extract.py` and `recall_conf.py` by path", and names check-verdict-epoch.sh, migrate_backlog.py and merge-rows.test.sh. `grep -rln 'extract\.py\|recall_conf' tools skills .githooks` also finds `skills/session-kickoff/manifest-check.test.sh:1325-1328` (it hides `extract.py` and expects the "id grammar lives in the memory-recall kit" NOTE), `.githooks/straggler-guard.test.sh:84` and `tools/unattended/check-unattended.sh:2035`.
- **Consequence:** After the move, the kickoff F1 arm hides a file that no longer holds the grammar. It either goes red on the bar or passes without testing the no-grammar path.
- **Fix:** Derive cl-0048's inventory from that grep and name every reader it finds. Each one gets re-pointed and its arm re-seen red.
- **Skeptic:** confirmed medium. The grep finds the three cited readers and others besides, such as `transition-audit.test.sh`.

### C1-F8 — Clause ids and the spec's `Carries` relation are registered as no address form or edge, and collide with the `carries` edge
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0001, read against cl-dClosedLoop-0058
- **Class:** K6
- **Severity:** medium
- **Evidence:** P33 addresses a node by "a tag, a section or a native id whose class is registered with its owner", with "typed edges from one closed set". cl-0058 registers native-id classes ("FAMILY-<slug>-<seq>", and later classes by the build that brings them) and pins only as `<tag>@<hash>`, legal only as an `amends` or `supersedes` target. memory-plan [frame] adds "no other edge carries a pin", and memory-plan:193 defines `carries` as "landing → unit, commit". cl-0001 parses `**Carries:** cl-…@<hash8>` lines, and no clause registers `cl-` ids.
- **Consequence:** Once the edge checks land, every chain spec's Carries line and every deviation pin either goes red or stays outside the closed set, as a prose relation P34 forbids.
- **Fix:** In cl-0058, register `cl-<slug>-NNNN` as a native-id class owned by dTrueNorth, with its `@hash8` pin form. Rename the spec relation (for example `carries-clause`), or widen `carries`'s from/to rows.
- **Skeptic:** confirmed medium. Nothing types the spec→clause relation, so it either clashes with `carries` or sits outside P33/P34's closed set.

### C1-F9 — The deviation record has no home or writer, and lacks fields its settling record sets
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0004
- **Class:** K3
- **Severity:** medium
- **Evidence:** final-questions [deviation] sets the record's fields: "its id; the hand-off; … the approver and where the approval is recorded; … and its cause (P35)". cl-0004's fields are "the departure's address, before and after, cause class, reason, evidence, risk class, approver and follow-through". The id, the hand-off, the approval's location and the cause are missing, and no home or writer is named.
- **Consequence:** The record has no home or door, and a spec built from the clause lacks fields the design settled.
- **Fix:** Give the record a home and a writer in cl-0004, and add the id, the hand-off, the approval location and `caused-by`.
- **Skeptic:** confirmed medium, narrowed. cl-0004 does register the kind ("joined to check 21's kinds"), and cl-0006 reads the record. The by-risk join reads the risk class and the approver, both present, so the missing hand-off does not stop it picking the approver. The unnamed home and writer and the missing fields stand.

### C1-F10 — The re-founded charter leaves out the core principles and the decision principles that outrank practices
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:** v2 [front-door] lists "the core principles, fixed; the decision principles that resolve unattended forks …, which outrank the practices". cl-0032's envelope list (front door, precedence and override rule, instruction map, active practices, hand-off to the loop, project block) leaves both out, and no clause names decision principles. gap-flow-02 ("nothing ranks them above the charter's adjustable practices") is dOrderedCharter's. P18's only enforcing clauses are cl-0176 and cl-0390 (v2:1702).
- **Consequence:** gap-flow-02 is owned but closed by no clause, and P18's ranking over practices never reaches the charter.
- **Fix:** Add the fixed core principles, rendered from cl-0037's registry, and the ranked decision principles to cl-0032's envelope list.
- **Skeptic:** confirmed medium.

### C1-F11 — gap-found-18, the `up —` micro-format that asks for a password, is owned by dOrderedCharter but carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:** layer-expansions:506 records gap-found-18 ("The `up —` micro-format asks for a password value, inviting a secret into chat") under dOrderedCharter, and it is in the build's Gaps owned cell. No clause mentions the micro-format, a password, or keeping credentials out of it. cl-0003's coverage report counts clauses and owned nodes, not gaps, so nothing checks that the gap is carried.
- **Consequence:** The re-founded charter keeps a micro-format that asks for a secret in chat, against the charter's [security] rule.
- **Fix:** In cl-0032 or cl-0042, rewrite the `up —` micro-format to name where a credential lives, never its value. Add a grammar red on a micro-format that asks for one.
- **Skeptic:** confirmed medium.

### C1-F12 — The override record and the exception register have no home, writer or door
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 and cl-dClosedLoop-0037
- **Class:** K3
- **Severity:** medium
- **Evidence:** foundations has the agent record each override ("the rule it set aside and the owner's words"), and every exception "carries its principle, the part it excuses and a reason". layer-memory:399-400 registers both kinds under dOrderedCharter with "writer item not named". cl-0032 and cl-0037 name no home or writer, and memory-plan [doors] lists neither.
- **Consequence:** Both records lack the one door P30 requires before dTotalRecall lands, and the Loop Review's audit of the exception register has nothing to read.
- **Fix:** Have cl-0032 and cl-0037 name each record's home, fields and writer, as stand-ins that dTotalRecall's registry adopts.
- **Skeptic:** confirmed medium, narrowed. Both kinds are registered, so the walker's "no kind" is wrong. The missing writer, home and door stand.

### C1-F13 — Cap values have two homes, and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015 and cl-dClosedLoop-0041
- **Class:** K4
- **Severity:** medium
- **Evidence:** The catalogue (v2:1217) and night-pass-two [p5-caps] (406-407) put each cap's value under `budgets.*`, the owner's. cl-0015 reads "each cap's value … from its one declaration" without naming it, and cl-0041 extends `template-size-limits.txt`. Stage 0's K4 lists `budgets.*` as unread. cl-0461 ("caps re-derived from evidence"), dCalibratedLens's only cap clause, does not name the key either.
- **Consequence:** Load-point caps are declared in `template-size-limits.txt` while the catalogue puts them under `budgets.*`. That is two answers to one fact, and the owner's policy write moves nothing a gate reads.
- **Fix:** Have cl-0015 name the one declaration: either `budgets.*`, with `template-size-limits.txt` migrated into it, or `template-size-limits.txt` alone, with `budgets.*` re-scoped to name it.
- **Skeptic:** confirmed medium.

### C1-F14 — dGroundRules' witness needs load sets and a composition that only dOrderedCharter builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0015 is "seen … on a load set missing a required unit and a composition over a harness's own limit, both still refused under `warn`". Load sets are cl-0041's and the composition is cl-0064's, both in the descendant dOrderedCharter.
- **Consequence:** dGroundRules' acceptance cannot be run when it lands.
- **Fix:** Plant today's consumer limit at dGroundRules (`CODEX_MAX=32768`, `tools/agent-instructions/adopt-agent-instructions.sh:31`), and move the load-set and composition cases to cl-0041 and cl-0064.
- **Skeptic:** confirmed medium. The consumer limit exists today at the cited line.

### C1-F15 — `install.retired-edits`' `keep` and `delete` values have no arm, and `delete` loses edits
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0026
- **Class:** K9
- **Severity:** medium
- **Evidence:** The catalogue (v2:1277) allows `order`, `keep` and `delete`. research-supersession:175 says "`keep` is today's silent `patched`; `delete` loses edits". cl-0026 builds and plants only the order arm ("extended with the order arm"), and no clause or flow item gives the other two an arm.
- **Consequence:** The schema accepts two values that no code routes. If `delete` is ever wired, it removes an adopter's edited file (P19, P38).
- **Fix:** Give `keep` and `delete` their arms and planted cases in cl-0026, or drop them from the allowed values.
- **Skeptic:** confirmed medium.

### C1-F16 — The floor's down step checks TOML only, while the up step removes the guard against newer Python syntax
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0028
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0028's down restores the old declaration, "refusing while a tracked TOML file fails to parse under the floor it restores". The same clause retires "the PEP 701 text ban in `merge-rows.test.sh`" (`tools/memory-tree/merge-rows.test.sh:353-355`, "PEP 701, 3.12+"). gap-tool-22 gives the old floor as 3.11.
- **Consequence:** After the raise, 3.12+ syntax can land. A rollback then restores a 3.11 floor under tracked Python that will not compile.
- **Fix:** Make the down refuse while any tracked `.py` fails `compile()` under the floor it restores. Plant a PEP 701 f-string landed after the raise.
- **Skeptic:** confirmed medium.

### C2-F3 — The runaway ceiling gets two homes and two rules for a round count at the ceiling
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0106, against cl-dClosedLoop-0139
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0106 moves `RUNAWAY_CEILING` "into the loop kit's definition" and refuses "a planted round count at the ceiling". The catalogue (v2:1127-1128) makes `review.max-rounds` the ceiling as a policy value. The pair rule (v2:1299) and cl-0139 hold `review.design.round-count` "at or below `review.max-rounds`". `tools/unattended/unattended.sh:783` refuses at or above the ceiling (`-lt`).
- **Consequence:** A repository that sets `round-count = max-rounds` passes dKeptSession's preset check and is refused by dDeclaredLoop's arm. The ceiling also ends up both a loop-kit constant and a policy key.
- **Fix:** In cl-0106, make the ceiling the policy key `review.max-rounds`. Plant a round count above it, refused, and one equal to it, admitted.
- **Skeptic:** confirmed medium.

### C2-F4 — The pre-claim budget is keyed to an intake record that does not exist until a later build
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0132
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0132 keys the budget "to the intake's content key". The design map gives `record-kind.intake` to dWellOiledMachine, which is not an ancestor of dPlacedRequest, and cl-0123 admits the same dependency. flow-steps `entry.intake` (fs:80) leaves intake absent when the hook crashes or never fires.
- **Consequence:** Before dWellOiledMachine lands, and whenever the intake hook never fired, the budget has no key.
- **Fix:** Key the budget to a content key cl-0132 computes from the request text, which the claim commit already carries, and key an absent intake the same way. Plant one red case with no intake record.
- **Skeptic:** confirmed medium, narrowed. `flow.route-backs`, in Entry's policy list (fs:105), still caps returns to `entry.place`, so placement loops are not fully unbounded.

### C2-F6 — dFairHearing's breakpoint items depend on, and route to, items owned by a later build
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0070 and cl-dClosedLoop-0075
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps `review.pin` (fs:484), owned by dFairHearing, needs `review.trigger`, and `review.report` (fs:487) routes to `review.dispose`. Both are dDeclaredLoop's, a descendant. v2:483 requires "each new dependency on a later build gets a stand-in, a class row or a move". cl-0070 and cl-0075 declare none, and Stage 0 leaves the lead UNCLASSED.
- **Consequence:** dFairHearing's acceptance cannot run its items end to end in order, or it reaches into dDeclaredLoop's program.
- **Fix:** Add a stand-in to cl-0070 and cl-0075: until dDeclaredLoop lands, the harness is invoked directly with its pin arguments, and the report's dispositions are written to the review record.
- **Skeptic:** confirmed medium.

### C2-F7 — Entry's placing items route to Plan and Design items no ancestor builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0122 and cl-dClosedLoop-0123
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps `entry.place` (fs:83) routes "new → `entry.claim`, then Plan, or `plan.triage-rule`". Those items are owned by dRankedPlan and dIndexedDesign, neither an ancestor of dPlacedRequest (v2:1639, 1648-1649). cl-0125 declares "a stand-in for each later part it rests on"; cl-0122 and cl-0123 declare none.
- **Consequence:** A request placed after dPlacedRequest lands, but before dRankedPlan and dIndexedDesign land, routes to items that do not exist.
- **Fix:** Give cl-0123 cl-0125's stand-in sentence: until Plan's and Design's items land, a `new` or `amend` placement files an owner item carrying the claim.
- **Skeptic:** confirmed medium. v2 has no general stand-in rule outside the chain rows.

### C2-F8 — The spine's transition table routes to and witnesses items owned by later builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0098 and cl-dClosedLoop-0100
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps [transitions] rows route on items owned by non-ancestors, such as "planning | `plan.exit` | designing" and "testing | `test.exit` | deploying". Stage 0 lists seven such leads for dDeclaredLoop (build.distill, build.ratify, deploy.notify, design.ready, plan.exit, plan.input, test.exit), all UNCLASSED. cl-0098 says only "the engine refusing any transition it lacks" and declares no stand-in, which v2:483 requires.
- **Consequence:** dDeclaredLoop's engine is specced against witnesses no ancestor produces, so its acceptance cannot be planted from real items.
- **Fix:** In cl-0098, have each row name its exit item by tag, with a fixture witness until that item's build lands. Class the seven Stage 0 leads in [stage0-classes].
- **Skeptic:** confirmed medium.

### C2-F10 — dPlacedRequest's keys `leases.granularity` and `card.follows` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0120 and cl-dClosedLoop-0121
- **Class:** K4
- **Severity:** medium (the walker said low)
- **Evidence:** Both keys appear in v2 only in the catalogue (v2:1031, 1042), the presets (1354, 1365) and line 62, never in [chain]. cl-0120 says only "one lease grammar for builds, units and cadence runs", and cl-0121 does not say when the card re-renders.
- **Consequence:** Presets set these keys (velocity sets `leases.granularity` to `build`), but nothing reads them.
- **Fix:** Name `leases.granularity` in cl-0120 and `card.follows` in cl-0121, each with one arm per value.
- **Skeptic:** confirmed medium, above the walker's low. Velocity's `build` value has nothing to route it, which a spec writer would trip over; it is not a wording defect.

### C2-F11 — dKeptSession's keys `deps.coordination`, `deps.early-build` and `orient.budget` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0145 and cl-dClosedLoop-0147
- **Class:** K4
- **Severity:** medium
- **Evidence:** No [chain] row names any of the three keys. cl-0145 says "dependency coordination by the parent's lease, interfaces confirmed at Design's exit", and cl-0147 "orientation cost recorded per stage". Coordination item 8 reads both `deps.*` keys, and strict sets its own values for all three (v2:1361, 1362, 1374).
- **Consequence:** strict's orientation ceiling is never read, and no clause carries strict's dependency posture.
- **Fix:** Name all three keys in cl-0145 and cl-0147, each seen on its strict value.
- **Skeptic:** confirmed medium, narrowed. flow-steps lists `deps.coordination` in Plan's policies (fs:147) and `deps.early-build` in Design's (fs:200), so "strict behaves like standard" holds whole only for `orient.budget`.

### C2-F12 — Two clauses give two rules for when a fresh session is recommended
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0150, against cl-dClosedLoop-0121
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0121 (dPlacedRequest) recommends a fresh session "by `resume.context`". cl-0150 (dKeptSession) recommends "a fresh session in the build's worktree … until the card-import fixture passes", with no key and no precedence. Velocity sets `resume.context` to `always-resume` (v2:1373).
- **Consequence:** Under velocity, while the fixture is red, one build recommends resuming and the other a fresh session, so the policy key is bypassed.
- **Fix:** Make cl-0150 a gate on cl-0121's key: while the card-import fixture is red, `always-resume` reads as `fresh-when-idle`, and that is reported.
- **Skeptic:** confirmed medium.

### C2-F13 — The termination check's red case plants only a raised budget
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0118
- **Class:** K10
- **Severity:** medium
- **Evidence:** stall-and-loop [design] item 8 (s&l:244) makes raising any loop bound (the budget, a round count, a retry count, a deadline) a loosening, and its [chain] (s&l:310) plants "an unattended raise of a loop bound". cl-0118 reads a raise of a loop bound as a loosening but plants only "an unattended raise of the budget".
- **Consequence:** An unattended raise of `review.max-rounds`, `flow.route-backs` or `flow.wait-ceiling` can pass a check only ever seen red on the budget, so the guard certifies more than it checks.
- **Fix:** Add one planted unattended raise each for a round count, a retry count and a deadline to cl-0118's red list.
- **Skeptic:** confirmed medium. v2 narrowed the settling record's planted case.

### C2-F15 — The mailbox message kind names no writer, and no reader carries the transition refusal
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0143
- **Class:** K3
- **Severity:** medium
- **Evidence:** Coordination item 6 (co:116-117) refuses every transition while a message "is neither answered nor acknowledged". cl-0143 says only "read and disposed at every transition". No flow-steps item reads the mailbox at an exit (the only item hit is fs:374, on the release hold), and layer-memory:438 says "writer item not named". cl-0162 implies the hold ("past which … transitions go on") but does not refuse.
- **Consequence:** The refusal that makes a transition wait on an unanswered message has no item to carry it, so a spec can build the mailbox without it.
- **Fix:** In cl-0143, name the writer (the posting command per kind) and the reader: each exit item refuses on an undisposed message until `flow.wait-ceiling`. Plant one red case.
- **Skeptic:** confirmed medium.

### C3-F1 — No clause carries P18's admitted-options rule or checks a fork's pick against the ranking
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0176
- **Class:** K5
- **Severity:** medium (the walker said high, c5)
- **Evidence:** P18: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record … only options the core admits are options". cl-0176 says only "every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says". cl-0390, P18's other enforcing clause, says "fork resolution by `design.forks`".
- **Consequence:** An unattended role's pick is never checked against the admitted set or the ranking, so a pick outside them passes.
- **Fix:** Add the core-admitted option set and the full record to cl-0176. Plant a fork whose recorded pick is not the top-ranked admitted option, and see it red.
- **Skeptic:** confirmed medium, not c5. cl-0390 names `design.forks`, whose default `agents-feature-rich-expandable` (v2:1019) carries the ranking, and P18 has two enforcing clauses (v2:1702). The part with no clause is "only options the core admits are options", and the check that a pick is the top admitted option.

### C3-F2 — `instructions.task-charter` is read by no clause, though dBoundRoles owns it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] (v2:1231) gives `instructions.task-charter` (when-not-static, always) to dBoundRoles, and its single-carry check "refuses `always` on a backend that loads the static block". systems (410-413) has the single-carry check read the key and the harness kind. cl-0180 says only "the role static block carried once per spawn", and no [chain] row names the key.
- **Consequence:** The single-carry check is built without its key. Either `always` is accepted where the charter loads twice, or the key's value never routes.
- **Fix:** Have cl-0180 name `instructions.task-charter` and its refusal of `always` on a static-block backend, seen red on a planted `always`.
- **Skeptic:** confirmed medium.

### C3-F4 — Replacing the protocol pointers omits the same-unit re-point of the machinery that asserts them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0199
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [tags] (lr:376-380) requires the slicing unit to re-point, in the same unit, `CARRIED_SECTIONS`, `check_roles.py` R0, R5 and R10, and `render_agents.py`'s self-test arm 4. cl-0199 says only "the role files' re-verification orders and protocol pointers replaced by rendered slices". In code, `tools/roles/roles_lib.py:67` is `CARRIED_SECTIONS = ("Protocols", "Facts")`, `check_roles.py:169` reads the carried Protocols body, and `render_agents.py:335-338`'s arm 4 asserts the carried text.
- **Consequence:** Built from the clause, the slicing unit leaves R5, R10 and the self-test asserting the Protocols carry. The roles catalogue goes red, or the whole-document carry survives beside the slices.
- **Fix:** Name the four consumers in cl-0199 and require them re-pointed in the same unit.
- **Skeptic:** confirmed medium.

### C3-F5 — Five keys dFurnishedOrders owns are read by none of its clauses
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] gives dFurnishedOrders `annotations.delivery`, `roles.orientation.house-index`, `instructions.slices`, `retrofit.slot-bytes` and `memory.map-unfold` (v2:1228, 1229, 1234, 1247, 1261). None appears in any [chain] row, and Stage 0's K4 lists all five as unread, three of them guard-bearing. cl-0202 says "legacy slot in its four states" with no cap key, and cl-0203 says "the unfolds each item declares (PM-6)" with no key.
- **Consequence:** Each key's non-default value never routes. The legacy slot's 1 KB cap and the code-notes delivery have no switch.
- **Fix:** Name each key in the clause that builds its slot: `retrofit.slot-bytes` in cl-0202, `annotations.delivery` in cl-0209, `instructions.slices` in cl-0199, `memory.map-unfold` in cl-0203, and `roles.orientation.house-index` in a slot clause. Each value is routed and seen.
- **Skeptic:** confirmed medium.

### C3-F6 — Role metrics are written into the value ledger, which a later build registers, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0201
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0201 writes "role metrics per role and item into the value ledger". The design map gives `record-kind.value-ledger` to dCalibratedLens, built by cl-0459. dCalibratedLens is not an ancestor of dFurnishedOrders, whose only parent is dBoundRoles (v2:1642), and no stand-in is named.
- **Consequence:** dFurnishedOrders cannot be specced or landed in order, because its writer has no registered kind to write.
- **Fix:** Have cl-0201 write a metrics record dFurnishedOrders owns, which dCalibratedLens's ledger reads later, or add a stand-in until cl-0459 lands.
- **Skeptic:** confirmed medium.

### C3-F7 — The memory slices read a sibling build's index and keys with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0202 delivers "the work order's memory slices … each under its own budget and its own answer". systems [cross] (systems:214-215) prices them by `memory.item-budget` and answers them by `memory.over-budget`, both dTotalRecall's, and sections resolve through dTotalRecall's `record show` (cl-0220). dTotalRecall is not an ancestor of dFurnishedOrders. cl-0203 and cl-0208 carry "not installed until dTotalRecall's renderer lands"; cl-0202 does not. cl-0195's three-state rule covers only optional components and expansions, and memory is core.
- **Consequence:** The slot cannot be built in order, or it is built against a section index that does not exist yet.
- **Fix:** Add a stand-in to cl-0202: the memory slot renders "not installed" until dTotalRecall's section extractors land, as cl-0203 and cl-0208 do.
- **Skeptic:** confirmed medium.

### C3-F8 — The answered-call hook omits the verifier exemption, so the default `refuse` blocks a verifier reading its subject
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0197
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [trust] item 10 (lr:331-336): "A verifier's read of its subject is never an answered call, and neither is a read the packet does not cover". It adds that below CLI 2.1.295 a rule on an ungated tool stays open when its hook fails, and the failure is recorded. cl-0197 says only "the answered-call hook (`roles.answered-calls`)", whose default is `refuse` (v2:1057). cl-0205 defers its details to unit specs.
- **Consequence:** A reviewer's or tester's read of its handed subject is refused, and verification stalls. The fail-open window also goes unrecorded.
- **Fix:** Carry both rules in cl-0197. See it green on a planted verifier read of its subject, and see a recorded failure on a planted hook crash.
- **Skeptic:** confirmed medium. P29 (v2:875-878) implies the exemption but does not carry it.

### C3-F9 — Typed relations drop the `depends-on` cycle check and the pending-target rule
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0217
- **Class:** K10, c3
- **Severity:** medium
- **Evidence:** layer-memory [relations] (lm:547-550): "every relation's target must exist, and `depends-on` must form no cycle … A target found nowhere is pending, not red, until its build lands". cl-0217 says only "typed relations (…), inverted, checked both ways and rendered as the relation graph". dTotalRecall owns gap-mem-07 (gap-register:189, "no cycle check").
- **Consequence:** A `depends-on` cycle passes the check, leaving gap-mem-07 open. Otherwise, a target on another node's unlanded branch reds and refuses legitimate work.
- **Fix:** Add both rules to cl-0217: red on a planted two-build cycle, and pending on a planted target on another node's branch.
- **Skeptic:** confirmed medium.

### C3-F10 — The slug grammar omits "binds new mints only", `BUILD_SLUG_RE`'s derivation and the named flips
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0216
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-memory [names] (lm:518-528): "A changed grammar binds new mints only. Existing slugs and ids keep their form, every reader accepts both, and the grammar in force at minting is recorded with each slug". It also derives `BUILD_SLUG_RE` from the `builds.slug-*` keys and names the flips. cl-0216 says only "proven by flipping the grammar in a scratch clone".
- **Consequence:** A grammar flip makes every reader reject existing slugs and ids across the tree, and the flip test can pass on one flip.
- **Fix:** Carry the new-mints-only rule, the recorded grammar per slug, the derived `BUILD_SLUG_RE` and the named flip set in cl-0216.
- **Skeptic:** confirmed medium.

### C3-F11 — The code record's re-timing has no losing bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0219
- **Class:** K10
- **Severity:** medium
- **Evidence:** v2 [owed] (v2:1894-1896): the code record's cold derivation re-timed at dTotalRecall's first unit, "over 30 s or over 1 MB loses, on gov's tree and on a planted adopter-scale fixture". cl-0219 has only "re-timed on a planted adopter-scale fixture": no bound, and no gov tree.
- **Consequence:** The re-timing cannot fail, so an over-budget derivation ships.
- **Fix:** Put the 30 s and 1 MB loss bound, on both trees, into cl-0219.
- **Skeptic:** confirmed medium.

### C3-F12 — The acceptance re-measure has no target or window
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0223
- **Class:** K10
- **Severity:** medium
- **Evidence:** systems [design-memory-structure] (systems:550-559): "Thirty days after landing, the median memory bytes per agent that reads memory are below 33 KB", with a note on why the first measure could not fail. cl-0223 says only "the acceptance re-measure counted over every read channel".
- **Consequence:** The measure has no pass bar, which repeats the could-not-fail defect the record already corrected.
- **Fix:** Add "median below 33 KB, 30 days after landing" to cl-0223.
- **Skeptic:** confirmed medium.

### C3-F15 — dTotalRecall owns gap-mem-23 (touch-drop wired to nothing), but no clause of it carries the gap
- **Address:** architecture-v2 [chain] dTotalRecall row, Gaps owned (`gap-mem-23`)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-mem-23: "`--drop-affordance-exempt` has no caller in `tools/`". In the working tree the flag appears only in `tools/codebase-map/map_diff.py` and its README. The touch-drop is wired by cl-0407 (dScopedBuild, a descendant), which calls `drop_touched_exemptions`. None of cl-0212 to cl-0237 mentions it.
- **Consequence:** The gap's owner lands without closing it, and its actual closer does not own it.
- **Fix:** Move gap-mem-23 to dScopedBuild, which completes the closure and descends from dTotalRecall, by the register's own rule. Alternatively, add a dTotalRecall clause wiring the drop.
- **Skeptic:** confirmed medium.

### C3-F16 — Memory keys dTotalRecall owns are read by no clause, one of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0220 (also cl-dClosedLoop-0225)
- **Class:** K4
- **Severity:** medium
- **Evidence:** `memory.over-budget` (refuse, report, off; exempt from `budgets.enforce`), `memory.superseded-slices` (refuse, mark) and `memory.map-overflow` (degrade, refuse) are dTotalRecall's (v2:1242, 1250, 1246), and none appears in any [chain] row. cl-0220 says "reported when exceeded" and cl-0225 "degraded in a fixed order", neither naming its key. No clause carries the superseded-slices check. Stage 0's K4 lists all three.
- **Consequence:** `refuse` and `off` never route, the superseded-slice check is never built, and the exemption from `budgets.enforce` is lost.
- **Fix:** Name the three keys with their values and checks in cl-0220 and cl-0225.
- **Skeptic:** confirmed medium.

### C3-F18 — `reuse_lookup.py` is retired without naming its by-value readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0240
- **Class:** K10
- **Severity:** medium (the walker said high, c3)
- **Evidence:** layer-memory [reuse] (lm:719-731) lists the by-value readers: hygiene check 12's §10 arm, which accepts the token `reuse_lookup` as reuse evidence (`tools/memory-tree/check-memory-hygiene.sh:2474`); `MAP_CLI` (`tools/unattended/kit.toml:174`); and the `reuse-probed` DoD item (`tools/unattended/PROTOCOL.template.md:356`). cl-0240 says only "retired with their readers rewritten".
- **Consequence:** A spec writer who skips the layer record leaves check 12 certifying a spec's reuse audit on a citation of a retired tool.
- **Fix:** Name the by-value readers in cl-0240. See red a planted spec citing `reuse_lookup` after the new cutoff.
- **Skeptic:** confirmed medium, below the walker's high. The design names these readers, so check 12 loosens only if a spec writer skips the layer record.

### C3-F20 — README routing and the relation graph are each built by two builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0242
- **Class:** K8
- **Severity:** medium
- **Evidence:** cl-0242 (dLinkedLibrary) builds "the generated views: README routing, the relation graph, …". cl-0215 (dTotalRecall) already builds "a generated routing region by purpose", and cl-0217 has relations "rendered as the relation graph". memory-plan [practice]: "every node gov ships names one owning build".
- **Consequence:** Two specs build one view. The one-owner check reds, or two renderers diverge.
- **Fix:** Drop the two views from cl-0242, or have it say it consumes dTotalRecall's renders.
- **Skeptic:** confirmed medium. The class is a view built twice, not a gap owned twice: gap-mem-05 is dTotalRecall's alone. The walk record listed all three as units 4, 6 and 14 of one build before the split moved unit 14.

### C3-F24 — The forced-name packs contradict the rule that namespaced closed sets apply by name
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0263
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [forced] item 1 (lines 245-253): "A namespaced closed set applies by name, and its rows carry a namespace pattern … (`pytest_*`, `__*__`)", with three outcome cases (unresolved base, in-repo parent, marker). cl-0263 applies all three pack kinds, host namespace included, "only where the site resolves statically through its imports to that base", and omits the three cases.
- **Consequence:** Module-level pytest hooks, and dunders on classes with no outside base, stay debt and are refused at commit under `lexicon.at-commit: refuse`, which leaves gap-lex-01 open.
- **Fix:** Split the rule in cl-0263: member and prefix rows resolve statically, and namespace closed sets apply by name. Add the three cases, each with its fixture.
- **Skeptic:** confirmed medium. cl-0265 covers marker verification only partly.

### C3-F25 — The noun canon's source contradicts the amended design
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0271
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [drift] (lines 371-373), amended by the debt fold's `nouns-table` row: noun clusters are "written exogenously, such as `sha` against `oid` … The corpus decides only which clusters are live". cl-0271 reads "a noun canon seeded from the corpus and frozen", which is L-3's pre-fold offer wording (lexicon line 539).
- **Consequence:** A corpus-seeded canon makes today's variants canonical, the opposite of the fix.
- **Fix:** Reword cl-0271: clusters written exogenously, with liveness from the corpus.
- **Skeptic:** confirmed medium.

### C3-F26 — `ratified` is retired without its readers by value
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0272
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [vocabulary] (lines 414-417) moves the drift signal, `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole and the scaffold to the record that replaces `ratified`, with the leg pack's arm seen red on a planted LANGS change newer than the record. The debt fold classes this `retirement-inventory-misses-readers-by-value`. `ratified` is read in `tools/lexicon/{adopt-lexicon.sh,kit.toml,lexicon.py,lexicon_conf.py,scaffold_lexicon.py,selftest.py}` and `tools/drift-audit/{drift_report.py,drift_signals.py}`. cl-0272 says only "with `ratified` replaced by its record".
- **Consequence:** The drift signal and the adopt check keep reading a dead field, and their signal silently stops moving.
- **Fix:** Name the readers in cl-0272, with the planted LANGS red.
- **Skeptic:** confirmed medium.

### C3-F28 — P29's enforcement row names one clause, though P29 has several rules
- **Address:** architecture-v2 [enforcement] P29
- **Class:** K5
- **Severity:** medium
- **Evidence:** v2:1713 names only cl-0178 for P29. P29 (v2:866-881) also covers verifiers alone and cold (`roles.verifier-context`), answered calls (`roles.answered-calls`), false facts (`roles.on-contradiction`), acting on keyed facts (`roles.trust`), and "Recall: recall is re-verified once, by the orientation scout at entry". cl-0196, cl-0197, cl-0198 and cl-0205 carry those keys but sit in no row. No clause carries the recall re-verification; cl-0192 and cl-0204 only compose the card.
- **Consequence:** The principle registry certifies P29 from a clause that carries one of its rules, and the recall boundary is never built.
- **Fix:** Add cl-0196, cl-0197, cl-0198 and cl-0205 to P29's row, and add the recall re-verification to cl-0192.
- **Skeptic:** confirmed medium.

### C4-F4 — The settling row names an orientation scout as `entry.intake`'s actor, though cl-0282 builds it as a hook
- **Address:** flow-steps [entry] `entry.intake` row, against architecture-v2 [chain] cl-dClosedLoop-0282
- **Class:** K1
- **Severity:** medium
- **Evidence:** flow-steps:81 reads "Actor: orientation scout, in an owner-bound session only … Proven by: the intake entry the scout writes". Against it stand the same record's amendment `hook-actor-kind` (flow-steps:796, "`entry.intake` is a hook"), its Owner note (flow-steps:99), layer-roles:414 ("| hook | `entry.intake` |") and cl-0282's prompt-submit hook "writing each owner prompt verbatim".
- **Consequence:** The item join and the owner check read an agent as the writer of the intake record. That record is "the mandate to land" (gap-rt-14), so the owner's verbatim mandate would be agent-typed. A builder of cl-0282 or of `entry.orient` meets two contradictory actors.
- **Fix:** Set the row's actor to "hook: prompt-submit, owner-bound sessions only", and its witness to "the intake entry the hook writes".
- **Skeptic:** confirmed medium.

### C4-F5 — The session-limit hold hands the lease over without the owner item the settling records require
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0325
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0325 releases "the build's lease as a hand-over at `runtime.hold-ceiling` so a node with quota takes the build over and the wake tick stops". Its red cases are "the lease still held or the tick firing again past the ceiling, a hand-over no second node takes". The catalogue's `runtime.hold-ceiling` row, layer-runtime [supervise] and layer-runtime [tests] `limits` all say an owner item is raised.
- **Consequence:** When no node with quota exists, which is the "hand-over no second node takes" case, the build sits released and nobody is told.
- **Fix:** Add "and raises an owner item" to cl-0325, with a red arm on a ceiling passed and no owner item.
- **Skeptic:** confirmed medium.

### C4-F6 — The no-progress and repeat detectors arm as blocking with no false-positive measurement first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324
- **Class:** K10
- **Severity:** medium
- **Evidence:** stall-and-loop [owed] (line 414): "The no-progress and repeat detectors' false positives measured on gov's own run logs before either blocks (dWellOiledMachine)". cl-0324 builds both detectors as acting, with no measurement step and no journal-only stage.
- **Consequence:** An untested detector can mark healthy items stuck and route them, spending the build's rework budget, with no check that could show the error.
- **Fix:** Add to cl-0324 the replay over gov's recorded run logs, and keep the detectors journal-only until their false-positive rate is recorded.
- **Skeptic:** confirmed medium.

### C4-F8 — Five of dWellOiledMachine's own runtime keys are read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0288 (also cl-dClosedLoop-0279, cl-dClosedLoop-0284, cl-dClosedLoop-0295)
- **Class:** K4
- **Severity:** medium
- **Evidence:** The catalogue gives `runtime.spawn-backend`, `runtime.relaunch`, `runtime.hook-failure`, `runtime.attended-allowance` and `runtime.secret-scan` to dWellOiledMachine, and no clause names any of them. Stage 0's K4 lists all five, two guard-bearing. cl-0279's spike decides the backend, cl-0284 says "relaunch capped", cl-0288 writes "`onFailure` … on every entry", and cl-0295 builds "the secret value scan", none naming its key.
- **Consequence:** `hook-failure: open`, `relaunch: resume` and `secret-scan`'s `+shape-report` arm are dead values. The `coverage` fixture's "every `runtime.*` key … has a reader" goes red with no clause owning the read.
- **Fix:** Name `runtime.spawn-backend` in cl-0279, `runtime.relaunch` in cl-0284, `runtime.hook-failure` (both values) and `runtime.attended-allowance` in cl-0288, and `runtime.secret-scan` in cl-0295. Give each value an arm.
- **Skeptic:** confirmed medium, narrowed. Both `secret-scan` values include the value gate, so the arm left unbuilt is `+shape-report`, not `value-gate`. cl-0288's "as `runtime.attended-judge` says" implies the allowance read.

### C4-F9 — Three remote-verdict gaps and their keys sit on dWitnessedBar with no clause to build them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0344 (also cl-dClosedLoop-0342, cl-dClosedLoop-0347, cl-dClosedLoop-0352)
- **Class:** K4
- **Severity:** medium
- **Evidence:** dWitnessedBar owns gap-test-11 ("A remote verdict certifies itself"), gap-test-12 and gap-test-13, and the catalogue gives it `verdict`, `verdict.remote.trust`, `verdict.remote.pin`, `verdict.remote.pin-scope`, `tests.product` and `retrofit.widen`. layer-expansions lets a remote verdict stand as a witness "only when … the pinned files at `head_sha` equal the pin". None of cl-0339 to cl-0368 names a verdict-backend registry, a remote pin, the held-CI reader's adapter, `tests.product` or `retrofit.widen`.
- **Consequence:** A remote verdict can be built with no source check, so once `verdict: remote-ci` is selected a pusher's workflow edit certifies itself. `tests.product` and `retrofit.widen` have no reader, and gap-test-12 and gap-test-13 close with nothing built.
- **Fix:** Add a dWitnessedBar clause for the verdict-backend registry under `verdict` and the remote verdict's source check under `verdict.remote.*`, seen red on a swapped workflow. Name the held-CI reader's adapter registration. Name `tests.product` in cl-0347 and `retrofit.widen` in cl-0352.
- **Skeptic:** confirmed medium.

### C4-F10 — No clause builds the runner's same-tree re-run, so a flaky leg never reaches `test.flakes`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0346
- **Class:** K2
- **Severity:** medium
- **Evidence:** flow-steps [test] (line 296) has `test.route` "re-runs each red leg once on the same tree", and line 304 calls that a runner mode dWitnessedBar owes (gap-test-04); today the bar retries only timeouts. cl-0346 says only "flake quarantine", and cl-0368 re-runs only CONTENDED reds on a quiet host.
- **Consequence:** `test.route` cannot tell a nondeterministic red from a real one. Flaky reds route to `test.attribute` as OWN reds, and the quarantine never receives a leg.
- **Fix:** Add to cl-0346 "the runner's mode re-running a red leg once on the same tree under `test.verdict`'s env, seen on a fixture leg that reds then greens reaching `test.flakes`".
- **Skeptic:** confirmed medium.

### C4-F11 — The card's retirement re-points an incomplete list of readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0316
- **Class:** K10 (a retirement by value)
- **Severity:** medium
- **Evidence:** cl-0316 re-points the write gate, `readCard`, `extractRouteUnits`, the route notice and `manifest-check.sh --card --write`, "with `check-wiring.test.sh` and `format-guard.test.sh`". `grep -rn "orientation/"` also finds `skills/session-kickoff/manifest-check.test.sh` (14 lines, such as 861, asserting "the card is at <common-dir>/orientation/<sid>.md") and `tools/hooks/scratch-guard.test.sh:537,539,737`.
- **Consequence:** Those tests still assert the retired card path, so the unit lands red.
- **Fix:** Add `scratch-guard.test.sh` and `manifest-check.test.sh` to cl-0316's inventory, each re-pointed in the same unit.
- **Skeptic:** confirmed medium, narrowed. The two `orientation-*.fragment.json` files the walker also named hold no card path; they wire `manifest-check.sh --card --write`, which cl-0316 already names. The consequence is a red bar, not a silent pass.

### C4-F12 — The portability pack moves in a "shell-hygiene mode" that `encoding_posture.py` does not have
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0362
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0362: "the last moved in from gate-lint's `encoding_posture.py` with its shell-hygiene mode". `encoding_posture.py` has no shell mode; its only modes are text and binary. `tools/gate-legs.json` runs `gate-lint/sh_hygiene.py` as its own script, with three legs plus a selftest. research-compatibility §4 puts P-launch's legs in the shell-hygiene spawn-idioms and loop legs.
- **Consequence:** A builder either looks for a mode that does not exist or leaves `sh_hygiene.py` in gate-lint.
- **Fix:** Read "moved in from gate-lint's `encoding_posture.py`, with `sh_hygiene.py`'s legs beside it".
- **Skeptic:** confirmed medium, narrowed. cl-0362 also names a bare-shell-name arm, so P-launch is not left without a core leg.

### C4-F13 — The event-wait sweep and the atomic landing rely on dShippedRelease items that no ancestor lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0296 (also cl-dClosedLoop-0337)
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0296's sweep "raises a wait past `build.release-ceiling` once", and the catalogue defines that key as how long `deploy.released` waits for an exit record. cl-0337 carries "the build's release with its landed notice … in one atomic push". flow-steps gives `deploy.released`, `deploy.notify`, `deploy.unlease` and `deploy.close` to dShippedRelease, which comes after dWellOiledMachine, and Stage 0's K2 shows the lead UNCLASSED. No dWellOiledMachine clause names a stand-in, unlike flow-steps' [probe] stand-ins (lines 569-576).
- **Consequence:** The sweep and layer-runtime's `event-wait` and `lifecycle` fixtures cannot run when dWellOiledMachine lands, so their arms are never seen red or are built against items that do not exist yet.
- **Fix:** Have cl-0296 and cl-0337 name a stand-in release slot and notice, with the same contract and owned by this build, until dShippedRelease lands. Alternatively, move the fixtures' release arms to dShippedRelease.
- **Skeptic:** confirmed medium.

### C5-F3 — A post-landing core red "stops that build from closing", but the settled route closes it through the post-close row
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0423
- **Class:** K2
- **Severity:** medium
- **Evidence:** cl-0423: "so a core red the landing merge introduced stops that build from closing (foundations K1)", which foundations:369-377 reads as no exit "until the red is fixed or excepted". flow-steps:369 (`deploy.core`): "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". layer-flow:326-328 routes the same red through the post-close row.
- **Consequence:** A lander built from the clause holds the build open, with its leases and mailbox, until the red is fixed. A Deploy step built from flow-steps closes it once the patch build is filed. The S6 landing route has two incompatible terminals.
- **Fix:** Reword cl-0423: "… a core red the landing merge introduced files a patch build through the post-close row before the build closes". Plant a red landed tree whose close happens without that filing, and see it red.
- **Skeptic:** confirmed medium.

### C5-F5 — Build drains only "in hunks" and always claims, so `retrofit.drain` and `retrofit.claim-on-touch` have unbuilt values, and velocity selects `carry`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0406
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0406 hard-codes "in hunks under `retrofit.drain-cap`" and "claiming … under `retrofit.claim-cap`". v2 gives dScopedBuild `retrofit.drain` (hunk, file, off) and `retrofit.claim-on-touch` (claim, carry, off), and no clause names either. The preset row at v2:1571 gives velocity `carry`. retrofit:404-406 defines the `file` and `off` arms.
- **Consequence:** A velocity repository still claims and drains, contradicting its preset. The `file` and `off` values validate in the schema and do nothing.
- **Fix:** Have cl-0406 read both keys and build each value's arm, each value seen on a planted unit.
- **Skeptic:** confirmed medium.

### C5-F7 — The Loop Review is fixed at "weekly", and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0460 (and cl-dClosedLoop-0461)
- **Class:** K4
- **Severity:** medium
- **Evidence:** cl-0460 fixes "the weekly Loop Review". v2:1213 gives dCalibratedLens `review.loop.cadence` (weekly, monthly, every-n-landings), which no clause names, and layer-expansions keys the Loop Review by ISO week. Stage 0's K4 lists `review.loop.cadence` and `budgets.*` as unread.
- **Consequence:** The monthly and every-n-landings values pass the schema and run weekly. The cap keys cl-0461 re-derives have no clause naming them.
- **Fix:** cl-0460 reads `review.loop.cadence`, keys the lease by the selected period, and sees each value on a planted case. cl-0461 names `budgets.*` as what it re-derives.
- **Same as:** C1-F13, for the `budgets.*` half only.
- **Skeptic:** confirmed medium, narrowed on the `budgets.*` half. cl-0015, cl-0041 and cl-0064 read `budgets.enforce` and `budgets.pinned`, and cl-0461's "caps re-derived" is in substance the `budgets.*` row's default.

### C5-F8 — Maintain's build delivers the Loop Review, a program its descendant dCalibratedLens owns
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0449
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0449 (dTendedCadence) delivers "Maintain and the Loop Review … as cadence steps of the observability expansion". The items `loop.lease` to `loop.record` (layer-expansions:253-262) and `record-kind.loop-review` (design-map:290) belong to dCalibratedLens, a descendant, and cl-0460 builds the Loop Review again.
- **Consequence:** When dTendedCadence lands, its cadence step registers a program with no items, and two builds' clauses carry the Loop Review's registration.
- **Fix:** cl-0449 registers Maintain's cadence step only, and cl-0460 registers the Loop Review's. Alternatively, cl-0449 names a "not installed" stand-in until dCalibratedLens lands.
- **Skeptic:** confirmed medium.

### C5-F9 — Maintain's host, cadence, events, reading admission and run record are built by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0443, cl-dClosedLoop-0445 and cl-dClosedLoop-0447
- **Class:** K4
- **Severity:** medium
- **Evidence:** `maintain.host`, `maintain.cadence`, `maintain.events`, `maintain.reading-admission` and `observability.run-record` are named by no clause. Stage 0's K4 lists all five as unread, three guard-bearing, and its K3 shows the run record with no writer and no reader (stage0-leads:129-130). layer-expansions admits a reading with no derivable owner only "under `maintain.reading-admission: report-unowned`", and has the journal reader write a run's record "as `observability.run-record` says". cl-0443, cl-0445 and cl-0447 say only "the cadence, on Runtime's hosts", "detectors with owners" and "the maintenance record". The default `maintain.events` includes `release-verify-failed`, whose producer kind is dShippedRelease's, not an ancestor.
- **Consequence:** The admission guard's refuse and report arms, the run record (gap-maint-14) and the event subset are unbuilt or unspecified.
- **Fix:** cl-0443 reads `maintain.host`, `maintain.cadence` and `maintain.events`, with `release-verify-failed` rendering "not installed" until dShippedRelease lands. cl-0445 builds both admission values. cl-0447 adds the run record under `observability.run-record`. Each is seen on a planted case.
- **Skeptic:** confirmed medium, narrowed. layer-expansions:232 already limits `release-verify-failed` to "when integrations is installed", so the missing stand-in is a partial gap only.

### C5-F10 — Three gaps Maintain owns are closed by no clause
- **Address:** architecture-v2 [chain] dTendedCadence row, Gaps owned (cl-dClosedLoop-0445)
- **Class:** K8
- **Severity:** medium
- **Evidence:** dTendedCadence owns gap-maint-09 (five drift signals become core legs: ledger_rows, non_terminal_specs, closed_specs, handkept, cutoff_keys_armed), gap-maint-10 (a reading varies with its tree, answered by `maintain.reading-tree`) and gap-maint-11 (the remote-CI drift signal is dead) (gap-register:427-429). A search of every clause for those signals, `reading-tree` or the remote-CI signal finds only cl-0277, the lexicon's two signals.
- **Consequence:** The five drift signals stay report-only in drift-audit, with the merge bar reaching them through an optional kit. The tree-variance and dead-probe gaps close in name only.
- **Fix:** Add a dTendedCadence clause carrying all three: the five legs moved to their owning layers' packs, readings taken under `maintain.reading-tree`, and the dead remote-CI signal fixed or retired. Alternatively, move gap-maint-09 to the builds that own those legs.
- **Skeptic:** confirmed medium.

### C5-F11 — The landing queue has no ordering rule, and Deploy and distribution keys are read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0422 (and cl-dClosedLoop-0417, cl-dClosedLoop-0437)
- **Class:** K4
- **Severity:** medium
- **Evidence:** P21: "landings go in plan priority, then first verified", and `landing.order` offers plan-priority-then-first-verified, first-verified and owner-orders. None of `landing.order`, `deploy.runs`, `deploy.currency`, `kits.cadence`, `kits.host`, `kits.watch-cadence` or `commits.squash` appears in any clause. cl-0422 says only "landings ordered through the landing queue it builds", and P21's row (v2:1705) relies on it. flow-steps:407 says "ordered by `landing.order`", but no clause carries it. cl-0437 builds `commits.squash`'s three values without naming the key.
- **Consequence:** P21's ordering half has no enforcing clause, and `owner-orders` is unbuilt. The cadence and host keys that `kits.currency` runs on have no clause reading them.
- **Fix:** cl-0422 orders the queue "as `landing.order` says", each value planted. cl-0417 reads `kits.watch-cadence`, `kits.host` and `deploy.currency`. cl-0437 names `commits.squash`.
- **Skeptic:** confirmed medium.

### C5-F12 — The derived runbook and release notes have no losing test, and the runbook is derived again at convergence
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0419 (and cl-dClosedLoop-0414, cl-dClosedLoop-0489)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0419 is only "a derived runbook" and cl-0414 only "kit release notes", with no red case. final-questions [help] (220, 225) and research-final-help:129 record that the derived runbook and release notes have no losing test, and final-questions [folded] (382-404) does not fold it. cl-0489 (dConvergedCharter) then migrates "the agent runbook … its reference half generated".
- **Consequence:** The first derivation's acceptance cannot fail, and two builds derive the same document under different rules.
- **Fix:** cl-0419 states its render-parity red on a hand-edited runbook section, and cl-0414 a red on notes missing a landing. cl-0489 either cites cl-0419's derivation, or cl-0419 moves into cl-0489.
- **Skeptic:** confirmed medium.

### C5-F13 — gap-flow-04's closure spans two builds that do not descend from each other, and gap-flow-03 has no closing clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0382 (dRankedPlan, Gaps owned)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-flow-04 ("no recorded plan revision and no re-design inventory of completed work") is dRankedPlan's, but its inventory half is `design.inventory` (dIndexedDesign, flow-steps:183). Neither build descends from the other, which the register's split rule (gap-register:12) forbids. cl-0382 only mentions "a plan revision" without building its record. No dRankedPlan clause matches gap-flow-03 (the card, plan and brief levels).
- **Consequence:** The gap join reads dRankedPlan as closing a gap whose inventory half lands elsewhere. No unit builds the plan-revision record, and the three-times-written plan stays.
- **Fix:** Split gap-flow-04 into a dRankedPlan key (the plan-revision record, built by a clause) and a dIndexedDesign key (the inventory). Add a dRankedPlan clause declaring the card, plan and brief levels, for gap-flow-03.
- **Skeptic:** confirmed medium.

### C5-F14 — Plan Review and the landing review run before the build that supplies their lenses, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0374 and cl-dClosedLoop-0424 (with cl-dClosedLoop-0458)
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0374 (dRankedPlan) builds "Plan Review", and cl-0424 (dShippedRelease) "the landing review blocking the build's close". cl-0458 (dCalibratedLens) supplies "lenses for Plan, Test, Deploy and Maintain". dCalibratedLens descends from dRankedPlan, and it and dShippedRelease do not descend from each other. `review.plan` is opt-in, and neither clause names a stand-in lens from dFairHearing's catalogue.
- **Consequence:** From dRankedPlan's landing until dCalibratedLens's, the Plan breakpoint has no lens, and the landing review is in the same position.
- **Fix:** cl-0374 and cl-0424 each name a stand-in lens from dFairHearing's catalogue until dCalibratedLens lands.
- **Skeptic:** confirmed medium, narrowed. The split-rule half does not hold: gap-plan-04, gap-deploy-06 and gap-review-01 are three gaps, each with one owner.

### C5-F16 — The Design hand-off and overlap keys are read by no clause, so the overlap refusal is unbuilt
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0383 and cl-dClosedLoop-0384
- **Class:** K4
- **Severity:** medium
- **Evidence:** `design.handoff` (derived-ready, ready-plus-audit, status-and-tier) and `design.overlap` (warn, refuse, index-only) are dIndexedDesign's (v2:1158-1159), and no clause names either; stage0-leads:155-156 agree. cl-0383 says only "the derived-READY hand-off" and cl-0384 "the design index". flow-steps:200 lists both among Design's policies.
- **Consequence:** The `refuse` value of the guard-bearing `design.overlap` passes the schema and only warns, and `ready-plus-audit` is never built.
- **Fix:** cl-0383 reads `design.handoff` and cl-0384 reads `design.overlap`, each value seen on a planted overlapping roster.
- **Skeptic:** confirmed medium.

### C5-F21 — Convergence folds the house file over the owner's earlier rulings on the same values
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0495 (against cl-dClosedLoop-0438)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0438 (dShippedRelease) proposes "the house file's efforts as `roles.effort.*` values … for the owner to rule once" (flow-roles-adoption:264). cl-0495 later folds "a repository's efforts … into the `roles.effort.*` policy keys … with an upgrade step", and reads no prior ruling or declined row. P8: "an update never overwrites or silently drops a repository's change".
- **Consequence:** An owner who declined a proposed effort has it written into the policy file by convergence's upgrade step, which overrides the ruling (P8, P38).
- **Fix:** cl-0495's step folds only values with no ruling from cl-0438, and reads a declined row as a drop. Plant a declined proposal and see it survive the fold.
- **Skeptic:** confirmed medium.

### CS1-F1 — The ratification fallback ends when "that hook" lands, but cl-0283 keeps it per harness, and the two builds are unordered
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0378, read against cl-dClosedLoop-0283
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0378: "until that hook and the intake kind land, `plan.exit` … falls back to dDeclaredLoop's owner gate". cl-0283 (dWellOiledMachine) drains "RC-9's fallback … per harness, only where an adapter's capability table declares the prompt-submit event and kept in force for any other, seen on a planted Codex-shaped adapter that still reaches Plan's exit". dRankedPlan's parents (dDeclaredLoop, dTotalRecall, dBoundRoles) do not include dWellOiledMachine, nor the reverse, so either may land first.
- **Consequence:** If dWellOiledMachine lands first, cl-0283's acceptance needs a Plan exit that does not exist yet. dRankedPlan's spec, reading cl-0378, then finds the hook landed and builds no fallback, so a Codex-shaped harness has no ratification path.
- **Fix:** Make cl-0378's condition per harness ("until the harness's adapter declares the prompt-submit event"). Order the two builds, or move cl-0283's planted case to whichever lands second.
- **Skeptic:** raised by skeptic batch 1 on re-walking cl-0378, which walker 5 had passed as holding. No second skeptic judged it.

### CS2-F1 — A message retried from a new session is not refused as a duplicate
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0160 (with cl-dClosedLoop-0150 and cl-dClosedLoop-0143)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0160 derives a message's id "from its sender's session, and its act once Runtime mints acts". Acts are dWellOiledMachine's, and that build is not an ancestor of dKeptSession. cl-0143 keys each mail ref by session. cl-0150, in the same build, recommends a fresh session, and the `resume.context` default is `fresh-when-idle`.
- **Consequence:** A post retried after a crash from a fresh session gets a new id and lands in a new ref, so the duplicate lands. The "post retried after a crash" case passes only when the retry runs in the same session.
- **Fix:** Until acts are minted, derive the id from the build, the item instance key cl-0092 computes, the pass, the kind, the subject and the answered id, not from the session. Plant the retry from a new session and see it refused.
- **Skeptic:** raised by skeptic batch 2 on re-walking cl-0160, which walker 2 had passed as holding. No second skeptic judged it.

### CS4-F1 — The policy namespaces' purposes are reviewed under a key no ancestor of dKeptSession registers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0154
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0154: "the policy namespaces' purposes, reviewed". project-map:660-666 reviews an existing node "under `memory.map-purpose: review` (PM-5)", by "the unit that adds its namespace's purpose field". v2:1248 gives `memory.map-purpose` to dTotalRecall, which is neither ancestor nor descendant of dKeptSession (whose parents are dDeclaredLoop and dPlacedRequest). project-map:668 covers only "Builds after dTotalRecall", and project-map:657 still names dDeclaredLoop as the owner of the policy namespace's purpose.
- **Consequence:** A dKeptSession spec carrying the clause has no review rule and no ask route, and it may land before the key exists.
- **Fix:** Name `memory.map-purpose` in cl-0154 with a stand-in until dTotalRecall lands, or move the review to cl-0227's reviewers. Correct project-map:657.
- **Skeptic:** raised by skeptic batch 4 on re-walking cl-0154, which walker 2 had passed as holding. No second skeptic judged it.

### CS4-F2 — `deploy.unlease` is built without its mailbox close, and no clause carries copy-before-prune
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0415
- **Class:** K1
- **Severity:** medium
- **Evidence:** cl-0415 builds `deploy.unlease` "closing each of a build's leases with a terminal tombstone" and says nothing of the mailbox. flow-steps:376's item "closes its mailbox". flow-steps:55-59: "every message still on its mailbox ref, disposed or not, is copied into the build folder, and the undisposed ones are marked … Only then is the ref pruned". No clause pairs mail with prune, copy or unlease; cl-0143 says only "kept in the build's transition log".
- **Consequence:** A builder of the clause may never close the mailbox, or may prune the ref without copying and lose undisposed messages. `life.unlease` has the same gap.
- **Fix:** Add the mailbox close to cl-0415, with copy-before-prune and undisposed messages marked. Plant a build with an undisposed message, unlease it, and see the copy in the folder and the ref pruned only after it.
- **Skeptic:** raised by skeptic batch 4 on re-walking cl-0415, which walker 5 had passed as holding. No second skeptic judged it.

## Low

### C1-F7 — The deviation clauses rely on a later build's overlay grammar and approval rule, and name no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0006 (also cl-0004)
- **Class:** K7
- **Severity:** low (the walker said medium)
- **Evidence:** final-questions [spine] puts each deviation's `amends` or `supersedes <clause-id>@<hash8>` row "in dOrderedCharter's overlay grammar". cl-0006 applies those rows, and cl-0004 reds "an approver below the risk", whose rule is `deviation.approval` (dDeclaredLoop's). dTrueNorth is the chain's root, and neither clause names a stand-in.
- **Consequence:** A dTrueNorth spec writer has to find the interim forms outside the clauses.
- **Fix:** Have cl-0004 and cl-0006 name their stand-ins, a fixed by-risk table and a local row form, each re-pointed when dOrderedCharter and dDeclaredLoop land.
- **Skeptic:** confirmed low. "Cannot be built" is refuted by this build's own instruments: `asbuilt.py` defines a local row form (`**Follow-through:** amends <clause-id>@<hash8>`), `deviations.py` hard-codes the by-risk table, and final-questions [bootstrap] turns them into product code with today's tools. What remains is the unnamed stand-in.

### C1-F18 — "A ninth join": spec-tokens already has nine
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0002
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0002 calls the carries join "a ninth join of the spec tokens leg". `tools/check-spec-tokens.py:30-36` counts eight joins, and `:959-960` adds a ninth, "THE COVERS JOIN (TOOL-aMendedFleet-75)".
- **Consequence:** The count is stale, and a builder looking for the ninth slot finds `covers` there.
- **Fix:** Call it "a further join".
- **Skeptic:** confirmed low. The carries join would be the tenth.

### C1-F19 — "Instruction packs … into the preset catalogue" reads against the rule that presets never touch `charter.practices`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0045
- **Class:** K9
- **Severity:** low
- **Evidence:** cl-0045: "instruction packs extending `charter.practices` into the preset catalogue". v2:1301-1302: "Presets never touch … `charter.practices`".
- **Consequence:** A builder may add packs to the policy presets, against the never-touch rule.
- **Fix:** Name it "a pack catalogue", separate from the policy presets.
- **Skeptic:** confirmed low. layer-instruction:584's "a preset catalogue" is a different thing from the policy presets, so this is wording only.

### C1-F20 — The card for other harnesses goes through Runtime harness adapters, which dWellOiledMachine builds later
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0038
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0038 delivers "another harness's [card] through its Runtime harness adapter". `runtime.harnesses` is owned by dWellOiledMachine (v2:1093), not an ancestor of dOrderedCharter, and no stand-in is named.
- **Consequence:** There is no adapter to deliver through when the build lands.
- **Fix:** Name agent-instructions' wiring as the stand-in until the adapters land.
- **Skeptic:** confirmed low.

### C2-F9 — dDeclaredLoop's guard-bearing keys `floor` and `transitions.record` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0087 and cl-dClosedLoop-0088
- **Class:** K4
- **Severity:** low (the walker said medium)
- **Evidence:** Stage 0's K4 lists `floor` and `transitions.record` as unread and guard-bearing. cl-0087 reads "the guard, the TTY CLI and the default floor", and cl-0088 "the transition record three ways"; neither names its key. [floor] makes each invariant "switchable only under the policy guard".
- **Consequence:** The switch that turns a floor invariant off, and the subset choice of transition-record channels, have no specced reader.
- **Fix:** Name `floor` in cl-0087 and `transitions.record` in cl-0088, each with a planted value seen red: an invariant switched off without the guard is refused, and an empty channel set is refused.
- **Skeptic:** confirmed low. The walker's "fails open" does not follow: hard-wiring the floor all on and all three channels is the stricter state, and cl-0014's arm reds an unread key once its Owner has landed.

### C2-F16 — "The panel's internals" does not carry the untyped harness agent gap that dFairHearing owns
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0078
- **Class:** K1
- **Severity:** low
- **Evidence:** gap-review-13 ("The review harness spawns an untyped agent that no stage declares") is dFairHearing's (systems:1000). cl-0078 says only "the panel's internals". The only "every stage naming its role" clause is cl-0187, in the later dBoundRoles.
- **Consequence:** A spec writer cannot tell from cl-0078 that the untyped spawn must be typed and declared.
- **Fix:** Add to cl-0078: "every agent the harness spawns typed and declared in a stage, seen red on a planted untyped spawn".
- **Skeptic:** confirmed low.

### C3-F3 — gap-roles-20, the static block's budget covering only its base body, is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-roles-20 (gap-register:171, "The static block's budget covers its base body only") is dBoundRoles's (v2:1641). layer-instruction:458 makes `BODY_CEILINGS` the role block's only budget carrier, research-instruction-writing-b N3 puts the 2,487–4,220 B charter blocks per role outside it, and `tools/roles/check_roles.py:84` reads "Bytes of each slot's BASE body". No clause of cl-0166 to cl-0191 budgets the whole rendered block.
- **Consequence:** The gap stays open after its owner lands, and the rendered charter blocks stay unbudgeted.
- **Fix:** Extend cl-0180: the budget covers the whole rendered static block, seen red on a planted charter block that pushes a role over its ceiling.
- **Skeptic:** confirmed low.

### C3-F22 — `annotations.resolve-scope` and `annotations.lookup` are not named
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 gives both keys to dLinkedLibrary (systems:363, 365): `annotations.resolve-scope` (notes, every-comment-ref) and `annotations.lookup` (query-and-map, query, map-index). No clause names either; cl-0244 carries AN-1's default behaviour in prose only. Stage 0's K4 lists both as unread.
- **Consequence:** `notes` and `map-index` never route.
- **Fix:** Name both keys in cl-0241 and cl-0244.
- **Skeptic:** confirmed low.

### C3-F23 — dLinkedLibrary owns gap-mem-11 and gap-mem-12, but no clause of it carries either
- **Address:** architecture-v2 [chain] dLinkedLibrary row, Gaps owned (`gap-mem-11`, `gap-mem-12`)
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-mem-11 covers records that contradict code: the map README path, `backlog.py`'s claim, the DEPL rows, `ANNOTATION-STYLE` saying no gate reads comment citations, and `HYGIENE.md`'s unused `note` kind. gap-mem-12: "the annotation follow-through test decides nothing: it has no threshold, sample size or window". No clause of cl-0238 to cl-0261 mentions either; a search of all clauses for follow-through, ANNOTATION-STYLE or `note` finds only cl-0241's grammar.
- **Consequence:** Both gaps survive their owner's landing, and the pushed-at-read fallback has no deciding test.
- **Fix:** Add a clause correcting gap-mem-11's records, including the ANNOTATION-STYLE guide and template pair. Set gap-mem-12's threshold, sample and window in cl-0244.
- **Skeptic:** confirmed low. layer-memory:1226 also gives gap-mem-12's threshold to dTotalRecall, not to the owner dLinkedLibrary.

### C3-F27 — The "one pin over three seams" rule is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0262
- **Class:** K10
- **Severity:** low
- **Evidence:** lexicon [classes] (lines 223-234): "`VERB_OFFENDER_PIN` becomes the debt pin. `SUFFIX_OFFENDER_PIN` folds into it … The per-cell `PINS:` block retires", and "Two cells re-arm. `py.file` and `py.constant`". cl-0262 names only "the shrink-only pin", and cl-0276 only "records kept out by the path selector". `tools/lexicon/lexicon.py:121` still holds both pins in `PIN_KEYS`.
- **Consequence:** The suffix pin and the per-cell pins survive as separate waivers beside the debt pin.
- **Fix:** Carry the fold, the `PINS:` retirement and the two cells' re-arming in cl-0262 and cl-0276.
- **Skeptic:** confirmed low.

### C3-F29 — The deployer's registration omits distribution's contract
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0166
- **Class:** K10
- **Severity:** low
- **Evidence:** layer-roles [roster] (lr:462, 466) and flow-steps [consequences] ("it registers under both") register the deployer under distribution and integrations: release notes for distribution, verify judgment for integrations. cl-0166 registers it only "through the integrations and observability layer contracts".
- **Consequence:** The release-notes item has a role its expansion never registers, so P28's no-expansion-role-in-core arm may red on it.
- **Fix:** Add distribution's contract to cl-0166.
- **Skeptic:** confirmed low.

### C3-F31 — The span rule's owed re-measure is not carried
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0254
- **Class:** K10
- **Severity:** low
- **Evidence:** v2 [owed]: "the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside spans sit in a derivable definition (point 4)". No clause carries "span share" or "80%", and cl-0254 builds the span rule with no losing test.
- **Consequence:** The hybrid span rule is built with no test that could reject it.
- **Fix:** Add the re-measure and its 80% bound to cl-0254.
- **Skeptic:** confirmed low.

### C5-F2 — "The memory's dead pointers" misnames the gate cl-0448 absorbs, whose population lies outside `memory/`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0448
- **Class:** K10
- **Severity:** low (the walker said high, c3)
- **Evidence:** cl-0448: "a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its merge-bar leg". `tools/check-dead-paths.sh:2` covers "nothing outside `memory/`, and no map dossier or gotcha page" naming a deleted file, and its leg is "dead-path carriers (deleted files still named)".
- **Consequence:** The wording points a builder at memory pointers rather than the shipped-text population the absorbed gate checks.
- **Fix:** Name both populations in cl-0448: the old gate's shipped text, dossiers and gotchas, plus the auto-memory pointers.
- **Skeptic:** confirmed low (wording). The clause keeps the script's merge-bar leg (NP-22, night-pass:755: "so a dead path still blocks a merge"). The script is an `[[exempt]]` row at `tools/govkit/registry.toml:242`, so no adopter install ever carried it and no core-only install loses it.

### C5-F18 — When the closing review runs is a dScopedBuild key no clause reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0402
- **Class:** K4
- **Severity:** low
- **Evidence:** `review.build.when` (per-build, per-unit, per-landing; v2:1208, dScopedBuild) is named by no clause, and no flow-steps item reads it. cl-0402 reads only "the closing review recorded".
- **Consequence:** The per-unit and per-landing values pass the schema and run per build.
- **Fix:** cl-0402: "the closing review recorded, run as `review.build.when` says", each value planted.
- **Skeptic:** confirmed low.

### C5-F19 — Plan's triage, kickoff and authority keys are built only at their defaults
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0371, cl-dClosedLoop-0375 and cl-dClosedLoop-0370
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 offers `plan.triage` (owner-batches, rules, archive-legacy), `plan.kickoff` (offer-next, binding, advisory) and `plan.authority` (planner-drafts-owner-ratifies, planner-within-themes, owner-orders), and Stage 0's K4 lists all three as unread. cl-0371 carries "rule-based triage", cl-0375 "kickoff offering the next item", and cl-0370 names no `plan.authority`. The presets select `owner-batches`, `binding` and `owner-orders` (v2:1469-1472), which no clause builds.
- **Consequence:** The other values, including those the presets select, are accepted by the schema and never take effect.
- **Fix:** Name each key in its clause, with each value's arm planted.
- **Skeptic:** confirmed low.

### C5-F20 — "Runs neither … both" in cl-0430 has no antecedent inside the clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0430
- **Class:** K1
- **Severity:** low
- **Evidence:** cl-0430: "an update `kits.offer` offers runs neither in the adopter's tree, and its outbox order names the adopter's own run of both". The referents, `adopt` and `test.seed`, are named only in cl-0427, and the carries hash pins the clause text alone.
- **Consequence:** A spec carrying cl-0430 whole cannot tell which runs are withheld.
- **Fix:** Reword: "… runs neither `adopt` nor `test.seed` in the adopter's tree, and its outbox order names the adopter's own run of each".
- **Skeptic:** confirmed low.

### C5-F22 — The fates join's population leaves out rows the table holds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0488
- **Class:** K10
- **Severity:** low
- **Evidence:** cl-0488's population is "`git ls-files` across `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, the runbook and the template". The fates table has "hand-written guides | RETIRED" (fates:210, under `memory/guides/`) and `.unattended.conf` (fates:158) at the repository root.
- **Consequence:** A guide or a root kit conf that survives convergence matches no file in the population and escapes the exit check.
- **Fix:** Derive the population from every fates row's path glob plus the listed directories, and plant a surviving `memory/guides/` file to see it red.
- **Skeptic:** confirmed low.

### CS3-F1 — The decision routing's below-kappa outcome is not carried, and the record's re-run loop has no bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0238
- **Class:** K10 (a loop with no end, P39)
- **Severity:** low
- **Evidence:** cl-0238 has "today's 200 rows routed by two raters at kappa 0.8 or better", with no outcome below the bar. layer-memory [decisions] (lines 678-682): "Below kappa 0.8 the rubric is revised and the routing re-run, and no row moves until it passes", with no cap. Its debt-fold row `kappa-below-threshold` (line 1193) is the fix the clause leaves out.
- **Consequence:** A spec carrying cl-0238 has no route below the bar. The record's route is revise-and-re-run until the bar passes, which P39 forbids, so the major-decision log can stay unrouted indefinitely.
- **Fix:** Carry the below-kappa route in cl-0238, with a bound: a set number of rubric revisions, then an owner item.
- **Skeptic:** raised by skeptic batch 3 on re-walking cl-0238, which walker 3 had passed as holding. No second skeptic judged it.

## Unverified

A skeptic refuted each finding below and a second confirmed it, so it stands unverified.

### C4-F7 — Lease expiry by "tip unchanged" cannot fire while the fenced pushes keep moving the tip
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324 (with cl-dClosedLoop-0284 and cl-dClosedLoop-0293)
- **Claim:** A looping holder that commits pushes a new lease beat at every pass, so its lease never expires.
- **Skeptic:** refuted. Under `build.push`'s default `every-pass`, a push and its lease beat (cl-0133) happen only at a pass commit, which is itself a witness. A holder looping without a witness makes no pass push, so its tip stays unchanged and the lease expires, as cl-0324's arm and layer-runtime's `renewal` fixture (line 1246) require. A holder whose commits are witnessed passes is making progress, so renewal there is intended.
- **Second skeptic:** Confirmed medium. cl-dClosedLoop-0133 makes every effect push carry a new lease beat, which moves the lease tip ("a re-push of an unchanged lease ref never counting as the fence"). `build.push` defaults to `every-pass`. cl-dClosedLoop-0135 and the `leases.expiry-hours` row judge expiry by "an observer seeing the tip unchanged". No clause separates a fence beat from a progress renewal. So layer-runtime:1246's `renewal` holder, "whose acts write commits … but never a witness", keeps moving the tip, and cl-dClosedLoop-0324's arm cannot go red under the observer rule.

### C5-F23 — `design.streams` names both an item and a key, and the planner item's Needs loops onto itself
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0397
- **Claim:** The needs graph and the tag index cannot tell the item from the key.
- **Skeptic:** refuted. flow-steps:188's Needs cell is "`design.overlaps`, where `design.streams` holds for the build". The only edge is to `design.overlaps`, the second name is a policy condition, and Stage 0's "cycle" is a parser artifact. The design map keeps items and policy keys in separate namespaces, as with `build.scope`, which cl-0407 grades by value without ambiguity.
- **Second skeptic:** Confirmed low. `design.streams` is both the planner item (flow-steps:188) and a key (v2:1160). The item's Needs cell reads "`design.overlaps`, where `design.streams` holds for the build", which is the self-cycle Stage 0's K1 reports (stage0-leads:13). The design's own precedent renamed `maintain.record-when` "so the item `maintain.record` keeps its name" (v2:1199). The impact is a naming collision only.

## Refuted

### C1-F4 — The join factory moves to `tools/lib`, which no adopter receives
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049
- **Claim:** After an update, a copy-installed codebase-map re-exports the moved factory from a `tools/lib` that was never installed, so its imports fail.
- **Skeptic:** refuted. retrofit.md:203-206 says both factories, including "`map_lib.compute_coverage` … the join factory", reach a copy-installed adopter as an inline copy, and each kit calling a factory carries a generated copy until the regen lands. cl-0351 and cl-0364 repeat the inline rule. Only cl-0049's not restating the rule remains.
- **Second skeptic:** Refuted. The finding says no clause or record has the moved functions carried inline, and that is false. retrofit.md:203-206 ("How it reaches an adopter") says both factories reach a copy-installed adopter as an inline copy, regenerated under dShippedRelease's `gap-tool-04` regen and its drift gate. Until that regen lands, "each kit that calls a factory carries a generated copy from its first unit". cl-dClosedLoop-0351 restates it ("reaching copy-installed adopters as every `tools/lib` primitive does"), and cl-dClosedLoop-0431 marks lib as not installable. So the adopter does not end up importing from a module that was never installed.

### C1-F17 — The render gate's legacy list is hard-wired shrink-only, so strict's `instructions.legacy: refuse` has no arm
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0050
- **Claim:** Under strict, a legacy document is still admitted.
- **Skeptic:** refuted. cl-0260 (dLinkedLibrary) reads `instructions.legacy` and gives `refuse` its arm ("under `refuse` admitted only with every paragraph ruled before the first landing"). Only cl-0050's interim wording remains.
- **Second skeptic:** Refuted. Strict's `refuse` does have an arm. cl-dClosedLoop-0260 (dLinkedLibrary) reads `instructions.legacy` and admits an adopter's legacy block "under `refuse` … only with every paragraph ruled before the first landing". It is seen red "on a planted strict install carrying an existing `CLAUDE.md`". cl-dClosedLoop-0050's shrink-only list is gov's own starting list, so a legacy document is not still admitted under strict.

### C2-F5 — Items declare a `map` slot before any ancestor registers it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0124
- **Claim:** dPlacedRequest's spec cites a work-order slot and a map that do not exist when it lands, with no stand-in.
- **Skeptic:** refuted. cl-0124 only declares data on items and reads nothing. Its reader, cl-0203 (dFurnishedOrders, a descendant), carries the stand-in "rendering 'not installed' until dTotalRecall's renderer lands". project-map's owners table (pm:717-718) deliberately puts the declarations in an earlier build than the slot, and the sibling cl-0126 has the same shape. The missing `memory.map-unfold` reader is carried by C3-F5.
- **Second skeptic:** Refuted. cl-dClosedLoop-0124 writes item declarations: the namespaces an item unfolds, which cl-dClosedLoop-0049's registry already holds. It reads nothing that no ancestor registers, which is what K6 requires. The reader of those declarations is cl-dClosedLoop-0203 (dFurnishedOrders), and it declares its own stand-in: the slot renders "'not installed' until dTotalRecall's renderer lands". project-map:718 placed the declarations even earlier (dDeclaredLoop), so the forward declaration is deliberate.

### C2-F14 — The commit kind's position-engine reader has no writer until the commit queue lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0108
- **Claim:** Between dDeclaredLoop and dWellOiledMachine the engine reads `Gov-*` trailers no commit carries, with no rule for falling back to subjects.
- **Skeptic:** refuted. cl-0108 registers the interim reader itself: "`Pass:` and `Decided:` registered with one reader that offers both views today's readers answer, the union of subject and trailer ids `routed_commits.py` reads". Today's commits carry those trailers.
- **Second skeptic:** Refuted. cl-dClosedLoop-0108's one reader "offers both views today's readers answer, the union of subject and trailer ids", with "each consumer naming its view". It also maps today's `Pass:` trailer to `serves`. So the position engine has populated subject and `Pass:` ids before the commit queue exists, and there is a stated rule for what it reads in the meantime.

### C3-F19 — The resolve check can go green on an empty population
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0241
- **Claim:** The resolve check's first green proves nothing, because its planted reds and non-empty assertion are not carried.
- **Skeptic:** refuted. systems [design-annotations] (lines 344-350) makes the resolve check one of the `annotations` leg's checks, "each seen red on a planted case first", and cl-0244 names that leg. The population is not empty: the check "is red on day one on the gotcha path that never existed", and under the default `annotations.resolve-scope: every-comment-ref` layer-memory:795 counts 35 cited ids that resolve nowhere.
- **Second skeptic:** Refuted. The check cannot go green on an empty population. The resolve check's pin is a ratchet (layer-memory:790, "shrink-only through the RATCHETS row"). The ratchet pack at cl-dClosedLoop-0352 has a `populated` row, and with cl-dClosedLoop-0353 (dWitnessedBar, an ancestor) an empty population "reads unarmed, until a planted row has been seen red" (retrofit.md:335-336). Also, standard's `annotations.resolve-scope` is `every-comment-ref` (v2 presets), whose population is not empty (layer-memory:795). The three planted reds are owed by the layer-memory section that cl-dClosedLoop-0241 builds.

### C3-F21 — The touched-block comment budget is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Claim:** New long comment blocks pass, and gap-mem-18 stays open.
- **Skeptic:** refuted. cl-0244 carries the `annotations` leg, and systems:350 lists "the touched-block budget" among that leg's checks. Since NT-22 the cap is a `budgets.*` value, and cl-0015's `budgets.enforce` decides whether a breach warns or refuses, warning by default, so a long new block passing with a warning is the owner's setting. cl-0248 handles the legacy blocks.
- **Second skeptic:** Refuted. cl-dClosedLoop-0244 builds "the `annotations` leg". systems [design-annotations]:342-350 defines that one leg's checks, "each seen red on a planted case first", and "the touched-block budget" is one of them; that section names dLinkedLibrary as owner. cl-dClosedLoop-0248 registers the untouched blocks "over 12 lines, the touched-block cap" as the complement. The budget is carried; the clause just names the leg rather than listing its checks.

### C3-F30 — The lexicon declaration kind has no declared writer or reader in any clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0269
- **Claim:** The kind's registry row has no door, and the one-door check cannot grade it.
- **Skeptic:** refuted. cl-0271 names `instructions.edit` for the families the owner declares, cl-0272 changes the vocabulary "only through the instruction write path", and lexicon [vocabulary] (lines 392-400) puts pack selection and custom packs under that path. The readers are the lexicon's own checks (cl-0270, cl-0271). The K3 lead reads only flow items as writers, and says so.
- **Second skeptic:** Refuted. The writer, door and readers are all in clauses. cl-dClosedLoop-0269 says "declared by the owner". cl-dClosedLoop-0271 says the families are declared "by the owner through `instructions.edit` (LX-1)", and cl-dClosedLoop-0272 says the vocabulary changes "only through the instruction write path". cl-dClosedLoop-0270 and cl-dClosedLoop-0274 read the declared families. dTotalRecall's registry clause has a later kind land its own row with its conformance arm. The "writer item not named" wording in layer-memory:471 is shared by about a dozen kinds in that table.

### C5-F4 — The playbook gate lives in the kit that convergence deletes, and no clause moves it out first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0486 (and cl-dClosedLoop-0392)
- **Claim:** Under cl-0486's "re-pointed or retired", a builder may retire the playbook gate with the unattended kit.
- **Skeptic:** refuted. cl-0392 already makes `check-playbook` "Design's pack" in dIndexedDesign, fates:151 marks it RESHAPED into that pack, and cl-0488 runs "every part in the fates table at its fate" as convergence's exit check, so retiring the leg under cl-0486 would turn that check red. The code facts hold.
- **Second skeptic:** Refuted. cl-dClosedLoop-0392 (dIndexedDesign, an ancestor of dConvergedCharter) already makes `check-playbook` Design's pack. The fates row (fates.md:151) marks it RESHAPED into that pack, with pieces built as units in dScopedBuild. When cl-dClosedLoop-0486 inventories readers to re-point or retire, it finds a leg its ancestor already declared live under Design, so retiring it would contradict 0392. The evidence itself checks out: the leg's argv is `{prefix}/unattended/check-playbook.sh` in tools/gate-legs.json, and the recorders are at unattended.sh:29-30.

### C5-F6 — Caps, the rework budget and deadlines are "re-derived" with no route through the owner
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0461, cl-dClosedLoop-0473 and cl-dClosedLoop-0474
- **Claim:** A builder can apply re-derived values directly, loosening a loop bound unattended or overwriting an owner's cap.
- **Skeptic:** refuted. Re-derivation is `loop.propose`'s, whose only route is `loop.file`, into Plan's triage and the owner's breakpoint (layer-expansions:260-261). The `budgets.*` row (v2:1217) makes each cap's value the owner's, cl-0116 makes raising the budget the owner's alone, and cl-0118 reads a raised loop bound as a loosening that waits for the owner.
- **Second skeptic:** Refuted. A builder cannot apply re-derived values directly. cl-dClosedLoop-0012 refuses agent writes to the policy file (owner-only, with the TTY proof). layer-expansions:260-261 routes `loop.propose`, which "re-derives the caps", through `loop.file` to "the owner's breakpoint". cl-dClosedLoop-0017 makes raising a loop bound a declared loosening, and cl-dClosedLoop-0118 has it wait for the owner. No unattended loosening or overwrite of an owner's cap is reachable.

### C5-F15 — The deviation and coverage gaps are owned by the bootstrap build, not the build whose gate closes them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0412 (and cl-dClosedLoop-0398)
- **Claim:** The gap join reads gap-build-07 and gap-design-13 as closed when dTrueNorth lands, before any gate exists.
- **Skeptic:** refuted. dTrueNorth's own clauses close both gaps when it lands. For gap-design-13, cl-0002 builds the carries join with its reds, and cl-0003 refuses a chain build's spec while its coverage is red. For gap-build-07, cl-0004 joins the deviation population at the commit and at the close, seen red on a planted revision with no record. cl-0398 and cl-0412 only add the policy-keyed exits.
- **Second skeptic:** Refuted. dTrueNorth already gates both gaps. cl-dClosedLoop-0002's carries join is a leg with red arms, for example "a revision that stops carrying a clause with no decision". cl-dClosedLoop-0003 refuses a chain spec while coverage is red. cl-dClosedLoop-0004 joins deviations "at the commit … and at the close", seen red on "a planted revision after a pass with no record". So reading gap-build-07 and gap-design-13 as closed at dTrueNorth is correct. cl-dClosedLoop-0398 and cl-dClosedLoop-0412 extend those gates under their keys.

### C5-F17 — The reuse check's re-entries omit the rework budget and the non-converging end
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0410
- **Claim:** A reuse-check loop built from the clause neither draws on the build's budget nor files its open rows as asks.
- **Skeptic:** refuted. The ancestor cl-0115 (dDeclaredLoop) gives one rework budget per build with "every repetition drawing on it", and makes `flow.route-backs` the per-item limit past which the loop ends non-converging with its open work going to asks. The engine applies both to cl-0410's fix passes.
- **Second skeptic:** Refuted. cl-dClosedLoop-0115 (dDeclaredLoop, an ancestor of dScopedBuild) already does this for every loop. Every repetition, "a fix pass" included, draws on the build's rework budget. `flow.route-backs` is "the per-item early limit past which that item's loop ends non-converging and its open work goes to asks". cl-dClosedLoop-0410's fix-pass re-entries inherit both, so the budget stays single per build.

## Clause table

Verdicts are the walkers'. A refuted id in a row stands refuted under Refuted. The skeptics' own findings on cl-0154, cl-0160, cl-0238, cl-0378 and cl-0415 do not appear in the rows.

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0001 | dTrueNorth | final-questions [spine] [coverage]; whole-audit [instruments]; v2 P33, P41; memory-plan [edges] | C1-F8 |
| cl-dClosedLoop-0002 | dTrueNorth | final-questions [coverage] join arms; tools/check-spec-tokens.py | C1-F18 |
| cl-dClosedLoop-0003 | dTrueNorth | final-questions [coverage] owner's report, [bootstrap]; gap-design-13 | holds |
| cl-dClosedLoop-0004 | dTrueNorth | final-questions [deviation] [spine]; stage0 leads; v2 catalogue deviation.approval; gap-build-07 | C1-F7, C1-F9 |
| cl-dClosedLoop-0005 | dTrueNorth | final-questions [bootstrap]; memory/HYGIENE.md record bindings | holds |
| cl-dClosedLoop-0006 | dTrueNorth | final-questions [spine] [deviation]; cl-0058 and cl-0063; gap-mem-47 | C1-F7 |
| cl-dClosedLoop-0007 | dGroundRules | v2 [policies] empty-set rule; shape-reviews `empty-sets`; final-questions [folded]; gap-spine-06 | holds |
| cl-dClosedLoop-0008 | dGroundRules | v2 [policies]; tools/push-main.sh, .githooks/pre-push read_policy_key | holds |
| cl-dClosedLoop-0009 | dGroundRules | v2 [policies], [presets] rules; standard vs defaults comparison | holds |
| cl-dClosedLoop-0010 | dGroundRules | v2 `policy-file.on-invalid` row; [presets] | holds |
| cl-dClosedLoop-0011 | dGroundRules | v2 [policies] mirror text, `policy-file.on-invalid` | holds |
| cl-dClosedLoop-0012 | dGroundRules | shape-reviews SA-12; adopter-instructions [chain]; v2 [witnesses] | holds |
| cl-dClosedLoop-0013 | dGroundRules | v2 [policies] kit-conf passage; .githooks/gate-env.sh header and keys; .githooks/pre-push GATE_POST_MERGE | holds |
| cl-dClosedLoop-0014 | dGroundRules | v2 catalogue Owner column; stage0 K4 leads | holds |
| cl-dClosedLoop-0015 | dGroundRules | night-pass-two [p5-caps]; v2 `budgets.*`, `budgets.enforce`, `budgets.pinned`; P9; gap-tool-24 | C1-F13, C1-F14 |
| cl-dClosedLoop-0016 | dGroundRules | night-pass-two [p7-agent-cap] [answers]; v2 `runtime.agents-in-flight`; tools/hooks/agent-cap.js, README.md; P38; gap-rt-34 | C1-F5 |
| cl-dClosedLoop-0017 | dGroundRules | v2 P39, `run.on-owner-silence`, `flow.rework-budget` rows | holds |
| cl-dClosedLoop-0018 | dSafePassage | shape-reviews `released-steps-frozen`; P38; gap-deploy-15, gap-deploy-16 | holds |
| cl-dClosedLoop-0019 | dSafePassage | shape-reviews `walk-failure-route`, SA-2; gap-deploy-19 | holds |
| cl-dClosedLoop-0020 | dSafePassage | shape-reviews `receipt-schema`; tools/govkit/govkit.py RECEIPT_SCHEMA and back-fill scope | holds |
| cl-dClosedLoop-0021 | dSafePassage | shape-reviews `walk-failure-route`; gap-deploy-17 | holds |
| cl-dClosedLoop-0022 | dSafePassage | shape-reviews SA-8; gap-tool-10 | holds |
| cl-dClosedLoop-0023 | dSafePassage | v2 `install.deprecation-window`, `install.on-shim-call`, pair rule; SA-8; gap-deploy-24 | holds |
| cl-dClosedLoop-0024 | dSafePassage | shape-reviews `step-contract`; dShippedRelease cl-0435 | holds |
| cl-dClosedLoop-0025 | dSafePassage | shape-reviews SA-3; adopter-instructions [reviewed]; gap-deploy-20 | holds |
| cl-dClosedLoop-0026 | dSafePassage | v2 `install.retired-edits`; research-supersession F5; govkit selfcheck 7g; gap-deploy-18 | C1-F15 |
| cl-dClosedLoop-0027 | dSafePassage | shape-reviews SA-11; flow-roles-adoption item 14; gap-deploy-25 | holds |
| cl-dClosedLoop-0028 | dSafePassage | P37; v2 `platforms.provision`; shape-reviews `floor-query`; tools/settings-merge.py; merge-rows.test.sh PEP 701 ban; gap-tool-12, gap-tool-22 | C1-F16 |
| cl-dClosedLoop-0029 | dSafePassage | gap-tool-23; shape-reviews `emitted-ci-pins` | holds |
| cl-dClosedLoop-0030 | dSafePassage | final-questions [help]; v2 `help.enforce`; P42; gap-found-35 | holds |
| cl-dClosedLoop-0031 | dOrderedCharter | foundations step 1 settled; v2 `charter.practices`, P14 | holds |
| cl-dClosedLoop-0032 | dOrderedCharter | v2 [front-door]; foundations step 1; layer-instruction R-B; tools/roles/roles_lib.py; gap-flow-02, gap-found-18; stage0 K3 override | C1-F2, C1-F10, C1-F11, C1-F12 |
| cl-dClosedLoop-0033 | dOrderedCharter | foundations R2; P13 | holds |
| cl-dClosedLoop-0034 | dOrderedCharter | foundations R2 re-derivation; gap-found-01 | holds |
| cl-dClosedLoop-0035 | dOrderedCharter | foundations step 1; gap-found-03 | holds |
| cl-dClosedLoop-0036 | dOrderedCharter | foundations R3, F1-6; night-pass-two [p5-caps] item 5; tools/template-size-limits.txt | holds |
| cl-dClosedLoop-0037 | dOrderedCharter | foundations [core] C1 to C7; stage0 K3 exception lead; gap-found-07, gap-found-08 | C1-F12 |
| cl-dClosedLoop-0038 | dOrderedCharter | layer-instruction R-K; gap-orient-13 | C1-F20 |
| cl-dClosedLoop-0039 | dOrderedCharter | layer-instruction R-A; systems [design-instruction-writing] unit fields; memory-plan [sites] | C1-F1 |
| cl-dClosedLoop-0040 | dOrderedCharter | systems [design-tags] grammar, namespaces, owners; flow-roles-adoption [renamed] | holds |
| cl-dClosedLoop-0041 | dOrderedCharter | layer-instruction R-C; P27; night-pass-two [p5-caps]; v2 `instructions.checks`, `budgets.*`; gap-found-10, gap-found-34 | C1-F1, C1-F13 |
| cl-dClosedLoop-0042 | dOrderedCharter | layer-instruction R-D; P11; gap-found-11 | holds |
| cl-dClosedLoop-0043 | dOrderedCharter | layer-instruction R-G; v2 [front-door] ladder | holds |
| cl-dClosedLoop-0044 | dOrderedCharter | layer-instruction R-H; P30; gap-found-14 | holds |
| cl-dClosedLoop-0045 | dOrderedCharter | layer-instruction R-I; v2 `instructions.edit`, `instructions.proof`, [presets] never-touch list; gap-found-15 | C1-F19 |
| cl-dClosedLoop-0046 | dOrderedCharter | P28; tools/memory-tree imports from memory-recall (row_grammar.py, backlog.py, corpus_ids.py, merge-rows.py, transition_audit.py, gen_build_index.py); gap-found-17 | holds |
| cl-dClosedLoop-0047 | dOrderedCharter | P28; core-kit references to optional kits over tools/; gap-found-17 | holds |
| cl-dClosedLoop-0048 | dOrderedCharter | grep of extract.py and recall_conf readers by path; check-verdict-epoch.sh DELEGATES | C1-F6 |
| cl-dClosedLoop-0049 | dOrderedCharter | systems [design-tags]; v2 tags.* keys; stage0 K4; tools/codebase-map/map_lib.py consumers; tools/lib inline rule; gap-found-33 | C1-F3, C1-F4 |
| cl-dClosedLoop-0050 | dOrderedCharter | systems [design-instruction-writing] renderer and checks; v2 `instructions.legacy`; gap-found-23 | C1-F17 |
| cl-dClosedLoop-0051 | dOrderedCharter | v2 [front-door] (IW-2); P14; gap-found-02 | holds |
| cl-dClosedLoop-0052 | dOrderedCharter | v2 `memory.map-purpose`; owed PM-5 | holds |
| cl-dClosedLoop-0053 | dOrderedCharter | P4, P20; v2 `attendance` | holds |
| cl-dClosedLoop-0054 | dOrderedCharter | P33; memory-plan [edges]; gap-found-24, gap-found-25 | holds |
| cl-dClosedLoop-0055 | dOrderedCharter | v2 `tags.bundle`, `tags.bundle-rows`; systems [design-tags] | holds |
| cl-dClosedLoop-0056 | dOrderedCharter | v2 `tags.positional`; night-pass NP-17; gap-found-26 | holds |
| cl-dClosedLoop-0057 | dOrderedCharter | v2 `memory.code-budget`; P27, P32 | holds |
| cl-dClosedLoop-0058 | dOrderedCharter | memory-plan [sites] [edges]; shape-reviews `edge-grammar`, `p33-addresses`; gap-mem-35 | C1-F8 |
| cl-dClosedLoop-0059 | dOrderedCharter | memory-plan [practice] [doors]; shape-reviews `p34-rationale-owned` | holds |
| cl-dClosedLoop-0060 | dOrderedCharter | P37; shape-reviews `p37-legs-missing`; gap-tool-19 | holds |
| cl-dClosedLoop-0061 | dOrderedCharter | adopter-instructions [design] items 16 and 17; shape-reviews `unattended-inventory`; P38; gap-found-30 | holds |
| cl-dClosedLoop-0062 | dOrderedCharter | adopter-instructions [design] items 1 to 8, [reviewed]; systems [design-tags]; P8; gap-found-29 | holds |
| cl-dClosedLoop-0063 | dOrderedCharter | adopter-instructions items 9 and 10, [reviewed]; v2 `instructions.stale` | holds |
| cl-dClosedLoop-0064 | dOrderedCharter | adopter-instructions items 12, 14 and 16; night-pass-two [p5-caps]; P8; gap-found-31 | holds |
| cl-dClosedLoop-0065 | dOrderedCharter | flow-roles-adoption [design] items 2 to 6, 13 and 14, [renamed] | holds |
| cl-dClosedLoop-0066 | dOrderedCharter | flow-roles-adoption [design] items 6, 9 and 10, [chain] | holds |
| cl-dClosedLoop-0067 | dOrderedCharter | final-questions [help]; P42; systems unit `usage` and `help` fields | holds |
| cl-dClosedLoop-0068 | dFairHearing | review-system [lenses] replay isolation, bar and scorer | holds |
| cl-dClosedLoop-0069 | dFairHearing | review-system [lenses] "How it is selected"; flow-steps `review.pin` | holds |
| cl-dClosedLoop-0070 | dFairHearing | review-system [lenses] channel and boundary check; flow-steps [breakpoint] | C2-F6 |
| cl-dClosedLoop-0071 | dFairHearing | review-system [adjudication] batches by address | holds |
| cl-dClosedLoop-0072 | dFairHearing | review-system [adjudication] duplicates; gap-review-08 | holds |
| cl-dClosedLoop-0073 | dFairHearing | review-system [adjudication] grade per id; gap-review-05 | holds |
| cl-dClosedLoop-0074 | dFairHearing | review-system [adjudication] twins; gap-review-06 | holds |
| cl-dClosedLoop-0075 | dFairHearing | review-system [adjudication] homing; flow-steps `review.report`; Stage 0 K2 | C2-F6 |
| cl-dClosedLoop-0076 | dFairHearing | review-system [lenses] anchored entries and lens notes | holds |
| cl-dClosedLoop-0077 | dFairHearing | review-system [stale]; gap-review-09; tools/workflows, tools/hooks/agent-cap.js:495, tools/roles/agents | holds |
| cl-dClosedLoop-0078 | dFairHearing | systems [design-role-shapes] owners; gap-review-12 and gap-review-13 | C2-F16 |
| cl-dClosedLoop-0079 | dFairHearing | flow-steps [probe] experiment shape; gap-test-18; research-testing-anywhere F6 | holds |
| cl-dClosedLoop-0080 | dFairHearing | flow-roles-adoption [design] 3 and [chain]; night-pass-two [p7] | holds |
| cl-dClosedLoop-0081 | dFairHearing | night-pass-two [p2] item 6; flow-steps [probe] | holds |
| cl-dClosedLoop-0082 | dFairHearing | night-pass-two [p6] NT-25; gap-review-20 | holds |
| cl-dClosedLoop-0083 | dFairHearing | night-pass-two [p7] rule table; tools/workflows/check-review-join.sh | holds |
| cl-dClosedLoop-0084 | dFairHearing | stall-and-loop [design] 4 and [chain]; gap-review-21; P39 | holds |
| cl-dClosedLoop-0085 | dFairHearing | final-questions [audit]; catalogue `review.design-audit.*`; gap-review-22 | holds |
| cl-dClosedLoop-0086 | dDeclaredLoop | P1; gap-spine-01; coordination [chain]; walk roster | holds |
| cl-dClosedLoop-0087 | dDeclaredLoop | v2 [floor] and [witnesses]; Stage 0 K4 | C2-F9 |
| cl-dClosedLoop-0088 | dDeclaredLoop | catalogue `transitions.record`; Stage 0 K3 and K4 | C2-F9 |
| cl-dClosedLoop-0089 | dDeclaredLoop | P1 coverage gate; gap-spine-01 | holds |
| cl-dClosedLoop-0090 | dDeclaredLoop | P2; flow-steps [rules]; gap-spine-02 | holds |
| cl-dClosedLoop-0091 | dDeclaredLoop | P16; ownership of factories | holds |
| cl-dClosedLoop-0092 | dDeclaredLoop | layer-runtime [decide] answer set; P22; gap-orient-03; P23 (see C2-F1) | holds |
| cl-dClosedLoop-0094 | dDeclaredLoop | P24; flow-steps [rules] | holds |
| cl-dClosedLoop-0095 | dDeclaredLoop | flow-steps [transitions] backward rows | holds |
| cl-dClosedLoop-0096 | dDeclaredLoop | P11; flow-steps [rules] | holds |
| cl-dClosedLoop-0097 | dDeclaredLoop | P24, P20; gap-flow-13 | holds |
| cl-dClosedLoop-0098 | dDeclaredLoop | flow-steps [transitions]; gap-flow-15; Stage 0 K2 | C2-F8 |
| cl-dClosedLoop-0099 | dDeclaredLoop | flow-steps [rules] refusal route | holds |
| cl-dClosedLoop-0100 | dDeclaredLoop | flow-steps [transitions] terminal list; P20 | C2-F8 |
| cl-dClosedLoop-0101 | dDeclaredLoop | flow-steps `entry.place` closed set; gap-flow-13 | holds |
| cl-dClosedLoop-0102 | dDeclaredLoop | P2; gap-flow-14; flow-steps [probe] | holds |
| cl-dClosedLoop-0103 | dDeclaredLoop | flow-roles-adoption [renamed]; tag-namespace owners in the design map | holds |
| cl-dClosedLoop-0104 | dDeclaredLoop | flow-steps [breakpoint] owner gate; P7; gap-flow-11 | holds |
| cl-dClosedLoop-0105 | dDeclaredLoop | flow-steps [breakpoint] item table and owners | holds |
| cl-dClosedLoop-0106 | dDeclaredLoop | catalogue v2:1127-1128; [presets] pair rule; unattended.sh:774,783; fates | C2-F3 |
| cl-dClosedLoop-0107 | dDeclaredLoop | flow-steps [rules] recommendation; gap-flow-12 | holds |
| cl-dClosedLoop-0108 | dDeclaredLoop | memory-plan [sites] and [edges]; gap-spine-08 and -09; routed_commits.py, lib-unattended.sh:1055, runlog/model.py:592 | C2-F14 |
| cl-dClosedLoop-0109 | dDeclaredLoop | flow-roles-adoption [design] items 6, 9, 11 and 14 | holds |
| cl-dClosedLoop-0110 | dDeclaredLoop | flow-roles-adoption [folded] FA-3; P20 | holds |
| cl-dClosedLoop-0111 | dDeclaredLoop | flow-roles-adoption [design] 14-15, FA-7 | holds |
| cl-dClosedLoop-0112 | dDeclaredLoop | night-pass-two [p1] NT-1, NT-6, NT-7; catalogue `flow.scenario-*` | holds |
| cl-dClosedLoop-0113 | dDeclaredLoop | night-pass-two [p1] NT-4; catalogue `flow.adapt` | holds |
| cl-dClosedLoop-0114 | dDeclaredLoop | night-pass-two [p2] item 3 and [p4] contract | holds |
| cl-dClosedLoop-0115 | dDeclaredLoop | stall-and-loop [design] 1-2 and [chain]; catalogue `flow.rework-budget`; gap-flow-23 | holds |
| cl-dClosedLoop-0116 | dDeclaredLoop | stall-and-loop [design] 3; catalogue `flow.on-exhausted`; flow-steps [transitions]; P20 | C2-F2 |
| cl-dClosedLoop-0117 | dDeclaredLoop | stall-and-loop [design] 4; catalogue `review.follow-up` and `review.max-rounds` | holds |
| cl-dClosedLoop-0118 | dDeclaredLoop | stall-and-loop [design] 8 and [chain]; gap-flow-24 | C2-F13 |
| cl-dClosedLoop-0119 | dDeclaredLoop | final-questions [deviation]; catalogue `deviation.approval`; P41 | holds |
| cl-dClosedLoop-0120 | dPlacedRequest | coordination [design] 1-5; catalogue `leases.*`; P5; Stage 0 K4 | C2-F10 |
| cl-dClosedLoop-0121 | dPlacedRequest | catalogue `card.*` and `resume.*`; P22 | C2-F10 |
| cl-dClosedLoop-0122 | dPlacedRequest | flow-steps [entry] items and owners; Stage 0 K2 | C2-F7 |
| cl-dClosedLoop-0123 | dPlacedRequest | flow-steps `entry.place`; catalogue `placement*`; Stage 0 K2 | C2-F7 |
| cl-dClosedLoop-0124 | dPlacedRequest | ownership:99-100; project-map role shapes; Stage 0 K4 | C2-F5 |
| cl-dClosedLoop-0125 | dPlacedRequest | flow-steps [probe] incl. stand-ins; P31 | holds |
| cl-dClosedLoop-0126 | dPlacedRequest | P32; night pass point 3 | holds |
| cl-dClosedLoop-0127 | dPlacedRequest | memory-plan [pockets] and [chain] | holds |
| cl-dClosedLoop-0128 | dPlacedRequest | night-pass-two [p1] NT-2 | holds |
| cl-dClosedLoop-0129 | dPlacedRequest | night-pass-two [p3] item 6 | holds |
| cl-dClosedLoop-0130 | dPlacedRequest | night-pass-two [p4] NT-18; memory-plan registers | holds |
| cl-dClosedLoop-0131 | dPlacedRequest | memory-plan [pockets] change feed; night-pass-two [answers-folded] NT-14 | holds |
| cl-dClosedLoop-0132 | dPlacedRequest | stall-and-loop [design] 1 and [layers]; the design map's `record-kind.intake` row; flow-steps `entry.intake` | C2-F4 |
| cl-dClosedLoop-0133 | dPlacedRequest | cloud-and-scale [defects] and [design] 2; gap-conc-12 | holds |
| cl-dClosedLoop-0134 | dPlacedRequest | cloud-and-scale [design] 3; `leases.queued-claim-days`; gap-conc-13 | holds |
| cl-dClosedLoop-0135 | dPlacedRequest | cloud-and-scale [design] 4; `leases.expiry-hours`; gap-conc-14 | holds |
| cl-dClosedLoop-0136 | dPlacedRequest | cloud-and-scale [design] 15; gap-conc-18 | holds |
| cl-dClosedLoop-0137 | dPlacedRequest | cloud-and-scale [design] 10; gap-conc-17 | holds |
| cl-dClosedLoop-0138 | dPlacedRequest | cloud-and-scale [design] 9; `leases.offer-seconds`; gap-conc-19 | holds |
| cl-dClosedLoop-0139 | dKeptSession | v2 [presets] rules and table; flow-steps [consequences] | holds |
| cl-dClosedLoop-0140 | dKeptSession | presets table `hooks.bypass` | holds |
| cl-dClosedLoop-0141 | dKeptSession | v2 [presets] charter-render rule | holds |
| cl-dClosedLoop-0142 | dKeptSession | walk wave-1-2 dKeptSession; catalogue `preset` | holds |
| cl-dClosedLoop-0143 | dKeptSession | coordination [design] 6; night-pass-two NT-16; Stage 0 K3 | C2-F15 |
| cl-dClosedLoop-0144 | dKeptSession | coordination [design] 7; `deps.messaging` | holds |
| cl-dClosedLoop-0145 | dKeptSession | coordination [design] 8; P21; Stage 0 K4 | C2-F11 |
| cl-dClosedLoop-0146 | dKeptSession | catalogue `actions.free` | holds |
| cl-dClosedLoop-0147 | dKeptSession | catalogue `orient.budget`; Stage 0 K4 | C2-F11 |
| cl-dClosedLoop-0148 | dKeptSession | flow-steps [rules] item boundary; `mailbox.reads` | holds |
| cl-dClosedLoop-0149 | dKeptSession | catalogue `notify.owner` | holds |
| cl-dClosedLoop-0150 | dKeptSession | catalogue and presets `resume.context` (v2:1050, 1373); 0121 | C2-F12 |
| cl-dClosedLoop-0151 | dKeptSession | catalogue `card.pointers`; flow-steps [rules] | holds |
| cl-dClosedLoop-0152 | dKeptSession | catalogue `context.*` | holds |
| cl-dClosedLoop-0153 | dKeptSession | compaction CX checks; v2 [owed] | holds |
| cl-dClosedLoop-0154 | dKeptSession | design-map policy namespaces owned | holds |
| cl-dClosedLoop-0155 | dKeptSession | flow-steps [rules] and [breakpoint] attendance; P4 | holds |
| cl-dClosedLoop-0156 | dKeptSession | flow-steps [transitions] `repeat` row; `entry.place` | holds |
| cl-dClosedLoop-0157 | dKeptSession | Stage 0 K4 population; v2 [policies] | holds |
| cl-dClosedLoop-0158 | dKeptSession | night-pass-two [p1] NT-3 | holds |
| cl-dClosedLoop-0159 | dKeptSession | night-pass-two [p3] NT-17; catalogue `mailbox.notice` and `mailbox.fetch-seconds` | holds |
| cl-dClosedLoop-0160 | dKeptSession | night-pass-two [p4] messages | holds |
| cl-dClosedLoop-0161 | dKeptSession | night-pass-two [answers-folded] NT-14; memory-plan change feed | holds |
| cl-dClosedLoop-0162 | dKeptSession | coordination [design] 6; `flow.wait-ceiling`; stall-and-loop [chain] | holds |
| cl-dClosedLoop-0163 | dKeptSession | stall-and-loop [chain] dKeptSession | holds |
| cl-dClosedLoop-0164 | dKeptSession | cloud-and-scale [design] 5; gap-conc-15 | holds |
| cl-dClosedLoop-0165 | dKeptSession | cloud-and-scale [design] 10 and [chain] | holds |
| cl-dClosedLoop-0166 | dBoundRoles | layer-roles [roster], [settled]; gap-roles-01, -07, -14; v2 [owed] expansion roles | C3-F29 |
| cl-dClosedLoop-0167 | dBoundRoles | layer-roles [tags]; gap-roles-03; v2 P25 | holds |
| cl-dClosedLoop-0168 | dBoundRoles | layer-roles [settled] two blocks; night-pass-two [p4] contradiction 1; gap-roles-05, -08 | holds |
| cl-dClosedLoop-0169 | dBoundRoles | v2 P26; layer-roles [roster] cycle role; gap-roles-02, -05 | holds |
| cl-dClosedLoop-0170 | dBoundRoles | v2 P26; policies `roles.retries`; gap-roles-04 | holds |
| cl-dClosedLoop-0171 | dBoundRoles | gap-roles-06, gap-orient-07; tools/hooks/agent-cap.js | holds |
| cl-dClosedLoop-0172 | dBoundRoles | gap-roles-03; layer-roles [tags] | holds |
| cl-dClosedLoop-0173 | dBoundRoles | gap-orient-09; tools/hooks/scratch-guard.js | holds |
| cl-dClosedLoop-0174 | dBoundRoles | gap-orient-09; check_roles.py WRITES | holds |
| cl-dClosedLoop-0175 | dBoundRoles | policies `driver.reads`, `prompts.author`, `roles.no-spawn`; v2 P25 | holds |
| cl-dClosedLoop-0176 | dBoundRoles | v2 P18, [enforcement] P18; policies `run.on-owner-question`; stage0 K5 lead | C3-F1 |
| cl-dClosedLoop-0177 | dBoundRoles | policies `placement.check`; layer-roles [matrix] entry.place | holds |
| cl-dClosedLoop-0178 | dBoundRoles | v2 P29; layer-roles [trust] items 1–3; gap-roles-11 | holds |
| cl-dClosedLoop-0179 | dBoundRoles | layer-roles [tags]; systems tags owners | holds |
| cl-dClosedLoop-0180 | dBoundRoles | systems [agree-instruction-writing], [design-instruction] keys; policies `instructions.task-charter`; gap-roles-19, -20; check_roles.py:84 | C3-F2, C3-F3 |
| cl-dClosedLoop-0181 | dBoundRoles | systems [design-role-shapes]; night-pass-two [p7]; RS-2 answers; gap-roles-18 | holds |
| cl-dClosedLoop-0182 | dBoundRoles | memory-plan [sites], [gates], [chain]; gap-roles-23 | holds |
| cl-dClosedLoop-0183 | dBoundRoles | v2 P38; night-pass-two [p4] contradiction 2 | holds |
| cl-dClosedLoop-0184 | dBoundRoles | v2 P38; memory-plan [doors] upgrade-step door | holds |
| cl-dClosedLoop-0185 | dBoundRoles | gap-roles-24, -25; check_roles.py BODY_CEILINGS, WORKFLOW_NAMES; layer-roles [matrix] composition revision | holds |
| cl-dClosedLoop-0186 | dBoundRoles | policies `roles.effort.*`, `roles.model.<role>`; systems [design-role-shapes]; roles_lib.py:561 | holds |
| cl-dClosedLoop-0187 | dBoundRoles | systems kinds bullet (NT-8); `runtime.agents-in-flight` | holds |
| cl-dClosedLoop-0188 | dBoundRoles | night-pass-two [p2] items 4–5, [answers] NT-12; gap-roles-27; house/policy.toml | holds |
| cl-dClosedLoop-0189 | dBoundRoles | night-pass-two [p4] contradiction 11; gap-roles-28 | holds |
| cl-dClosedLoop-0190 | dBoundRoles | night-pass-two [p7] rule table; gap-roles-30 | holds |
| cl-dClosedLoop-0191 | dBoundRoles | stall-and-loop [design] item 7; v2 P39; gap-roles-31 | holds |
| cl-dClosedLoop-0192 | dFurnishedOrders | project-map [delivery]; gap-orient-15; v2 P29 recall | holds |
| cl-dClosedLoop-0193 | dFurnishedOrders | policies `prompts.batch` | holds |
| cl-dClosedLoop-0194 | dFurnishedOrders | policies `notices.record`; gap-roles-09 | holds |
| cl-dClosedLoop-0195 | dFurnishedOrders | night-pass-two [p6]; gap-mem-44 | holds |
| cl-dClosedLoop-0196 | dFurnishedOrders | layer-roles [trust] items 4–6; policies `roles.trust`, `roles.verifier-context`; gap-roles-10, -16 | holds |
| cl-dClosedLoop-0197 | dFurnishedOrders | layer-roles [trust] item 10; policies `roles.answered-calls`; gap-roles-13 | C3-F8 |
| cl-dClosedLoop-0198 | dFurnishedOrders | layer-roles [trust] item 7; policies `roles.on-contradiction`; gap-roles-17 | holds |
| cl-dClosedLoop-0199 | dFurnishedOrders | layer-roles [tags] pointers' source; gap-roles-10, -12; roles_lib.py:67, check_roles.py, render_agents.py | C3-F4 |
| cl-dClosedLoop-0200 | dFurnishedOrders | layer-roles [matrix]; gap-roles-15 | holds |
| cl-dClosedLoop-0201 | dFurnishedOrders | layer-roles [trust] item 11; layer-memory [contract] value ledger; 0459 | C3-F6 |
| cl-dClosedLoop-0202 | dFurnishedOrders | systems [cross] one budget per slot; policies `retrofit.slot-bytes`, `annotations.delivery`, `instructions.slices`, `roles.orientation.house-index`; dTotalRecall 0220 | C3-F5, C3-F7 |
| cl-dClosedLoop-0203 | dFurnishedOrders | project-map [tiers], [delivery], [keys]; policies `memory.map-unfold` | holds |
| cl-dClosedLoop-0204 | dFurnishedOrders | project-map [delivery] orientation scout row | holds |
| cl-dClosedLoop-0205 | dFurnishedOrders | v2 RC-7; layer-roles [trust] items 7, 10 | holds |
| cl-dClosedLoop-0206 | dFurnishedOrders | gap-roles-21; layer-memory probe kind (dPlacedRequest) | holds |
| cl-dClosedLoop-0207 | dFurnishedOrders | night-pass [p1-unattended] item 2; v2 P4 | holds |
| cl-dClosedLoop-0208 | dFurnishedOrders | project-map [placement]; policies `memory.code-budget`, `memory.code-roles`; v2 P32; gap-roles-22 | holds |
| cl-dClosedLoop-0209 | dFurnishedOrders | systems annotations delivery; NP-13 | holds |
| cl-dClosedLoop-0210 | dFurnishedOrders | night-pass-two [p4] contract; gap-roles-29 | holds |
| cl-dClosedLoop-0211 | dFurnishedOrders | night-pass-two [p4] problems; memory-plan refs: problems; gap-conc-10 | holds |
| cl-dClosedLoop-0212 | dTotalRecall | v2 P16, P30; layer-memory [contract]; gap-mem-01 | holds |
| cl-dClosedLoop-0213 | dTotalRecall | v2 P30; memory-plan [doors] | holds |
| cl-dClosedLoop-0214 | dTotalRecall | gap-mem-13; policies `leases.offline`; gen_build_index.py check_slug_claimed | holds |
| cl-dClosedLoop-0215 | dTotalRecall | layer-memory [build]; policies `builds.agent-root`; gap-mem-05, -40 | holds |
| cl-dClosedLoop-0216 | dTotalRecall | layer-memory [names]; policies `builds.slug-*`; gap-mem-06 | C3-F10 |
| cl-dClosedLoop-0217 | dTotalRecall | layer-memory [relations]; gap-mem-07; v2 P30 | C3-F9 |
| cl-dClosedLoop-0218 | dTotalRecall | layer-memory [asks]; policies `asks.acceptance` | holds |
| cl-dClosedLoop-0219 | dTotalRecall | layer-memory [map]; v2 [owed] re-timing; v2 P32; gap-mem-04, -28 | C3-F11 |
| cl-dClosedLoop-0220 | dTotalRecall | systems [design-memory-structure]; policies `memory.*`; gap-mem-20, -21 | C3-F16 |
| cl-dClosedLoop-0221 | dTotalRecall | systems [design-memory-structure] repeated heading (M35) | holds |
| cl-dClosedLoop-0222 | dTotalRecall | systems [design-role-shapes] metric; layer-memory [contract] shape-run; flow-steps review.cost | holds |
| cl-dClosedLoop-0223 | dTotalRecall | systems [design-memory-structure] acceptance re-measure | C3-F12 |
| cl-dClosedLoop-0224 | dTotalRecall | lexicon [integration]; LX-2 | holds |
| cl-dClosedLoop-0225 | dTotalRecall | project-map [placement], [fit], [keys]; gap-mem-26, -30, gap-design-01 | holds |
| cl-dClosedLoop-0226 | dTotalRecall | project-map [checks], [owners] | holds |
| cl-dClosedLoop-0227 | dTotalRecall | project-map [purpose], PM-5; gap-mem-27 | holds |
| cl-dClosedLoop-0228 | dTotalRecall | project-map [test] | C3-F13 |
| cl-dClosedLoop-0229 | dTotalRecall | memory-plan [pockets], [integration]; gap-mem-37, -38 | holds |
| cl-dClosedLoop-0230 | dTotalRecall | memory-plan [doors], [sites], [migration], [gates]; v2 P34, P35; gap-mem-36 | holds |
| cl-dClosedLoop-0231 | dTotalRecall | memory-plan [integration] distribution row, [migration]; v2 P38 | C3-F14 |
| cl-dClosedLoop-0232 | dTotalRecall | night-pass-two [p3] item 2; systems [cross]; gap-mem-41 | holds |
| cl-dClosedLoop-0233 | dTotalRecall | night-pass-two [p3] item 3; gap-mem-42 | holds |
| cl-dClosedLoop-0234 | dTotalRecall | night-pass-two [p3] item 2; gap-mem-43 | holds |
| cl-dClosedLoop-0235 | dTotalRecall | memory-plan [pockets] change feed; night-pass-two [answers-folded] NT-14 | holds |
| cl-dClosedLoop-0236 | dTotalRecall | layer-memory [contract] stream plan; whole-audit [readings] CL-3 | holds |
| cl-dClosedLoop-0237 | dTotalRecall | final-questions [atlas], FQ-8; policies `help.atlas`; v2 P42; gap-mem-48 | holds |
| cl-dClosedLoop-0238 | dLinkedLibrary | layer-memory [decisions]; gap-mem-02 | holds |
| cl-dClosedLoop-0239 | dLinkedLibrary | layer-memory [reuse]; night-pass-two [p2] item 7; research-scoutedseam-apply; gap-mem-03 | C3-F17 |
| cl-dClosedLoop-0240 | dLinkedLibrary | layer-memory [reuse] readers by value; check-memory-hygiene.sh:2474; unattended kit.toml:174; gap-mem-09 | C3-F18 |
| cl-dClosedLoop-0241 | dLinkedLibrary | layer-memory [annotations]; policies `annotations.grammar`; gap-mem-08, -17, -32 | C3-F19 |
| cl-dClosedLoop-0242 | dLinkedLibrary | dTotalRecall 0215, 0217; memory-plan [practice] one owner | C3-F20 |
| cl-dClosedLoop-0243 | dLinkedLibrary | layer-library [research-view]; gap-mem-15 | holds |
| cl-dClosedLoop-0244 | dLinkedLibrary | systems [design-annotations] budget, checks, keys; AN-1, AN-2; gap-mem-18, -19 | C3-F21, C3-F22 |
| cl-dClosedLoop-0245 | dLinkedLibrary | flow-steps [adopt]; policies `retrofit.*`; gap-mem-24, -25 | holds |
| cl-dClosedLoop-0246 | dLinkedLibrary | retrofit record origin; gap-mem-25 | holds |
| cl-dClosedLoop-0247 | dLinkedLibrary | gap-mem-24 | holds |
| cl-dClosedLoop-0248 | dLinkedLibrary | systems [cross] retrofit ledger populations | holds |
| cl-dClosedLoop-0249 | dLinkedLibrary | systems marker registration | holds |
| cl-dClosedLoop-0250 | dLinkedLibrary | gap-mem-15 (72 at `1b759b620`); layer-memory [contract] research return | holds |
| cl-dClosedLoop-0251 | dLinkedLibrary | v2 P32; project-map [placement] counted code line | holds |
| cl-dClosedLoop-0252 | dLinkedLibrary | policies `memory.code-enrich`; v2 P32; gap-mem-29 | holds |
| cl-dClosedLoop-0253 | dLinkedLibrary | project-map [test]; dTotalRecall 0228 | holds |
| cl-dClosedLoop-0254 | dLinkedLibrary | v2 [owed] span re-measure; v2 P33; gap-mem-31 | C3-F31 |
| cl-dClosedLoop-0255 | dLinkedLibrary | gap-mem-33; check_roles.py and render_playbook.py REGION constants | holds |
| cl-dClosedLoop-0256 | dLinkedLibrary | NP-16; memory-plan [pockets] dossiers | holds |
| cl-dClosedLoop-0257 | dLinkedLibrary | NP-13; memory-plan [cycle] | holds |
| cl-dClosedLoop-0258 | dLinkedLibrary | policies `memory.code-languages`; NP-10; gap-mem-34 | holds |
| cl-dClosedLoop-0259 | dLinkedLibrary | memory-plan [cycle], [migration]; v2 P37; gap-mem-39, gap-tool-17 | holds |
| cl-dClosedLoop-0260 | dLinkedLibrary | policies `instructions.legacy`; IA-5; gap-deploy-26 | holds |
| cl-dClosedLoop-0261 | dLinkedLibrary | night-pass-two [p6] items 3–4; gap-mem-45 | holds |
| cl-dClosedLoop-0262 | dMindYourWords | lexicon [classes]; policies `lexicon.pin`; lexicon.py:121; gap-mem-10 | C3-F27 |
| cl-dClosedLoop-0263 | dMindYourWords | lexicon [forced] item 1, L-1; policies `lexicon.forced`; gap-lex-01 | C3-F24 |
| cl-dClosedLoop-0264 | dMindYourWords | lexicon [forced] item 2, LX-3 | holds |
| cl-dClosedLoop-0265 | dMindYourWords | lexicon [forced] item 3 | holds |
| cl-dClosedLoop-0266 | dMindYourWords | lexicon [forced] item 4; gap-lex-06 | holds |
| cl-dClosedLoop-0267 | dMindYourWords | lexicon [forced] `--suggest`; gap-lex-02 | holds |
| cl-dClosedLoop-0268 | dMindYourWords | lexicon [packs]; v2 [owed] adopter census | holds |
| cl-dClosedLoop-0269 | dMindYourWords | lexicon [packs] selection, L-5; layer-memory [contract] lexicon declaration; stage0 K3 lead | C3-F30 |
| cl-dClosedLoop-0270 | dMindYourWords | lexicon [enforcement] items 1–3; policies `lexicon.at-commit`; gap-lex-03 | holds |
| cl-dClosedLoop-0271 | dMindYourWords | lexicon [drift], debt-fold `nouns-table`, L-3; gap-lex-05 | C3-F25 |
| cl-dClosedLoop-0272 | dMindYourWords | lexicon [vocabulary], debt-fold `ratified-readers`; tools/lexicon and drift-audit readers of `ratified`; gap-lex-06 | C3-F26 |
| cl-dClosedLoop-0273 | dMindYourWords | lexicon [integration], LX-2; dTotalRecall 0224 | holds |
| cl-dClosedLoop-0274 | dMindYourWords | lexicon [integration] tag vocabulary; gap-lex-10 | holds |
| cl-dClosedLoop-0275 | dMindYourWords | lexicon [fixes]; gap-lex-07 | holds |
| cl-dClosedLoop-0276 | dMindYourWords | lexicon [classes] out of scope, [fixes]; gap-lex-04 | holds |
| cl-dClosedLoop-0277 | dMindYourWords | lexicon [enforcement] item 6; gap-lex-08 | holds |
| cl-dClosedLoop-0278 | dMindYourWords | gap-lex-09 | holds |
| cl-dClosedLoop-0279 | dWellOiledMachine | layer-runtime [tests] spike, [spawn]; catalogue runtime.spawn-backend; stall-and-loop [owed] | C4-F8 |
| cl-dClosedLoop-0280 | dWellOiledMachine | layer-runtime [build] unit 2; v2 [owed] `next` row; gap-found-06 | holds |
| cl-dClosedLoop-0281 | dWellOiledMachine | flow-steps [lifecycle]; night-pass [p1]; catalogue attendance.scope; cloud-and-scale [design] 3 | holds |
| cl-dClosedLoop-0282 | dWellOiledMachine | flow-steps [entry] entry.intake; layer-roles hook row; gap-rt-14 | C4-F4 |
| cl-dClosedLoop-0283 | dWellOiledMachine | research-harness-cli dWellOiledMachine row (DA-M14); layer-runtime [harness] | holds |
| cl-dClosedLoop-0284 | dWellOiledMachine | layer-runtime [supervise], [build] unit 3; fates rows 145-146; catalogue runtime.relaunch | C4-F1, C4-F7, C4-F8 |
| cl-dClosedLoop-0285 | dWellOiledMachine | layer-runtime [act] binding, [enforce] | holds |
| cl-dClosedLoop-0286 | dWellOiledMachine | layer-runtime [spawn] returns and deferral | holds |
| cl-dClosedLoop-0287 | dWellOiledMachine | layer-runtime [supervise] agents in flight; catalogue runtime.agents-in-flight | holds |
| cl-dClosedLoop-0288 | dWellOiledMachine | layer-runtime [enforce], [invariants] fail-closed; catalogue runtime.hook-failure, runtime.attended-allowance; Stage 0 K4 | C4-F8 |
| cl-dClosedLoop-0289 | dWellOiledMachine | layer-runtime [isolate]; catalogue build.worktree; gap-conc-03 | holds |
| cl-dClosedLoop-0290 | dWellOiledMachine | layer-runtime [sessions], [build] unit 9; night-pass [p5]; gap-orient-12/14 | C4-F3 |
| cl-dClosedLoop-0291 | dWellOiledMachine | layer-runtime [schedule] | holds |
| cl-dClosedLoop-0292 | dWellOiledMachine | layer-runtime [harness]; gap-rt-19 | holds |
| cl-dClosedLoop-0293 | dWellOiledMachine | catalogue leases.expiry-hours; cloud-and-scale [design] 4; layer-runtime [harness] | C4-F7 |
| cl-dClosedLoop-0294 | dWellOiledMachine | layer-runtime [schedule] retention; catalogue runtime.journal; gap-rt-16 | holds |
| cl-dClosedLoop-0295 | dWellOiledMachine | layer-runtime [extend] grant and secret scan; catalogue runtime.secret-scan | C4-F8 |
| cl-dClosedLoop-0296 | dWellOiledMachine | layer-runtime [schedule], [supervise]; catalogue build.release-ceiling; flow-steps [deploy] owners; Stage 0 K2 | C4-F13 |
| cl-dClosedLoop-0297 | dWellOiledMachine | v2 system.role-shapes; layer-runtime [act] | holds |
| cl-dClosedLoop-0298 | dWellOiledMachine | v2 system.tags; gap-rt-13 | holds |
| cl-dClosedLoop-0299 | dWellOiledMachine | gap-rt-13, gap-rt-20 | holds |
| cl-dClosedLoop-0300 | dWellOiledMachine | gap-rt-13; v2 system.tags | holds |
| cl-dClosedLoop-0301 | dWellOiledMachine | night-pass [p5]; night-pass-two [p5-caps]; v2 [owed] map headroom; catalogue memory.default-load | C4-F3 |
| cl-dClosedLoop-0302 | dWellOiledMachine | v2 system.project-map; gap-orient-18 | holds |
| cl-dClosedLoop-0303 | dWellOiledMachine | night-pass [p1] item 3; v2 [owed] spike row; P25 | holds |
| cl-dClosedLoop-0304 | dWellOiledMachine | night-pass [p1] item 4; P4; gap-orient-16 | holds |
| cl-dClosedLoop-0305 | dWellOiledMachine | night-pass [p1] item 5; gap-orient-17 | holds |
| cl-dClosedLoop-0306 | dWellOiledMachine | layer-runtime [supervise]; fates rows 145-146; night-pass [p1]; tools/unattended/README.md:211 | C4-F1 |
| cl-dClosedLoop-0307 | dWellOiledMachine | night-pass [p2] item 7; gap-rt-23 | holds |
| cl-dClosedLoop-0308 | dWellOiledMachine | night-pass [p2] item 6 | holds |
| cl-dClosedLoop-0309 | dWellOiledMachine | gap-rt-24; stall-and-loop [design] 7 | holds |
| cl-dClosedLoop-0310 | dWellOiledMachine | away-pass AP-8 fold; catalogue trace.identity, trace.cost; P35, P36 | holds |
| cl-dClosedLoop-0311 | dWellOiledMachine | catalogue commits.edge-check, trace.identity; presets (strict commit-msg); away-pass AP-6, SA-4 | holds |
| cl-dClosedLoop-0312 | dWellOiledMachine | P35; catalogue trace.rows; gap-rt-25, gap-rt-27; tools/runlog/model.py:1558 | holds |
| cl-dClosedLoop-0313 | dWellOiledMachine | P33, P36; gap-orient-19 | holds |
| cl-dClosedLoop-0314 | dWellOiledMachine | P36, P37; away-pass AP-16; gap-rt-31, gap-rt-32, gap-tool-14, gap-tool-18 | holds |
| cl-dClosedLoop-0315 | dWellOiledMachine | catalogue runtime.act-auth; away-pass AP-14 fold; gap-rt-28, gap-rt-30, gap-tool-16 | holds |
| cl-dClosedLoop-0316 | dWellOiledMachine | memory-plan [pockets] row 107; code readers of `orientation/` | C4-F11 |
| cl-dClosedLoop-0317 | dWellOiledMachine | shape-reviews-compared SA-10; memory-plan refs row | holds |
| cl-dClosedLoop-0318 | dWellOiledMachine | night-pass-two [p4], NT-19; catalogue build.push; .githooks/pre-push:1163 | holds |
| cl-dClosedLoop-0319 | dWellOiledMachine | night-pass-two [p4], NT-20; catalogue build.unit-holders | holds |
| cl-dClosedLoop-0320 | dWellOiledMachine | night-pass-two [p4] contradiction 2, NT-21; `gov-session` readers by grep | holds |
| cl-dClosedLoop-0321 | dWellOiledMachine | night-pass-two [p7]; layer-runtime [supervise], [tests] in-flight; research-agent-cap fallback | holds |
| cl-dClosedLoop-0322 | dWellOiledMachine | catalogue memory.mirror; night-pass-two NT-14 fold; layer-runtime [extend] | holds |
| cl-dClosedLoop-0323 | dWellOiledMachine | night-pass-two NT-28 and answers' review; layer-runtime [supervise], [tests] in-flight | holds |
| cl-dClosedLoop-0324 | dWellOiledMachine | stall-and-loop [design] 5, [owed]; catalogue runtime.no-progress, leases.renewal, leases.expiry-hours; layer-runtime [tests] renewal | C4-F6, C4-F7 |
| cl-dClosedLoop-0325 | dWellOiledMachine | stall-and-loop [design] 6; catalogue runtime.hold-ceiling; layer-runtime [supervise], [tests] limits, act-ceiling | C4-F5 |
| cl-dClosedLoop-0326 | dWellOiledMachine | stall-and-loop [design] 6, 10, SL-4 to SL-6; catalogue run.*, notify.owner-items | holds |
| cl-dClosedLoop-0327 | dWellOiledMachine | stall-and-loop [design] 7; catalogue runtime.refusal-repeats | holds |
| cl-dClosedLoop-0328 | dWellOiledMachine | stall-and-loop [design] 9; catalogue deps.on-parent-withdrawn | holds |
| cl-dClosedLoop-0329 | dWellOiledMachine | catalogue build.spend-cap; SL-8 | holds |
| cl-dClosedLoop-0330 | dWellOiledMachine | cloud-and-scale [design] 6, [fleet] | holds |
| cl-dClosedLoop-0331 | dWellOiledMachine | cloud-and-scale [design] 7, [fleet]; catalogue runtime.admission-scope | holds |
| cl-dClosedLoop-0332 | dWellOiledMachine | cloud-and-scale [design] 8, 18; gap-conc-16 | holds |
| cl-dClosedLoop-0333 | dWellOiledMachine | cloud-and-scale [design] 11; catalogue deps.messaging | holds |
| cl-dClosedLoop-0334 | dWellOiledMachine | cloud-and-scale [design] 12; catalogue roles.harness/auth.<role> | holds |
| cl-dClosedLoop-0335 | dWellOiledMachine | cloud-and-scale [design] 10, 13; gap-rt-44 | holds |
| cl-dClosedLoop-0336 | dWellOiledMachine | cloud-and-scale [design] 14; gap-rt-45 | holds |
| cl-dClosedLoop-0337 | dWellOiledMachine | cloud-and-scale [design] 2; layer-runtime [supervise] fencing; flow-steps [deploy] owners | C4-F13 |
| cl-dClosedLoop-0338 | dWellOiledMachine | cloud-and-scale [design] 18, [fleet]; gap-rt-46 | holds |
| cl-dClosedLoop-0339 | dWitnessedBar | gap-test-01; flow-steps [test] | holds |
| cl-dClosedLoop-0340 | dWitnessedBar | layer-runtime [enforce] bypasses; gap-test-09 | holds |
| cl-dClosedLoop-0341 | dWitnessedBar | flow-steps test.route; catalogue verdict.blocks | holds |
| cl-dClosedLoop-0342 | dWitnessedBar | flow-steps test.verdict; P3; catalogue verdict; gap-test-02 | C4-F9 |
| cl-dClosedLoop-0343 | dWitnessedBar | flow-steps [test] held legs; catalogue verdict.held | holds |
| cl-dClosedLoop-0344 | dWitnessedBar | P3; layer-expansions remote verdict; catalogue verdict.remote.*; gap-test-11 to gap-test-13; Stage 0 K4 | C4-F9 |
| cl-dClosedLoop-0345 | dWitnessedBar | gap-test-06, gap-test-10; night-pass [p2] seen-red choice | holds |
| cl-dClosedLoop-0346 | dWitnessedBar | flow-steps test.route, test.flakes, the "Where a flake is seen" note; gap-test-04 | C4-F10 |
| cl-dClosedLoop-0347 | dWitnessedBar | gap-test-03; catalogue tests.product; Stage 0 K4 | C4-F9 |
| cl-dClosedLoop-0348 | dWitnessedBar | gap-test-07, gap-test-08 | holds |
| cl-dClosedLoop-0349 | dWitnessedBar | gap-tool-01; P16 | holds |
| cl-dClosedLoop-0350 | dWitnessedBar | systems record (leg name the join key); retrofit [owners] pack namespace | holds |
| cl-dClosedLoop-0351 | dWitnessedBar | retrofit [ledger]; v2 dOrderedCharter row (H5); tools/memory-tree/merge-rows.*; map_lib.py:1404,1502 | holds |
| cl-dClosedLoop-0352 | dWitnessedBar | retrofit [ratchet]; catalogue retrofit.widen | C4-F9 |
| cl-dClosedLoop-0353 | dWitnessedBar | retrofit [seed]; catalogue retrofit.unseeded | holds |
| cl-dClosedLoop-0354 | dWitnessedBar | retrofit [ledger] directions 17/2/7/1, RF-5; gap-test-14, gap-test-15 | holds |
| cl-dClosedLoop-0355 | dWitnessedBar | retrofit [ledger] pins, [owners] | holds |
| cl-dClosedLoop-0356 | dWitnessedBar | retrofit [owners]; v2 dOrderedCharter and dSafePassage rows | holds |
| cl-dClosedLoop-0357 | dWitnessedBar | tools/gate-legs.json (140 legs, no purpose field); PM-5 | holds |
| cl-dClosedLoop-0358 | dWitnessedBar | v2 dGroundRules row; retrofit [ledger] | holds |
| cl-dClosedLoop-0359 | dWitnessedBar | flow-steps [test] "A fix pass keeps its check"; gap-test-19 | holds |
| cl-dClosedLoop-0360 | dWitnessedBar | night-pass [p4]; P33 | holds |
| cl-dClosedLoop-0361 | dWitnessedBar | flow-steps [test] WK-1 note; test.attribute and test.reason rows | holds |
| cl-dClosedLoop-0362 | dWitnessedBar | P37; research-compatibility §4; away-pass [p4]; tools/gate-legs.json argv | C4-F12 |
| cl-dClosedLoop-0363 | dWitnessedBar | catalogue trace.leg-output; P35; gap-test-20 | holds |
| cl-dClosedLoop-0364 | dWitnessedBar | away-pass AP-33 fold and [p4] platform matrix; gap-tool-20; govkit.py:1138; profile_bar.py:282 | C4-F2 |
| cl-dClosedLoop-0365 | dWitnessedBar | away-pass AP-33; research-python-floor §1 | holds |
| cl-dClosedLoop-0366 | dWitnessedBar | flow-roles-adoption [design] 9 to 14, [chain]; catalogue instructions.exclude; gap-test-21 | holds |
| cl-dClosedLoop-0367 | dWitnessedBar | night-pass-two [p5] item 4, NT-23; gap-test-22 | holds |
| cl-dClosedLoop-0368 | dWitnessedBar | catalogue verdict.flakes, flow.wait-ceiling; stall-and-loop [folded]; flow-steps test.route, test.select | holds |
| cl-dClosedLoop-0369 | dRankedPlan | gap-plan-01; flow-steps [plan] `plan.place` | holds |
| cl-dClosedLoop-0370 | dRankedPlan | v2 [policies] plan.*; ownership.md key rows; cl-0166 roster | C5-F19 |
| cl-dClosedLoop-0371 | dRankedPlan | gap-plan-02, gap-plan-06; flow-steps `plan.triage-rule`; v2 `plan.triage` | C5-F19 |
| cl-dClosedLoop-0372 | dRankedPlan | gap-plan-05; v2 `maintain.fixes` | holds |
| cl-dClosedLoop-0373 | dRankedPlan | v2 [chain] live-build note | holds |
| cl-dClosedLoop-0374 | dRankedPlan | gap-plan-04, gap-review-01; flow-steps [plan] breakpoints; cl-0458 | C5-F14 |
| cl-dClosedLoop-0375 | dRankedPlan | gap-plan-07; v2 `plan.kickoff` | C5-F19 |
| cl-dClosedLoop-0376 | dRankedPlan | v2 `kickoff.runs`; fates skills rows; cl-0490 | holds |
| cl-dClosedLoop-0377 | dRankedPlan | flow-steps [entry] `entry.intake`; recut H2 and RC-9; cl-0282, cl-0283 | holds |
| cl-dClosedLoop-0378 | dRankedPlan | audit-fold H1; recut tolerance row; cl-0123; cl-0283 | holds |
| cl-dClosedLoop-0379 | dRankedPlan | v2 `memory.item-budget`; walk [wave-2] | holds |
| cl-dClosedLoop-0380 | dRankedPlan | night-pass point 2; flow-steps `plan.record` | holds |
| cl-dClosedLoop-0381 | dRankedPlan | gap-plan-08; night-pass point 6 | holds |
| cl-dClosedLoop-0382 | dRankedPlan | gap-flow-03, gap-flow-04; gap-register split rule; ownership-population P15 | C5-F13 |
| cl-dClosedLoop-0383 | dIndexedDesign | gap-design-04; flow-steps `design.ready`; v2 `design.handoff` | C5-F16 |
| cl-dClosedLoop-0384 | dIndexedDesign | gap-design-02; flow-steps `design.overlaps`; v2 `design.overlap` | C5-F16 |
| cl-dClosedLoop-0385 | dIndexedDesign | gap-design-03; audit-fold [af-1]; flow-steps [design] breakpoints | holds |
| cl-dClosedLoop-0386 | dIndexedDesign | gap-design-05, gap-design-06 | holds |
| cl-dClosedLoop-0387 | dIndexedDesign | gap-design-07; walk WK-2 | holds |
| cl-dClosedLoop-0388 | dIndexedDesign | gap-design-09 | holds |
| cl-dClosedLoop-0389 | dIndexedDesign | P12; [enforcement] | holds |
| cl-dClosedLoop-0390 | dIndexedDesign | gap-flow-01; P17, P18; v2 `design.reentry`, `design.forks` | holds |
| cl-dClosedLoop-0391 | dIndexedDesign | gap-design-10; P12 | holds |
| cl-dClosedLoop-0392 | dIndexedDesign | gap-flow-17; fates unattended row; gate-legs.json "playbook validity gate" | C5-F4 |
| cl-dClosedLoop-0393 | dIndexedDesign | Stage 0's leads K3 playbook-set; dWitnessedBar ancestry | holds |
| cl-dClosedLoop-0394 | dIndexedDesign | night-pass point 4; P12 | holds |
| cl-dClosedLoop-0395 | dIndexedDesign | gap-design-11; night-pass-two [p2] item 2; scoutedseam-apply §5c | holds |
| cl-dClosedLoop-0396 | dIndexedDesign | night-pass-two NT-26 | holds |
| cl-dClosedLoop-0397 | dIndexedDesign | gap-design-12; v2 `design.streams`; flow-steps `design.streams`; parked-debt values-no-arm; Stage 0's leads K1 | C5-F23 |
| cl-dClosedLoop-0398 | dIndexedDesign | final-questions [gaps], [folded]; v2 `design.coverage*`; gap-register rule | C5-F15 |
| cl-dClosedLoop-0399 | dScopedBuild | gap-spine-03; flow-steps [build] exits | holds |
| cl-dClosedLoop-0400 | dScopedBuild | P19; gap-flow-05; v2 `review.findings` (dDeclaredLoop) | holds |
| cl-dClosedLoop-0401 | dScopedBuild | gap-build-01; flow-steps `build.scope` | holds |
| cl-dClosedLoop-0402 | dScopedBuild | gap-build-02; v2 `review.build.when` | C5-F18 |
| cl-dClosedLoop-0403 | dScopedBuild | gap-build-03; cl-0172 | holds |
| cl-dClosedLoop-0404 | dScopedBuild | gap-build-04; night-pass-two NT-24; checklist-unowned fold | holds |
| cl-dClosedLoop-0405 | dScopedBuild | flow-steps `build.core` | holds |
| cl-dClosedLoop-0406 | dScopedBuild | gap-build-05; retrofit [drain]; v2 [presets] line 1571 | C5-F5 |
| cl-dClosedLoop-0407 | dScopedBuild | retrofit [drain]; recut H5; cl-0049; map_lib.py:1373 | holds |
| cl-dClosedLoop-0408 | dScopedBuild | P31; night-pass point 2 | holds |
| cl-dClosedLoop-0409 | dScopedBuild | fates playbook-mode row; gap-flow-17 | holds |
| cl-dClosedLoop-0410 | dScopedBuild | gap-build-06; flow-steps `build.reuse-check`; v2 `flow.rework-budget` | C5-F17 |
| cl-dClosedLoop-0411 | dScopedBuild | gap-flow-22; scoutedseam-apply §6 rank 2 | holds |
| cl-dClosedLoop-0412 | dScopedBuild | final-questions [gaps]; v2 `deviation.gate`; gap-register rule | C5-F15 |
| cl-dClosedLoop-0413 | dShippedRelease | flow-steps `deploy.record` | holds |
| cl-dClosedLoop-0414 | dShippedRelease | final-questions [help]; research-final-help #18 | C5-F12 |
| cl-dClosedLoop-0415 | dShippedRelease | flow-steps `deploy.unlease`; P40; parked-debt release-deletes-lease | holds |
| cl-dClosedLoop-0416 | dShippedRelease | walk WK-8 | holds |
| cl-dClosedLoop-0417 | dShippedRelease | gap-deploy-04; layer-expansions `kits.currency`; v2 `kits.*` | C5-F11 |
| cl-dClosedLoop-0418 | dShippedRelease | gap-deploy-03 | holds |
| cl-dClosedLoop-0419 | dShippedRelease | gap-deploy-08; final-questions [help]; cl-0489 | C5-F12 |
| cl-dClosedLoop-0420 | dShippedRelease | gap-tool-07; foundations K3 | holds |
| cl-dClosedLoop-0421 | dShippedRelease | P21; flow-steps `deploy.parents`; v2 `deps.landing` | holds |
| cl-dClosedLoop-0422 | dShippedRelease | P21; gap-flow-08; v2 `landing.order`; stall-and-loop [layers] | C5-F11 |
| cl-dClosedLoop-0423 | dShippedRelease | foundations K1; layer-flow [settled]; flow-steps `deploy.core` | C5-F3 |
| cl-dClosedLoop-0424 | dShippedRelease | gap-deploy-06; layer-flow [settled]; cl-0458 | C5-F14 |
| cl-dClosedLoop-0425 | dShippedRelease | gap-deploy-01; flow-steps [deploy] extension points | holds |
| cl-dClosedLoop-0426 | dShippedRelease | gap-deploy-13; layer-expansions distribution | holds |
| cl-dClosedLoop-0427 | dShippedRelease | gap-deploy-27; retrofit [owners]; adopter-instructions | holds |
| cl-dClosedLoop-0428 | dShippedRelease | P8; folds-reviews self-update-unplaced | holds |
| cl-dClosedLoop-0429 | dShippedRelease | retrofit [practices] CI row | holds |
| cl-dClosedLoop-0430 | dShippedRelease | cl-0427; cl-0426 | C5-F20 |
| cl-dClosedLoop-0431 | dShippedRelease | audit-fold M16; FM10; code consumers of `*/kit.toml` | holds |
| cl-dClosedLoop-0432 | dShippedRelease | v2 `integrations.tracker` | holds |
| cl-dClosedLoop-0433 | dShippedRelease | cl-0166; recut decided rows | holds |
| cl-dClosedLoop-0434 | dShippedRelease | gap-deploy-14; v2 `install.guards` | holds |
| cl-dClosedLoop-0435 | dShippedRelease | gap-deploy-12; layer-expansions receipt row, `install.from`; cl-0020; govkit.py:49, 8020 | C5-F1 |
| cl-dClosedLoop-0436 | dShippedRelease | gap-tool-11; v2 `platforms.*`; run-held-wsl.sh exists | holds |
| cl-dClosedLoop-0437 | dShippedRelease | gap-deploy-21, 22, 23; v2 `commits.squash`; memory-plan | C5-F11 |
| cl-dClosedLoop-0438 | dShippedRelease | flow-adoption FA-1; effort-default-homeless fold | holds |
| cl-dClosedLoop-0439 | dShippedRelease | gap-deploy-28; widening-unchecked fold | holds |
| cl-dClosedLoop-0440 | dShippedRelease | stall-and-loop [chain]; flow-steps `deploy.released`; keep-waiting fold | holds |
| cl-dClosedLoop-0441 | dShippedRelease | gap-deploy-29; cloud-and-scale | holds |
| cl-dClosedLoop-0442 | dTendedCadence | P6; layer-expansions Maintain | holds |
| cl-dClosedLoop-0443 | dTendedCadence | gap-maint-01; v2 `maintain.host`, `maintain.cadence`, `maintain.events` | C5-F9 |
| cl-dClosedLoop-0444 | dTendedCadence | v2 `maintain.fixes`; P6 | holds |
| cl-dClosedLoop-0445 | dTendedCadence | gap-maint-02, 09, 10, 11; layer-expansions admission rule | C5-F9, C5-F10 |
| cl-dClosedLoop-0446 | dTendedCadence | gap-maint-06 | holds |
| cl-dClosedLoop-0447 | dTendedCadence | v2 `maintain.record-when`, `observability.run-record`; gap-maint-14 | C5-F9 |
| cl-dClosedLoop-0448 | dTendedCadence | gap-orient-10; fates check-dead-paths row; tools/check-dead-paths.sh:2; layer-expansions line rule | C5-F2 |
| cl-dClosedLoop-0449 | dTendedCadence | layer-expansions Loop Review owners; map record-kind.loop-review | C5-F8 |
| cl-dClosedLoop-0450 | dTendedCadence | retrofit [cadence], [never]; v2 `retrofit.cadence` | holds |
| cl-dClosedLoop-0451 | dTendedCadence | cl-0166; recut | holds |
| cl-dClosedLoop-0452 | dTendedCadence | flow-steps [entry] repeat; cl-0305 | holds |
| cl-dClosedLoop-0453 | dTendedCadence | night-pass point 4 | holds |
| cl-dClosedLoop-0454 | dTendedCadence | gap-maint-12; v2 `maintain.security-review` | holds |
| cl-dClosedLoop-0455 | dTendedCadence | gap-maint-13; v2 `maintain.tiers` | holds |
| cl-dClosedLoop-0456 | dTendedCadence | P35; shape-reviews legacy-populations | holds |
| cl-dClosedLoop-0457 | dTendedCadence | gap-maint-15; v2 `maintain.interpreter-eol` | holds |
| cl-dClosedLoop-0458 | dCalibratedLens | gap-review-01; audit-fold [af-1]; v2 `review.<stage>.effort` | C5-F14 |
| cl-dClosedLoop-0459 | dCalibratedLens | P9; layer-expansions `loop.price` | holds |
| cl-dClosedLoop-0460 | dCalibratedLens | gap-review-02; v2 `review.loop.cadence`; layer-expansions ISO week | C5-F7 |
| cl-dClosedLoop-0461 | dCalibratedLens | P9; v2 `budgets.*`; layer-expansions `loop.propose` | C5-F6, C5-F7 |
| cl-dClosedLoop-0462 | dCalibratedLens | gap-found-16; P11 | holds |
| cl-dClosedLoop-0463 | dCalibratedLens | v2 `memory.item-budget` | holds |
| cl-dClosedLoop-0464 | dCalibratedLens | gap-review-11; audit-fold `review.cost` | holds |
| cl-dClosedLoop-0465 | dCalibratedLens | project-map losing test (15 points, 38 findings); cl-0228 | holds |
| cl-dClosedLoop-0466 | dCalibratedLens | night-pass points 2 and 5 | holds |
| cl-dClosedLoop-0467 | dCalibratedLens | gap-review-14; shape-reviews replay-scorers | holds |
| cl-dClosedLoop-0468 | dCalibratedLens | gap-review-15, gap-review-16 | holds |
| cl-dClosedLoop-0469 | dCalibratedLens | P35; away-pass point 5 | holds |
| cl-dClosedLoop-0470 | dCalibratedLens | gap-review-17; flow-adoption folds fixed-set, joins, policy-names | holds |
| cl-dClosedLoop-0471 | dCalibratedLens | gap-review-18; v2 `flow.promote`; decline-unrecorded fold | holds |
| cl-dClosedLoop-0472 | dCalibratedLens | gap-review-19; P9 | holds |
| cl-dClosedLoop-0473 | dCalibratedLens | P39, P9; stall-and-loop items 8 and 11; v2 `flow.rework-budget` | C5-F6 |
| cl-dClosedLoop-0474 | dCalibratedLens | P40, P9; cloud-and-scale | C5-F6 |
| cl-dClosedLoop-0475 | dConvergedCharter | gap-found-12 | holds |
| cl-dClosedLoop-0476 | dConvergedCharter | P11 | holds |
| cl-dClosedLoop-0477 | dConvergedCharter | gap-maint-04 | holds |
| cl-dClosedLoop-0478 | dConvergedCharter | gap-tool-05; fates RETIRED rows | holds |
| cl-dClosedLoop-0479 | dConvergedCharter | gap-spine-04; P8 | holds |
| cl-dClosedLoop-0480 | dConvergedCharter | P16; shape-reviews kind-factory-dup; cl-0212 | holds |
| cl-dClosedLoop-0481 | dConvergedCharter | gap-found-36; v2 `help.explanation`; final-questions FQ-6 | holds |
| cl-dClosedLoop-0482 | dConvergedCharter | fates top-level rows | holds |
| cl-dClosedLoop-0483 | dConvergedCharter | gap-found-13, gap-found-28; fates skills row; SKILL.template.md census | holds |
| cl-dClosedLoop-0484 | dConvergedCharter | gap-found-12 | holds |
| cl-dClosedLoop-0485 | dConvergedCharter | audit-fold H5 and M6; v2 [policies]; four `read_policy_key` copies in code; roles_lib.py:363 | holds |
| cl-dClosedLoop-0486 | dConvergedCharter | gap-tool-08; fates unattended rows; gate-legs.json unattended legs | C5-F4 |
| cl-dClosedLoop-0487 | dConvergedCharter | night-pass point 4 | holds |
| cl-dClosedLoop-0488 | dConvergedCharter | gap-tool-09; fates [table] kits; fates check limits | C5-F22 |
| cl-dClosedLoop-0489 | dConvergedCharter | P42; final-questions [help]; cl-0419 | C5-F12 |
| cl-dClosedLoop-0490 | dConvergedCharter | gap-orient-21; shape-reviews SA-9 | holds |
| cl-dClosedLoop-0491 | dConvergedCharter | shape-reviews SK-1 | holds |
| cl-dClosedLoop-0492 | dConvergedCharter | memory-plan [cycle]; shape-reviews cycle-walk | holds |
| cl-dClosedLoop-0493 | dConvergedCharter | P34, P37; memory-plan guides row | holds |
| cl-dClosedLoop-0494 | dConvergedCharter | P38 | holds |
| cl-dClosedLoop-0495 | dConvergedCharter | gap-roles-26; P8; cl-0438; flow-adoption folds | C5-F21 |
| cl-dClosedLoop-0496 | dConvergedCharter | gap-found-32; fates `.unattended.conf` row | holds |

## Build verdicts

Each build lists its confirmed findings. Refuted ids are dropped, and the skeptics' own findings are added to the build whose clause carries them.

| Build | Verdict |
|---|---|
| dTrueNorth | C1-F7, C1-F8, C1-F9, C1-F18 |
| dGroundRules | C1-F5, C1-F13, C1-F14 |
| dSafePassage | C1-F15, C1-F16 |
| dOrderedCharter | C1-F1, C1-F2, C1-F3, C1-F6, C1-F8, C1-F10, C1-F11, C1-F12, C1-F13, C1-F19, C1-F20 |
| dFairHearing | C2-F6, C2-F16 |
| dDeclaredLoop | C2-F1, C2-F2, C2-F3, C2-F8, C2-F9, C2-F13 |
| dPlacedRequest | C2-F4, C2-F7, C2-F10 |
| dKeptSession | C2-F11, C2-F12, C2-F15, CS2-F1, CS4-F1 |
| dBoundRoles | C3-F1, C3-F2, C3-F3, C3-F28, C3-F29 |
| dFurnishedOrders | C3-F4, C3-F5, C3-F6, C3-F7, C3-F8, C3-F28 |
| dTotalRecall | C3-F9, C3-F10, C3-F11, C3-F12, C3-F13, C3-F14, C3-F15, C3-F16 |
| dLinkedLibrary | C3-F17, C3-F18, C3-F20, C3-F22, C3-F23, C3-F31, CS3-F1 |
| dMindYourWords | C3-F24, C3-F25, C3-F26, C3-F27 |
| dWellOiledMachine | C4-F1, C4-F3, C4-F4, C4-F5, C4-F6, C4-F8, C4-F11, C4-F13 |
| dWitnessedBar | C4-F2, C4-F9, C4-F10, C4-F12 |
| dRankedPlan | C5-F13, C5-F14, C5-F19, CS1-F1 |
| dIndexedDesign | C5-F16 |
| dScopedBuild | C5-F5, C5-F18 |
| dShippedRelease | C5-F1, C5-F3, C5-F11, C5-F12, C5-F14, C5-F20, CS4-F2 |
| dTendedCadence | C5-F2, C5-F8, C5-F9, C5-F10 |
| dCalibratedLens | C5-F7, C5-F14 |
| dConvergedCharter | C5-F12, C5-F21, C5-F22 |

review-shape kind=spec-audit round=1 intensity=full at=synth raw=108 confirmed=95 refuted=11 unverified=2 blocker=1 high=12 medium=64 low=18 agents=11 out-tokens=669519
