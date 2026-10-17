# The review debt's six pieces, each reviewed twice, compared

**Serves:** research PLAY-dClosedLoop-1

The state record's `[unreviewed]` named six pieces of the design that no review had read
(`build/2026-10-16-build-PLAY-dClosedLoop-1-state.md`). The owner asked for each to be reviewed twice at
medium effort. This record holds the twelve runs, and their comparison once they return. The args, and the
script that wrote them, are in `build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md`.

## [words] The owner's words, 2026-10-16

> fix everything that's stale, then review all 6 unreviewed pieces - medium effort, twice each.

## [runs] The twelve runs

| Dispatch | Piece | Kind | Subject | Round | Prior set | Reports |
|---|---|---|---|---|---|---|
| 61, 62 | the lexicon | spec audit, full | `lexicon.md` at `424d2a7de` | 1 | — | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md`, `-b.md` |
| 63, 64 | the review system | spec audit, full | `review-system.md` at `40738693d` | 1 | — | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md`, `-b.md` |
| 65, 66 | the runtime fold and its two settlements | diff review, light | `6cfd21619..3611a60e9` | 1 | none; the two audit reports ride as specs | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-a.md`, `-b.md` |
| 67, 68 | the layers round's follow-up fold | diff review, light | `cc4c83ad5..1bc4883fe` | 3 | round 2's 31 confirmed, from `wf_e26eda01-523` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md`, `-b.md` |
| 69, 70 | the library round's fold | diff review, light | `d4fc4bb51..0dd962724` | 2 | round 1's 25 confirmed, from `wf_9d4cc07b-2f2` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-library-followup-a.md`, `-b.md` |
| 71, 72 | the expansion round's follow-up fold | diff review, light | `67c79f7cc..5e139d377` | 3 | round 2's 24 confirmed, from `wf_c69ed990-543` | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md`, `-b.md` |

## [method] How they run

- **Medium effort.** Every stage, finder, skeptic and synthesis, runs at `medium`, as the owner asked, and
  as the layers' and the runtime layer's audits ran.
- **Kinds.** The two designs no review read get the spec audit the layers got: round 1, full, the record
  at its blob as the subject, and the same six questions. The four folds get the light diff review every
  fold review got. A fold that answers an earlier round is that chain's next round, handed that round's
  confirmed set from its workflow's own ledger.
- **At HEAD.** The worktree is past each fold, and later commits changed some of its text. So each fold
  review reports a defect only if HEAD still carries it, and cites HEAD's line.
- **Independent pairs.** Runs A and B share every field but the run label, the report path and a spec
  audit's scratch directory, which the instruments' `[pairs]` checks. Each run is told the other run's
  report is not evidence.
- **One at a time.** No more than five agents run at once, the review protocol's at-once bound, and one
  run already reaches five. So the twelve run in the table's order, each after the one before returns,
  as dispatches 57 and 58 did. The owner opened the systems round while dispatch 62 ran, so its two
  research waves run between dispatches 62 and 63.
- **The spec audits' opt-in.** This build's README carries `spec-audit:` under `authorized-by: prompt`,
  and agent-cap admits no audit on a key under that mode. So, as for dispatches 39 to 46, the README's line
  is set aside and `.unattended.conf` dates `SPEC_AUDIT_DEFAULT` around each spec audit's dispatch call,
  in the working tree only. Both are restored as soon as the call is admitted, and neither change is
  committed.
- **The comparison** follows the layers' method: each pair's findings are placed on shared defects, and
  what one run alone found is named.

## [map-lexicon] The lexicon's findings, placed

