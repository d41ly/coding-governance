# Research: the answers fold's closing review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked for the closing review of the answers fold "at medium effort twice" (2026-10-18). Two independent
runs, A and B, reviewed the same pinned diff. This record compares them defect by defect, as the layers' paired rounds
were compared (`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`), and plans the fold. No defect
contradicts an owner's answer, so none goes to the owner first.

## [runs] The two runs

- **Subject:** `fe3d09aba` over `a9b00addd`: the owner's answers to the away pass's thirty-five forks, folded, and
  the instruments record's retitle.
- **Harness:** `tools/workflows/tier2-review.js`, light: three `gov-diff-reviewer` lenses (correctness, seams,
  verification), five `gov-skeptic` batches and one `gov-synthesizer`, every role at the owner's medium.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 114 | `wf_663c6465-b15` | `reviews/2026-10-18-review-PLAY-dClosedLoop-1-answers-fold-a.md` |
  | B | 115 | `wf_7b253e00-228` | `reviews/2026-10-18-review-PLAY-dClosedLoop-1-answers-fold-b.md` |

- **The args:** `build_args_answers.py` wrote both. They differ only in the run label, the report path and the
  scratch path, checked equal otherwise before run B launched. The runs went one after the other, so no more than
  five agents ran at once.
- **The ledger:** the roles kit derived every agent and returned line. The session log holds them.

## [method] How the runs were compared

The runtime comparison's `[method]`, with the layers' additions, applies unchanged:
- every finding of both runs, confirmed or refuted, is placed on the defect it names, and a finding that names two
  defects lands on both;
- a run finds a defect when one of its findings on it was confirmed, and the defect takes the highest grade any
  confirmed finding on it got, the skeptic's where one was given;
- the tables are derived: `compare_rounds.py` reads the two reports, `[map]` and the session log.

## [map] Every finding, placed

| Defect | What | A | B | Fold |
|---|---|---|---|---|
| `auth-transient-route` | a transient-auth failure skips its credential, so a contended refresh on the last entry has no route | 1 | — | fold: two classes, each with a planted arm |
| `apikey-last-unstated` | v2 lets api-key sit anywhere in `runtime.act-auth`, and lets the list be empty | — | 4 | fold: a schema arm for each |
| `pep701-ban-early` | dSafePassage retires the PEP 701 ban before anything refuses a below-floor interpreter | 9 | 1 | fold: the resolver's refusal moves into dSafePassage |
| `floor-reliance-unenforced` | interpretation 5 lets later builds rely on a floor no launch enforces | 10 | 1 | fold: the same move, and the interpretation restated |
| `remote-ci-floor` | gov's own remote CI gets no interpreter at the floor | 13 | 8, 13 | fold: a dSafePassage clause, and gap-tool-21 split |
| `ap30-self-run` | "gov runs it on itself first" cites a self-run on a later build | 2 | 9 | fold: the same clause applies the step to gov's tree |
| `toml-drop-reason` | the reason for dropping the TOML 1.0 arm and the template fails on the floor step's down | 3 | 2, 10, 14 | fold: the down refuses a TOML file the restored floor cannot parse |
| `floor-file-count` | gap-tool-22's eight files are the research's edit count, not the tree's declarations | 11 | 6 | fold: restated by its query |
| `bash-census-js` | the AP-33 correction and gap-tool-20 omit the stop guard's bare `bash` | — | 3 | fold: the census covers JavaScript |
| `gov-session-unchecked` | no check can fail the `Gov-Session` rule | 5 | — | fold: two planted arms |
| `macos-trigger-widened` | [planned]'s macOS trigger adds an adopter's request the owner did not choose | 6 | 5 | fold: the owner's trigger |
| `planned-gaps-deferred` | [planned] defers gaps the register already holds | 7 | — | fold: the sentence narrowed |
| `separator-lost` | dDeclaredLoop's commit-node clause lost a separator | 8 | 12 | fold: restored |
| `eol-gap-evidence` | gap-maint-15's evidence is a below-floor interpreter, not the floor's end of life | 12 | — | fold: restated |
| `final-stale` | the instruments record's [final] reports the run before the record was written | 4, 14 | 15 | fold: the recorder re-runs to a fixed point |
| `atlas-decision-guard` | the atlas refuses no section wrongly read as a decision | 14 | 16 | fold: a refusal in instruments records, planted |
| `planned-view-unrendered` | the atlas maps [planned] to a view that renders none of it | — | 7 | fold: mapped to records, and a read guard, planted |
| `p37-floor-value` | P37 states the floor's value beside its one declaration | — | 11 | refuted |
| `policy-values-unrouted` | catalogue values no unit routes | 15 | 17 | refuted |

