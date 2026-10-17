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

## [forks] Asked, 2026-10-17

Four pairs are compared so far. Their maps send four defects to the owner, since each one's repair changes a
settled answer or a standing decision. The last two pairs may add more.

| Fork | Defects | The question | Options, the recommendation first |
|---|---|---|---|
| LX-1 | `acquire-family` | L-3 settled "refuse new splits" as one verb per family per object. The canon has no families: load, read and parse are three clusters, and the "acquire" family was a researcher's probe set. What does the drift rule refuse? | families the owner declares above the canon's clusters, through `instructions.edit`, with `lexicon.drift` reporting until a family is declared; the canon's clusters as the families, so only a split inside one cluster is refused; report only, L-3's second option |
| LX-2 | `map-extraction-states`, `map-dependency-undeclared` | The lexicon was to classify the map's definitions. That makes it require the map, against KN-1's independent components and the standing decision TOOL-dClosedLexicon-12. The map also reads only the working tree, while the bar, the commit check and `--merge-losses` need the base, the index and both parents of a merge. Where does extraction live? | one extraction primitive in `tools/lib` that reads the working tree, the index or a revision, which both kits call, so neither requires the other; the lexicon requires the map, declared and superseding the decision, and the map learns to read revisions and the index; two extractors, as today |
| LX-3 | `declaration-home` | Contract declarations are to change only through `instructions.edit`, yet the design places them as `gov:` markers in product code, where any builder's commit edits them. Where do they live? | in a declarations table the instruction write path owns, with at most a pointer in the code that a check resolves; inline `gov:` markers, with a check that refuses a marker change carrying no owner instruction record; in `.lexicon.conf`, owner-edited, as today |
| RV-1 | `design-audit-selection`, `design-audit-readers` | The design-audit preset is chosen by the subject's kind, and nothing says whether that is a third kind. A third kind passes agent-cap RULE 0's owner opt-in unexamined and misses every reader that keys on the two kinds by value. How is the preset selected? | as a preset of the spec-audit kind, selected by the subject, so RULE 0 and every reader stay as they are; as a third kind, with RULE 0, the harness's kind set, the record-kind vocabulary and the replay scorer updated |

## [answers] Answered, 2026-10-17

Each answer is quoted verbatim.

| Fork | The owner's answer | What it settles |
|---|---|---|
| LX-1 | "mechanism that automatically declares families based on what kits were discovered in the adopting repo + owner-declared families" | the drift rule's verb families come from two sources. Each pack that the stack census selects for a kit it discovers in the repository declares that kit's families. The owner declares the rest through `instructions.edit`. `lexicon.drift` refuses a new split inside a declared family and reports one outside every family |
| LX-2 | "Shared primitive in tools/lib (Recommended)" | one extraction primitive in `tools/lib` reads the working tree, the index or a revision. The map and the lexicon each call it, so neither kit requires the other, and the standing decision TOOL-dClosedLexicon-12 stands |
| LX-3 | "Instruction-owned table (Recommended)" | contract declarations live in a table the instruction write path owns. The code carries at most a pointer, which a check resolves |
| RV-1 | "Preset of spec-audit (Recommended)" | design-audit is a preset of the spec-audit kind, selected by its subject. agent-cap RULE 0's owner opt-in and every reader keyed on the two kinds stay as they are |

## [map-lexicon] The lexicon's findings, placed

