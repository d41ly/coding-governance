# aBoundedCeiling - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: d4eae035e0cec30f209f04f8c4842c3c996af4f5
phase: BUILDING
branch-sha: 1d83cc94eec944f8ecb3bae8e7186a545a58934c
branch-ref: refs/heads/branch/unattended-self-check-perf-373152
mode: prompt
anchor-kind: run-branch
keepalive: b8574078
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: f5dff6aee0b0a0177fac8ec842532b461eeca71f
anchor-ref: refs/heads/main
base: 1d83cc94eec944f8ecb3bae8e7186a545a58934c

## Parked

2026-08-26T22:53:15Z decision · item Should the close/land double bar be removed, which requires relaxing .githooks/pre-push predicate 5? · reason MEASURED: an unattended landing pays two full bars. --close runs $GATE_CMD and stamps a green; pre-push predicate 5 then fires — 'the pushed tip is a merge whose second parent the recorded green does not cover' — and forces a second, full bar. Predicate 5 is STRUCTURALLY unsatisfiable by a close-time bar whatever the environment, because --close writes the LANDING phase AFTER the gate and the agent then commits it, so HEAD always moves past the sha the green was earned at. OPTIONS SEEN: (1) relax predicate 5 to accept an ancestor within the existing lag bound — removes the second bar, and weakens the boundary that predicate's own header defends; (2) make gates-green verify a recorded green instead of running one — does NOT help, predicate 5 still fires; (3) move the close bar after the record commit — circular, the DoD gates the record. REFUSED because (1) widens what can land unverified, which is M3 veto 3, an owner turn that a standing mandate does not delegate.

2026-08-26T22:53:30Z decision · item Six abandoned processes are running on node a, one of them an adopter's --close hung for 3h19m with a dead parent. Kill them? · reason OBSERVED 2026-08-27 01:45, recorded with pids at memory/builds/aBoundedCeiling/build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md. Five belong to an ADOPTER repo (scripts/unattended/, scripts/gate.sh); one is gov's own orphaned check-memory-hygiene.sh, parent gone. Two have accumulated ZERO CPU across 2.5+ hours, so they are blocked rather than slow and will not end on their own. They are measurably degrading this node: this run's own commit hook ran at 3.7 percent CPU alongside 66 resident bash processes. OPTIONS SEEN: (1) kill by command line, which is the remedy memory/gotchas/bounded-through-a-pipe-is-unbounded.md records, after which a comparable hygiene run finished in 42s green; (2) leave them and let the owner decide. REFUSED to take (1): they are another repository's work and another session's, an abandoned process may still hold a scratch directory or an index someone intends to inspect, and process cleanup in a foreign tree is outside anything this build's mandate authorizes. There is no owner turn in an unattended run in which to ask, so it is parked with the pids rather than guessed.

2026-08-26T23:21:18Z review · item TOOL-aBoundedCeiling-1 · reason verdict BLOCKED · blockers 1

2026-08-26T23:50:28Z review · item TOOL-aBoundedCeiling-1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-27T00:59:28Z decision · item TOOL-aBoundedCeiling-5 is specced and only partly built. Land the build at 2.5 of 3 units, or hold for the rest? · reason BUILT AND VERIFIED: -1 (per-leg ceilings on gov's bar, both failing cases observed) and -6 (one bounded runner at both unbounded seams in the driver, four arms observed against the shipped function). Of -5, only S6 is built: the live KeyError in govkit's emitter below-floor path, which this build's own spec audit found and which is a defect fix that stands alone. NOT built: S1-S5 and S7 -- the ceiling key on kit descriptors, the emitter write, the version floor and its KIT_RUN_GATES_VERSION bump, the selfcheck check-7h parity arm, and the receipt-joined override predicate. WHY IT MATTERS LESS THAN IT LOOKS: the adopter half of the owner's ask is substantially met WITHOUT -5, because -6 ships in the unattended kit and bounds whatever gate command an adopter declares -- which is exactly the scripts/gate.sh case observed hanging on this node for 3h19m. -5 extends the PER-LEG ceiling to adopters, which is additive rather than load-bearing for the named symptoms. OPTIONS SEEN: (1) land 2.5 of 3 and carry -5 as a backlog row, which keeps two complete reviewed units moving and leaves the deployer work to a fresh build; (2) hold the whole branch until -5 is built, which delays the hang fix that is already verified. REFUSED to decide: -5 was scoped as a unit of THIS build on the strength of the owner's explicit 'and its adopters', so dropping it is a scope decision against a stated requirement rather than an amendment M2 delegates, and the run reached this point deep enough into one context that a fresh look is worth more than a fast call.

2026-08-27T03:33:42Z review · item aBoundedCeiling · reason verdict BLOCKED · blockers 6

2026-08-27T05:50:03Z review · item aBoundedCeiling · reason verdict BLOCKED · blockers 1
