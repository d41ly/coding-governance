# TOOL-dFairHearing-30 — unit 15's with-and-without replay run with one fresh clone per record and arm, so no arm reviews a tree holding the other's report

**Status:** OPEN · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 21 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-30-deviation-301.md](../build/2026-10-23-build-TOOL-dFairHearing-30-deviation-301.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-30-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-30-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md) | spec-audit | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit's finding id 28 (item H2, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`) is
closed. `TOOL-dFairHearing-25` runs unit 15's `selected` and `ungated` arms of each record in one
clone, and the harness writes each report under `${repo}/${reviewDir}`
(`tools/workflows/tier2-review.template.js:297`, `:1749`). The first arm's report therefore sits in
the working tree the second arm reviews, and the recall comparison that decides spec 15 S6's product
state can be contaminated. This unit takes that replay from unit 25 and runs each record and arm in
its own freshly made clone, checked clean before its call, so no arm can read another arm's output.
The decision then follows from these runs.

## 2. Scope (IN)

- **S1** — One clone per record and arm. Unit 15's eight runs (spec 15 S5, its §4 corpus, arms
  `selected` and `ungated`) each take a fresh clone made by unit 25 §4's "The run, per clone" block at
  that record's range head. A clone is named `f<r><a><n>`: `<r>` the record's position 1 to 4 in
  spec 15 §4's corpus, `<a>` `s` or `u` for the arm, `<n>` the attempt from 1. So the first attempts
  are eight distinct names, `f1s1` to `f4u1`. Observed by AC1.
- **S2** — Clean before the call. Immediately before each arm's harness call, `git -C "$TEMP/<clone>"
  status --porcelain --untracked-files=all` prints nothing, and the call names that clone as its
  `repo`. A non-empty status refuses the call, and the arm takes a new attempt in a new clone. The
  verdict record keeps each observed status beside its clone. Observed by AC1 and AC2.
- **S3** — No clone is reused. A re-run of a record and arm, for any cause, takes the next attempt
  number and a new clone, and unit 25 §4's stale-directory refusal holds for every name. A clone stays
  on disk until the verdict record cites it. Observed by AC2.
- **S4** — Scoring and the decision, on unit 25's stated terms. The manifest declares the two arms one
  variable apart and `dispatched` 4 per arm, in unit 23 S4's terms, and
  `tools/workflows/replay_scorer.py --experiment` checks it. Pairing, the pooled figures and the
  decision are unit 25 S4's and S5's unit-15 half, read as written, and spec 15 S6 lands only when
  `ungated`'s pooled recall is above `selected`'s. Observed by AC3 and AC4.
- **S5** — One verdict record,
  `memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-30-replay-verdict.md`, opening
  `**Serves:** research TOOL-dFairHearing-30 TOOL-dFairHearing-15`. For each record and arm it names
  every attempt's clone, the clone's `HEAD`, the status S2 observed and the report path. It names each
  record's recall under both arms, the pooled figures, the decision and the class set the `ungated`
  arm carried. Observed by AC1 and AC3.
- **S6** — Supersession. Unit 25's S4, AC4, the unit-15 half of S5, AC6, and the unit-15 lines of S6
  and AC7 (the `ungated` class set) are answered by this unit's S1 to S5 and AC1 to AC4. Unit 25's
  acceptance ledger records them superseded here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by
  a criterion of this unit: it is a ledger entry in unit 25's record, read there.

## 3. Non-goals (OUT)

- No replay 1. Its two design-audit runs each already take their own clone (unit 25 S1), so the shared
  tree this finding names does not arise there, and they stay unit 25's.
- No change to the recipe, the manifest grammar, the corpus, the arms or the decision rule. They are
  units 23, 14 and 15's, read here.
- No fix of the same audit's minors on unit 25: ids 4, 5, 13, 21, 24, 29, 30 and 31 are
  `TOOL-dFairHearing-32`'s, after this unit.
- No change to where the harness writes its report. A per-arm clone removes the shared tree without a
  product change, and the harness's `reviewDir` contract serves every other caller.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-25` — the per-clone block (stale refusal, recipe, exact-commit check, ref cleanup), unit 15's run terms and the decision rule; this unit runs that replay in its place
