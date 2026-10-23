# TOOL-dFairHearing-25 — the owed replays run after the replay contract is corrected, and their verdicts set the dark switches

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 20 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-25-deviation-251.md](../build/2026-10-23-build-TOOL-dFairHearing-25-deviation-251.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md) | research | TOOL-dFairHearing-26 TOOL-dFairHearing-27 |
| [2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md) | research | TOOL-dFairHearing-4 TOOL-dFairHearing-18 TOOL-dFairHearing-27 |
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
unit, ordered directly after unit 23, runs replay 1's two design-audit runs and unit 15's eight
with-and-without runs on the corrected contract, and the switch state at its commit is what those
verdicts say.

## 2. Scope (IN)

- **S1** — Replay 1, run once on the corrected contract: the two design-audit runs of
  `TOOL-dFairHearing-1` S5, with the arguments its §4 "The isolation" names. Each run takes its own
  clone, made by the recipe in `tools/workflows/README.md`'s replay section (unit 23 S17) under a
  fresh name, `fhr1` and `fhr2`. A clone directory that already exists is refused, never reused, and
  the clone's `HEAD` must equal the commit the recipe was given. Observed by AC1.
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
  the clone and the scratchpad is re-run, never scored. Observed by AC3.
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
  names each replay's figures, bar and verdict, its raw outputs, the commit the runs started from and
  unit 23's build commit, and the class set the `ungated` arm carried. Observed by AC7.

## 3. Non-goals (OUT)

- No re-run of spec 1's replays 2, 3 and 4. They clone nothing, make no spec-audit call, and spec 1
  applies the void rule to replay 1's runs alone, so no corrected term touches their verdicts.
- No change to the known set, the matched-list reader, the calibration or the bars: spec 1 S1 to S4
  stand and this unit reads them.
