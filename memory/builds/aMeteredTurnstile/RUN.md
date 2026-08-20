# aMeteredTurnstile - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 4240167bc26ef8c2cf5c7149fe84a5c4129ebe8f
phase: ABORTED
branch-sha: 3355837aa7e072de44a7e1d10c8e5e8020c22b15
branch-ref: refs/heads/branch/full-gate-bar-performance-828ae8
mode: slug
anchor-kind: run-branch
keepalive: 2daed484
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 56b945cbb0613b1352dd06221d4d39940db33419
anchor-ref: refs/heads/main
base: 3355837aa7e072de44a7e1d10c8e5e8020c22b15
keepalive-reaped: yes
parked-surfaced: yes

## Parked

2026-08-19T23:32:21Z decision · item The spec TOOL-aMeteredTurnstile-1 was authored and BUILT in the same attended session, before this mandate existed, so M4's spec audit never preceded its code. · reason Options seen: (a) run the spec audit now, which would be a pre-code pass performed after the code and would record a false ordering; (b) rebuild the unit behind a real audit, which discards working, measured, merged work to satisfy a sequence; (c) park it and let the owner decide whether the unit needs a retroactive design pass. Refused (a) because a spec-audit record dated after the build is the kind of green-by-construction artifact this repo's charter exists to prevent, and refused (b) as disproportionate. The closing M8 diff review DID run and covers the code; what is missing is the pre-code design pass, and only the owner can judge whether that matters for a unit whose deliverable is a measurement.

2026-08-20T03:10:43Z decision · item This run cannot land: the merge bar is RED on this host for an environmental reason, not a defect in the build. · reason The run-gates canary reports that GATE_JOBS=0 and its width-1 control BOTH expired, on three arms, so this host could not finish the fixture at any width and the clamp is unproven either way; it also skipped the spun-outcome arm for the same reason. That is the canary correctly refusing to certify what it could not observe, and the cause is the latency regression this build measured: process creation on node a is about 25x its 2026-08-11 baseline (bash -c true 22.5ms to 581ms), with CPU at 39% and both CPU and disk queues at zero. Options seen: (a) force the landing with the hook-bypass flag, refused outright because the gate greps this file for that literal and bypassing discards the entire bar the authorization leaned on; (b) re-run the bar hoping the host recovers, refused because the canary controls expire on wall clock and the host is degrading rather than recovering, with foreign bars still running; (c) abort and hand the landing to the owner. Took (c). The work is merged to LOCAL main at 3214f39 and is complete; only the push to shared main is blocked, and the machine is what blocks it.

2026-08-20T03:11:30Z abort · item aMeteredTurnstile · reason The build is complete and merged to local main at 3214f39; this run aborts at the landing boundary because the merge bar cannot pass on this host. The run-gates canary's timing controls expire at every width, which is the canary correctly refusing to certify a clamp it could not observe, and the cause is the ~25x process-creation latency regression this build was opened to measure. Two parked decisions go to the owner: this one, and the pre-code spec audit M4 requires, which cannot be performed after the code without dating a pre-code pass after the code. Keepalive 2daed484 was deleted and the deletion read back, which returned no scheduled jobs.
