# Research: the last three folds' closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "Run the reviews of the same shape (medium effort, twice) for the last three folds." Two independent
light diff reviews read the shape audit's fold, the Skills' fold and the adopter instructions' fold. This record
compares them defect by defect, as the earlier paired rounds were compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `320c79646` over `dd1ebb01b`: the shape audit's fold (`23baa12de`), the Skills' answers (`17355b8b1`,
  `a0b1a06c4`), and the adopter-instructions research and fold (`926106e87`, `320c79646`).
- **Harness:** `tools/workflows/tier2-review.js`, a light diff review: three `gov-diff-reviewer` lenses (correctness,
  seams, verification), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the owner's medium. The 35
  design records the folds touch or rest on were the intent inputs, and `gotchas.py --for-diff` gave the 34-item
  checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 122 | `wf_32d759cc-d9a` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-folds-closing-a.md` |
  | B | 126 | `wf_a3ab6ac1-aba` | `reviews/2026-10-19-review-PLAY-dClosedLoop-1-folds-closing-b.md` |

- **The args:** `build_args_folds.py` wrote both. They differ only in the run label, the report path and the scratch
  path, checked before run B launched, and the runs went one after the other.
- **Independence:** run A's report was moved out of the tree while run B ran, so no run B agent could read it, and was
  restored byte for byte after (sha256 `af2916008b87`).

## [method] How the runs were compared

The runtime comparison's `[method]` applies unchanged: every finding of both runs, confirmed or refuted, is placed on
the defect it names, a finding naming two defects lands on both, a run finds a defect when one of its findings on it was
confirmed, and the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.
The tables are derived by `compare_rounds.py` from the two reports, `[map]` and the session log.

A defect goes to the owner as a fork when its fix is a choice the design does not make itself: a new mechanism, a
change of owner, or one of two routes the reviewers left open. Where the reviewers offered two routes and the owner's
earlier answers settle one, the defect folds by that answer, and its `[fold]` row names it.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `receipt-steps-later` | dSafePassage's walk and gov first read the receipt's `steps` field, which only dShippedRelease's schema 4 adds | 1 | — | fold: the field moves with the clauses that read it, as SA-3 placed gov first |
| `self-update-unplaced` | gov's update of itself every release sits on no chain row, and the adopter record's `[chain]` and `[folded]` disagree | — | 6 | fold |
| `native-id-later` | dOrderedCharter's native-id edge names only classes later builds register, and FAMILY ids and gap keys have no owner | 2 | 3 | fold |
| `own-steps-missing` | dOrderedCharter's own upgrade steps omit the adopter rules' move, the seeded template's retirement and the census moves | 3 | 19 | fold |
| `stale-values-unrouted` | `instructions.stale`'s `refuse` and `warn` have no arm, witness or planted case | 4, 12, 30 | 11 | fold |
| `kickoff-path-readers` | the `/session-kickoff` retirement inventories its readers by value only and misses the directory's path readers | 5 | — | fold |
| `deploy-row-units` | the memory plan's deploy-overlay row still gives `deploy.toml` level-0 units and `instructions.edit` as its one door | 6, 14 | 1, 17 | fold |
| `unit-schema-stale` | the systems record's unit schema lacks the origin, the class, pinned edges and a list successor, and still says merged by row key | 7, 18 | 4, 5, 14 | fold |
| `p8-only` | P8's "only through its own units' typed edges" leaves out `instructions.exclude` and the in-document parts | 10, 22 | — | fold |
| `house-glob` | dBoundRoles moves "the roles kit's house files" without scoping out `house/policy.toml` | 11 | 8 | fold |
| `selector-fates` | the fates record still hands the bug-class selector to dLinkedLibrary | 13 | — | fold |
| `two-successions` | the step gate admits a `[[retired]]` row and a change record as two witnesses of one unit-tag rename | 15 | 13 | fold: the change record is the unit tags' one witness |
| `owner-field` | the unit field "owner, a kit or the repository" clashes with the `owner` edge and the one-owner rule | 17 | — | fold: the field is renamed `origin` |
| `sk2-readers` | the `gov-<name>` renames take no reader inventory | 20 | — | fold |
| `arm-3c` | the retired-edited check is pinned to arm 3c, which never reads a receipt row | 24 | — | fold |
| `editorial-unchecked` | nothing checks the `editorial` mark that exempts a pin from drift | 25 | 18 | fold |
| `joins-unarmed` | no owning build arms the step gate's later classes, and v2's `[owed]` dropped the restructure map | 26 | 2, 20 | fold |
| `edited-render-unplanted` | the update's held edited render has no planted case | 27 | — | fold |
| `pin-grammar` | the pinned target `<tag>@<hash>` has no parse rule in the address grammar and no malformed-input case | 19, 28 | 12, 23 | fold: a tag qualified by its hash, legal on `amends` and `supersedes` only |
| `adopt-unfixtured` | `adopt.instructions`' no-overwrite and wiring promises have no fixture | 29 | — | fold |
| `repo-keys-unread` | a repository's `repo.` policy keys have no file, schema or reader | — | 15 | fold |
| `fixed-class-typed` | the fixed class is declared by hand, and no query derives the units a gov tool parses | — | 21 | fold |
| `deploy-26-halves` | `gap-deploy-26` joins two facts that two builds close | 9 | 9 | fold: the register writes down its rule for a gap two builds close, which keeps this one with dLinkedLibrary, dOrderedCharter's descendant |
| `p38-wording` | P38 says the step gate reds a change of a surface, and the gate passes a content-only change | — | 10 | fold |
| `legacy-block-key` | the install's legacy block does not say how `instructions.legacy` governs it | — | 16 | fold |
| `derived-fact-hash` | a pin hashes gov's unit text, though a fact's text is derived | 8 | — | refuted: the unit is its row, and a derived value is no change to it |
| `stale-lock-holder` | the moved stale-lock reclaim publishes no holder record | 16 | — | refuted: the gap was there at the base, and its mechanics are unit-level |
| `found-29-halves` | `gap-found-29`'s `re-rendered` half is closed by dSafePassage, whose row lists no key | 21 | — | refuted: the descendant completing the closure owns the gap, the rule `deploy-26-halves` writes down |
| `retired-edits-values` | `install.retired-edits`' `keep` and `delete` have no arm | 23 | — | refuted: unchanged from the base |
| `repo-keys-presets` | dropping "outside the presets' completeness check" lets a repository key collide with the presets | — | 7 | refuted: a repository key is neither catalogued nor presettable |
| `guard-unplanted` | the minimal guard's added path has no planted arm | — | 22 | refuted: the guard had none at the base |

## [summary] The two runs side by side

```text
$ python compare_rounds.py folds-closing-a.md folds-closing-b.md folds-reviews-compared.md session-log.md wf_32d759cc-d9a wf_a3ab6ac1-aba
== runs
A: raw 30, confirmed 24, refuted 6, precision 0.80, high findings 1, agents 10, out 152.8k (sum of returned lines)
B: raw 23, confirmed 21, refuted 2, precision 0.91, high findings 0, agents 10, out 143.0k (sum of returned lines)
== defects
map rows 31, confirmed defects 25, refuted-only 6
both 10, A only 9, B only 6
A alone covers 19 of 25 (76%)
B alone covers 16 of 25 (64%)
overlap (Jaccard) 0.40
Chapman estimate of the population: 29.9, so about 5 found by neither
A only: receipt-steps-later, kickoff-path-readers, p8-only, selector-fates, owner-field, sk2-readers, arm-3c, edited-render-unplanted, adopt-unfixtured
B only: self-update-unplaced, repo-keys-unread, fixed-class-typed, deploy-26-halves, p38-wording, legacy-block-key
== severity (a defect takes its highest confirmed grade per round)
high defects 1: receipt-steps-later
  receipt-steps-later: A 3 B 0