Run A is `wf_14950dae-859` and run B is `wf_b52591b3-8f4`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `ratified-readers` | retiring the `ratified` stamp names none of its readers: the drift signal v2 makes the lexicon's own leg pack, `adopt-lexicon.sh --check`, the kit's hole and the scaffold | 3, 30, 37, 41 | 2, 30, 38 | amend |
| `acquire-family` | the drift rule's verb families do not exist: the canon has no `acquire` family, and load, read and parse are three clusters | 25 | 14, 29 | fork |
| `drift-vs-classes` | a declared verb that breaks the one-verb rule is conforming by the class table and debt by `[drift]` | 1 | — | amend |
| `drift-object-undefined` | "one verb per family per object" defines neither the object nor the established verb when an object has two | 48 | 54 | amend |
| `drift-enforcement-site` | where "refuse new splits" is enforced, and how `lexicon.drift` combines with `lexicon.at-commit`, is unsaid | — | 9 | amend |
| `map-extraction-states` | the map reads only the working tree, yet the base comparison, the commit check and `--merge-losses` need other states | 35 | 40 | fork |
| `map-dependency-undeclared` | the lexicon comes to require the map, against the kit's self-containment gate and KN-1's independent components, with no `requires` and no absent state | 18, 28, 36, 40 | 5, 25, 28, 42, 52 | fork |
| `shim-uncovered` | no pack covers the `mktemp` shim, so 5 of 6 third-party names are covered and the pin cannot fall by 28 | 4, 17, 43 | 6, 16 | amend |
| `pin-absorb-dead` | the pin "only falls", yet `absorb` and `no-gate` stay allowed and velocity's `absorb` is unreachable | 2 | 12 | amend |
| `pin-rebaseline` | changes that widen or reclassify debt (the `init` row, frozen nouns, pack upgrades) have no re-baseline route | 47 | 49 | amend |
| `markers-pep698` | the marker rule misstates PEP 698 and would red correct overrides of in-repository bases | 16 | 1 | amend |
| `unresolved-base` | a site whose base cannot be resolved statically gets no class | 49 | 47 | amend |
| `declaration-home` | contract declarations sit inline in source as `gov:` markers, outside `instructions.edit`, so an agent can clear its own debt; the readers they cite do not exist | 19, 52 | 23, 35, 48 | fork |
| `suppression-path` | a site suppression names no writer or write path, and TOOL-dScaffoldedMirror-4 already designs one | 6 | 31 | amend |
| `bar-comparison-seam` | the bar's offender comparison runs only on a red leg under `GATE_ATTRIBUTE`, against the landing base, and never in remote CI | 12, 27 | 15 | amend |
| `commit-check-seam` | the commit check names no seam, host, budget or bypass handling | 29, 45 | 8, 33, 51 | amend |
| `commit-check-moves` | move-awareness is required at the bar but not at the commit check | 46 | 24 | amend |
| `replay-threshold` | the move-aware replay names a measurement with no threshold or consequence | 8 | 32 | amend |
| `stdlib-pack-platform` | the stdlib pack depends on the Python minor and the platform it is generated on, and nothing chooses either | 7, 15 | 17 | amend |
| `pack-selection-inputs` | pack selection says nothing of a kit with no pack, a version outside every range, no manifest, or several minors | 50 | 50 | amend |
| `pack-fixture` | the research's owed fixture across five frameworks is dropped | 5 | — | amend |
| `prototype-live-import` | "5 of 5, byte-identical" was measured with the live import the design forbids, on one resolved site | 42 | — | amend |
| `pack-row-validation` | what makes a host set namespaced, and how a custom pack's rows are validated, are unsaid | — | 55 | amend |
| `forced-by-name-route` | `lexicon.forced` catalogues `by-name`, which no item routes | 32 | 36 | amend |
| `suggest-forced-aware` | `--suggest` cannot be forced-aware before the enclosing class exists | 14 | — | amend |
| `no-pack-owner-route` | a host with no pack goes to the owner only, with no outcome for a decline or an absent owner | 13 | — | amend |
| `vocabulary-proposal-route` | a name that will not fit becomes a vocabulary proposal with no pending or rejected outcome | — | 22 | amend |
| `nouns-table` | the NOUNS table rebuilds the canon's clusters and its owner overlay | 26 | — | amend |
| `init-row-inventory` | removing the `init` row reds the map's `lexicon-verbs` inventory, and NOUNS has no inventory | — | 41 | amend |
| `leg-placement` | the lexicon's bar legs are placed in no leg pack | — | 4 | amend |
| `later-records` | later records changed this one with no revision note: gap-lex-08's leg pack and Runtime's hook pack | 9, 20, 51 | 27, 43, 56 | amend |
| `chain-order` | L-4 orders dMindYourWords after dTotalRecall alone, before the builds whose extension points it fills | — | 3 | owed |
| `chain-count` | the record's chain count is thirteen where v2 now has fifteen | 39 | 45 | amend |
| `l6-misstated` | L-6 declared `html` and `svg` dark; the refusal still stands for every other extension | 53 | 11 | amend |
| `settled-stale` | `[settled]` still gives dTotalRecall the lexicon's work and gap-mem-10, which L-4 moved | 10, 34 | 37 | amend |
| `drain-count` | "one real drain in 60 days" against 11 drains measured | 22 | — | amend |
| `readme-misread` | the README's "shrink-only" is the waiver registries', and the two-sided pin has more carriers than `[fixes]` names | 21 | 20, 39 | amend |
| `pytest-installed` | "pytest is not installed on this node" is false | 24 | 18 | amend |
| `doc-reads-stale` | the legs' `doc_reads` on `memory/builds/` go stale once records leave the population | — | 46 | amend |
| `three-pins` | the kit carries three pin seams, and the design names one | — | 34 | amend |
| `pins-plain-edit` | the pins and the cell arming still change by plain edit | 38 | — | amend |
| `gaps-cite-asks` | the new gaps cite none of the live asks that already state them | 31 | — | amend |
| `raise-misread` | "+24 of +30 in `301a36664`" misreads the commit | 23 | — | amend |
| `gap2-example` | gap 2's example list drops `get_queryset` | — | 13 | amend |
| `foreign-ask` | the out-of-scope class rests on aSurfacedLexicon's open ask, unabsorbed | — | 10, 44 | amend |
| `main-red-stale` | `[now]`'s red on main is gone since `ef9c3fbab` | — | 19 | amend |
| `fixture-undefined` | "fixture" in the out-of-scope class is undefined | 11 | — | amend |
| `tokenizers-thin` | the shell and JavaScript tokenizers cannot give the enclosing class and its bases | 44 | 26 | amend |
| `tag-check-point` | the vocabulary check on namespaced tag names, which dOrderedCharter builds, is filled by no lexicon unit | — | 7 | amend |
| `declaration-second-carrier` | a contract declaration as a hand-kept copy of the reader's constants | 33 | — | none: refuted, the example limits nothing and a stale arm guards the copy |
| `import-census` | no extractor collects imports | — | 21 | none: refuted, `lexicon.py`'s Python and JS extractors collect imports |
| `keys-absent` | the four new keys have no absent state | — | 53 | none: refuted, v2's `policy.on-missing-expansion` covers an absent component |
