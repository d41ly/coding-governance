# Research: the runtime layer, hooks, isolation and supervision

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 32's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

---

# Runtime research: hooks, isolation and supervision

The short answer: every enforcement hook fails open when it crashes, and that happened 31 times in one burst on 2026-10-14. The platform's fail-closed switch exists but no entry uses it, and the `claude` on PATH here is too old for it. Isolation per unit has no carrier today: 13 worktrees were made by hand, 8 of them merged and never removed. Nothing ever expires a claim on the remote.

## Inventory

**Claude Code hooks** (`.claude/settings.json:3-121`; none have `onFailure` set (`grep -c onFailure` returns 0); no agent file declares hooks). Firings are visible attachments over 60 days (3,484 transcripts, `hookagg.py` in Measurements). A guard that allows silently leaves no attachment, so PreToolUse counts are lower bounds.

| Event / matcher | Script (kit) | Enforces or records (layer) | Latency (measured) | On crash or timeout | Bypass |
|---|---|---|---|---|---|
| PreToolUse Workflow\|Agent | `tools/hooks/agent-cap.js` (hooks) | Fan-out cap, raw-primitive ban, rule 6 role-sha/task-sha spawn guard (Runtime) | 56 ms/call (node floor 39 ms) | Open on exit≠2 or timeout. Rule 6 denies on its own throw (`agent-cap.js:2288-2293`); unparseable stdin admits (`:2235-2237`) | Lowering `FANOUT_CAP` only; `AGENT_CAP` is refused (`:2245-2256`) |
| PreToolUse Bash\|PowerShell\|Edit\|Write\|MultiEdit\|NotebookEdit | `tools/hooks/scratch-guard.js` (hooks) | Write allowance: scratch roots, routed paths (Runtime) | 57 ms; visible p50 94 / p95 194 / max 1978 ms | Declared "FAILS OPEN" (`scratch-guard.js:41`) | Writes the command parser misses |
| PreToolUse Bash\|PowerShell\|AskUserQuestion | `tools/unattended/gate-guard.js` (unattended) | Refuses the bar and self-tests before VERIFYING, and AskUserQuestion under a lease (Runtime) | 52 ms | Open: a throw on the ask arm exits 0 (`gate-guard.js:768-773`) | Spellings outside the parsed prefixes (`:21`, `:487`) |
| SessionStart startup\|clear / resume\|compact | `manifest-check.sh --card --write` / `--replay` (session-kickoff) | Renders or replays the card (Context) | p50 1266 / max 20995 ms; p50 339 ms | Errors exit 2, which SessionStart does not block | — |
| SessionStart startup\|resume\|clear | `tools/check-wiring.sh --session` | Wiring repair, always exits 0 (`check-wiring.sh:9,1987`) (Runtime/deploy) | p50 2682 / p95 10389 / max 24717 ms | Open by design | — |
| SessionStart + PostToolUse Bash\|PowerShell | `procmon-hook.js` (process-monitor) | Reports processes past the ceiling (Observability) | PostToolUse p50 1255 / p95 2468 / max 13398 ms, n=580 visible (census path; throttled path is one `stat`, `:21-24`) | "FAILS OPEN, ALWAYS" (`procmon-hook.js:26`) | — |
| PostToolUse Read | `recall-opened.js` (memory-recall) | Recall on open (Memory) | none visible | exit 0 always (`:206-208`) | — |
| Stop | `stop-guard.js` (unattended) | Blocks a stop under a live unattended lease (Runtime) | p50 3780 / p95 9453 / max 41933 ms, n=95 | `onFailure` cannot apply to Stop (docs) | Harness ends the turn after 8 blocks (`stop-guard.js:53`) |
| Stop | `format-guard.js` (hooks) | Final-message format for a routed build (Runtime) | — | Allows on an internal error (`format-guard.js:549`) | — |
| StopFailure | `stall-recorder.js` (unattended) | Records a stall (Observability) | — | Cannot block (`:15`) | — |
| SubagentStart | `scratch-guard.js` (hooks) | Injects route context (Context) | p50 72 / max 122 ms, n=276 | Open | — |
| User level (outside the repo) | `git_dash_c_guard.py`, `msys_pathconv_guard.py` | Node-local Bash guards | p50 20–22 ms | Open | — |