Run A is `wf_14950dae-859` and run B is `wf_b52591b3-8f4`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
`ratified-readers` | retiring the `ratified` stamp names none of its readers: the drift signal v2 makes the lexicon's own leg pack, `adopt-lexicon.sh --check`, the kit's hole and the scaffold | 3, 30, 37, 41 | 2, 30, 38 | amend; `lexicon` `[debt-fold]`
`acquire-family` | the drift rule's verb families do not exist: the canon has no `acquire` family, and load, read and parse are three clusters | 25 | 14, 29 | fork, amend; `lexicon` `[debt-fold]`
`drift-vs-classes` | a declared verb that breaks the one-verb rule is conforming by the class table and debt by `[drift]` | 1 | — | amend; `lexicon` `[debt-fold]`
`drift-object-undefined` | "one verb per family per object" defines neither the object nor the established verb when an object has two | 48 | 54 | amend; `lexicon` `[debt-fold]`
`drift-enforcement-site` | where "refuse new splits" is enforced, and how `lexicon.drift` combines with `lexicon.at-commit`, is unsaid | — | 9 | amend; `lexicon` `[debt-fold]`
`map-extraction-states` | the map reads only the working tree, yet the base comparison, the commit check and `--merge-losses` need other states | 35 | 40 | fork, amend; `lexicon` `[debt-fold]`
`map-dependency-undeclared` | the lexicon comes to require the map, against the kit's self-containment gate and KN-1's independent components, with no `requires` and no absent state | 18, 28, 36, 40 | 5, 25, 28, 42, 52 | fork, amend; `lexicon` `[debt-fold]`
`shim-uncovered` | no pack covers the `mktemp` shim, so 5 of 6 third-party names are covered and the pin cannot fall by 28 | 4, 17, 43 | 6, 16 | amend; `lexicon` `[debt-fold]`
`pin-absorb-dead` | the pin "only falls", yet `absorb` and `no-gate` stay allowed and velocity's `absorb` is unreachable | 2 | 12 | amend; `lexicon` `[debt-fold]`
`pin-rebaseline` | changes that widen or reclassify debt (the `init` row, frozen nouns, pack upgrades) have no re-baseline route | 47 | 49 | amend; `lexicon` `[debt-fold]`
`markers-pep698` | the marker rule misstates PEP 698 and would red correct overrides of in-repository bases | 16 | 1 | amend; `lexicon` `[debt-fold]`
`unresolved-base` | a site whose base cannot be resolved statically gets no class | 49 | 47 | amend; `lexicon` `[debt-fold]`
`declaration-home` | contract declarations sit inline in source as `gov:` markers, outside `instructions.edit`, so an agent can clear its own debt; the readers they cite do not exist | 19, 52 | 23, 35, 48 | fork, amend; `lexicon` `[debt-fold]`
`suppression-path` | a site suppression names no writer or write path, and TOOL-dScaffoldedMirror-4 already designs one | 6 | 31 | amend; `lexicon` `[debt-fold]`
`bar-comparison-seam` | the bar's offender comparison runs only on a red leg under `GATE_ATTRIBUTE`, against the landing base, and never in remote CI | 12, 27 | 15 | amend; `lexicon` `[debt-fold]`
`commit-check-seam` | the commit check names no seam, host, budget or bypass handling | 29, 45 | 8, 33, 51 | amend; `lexicon` `[debt-fold]`
`commit-check-moves` | move-awareness is required at the bar but not at the commit check | 46 | 24 | amend; `lexicon` `[debt-fold]`
`replay-threshold` | the move-aware replay names a measurement with no threshold or consequence | 8 | 32 | amend; `lexicon` `[debt-fold]`
`stdlib-pack-platform` | the stdlib pack depends on the Python minor and the platform it is generated on, and nothing chooses either | 7, 15 | 17 | amend; `lexicon` `[debt-fold]`
`pack-selection-inputs` | pack selection says nothing of a kit with no pack, a version outside every range, no manifest, or several minors | 50 | 50 | amend; `lexicon` `[debt-fold]`
`pack-fixture` | the research's owed fixture across five frameworks is dropped | 5 | — | amend; `lexicon` `[debt-fold]`
`prototype-live-import` | "5 of 5, byte-identical" was measured with the live import the design forbids, on one resolved site | 42 | — | amend; `lexicon` `[debt-fold]`
`pack-row-validation` | what makes a host set namespaced, and how a custom pack's rows are validated, are unsaid | — | 55 | amend; `lexicon` `[debt-fold]`
`forced-by-name-route` | `lexicon.forced` catalogues `by-name`, which no item routes | 32 | 36 | amend; `lexicon` `[debt-fold]`
`suggest-forced-aware` | `--suggest` cannot be forced-aware before the enclosing class exists | 14 | — | amend; `lexicon` `[debt-fold]`
`no-pack-owner-route` | a host with no pack goes to the owner only, with no outcome for a decline or an absent owner | 13 | — | amend; `lexicon` `[debt-fold]`
`vocabulary-proposal-route` | a name that will not fit becomes a vocabulary proposal with no pending or rejected outcome | — | 22 | amend; `lexicon` `[debt-fold]`
`nouns-table` | the NOUNS table rebuilds the canon's clusters and its owner overlay | 26 | — | amend; `lexicon` `[debt-fold]`
`init-row-inventory` | removing the `init` row reds the map's `lexicon-verbs` inventory, and NOUNS has no inventory | — | 41 | amend; `lexicon` `[debt-fold]`
`leg-placement` | the lexicon's bar legs are placed in no leg pack | — | 4 | amend; `lexicon` `[debt-fold]`
`later-records` | later records changed this one with no revision note: gap-lex-08's leg pack and Runtime's hook pack | 9, 20, 51 | 27, 43, 56 | amend; `lexicon` `[debt-fold]`
`chain-order` | L-4 orders dMindYourWords after dTotalRecall alone, before the builds whose extension points it fills | — | 3 | owed; `lexicon` `[debt-fold]`
`chain-count` | the record's chain count is thirteen where v2 now has fifteen | 39 | 45 | amend; `lexicon` `[debt-fold]`
`l6-misstated` | L-6 declared `html` and `svg` dark; the refusal still stands for every other extension | 53 | 11 | amend; `lexicon` `[debt-fold]`
`settled-stale` | `[settled]` still gives dTotalRecall the lexicon's work and gap-mem-10, which L-4 moved | 10, 34 | 37 | amend; `lexicon` `[debt-fold]`
`drain-count` | "one real drain in 60 days" against 11 drains measured | 22 | — | amend; `lexicon` `[debt-fold]`
`readme-misread` | the README's "shrink-only" is the waiver registries', and the two-sided pin has more carriers than `[fixes]` names | 21 | 20, 39 | amend; `lexicon` `[debt-fold]`
`pytest-installed` | "pytest is not installed on this node" is false | 24 | 18 | amend; `lexicon` `[debt-fold]`
`doc-reads-stale` | the legs' `doc_reads` on `memory/builds/` go stale once records leave the population | — | 46 | amend; `lexicon` `[debt-fold]`
`three-pins` | the kit carries three pin seams, and the design names one | — | 34 | amend; `lexicon` `[debt-fold]`
`pins-plain-edit` | the pins and the cell arming still change by plain edit | 38 | — | amend; `lexicon` `[debt-fold]`
`gaps-cite-asks` | the new gaps cite none of the live asks that already state them | 31 | — | amend; `lexicon` `[debt-fold]`
`raise-misread` | "+24 of +30 in `301a36664`" misreads the commit | 23 | — | amend, owed; `lexicon` `[debt-fold]`
`gap2-example` | gap 2's example list drops `get_queryset` | — | 13 | amend, owed; `lexicon` `[debt-fold]`
`foreign-ask` | the out-of-scope class rests on aSurfacedLexicon's open ask, unabsorbed | — | 10, 44 | amend; `lexicon` `[debt-fold]`
`main-red-stale` | `[now]`'s red on main is gone since `ef9c3fbab` | — | 19 | amend; `lexicon` `[debt-fold]`
`fixture-undefined` | "fixture" in the out-of-scope class is undefined | 11 | — | amend; `lexicon` `[debt-fold]`
`tokenizers-thin` | the shell and JavaScript tokenizers cannot give the enclosing class and its bases | 44 | 26 | amend; `lexicon` `[debt-fold]`
`tag-check-point` | the vocabulary check on namespaced tag names, which dOrderedCharter builds, is filled by no lexicon unit | — | 7 | amend, owed; `lexicon` `[debt-fold]`
| `declaration-second-carrier` | a contract declaration as a hand-kept copy of the reader's constants | 33 | — | none: refuted, the example limits nothing and a stale arm guards the copy |
| `import-census` | no extractor collects imports | — | 21 | none: refuted, `lexicon.py`'s Python and JS extractors collect imports |
| `keys-absent` | the four new keys have no absent state | — | 53 | none: refuted, v2's `policy.on-missing-expansion` covers an absent component |

