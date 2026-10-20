# Research: the night pass two's closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "Run tier2 reviews on the folds twice." Two independent light diff reviews read the night pass two's
folds, the seven points worked unattended. This record compares them defect by defect, as the earlier paired rounds
were compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `ad54fe388` over `e1a54ac67`: the record that opens the night pass two (`0657a8667`) and the seven
  points' folds, `43bd58baa`, `f27b6e3b2`, `dff70c5f8`, `da51d45c4`, `d171bcb47`, `723abc12b` and `ad54fe388`.
- **Harness:** `tools/workflows/tier2-review.js`, a light diff review: three `gov-diff-reviewer` lenses (correctness,
  seams, verification), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the owner's medium. The 33
  design records and research returns the folds touch or rest on were the intent inputs, and `gotchas.py --for-diff`
  gave the 26-item checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 137 | `wf_4e7e18b8-a33` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-a.md` |
  | B | 138 | `wf_9c278556-e2c` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-b.md` |

- **The args:** `build_args_night2.py` wrote both. They differ only in the run label, the report path and the scratch
  path, and the runs went one after the other.
- **Independence:** run A's report was moved out of the tree while run B ran, so no run B agent could read it, and was
  restored byte for byte after (sha256 `2ed7e7563b28`).

## [method] How the runs were compared

The runtime comparison's `[method]` applies unchanged: every finding of both runs, confirmed or refuted, is placed on
the defect it names, a finding naming two defects lands on both, a run finds a defect when one of its findings on it was
confirmed, and the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.
The tables are derived by `compare_rounds.py` from the two reports, `[map]` and the session log.