shared defects graded alike 10 of 10
== lenses behind the defects one round alone found
A: seams 4, correctness 3, verification 3
B: correctness 3, seams 2, verification 1
== refuted findings and their twins
A8 (derived-fact-hash): confirmed twin none
A9 (deploy-26-halves): confirmed twin B9
A16 (stale-lock-holder): confirmed twin none
A19 (pin-grammar): confirmed twin A28, B12, B23
A21 (found-29-halves): confirmed twin none
A23 (retired-edits-values): confirmed twin none
B7 (repo-keys-presets): confirmed twin none
B22 (guard-unplanted): confirmed twin none
```

- **Every defect sits in the folds' own text.** None reaches shipped code, and the adopter-instructions fold holds the
  most: a design record landed whole, while the schemas, the grammar and the checks it rests on moved only halfway.
- **One run finds about seven in ten.** Run A alone covers 19 of the 25 and run B 16, an overlap of 0.40, inside the
  range of the earlier pairs. Chapman's estimate puts about five more beyond both.
- **Run A caught the one high alone:** dSafePassage's walk and gov first read a receipt field that only a later
  build adds.
- **Precision held at 0.80 and 0.91.** Two refuted findings sit on defects another finding confirmed. One is a true
  conflict: run A's skeptic refuted `gap-deploy-26`'s split under an unwritten rule, and run B's confirmed it.

## [fold] The fold plan

Each defect folds as its `[map]` row says, in the records below. None needs the owner: where the reviewers left two
routes, an earlier answer chose one.

| Defect | Where it folds |
|---|---|
| `receipt-steps-later` | v2: dSafePassage gains the receipt's schema 4 with `steps`, its down and its readers; dShippedRelease's bump becomes schema 5. SA-3 put gov first, which reads the field, in dSafePassage |
| `self-update-unplaced` | v2: gov first creates gov's receipt and runs `update` on gov; dShippedRelease updates gov's own install first at every release. The adopter record's `[chain]` follows |
| `native-id-later` | v2: dOrderedCharter plants the native-id edge on the FAMILY ids it owns; dTotalRecall registers gap keys. The memory plan's `[frame]` names both owners |
| `own-steps-missing` | v2: dOrderedCharter's own steps gain the adopter rules' conversion, the template's `[[retired]]` row and the census moves' change records |
| `stale-values-unrouted` | v2: each `instructions.stale` value gets its arm and a planted semantic change |
| `kickoff-path-readers` | v2: `/session-kickoff`'s retirement inventories by path and by value, and `manifest-check.sh` moves to a kit home of its own first |
| `deploy-row-units` | the memory plan: the deploy overlay holds answers and kit selection, never units; govkit and the upgrade-step kind join `[doors]` |
| `unit-schema-stale` | the systems record: the unit gains `origin`, `class` and `edges`, `status` takes a list or `none`, the change record a list, and "merged by row key" goes |
| `p8-only` | v2: P8 names the add, the edges and the exclusion, and the marked parts |
| `house-glob` | v2: dBoundRoles moves `house/*.md` only |
| `selector-fates` | the fates record: `gotchas.py`'s row names dFurnishedOrders (SA-7) |
| `two-successions` | v2: a class whose change record names its successor reads that record as its one witness |
| `owner-field` | v2, the systems record, the memory plan and the adopter record: the field is `origin`, and `one-owner` applies to what gov ships |
| `sk2-readers` | v2: each `gov-<name>` rename inventories and re-points its readers |
| `arm-3c` | v2: the retired-edited check reads update's role-to-verdict mapping |
| `editorial-unchecked` | v2: `editorial` only for a mechanical diff or the owner's proof-carrying ruling, seen red on a mislabelled meaning change |
| `joins-unarmed` | v2: the step gate takes policy keys at once, dOrderedCharter arms unit tags and dTotalRecall record-kind schemas; the restructure map returns to `[owed]` |
| `edited-render-unplanted` | v2: a planted hand-edited render, red on today's mapping |
| `pin-grammar` | v2 and the memory plan: the pinned tag is an address form legal on `amends` and `supersedes`, with four malformed cases |
| `adopt-unfixtured` | v2: `adopt.instructions` on a fixture with three existing instruction files, red on today's installer |
| `repo-keys-unread` | v2: repository keys declared in the overlay, set in the policy file, tagged `policy.repo.<key>`, read through dGroundRules' reader |
| `fixed-class-typed` | v2: the class derived from the parsers and the floor, a parsed unit declared `open` red |
| `deploy-26-halves` | the gap register: the rule for a gap two builds close, written down |
| `p38-wording` | v2: P38 says what the gate reds, and leaves a change of meaning to review |
| `legacy-block-key` | v2: the legacy block joins `instructions.legacy`'s population, admitted at install only |

## [folded] Every defect folded, 2026-10-19

All 25 are folded: v2's rows and principles, the memory plan's `[frame]`, deploy row, `[practice]` and `[doors]`, the
systems record's unit and change record, the fates record's `gotchas.py` row, the gap register's ownership rule, and
the adopter record's items 1 and 8, its `[chain]` and a `[reviewed]` section. Nine bug classes carry the instances,
and `[owed]` regains the restructure map. dSafePassage gains one planned unit, the receipt's `steps`, and
dShippedRelease one, gov's update of itself every release.

The reconciliation probe reddened once on the fold, on two clauses. dOrderedCharter first admitted
`editorial` on a review breakpoint's ruling, a route into the breakpoint program that only later builds bring;
the ruling is now the owner's, carried by `instructions.edit`'s proof. The chain rows also cited the fold as "the
folds' closing review", one of the breakpoint program's declared names, so they now cite "the folds' review". A second run then reddened on the receipt's `commit` field, moved into
dSafePassage's row with the schema-4 bump, which reads as dDeclaredLoop's `commit` kind; the row now names the
field in plain words.
