# aGatheredDeclaration - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
keepalive-reaped: yes
parked-surfaced: yes, 3 surfaced
witness: d7d3883f03a19475a1a4bec6e32cb77a9091c38f
phase: BUILDING
branch-sha: 44734f152c0f6a2d7ea5c6438dc969de8a7e9f33
branch-ref: refs/heads/branch/gate-bar-tooling-review-020565
mode: prompt
anchor-kind: run-branch
keepalive: 5d32537e
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 14e21399f7dd0559224837a2754fcbf9fc4a754b
anchor-ref: refs/heads/main
base: 44734f152c0f6a2d7ea5c6438dc969de8a7e9f33

## Parked

2026-08-30T22:42:29Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 5

2026-08-30T22:43:33Z rescope · item add TOOL-aGatheredDeclaration-8 · reason F9 and F29 of the round-1 spec audit: unit 2's S6 lanes and S7 tool probe cannot be built without rewriting the dispatch loop (one pool at one width, one global longest-first hint), which S2 asserts does not change and Section 5 prices as no regression. R3 of the architecture record reaches the same place from the migration side — a behaviour change inside a format change is unreviewable. Lanes and the tool probe become their own unit so unit 2 is provably behaviour-neutral.

2026-08-30T23:16:43Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 4

2026-08-30T23:46:31Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 3

2026-08-31T02:27:36Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT

2026-08-31T10:49:50Z decision · item Do units 6 and 8 close on a descoped scope, or does this build hold until their remainders ship? · reason Unit 6 shipped the push boundary and the entry-point fold; nine readers, govkit's toml-legs grammar, the 68-row descriptor migration and the deletion of the legacy pair did not. Unit 8 shipped its tool probe; the lane dispatcher did not. Options seen: (a) hold the build until both are whole, which blocks a verified subset behind work whose value is currently zero — gov keeps one lane and the legacy pair is deliberately permanent as the pre-3.11 floor; (b) close on the descoped scope and carry the remainders as TOOL-aGatheredDeclaration-9 and -10. I took (b) and recorded it in each spec's section 9 and in the README. Refused to decide alone whether that is the right trade for the FLEET: the unmoved readers are gov-internal, but govkit's missing toml-legs grammar means an adopter cannot take this format through the deployer at all, only by running --upgrade by hand.

2026-08-31T10:50:03Z decision · item Should ceilings ship OFF for a JSON manifest too, or only where the TOML declares it? · reason A JSON manifest declares no [bar], so I made the shipped default apply there as well: the owner's ruling is about what a ceiling COSTS, not which format declared it. That means a legacy-pair tree — including every pre-3.11 adopter — also gets enforcement off, and those are the trees least likely to notice. Options seen: scope the default to TOML only, which would leave two behaviours for one ruling; or apply it everywhere, which is what I did. Refused to decide alone because it changes an adopter's bar without their declaration saying anything.

2026-08-31T10:50:05Z decision · item Eleven mediums and three lows from the closing review remain OPEN and unfiled. · reason All four blockers and all eight highs are fixed. The remainder is listed in memory/builds/aGatheredDeclaration/reviews/2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md with file:line and a fix each — among them --manifest creating a run dir while declared read-only, the BUDGET_* ceilings the unattended wrapper still declares and nothing enforces, and the gov canary's guard naming only the JSON so a declaration-only edit skips its own grader. I did not file them as backlog rows because that would scatter one review across fourteen rows; the record is the better carrier. Refused to decide alone whether they block the landing.
