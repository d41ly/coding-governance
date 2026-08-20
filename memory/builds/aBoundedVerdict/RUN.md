# aBoundedVerdict - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 324bfd5862353bcff81571056ca306b49a9c0098
phase: REVIEWING
mode: slug
anchor-kind: default-branch
keepalive: 6f555262
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 43a6c13e853ba6149600a2053cd439962413dc9d
anchor-ref: refs/heads/main
base: 43a6c13e853ba6149600a2053cd439962413dc9d

## Parked

2026-08-20T06:31:57Z decision · item TOOL-aBoundedVerdict-21 F3 — should a bounded-out push whose outcome is UNKNOWN wake the owner immediately, rather than wait for the resume path? · reason The owner raised this fork explicitly as theirs, not delegated, because the options differ in whether the unattended kit gains an owner-notification mechanism at all. Options seen: leave it to the resume path, as the spec already says, where a resumed run re-observes the remote and decides; or notify-and-stop, which surfaces the one state a finished run cannot resolve for itself. The run RESOLVED F3 to the specced option by VETO rather than by choice — notify-and-stop needs a new public surface this kit does not have, which is M3 veto 2, an owner turn — so the unit is buildable and its scope did not widen. But a veto is not an answer to the question the owner asked, and the vetoed option is the interesting one: a run that bounds out at the push has finished its work and cannot tell whether it landed, which is arguably the single state worth waking someone for. Parking it so the owner gets that turn.

2026-08-20T07:41:48Z decision · item TOOL-aBoundedVerdict-21 cannot be built as specced: S1 bounds a lander invocation the driver never makes, and every fix M3 leaves is vetoed by the unit's own Non-goals · reason Measured, not inferred: grep over the kit shows $LANDER appears at unattended.sh:65 (conf default), :1697 (an echo telling the agent what to run), :1745 (the bypass predicate), check-unattended.sh:48/54/765 (conf plumbing) and SKILL.template.md:271 (the fenced command the AGENT runs). The driver never invokes the lander, so S1's bound, S3's refusal and AC1/AC2/AC4/AC6 all assert over a code path with no host. Options seen: (a) add a --land verb that invokes $LANDER under the bound and writes the attempt fact — refused by M3 veto 1, because the unit's own section 3 Non-goals say 'No change to LANDER's value set, to which verb invokes it, or to the bypass ban', and a new verb is also a new public surface every adopter's rendered Skill and protocol carries; (b) move the bound into the rendered Skill — the whole of sections 2, 4 and 6 is written against the driver, so this is a rewrite of the unit rather than a fold, and a Skill instruction is an instruction rather than a bound; (c) prefix the rendered lander command with timeout — mechanical, but S4's attempt fact and S5's resume arm still need driver support, so it delivers the unknown-outcome state without the record that makes it recoverable, which the spec's own Alternatives section already rejects as strictly worse than the hang. No survivors after the vetoes, so M3 says park rather than take the least-bad option. Two consequences the owner should know. First, F1's 900s bound is separately dead: it was sized against 335s serial / ~95s at width 8, and the tracked figure at HEAD is 873s concurrent against a 4018s leg-sum, with .githooks/pre-push running the full bar INSIDE the push the deadline wraps — 900s leaves about 27s of margin and is 4.5x below the documented GATE_JOBS=1 rollback, so the bound as written converts a normal landing into a bounded-out one. Second, parking this unit means the authored region's fact pin now has exactly ONE mover this build (-2), which simplifies the coordination the README was corrected for this morning. The hung-push stall that TOOL-aBoundedVerdict-13 F3 raised therefore survives this build, and -13 already says so rather than implying the bound is complete.