## [map-review-system] The review system's findings, placed

Run A is `wf_84ae201a-775` and run B is `wf_dd2730e2-e29`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `design-audit-selection` | nothing says how a run or the flow selects the design-audit preset, or whether it is a third kind or a spec-audit preset, and no breakpoint can select it | 1, 13, 30 | 8, 12, 25 | fork |
| `design-audit-readers` | a third kind meets readers that key on the two kinds by value, and the record names none: agent-cap RULE 0's owner opt-in, the harness's kind set and its `isSpec` branches, the record-kind vocabulary, the replay scorer | 10, 13, 30, 32 | 1, 12, 30, 31, 40 | fork, with `design-audit-selection` |
| `rendered-targets` | the edits point at rendered copies, never their sources: `tier2-review.template.js`, `REVIEW-PROTOCOL.template.md` and `gov-synthesizer.agent.md` | 3, 20, 33, 45 | 2, 14, 22, 33 | amend |
| `gate-home-grammar` | the record's gate homes, "an existing leg, suite or bug class, or new", disagree with `review.report`'s settled dispositions, `class:`, `new:`, `gate:` and `none` | 8, 18, 23, 43 | 3, 23, 44 | amend |
| `gap-range-stale` | dFairHearing's range reads gap-review-04 to 09, where v2 and the register give it 04 to 10 since the library round | 12, 22, 38 | 4, 18, 28, 39 | amend |
| `stale-gap-review-03` | `[stale]` lists gap-review-03's agent count as disagreeing, though the register already took the measured count | 12, 22 | — | amend |
| `preset-two-names` | the current preset is `spec-audit` in `[current]` and "the unit-spec preset" in `[lenses]` | 12 | — | amend |
| `change-count` | five harness changes in the heading and R-2's fork, four in R-2's answer, which folds the duplicate fix into batching | 9, 31, 40 | 5 | amend |
| `lenses-heading` | `[lenses]`' heading still reads "no opt-in lenses yet" after R-1's "Both" | 40 | 27 | amend |
| `owed-tests-missing` | the duplicates change, its orphan check on the diff kind, and gates with a home have no owed test | 9 | 6 | amend |
| `twins-test-positive-only` | the twins test hands the synthesizer only positive pairs, so one that flags every pair passes | — | 6 | amend |
| `fix-verdict-test` | the class-level fix-verdict test has a one-instance fixture and no expected verdict | 11 | — | amend |
| `grade-test-synthetic` | the grade-per-id test uses a hand-built mixed-grade item, not the 110 real same-address pairs | 46 | — | amend |
| `batch-test-weak` | the batching test's twin arm can move one of three uneven twins, so it can hardly fail | 17 | — | amend |
| `opt-in-tests` | the opt-in lenses ship with none of the research's losing tests | 6 | — | amend |
| `replay-blindness` | nothing makes the blind replay blind: a worktree at `6cfd21619` shares refs and objects with the branch that holds the reports | 5, 44 | — | amend |
| `replay-threshold` | the replay's bar, "about 70%", is not a decidable threshold, sits below what the current preset scores, and has no rule for matching a finding | 4, 14, 44 | 11, 43 | amend |
| `replay-scorer` | the replay never names `review_replay.py`, which refuses `[tag]`-addressed findings, and the known escapes sit in no appendix | 24, 34 | 43 | amend |
| `replay-reject-route` | the owed replays route only a pass, and nothing says what happens when one loses | 15 | 17 | amend |
| `replay-rule0` | the replay's procedure omits agent-cap RULE 0 on that tree | 21 | — | none: refuted, a unit admits its own replay as its spec writes, and the one-off opt-in already exists |
| `opt-in-extension` | the opt-in catalogue is a closed list in the harness, tied to neither the flow's lens packs nor the roles layer's registration, so an expansion's lens needs a code edit | 7, 19, 26, 37 | 9, 26, 35, 45 | amend |
| `opt-in-no-reader` | no item in the flow's review program reads `review.opt-in` | 27 | 24 | amend |
| `opt-in-preset-meaning` | `review.opt-in` mixes policy presets with review presets and is not scoped by review kind | — | 7, 24 | amend |
| `opt-in-inputs` | `review.opt-in` covers only well-formed values: no validator, no malformed or contradictory value, and no change to the resume key | 41 | 7, 41 | amend |
| `lensnotes-collision` | the opt-in swap collides with the lens notes' key validation and the light-lens check | 35 | 34 | amend |
| `lens-duplicates-briefs` | opt-in lenses rebuild briefs the default lenses carry, reopening the retirement of prior-art and unstated-assumption | 25 | 21 | amend |
| `universal-budget` | three new universal classes take the count to 9 against `UNIVERSAL_BUDGET=6`, which gotchas.py's check 19 refuses | — | 13, 32 | amend |
| `ordering-unenforced` | nothing orders the chain builds' audits after dFairHearing: only dCalibratedLens names it as a parent | 2 | 10, 16 | amend |
| `opt-in-depends-on-later-build` | dFairHearing reads `review.opt-in`, whose policy file, schema and reader land later, in dDeclaredLoop | 1 | — | amend |
| `batch-sort-key` | "sorted by the address they cite" defines no key for a free-text, multi-section or empty address, and a literal sort does not reproduce the measured gains | 42 | 15, 42 | amend |
| `batch-contiguity` | an address sort breaks the contiguous ids that batch labels, resume files and a code comment assume, and the test file holds 25 references, not 24 | 16 | 19, 36 | amend |
| `twins-input` | the synthesizer gains no new input from the twins change | 29 | — | none: refuted, the synthesizer is not handed refuted rows' claims today, so the change does add one |
| `orphan-check-wrong-half` | extending the orphan check to the diff kind extends the parser, while the diff skeptic's prompt asks for a bare "duplicate" | 28 | — | amend |
| `grade-per-id-f2` | "the counts stay by binding grade, so F2 stands", where F2 chose counts derived from the synthesis's items | — | 20 | amend |
| `leg-manifest-dependency` | handing the synthesizer the leg manifest adds a dependency the kit does not declare, with no case for an install without it | 36, 47 | — | amend |
| `rate-denominator` | the twin gain is quoted over 8 beside a population of 9, and lens-note use over "about 49" beside 50 | 39 | 38 | amend |
| `review-driver-nonexistent` | "the review driver" passes lens notes, but no tool by that name exists, and the Audit stage passes none | — | 29 | amend |
| `restatement-gate` | restating the hook's lens count as a digit is what the restatement gate refuses | — | 37 | none: refuted, the restatement leg refuses a bare digit at the bar, so nothing wrong ships |

