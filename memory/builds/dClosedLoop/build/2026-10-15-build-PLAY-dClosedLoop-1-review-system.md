# Review system: lenses, skeptics and synthesis

**Serves:** research PLAY-dClosedLoop-1

While the reviews of layers 1 to 4 ran, the owner asked two questions:
- does gov's rework need opt-in review lenses?
- do the skeptics' and the synthesizer's instructions need changing?

Two researchers measured gov's review history to answer them, as dispatches 37 and 38. Their returns
and instruments are saved beside this record. This record turns them into a design and the owner's
forks.

The eight layer rounds run on today's harness. They are the baseline that these changes are measured
against.

## [words] The owner's words, 2026-10-15

> Before proceeding to the Knowledge layer, lets run 2x tier2 reviews on layers 1-4 to find gaps, same
> as Runtime. In addition, reviews run by preset scenarios currently. Do we need any additional
> (optional) lenses that will also become part of the Gov rework (additional opt-in review lenses), do
> we need any instruction changes to the skeptics and the adjudicator (synthesyzer) to improve their
> results?

## [research] Dispatched and returned, 2026-10-15

| # | Part | Return | Wall | Out |
|---|---|---|---|---|
| 37 | which lenses gov should carry | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md` | 17m01s | 55.5k |
| 38 | the skeptic's and the synthesizer's instructions | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | 18m51s | 96.0k |

Each return's instruments are kept in its `-instruments.md` record.

**Coverage.** Every measure of lenses and verdicts covers the 50 reports that carry a parseable
appendix: 13 spec audits and 37 diff reviews, 1,122 findings in all, every one from October. The other
448 reports attribute no finding to a lens.

## [current] What review is today, measured

**The lens sets** (`tools/workflows/tier2-review.js`):

| Preset | Lenses |
|---|---|
| spec-audit | coherence, grounding, reuse, blast-radius, failure-envelope |
| diff-review | security, correctness, seams, verification, intent |
| light diff-review | correctness, seams, verification |

- A run's kind is one of a closed set of two, and the kind fixes the preset.
- `lensNotes` adds a note to a lens, never a new lens. Callers passed it in 2 of about 49 reports.
- **The five-lens limit applies per array literal** (aNumeralWarden-1 F2, owner, 2026-08-10). The
  agent-cap hook:
  - refuses a preset array concatenated with opt-in lenses;
  - refuses a larger catalogue filtered down to five;
  - admits a lens swapped into a five-element literal;
  - admits a second pass run as a separate review.

**Yield.**
- **Diff lenses, over 37 reports:**
  - precision runs from 0.75 for security to 0.91 for intent;
  - security has the highest share of high and blocker findings, 0.22.
- **Spec lenses, on the runtime design's two rounds:**
  - precision runs from 0.82 for blast-radius to 1.00 for grounding and reuse;
  - blast-radius found the fewest defects that no other lens found: 4, all medium or low.

**Escapes.**
- **Inside the presets.** 89 of the 116 bug-class records that are not invariants sit inside a brief
  some preset already runs. Those are recall misses, not missing lenses.
- **Outside every brief.** 27 sit outside every brief: portability 9, topology 7, adopter migration 5,
  cost 4, assumptions 2.
- **The runtime design's post-review defects** all fell outside the spec preset:
  - the act with no ceiling: cost;
  - the fresh worktree that starts dirty: portability;
  - the kit confs beside the policy file: adopter migration;
  - the cheaper spawn backend: alternatives;
  - the version floor taken from a docs line: assumptions;
  - the allow rule that bypasses the dispatcher: security.

**Skeptics.**
- **Refutations.** 150 in all. 42 were refuted by design. Of those, 40 cite a spec, design or owner
  source, and 39 already quote a line.
- **Twins.** 9 refutations by design sit beside a confirmed finding on the same defect, verified.
  Every one of the nine is in a different skeptic batch from its twin.
- **Why twins split.**
  - Ids are assigned lens by lens, and batches are contiguous slices of the ids.
  - So only 8% of pairs where two lenses cite one address meet one skeptic.
- **Duplicates.** 15 were counted as refuted. That puts pooled precision at 0.866, against 0.880 with
  duplicates counted as merged.
- **Regrades.** 15.3% of confirmed findings were regraded. 37% of the findings a finder graded high
  ended up bound below high.
- **Unsound fixes.** 15.5% of confirmed findings carried one, and the skeptic's correction was carried
  forward each time.
- **The uncertain verdict** has never fired.

**Synthesis.**
- **"Merge findings of one binding grade only" binds completely.**
  - Same-address pairs with different grades were merged 0 times in 110.
  - Pairs with the same grade were merged 76% of the time.
  - Synthesizers wrote 29 statements naming the split themselves.
- **Naming.** No report names its items by tag.
- **Gates.** Of 721 proposed gates:
  - 17% name an existing leg or suite;
  - 2% name a bug class;
  - 24% name a generic checklist entry;
  - 56% name no home at all.
- **Re-finds.** 2 of the 5 round-2 reports with an appendix re-found a defect that round 1's fold
  should have closed. In both cases the fix had covered the instance, not the class.
- **Revised: 2026-10-17, the debt round.** Two readings above are refined:
  - "outside every brief" holds for the diff briefs. The spec briefs of reuse and grounding already
    carry precedent and assumptions;
  - callers passed `lensNotes` in 2 of the 50 reports with an appendix.

## [design] The review system for the rework

Revised: 2026-10-17, the debt round's fold. Its subsections are amended in place, and `[debt-fold]` names
where each defect's fix sits.

### [lenses] A design-audit preset, and opt-in lenses by swap

- **A design-audit preset of the spec-audit kind** (RV-1), for design and architecture records such as
  the layer records and v2. Its lenses:
  - coherence;
  - grounding, whose spec brief gains load-bearing claims that rest on a docs line or a single
    observation (assumptions);
  - reuse, whose spec brief gains prior decisions, owner rulings and open asks (precedent);
  - failure-envelope, extended to trust boundaries (security);
  - alternatives-and-cost, in place of blast-radius.
- **How it is selected.** The run's kind stays `spec-audit`, so its records bind `**Serves:** spec-audit`,
  agent-cap RULE 0's owner opt-in admits it as it admits any spec audit, and every reader keyed on the two
  kinds stays as it is. A `preset` argument picks the lens literal: `unit-spec` or `design-audit`. The
  harness chooses among its three literals with the marked ternary the hook admits. Design's breakpoint's
  `review.pin` passes `design-audit` when every pinned spec revision is a design or architecture record,
  which the record-kind registry tells apart from a unit spec. A manual call may pass it for any spec audit. An
  `agent-cap.test.sh` arm sends a design-audit call against a README with no `spec-audit:` date, and it
  is denied.
- **The unit-spec and diff presets keep their lenses,** since their escapes are recall misses inside a
  brief.
- **Portability, topology and adopter migration** become bug-class checklist entries anchored to the
  paths they concern, never universal. The universal budget stays at six, which gotchas.py's check 19
  holds.
- **Lens notes come from their callers.** The Audit stage's delegation in
  `unattended-build.template.js`, and the closing review's caller, pass `lensNotes`, declared in the
  review kit's conf. After a swap, the notes are derived from the run's lens set, keyed per preset. So a
  swapped-out lens's note never throws, and `LIGHT_LENSES` stays valid.
- **Opt-in lenses on every preset, as the owner settled (R-1, "Both").**
  - The catalogue is security, alternatives, cost, portability, adopter migration and topology, each
    with the brief its research return gives. Precedent and assumptions stay inside the reuse and
    grounding briefs, where `TOOL-aEvidencedLens-1` folded them, so they are not opt-ins. Portability is
    scoped to the diff kind.
  - **The admitted shape is a swap.** A run's lenses are a five-element literal, and each slot chooses its
    default brief or an opt-in brief. Concatenating a sixth lens, or filtering a larger set, is refused at
    the tool call, so a swap is the only shape the hook admits in one run.
  - **The channel.** The harness takes `optIn` and `preset` as arguments, supplied per review by its
    caller. `review.opt-in` holds the policy default, keyed by preset: none, or a set of named lenses, each
    with the default it replaces. Every preset carries none, so a review opts in for its subject.
    `review.pin`, the command item before the fan-out, reads the key and passes the arguments (Revised 2026-10-17, the folds' closing review:
    this line once named `review.lens`, which runs inside the act after the lens set is fixed). The witness is the lens keys in the
    report's lens-yield table, joined to the policy value. The running lens keys join the review key's
    input print, so a changed opt-in set never resumes an older run.
  - **One check at the argument boundary** refuses, by name: an unknown lens; a replaced default the
    preset lacks; an opt-in already among the preset's lenses or folded into one of them; and two swaps
    of one default. Swapping out a default loses that lens's coverage for the run.
  - **The extension point.** The flow's lens packs are what `review.opt-in` fills. The hook denies a map,
    an object or a registry of lens sets. So an expansion's lens enters the catalogue by an edit to the
    harness's literal catalogue, made in the expansion's own build. "Registers its lenses through its
    layer contract" means a declared catalogue entry plus that edit. Revised 2026-10-19 (the flow and roles
    adoption, FA-1, and the night pass two): the catalogue is data, a lens is a catalogue row whose brief is a
    unit, and the harness keeps a five-slot literal filled from it, so the merge bar's harness check counts slots,
    never names (agent-cap's count until the night pass two's point 7); an
    expansion's or a repository's lens is a row, never an edit to the harness.
  - **Each lens ships on its test.** Each catalogue lens's losing test, from the lens research's
    `[catalogue]`, is owed. On a blind replay, a swapped-in lens must raise more unique confirmed
    findings than the defects only the dropped lens found.
  - A second pass stays possible as a separate run. It would have to beat what a second round of the
    same preset bought on the runtime design: about 6.3 confirmed new defects per 100k output tokens.
  - dCalibratedLens draws its per-stage lenses from this catalogue, once Plan, Test, Deploy and Maintain
    have reviews to calibrate on. Today there are none.
- **Owed before the preset ships: a blind replay** of the runtime design's blob `767187aa`.
  - **Its isolation.** A bundle holds only the history up to `6cfd21619`, made with `git bundle create`
    from a ref at that commit. It is cloned outside the repository and its checkouts, so no later object,
    ref or reflog exists there. The replay runs on that clone, its probe rules drop the
    another-revision allowance, and a transcript that reads any path outside the clone, or any revision
    after `6cfd21619`, voids the run.
  - **Its bar.** Each of two runs must find at least 4 of the 6 known escapes, 7 of the 8 highs, and 45
    of the 59 known defects, which is the spec-audit preset's own lower run on that blob (76%). A defect
    counts as found only through a confirmed finding (layers-reviews-compared `[method]`).
  - **Its scorer.** `review_replay.py`'s spec mode is extended to `[tag]`-addressed sections. A known-set
    file holds all 59 known defects, each with its address, its grade and whether it escaped, from the
    runtime comparison record's `[map]`. A finding matches a known defect by the address key, and the
    scorer counts each matched defect once, however many findings match it; a planted known defect
    confirmed twice scores once. A named adjudicator records the matched list. A run with a dead finder or skeptic is re-run, not
    scored. A deliberately weak candidate is seen scored below the bar once.
  - **Its reject outcome.** If either run misses its bar, design records keep the unit-spec preset,
    dFairHearing ships only the harness changes, and an owner item reopens R-1 with the replay's
    numbers.
  - The replay costs about 24 agents and 430k output tokens.

### [adjudication] Four harness changes, each with its owed test

Each change lands in `tools/workflows/tier2-review.template.js`, in its code and its prompts, and
`tier2-review.js` is re-rendered from it. dFairHearing bumps the template's `version:` and
`REVIEW_SHAPE` once. The legs a change trips are the tier2-review selftest, the verifier fan-out
selftest, the review-protocol parity leg, and the roles render wiring and selftest. Each owed test states
how it loses, and a loss parks that change while the others ship.
- **Batches by address.**
  - Findings are sorted by one shared address key before they are sliced into skeptic batches, so
    batch sizes stay the same. The synthesizer's same-address pairs use the same key. For the diff kind
    it is the file and the line within ±3. For the spec kind it is the file plus the first `[tag]` or
    section token. An empty or multi-address `where` takes its first address, else the finding's lens,
    and ids break ties.
  - Batches are labelled `verify:batch-<n>`, with each batch's member ids in its resume file. The
    contiguous-id labels go, at the harness's four label sites, the template comment, README.md:430, and
    REVIEW-PROTOCOL's description of the resume file. `tier2-review.test.sh` carries 25 batch references.
  - Same-address pairs that meet one skeptic rose from 8% to 59% under the normalised key the research
    measured. The owed replay reports the same-batch rate under the key built.
  - **The twins arm.** A59 and A38 must join one batch, and B61 with B43 is a known miss. Of the 8
    verified twins that share a run, 4 must meet one skeptic. The ninth twin, B47 with A39, spans runs A
    and B. Cross-round twins are out of reach for batching, and fall to synthesis.
  - **Duplicates ride with batching** (R-2). A duplicate refutation counts as a merged confirmation. The
    diff skeptic's prompt gains case (5)'s `duplicate of id=<n>` reason form, and the orphan check drops
    its `isSpec` guard. Its owed arms: in a diff-kind run, a duplicate refutation pointing at a confirmed
    id in another batch is demoted to unverified, and the orphan check is seen red on a planted orphan.
    Recomputed over the 50 appendix reports, pooled precision moves from 0.866 to 0.880.
- **A grade per id.**
  - An item carries each of its findings' binding grades, and ranks by the highest, so one defect makes
    one item.
  - The counts are derived from the synthesis's items, as `TOOL-aSightedSkeptic-6` §8 F2 chose. Blockers
    and highs come from the per-id placements. The `regraded` warning and the re-grade clause stay, and
    `TOOL-dMergedTally-1`'s agreement rule is the constraint the tally test holds.
  - **Owed:** the tally arms with a mixed-grade item, as the unit check. A replay of synthesis on runtime
    rounds A and B must put the same-address, different-grade pairs the I7 instrument lists into one
    item, at a stated floor.
- **Twins shown to the synthesizer.**
  - It is handed the refuted rows' claims and the same-address pairs, with an instruction to flag a
    refuted twin of a confirmed finding. It can note a twin, never overturn a verdict.
  - **Owed:** a replay of synthesis on runtime rounds A and B, where A59 and A38, and B61 and B43, must
    be flagged. A negative pair, two defects at one address, must not be.
- **Class-level fix verdicts, and every confirmed finding homed.**
  - The skeptic judges whether a fix covers the class, not just the instance.
  - The synthesizer gives every confirmed finding one disposition from `review.report`'s grammar:
    `class:<slug>`, `new:<slug>`, `gate:<leg>`, or `none` under `review.unclassed`. A suite runs as a leg,
    so it is `gate:<leg>`. A new gate is `new:<slug>` with a patch-build intake. This closes
    `gap-review-07` and `gap-review-10`.
  - It is handed the leg manifest and the class slugs. The manifest path is a caller argument, as the
    checklist is, defaulting to `{prefix}/gate-legs.json`. With no manifest, the run announces it under
    RUN INTEGRITY and refuses `gate:` dispositions.
  - **Owed:** the skeptic re-judges aRoutedQuill #23's fix with the class wording, and must mark it
    instance-only. A control fix that does cover its class must not be flagged. A synthesis replay
    resolves every gate to a leg in `tools/gate-legs.json` or a class under `memory/gotchas/`, and a
    planted unknown leg reds. A synthesis output holding a confirmed finding with no disposition is
    refused.

**Rejected, by measurement:**
- **Making a refutation by design quote its line:** 39 of 42 already do. The disagreement is over
  whether the line covers the case.
- **One grade applied to a whole item:** it would reverse `TOOL-aSightedSkeptic-6` §8 F2.
- **One batch per section:** batches would grow, up to 3.8 times.

**Undetermined: items named by tags.**
- Tags coined per run would differ between runs.
- A derived key would join them instead: the cited address, or a prior round's ref.
- dConvergedCharter already owns migrating positional references.

**One role-file line changes.** The synthesizer's role, `tools/roles/agents/gov-synthesizer.agent.md`
lines 15-16 and 24, says it is handed only confirmed findings. It is also handed the unverified and
refuted rows. `.claude/agents/gov-synthesizer.md` is re-rendered from it.

### [where] One build carries the harness changes

Settled by R-3: an early build of its own, **dFairHearing**, a child of dClosedLoop beside dOrderedCharter.
- Its first units are the owed replays.
- Audits that start after dFairHearing lands run on the changed harness, and each chain build's audit
  records the harness version it ran on. dFairHearing becomes a parent of dDeclaredLoop, and so of every
  chain build that runs a design audit.
- dCalibratedLens keeps review by policy, per-stage lenses drawn from dFairHearing's catalogue, and the
  Loop Review. It gains dFairHearing as a parent.

## [stale] Records the research found disagreeing with the code

- **`memory/guides/REVIEW-PROTOCOL.md`:**
  - line 192 lists lenses that were retired;
  - line 199 allows "3-6" lenses, where the hook allows five per array;
  - it calls skeptics "default-refute", but the default depends on the finder's grade.
- **`tools/hooks/agent-cap.js`:** the comment at line 495 says tier2-review has four lenses. Both kinds
  have five.
- **`gap-review-03`** says a spec audit costs about 9 agents. Today's runs use 11 or 12.
- **`gov-synthesizer.md`** lines 11-12 and line 20, as above.
- **Revised: 2026-10-17, the debt round.** The edit sites are the sources:
  `tools/workflows/REVIEW-PROTOCOL.template.md` lines 192 and 199, and
  `tools/roles/agents/gov-synthesizer.agent.md` lines 15-16 and 24, each live copy re-rendered. The
  `gap-review-03` bullet is resolved: the register took the measured count.
- **This build's question to dispatch 38** said run B's report split three defects across seven items.
  It was three defects across six:
  - `relaunch-replay` over H3 and M1;
  - `chain-overlap` over H4 and M15;
  - `catalogue-duplicates` over H5 and M2.

## [gaps-proposed] Gaps, registered 2026-10-15

The register is canonical. dFairHearing owns `gap-review-04` to `gap-review-09`, in this order, and
`gap-review-03` took the measured agent count:
1. HIGH. Design records are audited by a unit-spec preset.
   - The spec lenses aim at unit-spec sections.
   - Every defect found after the runtime design's two rounds fell outside them.
2. MED. One defect splits across items by grade. Same-address pairs with different grades were merged
   0 times in 110, and synthesizers named the split 29 times.
3. MED. Twins meet different skeptics.
   - Ids are assigned by lens, and batches are contiguous slices.
   - 9 refutations by design sit beside a confirmed twin, all in a different batch.
4. MED. Proposed gates have no home.
   - 56% of 721 name nothing, and 2% name a bug class.
   - 2 of 5 round-2 reports re-found a defect whose fix had covered the instance.
5. LOW. Duplicates count as refuted, which understates precision, and the orphan check runs on the
   spec kind only.
6. LOW. Review records contradict the code, as `[stale]` lists.

- **Revised: 2026-10-17, the debt round.** The register stays canonical. dFairHearing owns
  `gap-review-04` to `gap-review-10` since the library round. `gap-review-10`, left-shift with no witness,
  closes with `review.report`'s disposition join (`[adjudication]`).

## [forks] To put to the owner

- **R-1.** The lens design: the design-audit preset, opt-in lenses, both, or neither.
- **R-2.** Which of the five harness changes the rework carries.
- **R-3.** Where the harness changes land: early in the chain, or with dCalibratedLens.

## [answers] The owner's answers, 2026-10-15

- **R-1:** "Both". The design-audit preset ships, and opt-in lenses join every preset. Each opt-in
  replaces a named default lens, chosen by `review.opt-in`.
- **R-2:** all four changes: "Batches by address", "A grade per id", "Twins shown to synthesizer", and
  "Class fixes, homed gates". "Batches by address" carries the duplicate fix with it.
- **R-3:** "Early, a small build of its own". dFairHearing joins the chain as its fifteenth build, a child
  of dClosedLoop. It starts with the owed replays.
- **Revised: 2026-10-17, reconciling R-2.** The owner's four named changes cover all five that
  `[adjudication]` first listed. The duplicate fix rides with "Batches by address", as the owner ruled,
  and owns `gap-review-08`. `[adjudication]` now heads four changes, under their own names.

## [debt-fold] The debt round's review-system pair, folded 2026-10-17

Dispatches 63 and 64 audited this record at `40738693d`
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md` and `-b.md`). Each of their 38 map rows
(the debt comparison record's `[map-review-system]`) went here, and RV-1 settled its fork. Each row's
classes are its confirmed findings' own, from the two ledgers.

| Defect | A | B | Disposition | Where the fix sits | Its classes |
|---|---|---|---|---|---|
| `design-audit-selection` | 1, 13, 30 | 8, 12, 25 | fork, amend | `[lenses]`, how it is selected (RV-1) | — |
| `design-audit-readers` | 10, 13, 30, 32 | 1, 12, 30, 31, 40 | fork, amend | `[lenses]`, the kind stays `spec-audit` (RV-1) | `retirement-inventory-misses-readers-by-value` |
| `rendered-targets` | 3, 20, 33, 45 | 2, 14, 22, 33 | amend, owed | `[adjudication]`'s lead and role-file line; `[stale]`'s dated note; v2's dFairHearing row after review 72 | `two-answers-to-one-question` |
| `gate-home-grammar` | 8, 18, 23, 43 | 3, 23, 44 | amend | `[adjudication]`, every confirmed finding homed | `two-answers-to-one-question` |
| `gap-range-stale` | 12, 22, 38 | 4, 18, 28, 39 | amend | `[gaps-proposed]`'s dated note | — |
| `stale-gap-review-03` | 12, 22 | — | amend | `[stale]`'s dated note | — |
| `preset-two-names` | 12 | — | amend | `[lenses]`, the `unit-spec` and `design-audit` presets | — |
| `change-count` | 9, 31, 40 | 5 | amend | `[adjudication]`'s heading; `[answers]`' dated note | `amendment-leaves-its-other-half-standing` |
| `lenses-heading` | 40 | 27 | amend | `[lenses]`' heading | `amendment-leaves-its-other-half-standing` |
| `owed-tests-missing` | 9 | 6 | amend | `[adjudication]`, the owed arms of duplicates and homing | `fixture-passes-by-finding-nothing` |
| `twins-test-positive-only` | — | 6 | amend | `[adjudication]`, the twins' negative pair | `fixture-passes-by-finding-nothing` |
| `fix-verdict-test` | 11 | — | amend | `[adjudication]`, the class-level owed test | `fixture-passes-by-finding-nothing` |
| `grade-test-synthetic` | 46 | — | amend | `[adjudication]`, a grade per id's replay arm | `staged-break-substitutes-a-synthetic-value` |
| `batch-test-weak` | 17 | — | amend | `[adjudication]`, the twins arm | — |
| `opt-in-tests` | 6 | — | amend | `[lenses]`, each lens ships on its test | — |
| `replay-blindness` | 5, 44 | — | amend | `[lenses]`, the replay's isolation | — |
| `replay-threshold` | 4, 14, 44 | 11, 43 | amend | `[lenses]`, the replay's bar | — |
| `replay-scorer` | 24, 34 | 43 | amend | `[lenses]`, the replay's scorer | — |
| `replay-reject-route` | 15 | 17 | amend | `[lenses]`, the replay's reject outcome | `owner-item-without-its-reject-outcome` |
| `replay-rule0` | 21 | — | none: refuted, a unit admits its own replay as its spec writes, and the one-off opt-in already exists | — | — |
| `opt-in-extension` | 7, 19, 26, 37 | 9, 26, 35, 45 | amend, owed | `[lenses]`, the extension point; flow-steps' lens packs after review 72 | — |
| `opt-in-no-reader` | 27 | 24 | amend, owed | `[lenses]`, the channel; flow-steps' breakpoint list after review 72 | `policy-value-with-no-route` |
| `opt-in-preset-meaning` | — | 7, 24 | amend | `[lenses]`, the channel | `policy-value-with-no-route` |
| `opt-in-inputs` | 41 | 7, 41 | amend | `[lenses]`, one check at the argument boundary | — |
| `lensnotes-collision` | 35 | 34 | amend | `[lenses]`, lens notes come from their callers | — |
| `lens-duplicates-briefs` | 25 | 21 | amend | `[lenses]`, the catalogue; `[current]`'s dated note | — |
| `universal-budget` | — | 13, 32 | amend | `[lenses]`, anchored entries | — |
| `ordering-unenforced` | 2 | 10, 16 | amend, owed | `[where]`; v2's chain after review 72 | — |
| `opt-in-depends-on-later-build` | 1 | — | amend | `[lenses]`, the channel's per-run arguments | — |
| `batch-sort-key` | 42 | 15, 42 | amend | `[adjudication]`, the shared address key | — |
| `batch-contiguity` | 16 | 19, 36 | amend | `[adjudication]`, batch labels | — |
| `twins-input` | 29 | — | none: refuted, the synthesizer is not handed refuted rows' claims today, so the change does add one | — | — |
| `orphan-check-wrong-half` | 28 | — | amend | `[adjudication]`, duplicates ride with batching | — |
| `grade-per-id-f2` | — | 20 | amend | `[adjudication]`, a grade per id | — |
| `leg-manifest-dependency` | 36, 47 | — | amend | `[adjudication]`, the manifest path | — |
| `rate-denominator` | 39 | 38 | amend | `[adjudication]`, the twins arm; `[current]`'s dated note | `rate-quoted-without-its-denominator` |
| `review-driver-nonexistent` | — | 29 | amend | `[lenses]`, lens notes come from their callers | — |
| `restatement-gate` | — | 37 | none: refuted, the restatement leg refuses a bare digit at the bar, so nothing wrong ships | — | — |

- **Owed after review 72.** Four fixes sit in records reviews 71 and 72 read as specs. v2's chain makes
  dFairHearing a parent of dDeclaredLoop (`ordering-unenforced`), and v2's dFairHearing row names the
  template sources (`rendered-targets`). flow-steps' breakpoint policy list gains `review.opt-in`
  (`opt-in-no-reader`), and its lens-pack extension point says what `[lenses]` says (`opt-in-extension`).
  They land with the systems fold. Revised 2026-10-17: they landed once review 72 returned, in v2's chain rows,
  flow-steps and the register.
- **The fold is unreviewed text.** A closing review of the debt fold is owed.
