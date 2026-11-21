# TOOL-dPlacedRequest-21 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-21

The unit was built from its spec at rev-9 (PINNED) on base `6053cf840`. The unattended driver gains
`--entry-claim <slug> --request <content key> [--pieces <n>]` in
`tools/unattended/unattended.sh#run_entry_claim`, its claim ref read through
`tools/unattended/unattended.sh#read_claim_ref` and its later keys added by
`tools/unattended/unattended.sh#add_claim_key`. The python half is the new `tools/loop/claim.py`: the
body in `tools/loop/claim.py#render_claim_body` from `tools/loop/claim.py#read_claim_lines`, the claim read
by `tools/loop/claim.py#read_claim_body`, the refusal routes by `tools/loop/claim.py#derive_claim_route`
and `tools/loop/claim.py#check_wait_expired`, the ratification by
`tools/loop/claim.py#check_patch_ratified`, the scaffold commit by `tools/loop/claim.py#write_claim_scaffold`
and the first record by `tools/loop/claim.py#write_first_transition`. The memory-tree kit's index generator
gains `--placed-build` in `tools/memory-tree/gen_build_index.py#cmd_placed_build`, rendered by
`tools/memory-tree/gen_build_index.py#render_placed_build_readme`, and
`tools/loop/loop_transition.py#write_transition` calls `check_patch_ratified` before a move into designing
of a build whose claim body reads `disposition: patch`.

One name moved from the spec's inventory: `route_claim_refusal` leads with `route`, which the naming
lexicon refuses as undeclared, so the function is `derive_claim_route(cause, leases)`, the same two
arguments and the same table. `check_patch_ratified` takes the repository root beside the slug, as every
reader of a build's records here does. The offline route follows the stops table TOOL-dPlacedRequest-34
names: `leases.offline: refuse` exits 1, any other value exits 4, and no claim is queued, since
TOOL-dPlacedRequest-1 S10 creates no ref while offline.

