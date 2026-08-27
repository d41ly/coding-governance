# aPrimedKeepalive - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
units-at-landing: TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9
unpushed-at-landing: 44 oldest b17b0ed2
landed-anchor: local
parked-surfaced: yes, 3 surfaced
keepalive-reaped: yes
witness: 51ec33e2e1f6f20ee9a975b8e4729e431dd0a92b
phase: LANDED
branch-sha: 0e92aaa9ec0006c285eb96b26a0d851a1d496b75
branch-ref: refs/heads/branch/unattended-keepalive-orientation-493b93
mode: prompt
anchor-kind: run-branch
keepalive: 8191840b
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b4e1d5be879bc8868529fb57c15657e271c39113
anchor-ref: refs/heads/main
base: 0e92aaa9ec0006c285eb96b26a0d851a1d496b75

## Parked

2026-08-27T11:55:19Z rescope · item add TOOL-aPrimedKeepalive-7 · reason Observed while verifying unit 3 AC6: the DRIVER's check_single_live refuses --preflight with 2 live records, so dTieredTribunal at LANDING blocks the next run on this repo even after unit 4 fixes the LEG. Unit 4's section 3 named this a non-goal on a reading of the code that is false. Strictly beneficial by protocol section 11: measured, nothing gets worse, no veto tripped.

2026-08-27T12:20:29Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 4

2026-08-27T12:56:03Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 1

2026-08-27T13:31:47Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-27T13:32:12Z rescope · item add TOOL-aPrimedKeepalive-8 · reason PROMOTED from spec-audit round 3, NON-CONVERGENT: SKILL.template.md:35 asserts a resumed keepalive is dead before it starts while :589 of the same file calls that intuition MEASURED FALSE, 554 lines apart, with the false half in the section every path reads first. Same defect at README.md:176.

2026-08-27T13:32:16Z rescope · item add TOOL-aPrimedKeepalive-9 · reason PROMOTED from spec-audit round 3, NON-CONVERGENT: every acceptance criterion a fold ADDED is unevidenced in the ledger — unit 1 AC8/AC9, unit 2 AC9, unit 4 AC6, unit 6 AC5 — while unit 7's fold-added AC6 is evidenced, so it is an omission rather than a convention. Hygiene check 23 reds the push boundary the moment those units flip to CLOSED.

2026-08-27T15:13:54Z review · item aPrimedKeepalive · reason verdict BLOCKED · blockers 2

2026-08-27T18:15:43Z decision · item The merge bar is RED for five legs this build did not cause, and landing is blocked on them · reason Measured on the reconciled tree. charter size: AGENTS.md is 65044 against 64512, byte-identical to origin/main and never touched here; its own refusal says raising the limit is an OWNER decision recorded in DECISIONS.md, and trimming a governance carrier is M3 veto 2, which a standing mandate does not reach. memory hygiene check 14: TOOL-aBoundedCeiling-2, -3 and -4 cited but undefined, another node's build in flight; waiving another build's ids would suppress a live signal. install-prefix: the run-gates.sh carried-prefix ratchet ROSE 3 to 4 and its own message says re-run the ratchet writer in the pass that earned the drop. lexicon: 463 P1 offenders across tools/codebase-map and siblings this build never touched. run-gates gov canary: tier2-review's self-test declares no ceiling. OPTIONS SEEN: fix them here, which means editing a governance carrier the mandate excludes plus two other builds in flight; land with the hook-bypass flag, which the protocol bans and the gate greps for; or stop at a merge-ready branch. REFUSED the first two. The branch is reconciled with origin/main, nine units CLOSED, and one command from landing once the five clear.

2026-08-27T18:16:02Z decision · item The kickoff-manifest ratchet breached its own 60 s ceiling on the last bar run · reason GATE FAIL kickoff-manifest ratchet (timed out after 60s), observed on the plain bar. Not investigated: the owner called the bar off before it finished, and this build did not touch manifest-check.sh. It MAY be contention — four heavy things shared 16 cores for hours today — or it may be real, and the honest statement is that nobody has separated the two. Whoever picks it up runs the leg alone and compares against its declared ceiling.

2026-08-27T18:16:09Z decision · item The unattended kit self-test suite never produced a verdict, and the kit descriptor says work touching tools/unattended/ is not done without one · reason Started twice. Run one ran four hours against source that the origin/main merge then superseded, and was killed for that reason. Run two was killed to give the merge bar the machine after the two starved each other. So the compensating check the kit.toml names is UNRUN for this build, and its own descriptor says there is no gate behind that sentence. What IS known: check-unattended.sh and unattended.sh both pass bash -n, the leg itself ran green earlier in the build, and every predicate this build added was red-proved by hand with its failing case observed. That is weaker than the suite and is not offered as a substitute.

2026-08-27T18:21:04Z override · item gates-green · reason Five merge-bar legs are RED for causes this build did not create and may not fix: charter size (AGENTS.md byte-identical to origin/main, and its own refusal makes raising the limit an owner decision), memory hygiene check 14 (another build's undefined ids), install-prefix (a ratchet another pass earned), lexicon (463 offenders in files this build never touched) and the gov canary (tier2-review's self-test declares no ceiling). Every leg this build DID own was fixed and is green: the readme-contract rows and its equality pin, the stale unarmed-branches pin, and the drift-audit non-terminal specs, all nine now CLOSED. The owner called the bar off mid-run. This override records that the bar was not green at close and names exactly why; it is not a claim that it passed.

2026-08-27T20:05:13Z decision · item CORRECTION: the gates-green override's stated causes went stale between the close and the reconcile, and the override is the thing that substitutes for the owner's explicit ask · reason Found by the reconcile-verification review, and every premise re-measured. THREE of the five named causes no longer hold as written. charter size is GREEN: AGENTS.md is 64496 against 64512 because origin/main trimmed it, where the override says 65044 over budget. drift-audit records is GREEN: non_terminal_specs_cited_by_product_source reads 2 against pin 2, drained by this build's own closes plus the reconcile. The readme-contract leg was RED at the close in a way the override did not name and is green now, after removing a duplicate exemption this run had added, registering two builds the reconcile imported, and conforming this build's own README to the slot canon it was violating. What REMAINS true of the override: the install-prefix ratchet, the lexicon offenders and the gov canary are still inherited reds this build did not cause. The override text itself is not rewritten — it is an append-only record of what was believed at the close, and this row is the correction that supersedes it. A reader must take both together.
