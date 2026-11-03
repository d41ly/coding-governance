# TOOL-dFairHearing-1 — replay 3, run A's synthesis: raw return and report

**Serves:** research TOOL-dFairHearing-1

Agent `gov-synthesizer` (its type's effort, high), spawned by the main loop on 2026-11-03 with the handoff `prompts/2026-11-03-prompt-TOOL-dFairHearing-1-8-synthesizer.md` over a copy of `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-a.md` holding only its prompt and schema sections (sha256 prefix a315c96c3fc8). 13 tool uses, 350.7 s, 103.5k tokens. Its report went to the run's scratch, not the committed path the prompt names; it is copied whole below. The first run on the whole file is void (`2026-11-03-build-TOOL-dFairHearing-1-replay-void-runs`).

Its `twinFlags`: `[{"refuted": 59, "confirmed": 38}, {"refuted": 59, "confirmed": 13}]`.

## The return, verbatim

````json
{"path":"C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/fh1-replay3-report-a.md","summary":"BLOCKED. No blocker was confirmed. Six findings are graded high, in five items: (1) a fresh relaunch cannot replay the dead driver's Workflow journal; (2) fixture 2 replays driver.log, which cannot hold the acts it exists to catch; (3) unit worktrees have no path back onto the build branch; (4) [build] takes deliverables that other chain builds still own; (5) a lease take-over leaves the old driver running with no fencing epoch. By item the tally is 39: 5 high, 30 medium, 4 low. By raw confirmed finding it is 56: 0 blocker, 6 high, 45 medium, 5 low. Id 20's fix was rejected with no correction, so its worktree half is still to be designed. The refuted id 59 is a twin of confirmed ids 38 and 13. The move check is UNCHECKED because no current blob was usable. The harness's appendix block arrived without a closing marker or any text, so the report says so instead of copying it.","items":[{"severity":"HIGH","ids":[1,15],"grades":{"1":"HIGH","15":"MEDIUM"}},{"severity":"HIGH","ids":[7,17,52],"grades":{"7":"MEDIUM","17":"HIGH","52":"HIGH"}},{"severity":"HIGH","ids":[3],"grades":{"3":"HIGH"}},{"severity":"HIGH","ids":[4,32,33,44],"grades":{"4":"HIGH","32":"MEDIUM","33":"MEDIUM","44":"MEDIUM"}},{"severity":"HIGH","ids":[50],"grades":{"50":"HIGH"}},{"severity":"MEDIUM","ids":[2,20],"grades":{"2":"MEDIUM","20":"MEDIUM"}},{"severity":"MEDIUM","ids":[5],"grades":{"5":"MEDIUM"}},{"severity":"MEDIUM","ids":[6,37],"grades":{"6":"MEDIUM","37":"MEDIUM"}},{"severity":"MEDIUM","ids":[8,16],"grades":{"8":"MEDIUM","16":"MEDIUM"}},{"severity":"MEDIUM","ids":[9],"grades":{"9":"MEDIUM"}},{"severity":"MEDIUM","ids":[10,23],"grades":{"10":"MEDIUM","23":"MEDIUM"}},{"severity":"MEDIUM","ids":[11],"grades":{"11":"MEDIUM"}},{"severity":"MEDIUM","ids":[18,29],"grades":{"18":"MEDIUM","29":"MEDIUM"}},{"severity":"MEDIUM","ids":[19,27],"grades":{"19":"MEDIUM","27":"MEDIUM"}},{"severity":"MEDIUM","ids":[22],"grades":{"22":"MEDIUM"}},{"severity":"MEDIUM","ids":[25,40,60],"grades":{"25":"MEDIUM","40":"MEDIUM","60":"MEDIUM"}},{"severity":"MEDIUM","ids":[26],"grades":{"26":"MEDIUM"}},{"severity":"MEDIUM","ids":[28,42],"grades":{"28":"MEDIUM","42":"MEDIUM"}},{"severity":"MEDIUM","ids":[30],"grades":{"30":"MEDIUM"}},{"severity":"MEDIUM","ids":[31],"grades":{"31":"MEDIUM"}},{"severity":"MEDIUM","ids":[34],"grades":{"34":"MEDIUM"}},{"severity":"MEDIUM","ids":[35],"grades":{"35":"MEDIUM"}},{"severity":"MEDIUM","ids":[36,41],"grades":{"36":"MEDIUM","41":"MEDIUM"}},{"severity":"MEDIUM","ids":[38,13],"grades":{"38":"MEDIUM","13":"LOW"}},{"severity":"MEDIUM","ids":[39],"grades":{"39":"MEDIUM"}},{"severity":"MEDIUM","ids":[43],"grades":{"43":"MEDIUM"}},{"severity":"MEDIUM","ids":[48],"grades":{"48":"MEDIUM"}},{"severity":"MEDIUM","ids":[49],"grades":{"49":"MEDIUM"}},{"severity":"MEDIUM","ids":[51],"grades":{"51":"MEDIUM"}},{"severity":"MEDIUM","ids":[53],"grades":{"53":"MEDIUM"}},{"severity":"MEDIUM","ids":[54],"grades":{"54":"MEDIUM"}},{"severity":"MEDIUM","ids":[55],"grades":{"55":"MEDIUM"}},{"severity":"MEDIUM","ids":[56],"grades":{"56":"MEDIUM"}},{"severity":"MEDIUM","ids":[57],"grades":{"57":"MEDIUM"}},{"severity":"MEDIUM","ids":[58],"grades":{"58":"MEDIUM"}},{"severity":"LOW","ids":[12],"grades":{"12":"LOW"}},{"severity":"LOW","ids":[21],"grades":{"21":"LOW"}},{"severity":"LOW","ids":[24],"grades":{"24":"LOW"}},{"severity":"LOW","ids":[47],"grades":{"47":"LOW"}}],"dispositions":[{"id":1,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"Recovery relies on journal replay that the spawn return says a fresh session cannot do."},{"id":15,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"Same defect as id 1, seen from the grounding lens."},{"id":7,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Fixture 2's population holds no Workflow acts, so it passes trivially."},{"id":17,"disposition":"class:fixture-passes-by-finding-nothing","reason":"driver.log holds 0 Workflow acts, so fixture 2 is green before act binding exists."},{"id":52,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Same fixture 2 defect, seen from the failure-envelope lens."},{"id":3,"disposition":"class:two-answers-to-one-question","reason":"[isolate] and two sibling records give opposite answers on how unit commits reach the build branch."},{"id":4,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"[build] takes v2 deliverables but leaves their owning v2 rows and gap owners standing."},{"id":32,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"The record settles where next lives but marks nothing in v2:704 or v2:711 for amendment."},{"id":33,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"The subagent-stop hook and act binding are given to dWellOiledMachine while the [settled] row and v2's dBoundRoles row still own them."},{"id":44,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Same chain-ownership overlap, seen from the blast-radius lens."},{"id":50,"disposition":"new:lease-without-fencing-epoch","reason":"A lease take-over has no epoch or token to stop the old holder acting."},{"id":2,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"The build-lifetime default assumes one -p run can serve many item schemas."},{"id":20,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"The build-lifetime default assumes one session can work in many unit worktrees, though its cwd is fixed at launch."},{"id":5,"disposition":"new:sibling-role-with-no-component","reason":"The roles layer's executor actor and its duties have no Runtime component."},{"id":6,"disposition":"class:two-answers-to-one-question","reason":"runtime.relaunch and runtime.driver-refresh both govern driver renewal."},{"id":37,"disposition":"class:two-answers-to-one-question","reason":"Same two-key renewal defect, seen from the reuse lens."},{"id":8,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"Invariant 2 claims a refusal that hooks cannot perform on agent() and nested workflow() calls."},{"id":16,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"Same invariant 2 overclaim, seen from the grounding lens."},{"id":9,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Fixture 6 passes on either branch, and fixture 12 has no bound."},{"id":10,"disposition":"class:two-answers-to-one-question","reason":"Invariant 7 says fail closed while allowed policy values say fail open or degrade."},{"id":23,"disposition":"class:two-answers-to-one-question","reason":"Same invariant 7 defect, seen from the grounding lens."},{"id":11,"disposition":"new:extension-point-selected-by-closed-enum","reason":"Registered-adapter extension points are selected by closed-enum policy keys."},{"id":18,"disposition":"class:two-answers-to-one-question","reason":"An authored CLI floor and the decided session-version source answer one question, against the wrong binary."},{"id":29,"disposition":"class:two-answers-to-one-question","reason":"Same CLI-floor defect, seen from the reuse lens."},{"id":19,"disposition":"class:two-answers-to-one-question","reason":"A new supervisor with its own stall predicate sits beside resume-tick.sh and --liveness, and has no host lifecycle."},{"id":27,"disposition":"class:two-answers-to-one-question","reason":"Same supervisor-host defect, seen from the reuse lens."},{"id":22,"disposition":"new:mechanism-contradicts-measured-platform-fact","reason":"The record claims Codex hook parity that the sessions research contradicts."},{"id":25,"disposition":"class:two-answers-to-one-question","reason":"runtime.fanout is a second carrier beside agent-cap's FANOUT_CAP."},{"id":40,"disposition":"class:two-answers-to-one-question","reason":"Same fanout carrier defect, seen from the blast-radius lens."},{"id":60,"disposition":"class:two-answers-to-one-question","reason":"Same fanout carrier defect, seen from the failure-envelope lens."},{"id":26,"disposition":"class:two-answers-to-one-question","reason":"runtime.reap is a second reap policy beside PROCMON_REAP_MODE."},{"id":28,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Retiring the absolute hooksPath names none of its readers or writers, and it reverses a decided position."},{"id":42,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Same hooksPath defect, seen from the blast-radius lens."},{"id":30,"disposition":"class:two-answers-to-one-question","reason":"The allowlist and the owner's auto permission-mode ruling are two models for one set of launches."},{"id":31,"disposition":"new:cites-superseded-decision","reason":"The record repeats a parallelism route that a later decision superseded, and omits that decision's conditions."},{"id":34,"disposition":"class:two-answers-to-one-question","reason":"The core sweep would be a second worktree classifier and remover beside branch-reconcile."},{"id":35,"disposition":"class:two-answers-to-one-question","reason":"Runtime claims the journal and run-record kinds that runlog already owns."},{"id":36,"disposition":"class:two-answers-to-one-question","reason":"The pack declaration is a second hook-registration format beside the fragment files."},{"id":41,"disposition":"class:two-answers-to-one-question","reason":"Same pack-format defect, seen from the blast-radius lens."},{"id":38,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"The permission-skip retirement names none of the flag's consumers and has no owning unit."},{"id":13,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Same retirement: the test consumers asserting the flag are unnamed, and no fixture gates it."},{"id":39,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Retiring --plan and --status names none of their readers."},{"id":43,"disposition":"class:two-answers-to-one-question","reason":"runtime.* keys duplicate v2 keys, one pair with opposite defaults."},{"id":48,"disposition":"new:retry-without-bound","reason":"Driver relaunch drops today's attempt cap and has no terminal state."},{"id":49,"disposition":"new:effect-without-idempotent-witness","reason":"Command adapters need not be idempotent when an effect lands before its witness."},{"id":51,"disposition":"new:reaper-without-ownership-predicate","reason":"The sweep has no ownership or clean-and-merged predicate."},{"id":53,"disposition":"class:staged-break-substitutes-a-synthetic-value","reason":"Fixture 4 stubs the CLI and fixture 7 uses a synthetic exit, so the measured partial fan is never staged."},{"id":54,"disposition":"new:counter-without-release-path","reason":"The in-flight counter has no stated feed and no slot release."},{"id":55,"disposition":"new:retry-without-bound","reason":"The SubagentStop hold has no retry bound."},{"id":56,"disposition":"new:recurring-item-without-period-witness","reason":"Cadence items have no period-keyed witness, so a late node re-runs a finished period."},{"id":57,"disposition":"new:derivation-without-closed-answer-set","reason":"next defines no answer for an empty frontier or bad input."},{"id":58,"disposition":"new:invariant-wider-than-its-enforcing-rule","reason":"Invariant 2 covers every act, but act binding covers only spawns, Workflow calls and transitions."},{"id":12,"disposition":"new:owed-check-left-undisposed","reason":"Three owed compaction checks have no disposition."},{"id":21,"disposition":"new:unmeasured-claim-left-ungated","reason":"Calls per act and the turn-based trigger are unmeasured."},{"id":24,"disposition":"new:unmeasured-claim-left-ungated","reason":"The dispatcher latency goal is untimed."},{"id":47,"disposition":"new:gap-without-register-key","reason":"The twelve new gaps carry no gap-<area>-NN key."}],"twinFlags":[{"refuted":59,"confirmed":38},{"refuted":59,"confirmed":13}]}
````

## The report it wrote, verbatim

````markdown
**Serves:** spec-audit PLAY-dClosedLoop-1
# Tier-2 spec audit: the dClosedLoop runtime layer's design record, run 1

Provenance: the synthesis of a full-intensity Tier-2 spec audit by the gov-synthesizer role. The finders were gov-spec-reviewer under the unit-spec preset (coherence, grounding, reuse, blast-radius, failure-envelope), the skeptic batches were gov-skeptic, and seven sibling spec records were supplied as context. This is run 1 of the two independent rounds the owner asked for.

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@767187aa4073f6e64cb2b2ef6b798f0a538347fd
Round: 1

## Verdict: BLOCKED

No blocker was confirmed. Six findings are graded high, in five items, and a spec audit's chain does not stop while a high stands. The tally by item is 39: 5 high, 30 medium, 4 low. The tally by raw confirmed finding is 56: 0 blocker, 6 high, 45 medium, 5 low.

Review shape: intensity full, raw 60, confirmed 56, refuted 4, merged 0, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 14 | 13 | 1 | 0 | 0 | 0 | 0.93 |
| grounding | yes | 10 | 10 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 13 | 13 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 8 | 2 | 0 | 0 | 0 | 0.80 |
| failure-envelope | yes | 13 | 12 | 1 | 0 | 0 | 0 | 0.92 |

Run integrity: 5 of 5 lenses and 5 of 5 skeptic batches returned, and none died. There were 0 contradictory, orphaned, duplicate or spurious verdicts. Of the 56 fixes, 55 were judged sound and 1 (id 20) was judged UNSOUND with no correction. The skeptics re-graded 15 findings and left none ungraded. No lens notes were supplied, so every lens ran on the kit's generic brief. The checklist held 11 items, each assigned to one lens.

The move check is UNCHECKED: the harness found no usable current blob for the subject, so whether the record moved since blob 767187aa is not known. No gate leg manifest was read, so no finding is homed to a gate leg. Every line address below is into blob 767187aa.

Every item's address is in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, given by its section tag. Each grade below is the finding's binding grade.

## High

### H1. A fresh relaunch cannot replay the dead driver's Workflow journal
- **Ids:** 1 (high), 15 (medium; the finder graded it high).
- **Where:** [supervise] Relaunch (:300-302), [spawn] replay and fallback (:333-335, :341-343), [policies] `runtime.relaunch` (:483), [tests] fixture 3.
- **Wrong:** [supervise] relaunches a driver "fresh, never resumed". [spawn] relies on `resumeFromRunId` journal replay so that no completed agent is paid for twice, and it names "the run journal" as the fallback if SubagentStop does not fire. The spawn research return (research-runtime-spawn.md:101) says replay works only in the same session or after `claude --resume`, and that a fresh session has nothing to resume.
- **Consequence:** On the fallback path, a relaunched driver loses completed returns, which breaks invariant 4, or it re-spawns and pays again for every agent the dead run had completed. Fixture 3 cannot pass on a correct build. Recovery rests on SubagentStop persistence, and fixture 6 has not verified that.
- **Fix (judged SOUND by the skeptic for both ids):** Pick one recovery path and state it in both [supervise] and [spawn]. One option: relaunch with `--resume <session-id>` while a Workflow run is in flight, which can be the `runtime.relaunch` default for that case, and keep `fresh` for clean act boundaries only. The other option: make per-agent SubagentStop-persisted returns the only replay source, drop `resumeFromRunId` from [spawn], and make fixture 6 a precondition of the whole design. Either way, restate the [spawn] fallback so it claims no cross-session durability. Restate fixture 3 against the chosen path and run it against a fresh relaunch, for example by comparing the journal's totalTokens before and after the kill.
- **Gate:** new:mechanism-contradicts-measured-platform-fact. A design-record check that each platform claim cites the research row that bears it out.

### H2. Fixture 2 replays `driver.log`, which cannot hold the acts it exists to catch
- **Ids:** 17 (high), 52 (high), 7 (medium).
- **Where:** [tests] fixture 2 (:533-534), [act] act-binding rule.
- **Wrong:** `driver.log` records only unattended.sh verb calls (--liveness 376, --dispatch 362, --check-commit 330, --brief 228, and so on). On a re-probe of its 1,964 lines, `grep -ci workflow` printed 0. The 17 inline Workflow calls and 25+ ad-hoc scripts that research-runtime-executor.md:42 and :153 name as the likely failures live in session transcripts. The log is also untracked and per-node, so on another node the population is empty.
- **Consequence:** Every logged act is a driver verb that maps to a transition, so the out-of-declaration rate is about 0% whatever the design. The fixture is green before act binding exists, and it certifies what it does not check. It still catches out-of-order verb transitions, which is why it is high and not blocker.
- **Fix (judged SOUND by the skeptic for all three ids):** Draw the replay population from the main-session transcripts: every main-thread Workflow, Agent and Bash act, plus Bash invocations of scripts outside the declared commands. State that population in the fixture, and require it to be non-empty. See it red before trusting it: count the inline `Workflow{script}` calls in session b710e9c3 and confirm the fixture reports them as outside a declared item.
- **Gate:** class:fixture-passes-by-finding-nothing. A fixture must declare a non-empty population and carry a seen-red run.

### H3. Unit worktrees have no path back onto the build branch
- **Ids:** 3 (high).
- **Where:** [isolate] (:381-391).
- **Wrong:** Each unit gets its own worktree, branched from the build branch tip, and release "reclaims all of it". Nothing merges a unit branch back, and nothing orders integration between parallel units. Two sibling records say the opposite: flow-steps.md:156 `build.unit-pass` has "commits queued by the executor", and v2's dScopedBuild row has parallel units' commits queued in one shared worktree.
- **Consequence:** Releasing a unit can discard committed work that never reached the build branch. Two records answer one question.
- **Fix (judged SOUND by the skeptic):** Add to [isolate] an integration step owned by the supervisor that fast-forwards or merges each unit branch into the build branch in declared order, before release. Refuse release while the unit branch has commits the build branch lacks, and name the witness for that. Reconcile the step with flow-steps `build.unit-pass` and v2's dScopedBuild row. Extend fixture 8 so that after release the build branch contains every unit's commits.
- **Gate:** class:two-answers-to-one-question.

### H4. [build] takes deliverables that other chain builds still own
- **Ids:** 4 (high), 32 (medium), 33 (medium), 44 (medium; the finder graded it high).
- **Where:** [build] units and gap tables (:499-512, :526-527), [gaps-proposed] "Already registered ... Their owners stand" (:592-598), [decide] client verbs (:263, :277-281), [settled] row 3 (:37), [enforce] roles pack (:357).
- **Wrong:** The v2 dDeclaredLoop row (architecture-v2.md:704) still holds the `next` verb, the position engine, the owner's pause, resume, withdraw and supersede, the executor launched where `run.host` says, the resume-card fix, the compact hook and gap-flow-10. v2's dBoundRoles row (:705) and [settled] :37 hold schema-forced returns, return validation at subagent stop and gap-roles-04. dShippedRelease holds lander hardening and gap-deploy-07. Yet [build] lists the `next` CLI, the client verbs, the subagent-stop durable returns hook and signal traps as dWellOiledMachine units, and puts act binding in the roles pack (:357) while building it as a Runtime unit (:501). It says those gap owners "stand", and RT-3 moves only four gaps. Line :263 claims to settle where `next` lives but marks nothing in v2 for amendment. v2:711 (dScopedBuild) still plans parallel commits in a shared worktree, which [isolate] abolishes. The client verbs omit `supersede` and are not mapped onto unattended's --hold, --park, --abort and --resume. v2's chain header "thirteen builds" goes stale.
- **Consequence:** Two builds each build one deliverable, or each assumes the other built it. That yields two SubagentStop rules that disagree, and it breaks the build order between dDeclaredLoop and its child dWellOiledMachine.
- **Fix (judged SOUND by the skeptic for all four ids):** In [build], add a "[chain] edits" or "units it takes from dDeclaredLoop" list that quotes each v2:704, v2:705 and v2:711 phrase that moves, and mark those v2 rows for amendment. Move gap-flow-10, gap-roles-04 and gap-deploy-07 (or the parts that move) with their units, or drop the units. For the subagent-stop hook and act binding, choose one owner each: either Runtime only wires dBoundRoles' check into the dispatcher, or move the item out of the [settled] row. Add `supersede` to the client verbs or record why it is gone, and map each verb onto the unattended verb it extends (pause to --hold, withdraw to --abort, resume to --resume, ask and answer to --park and --propose), or say which are new. Note that the chain grows from thirteen to fourteen builds. Put the moves to the owner as part of RT-3.
- **Gate:** class:amendment-leaves-its-other-half-standing.

### H5. A take-over leaves the old driver running, and nothing fences it
- **Ids:** 50 (high).
- **Where:** [supervise] take-over (:312-313), [act] act-binding rule (:323-324).
- **Wrong:** When a supervisor dies and another node takes the run lease, the old node's detached driver and its Workflow agents keep running (research-runtime-spawn.md:23: launch is detached through Start-Process or setsid). The new supervisor launches a second driver for the same act. Act binding checks only that `next` named the act, not which lease epoch the driver serves. The record has no epoch, token or fencing anywhere.
- **Consequence:** On the take-over path, two drivers can perform the same act. That means duplicate spawns, agents paid for twice, and concurrent commits on one worktree, the E4 index-lock failure (research-runtime-hooks.md:134).
- **Fix (judged SOUND by the skeptic):** Bind each driver to a lease epoch or token that the supervisor issues. Have act binding refuse an act from a driver whose epoch is no longer current. State that an old driver that sees a lost lease stops at its next tool call. Add a fixture that takes over the lease while a driver is mid-act and checks that the old driver's next spawn is refused.
- **Gate:** new:lease-without-fencing-epoch.

## Medium

### M1. The default `build` driver lifetime conflicts with a single-schema, single-cwd `-p` launch
- **Ids:** 2 (medium; the finder graded it high), 20 (medium).
- **Where:** [supervise] launch flags (:293-294), [act] Lifetime (:325), [policies] `runtime.driver-lifetime` (:481), [isolate] workspace per unit lease (:381-385).
- **Wrong:** Drivers are launched as `claude -p --json-schema <item schema>`. A `-p` run returns one `structured_output` against one schema, and its working directory is fixed at launch. The default lifetime `build` has one driver serve many items and many unit worktrees. research-runtime-sessions.md:172 picks S2, a fresh driver per item.
- **Consequence:** A build-lifetime driver either loses the per-item schema fallback or is relaunched per item, which makes the default `item` in practice. Its role agents for later units run outside their own worktree, which brings back the shared-index hazard and defeats fixture 8.
- **Fix, schema half (id 2, judged SOUND by the skeptic):** Either make `item` the default and say that `--json-schema` binds a single item, or keep `build` and state how per-item returns are schema-forced inside one session, dropping the session-level fallback for that lifetime. Add a fixture that runs two items through one driver and checks each return against its own schema.
- **Fix, worktree half (id 20):** REJECTED by the skeptic, who gave no correction. How a driver's role agents reach each unit's worktree is still to be designed.
- **Gate:** new:mechanism-contradicts-measured-platform-fact.

### M2. "The executor" has no component, and hook items have no route
- **Ids:** 5 (medium).
- **Where:** [extend] actor kinds (:435), [supervise] each tick (:288-292), [act].
- **Wrong:** Runtime's actor kinds are command, role, hook and owner. The roles layer's (layer-roles.md:345) are role, command, hook, executor and owner, and its matrix (:335) gives the executor `build.unit-pass`, `build.acceptance` and `build.core`. The tick routes only command items and role or owner items. The executor's duties in layer-roles.md:197-220 (resolve inputs, key and class facts, recompute them at the spawn, wrap the work order) have no component.
- **Consequence:** `build.acceptance`, `build.unit-pass` and hook items have no handler. A Workflow harness has no filesystem access, so it cannot do the executor's duties. A model driver doing them would break P29. A new actor kind would need dispatch code.
- **Fix (judged SOUND by the skeptic):** State that "the executor" is the supervisor, or rename it in one place. Add `executor` (or its mapping) to the actor kinds, and say how hook items are dispatched or witnessed. Assign work-order assembly and fact keying to the supervisor before the driver's act, passed as Workflow args. Make dispatch by actor kind a registered adapter.
- **Gate:** new:sibling-role-with-no-component.

### M3. Two policy keys govern one driver renewal
- **Ids:** 6 (medium), 37 (medium; the finder graded it low).
- **Where:** [policies] `runtime.relaunch` and `runtime.driver-refresh` (:482-483), [supervise] Relaunch (:300-301), [sessions] (:403).
- **Wrong:** `runtime.relaunch` (fresh, resume) and `runtime.driver-refresh` (fresh, compact-with-card) both set how a driver at `context.threshold` is renewed. [supervise] says "never resumed", although `resume` is an allowed value. [sessions] cites only `runtime.driver-refresh`, and nothing in the record reads `runtime.relaunch`.
- **Consequence:** With non-default values the record gives two verdicts, and the builder has to guess which key wins.
- **Fix (judged SOUND by the skeptic for both ids):** Either merge them into one key, for example `runtime.driver-renewal` with the values fresh, resume and compact-with-card, or split them by trigger: death or a limit goes to `runtime.relaunch`, the threshold to `runtime.driver-refresh`, with the split named in both [supervise] and [policies]. Reword "never resumed" as "resumed only under runtime.relaunch=resume".
- **Gate:** class:two-answers-to-one-question.

### M4. Invariant 2 claims to refuse spawns that no hook can see
- **Ids:** 8 (medium), 16 (medium; the finder graded it high).
- **Where:** [invariants] 2 (:451), [act] act-binding rule (:323-324), [supervise] agents in flight (:303-304), [tests] fixture 5.
- **Wrong:** Workflow `agent()` calls and nested `workflow()` calls are not tool calls, so no hook sees them (tools/hooks/agent-cap.js:18-27, research-runtime-spawn.md). Invariant 2 still says a spawn that `next` did not name is refused, and the in-flight count runs "across every Workflow call". SubagentStart may observe these spawns but cannot block them. Fixture 5 assumes a queue, but a PreToolUse hook can only refuse. No fixture asserts that an unnamed spawn is refused.
- **Consequence:** Inside an admitted script, extra agents and nested workflows run unrefused and uncounted. The invariant certifies more than the hook surface can check. The effect is contained because harness scripts are declared code.
- **Fix (judged SOUND by the skeptic for both ids):** Restate invariant 2 and `runtime.fanout` at the Workflow-call granularity: the call, its declared script by sha, and a static bound on the script's `agent()` sites, as agent-cap rules 1-3 do today. Name what stays unchecked: the runtime `agent()` count and nested `workflow()`. Change fixture 5 to assert a refusal plus a supervisor-side queue. Add fixtures for an unnamed spawn or Workflow call being refused, and for an admitted script calling `agent()` once more than declared.
- **Gate:** new:mechanism-contradicts-measured-platform-fact.

### M5. Fixtures 6 and 12 cannot fail
- **Ids:** 9 (medium).
- **Where:** [tests] fixtures 6 (:540) and 12 (:549).
- **Wrong:** The [tests] heading (:529) promises fixtures "each able to make the design lose". Fixture 6 ("SubagentStop fires ... If not, the stated fallback") passes on either branch and never checks that the fallback persists a valid return. Fixture 12 ("the cost ... measured") has no bound.
- **Consequence:** Return durability and per-start cost go ungated.
- **Fix (judged SOUND by the skeptic):** Split fixture 6 in two. First, SubagentStop fires for a role-typed sidechain and its return file exists, keyed by agent_id. Second, with the hook removed, the journal plus `--json-schema` still yields a persisted, schema-valid return, and a staged invalid return is held. Give fixture 12 a bound derived from [current], for example a headless start under N seconds or under 84k tokens.
- **Gate:** class:fixture-passes-by-finding-nothing.

### M6. Invariant 7 is unconditional, and session binding has no witness
- **Ids:** 10 (medium), 23 (medium).
- **Where:** [invariants] 7 (:457), [policies] `runtime.hook-failure` (:484) and `runtime.below-floor` (:486), [enforce] failing closed (:371-373), [sessions] binding (:395-396).
- **Wrong:** Invariant 7 says every enforcement rule fails closed, yet `runtime.hook-failure=open` and `runtime.below-floor=degrade` are allowed values. SessionStart, which binds a session to its build and delivers the card, cannot block: its errors exit 2, which SessionStart does not block (research-runtime-hooks.md:24). SubagentStart cannot block either. Neither event is in the witness list, which names only Stop, SubagentStop and git hooks. The record never says how act binding treats an unbound session, notably an attended one that the supervisor did not launch with a known item.
- **Consequence:** A crashed SessionStart dispatcher leaves a session unbound, with nothing recorded. Resume already misses the card 7 of 14 times. Whether act binding then refuses everything or nothing is unstated, so binding may fail open.
- **Fix (judged SOUND by the skeptic for both ids):** Qualify invariant 7 with "under `runtime.hook-failure=closed` on a node at or above `runtime.cli-floor`". Add SessionStart and SubagentStart to the witness-backed events: the hook writes a binding record, and the PreToolUse act-binding rule requires it, so a missing binding refuses the first tool call. Add a fixture with a crashed SessionStart dispatcher, and add that case to fixture 9.
- **Gate:** class:two-answers-to-one-question.

### M7. Extension-point selector keys are closed enums
- **Ids:** 11 (medium).
- **Where:** [extend] (:439-445), [policies] `runtime.harnesses`, `runtime.scheduler`, `runtime.journal` (:490-492), [schedule] (:414-418).
- **Wrong:** [extend] says a new harness, scheduler backend or journal sink is "a filled contract. Runtime gains no code". The keys that select them are closed enums of today's adapters: `runtime.harnesses` is fixed at `claude-code-and-codex`, `runtime.scheduler` is single-valued, and `runtime.journal` is local-and-summary or local. [schedule] runs a node task together with CI's schedule, which a single-valued key cannot express.
- **Consequence:** A newly registered adapter cannot be selected without changing the key schema.
- **Fix (judged SOUND by the skeptic):** Make these keys take lists of registered adapter names, validated against the registry. For example: `runtime.harnesses = [claude-code, codex]`, `runtime.scheduler = {cadence item -> backend}`, `runtime.journal = [runlog, observability]`.
- **Gate:** new:extension-point-selected-by-closed-enum.

### M8. The CLI floor grades the PATH binary, not the session's version
- **Ids:** 18 (medium; the finder graded it high), 29 (medium).
- **Where:** [enforce] CLI floor (:369-370), [policies] `runtime.cli-floor`, [harness] node registry (:428-429), [supervise] headless launch (:293).
- **Wrong:** This node runs the desktop session at 2.1.295 and the PATH `claude` at 2.1.292. The supervisor would launch the PATH binary for every headless driver. The record never says which binary is checked or launched. It also authors a version floor, which TOOL-aMendedFleet-61's review rejected in favour of the launching session's own version (read_cli_version, the `cli-version` fact). unattended.sh:8790-8795 explains why `claude --version` is the wrong source.
- **Consequence:** The floor grades the wrong binary. Every headless driver on this node runs below the floor and may fail open. Below-floor handling is still an open owner question (RT-2), which keeps the grade at medium.
- **Fix (judged SOUND by the skeptic for both ids):** Read the running session's own version through read_cli_version and the `cli-version` fact, never PATH. Have the supervisor resolve and pin the absolute `claude` it launches, and check that binary against `runtime.cli-floor` before any launch. Record both versions per node. Cite TOOL-aMendedFleet-61 and state why a fail-closed feature floor differs from the launch-version pin it rejected.
- **Gate:** class:two-answers-to-one-question.

### M9. Nothing hosts the supervisor, and resume-tick.sh already is one
- **Ids:** 19 (medium; the finder graded it high), 27 (medium).
- **Where:** [supervise] where it runs (:285), [schedule] node-task backend (:414-416), [invariants] 5, [build] the supervisor unit.
- **Wrong:** The supervisor is a per-node process with no model. Nothing launches it, keeps it alive or restarts it after a reboot, and nothing says who triggers a take-over. The desktop scheduled task named as a carrier wakes a model session, which only an agent can register (`.unattended.conf` lines 132-137). resume-tick.sh is already that process: OS-scheduled every 10 minutes as gov-resume-tick, it treats `--liveness` as its only stale verdict, kills stale trees and launches detached `claude -p`. The record cites it only for the permissions flag (:153, :299, :569).
- **Consequence:** After a reboot no tick runs, or the supervisor ends up hosted in a model session, which breaks invariant 5. A second out-of-session actor with its own "stalls" predicate competes with `--liveness`.
- **Fix (judged SOUND by the skeptic for both ids):** State that the supervisor is resume-tick.sh grown. It keeps `--liveness` as the only stale or terminal verdict, `--beat`, the attempt cap and run_detached, and replaces only the `--resume --dangerously-skip-permissions` launch. Make the node-task backend the existing gov-resume-tick registration (README lines 202-218), extended to wake cadence items. That gives an OS-level carrier with a restart policy and a liveness beat under the run lease. Say that a desktop-app task, if kept, wakes a model session and is therefore an act, not the supervisor.
- **Gate:** class:two-answers-to-one-question.

### M10. Codex hook parity is claimed but not measured
- **Ids:** 22 (medium).
- **Where:** [harness] one guard core (:424-425), [policies] `runtime.harnesses`.
- **Wrong:** [harness] says Codex's events "now match one for one". The research (research-runtime-sessions.md:126) lists only PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd for Codex, and :133 says Codex has no Workflow tool (unverified). The dispatcher (:352-354) needs SessionStart, PostToolUse, Stop and PostCompact. Codex's own docs call its hooks "not a complete enforcement boundary".
- **Consequence:** Under `claude-code-and-codex`, a Codex driver gets no binding, card or Stop witness, and no role harness, so invariant 7 does not hold there. The effect is limited to that opt-in value.
- **Fix (judged SOUND by the skeptic):** Replace the claim with the measured event map, list the missing events and the missing Workflow capability, and state the degraded guarantees. Alternatively, restrict Codex to role-agent or instructions-plus-guards use until a spawn backend is declared.
- **Gate:** new:mechanism-contradicts-measured-platform-fact.

### M11. `runtime.fanout` is a second, unbounded carrier for agent-cap's bound
- **Ids:** 25 (medium), 40 (medium), 60 (medium).
- **Where:** [policies] `runtime.fanout` (:487) and `runtime.hook-failure` (:484), [supervise] agents in flight (:303-304), [invariants] 7.
- **Wrong:** `runtime.fanout` ("an agent count", default 5, no range) is a second carrier beside agent-cap's MAX_VERIFIERS and EFFECTIVE_CAP, `.agent-cap.conf` FANOUT_CAP (which can only lower the cap), the FANOUT_CAP placeholder in four workflow templates, and the agent-cap-restatement leg. It also changes the semantics: agent-cap counts a per-prompt total, "never the concurrency bound" (agent-cap.js:1533). TOOL-aRepatriatedFork-7 decided the cap is never raisable, and TOOL-aUnmannedHelm-1 measured that a hook counter is racy. A value of 0 deadlocks, and values above the platform's 16 or 20 cannot be enforced. Allowing `runtime.hook-failure=open` also falsifies invariant 7, the defect M6 holds.
- **Consequence:** Two enforcers answer one question with different semantics. A value above 5 does nothing, or revives the override that was removed on purpose.
- **Fix (judged SOUND by the skeptic for all three ids):** Name one carrier: either `runtime.fanout` replaces `.agent-cap.conf` and agent-cap.js reads it through the policy mirror, or it is an alias of FANOUT_CAP limited to 1..5 that can only lower the cap. Have the in-flight count read min(FANOUT_CAP, 5), and do not make the supervisor's counter a per-hook read. Validate the range at intake, 1 to min(16, 20). Either drop `open` from `runtime.hook-failure` or qualify invariant 7 with it, and have the class check report the policy value. List the consumers to change: agent-cap.js, the FANOUT_CAP templates, check-agent-cap-restatement.sh and its leg, and the agent-cap self-test leg. Cite TOOL-aRepatriatedFork-7 and TOOL-aUnmannedHelm-1. Add a fixture: with `runtime.fanout=3`, both the hook and the supervisor refuse the 4th agent.
- **Gate:** class:two-answers-to-one-question.

### M12. `runtime.reap` is a second reap policy beside PROCMON_REAP_MODE
- **Ids:** 26 (medium).
- **Where:** [policies] `runtime.reap`, [supervise] "reaps orphans and stalls", [gaps-proposed] 7.
- **Wrong:** `runtime.reap` has the values orphans, orphans-and-idle and report. `.process-monitor.conf:54-70` declares PROCMON_REAP_MODE with the closed set report, reap-orphans and reap-all, and reap.py:367-368 and :439-440 refuse anything outside it. `orphans-and-idle` has no counterpart, and the record never names `reap.py --sweep` as the reaper.
- **Consequence:** A second reap policy, and possibly a second reaper, that bypasses process-monitor's safety fences (TOOL-aReapedSpinner-8..10).
- **Fix (judged SOUND by the skeptic):** Have the supervisor run `reap.py --sweep` under PROCMON_REAP_MODE. Retire `runtime.reap`, or make it name that closed set exactly. Reword gap 7 to: the existing sweep is never scheduled.
- **Gate:** class:two-answers-to-one-question.

### M13. A per-worktree `core.hooksPath` lets a unit branch weaken its own gate
- **Ids:** 28 (medium; the finder graded it high), 42 (medium).
- **Where:** [enforce] "`core.hooksPath` becomes per-worktree" (:374), [isolate] "the worktree's own hooks path" (:383).
- **Wrong:** WIRE-INTO-PROJECT.md:855-858 and check-wiring.sh:615-630 (TOOL-aWeldedTribunal-7) chose an out-of-tree path so a branch cannot make the guard inert. Running each worktree's own hooks lets a unit branch weaken its own gate, and the record never says the per-worktree path is a trusted copy. The change also touches readers the record does not name: check-wiring Check H (:740-773) sets the path only when it is unset and reports "ok" on today's absolute value; run-gates KF3 (:4928-4931) blanks an absolute hooksPath; govkit/matrix.py:143 sets the path; and the check-wiring self-test leg depends on all of them.
- **Consequence:** A guard bypass on a narrow path, limited to one unit's commits. The fix never reaches existing clones, and fixture 8 passes only on fresh worktrees.
- **Fix (judged SOUND by the skeptic for both ids):** Cite the decided position. Either keep one trusted out-of-tree copy per worktree, written by the supervisor from the build branch tip at allocation, or require the hook to refuse a `.githooks` that differs from the trusted copy. Name the mechanism (a relative `.githooks`, or `config.worktree` with extensions.worktreeConfig). List the consumers above, and make Check H refuse an absolute value, reusing its arm. Extend fixture 8 two ways: an edited `.githooks` in a worktree must not run, and an existing clone with an absolute hooksPath must report UNWIRED.
- **Gate:** class:retirement-inventory-misses-readers-by-value.

### M14. The permission allowlist ignores the owner's auto-mode ruling
- **Ids:** 30 (medium).
- **Where:** [supervise] "an explicit permission allowlist" (:296), [invariants] 8.
- **Wrong:** DECISIONS.md:225, TOOL-aMendedFleet-116 (owner, 2026-10-07), moves unattended runs to `--permission-mode auto` once node CLIs reach 2.1.281, and TOOL-aMendedFleet-117 is the open build. The record neither cites nor reconciles either. The two are not strictly exclusive, since auto mode can honour allow rules.
- **Consequence:** Two permission models get built for the same launches.
- **Fix (judged SOUND by the skeptic):** Cite both decisions. Either adopt auto mode with the allowlist as its floor, or raise the conflict as an RT question to the owner. Do not settle it by default.
- **Gate:** class:two-answers-to-one-question.

### M15. The record repeats a superseded parallelism route and omits its conditions
- **Ids:** 31 (medium).
- **Where:** [current] "No parallel units" (:166-167), [isolate], [tests] fixture 8.
- **Wrong:** The record repeats "parallelism route: none" (TOOL-cBriefedPilot-21, DECISIONS:76). TOOL-aHoistedPass-10 (DECISIONS:179) superseded it after TOOL-dUnstalledConvoy-7 cleared R2 with R5. The clearance depends on E3 condition 2 (passes stay off shared mutable records), which [isolate] omits. Fixture 8 re-tests only the index lock, which is already known, and skips E4 conditions 5-7 (merging without markers or loss).
- **Consequence:** Merge conflicts or lost writes on RUN.md, the decision log, backlog shards and generated indexes.
- **Fix (judged SOUND by the skeptic):** Cite TOOL-dUnstalledConvoy-7 and TOOL-aHoistedPass-10. Add to [isolate] that the supervisor alone writes shared records and merges unit branches through the row-keyed merge driver. Restate fixture 8 as E4 conditions 5-7 over a run that touches shared records.
- **Gate:** new:cites-superseded-decision.

### M16. The core sweep duplicates branch-reconcile
- **Ids:** 34 (medium).
- **Where:** [isolate] "Release reclaims all of it, and a sweep reaps orphans: today, 8 merged worktrees", [contract] engine kits (:29, :467).
- **Wrong:** branch_reconcile.py:15-17 already classifies worktrees as MERGED, EQUIVALENT or SUPERSEDED and removes them under `--write` with a recovery manifest (TOOL-dSweptBranches-1..4). [contract] keeps branch-reconcile an expansion, and "the core never depends on an expansion". So the core must either rebuild that classifier or break its own rule.
- **Consequence:** A second classifier and remover, and two removers that disagree.
- **Fix (judged SOUND by the skeptic):** Either promote branch-reconcile's verdicts and removal into the core engine kit, or limit the core sweep to workspaces the supervisor leased and leave merged-branch housekeeping to branch-reconcile. State the choice in [isolate] and [contract].
- **Gate:** class:two-answers-to-one-question.

### M17. Journaling supervisor events needs a runlog change no unit lists
- **Ids:** 35 (medium).
- **Where:** [contract] record kinds and engine kits (:467-468), [extend] journal sinks (:443), [policies] `runtime.journal`.
- **Wrong:** runlog already owns the journal grammar, the journals and the committed run record (record.py). runlog_lib.py:40 closes PRODUCER_FILES to driver, gates and pushes, runlog.py:499 takes `--producer` choices from it, and selftest.py:1009 pins it. [contract] claims the run journal and the run record as Runtime's record kinds and omits runlog from the engine kits, while the supervisor "journals every event to runlog" (:311). No [build] unit lists the runlog change.
- **Consequence:** Possibly a second journal format. The claim "Runtime gains no code" fails at the first new producer.
- **Fix (judged SOUND by the skeptic):** Name runlog as the engine kit for the journal and the run record, and make `runtime.journal`'s summary record.py's committed record. List adding the supervisor and dispatcher producers as a runlog unit in [build], or make the producer set declarable.
- **Note:** The refuted id 14 held that listing runlog as a Runtime engine kit would contradict the layer model, since runlog is an Observability expansion. It is a different defect, so it is not flagged as a twin. The fix's first clause should still be read against that refutation.
- **Gate:** class:two-answers-to-one-question.

### M18. The hook-pack declaration ignores the fragment files and their readers
- **Ids:** 36 (medium), 41 (medium).
- **Where:** [enforce] "Rules come in packs", "One dispatcher entry per event" and "onFailure: block" (:352-366), [extend] hook packs, [build] the enforcement-surface unit (:505).
- **Wrong:** The pack declaration is designed from scratch, beside 12 tracked `*.fragment.json` files and their readers: settings-merge.py, check-wiring.sh, check-hook-destinations.sh and govkit. settings-merge.py:435-436 writes entries as `{type, command}` only, and its `--check` (:457-462) compares only the command. No wiring code mentions `onFailure`.
- **Consequence:** A second registration format. Wiring legs go red, or grade fragments the dispatcher no longer reads. Adopters stay fail-open while `--check` reports them wired.
- **Fix (judged SOUND by the skeptic for both ids):** Define a pack as the fragment schema extended with owner, decision class, failure mode, latency budget and policy key. Have settings-merge.py render one dispatcher entry per event, write `onFailure`, and compare it in `--check`. List as files the enforcement-surface unit touches: every fragment, including the kickoff's orientation-card and orientation-replay; settings-merge.py; each adopt-*.sh; check-hook-destinations.sh and its leg; check-wiring.sh and govkit; and the kit version markers.
- **Gate:** class:two-answers-to-one-question.

### M19. The permission-skip retirement has no owner, no gate and no consumer list
- **Ids:** 38 (medium; the finder graded it high), 13 (low).
- **Where:** [supervise] "No session the runtime launches skips permissions" (:298-299), [invariants] 8 (:458), [build] units (:499-512), [tests] 1-12 (:531-549).
- **Wrong:** The flag at resume-tick.sh:385 is "retired", but no [build] unit retires or rewrites resume-tick, and no fixture gates the retirement. The record names none of the consumers: resume-tick.test.sh:368 and :385, which assert the flag; check-unattended.sh:5770, which scans resume-tick.sh; and the unattended SKILL's CronCreate keepalive (.claude/skills/unattended/SKILL.md:16, rendered from tools/unattended/SKILL.template.md).
- **Consequence:** An unchanged resumer still launches `--dangerously-skip-permissions`, which breaks invariant 8, or the test goes red with no owner. The test arm would go red visibly, so the risk is an unowned change, not a silent ship.
- **Fix (judged SOUND by the skeptic for both ids):** Add a [build] unit that retires resume-tick or rewrites it onto the fresh relaunch, naming these consumers. Add a fixture that greps every runtime launcher's argv and every launch site under tools/ for `--dangerously-skip-permissions` and fails on any hit, seen red on resume-tick.sh:385.
- **Twin:** The refuted id 59 describes this defect. Its skeptic held that naming each reader of a retired value is unit-level detail for the chain build's own spec. The skeptics on 13 and 38 confirmed it, so the flag changes no grade or count.
- **Gate:** class:retirement-inventory-misses-readers-by-value.

### M20. Retiring `--plan` and `--status` misses their readers
- **Ids:** 39 (medium).
- **Where:** [decide] "It replaces today's three derivations: --plan, --status and the run phase" (:265-266).
- **Wrong:** Three kinds of reader depend on the old verbs. runlog's model.py:120-140 classifies `--status` as heartbeat, read-only and tree-blind. stop-guard.js:167 sends sessions to `--plan`. unattended-build.js calls `--plan` 20 times. gen_build_index.py also reads these verbs. The record names none of them and does not say whether the old verbs survive as aliases.
- **Consequence:** runlog misreads liveness on supervised runs, and stop-guard points to a retired derivation.
- **Fix (judged SOUND by the skeptic):** List these readers for re-pointing in the same unit: model.py and its fixtures, stop-guard.js, unattended-build.js and its template, and gen_build_index.py. State whether `--plan` and `--status` stay as aliases. Add a fixture in which runlog reads a heartbeat from a journal holding only `next` calls.
- **Gate:** class:retirement-inventory-misses-readers-by-value.

### M21. Four `runtime.*` keys duplicate v2 keys, and none has preset values
- **Ids:** 43 (medium; the finder graded it high).
- **Where:** [policies] `runtime.isolation` (:488), `runtime.scheduler` (:490), `runtime.hook-failure`, `runtime.below-floor` (:486), [contract] (:471).
- **Wrong:** `runtime.isolation` (default worktree-per-unit) duplicates v2's `build.worktree` (:483, default shared), with opposite defaults. `runtime.scheduler` overlaps `maintain.host` (:490) and `run.host` (:449), which use a different vocabulary. `runtime.hook-failure` sits beside `hooks.bypass`. No `runtime.*` key has preset values, though v2:512 defines a preset as a complete assignment, and `runtime.below-floor` has no default.
- **Consequence:** Two keys answer one behaviour, and the record fails v2's completeness rule for presets. The planned completeness check would catch the missing preset rows, which contains the effect.
- **Fix (judged SOUND by the skeptic):** For each pair, retire or fold one key and say which: reconcile the isolation default, and give the scheduler keys one value vocabulary. State how `hooks.bypass` relates to fail-closed. Give every `runtime.*` key a value in each of the four presets, and give `runtime.below-floor` a provisional default until RT-2 is answered.
- **Gate:** class:two-answers-to-one-question.

### M22. Driver relaunch has no attempt bound
- **Ids:** 48 (medium; the finder graded it high).
- **Where:** [supervise] Relaunch (:300-302), [policies].
- **Wrong:** A driver that dies or hits a limit is relaunched with no count, backoff or terminal state. This drops today's RESUME_ATTEMPTS (resume-tick.sh:121 and :326, default 6, "ATTEMPTS EXHAUSTED"). `roles.retries` governs role-return retries, not driver relaunch (v2:430).
- **Consequence:** An unbounded token sink at 84k tokens per start when an item never completes or the node is exhausted.
- **Fix (judged SOUND by the skeptic):** Add `runtime.relaunch-attempts` and a backoff. Once attempts are exhausted, park the run and raise an owner item. Add a fixture in which a stub CLI that always exits at `--max-turns` ends parked after N attempts.
- **Gate:** new:retry-without-bound.

### M23. A take-over can re-run a command whose effect landed before its witness
- **Ids:** 49 (medium; the finder graded it high).
- **Where:** [supervise] "The supervisor's own death" (:312-313), [invariants] 3 (:452), [extend] command adapters (:436).
- **Wrong:** A command item whose effect landed before its witness was written is re-dispatched. No command adapter is required to be idempotent or to reconcile.
- **Consequence:** A double push attempt or a duplicate record. A lander re-push of the same sha is largely a no-op at git level, so the harm is mostly a duplicate record.
- **Fix (judged SOUND by the skeptic):** Require each command adapter's witness contract to declare idempotence or a reconcile probe; for the lander, the probe is that origin is already at the expected sha. Add a fixture that kills the supervisor after the lander's push and before its witness, and checks that the take-over does not push twice.
- **Gate:** new:effect-without-idempotent-witness.

### M24. The sweep has no ownership or clean-and-merged predicate
- **Ids:** 51 (medium; the finder graded it high).
- **Where:** [isolate] "Release reclaims all of it, and a sweep reaps orphans" (:388-389), [tests] fixture 8.
- **Wrong:** The sweep targets 497 temp directories whose source research-runtime-hooks.md:98 calls not attributable, since `mktemp -d` is used by unattended, run-gates and others. Nothing protects a dirty or unmerged worktree, and the census has one of each. "Merged" appears only in the census, not as a rule.
- **Consequence:** Foreign scratch and uncommitted or unmerged work get deleted. Fixture 8's "counts return to baseline" rewards over-deletion.
- **Fix (judged SOUND by the skeptic):** Reap only what the supervisor allocated: lease-marked directories under a gov-owned scratch root, and worktrees it created. Require a worktree to be clean and merged (or pushed) before removal. Change fixture 8 so that a dirty worktree and a foreign temp directory both survive.
- **Gate:** new:reaper-without-ownership-predicate.

### M25. The deferral path is tested only against a stubbed CLI
- **Ids:** 53 (medium).
- **Where:** [tests] fixtures 4 (:537-538) and 7, [spawn] deferral factory (:344-345).
- **Wrong:** Fixture 4 puts a stub `claude` ahead of the real one on PATH, so no Workflow `agent()` returns null and the deferral factory is never exercised. Fixture 7 invites a synthetic exit-1 guard. Neither covers the measured partial fan, in which up to 10 of 20 agents died (research-runtime-spawn.md:89). [spawn] gives a per-agent null-to-deferral rule but no unit-level outcome for a mixed fan.
- **Consequence:** The deferral path ships unproven, and done returns may be paid for again.
- **Fix (judged SOUND by the skeptic):** Specify the partial-fan outcome in [spawn]. Add a fixture in which some of k agents return null: the done returns persist, the nulls become deferred-platform, and the relaunch re-pays only the nulls. For fixture 7, require a guard with a missing interpreter path and one killed by a resource limit.
- **Gate:** class:staged-break-substitutes-a-synthetic-value.

### M26. The in-flight counter has no feed and no slot release
- **Ids:** 54 (medium).
- **Where:** [spawn] `runtime.fanout` counting, [supervise] agents in flight (:303-304).
- **Wrong:** The record never says what feeds the counter or how a dead agent's slot is released. Agents inside a script are invisible to hooks (research-runtime-spawn.md:22-23), and today's ledger relies on a 45-minute expiry (:126).
- **Consequence:** Leaked slots fill `runtime.fanout` and every later dispatch queues forever. If hooks alone feed the counter, it under-counts.
- **Fix (judged SOUND by the skeptic):** Feed the counter from the script's declared concurrency at launch, or from SubagentStart and SubagentStop once fixture 6 proves they fire. Give each slot an expiry, or reconcile it against live processes and journal state. Add a fixture: kill a driver holding 5 slots, and the next dispatch is admitted after reconcile.
- **Gate:** new:counter-without-release-path.

### M27. The SubagentStop hold is unbounded and unspecified on bad input
- **Ids:** 55 (medium).
- **Where:** [spawn] "exit 2 holds an agent whose return fails" (:336-343).
- **Wrong:** The hold has no retry bound. Empty, unparseable and oversized `last_assistant_message` values are not handled. A crashed SubagentStop hook admits the stop, because onFailure has no effect there (research-runtime-hooks.md). The 5 schema retries in research-runtime-spawn.md apply to Workflow schemas, not to this hook.
- **Consequence:** The agent is held indefinitely, or the item stops with nothing persisted and an unclear status.
- **Fix (judged SOUND by the skeptic):** Bind the hold to `roles.retries` (or the 5 schema retries), then persist a refusal and route the item. Specify handling for empty, unparseable and oversized messages, with a size cap. State that a missing return after a stop means the item is unwitnessed and can be dispatched again. Test it with a SubagentStop hook pointed at a missing path.
- **Gate:** new:retry-without-bound.

### M28. A late node can re-run a cadence period another node finished
- **Ids:** 56 (medium).
- **Where:** [schedule] missed fire and lease (:413, :416), [invariants] 3 (:452), [tests] fixture 10.
- **Wrong:** A lease excludes only concurrent runs. A missed-fire catch-up on node B re-runs a period node A has already finished. The record has no period-keyed witness, so invariant 3 is undefined for recurring items.
- **Consequence:** The weekly Loop Review or the nightly bar runs twice per period, or never again.
- **Fix (judged SOUND by the skeptic):** Key each cadence witness by its period (ISO week or date), and consult it before acquiring the lease. Extend fixture 10: node A runs the period's item, then node B launches late and must skip.
- **Gate:** new:recurring-item-without-period-witness.

### M29. `next` has no answer outside "one act per frontier item"
- **Ids:** 57 (medium).
- **Where:** [decide] One derivation (:264-275).
- **Wrong:** Only "exactly one act per frontier item" is defined. There are no answers for an empty frontier, malformed declarations, invalid policy values, corrupt witnesses or an unreachable remote. The record's own census (:133, :558) measures two runs stalled at BUILDING with all work terminal, and the design does not close that case.
- **Consequence:** The supervisor ticks forever on no act, or acts on a guess.
- **Fix (judged SOUND by the skeptic):** Add a closed answer set: terminal, blocked (with a reason), invalid-input (naming the bad declaration, policy or witness) and stale-remote. Make each a declared supervisor transition. Add fixtures: an empty frontier closes the run, and a corrupt witness answers invalid-input.
- **Gate:** new:derivation-without-closed-answer-set.

### M30. Act binding skips Bash scripts and leaves unbound sessions unstated
- **Ids:** 58 (medium).
- **Where:** [act] act-binding rule (:323-324, :328), [invariants] 2 (:451).
- **Wrong:** The rule covers only spawns, Workflow calls and transitions, while invariant 2 says "Every act was named by next". The 25+ improvised scripts that [gaps-proposed] 1 (:557) cites run through Bash and are uncovered. "Attended sessions are drivers too" leaves a session bound to no build, such as owner work or a review fan-out, unspecified.
- **Consequence:** Invariant 2 is false as built. Attended sessions are either refused everything or silently exempt.
- **Fix (judged SOUND by the skeptic):** Widen the rule to Bash execution of scripts outside the declared commands, or narrow invariant 2 and record the script class as unenforced. State the no-binding behaviour, and add a fixture for each.
- **Gate:** new:invariant-wider-than-its-enforcing-rule.

## Low

### L1. Three owed compaction checks have no disposition
- **Ids:** 12 (low; the finder graded it medium).
- **Where:** [sessions] (:393-404), [settled] owed checks (:46-48).
- **Wrong:** Three owed checks are left open: whether a subagent's brief is re-injected after its own compaction, the re-attachment cap (5 files of 5,000 tokens each), and whether PreCompact can flush inside a subagent (v2 ~:752-755). [current] :196-198 records the facts, but [sessions], [build] and [tests] dispose of none of them.
- **Consequence:** A future card over 5,000 tokens would come back as a path only, with no gate. The effect is small because SessionStart re-delivers the card on compaction and no subagent has ever compacted.
- **Fix (judged SOUND by the skeptic):** Dispose of each check in [sessions]. Bound the card under 5,000 tokens with a size check in the build's units, and declare subagent compaction out of scope (0 of 2,708 transcripts compacted). Add a fixture that compacts a session and finds the card's content re-attached.
- **Gate:** new:owed-check-left-undisposed.

### L2. Calls per act are assumed, and the trigger is stated in turns
- **Ids:** 21 (low; the finder graded it medium).
- **Where:** [act] Lifetime (:326-327).
- **Wrong:** [act] says a few calls per act fit hundreds of acts below "the 1,000-turn compaction distance". Calls per act were never measured, and the measured median is about 44 main-session calls per unit (research-runtime-executor.md). Compaction triggers on tokens (preTokens about 914k to 1M), not turns.
- **Consequence:** More relaunches than the design expects, at 84k tokens each.
- **Fix (judged SOUND by the skeptic):** Add a fixture that measures calls and tokens per act for a thin driver, choose the lifetime default from it, and restate the trigger as tokens against `context.threshold`.
- **Gate:** new:unmeasured-claim-left-ungated.

### L3. The dispatcher's latency goal is untimed
- **Ids:** 24 (low).
- **Where:** [enforce] one dispatcher entry per event (:354-355).
- **Wrong:** [enforce] claims lazy packs stay within the 57 ms one guard costs today. research-runtime-hooks.md puts an in-process dispatcher at about 85 ms (39 + 3 x 15), "neutral if lazy", which is untimed. A Bash call loads at least two packs, the write-allowance and gate-guard packs. No fixture times the dispatcher.
- **Consequence:** A latency-only regression that no fixture would catch.
- **Fix (judged SOUND by the skeptic):** Add a fixture that times the dispatcher on a benign Bash payload over 10 runs against the 57 ms baseline, or restate the goal as a measured budget once the dispatcher exists.
- **Gate:** new:unmeasured-claim-left-ungated.

### L4. The twelve new Runtime gaps carry no register key
- **Ids:** 47 (low).
- **Where:** [gaps-proposed] "New area Runtime: 1. ... 12." (:553-590).
- **Wrong:** The twelve gaps have no `gap-<area>-NN` key, while the register keys every row (for example gap-orient-14, gap-roles-17). [build]:527 does tie them to dWellOiledMachine.
- **Consequence:** The register's acceptance join has nothing to match. The defect is cosmetic until registration.
- **Fix (judged SOUND by the skeptic):** Name the prefix (for example `gap-rt-01` to `gap-rt-12`) and each gap's owner build. Update the register's re-measured counts (:226-297).
- **Gate:** new:gap-without-register-key.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=60 confirmed=56 refuted=4 merged=0 unverified=0 blocker=0 high=6 medium=45 low=5 agents=11 out-tokens=unknown

## Appendix

The harness's appendix text did not arrive. Its opening marker is the last line of the prompt and has no closing marker, so there is no text to copy here. Each confirmed finding's disposition is on its item's Gate line above.
````
