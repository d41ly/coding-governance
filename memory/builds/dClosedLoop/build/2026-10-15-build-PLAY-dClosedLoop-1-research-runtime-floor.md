# Research: the runtime layer, whether CLI 2.1.295 is needed to fail closed

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 36's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-15-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

---

I tested this on both binaries. 2.1.295 is not needed to fail closed on tool calls: 2.1.292 already refuses gated calls under every burst failure class when the permitted calls are approved by a hook that answers the permission prompt, not by a PreToolUse allow. The switch itself really is new in 2.1.295, and 2.1.292 ignores it without any warning.

## [version]

**The sources.** The changelog adds the switch in 2.1.295: "Added `onFailure: "block"` for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code blocks the action instead of letting it through". The hooks page says it "Requires Claude Code v2.1.295 or later". It counts five things as failure: can't start, exit other than 0 or 2, HTTP error, timeout, and output that won't parse. It has no effect on Stop, SubagentStop, TaskCompleted, TeammateIdle or async hooks. Without it, a failure is a "non-blocking error" and the action goes ahead.

**The test.** I ran it in a new scratch directory outside every repository (`git rev-parse` fails there) with `--setting-sources local`. The settings had a PreToolUse hook on Bash pointing at a missing script, with `onFailure: "block"`, plus `--allowedTools Bash`:

| Binary | Result |
|---|---|
| 2.1.292, `C:/Users/d41ly/.local/bin/claude.exe` | **Ignores the key.** No warning, the settings load, and `echo hi` runs. |
| 2.1.295, `C:/Users/d41ly/AppData/Roaming/Claude/claude-code/2.1.295/d2e29494ec83/claude.exe` | **Blocks:** `failed; blocking because onFailure is "block"` |

On 2.1.295 the switch blocked every class I tried: a hook that can't be spawned (`ENOENT … uv_spawn`), a silent exit 1, exit 126, and a node OOM (exit 134). It also blocks in auto mode. On 2.1.292 each of those classes let the call through.

## [mechanisms]

The burst classes are: OOM, `uv_spawn` (I simulated it with a hook whose executable doesn't exist), exit 126, and exit with no stderr. I also added a missing script (exit 127) and a timeout. "Gated" means a call that needs approval. Every run below is on 2.1.292 unless marked otherwise.

**A. A PreToolUse hook as the only allow path** (manual or `dontAsk`, `-p`)
- **Losing test:** any burst class lets a gated call run.
- **Result:** every class was denied ("This command requires approval"). A healthy hook that allows let the call run. A Write in manual mode was denied too, and so was the same test on 2.1.295.
- **It loses on four other tests:**
  - `echo hi` runs even with the hook missing. `echo`, `cat`, `ls`, `grep` and read-only `git` are in the built-in read-only set, which skips approval in every mode. So the `echo hi` probe the brief asked for cannot test this mechanism, and I used `node -e` instead.
  - A crashed guard sitting beside a healthy allowing hook: the call runs. The hook that allows must be the one that does the checking.
  - Any allow rule bypasses it. This repo's `.claude/settings.local.json` allows `Bash(git fetch *)`.
  - Under auto mode it fails open (missing script and exit 1 both ran, on 2.1.292 and on 2.1.295).
- **Interactive:** by the docs, a failure falls back to a prompt to the person in manual mode, and to the classifier in auto mode, which is the built-in start mode from 2.1.283. Not tested, because it needs a terminal.

**B. Auto mode with ask rules plus a PermissionRequest hook as the answer**
- **What I found in auto mode:**
  - A failed PreToolUse hook lets the classifier allow the call.
  - A deny rule beats a hook's allow.
  - An ask rule beats a PreToolUse allow, so in this form the PreToolUse hook cannot be the allow path.
- **The working combination:** an ask rule on each gated tool (`Bash`, `Write`/`Edit`, `Agent`), with a PermissionRequest hook that answers allow.
  - With a healthy hook the call runs.
  - Every failure class was denied ("…you haven't granted it yet"), and the OOM case was denied on 2.1.295 too.
  - Read-only `echo` was denied as well, which closes A's read-only gap.
  - Write and Agent were both denied.
- **Losing tests it carries:**
  - **The classifier is lost.** By the docs, an ask rule resolves to a prompt before the classifier, so the classifier never sees the gated tools.
  - **The hook must answer with JSON.** PermissionRequest ignores exit 2, so a deny must be returned as a decision object.
  - **Interactive behaviour is untested.** By the docs, a failure there falls back to a prompt to the person.
  - **The platform may narrow it.** In 2.1.299, PermissionRequest hooks lost the power to approve shell commands in auto mode in Cowork cloud sessions. That doesn't apply here, but it shows the platform narrowing this power.

**C. A wrapper that turns any guard exit other than 0 or 2 into 2**
- **Losing test:** the wrapper itself can't be spawned.
- **What it catches** (I tested a scratch wrapper): OOM, exit 126, exit 1, and a missing child script, all blocked, read-only calls included.
- **What it cannot catch:** when the wrapper itself can't be spawned, the call runs. That is the `uv_spawn` class. A wrapper at a missing path, or a wrapper that dies itself, are the same class. A timeout is caught only if the wrapper sets a shorter one of its own; I did not test that.

**D. Other options in the docs**
- A `--permission-prompt-tool` that doesn't exist stops the run before it starts ("Error: MCP tool … not found"). A host that crashes mid-run was not tested; that needs an MCP server built first, and that is the test the build must run.
- `dontAsk` and `--permission-prompts none` (2.1.259 and later) make A stricter but are not separate mechanisms. `dontAsk` denied with a missing hook and allowed with a healthy one.

## [verdict]

| Session | 2.1.292 | 2.1.295 |
|---|---|---|
| Act session (`-p`, auto mode) | B closes every burst class for gated tools. A is enough under manual or `dontAsk`, except for read-only commands. | The switch closes every class on any PreToolUse entry, including tools that are not gated. B still applies. |
| Attended session | B falls back to a person (docs only). A in auto mode falls back to the classifier, which is open. | The switch blocks. |

**Left uncovered on both versions:**
- Stop and SubagentStop, where the switch has no effect either; they keep the design's witnesses.
- SessionStart and SubagentStart. The design's SubagentStart enforcement can move to an ask rule on the `Agent` tool, which I showed denies on 2.1.292.
- Any allow rule that matches a gated tool.
- An interactive session's failure falling back to a person (docs only).

**Is a floor needed?** Not for tool-call enforcement. One is needed only if the design requires blocking on events that have no permission step, mainly SubagentStart, and its job moves to gating the `Agent` tool. The silent ignore on 2.1.292 means no one can rely on the switch without checking the version, so it should be treated as a capability that is detected, not a floor that refuses.

## Candidates

1. **The floor stays, gating only the switch.**
   - **Losing test:** an older binary gives the same guarantee.
   - **Lost:** B denied every class on 2.1.292. It also refuses what the owner said older binaries should run.
2. **The allow-path replaces the floor (A alone).**
   - **Losing test:** any burst class lets a gated call run in auto mode, which TOOL-aMendedFleet-116 moves unattended runs to.
   - **Lost:** the call ran in auto mode with the hook missing and with exit 1. It also lets read-only commands through, a second allowing hook opens it, and allow rules bypass it.
3. **A combination. Recommended.**
   - **What it is:**
     - B is the baseline on every version.
     - The one checking hook (the dispatcher) is the only allow path.
     - A class check refuses any allow rule that matches a gated tool.
     - The switch is added where the version check shows it is supported, without a floor.
     - Stop and SubagentStop keep the witnesses.
   - **Its losing tests:**
     - An interactive 2.1.292 session with the PermissionRequest hook missing must show the prompt to the person and never run the call. Not run; it needs a terminal.
     - A dead dispatcher refuses every call, including its own repair. Same as the design's existing note; not run.
     - A permission-prompt host that crashes mid-run. Not run; it needs a build.

## Records and evidence

**Where the records and the code disagree:**
- The runtime design's `[enforce]` and RT-2 assume that below 2.1.295 the enforcement hooks fail open. That is true for PreToolUse plus allow rules or auto mode, and false for the B form.
- The research table B's `echo hi` style test can't separate the candidates, because `echo` never needs approval.

**Evidence:** each probe's command, the settings it used, its output and which hooks fired are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/probe/logs/<label>.txt`. The probe runner, the settings files and the hook fixtures are in the `run.sh`, `settings/` and `hooks/` folders beside it. One caution: the `claude exit:` line in every log is always 0, because it records the status of an `echo`, not of claude. The verdicts above come from the JSON result and `permission_denials`.

Sources:
- [Hooks reference](https://code.claude.com/docs/en/hooks)
- [Changelog](https://code.claude.com/docs/en/changelog)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Permission modes](https://code.claude.com/docs/en/permission-modes)
- [Headless mode](https://code.claude.com/docs/en/headless)