No gate, suite or bar ran in this pass, and no `--selftest`. Each criterion below was observed by a probe
of the changed code: `python tools/loop/claim.py --fixture --plant <case>` per plant, each printing `held`,
then `python tools/loop/claim.py --fixture`, the leg's own argv, printing
`claim: fixtures · PASS · 11 case(s) · 0 failed` (the run's node, 2026-11-20, PINNED) before the checklist pass added 2 (PINNED) plants, each run by its own `--plant`. The leg's RED was
staged once as a probe: with `derive_claim_route` sending a terminal cause to `wait` under `leases: warn`,
`--plant tombstone-warn` printed `MISSED` naming `the refusal printed 0 ask lines, not one`, and held again
once restored. The index generator's `--check` printed the same lines before and after its edit.

**Evidences:** TOOL-dPlacedRequest-21
- AC1 — `--plant patch-owner-unratified`: a patch of the fixture's closed build under `patch.ratify` =
  `owner` exited 1, printing `owner item: ratify dFixPatch` naming the unit `TOOL-dFixPatch-1` and the
  transition writer's refusal naming `patch.ratify`; HEAD carried no `Gov-Transition` trailer.
  `--plant patch-owner-ratified`: the owner's disposition record of `item.entry.claim` `ratified`, written
  through the record factory under `TOOL-dFixPatch-1` and committed, and the same claimant's second run
  exited 0, resumed, recording `none -> designing` with `item=item.plan.dedupe`.
  `--plant patch-owner-rejected`: the owner's record disposing `rejected`, and the resumed claim exited 1
  naming `rejected for good` and `patch.ratify`, no transition recorded.
- AC2 — `--plant tombstone-warn`: the build lease's tip a `status: landed` build lease of another node,
  under the default `leases: warn`; the verb exited 1 printing `tombstone` and exactly one
  `ask: dRunAgain · tombstone · request <key>` line, the lease ref still at the tombstone's commit, 2
  (DERIVED) commits, and no README written.
- AC3 — `--plant claim-twice`: a repeat claimed, its scaffold and first record committed, exit 0; the
  second run printed `claimed by this claimant` and `first record at`, exit 0, ran no local pre-check,
  while `check_slug_claimed` over the slug refuses it; the claim ref stayed at one commit (PINNED) and HEAD
  where the first run left it. `--plant slug-minted-locally`: a slug whose build folder a local commit
  touched was refused naming `the local pre-check of a fresh claim`, exit 1, and no claim ref was created.
- AC4 — `--plant slug-taken`: a claim ref under the key `z:s-other`; the verb exited 5 printing
  `claimed under another key` and `a fresh slug owed`, and the request ref gained one
  `route-back · item.entry.claim` row, the record created from the kept copy. With the scratch remote renamed away, a
  second slug exited 4 printing `claim not written — offline`, and no build folder was written.
- AC5 — the index generator's `--placed-build`, probed in a scratch repository through
  `tools/memory-tree/gen_build_index.py#cmd_placed_build`: `--origin aFoo` wrote and staged a README whose
  front matter carries the six required keys, `status: OPEN` and `parents: aFoo`;
  `--playbook playbooks/zq-run.md --pieces 3` wrote `authorized-by: recipe`, the `playbook:` key and `pieces: 3` (PINNED); no
  request text appears in either, and a repeat with no `--pieces` was refused before any write.
  `--plant repeat-no-pieces`: the verb printed one line naming `--pieces` and exited 2, the scratch remote
  holding no `refs/gov/claims/dRunAgain` and the fixture no build folder.
- AC6 — `--plant live-holder`: another node's live build lease; the first run exited 4, the claim ref
  gaining a second commit holding `wait-since:`; a planted later commit dated the stamp in 2000, and the
  same claimant's second run printed `claimed by this claimant`, ran no local pre-check, reached the lease
  take and exited 1 printing `owner item: dRunAgain · live-holder past flow.wait-ceiling`.
  `--plant overlap-warn`: a remote branch and this run's own commit sharing one path under `leases: warn`;
  the verb exited 0 printing `overlap noted`, the claim ref's newest commit holding `overlap:`, and the
  first record written.
- AC7 — `--plant first-record`: a repeat exited 0; `HEAD~1` is
  `records(dRunAgain): entry.claim's derived plan record`, carrying the README and `memory/project/readme-contract.txt` alone, and HEAD the
  transition commit carrying no file, its trailer `none -> designing` with `item=item.entry.claim` and
  `scenario=scenario.playbook-run`, the index left clean. `--plant first-record-patch`: a patch under
  `patch.ratify` = `auto` recorded `item=item.plan.dedupe`, `stand-in=dRankedPlan` and
  `scenario=scenario.patch`. A `new` claim probed through the same fixture recorded `none -> planning`
  under `item.entry.claim` with no scaffold commit, and its re-run wrote nothing.
- The checklist pass's refusals — `--plant refusals`: a `continue` placement refused exit 1 naming the
  disposition; `--pieces 2` on a patch refused exit 2; a stray staged path refused the scaffold exit 1
  naming it, no README written, and once unstaged the same claimant's run resumed, committed the scaffold
  and recorded `none -> designing`; under `leases.offline: refuse` with the remote renamed away a fresh
  slug exited 1 printing `lease refused — offline · claims/dElsewhereNow`.
- AC8 — `grep -n '"loop claim fixtures"' tools/gate-legs.json` finds the row, its argv
  `python {prefix}/loop/claim.py --fixture`, and `python -m json.tool tools/gate-legs.json` parses with that
  row's `enforces` holding `principle.p39`. `tools/playbook/core-pending.txt` holds no `principle.p39`
  row, so none was deleted.

Owed at the close, never run here: the leg `loop claim fixtures` whole under the bar, its RED observation
on the `tombstone-warn` break named in the gates section; the `build-index selftest` arms of
`--placed-build`, RED on a patch scaffold written with no `parents:` key; the `unattended.test.sh` block
`DPR21`, waived by README rule 8.