In all: 13 command entries from 6 owners (hooks, unattended, process-monitor, memory-recall, session-kickoff, and check-wiring at the tools root). 12 per-kit `*.fragment.json` files exist and are merged by `check-wiring.sh:151-190`. agent-cap is wired by a hard-coded arm instead (`check-wiring.sh:806`). There is no SubagentStop hook today, so the settled return check has no carrier yet.

**Git hooks.** `core.hooksPath` is set to the **absolute** `C:\projects\coding-governance\.githooks`, so every worktree runs the primary tree's hooks. That is the drift `pre-push:11-18` describes.

| Hook | Enforces | Cost | Crash or kill | Bypass |
|---|---|---|---|---|
| `pre-commit` | Staged-scoped fast gates | Not measured (lead: can outrun a tool timeout; unverified) | Refuses when no toplevel (`:9-12`). It has **no signal trap** (grep), so a killed hook reads as success on Git for Windows, by the mechanism in `pre-push:51-53`: **open** | `--no-verify` |
| `commit-msg` | Merge transition audit, plus unattended `--check-commit` | — | `|| exit 0` with no toplevel (`:38`); a check that cannot run prints and passes (`:61`): **open**, graded later at the close | `--no-verify` |
| `pre-push` | Full bar on a default-branch push | The bar itself; health.log has "canary after a 13200s timeout" | Traps HUP/INT/QUIT/PIPE/TERM and refuses (`:81-85`). KILL or TerminateProcess still lands, caught after the fact by push-main's `landed UNGATED` (exit 4) (`push-main.sh:60,342-350`) | `--no-verify`, a redirected hooksPath (`:992`); non-default pushes are ungated unless `GOV_BRANCH_GATE_CMD` is set (`:1135-1141`) |
| `pre-rebase` | Straggler rebase refusal | — | No trap: open | `--no-verify` |
| `gate-env.sh`, `straggler-guard.sh` | Sourced policy and libraries | — | — | — |

## Sequence

For one Bash call today:
1. Three node processes start in parallel: agent-cap does not match Bash, so scratch-guard, gate-guard and two user-level python guards run. The docs say "All matching hooks run in parallel."
2. The tool runs.
3. procmon-hook runs: a `stat` when throttled, otherwise a census of about 1.2 s.

At a stop, stop-guard and format-guard run. Pushes go `push-main.sh` → `pre-push` → `run-gates.sh`, and the allow record in the git dir is the witness push-main reads, not git's exit code.

## Measurements

Hook aggregation over 60 days (script `scratchpad/hookagg.py`):
```
files 3484
[('hook_success',1323),('hook_additional_context',345),('hook_non_blocking_error',31),('hook_blocking_error',12)]
```