## [map-runtime-fold] The runtime fold's findings, placed

Run A is `wf_c8860577-b54` and run B is `wf_dea5d838-89e`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `binding-on-fail-open-entry` | act binding and the stale-epoch fence sit on the PreToolUse entry, which fails open below 2.1.295, while the PermissionRequest entry, the one path that fails closed, decides by the allowance alone; no fixture crashes PreToolUse beside a healthy PermissionRequest | 1, 13 | 3, 10, 17 | amend |
| `return-key-per-act` | a persisted return is keyed by the item and the act's task-sha, so the agents of one fan share a key and a relaunch cannot tell which returned | — | 1 | amend |
| `fencing-epoch` | fencing rests on an epoch no lease grammar carries, says nothing of how a dispatcher on another node learns it, and its fixture can pass without the refusal running | — | 2 | amend |
| `permission-request-unlisted` | `[enforce]`'s event list and the owner-pack table leave out PermissionRequest, the only allow path for gated tools after RT-2 | 2, 14 | 11, 18 | amend |
| `mid-run-crash-untested` | RT-2's answer says a permission host that crashes mid-run stays a losing test in `[tests]`, and `[tests]` holds no such case | 3, 11, 16 | 7, 15, 24 | amend |
| `onfailure-three-ways` | `onFailure` is written unconditionally by settings-merge, conditionally by unit 7, and omitted by the `binary` fixture, over one tracked settings file for every node | 10, 15 | 14, 19 | amend |
| `next-awaiting-answer` | `[terms]` has `next` report a hook item as awaiting its event, and the closed answer set has no such answer | 4 | 13 | amend |
| `next-answers-untested` | the `next` fixture checks terminal, stuck and invalid-input only, not blocked, stale-remote or act | 17 | — | amend |
| `seen-red-count` | the instrument's red evidence is two planted copies in `[method]` and three in the kept output | 7 | 9, 25 | amend |
| `open-policy-untested` | the `fail-closed` invariant's clauses for a journaled bypass and for `runtime.hook-failure: open` have no fixture arm | 20 | 21 | amend |
| `coverage-arm-design-text` | the `coverage` arm asks whether each `runtime.*` key has a reader in the design record, not in the built code | 18 | 22 | amend |
| `neither-additions-untested` | the fold's own additions, the reap past `runtime.act-ceiling` and the workspace line endings from the node registry, have no fixture | — | 22 | amend |
| `attended-no-allowance` | PermissionRequest decides by the act's allowance, and attended and unbound sessions have no act | 12 | — | amend |
| `dispatcher-start-two-ways` | a dispatcher that cannot start refuses every call at line 617, and hands an attended call to the person at lines 565-566 and in the fixture | — | 6 | amend |
| `allow-rule-bypass` | a gated call "runs only on the dispatcher's approval", yet an allow rule in local or user settings is only warned about, and the act session's launch does not restrict its setting sources | — | 5 | amend |
| `second-permission-hook` | nothing checks local or user settings for a second PermissionRequest hook beside the single dispatcher | — | 20 | amend |
| `attended-slot-release` | an attended session's PreToolUse entry reserves fan slots, and only an act session's exit or reap releases them | — | 12 | amend |
| `cadence-dedup-race` | the supervisor reads the cadence witness before it takes the lease and never re-reads it after | — | 4 | amend |
| `stop-witness-producer` | the Stop row names the act's outcome record as its witness, and nothing produces it | — | 16 | amend |
| `latency-fixture-no-red` | the `latency` fixture's p50 sets the budget it measures, so it names no red | — | 23 | amend |
| `fail-closed-arm-ungated` | the `fail-closed` arm's first tool call after a crashed SessionStart names no gated tool, and Read stays open below 2.1.295 | 5 | — | amend |
| `trap-untested` | git hooks trapping signals closes gap-deploy-07's class, says the record, and the only git arm sends SIGKILL, which no trap catches | 19 | — | amend |
| `capability-claimed` | the capability table claims PermissionRequest answers ask rules on every version, under a heading that claims nothing unmeasured, and only 2.1.292 and 2.1.295 were measured | 21 | — | amend |
| `rt1-two-ways` | RT-1 is restated as a fresh start at every boundary | 6 | — | none: refuted, the line answers the on-full check and the next bullet keeps `context.on-full` |
| `relaunch-cap-fixture` | the relaunch cap's fixture counts resume-tick's resetting counter | 8 | — | none: refuted, the design defines the cap per act and carries no reset rule over |
| `act-ceiling-registration` | `runtime.act-ceiling` is a second carrier of process-monitor's ceiling | 9 | — | none: refuted, the two keys carry different facts |
| `chain-count` | "the chain has fourteen builds" against v2's fifteen | 22 | 8 | amend: refuted only as outside the range, and HEAD still carries it |

