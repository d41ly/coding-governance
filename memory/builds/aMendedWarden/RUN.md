# aMendedWarden - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
halt-code: repo-state-out-of-mandate
parked-surfaced: yes, 2 surfaced
keepalive-reaped: yes, CronDelete returned 'Cancelled job 19b465ac' and CronList then returned 'No scheduled jobs'
witness: 2724ab913359023b2ec3ff6f421b61b7b1df48d2
phase: ABORTED
branch-sha: 2724ab913359023b2ec3ff6f421b61b7b1df48d2
branch-ref: refs/heads/branch/backlog-review-prioritize-f617d8
mode: prompt
anchor-kind: run-branch
keepalive: 19b465ac
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4b0051ae8db155299fa1c4a31ae61febe76ccdce
anchor-ref: refs/heads/main
base: 2724ab913359023b2ec3ff6f421b61b7b1df48d2

## Parked

2026-09-04T14:38:11Z decision · item How should the diverged default branch be reconciled: local main is 17 commits ahead of origin/main and 108 behind it, merge-base 51444cc1 dated 2026-09-02? · reason Options seen: (a) merge origin/main into local main and push, (b) rebase the 17 local commits onto origin/main, (c) leave it for the owner. REFUSED all three. The 17 local-only commits are a whole landed build (aCollapsedScan) that exists on this box and nowhere else, and the lander reconciles the remote before the gate, so an unattended run choosing any of (a)(b) would resolve a 125-commit divergence over unpushed work with no owner turn. Template section 1 Landing and the mandate delegate a build's own scope, not the repository default branch's history.

2026-09-04T14:38:21Z decision · item Should this run rescope onto origin/main and build only the units still live there, instead of aborting? · reason Measured on origin/main, not inferred from commit subjects: four of the ten units are ALREADY CLOSED upstream — U4 verb_landed writes landed-anchor at unattended.sh:2444 and phase LANDED at :2445 with a comment naming the old ordering (d19cf7d7), U5 govkit carries pathspec-from-file at six sites, U6 carries the DEPL-dRatifiedSeam-1 S3 unclaimed-source block at govkit.py:6989 (3fe56d56), U9 ships playbook.fixture.template.md (c1bed039). Five stay live (U1 renderBlankedView mode at :1041 outside the loop at :1042, U2 the for|while predicate at :705/:738/:934 with no for-await arm, U3, U7 zero RUN INTEGRITY in tier2-review.js, U10 the naive conf strip at gotchas.py:92) and U8 is uncertain because check-wiring.sh changed. Options seen: (a) rescope-retire the four and continue, (b) abort. REFUSED (a): the pinned BASE 2724ab91 is 108 commits behind the remote, so continuing needs a new BASE, and a new BASE needs a new preflight on a clean tree — which would have this run re-authorize itself on an anchor it wrote. The roster is not the blocker; the base is.

2026-09-04T14:38:44Z abort · item aMendedWarden · reason Local main has DIVERGED from origin/main: 17 commits ahead, 108 behind, merge-base 51444cc1 (2026-09-02). That is the session-kickoff Step 1 STOP condition, and Step 5b exit 3 routes it to an abort rather than a guess. Two consequences, both measured. FIRST, the run BASE 2724ab91 sits 108 commits behind the remote and the lander reconciles the remote before the gate, so this run would have resolved a 125-commit divergence over 17 unpushed commits of an already-landed build with no owner turn. SECOND, the triage that produced the roster measured at d0a18683, which is those same 108 commits stale, and four of the ten units are already closed on origin/main - verified in the code, not from commit subjects: U4 at unattended.sh:2444-2445, U5 pathspec-from-file in govkit.py, U6 at govkit.py:6989, U9 playbook.fixture.template.md. Five remain live (U1 U2 U3 U7 U10) and U8 is uncertain. Nothing was built and nothing was merged.