- **consumes-from** `TOOL-dFairHearing-15` — the `resume:checklist` agent, the corpus, the two arms, the instrument and S6's product change
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment` and the manifest's `parsed` lines, which AC3 reads literally
- **hands-off** `TOOL-dFairHearing-32` — the minors that read this unit's verdict record: the behavioural `selected` check (id 4), the runs' orchestrating commit (ids 5, 13) and the one rule for a dead run (id 30)
- **hands-off** `TOOL-dFairHearing-35` — finding id 32 (item H2) of the round-4 spec audit: the attempt rule that decides which completed attempt is scored, and with it the scoring and the decision; this unit's S4, the figure and decision half of S5 and AC3, AC4's ungated half, spec 15 S6's product files and the selftest arm on the flag are superseded by its S1 to S6 and AC1 to AC4
- **hands-off** `TOOL-dFairHearing-37` — the same audit's minors on this spec, ids 1, 5, 12, 20, 26, 33 and 34: AC1 restated over the scored attempt, AC4's selected half observed by behaviour, and the per-arm clone, the forward-slash path and the checked status carried into the one replay procedure for every later replay (its S1, S4, S6, S8, S11, S12 and S18)
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors that read this unit's verdict record, ids 9, 13, 24 and 29: the void column re-derived from each attempt's report and quoted transcript line, so each report and transcript the record names stays on disk until that unit's pass, the record's `**Serves:**` line read for `TOOL-dFairHearing-35`, and the `ungated` class set re-derived (its S9, S24, S25 and S30)


## 4. Design

### Why the replay moves here

Unit 25 runs at order 20 and this unit at 21. Correcting the isolation after unit 25 had run would
mean about 100 agents spent on a comparison the build had already found contaminable, then run
again, the shape unit 25 §8 F1 refused for the same reason. So unit 25 hands this replay over, as
units 1 and 15 handed their replays to unit 25. Replay 1 stays with unit 25.

### The run, per record and arm

```bash
c="$TEMP/f<r><a><n>"
# unit 25 §4's block over "$c" at the record's range head: stale refusal, recipe, exact-commit check
test -z "$(git -C "$c" status --porcelain --untracked-files=all)" || { echo "dirty: $c"; exit 2; }
# the harness call, `repo` set to "$c"; its report lands under "$c/<reviewDir>"
```

The status check sits after the clone is made and before the call, so it reads the tree the arm will
review. After the call, that clone's status lists one untracked path, the arm's own report, which is
what AC1 observes after the fact.

### What it does not check

That no agent reads a sibling clone by absolute path. The per-arm clone and the clean-tree check
remove the in-tree path the finding names. A read outside the clone is what spec 1 §4's outside-read
void rule reads for replay 1. For these runs, the dead-run rule is `TOOL-dFairHearing-32`'s item for
id 30.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/README.md`
- `memory/builds/dFairHearing/build/`

`gotchas.py`, the harness template and its render change only when `ungated` wins, as spec 15 S6
states. The README's switch paragraph states the default the verdict leaves.

### Alternatives rejected

- **Keep one clone per record and delete arm 1's report before arm 2.** A cleanup step is one more
  thing a run can skip, and the durability files a resumed run writes sit beside the report. A fresh
  clone has nothing to clean.
- **Write the report outside the clone.** That changes the harness's `reviewDir` contract for every
  caller to serve one comparative run.

## 5. Production-readiness checklist

- security — the clones sit under `%TEMP%`, outside the repository, and unit 25 §4's block clears its
  transient ref. The lenses keep the diff kind's read-only probe rules.
- perf / scale — eight clones in place of four, each a local fetch of one range head. The agent cost
  is unit 25's, about 100 agents (spec 15 AC8).
- error / empty / loading states — a stale clone name, a `HEAD` that is not the range head and a dirty
  tree are each refused before the call, and the arm takes a new attempt.
- observability — the verdict record names every attempt's clone, `HEAD` and status beside the figures.
- risks — a flaky run costs a new clone per attempt; the attempt cap is `TOOL-dFairHearing-32`'s item
  for id 29.
- testing — AC1 to AC4. On an `ungated` win, spec 15's `New arm:` line for `gotchas.py`'s selftest
  applies, and the close observes it.
- migration — none for adopters. A flag landing changes what the harness acquires, and the README
  names it.
- user docs — `tools/workflows/README.md`'s switch paragraph; no `help/` page.