## [map-fold-round3] The layers round's round-3 fold findings, placed

Run A is `wf_588892a6-fb7` and run B is `wf_fc0975c8-622`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `claim-unreachable-from-triage` | `entry.claim` lists triage's select among its needs, and no route reaches it from triage, whose records are written before any claim | 2 | 7 | amend |
| `publish-failed-no-arm` | `deploy.core` reads the verdict from the per-SHA log and routes green, red and REFUSED, and a failed publication prints none of the three there, while `refs/gov/bar-red` is not always published | 1, 7 | 2, 11, 17 | amend |
| `held-leg-no-release` | the held-flaky-leg ask's acceptance names a consecutive-green count nothing produces, and no item lifts the hold when it is met | 4, 11 | 12, 18 | amend |
| `flake-record-two-writers` | the runner and the `test.flakes` command are both named writers of the flake record | 13 | 5 | amend |
| `parser-indented-rows` | `role_matrix.py`'s widened arm 0 still drops an indented or pipe-less row, and its body-row count shrinks with it | 5, 15 | 1, 14, 16 | amend |
| `ask-claim-create-once` | the per-family ask claim ref is created once, so it serialises only a family's first ask | 3, 10 | — | amend |
| `ask-lock-narrowed` | the ask mint lock covers only `entry.place`'s asks, while the owner, a surfaced idea, an expansion and the supervisor also file outside a build | — | 9 | amend |
| `claim-no-idempotence-key` | `entry.claim` declares no key that lets a retry recognise its own claim | — | 8 | amend |
| `claim-prune-two-ways` | a slug's claim ref is never pruned in memory, and the runtime supervisor prunes terminal claim refs with no namespace limit | 9 | — | amend |
| `flakes-duplicate-ask` | under `quarantine`, `test.flakes` files the held-leg ask on every flake past the threshold, with no idempotence key | 12 | — | amend |
| `removal-pending-no-filer` | a `removal-pending` entry waits on a patch build that no item files | 14 | 13 | amend |
| `land-outcome-overlap` | `deploy.land`'s "landed ungated" and "nothing pushed" both hold on a no-op push, and its sources cannot tell them apart | 8 | 4 | amend |
| `gaps-registered-list` | "the gaps registered" lists two new gaps after the follow-up round, and v2, the register and the record's own L4 row name a third, gap-mem-14 | — | 6, 15 | amend |
| `start-guard-blocks-refused-rerun` | `deploy.core`'s start guard makes its own REFUSED re-run dead | 6 | 10 | none: refuted, the re-run is an explicit route that never passes back through the start guard |
| `gap-test-04-contract` | gap-test-04's row omits the re-run contract and probe the flow says it owes | 16 | — | none: refuted, the row carries the contract the design relies on, and the probe sits in the text that cites it |
| `gap-rows-no-check` | gap-deploy-02 and gap-deploy-09 state the defect with no check that can fail | 17 | — | none: refuted, the register's rows carry no check column by its own form |
| `replacement-route` | the route after `plan.dedupe` contradicts itself on a re-placement | — | 3 | none: refuted, a re-placement goes to `plan.triage-rule` and keeps its claim, as `[transitions]` says |

