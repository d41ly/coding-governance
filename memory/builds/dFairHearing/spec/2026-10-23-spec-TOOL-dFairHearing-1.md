# TOOL-dFairHearing-1 — the owed replays: the design-audit preset run blind at blob 767187aa, and the verdicts that flip the dark switches

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0068@d09495d0 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-1-deviation-11.md](../build/2026-10-23-build-TOOL-dFairHearing-1-deviation-11.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-1-reuse-scout.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-1-reuse-scout.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-3-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-3-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-4-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-4-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-amend-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-amend-fix-brief.md) | research | TOOL-dFairHearing-17 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-repin-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-repin-brief.md) | research | TOOL-dFairHearing-17 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

Four harness changes of this build ship dark (S9): the design-audit preset (`TOOL-dFairHearing-2`),
skeptic batches by address (`TOOL-dFairHearing-4`), twins shown to the synthesis
(`TOOL-dFairHearing-7`) and fix verdicts judged by class (`TOOL-dFairHearing-8`). Each was argued
from data and none was tested. This unit runs the owed replays first: the design-audit preset run
blind at blob `767187aa`, from a bundle of the history to `6cfd21619` cloned outside the repository,
scored by `review_replay.py` against a known-set file of every known defect, each with its address,
grade and escape flag, counting each matched defect once, at 45 of 59 known defects, 4 of 6 escapes
and 7 of 8 highs in each run. It replays the verify stage with batches by address, the synthesis with
twins shown, and aRoutedQuill #23's fix re-judged by class. A hit flips that switch's default; a miss
keeps today's, the unit-spec preset for design records included, and the verdict is recorded with
the replay's raw outputs.

## 2. Scope (IN)

- **S1** — The known-set file (S11), a record under `memory/builds/dFairHearing/build/` named
  `…-build-TOOL-dFairHearing-1-known-set.md`. It opens `**Serves:** research TOOL-dFairHearing-1`,
  states `**Population:** 65 · reviewed 59 · escaped 6 · high 8`, and holds one table row per known
  defect: `| tag | address | grade | escaped |`. `tag` is the defect's slug; `address` is
  `<record path>:[<section tag>]`, the form `extract_tag_ref` reads; `grade` is `high`, `medium` or
  `ungraded`; `escaped` is `yes` or `no`. Observed by AC1.