A defect goes to the owner as a fork when its fix is a choice the design does not make itself. Where the reviewers
offered two routes and the owner's words or an earlier answer settle one, the defect folds by that answer, and its
`[fold]` row names it. A recommendation still pending on an NT fork is revised in place, and stays pending.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `problem-keys` | the problem register keeps one problem per path, and no dotfile path is a legal ref name | 2 | — | fold: one ref per problem under its encoded subject |
| `clamp-kept` | dGroundRules re-points agent-cap's readers but keeps its clamp to 1 to 5 and the two rules point 7's table gives it | 1 | 10 | fold |
| `over-budget-stale` | layer-instruction, layer-roles and the adopter record still refuse a set over budget under `instructions.checks` | 3, 21 | 6, 19 | fold |
| `direct-refuses` | the record says both harness settings queue, where the direct one refuses and is unenforced under ultracode | 4, 24 | 9 | fold, the window recorded as `gap-rt-35` |
| `grammar-class-dropped` | point 5 drops the caps research's third kept class, the limits that define a format, and NT-22 never offers it | 6 | — | fold: NT-22's second option |
| `checklist-unowned` | no build retires the per-pass checklist and the prebuild point 6 retires, and dScopedBuild still witnesses the checklist | 7, 35 | — | fold |
| `mail-ref-node` | the mail ref is keyed by node in coordination and v2 and by sender in the memory plan, and one node's sessions share it | 9, 29 | 5, 21 | fold: keyed by writing session |
| `message-id-collides` | derived message ids collide for two answers from one item, and a sender with no act has no key | 10 | 12 | fold: the answered id joins the key |
| `blob-keys-paths` | the index keys what a path names by blob alone, though one blob sits at many paths | 11 | — | fold |
| `hook-counts` | the review-system's new text and the adoption record still have agent-cap count lens slots and admit harnesses | 12 | 3 | fold |
| `method-misdescribes` | the record's method says agent-cap admits five spawns at a time, which its point 7 measured otherwise | 12 | 22 | fold |
| `population-misstated` | point 6 gives its population as 47 reviews with a classes column, where 66 carry one and 47 of them a range | 13 | — | fold |
| `record-unrouted` | `budgets.enforce`'s `record` has no meaning and no arm | 15, 16 | — | fold: dropped |
| `fates-stale` | the fates table keeps `agent-cap.js` as staying and `gotchas.py` handing classes by write set | 17, 18, 34 | 1, 18 | fold |
| `fanout-systems` | the systems record still bounds the shapes' cap by `FANOUT_CAP` and lists agent-cap's `args.roles` refusal | 19, 32 | 2, 16 | fold |
| `fanout-adoption` | the adoption record's fixed set still names `FANOUT_CAP`'s bound | 20, 33 | 17 | fold |
| `ledger-double-counts` | the kept reservation and the new SubagentStart claims count a Workflow's agents twice | 22 | 15 | fold |
| `direct-unbounded` | the key is a session total no build enforces before the ledger arms, and dGroundRules tests only its Workflow half | 5, 23, 30 | 14, 25 | fold |
| `decline-unrecorded` | a declined scenario promotion has no record, so every Loop Review raises it again | 27 | — | fold |
| `reuse-dispute` | the reuse check has no route for a disputed row and no bound on its re-entries | 28 | — | fold |
| `switch-census` | `budgets.enforce` covers every size gate and is proven on one planted file | 31 | 26 | fold: a census |
| `session-readers` | `gov-session`'s retirement inventories none of its readers | 36 | 30 | fold |
| `overflow-clean` | units past the reuse check's cap of sixty read clean | 37 | — | fold |
| `gated-self-declared` | a bug class leaves every review checklist on a gated mark that nothing verifies | 38 | 24 | fold: run B's confirmation, since the mark exempts a class from review and is no unit detail |
| `gated-field-later` | dFairHearing's checklist cut reads a gate status only dLinkedLibrary creates | 8 | 7 | fold: the cut moves to dLinkedLibrary |
| `keys-later-kinds` | dKeptSession keys message ids on acts and dPlacedRequest decisions on work-order slots, both minted later | — | 8 | fold: each names the key it uses until then |
| `preset-values-unrouted` | presets select `flow.*` and `build.unit-holders` values that no reading clause routes or witnesses | — | 13 | fold |
| `spike-cannot-fail` | the spike never plants the four end kinds that arm the ledger, and the in-flight fixture has no mixed case | — | 23 | fold |
| `fork-options-excluded` | NT-27 and NT-28 offer options the owner's words rule out | — | 11 | fold: the options restated |
| `over-budget-exempt-stale` | `memory.over-budget` still exempts slices from `instructions.checks`' refusal | — | 20 | fold |
| `per-tree-stale` | dWellOiledMachine still reads beside "the per-tree index", and the shared index's dirty rows have no worktree | — | 4 | fold |
| `stage-cap-lowered` | lowering the limit reds gov's own five-wide workflow entries | 14 | 27 | refuted: the stated invariant, which an overlay meets |
| `push-values` | `build.push`'s non-default values have no witness | 25 | — | refuted: owner options whose cost is the choice |
| `notice-values` | `mailbox.notice`'s `every-item` and `off` cannot be told apart | 26 | — | refuted: they differ under `mailbox.reads: transitions-only` |
| `lens-unplanted` | dCalibratedLens' new clauses name no planted case | 39 | 28 | refuted: their observable is stated, and the fixture is unit detail |
| `scenario-never-touch` | nothing reds a scenario override of a key presets never touch | 40 | — | refuted: the clause forbids it, and the red arm is unit detail |
| `rebuild-unchecked` | the index's rebuild equality names no check | 41 | — | refuted: the owning clause states it, and the record lists the test as owed |
| `unit-holders-unchecked` | `build.unit-holders` names no planted case | — | 29 | refuted: the lease and fencing design already stops a second driver |

## [summary] The two runs side by side

