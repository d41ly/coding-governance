---
slug: dRedressedBar
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26 TOOL-dRedressedBar-27 TOOL-dRedressedBar-28
spec-audit: 2026-10-13
---

# dRedressedBar — every traced red of the full bar with self-tests at ebce889c7, fixed at its root

## The problem this build exists to solve

Local main at `ebce889c7` is two landings that met without a bar running the self-tests:
aOrientedCast's addenda and the reconcile of origin/main `2a9d8191`. The owner asked for the full
bar with every self-test, profiled, and every red it finds fixed. The run refused first on a stale
generated output, then, past that refusal, reported 16 of 140 legs red with the run-gates canary
still in its retry. Every red but the canary is traced to a cause, and all but push-main's two arms
are causes of their own.

## Expected improvements

- Each of the 16 legs red at `ebce889c7` reads `GATE ok` in one full bar with self-tests over the
  build tip, with the regen preflight fresh and no knob overriding it.
- Every stale suite fixture is re-armed against the code that moved, never waived.
- Local main can take a push whose forced full bar is green, canary aside.

## Detriments if this is not built

- Every push from local main forces a full bar that cannot pass.
- The next bar-less landing hides its own reds among sixteen inherited ones.
- Five suites grade nothing while reading red, so a real regression in their subjects goes unseen.

## Build-level rules

- **Classification (M2)**: seven units, MISSING at open, one mechanism each, authored by the build
  harness from the brief under `prompts/`.
- The run-gates canary is out of scope until its retry reports; a red there is added as a unit.
- `GATE_REGEN_CHECK` reaching the canary's nested runners is a separate finding and not this build's.
- Tiers per the manifest's tier rule: a unit moving a shipped engine's bytes is Tier-2, a stale
  fixture, a registry row, a pin or a regenerated output Tier-1.
- No `tools/unattended/` self-test suite runs: standing owner instruction, 2026-08-23.
- Owner rulings, 2026-10-13: confirm the four unconfirmed reds, then fix every traced red; spec
  audit declared; go.