- **S2** — `parse_known_set(text)` in the factory's `review-replay` instance, and `review_replay.py
  --known-set <src> --candidate <src> [--matched <src>]`. The reader refuses a row count or a
  partition count that disagrees with the `**Population:**` line, a repeated `tag`, and an `address`
  `extract_tag_ref` cannot read. Its `case_evidence` is the row's address and the record it names.
  Observed by AC1 and AC2.
- **S3** — Adjudicated matches. `--matched` names a record holding `**Adjudicator:** <who>` and a
  table `| candidate | tag |`. Each pair's candidate must be a confirmed appendix row of the
  candidate report whose `ref` cites the known row's `[tag]` somewhere, and each tag counts once
  however many candidates name it. The scorer prints the address matches `extract_tag_ref` finds as
  `address-match` lines for the adjudicator, then, from the adjudicated pairs only, `reviewed <k>/59`,
  `escaped <k>/6` and `high <k>/8`. Observed by AC2 and AC3.
- **S4** — The calibration. Matched lists for the two baseline rounds, derived from the comparison
  record's `[map]` by a probe and committed beside it, reproduce that record's own figures, and a
  deliberately weak candidate is seen scored below the bar once. Observed by AC3.
- **S5** — Replay 1, the design-audit preset blind. The history to `6cfd21619` is bundled from a
  transient ref and cloned under `%TEMP%`, outside the repository. Two runs of `tier2-review.js` with
  `kind` `spec-audit` and `preset` `design-audit` audit the runtime record at blob `767187aa` there,
  with run B's arguments otherwise (§4). Each run is adjudicated and scored by S3; its bar is at
  least 45 of 59 reviewed, 4 of 6 escaped and 7 of 8 high. Observed by AC4 and AC5.
- **S6** — Replay 2, the verify stage with batches by address: runs A and B and the three other
  reports holding the 8 verified same-run twins, re-batched under `batchBy` `address` by the
  template's own batching code, with no agent. Its bar: A59 joins A38 in one batch, and at least 4 of
  the 8 twins meet one skeptic. Observed by AC6.
- **S7** — Replay 3, the synthesis with twins shown: one synthesis each over runs A and B under
  `addressTwins` `shown`. Its bar: A59 with A38 and B61 with B43 flagged, and the negative pair of
  §4 not flagged. Observed by AC7.
- **S8** — Replay 4, aRoutedQuill #23's fix re-judged by class: one skeptic under the fix-verdict
  switch `TOOL-dFairHearing-8` ships, over round 1's finding #23 and its fix `5b4f964d5`, and one
  over the control fix §8 F4 selects. Its bar: #23's fix judged instance-only, the control not
  flagged. Observed by AC8.
- **S9** — The verdicts. A replay meeting its bar flips its switch's default in
  `tools/workflows/tier2-review.template.js`, re-rendered into `tools/workflows/tier2-review.js`;
  for replay 1 the flip is `review.pin` passing `design-audit` when every pinned revision is a design
  record, in the mapping `TOOL-dFairHearing-3` owns. A replay missing its bar changes nothing, and a
  miss on replay 1 files an ask in this build's `BACKLOG.md` reopening R-1 with the replay's numbers.
  One verdict record lists each replay's figures, bar, verdict and raw outputs. Observed by AC9.

## 3. Non-goals (OUT)

- Building any of the four switches: each is its own unit's, default-off.
- The lens catalogue rows of the preset (`TOOL-dFairHearing-2`, `TOOL-dFairHearing-13`) and the
  opt-in swaps (`TOOL-dFairHearing-3`).
- Re-adjudicating the comparison record's `[map]`. The baseline's placement is the main loop's
  judgment of 2026-10-15 and is read, never revised.
- Editing the runtime record, the two baseline reports or any aScoutedSeam record.
- Scoring by an anchor or a word of the defect, as the whole-design audit's matcher does. The
  adjudicator reads each match; the scorer checks its address (§4).

### Edges

- **consumes-from** `TOOL-dFairHearing-12` — the factory, `extract_tag_ref` and the `review-replay` instance that S2 extends
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment`, whose parsed counts and manifest each replay run declares
- **consumes-from** `TOOL-dFairHearing-2` — the `design-audit` preset replay 1 runs
- **consumes-from** `TOOL-dFairHearing-4` — `batchBy` and `deriveAddressOrder`, which replay 2 runs
- **consumes-from** `TOOL-dFairHearing-7` — `addressTwins`, which replay 3 runs
- **consumes-from** `TOOL-dFairHearing-8` — the class-level fix verdict behind its switch, which replay 4 runs
- **consumes-from** `TOOL-dFairHearing-3` — `review.pin`'s record-kind mapping, whose default replay 1's verdict sets
- **hands-off** `TOOL-dFairHearing-15` — the bundle-and-clone procedure of §4, which its replays reuse
- **hands-off** `TOOL-dFairHearing-18` — the known-set row shape and `parse_known_set`, which its seeded key reuses

## 4. Design

### The known set

