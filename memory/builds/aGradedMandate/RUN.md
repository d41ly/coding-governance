# aGradedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
units-at-landing: TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11
unpushed-at-landing: 0
landed-anchor: remote
parked-surfaced: yes, 6 surfaced
keepalive-reaped: yes
witness: 1bf012fcc205d0b63e434d679518aaa9bf99e4e8
phase: LANDED
branch-sha: 54309e9c565d30b695ba353adfb8503a3a98dfee
branch-ref: refs/heads/branch/unattended-kit-adversarial-review-6810dc
mode: prompt
anchor-kind: run-branch
keepalive: 61c79592
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 396cd9db154f1621db5cb4cde72b93470b2f690c
anchor-ref: refs/heads/main
base: 54309e9c565d30b695ba353adfb8503a3a98dfee

## Parked

2026-08-30T23:41:31Z review · item aGradedMandate-specs · reason verdict BLOCKED · blockers 2

2026-08-30T23:46:23Z rescope · item retire TOOL-aGradedMandate-3 · reason The spec audit's round-1 BLOCKER F1: every implementation that buys anything in this repository reverses the owner ruling of 2026-08-27 recorded in .githooks/gate-env.sh, and the in-driver form is refused independently by govkit selfcheck check 7h3 because kit.toml ships that file to every adopter. F3 also measured the proposed intersection firing on 100% of closes, since the recall floor arms leg guards memory/ and every unattended run commits under it. Retired at rev-2 before any code; the fork and its five options are the spec's section 8 and are parked

2026-08-30T23:46:34Z decision · item Should a --close whose diff touches a held self-test leg's guard path run that leg? Today 46 of 86 legs are held, no carrier an unattended run reads even names GATE_SELFTESTS, and a run that edits a checker lands with none of that checker's arms exercised. · reason OPTIONS SEEN. (a) export GATE_SELFTESTS=1 inside tools/unattended/unattended.sh, refused by govkit selfcheck check 7h3 because kit.toml ships that file verbatim to every adopter and a repo-local policy may not ride out in a kit payload. (b) Set it in .githooks/gate-env.sh, which IS the sanctioned repo-local channel, and which is a straight reversal of the owner ruling of 2026-08-27 whose recorded reason is that the cost lands on every push including the majority that touch no kit source. (c) A .unattended.conf key defaulting OFF so the mechanism travels and the choice does not, lawful but inert here unless gov declares it ON, which is (b) wearing a longer name. (d) A new Definition-of-Done item reading a RECORDED self-test verdict joined to the kit tree state, a new public record surface and M3 veto 2. (e) Retire the unit and park the fork. WHY I REFUSED. Every option that buys anything in this repository is an owner turn: (b) reverses a dated ruling, (c) and (d) trip M3 veto 2, and M3 is explicit that a veto is not a licence to take the vetoed option. TWO MEASUREMENTS THE OWNER NEEDS. The gap is real, 46 of 86 legs held and zero mentions of the flag in any kit carrier; and the naive fix is worse than it looks, because the recall floor arms leg guards memory/ so the intersection fires on every unattended close, at a bar this repo sizes near 26 minutes of wall at width 8 and roughly twice that on a width-2 profile row, which breaches GATE_BOUND

2026-08-31T02:41:12Z review · item aGradedMandate-specs · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-31T02:45:14Z rescope · item add TOOL-aGradedMandate-10 · reason PROMOTED from round 2 of the spec audit, blocker R1, under the build method M4 exit rule: the loop went 2 blockers then 2 blockers, did not shrink, and stopped NON-CONVERGENT, so every blocker still standing becomes a unit rather than a fold. R1 is that unit 5 makes the OWED side of the parked split act-aware while park_kinds_unowed still subtracts at kind granularity, so a rescope retire row matches both alternations and --status reports one retirement as a decision AND as a note. Split from unit 5 rather than folded into it because the owed side and the history side are two mechanisms and M2 allows one per spec

2026-08-31T02:45:15Z rescope · item add TOOL-aGradedMandate-11 · reason PROMOTED from round 2 of the spec audit, blocker R2, under the same M4 exit rule. R2 is that unit 1's AC7 invoked the charter rule to run a candidate gate predicate over the real tree before wiring it and then answered it from memory: it pinned three expected hits where the executed predicate returns twenty-one over 28 tracked records. The unit produces the census as a committed journal record and rewrites AC7 to read it

2026-08-31T03:08:36Z review · item aGradedMandate-promoted · reason verdict BLOCKED · blockers 1

