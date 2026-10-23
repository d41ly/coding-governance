# TOOL-dFairHearing-35 — unit 15's replay scored by one attempt rule fixed before the runs, so no figure rests on the attempt a runner prefers

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 22 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-35-deviation-351.md](../build/2026-10-23-build-TOOL-dFairHearing-35-deviation-351.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |
| [2026-10-23-prompt-TOOL-dFairHearing-35-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-35-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md) | spec-audit | TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit's finding id 32 (item H2, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) is
closed. `TOOL-dFairHearing-30` S3 allows a re-run of any record and arm for any cause, S5 records every
attempt, and nothing says which completed attempt is scored. The decision that lands spec 15 S6 can
therefore rest on whichever attempt the runner prefers. The cap and the dead-run rule sit in
`TOOL-dFairHearing-32` S20 and S21, two orders after the runs they govern. This unit takes the scoring
and the decision from unit 30 and scores by one rule written now, before any run: refused attempts
count for nothing, the first completed attempt that is not void is scored, only the first two
completed attempts are eligible, and a record and arm with no eligible attempt ends the replay with no
decision. The choice of attempt then depends on attempt numbers and void reasons alone, never on a
figure.

## 2. Scope (IN)

- **S1** — The attempt rule, for each record and arm of unit 15's replay. An attempt refused before
  its harness call, by unit 30 S2's status check, unit 25 §4's stale-name refusal or its exact-commit
  check, is listed with its reason and counts toward nothing. A completed attempt is one whose harness
  call returned a report. Of the completed attempts in attempt order, only the first two are eligible.
  The scored attempt is the first eligible one that is not void under spec 1 §4's void rule, as unit
  25 S3 reads it. A record and arm whose two eligible attempts are both void, or that has none, is
  `void after cap`. Every other completed attempt is `unscored` and no figure reads it. Observed by
  AC1 and AC2.
- **S2** — The rule is applied by a checker, `attempts.py` (§4), over a table of attempts that this
  unit writes from unit 30's verdict record: record, arm, attempt number, clone, outcome and void
  reason. The checker derives the scored attempt; the pass never picks one. Observed by AC1 and AC2.
- **S3** — Scoring and the decision, moved here from unit 30. The replay manifest, in unit 23 S4's
  terms (`candidates` entries `{case, report, matched}`, `dispatched` 4 per arm), names for each record
  and arm the report of the attempt the checker scored. `tools/workflows/replay_scorer.py --experiment`
  checks it. Pairing, the pooled figures and the decision are unit 25 S4's and S5's unit-15 half, read
  as unit 30 S4 states them, and spec 15 S6 lands only when `ungated`'s pooled recall is above
  `selected`'s. Observed by AC3 and AC4.
- **S4** — A void record ends the replay. When the checker names any `void after cap`, no pooled
  figure is computed, the record states `no decision` beside the void record and arm, and no product
  file of spec 15 S6 changes. Observed by AC4.
- **S5** — The record. Unit 30's verdict record,
  `memory/builds/dFairHearing/build/<date>-build-TOOL-dFairHearing-30-replay-verdict.md`, gains a
  `## Scoring` section written by this unit: the attempts table, the checker's output, the manifest's
  path, each record's recall under both arms, `paired 4 of 4`, both pooled figures, the decision and the
  class set the `ungated` arm carried. Its `**Serves:**` line gains `TOOL-dFairHearing-35`. Observed by
  AC1 and AC3.
- **S6** — Supersession. Unit 30's S4, the figure and decision half of its S5 and AC3, and its AC4's
  `ungated` half, are answered by this unit's S3 to S5 and AC3 to AC4. Spec 15 S6's product files and
  unit 30's `New arm:` line for the selftest of `gotchas.py` move here with them. Unit 30's S3 still
  permits a re-run; S1 decides whether that re-run is read. Unit 30's acceptance ledger records them
  superseded here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by a criterion of this unit: it
  is a ledger entry in unit 30's record, read there.

## 3. Non-goals (OUT)

- No run and no re-run. The runs are unit 30's, at order 21; this unit reads what they left. The cost
  of a run past the second completed attempt is spent there and never read here.
- No new void cause. The void rule is spec 1 §4's, as unit 25 S3 reads it.
- No change to the corpus, the arms, the instrument or the decision rule. They are units 14 and 15's.
- No change to unit 32's S20, S21 or AC12: their unit-15 half reading this rule is finding id 2's item
  in `TOOL-dFairHearing-37`, and their replay-1 half stays unit 32's.
- The behavioural check of a `selected` verdict's flag is finding id 5's item in
  `TOOL-dFairHearing-37`, not this unit's.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-30` — every attempt's clone, outcome, report and void reason in its verdict record; without them there is nothing to score
- **consumes-from** `TOOL-dFairHearing-15` — the corpus, the two arms, the instrument, the decision rule and S6's product change, which this unit lands or leaves
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment` and the manifest's `parsed` lines, which AC3 reads literally
- **hands-off** `TOOL-dFairHearing-37` — finding ids 2 and 33 of the same audit: unit 32's S20, S21 and AC12 and unit 30's AC1 read this unit's scored attempt instead of a fixed attempt number or an after-the-fact cap
- **hands-off** `TOOL-dFairHearing-38` — finding id 1 (item H1, shared with id 11) of the round-5 spec audit: the record's `selected` or `ungated` decision, which decides whether that unit's AC1 and AC2 apply
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors on this spec, ids 4, 6, 9, 13, 14, 21, 24, 25 and 35: the checker's `failed` outcome, its refusal of an unplaceable or empty row, the void column re-derived (the reports the manifest names stay on disk until that unit's pass), AC3 conditional on the checker's exit 3, S5's `**Serves:**` line observed, and the prose carriers checked on an `ungated` decision; the checker of §4 is superseded by its §4, re-run over unit 30's record there (its S6 to S10, S16, S21, S24 and S25)


## 4. Design

### Why a scoring rule and not a run rule

Unit 30's runs happen at order 21 and this unit sits at order 22. A rule that a run must obey, placed
after the run, is the defect id 32 names. A scoring rule placed after the runs is not: it decides only
which attempt is read, and it is written before any run happens, so a runner knows at order 21 that a
re-run of an attempt that was not void is never read. What the rule removes is the choice; what it
does not bound is the agents a needless re-run spends.

### The checker

```python
# attempts.py <record> — unit 15's replay: the scored attempt of each record and arm, by rule
import re, sys
rows, seen = {}, set()
for line in open(sys.argv[1], encoding="utf-8"):
    m = re.match(r"^\|\s*([1-4])\s*\|\s*(selected|ungated)\s*\|\s*(\d+)\s*\|\s*(\S+)\s*\|\s*(refused|completed)\s*\|\s*(.*?)\s*\|\s*$", line)
    if not m:
        continue
    r, a, n, clone, outcome, void = m.groups()
    if (r, a, int(n)) in seen:
        sys.exit(f"attempts: attempt {n} of record {r} {a} is listed twice")
    seen.add((r, a, int(n)))
    rows.setdefault((r, a), []).append((int(n), clone, outcome, void))
pairs = [(r, a) for r in "1234" for a in ("selected", "ungated")]
if sorted(rows) != sorted(pairs):
    sys.exit(f"attempts: {len(rows)} of the 8 record and arm pairs are listed")
capped = []
for key in pairs:
    tries = sorted(rows[key])
    if [t[0] for t in tries] != list(range(1, len(tries) + 1)):
        sys.exit(f"attempts: record {key[0]} {key[1]} does not number its attempts from 1")
    done = [t for t in tries if t[2] == "completed"]
    scored = next((t for t in done[:2] if t[3] == "-"), None)
    if scored:
        print(f"scored {key[0]} {key[1]} {scored[0]} {scored[1]}")
    else:
        capped.append(key)
        print(f"void after cap {key[0]} {key[1]}")
    for t in done:
        if t is not scored and not (t in done[:2] and t[3] != "-"):
            print(f"unscored {key[0]} {key[1]} {t[0]}")
sys.exit(3 if capped else 0)
```

The table rows are `| <record 1-4> | <arm> | <attempt> | <clone> | refused or completed | <void reason
or -> |`. For a refused attempt the last column holds the refusal's reason. The pass writes the
checker with its file-writing tool under its scratch directory. Measured on 2026-10-23 over a scratch
table: a record whose attempts read refused, void, completed and completed scored attempt 3 and listed
4 `unscored`; with attempt 3 void as well it printed `void after cap` and exited 3.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/README.md`
- `memory/builds/dFairHearing/build/`

`gotchas.py`, the harness template and its render change only when `ungated` wins, as spec 15 S6
states. The README's switch paragraph states the default the decision leaves. Under the build folder,
the manifest and unit 30's verdict record change.

### Alternatives rejected

- **Score the last non-void attempt, as the finding's fix words it.** The runner then still chooses,
  by deciding whether to run once more. The first eligible non-void attempt is fixed by the time it
  completes.
- **Cap the runs inside unit 30.** That edits a spec the audit reviewed, which M4 refuses, and a run
  rule placed after the runs is the defect itself.

## 5. Production-readiness checklist

- security — N/A: a read-only checker over a record, and the product change spec 15 S6 already priced.
- perf / scale — one table of at most a few dozen rows; one `--experiment` run.
- error / empty / loading states — a duplicate attempt, a missing record and arm pair or a gap in the
  attempt numbers exits 1 naming it, so a partial table cannot be scored.
- observability — the checker prints every scored, unscored and void-after-cap line, and the record
  keeps them beside the figures.
- risks — a runner re-runs past the second completed attempt; the run costs agents and changes nothing.
- testing — AC1 to AC4; on an `ungated` win, spec 15's `New arm:` line for the selftest of
  `gotchas.py` applies, and the close observes it.
- migration — none for adopters. A flag landing changes what the harness acquires, and the README
  names it.
- user docs — `tools/workflows/README.md`'s switch paragraph; no `help/` page.

## 6. Acceptance criteria

`attempts.py` is the checker of §4, written under the pass's scratch directory.

- **AC1** — When `python attempts.py <unit 30's verdict record>` runs at this unit's commit, it prints
  one `scored` or `void after cap` line for each of the 8 record and arm pairs, and the record's
  `## Scoring` section quotes that output. Each `candidates` entry of the committed manifest names the
  report of the clone its `scored` line names.
  Red when: a manifest entry names the report of an attempt the checker did not score.
- **AC2** — When `attempts.py` runs over a scratch table whose record 4 `selected` attempts read
  refused, completed void, completed and completed, it prints `scored 4 selected 3` and `unscored 4
  selected 4`. With attempt 3 void too it prints `void after cap 4 selected` and exits 3. A table
  listing attempt 2 twice exits 1 naming it.
  Red when: the checker scores attempt 4, counts the refused attempt as eligible, or scores past two
  completed attempts.
  fixture: the table under the pass's scratch directory, written by the probe.
- **AC3** — When `replay_scorer.py --experiment` runs over this unit's committed manifest, it prints
  `arm ungated: varies checklist from selected`, then `parsed selected: 4 of 4` and `parsed ungated: 4 of
  4` before any figure. The record names each record's recall under both arms, `paired 4 of 4`, both
  pooled figures, the decision and the `ungated` class set.
  Red when: a record one arm did not answer is pooled.
- **AC4** — When the decision lands, `git diff <this unit's parent> HEAD -- tools/memory-tree/gotchas.py tools/workflows/tier2-review.template.js`
  prints nothing unless the record states `ungated` wins. When it states that, `gotchas.py --for-diff
  <range> --all-ungated` over a fixture catalogue prints the range's selection first, then every class
  naming no manifest leg, and the acquiring command carries the flag. When the checker exited 3, the
  record states `no decision` and the same diff prints nothing.
  Red when: the product changes against the decision, or a void record is decided.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `gotchas selftest` · `workflow script syntax` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py (its selftest, only on an `ungated` win) · covers AC4 · spec 15's planted class record naming a manifest leg, which the flag must omit, staged against `gotchas.py` at this unit's parent · none

## 8. Open questions

- **F1 — Which completed attempt is scored?** Options: (a) the last non-void one, as the finding's fix
  words it; (b) the first eligible non-void one, the first two completed attempts eligible. (a) leaves
  the runner a choice through whether to run again. (b) fixes the scored attempt when it completes.
  RESOLVED (agent, 2026-10-23, delegated): (b), rung 3; it satisfies every criterion (a) does and
  closes the choice (a) leaves. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 32 (item H2, HIGH) of the round-4 spec
  audit of specs 28 to 32.
- rev-2 · 2026-10-23 · §3 · the round-5 spec audit's disposal: hands-off edges to TOOL-dFairHearing-38 (the decision it reads, item H1) and
  TOOL-dFairHearing-40 (nine minors).

## 10. Reuse audit

No new scoring mechanism: the manifest and `--experiment` are unit 14's `check_experiment` in unit
12's factory, the void rule is spec 1 §4's and the decision is unit 25's. `python
tools/codebase-map/reuse_lookup.py "choose which attempt of a re-run review is scored"` ranked the
generic `run` and `run_arms` stems and `score` in `tools/memory-recall/bench.py`, a recall bench's
scorer, and no attempt-selection function; no existing seam fits a rule over attempt numbers, so the
checker is a scratch script of one table read. The recall query returned `TOOL-aSightedSkeptic-9`,
the replay benchmark's origin, the audit's H2 item and unit 32's criteria, whose after-the-fact cap
this unit's rule answers for unit 15's replay.

Recall terms used: `python tools/memory-recall/query.py "which attempt of a re-run replay arm is scored when several complete" --terms "replay attempt cap scored attempt void re-run selection bias unscored ungated selected decision"`
