# Research: the parked review debt's closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "run the review pair on the 11 commits, medium effort." Two independent full diff reviews read the
eleven design commits that no closing review had covered, which the owner had parked as review debt. This record
compares them defect by defect, as the earlier paired rounds were compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `6ba4eaaa1` over `320c79646`, the one range that holds all eleven parked commits: the review folds
  `67995cb6f`, `6310bda3d`, `1edb2d167` and `a09f1a3b0`, the tag-grammar changes `98f0439ab` and `d56d7da4d`, the
  stall-and-loop round `ad530a80c` and `7e0322a5c`, and the cloud round `ace51f4a7`, `b398ab226` and `6ba4eaaa1`. The
  three rounds already reviewed inside the range were named to the reviewers as context.
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review: five `gov-diff-reviewer` lenses (security,
  correctness, seams, verification, intent), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the
  owner's medium. Full, not the earlier pairs' light, because the security and intent lenses that light skips are the
  ones the cloud round's seams and the owner's answers need. The 36 design records and research returns the range
  touches or rests on were the intent inputs, and `gotchas.py --for-diff` gave the 33-item checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 153 | `wf_aeec13f0-079` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-parked-debt-a.md` |
  | B | 154 | `wf_e27db12b-1f9` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-parked-debt-b.md` |

- **The args:** `build_args_debt.py` wrote both. The runs differ only in the run label, the report path and the scratch
  path, and they went one after the other.
- **Independence:** run A's report was moved out of the tree while run B ran, so no run B agent could read it, and was
  restored byte for byte after (sha256 `6a8baab0c76c`).

## [method] How the runs were compared

