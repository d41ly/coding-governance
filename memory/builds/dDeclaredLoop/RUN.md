# dDeclaredLoop - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 96526383cd50d5e04e87a311971fc8776b764710
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-declared-loop-82e374
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-24T08:52:36Z
pid-image: claude.exe
host: compeeto
pid: 32640
session: fe9ab66e-8bde-4f94-90b4-e764fe4c1760
keepalive: 5ced0c78
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: ed497191df0d973f903426cedc30f0ba6eb80d24
anchor-ref: refs/heads/main
base: ed497191df0d973f903426cedc30f0ba6eb80d24

## Parked

2026-10-24T11:09:26Z rescope · item add TOOL-dDeclaredLoop-36 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 35 HIGH, item H12: a default govkit apply refuses because loop is not in the registry's default selection; repairs TOOL-dDeclaredLoop-1

2026-10-24T11:09:41Z rescope · item add TOOL-dDeclaredLoop-37 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 8 HIGH, item H8: no criterion observes the trailer re-points, every one a base-versus-tree equality green before the build; repairs TOOL-dDeclaredLoop-23

2026-10-24T11:09:42Z rescope · item add TOOL-dDeclaredLoop-38 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 18 HIGH, item H9: the trailer CLI writes CRLF on win32 and a final token is silently dropped; repairs TOOL-dDeclaredLoop-23

2026-10-24T11:09:43Z rescope · item add TOOL-dDeclaredLoop-39 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 19 HIGH, item H10: read_commits drops the replace-ref, graft and env-leak pins the readers it replaces carry; repairs TOOL-dDeclaredLoop-23

2026-10-24T11:09:43Z rescope · item add TOOL-dDeclaredLoop-40 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 47 HIGH, item H13: the trailer reader refuses every key where edges.toml is absent; repairs TOOL-dDeclaredLoop-23

2026-10-24T11:09:44Z rescope · item add TOOL-dDeclaredLoop-41 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 48 HIGH, item H14: the actor-witness list wedges every adopter; repairs TOOL-dDeclaredLoop-5

2026-10-24T11:09:45Z rescope · item add TOOL-dDeclaredLoop-42 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 51 HIGH, item H17: the acceptance re-run timeout bounds nothing through a pipe and runs bash syntax under cmd.exe; repairs TOOL-dDeclaredLoop-17

2026-10-24T11:09:45Z rescope · item add TOOL-dDeclaredLoop-43 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 49 HIGH, item H15: write_guarded deletes the owner's policy file on a failed write; repairs TOOL-dDeclaredLoop-2

2026-10-24T11:09:46Z rescope · item add TOOL-dDeclaredLoop-44 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 50 HIGH, item H16: the policy push arm leaves merge commits and an all-zero base undefined; repairs TOOL-dDeclaredLoop-2

2026-10-24T11:09:47Z rescope · item add TOOL-dDeclaredLoop-45 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 6 HIGH, item H6: built needs an acceptance record nothing writes in a real run; repairs TOOL-dDeclaredLoop-7

2026-10-24T11:09:48Z rescope · item add TOOL-dDeclaredLoop-46 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 25 HIGH, item H11: the stage field skips govkit's emitter, the kit descriptors and selfcheck 7h; repairs TOOL-dDeclaredLoop-4

2026-10-24T11:09:48Z rescope · item add TOOL-dDeclaredLoop-47 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 3 HIGH, item H3: the stage factory writes a step the loop definition leg must refuse; repairs TOOL-dDeclaredLoop-6

2026-10-24T11:09:49Z rescope · item add TOOL-dDeclaredLoop-48 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 7 HIGH, item H7: the budget refuses every draw under a channel set without log; repairs TOOL-dDeclaredLoop-30

2026-10-24T11:09:50Z rescope · item add TOOL-dDeclaredLoop-49 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 52 HIGH, item H18: the budget's spent resets at every transition record; repairs TOOL-dDeclaredLoop-30

2026-10-24T11:09:50Z rescope · item add TOOL-dDeclaredLoop-50 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 2 HIGH, item H2: the four review item rows break the program and actor checks; repairs TOOL-dDeclaredLoop-20

2026-10-24T11:09:51Z rescope · item add TOOL-dDeclaredLoop-51 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 1 HIGH, item H1: the eight recommendation rows are re-added with actors the declaration check refuses; repairs TOOL-dDeclaredLoop-22

2026-10-24T11:09:52Z rescope · item add TOOL-dDeclaredLoop-52 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 4 HIGH, item H4: the phase-to-step table no unit ships as code; repairs TOOL-dDeclaredLoop-19

