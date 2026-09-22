# aSurfacedLexicon - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
landed-anchor: remote
units-at-landing: TOOL-aSurfacedLexicon-1 TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-10 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-12
unpushed-at-landing: 0
parked-surfaced: yes, 5 surfaced
keepalive-reaped: yes
witness: e1f453a9ddf15c53f862b75d73bb32a381259640
phase: LANDED
mode: slug
anchor-kind: default-branch
keepalive: 7c71fd36
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6c670b024644bf6bbcc28ee74d2265c0efd453c6
anchor-ref: refs/heads/main
base: 6c670b024644bf6bbcc28ee74d2265c0efd453c6

## Parked

2026-09-04T18:42:19Z decision · item TOOL-aSurfacedLexicon-10 fork F1: where does the --expand candidate computation live? · reason Both listed options are vetoed under M3, so no resolver the mandate delegates exists. Option B (compute in lexicon.py) fails veto 1: AC5 names the staged line by path as tools/lexicon/scaffold_lexicon.py:146, so under B the arm grades a lexicon.py copy and breaking :146 leaves it GREEN, removing the unit's only observed-RED criterion. Option A (a second entry point reached through a MODE FLAG) fails veto 3: it reverses the write guard at scaffold_lexicon.py:98, whose ten-line header records a real adopter (incms/main, 2026-08-23) committing and pushing a file literally named --help through a 62-leg bar because --help was a well-formed one-argument call. Section 5 prices this unit at 'writes at most one scalar'; a new write mode is beyond that. A veto is not a licence to take the vetoed option, so this is a park and not a least-bad pick. UNRATIFIED and for the owner: 'second entry point' and 'mode flag' are separable -- an importable derive_candidates() beside :146, reached from lexicon.py's existing dispatcher, keeps AC5's locus and touches no guard. A third route nobody listed: lexicon.py:1053-1136 (run_probe) already implements S3's candidate computation and S4's unruled tail, but TOOL-aSurfacedLexicon-3 deletes it at build order 1, five orders before this unit needs it. CONSEQUENCE: TOOL-aSurfacedLexicon-10 is not built by this run and does not close.

2026-09-04T19:31:29Z review · item TOOL-aSurfacedLexicon-2 · reason verdict BLOCKED · blockers 2

2026-09-04T19:31:30Z review · item TOOL-aSurfacedLexicon-3 · reason verdict BLOCKED · blockers 5

2026-09-04T19:31:31Z review · item TOOL-aSurfacedLexicon-4 · reason verdict BLOCKED · blockers 6

2026-09-04T19:55:00Z review · item TOOL-aSurfacedLexicon-2 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T19:55:01Z review · item TOOL-aSurfacedLexicon-3 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T19:55:02Z review · item TOOL-aSurfacedLexicon-4 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T20:26:52Z review · item TOOL-aSurfacedLexicon-5 · reason verdict BLOCKED · blockers 4

2026-09-04T20:26:53Z review · item TOOL-aSurfacedLexicon-6 · reason verdict BLOCKED · blockers 7

2026-09-04T20:26:54Z review · item TOOL-aSurfacedLexicon-9 · reason verdict BLOCKED · blockers 8

2026-09-04T21:15:39Z review · item TOOL-aSurfacedLexicon-5 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T21:15:40Z review · item TOOL-aSurfacedLexicon-6 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T21:15:42Z review · item TOOL-aSurfacedLexicon-9 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T21:48:41Z review · item TOOL-aSurfacedLexicon-13 · reason verdict BLOCKED · blockers 4

2026-09-04T21:48:43Z review · item TOOL-aSurfacedLexicon-14 · reason verdict BLOCKED · blockers 5

2026-09-04T21:48:44Z review · item TOOL-aSurfacedLexicon-7 · reason verdict BLOCKED · blockers 7

2026-09-04T22:19:03Z review · item TOOL-aSurfacedLexicon-13 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T22:19:05Z review · item TOOL-aSurfacedLexicon-14 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-04T22:19:06Z review · item TOOL-aSurfacedLexicon-7 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T01:25:01Z review · item TOOL-aSurfacedLexicon-8 · reason verdict BLOCKED · blockers 1

2026-09-05T01:25:02Z review · item TOOL-aSurfacedLexicon-11 · reason verdict BLOCKED · blockers 2

2026-09-05T01:25:03Z review · item TOOL-aSurfacedLexicon-12 · reason verdict BLOCKED · blockers 5

2026-09-05T01:56:13Z review · item TOOL-aSurfacedLexicon-8 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T01:56:13Z review · item TOOL-aSurfacedLexicon-11 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T01:56:14Z review · item TOOL-aSurfacedLexicon-12 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T02:01:00Z dispatch · item 8674f4f0 TOOL-aSurfacedLexicon-2 · reason tools/lexicon/lexicon.py tools/lexicon/selftest.py tools/lexicon/kit.toml tools/lexicon/README.md tools/lexicon/LEXICON.md tools/lexicon/adopt-lexicon.sh tools/lexicon/SKILL.template.md .claude/skills/lexicon/SKILL.md .lexicon.conf memory/map/features/lexicon.md memory/map/generated/symbols.json coding-governance-agents.template.md AGENTS.md

2026-09-05T03:27:36Z dispatch · item e6af6206 TOOL-aSurfacedLexicon-4 · reason tools/lexicon/lexicon.py tools/lexicon/lexicon_conf.py tools/lexicon/subtokens.py tools/lexicon/selftest.py tools/lexicon/README.md .lexicon.conf memory/map/features/lexicon.md

