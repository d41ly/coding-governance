**Serves:** diff-review TOOL-aQueuedIndex-1 TOOL-aQueuedIndex-2

# aQueuedIndex: Tier-2 diff review of TOOL-aQueuedIndex-1 and TOOL-aQueuedIndex-2, round 2

*2026-11-12, on `branch/unattended-aqueuedindex`. This is an adversarial pass over the build on the owner's prompt "fix the tag index contention so bars don't flake". Five finder lenses ran (`gov-diff-reviewer`), then one skeptic batch prompted to refute each finding (`gov-skeptic`), then one synthesis (`gov-synthesizer`). Unit 1 (dd195a2e1) runs the shared tag index connection in autocommit, opens the tree-build, overlay and collection write blocks with `BEGIN IMMEDIATE`, re-reads `tree_built` under the lock and sets `BUSY_TIMEOUT` to 600. Unit 2 (a03bb6339) fixes round 1's blocked arms in the `queued-writers` plant. It grades writer two on runs and skipped as well as parsed. It adds an ast check that every write block opens with `BEGIN IMMEDIATE`, with at least one found. It prints `both writers green` last. Each pin below names the file's blob at the reviewed sha.*

Reviewed range: 97e0841d7d0bdb38df314a1f8d01616a4d431dad...56929f33c651c73f268e8dd855aaf457a3d9f3db. ROUND: 2.

## Verdict: CLEAN WITH FIXES

One low item stands, and nothing above low. The value `BUSY_TIMEOUT = 600` has no gate that fails if it shrinks.

Round 1's three items (B1, M1, L1) drew no confirmed finding this round. The main loop observed each staged break red at a03bb6339. Those breaks were the re-read deleted (skipped 7) and each write block's lock deleted (that block's line named). The restored module was green.

The run is complete. All five lenses and the one skeptic batch returned, and no integrity counter is non-zero.

## Review shape

Intensity full, raw 1, confirmed 1, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

Adjudicated tally by item: 0 BLOCKER, 0 HIGH, 0 MEDIUM, 1 LOW, 1 item in all.

Adjudicated tally by raw confirmed finding: 0 blocker, 0 high, 0 medium, 1 low, 1 finding in all.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 1/1 returned, 0 DIED.
- Demotions: 0 contradictory verdicts demoted to unverified, and 0 orphaned duplicate refutations demoted to unverified.
- Merges and discards: 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, and 0 duplicates.
- Fixes on confirmed findings: 1 judged sound, 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 none proposed, and 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, and 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were `gov-diff-reviewer`, the skeptic batch was `gov-skeptic`, and the synthesis was `gov-synthesizer`.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 29 items, acquired by the harness from `--for-diff 97e0841d7d0bdb38df314a1f8d01616a4d431dad..HEAD`. Each was assigned to exactly one of 5 lenses: security 6, correctness 6, seams 6, verification 6, intent 5.
- By design: the caller's byDesign.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twins are flagged.

## Items

### LOW-1. `BUSY_TIMEOUT = 600` has no gate that can fail (id 1)

**Where:** `tools/playbook/tag_index.py@56929f33:117`.

**What is wrong:** dd195a2e1 raises `BUSY_TIMEOUT` from 60 to 600 (unit 1's S4), and no gate pins the value. The `queued-writers` plant's waiter only queues for about 2.5 s behind a 3 s staged parse. So setting the value back to 60, or to anything of 3 s or more, leaves that row and every other plant green. The plant's held connection at `tools/playbook/gov_tag.py@1dcf72fa:765` reads `BUSY_TIMEOUT` as its own timeout, and no check asserts the value. Spec-1 AC4 (line 310) is a grep that was run once by hand and is wired into no leg. Spec-1 lines 207-210 record this blind spot. It is not on this round's by-design list, since unit 1's resolved F1 settles the value's choice, not its pinning.

**Consequence:** Today's behaviour is correct, because 600 is in place. A later edit that shrinks the timeout below a real full build (95 s measured) would bring back the "database is locked" bar flake the owner asked to fix. No bar would notice, and `help/tags.md` would still say 600 seconds. Grade: low, the binding grade, because the risk is a silent regression and not a wrong result today.

**Fix (judged SOUND by the skeptic):** Pin the value in a check the bar runs. The cheapest way is for the `queued-writers` plant to print `busy timeout <ti.BUSY_TIMEOUT> s` and for its `adopt-playbook.sh` row to require `busy timeout 600 s`. Another way is to add `ti.BUSY_TIMEOUT >= 600` to the plant's green verdict. Then observe the check go red on a scratch copy with `BUSY_TIMEOUT = 60`.

**Left-shift gate:** File the class `rule-stated-with-no-check-that-fails` against this finding. Any spec criterion that is a grep, observed once, must either be wired into a leg's row or be named as a residual in the spec's acceptance table. The `harness arms (fail branches armed or pinned)` leg could then require every policy constant a spec names to appear in some plant's required output.

review-shape kind=diff-review round=2 intensity=full at=synth raw=1 confirmed=1 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=0 low=1 agents=7 out-tokens=37682
review-round round=2 limit=- prior=3 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/playbook/tag_index.py@46bfe37d:117 | low | low | confirmed | This is in scope. The three-dot range includes dd195a2e1, which changes tools/playbook/tag_index.py@46bfe37d:117 from `BUSY_TIMEOUT = 60` (as at base) to 600. I found no gate that pins the value. A grep of gov_tag.py, adopt-playbook.sh and tools/gate-legs.json finds BUSY_TIMEOUT only at tools/playbook/gov_tag.py@1dcf72fa:765, where the plant's held connection uses it as its own timeout. It is never asserted. Spec-1 AC4 (line 310) is a one-off grep that no leg runs. Spec-1 lines 207-210 admit that 'a busy timeout shorter than the hold is not staged either, since 3 s sits inside both 60 and 600'. So any value of a few seconds or more keeps the queued-writers row green. That blind spot is written down but is not on this round's BY DESIGN list. The listed item, unit 1's resolved F1, settles the value's choice, not its pinning. Today's behaviour is correct (600 is in place), so the consequence is only that a later regression would go unseen. That is low. | sound | - | class:rule-stated-with-no-check-that-fails |