2026-10-24T11:09:52Z rescope · item add TOOL-dDeclaredLoop-53 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 54 HIGH, item H19: default plan-only holds every in-flight run; repairs TOOL-dDeclaredLoop-19

2026-10-24T11:09:53Z rescope · item add TOOL-dDeclaredLoop-54 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 5 HIGH, item H5: the termination rule demands terminal sets the feature and unit tables lack; repairs TOOL-dDeclaredLoop-33

2026-10-24T11:09:54Z rescope · item add TOOL-dDeclaredLoop-55 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) id 55 HIGH, item H20: the loop termination leg's guard misses most of its inputs; repairs TOOL-dDeclaredLoop-33

2026-10-24T11:09:55Z rescope · item add TOOL-dDeclaredLoop-56 · reason spec-audit round 1 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) the 47 confirmed minors batched into one unit: 44 MEDIUM, ids 9 10 11 13 14 15 16 17 20 21 22 23 26 27 28 29 30 31 32 33 36 37 38 39 40 41 42 43 44 45 46 53 56 57 58 59 60 61 62 63 64 65 66 67 (items M1 to M37), and 3 LOW, ids 12 24 34 (items L1 to L3)

2026-10-24T11:39:57Z review · item dDeclaredLoop-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 20 · minors 47 · disposition promote

2026-10-24T12:32:48Z rescope · item add TOOL-dDeclaredLoop-57 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 52 HIGH, item H6: update's default-gained path can leave roles updated without the loop kit it requires; repairs TOOL-dDeclaredLoop-36

2026-10-24T12:32:59Z rescope · item add TOOL-dDeclaredLoop-58 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 51 HIGH, item H5: AC1's tokens HEAD~3..HEAD over a three-commit fixture never observes the LF-only fix; repairs TOOL-dDeclaredLoop-38

2026-10-24T12:33:00Z rescope · item add TOOL-dDeclaredLoop-59 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 17 HIGH, item H2: the diff-tree --cc --name-only grade lists a cleanly auto-merged policy file, so landing wedges; repairs TOOL-dDeclaredLoop-44

2026-10-24T12:33:01Z rescope · item add TOOL-dDeclaredLoop-60 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 19 HIGH, item H3: the budget reader drops draws stored in rotated run records and globs a literal memory root; repairs TOOL-dDeclaredLoop-48

2026-10-24T12:33:02Z rescope · item add TOOL-dDeclaredLoop-61 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 53 HIGH, item H4 (shared with id 38): a draw row carries no unique field, so two identical parallel draws merge into one and the budget under-counts; repairs TOOL-dDeclaredLoop-49

2026-10-24T12:33:03Z rescope · item add TOOL-dDeclaredLoop-62 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 38 HIGH, item H4 (shared with id 53): merge=union collapses two identical draw rows and reintroduces a driver .gitattributes records as rejected; repairs TOOL-dDeclaredLoop-49

2026-10-24T12:33:04Z rescope · item add TOOL-dDeclaredLoop-63 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 56 HIGH, item H8: the phase map covers PHASES_CORE only, so every --phase move into an adopter's extra phase is refused; repairs TOOL-dDeclaredLoop-52

2026-10-24T12:33:05Z rescope · item add TOOL-dDeclaredLoop-64 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 57 HIGH, item H9: the pre-placement rule finds a build's opening commit at a literal memory path, so a non-default root holds every build; repairs TOOL-dDeclaredLoop-53

2026-10-24T12:33:06Z rescope · item add TOOL-dDeclaredLoop-65 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 55 HIGH, item H7: the stale-remote reading uses the tracking ref's reflog, which a fresh clone and a no-op fetch never write; repairs TOOL-dDeclaredLoop-56

2026-10-24T12:33:06Z rescope · item add TOOL-dDeclaredLoop-66 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) id 1 HIGH, item H1: build-order groups derive Parallel yes for units whose write sets intersect; repairs no unit in particular

2026-10-24T12:33:12Z rescope · item add TOOL-dDeclaredLoop-67 · reason spec-audit round 2 (reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) the 54 confirmed minors batched into one unit: 38 MEDIUM, ids 2 3 4 5 6 7 8 9 10 11 18 20 21 22 23 24 25 26 27 33 35 36 39 40 41 42 43 44 45 46 47 54 61 62 63 64 65 66 (items M1 to M31), and 16 LOW, ids 12 13 14 15 16 28 29 30 31 37 48 49 50 60 67 68 (items L1 to L12)

2026-10-24T13:03:10Z review · item dDeclaredLoop-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 10 · minors 54 · disposition promote
