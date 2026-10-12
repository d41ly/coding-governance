# push-main — the lander and the pre-push hook that gates every default-branch push

```toml
feature = "push-main"
title = "the lander that reconciles, gates and pushes the default branch, and the pre-push hook that refuses any default-branch push it did not gate"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aLeasedGauntlet-1", "TOOL-dLoggedFlight-4", "TOOL-dDerivedDocket-26",
  "TOOL-aSignalledHook-1"]

[claims]
gate-legs = ["pre-push self-test", "push-main self-test"]
kits = []
git-hooks = ["pre-push"]
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["signal-killed-hook-reads-as-success.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/push-main.sh",
  "tools/push-main.test.sh",
  ".githooks/pre-push",
  ".githooks/pre-push.test.sh",
]
```

Two halves that ship in one govkit entry (`tools/govkit/entries/push-main.kit.toml`) and must move
together. The lander, `tools/push-main.sh`, reconciles the default branch onto the remote's tip and
pushes it; the hook, `.githooks/pre-push`, runs the merge bar inside that push and refuses a red one.

## Constraints & why

**The hook talks to the lander through files in the git dir, never through output.** The push's
output carries the bar's own output, so classifying on its words let a leg that printed `connection`
pass for an unreachable remote. Three files: `pre-push-refusal` (a token on every refusal),
`pre-push-bar` (the bar the hook vetted, written before it runs) and `pre-push-allow` (written only at
the hook's one success exit on a default-branch push). Each is cleared by the hook on every run and
by the lander before every push.

**git's exit 0 is not the hook's verdict.** On Git for Windows a hook that dies by a signal is read
as success, and 69e0ff0f landed that way with its bar queued (`TOOL-aSignalledHook-1`). So the hook
traps every catchable signal into a `signalled` refusal, the bar runs as a child the hook waits on
so that trap is not delayed an hour, and the lander requires `pre-push-allow` to name the pushed
commit before it calls the push landed or writes the lander marker.

**An exit 0 from the runner is not GREEN until its run record says so** (`TOOL-dDerivedDocket-26`):
the hook pins and clears its own run id, and reads that run's `verdict` file.

## Shared seams

- The run log (`runlog` dossier): the hook writes START and END lines to `pushes.log`, and a signal
  now ends `exit=clean decision=refuse-signal`. `.githooks/pre-push.runlog.test.sh` is that kit's.
- The merge bar (`run-gates` dossier): the hook runs the runner, whose turnstile may queue it for an
  hour, and forwards TERM to it when the hook is signalled.
- The unattended driver reads the lander marker this lander writes; a `landed UNGATED` push writes
  none, so `--landed` refuses it.

## Gaps

- KILL and a TerminateProcess of the hook's bash still land a push on Git for Windows. The lander
  reports it after the fact and cannot unpush it.
- A lander paired with a hook older than the allow record reports every landing as UNGATED. Under a
  relative `core.hooksPath` the two come from one tree.
- `--land` names `HEAD` to the check, not the prepared merge: under in-place the close commits on top
  of it, and that is the commit pushed (TOOL-aPrimedIndex-10).
- The branch bar (`GOV_BRANCH_GATE_CMD`) still runs in the foreground, so a signal during it is
  handled when it returns.

## Reuse affordance

seam: `write_refusal` in `.githooks/pre-push` — reuse for any new reason the hook refuses a push;
extend via a token and its run-log decision in its one `case`, which `derive_push_failure` in the
lander reads without a code change.

seam: the verdict-file set (`pre-push-refusal`, `pre-push-bar`, `pre-push-allow`) — reuse for any new
verdict the lander needs from the hook; extend via a fourth file cleared at the same two sites, never
a word parsed out of the push's output.
