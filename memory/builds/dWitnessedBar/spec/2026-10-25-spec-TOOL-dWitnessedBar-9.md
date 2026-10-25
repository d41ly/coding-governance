# TOOL-dWitnessedBar-9 — the product-test contract: `level` on legs, the three `tests.*` keys, and runner adapters

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 16 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0347@934d7dcb whole
**Carries:** node:policy-key.tests.product
**Carries:** node:policy-key.tests.landing-levels
**Carries:** node:policy-key.tests.without-cadence

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter gets no product-test contract: no test levels, no selection by level, no runner, and its
manifest starts empty (gap-test-03). The owner chose to ship runners too (walk T4, "Also ship test
runners"). This unit gives a leg a declared test `level`, owns the three `tests.*` policy keys, and
ships the first runner adapter, the guardrails kit's pytest pack, rendered into a repository's
manifest only as `tests.product` says, each of its three values seen on a planted repository.

## 2. Scope (IN)

- **S1** — The row key. `level`, one of `unit`, `integration`, `e2e` or `performance` (the levels
  `tests.landing-levels` names, v2:1277), added once to the extracted known-key constant `LEG_KEYS` and given its
  `LEG_KEY_FLOORS` row (I1, unit 12). A leg carrying `level` is a product-test leg. Observed by AC5.
- **S2** — The contract. `tools/run-gates/product_tests.py`, its `derive_product_rows(repo, value)`
  yielding a repository's product-test rows under each `tests.product` value as §4 "The three values"
  states, and its `check` verb grading the manifest against them. Observed by AC1, AC2 and AC3.
- **S3** — The runner adapter. A `[[test_runner]]` table in
  `tools/pytest-parallel-guardrails/kit.toml`, one row per runner, holding its `detect` argv and one
  argv per level, and `tools/pytest-parallel-guardrails/run_level.py <level>`, which runs pytest with
  the kit's crash probe armed at that marker. Observed by AC3 and AC4.
- **S4** — The render. The leg factory `tools/run-gates/leg_factory.py` (I3, unit 11) adds each
  repository's adapter rows from `derive_product_rows` when it renders that repository's manifest, each
  row carrying `level`, `pack` `product-tests` and a tag `leg.<runner>.<level>` (I2). Observed by AC3.
- **S5** — The leg. A `[[gate_leg]]` `product-test contract (tests.product)` in
  `tools/run-gates/kit.toml`, argv `product_tests.py check`; gov's own argv, under the row's
  `[gate_leg.gov]` sub-table (TOOL-dWitnessedBar-11 S1), adds `--fixture`, so gov, which holds no
  product suite, runs the planted cases. Observed by AC1, AC2 and AC3.
- **S6** — The three keys. `tests.product`, `tests.landing-levels` and `tests.without-cadence` are rows
  of dGroundRules' catalogue `tools/policy/catalogue.toml` (TOOL-dGroundRules-1 S3), read through
  `policy.py get` (TOOL-dGroundRules-2) with the catalogue default where the reader cannot run
  (TOOL-dGroundRules-3); this unit fills each row's `summary` and `usage` and drains them from
  `tools/policy/unsummarised-keys.txt` with `policy.py lists --write`, adding no row. Observed by AC6.
- **S7** — The kit pages. `tools/run-gates/README.md` states the contract and the `level` key;
  `tools/pytest-parallel-guardrails/README.md` states the adapter and how a suite marks its levels.
  NOT OBSERVED — prose, read by the closing review.

## 3. Non-goals (OUT)

- Selecting legs by level at landing, and what `tests.without-cadence` does to the slower levels:
  `test.select`, unit 5's, which reads both keys (flow-steps.md:357).
- Flake handling of a product-test leg: units 8 and 30's.
- A second runner (a JavaScript or PowerShell adapter): v2's `[planned]`; the `[[test_runner]]` table
  takes one when it lands.
- Levels on gov's own legs: gov's kit self-tests are held by `verdict.held`, and giving them a level
  would put them in `test.select`'s landing set against the owner's T2 answer.
- The adopter's overlay legs and the emitter path for them: unit 28's.
- pytest itself: an adopter that runs the adapter carries pytest and its plugins, as the kit's snippet
  states today.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-11` — `leg_factory.py`, which renders the adapter rows this unit derives into a repository's manifest
- **hands-off** `TOOL-dWitnessedBar-5` — `tests.landing-levels`, and beside it `tests.without-cadence`, the two keys `test.select` reads to choose a landing's product-test levels from the rows carrying `level`
- **consumes-from** external — dGroundRules' catalogue rows, `policy.py get` and `lists --write` (TOOL-dGroundRules-1, -2, -3); unit 12's known-key constant `LEG_KEYS` and `LEG_KEY_FLOORS` (I1)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 7, 9, 11, 16 and 46: the contract leg's `enforces`, the `LEG_KEYS` observation, the flagged `New arm:` line, the adapter rows' tags, and the contract read where unit 28 has not routed a target, each a scope item of that unit
- **hands-off** `TOOL-dWitnessedBar-57` — the `product-tests` legs, whose count unit 51's AC35 must find above 0 under the resolver and ledger minors batch (id 38)

## 4. Design

### The three values

| `tests.product` | Product-test rows a repository's manifest may hold | `check` red when |
|---|---|---|
| `none` | none | any manifest row carries `level` |
| `declared` | the repository's own rows carrying `level`; no adapter row is rendered | a row's `level` is outside the four, or no row carries `level` and the repository declares a runner `detect` would find |
| `declared-with-runners` (default, v2:1276) | the repository's own rows plus one adapter row per level each detected runner declares | a row's `level` is outside the four, or a detected runner's rows are missing from the manifest |

Under every value `check` prints the value it read, where it read it (`policy.py get` or the catalogue
default with its reason), and each product-test row with its level. A repository that declares no
product test and holds no runner prints `0 product-test legs declared` and exits 0: the contract is
satisfied by a repository with nothing to test, and the zero is printed, never implied (§8 F2).

### The adapter

```toml
# tools/pytest-parallel-guardrails/kit.toml
[[test_runner]]
runner = "pytest"
detect = ["python3", "{kit}/run_level.py", "--detect"]
levels = ["unit", "integration", "e2e", "performance"]
argv = ["python3", "{kit}/run_level.py", "{level}"]
```

`run_level.py --detect` exits 0 when a tracked `pyproject.toml` carries `[tool.pytest.ini_options]`
declaring the marker of at least one level, the probe the kit's `[[hole]]` `pytest-ini-knobs` already
runs, and names each declared level. `run_level.py <level>` puts the kit directory on the import path
and runs `pytest -p crashprobe -m <level>`, so the guardrails ride every adapter run (the kit README's
"Arm the probe" step). A level whose marker the suite does not declare yields no row.

### Gov's own row

Gov tracks no `pyproject.toml` with a pytest table, so `detect` fails there and gov renders no adapter
row; gov's `check` would print its zero. Gov's row therefore runs `product_tests.py check --fixture`,
which plants one scratch repository per case of §6 and prints `case <name>: red|green`, declared under
the row's `[gate_leg.gov]` sub-table, the posture gov's `shell hygiene` rows take when they pass gov's
own registry (`tools/gate-lint/kit.toml:68-75`).

### Inventory

Minted: the row key `level` and its four values; `tools/run-gates/product_tests.py` with
`derive_product_rows`, `check` and `--fixture`; the `[[test_runner]]` table with `runner`, `detect`,
`levels` and `argv`; `run_level.py` with `--detect`; the pack word `product-tests`; the leg
`product-test contract (tests.product)`. Naming cells: each is asked of `python
tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

Additive. No manifest row carries `level` at base, so `check` reads every existing repository green
under any value; an adopter with a pytest suite gains adapter rows at the first render after it lands.

### Rollout

Live at landing; the adopter's rows reach it when its manifest is next rendered.

### Files touched (estimate)

- `tools/run-gates/product_tests.py`
- `tools/run-gates/leg_factory.py`
- `tools/run-gates/kit.toml`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `tools/pytest-parallel-guardrails/kit.toml`
- `tools/pytest-parallel-guardrails/run_level.py`
- `tools/pytest-parallel-guardrails/README.md`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `tools/govkit/govkit.py`
- `tools/gate-legs.json` (rendered by the leg factory, never edited)

### Alternatives rejected

- **Adapter rows as `[[gate_leg]]` rows.** The deployer emits every `[[gate_leg]]` to every adopter
  today, before unit 28 routes adopters through the factory, so an adapter row would reach a
  repository whose `tests.product` refuses it.
- **Levels on gov's self-tests**: §3.

## 5. Production-readiness checklist

- security — no new write path; the adapter runs the adopter's own suite with argv the kit declares.
- perf / scale — `detect` reads tracked `pyproject.toml` files once per render.
- error / empty / loading states — a repository with no product test prints its zero (§8 F2); a policy
  reader that cannot run prints the catalogue default and its reason.
- observability — `check` prints the value, its source and every product-test row.
- risks — an adopter whose suite declares a level marker gains a leg at its next render; its ceiling
  comes from the adapter row, sized by the kit's snippet guidance.
- testing — the `--fixture` cases of §6; the suite arm in §7 is observed RED then GREEN by the main loop
  at the close.
- migration — additive, as §4 Migration says.
- user docs — the two kit READMEs (S7); no page under `help/` covers the runner.

## 6. Acceptance criteria

- **AC1** — When `python product_tests.py check --fixture none-with-level` runs, its planted repository
  holding `tests.product = "none"` and a manifest row carrying `level = "unit"`, it prints
  `case none-with-level: red` naming the row; with the row's `level` removed it prints `green`.
  Red when: `none` lets a product-test row stand.
- **AC2** — When `python product_tests.py check --fixture declared` runs, its planted repository holding
  `tests.product = "declared"`, a pytest table declaring the `unit` marker and no row carrying `level`,
  the rendered manifest holds no adapter row and the case prints `red` naming the undeclared level; with
  a row `level = "unit"` declared it prints `green`, and with `level = "smoke"` it prints `red`.
  Red when: `declared` renders the adapter, or accepts a level outside the four.
- **AC3** — When `python product_tests.py check --fixture declared-with-runners` runs over the same
  planted repository under `tests.product = "declared-with-runners"`, the rendered manifest holds the
  row `leg.pytest.unit` with `level` `unit` and `pack` `product-tests`, and the case prints `green`;
  with the pytest table removed it renders no adapter row.
  Red when: the adapter renders with no runner detected, or the default value renders nothing.
- **AC4** — When `python run_level.py --detect` runs under `tools/pytest-parallel-guardrails/` in a
  scratch repository whose `pyproject.toml` declares markers `unit` and `e2e`, it exits 0 printing
  `unit` and `e2e`; on gov's tree it exits 1.
  Red when: detection ignores the marker set, so a level the suite never declares gains a row.
- **AC5** — When `grep -n '"level"' run-gates.test.sh` runs under `tools/run-gates/`, the key appears in
  the one known-key constant `LEG_KEYS`, and `grep -n '"level"' govkit.py` under `tools/govkit/` names its
  `LEG_KEY_FLOORS` row.
  Red when: the canary refuses a row carrying `level`.
- **AC6** — When `python policy.py get tests.product` runs on the built tree, it prints
  `declared-with-runners`; and `grep -cE '^tests\.(product|landing-levels|without-cadence)$'
  unsummarised-keys.txt` under `tools/policy/` prints 0.
  Red when: a row keeps an empty `summary` or `usage`, so it stays on the shrink-only list.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `pytest-guardrails self-test` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene`

The `product-test contract (tests.product)` leg and dGroundRules' `policy check` leg are not in the
manifest at this spec's base, so they are named in prose; the guards join's broad `tools/` and
`tools/run-gates/` guards are excluded by the checker's floor.

New arm: tools/run-gates/product_tests.py --fixture · covers AC1 AC2 AC3 · each case plants its repository and its `tests.product` value; the failing case is staged by planting the row the value forbids · none

## 8. Open questions

- **F1 — Where is an adapter declared, when a `[[gate_leg]]` reaches every adopter?** Options: (a) a
  `[[test_runner]]` table the factory expands per repository by `tests.product` and `detect`; (b) one
  `[[gate_leg]]` per level in the guardrails descriptor; (c) a leg row an adopter copies by hand. (b)
  ships rows to repositories whose value is `none` or `declared` until unit 28's emitter route lands;
  (c) is the hand-added row gap-test-21 names. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  only option under which each value renders differently on one repository. widens: none · relaxes:
  none
- **F2 — Under `declared` or `declared-with-runners`, is a repository with no product test and no
  runner red?** Options: (a) it prints `0 product-test legs declared` and exits 0; (b) it reds. (b) reds
  gov, whose product is its kits and holds no product suite, and every adopter that has not written a
  test yet, under the default; the zero is printed so it is never read as coverage, and the planted
  cases of gov's own row are what is graded there. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3;
  `declared` still reds a repository whose detected runner declares a level it does not carry, AC2.
  widens: none · relaxes: none
- **FACT-QUESTION · F3 — Does dGroundRules' catalogue already hold the three `tests.*` rows?** Probe:
  TOOL-dGroundRules-1 S3, "one `[[key]]` table per row of v2's `[policies]` table", over v2:1269 and
  v2:1276-1277. Observation, 2026-10-25: all three are `[policies]` rows naming dWitnessedBar, so S3
  lands them, unsummarised, as TOOL-dSafePassage-11 S11 found for `platforms.provision`. Liveness: a key
  outside v2's table would be absent from the catalogue. RESOLVED (agent, 2026-10-25, delegated): this
  unit fills `summary` and `usage` and adds no row; the build run re-grounds on the landed catalogue.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 9 and Obligations rows v2:1269, :1276 and
  :1277, the brief's I1 to I3 and I18, scout B's row for cl-0347, and walk T4.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams extended are the leg factory and row keys of units 11 and 12, the guardrails kit
`tools/pytest-parallel-guardrails/` whose crash probe and ini detection (`kit.toml`'s `[[hole]]`
`pytest-ini-knobs`) the adapter reuses, and dGroundRules' catalogue rows and reader. `python
tools/codebase-map/reuse_lookup.py "declare product test levels and run an adopter's test runner as
gate legs"` ranked generic stems (`run`, `legs`, `adopt`) and "no existing seam fits" the contract
itself: `git grep -n 'level\|tests\.product' -- tools/gate-legs.json tools/run-gates/run-gates.sh`
finds no level or product-test field at `cdfbd1cf`, as scout B measured. The recall probe returned
scout B's row, the brief's rows for units 9 and 5, and the guardrails kit's founding spec
TOOL-bTamedTempest-1; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "what is the product-test contract for adopters with runner adapters and test levels" --terms "tests.product declared-with-runners runner adapter level unit integration e2e pytest guardrails landing-levels without-cadence"`
