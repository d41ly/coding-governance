# TOOL-dFairHearing-1 — replay 3, run B's synthesis: raw return and report

**Serves:** research TOOL-dFairHearing-1

Agent `gov-synthesizer` (its type's effort, high), spawned by the main loop on 2026-11-03 with the handoff `prompts/2026-11-03-prompt-TOOL-dFairHearing-1-9-synthesizer.md` over a copy of `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-b.md` holding only its prompt and schema sections (sha256 prefix 04eacfdd0fe0). 11 tool uses, 378.1 s, 114.3k tokens. Its report went to the run's scratch, not the committed path the prompt names; it is copied whole below. The first run on the whole file is void (`2026-11-03-build-TOOL-dFairHearing-1-replay-void-runs`).

Its `twinFlags`: `[{"refuted": 61, "confirmed": 43}, {"refuted": 61, "confirmed": 28}]`.

## The return, verbatim

````json
{"path":"C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/fh1-replay3-report-b.md","summary":"Verdict CLEAN WITH FIXES. There are 38 items covering all 57 confirmed findings: 0 BLOCKER, 7 HIGH, 28 MEDIUM, 3 LOW by item, and 0 BLOCKER, 9 HIGH, 44 MEDIUM, 4 LOW by raw finding. Every binding grade is kept. The HIGH items are: the SubagentStop hook reads last_assistant_message, which schema-forced agents leave empty (15, 49); fixture 2 replays a driver.log that cannot hold improvised acts (17, 40); a fresh relaunch cannot replay a Workflow run (16, 1, 50); act binding refuses the roles layer's prompt-writer and scout spawns (5); v2 chain rows are left standing after scope moves (31, 9, 48); runtime policy keys duplicate v2 keys (37, 2); a take-over has no fencing (51). Three fixes were judged UNSOUND with no correction (18, 28, 50). For 28 and 50 the item rests on a twin's sound fix, and 18 is still to be designed. Refuted id 61 is flagged as a twin of 28 and 43. The prompt's appendix marker never closes, so the appendix text was not delivered and none was copied.","items":[{"severity":"HIGH","ids":[15,49],"grades":{"15":"HIGH","49":"HIGH"}},{"severity":"HIGH","ids":[17,40],"grades":{"17":"HIGH","40":"HIGH"}},{"severity":"HIGH","ids":[16,1,50],"grades":{"16":"HIGH","1":"MEDIUM","50":"MEDIUM"}},{"severity":"HIGH","ids":[5],"grades":{"5":"HIGH"}},{"severity":"HIGH","ids":[31,9,48],"grades":{"31":"HIGH","9":"MEDIUM","48":"MEDIUM"}},{"severity":"HIGH","ids":[37,2],"grades":{"37":"HIGH","2":"MEDIUM"}},{"severity":"HIGH","ids":[51],"grades":{"51":"HIGH"}},{"severity":"MEDIUM","ids":[4,20],"grades":{"4":"MEDIUM","20":"MEDIUM"}},{"severity":"MEDIUM","ids":[12,54],"grades":{"12":"MEDIUM","54":"MEDIUM"}},{"severity":"MEDIUM","ids":[3],"grades":{"3":"MEDIUM"}},{"severity":"MEDIUM","ids":[6],"grades":{"6":"MEDIUM"}},{"severity":"MEDIUM","ids":[7],"grades":{"7":"MEDIUM"}},{"severity":"MEDIUM","ids":[8],"grades":{"8":"MEDIUM"}},{"severity":"MEDIUM","ids":[10],"grades":{"10":"MEDIUM"}},{"severity":"MEDIUM","ids":[11,36],"grades":{"11":"MEDIUM","36":"MEDIUM"}},{"severity":"MEDIUM","ids":[13,21],"grades":{"13":"MEDIUM","21":"MEDIUM"}},{"severity":"MEDIUM","ids":[18],"grades":{"18":"MEDIUM"}},{"severity":"MEDIUM","ids":[19],"grades":{"19":"MEDIUM"}},{"severity":"MEDIUM","ids":[22],"grades":{"22":"MEDIUM"}},{"severity":"MEDIUM","ids":[24,46],"grades":{"24":"MEDIUM","46":"MEDIUM"}},{"severity":"MEDIUM","ids":[25,55],"grades":{"25":"MEDIUM","55":"MEDIUM"}},{"severity":"MEDIUM","ids":[45,26],"grades":{"45":"MEDIUM","26":"LOW"}},{"severity":"MEDIUM","ids":[28,43],"grades":{"28":"MEDIUM","43":"MEDIUM"}},{"severity":"MEDIUM","ids":[29,41],"grades":{"29":"MEDIUM","41":"MEDIUM"}},{"severity":"MEDIUM","ids":[30,42],"grades":{"30":"MEDIUM","42":"MEDIUM"}},{"severity":"MEDIUM","ids":[32],"grades":{"32":"MEDIUM"}},{"severity":"MEDIUM","ids":[33],"grades":{"33":"MEDIUM"}},{"severity":"MEDIUM","ids":[34,39],"grades":{"34":"MEDIUM","39":"MEDIUM"}},{"severity":"MEDIUM","ids":[35,44],"grades":{"35":"MEDIUM","44":"MEDIUM"}},{"severity":"MEDIUM","ids":[52],"grades":{"52":"MEDIUM"}},{"severity":"MEDIUM","ids":[53],"grades":{"53":"MEDIUM"}},{"severity":"MEDIUM","ids":[56],"grades":{"56":"MEDIUM"}},{"severity":"MEDIUM","ids":[57],"grades":{"57":"MEDIUM"}},{"severity":"MEDIUM","ids":[58],"grades":{"58":"MEDIUM"}},{"severity":"MEDIUM","ids":[59],"grades":{"59":"MEDIUM"}},{"severity":"LOW","ids":[23],"grades":{"23":"LOW"}},{"severity":"LOW","ids":[27],"grades":{"27":"LOW"}},{"severity":"LOW","ids":[60],"grades":{"60":"LOW"}}],"dispositions":[{"id":1,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Relies on Workflow replay after a fresh relaunch, which the spawn research says the platform does not support."},{"id":2,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Adds runtime.isolation and moves gap-conc-03 while build.worktree and dScopedBuild's commit queue stand."},{"id":3,"disposition":"class:two-answers-to-one-question","reason":"runtime.relaunch, runtime.driver-refresh and the prose each answer which key governs a relaunch."},{"id":4,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Invariant 2 claims a refusal no hook can make on agent() calls."},{"id":5,"disposition":"new:sibling-statement-with-no-carrier","reason":"The roles layer's prompt-writer and scout spawns have no bound act in Runtime."},{"id":6,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Both branches of fixture 6 pass, and fixture 12 has no bar."},{"id":7,"disposition":"new:claim-without-a-losing-fixture","reason":"Invariants 3, 6, 8 and 9 and the primary-tree rule have no fixture that can fail."},{"id":8,"disposition":"class:two-answers-to-one-question","reason":"Invariant 3 and the flow's re-entry routes disagree on whether a witnessed item runs again."},{"id":9,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Moves scope to dWellOiledMachine while the v2 chain rows still hold it."},{"id":10,"disposition":"new:sibling-statement-with-no-carrier","reason":"The siblings' 'executor' has no term in Runtime's design."},{"id":11,"disposition":"class:two-answers-to-one-question","reason":"Invariant 7 and the allowed fail-open and bypass values answer the failure mode two ways."},{"id":12,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Counts agents across Workflow calls that no hook can observe or block."},{"id":13,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Asserts Codex event parity that the sessions return does not show."},{"id":15,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Reads last_assistant_message, which schema-forced agents leave without the return."},{"id":16,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Relies on resumeFromRunId replay from a fresh session, which the research says has nothing to resume."},{"id":17,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Fixture 2's driver.log population cannot contain the improvised acts it should refuse."},{"id":18,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Launches a PATH claude that the node measurement shows is below the floor."},{"id":19,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Assumes claude -p hosts a Workflow run to completion, with no session measured on that entrypoint."},{"id":20,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Twin text of id 4: a refusal no hook can make on agent() calls."},{"id":21,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Twin text of id 13: Codex parity the returns do not show."},{"id":22,"disposition":"new:failure-path-left-undefined","reason":"No starter, keep-alive or restart is given for the supervisor process."},{"id":23,"disposition":"new:claim-without-a-losing-fixture","reason":"The driver-lifetime default rests on an unmeasured turn distance."},{"id":24,"disposition":"new:claim-outruns-measured-platform-fact","reason":"States as fact that an imported Compact instructions section is honoured, which the research marks unverified."},{"id":25,"disposition":"new:fixture-scope-wider-than-mechanism","reason":"Fixture 7 expects refusals from user-level guards the dispatcher does not wire."},{"id":26,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"The hooksPath change ignores that the value's absolute form is the defect, and the readers keyed on that form."},{"id":27,"disposition":"new:claim-without-a-losing-fixture","reason":"The 57 ms latency budget has no measuring fixture."},{"id":28,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"The flag retirement leaves resume-tick, its test arms, the keepalive cron and stop-guard unaddressed."},{"id":29,"disposition":"class:two-answers-to-one-question","reason":"runtime.fanout is a second, raisable carrier of agent-cap's ceiling."},{"id":30,"disposition":"class:two-answers-to-one-question","reason":"runtime.reap duplicates PROCMON_REAP_MODE."},{"id":31,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Claims the next verb and the owner verbs while v2's dDeclaredLoop row still owns them."},{"id":32,"disposition":"class:two-answers-to-one-question","reason":"The subagent-stop check is owned by dBoundRoles and also listed as a dWellOiledMachine unit."},{"id":33,"disposition":"new:existing-seam-unnamed","reason":"Hook packs ignore the fragment seam and v2's hook factory."},{"id":34,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"The dispatcher consolidation drops the StopFailure stall-recorder and leaves live hooks with no pack."},{"id":35,"disposition":"new:existing-seam-unnamed","reason":"Specifies a new deferral factory beside tier2-review's existing deferred-platform shape."},{"id":36,"disposition":"class:two-answers-to-one-question","reason":"Twin text of id 11: invariant 7 against the allowed bypass and fail-open values."},{"id":37,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Adds runtime keys overlapping v2 keys with no retirement and no preset values."},{"id":39,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Twin text of id 34: the consolidation's inventory misses live entries."},{"id":40,"disposition":"class:fixture-passes-by-finding-nothing","reason":"Twin text of id 17: fixture 2 is blind to the class it tests."},{"id":41,"disposition":"class:two-answers-to-one-question","reason":"Twin text of id 29: a second fanout carrier."},{"id":42,"disposition":"class:two-answers-to-one-question","reason":"Twin text of id 30: a second reap switch."},{"id":43,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"Twin text of id 28: resume-tick's disposition and readers are unlisted."},{"id":44,"disposition":"new:existing-seam-unnamed","reason":"Twin text of id 35: the existing deferral shape and its consumers are unnamed."},{"id":45,"disposition":"class:retirement-inventory-misses-readers-by-value","reason":"The hooksPath change lists none of check-wiring, KF3 or pre-push, which branch on the value's form."},{"id":46,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Twin text of id 24: an unverified import is stated as honoured."},{"id":48,"disposition":"class:amendment-leaves-its-other-half-standing","reason":"Twin text of id 9: the v2 chain rows are left standing."},{"id":49,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Twin text of id 15: the wrong SubagentStop field carries the return."},{"id":50,"disposition":"new:claim-outruns-measured-platform-fact","reason":"The fallback is a run journal that a fresh session cannot replay, and SubagentStop firing is unverified."},{"id":51,"disposition":"new:failure-path-left-undefined","reason":"A take-over does not fence the old drivers."},{"id":52,"disposition":"new:failure-path-left-undefined","reason":"Driver relaunch has no cap and no terminal outcome."},{"id":53,"disposition":"class:two-answers-to-one-question","reason":"A per-launch item schema against a build-lifetime driver serving many schemas."},{"id":56,"disposition":"new:witness-without-a-reader","reason":"Commit-side git-hook witnesses have no consumer."},{"id":57,"disposition":"new:failure-path-left-undefined","reason":"next has no output for an empty, non-terminal frontier or an unreadable input."},{"id":58,"disposition":"new:cure-covers-part-of-its-class","reason":"Act binding omits the Bash improvisation that gap 1 cites."},{"id":59,"disposition":"class:two-answers-to-one-question","reason":"Invariant 6 and the hook's direct write disagree on how return records change."},{"id":60,"disposition":"new:failure-path-left-undefined","reason":"The limit hold names no wake signal, no lease behaviour and no bound."},{"id":54,"disposition":"new:claim-outruns-measured-platform-fact","reason":"Twin text of id 12: an unobservable agents-in-flight count."},{"id":55,"disposition":"new:fixture-scope-wider-than-mechanism","reason":"Twin text of id 25: fixture 7's population exceeds the dispatcher's reach."}],"twinFlags":[{"refuted":61,"confirmed":43},{"refuted":61,"confirmed":28}]}
````

## The report it wrote, verbatim

````markdown
**Serves:** spec-audit PLAY-dClosedLoop-1
# Tier-2 spec audit: the runtime layer's design record for dClosedLoop, run b

Synthesis by gov-synthesizer from the skeptic-confirmed findings of run 2 of the owner's two independent Tier-2 rounds on this layer.

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@767187aa4073f6e64cb2b2ef6b798f0a538347fd
Round: 1

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. Seven HIGH items hold nine HIGH findings, and each needs a design change before a chain build adopts the record. By item, the tally is 38 items: 0 BLOCKER, 7 HIGH, 28 MEDIUM, 3 LOW. By raw confirmed finding, it is 57: 0 BLOCKER, 9 HIGH, 44 MEDIUM, 4 LOW. Every binding grade is kept, so the two tallies agree with the returned `grades`. Every address below is a section tag of the subject record, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

## Review shape

Intensity full, raw 61, confirmed 57, refuted 2, merged 2, unverified 0 (0 uncertain), precision 0.97.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 14 | 13 | 0 | 1 | 0 | 0 | 1.00 |
| grounding | yes | 13 | 13 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 9 | 9 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 12 | 10 | 1 | 1 | 0 | 0 | 0.92 |
| failure-envelope | yes | 13 | 12 | 1 | 0 | 0 | 0 | 0.92 |

Run integrity: lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died. There were 0 contradictory verdicts, 0 orphaned duplicate refutations, 0 spurious verdicts and 0 duplicates. 2 duplicate refutations were counted as merged confirmations. On confirmed findings, 54 fixes were judged sound, 3 were judged UNSOUND (ids 18, 28, 50), and none went unjudged or unproposed. 8 grades were re-graded by a skeptic, and none was left ungraded. No lens notes were supplied, so every lens ran on the kit's generic brief. The run is complete.

Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Preset: unit-spec, running coherence, grounding, reuse, blast-radius and failure-envelope. Seven sibling specs were supplied as context. An 11-item checklist was split across the five lenses. By-design came from the caller.

The move check is UNCHECKED: the harness had no usable current blob for the subject. No leg manifest was read from `tools/gate-legs.json`, so no finding is homed as `gate:`.

Refuted twins: id 61 (resume-tick's skip-permissions test arms left unlisted) describes part of the defect that ids 28 and 43 confirm, so it is flagged as their twin. Id 47 (the consumers of `--plan` and `--status`) is a different defect from ids 9, 31 and 57 at [decide], so it is not flagged.

## Items

### H1. The durable-return hook reads a field that schema-forced agents leave empty (HIGH)
- **Ids:** 15 HIGH, 49 HIGH.
- **Where:** [spawn] "returns persisted and validated by a SubagentStop hook"; [build] unit 5; [tests] 6.
- **What is wrong:** The SubagentStop hook persists `last_assistant_message` and checks it against the item's schema. A schema-forced Workflow agent ends on a `StructuredOutput` tool_use and has no text block. This session's transcripts show 18 such endings, and the roles research measured 2,588 `StructuredOutput` endings against 226 final-text endings. The [spawn] fallback covers only the case where the hook does not fire, not the case where it fires with no text.
- **Consequence:** Every schema-forced role return would be persisted empty or wrong, and every valid return would fail validation and be held (exit 2). Invariant 4 rests on a channel that carries no result, and fixture 6 still passes because it asks only whether the hook fires.
- **Fix (judged SOUND by the skeptic):** Read the return from `agent_transcript_path`, taking the input of the last `StructuredOutput` tool_use (or the journal's result). Use `last_assistant_message` only for free-text roles, and key the record by `agent_id`. Extend fixture 6 in two ways: a schema-forced agent's persisted return must byte-match what `agent()` resolved to, and a hand-built payload whose final text is valid JSON but whose `StructuredOutput` input is not must be refused.
- **Gate:** A spec-audit checklist entry: any hook field a design consumes is cited to a research return that shows it carrying the payload.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### H2. Act binding's losing test replays a log that cannot hold the acts it should refuse (HIGH)
- **Ids:** 17 HIGH, 40 HIGH.
- **Where:** [tests] 2.
- **What is wrong:** Fixture 2 replays "every act in the journaled builds' driver.log". That file has 1,964 lines, all start or end records of `unattended.sh` verbs, and `grep -c -i workflow` on it prints 0. The improvised acts act binding exists to refuse are the 17 inline workflows and the 25+ ad-hoc scripts, and none of them can appear there. Hook-issued verbs (`--liveness`, `--check-commit`) also dilute the 5% denominator.
- **Consequence:** The fixture passes whether or not act binding refuses an improvised act. It certifies what it does not check and would mislead the build that adopts it.
- **Fix (judged SOUND by the skeptic):** Take the replay population from the main-session transcripts: every Workflow and Agent call, plus every Bash call that runs a driver verb or a script, joined to runs. Alternatively, require act binding's own journal to exist first and state the fixture over that journal. Exclude hook-issued verbs from the denominator. Keep a red case: a transcript holding session b710e9c3's 17 inline workflows must exceed the threshold.
- **Gate:** A checklist entry: each design fixture names its population and shows that population can contain the failure class.
- **Disposition:** class:fixture-passes-by-finding-nothing.

### H3. A fresh relaunch cannot replay a Workflow run, so a killed item pays its agents twice (HIGH)
- **Ids:** 16 HIGH, 1 MEDIUM, 50 MEDIUM.
- **Where:** [supervise] Relaunch; [spawn] first bullet, "a run replays from its journal (resumeFromRunId)", and its fallback; [policies] runtime.relaunch; [tests] 3.
- **What is wrong:** A dead driver is "relaunched fresh, never resumed", yet [spawn] relies on `resumeFromRunId` replay. The spawn research says replay works only in the same session or after `claude --resume`, and that a fresh session has "nothing to resume". Persisted SubagentStop returns do not close the gap: a new run gets new agent ids, and nothing makes the harness consult earlier returns. Id 50 adds that whether SubagentStop fires for Workflow sidechains is unverified, and the stated fallback is the run journal, which a fresh session cannot replay.
- **Consequence:** A multi-agent item killed mid-fan re-runs and re-pays every agent that had already completed. Fixture 3 then fails, or passes only for one-agent items. Otherwise the build quietly switches to resume and pays the 503k resume cost the design argues against.
- **Fix (judged SOUND by the skeptic for ids 1 and 16):** Key each persisted return by item and work-order task-sha, which is stable across sessions, not by `agent_id`. Have the role harness skip any agent whose keyed return already exists before it spawns. Where no return was persisted (SubagentStop absent), either relaunch that act with `--resume <session-id>`, overriding runtime.relaunch=fresh, or record that the re-spend is accepted. Split runtime.relaunch by trigger (see M3). Make fixture 3 use a multi-agent item, such as a review fan, run it once with SubagentStop enabled and once disabled, and compare the journals' `totalTokens`.
- **Id 50's own fix:** Judged UNSOUND by the skeptic, with no correction, so it is still to be designed. The item's fix rests on ids 1 and 16 alone. The note on id 50 quotes the same wording as id 1's fix; the report carries that wording only under id 1's sound judgement.
- **Grades:** The binding grades are kept. Id 16 stands at HIGH because the design contradicts itself on the death path, and ids 1 and 50 stand at MEDIUM because their skeptics weighed the cost as wasted tokens with no wrong result.
- **Gate:** A checklist entry: a recovery path cites the research condition under which the platform supports it, and the record states that condition holds on the path.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### H4. Act binding refuses the roles layer's prompt-writer and scout spawns (HIGH)
- **Ids:** 5 HIGH.
- **Where:** [act]; [decide] "names exactly one act per frontier item"; [invariants] 2.
- **What is wrong:** The roles layer spawns a prompt writer in every role item's cycle ("not as items") and an orientation scout at session start. Neither is an item, so `next` never names them. Runtime's driver performs only the act `next` named and refuses any other spawn, and the record never mentions either spawn.
- **Consequence:** Built as written, act binding refuses the prompt writer in every role item and the scout at every session start. Otherwise the builder improvises an exemption, the hand-held exception path [framing] forbids. Roles cycle steps 2 and 3 have no carrier in Runtime either way.
- **Fix (judged SOUND by the skeptic):** In [act], define a role act as the whole roles [cycle]: the prompt-writer spawn, the work-order wrap and the role spawn. Either have `next`'s act carry both spawns, or have the role harness perform both inside one bound Workflow call. Name the session-start scout spawn as a bound act of SessionStart binding. Add both cases to the act-binding fixture.
- **Gate:** A checklist entry: every spawn a sibling layer specifies is traced to the bound act that carries it.
- **Disposition:** new:sibling-statement-with-no-carrier.

### H5. Moving `next`, the owner verbs and gaps to dWellOiledMachine leaves the v2 chain rows standing (HIGH)
- **Ids:** 31 HIGH, 9 MEDIUM, 48 MEDIUM.
- **Where:** [decide] Owners and client verbs; [build] units "the next CLI" and "the client verbs" and the gaps taken from other builds; [gaps-proposed] "Their owners stand".
- **What is wrong:** Runtime moves the `next` CLI and pause, resume and withdraw into dWellOiledMachine, and says this "settles the layer model's two placements of next". v2 still says "dDeclaredLoop builds the next verb". v2's dDeclaredLoop row still owns the four owner controls, the executor launch, gap-flow-10, gap-orient-12, gap-orient-14 and gap-tool-03. v2's dScopedBuild row still owns gap-conc-03 and the shared-worktree commit queue. The v2 chain heading still says "thirteen builds". Runtime's gap table does not take gap-flow-10, and its verb list drops `supersede`.
- **Consequence:** Two chain builds each ship a `next` verb and owner controls, and the next change cannot tell which owns them. One gap and one unit sit with two builds, and dScopedBuild's commit queue contradicts [isolate]'s worktree-per-unit lease. `supersede`, a terminal state the flow settles, has no client verb.
- **Fix (judged SOUND by the skeptic):** Choose one owner. If Runtime takes them, add the `next` CLI, the client verbs and gap-flow-10 to [build]'s "Gaps it would take" table and state the v2 chain re-cut. Otherwise word the [build] units as "extends dDeclaredLoop's next verb and guarded owner commands" and drop the client-verbs unit. In [build], quote each v2 [chain] row text that moves and each that stays, for the dDeclaredLoop and dScopedBuild rows. Name the heading-count change and the gap-register owner column. Add `supersede`, or state why it is excluded.
- **Grades:** The binding grades are kept. Id 31 stands at HIGH for misleading the next change, and ids 9 and 48 stand at MEDIUM.
- **Gate:** A checklist entry: any scope or gap a record moves is matched by an edit to, or a quoted retirement of, the row it leaves.
- **Disposition:** class:amendment-leaves-its-other-half-standing.

### H6. Runtime's new policy keys answer questions v2 keys already answer, with no presets and no retirement (HIGH)
- **Ids:** 37 HIGH, 2 MEDIUM.
- **Where:** [policies] (with [isolate], [schedule], [enforce], [supervise]); [build] gap-conc-03 row.
- **What is wrong:** `runtime.isolation` (default worktree-per-unit) answers the same question as v2's `build.worktree` (default shared), and flow-steps build.unit-pass still describes "commits queued by the executor" in the shared worktree. `runtime.scheduler` overlaps `run.host` and `maintain.host`. `runtime.relaunch` and `runtime.driver-refresh` overlap `resume.context`, which the velocity preset sets to always-resume. `runtime.hook-failure=closed` sits beside `hooks.bypass=allowed` and `core.exceptions=any-session-recorded`. The table gives single defaults, with no preset columns, no "joins the catalogue and the presets" line and no retirement.
- **Consequence:** Two keys govern one switch, and one preset can set them in opposite ways. A policy.toml reader has no rule for which wins. dDeclaredLoop's preset completeness check would red on 12 keys no preset carries.
- **Fix (judged SOUND by the skeptic):** For each overlap, either rename the v2 key into the runtime one (build.worktree to runtime.isolation, maintain.host and run.host to runtime.scheduler plus host adapters, resume.context to runtime.relaunch) and list it as retired in v2's next Revised line, or drop the runtime key and reference the v2 one. For isolation, that means [isolate] reads build.worktree with its value spellings, or build.worktree is retired with the change owed to v2 and to flow-steps build.unit-pass named. In [build]'s gap-conc-03 row, state that dScopedBuild's shared-worktree commit queue moves to, or is retired by, dWellOiledMachine. State how runtime.hook-failure=closed interacts with hooks.bypass and core.exceptions. Give every runtime.* key a value in each of velocity, standard, strict and guarded.
- **Grades:** The binding grades are kept. Id 37 stands at HIGH, and id 2, which covers one of its overlaps, stands at MEDIUM.
- **Gate:** A checklist entry, or a check over the policy catalogue: a new key is compared against every existing key for the same question, and each key carries a value in every preset.
- **Disposition:** class:amendment-leaves-its-other-half-standing.

### H7. A supervisor take-over cannot fence the drivers the dead supervisor launched (HIGH)
- **Ids:** 51 HIGH.
- **Where:** [supervise] "The supervisor's own death"; [act] act-binding rule.
- **What is wrong:** The record says a supervisor's death "loses only the tick in flight", with take-over from any node. The detached drivers the dead supervisor launched keep running. No driver identity, lease epoch or fencing token lets act binding tell an old driver from a new one.
- **Consequence:** After a take-over, `next` re-names the old driver's unwitnessed act (invariant 3), so two drivers perform one act. The result can be a duplicate commit, a duplicate fan or a race into the lander. Act binding refuses neither driver, because `next` named both.
- **Fix (judged SOUND by the skeptic):** Bind each act to a lease epoch, or to the driver's `--session-id`, recorded in the witness store. Have act binding refuse a driver whose epoch is not current. Require a take-over to kill or fence the previous holder's process tree before it relaunches. Add a fixture: kill only the supervisor mid-act, take over from a second process, and assert one witness and one commit.
- **Gate:** A checklist entry: every take-over path names how it fences the previous holder's in-flight work.
- **Disposition:** new:failure-path-left-undefined.

### M1. Invariant 2 claims a refusal no hook can make inside a Workflow script (MEDIUM)
- **Ids:** 4 MEDIUM, 20 MEDIUM.
- **Where:** [invariants] 2; [act] act-binding rule; [supervise] agents in flight; [tests] 2 and 5.
- **What is wrong:** Invariant 2 refuses any spawn `next` did not name. Workflow `agent()` and nested `workflow()` calls are not tool calls, so no hook sees them, and SubagentStart cannot block. agent-cap.js:24-27 says such agents "remain uncounted and always will be". No fixture stages an unnamed spawn and observes a refusal, and fixture 2 measures only how far the declaration covers past acts.
- **Consequence:** A named harness can spawn extra agents and pass, so the invariant certifies more than it checks. The rule can ship broken while fixture 2 passes.
- **Fix (judged SOUND by the skeptic):** Restate invariant 2 and [act] at the enforceable granularity. A spawn is bound at the Workflow or Agent call (script path and args against `next`'s act), plus transitions. Agents inside a script are bound by the registered harness's static fan declaration and reconciled through SubagentStart and SubagentStop journal entries. Add a fixture that stages, in a driver, a Workflow call, an Agent call and a `--phase` transition that `next` did not name, and asserts each is refused. Label fixture 2 as the declaration-coverage test it is.
- **Gate:** A checklist entry: each invariant names the hook event that enforces it and a research line showing that event can block.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M2. The agents-in-flight count has no counting unit, no queue and no release on a killed driver (MEDIUM)
- **Ids:** 12 MEDIUM, 54 MEDIUM.
- **Where:** [supervise] "Agents in flight are counted under the lease (runtime.fanout)"; [tests] 5.
- **What is wrong:** The count spans "every Workflow call", and fixture 5 requires a second 5-agent dispatch to queue. `agent()` calls are invisible to hooks, SubagentStart cannot block, and only a per-script static scan bounds Workflow concurrency. The record names no counting unit, no queue and no release when a driver dies without a stop event.
- **Consequence:** The bound can only be a per-call refusal, and a harness can escape the count. A killed driver, routine under fixture 3, leaks its slots, and every later dispatch queues forever.
- **Fix (judged SOUND by the skeptic):** The PreToolUse Workflow/Agent entry reserves the script's declared maximum concurrency against a lease-held counter, and the PostToolUse or completion notice releases it. Slots are also released when the dead process tree is reaped. State whether over-budget means refuse-and-retry or a supervisor-held queue, and reword fixture 5 to match. Extend fixture 5: kill the first dispatch mid-fan, and admit the second once the reap has run.
- **Gate:** A checklist entry: every counter a design holds names its reserve point, its release point and its release on death.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M3. Three answers to which key governs a driver relaunch (MEDIUM)
- **Ids:** 3 MEDIUM.
- **Where:** [policies] runtime.relaunch and runtime.driver-refresh; [supervise] Relaunch; [sessions] Context.
- **What is wrong:** [supervise] says a driver is "relaunched fresh, never resumed" on death, on a limit or on reaching context.threshold. [sessions] cites runtime.driver-refresh (fresh, compact-with-card) for the same renewal. runtime.relaunch (fresh, resume) appears only in [policies], and no body section reads it. v2 says context.threshold is read only under `fresh-at-boundary`, yet Runtime reads it for every driver.
- **Consequence:** A builder cannot tell which key governs a threshold relaunch. Setting runtime.relaunch=resume contradicts the prose, and the context.threshold semantics drift from v2.
- **Fix (judged SOUND by the skeptic):** Split the keys by trigger and name each trigger in [supervise] and [policies]: death or a limit uses runtime.relaunch, and reaching the threshold uses runtime.driver-refresh. Reword "never resumed" to "per runtime.relaunch". State that drivers read context.threshold whatever context.on-full is, and name the v2 row that must change.
- **Gate:** A checklist entry, or a policy check: every [policies] key has at least one body-section reader.
- **Disposition:** class:two-answers-to-one-question.

### M4. Fixture 6 passes on either branch, and fixture 12 has no bar (MEDIUM)
- **Ids:** 6 MEDIUM.
- **Where:** [tests] 6 and 12.
- **What is wrong:** Fixture 6 reads "SubagentStop fires ... If not, the stated fallback", so both outcomes pass. Fixture 12 says only "measured". The spawn research says the fallback leaves role returns "non-durable within a run", and the [tests] heading claims every fixture can make the design lose.
- **Consequence:** No gate decides the durable-return mechanism behind invariant 4. A too-slow headless start on Windows passes.
- **Fix (judged SOUND by the skeptic):** Give each branch of fixture 6 a hard assertion. If SubagentStop fires, a return record keyed by agent_id exists and a malformed return is held (exit 2). If it does not fire, kill the driver after one agent returns and assert the return survives on disk through the fallback, or the fixture fails. Give fixture 12 a pass bar, for example a start cost below the 84k-token and N-second budget that justifies fresh relaunch.
- **Gate:** A checklist entry: each fixture states a failing outcome, and no branch of it passes unconditionally.
- **Disposition:** class:fixture-passes-by-finding-nothing.

### M5. Invariants 3, 6, 8 and 9 and the primary-tree rule have no fixture (MEDIUM)
- **Ids:** 7 MEDIUM.
- **Where:** [invariants] 3, 6, 8 and 9; [isolate] primary tree; [contract] gates.
- **What is wrong:** [contract] names [tests] as Runtime's gates. No fixture observes invariant 3, 6, 8 or 9, or "no session works in the primary tree". resume-tick.sh:385 still passes `--dangerously-skip-permissions`.
- **Consequence:** Nothing stops a later launcher from re-adding the flag, or a session from opening in the primary tree.
- **Fix (judged SOUND by the skeptic):** Add a fixture for each guarantee. Invariant 8: a class check over every launcher that fails on `--dangerously-skip-permissions`, observed red against today's resume-tick.sh:385. Invariant 3: re-run the supervisor on a witnessed item and assert no dispatch. Invariant 6: a direct write to a record and to an instruction file, and a direct push to main, each refused. Invariant 9: each [policies] key has a reader, and each event class has a journal line. [isolate]: a session started in the primary tree is refused.
- **Gate:** A checklist entry: every invariant maps to at least one fixture that can fail on it.
- **Disposition:** new:claim-without-a-losing-fixture.

### M6. Invariant 3 forbids the re-entry routes the flow defines (MEDIUM)
- **Ids:** 8 MEDIUM.
- **Where:** [invariants] 3.
- **What is wrong:** The invariant says "a witnessed item never runs again" and has no notion of an item instance. flow-steps routes a failed check back to entry.place, a build.acceptance failure to a fix pass, and a HIGH finding to a follow-up review round. v2 records backward transitions and design re-entry.
- **Consequence:** A supervisor built to this invariant refuses legitimate re-entries, or the builder weakens the invariant silently.
- **Fix (judged SOUND by the skeptic):** Restate the invariant as "an item instance whose witness is current never runs again", keyed by item, round or pass, and input SHA. Note that a route back mints a new instance, and cite flow-steps' re-entry routes.
- **Gate:** A checklist entry: each invariant is checked against every backward route in the flow's step definitions.
- **Disposition:** class:two-answers-to-one-question.

### M7. "The executor" the siblings rely on has no carrier in Runtime's design (MEDIUM)
- **Ids:** 10 MEDIUM.
- **Where:** [design]; [supervise]; [act]; [settled].
- **What is wrong:** [settled] and v2 [owed] assign "the executor" to this layer, but [design] never uses the term. Runtime splits it into `next`, a supervisor and a headless "driver session". The siblings use "executor" for the actor that wraps, spawns, re-runs acceptance and queues commits, and "driver" for the main session.
- **Consequence:** Sibling statements about the executor (roles cycle step 3, build.acceptance "command: the executor", the lease-beat liveness) have no unambiguous carrier.
- **Fix (judged SOUND by the skeptic):** Add a term map to [design]. The executor is the supervisor for command items, the lease beat and launches. The executor's spawns are the driver session's role harness. The roles layer's "driver" is an attended session or a headless driver session. Name the sibling sentences each term maps.
- **Gate:** A checklist entry: every actor term a sibling assigns to a layer appears in that layer's design or in a term map.
- **Disposition:** new:sibling-statement-with-no-carrier.

### M8. Invariant 7 "fails closed" is false under allowed and default values (MEDIUM)
- **Ids:** 11 MEDIUM, 36 MEDIUM.
- **Where:** [invariants] 7; [enforce] Failing closed and "An out-of-agent escape"; [framing] row 5; [policies] runtime.hook-failure and runtime.below-floor.
- **What is wrong:** Invariant 7 says every enforcement rule fails closed, yet runtime.hook-failure=open and runtime.below-floor=degrade are allowed values. The record never mentions v2's hooks.bypass (default allowed) or core.bypass=with-hooks-report (owner-confirmed 2026-10-15), and both permit a git-hook bypass past the floor [enforce] relies on. It never mentions core.exceptions=any-session-recorded, whose register the Loop Review audits, and journals its own escape elsewhere.
- **Consequence:** A class check written to the invariant either reds a valid configuration or skips it. Self-exception and bypass have two answers.
- **Fix (judged SOUND by the skeptic):** Qualify invariant 7 ("under runtime.hook-failure=closed and hooks.bypass=refused"), or require a journaled witness for every fail-open setting or bypass, checked by the supervisor. State that the git-hook packs honour core.bypass=with-hooks-report, with its witness, so the invariant reads "fails closed, is excepted through the register, or has a witness behind its act". Record the out-of-agent escape as an entry in dOrderedCharter's exception register. Say whether narrowing a guard disable to owner-only is an explicit deviation, and why.
- **Gate:** A checklist entry: each invariant is read against every allowed value of the keys it governs.
- **Disposition:** class:two-answers-to-one-question.

### M9. Codex parity is asserted against events the returns do not show, and the harness lists are closed (MEDIUM)
- **Ids:** 13 MEDIUM, 21 MEDIUM.
- **Where:** [harness] "Codex wires hooks.json, whose events now match one for one"; [extend]; [invariants] 2 and 7; [policies] runtime.harnesses and runtime.scheduler.
- **What is wrong:** The sessions return lists only PreToolUse (Bash, apply_patch, MCP), SubagentStart, SubagentStop, PreCompact and SessionEnd for Codex. The dispatcher needs 11 events, including SessionStart, PostToolUse, Stop and PostCompact. Codex has no Workflow tool (unverified) and no evidenced `onFailure: "block"`, and its own docs call its hooks "not a complete enforcement boundary". runtime.harnesses and runtime.scheduler are closed value lists.
- **Consequence:** Under the opt-in claude-code-and-codex setting, card binding, act binding, the spawn guard and invariant 7 have no carrier on Codex. "A new harness ... is a filled contract. Runtime gains no code" cannot hold, because any new adapter means editing the policy schema.
- **Fix (judged SOUND by the skeptic):** Replace "match one for one" with a per-event table for each harness, built from the vendor docs, listing the floor for each missing event. Mark each invariant as held, witnessed or absent per harness. Make the spawn-backend and harness-adapter contracts carry spawning, so a Codex adapter supplies its own. Make runtime.harnesses and runtime.scheduler take the set of registered adapter names. Add to fixture 11 a check that a crashing Codex hook is refused, or record that it cannot be.
- **Gate:** A checklist entry: an extension point whose values are a closed list is flagged against any "gains no code" claim.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M10. The supervisor launches `claude -p` without saying which binary, and this node's PATH CLI is below the floor (MEDIUM)
- **Ids:** 18 MEDIUM.
- **Where:** [supervise] driver sessions launched headless; [enforce] cli-floor; [policies] runtime.cli-floor and runtime.below-floor.
- **What is wrong:** Drivers launch with `claude -p`, which resolves to the PATH CLI. On this node that CLI is 2.1.292, below the 2.1.295 floor, and only the desktop's bundled CLI meets it. The floor is checked only at session start, and the record never says which binary the supervisor resolves. [harness] records the CLI version in the node registry, which narrows the gap.
- **Consequence:** Every runtime-launched driver on this node is below the floor. Under RT-2, either no driver launches or every unattended driver runs with hooks failing open.
- **Fix:** The skeptic judged the proposed fix UNSOUND and gave no correction, so the fix is still to be designed. It must settle which `claude` binary the supervisor launches, and what happens before launch when none meets runtime.cli-floor.
- **Gate:** A checklist entry: every launched binary is named with its resolution rule, checked against the measured node facts.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M11. No fixture shows a Workflow run can complete inside a headless `claude -p` driver (MEDIUM)
- **Ids:** 19 MEDIUM.
- **Where:** [supervise] and [act], the driver running the role harness through Workflow `agent()` inside `claude -p`; [tests].
- **What is wrong:** All 64 measured sessions were desktop sessions, with 0 sdk-cli entrypoints. Workflow runs stop with their session unless backgrounded, and the only launcher sets `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`. The executor research's losing test for this path was dropped, and the record does not say whether the Workflow call is foreground or background.
- **Consequence:** If `-p` cannot host a Workflow run, or exits before it finishes, the spawn layer has no working path, and that is discovered only during the build.
- **Fix (judged SOUND by the skeptic):** Add a fixture ahead of the supervisor unit: a `claude -p --json-schema` driver runs one role-typed Workflow `agent()` to completion, SubagentStart and SubagentStop fire with agent_type, and the driver's structured_output carries the item return. State the call as foreground, or set the background-wait ceiling explicitly.
- **Gate:** A checklist entry: each load-bearing platform path the research did not measure has a fixture ordered before the units that rely on it.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M12. Nothing starts, keeps alive or restarts the supervisor (MEDIUM)
- **Ids:** 22 MEDIUM.
- **Where:** [supervise] "One supervisor runs per node"; [schedule] runtime.scheduler = node-task; [extend] host-adapter row.
- **What is wrong:** The supervisor is "a process, outside any session, no model", but no mechanism starts it, keeps it alive across a reboot or restarts it. A desktop scheduled task is a SKILL.md prompt that a model session runs. The [extend] host-adapter row names where it runs, not its lifecycle.
- **Consequence:** Cadence items and wake-ups pass through a model session, which contradicts deciding by program and invariant 5. A supervisor that dies between ticks is not restarted.
- **Fix (judged SOUND by the skeptic):** Add a host adapter that owns the supervisor's lifecycle, for example an OS-scheduled tick like resume-tick.sh's, with its registration checked by preflight. Make the node-task backend run the supervisor command directly, or state that cadence items whose work is a command never pass through a session.
- **Gate:** A checklist entry: every long-lived process names its starter, its keep-alive and its restart.
- **Disposition:** new:failure-path-left-undefined.

### M13. The `# Compact instructions` section rests on an unverified import and names no target or route (MEDIUM)
- **Ids:** 24 MEDIUM, 46 MEDIUM.
- **Where:** [sessions] "The instruction file gains `# Compact instructions`"; [current]; [tests] 9.
- **What is wrong:** Root CLAUDE.md holds only `@AGENTS.md`. The research marks it unverified whether a section reached through that import is honoured, yet the record states that it is. The record names no target file. AGENTS.md is the charter rendered from the template, under the charter-size and template-size legs, and no route through the instruction command is given, though invariant 6 requires one.
- **Consequence:** If the import is not honoured, compactions keep no card pointers or open asks, and gap-orient-14 is recorded fixed while it stands. A hand edit to AGENTS.md breaks invariant 6 and is overwritten at the next render, and a template edit ships the section to every adopter.
- **Fix (judged SOUND by the skeptic):** Name the target: either an instruction unit rendered into the charter, or root CLAUDE.md directly. Route the change through the instruction layer's manifest and the instruction command. Add to fixture 9: after a manual compaction, the summary names the build, the item and the open asks, including through `@AGENTS.md` if that is the target. If it fails, place the section in root CLAUDE.md.
- **Gate:** A checklist entry: a claim a research return marks unverified is not stated as fact without a fixture.
- **Disposition:** new:claim-outruns-measured-platform-fact.

### M14. Fixture 7 expects refusals from user-level guards the dispatcher does not wire (MEDIUM)
- **Ids:** 25 MEDIUM, 55 MEDIUM.
- **Where:** [tests] 7; [enforce] "One dispatcher entry per event" and failing closed.
- **What is wrong:** Fixture 7 expects "all 31" failures of the 2026-10-14 burst to be refused under `onFailure: "block"`. Part of the burst came from user-level python guards (git_dash_c_guard, exit 126, and msys_pathconv_guard), which are wired outside the repo and fail open. The dispatcher sets onFailure only on the repo's own entries.
- **Consequence:** The fixture cannot pass as worded, or it is quietly narrowed during the build. The node-local guards keep failing open under resource exhaustion.
- **Fix (judged SOUND by the skeptic):** Split the replay: every repo-wired enforcement entry in the burst must be refused. For user-level guards, either bring them under the floor rule (the class check reads every settings scope and requires `onFailure: block` on each enforcement entry, or a node-registry check does), or declare them outside Runtime's surface. Restate fixture 7 to match.
- **Gate:** A checklist entry: a fixture's expected population is checked against the scope the mechanism under test reaches.
- **Disposition:** new:fixture-scope-wider-than-mechanism.

### M15. "core.hooksPath becomes per-worktree" changes nothing and ignores the readers of its form (MEDIUM)
- **Ids:** 45 MEDIUM, 26 LOW.
- **Where:** [enforce] "core.hooksPath becomes per-worktree"; [isolate] the worktree's own hooks path.
- **What is wrong:** The value is already stored per worktree in config.worktree. The defect is that it is an absolute path to the primary tree, as [current] line 165 itself says. Three readers depend on its form: check-wiring.sh's Check H never overwrites a set value, run-gates.sh:4928-4931 (KF3) attributes pre-push edits only for a relative path, and pre-push:243,873 has rollout and straggler fallbacks written for an absolute path.
- **Consequence:** Done as worded, the change does nothing, and fixture 8 catches it only after the work. `check-wiring --fix` will not replace today's value. Once a real change lands, KF3 starts attributing pre-push edits, which changes the bar's red attribution with no leg named.
- **Fix (judged SOUND by the skeptic):** Reword it: the workspace allocator writes the relative `.githooks` into each new worktree's config.worktree, and the shared `.git/config` value becomes relative too (or name extensions.worktreeConfig with config.worktree as the mechanism). List check-wiring.sh (Check H :740-773, :615, :1947), run-gates.sh:4928-4931 and `.githooks/pre-push`:243,873 as touched. Add to fixture 8 a check that each worktree's own hook is reported effective.
- **Grades:** The binding grades are kept. Id 45 stands at MEDIUM for the KF3 attribution change, and id 26 at LOW for the wording alone.
- **Gate:** A checklist entry: a value change lists every reader that branches on the value's form.
- **Disposition:** class:retirement-inventory-misses-readers-by-value.

### M16. resume-tick.sh, the existing out-of-session resumer, is neither reused nor retired (MEDIUM)
- **Ids:** 28 MEDIUM, 43 MEDIUM.
- **Where:** [supervise] skip-permissions retired and the supervisor unit; [policies] runtime.relaunch=fresh; [schedule] in-session cron retired; [gaps-proposed] 8.
- **What is wrong:** resume-tick.sh is already the OS-scheduled, out-of-process resumer (gov-resume-tick, every 10 minutes). The record mentions it only to retire its `--dangerously-skip-permissions` launch. It never says what becomes of resume-tick.sh, whose mechanism is `--resume` and so contradicts runtime.relaunch=fresh. It never says what becomes of resume-tick.test.sh's arms that assert the flag (:368, :385), the unattended skill's CronCreate keepalive (SKILL.md:16, 130, 192), or stop-guard's session_crons. Gap 8 ("cadence runs only as in-session cron") misstates the tree.
- **Consequence:** A builder writes a second launcher next to the first, and two out-of-session actors relaunch the same stale run. The measured safeguards must be rediscovered. Removing the flag reds the AC1 arms, and the keepalive and stop-guard lose their purpose with no unit to retire them.
- **Fix (judged SOUND by the skeptic for id 43):** Name tools/unattended/resume-tick.sh as the seam the supervisor generalises. Keep its index-read lease, foreign-lease stand-off, login-before-kill order, kill-only-what-it-launched rule, RESUME_ATTEMPTS cap and run_detached. Move the launch to `--session-id` or fresh, with `--output-format json`, `--json-schema` and an allowlist. State that gov-resume-tick becomes the node-task scheduler backend. Rewrite gap 8: today's out-of-session scheduled actors are the resume tick, the desktop durable-restart task and the remote CI cron (read-only held bar), and no declared cadence item (Maintain detectors, Loop Review, sweeps) runs out of session. In [build], state resume-tick.sh's disposition and list resume-tick.test.sh:368,385, `.claude/skills/unattended/SKILL.md`:16,130,192 and stop-guard.js and its tests as touched. State whether stop-guard's block-while-run-open survives once drivers are one-act sessions.
- **Id 28's own fix:** Judged UNSOUND by the skeptic, with no correction, so it is still to be designed. The item's fix rests on id 43 alone. The note on id 28 quotes the same wording as id 43's fix; the report carries that wording only under id 43's sound judgement.
- **Twin:** Refuted id 61 (the flag's test consumers left unlisted) is part of this defect.
- **Gate:** A checklist entry: a retirement lists every test arm, skill line and hook that reads the retired value.
- **Disposition:** class:retirement-inventory-misses-readers-by-value.

### M17. runtime.fanout is a raisable second carrier of agent-cap's never-raisable ceiling (MEDIUM)
- **Ids:** 29 MEDIUM, 41 MEDIUM.
- **Where:** [policies] runtime.fanout; [supervise] "Agents in flight are counted under the lease".
- **What is wrong:** `runtime.fanout | an agent count | 5` is "switchable". agent-cap.js pins `CAP = 5` and `MAX_VERIFIERS = 5` as a ceiling that is never raised, which a repo may only lower through FANOUT_CAP in `.agent-cap.conf`. Parity rows (check-playbook-parity.sh:266-269), the restatement-waiver registry and `{{FANOUT_CAP}}` bind that number. The record names none of them.
- **Consequence:** The policy could set a count above 5 while agent-cap enforces min(FANOUT_CAP, 5). The two carriers drift silently, which is what check-agent-cap-restatement.sh exists to prevent.
- **Fix (judged SOUND by the skeptic):** Make runtime.fanout read and extend the existing carrier: the in-flight counter takes its bound from agent-cap's effective cap (lower-only, ceiling 5). Drop the literal default, or declare the key lower-only with the existing ceiling. Name agent-cap.js:61-72 and `.agent-cap.conf` in [supervise]. If the policy file becomes the carrier, re-point the parity rows and the waiver registry at it, render `{{FANOUT_CAP}}` from it, state whether `.agent-cap.conf` is retired, and update agent-cap.js's header in the same unit.
- **Gate:** Extend check-agent-cap-restatement.sh's scope to design records under `memory/builds/`, so a restated cap digit there reds.
- **Disposition:** class:two-answers-to-one-question.

### M18. runtime.reap duplicates PROCMON_REAP_MODE with a different value set and a default (MEDIUM)
- **Ids:** 30 MEDIUM, 42 MEDIUM.
- **Where:** [policies] runtime.reap; [supervise] "reaps orphans and stalls"; [current] Supervision reports and never reaps; [build] supervision unit.
- **What is wrong:** `runtime.reap` (orphans, orphans-and-idle, report; default orphans) duplicates process-monitor's PROCMON_REAP_MODE (report, reap-orphans, reap-all). The conf calls its default conditional. adopt-process-monitor.sh and reap.py refuse an unset key "because a defaulted kill policy is a policy nobody chose". orphans-and-idle is not a mode reap.py implements, reap-all disappears, and reap.py is never named as the reaper.
- **Consequence:** Two switches govern one irreversible act. Migrating the kit to the runtime values reds the "process-monitor wiring" leg. A runtime key that bypasses the conf could re-enable killing parentless desktop processes. The no-default principle is overturned silently.
- **Fix (judged SOUND by the skeptic):** Make runtime.reap the PROCMON_REAP_MODE key, read and written in `.process-monitor.conf`, with values mapped (orphans to reap-orphans, report to report, orphans-and-idle reconciled with reap-all). Alternatively, delete the key and cite PROCMON_REAP_MODE. Propose orphans-and-idle, if wanted, as a new mode through reap.py and classify.py. Keep the no-default rule or record why it is overturned. Name reap.py's leaves-first, read-back kill in the supervision unit, and list adopt-process-monitor.sh, reap.py and the conf as touched.
- **Gate:** A checklist entry: a new policy key is grepped against every kit conf key for the same switch.
- **Disposition:** class:two-answers-to-one-question.

### M19. The subagent-stop return check has two builders (MEDIUM)
- **Ids:** 32 MEDIUM.
- **Where:** [spawn] returns persisted and validated by a SubagentStop hook; [build] unit "the role harness's durable returns (the subagent-stop hook)".
- **What is wrong:** roles.md:264 and v2:705 give the subagent-stop return check and gap-roles-04 to dBoundRoles, and Runtime's own [settled] and [gaps-proposed] keep that owner. Yet [build] lists the hook as a dWellOiledMachine unit and [spawn] redesigns it.
- **Consequence:** One hook has two builders and two writers.
- **Fix (judged SOUND by the skeptic):** Remove the hook from dWellOiledMachine's units, and state that Runtime runs dBoundRoles' check through its dispatcher as a roles pack. Alternatively, move gap-roles-04 into the "Gaps it would take" table and re-point the roles round.
- **Gate:** A checklist entry: every [build] unit is checked against the owner column of the gap it closes.
- **Disposition:** class:two-answers-to-one-question.

### M20. Hook packs ignore the existing fragment seam and v2's hook factory (MEDIUM)
- **Ids:** 33 MEDIUM.
- **Where:** [enforce] dispatcher and packs; [extend] hook packs row.
- **What is wrong:** The existing seam is the 12 per-kit `*.fragment.json` files, merged by settings-merge.py and read by check-wiring.sh's fragment reader. v2 gives the hook factory and its conformance gate to dDeclaredLoop. The record cites neither.
- **Consequence:** Packs become a second registry. The fragment reader, settings-merge and check-hook-destinations then grade entries that no longer carry the rules, and "Runtime gains no code" cannot hold.
- **Fix (judged SOUND by the skeptic):** A hook pack is a fragment with added fields: owner, decision class, failure mode, latency budget and policy key. settings-merge.py renders one dispatcher entry per event from the fragments. The fails-closed class check is a new arm of check-wiring.sh over the same reader. The pack factory is v2's dDeclaredLoop hook factory.
- **Gate:** A checklist entry: a new registry in a design names the existing seam it extends or retires.
- **Disposition:** new:existing-seam-unnamed.

### M21. The dispatcher's event list drops StopFailure and leaves live hooks with no pack (MEDIUM)
- **Ids:** 34 MEDIUM, 39 MEDIUM.
- **Where:** [enforce] "One dispatcher entry per event" event list and pack list; [spawn] "A session limit defers the item"; [tests] 4.
- **What is wrong:** The event list omits StopFailure, which `.claude/settings.json:100` wires for stall-recorder.js, the existing seam that records API-limit stalls for `--liveness`. The limit-deferral design names no limit signal. The pack list assigns no pack to format-guard, gate-guard, stop-guard, stall-recorder, procmon-hook and procmon-session, recall-opened, or check-wiring's session entry.
- **Consequence:** Consolidating into the listed dispatchers drops stall recording. Live guards and recorders are orphaned, or their placement is invented. The supervisor's hold is built on a new limit detector while the existing `last-stall:` line goes unused.
- **Fix (judged SOUND by the skeptic):** Add StopFailure as a record-class entry, and UserPromptSubmit if agent-cap's per-prompt keying needs it. Name stall-recorder.js and its `stall.<slug>.log` as the limit signal the supervisor reads to defer and hold, and drive that path in fixture 4. Add an [enforce] table mapping every current settings.json entry to a pack and an owner (for example hooks kit: scratch-guard, format-guard, agent-cap; unattended: gate-guard, stop-guard, stall-recorder; process-monitor: procmon; memory-recall: recall-opened; session-kickoff: the card). Gate that table against settings.json.
- **Gate:** The table-against-settings.json check the fix names.
- **Disposition:** class:retirement-inventory-misses-readers-by-value.

### M22. The "one deferral factory" is specified as new beside an existing shape and consumer (MEDIUM)
- **Ids:** 35 MEDIUM, 44 MEDIUM.
- **Where:** [spawn] "One deferral factory" and "role agents stay write-less".
- **What is wrong:** tier2-review.js:1243, 1268, 1596 and 1630 already return `{exit:'deferred-platform', key, pending, durable}`. unattended-build.js:1657 consumes that shape and holds with `--code platform-limit`, and VERBS.template.md and STOPS.template.md consume it too. The Workflow runtime injects only fixed globals, so "shared" cannot be an import. tier2-review, its template and its test carry DURABILITY Write instructions, and drift-audit-code.js:90 makes the agent's writeup its durability control. The committed:false carriers are not listed for the null-to-deferred change.
- **Consequence:** A factory built to a different shape breaks the existing consumer or forks a second deferral shape. "Write-less" contradicts today's harnesses.
- **Fix (judged SOUND by the skeptic):** State that the factory is tier2-review's deferred-platform exit, extended to unattended-unit.js's null path. Share it as a byte-identical copy under a parity gate, and keep the unattended-build.js consumer as its contract. In [build], list every DURABILITY writer and every committed:false and deferred-platform carrier, with the test arms that change.
- **Gate:** A checklist entry: a "new" shared shape is grepped for an existing return of the same name first.
- **Disposition:** new:existing-seam-unnamed.

### M23. Driver relaunch is uncapped (MEDIUM)
- **Ids:** 52 MEDIUM.
- **Where:** [supervise] Relaunch; [spawn] "exit 2 holds an agent whose return fails"; [policies].
- **What is wrong:** Return retries are capped by reference to roles.retries. Driver relaunch is uncapped, and invariant 3 keeps an unwitnessed item always re-dispatchable. Today's launcher stops at RESUME_ATTEMPTS (6).
- **Consequence:** An item that crashes its driver every time is relaunched without end and burns session and weekly limits.
- **Fix (judged SOUND by the skeptic):** Add `runtime.relaunch-cap`, and take the return-retry cap from roles.retries or a new key. Past the cap, the item becomes a parked outcome with a journaled reason. Add a fixture: a stub driver that always exits non-zero must park after N launches.
- **Gate:** A checklist entry: every retry or relaunch loop names its cap and its terminal outcome.
- **Disposition:** new:failure-path-left-undefined.

### M24. A session-level `--json-schema` cannot fit a driver that lives one build (MEDIUM)
- **Ids:** 53 MEDIUM.
- **Where:** [supervise] driver launch flags; [act] Lifetime; [policies] runtime.driver-lifetime=build.
- **What is wrong:** `--json-schema` is fixed once per launch and set to "the item's return schema". The default driver lives one build and serves items with different schemas, and the [spawn] fallback leans on that session-level schema.
- **Consequence:** The session-level schema fits at most one item. Every other act's output is unconstrained or forced into the wrong shape.
- **Fix (judged SOUND by the skeptic):** Choose one: either the session schema is an act-envelope schema shared by every act, with item schemas enforced only at the role harness, or the default lifetime becomes `item`. State which in [supervise] and [act].
- **Gate:** A checklist entry: a per-launch setting is checked against the lifetime of the session it is set on.
- **Disposition:** class:two-answers-to-one-question.

### M25. Git-hook witnesses other than push have no reader (MEDIUM)
- **Ids:** 56 MEDIUM.
- **Where:** [enforce] "a witness record stands behind the act: Stop, SubagentStop and every git hook. The supervisor trusts the witness".
- **What is wrong:** Only push has a reader: push-main reads the allow record. For pre-commit, commit-msg and pre-rebase, the record names no consumer and no point at which the witness is checked, and drivers, not the supervisor, make the commits.
- **Consequence:** A pre-commit killed by TerminateProcess still lands a commit, and nothing reads the missing witness. The full bar on a default-branch push contains the damage.
- **Fix (judged SOUND by the skeptic):** Name the reader of each git-hook witness. For example, `next` treats a commit without a pre-commit witness as an unwitnessed item, or the lander refuses a range that holds one. Add a fixture that kills pre-commit with SIGKILL and asserts the refusal.
- **Gate:** A checklist entry: every witness a design writes names its reader.
- **Disposition:** new:witness-without-a-reader.

### M26. `next` has no output for an empty, non-terminal frontier or an unreadable input (MEDIUM)
- **Ids:** 57 MEDIUM.
- **Where:** [decide] One derivation; [supervise] "reaps orphans and stalls".
- **What is wrong:** `next` returns nothing defined for an empty, non-terminal frontier, which is the measured BUILDING-with-all-work-terminal stall of aClosedDocket and aUnblockedFleet. It also returns nothing defined for an unreadable declaration, witness or policy file. "Stalls" is never defined.
- **Consequence:** The supervisor idles under a live lease, reproducing the stranded runs, or crashes on every tick.
- **Fix (judged SOUND by the skeptic):** Add two outputs to `next`'s contract. "Stuck: no frontier, build not closed" raises an owner item. "Invalid declaration" refuses and journals the parse error with its path. Define a stall as either output persisting past a bound, and add a fixture for each.
- **Gate:** A checklist entry: a derivation's contract lists its output for empty and unreadable inputs.
- **Disposition:** new:failure-path-left-undefined.

### M27. Act binding does not reach Bash, where the ad-hoc scripts ran (MEDIUM)
- **Ids:** 58 MEDIUM.
- **Where:** [act] act-binding rule; [tests] 2.
- **What is wrong:** Act binding covers only "any spawn, Workflow call or transition". The 25+ ad-hoc scripts gap 1 cites ran through Bash, and the permission allowlist is not tied to the named act.
- **Consequence:** A driver can still improvise through scripts, gap 1 stays open, and fixture 2 cannot see it.
- **Fix (judged SOUND by the skeptic):** Extend act binding to Bash and PowerShell commands that the named act's allowance does not cover, or state Bash improvisation as an explicit non-goal and drop the scripts from gap 1's evidence. Have fixture 2 replay the transcripts' tool calls (see H2).
- **Gate:** A checklist entry: a cure's scope is checked against every evidence line of the gap it claims to close.
- **Disposition:** new:cure-covers-part-of-its-class.

### M28. The SubagentStop hook writes return records outside `record`, contradicting invariant 6 (MEDIUM)
- **Ids:** 59 MEDIUM.
- **Where:** [spawn] SubagentStop writes returns "under the run's area"; [invariants] 6; [contract] record kinds.
- **What is wrong:** "Return records" are a record kind, and invariant 6 says records change only through `record`. Yet the hook writes model-controlled content to disk directly, with no path, size cap or encoding rule.
- **Consequence:** Either invariant 6 is false for the most frequent record write, or the route through `record` has no contract. An oversized or non-UTF-8 return lands unvalidated.
- **Fix (judged SOUND by the skeptic):** The hook writes through `record` under the return-record kind, with a byte cap and a schema check before the write. Alternatively, exempt return records from invariant 6 and name their path and size bound in [spawn].
- **Gate:** A checklist entry: every write path in a design is traced to the record route its invariants require.
- **Disposition:** class:two-answers-to-one-question.

### L1. The driver-lifetime default rests on an unmeasured turn distance (LOW)
- **Ids:** 23 LOW.
- **Where:** [act] Lifetime; [policies] runtime.driver-lifetime = build.
- **What is wrong:** The default rests on "below the 1,000-turn compaction distance", but compaction triggers on tokens (median 969,959). The research picked S2, a fresh driver per item, and the record does not say why it departs from that pick.
- **Consequence:** The justification is unmeasured. The skeptic graded it low because the threshold relaunch already covers mid-build compaction.
- **Fix (judged SOUND by the skeptic):** Default to `item`, as the research picked, or add a fixture that measures driver tokens per act on a replayed build and asserts that a build's total stays under context.threshold.
- **Gate:** A checklist entry: a default that departs from the research's pick states why.
- **Disposition:** new:claim-without-a-losing-fixture.

### L2. The dispatcher's 57 ms latency budget is never measured (LOW)
- **Ids:** 27 LOW.
- **Where:** [enforce] "to stay within the 57 ms that one guard costs today".
- **What is wrong:** The research projects about 85 ms in-process unless rules load lazily, and no fixture measures the dispatcher.
- **Consequence:** A dispatcher slower than today passes unnoticed. The effect is limited to performance.
- **Fix (judged SOUND by the skeptic):** Add a fixture: 10 runs of the dispatcher on a benign Bash payload, with the p50 compared against 57 ms.
- **Gate:** The fixture the fix names.
- **Disposition:** new:claim-without-a-losing-fixture.

### L3. The limit hold does not say how the reset is learned or whether the lease is kept (LOW)
- **Ids:** 60 LOW.
- **Where:** [spawn] "A session limit defers the item, the supervisor holds until the reset".
- **What is wrong:** The record does not say how the reset time is learned, whether the lease is renewed during the hold, or what happens on a weekly limit of up to 7 days.
- **Consequence:** A lapsed lease hands the build to another node, which hits the same limit. Otherwise the build is pinned with no owner signal. Either way the run is delayed and no result is lost.
- **Fix (judged SOUND by the skeptic):** The supervisor parses the reset time from the limit message, keeps renewing the lease, and raises an owner item when the hold exceeds a policy bound. Add both cases to fixture 4.
- **Gate:** A checklist entry: every hold names its wake signal, its lease behaviour and its bound.
- **Disposition:** new:failure-path-left-undefined.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=61 confirmed=57 refuted=2 merged=2 unverified=0 blocker=0 high=9 medium=44 low=4 agents=11 out-tokens=unknown
## Appendix

The harness's appendix text did not arrive. The rendered prompt opens its appendix marker and never closes it, so there is nothing to copy here verbatim. Each confirmed id's disposition is on its item above and in the returned `dispositions`.
````
