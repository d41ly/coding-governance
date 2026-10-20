# Research: the flow and roles adoption's closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "run the review pair on both folds, medium effort." Two independent light diff reviews read the flow
and roles adoption: its design, the owner's FA-1 to FA-7 folded, and the namespaces that followed. This record compares
them defect by defect, as the earlier paired rounds were compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `e1a54ac67` over `67995cb6f`: the design record and its three researchers' returns (`caca7a636`), the
  owner's FA-1 to FA-7 folded into v2, the systems record, the memory plan, the register, the fates and the design
  record (`cf6f1434c`), the fold's final checks (`dbabaa1fd`), and the `workflow` and `lens` namespaces (`e1a54ac67`).
- **Harness:** `tools/workflows/tier2-review.js`, a light diff review: three `gov-diff-reviewer` lenses (correctness,
  seams, verification), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the owner's medium. The 22
  design records and research returns the folds touch or rest on were the intent inputs, and `gotchas.py --for-diff`
  gave the 21-item checklist. The night pass two's commits through `f8ad789e1` stood in the tree, and each finding
  was judged against the records as they stand.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 139 | `wf_319e98b7-dc6` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-flow-adoption-a.md` |
  | B | 140 | `wf_75d61367-fe8` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-flow-adoption-b.md` |

- **The args:** `build_args_pairs.py` wrote both, beside the answers pair's. A pair's runs differ only in the run
  label, the report path and the scratch path, and the runs went one after the other.
- **Independence:** run A's report was moved out of the tree while run B ran, so no run B agent could read it, and was
  restored byte for byte after (sha256 `ffaf542b78d7`).

## [method] How the runs were compared

The night pass two's comparison's `[method]` applies unchanged
(`build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`). Every finding of both runs,
confirmed or refuted, is placed on the defect it names. A run finds a defect when one of its findings on it was
confirmed, and the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.
The tables are derived by `compare_rounds.py` from the two reports, `[map]` and the session log.

A defect goes to the owner as a fork when its fix is a choice the design does not make itself. Where a skeptic judged a
finder's fix unsound, the skeptic's corrected fix folds. Where the reviewers offered two routes and the owner's words or
an earlier answer settle one, the defect folds by that answer, and its `[fold]` row names it.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `fixed-set-unchecked` | no check refuses an `amends`, a widening or a `supersedes` touching the composition's fixed set, only an exclusion | 2, 9, 12 | 1, 12, 16 | fold: dOrderedCharter's row checks over a fixture kind, each kind's fixed list and reds on its own build |
| `effort-two-homes` | role effort is read from the `roles.effort.*` keys and kept in the house file from dBoundRoles to dConvergedCharter, with no precedence | 1, 7 | 11 | fold: dBoundRoles re-points the readers, keys first and the house file a fallback until the seed retires |
| `effort-default-homeless` | the house file's required `[effort] default` has no destination | 3 | 3 | fold: `roles.effort.default`, the blanket today's resolver reads |
| `stage-default-skips-role` | the stage key's default skips the role's own key, inverting today's resolution order | 4 | — | fold |
| `widening-report-later` | dBoundRoles names a widening in the update's report, which only dShippedRelease extends to rows | 5 | 8 | fold: the clause leaves dBoundRoles for dShippedRelease's |
| `never-policy-file` | dConvergedCharter says effort folds "never [into] the policy file" | 6 | — | fold |
| `gates-two-targets` | the `load_policy` re-point sends the `[gates]` reads to the policy reader, where FA-6 sends them to the role grant | 8 | — | fold |
| `exclude-unplanted` | the widened exclude refusals have no red case | 10 | 17 | fold: a mechanism over a fixture kind, each kind's red on its own build |
| `joins-unplanted` | the item, role, workflow, leg and lens step-gate joins plant no red | 11 | — | fold |
| `widening-unchecked` | FA-5's every widening reported has no check that can fail, and no field declares the direction that widens it | 13 | 19 | fold: directions declared per field, the report compared with the classifier |
| `policy-names-excluded` | an exclusion that a policy value names composes green | 14 | — | fold |
| `model-preset-proof` | the fold put `roles.model.<role>` on the keys presets never touch, where the owner's FA-6 option lets presets set it | — | 2 | fold: by the owner's FA-6 words, presettable |
| `repo-stage-untagged` | a repository stage has no tag, no overlay kind and no place in the step gate | — | 6, 13 | fold |
| `stale-row-values` | `instructions.stale`'s `warn` and `refuse` are undefined or wrong for rows | — | 14 | fold |
| `gov-workflows-untagged` | the `workflow` and `lens` namespaces cover a repository's rows only | — | 15 | fold |
| `splice-ends-unplanted` | the splice check plants no stage before Plan, after Deploy or across non-adjacent stages | — | 18 | fold |
| `chain-map-stale` | the record's `[chain]` misses repository stages and the harness-path check | — | 5 | fold |
| `warn-row-silent` | row `warn` has no failure path and prints nothing | — | 7 | fold |
| `plan-pins-text` | the memory plan pins rows to gov's text, not their canonical form | — | 9, 21 | fold |
| `item-three-stale` | item 3 still states the rejected no-new-stage option | — | 4 | refuted: the bullet marks it unchosen and points at `[folded]` |
| `lens-home-overstated` | `gap-review-17` says a lens has no home beyond per-call notes | — | 10 | refuted: the research measured exactly that |
| `seed-count-reader` | the seed's retirement inventory misses selftest's count of the house file | — | 20 | refuted: a search by name finds it, and the selftest reds on the retirement |

