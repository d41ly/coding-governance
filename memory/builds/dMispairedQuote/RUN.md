# dMispairedQuote - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
halt-code: gate-red-out-of-scope
parked-surfaced: yes, 2 surfaced
keepalive-reaped: yes
witness: 91058925b19addc557954bae0f8884d7f03d81a3
disposition-source: reconstructed 2026-09-01 by TOOL-dFoldedVerdict-3, by hand and not by a verb.
  `--review --disposition` did not exist when these rounds were recorded — it lands in
  TOOL-dFoldedVerdict-1 — and `verb_review` refuses a second round for a subject already carrying a
  terminal token, so no verb can write these two values now or ever. WHAT VERIFIES EACH, re-derived
  from this build's own records before either was written. TOOL-dMispairedQuote-1: its spec's rev-3
  log records the round-2 exit at 4 blockers against a ceiling of 2 and disposes all four by name —
  blockers 1, 8 and 17 PROMOTED to TOOL-dMispairedQuote-3, blocker 24 FOLDED by narrowing
  LITERAL_OPENERS. Corroborated at the other end: TOOL-dMispairedQuote-3's own rev-1 log says it was
  promoted from that exit carrying exactly 1, 8 and 17. That subject took BOTH dispositions and the
  field holds one value; `promote` is recorded, per
  memory/gotchas/one-value-field-records-a-mixed-outcome.md, because promote is the value that
  DEMANDS an id and fold is the value that demands nothing — recording the demanding one over-asks
  and recording the other would let a real promotion go unobserved. TOOL-dMispairedQuote-3: its
  rev-4 log records the round-3 exit holding at 2 against a ceiling of 2 and disposes both blockers
  as FOLDS, stating that neither needed a mechanism the build lacked. All six blockers of the two
  exits are accounted for. NOT reconstructed: which blocker each row's single value belongs to. The
  field is per SUBJECT, the mixed accounting lives in the spec revision log that already holds it,
  and inventing a per-blocker field here would be a second grammar nothing reads.
phase: ABORTED
branch-sha: d9efe373a3b86a91f82ab9062a9dff4306e3293c
branch-ref: refs/heads/branch/agent-cap-apostrophe-bug-46c953
mode: prompt
anchor-kind: run-branch
keepalive: f9625ca8
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: d65da7abb562957247720898fba1d7ef983f242a
anchor-ref: refs/heads/main
base: d9efe373a3b86a91f82ab9062a9dff4306e3293c

## Parked

2026-09-01T09:21:32Z review · item TOOL-dMispairedQuote-1 · reason verdict BLOCKED · blockers 2

2026-09-01T09:21:32Z review · item TOOL-dMispairedQuote-2 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-01T09:58:47Z review · item TOOL-dMispairedQuote-1 · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT · disposition promote

2026-09-01T09:58:55Z decision · item The rendered unattended Skill documents a --disposition fold|promote flag on --review that the installed driver 1.14 refuses (check 14, unknown argument). The Skill says the merge bar reads that field, and a fold with nothing recorded is indistinguishable from a promotion that never happened — so the field the bar reads cannot be written. · reason Out of this build's goal, which is agent-cap.js's string views. Not a blocker: round 2's disposition is recorded in the build README and in each spec's revision log instead, and the round itself is on the record with its NON-CONVERGENT verdict. Filed as a backlog row rather than fixed here, because the unattended kit is a different mechanism and M3 veto 2 puts its contract outside what this mandate delegates.

2026-09-01T10:06:43Z rescope · item add TOOL-dMispairedQuote-3 · reason Spec-audit round 2 exited NON-CONVERGENT at 4 blockers. Three of them — 1, 8 and 17 — are one property: correcting what counts as a string literal un-hides every OTHER character the old mispairing was blanking, and rules 2 and 3 walk brackets and balance parens ACROSS lines. Three DENY-to-ADMIT moves were reproduced against unit 1's mechanism alone. Closing it needs a mechanism unit 1 does not have, so M4 promotes it to a unit.

2026-09-01T10:52:54Z review · item TOOL-dMispairedQuote-3 · reason verdict BLOCKED · blockers 5

2026-09-01T11:30:42Z review · item TOOL-dMispairedQuote-3 · reason verdict BLOCKED · blockers 2

2026-09-01T12:04:02Z review · item TOOL-dMispairedQuote-3 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold

2026-09-01T13:16:41Z review · item dMispairedQuote · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-01T13:30:16Z decision · item This build cannot MERGE unattended: the unattended kit gate is red on check 2, and the merge bar is what the standing mandate leaned on. The check demands one new non-WONTDO unit id per review subject that exited NON-CONVERGENT. This run had two such exits. Unit 1's PROMOTED its three standing blockers into TOOL-dMispairedQuote-3. Unit 3's FOLDED both of its two, which BUILD-METHOD M4 permits verbatim and which the round-3 review itself prescribed - and a fold leaves no id, so the check reads it as a blocker neither fixed nor promoted. Both were in fact fixed and built. · reason Three options, and the choice is the owner's. (1) Accept and merge by hand: 85 of 86 legs are green, the reported bug is fixed and gated, and the check's own comment calls its count a LOWER BOUND that cannot attribute an id to a subject. (2) Give the driver the --disposition fold|promote flag its own rendered Skill already documents and the merge bar is said to read, then teach check 2 to accept a recorded fold. That is TOOL-dMispairedQuote-7, and it is new public CLI surface, which M3 veto 2 makes an owner turn a standing mandate does not delegate. (3) Retro-promote unit 3's two folded blockers into a unit to satisfy the counter - refused, because both are already fixed and a unit invented to move a number is the shape this repo gates against everywhere else. I refused to decide between them rather than pick the one that lands.

2026-09-01T13:30:35Z abort · item dMispairedQuote · reason 85 of 86 merge-bar legs are green and the reported defect is fixed, gated and pushed on branch/agent-cap-apostrophe-bug-46c953. The one red is the unattended kit gate's check 2, about THIS run's own review bookkeeping and not about the product: it counts one promoted unit id per NON-CONVERGENT review exit, this run had two such exits, and one of them disposed its blockers by FOLDING them, which BUILD-METHOD M4 permits and which leaves no id to count. Both folded blockers were fixed and built. Closing the check needs the --disposition fold|promote flag the rendered Skill already documents and unattended 1.14 refuses, which is new public CLI surface and therefore an owner turn under M3 veto 2. The alternative code is scope-approval-needed and the difference is a reading: a gate is red AND the decision that clears it is the owner's. Nothing is lost - three units CLOSED, an acceptance ledger answering every criterion, and the merge is the only step withheld.