The flow adoption comparison's `[method]` applies unchanged
(`build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`). Every finding of both runs, confirmed
or refuted, is placed on the defect it names, and a finding naming two defects lands on both. Where a skeptic judged a
finder's fix unsound, the skeptic's corrected fix folds. Where the reviewers offered two routes, the `[fold]` row names
the one taken and why.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `fence-still-check-then-act` | layer-runtime's Fencing, its `named-acts` invariant and its `fencing` fixture still specify the re-read before the push that P2(a) beat, and call it safe | 28 | 6, 18, 28, 37 | fold |
| `release-deletes-lease` | the unlease items, Deploy's Memory bullet, layer-runtime's prune and two layer records still delete a lease at release, the cause of the restarted epoch | 29 | 5, 17, 27, 38 | fold: a terminal tombstone, its kind settled with `release-kinds-merged` |
| `tombstone-prune-outrun` | a queued claim's age runs from its queuing and the tombstone's prune age from the release, so a node offline past the prune age still wins a landed unit | 6 | — | fold |
| `route-back-owner-item-stands` | the verification round and `build.reuse-check` still turn an overflow past `flow.route-backs` into an owner item, the route SL-1 and SL-2 replaced | 7, 13 | 8, 19, 39 | fold |
| `fixtures-assert-replaced` | `relaunch-cap` and `limits` still assert the park and the held lease P39 replaced, and no fixture covers a twice-reaped instance | 14, 15, 30 | 9, 30, 31 | fold |
| `renewal-progress-no-interim` | `leases.renewal: progress` is dPlacedRequest's default, yet only dWellOiledMachine's ledger evaluates it | 16 | — | fold: renewal at item boundaries from the transition record until the ledger lands |
| `request-record-unscanned` | the project-level request record carries the owner's words to the remote before any scan or redaction exists, bound to no intake | 1, 2 | 4 | fold: run B's skeptic's corrected fix |
| `shared-store-undefined` | "the shared store" charging a plan shared across machines is defined nowhere, cuts across each node's own plan and has no plant | 3, 11, 19, 27 | 21, 47 | fold: moved to `[planned]` as the fleet's pool ledger |
| `node-profile-unguarded` | the node profile and the node's ledgers have no guard, write path or schema, so any agent on the node can rewrite shares, harnesses or reservations | 4 | 2, 44 | fold: run B's skeptic's corrected fix |
| `silence-values-no-route` | `remind-then-park` and `wait` have no route, and `wait` never ends | 8 | 48 | fold: every value ends by parking the build with its lease released |
| `spend-cap-no-outcome` | a set `build.spend-cap` has no outcome at the cap | 9 | — | fold |
| `repeat-detector-unkeyed` | the repeat detector fires at a fixed two and declares no outcome | 10 | 35 | fold: a repeat counts as no new witness, so `runtime.no-progress` governs it |
| `ledger-result-overstated` | gap-rt-40, `[shapes]` and `[fleet]` drop the conditions behind the ledger's full result: a live reading and p90 estimates | 12 | 46 | fold |
| `node-ledger-no-schema` | the node's ledgers and profile carry no schema version or owner across mixed gov releases on one node | 21 | — | fold |
| `p40-clauses-no-plant` | P40's records claim each clause is seen red, yet the relayed-consent rule, the stale acquisition, the declared clock, the per-role harness, the profile's credential, the lander's re-pointing and four scanned payloads have no plant | 22 | 34 | fold |
| `p39-clauses-no-plant` | P39's records claim each clause is seen red, yet the card's budget, the trends, the spend record, the twice-reaped instance and the immediate `invalid-input` item have no plant | 23 | — | fold |
| `max-rounds-no-red` | `review.max-rounds` is planted only on a flat sequence the convergence rule already ends, and CEILING and BOUNDED have no red | 24 | 33 | fold |
| `termination-soundness-no-red` | the static check's planted stage cannot isolate the counted-edge rule, and no dead-end stage or unreachable item is planted | 25 | 32 | fold |
| `values-no-arm` | the new multi-valued keys are planted on one value each | 26 | — | fold |
| `expiry-reads-later-fact` | dPlacedRequest reads the clock offset dWellOiledMachine registers, and plants a landing only later builds can stage | 31 | 20, 40 | fold: the observer clock and the fence primitive stay, the rest moves to dWellOiledMachine |
| `node-arbitration-undefined` | nothing names what arbitrates a node between its projects, and node-wide admission reads per-repository keys | 32 | 43 | fold: the node ledger weighs projects by share, and every project charges it |
| `chain-plant-shared-account` | the cloud record's chain still plants two nodes sharing one pool | 11, 27 | 36, 47 | fold |
| `silence-applies-loosening` | owner silence can apply a role's own loosening, a `flow.adapt` change or a raised loop bound, on every preset but strict | — | 1 | fold: run B's skeptic's corrected fix |
| `push-to-closed-terminal` | `push-when-away` pushes to a terminal no session has open on a core-only install | — | 11 | fold: run B's skeptic's corrected fix |
| `reclaim-attended-slots` | the admission queue reclaims an attended session's live slots at the act ceiling | — | 12 | fold |
| `release-kinds-merged` | one release serves both a hand-over and a terminal end | — | 13 | fold |
| `keep-waiting-uncounted` | the release hold's item never counts the keep-waiting answers the chain bounds | — | 14 | fold |
| `stream-plan-unread` | CL-3's stream plan names a reader that never reads it | — | 22, 41 | fold: the kind declared on dTotalRecall, an ancestor of its writer and its reader |
| `owner-keys-no-precedence` | `run.on-owner-question` and `run.on-owner-silence` both resolve an unanswered item, with no precedence and no witness for the deadline | — | 24 | fold |
| `fence-red-no-interleaving` | the fenced push's red does not place the take-over between the read and the push | — | 29 | fold |
| `round-count-no-pair-rule` | no pair rule holds `review.design.round-count` at or below `review.max-rounds` | 17 | 15, 23 | fold |
| `no-progress-off-by-one` | "past it" and "this many" disagree by one act | — | 16 | fold |
| `budget-before-design-exit` | the rework budget's value before Design's exit is unstated | 20 | 25 | fold |
| `fleet-rename-half` | the `fleet` kind and `kits.fleet` still name adopters | — | 45 | fold |
| `beat-renews-lease` | the supervisor's beat renews the lease every beat, against `leases.renewal: progress` | — | 7 | fold |
| `pool-label-names-login` | the pool label could carry an account's login email | 5 | 3 | refuted in both runs: the owner writes the label |
| `resume-cap-unreachable` | the relaunch cap can never be reached | — | 10 | refuted |
| `open-reading-no-reject` | the CL-3 reading under `[open]` routes no rejection | — | 26 | refuted |
| `coordination-other-stale` | the coordination record keeps other stale statements | — | 42 | refuted |
| `route-backs-vs-max-rounds` | two limits bound one spec-audit loop | 18 | — | refuted |
| `queued-claim-clock-lag` | a lagging claimant clock admits an old queued claim | 33 | — | refuted |
| `proposal-list-stale-value` | the cloud record's proposed key list misses `project` | 34 | — | refuted |