## 6. Acceptance criteria

- **AC1** — When the verdict record lands, it names eight first-attempt clones, `f1s1` to `f4u1`, all
  distinct, each with an empty observed status. For each, `git -C "$TEMP/<clone>" rev-parse HEAD`
  equals its record's range head, and `git -C "$TEMP/<clone>" status --porcelain
  --untracked-files=all` lists exactly one path, that arm's own report.
  Red when: two arms of one record share a clone, so one clone lists both reports, or a clone at
  another commit is reviewed.
  fixture: the clones under `%TEMP%`, made by the pass and kept until the record cites them.
- **AC2** — When the per-arm block runs into a scratch clone holding one planted untracked file, it
  exits 2 printing `dirty:` and the clone's path before any harness call. A second run into an existing
  clone name exits 2 before any fetch. Every re-run the record lists names a clone whose attempt number
  is higher than the one before.
  Red when: the dirty clone is reviewed, or a re-run reuses a clone.
  fixture: one scratch clone under `%TEMP%/fdirty`, made by the probe.
- **AC3** — When `replay_scorer.py --experiment` runs over this unit's committed manifest, it prints
  `arm ungated: varies checklist from selected`, then `parsed selected: 4 of 4` and `parsed ungated: 4 of
  4` before any figure. The verdict record names each record's recall under both arms, `paired 4 of 4`,
  both pooled figures, the decision and the `ungated` class set.
  Red when: a record one arm did not answer is pooled.
  cost: about 8 review runs, roughly 100 agents.
- **AC4** — When the decision lands, unit 25 AC6's observation holds at this unit's commit against the
  decision this unit's verdict record states. When `selected` holds, `grep -c -- "--all-ungated"
  tools/memory-tree/gotchas.py` prints 0. When `ungated` wins, `gotchas.py --for-diff <range>
  --all-ungated` over a fixture catalogue prints the range's selection first, then every class naming
  no manifest leg, and the acquiring command carries the flag.
  Red when: the product changes against the decision.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `gotchas selftest` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py (its selftest, only on an `ungated` win) · covers AC4 · spec 15's planted class record naming a manifest leg, which the flag must omit, staged against `gotchas.py` at this unit's parent · none

## 8. Open questions

- **F1 — Does unit 25 still run unit 15's replay at order 20?** Options: (a) it runs it as written,
  and this unit re-runs it in isolated clones and reverses any verdict that moves; (b) unit 25 hands
  the replay to this unit, each superseded criterion named in its hands-off bullet, and the runs
  happen once, here. (a) spends about 100 agents on a comparison already found contaminable and can
  land spec 15 S6 only to take it out again. (b) closes the finding with one run per arm and leaves
  unit 25 replay 1. RESOLVED (agent, 2026-10-23, delegated): (b), rung 3, unit 25 §8 F1's form.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 28 (item H2, HIGH) of the round-3 spec
  audit of specs 4, 14, 25, 26 and 27.
- rev-2 · 2026-10-23 · §3 · the round-4 spec audit's disposal: hands-off edges to TOOL-dFairHearing-35 (the attempt rule,
  the scoring and the decision, finding id 32) and TOOL-dFairHearing-37 (seven minors).
- rev-3 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (four minors that read the verdict record).

## 10. Reuse audit

No new mechanism: the clone block is unit 25 §4's, the recipe is unit 23's in
`tools/workflows/README.md`, and the scorer is unit 14's `check_experiment`. `python
tools/codebase-map/reuse_lookup.py "give each comparative review run its own clean working tree"`
ranked the generic `tree`, `run`, `run_arms` and `run_git` stems, none a per-run clone. The
report-path seam was read at `tools/workflows/tier2-review.template.js:297` (the `reviewDir`
default) and `:1749` (the report written under `${repo}/${reviewDir}`). The recall query returned
the audit's H2 item, spec 15's brief row for the replay and `TOOL-aEvidencedLens-10`, the replay
scorer's origin, and no prior per-arm isolation rule. §8 F1 follows unit 25 §8 F1's hand-off form,
read from that spec.

Recall terms used: `python tools/memory-recall/query.py "two arms of a comparative replay share one clone so the second reads the first report" --terms "replay arm clone isolation reviewDir report working tree selected ungated porcelain fresh attempt contamination"`
