# TOOL-dCalibratedLens-36 — the eval seed's `**Loads:**` stated, every edit to them since its replay listed, and its `held` read only after the main loop's replay

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 14 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-36-deviation-361.md](../build/2026-11-02-build-TOOL-dCalibratedLens-36-deviation-361.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 6, HIGH, item H3 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 23 §4 counts only the
guard-path edits made after unit 10 lands, but unit 10's owed rule diffs a case's `**Loads:**` from
the seed's replayed sha, TOOL-dFairHearing-25's replay, which predates this build. Unit 5 (order 11)
edits `coding-governance-agents.template.md` and `tools/workflows/tier2-review.template.js` before
unit 10 lands, and unit 10 S5 never states the seed's `**Loads:**`, so whether unit 23 AC2 reads
`held` at its order cannot be decided from the text and plausibly reds on a correct build. This unit
states the seed's loads, lists every edit to them since the replay, moves the `held` observation to
after the replay the main loop records, and proves the owed rule on the seed's own loads. It repairs
`TOOL-dCalibratedLens-23`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text. Unit 10 S5
  (rev-3, r2 id 6): the seed case's `**Loads:**` line is `tools/workflows/tier2-review.template.js,
  tools/workflows/lenses.toml, tools/roles/agents/gov-spec-reviewer.agent.md,
  tools/roles/agents/gov-skeptic.agent.md, tools/roles/agents/gov-synthesizer.agent.md,
  coding-governance-agents.template.md`, the files a design audit's agents load, each inside unit
  10's guard. Unit 23 (rev-2, id 6): §4 lists every edit to those loads after the replayed sha that
  this build makes, units 5 and 1, and the guard-path edits outside them that owe the seed nothing,
  units 8 and 25; and AC2 reads `held` only after the main loop records the one replay, never at
  unit 23's order. Observed by AC1.
- **S2** — The proof, a `--fixture` plant `seed-loads` of `replay_scorer.py --instance
  instruction-eval` in `tools/workflows/replay_scorer.py`. In a scratch repository it copies the
  shipped seed case, rewrites in place only the sha of its `**Replayed:**` line to the scratch
  repository's first commit, and commits a copy of each path the seed loads. It then commits an edit
  to `tools/hooks/format-guard.test.sh`, a guard path the seed does not load, and runs
  `check_eval_suite`: the seed reads `held`. It then commits an edit to
  `coding-governance-agents.template.md`: the seed reads `owed`, the detail naming that path and no
  other. The plant prints `seed-loads — ok` when both verdicts hold and a `seed-loads — FAIL` line
  naming the verdict it read otherwise. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Running a replay in the plant or in a pass: unit 10 §3, unchanged.
- The rule for when the main loop's replay is recorded and re-checked: id 36, `TOOL-dCalibratedLens-41`,
  which restates unit 23 S1 as a rule over the last commit touching a loaded path.
- Per-unit pins on a loaded file: unit 10 §4 "The guard" names them as the upgrade.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-10` — `check_eval_suite`, the seed case and the `--fixture` frame of `replay_scorer.py --instance instruction-eval`; without them there is no case to copy and no verdict to read

## 4. Design

### Evidence

- spec-10 S3: `owed` when `git diff --name-only <replayed sha> HEAD -- <the case's Loads>` names a
  path; spec-10 S5 states the seed's `**Known:**`, `**Expect:**`, `**Replayed:**` and `**Baseline:**`
  and no `**Loads:**`; spec-10 §4 "The case" lists `**Loads:**` as the files the item's agents and its
  review's agents load.
- The round-2 audit's Roles line: a spec audit's finders are `gov-spec-reviewer`, its skeptic
  batches `gov-skeptic` and its synthesis `gov-synthesizer`; each has a file under
  `tools/roles/agents/` at base.
- Edits to the seed's loads in this build, read from each spec's Files touched: unit 5 (order 11)
  `coding-governance-agents.template.md` and `tools/workflows/tier2-review.template.js`; unit 1
  (order 16) `tools/workflows/tier2-review.template.js` and `tools/workflows/lenses.toml`. Guard-path
  edits outside the loads: unit 5's `instructions.toml`, `unattended-build.template.js` and
  `unattended-unit.js`, unit 8's `unattended-build.template.js`, unit 25's
  `tools/hooks/format-guard.test.sh`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `seed-loads` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/workflows/replay_scorer.py` — S2, the plant

### Alternatives rejected

- **Loads naming the whole guard.** Every guard-path edit would owe the seed, units 8 and 25 included,
  and a replay costing about 0.81 M tokens would be owed by edits no audit agent loads.
- **Keep AC2 at unit 23's order with the edits since unit 10.** The owed rule diffs from the replay
  sha, not from unit 10's landing, so unit 5's edits already owe the seed when unit 23 builds.

## 5. Production-readiness checklist

- security — no new surface; the plant writes under its scratch repository.
- perf / scale — two commits and two checks per plant run.
- error / empty / loading states — a seed with no `**Loads:**` line is refused by `parse_eval_case`
  by name (spec-10 S1).
- observability — the `owed` detail names the moved path.
- risks — a new audit agent added to the harness: its file joins the seed's loads in the pass that
  adds it.
- testing — AC1 and AC2 by the pass.
- migration — N/A: the suite is new in unit 10.
- user docs — N/A: unit 10 S8's README section names `**Loads:**`.

## 6. Acceptance criteria

- **AC1** — When `python replay_scorer.py --instance instruction-eval --fixture --plant seed-loads`
  runs from the workflows kit directory, it prints the seed `held` after the plant's first edit, to
  the format guard's suite, a guard path the seed does not load (S2), and `owed` naming
  `coding-governance-agents.template.md` after the second edit.
  Red when: an edit the seed does not load owes it, or an edit it loads leaves it held.
- **AC2** — When the plant runs with the copied case's `**Loads:**` line emptied in place, it prints
  a `seed-loads — FAIL` line: the second check read `held` where `owed` was expected, or
  `parse_eval_case` refused the case by name.
  Red when: a seed with no stated loads passes, so the verdict is undecidable again.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The leg `instruction-eval` is not in the manifest at base and is named here in prose.

New arm: tools/workflows/replay_scorer.py · covers AC1 AC2 · the `seed-loads` plant, staged red by the copied seed's `**Loads:**` line emptied in place · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 6 (HIGH, item H3) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; units 10 and 23 amended at the disposal
  (their rev-3 and rev-2).

## 10. Reuse audit

The seam extended is unit 10's own suite: `check_eval_suite`, its `owed` rule over a case's
`**Loads:**`, and the `--fixture` frame of `replay_scorer.py`, which unit 23's `close-bar` plant
already uses. `python tools/codebase-map/reuse_lookup.py "render an optional bracket group of a
shape definition into an emitted line"`, run once for this disposal's set, ranked name stems only;
`replay_scorer.py` is absent at base, so no code seam fits beyond the sibling specs. The recall probe
returned TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