2026-09-05T05:49:23Z dispatch · item e354db0a TOOL-aSurfacedLexicon-14 · reason tools/lexicon/lexicon.py tools/lexicon/selftest.py tools/lexicon/README.md .lexicon.conf

2026-09-05T12:03:59Z dispatch · item 2d487019 TOOL-aSurfacedLexicon-11 · reason tools/lexicon/lexicon.py tools/lexicon/canon.py tools/lexicon/lexicon_conf.py tools/lexicon/selftest.py .lexicon.conf tools/lexicon/README.md

2026-09-05T21:26:36Z review · item aSurfacedLexicon · reason verdict BLOCKED · blockers 7

2026-09-05T22:56:07Z review · item aSurfacedLexicon · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-06T02:51:27Z override · item gates-green · reason The bar does not RETURN within GATE_BOUND, and the cause is one leg that breached its own ceiling before this build existed. pass-order history declares ceiling 900 and needs 4438s at this tip; measured at the pinned BASE 6c670b02 it needs 4067s, already 4.5x over, and it exits 0 with a CLEAN verdict at both points. Filed as TOOL-aSurfacedLexicon-22 with both measurements. Every other leg was run directly and is green: lexicon selftest 509 arms, lexicon --check, adopt-lexicon --check, adopt-playbook --check, drift-audit selftest, drift_report --check, codebase-map coverage+freshness, memory hygiene (unstaged, so check 23 binds), check-spec-tokens, govkit selfcheck, check-testsuite-counts, check-dead-paths, check-kit-placeholders, check-line-length, check-install-prefix, template-size on both charter halves. This is an override of a bar that never returned, not of a leg that failed.

2026-09-06T02:51:28Z override · item build-complete · reason TOOL-aSurfacedLexicon-10 is SPECCED and was never built. Its fork F1 lost BOTH options to the M3 veto ladder: option B fails a written acceptance criterion that names the staged line by path, and option A widens a write surface beyond what the unit tier priced, reversing a guard whose header records a real adopter committing a file named --help through a 62-leg bar. A veto is not a licence to take the vetoed option, so no resolver this mandate delegates exists and the fork is PARKED for the owner. M8 says a blocker unfixable inside the mandate is a park and its unit does not close. The other twelve units are CLOSED with acceptance ledgers.

2026-09-06T02:51:28Z override · item specs-audited · reason TOOL-aSurfacedLexicon-1 arrived CLOSED at the pinned BASE: it is the design pass, built and closed by the session that wrote this spec set, before this run existed. Its code predates this run and no spec-audit record names it. Writing one now would claim a pre-code review that did not happen, which is the one thing an audit record must not do. The twelve units this run BUILT were each audited before their code, across four batches, every one converged, and both rounds of each are recorded under the build reviews folder.

2026-09-06T06:10:21Z decision · item The push to origin/main is BLOCKED by one leg, and the ceiling raise this run made was not enough. · reason The full bar is green on 43 of 44 legs. The one red is pass-order history, which is not this build's defect: measured 4067s at the pinned BASE over 45 closed units and 4438s at the merged tip over 58, exiting 0 with a CLEAN verdict at both points, against a ceiling that was 900 and then 2400 and has never once been met -- the gate ledger holds exactly one row for this leg and it is the kill. This run re-declared it to 5400s, which is the sanctioned interim under the fix-or-re-declare rule, and it STILL timed out: inside the bar at width 8 the leg contends and costs materially more than the quiet measurement, which is a known ~3x inflation in this repo. WHAT I REFUSED TO DO, and why it is the owner's call rather than mine: raise the ceiling again by guess. A ceiling that covers the contended run is roughly 13000s, which is inside this repo's existing range but puts a THREE AND A HALF HOUR floor under every full bar, since wall clock cannot fall below the longest leg. Imposing that on every future push on my own authority is a cost decision nobody reviewed, and each guess costs ninety minutes to test. Bypassing the gate is forbidden by the protocol and grepped for. THE WORK IS LANDED ON LOCAL MAIN: the merge is committed, every conflict reconciled additively, every generated artifact re-rendered, and the manifest re-stamped post-merge. What is missing is only the push. The owner decides between raising the ceiling with a measured contended figure, moving this leg off the wall-clock bar to an on-demand runner the way the kit self-tests went by owner ruling, or fixing the walk. TOOL-aSurfacedLexicon-22 holds the measurements and both real remedies.

2026-09-06T09:24:36Z review · item TOOL-aSurfacedLexicon-10 · reason verdict CLEAN WITH FIXES · blockers 1

2026-09-06T10:14:15Z review · item TOOL-aSurfacedLexicon-10 · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold

2026-09-06T13:55:44Z override · item specs-audited · reason TOOL-aSurfacedLexicon-1 arrived CLOSED at the pinned BASE: it is the design pass, built and closed by the session that wrote this spec set, before this run existed. Its code predates this run and no spec-audit record names it. Writing one now would claim a pre-code review that did not happen, which is the one thing an audit record must not do. UNCHANGED FROM THE PREVIOUS CLOSE and narrower than it: that close carried this override for TWO units, -1 and -10. TOOL-aSurfacedLexicon-10 now HAS its spec-audit record, written before its code on the owner turn that resolved its fork, so this override covers -1 alone. Every other unit this run built was audited before its code, both rounds recorded under the build reviews folder.
