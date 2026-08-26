# dTieredTribunal - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 668eb2e3174f2fd62d13a7ab6895883d5338f4b7
phase: REVIEWING
mode: slug
anchor-kind: default-branch
keepalive: 91052d0a
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: da9e4cd28072501cd4fe87a81db36c01b9a80f9e
anchor-ref: refs/heads/main
base: da9e4cd28072501cd4fe87a81db36c01b9a80f9e

## Parked

2026-08-25T23:03:44Z decision · item Which proposal set becomes this build's units — and specifically, does P1 (a subject descriptor on tier2-review.js) get built, which requires editing BUILD-METHOD.md M4? · reason The research record ranks P1/P2/P12 RECOMMENDED and the build README says the owner narrows before anything is specced; the invocation said 'spec the build and execute' without naming a set. P1 is the build's own goal, but landing it makes M4's 'Not the harness' rule FALSE, and this build's README rule 3 puts BUILD-METHOD M4/M8 and REVIEW-PROTOCOL.md in scope as PROPOSALS, not as edits. So P1 without a rule edit ships a capability M4 still forbids (dead by construction), and P1 with one breaches the build's own stated rule. Options seen: (a) build P1 + P6's rule edits, breaching README rule 3; (b) build P1 alone, leaving M4 stating something false; (c) build P9 (the record-shape hygiene gate), which the research names as the substitute 'worth doing alone if P1 is declined' and which needs no rule edit; (d) park P1 and P9 together as one owner turn and build only what needs no governance-carrier edit. Refused (a) and (b) because both breach a stated constraint, and M3's veto 2 makes a governance-carrier change an owner turn that the mandate's delegation does not reach. Refused (c) alone because substituting P9 for a parked P1 pre-empts the owner's call on the stronger mechanism. Proceeding on (d).

2026-08-25T23:54:39Z review · item dTieredTribunal-specs · reason verdict BLOCKED · blockers 3

2026-08-26T00:38:36Z decision · item P3 — should the four M4 lens briefs become declared data the caller passes through args, with a parity leg holding tools/memory-tree/README.md to the declaration? · reason Options seen: build it now as a fourth unit; fold it into whichever engine change P1 becomes; leave it. Refused to take it because the research ranks it below both RECOMMENDED items, no measured defect is charged to the prose copy, and its parity leg is a new mechanism this run would have to price without an owner turn. Detail in the build README's Parked decisions.

2026-08-26T00:38:37Z decision · item P4 — should the attended path get a home for the review row set, and should M4 gain a pointer line naming the verb that already carries its convergence loop? · reason Options seen: build the attended home only; build the home and the M4 pointer; leave both. Refused because the pointer half edits BUILD-METHOD.md, which this build's own rule 3 puts in scope as a proposal and not an edit, and M3 veto 2 reserves a governance-carrier change to the owner. The other half is a change to the unattended driver rather than to a review harness, so it is a different build.

2026-08-26T00:38:39Z decision · item P5 — should check-review-join.sh's ref-keyed-join predicate be lifted into tools/hooks/agent-cap.js, which is the only enforcement point that reaches an inline ad-hoc review script? · reason Options seen: port the join predicate alone; port it plus the uncounted filter(Boolean) predicate; leave it. Refused because it changes the enforcement hook and lands a gate whose failing case must be observed before it can land, and the research ranks it VIABLE rather than RECOMMENDED. Worth flagging to the owner: it is the ONLY lever that reaches a hand-rolled driver, a shipped engine cannot make the bad path impossible, and its optional second predicate correctly reds both drift-audit siblings so it gets cheaper once TOOL-dTieredTribunal-3 lands.

2026-08-26T00:38:41Z decision · item P7 — should the three workflow harnesses become one engine with a profile table, or a renderer emitting several files behind a parity gate? · reason Options seen: one large engine file with profiles inside it; a renderer plus a parity gate; neither. Refused because the research prices it high, the runtime forecloses the obvious shape since workflow scripts cannot import, and it names the cheaper substitute in the same breath — which this run specced as TOOL-dTieredTribunal-3. It also re-enters the recorded refusal on any replacement engine unless every trust counter survives on every exit path of every profile.

2026-08-26T00:38:43Z decision · item P10 — should a review record gain a round axis and a reviewed-rev axis, stamped by the driver rather than typed? · reason Options seen: build it now; build it after P4 gives the rounds a driver; leave it. Refused because the value depends on a program emitting the fields and nothing runs the rounds on the attended path today, so it waits on P4, which is itself parked. The binding grammar already admits a trailing rev qualifier and exactly one record in the corpus uses it, so the data half exists and the driver half does not.

