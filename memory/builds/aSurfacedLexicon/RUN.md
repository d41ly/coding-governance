# aSurfacedLexicon - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 6ee7d96a5a797f29d94309b504d9a5f64637cb1a
phase: REVIEWING
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
