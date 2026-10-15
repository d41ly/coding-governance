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

## [design] The review system for the rework

### [lenses] A design-audit preset, and no opt-in lenses yet

- **A third preset, design-audit,** for design and architecture records such as the layer records and
  v2. Its lenses:
  - coherence;
  - grounding, which also flags load-bearing claims that rest on a docs line or a single observation
    (assumptions);
  - reuse, held to prior decisions, owner rulings and open asks (precedent);
  - failure-envelope, extended to trust boundaries (security);
  - alternatives-and-cost, in place of blast-radius.
- **The unit-spec and diff presets keep their lenses,** since their escapes are recall misses inside a
  brief.
- **Portability, topology and adopter migration** become universal bug-class checklist entries. The
  review driver passes lens notes by default.
- **Opt-in lenses on every preset, as the owner settled (R-1, "Both").**
  - The catalogue is security, precedent, assumptions, alternatives, cost, portability, adopter
    migration and topology, each with the brief its research return gives.
  - An opt-in lens replaces a named default lens of its preset. Concatenating a sixth lens onto a preset
    is refused at the tool call, so a swap is the only shape the hook admits in one run.
  - `review.opt-in` chooses them: none, or a set of named lenses, each with the default it replaces.
    Every preset carries none, so a review opts in for its subject. Swapping out a default loses that
    lens's coverage for the run.
  - A second pass stays possible as a separate run. It would have to beat what a second round of the
    same preset bought on the runtime design: about 6.3 confirmed new defects per 100k output tokens.
  - dCalibratedLens draws its per-stage lenses from this catalogue, once Plan, Test, Deploy and Maintain
    have reviews to calibrate on. Today there are none.
- **Owed before the preset ships: a blind replay** on the runtime design's blob `767187aa`, in a worktree
  at `6cfd21619`.
  - Each of two runs must find at least 4 of the 6 known escapes, 7 of the 8 highs, and about 70% of
    the 59 known defects.
  - The replay costs about 24 agents and 430k output tokens.

### [adjudication] Five harness changes, each with its owed test

Each change lands in `tools/workflows/tier2-review.js`, in its code and its prompts:
- **Batches by address.**
  - Findings are sorted by the address they cite before they are sliced into skeptic batches, so batch
    sizes stay the same.
  - Same-address pairs that meet one skeptic rise from 8% to 59%. Verified twins batched together rise
    from 0 of 8 to 4 of 8.
  - The owed test replays the verify stage on the runtime findings. It loses if the uneven twins, three
    today, or the grade splits do not drop.
  - It touches 24 batch references in `tier2-review.test.sh`.
- **A grade per id.**
  - An item carries each of its findings' binding grades and ranks by the highest, so one defect makes
    one item.
  - The counts stay by binding grade, so aSightedSkeptic-6 §8 F2 stands.
  - The owed test is the tally arms with a mixed-grade item.
- **Twins shown to the synthesizer.**
  - It is handed the refuted rows' claims and the same-address pairs, with an instruction to flag a
    refuted twin of a confirmed finding. It can note a twin, never overturn a verdict.
  - The owed test replays synthesis on runtime rounds A and B, where A59 and A38, and B61 and B43, must
    be flagged.
- **Duplicates as merged confirmations.**
  - This is a metric fix that moves pooled precision by +0.013.
  - The orphan check is extended to the diff kind.
- **Class-level fix verdicts, and gates with a home.**
  - The skeptic judges whether a fix covers the class, not just the instance.
  - The synthesizer is handed the leg manifest and the class names. Each proposed gate names an
    existing leg, suite or bug class, or says it is new.
  - The owed test re-judges aRoutedQuill #23's fix with the class wording.

**Rejected, by measurement:**
- **Making a refutation by design quote its line:** 39 of 42 already do. The disagreement is over
  whether the line covers the case.
- **One grade applied to a whole item:** it would reverse aSightedSkeptic-6 §8 F2.
- **One batch per section:** batches would grow, up to 3.8 times.

**Undetermined: items named by tags.**
- Tags coined per run would differ between runs.
- A derived key would join them instead: the cited address, or a prior round's ref.
- dConvergedCharter already owns migrating positional references.

**One role-file line changes.** `gov-synthesizer.md` says it is handed only confirmed findings, but it
is also handed the unverified and refuted rows.

### [where] One build carries the harness changes

Settled by R-3: an early build of its own, **dFairHearing**, a child of dClosedLoop beside dOrderedCharter.
- Its first units are the owed replays. Every later chain build's audits then run on the changed
  harness.
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