```text
$ python compare_rounds.py night-pass-two-a.md night-pass-two-b.md night-pass-two-reviews-compared.md session-log.md wf_4e7e18b8-a33 wf_9c278556-e2c
== runs
A: raw 41, confirmed 31, refuted 10, precision 0.76, high findings 1, agents 10, out 177.6k (sum of returned lines)
B: raw 30, confirmed 26, refuted 4, precision 0.87, high findings 2, agents 10, out 149.7k (sum of returned lines)
== defects
map rows 38, confirmed defects 31, refuted-only 7
both 13, A only 10, B only 8
A alone covers 23 of 31 (74%)
B alone covers 21 of 31 (68%)
overlap (Jaccard) 0.42
Chapman estimate of the population: 36.7, so about 6 found by neither
A only: problem-keys, grammar-class-dropped, checklist-unowned, message-id-collides, blob-keys-paths, population-misstated, record-unrouted, decline-unrecorded, reuse-dispute, overflow-clean
B only: gated-self-declared, gated-field-later, keys-later-kinds, preset-values-unrouted, spike-cannot-fail, fork-options-excluded, over-budget-exempt-stale, per-tree-stale
== severity (a defect takes its highest confirmed grade per round)
high defects 3: problem-keys, fates-stale, gated-self-declared
  problem-keys: A 3 B 0
  fates-stale: A 2 B 3
  gated-self-declared: A 0 B 3
shared defects graded alike 9 of 13
== lenses behind the defects one round alone found
A: correctness 6, seams 3, verification 2
B: correctness 4, verification 2, seams 2
== refuted findings and their twins
A5 (direct-unbounded): confirmed twin A23, A30, B14, B25
A8 (gated-field-later): confirmed twin B7
A14 (stage-cap-lowered): confirmed twin none
A15 (record-unrouted): confirmed twin A16
A25 (push-values): confirmed twin none
A26 (notice-values): confirmed twin none
A38 (gated-self-declared): confirmed twin B24
A39 (lens-unplanted): confirmed twin none
A40 (scenario-never-touch): confirmed twin none
A41 (rebuild-unchecked): confirmed twin none
B12 (message-id-collides): confirmed twin A10
B27 (stage-cap-lowered): confirmed twin none
B28 (lens-unplanted): confirmed twin none
B29 (unit-holders-unchecked): confirmed twin none
```

- **Every defect sits in the night's own text.** None reaches shipped code. Most are folds that landed in v2 and
  stopped there: point 5's over-budget refusal, and point 7's `FANOUT_CAP` and agent-cap, still stood in the layer,
  systems, adoption and fates records.
- **One run finds about seven in ten.** Run A alone covers 23 of the 31 and run B 21, an overlap of 0.42, inside the
  range of the earlier pairs. Chapman's estimate puts about six more beyond both.
- **Each run caught a high the other missed.** Run A alone found the problem register's per-path key. Run B alone
  confirmed the self-declared gated mark, which run A's skeptic refuted as unit detail, and graded the stale fates
  high where run A graded them medium.
- **Precision held at 0.76 and 0.87.** Five of the 14 refuted findings sit on defects another finding confirmed. Three
  are conflicts between the runs' skeptics: `gated-self-declared` and `gated-field-later`, refuted in run A and
  confirmed in run B, and `message-id-collides`, confirmed in run A and refuted in run B for want of a defined subject.

## [fold] The fold plan

Each defect folds as its `[map]` row says. None needs the owner. Where the runs left two routes, the owner's words or
an earlier answer chose one, and a recommendation pending on an NT fork stays pending.

