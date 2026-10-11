---
slug: dRemeasuredRender
node: d
opened: 2026-10-11
streams: tooling+deployer
roster: TOOL+DEPL
authorized-by: prompt
ids: DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 TOOL-dRemeasuredRender-1 TOOL-dRemeasuredRender-2
---

# dRemeasuredRender — gov's shipped suites scrub their probes, and `govkit update` reports what it rendered

## The problem this build exists to solve

The inCMS and NicoCares pull from gov `40a8b8c3` to `b726385f` exposed three gov defects. The
location-probe leg's adopter row grades gov's own shipped suites, which gov's row excludes, so every
adopter reds on 58 bare probes in 30 suites it may not edit. `govkit update` re-renders a `rendered`
row and never re-measures its receipt, so `install.sums` names bytes git no longer stores. And it
probes a `[[hole]]` before the render that discharges it, so it reports a false red. The prompt is
in `prompts/`.

## Expected improvements

- No adopter reds on gov's suites, and gov's own row grades the class it ships.
- A rendered row's receipt and `install.sums` name the bytes its render landed.
- A hole the render discharges is not reported undischarged by that same run.

## Detriments if this is not built

- Every adopter keeps a hand-kept list of gov's probe sites, which grows with each pull.
- Each pull leaves rendered sums stale, and nc re-records them by hand every time.
- Operators read a false hole red on every lexicon pull.

## Build-level rules

- The units are the owner's: one per defect, plus whatever discovery adds. The two govkit units
  both write `tools/govkit/govkit.py` and its self-test, so they are sequenced.
- Classified at kickoff (M2): all three MISSING; authored and built inline, in roster order.
- `TOOL-dRemeasuredRender-1` drops `:!*.test.sh` rather than shipping the exclusion, because the
  leg's header bans a spelling, not a population.
- Every new govkit arm is observed RED against BASE `9a8777b8` before its fix lands.
- The six touched `tools/unattended/` suites are NOT run, under the owner's standing instruction
  (2026-08-23; TOOL-dDerivedDocket-76). Each scrub there is verified by a parse check and a probe
  of the scrubbed line; the full run is handed to the owner at the close.
- No self-test suite and no bar inside a pass. The bar runs once, at the close.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dRemeasuredRender-1` | 2 | gov's shipped suites scrub every bare location probe, and gov's own row stops excluding them |
| 2 | `DEPL-dRemeasuredRender-1` | 2 | `update` re-measures a rendered row's receipt from the bytes its render landed |
| 3 | `DEPL-dRemeasuredRender-2` | 2 | `update` re-probes a hole after the render, and reports only the verdict that stands |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node d · opened 2026-10-11 · streams tooling+deployer
ids DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 TOOL-dRemeasuredRender-1 TOOL-dRemeasuredRender-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRemeasuredRender-1 — gov's shipped suites scrub every bare location probe, and gov's own row stops excluding them](spec/2026-10-11-spec-TOOL-dRemeasuredRender-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [DEPL-dRemeasuredRender-1 — `govkit update` re-measures a rendered row's receipt from the bytes its render landed](spec/2026-10-11-spec-DEPL-dRemeasuredRender-1.md) | 2 | 2 | SPECCED | rev-1 | 2026-10-11 |
| [DEPL-dRemeasuredRender-2 — `govkit update` re-probes a hole after the render, and reports only the verdict that stands](spec/2026-10-11-spec-DEPL-dRemeasuredRender-2.md) | 3 | 2 | SPECCED | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 TOOL-dRemeasuredRender-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRemeasuredRender-1` | no |
| 2 | `DEPL-dRemeasuredRender-1` | no |
| 3 | `DEPL-dRemeasuredRender-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