The 59 reviewed rows are the `[map]` rows of
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md:162-224`
that carry a confirmed finding: every row but `prose-ceilings` and `slug-shape`, which only refuted
findings name. A row's `address` is the first `[tag]` of the lowest-numbered confirmed finding
`[map]` places on it, run A's ids before run B's, read from the two reports' appendices. Its grade is
`high` for the eight defects `[numbers]` grades high (:90-98) and `medium` otherwise, since that
instrument grades only those two (:74).

The six escaped rows are the defects found after both rounds: the four the fold found (`[neither]`,
:226-245) and the two the floor probe found
(`2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md:107-109`). Each takes the section of
the record at blob `767187aa` holding the claim it corrects, and `grade` `ungraded`, since no review
graded it. They are rows beyond the 59, which is the deviation this spec records (§8 F1).

### The isolation

```bash
git update-ref refs/replay/fh-base 6cfd21619
git bundle create "$TEMP/fhb/h.bundle" refs/replay/fh-base
git update-ref -d refs/replay/fh-base
git clone --branch fh-base "$TEMP/fhb/h.bundle" "$TEMP/fh1"
```

The clone holds no object, ref or reflog after `6cfd21619`, and it sits under `%TEMP%` rather than
the session scratchpad, whose path is too long for a clone on Windows. The workflow runs with
`scriptPath` this repository's `tools/workflows/tier2-review.js` and `repo` the clone. The other
arguments are run B's, verbatim from the comparison record (:27-50): the subject at blob `767187aa`,
the seven sibling records as `specs`, run B's `context` with its run label replaced by "run 1" or
"run 2", the roles and efforts at medium, and the checklist `gotchas.py --for-paths` prints in the
clone over the subject. `scratch` is the session scratchpad, outside the clone. The added argument is
`preset: 'design-audit'`.

A run is void, and re-run rather than scored, when its manifest's parsed counts (S5 of
`TOOL-dFairHearing-14`) fall short, when its report names a dead finder or skeptic, or when a probe
over its agent transcripts finds a read of any absolute path outside the clone and the scratchpad.

### Scoring

`review_replay.py --known-set <known set> --candidate <report> --matched <list>` for each run. The
adjudicator, the build pass's main loop, writes each matched list after reading the run's confirmed
findings beside the known set, taking the `address-match` lines as candidates and confirming or
refusing each. The address check holds every pair to a cited `[tag]`, so an adjudicated pair cannot
cross sections the finding never cited; a defect found only under a tag its finding does not cite is
a miss. Matching by any cited tag, not only the first, is deliberate: the baseline's 46 and 45 were
placed by reading, and a first-tag-only scorer would hold the preset to a harsher measure than the
baseline it must match.

### The other three replays

- **Batches.** The eight verified same-run twins are the research's
  (`2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md:37-40`): six flagged by
  synthesizers in aGraftedHelix-1's closing review, aSightedSkeptic's and aPairedSlots', and A59 with
  A38 and B61 with B43. A probe evaluates the template's prelude as the kit's review suite does,
  feeds each report's appendix rows as findings with each report's own batch count, and reads which
  pairs share a batch. Deterministic: no agent.
- **Twins.** The synthesis prompt under `addressTwins: 'shown'` over each run's verified findings and
  refuted claims, one synthesizer each. The negative pair is the first same-address pair in id order
  whose two findings `[map]` places on different defects.
- **Fix verdict.** One skeptic per fix, handed round 1's finding and the fix's diff
  (`ff0b3dc3..5b4f964d5` for #23), under the switch `TOOL-dFairHearing-8` ships.

### Inventory

| Identifier | Kind | Lexicon verb |
|---|---|---|
| `parse_known_set` | function, `replay_scorer.py` | parse |
| `read_matched_list` | function, `replay_scorer.py` | read |
| `--known-set`, `--matched` | flags, `review_replay.py` | — |
| `refs/replay/fh-base` | transient ref, deleted after the bundle | — |

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/review_replay.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/README.md`
- `memory/builds/dFairHearing/build/`
- `memory/builds/dFairHearing/BACKLOG.md`, only on a replay 1 miss

`review.pin`'s mapping lives in the file `TOOL-dFairHearing-3`'s spec names; the build pass adds that
path to its `--dispatch --writes` set from that spec, and touches it only on a replay 1 hit.

### Rollout

The template's edits are default flips only, one per hit, each a constant `TOOL-dFairHearing-2`, -4,
-7 or -8 named; the render is `check-protocol-parity.test.sh --render`. The kit README's switch
paragraphs state the new defaults.

### Alternatives rejected

- **A worktree at `6cfd21619`.** It shares refs and objects with the branch holding the reports, the
  debt round's `replay-blindness` finding
  (`2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md:220`).