| Defect | Where it folds |
|---|---|
| `problem-keys` | v2's dPlacedRequest: `refs/gov/problems/<encoded subject>/<problem id>`, two problems on one path and a dotfile path planted; the record's `[p4-handoffs]` |
| `clamp-kept` | v2's dGroundRules: the raw-primitive ban, the bound rule's concurrency half and the clamp retired, a limit of eight admitted |
| `over-budget-stale` | layer-instruction's R-C and P27 check, layer-roles' render and budgets, the adopter record's item 12 and table |
| `direct-refuses` | the record's `[p7-agent-cap]`, the key's catalogue row, and `gap-rt-35`, owned by dWellOiledMachine, whose ledger closes it |
| `grammar-class-dropped` | the record's `[p5-caps]`, its dispatch row and NT-22's options |
| `checklist-unowned` | v2's dFurnishedOrders retires the per-pass checklist, the prebuild and every call of the lookup by a write set's paths, readers inventoried; dScopedBuild witnesses the retirement |
| `mail-ref-node` | v2's dKeptSession, coordination's item 6, the memory plan, the record's `[p3-storage]` and NT-16: `refs/gov/mail/<slug>/<fleet tag>/<session>` |
| `message-id-collides` | v2's dKeptSession: the session, the item and pass, the kind, the subject and the answered id, two acknowledgements planted |
| `blob-keys-paths` | v2's dOrderedCharter and the systems record's `[cross]` and index bullet: a tree-and-path table, path rows keyed by path and blob |
| `hook-counts` | the review-system record, and the adoption record's three agent-cap lines |
| `method-misdescribes` | the record's `[method]` and `[p1-scenarios]` |
| `population-misstated` | the record's `[p6-gotchas]` |
| `record-unrouted` | v2's `budgets.enforce` row: `warn` and `refuse` |
| `fates-stale` | the fates table: `agent-cap.js` retired, `gotchas.py` reshaped, the counts restated; layer-memory's gotcha row |
| `fanout-systems` | the systems record's shapes cap and `args.roles` consumer |
| `fanout-adoption` | the adoption record's fixed set |
| `ledger-double-counts` | v2's dWellOiledMachine and layer-runtime's `[supervise]`: a Workflow agent's claim converts a slot of its call's reservation |
| `direct-unbounded` | v2's key row states the interim, dGroundRules plants the direct half and the rendered settings, dWellOiledMachine names the fallback's split and plants the combined total |
| `decline-unrecorded` | v2's dCalibratedLens: a decline recorded and not raised again |
| `reuse-dispute` | v2's dScopedBuild and flow-steps' `build.reuse-check`: a disputed row to the closing review, re-entries bounded by `flow.route-backs` |
| `switch-census` | v2's dGroundRules: every listed cap planted under each value, and the correctness refusals planted under `warn` |
| `session-readers` | v2's dWellOiledMachine: `gov-session`'s readers inventoried by value and re-pointed |
| `overflow-clean` | v2's dScopedBuild and flow-steps: an overflow takes a further pass, never clean |
| `gated-self-declared` | v2's dLinkedLibrary: the gate status derived from a named leg seen to refuse a planted case; the record's `[p6-gotchas]` |
| `gated-field-later` | v2's dFairHearing leaves the cut to dLinkedLibrary's derived status |
| `keys-later-kinds` | v2's dKeptSession and dPlacedRequest name the keys they use until acts and work-order slots exist |
| `preset-values-unrouted` | v2's dDeclaredLoop, dCalibratedLens and dWellOiledMachine: each catalogued value's arm and planted case |
| `spike-cannot-fail` | layer-runtime's `spike` and `in-flight` fixtures |
| `fork-options-excluded` | the record's NT-27 and NT-28 |
| `over-budget-exempt-stale` | v2's `memory.over-budget` row |
| `per-tree-stale` | v2's dWellOiledMachine and dOrderedCharter, and the systems record's uncommitted-edit bullet |

## [folded] Every defect folded, 2026-10-19

All 31 are folded, in v2's catalogue and chain rows, the layer-instruction, layer-roles, layer-memory and
layer-runtime records, the systems, coordination, memory-plan, adopter-instructions, adoption, review-system and fates
records, flow-steps' reuse check, and the night record's sections, `[reviewed]` and forks. The register gains
`gap-rt-35`, owned by dWellOiledMachine, and eleven bug classes record the instances. The fates table now holds 22
staying, 74 reshaped, 25 merged and 18 retired parts. The folds edited clauses in place, so the chain keeps 236 units
on its critical path. Every final check passed over the folded records on the first run.