## [summary] The two runs side by side

```text
$ python compare_rounds.py answers-fold-a.md answers-fold-b.md answers-reviews-compared.md session-log.md wf_663c6465-b15 wf_7b253e00-228
== runs
A: raw 15, confirmed 11, refuted 4, precision 0.73, high findings 2, agents 10, out 112.1k (sum of returned lines)
B: raw 17, confirmed 12, refuted 5, precision 0.71, high findings 1, agents 10, out 131.5k (sum of returned lines)
== defects
map rows 19, confirmed defects 17, refuted-only 2
both 6, A only 5, B only 6
A alone covers 11 of 17 (65%)
B alone covers 12 of 17 (71%)
overlap (Jaccard) 0.35
Chapman estimate of the population: 21.3, so about 4 found by neither
A only: auth-transient-route, gov-session-unchecked, planned-gaps-deferred, eol-gap-evidence, atlas-decision-guard
B only: apikey-last-unstated, ap30-self-run, toml-drop-reason, floor-file-count, bash-census-js, planned-view-unrendered
== severity (a defect takes its highest confirmed grade per round)
high defects 3: auth-transient-route, pep701-ban-early, floor-reliance-unenforced
  auth-transient-route: A 3 B 0
  pep701-ban-early: A 3 B 3
  floor-reliance-unenforced: A 2 B 3
shared defects graded alike 4 of 6
== lenses behind the defects one round alone found
A: correctness 3, seams 1, verification 1
B: correctness 3, seams 3
== refuted findings and their twins
A2 (ap30-self-run): confirmed twin B9
A3 (toml-drop-reason): confirmed twin B10
A11 (floor-file-count): confirmed twin B6
A15 (policy-values-unrouted): confirmed twin none
B2 (toml-drop-reason): confirmed twin B10
B11 (p37-floor-value): confirmed twin none
B14 (toml-drop-reason): confirmed twin B10
B16 (atlas-decision-guard): confirmed twin A14
B17 (policy-values-unrouted): confirmed twin none
```

- **One run finds about two thirds of what two find.** Run A alone covers 11 of the 17 defects and run B 12, an
  overlap of 0.35, below the layers' 0.49. Chapman's estimate leaves about four defects beyond both runs.
- **A high defect slipped past one run.** `auth-transient-route`, the inverted credential rule, was found by run A
  alone. Run B would have let it reach dWellOiledMachine's spec.
- **Adjudication is again the noisier half.** Six of the nine refuted findings sit on a defect another finding
  confirmed: run A's skeptics refuted three that run B's confirmed, run B's refuted one that run A's confirmed, and two
  of run B's refutations sat beside its own confirmation.
- **Most defects are the fold's own text.** Seven of the seventeen say more than their source, and four lean on a later
  build. `[fold]` names the class each one is an instance of.

## [fold] The fold plan

