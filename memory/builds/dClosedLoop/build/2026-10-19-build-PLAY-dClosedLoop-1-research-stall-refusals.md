# Research: every refusal, and whether its target can act on it

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 144's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-19-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md`.

---

**The refusals: what each refuses, whether its target can act on it, and what happens on a repeat**

I wrote nothing in the repository. My probe scripts lived in the session scratchpad and are deleted; `git status` shows no change of mine. Code cites are at the worktree HEAD `d56d7da4d`, and records are cited as `<record> [<tag>]`. The records live under `memory/builds/dClosedLoop/build/` and are abbreviated: v2 = `...-architecture-v2.md`, FS = `...-flow-steps.md`, RT = `...-layer-runtime.md`, RL = `...-layer-roles.md`, IN = `...-layer-instruction.md`, MEM = `...-layer-memory.md`, SYS = `...-systems.md`, FRA = `...-flow-roles-adoption.md`, NP2 = `...-night-pass-two.md`.

"Actionable" means the refused actor can perform the named remedy within its own allowance and grant. "On repeat" means what the code or record does when the same refusal fires again.

## 1. Inventory

### Today's tree

| id | where | refuses whom | says what | actionable | on repeat | cycle partner |
|---|---|---|---|---|---|---|
| T1 | `tools/hooks/scratch-guard.js:540-560`, `:1580-1583` | any session or agent; subagents included | the write lands outside a sanctioned scratch root; lists the roots | yes | nothing counted | — |
| T2 | `scratch-guard.js:733-744`, `:758-790` | the main loop's `git commit`; subagents are exempt (`:763`) | the card holds the READY sentinel or names another tree; run `/session-kickoff` | yes | nothing counted | — |
| T3 | `scratch-guard.js:1122`, `:1126`, `:1152` | any writer | the payload has no target or cwd, or the conf can't be read; refuses (fails closed) | no (harness payload or filesystem) | nothing counted | — |
| T4 | `scratch-guard.js:1160` | every Edit or Write except to the conf | write gate UNARMED; fix `.memory-tree.conf` | yes (the conf write is admitted) | nothing counted | — |
| T5 | `scratch-guard.js:1183`, `:1188`, `:1200`; reasons at `:901-909` | main loop and subagents alike (no `agent_id` exemption, `:1111`) | no card, no route, or no buildable unit; run `/session-kickoff`; a Tier-2 unit admits writes "at INPROGRESS, which follows the owner's scope approval" | depends. Main loop: yes. Subagent: no, it cannot kick off the parent's card. The Tier-2 flip is admitted from the main loop even without owner approval (`:88-89`, `:1075-1083`), so the remedy names a step the protocol withholds | nothing counted | T6 (kickoff writes a spec, which meets the role arm) |
| T6 | `scratch-guard.js:1064-1085`; remedy text `:1045` | main loop, builder, untyped `workflow-subagent` | only the spec writer may write the spec class; "render that role's handoff … and pass the output as the prompt of an Agent call" | depends. Main loop: yes. Role agent: no, the remedy is a spawn it cannot make. Record and code disagree here: RL `[trust]` and v2 P25/P26 say workers never spawn or message each other | nothing counted | T5; A3 (the spawn the remedy needs) |
| T7 | `scratch-guard.js:1068`, `:1072` | every spec and product writer | role index broken ("re-render it") or UNARMED for the class | depends. Main loop: yes, by a Bash re-render. Role agent: no, since a broken index also refuses its scripts (`:1439`) | nothing counted | T8, A3 |
| T8 | `scratch-guard.js:1381-1388`, `:1421-1451`; a throw refuses (`:1604`) | role agents only | "a role agent runs no gate … return the need in your result, and verify your change with a fixture or a probe" | yes as a redirect, but the role cannot run a check it is asked to observe, so the result becomes a claim | nothing counted | G1 |
| T9 | `scratch-guard.js:1536-1546` | nobody: the SubagentStart context never blocks | — | — | — | — |
| A1 | `tools/hooks/agent-cap.js:2244-2255` | every Agent and Workflow call | `AGENT_CAP` is set; "Unset AGENT_CAP and re-run" | no: the hook's environment is the operator's | every call refused, nothing counted | — |
| A2 | `agent-cap.js:2261-2264` | every spawner | `FANOUT_CAP` malformed; fix or remove it | yes (main loop) | nothing counted | — |
| A3 | `agent-cap.js:2088-2148` (Agent), `:2157-2187` (Workflow), `:2280-2294` | the spawning session | rule 6: prompt, marker, task-sha or description mismatch; or an undeclared harness or `args.roles` | yes, except an adopter install where `roles.json` names harnesses that aren't installed, so the guard refuses gov's own `tier2-review.js` (FRA `[today]`, `gap-roles-25`): no | nothing counted | T6 |
| A4 | `agent-cap.js:1740-1751` | direct Agent spawner | budget exhausted; "a new user prompt resets the budget, and a slot idle longer than 45 minutes is reclaimed" | depends: the remedy is time or a new prompt, which an unattended agent cannot produce | nothing counted | — |
| A5 | `agent-cap.js:1730-1734` | direct spawner | the slot token cannot be created | no | nothing counted | — |
| A6 | `agent-cap.js:1895-1903` | Workflow `kind: spec-audit` | the opt-in is the owner's README key or `SPEC_AUDIT_DEFAULT` | no for an agent in an `authorized-by: prompt` or recipe README | nothing counted | — |
| A7 | `agent-cap.js:2325-2421` | script author | fan-out, unresolvable bound, raw `parallel`/`pipeline`, ref-keyed join | yes (rewrite the script) | nothing counted | — |
| F1 | `tools/hooks/format-guard.js:466-545`; remedy `:460` | main loop at turn end, routed build | resend the final message with the BUILD/SPEC pair and commit lines | yes | at most once per turn end (`stop_hook_active`, `:469`) | S1 (shared stop chain) |
| S1 | `tools/unattended/stop-guard.js:141-157`, `:160-175` | the main session holding an unattended run | run `--plan` and build, or `--abort`; or `--landed`; "Never end the turn by asking" | yes (`--abort` is always open) | counted: lifetime cap `STOP_GUARD_BLOCKS` 6 (`:89`; `.unattended.conf:84`), then allowed as `blocks-exhausted`; the harness stops after 8 consecutive (`:85`) | Q1 |
| Q1 | `tools/unattended/gate-guard.js:739-757` | `AskUserQuestion` from a lease holder | decide it, or `unattended.sh --park`; or `--landed` | yes, unless the driver cannot run: an unreadable liveness keeps the deny (header, "ONE input does not allow"), and `--park` needs the same driver | nothing counted | S1, which allows the stop on `liveness-unreadable`, so the session ends with the question unasked |
| G1 | `gate-guard.js:669-681` | anyone on the run's branch, sidechains included | flagged bar or self-test suites before VERIFYING; "observed by the direct check its spec names" | yes | nothing counted | T8 |
| SR | `tools/unattended/stall-recorder.js:13-15` | nobody: records, cannot block | — | — | no counter, no ceiling (see section 2.2) | — |
| H1 | `.githooks/pre-commit:10-14` | committer | work tree unresolvable; `--no-verify` | yes | nothing counted | — |
| H2 | `pre-commit:80-85` | committer in the primary tree off the default branch | use a sibling worktree | yes | nothing counted | — |
| H3 | `pre-commit:107-121` | committer staging a straggler shard | relocation recipe | yes | nothing counted | — |
| H4 | `pre-commit:185-258`, `:262` | committer | "a gate failed — fix or `git commit --no-verify`" | depends: a size cap's raise is the owner's (NP2 `[p5-caps]`); `--no-verify` is allowed (`hooks.bypass: allowed`) | nothing counted | — |
| H5 | `.githooks/commit-msg:56-61`; `unattended.sh:13340-13400` (check 49) | committer in a run-bound worktree | add a `Pass:` trailer, or `--dispatch … --writes` | yes | nothing counted | — |
| H6 | `commit-msg:104` | merge concluder | transition audit (merges only) | yes | nothing counted | — |
| H7 | `.githooks/pre-rebase:57-65` | rebaser | relocation recipe, or `--no-verify` | yes | nothing counted | — |
| H8 | `.githooks/pre-push:76`, `:573-594`, `:646`, `:913`, `:961`, `:1077-1144`, `:1156`, `:1200-1232`, `:1878`, `:2376-2387` | pusher | default branch, declared bar, manifest, raw push, HEAD mismatch, dirty tree, merge loss, straggler, gate RED, HEAD moved, signal ("Push again") | mostly yes; a gate RED from another unit's work depends | per push nothing; the lander retries 3 times (`tools/push-main.sh:188`, `:952-1005`), then "moving faster than the gate" | — |
| D1 | `tools/unattended/unattended.sh:793` (`fail()`): 325 fail sites, 113 distinct checks | the run's session | per check, e.g. check 2 dirty tree, 8 keepalive id ("only the agent can do it"), 13 DoD unmet at `--close` | mostly yes. Check 8 depends on the harness offering a cron tool. Check 2 depends on whether another session's writes dirtied a shared tree | per verb nothing; run-level bounds: `RUNAWAY_CEILING` 8 (`:774`), `REVIEW_ROUNDS` below it (`:783`), `RESUME_ATTEMPTS` 6 (`.unattended.conf:98`) | — |