- No change to the recipe, the manifest grammar or the placement: they are unit 23's, read here.
- No fix of the minors the same audit raised on unit 23. Ids 13, 36 and 39 land with
  `TOOL-dFairHearing-27`, after this unit; §5 says why none of them moves a verdict here.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-23` — the corrected manifest terms (S4), the recipe (S17, S18), the placement (S22) and the flip site (S40); without them these runs repeat the defect
- **consumes-from** `TOOL-dFairHearing-1` — the known set, `parse_known_set`, `--matched`, the calibration, replay 1's arguments and bar, and the R-1 ask rule
- **consumes-from** `TOOL-dFairHearing-15` — the `resume:checklist` agent, the corpus, the two arms and their instrument, and the decision rule
- **hands-off** `TOOL-dFairHearing-30` — finding id 28 (item H2) of the round-3 spec audit: unit 15's with-and-without replay, run with one fresh clone per record and arm, and its decision; this unit's S4, AC4, the unit-15 half of S5, AC6 and the unit-15 lines of S6 and AC7 are superseded by its S1 to S5 and AC1 to AC4
- **hands-off** `TOOL-dFairHearing-32` — the same audit's minors on this spec, ids 4, 5, 9, 13, 21, 24, 29, 30 and 31: its S13 to S21, each naming what it supersedes

## 4. Design

### Why the runs move here rather than run twice

Units 1 and 15 hand these runs to this unit (§8 F1): spec 1 keeps S1 to S4 and replays 2 to 4, and
spec 15 keeps S1 to S4. Each hands-off bullet names the criteria this unit answers in its place, and
that unit's acceptance ledger records them as superseded by the criteria named here (spec 23 §8 F7's
form). Running first at order 15 or 16 would mean running spec 1's clone step, which exits 128, or
scoring on manifest terms the build already declared defective. It would spend about 130 agents on
verdicts this unit would then have to reverse.

### The run, per clone

```bash
test ! -e "$TEMP/<name>" || exit 2                     # a stale directory is refused, never reused
# the recipe of tools/workflows/README.md, each step's exit status checked
test "$(git -C "$TEMP/<name>" rev-parse HEAD)" = "<the commit given>"   # the liveness check
git show-ref refs/replay/<name>                        # prints nothing afterwards
```

For replay 1, `<the commit given>` is the placement commit of S2. It is made on a transient branch
at `6cfd21619` in this repository and deleted with the transient ref, so this repository keeps
neither. For unit 15, it is the record's range head. The exact-commit comparison is this unit's own
liveness check. It does not wait for `TOOL-dFairHearing-27`'s recipe fix (finding id 36).

### What the verdict record proves

Each run starts from a commit that descends from unit 23's build commit, and the record names both
shas. That ancestry is the property finding id 1 found missing: no verdict that sets a switch rests
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
- **Move the corrected items before order 15** — the skeptic's first fix. This unit's order is fixed
  one above the unit it repairs, and that unit is `TOOL-dFairHearing-23`.

## 5. Production-readiness checklist

- security — the clones and bundles sit under `%TEMP%`, outside the repository. The transient refs
  and the placement branch are deleted in the step that made them. The lenses keep the spec kind's
  read-only probe rules.
- perf / scale — replay 1 costs about 24 agents and 430k output tokens (spec 1 §5). Unit 15's replay
  costs about 8 review runs, roughly 100 agents (spec 15 AC8).
- error / empty / loading states — a stale clone directory, a `HEAD` that is not the given commit, a
  void run and a manifest the factory refuses are each named and re-run or refused, never scored.
- observability — the verdict record carries every figure beside its bar, its raw output and both
  shas.
- risks — `TOOL-dFairHearing-27` lands three corrections to unit 23's code after this unit, and none
  of them moves a verdict here. Id 13 adds the item-only row of the spec-kind ref reader, but every
  replay-1 pair must cite its known row's `[tag]` (spec 1 S3), and unit 15's corpus is diff-review
  records, scored by line (`tools/workflows/review_replay.py:87-97`, chosen by kind at `:248`). Id 36 is covered by §4's own
  exact-commit check. Id 39 can widen the `ungated` arm by the classes whose gate token wraps onto the
  next line, so S6 lists the arm's class set and the batch's corrected predicate can be checked
  against it.
- testing — the criteria below. This unit adds no suite arm: its outputs are records and verdicts.
- migration — none for adopters. A default flip changes what an unflagged call does, and the README
  names it.
- user docs — `tools/workflows/README.md`'s switch paragraphs; no `help/` page.

## 6. Acceptance criteria

- **AC1** — When each replay-1 clone is made, `git -C "$TEMP/fhr1" rev-parse HEAD` equals the
  placement commit and `git -C "$TEMP/fhr1" rev-list --all` names no commit absent from `git rev-list
  6cfd21619` except that one. `git -C "$TEMP/fhr1" diff --name-only 6cfd21619 HEAD` prints exactly
  `memory/builds/dFairHearing/README.md`, and `git -C "$TEMP/fhr1" rev-parse
  6cfd21619:memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` prints
  `767187aa4073f6e64cb2b2ef6b798f0a538347fd`. Afterwards, `git show-ref refs/replay/fhr1` in this
  repository prints nothing. The same holds for `fhr2`, and a second recipe run into an existing
  `fhr1` exits 2 before any fetch.
  Red when: a clone reaches a later object, a reused directory ends at another commit, or a ref
  survives.
  fixture: the clones under `%TEMP%/fhr1` and `%TEMP%/fhr2`, made by the pass.
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
- **AC7** — When the verdict record lands, it names unit 23's build commit and the commit the runs
  started from. `git merge-base --is-ancestor <unit 23's commit> <the runs' commit>` exits 0, and
  `git log -1 --format=%s <unit 23's commit>` names `TOOL-dFairHearing-23`. The record also lists the
  `ungated` arm's classes.
  Red when: a run started from a commit that does not contain unit 23's corrections.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `gotchas selftest` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

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

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (item H1) of the spec audit of units 20
  to 23.
- rev-2 · 2026-10-23 · §3 · the round-3 spec audit's disposal: hands-off edges to TOOL-dFairHearing-30
  (unit 15's replay in per-arm clones, finding id 28) and TOOL-dFairHearing-32 (nine minors).

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
