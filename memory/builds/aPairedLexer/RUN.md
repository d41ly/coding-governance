# aPairedLexer - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 638c888e54ef8eef71efa8b4bfa6437818c81c55
phase: BUILDING
branch-sha: 72dff924d77c5a482a01150141da31e4bdd52334
branch-ref: refs/heads/branch/paired-lexer-followup-9c31a2
mode: prompt
anchor-kind: run-branch
keepalive: 77db67c6
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 14e21399f7dd0559224837a2754fcbf9fc4a754b
anchor-ref: refs/heads/main
base: 72dff924d77c5a482a01150141da31e4bdd52334

## Parked

2026-08-30T21:39:54Z review · item aPairedLexer · reason verdict BLOCKED · blockers 2

2026-08-30T21:39:55Z review · item aPairedLexer · reason verdict BLOCKED · blockers 5 · NON-CONVERGENT

2026-08-30T22:21:57Z review · item spec-audit-6-through-12 · reason verdict BLOCKED · blockers 7

2026-08-30T23:04:28Z review · item spec-audit-6-through-12 · reason verdict BLOCKED · blockers 5

2026-08-30T23:43:31Z review · item spec-audit-6-through-12 · reason verdict BLOCKED · blockers 4

2026-08-31T02:42:44Z review · item spec-audit-6-through-12 · reason verdict BLOCKED · blockers 5 · NON-CONVERGENT

2026-08-31T04:23:27Z review · item promoted-units-6-through-12 · reason verdict BLOCKED · blockers 5

2026-08-31T05:09:40Z review · item promoted-units-6-through-12 · reason verdict BLOCKED · blockers 5 · NON-CONVERGENT

2026-08-31T05:11:44Z decision · item The ambiguity-routing design is refuted: falling back to the per-line view is NOT the fail-closed direction, so units 6, 9, 10 and 11 rest on a false premise. Redesign or revert — the owner's call. · reason MEASURED, not argued. 'dirty' does not deny; it routes all four rules onto stripStrings(l).split('//')[0], and that view sees STRICTLY LESS on some lines: stripStrings leaves backticks alone and the // split truncates inside a template literal. Probe: 'const REF = /\.ref\b/' above a line holding a backtick URL and a raw primitive. The paren-safe view renders the primitive VISIBLE; the fallback renders 'const u = `see http:' with it GONE. The script flips DENY to ADMIT purely by raising dirty. OPTIONS SEEN. (a) Keep routing and accept that dirty is sometimes a fail-open — refused, it is the defect the build exists to close. (b) Make the fallback view strictly stronger than the paren-safe one, so routing to it can only ever see MORE. That is the real fix and it is a redesign of a view every rule reads, not a patch. (c) Deny instead of routing when a view is not clean — fail-closed and simple, but its false-DENY cost is unmeasured and it would re-break the lens-prompt admit class TOOL-aPairedLexer-2 was built for. (d) Revert the whole build to 14e21399. WHY I REFUSED TO DECIDE. M3 veto 2: (b) and (c) both change a mechanism every rule depends on, which is beyond what the mandate delegates; and the fork I already ratified in unit 8 section 8 F1 chose option (c) of THAT fork on the stated grounds that routing was 'the only option that is not fail-open' — that reasoning is now refuted by measurement, so the ratification rested on a false premise and is the owner's to revisit rather than mine to re-ratify.
