# TOOL-aQuenchedHarness-3 — a self-test leg never reaches an adopter's manifest

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-5 |

<!-- /gen:spec-records -->

## 1. Goal

Stop shipping this repo's kit self-tests into adopter repositories. Thirty `[[gate_leg]]` rows across
the kit descriptors name a `*.test.sh`, a `test_*.py` or a `--selftest` verb, and `govkit`'s emit
copies them into a target's `gate-legs.json` — while `chunk`, half of the predicate that HOLDS them
here, reaches no descriptor and no emitted row. An adopter therefore runs suites that grade kit
source they never edit, on every bar.

## 2. Scope (IN)

- **S1** — a single DERIVED predicate, `is_selftest(leg)`, computed from the leg's own `argv`: a
  path component matching `*.test.sh` or `test_*.py` or `selftest.py`, or a `--selftest` argument.
  One function, one definition, used by both readers.
- **S2** — `tools/run-gates/run-gates.sh`'s hold reads that predicate in ADDITION to the existing
  `subject == kit || chunk == selftests`, so the hold widens and never narrows. A leg held today
  stays held.
- **S3** — `govkit`'s emit verb DROPS a leg the predicate selects, so an adopter's manifest never
  receives one. The drop is REPORTED per target, with the count and the names, because an emit that
  silently ships less is indistinguishable from an emit that failed.
- **S4** — a gate leg asserting the two directions: no leg `is_selftest` selects appears in an
  emitted manifest, and every leg the descriptors mark as a self-test is one the predicate selects.
  The second direction is what stops the predicate from quietly matching nothing.
- **S5** — the predicate is asserted against gov's OWN manifest too: every leg carrying
  `chunk = selftests` or `subject = kit` must be one the predicate selects, or the disagreement is
  named. Three answers to one question is worse than two, so the assertion is how the third stays
  joined rather than becoming a rival.
- **S6** — arms staging: a descriptor row naming a `.test.sh`, one naming `--selftest`, one naming
  neither, and an emitted manifest hand-edited to contain a self-test leg.

## 3. Non-goals (OUT)

- Not adding `chunk` to the descriptor schema. `TOOL-aScouredKit-27` records why that is a
  five-declaration act against a PINNED key set the `run-gates canary` asserts, and warns that
  half-building it is worse than the gap. This unit does not do it and does not half-do it.
- Not deleting the self-test FILES from what a kit copies. An adopter who edits a kit is entitled to
  its suites; what they are not entitled to is a bar leg they never asked for. The files ship, the
  legs do not.
- Not changing which legs run in THIS repo today. The hold widens; `GATE_SELFTESTS=1` is unchanged.
- Not the on-demand runner, which is `TOOL-aQuenchedHarness-4`.

## 4. Design

### Data model

No new key anywhere. That is the design decision and it is the one worth defending: charter §12 says
prefer runtime derivation over a committed artifact when the only consumer is same-language and
in-process, and both consumers here are. A derived predicate cannot drift from the thing it
describes, and it needs no pin, no ratchet and no migration.

The predicate lives beside the manifest reader that both consumers already share, so gov's runner and
`govkit` call one function rather than spelling the same regex twice.

### Rollout

Landing S3 alone would change what adopters receive on their next `govkit` emit. Nothing in an
adopter's tree breaks: a manifest with fewer rows is a valid manifest, and the legs removed are the
ones that grade files the adopter does not edit. The emit report names the drop so an adopter running
it sees what changed rather than discovering it from a shorter bar.

### Inventory

- `is_selftest` — the predicate; named for what it answers, in the shared manifest reader.
- `no self-test leg reaches an adopter` — the new gate leg's name in `tools/gate-legs.json`.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/run-gates/run-gates.sh` · `tools/gate-legs.json` ·
`tools/govkit/selftest.py` · `tools/run-gates/run-gates.test.sh`.

### Alternatives rejected

Emitting `chunk` into a target's manifest — the fix `TOOL-aScouredKit-27` scopes — was rejected on
that row's own warning: it needs a descriptor key, a schema change, a pinned-key-set change and a
canary change, and each of those is a place the join can be forgotten. A derivation needs none of
them and is checkable in both directions on the day it lands.

## 5. Production-readiness checklist

- security — an adopter receiving FEWER executable legs is a narrowing, not a widening. No new path
  executes anything new.
- perf / scale — one regex per leg at manifest-parse time.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a predicate that selects NOTHING is the hazard, and S4's second
  direction is what catches it. An emit that drops zero legs says so explicitly.
- observability — the emit report names every dropped leg per target.
- risks — a predicate too WIDE would hold a real repo check off an adopter's bar. Mitigated by S5:
  the predicate is asserted against gov's own manifest, where a leg it wrongly selects is a leg this
  repo would stop running and would notice.
- testing + left-shift gates — S6's arms, each observed RED before landing.
- migration / rollback — reverting the predicate call sites restores today's emit; no adopter state
  is written that would need undoing.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence saying adopters do not receive kit
  self-tests, and `tools/govkit/README.md` records the drop.

## 6. Acceptance criteria

- **AC1** — When `govkit` emits a manifest for a fixture target, no row in the result satisfies
  `is_selftest`, and the emit prints the names it dropped.
- **AC2** — When the `no self-test leg reaches an adopter` leg runs against a hand-edited emitted
  manifest containing `bash {kit}/foo.test.sh`, it reds.
- **AC3** — When a leg in `tools/gate-legs.json` carries `chunk: selftests` but its `argv` does not
  satisfy `is_selftest`, the same leg names the disagreement rather than passing.
- **AC4** — When the predicate is made vacuous, the arm in `tools/govkit/selftest.py` asserting the
  second direction reds, so a selector matching nothing cannot report clean.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs without `GATE_SELFTESTS`, the set of legs
  it holds is a superset of today's set, verified by comparing the run's own held report before and
  after.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `no self-test leg reaches an adopter` leg ·
`govkit selfcheck` and `govkit acceptance matrix`, both `subject = repo` and on every bar ·
`GATE_SELFTESTS=1` for `govkit selftest` and the `run-gates canary` at the Definition of Done.

## 8. Open questions

- **F1 — the owner's own either/or.** The prompt says self-checks must "NOT ship to the repo adopters
  (or ship strictly OPT-IN and do not execute on a full bar by default)". RESOLVED (agent,
  2026-09-06, delegated): take BOTH halves at their narrowest — the FILES ship, because an adopter
  who edits a kit needs them and deleting them would break the copy-install contract; the LEGS do
  not, so nothing executes on an adopter's bar by default or otherwise. That is the more
  feature-rich survivor under M3: it satisfies every stated criterion and leaves no follow-up open.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

No new mechanism: the seam is the shared manifest reader that `tools/run-gates/run-gates.sh` and
`tools/govkit/govkit.py` already both use, plus the hold predicate at the runner's `subjects`/`chunks`
comparison. `tools/codebase-map/reuse_lookup.py` returned `registry.toml` [govkit] and
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seams for this area, and
`check_target_reads_subject` in `tools/govkit/govkit.py` as the existing emit-side guard this unit
extends rather than duplicates. The prior record that scopes the gap is `TOOL-aScouredKit-27`, read
in full before writing, and its warning is why the descriptor-key route is a rejected alternative
rather than the design.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