## [map-library-followup] The library round's fold findings, placed

Run A is `wf_579f3126-0b4` and run B is `wf_0beb4276-c5c`. The ids are each report's appendix ids. A
refuted finding sits on the defect its claim names, beside its confirmed twin where one exists.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `distill-class-no-producer` | `build.distill` reds on a fork with no class, yet no Design item's witness requires the class, and the red has no route | 1, 20 | 2, 12 | amend |
| `ratification-two-places` | under `author-owner-ratifies`, Build's breakpoints put the owner's ratification before `build.distill`, its Needs and Then put it after, and a rejected re-class has no writer | 10, 19 | 1, 11, 23 | amend |
| `owner-only-no-arm` | `owner-only`'s rule that only an owner-resolved fork may be major sits in Does, with no witness arm and no route | 2, 19 | 20 | amend |
| `distill-key-no-fork-field` | `build.distill`'s idempotence and its one-to-one witness are keyed by build and fork, and the row it writes has no fork field | 9, 17 | 8 | amend |
| `deploy-distill-no-route` | `deploy.distill` can now go red on a row missing at the landed SHA, and its only route is `deploy.recommend` | 7, 12, 20 | 6, 21 | amend |
| `distill-after-core` | `build.distill` runs after `build.core`, so the core checks, check 27 among them, never grade the rows it appends, and Build's exit is certified before its last commit | 3, 13 | — | amend |
| `layer-memory-stale-writer` | layer-memory `[decisions]` still has `deploy.distill` append the major decisions when the build lands | 4 | 5, 13 | amend |
| `typed-reuse-witness` | round 1's typed-witness finding stands: `build.unit-pass` is still proven by the builder's own reuse line, whose `none` arm cannot fail | 22 | 3, 22 | amend |
| `built-path-class-unchecked` | on built work nothing checks that an owed class record was written; a write set only allows the path | 18 | 19 | amend |
| `ask-form-not-catalogued` | the new acceptance, "accepted once the class record exists", is not among layer-memory `[asks]`' closed forms | 16 | 14 | amend |
| `plan-scope-tags` | Plan reads the research view and the decision log by scope tags that neither carries | 14 | 7, 15 | amend |
| `build-policy-list-missing` | `build.distill` routes by `run.on-owner-question`, which Build's policy list leaves out | 11 | 10 | amend |
| `research-kind-selector` | the research-return kind declares no selector, and its witness's planted red cannot fire, since no record in the tree carries the kind | 15 | 18 | amend |
| `reuse-token-population` | gap-design-05 sizes the token migration against the wrong predicate: the hygiene check admits the substring "no existing seam" | 8, 24 | — | amend |
| `fork-population-unobserved` | the witness reads only the forks Design recorded, so an empty set cannot show that no fork was resolved | 21 | — | amend |
| `ordering-dorderedcharter` | dOrderedCharter's widened dependency check can pass only after dTotalRecall lands, though dOrderedCharter comes first | 5 | — | amend |
| `new-slug-collision` | a `new:` slug passes if no record held it at the report's pinned SHA, so two concurrent reviews can mint one slug | 6 | — | amend |
| `research-population-count` | the "59 research returns" are selected by file name and include instrument records | 23 | — | amend |
| `owner-asks-two-meanings` | `owner-asks` means "no line is owed" in LB-2's offer and "a line for the features an owner ask names" in the fold | — | 4 | amend |
| `recall-imports-eight` | the planned move covers recall's two core-read functions, and check 27 imports eight names from the recall kit | — | 9 | amend |
| `fix-unit-write-set` | the fix unit's write set omits the dossier edit that claims the new class | — | 17 | amend |
| `gotcha-claim-wrong-dossier` | the idempotence class is claimed by a dossier of checkers | — | 16 | none: refuted, gotchas.py selects a class by its own anchors, not by a dossier's claims |