| Defect | The fold | Left-shift |
|---|---|---|
| `auth-transient-route` | v2's catalogue row and dWellOiledMachine's preflight clause split the classes: an absent, expired or rejected credential moves to the next, and a transient failure relaunches on the same credential under its own cap, outside the act's resume attempts, before it moves on, each class seen on a planted node | `fold-text-is-unreviewed-surface`, an instance, and the planted arms |
| `apikey-last-unstated` | the Allowed cell and the clause require a non-empty list with api-key only last, each refusal seen red on a planted policy file | `rule-stated-with-no-check-that-fails`, an instance, and the schema arms |
| `pep701-ban-early` | the resolver's refusal below the floor, its preference for a direct executable and its install message move into dSafePassage's floor step, seen red on a planted below-floor interpreter, so the ban retires in the unit that replaces it, and `gap-tool-12` moves with them | `step-depends-on-a-later-build`, an instance |
| `floor-reliance-unenforced` | the same move, and interpretation 5 restated | the same |
| `remote-ci-floor` | a seventh dSafePassage clause sets up Python at the floor in every remote-CI job that runs it, pinned by full sha, with the floor's preflight as the bar's first step, and `gap-tool-21`'s remote-CI fact becomes `gap-tool-23`, owned by dSafePassage | the same |
| `ap30-self-run` | the same clause applies the floor step to gov's own tree in its landing, its witness recorded | the same |
| `toml-drop-reason` | the floor step's down refuses while a tracked TOML file fails to parse under the floor it restores, and the step is named the template a later raise copies | `fold-text-is-unreviewed-surface`, an instance |
| `floor-file-count` | `gap-tool-22` counts the five files that state the floor and the two that mention it, with the query | the same |
| `bash-census-js` | the census covers JavaScript, one site, the stop guard's, and `gap-tool-20`, the AP-33 correction and dWitnessedBar's resolver clause name every bare-bash launch site a query finds | the same |
| `gov-session-unchecked` | the plan's commits gate and dWellOiledMachine's commit-key leg refuse a `Gov-Session:` under `act-only` and a missing one under `session`, each seen red | `rule-stated-with-no-check-that-fails`, an instance |
| `macos-trigger-widened` | the trigger is the owner's: a node registers darwin | `fold-text-is-unreviewed-surface`, an instance |
| `planned-gaps-deferred` | `[planned]` and interpretation 7 say pwsh-launch's measured gaps joined under AP-33 | `two-answers-to-one-question`, an instance |
| `separator-lost` | restored | `fold-text-is-unreviewed-surface`, an instance |
| `eol-gap-evidence` | `gap-maint-15` measures the floor's end date | the same |
| `final-stale` | the recorder re-runs `[final]` over the record it writes until two passes agree, and refuses after four | the fixed point is the gate |
| `atlas-decision-guard` | the atlas refuses a decision-titled section in an instruments record | the refusal, planted as `instruments-decision` |
| `planned-view-unrendered` | `[planned]` maps to the records view, and a section mapped to any other view must be one the derivation reads | the read guard, planted as `view-unread` |

## [folded] Every defect folded, 2026-10-18

All seventeen are folded as `[fold]` plans, in one commit:
- **v2:** the catalogue's `runtime.act-auth` row; dSafePassage's floor clause and its seventh clause, with
  `gap-tool-12` and `gap-tool-23`; dWitnessedBar's portability and resolver clauses, less `gap-tool-12`;
  dWellOiledMachine's commit-queue and preflight clauses; dDeclaredLoop's commit-node clause; `[planned]`; and a
  revision note.
- **The memory plan:** the commits gate's two `Gov-Session:` arms.
- **The gap register:** `gap-tool-20`, `gap-tool-21`, `gap-tool-22` and `gap-maint-15` restated, `gap-tool-23` added,
  and the tally re-measured.
- **The away-pass record:** `[folded-answers]`' floor, credential, resolver and atlas lines, the AP-33 correction with
  the JavaScript census, interpretations 5 and 7, and a pointer here.
- **Four bug classes** carry the instances, and `gotchas.py --write` re-renders their index.
- **The atlas** maps `[planned]` to its records view and refuses both misreadings, and **the recorder** writes
  `[final]` to a fixed point. The instruments record's `[plants]` shows each new plant red.

The chain, recomputed:

```text
critical path: 196 units, dGroundRules > dSafePassage > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dSafePassage 15, dFairHearing 27, dOrderedCharter 46, dDeclaredLoop 69, dPlacedRequest 77, dKeptSession 96, dWitnessedBar 96, dBoundRoles 113, dTotalRecall 115, dRankedPlan 128, dFurnishedOrders 131, dLinkedLibrary 139, dIndexedDesign 151, dWellOiledMachine 152, dScopedBuild 163, dTendedCadence 168, dMindYourWords 169, dShippedRelease 177, dCalibratedLens 180, dConvergedCharter 196
```

dSafePassage's seventh unit lengthens the path by one.
