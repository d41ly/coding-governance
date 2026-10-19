# Research: the owner's answers' closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "run the review pair on both folds, medium effort." Two independent light diff reviews read the fold
of the owner's answers to the night pass two's forks, NT-1 to NT-28. This record compares them defect by defect, as
the earlier paired rounds were compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `f8ad789e1` over `f064bf378`: the owner's answers folded into v2, the layer records, coordination, the
  memory plan, the register and the night record. Six answers changed the design: NT-12 (effort the owner's), NT-14
  (a change feed and a memory mirror), NT-17 (the notice at every item), NT-19 (a push at every pass commit), NT-22
  (pinned caps) and NT-28 (a limit of six and an admission queue).
- **Harness:** `tools/workflows/tier2-review.js`, a light diff review: three `gov-diff-reviewer` lenses (correctness,
  seams, verification), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the owner's medium. The 25
  design records and research returns the fold touches or rests on were the intent inputs, and `gotchas.py --for-diff`
  gave the 24-item checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 141 | `wf_19434550-87a` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-answers-a.md` |
  | B | 142 | `wf_035611d1-d5f` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-answers-b.md` |

- **The args:** `build_args_pairs.py` wrote both, beside the flow adoption pair's. A pair's runs differ only in the
  run label, the report path and the scratch path, and the runs went one after the other.
- **Independence:** run A's report was moved out of the tree while run B ran, so no run B agent could read it, and was
  restored byte for byte after (sha256 `15006db0cb60`).

## [method] How the runs were compared

The flow adoption comparison's `[method]` applies unchanged
(`build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`). Every finding of both runs, confirmed
or refuted, is placed on the defect it names, and a finding naming two defects lands on both. Where a skeptic judged a
finder's fix unsound, the skeptic's corrected fix folds. Where the reviewers offered two routes and the owner's words
settle one, the defect folds by those words, and its `[fold]` row names them.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `oversize-fan-hangs` | a call whose declared fan exceeds the largest share it can hold waits forever, and in order holds every call behind it | 3 | 1, 19 | fold: the reservation clamped to that share, as the owner's NT-28 asks for a queue instead of a refusal |
| `fallback-refuses` | the ledger's split fallback still refuses the Workflow call the queue now holds, at a limit of five, with no release signal under the fallback | 1, 12, 25 | 11, 20 | fold |
| `start-omits-reservations` | the queue's start condition counts the agents in flight and leaves out the outstanding reservations | 2 | — | fold |
| `queue-witness-vacuous` | the queue's one witness passes with no queue installed, since the harness queues the agents inside one Workflow run | — | 2 | fold |
| `hold-unspiked` | the attended hold rests on a spike no fixture takes and names no outcome past the hold, and layer-runtime states it unconditionally | 4, 21 | 4, 14 | fold |
| `notice-every-item-hollow` | the every-item notice reads a stale local copy, so its witness cannot hold and it adds nothing over `mailbox.reads` | 5, 16 | 15 | fold: one bounded fetch at each item, as the owner's NT-17 sets news at every item |
| `pinned-outside-switch` | `budgets.pinned` can name a cap outside the switch or none at all, and P9 still says one switch decides | 7 | 24 | fold |
| `mirror-no-reader` | no session-side read is routed to the mirror | 10 | 16 | fold: the skeptic's corrected fix, the reads named on dWellOiledMachine |
| `feed-commit-missing` | a record event needs a commit that a `record` write does not have yet | 11 | — | fold: appended when the commit lands |
| `feed-unrebuildable` | the feed's "rebuilt equal from git" cannot hold for pruned refs, has no order across refs and misses hand commits | — | 5 | fold |
| `feed-unwitnessed` | the change feed and its two joins carry no seen case | 23 | 17, 22 | fold |
| `floor-unguarded-file` | NT-12's owner-only floor guards a house file no guard covers | 14 | — | fold: provenance read from the guarded policy file alone |
| `floor-one-carrier` | the floor's witness covers the role key only, never a stage effort or the blanket default | 8 | — | fold |
| `effort-two-defaults` | the effort rows read both the role's declared effort and medium by default | 27 | 18 | fold |
| `floor-no-green-arm` | no arm shows the owner's own low effort accepted | — | 27 | fold |
| `mirror-verdict-unchecked` | nothing turns red when a verdict reads the mirror | 22 | 6, 23 | fold |
| `mirror-pocket-misclassed` | the memory plan files the mirror pocket as out, though it answers reads | — | 6 | fold |
| `push-unwitnessed` | the pass push's freedom from the lander's lock and its bar choice have no check | 24 | 25 | fold |
| `push-clears-verdicts` | a push from the lander's git dir clears a landing's verdict files, which the NT-19 answer's account of the tree misses | — | 7 | fold: the hook leaves them alone on a push not to the default branch, so the push stays free of the lock, as the NT-19 answer gave it |
| `runs-no-gate` | the night record says a pass push runs no gate, where v2 keeps a declared branch bar | 9 | 26 | fold |
| `night-record-stale` | the night record's analysis still states the tool-call notice and the doorbell-only database the answers replaced | 19 | 9 | fold |
| `mirror-point-undeclared` | layer-expansions' integrations contract never declares the memory-mirror point layer-runtime says it fills | — | 10 | fold |
| `gap-mem-46-evidence` | `gap-mem-46` cites evidence that argues against what it needs | 20 | — | fold |
| `gap-rt-36-overstated` | `gap-rt-36` says every spawn over the limit is refused, where a Workflow run's agents queue | 15, 26 | 8 | fold |
| `feed-duplicates` | the feed declares no idempotence key for retried writes | 6 | — | refuted: a retried write is refused by compare-and-swap or as a duplicate, so it appends nothing |
| `feed-population-short` | the feed's population omits the bindings and the card's refs | 18 | — | refuted: the population is the stated design, and the memory plan agrees |
| `partial-admit-stale` | the `in-flight` fixture still admits part of a Workflow's fan | 13 | 3, 13 | refuted: the bullet predates the diff |
| `backstop-ambiguous` | the harness's settings are called a backstop above a key they are rendered at | 17 | 12, 21 | refuted: the backstop is the outer layer, not a higher number |

## [summary] The two runs side by side

```text
$ python compare_rounds.py night-pass-two-answers-a.md night-pass-two-answers-b.md night-pass-two-answers-reviews-compared.md session-log.md wf_19434550-87a wf_035611d1-d5f
== runs
A: raw 27, confirmed 21, refuted 6, precision 0.78, high findings 1, agents 10, out 118.0k (sum of returned lines)
B: raw 27, confirmed 17, refuted 10, precision 0.63, high findings 1, agents 10, out 132.6k (sum of returned lines)
== defects
map rows 28, confirmed defects 24, refuted-only 4
both 9, A only 8, B only 7
A alone covers 17 of 24 (71%)
B alone covers 16 of 24 (67%)
overlap (Jaccard) 0.38
Chapman estimate of the population: 29.6, so about 6 found by neither
A only: start-omits-reservations, notice-every-item-hollow, pinned-outside-switch, feed-commit-missing, floor-unguarded-file, floor-one-carrier, effort-two-defaults, gap-mem-46-evidence
B only: queue-witness-vacuous, feed-unrebuildable, floor-no-green-arm, mirror-pocket-misclassed, push-clears-verdicts, runs-no-gate, mirror-point-undeclared
== severity (a defect takes its highest confirmed grade per round)
high defects 2: oversize-fan-hangs, fallback-refuses
  oversize-fan-hangs: A 2 B 3
  fallback-refuses: A 3 B 2
shared defects graded alike 7 of 9
== lenses behind the defects one round alone found
A: correctness 4, seams 4, verification 1
B: correctness 5, verification 2
== refuted findings and their twins
A6 (feed-duplicates): confirmed twin none
A9 (runs-no-gate): confirmed twin B26
A13 (partial-admit-stale): confirmed twin none
A15 (gap-rt-36-overstated): confirmed twin A26, B8
A17 (backstop-ambiguous): confirmed twin none
A18 (feed-population-short): confirmed twin none
B3 (partial-admit-stale): confirmed twin none
B4 (hold-unspiked): confirmed twin A4, A21, B14
B12 (backstop-ambiguous): confirmed twin none
B13 (partial-admit-stale): confirmed twin none
B15 (notice-every-item-hollow): confirmed twin A5, A16
B18 (effort-two-defaults): confirmed twin A27
B21 (backstop-ambiguous): confirmed twin none
B22 (feed-unwitnessed): confirmed twin A23, B17
B23 (mirror-verdict-unchecked): confirmed twin A22, B6
B24 (pinned-outside-switch): confirmed twin A7
```

- **Every defect sits in the answers' design text.** None reaches shipped code. Most are NT-28's queue and NT-14's
  feed and mirror: new mechanisms whose clauses stated a promise with no case that could fail.
- **One run finds about two thirds.** Run A alone covers 17 of the 24 and run B 16, an overlap of 0.38. Chapman's
  estimate puts about six more beyond both.
- **Each run graded a different high.** Run A graded the fallback's refusal high, and run B the queue's hang on an
  oversize fan. Each run found the other's high and graded it medium.
- **Precision fell to 0.78 and 0.63.** Sixteen findings were refuted, eight of them on defects another finding
  confirmed. Four are conflicts inside one run, where one skeptic refuted what another confirmed: the gap-rt-36
  wording in run A, and in run B the feed's witness, the mirror's verdict check and the attended hold.

## [fold] The fold plan

Each defect folds as its `[map]` row says. None needs the owner. Three defects left two routes, and the owner's own
words chose each: NT-28 asks for "a queue of agents/workflows instead of simply refusing", so a fan too large for its
share is clamped to it rather than refused; NT-17 sets news at every item, so the notice fetches once at each item
rather than restating a slower witness; and the NT-19 answer gave the pass push freedom from the lander's lock, so the
pre-push hook leaves a landing's verdict files alone rather than the push taking the lock.

| Defect | Where it folds |
|---|---|
| `oversize-fan-hangs` | v2's dWellOiledMachine queue: a reservation clamped to the largest share, the harness's per-run setting rendered at it, re-read at admission; a fan of four under a limit of three planted |
| `fallback-refuses` | dWellOiledMachine's ledger fallback: the second Workflow call held, released at the first run's saved result or by the liveness sweep, planted at a limit of six; the queue's count and release under the fallback; the `runtime.agents-in-flight` row |
| `start-omits-reservations` | dWellOiledMachine's queue: the ledger's one admission rule, two fan-four calls planted |
| `queue-witness-vacuous` | dWellOiledMachine's queue: the spawns named, red with the queue stubbed out |
| `hold-unspiked` | dWellOiledMachine's platform spike gains its hold case; the queue's attended route past the hold; layer-runtime's attended entry, `in-flight` and `spike` fixtures |
| `notice-every-item-hollow` | dKeptSession's notice clause and the `mailbox.notice` row; coordination's item 7 |
| `pinned-outside-switch` | the `budgets.pinned` row, P9, the instruction paragraph and dGroundRules' census |
| `mirror-no-reader` | dWellOiledMachine's mirror clause: `record show`, `record find`, the mail notice and the card's pointers |
| `feed-commit-missing` | dTotalRecall's join: every commit that touches a record, once it lands |
| `feed-unrebuildable` | dPlacedRequest's feed: its key, order and population, rebuilt over the refs git still holds |
| `feed-unwitnessed` | the feed's census on dPlacedRequest, and its joins' reds on dKeptSession and dTotalRecall |
| `floor-unguarded-file` | dBoundRoles' NT-12 clause |
| `floor-one-carrier` | dBoundRoles' NT-12 clause: a role key, a stage key and `roles.effort.default` planted |
| `effort-two-defaults` | the three `roles.effort.*` rows' Source cells |
| `floor-no-green-arm` | dBoundRoles' NT-12 clause: the owner's low effort planted green |
| `mirror-verdict-unchecked` | dWellOiledMachine's mirror clause: outputs compared with the mirror on and off |
| `mirror-pocket-misclassed` | the memory plan's mirror pocket, a witness keyed by the feed's event key |
| `push-unwitnessed` | dWellOiledMachine's push clause: a push under a held lock, its run-log line |
| `push-clears-verdicts` | dWellOiledMachine's push clause, the night record's point 4 and its NT-19 answer |
| `runs-no-gate` | the night record's point 4 and its NT-19 answer |
| `night-record-stale` | the night record's point 3 and point 4 analysis |
| `mirror-point-undeclared` | layer-expansions' integrations kinds and points |
| `gap-mem-46-evidence` | the register's `gap-mem-46` |
| `gap-rt-36-overstated` | the register's `gap-rt-36` |

## [folded] Every defect folded, 2026-10-19

All 24 are folded: in v2's catalogue, principles and chain rows, layer-runtime, layer-expansions, coordination, the
memory plan, the register and the night record. The folds edited clauses in place and added no key and no gap, so
the critical path stays at 239 units, as at `1edb2d167`. Seven bug classes record the instances. Every final check
passed over the folded records.