### The v2 design

| id | where | refuses whom | says what | actionable | on repeat | cycle partner |
|---|---|---|---|---|---|---|
| V1 | FS `[rules]`; v2 `[chain]` dDeclaredLoop "a default failure route" | any item's actor | "the refusal recorded, `next` returning the frontier" | depends on the refusal routed | **unstated**: the frontier re-offers the same item; RT `[decide]` lists route backs (failed entry check, fix pass, review round, backward transition) without a re-offered refusal, so `flow.route-backs` may not count it (ambiguous) | itself |
| V2 | FS `[transitions]`; RT `[decide]` `invalid-input` | engine / supervisor | undeclared transition; malformed declaration, policy value or witness | no (a declaration defect) | "refuses to act, and journals it": no owner item, no count, so it repeats every beat (unlike `stuck`, which raises an owner item at once) | — |
| V3 | FS `[entry]` `entry.place-check`; `placement.check: refuse` | requester / scout | "the request returned with the refusal" | yes | the route back counts "in the build's transition record" (FS `[rules]`), which does not exist before `entry.claim`, so it can't be counted (ambiguous) | — |
| V4 | v2 `[policies]` `leases` refuse (strict, guarded); FS `plan.lease`, `build.unit-lease` | driver | lease held: "refused → as `leases` says" | no (another build's live lease) | no ceiling stated. RT `[decide]` `blocked` raises an owner item only "once nothing the item waits on is in flight", and `leases.renewal: activity` keeps a live but looping holder renewed | another build's own loop |
| V5 | `leases.offline` refuse / `follow-leases` | driver | remote unreachable | no (network) | `stale-remote`: holds, retries, parks at `leases.expiry-hours` | — |
| V6 | FS `[build]` `build.scope` refuse (strict) | builder | stray path; revert pass | yes | revert pass counting unstated (ambiguous) | — |
| V7 | v2 `[chain]` dScopedBuild; FS `build.core` | driver / builder | exit refused while the build's own core red stands | depends: a fix unit, or `core.exceptions` (any session under standard; owner only under strict) | the fix unit is a counted route back | — |
| V8 | FS `[test]` `test.route` | tester / driver | CONTENDED: re-run on a quiet host. DEAD PROBE: "the probe repaired, or an owner exception". INHERITED: fix unit or exception | INHERITED and CONTENDED: no (another unit, the host). DEAD PROBE: no actor named | flake re-entries are counted; the CONTENDED re-run's count is unstated | — |
| V9 | FS `[test]` "a fix pass keeps its check" | builder | test files and gate script excluded from a fix pass's allowance | yes, through the tester's judgment and a new Design unit | counted | — |
| V10 | v2 `[presets]` `hooks.bypass: refused` (strict, guarded) | any committer | — | no while the gates are unreliable: v2 itself says "choosing either one will stall on the same gate problems" | nothing counted | H4, H8 |
| V11 | FS `[deploy]` `deploy.land`, `deploy.core` | lander command | refused before the push goes to Test; REFUSED bar | yes | REFUSED: one re-run after a fetch, then an owner item; unreachable remote: retry, then an owner item | — |
| V12 | FS `[lifecycle]` `life.quiesce` | owner | pause or withdraw after the push is refused | yes (the alternative is stated) | — | — |
| V13 | RT `[act]` act binding, epoch, shell allowance; SYS `[design-role-shapes]` shape digest; verifier stage writing its own artifact | the act session's agent | unnamed call, stale epoch, or roles/efforts/fan differing from the digest | no: only `next` names acts, and the digest comes from the render | death relaunches stop at `RESUME_ATTEMPTS`; whether a returned refusal counts is unstated; stale epoch: the supervisor kills the session | stale composition |
| V14 | RT `[enforce]` dead dispatcher; `[act]` crashed SessionStart | act agent | every gated call denied, the exception record included | no | "repair … outside the agent: from the owner's terminal, or by the supervisor parking the run" | — |
| V15 | RT `[enforce]` / `[supervise]` preflight | supervisor / operator | allow rule or second permission hook, unregistered run host, act in the primary tree | no for the supervisor | whether the supervisor parks or raises an owner item is unstated | — |
| V16 | v2 `runtime.agents-in-flight`; NP2 `[p7-agent-cap]` | spawner | until the queue arms, a direct spawn over the limit is refused with the harness's "Do not retry" | depends: the remedy is waiting; NT-28's queue turns it into a wait once armed | — | — |
| V17 | RL `[trust]` R3-C; v2 `[chain]` dBoundRoles | prompt writer / driver | spawn guard; under `cold` verifier context, a packet carrying the author's reasoning; harness admission compared with its landed blob | yes, except an in-build harness edit, which waits for landing | nothing counted | — |
| V18 | RT `[spawn]`; NP2 `[p4-handoffs]` | role agent | failing or per-order return schema | yes | counted: `roles.retries` 3, then "persisted as a refusal and routed by the item's outcome table", which leads to V1 | V1 |
| V19 | RL `[trust]` 10; `roles.answered-calls` refuse | role agent | the read is already handed; "name the anchor" | yes (partial-overlap reads run) | recorded as a metric, not escalated | — |
| V20 | v2 P27; IN `[load]` lines 460-468; NP2 `[p5-caps]`; `budgets.pinned` | prompt writer / renderer | load set missing a required unit; over the harness's own limit; over a pinned cap | no: a missing unit is a declaration defect, a cap raise is a policy write, a harness limit is fixed | "A refusal leaves the spawn undone, and the caller files an ask", then V1; only the over-budget demote-then-split route back is counted (RL `[trust]` 1) | V27 |
| V21 | v2 P30; MEM `[contract]` | any writer | the `record` command refuses an invalid value; unknown README keys | yes | — | — |
| V22 | MEM `[asks]`; `asks.acceptance` refuse | filer | "returns to the filer with the forms" | yes | "routes as any refusal does", which is V1 | V1 |
| V23 | v2 dPlacedRequest, dKeptSession; NP2 `[p4-handoffs]` | session | create-only register: a second decision or a duplicate message is refused | yes ("reads the first") | terminal, no loop | — |
| V24 | v2 `lexicon.at-commit` refuse, `lexicon.drift` refuse-new | committer | name drift | depends: renaming is yes; a contract-forced name missing from its table needs `instructions.edit` (owner command, agents propose): no | nothing counted | V27 |
| V25 | v2 `tags.retired-cites`, `tags.positional`, `instructions.legacy`; SYS `[design-instruction-writing]` render gate | committer | retired cite, positional reference, legacy doc only shrinks, hand edit of a render | depends: adding guidance to a legacy doc needs owner-written units | nothing counted | V27 |
| V26 | NP2 `[p1-scenarios]` 7; `flow.scenario-conflict` refuse | placement / driver | two scenarios set one field: "red at composition and wait for the owner" | no | becomes the `blocked` owner item; whether `run.on-owner-question` resolves it is unstated | — |
| V27 | v2 `[witnesses]`, dGroundRules guard | every agent | writes to the policy file, its mirror, `instructions.toml` and `deploy.toml` refused; owner TTY proof | no | — | V20, V24, V25, V28 |
| V28 | v2 `[chain]` dGroundRules, `policy-file.on-invalid` | lander / pusher | with no valid revision, "the push and landing gates refusing and naming the line" | no: the fix is a V27 write | no owner item stated | V27 |
| V29 | FRA `[design]` 4-6, 9, 11, 13; `instructions.stale` refuse | overlay author (owner) | fixed-row patch, widening or exclusion refused; composition red at push; update held | yes (owner) | an adopter's update is stalled, not a build | — |
| V30 | v2 `design.overlap` refuse, `plan.unplaced` refuse-new | architect / planner | overlap with another build; unplanned work | no / owner | no ceiling stated | V4 |
| V31 | FS `[breakpoint]` `review.unclassed`, `review.unverified`; FS `[probe]` | synthesizer / skeptic | unclassed finding; unverified finding; probe claimed or unrunnable | yes | counted within `flow.route-backs`, then an owner item | — |
| V32 | v2 `[chain]` dWellOiledMachine: "a hook pack's refusal text, naming its rule and its remedy, declared in the pack's contract and checked at registration" | the contract over every pack | — | — | no clause checks that the remedy lies within the refused actor's grant | all of the above |
| V33 | grouped: `retrofit.unseeded`, `commits.squash`, `install.on-shim-call`, `maintain.reading-admission`, `platforms.provision`, the wrong-shell refusal (AP-33), dSafePassage's step gate, dFairHearing's partial-population scorer, dLinkedLibrary's missing-clone refusal | operator / adopter / owner | adoption- and operator-level | mostly owner or operator; the missing clone: no | — | — |

## 2. Measured counts

Everything here was read-only.

### 2.1 Stop-guard sidecars

Command: a Python tally of `decision`/`reason` per session over `C:/projects/coding-governance/.git/worktrees/*/unattended/stop.*.log`.

- 8 run sidecars hold 184 stops and 5 blocks (`run-open` ×3, `landing-unstamped` ×2).
- The most blocks in a row for any session was 1.
- No run reached `blocks-exhausted`.
- Every run ended `terminal` (LANDING or LANDED).

### 2.2 Stall recorder

Command: `awk '{print $3}' .git/worktrees/build-readme-governance-18d6ea/unattended/stall.dDerivedDocket.log | sort | uniq -c`

```
112 rate_limit
  3 server_error
```

- All 115 lines come from one session, `2588f719`, between 2026-09-22 and 2026-09-29.
- They cluster at :04/:14/:24/:34/:44/:54 past the hour, so a 10-minute tick kept firing into the limit with no counter or ceiling.
- This is a retry loop, not a refusal; it belongs to the census and history questions.

### 2.3 Driver run log

Command: a Python pass over the tab-separated `k=v` lines of `.git/runlog/driver.log`, keeping `ev=end` lines.

- 981 verb ends: 895 `rc=0`, 85 `rc=1`, 1 `rc=2`.
- Top refusals: `--dispatch` check 49 ×26, `--review` 37 ×11, `--close` 13 ×11 (plus 3 more where check 13 fired more than once), `--dispatch` 14 ×10, `--check-commit` 49 ×5.
- Same verb and same check refused twice in a row, per slug: 5 pairs (`--review` 37 ×2, `--dispatch` 49, `--check-commit` 49, `--preflight` 4). Each was followed by an admitted call of the same verb.
- `.git/runlog/pushes.log` decisions: 110 `skip-nondefault`, 12 `full`, 9 `scoped`, 1 `covered`.

### 2.4 Transcripts

The corpus is 4,162 `.jsonl` files under `C:/Users/d41ly/.claude/projects/C--projects-coding-governance*` (4,095 of them subagent files). The scanner:

- read each `tool_result` with `is_error` matching `^PreToolUse:<tool> hook error: [<script>]: …`;
- read each `user` record starting `Stop hook feedback:`;
- counted git-hook refusal lines (`^(pre-push|pre-commit|pre-rebase|commit-msg): (REFUSING|refusing|gate RED|branch bar RED|a gate failed…)`) only on Bash calls running `git commit|push|rebase` or push-main;
- counted driver `^UNATTENDED check N FAILED` only on calls of `unattended.sh --<verb>`;
- excluded commands naming a temp, scratch, fixture or `.test.sh` path.

A first, unfiltered pass counted 500 driver events. Most of those were reviewers deliberately running `check-unattended.sh`, which prints the same prefix, so the filtered numbers below are the ones to use.

**Refusals by guard (events / transcripts):**

| Guard | Events | Transcripts | Breakdown |
|---|---|---|---|
| scratch-guard | 197 | 166 | scratch 131 (123 under `/tmp`, 112 of them in subagents); role-gate 30, all in subagents; write-gate route 13; role arm 12, all subagent builders; orientation 11 |
| driver | 129 | 57 | — |
| pre-commit | 93 | 36 | — |
| agent-cap | 48 | 22 | fan-out/bound/raw 28; rule 6 15; spec-audit 3; spawn budget 2 |
| `msys_pathconv_guard.py` | 34 | 33 | a node-level guard, outside gov's surface |
| gate-guard | 19 | 17 | — |
| pre-push | 16 | 14 | gate RED 10; raw push 5 |
| format-guard | 14 | 2 | — |
| stop-guard | 5 | 4 | — |

The harness's "Do not retry" on Agent did not appear.

**Same refusal twice or more in a row** (consecutive tool results, same guard and rule):

| Guard and rule | Streaks | Longest | How it ended |
|---|---|---|---|
| scratch-guard role arm (builder writing specs) | 2 | **10** | see below |
| scratch-guard write-gate route | 1 | 3 | next call admitted |
| pre-commit "a gate failed" | 3 | 2 | next call admitted |
| driver check 49 | 3 | 2 | next call admitted |
| driver check 37 | 2 | 3 | next call admitted |
| driver check 56 | 1 | 2 | next call admitted |
| gate-guard suite | 1 | 2 | next call admitted |
| `msys_pathconv_guard.py` | 1 | 2 | next call admitted |

- **The 10-streak:** subagent `agent-a9dc7a3dab9bd4a86` (workflow `wf_86678f56`, session `8d2976c7`) tried 5 spec files twice each. It ended with the builder's return `committed:false, "DIVERGENCE: … The scratch-guard hook refused all five edits"`, adding "Until the spec is revised, --plan will keep naming this unit."
- **Same rule two or more times in one transcript, not necessarily in a row:** pre-commit "a gate failed" in 20 transcripts (12 with three or more); agent-cap fan-out in 3; driver checks 49 and 37 in 3 each.
- **format-guard:** 9 blocks in one session, each in a different turn, never two in a row, which matches `:469`.
- **Endings:** none of these runs ended on an unresolved repeated refusal by itself. Each ended in an admitted call or a typed divergence return, and the role-arm streak's divergence is a route back that `--plan` re-offers.

## 3. Classes of non-actionable refusal

1. **The remedy needs a grant the actor lacks** (a spawn, a policy write, an owner command or approval): T5 for subagents and its Tier-2 approval half, T6 and T7 for role agents, A1, A6, V10, V20, V24, V25, V26, V27, V28, and V7 under strict. Measured: the 10-run streak in T6. Root: V32 checks that a remedy is *named*, not that it lies within the refused actor's grant.
2. **A fact the actor cannot change** (another unit's or build's state, the network, the host): V4, V5, V8 (INHERITED and CONTENDED), H8 on an inherited red, V30, A5, T3, and the missing clone in V33.
3. **Stale state the actor cannot refresh:**
   - V13: a shape digest from a stale composition;
   - V17: a harness edited before landing;
   - Q1: an unreadable liveness keeps the recorded phase;
   - V2: a malformed witness;
   - T6's aftermath: `--plan` re-names the unit until its spec is revised.
4. **The remedy is time, which an agent cannot spend:**
   - A4: a new prompt or 45 minutes;
   - V16: "Do not retry" until the admission queue arms;
   - V5.
5. **The refusal keeps no counter, so a repeat is unbounded:**
   - every PreToolUse hook today (T1–T8, A1–A7, G1, Q1) and every git hook (H1–H8);
   - V1, the default route, if a re-offered refusal is not a route back;
   - V2's `invalid-input` (a journal line every beat);
   - V20 and V22, which flow into V1;
   - V3, counted in a record that does not exist yet.
   Today's only counted refusals are S1 (6 lifetime), F1 (1 per turn), the lander's 3 retries, and the driver's run-level `RUNAWAY_CEILING`, `RESUME_ATTEMPTS` and `REVIEW_ROUNDS`.
6. **Refusal cycles between guards:**
   - **T5 → T6 in a subagent:** kickoff writes a spec, the role arm refuses, and the spawn remedy is out of reach. The only exit is a divergence return.
   - **V28 ↔ V27:** a malformed policy with no valid revision refuses every landing, and fixing it is refused to agents. The only exit is the owner, and no owner item is named.
   - **Q1 ↔ S1:** the question is refused, `--park` needs the same driver, and stop-guard fails open, so the session ends silently.
   - **T8 ↔ G1:** a verifying role is told to probe, G3 and gate-guard refuse suites and fixtures shaped as `*.test.sh`, and the verification becomes a claim.
   - **T7 ↔ A3 ↔ T8:** a broken role index refuses writes, spawns and role scripts at once. Only the main loop's Bash re-render gets out.
   - **V10 with H4/H8:** bypass is refused while gate reds are unreliable; v2 admits this stall.

**Ambiguities to settle in the records** (each recorded above where it bites):
- whether a re-offered refused item counts against `flow.route-backs`, and whether `next` reports it as `act` or as `blocked`;
- whether `run.on-owner-question` resolves V26;
- whether V6's revert pass and V8's CONTENDED re-run count;
- who repairs a DEAD PROBE;
- whether `RESUME_ATTEMPTS` covers an act that returns a refusal rather than dying.

Belongs to other researchers, one line each:
- the 112-line `rate_limit` tick loop: history or census;
- V4's live-but-looping lease holder: census.