**The fail-open incident.** All 31 non-blocking errors fell on 2026-10-14 14:01–14:02:
```
PreToolUse:Bash 3   gate-guard.js    | Fatal JavaScript out of memory: Committing semi space failed
PreToolUse:Bash 1   scratch-guard.js | Failed to run: EUNKNOWN: unknown error, uv_spawn
PreToolUse:Bash 126 git_dash_c_guard | ...python: Resource temporarily unavailable
PreToolUse:Bash 66  scratch-guard.js | No stderr output   (x many)
```
Under resource exhaustion, every guard failed and every one was non-blocking. The docs say "a policy hook with a wrong path or a crashing script lets everything through" (https://code.claude.com/docs/en/hooks).

The 12 blocking errors are all Stop hooks: 5 from stop-guard and 7 from format-guard.

**Platform.** `onFailure: "block"` turns a failure (cannot start, exit≠0/2, timeout, invalid output) into exit 2. It "requires Claude Code v2.1.295" and "has no effect on Stop, SubagentStop…" (same URL). The default command timeout is 600 s.
```
$ claude --version
2.1.292 (Claude Code)
```
This disagrees with the handed fact "CLI 2.1.295": the PATH CLI on this node is 2.1.292. The desktop's bundled CLI is 2.1.295, as procmon's report shows `...\claude-code\2.1.295\...`.

**Guard latency** (10 runs each, a benign Bash payload): scratch-guard 57 ms, gate-guard 52, agent-cap 56, `node -e 0` 39. Process start is about 70% of each guard's cost.

**Worktrees.**
```
$ git worktree list --porcelain | grep -c ^worktree   -> 14 (primary + 13)
8 clean and merged into origin/main (orphans); 1 dirty (gov-bar-reds-fix, 3 files);
recursing-zhukovsky-06ca9e unmerged, 3 weeks old; .claude/worktrees holds 13 stray non-worktree files (gs.out, lb.txt, ...)
primary tree: main, 4 ahead of origin/main
```
The Facts line "Worktrees: none yet" disagrees with the tree.

**Hazards:**
- `core.autocrlf=true` with `* text=auto` and `*.sh eol=lf`: the CRLF smudge applies to everything that is not `.sh`.
- `core.longpaths=true` mitigates `MAX_PATH`.
- `extensions.worktreeConfig=true`.
- `.claude/scheduled_tasks.lock` is absent now, so that lead is unverifiable at this moment.

**Scratch.** `%TEMP%` holds 3,371 `tmp.*` dirs, 497 of them older than 7 days. Their source is not attributable: `mktemp -d` is used by unattended, run-gates and others.

**Ports and databases.** No allocator anywhere in `tools/` (grep hits are incidental). gov runs no services, so the `[isolate]` clause "own ports and databases" (`AGENTS.md:30`, template `:29`) has no carrier.

**Supervision.** Ceilings (`.process-monitor.conf`):

| Setting | Value |
|---|---|
| AGE_CEILING | 14400 s |
| SPIN_RATE | 0.5 |
| REAP_MODE | reap-orphans |
| THROTTLE | 300 s |

The hook never kills (`procmon-hook.js:28`). Reaps happen only through `reap.py`, whose classes are ORPHAN / SPIN / IDLE / UNKNOWN (`reap.py:367-368`).

60 days (`scratchpad/procmon.py`, `reapforms.py`):
```
reports 598   distinct pids flagged {'IDLE': 44, 'ORPHAN': 1}   (SPIN 0)
reap.py invocations: --kill 4, --sweep --dry-run 2, live --sweep 0
3 "process-monitor: could NOT run" reports
.git/health.log: 7 lines since 2026-10-11 -> 1 reap tree-killed, 3 beacon-reaped, 2 retry-passed
```
The run log (`.git/runlog/*`, 2,299 lines) records no reap.

**Claims on the remote** (`git ls-remote origin 'refs/gov/runs/*'`, objects read locally):
```
17 claims: landed 8 (beat 2-5 d) · held 8 (beat 2-8 d) · live 1: aFrugalTurnstile, beat 4 d
```
`stale` is a read-time verdict only: beat age greater than `RESUME_STALE_BOUND=5400` (`.unattended.conf:95`, `unattended.sh:2180-2185`). It permits a take-over (`:2291`). `held` never ages into stale (`:2183`), and no code deletes a terminal ref. Nothing expires a claim. The "beats days old" lead is confirmed.

## Gaps

1. No enforcement hook is fail-closed. 31 failures in one burst all admitted.
2. The fail-closed switch needs 2.1.295. The PATH CLI is 2.1.292, and the switch cannot cover Stop or SubagentStop, which is where return validation is settled to live.
3. `pre-commit`, `commit-msg` and `pre-rebase` have no signal traps or after-the-fact witness. Only the push has the allow-record pattern.
4. The absolute `core.hooksPath` makes every worktree run the primary tree's hooks.
5. Units share one worktree. `unattended-build.js:76-80` ratifies "parallelism route: none" because E4 (two passes committing on one index) failed, and a concurrent caller commit "meets git's index lock" (`:133-135`). Nothing creates or removes a unit worktree; `unattended.sh:3901` only prints a recipe.
6. Platform `isolation: worktree` "branch[es] by default from your default branch rather than the parent session's HEAD" (https://code.claude.com/docs/en/sub-agents). The configurable base ("choose the base branch") was not read.
7. Nothing reaps automatically. 44 IDLE pids were flagged and 4 were killed by hand.
8. Claims never expire, and `held` is immortal.
9. Hook wiring is split: 12 fragments plus one hard-coded arm.

## Candidates

**A. One Runtime hook surface.** A single dispatcher entry per event, which reads per-kit hook packs and routes by `tool_name`. It extends the existing seam: fragments plus the `check-wiring.sh` resolver.

| Test that could make it lose | Result |
|---|---|
| Wall-clock per Bash call: three guards in parallel vs one dispatcher running the rules in-process | Parallel max is about 57 ms. In-process is about 39 + 3×~15 ≈ 85 ms unless rule modules load lazily per tool. **Loses on latency**; neutral if lazy. |
| Process starts per Bash call under exhaustion | Today 3–5 per call (5 counting the two node-local python guards), and the 10-14 failures were spawn and OOM failures. One per call: **wins** |
| Blast radius: one dispatcher throw disables every guard | **Loses unless paired with B1** |
| Class check "every enforcement entry is fail-closed" | One entry to check instead of 13: **wins** |

**A0. Today's per-kit entries.** Rejected by the class test above: 13 entries, none fail-closed, and wiring split two ways (`check-wiring.sh:574,806`).

**B. Fail-closed rule for enforcement hooks.**

| Mechanism | Test that could make it lose | Result |
|---|---|---|
| B1: platform `onFailure: "block"` on PreToolUse and SubagentStart enforcement entries | (i) `claude --version` ≥ 2.1.295 on every node that runs a session. (ii) Replay the 10-14 burst: does it block all 31? (iii) Does a missing-path fixture lock the session out of its own repair (reap, revert)? | (i) **Fails on this node's PATH CLI** (2.1.292); the desktop passes. (ii) Wins by spec: every one was a start, exit or OOM failure. (iii) Untested, and it is the build's required fixture; needs an out-of-agent escape. |
| B2: script-level catch-all that denies | Same burst replay | **Rejected**: OOM and `uv_spawn` happen before or outside the script, so 0 of 31 would be caught |
| B3: witness record behind the act (push-main's allow record) | Is there a witness for each act? | Exists only for push (`push-main.sh:342-350`). It is the only mechanism for Stop and SubagentStop, where B1 has no effect. |

**C. Isolation per unit by construction.**

| Mechanism | Test that could make it lose | Result |
|---|---|---|
| C1: executor creates `git worktree add -b` from the build branch tip, sets the per-unit scratch and env, and removes the worktree at release | (i) Two passes commit concurrently with no index lock (E4). (ii) After N units, worktree and `tmp.*` counts return to baseline. (iii) In the new worktree, `git rev-parse --git-path hooks` resolves to its own tree. | Not built. (ii) Fails today's baseline: 8 orphans, 497 stale tmp dirs. (iii) **Fails today** with the absolute hooksPath. All three are the build's fixtures. |
| C2: platform `isolation: worktree` on the Agent or Workflow call | The base equals the build branch tip | **Loses by docs**: the default branch, not HEAD. Reopen only if the unread base option sets it per call. |
| C3: today's shared worktree with sequential dispatch | Concurrent commits | **Rejected**: E4 failed (`unattended-build.js:78`). |

## Pick

- **A + B1**, gated on the 2.1.295 floor being declared and checked per node.
- **B3** for Stop and SubagentStop and for every git hook: the executor trusts a witness record, never an exit code.
- **C1**, with relative or per-worktree `core.hooksPath` and removal at release.
- Out of the candidates, but measured: claim expiry (`held` and `live` past a bound becoming takeable, terminal refs pruned) and auto-reap of ORPHAN are supervision's missing halves.

Scripts used: `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\hookagg.py`, `hookerr.py`, `procmon.py`, `reapforms.py`.