2026-08-31T10:09:23Z decision · item The gate-leg self-test suite (check-unattended.test.sh) was NOT run over this build's leg-side units, on an explicit owner instruction to skip it mid-run. · reason WHAT IS THEREFORE UNVERIFIED, stated rather than implied away. Units 6, 7 and 9 and unit 5's leg half edit tools/unattended/check-unattended.sh and tools/unattended/lib-unattended.sh, and that suite is the only thing that stages breaks into those checkers and asserts they still catch them. WHAT IS VERIFIED WITHOUT IT, each observed directly. The leg itself runs GREEN on this tree end to end. Check 16d was observed RED in both directions against staged breaks: a driver DOD_NO_OVERRIDE carrying a bogus member fired the driver-side refusal, and a Skill paragraph naming an invented item fired the Skill-side one. The act-axis arm was observed RED against PARK_ACTS_OWED set to supercede. Check 16d's empty-population refusal was verified by running its own awk selector over a Skill whose sentence had been removed, which yields zero lines. WHAT REMAINS UNOBSERVED: the failing case of check 24's rekeyed RETIRE arm and of check 2's non-WONTDO promotion filter. Both need a multi-commit record fixture with phase history and a units-region delta, which is what that suite exists to build. The driver suite IS green at 895 assertions, so the driver-side units are covered

2026-08-31T10:55:38Z review · item aGradedMandate · reason verdict BLOCKED · blockers 1

2026-08-31T12:08:31Z decision · item The gate-leg self-test suite was not merely UNRUN, it was RED, and this run repaired it without re-running it. · reason FOUND BY THE CLOSING REVIEW, finding H2, after the owner had already instructed the skip. Three check-24 arms in check-unattended.test.sh asserted a message string this build deleted, so grep -c for it against the leg returned 0 and hit() could not pass; and seed_ros pinned its fixture base: to git merge-base origin/main HEAD, a commit predating the fixture build folder entirely, so pinned_units would have REFUSED and the rekeyed RETIRE arm would have SKIPPED rather than graded even once the strings matched. Both are repaired in this build: the arm strings now match the shipped messages, verified by grep in both directions, and seed_ros pins the commit that actually carries the units region. WHAT I REFUSED TO DECIDE: whether the repair works, because verifying it means running the suite the owner told me to skip, and I read that instruction as standing rather than as scoped to the one invocation in flight. WHY IT MATTERS TO THE OWNER: an unrun suite and a broken suite are different states, and run-unattended-gates.sh names a GREEN --selftests verdict as the DoD for any work touching this kit, which was unobtainable before this repair and is untested after it. The next person to run that suite should expect either green or a fixture defect, not a defect in the checkers

2026-08-31T12:08:32Z decision · item The merge to main and the push have NOT happened, and this run cannot perform them. · reason tools/push-main.sh refuses when HEAD is not the default branch, by design, because it lands main from the primary tree; and this session's environment forbids leaving its worktree or cd-ing to the repository root. OPTIONS SEEN. (1) Run the lander through git -C against the primary tree, refused because it is the same act the instruction forbids and because the primary tree may hold another session's work. (2) Abort, refused because the build is complete and an abort would misrepresent it. (3) Park, taken, which is what aScouredKit did at the same wall on 2026-08-30. TO LAND: from the primary tree on main, git merge --no-ff branch/unattended-kit-adversarial-review-6810dc then bash tools/push-main.sh, then bash tools/unattended/unattended.sh --landed aGradedMandate WITHOUT committing anything in between, because check 34 compares the lander marker to HEAD by equality. NOTE FOR THE MERGE: several sibling worktrees were running this same kit's suites throughout this build, and one of them is branch/unattended-builds-blocking-640d0d, so expect a real reconcile on tools/unattended/ rather than a clean fast-forward

2026-08-31T13:17:30Z decision · item The merge to LOCAL main was performed BEFORE --close evaluated the Definition of Done, which inverts the protocol's order. · reason OWNER INSTRUCTION, given mid-session: this session is running out of limits, merge what is already built to local main just in case. The protocol's order is --close then land, so that a merge never carries work the Definition of Done has not passed. Taken deliberately and recorded rather than smoothed over. WHAT THE MERGE CARRIES THAT --close HAS NOT GRADED: the full merge bar has not run on the merged tip, so gates-green is unevaluated; specs-audited, build-complete and closing-review-recorded are unevaluated; and round 2 of the closing diff review was still in flight when the merge was made. WHAT IS KNOWN: the gate leg was green on the pre-merge branch tip, the driver suite was green at 895 assertions before the closing fold and was re-running when the merge was made, and every conflict in both reconciles was resolved additively with the two semantic ones stated in the merge message. NOTHING IS PUSHED. Local main is 21 commits ahead of origin/main and the push remains an owner act

2026-08-31T13:34:46Z review · item aGradedMandate · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED
