# Brief — aSignalledHook: a signal-killed pre-push hook refuses the push

**Serves:** research TOOL-aSignalledHook-1

## The prompt

> Task: determine whether .githooks/pre-push or run-gates.sh can return exit 0 (or be read by git as
> success) when (a) a fork fails with EAGAIN / 0xC0000142 while the bar is queued in the turnstile, or
> (b) the hook's Windows-side parent is terminated by a tree kill. Reproduce on a `git clone --local`
> under %TEMP%/<short> with a stub bar that sleeps in the queue. If either is a fail-open, fix it so any
> abnormal end of the queued bar refuses the push (fail closed), add a regression arm to the pre-push
> self-test (tools/.githooks pre-push tests / run-gates.test.sh as appropriate), and record the class
> in memory/gotchas/. Follow AGENTS.md: spec first (Tier-2, it changes a gate's semantics), build under
> a routed unit, no merge bar inside the pass.

## The brief

### Goal
Make a pre-push hook that is signalled while its bar runs, or before it, refuse the push on Git for
Windows, where a hook killed by a signal is read as success; and make the lander report a push git
calls successful when no hook verdict allowed it.

### Items
1. Trap the hook's catchable signals into a refusal that stops the bar (spec S1, S2, S5, S6).
2. An allow record the hook writes only at its success exit, which push-main requires (S3, S4).
3. Regression arms in the pre-push, run-log and push-main suites.
4. The class recorded under memory/gotchas/ (S7).

### Acceptance
The spec's AC1 to AC7, each observed by a fixture push in its suite.

### Gates
`pre-push self-test` · `pre-push run-log line` · `push-main self-test`, run as slices during the pass;
no merge bar inside the pass.

### Non-goals
Preventing a landing after a KILL; any run-gates change; reverting 69e0ff0f.

### Limitations
No merge bar inside the pass. No merge to main and no push without an explicit ask.

### Reuse
The hook's refusal channel and the lander's verdict-file pair (`pre-push-refusal`, `pre-push-bar`);
the recall query named TOOL-dLoggedFlight-4 (the run log) and TOOL-aSurfacedLexicon-25 (an earlier
unexplained no-bar push of the same shape).

## Drawn from the session

> TERM: git push rc=0 remote=dec326f local=dec326f ... KILL: git push rc=0 ... control exit1: rc=1
— agent, the first scratch reproduction, git 2.54.0.windows.1

## Owner confirmation

Asked: Should this unit also make push-main DETECT it after the fact (hook writes a positive allow record before its success exit; push-main, on git rc=0 with no allow record for the pushed sha, reports 'landed UNGATED', exits non-zero and withholds the lander marker so --landed refuses)?
Answer: Hook + lander detection