## [summary] The two runs side by side

```text
$ python compare_rounds.py parked-debt-a.md parked-debt-b.md parked-debt-reviews-compared.md session-log.md wf_aeec13f0-079 wf_e27db12b-1f9
== runs
A: raw 34, confirmed 27, refuted 7, precision 0.79, high findings 7, agents 12, out 180.1k (sum of returned lines)
B: raw 48, confirmed 43, refuted 5, precision 0.90, high findings 9, agents 12, out 226.3k (sum of returned lines)
== defects
map rows 42, confirmed defects 35, refuted-only 7
both 15, A only 7, B only 13
A alone covers 22 of 35 (63%)
B alone covers 28 of 35 (80%)
overlap (Jaccard) 0.43
Chapman estimate of the population: 40.7, so about 6 found by neither
A only: tombstone-prune-outrun, renewal-progress-no-interim, spend-cap-no-outcome, repeat-detector-unkeyed, node-ledger-no-schema, p39-clauses-no-plant, values-no-arm
B only: silence-applies-loosening, push-to-closed-terminal, reclaim-attended-slots, release-kinds-merged, keep-waiting-uncounted, stream-plan-unread, owner-keys-no-precedence, fence-red-no-interleaving, round-count-no-pair-rule, no-progress-off-by-one, budget-before-design-exit, fleet-rename-half, beat-renews-lease
== severity (a defect takes its highest confirmed grade per round)
high defects 8: fence-still-check-then-act, release-deletes-lease, tombstone-prune-outrun, route-back-owner-item-stands, fixtures-assert-replaced, renewal-progress-no-interim, request-record-unscanned, silence-applies-loosening
  fence-still-check-then-act: A 3 B 3
  release-deletes-lease: A 3 B 3
  tombstone-prune-outrun: A 3 B 0
  route-back-owner-item-stands: A 3 B 2
  fixtures-assert-replaced: A 3 B 2
  renewal-progress-no-interim: A 3 B 0
  request-record-unscanned: A 3 B 2
  silence-applies-loosening: A 0 B 3
shared defects graded alike 9 of 15
== lenses behind the defects one round alone found
A: correctness 3, seams 2, verification 2
B: correctness 7, seams 4, intent 2, security 1, verification 1
== refuted findings and their twins
A2 (request-record-unscanned): confirmed twin A1, B4
A5 (pool-label-names-login): confirmed twin none
A17 (round-count-no-pair-rule): confirmed twin B15, B23
A18 (route-backs-vs-max-rounds): confirmed twin none
A20 (budget-before-design-exit): confirmed twin B25
A33 (queued-claim-clock-lag): confirmed twin none
A34 (proposal-list-stale-value): confirmed twin none
B3 (pool-label-names-login): confirmed twin none
B10 (resume-cap-unreachable): confirmed twin none
B26 (open-reading-no-reject): confirmed twin none
B35 (repeat-detector-unkeyed): confirmed twin A10
B42 (coordination-other-stale): confirmed twin none
```

- **Every defect sits in the design text.** None reaches shipped code. Nine are an amendment's other half: the cloud
  and stall folds changed v2 and stopped there, leaving layer-runtime's fence, beat and fixtures, flow-steps' unlease
  items and route-back rule, and the cloud record's own `[chain]` stating the replaced design. Seven are clauses with
  no check that can fail, four sit on a build that cannot yet name what they read, and fifteen are holes in what the
  two rounds designed, among them the node's profile and ledgers, owner silence and the lease's release kinds.
- **One run finds about two thirds.** Run A alone covers 22 of the 35 and run B 28, an overlap of 0.43. Chapman's
  estimate puts about six more beyond both.
- **Eight defects are high.** Both runs found the fence and the deleted lease high. Run A alone found the tombstone's
  prune age outrun and the renewal default with no interim, and run B alone found owner silence applying a loosening.
