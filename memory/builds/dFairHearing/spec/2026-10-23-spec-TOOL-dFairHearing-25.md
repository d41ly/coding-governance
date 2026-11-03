# TOOL-dFairHearing-25 — the owed replays run after the replay contract is corrected, and their verdicts set the dark switches

**Status:** INPROGRESS · rev-5 · 2026-11-03 · node d · Tier-2 · base 3708a705 · streams tooling · order 22 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-25-deviation-251.md](../build/2026-10-23-build-TOOL-dFairHearing-25-deviation-251.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 |
| [2026-11-03-build-TOOL-dFairHearing-25-1-builder-return.md](../build/2026-11-03-build-TOOL-dFairHearing-25-1-builder-return.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md) | research | TOOL-dFairHearing-26 TOOL-dFairHearing-27 |
| [2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md) | research | TOOL-dFairHearing-4 TOOL-dFairHearing-18 TOOL-dFairHearing-27 |
| [2026-11-02-prompt-TOOL-dFairHearing-25-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-25-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief.md) | research | TOOL-dFairHearing-10 TOOL-dFairHearing-22 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-1 TOOL-dFairHearing-21 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-23 TOOL-dFairHearing-26 |
| [2026-11-03-prompt-TOOL-dFairHearing-25-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-2-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-2-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md) | research | TOOL-dFairHearing-30 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-37 TOOL-dFairHearing-40 |
| [2026-11-03-prompt-TOOL-dFairHearing-25-pass-a-build-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-pass-a-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief.md) | research | TOOL-dFairHearing-30 TOOL-dFairHearing-35 |
| [2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md) | spec-audit | TOOL-dFairHearing-4 TOOL-dFairHearing-14 TOOL-dFairHearing-26 TOOL-dFairHearing-27 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted units, finding id 1 (item H1, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`), is
closed. Today `TOOL-dFairHearing-1` (order 15) and `TOOL-dFairHearing-15` (order 16) run their blind
replays before `TOOL-dFairHearing-23` (order 19) corrects the contract those replays run on: the
review-replay manifest's terms (its S4), the bundle-and-fetch recipe (S17, S18), the spec-audit
placement (S22) and replay 1's flip site (S40). Spec 1's own clone step, `git clone --branch fh-base`
on a bundle holding only `refs/replay/fh-base`, is the step spec 23 AC10 names as exiting 128. This
unit, ordered after unit 23 and after `TOOL-dFairHearing-27`, which corrects unit 23's recipe, runs
replay 1's two design-audit runs and unit 15's eight with-and-without runs on the corrected
contract, and the switch state at its commit is what those verdicts say. Every correction a later
unit had written to the procedure these runs follow is carried here, before them (§8 F2).

## 2. Scope (IN)

- **S1** — Replay 1, run once on the corrected contract: the two design-audit runs of
  `TOOL-dFairHearing-1` S5, with the arguments its §4 "The isolation" names. Each run takes its own
  clone, made by the replay section of `tools/workflows/README.md` (unit 23 S17, unit 27 S22's
  envelope, and S8's placement step) under a fresh name per attempt (S10). A clone directory that
  already exists is refused, never reused, and the clone's `HEAD` must equal the commit the recipe was
  given. Observed by AC1.
- **S2** — The placement. The commit each replay-1 clone checks out is `6cfd21619` plus one commit
  adding `memory/builds/dFairHearing/README.md` as at base `3708a705`, and the call names `reviewDir`
  `memory/builds/dFairHearing/reviews`, unit 23 S22's placement. Blindness is held as spec 1 AC4 holds
  it, with that one commit admitted: no other commit outside `6cfd21619`'s history, and that commit's
  tree differs from `6cfd21619`'s by that one path alone. Each run's call, replayed through
  `tools/workflows/spec-audit-optin.js`, unit 16's opt-in pack, is admitted. Observed by AC1 and AC2.
- **S3** — Scoring on the corrected terms. Each replay is declared in a manifest in unit 23 S4's
  terms (`candidates` entries `{case, report, matched}`, `dispatched` per arm) and checked by
  `tools/workflows/replay_scorer.py --experiment`, unit 12's factory. Each replay-1 run is scored by `review_replay.py --known-set
  --candidate --matched` (spec 1 S3). Spec 1 §4's void rule reads S4's terms: a run whose report is
  not parsed, whose `RUN INTEGRITY` names a dead finder or skeptic, or whose transcripts read outside
  the clone and the scratchpad is re-run under S10's cap, never scored. Observed by AC3.
- **S4** — Unit 15's replay, run once on the corrected contract: the eight runs of
  `TOOL-dFairHearing-15` S5 over its §4 corpus, arms `selected` and `ungated`. Each record's range head
  gets its own clone by the same recipe, a fresh name per clone, `HEAD` equal to that range head.
  Its manifest declares `dispatched` 4 per arm, and the verdict pairs over the records both arms
  answered. Observed by AC4.
- **S5** — The verdicts set the switches. Replay 1: `DESIGN_RECORD_PRESET` in
  `tools/workflows/review_pin.py` reads `design-audit` when both runs meet spec 1's bar (45 of 59
  reviewed, 4 of 6 escaped, 7 of 8 high), and keeps unit 3's default otherwise; the template's
  `preset` default stays `unit-spec` (unit 23 S40). A miss files spec 1 S9's R-1 ask in this build's
  `BACKLOG.md`, naming both runs' counts. Unit 15's replay: spec 15 S6 lands, `--all-ungated` and the
  acquiring command carrying it, when `ungated`'s pooled recall is above `selected`'s, and no product
  file of spec 15 S6 changes otherwise. Observed by AC5 and AC6.
- **S6** — One verdict record, `memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-25-replay-verdicts.md`,
  opening `**Serves:** research TOOL-dFairHearing-25 TOOL-dFairHearing-1 TOOL-dFairHearing-15`. It
  names each replay's figures, bar and verdict, its raw outputs, the orchestrating commit and blobs S7
  binds, unit 23's build commit, and the class set the `ungated` arm carried. Observed by AC7.
- **S7** — The orchestrating commit, carried from `TOOL-dFairHearing-32` S14 (ids 5 and 13 of the
  round-3 spec audit). Before the first run, this repository's `HEAD` is read by `git rev-parse
  --verify HEAD`, its exit checked, and the verdict record names it as the orchestrating commit, on a
  line apart from each clone's `HEAD`. Beside it the record names the blob of
  `tools/workflows/README.md`, `tools/workflows/tier2-review.js` and `tools/workflows/replay_scorer.py`
  as the runs read them, each by `git hash-object`. The binding is evidence the writer does not
  choose: the commit that adds the record has the orchestrating commit as its first parent, each named
  blob equals that commit's blob at its path, and the orchestrating commit descends from unit 23's
  build commit. This replaces S6's "the commit the runs started from" and AC7's ancestry test.
  Observed by AC7.
- **S8** — One replay procedure, carried from `TOOL-dFairHearing-32` S17 (id 21) and S18 (id 31). The
  replay section of `tools/workflows/README.md`, as unit 27 S22 leaves it (the stale refusal, every
  step's exit checked, the exact-commit check and the EXIT trap), is the procedure every run here
  follows, and §4 restates none of it. Before the first run, this unit adds the placement step of §4
  to that section: a commit the source history lacks is made by `git commit-tree` over a tree written
  through a temporary `GIT_INDEX_FILE`, referenced only by the transient ref the recipe bundles. The
  working tree, the index and `HEAD` of this repository never move. This replaces the transient
  branch §4 named and §5's claim that id 36 is covered by this unit's exact-commit check. Observed by
  AC8.
- **S9** — One EXIT trap, carried from `TOOL-dFairHearing-37` S19 (id 37 of the round-4 spec audit),
  counted as `TOOL-dFairHearing-40` S20 (id 5 of the round-5 audit) counts it. The placement step and
  the recipe set one trap holding both `rm -f "$idx"` and `git update-ref -d refs/replay/<name>`, so
  neither replaces the other. Over the replay section's fenced bash lines, sliced from its heading to
  the next `## ` with comment lines left out, one line opens `trap '`. Observed by AC8.
- **S10** — Attempts, carried from `TOOL-dFairHearing-32` S20 (id 29) and S21's replay-1 half (id 30).
  A re-run takes a new clone named per attempt, `fhr<run><a>`: `<run>` 1 or 2, `<a>` the attempt
  letter from `a`, so the first attempts are `fhr1a` and `fhr2a`. A voided clone stays on disk until
  the record cites it. A run takes at most two attempts. After a second void, the record states
  replay 1 `not run`, `DESIGN_RECORD_PRESET` keeps its default and spec 1 S9's R-1 ask is filed, as
  S5's miss. This replaces S1's fixed names `fhr1` and `fhr2` and S3's unbounded re-run. Observed by
  AC1 and AC9.

## 3. Non-goals (OUT)

- No re-run of spec 1's replays 2, 3 and 4. They clone nothing, make no spec-audit call, and spec 1
  applies the void rule to replay 1's runs alone, so no corrected term touches their verdicts.
- No change to the known set, the matched-list reader, the calibration or the bars: spec 1 S1 to S4
  stand and this unit reads them.
- No change to the manifest grammar or to the recipe's own steps: they are units 23 and 27's, read
  here. The placement step and its one trap (S8, S9) are this unit's one change to the replay
  section, made before its first run.
- No reading of the records after the runs. The re-reads are `TOOL-dFairHearing-32`'s: its S13, S19,
  and the post-run halves of its S14, S17, S20 and S21.
- No fix of the minors the same audit raised on unit 23. Ids 13, 36 and 39 land with
  `TOOL-dFairHearing-27`, before this unit; §5 says why none of them moves a verdict here.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-23` — the corrected manifest terms (S4), the recipe (S17, S18), the placement (S22) and the flip site (S40); without them these runs repeat the defect
- **consumes-from** `TOOL-dFairHearing-1` — the known set, `parse_known_set`, `--matched`, the calibration, replay 1's arguments and bar, and the R-1 ask rule
- **consumes-from** `TOOL-dFairHearing-15` — the `resume:checklist` agent, the corpus, the two arms and their instrument, and the decision rule
- **hands-off** `TOOL-dFairHearing-30` — finding id 28 (item H2) of the round-3 spec audit: unit 15's with-and-without replay, run with one fresh clone per record and arm, and its decision; this unit's S4, AC4, the unit-15 half of S5, AC6 and the unit-15 lines of S6 and AC7 are superseded by its S1 to S5 and AC1 to AC4
- **hands-off** `TOOL-dFairHearing-37` — this unit's verdict record, whose call-time orchestrating commit its AC3 reads after the runs
- **hands-off** `TOOL-dFairHearing-32` — the same audit's minors on this spec, ids 4, 5, 9, 13, 21, 24, 29, 30 and 31: what reads this unit's records after the runs, its S13, S16, S19 and the post-run halves of S14, S17, S20 and S21; what had to hold before the runs, from its S14, S17, S18, S20 and S21, is carried here as S7, S8 and S10

## 4. Design

### Why the runs move here rather than run twice

Units 1 and 15 hand these runs to this unit (§8 F1): spec 1 keeps S1 to S4 and replays 2 to 4, and
spec 15 keeps S1 to S4. Each hands-off bullet names the criteria this unit answers in its place, and
that unit's acceptance ledger records them as superseded by the criteria named here (spec 23 §8 F7's
form). Running first at order 15 or 16 would mean running spec 1's clone step, which exits 128, or
scoring on manifest terms the build already declared defective. It would spend about 130 agents on
verdicts this unit would then have to reverse.

### The run, per clone

The procedure is the replay section of `tools/workflows/README.md` (S8), run once per attempt clone,
`<name>` the clone's S10 name and `<commit>` the commit given. Its exact-commit check, unit 27 S22's,
is the liveness check. For replay 1, `<commit>` is the placement commit of S2, made by the step
below and reachable only from the transient ref. Unit 15's runs are unit 30's.

### The placement step (S8, S9)

```bash
idx=$(mktemp -p "$SCRATCH")
trap 'rm -f "$idx"; git update-ref -d refs/replay/<name> 2>/dev/null' EXIT   # the one trap
GIT_INDEX_FILE="$idx" git read-tree 6cfd21619
GIT_INDEX_FILE="$idx" git update-index --add --cacheinfo 100644,<blob>,memory/builds/dFairHearing/README.md
tree=$(GIT_INDEX_FILE="$idx" git write-tree)
git update-ref refs/replay/<name> "$(git commit-tree "$tree" -p 6cfd21619 -m placement)"
# then the recipe, bundling refs/replay/<name>, with its own trap line taken out
```

`<blob>` is `git rev-parse 3708a705:memory/builds/dFairHearing/README.md`, which printed
`606886dda5815c5979992ea50842b2a3368061a5` on 2026-11-03. `$SCRATCH` is the run's scratch directory.
Each command's exit status is checked, and no step touches the working tree, the index or `HEAD`.

### What the verdict record proves

The runs read the procedure files whose blobs S7 names, and the commit that adds the record holds
exactly those blobs over a first parent, the orchestrating commit, that descends from unit 23's build
commit. That ancestry is the property finding id 1 found missing: no verdict that sets a switch rests
on a contract the build had already declared defective.

### Files touched (estimate)

- `tools/workflows/review_pin.py`
- `tools/memory-tree/gotchas.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/README.md`
- `memory/builds/dFairHearing/build/`
- `memory/builds/dFairHearing/BACKLOG.md`

`review_pin.py` changes only on a replay 1 hit. `gotchas.py` and the harness template change only
when `ungated` wins, as spec 15 S6 states. The README's switch paragraph states the default the
verdict leaves. `tools/workflows/tier2-review.js` is the template's render.

### Alternatives rejected

- **Re-run after units 1 and 15 have run** — §8 F1 (a).
- **Run first, and let the later units patch the records** — §8 F2 option 2.
- **Move the corrected items before order 15** — the skeptic's first fix. This unit's order is fixed
  above the unit it repairs, `TOOL-dFairHearing-23`, and above `TOOL-dFairHearing-27`, which corrects that unit's recipe.

## 5. Production-readiness checklist

- security — the clones and bundles sit under `%TEMP%`, outside the repository. The placement makes
  no branch: its commit is reachable only from the transient ref, which the one EXIT trap deletes
  with the temporary index (S9). The lenses keep the spec kind's read-only probe rules.
- perf / scale — replay 1 costs about 24 agents and 430k output tokens (spec 1 §5). Unit 15's replay
  costs about 8 review runs, roughly 100 agents (spec 15 AC8).
- error / empty / loading states — a stale clone directory, a `HEAD` that is not the given commit, a
  void run and a manifest the factory refuses are each named and re-run or refused, never scored; a
  third attempt is never made (S10).
- observability — the verdict record carries every figure beside its bar, its raw output, the
  orchestrating commit and its blobs (S7).
- risks — `TOOL-dFairHearing-27` lands three corrections to unit 23's code before this unit, and none
  of them moves a verdict here. Id 13 adds the item-only row of the spec-kind ref reader, but every
  replay-1 pair must cite its known row's `[tag]` (spec 1 S3), and unit 15's corpus is diff-review
  records, scored by line (`tools/workflows/review_replay.py:87-97`, chosen by kind at `:248`). Id 36 is unit 27 S22's envelope,
  which S8 follows. Id 39 can widen the `ungated` arm by the classes whose gate token wraps onto the
  next line, so S6 lists the arm's class set and the batch's corrected predicate can be checked
  against it.
- testing — the criteria below. This unit adds no suite arm: its outputs are records and verdicts.
- migration — none for adopters. A default flip changes what an unflagged call does, and the README
  names it.
- user docs — `tools/workflows/README.md`'s switch paragraphs; no `help/` page.

## 6. Acceptance criteria

- **AC1** — When each replay-1 attempt's clone is made, `git -C "$TEMP/<clone>" rev-parse HEAD` equals
  the placement commit and `git -C "$TEMP/<clone>" rev-list --all` names no commit absent from `git
  rev-list 6cfd21619` except that one. `git -C "$TEMP/<clone>" diff --name-only 6cfd21619 HEAD` prints
  exactly `memory/builds/dFairHearing/README.md`, and `git -C "$TEMP/<clone>" rev-parse
  6cfd21619:memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` prints
  `767187aa4073f6e64cb2b2ef6b798f0a538347fd`. This holds for every clone the record names, `fhr1a`,
  `fhr2a` and any S10 re-run, and a second recipe run into an existing `fhr1a` exits 2 before any
  fetch. Afterwards, `git for-each-ref refs/replay/` in this repository prints nothing.
  Red when: a clone reaches a later object, a reused directory ends at another commit, or a ref
  survives.
  fixture: the clones under `%TEMP%`, made by the pass.
- **AC2** — When each replay-1 run returns, its report sits under the clone's
  `memory/builds/dFairHearing/reviews/`, and its `**Serves:** spec-audit` line names the runtime
  record. Replaying that call's payload on stdin through `node spec-audit-optin.js`, the opt-in pack
  §2 S2 names by path, exits 0.
  Red when: the opt-in pack denies the replayed call, so no report lands.
  cost: about 24 agents and 430k output tokens for the two runs.
- **AC3** — When `python replay_scorer.py --experiment <manifest>`, the factory §2 S3 names by path,
  runs over replay 1's committed manifest, it prints `parsed <arm>: 2 of 2` before any figure. Each run's
  `review_replay.py --known-set <known set> --candidate <report> --matched <list>` prints `reviewed
  <k>/59`, `escaped <k>/6` and `high <k>/8`, and the verdict record states those figures against
  `45/59`, `4/6` and `7/8`.
  Red when: a void run is scored, or the manifest's `matched` entries are refused.
- **AC4** — When `replay_scorer.py --experiment` runs over unit 15's committed manifest, it prints
  `arm ungated: varies checklist from selected`, then `parsed selected: 4 of 4` and `parsed ungated:
  4 of 4` before any figure. Each clone's `git -C <clone> rev-parse HEAD` equals its record's range
  head, and the verdict record names each record's recall under both arms, `paired 4 of 4`, both
  pooled figures and the decision.
  Red when: a clone at another commit is reviewed, or a record one arm did not answer is pooled.
  cost: about 8 review runs, roughly 100 agents.
  fixture: four clones under `%TEMP%`, one per range head, made by the pass.
- **AC5** — When `grep -n "DESIGN_RECORD_PRESET" review_pin.py` runs over the file §2 S5 names by
  path, its value is `design-audit` exactly when the verdict record states both replay-1 runs hit. The template's
  `preset` default literal in `tools/workflows/tier2-review.template.js` reads `unit-spec`. On a miss,
  `memory/builds/dFairHearing/BACKLOG.md` gains one ask naming R-1 and both runs' counts.
  Red when: the switch disagrees with the verdict record, or a template default is flipped.
- **AC6** — When `selected` holds, `grep -c -- "--all-ungated" tools/memory-tree/gotchas.py` prints 0.
  When `ungated` wins, spec 15 AC9's fixture observation holds: `gotchas.py --for-diff <range>
  --all-ungated` over a fixture catalogue prints the range's selection first, then every class naming
  no manifest leg, and the acquiring command carries the flag.
  Red when: the product changes against the decision.
- **AC7** — When the verdict record lands, `git log --diff-filter=A --format=%P -1 -- <record>` prints
  a first parent equal to the orchestrating commit the record names. `git merge-base --is-ancestor
  <unit 23's commit> <that commit>` exits 0, and `git log -1 --format=%s <unit 23's commit>` names
  `TOOL-dFairHearing-23`. Each blob the record names equals `git rev-parse <the adding commit>:<path>`
  for its path, and each clone's `HEAD` stands on a line of its own. The record also lists the
  `ungated` arm's classes.
  Red when: a run started from a commit that does not contain unit 23's corrections, a procedure file
  changed between the runs and the commit, or a clone's `HEAD` stands in for the orchestrating commit.
- **AC8** — When `grep -n "commit-tree" tools/workflows/README.md` runs, it prints the placement step
  inside the replay section. Over that section's fenced bash lines, sliced from its heading to the
  next `## ` with comment lines left out, `grep -c "^\s*trap '"` prints 1, and a copy whose prose holds
  the word `trap ` still prints 1. A scratch run of the placement and the recipe in a fixture
  repository, with `git bundle create` forced to fail, leaves `git for-each-ref refs/replay/` printing
  nothing, `test ! -e "$idx"` exiting 0, and that repository's `git status --porcelain` and `HEAD`
  unchanged.
  Red when: a failed bundle leaves a transient ref or the temporary index, the placement moves the
  working tree, or a second trap line replaces the first.
  fixture: the repository under `%TEMP%/fpl`, made by the probe and removed after it.
- **AC9** — When the verdict record lands, it lists for each replay-1 run one or two attempts, each
  under its own `fhr<run><a>` clone, none named twice, with each void attempt's cause beside it. A run
  whose two attempts are void reads `not run`, and `grep -n "R-1" memory/builds/dFairHearing/BACKLOG.md`
  prints its ask.
  Red when: a clone serves two attempts, a third attempt runs, or a twice-void run is scored.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `gotchas selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: this unit's outputs are the verdict record, the manifests and the switch state they set,
each observed directly by §6.

## 8. Open questions

- **F1 — Do units 1 and 15 still run these replays at their own order?** Options: (a) they run them
  as written, and this unit re-runs them and reverses any verdict that moves; (b) they hand these runs
  to this unit, each superseded criterion named in its hands-off bullet, and the runs happen once,
  here. (a) puts spec 1's clone step, which exits 128, into unit 1's pass. It also spends about 130
  agents on verdicts made under a contract the build has declared defective, and it can flip a switch
  only to flip it back. (b) closes the finding with one run per replay and leaves units 1 and 15
  every item the corrected contract does not touch. RESOLVED (agent, 2026-10-23, delegated): (b),
  rung 3. widens: none · relaxes: none
- **F2 — The replays' pre-run corrections sit in units ordered after the runs: fold them here, or run
  first?** Units 32, 37 and 40 each correct the procedure these runs and unit 15's replay follow (the
  orchestrating-commit binding, one clone envelope, the placement step, per-attempt clones and their
  cap, the void and re-run rule, the per-arm clone, path and status, the attempt checker, and the
  reports kept on disk), and each also reads the records the runs leave, so no order puts them both
  before and after the replays (the return of fix brief
  2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief). Options: (1) fold each correction that
  must hold before a run into the replay unit's own spec, 25, 30 or 35, under M4's repair rule ("A
  repair unit corrects an UNBUILT sibling's spec itself", owner 2026-11-01), and leave in 32, 37 and
  40 only what reads or completes the records afterwards; (2) run the replays at their orders on the
  procedure as written, and let 32, 37 and 40 patch the records after. (2) spends the ten runs on the
  old procedure and patches the records after, the defect class unit 35 was promoted to close. (1)
  leaves no follow-up. Recommendation: (1). RESOLVED (agent, 2026-11-03, delegated): option 1, M3's
  most feature-rich survivor; this unit's S7 to S10, unit 30's S7 to S10 and unit 35's S7 to S9 carry
  the folded items. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (item H1) of the spec audit of units 20
  to 23.
- rev-2 · 2026-10-23 · §3 · the round-3 spec audit's disposal: hands-off edges to TOOL-dFairHearing-30
  (unit 15's replay in per-arm clones, finding id 28) and TOOL-dFairHearing-32 (nine minors).
- rev-3 · 2026-11-03 · §7 · the leg line adds `policy fixtures`, whose guard §4's
  `tools/memory-tree/gotchas.py` trips (2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief,
  item 1).
- rev-4 · 2026-11-03 · header · §1 · §3 · §4 · §5 · the header's order 20 to 22, after
  `TOOL-dFairHearing-27`, whose S22 corrects the recipe these runs follow; §1, §3, §4 and §5 re-word
  this unit's position to match (fix brief 2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief,
  items 2 and 3).
- rev-5 · 2026-11-03 · §1 · S1 · S3 · S6 · S7 · S8 · S9 · S10 · §3 · §4 · §5 · AC1 · AC7 · AC8 · AC9 ·
  §8 F2 · the replays' pre-run corrections folded in (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief, items 1 and 2). S7 carries unit 32 S14's
  orchestrating-commit binding (ids 5 and 13), rewriting AC7; S8 carries unit 32 S17's one clone
  envelope (id 21) and S18's placement through a temporary index (id 31), replacing §4's block and
  transient branch; S9 carries unit 37 S19's one EXIT trap (id 37), counted as unit 40 S20 counts it
  (id 5); S10 carries unit 32 S20's per-attempt clones and two-attempt cap (id 29) and S21's replay-1
  void and re-run rule (id 30), renaming AC1's clones. §8 F2 records the fork. §3 takes a hands-off
  edge to unit 37, whose AC3 reads this unit's record.

## 10. Reuse audit

No new mechanism: the unit runs replays that units 1 and 15 specify, through seams those units and
unit 23 build. Those seams are the recipe in `tools/workflows/README.md`, the factory's
`check_experiment`, `review_replay.py`'s `--known-set` and `--matched`, `review_pin.py`'s
`DESIGN_RECORD_PRESET` and `gotchas.py`'s `--all-ungated`. `python tools/codebase-map/reuse_lookup.py
"re-run a blind replay after its scoring contract is corrected"` ranked generic `run` stems and
`score` in `tools/memory-recall/bench.py`, and no replay driver. No existing seam fits a driver,
and none is needed, because each replay's procedure is already written in its unit's spec. The recall
query returned spec 1, the audit's H1 item and spec 1's hands-off bullets, which §4 follows.

Recall terms used: `python tools/memory-recall/query.py "when a later unit corrects the contract an earlier replay ran under, how are the replay verdicts re-derived" --terms "blind replay re-run verdict dark switch flip corrected contract bundle fetch manifest matched order inversion"`