- Every amendment that added a unit (8, 9, 11, 14, 15, 18, 20 to 28), the build-wide unit order and
  the owner's rulings from 2026-10-14 on are in
  `build/2026-10-16-build-TOOL-dRedressedBar-28-1-amendments.md`.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1` | stale suite fixtures re-armed against the code the bar-less landings moved |
| 2 | `TOOL-dRedressedBar-2` | the one verb offender over the lexicon pin, renamed |
| 3 | `TOOL-dRedressedBar-3` | the govkit selftest's reds, each at its root |
| 4 | `TOOL-dRedressedBar-4` | shipped-surface bans: the `workflows` homonyms install-prefix reads as a kit path |
| 5 | `TOOL-dRedressedBar-5` | fork idioms past the spawn-idiom registry, converted |
| 6 | `TOOL-dRedressedBar-6` | the adopt-roles exits the harness-arms leg finds unarmed, armed |
| 7 | `TOOL-dRedressedBar-7` | records, the regenerated index and the kit versions, measured over the fixed tree |
| 8 | `TOOL-dRedressedBar-8` | the canary's memory-pause arm 11g AC14 hangs when its FIFO server dies, bounded and its server kept alive |
| 9 | `TOOL-dRedressedBar-9` | govkit update's gained settings-merge no longer fails an update that left agent-cap out |
| 10 | `TOOL-dRedressedBar-10` | PROMOTED: the round-1 spec audit's 12 mediums and 11 lows, batched — report ids 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 and 23 |
| 11 | `TOOL-dRedressedBar-11` | a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route |
| 12 | `TOOL-dRedressedBar-12` | PROMOTED: the units-10-11 spec audit's one high, report id 23 — an apply narrower than its receipt keeps every other installed kit's claim and rows |
| 13 | `TOOL-dRedressedBar-13` | PROMOTED: the units-10-11 spec audit's 5 mediums and 18 lows, batched — report ids 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 and 24 |
| 14 | `TOOL-dRedressedBar-14` | a first apply at a per-kit prefix writes its receipt before CONFIGURE, so settings-merge finds the hook it just installed |
| 15 | `TOOL-dRedressedBar-15` | agent-cap's adopter resolves settings-merge at settings-merge's own home, not at agent-cap's prefix |
| 16 | `TOOL-dRedressedBar-16` | PROMOTED: the units-12-15 spec audit's one high, report id 7 — an apply that keeps a carried kit's claim keeps that kit's gate-leg ownership too |
| 17 | `TOOL-dRedressedBar-17` | PROMOTED: the units-12-15 spec audit's 12 mediums and 9 lows, batched — report ids 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23 and 24 |
| 18 | `TOOL-dRedressedBar-18` | a gate profiler: every leg run clean and unbounded, serially or under a load cap, each profiled to its processes, stalls reported and never killed |
| 19 | `TOOL-dRedressedBar-19` | PROMOTED: the units-16-18 spec audit's 19 mediums and 22 lows, batched — report ids 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42 and 43 |
| 20 | `TOOL-dRedressedBar-20` | govkit's mint writes a version only into its own entry's file group, never another kit's |
| 21 | `TOOL-dRedressedBar-21` | PROMOTED: the closing review's one high, finding H1 — the profiler's dead-run sweep trusts no path a shared temp dir supplies |
| 22 | `TOOL-dRedressedBar-22` | PROMOTED: the closing review's profiler findings M1, M2, M5, M7, L1, L2, L3 and L5, batched |
| 23 | `TOOL-dRedressedBar-23` | PROMOTED: the closing review's govkit findings M3, M4, M6 and L4, batched |
| 24 | `TOOL-dRedressedBar-24` | the runner scripts' fixed-name temp-then-replace writers take unpredictable temps, under a bash-side static check |
| 25 | `TOOL-dRedressedBar-25` | PROMOTED: the round-2 review's profiler arm and guard findings H1, M1, L1 and L6 |
| 26 | `TOOL-dRedressedBar-26` | PROMOTED: the round-2 review's temp-name lint and runner temp findings H2, M2, M3, M4, L2, L3, L4 and L5 |
| 27 | `TOOL-dRedressedBar-27` | hygiene check 23 green: this build's eight missing acceptance ledgers written, and the base's foreign ledger lines put in a legal form |
| 28 | `TOOL-dRedressedBar-28` | the landing bar's install-prefix red: the two kit-path spellings units 10, 11 and 14 wrote, respelled at their root |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 28 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13
ids TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26
ids TOOL-dRedressedBar-27 TOOL-dRedressedBar-28

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRedressedBar-1 — stale suite fixtures re-armed against the code the bar-less landings moved](spec/2026-10-14-spec-TOOL-dRedressedBar-1.md) | 1 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb](spec/2026-10-14-spec-TOOL-dRedressedBar-2.md) | 1 | 2 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-8 — arm 11g AC14 bounded, and its FIFO server kept alive through MSYS's failed opens and broken pipes](spec/2026-10-14-spec-TOOL-dRedressedBar-8.md) | 1 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-9 — settings-merge's adopter exit with no agent-cap hook declared an accepted stop, so a gaining update completes](spec/2026-10-14-spec-TOOL-dRedressedBar-9.md) | 1 | 2 | CLOSED | rev-7 | 2026-10-14 |
| [TOOL-dRedressedBar-3 — the govkit selftest's 56 reds, traced to four root causes and re-armed](spec/2026-10-14-spec-TOOL-dRedressedBar-3.md) | 2 | 1 | CLOSED | rev-4 | 2026-10-14 |
| [TOOL-dRedressedBar-4 — the `workflows` homonyms the install-prefix ban reads as a kit path, held in a named constant](spec/2026-10-14-spec-TOOL-dRedressedBar-4.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-5 — fork idioms past the spawn-idiom registry, converted to their no-fork forms](spec/2026-10-14-spec-TOOL-dRedressedBar-5.md) | 3 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-20 — govkit's carrier writer counts an entry's version pattern only inside that entry's own basis, so a mint never writes another kit's file](spec/2026-10-14-spec-TOOL-dRedressedBar-20.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-6 — the roles adopter's two exit-1 refusals, armed in its own suite](spec/2026-10-14-spec-TOOL-dRedressedBar-6.md) | 4 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-7 — records, the regenerated index and the kit versions, measured over the fixed tree](spec/2026-10-14-spec-TOOL-dRedressedBar-7.md) | 5 | 2 | CLOSED | rev-5 | 2026-10-14 |
| [TOOL-dRedressedBar-10 — the round-1 spec audit's 12 mediums and 11 lows, batched: each criterion observed in a form that can pass and fail, each false sentence corrected, and settings-merge's accepted stop narrowed](spec/2026-10-14-spec-TOOL-dRedressedBar-10.md) | 6 | 2 | CLOSED | rev-7 | 2026-10-16 |
| [TOOL-dRedressedBar-11 — a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route](spec/2026-10-14-spec-TOOL-dRedressedBar-11.md) | 7 | 2 | CLOSED | rev-7 | 2026-10-16 |
| [TOOL-dRedressedBar-12 — an apply narrower than its receipt keeps every other installed kit's claim and rows, so a refused settings-merge exit stays refused on the next run](spec/2026-10-14-spec-TOOL-dRedressedBar-12.md) | 8 | 2 | CLOSED | rev-9 | 2026-10-15 |
| [TOOL-dRedressedBar-13 — the units-10-11 spec audit's 5 mediums and 18 lows, batched: each criterion half observed in a form that can fail, each false sentence corrected, and the code sites they describe made to say what the specs claim](spec/2026-10-14-spec-TOOL-dRedressedBar-13.md) | 9 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-16 — an apply that keeps a carried kit's claim keeps that kit's gate-leg ownership too, so a later argv change does not wedge the kit](spec/2026-10-14-spec-TOOL-dRedressedBar-16.md) | 9 | 2 | CLOSED | rev-5 | 2026-10-15 |
| [TOOL-dRedressedBar-14 — a first apply at a per-kit prefix configures against the homes it just wrote: the receipt is written ahead of CONFIGURE](spec/2026-10-14-spec-TOOL-dRedressedBar-14.md) | 10 | 2 | CLOSED | rev-8 | 2026-10-15 |
| [TOOL-dRedressedBar-15 — agent-cap's adopter runs settings-merge's own adopter at settings-merge's home, declared as `[adopt] via`, and selfcheck refuses any argv naming another entry's file](spec/2026-10-14-spec-TOOL-dRedressedBar-15.md) | 11 | 2 | CLOSED | rev-7 | 2026-10-15 |
| [TOOL-dRedressedBar-17 — the units-12-15 spec audit's 12 mediums and 9 lows, batched: each faulted criterion observed in a form that can pass and fail, each false sentence corrected, and the code sites they describe made to hold what the specs claim](spec/2026-10-14-spec-TOOL-dRedressedBar-17.md) | 12 | 2 | CLOSED | rev-6 | 2026-10-15 |
| [TOOL-dRedressedBar-18 — a gate profiler: every leg run clean and unbounded, serially or under a load cap, each profiled to its processes, stalls reported and never killed](spec/2026-10-14-spec-TOOL-dRedressedBar-18.md) | 13 | 2 | CLOSED | rev-9 | 2026-10-16 |
| [TOOL-dRedressedBar-19 — the units-16-18 spec audit's 19 mediums and 22 lows, batched: the profiler's census, path, launch, turnstile, redaction and leg-declaration gaps closed, the receipt sidecar made atomic, and specs 12 and 14 to 18 corrected](spec/2026-10-14-spec-TOOL-dRedressedBar-19.md) | 14 | 2 | CLOSED | rev-8 | 2026-10-15 |
| [TOOL-dRedressedBar-21 — the profiler trusts no path a temp dir supplies: a dead run's logs land in this run's record, no capture is opened, read or deleted through a link, and run-gates' Python temp files take unpredictable names](spec/2026-10-15-spec-TOOL-dRedressedBar-21.md) | 15 | 2 | CLOSED | rev-3 | 2026-10-15 |
| [TOOL-dRedressedBar-22 — the closing review's profiler findings, batched: an interrupt names every kept capture, the probe spawns the base interpreter, and each faulted arm proves its work](spec/2026-10-15-spec-TOOL-dRedressedBar-22.md) | 16 | 2 | CLOSED | rev-2 | 2026-10-15 |
| [TOOL-dRedressedBar-23 — the closing review's govkit findings M3, M4, M6 and L4: a narrower apply keeps a carried kit's orders and order-file legs, target spawns decode stderr through one helper, a leg guard widens, and a routing arm grades each member](spec/2026-10-15-spec-TOOL-dRedressedBar-23.md) | 17 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-24 — the runner scripts' fixed-name temp writers take unpredictable temps, and a shell-hygiene mode reds a new one](spec/2026-10-15-spec-TOOL-dRedressedBar-24.md) | 18 | 2 | CLOSED | rev-2 | 2026-10-15 |
| [TOOL-dRedressedBar-25 — the round-2 review's profiler findings, batched: the A/B verdict gate grades the condition, the selftest's guard covers its kit dir, and AC9's orphan is waited on](spec/2026-10-15-spec-TOOL-dRedressedBar-25.md) | 19 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-26 — the round-2 temp-name findings, batched: every command-word `mv` is read, no positional or two-hop source reds, no bare `SRANDOM` is admitted, and the cache writer and leftover check hold on every runtime](spec/2026-10-15-spec-TOOL-dRedressedBar-26.md) | 20 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-27 — hygiene check 23 green by evidence: this build's eight missing acceptance ledgers written, and the base's 37 foreign ledger lines put in a legal form](spec/2026-10-15-spec-TOOL-dRedressedBar-27.md) | 21 | 1 | CLOSED | rev-2 | 2026-10-16 |
| [TOOL-dRedressedBar-28 — install-prefix's two hits at the landing: settings-merge's static absence terms give way to the resolver term, and unit 14's measured landing is spelled through `{prefix}`](spec/2026-10-16-spec-TOOL-dRedressedBar-28.md) | 22 | 2 | CLOSED | rev-2 | 2026-10-16 |
<!-- /gen:build-units -->

Records: 130 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26 TOOL-dRedressedBar-27 TOOL-dRedressedBar-28.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1`, `TOOL-dRedressedBar-2`, `TOOL-dRedressedBar-8`, `TOOL-dRedressedBar-9` | yes |
| 2 | `TOOL-dRedressedBar-3`, `TOOL-dRedressedBar-4` | yes |
| 3 | `TOOL-dRedressedBar-5` | no |
| 4 | `TOOL-dRedressedBar-20`, `TOOL-dRedressedBar-6` | yes |
| 5 | `TOOL-dRedressedBar-7` | no |
| 6 | `TOOL-dRedressedBar-10` | no |
| 7 | `TOOL-dRedressedBar-11` | no |
| 8 | `TOOL-dRedressedBar-12` | no |
| 9 | `TOOL-dRedressedBar-13`, `TOOL-dRedressedBar-16` | yes |
| 10 | `TOOL-dRedressedBar-14` | no |
| 11 | `TOOL-dRedressedBar-15` | no |
| 12 | `TOOL-dRedressedBar-17` | no |
| 13 | `TOOL-dRedressedBar-18` | no |
| 14 | `TOOL-dRedressedBar-19` | no |
| 15 | `TOOL-dRedressedBar-21` | no |
| 16 | `TOOL-dRedressedBar-22` | no |
| 17 | `TOOL-dRedressedBar-23` | no |
| 18 | `TOOL-dRedressedBar-24` | no |
| 19 | `TOOL-dRedressedBar-25` | no |
| 20 | `TOOL-dRedressedBar-26` | no |
| 21 | `TOOL-dRedressedBar-27` | no |
| 22 | `TOOL-dRedressedBar-28` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