## [summary] The two runs side by side

```text
$ python compare_rounds.py flow-adoption-a.md flow-adoption-b.md flow-adoption-reviews-compared.md session-log.md wf_319e98b7-dc6 wf_75d61367-fe8
== runs
A: raw 14, confirmed 14, refuted 0, precision 1.00, high findings 5, agents 10, out 101.0k (sum of returned lines)
B: raw 21, confirmed 18, refuted 3, precision 0.86, high findings 3, agents 10, out 106.7k (sum of returned lines)
== defects
map rows 22, confirmed defects 19, refuted-only 3
both 6, A only 5, B only 8
A alone covers 11 of 19 (58%)
B alone covers 14 of 19 (74%)
overlap (Jaccard) 0.32
Chapman estimate of the population: 24.7, so about 6 found by neither
A only: stage-default-skips-role, never-policy-file, gates-two-targets, joins-unplanted, policy-names-excluded
B only: model-preset-proof, repo-stage-untagged, stale-row-values, gov-workflows-untagged, splice-ends-unplanted, chain-map-stale, warn-row-silent, plan-pins-text
== severity (a defect takes its highest confirmed grade per round)
high defects 2: fixed-set-unchecked, effort-two-homes
  fixed-set-unchecked: A 3 B 3
  effort-two-homes: A 3 B 2
shared defects graded alike 5 of 6
== lenses behind the defects one round alone found
A: correctness 2, seams 2, verification 1
B: correctness 5, seams 3, verification 2
== refuted findings and their twins
B4 (item-three-stale): confirmed twin none
B10 (lens-home-overstated): confirmed twin none
B20 (seed-count-reader): confirmed twin none
```

- **Every defect sits in the adoption's design text.** None reaches shipped code. Most are clauses the FA fold placed
  with no check that can fail: the fixed set, the exclude refusals, four step-gate joins and the widening report.
- **One run finds about two thirds.** Run A alone covers 11 of the 19 and run B 14, an overlap of 0.32, the lowest of
  the paired rounds so far. Chapman's estimate puts about six more beyond both.
- **Both runs found the fixed set high, and both found effort's two homes.** Run A graded the two homes high and run B
  medium. Run B alone found that the fold had narrowed the owner's FA-6 answer.
- **Precision held at 1.00 and 0.86.** Run B's three refuted findings have no confirmed twin: the stale item 3, the
  lens gap and the seed-count reader, each refuted on the record or the tree.
- **The skeptics rewrote nine fixes.** Three in run A and six in run B were judged unsound, and the skeptics'
  corrections fold. Most move a red case from a build that cannot yet name the kind onto the kind's own build, and one
  widens the widening rule to a `remove` from a constraint set.

## [fold] The fold plan

Each defect folds as its `[map]` row says. None needs the owner: the one route the runs left open on the owner's
ground, whether presets may set `roles.model.<role>`, the owner's FA-6 answer settles, since its chosen option reads
"effort and model as policy keys that presets can set".

