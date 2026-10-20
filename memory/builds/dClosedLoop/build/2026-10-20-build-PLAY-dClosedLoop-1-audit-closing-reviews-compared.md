# Research: the whole-design audit's closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

Two independent full diff reviews, runs A and B, read the range `8d21999a9` over `6ba4eaaa1`, which holds every design
commit since the parked debt's closing pair, up to and including the whole-design audit's fold. This record compares
the two runs defect by defect, as the last pair was compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `8d21999a9` over `6ba4eaaa1`. It covers every design commit since the parked debt's closing pair: that
  pair's fold, the owner's final questions and answers, the clause ids, Stage 0 and the walk kit, the owner's readings,
  the walk's records and the audit's fold (the args' context names each commit).
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review. Each run had five `gov-diff-reviewer` lenses
  (security, correctness, seams, verification, intent), five `gov-skeptic` batches and one `gov-synthesizer`, every
  role at the owner's medium. The 32 design and research records the range touches or rests on were the intent
  inputs, and `gotchas.py --for-diff` gave the 35-class checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 208 | `wf_fe1512b8-f16` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-a.md` |
  | B | 209 | `wf_e897bbe0-97d` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-b.md` |

- **The args:** `build_args_closing.py` wrote both. The runs differ only in the run label, the report path and the
  scratch path, and they ran one after the other.
- **Independence:** run A's report was moved out of the tree about thirty seconds into run B, and restored byte for
  byte after it (sha256 `d7b8e69ee5ab`). Run B's transcripts name it only in the git status the harness injects at
  start, six times, never in a tool call or a tool result.

## [method] How the runs were compared

The last pair's `[method]` applies unchanged
(`build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`, itself the flow adoption comparison's
method). Every finding of both runs, confirmed or refuted, is placed on the defect it names, and a finding naming two
defects lands on both. Where a skeptic judged a finder's fix unsound, the skeptic's corrected fix folds. Where the
reviewers offered two routes, the `[fold]` row names the one taken and why.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `unit-lease-needs-cycle` | `build.unit-lease`'s new Needs cell (flow-steps:281) waits on the `build.reuse-check` of every earlier unit, closing a Needs cycle that Stage 0's K1 reds; run A also reads it as running units one at a time, against `build.unit-pass`'s "disjoint write sets in parallel" | 3, 4, 18, 21 | 9, 18 | fold: A's skeptic's corrected fix |
| `closed-root-draw-pruned` | cl-0440's draw on a closed root acquires the root's terminal lease, but cl-0134, the `leases.queued-claim-days` row and layer-runtime:465 prune that tombstone after 7 days, and no clause says what a later draw does | 8, 22 | 21 | fold |
| `tolerance-rows-unnamed-tool` | the FK-4-9 tolerance rows in recut `[reconciled-order]` say a route "reaches today's tool" for commands no tool serves, and recut:216's `build.distill` row contradicts FK-4-8's unarmed row at :214 | 7, 23 | 13, 22 | fold |
| `stage0-red-unreported` | whole-audit `[fold-applied]` reports ten checks "ALL rc 0" and omits Stage 0, which is red at 113 findings with none classed, some of them the fold's own, while `[stage0-classes]` stays empty | 4, 18 | 9, 14, 18 | fold: B's skeptic's corrected fix |
| `mailbox-answer-actor` | `mailbox.answer`'s Actor cell, "the role that owns the asked interface or item", is no kind Stage 0's K1 reads, while layer-roles' matrix declares that form | 4, 5, 18, 25 | 18 | fold |
| `mailbox-answer-targets` | `mailbox.answer`'s Then targets are prose in no declared route form, so K2 reads the item as ending nowhere and reached from no entry | 25 | 18 | fold: A's skeptic's corrected fix |
| `guard-no-positive-arm` | cl-0012 and cl-0087 plant only the shapes the guard must refuse, never the one raise it must admit, and cl-0012 ends its refused list "each admitted" | 6, 24 | 24 | fold |
| `door-misses-coordination-verbs` | cl-0505 puts FK-5-3's writer binding at `record`'s door, but memory-plan, layer-memory and v2's mailbox clause write mail, leases and tombstones through the coordination verbs, which never pass that door | 10 | — | fold |
| `close-path-writes-refused` | cl-0505 refuses the cross-session tombstone and mail-ref writes that its own build's unlease, withdrawal, mailbox close and prune clauses make | 9 | 3, 6 | fold: B's skeptic's corrected fix |
| `change-record-undefined` | cl-0012's admitted raise needs "a change record attached", a record kind no ancestor of dGroundRules defines, and no stand-in is named | 14 | — | fold |
| `dedupe-patch-no-transition` | a patch whose `plan.dedupe` finds a duplicate is re-placed, but `[transitions]` has re-placement rows only from `planning`, which a patch never enters | 11 | — | fold |
| `patch-route-skips-dedupe` | `entry.place`'s patch arm, `maintain.patch` and flow.md's Maintain row still route a patch from claim straight to Design, skipping `plan.dedupe` | 12 | — | fold |
| `flakes-measured-no-writer` | `verdict.flakes.entry: measured` switches to "a threshold set from that evidence", but no item derives, writes or switches to it | 13 | — | fork: who derives `measured`'s threshold from the flake records, and when does a leg switch to it? |
| `reconcile-key-no-rule` | reconcile.py keys class rows by (build, node) with no rule, so a row written for a route or a read silently classes a cite, and no stand-in cell is checked | 15, 19 | — | fold |
| `policy-prefix-unread` | flow-steps:234-235 spell the read `policy.design.streams-when`, and reconcile.py's rule 4 looks tokens up as bare keys only, so the probe cannot see those reads | 16 | 11, 15 | fold |
| `budgets-namespace-stale` | ownership `[namespaces]`' `budgets` row still names dCalibratedLens as owner after FK-1-3 moved `budgets.*` to dGroundRules | 17 | — | fold |
| `prose-stage-words-as-routes` | the widened rule 3 of reconcile.py reads capitalised stage words in prose as routes, and recut:215, :222 and :235 class the phantom edges | — | 12 | fold: B's skeptic's corrected fix |
| `silence-loosening-two-copies` | flow-steps:531-532 exclude a loosening from `apply-recommendation`, while v2:1209 and stall-and-loop:210-212 apply its recommended decline | — | 7 | fold |
| `fates-runaway-ceiling-stale` | fates:153 still sends `RUNAWAY_CEILING` to the loop kit's definition after C2-F3 made it `review.max-rounds` | — | 8 | fold |
| `answer-dispatch-non-ancestor` | cl-0504 on dKeptSession has `mailbox.answer` dispatched by `next` (dWellOiledMachine, a descendant) and run by a role of dBoundRoles, with no stand-in and no tolerance row | 5 | 23 | fold |
| `fates-fleet-register` | fates:179 still names "the fleet register" after the rename to the adopter register | — | 10 | fold |
| `rule3-doc-overstates` | reconcile.py:147 says expansion routes are read "under --all-routes", which nothing parses, and the docstring promises step names STEP_NAME does not hold | — | 17, 20 | fold |
| `guard-skips-raise-conditions` | the minimal guard should check the four raise conditions mechanically, and a pinned cap's value is reserved to the owner | 1 | — | no fold: refuted, re-argues FK-9-2 and misreads `budgets.pinned` |
| `guard-admits-budget-switches` | an agent write to `budgets.enforce` or `budgets.pinned` passes as the admitted raise | — | 4 | no fold: refuted, neither key is a measured-file cap |
| `door-window-before-binding` | coordination writes stay unbound in the builds before cl-0505's door lands, with no stand-in | 2 | 5 | no fold: refuted in both runs, pre-existing at the base |
| `ack-by-non-recipient` | a session can clear another's message by acknowledging it under its own identity | — | 1 | no fold: refuted, pre-existing at the base |
| `lease-rewrite-by-other` | a session can rewrite another holder's live lease under its own name | — | 2 | no fold: refuted, re-argues FK-5-3 |
| `walk-fixtures-pinned` | the walk kit's check cases run on the pinned tree's copy, so they certify nothing about the post-fold items | 20 | 19 | no fold: refuted in both runs, the pin is disclosed |
| `guard-row-not-a-use` | recut:188 classes dGroundRules' guard as "not a use" of the policy-file keys while cl-0012 admits a raise | — | 16 | no fold: refuted, the guard still reads neither key |

## [summary] The two runs side by side

```text
$ python compare_rounds.py audit-closing-a.md audit-closing-b.md audit-closing-reviews-compared.md session-log.md wf_fe1512b8-f16 wf_e897bbe0-97d
== runs
A: raw 25, confirmed 21, refuted 4, precision 0.84, high findings 4, agents 12, out 213.8k (sum of returned lines)
B: raw 24, confirmed 17, refuted 7, precision 0.71, high findings 0, agents 12, out 220.3k (sum of returned lines)
== defects
map rows 29, confirmed defects 22, refuted-only 7
both 9, A only 7, B only 6
A alone covers 16 of 22 (73%)
B alone covers 15 of 22 (68%)
overlap (Jaccard) 0.41
Chapman estimate of the population: 26.2, so about 4 found by neither
A only: door-misses-coordination-verbs, change-record-undefined, dedupe-patch-no-transition, patch-route-skips-dedupe, flakes-measured-no-writer, reconcile-key-no-rule, budgets-namespace-stale
B only: prose-stage-words-as-routes, silence-loosening-two-copies, fates-runaway-ceiling-stale, answer-dispatch-non-ancestor, fates-fleet-register, rule3-doc-overstates
== severity (a defect takes its highest confirmed grade per round)
high defects 4: unit-lease-needs-cycle, closed-root-draw-pruned, tolerance-rows-unnamed-tool, door-misses-coordination-verbs
  unit-lease-needs-cycle: A 3 B 2
  closed-root-draw-pruned: A 3 B 2
  tolerance-rows-unnamed-tool: A 3 B 2
  door-misses-coordination-verbs: A 3 B 0
shared defects graded alike 5 of 9
== lenses behind the defects one round alone found
A: seams 7, verification 1
B: correctness 3, seams 2, intent 1, verification 1
== refuted findings and their twins
A1 (guard-skips-raise-conditions): confirmed twin none
A2 (door-window-before-binding): confirmed twin none
A5 (mailbox-answer-actor): confirmed twin A4, A18, A25, B18
A20 (walk-fixtures-pinned): confirmed twin none
B1 (ack-by-non-recipient): confirmed twin none
B2 (lease-rewrite-by-other): confirmed twin none
B4 (guard-admits-budget-switches): confirmed twin none
B5 (door-window-before-binding): confirmed twin none
B15 (policy-prefix-unread): confirmed twin A16, B11
B16 (guard-row-not-a-use): confirmed twin none
B19 (walk-fixtures-pinned): confirmed twin none
```

## [fold] The fold plan

Three places take more than one fold. cl-0505 takes `door-misses-coordination-verbs` and `close-path-writes-refused`.
recut `[reconciled-order]` takes `tolerance-rows-unnamed-tool`, `prose-stage-words-as-routes` and
`reconcile-key-no-rule`. Stage 0 is re-run for `stage0-red-unreported` only after the `build.unit-lease` and
`mailbox.answer` folds.

| Defect | Where it folds |
|---|---|
| `unit-lease-needs-cycle` | flow-steps `build.unit-lease` (:281): its Needs goes back to `build.base` alone, one per unit. Its Does/Then cell takes the lease only once every unit the build's spec declares as a dependency has its `build.reuse-check` witnessed clean, with that dependency record as the witness. `build.unit-pass` (:282) keeps "disjoint write sets in parallel" and `design.streams` (:235) is unchanged. `stage0.py --arms K1` no longer prints the unit-lease cycle line. |
| `closed-root-draw-pruned` | v2 cl-0134 (:1749), the `leases.queued-claim-days` row (:1142) and layer-runtime's supervisor prune (:465): the prune age applies to run claims only, and a build lease's terminal tombstone is never pruned, as layer-memory:333 already states. cl-0440 (:1761) states that a draw on a closed root always finds the root's tombstone. Its witness adds two concurrent draws on a root closed past the prune age, one of them refused. Route taken: the tombstone is kept, not re-created or swapped for the claim ref, because layer-memory's contract already says so and cl-0440's lease serialisation then stands unchanged. |
| `tolerance-rows-unnamed-tool` | recut `[reconciled-order]`: each row reading "today's tool" (:216, :218, :219, :220, :221, :224, :225, :233, :241) names its real stand-in, the tool's path under tools/ or skills/ checked by listing it, or the attended session's agent doing the command by hand, or `unarmed`. :216 (dDeclaredLoop → `build.distill`) reads `unarmed` as FK-4-8's row at :214 does: no decision-log row is written and `build.recommend` routes on. :218 (`deploy.notify`) reads `unarmed`, since the mailbox it posts to is dKeptSession's. :215 is dropped under `prose-stage-words-as-routes`. flow-steps `[rules]`' stand-in bullet (:100-104) says a command with no tool today is unarmed, as FK-4-8 has it. FK-4-9's answer, a rules bullet plus rows, stands. reconcile.py reds a tolerance row whose stand-in cell is the bare "today's tool" or resolves to no path, item or `unarmed`, seen red on a plant. |
| `stage0-red-unreported` | whole-audit `[fold-applied]`'s checks line (:532) and the night pass's instruments `[final]` gain `stage0.py`, all five arms, with its real result: rc 1, 113 findings (K1 2, K2 31, K3 76, K4 4), 0 classed. The fold's own reds are fixed: the K1 cycle under `unit-lease-needs-cycle`, and `mailbox.answer` under its two rows. `leases.overlap` is named in the chain clause or item that applies flow-steps `[rules]`:55's overlap reading, so K4 reads it, and `kits.cadence` is named in the clause that uses it. `runtime.attended-allowance` and the unreached `adopt.declarations`, `adopt.instructions`, `kits.install-attended` and `kits.update-attended` are fixed, or classed in `[stage0-classes]` with a class from their arm's closed set. A red is classed only where it fits that set. Stage 0 is re-run and its rc and "classed N" recorded. Any red left to plan step 3's "Stage 0 again" is named in `[fold-applied]`, and `[stage0]`'s "The audit's fold fixes each red or classes it there" (:69-71) is amended to match. |
| `mailbox-answer-actor` | stage0.py's K1 actor reading (:255-261) accepts an Actor cell opening "the role that owns" as one actor, the owning role, as layer-roles `[matrix]` (:393-437) and `role_matrix.py`'s 2026-10-20 revision already do. flow-steps `[rules]`' "One actor per item, of one kind" (:21) names the owning role, chosen per instance, as a role. A K1 plant keeps that opening green and any other undeclared actor red. Route taken: run B's, not A's skeptic's corrected fix of one fixed role such as the architect, because layer-roles already declares the owning-role form for `mailbox.answer` and a fixed role would contradict it. |
| `mailbox-answer-targets` | flow-steps `mailbox.answer` (:121): the Then targets are written in declared target forms, a mailbox-post terminal for the `answer` and a return to the asker's waiting item for the declared default under cl-0162. The item's reach from `next`'s dispatch is written as a route K2 reads, or classed in `[stage0-classes]`. Stage 0's K1 and K2 are re-run. |
| `guard-no-positive-arm` | v2 cl-0012 (:1744): the witness is green on a planted raise of a single measured-file cap under `budgets.*`, nothing else changed and its change record attached (as `change-record-undefined` defines it), which must be admitted, and the arm reds if the guard refuses it. It is red on each other planted shape, ending "each refused" where it now reads "each admitted". cl-0087 (:1748) gains the same positive arm and "each refused". cl-0032 and cl-0036 carry the same wording where they cite the admitted shape. |
| `door-misses-coordination-verbs` | memory-plan `[doors]` (:277), layer-memory's lease and mailbox rows (:441) and v2's mailbox clause (cl-0157, :1750): the coordination verbs write refs, claims, leases and mail through `record`'s door, and each says so. cl-0505 (:1756) plants the cross-session mail and the forged tombstone through the `gov` coordination verbs, not at `record`. Route taken: the verbs pass `record`'s door, because moving the check into the verbs' own door would re-argue the owner's FK-5-3 answer, "Refuse at record's door". |
| `close-path-writes-refused` | v2 cl-0505 (:1756): the admitted writers of a terminal tombstone are the holder, the take-over verb, and the unlease commands `deploy.unlease` and `life.unlease` acting under the build lease. That includes a unit lease still held by an act on another node when `life.quiesce` ends on `runtime.act-ceiling` (flow-steps :676-679, :438). A delete of a ref under the build's own `refs/gov/mail/<slug>/` is admitted only from that build's closing verbs (`deploy.unlease`, `life.release`, cl-0281's withdraw and supersede, and Maintain's prune at coordination:122), only after the copy into the build folder, and only under the build's lease as holder, through the take-over verb or as the owner's guarded command. The witness admits a planted closing build holding a cross-session mail ref and closed by each verb, and a withdraw that unleases a unit held on another node. It refuses a prune by a session holding no lease, a delete of another build's mailbox and a cross-session post. cl-0281, cl-0415, cl-0508 and flow-steps :80-82 and :421 are cross-read against the admitted list. |
| `change-record-undefined` | v2 cl-0012 (:1744) and v2:766-769: at dGroundRules the change record is today's rule from tools/template-size-limits.txt, the RAISED argument in place beside the cap and a memory/DECISIONS.md row in the same commit, and the minimal guard checks for both. It stands until dOrderedCharter's instruction change-record kind lands and re-points it. The red "a raise with no change record" plants a raise with neither. cl-0087 and cl-0036 carry the same definition. Route taken: today's rule, not a new commit trailer, because writer 9 framed the owner's FK-9-2 option as leaving the conditions to the record's argument "as the file's rules leave them today". |
| `dedupe-patch-no-transition` | flow-steps `[transitions]` (:722-728) gains three rows From `none`, for a placement disposition `patch` whose `plan.dedupe` finds a duplicate or an overlap and re-places it. Continue, amend or patch onto the matched build goes to `merged`, ask goes to `deferred`, and none goes to `answered`. The witnesses are the placement disposition, the dupes record and the claim ref, and each row releases the patch's lease. A duplicate patch is planted through the transition walk. |
| `patch-route-skips-dedupe` | flow-steps `entry.place`'s patch arm (:117), layer-expansions `maintain.patch`'s Routes cell (:225) and flow.md's Maintain and post-close rows (:626-628) read "`entry.claim`, then `plan.dedupe`, then Design". A grep of the design records for "then Design" beside "patch" finds no other copy. |
| `flakes-measured-no-writer` | Fork. Question: who derives `verdict.flakes.entry: measured`'s threshold from the flake records, and when does a leg switch from 2/10 to it? Option (a): dWitnessedBar's gate-health clause cl-0339 derives it by a rule the clause states, writes it to the gate-health record, and `test.flakes` (flow-steps:354) reads it, planted with a leg whose measured threshold differs from 2/10. Option (b): the Loop Review sets it as a recorded decision. Option (c): drop the second phase, so `measured` holds 2/10 until the value is changed, which changes what v2:1253 says the default means. Recommended: (a), because dWitnessedBar owns the key and already measures gate health. Whichever is chosen, v2:1253, layer-memory:584-585 and cl-0346 follow it. |
| `reconcile-key-no-rule` | recut `[reconciled-order]` gains a Rule column (cites, routes, reads). reconcile.py keys `classes` by (rule, build, node) (:235-242) and looks dependencies up by that key (:266-268, :288), so a dependency with no row for its own rule is UNCLASSED. The reused rows split. A cites tolerance row for dFairHearing → `review.trigger` names cl-0070's stand-in, the direct `review.pin`, beside recut:198's "not a use" row. Cites rows for dDeclaredLoop → `plan.exit`, `build.ratify` and `decisions.major` name cl-0104's owner-gate stand-in, the owner's FK-9-1. A `--plant-add` cites dependency on a node that holds only a routes row reds, and is kept in the probe's self-test. |
| `policy-prefix-unread` | reconcile.py rule 4 (:199-200) strips a leading `policy.` from each token before the `keys` lookup. A plant of an item reading a non-ancestor's key as `policy.<key>` reds. flow-steps:234-235 keep the full spelling. Route taken: the probe reads the full spelling rather than the cells being rewritten bare, because flow-steps:17 declares the full spelling legal. |
| `budgets-namespace-stale` | ownership `[namespaces]`' `budgets` row (:128) names dGroundRules as owner after FK-1-3 (:392), or reads 0 keys with a note pointing to FK-1-3. The lead-in's count of "78 keys that nothing names" is recounted. |
| `prose-stage-words-as-routes` | flow-steps' prose cells name no capitalised stage where they mean no route. In `review.dispose`'s cell, "Build's tail waiting until it is built" becomes "the build's remaining units waiting until it is built". In `life.quiesce`'s refusal, "the build closes through Deploy" becomes "the build closes through its landing". The rows are regenerated: recut:215 and :235 are dropped, and :222 is dropped if its edge goes. A plant in reconcile.py's self-test checks that a Then cell reading "the Plan breakpoint", with no `→` before the stage word, yields no edge, while "→ a fix unit through Design" still yields one. |
| `silence-loosening-two-copies` | flow-steps :531-532 read, as v2:1209 does: "the item's recommended option applied past the deadline, a loosening's recommendation being the decline, never for a ratification or an owner-only write". A loosening approval left silent past `run.owner-deadline` is planted, and a recorded decline is expected. |
| `fates-runaway-ceiling-stale` | fates:153's fate reads "the policy key `review.max-rounds` (dDeclaredLoop), `unattended.sh` and `check-unattended.sh` re-pointed in the unit that retires `REVIEW_ROUNDS`", citing cl-dClosedLoop-0106 and C2-F3. |
| `answer-dispatch-non-ancestor` | v2 cl-0504 (:1750), flow-steps' mailbox rules (:76-79) and `mailbox.answer` (:121) state the stand-in: until dWellOiledMachine lands `next`, a question addressed to an unattended build is answered by the asker's declared default under cl-0162. recut gains a tolerance row dKeptSession → `next` (dWellOiledMachine). Route taken: the declared default, not the attended session's agent, because an unattended build has no attended session and the default is already the item's no-answer route. The same stand-in covers the answering role, and run A's skeptic found that earlier builds already name roles, so the roles half needs no row of its own. |
| `fates-fleet-register` | fates:179 reads "the adopter register (dShippedRelease), its rows read by `kits.adopters`". |
| `rule3-doc-overstates` | reconcile.py's comment at :147 reads "read in every run". The argv handling notes that `--all-routes` is ignored. The docstring (:28-32) and the "left out" line say rule 3 reads only the five flow steps' names in STAGES (:100). Route taken: narrow the docstring rather than add Entry and Maintain to STEP_NAME, because run B's scratch run showed widening changes nothing today and a wider stage-word set widens the prose over-match `prose-stage-words-as-routes` closes. |

## [folded] Every defect folded, 2026-10-20

The owner's answers, verbatim from the question tool:

- Closing pair fork, flakes-measured-no-writer: "verdict.flakes.entry defaults to 'measured' (2 flakes in a leg's last 10 verdicts until measured), but nothing derives the measured threshold or says when a leg switches to it. Who derives it?" — "dWitnessedBar derives it (Recommended)"
- FK-10-1: "You chose that dWitnessedBar derives verdict.flakes.entry's measured threshold (cl-0339). No record fixes the rule itself. Which rule does cl-0339 state?" — "Fleet p90, after 30 (Recommended)"

- **The main loop's parts.**
  - **The probe.** reconcile.py keys class rows by (rule, build, node), reads a key spelled `policy.<key>`, counts a
    stage word as a route only after its branch's arrow, reds a tolerance row naming "today's tool" with no path that
    exists, and its docstring says what rule 3 reads. Each rule is seen red in the instruments record's
    `[closing-probe]`.
  - **Stage 0.** Its K1 reads the owning-role actor, and the plant `k1-owning-role` reds any other undeclared opening.
  - **The Rule column.** It is derived by `rule_column.py` from the probe's own dependency lines.
  - **The classes.** The five K2 entries writer 10 asked for are classed in the round record's `[stage0-classes]`.
- **Writer 10's fold**, its dispositions copied whole from its return (`build/2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w10.md`):

| defect | records · places | disposition | the fold's one-line gist |
|---|---|---|---|
| unit-lease-needs-cycle | flow-steps `build.unit-lease` | fold | Needs is `build.base` alone. The Does cell takes the lease only once every unit the spec declares as a dependency has a clean `build.reuse-check`, with the dependency record as witness, and Then waits for one not yet clean. K1 now finds 0. |
| closed-root-draw-pruned | v2 cl-0134, cl-0440, `leases.queued-claim-days` row; layer-runtime supervision bullet | fold | Only a run claim's tombstone is pruned. A build's or unit's tombstone is kept, so a draw always finds it. cl-0440's witness adds two concurrent draws on a root closed past the prune age. |
| tolerance-rows-unnamed-tool | recut rows; flow-steps `[rules]` stand-in bullet | fold | `design.ready` names `tools/memory-tree/gen_build_index.py`. `plan.exit` and `test.exit` name cl-0098's fixture witness. `build.distill`, `deploy.notify` and the three `design.input` rows read unarmed. The bullet now says a command with no tool today is unarmed. |
| stage0-red-unreported | v2 cl-0120, cl-0288, cl-0414 | fold, design part; main loop's for the round record and instruments | `leases.overlap`, `runtime.attended-allowance` and `kits.cadence` are now read by a clause. The five unreached reds are listed under Requests. |
| mailbox-answer-actor | flow-steps `[rules]` one-actor bullet | fold (K1 reading is main loop's) | The rule now allows the role that owns what the item's input names, chosen per instance (layer-roles `[matrix]`). |
| mailbox-answer-targets | flow-steps `mailbox.answer` Then | fold | "answered → done: the `answer` posted…" and "→ back to the asking item, which takes its declared default (cl-0162)". The item now ends. Its reach is a request. |
| guard-no-positive-arm | v2 cl-0012, cl-0087 | fold | Each clause is green on the planted single-cap raise and red if the guard refuses it. Every other shape is "each refused". cl-0032 does not cite the admitted shape, so it is unedited. |
| door-misses-coordination-verbs | memory-plan `[doors]`; layer-memory lease and mailbox rows; v2 cl-0143, cl-0505 | fold | The coordination verbs write through `record`'s door once dTotalRecall lands it, and straight to the remote before then. The comparison record says cl-0157, but the mailbox clause is cl-0143. cl-0505 plants through the `gov` verbs, not at the door. |
| close-path-writes-refused | v2 cl-0505; recut new cites row; flow-steps "Closing a mailbox" | fold (B's skeptic's corrected fix) | cl-0505 now admits tombstones from the holder, the take-over verb, `deploy.unlease` and `life.unlease`. Mailbox-ref deletes come only from the build's closing verbs, under its lease. A new row covers dWellOiledMachine's cite of `deploy.unlease`, with `life.unlease` as stand-in. |
| change-record-undefined | v2 cl-0012, cl-0087, cl-0036 | fold | The change record is today's rule: the RAISED argument beside the cap and a `memory/DECISIONS.md` row in the same commit. It holds until dOrderedCharter's change-record kind takes over. cl-0087 and cl-0036 point at cl-0012. The old revision note at v2:766-769 is left as history. |
| dedupe-patch-no-transition | flow-steps `[transitions]` | fold | Three `none` rows for a re-placed patch: to merged, deferred or answered, each releasing the patch's lease. |
| patch-route-skips-dedupe | flow-steps `entry.place`; layer-expansions `maintain.patch`; flow.md Maintain and post-close rows | fold | All read "`entry.claim`, then `plan.dedupe`, then Design". |
| flakes-measured-no-writer | v2 cl-0339, cl-0346, `verdict.flakes.entry` row; layer-memory held-leg bullet; flow-steps `test.flakes` | fork answered: (a) | cl-0339 states the rule, writes the threshold to the gate-health record, and `test.flakes` reads it. Planted cases cover a threshold that differs from 2 in 10. |
| reconcile-key-no-rule | recut split rows and `[reconciled-order]` prose | fold (probe and column are main loop's) | Each split row is worded for its own rule. The prose now says each row names its rule. `review.trigger` cites cl-0070. `review.dispose` keeps cl-0075, because cl-0070 does not cite it. |
| policy-prefix-unread | reconcile.py | main loop's | Done in reconcile.py. |
| budgets-namespace-stale | ownership `[namespaces]` and `[amended]` | fold | The `budgets` row now reads dGroundRules with 0 keys, and the lead-in counts 77. |
| prose-stage-words-as-routes | flow-steps `review.dispose`, `life.quiesce`; recut | fold (the arrow rule is main loop's) | "the build's remaining units" and "closes through its landing". The dDeclaredLoop `build.base` and dWellOiledMachine `deploy.current` rows are dropped. The `plan.input` row stays: its edge follows an arrow. |
| silence-loosening-two-copies | flow-steps silence rule; v2 cl-0326 | fold | The flow-steps copy now says what v2:1209 says. cl-0326 adds a planted silent loosening whose decline is recorded. |
| fates-runaway-ceiling-stale | fates `RUNAWAY_CEILING` row | fold | The row now names `review.max-rounds`, re-pointed with `unattended.sh` and `check-unattended.sh`, citing cl-0106 and C2-F3. |
| answer-dispatch-non-ancestor | v2 cl-0504; flow-steps mailbox rule and `mailbox.answer` Needs | fold, minus the row (see top) | Until dWellOiledMachine lands `next`, the asker's declared default (cl-0162) answers. The same stand-in covers the answering role. |
| fates-fleet-register | fates `adopters.toml` row | fold | Now reads "the adopter register (dShippedRelease), its rows read by `kits.adopters`". |
| rule3-doc-overstates | reconcile.py | main loop's | Done in reconcile.py. |

- **Stage 0 on the folded tree** reads as follows. K1 and K5 are clean, and the 98 findings left are the
  leads for plan step 3's "Stage 0 again".

```text
K1: items 127 (98 flow, 29 expansion), roles 14 · findings 0
K2: targets by form: ask 4, edge 186, owner 13, policy 4, program 7, return 24, terminal 58, wait 5; roots 14, reached 116, ending 126 · findings 21 · classed 7
K3: kinds 83, table rows 83 · findings 76
K4: keys 267 · findings 1
K5: principles 42, clauses 509, retired 0 · findings 0
stage0: arms K1,K2,K3,K4,K5,reruns · findings 98 · classed 7 · reruns red 0
```
