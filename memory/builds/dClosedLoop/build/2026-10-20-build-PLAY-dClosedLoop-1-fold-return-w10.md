# Fold return: writer 10, the closing pair's fold

**Serves:** research PLAY-dClosedLoop-1

Dispatch 211's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-49-spec-writer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

Every defect has a disposition and the fold script is complete. I made one choice the owner hasn't made yet (FK-10-1 below), and two of my edits differ from what the comparison record's `[fold]` rows say, for reasons the records show:
- **No re-cut row for `next`.** `next` is a command, and the probe does not read commands as nodes. A row for it would red the probe. Planting it shows that: `--plant-add dKeptSession:next:dWellOiledMachine` gives `class row with no dependency`.
- **`life.release` is now `life.unlease`.** v2:293 renamed it, so cl-0505 names `life.unlease`.

## 1. Dispositions

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

## 2. Fold script

`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w10/fold-10.py` makes 68 edits:

| record | edits |
|---|---|
| architecture-v2 | 19 |
| recut | 19 |
| flow-steps | 14 |
| layer-memory | 4 |
| flow | 3 |
| layer-runtime | 2 |
| layer-expansions | 2 |
| ownership | 2 |
| fates | 2 |
| memory-plan | 1 |

Every edit matched its anchor exactly once. No clause is new, so there are no placeholder ids. Mint ran with 0 minted, and the next free id stays `cl-dClosedLoop-0510`. Clauses cite other clauses in the short form (`cl-0134`), because a backticked full id inside a clause reds the clause-ids check. Every record that keeps a revision log gets a note; memory-plan and fates keep none.

## 3. Forks

### FK-10-1 — What rule does cl-0339 state for `measured`'s threshold?
The owner chose (a), but none of the records fixes the rule itself.
- **(a)** Hold at 2 in 10 until every leg has 30 verdicts in the flake records. Then use one more than the 90th percentile, across legs, of each leg's flakes in its last ten verdicts, re-derived at each gate-health measurement.
- **(b)** The same, but per leg, from each leg's own percentile.
- **(c)** Like (a), but never looser than 2 in 10.

**Recommended: (a).** It follows `memory.item-budget`'s `measured` pattern (fixed until 30 measured, then a p90). (b) would never hold a chronically flaky leg. The script writes (a), so changing it means swapping one sentence in cl-0339. Rests on `flakes-measured-no-writer`.

## 4. Requests

Each needs a class from K2's set. K2 does not carry a classed entry's reach on to the items it reaches, which is why each needs its own row.

| arm | node | class | reason |
|---|---|---|---|
| K2 | `adopt.instructions` | external entry | Entered only from `kits.install` or the core's own command, both started outside any item. |
| K2 | `adopt.declarations` | external entry | Same, through `kits.install` or `kits.update`. |
| K2 | `kits.install-attended` | external entry | Reached only through `kits.install`, which the owner's operator order, an outbox order or the prepared merge starts (cl-0025). |
| K2 | `kits.update-attended` | external entry | Same, through `kits.update`. |
| K2 | `mailbox.answer` | external entry | A `question` arrives from another build's session through the mailbox, and `next` is a verb, not an item. |

## 5. The dry run and Stage 0

- **Dry run:** last line `ALL rc 0`. All ten checks are rc 0, and the reconciliation probe reports findings 0.
- **Stage 0, from the dry folder:**

| | K1 | K2 | K3 | K4 | K5 | total |
|---|---|---|---|---|---|---|
| after the fold | 0 | 28 | 76 | 1 | 0 | 105 (classed 0) |
| after the Rule-column step alone | 1 | 31 | 76 | 4 | 0 | 112 |

- The K1 cycle is gone, and so are `mailbox.answer`'s actor, unformed-target and ends-nowhere reds and K4's `leases.overlap`, `kits.cadence` and `runtime.attended-allowance`.
- The one K4 red left, `roles.shape-enforce`, was red before the fold and is not one the fold names.
- Two reruns are red, line coverage and review debt. Both call git, and the dry folder is not a repository. Line coverage in the worktree shows unreviewed 0.
- **K1 plants** still red: `k1-cycle` and `k1-owning-role`.
- **Planted rows:**

| plant | result |
|---|---|
| `--plant-why "dDeclaredLoop:design.ready=today's tool"` | `tolerance row names no stand-in: dDeclaredLoop routes design.ready says today's tool and names no path that exists`, findings 1 |
| same row naming a missing path | red |
| `--plant-why` on the `build.distill` row | red |
| `--plant-drop dWellOiledMachine:deploy.unlease:cites` | UNCLASSED |

## 6. Read outside the list above

Git history at `10c0c4fb4`, to see which reds and rows the fold introduced. I also read the scratch copies in `w10/base` (the Rule-column step's output) and `w10/work`, which I made for iterating. Everything else was the working tree, the composite, the two reports, the comparison record or the scratch fold tools.