- **Scoring by address alone.** A finding addressed `[supervise]` would match every defect in that
  section, and the record's own rule is that an adjudicator records the matched list
  (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:189`).

## 5. Production-readiness checklist

- security — the clone and the bundle sit outside the repository; the transient ref is deleted in the
  same step; the lenses keep the spec kind's read-only probe rules.
- perf / scale — replay 1 costs about 24 agents and 430k output tokens; replays 3 and 4 four agents.
- error / empty / loading states — a void run is re-run, never scored; every reader refuses a
  population it read in part.
- observability — the verdict record carries every figure beside its bar and its raw output.
- risks — an adjudicator biased toward the bar; S4's calibration reproduces the baseline's figures
  with the same scorer, and the matched lists are committed for anyone to re-read.
- testing — AC1 to AC9; the reader's arms join the factory's runner.
- migration — none for adopters; a default flip changes what an unflagged call does, named in the
  README.
- user docs — the kit README; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When a probe runs `parse_known_set` over the committed known set, it returns 65 rows,
  59 with `escaped` `no`, 6 with `yes`, 8 graded `high` among the reviewed; and a scratch copy with one
  row cut, or one `tag` repeated, is refused naming the count or the tag.
  Red when: the reader returns 64 rows at exit 0.
- **AC2** — When `python tools/workflows/review_replay.py --known-set <known set> --candidate <run A
  report> --matched <scratch list>` reads a pair whose candidate `ref` cites no `[tag]` of its known
  row, it exits 2 naming the pair; and a list naming one tag twice scores that tag once.
  Red when: a cross-section pair is counted, or a doubly matched defect counts two.
- **AC3** — When the baseline matched lists score runs A and B, they print `reviewed 46/59` and
  `reviewed 45/59`, `escaped 0/6` for both, and `high 6/8` and `high 8/8`; and a list keeping every
  other pair of run A's prints a reviewed count under 45.
  Red when: the scorer or the known set disagrees with the record's `[numbers]`.
  figure: PINNED, the comparison record's instrument output of 2026-10-15 (:77-111).
- **AC4** — When the bundle is cloned, `git -C <clone> rev-list --all` names no commit absent from
  `git rev-list 6cfd21619`, `git -C <clone> rev-parse 6cfd21619:<record>`, `<record>` being the
  dClosedLoop build folder's `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, prints
  `767187aa4073f6e64cb2b2ef6b798f0a538347fd`, and `git show-ref refs/replay/fh-base` in this
  repository finds nothing.
  Red when: the clone reaches a later object, or the transient ref is left behind.
  fixture: the clone under `%TEMP%/fh1`, made by the pass.
- **AC5** — When each of the two design-audit runs is scored, its verdict record line prints its
  three counts against `45/59`, `4/6` and `7/8`, its manifest's parsed counts equal its dispatched
  counts, and the transcript probe names no read outside the clone and the scratchpad.
  Red when: a run with a dead agent or an outside read is scored instead of re-run.
  cost: about 24 agents and 430k output tokens for the two runs.
- **AC6** — When the batching probe runs under `batchBy` `address`, it prints which of the 8 twins
  share a batch, and the record states A59 and A38 together and the count against 4; under `batchBy`
  `id` the same probe prints 0 of 8, as the research measured.
  Red when: the probe slices by id under both values, so both print 0.
- **AC7** — When the two syntheses return under `addressTwins` `shown`, the verdict record lists the
  pairs each flagged, A59 with A38 and B61 with B43 among them, and the negative pair absent.
  Red when: a flag is read from the synthesizer's prose instead of its returned fields.
  cost: two agents.
- **AC8** — When the two skeptics return, the verdict record shows #23's fix, `ff0b3dc3..5b4f964d5`,
  judged instance-only and the control's not flagged, each with the skeptic's returned `fixVerdict`
  quoted.
  Red when: the control is flagged too, which reads as a skeptic that flags every fix.
  cost: two agents.
- **AC9** — When the verdict record lands, each of the four replays names its figures, its bar and
  hit or miss; `git diff` of `tools/workflows/tier2-review.template.js` over the pass changes exactly
  the defaults of the hits; and on a replay 1 miss `memory/builds/dFairHearing/BACKLOG.md` gains one
  ask naming R-1 and the two runs' counts.
  Red when: a miss flips a default, or a hit leaves it.

## 7. Gates

`review-replay selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC1 AC2 · a known set with one row cut and one tag repeated, and a matched pair crossing sections · none

The record writes under `memory/builds/` owe the two recall-floor legs by the guard join.

## 8. Open questions

- **FACT-QUESTION · F1 — Are the 6 escapes among the 59 known defects?** Probe: the comparison
  record's `[numbers]` (:80-81, 59 confirmed defects) and `[map]`, against `[neither]` (:226-245)
  and the lens research's escapes (:102-109). Observation: no escape is a `[map]` row; an escape is,
  by the records' definition, found after both rounds. Liveness: a `[map]` row naming an escape's
  defect would have answered yes. RESOLVED (agent, 2026-10-23, delegated): no. The clause's "all 59
  known defects, each with … escape flag" cannot flag an escape among 59 rows that hold none, so the
  file holds 65 rows and the bar reads 45 of the 59 reviewed and 4 of the 6 escaped. A departure from
  the clause's wording, recorded as
  `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-1-deviation-11.md`. Rung 2.
  widens: none · relaxes: none
- **F2 — How is a finding matched to a known defect?** (a) Adjudicated pairs, each checked to cite
  the row's `[tag]`. (b) The first-tag address alone. (c) Address plus an anchor and a word, the
  whole-design audit's matcher. (b) matches a section's every defect to one finding, failing "counting
  each matched defect once" in substance (veto 1); (c) holds the preset to a measure the baseline was
  never held to, so AC3 cannot calibrate it. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — Who adjudicates?** (a) The build pass's main loop, named in each matched list. (b) A
  spawned skeptic per run. Both survive; (b) adds an agent whose own recall is unmeasured, and the
  record names "a named adjudicator" without a role (review system :189). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Which fix is replay 4's control?** The record asks for "a control fix that does cover its
  class" (review system :245-246) and names none. (a) A selection rule fixed now: the first round-1
  confirmed finding, in `review_replay.py --corpus memory/builds` order, whose fix commit the next
  round of the same build reviewed with no confirmed finding sharing its `classes` cell, the pass
  recording the pick with both records. (b) A hand-written synthetic fix. (b) is not a fix any build
  shipped, so a skeptic flagging it says nothing about real fixes. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — Where does replay 1's flip land?** The preset is chosen per call by `review.pin`
  (`cl-dClosedLoop-0070`), not by a harness default. (a) The flip is `review.pin`'s mapping passing
  `design-audit` for design records. (b) A harness default of `design-audit` for every spec audit,
  which unit specs then also get, against the clause's "for design records" (veto 1). Recommendation
  (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §8 F1 · the `**Carries:**` pin moves from `b4e6c04e` to `d09495d0`, following
  the `amends cl-dClosedLoop-0068@b4e6c04e` row of this spec's own deviation record,
  `2026-10-23-build-TOOL-dFairHearing-1-deviation-11`; nothing else changed.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "known defect set scored for recall by address grade
and escape flag"` ranked `score` (`tools/memory-recall/bench.py`) and `build_grader`
(`tools/memory-tree/backlog.py`), neither a recall scorer over review findings. The seam is
`tools/workflows/review_replay.py`'s spec mode, extended by `TOOL-dFairHearing-12` into the factory
`tools/workflows/replay_scorer.py` with `extract_tag_ref`; this unit adds the known-set reader and the
matched list to its `review-replay` instance. The baseline's figures come from the comparison
record's own instrument (`…-runtime-reviews-compared.md:250-402`), read, not rerun. The recall query
returned the lens research's C3 losing test and the review system record's replay design, both of
which this spec follows, and the as-built view, whose wording of the clause equals the packet's.

Recall terms used: `python tools/memory-recall/query.py "the blind replay of the runtime design known
defects escapes highs bar" --terms "blind replay 767187aa 6cfd21619 bundle known-set escapes highs
design-audit preset runtime-a runtime-b recall"`