| Defect | Where it folds |
|---|---|
| `fixed-set-unchecked` | v2's dOrderedCharter gains one clause, the row checks over a fixture kind; dDeclaredLoop, dBoundRoles, dWitnessedBar and dCalibratedLens each declare their kind's fixed list and plant its reds; the adoption record's items 4, 5, 9 and 11 |
| `effort-two-homes` | v2's preamble and dBoundRoles' shapes and keys clauses: the readers re-pointed in dBoundRoles' unit, keys first, the house file a fallback until dConvergedCharter retires it, red on a planted disagreement; the systems record's effort bullet; layer-roles' effort line; the fates row |
| `effort-default-homeless` | v2's `roles.effort.default` row and its preset row, dBoundRoles' keys clause, dShippedRelease's `adopt.declarations` and its fixture, dConvergedCharter's seed clause; the adoption record's item 8 |
| `stage-default-skips-role` | the two `roles.effort.*` rows' Default cells and dBoundRoles' keys clause: stage, then role, then blanket, then declared; item 8 |
| `widening-report-later` | dBoundRoles' FA clause drops the report; dShippedRelease's report clause already carries it |
| `never-policy-file` | dConvergedCharter's seed clause, reworded |
| `gates-two-targets` | dConvergedCharter's reader clause: `load_policy`'s fallback retired with the seed, its `[gates]` readers on the role grant, never the policy reader |
| `exclude-unplanted` | dOrderedCharter's row checks; the needs red on dDeclaredLoop, the actor and grant reds on dBoundRoles |
| `joins-unplanted` | each join's own build plants a tag removed with no change record, and a successor named green: dDeclaredLoop, dBoundRoles, dWitnessedBar and dCalibratedLens; item 14 |
| `widening-unchecked` | dOrderedCharter's classifier; each kind's directions on its own build; dShippedRelease's report compared with the classifier, red on a dropped widening of each direction; item 10 |
| `policy-names-excluded` | `instructions.exclude`'s row and dOrderedCharter's row checks; the `review.breakpoints` red on dDeclaredLoop and the `review.opt-in` red on dCalibratedLens; item 6 |
| `model-preset-proof` | v2's `roles.model.<role>` row off the never-touch list and onto the preset table; the preset check's free values; the adoption record's `[folded]` |
| `repo-stage-untagged` | dDeclaredLoop's stage clause: `step.repo.<name>`, `item.repo.<stage>.<name>`, the splice row an overlay kind, stage tags joined to the step gate; the adoption record's items 1, 2 and 14; the systems record's row grammar |
| `stale-row-values` | `instructions.stale`'s row and dOrderedCharter's row mechanism: each value defined for rows and planted |
| `gov-workflows-untagged` | the systems record's namespaces; dBoundRoles tags gov's `workflows.toml` entries, red on an `amends` naming a workflow tag gov does not ship |
| `splice-ends-unplanted` | dDeclaredLoop's stage clause: a stage before Plan, after Deploy and across non-adjacent stages, each planted red |
| `chain-map-stale` | the adoption record's `[chain]`, for this fold's clauses too |
| `warn-row-silent` | item 13 and the `instructions.stale` row: a held patch under `warn` prints why |
| `plan-pins-text` | the memory plan's instruction overlay row |

**Found while folding, not folded.** The systems record's tag grammar forbids a namespace word as the first segment
of a tag's name. `repo` has been a namespace since IA-1, and it is that first segment in every repository tag a kind's
namespace holds, `role.repo.<name>` and `policy.repo.<key>` among them. The catalogue's four `policy.*` keys, which the
tags research found free to rename, never were renamed. Neither run raised either. The fix is an exception for the
owner segment or a rename, and both change the grammar the owner's IA-1 and FA-1 answers use, so it waits for the
owner.

**The owner's answer, 2026-10-19, verbatim:** "rename that segment to conform to tag grammar". The segment is
`adopter`, renamed in every design record that carried it; the adoption record's `[renamed]` gives the account. The
four `policy.*` keys were a separate question, put to the owner with the answer. The owner answered, verbatim:
"yes, rename them and add the check but also -  shouldn't lexicon integrate with the tag grammar? Will this be accounted for?" The keys are
`policy-file.*`, dOrderedCharter's shape check enforces the rule, and the lexicon's tag-name check reads the same
namespace words.

## [folded] Every defect folded, 2026-10-19

All 19 are folded: in v2's catalogue, presets and chain rows, the adoption record's design items, `[chain]` and
`[folded]`, the systems record, the memory plan, the fates and layer-roles. `roles.effort.default` joins the catalogue,
now 244 keys, and `roles.model.<role>` joins the preset table. dOrderedCharter gains one clause, the row checks.
The critical path grows by that unit, from 238 at `f8ad789e1` to 239. The preset check's free values gained the
adapter's model set, after the check was seen red on that key's four preset values. Seven bug classes record the
instances. Every final check passed over the folded records.