- **Precision held at 0.79 and 0.90.** Eight refuted findings, on seven defects, have no confirmed twin: the pool
  label twice, the relaunch cap, the open reading, the coordination record, the two limits on one loop, the clock lag
  and the proposed key list, each refuted on the record.
- **The skeptics rewrote four fixes.** All four were run B's, ids 1, 2, 4 and 11, and their corrections fold: the
  loosening's decline, the profile's guard, the request record's content key and the push channel's report. Run A's
  skeptics judged all 27 of its fixes sound.

## [fold] The fold plan

Each defect folds as its `[map]` row says, into the records named here. None needs the owner. One reading joins v2
`[open]` for the owner to confirm: `run.on-owner-silence: wait`, SL-4's "wait, as today", becomes a wait parked with
the lease released, since P39 gives every wait an outcome, and no preset selects it.

| Defect | Where it folds |
|---|---|
| `fence-still-check-then-act` | layer-runtime's Fencing, rewritten so the fence travels with the effect, its `named-acts` invariant, and its `fencing` fixture, which now takes the lease over between the holder's read and its push |
| `release-deletes-lease` | flow-steps' `deploy.unlease`, Deploy's Memory bullet and `life.unlease`, each closing a lease with a terminal tombstone; layer-runtime's `awaiting` row, prune bullet and `next` fixture; layer-memory's lease contract and lease kind; layer-expansions' naming; red cases on dShippedRelease and dWellOiledMachine |
| `tombstone-prune-outrun` | `leases.queued-claim-days` and dPlacedRequest's tombstone clause: a queued claim's age counts from its node's last fetch of the lease refs, red on a claim queued after a release by a node whose fetch preceded the lease; the cloud record's item 3 |
| `route-back-owner-item-stands` | flow-steps' `build.reuse-check` and the unverified-finding rule: past `flow.route-backs` the loop ends non-converging and its open work goes to asks |
| `fixtures-assert-replaced` | layer-runtime's `limits` and `relaunch-cap` fixtures, restated with the hand-over release, the lifetime cap and the twice-reaped split; dWellOiledMachine's ledger and waits clauses |
| `renewal-progress-no-interim` | `leases.renewal` and dPlacedRequest's lease clause: until the progress ledger lands, `progress` renews at each item boundary the transition record witnesses, seen on the default preset loaded with no ledger |
| `request-record-unscanned` | dPlacedRequest's request clause pushes only the content key; dWellOiledMachine's scan clause adds request records, publishes the redacted text and binds it by the owner binding's proof; the cloud record's items 10 and 13, and `gap-rt-44` |
| `shared-store-undefined` | dWellOiledMachine's admission clause drops the shared store; the fleet in v2's and the cloud record's `[planned]` gains the pool ledger across machines; the cloud record's item 7 |
| `node-profile-unguarded` | the profile clause: one of the floor's owner-only writes, behind the guarded command, validated at write and at read; the admission clause's one local writer; layer-memory's two node kinds; `[planned]`'s layered proof covers the profile |
| `silence-values-no-route` | `run.on-owner-silence` and the owner-item clause: `remind-then-park` and `wait` each park the build with its lease released, and v2 `[open]` holds the reading of `wait` |
| `spend-cap-no-outcome` | `build.spend-cap` and the spend clause: a build at a set cap ends as `flow.on-exhausted` says |
| `repeat-detector-unkeyed` | `runtime.no-progress`, the ledger clause and the stall record's item 5: a repeat is no new witness |
| `ledger-result-overstated` | `gap-rt-40` in the register and the cloud record, and the cloud record's `[shapes]` and `[fleet]`: the result carries its live reading and p90 sizing; the admission clause witnesses the reading's age |
| `node-ledger-no-schema` | the admission and profile clauses: a versioned schema, a reader refusing a newer major version, a project predating the ledgers counted by its beat; layer-memory's node kinds |
| `p40-clauses-no-plant` | dPlacedRequest's request, acquisition and expiry clauses, and dWellOiledMachine's harness, profile, scan and lander clauses, each with a red of its own |
| `p39-clauses-no-plant` | dKeptSession's card clause, dCalibratedLens's trend clause, and dWellOiledMachine's spend, ledger and waits clauses |
| `max-rounds-no-red` | dDeclaredLoop's convergence clause and dFairHearing's round states: a falling sequence past the limit reads CEILING, and one at it BOUNDED |
| `termination-soundness-no-red` | dDeclaredLoop's static check: the self-routing stage with an exit, a dead-end stage, an unreachable item and an empty state set |
| `values-no-arm` | dWellOiledMachine's owner-item and admission clauses, and dIndexedDesign's `design.streams` clause, each value planted |
| `expiry-reads-later-fact` | dPlacedRequest keeps the observer's clock and the fence primitive; the corrected stamp joins dWellOiledMachine's node-registry clause, and the landing red its lander clause; `leases.expiry-hours` and the cloud record's item 4 |
| `node-arbitration-undefined` | `runtime.admission-scope` and the admission clause: every project charges the node's ledgers, which weigh projects by share; each project's gov reads only its own claimable set; the beat counts free slots against the profile's capacity |
| `chain-plant-shared-account` | the cloud record's `[chain]`, its plants restated as v2's |
| `silence-applies-loosening` | `run.on-owner-silence`, the owner-item clause and dDeclaredLoop's static check: an approval that would loosen a value recommends the decline |
| `push-to-closed-terminal` | `notify.owner-items`, the owner-item clause, and the stall record's item 10 and SC-own-5 row: a core-only install reports `push-when-away` with no push channel |
| `reclaim-attended-slots` | dWellOiledMachine's waits clause, the stall record's item 6 and layer-runtime's `act-ceiling` fixture: only a launched act's slots are reclaimed at the ceiling |
| `release-kinds-merged` | dPlacedRequest's lease clause: a release is a hand-over or terminal; the hold ceiling writes the hand-over and both unlease items the terminal; discovery takes only hand-overs |
| `keep-waiting-uncounted` | flow-steps' `deploy.released` and dShippedRelease's patch-chain clause: the third keep-waiting answer per build and landed SHA parks the build, planted |
| `stream-plan-unread` | dTotalRecall registers the stream-plan kind, dIndexedDesign writes it and dWellOiledMachine's pick reads it, red on a stream picked out of order; layer-memory's kind row |
| `owner-keys-no-precedence` | both owner keys' rows and flow-steps' `[breakpoint]`: the question key decides when the item is raised, the silence key only what stays open at the deadline, its applied recommendation a third witness |
| `fence-red-no-interleaving` | dPlacedRequest's fence clause and layer-runtime's `fencing` fixture: the take-over between the read and the push, and an unchanged lease ref re-pushed |
| `round-count-no-pair-rule` | `[presets]`' pair rules, dKeptSession's preset clause and the preset check, which holds `review.design.round-count` at or below `review.max-rounds` |
| `no-progress-off-by-one` | `runtime.no-progress`'s row reads "this many", and the ledger clause plants an item at exactly that count |
| `budget-before-design-exit` | `flow.rework-budget`, dDeclaredLoop's budget clause and the stall record's item 1: the base alone before Design's exit |
| `fleet-rename-half` | the `adopters` kind, `kits.adopters` and the adopter register in v2, layer-memory, layer-expansions, flow-steps, layer-runtime and the gap register; dShippedRelease's rename clause and its two readers |
| `beat-renews-lease` | layer-runtime's beat renews only as `leases.renewal` says, with a `renewal` fixture; the ledger clause |

**Offered and not folded.** Run B's L1 also offered holding `flow.route-backs` beneath `flow.rework-budget`'s base. No
record states that bound, and wherever the budget is the lower it ends the loop first, as the ceiling does for the round
count, so there is no stated bound to check.

## [folded] Every defect folded, 2026-10-19

All 35 are folded: in v2's catalogue rows, pair rules, chain rows, `[planned]` and `[open]`; in flow-steps,
layer-runtime, layer-memory and layer-expansions; in the cloud and stall records; and in the gap register. No key joins
the catalogue and no gap joins the register. Three kinds join layer-memory: the stream plan, the node profile and the
node ledger. dTotalRecall gains one clause, the stream-plan kind, off the critical path, which stays at 263 units as at `6ba4eaaa1`.
The preset check's pair rules gained the round-count rule, seen red first on a planted override. Five bug classes
record the instances. Every final check passed over the folded records.