2026-08-26T00:38:44Z decision · item P11 — should agent-cap.js's marked-derivation branch require EVERY non-self reference to be bounded rather than just one, closing the reproduced hole where a caller-supplied array reaches agent() once per element? · reason Options seen: tighten it now; tighten it as part of whatever P1 becomes, since P1's dialect sits directly on the hole; leave it. Refused because the research calls it a prerequisite for P1's dialect and P1 is parked, and because its one shipped user is drift-audit-state.js:224 — the same file TOOL-dTieredTribunal-3 is re-shaping — so the two units would contend for one file. The hole is REAL and reproduced, not theoretical.

2026-08-26T01:18:58Z review · item dTieredTribunal-specs · reason verdict BLOCKED · blockers 2

2026-08-26T01:25:12Z decision · item F2 on TOOL-dTieredTribunal-1 — should tools/check-kit-versions.sh gain an assertion pairing tier2-review.js's meta.version with its same-line gov:kit tier2-review@ marker, the way it already pairs both drift-audit siblings? · reason Round 2 finding 35 established the asymmetry from source: check-kit-versions.sh:24 is a bare presence check that this file carries SOME version-shaped token, while :180-193 holds the full constant-to-marker-to-meta.version chain for both drift-audit harnesses. So a bump that moves one of tier2-review.js's two same-line tokens and not the other is invisible to the bar. Options seen: add the assertion inside TOOL-dTieredTribunal-1; add it as a separate gate unit; leave the asymmetry. Refused to decide because a gate is a MECHANISM and folding one into a spec-text review round smuggles it past the round meant to price it, which is the disposition round 1 already gave finding 45. A new gate also owes its failing case observed before it lands, which is work this run did not scope.

2026-08-26T02:06:53Z review · item dTieredTribunal-specs · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-26T02:16:47Z dispatch · item ac57d4a2 TOOL-dTieredTribunal-1 · reason tools/workflows/tier2-review.js

2026-08-26T02:20:28Z dispatch · item 4c9f752f TOOL-dTieredTribunal-2 · reason memory/gotchas/fold-text-is-unreviewed-surface.md memory/gotchas/INDEX.md memory/map/features/build-method.md memory/map/generated

2026-08-26T02:26:42Z dispatch · item 7ce98b64 TOOL-dTieredTribunal-3 · reason tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js tools/drift-audit/drift_report.py tools/drift-audit/README.md memory/map/features/review-harnesses.md

2026-08-26T03:16:30Z review · item dTieredTribunal · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-26T03:18:53Z decision · item The closing review's D1 and D2 were FIXED but not LEFT-SHIFTED. Should the false-clean family they belong to get a memory/gotchas/ record, or a scanner, or neither? · reason BUILD-METHOD M8 requires every confirmed finding left-shifted into a gate or a gotchas class, and says plainly that a finding fixed and not left-shifted returns. I fixed both in place — D1 at three files, D2 at two — and did NOT left-shift either. Options seen: write the gotcha record now; write a scanner asserting a returned counter also reaches a prompt; do neither and carry the backlog row. Refused to take the first because this build MEASURED that fold prose written after a review is the dominant source of the next round's defects, at 20 of 29 and then 20 of 32, and a new record authored after the closing review is exactly that surface with no round left to catch it. Refused the second because a new gate owes its failing case observed before it lands and that is a unit, not a fold. Recorded as TOOL-dTieredTribunal-5 with both candidate mechanisms and the reason each is not obviously safe. This is a deliberate incompleteness against a binding rule, surfaced rather than skipped.

2026-08-26T03:25:01Z decision · item F2 was RECLASSIFIED out of spec-1 section 8 into backlog row TOOL-dTieredTribunal-6, by the run whose own close it was blocking. Was that legitimate? · reason The question itself is unchanged and still open and still yours: should tools/check-kit-versions.sh pair tier2-review.js's meta.version with its same-line gov:kit marker, as it already does for both drift-audit siblings. The argument for moving it: a section 8 item is an open question about the UNIT's design, and TOOL-dTieredTribunal-1 is complete and correct either way, touches no file in that kit, and already excludes new gate legs in its section 3 non-goals. The argument against, which I am recording because nobody else will: filing it in section 8 made the unit unclosable under hygiene check 12, an unclosable built unit holds non_terminal_specs_cited_by_product_source above its pin, that reds drift-audit records, and a red bar blocks the push. So the mover had an interest in the move. Round 3 of this build's spec audit predicted this collision as finding 31 before it happened. Options seen: leave F2 in section 8 and abort the landing; resolve F2 in place, which would sign your name to a gate decision you never made; reclassify it to the backlog and disclose. Took the third and wrote the disclosure into the spec itself so it is reversible.
