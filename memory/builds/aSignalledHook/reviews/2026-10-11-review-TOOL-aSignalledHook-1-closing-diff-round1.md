**Serves:** diff-review TOOL-aSignalledHook-1

# Tier-2 closing diff review — aSignalledHook, ROUND 1

*The closing review of TOOL-aSignalledHook-1 before its landing, run attended on node `a` on
2026-10-11. It reviews the unit's product commit 83269a93e and, after the finders started, the
reconcile merge 312f5398c of origin/main 63a43402, which brought in aFrugalTurnstile's `covered` exit
and `--decide` mode in the same hook. The incoming content is another build's; its seams with this
unit are in scope.*

Reviewed range: `b726385f2b5b8fd16802925c02104377253a9045...312f5398c` · ROUND 1

## Verdict: CLEAN WITH FIXES

Three finder lenses, no separate skeptic: each confirmed finding below was re-established by the
synthesizer reading the code at 312f5398c, and two were raised independently by two lenses. Five are
folded into the unit (rev-2); one is filed as an ask.

## Review shape

Lenses: signal-handling correctness, integration seams with the hook's readers, test arms and records.
Each was given the security model (the hook is the merge gate; a signal-killed hook reads as success
on Git for Windows) and the by-design list (KILL and TerminateProcess are uncatchable; an old hook
beside a new lander reads every landing UNGATED). No finder ran a suite whole or pushed anywhere.

## What was verified and holds

- The handler cannot abort before its `exit` under `set -u`, in any state from the first line on.
- Traps reset in command substitutions; a signal there is held until it returns, then refuses.
- `wait` returns at once for each trapped signal, and the handler stops the async bar (run on MSYS).
- A bar killed by a signal or exiting 127 reads red; the inherited-red landing writes the allow record.
- No pusher other than the lander reads or clears another push's allow record.
- Nothing holds a closed list of hook decisions, so `refuse-signal` is accepted by the run-log reader.
- The run-log exit table matches the merged hook's exit sites, the handler's included.

## Findings

- **R1 [high] — a covered push wrote no allow record (two lenses).** aFrugalTurnstile's `covered` exit
  allows a default-branch push with no bar, and the lander read every such landing as UNGATED.
  FIXED: the exit writes `pre-push-allow` naming the covering run; arm "SG covered" in the BG block.
- **R2 [medium] — a push of nothing was reported UNGATED (two lenses, reproduced).** With the remote
  already at HEAD, git runs the hook with no ref lines, it exits `skip-nondefault`, and the lander
  exited 4. FIXED: `check_push_allow` takes the pushed sha and the remote's prior tip, captured before
  the push, and reports "nothing was pushed"; arm "SG re-run".
- **R3 [medium] — the `--land` guard was untested.** Only the attended path was driven, and the
  incident took `--land`. FIXED: arm SG AC3b.
- **R4 [low] — the allow check read HEAD after the push.** FIXED by R2's capture before the push.
- **R5 [low] — a `signalled` refusal printed "a precondition; no leg ran".** FIXED: its own case in
  `derive_push_failure`.
- **R6 [low] — the run-log suite header called AC3's time check "not a threshold".** FIXED: it names
  the 15 s threshold against the 20 s stub.
- **R7 [low-medium] — nothing handles exit 4 in the unattended kit.** NOT FOLDED: the fix is a protocol
  change to another kit. Filed as `TOOL-aSignalledHook-2`.
