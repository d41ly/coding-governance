# aBoundedVerdict - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 43a6c13e853ba6149600a2053cd439962413dc9d
phase: SPECCING
mode: slug
anchor-kind: default-branch
keepalive: 6f555262
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 43a6c13e853ba6149600a2053cd439962413dc9d
anchor-ref: refs/heads/main
base: 43a6c13e853ba6149600a2053cd439962413dc9d

## Parked

2026-08-20T06:31:57Z decision · item TOOL-aBoundedVerdict-21 F3 — should a bounded-out push whose outcome is UNKNOWN wake the owner immediately, rather than wait for the resume path? · reason The owner raised this fork explicitly as theirs, not delegated, because the options differ in whether the unattended kit gains an owner-notification mechanism at all. Options seen: leave it to the resume path, as the spec already says, where a resumed run re-observes the remote and decides; or notify-and-stop, which surfaces the one state a finished run cannot resolve for itself. The run RESOLVED F3 to the specced option by VETO rather than by choice — notify-and-stop needs a new public surface this kit does not have, which is M3 veto 2, an owner turn — so the unit is buildable and its scope did not widen. But a veto is not an answer to the question the owner asked, and the vetoed option is the interesting one: a run that bounds out at the push has finished its work and cannot tell whether it landed, which is arguably the single state worth waking someone for. Parking it so the owner gets that turn.
