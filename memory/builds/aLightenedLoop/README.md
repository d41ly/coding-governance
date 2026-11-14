---
slug: aLightenedLoop
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
ids: TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5
---

# aLightenedLoop — a build unit's fixed overhead cut, every verdict and byte unchanged

## The problem this build exists to solve

In dSafePassage, a median builder ran 17.6 min, of which 9.6 came before its first product edit and
5.1 after its last. That is about 31 h of overhead across 101 builders. The overhead is the commit
tail, which renders the build index twice per commit; idle-wake ticks firing over tracked work;
`--dispatch` grading the whole tree inside a spawned builder; builders diverging late on spec
claims; and the stop-guard spawning `--liveness` on every Stop. The brief and the owner's fork
answers are in `prompts/`.

## Expected improvements

- A records-only commit's hook no longer renders the build index twice.
- An idle-wake tick over healthy tracked work costs seconds, not minutes.
- A dispatch refusal costs seconds, without a spawned builder.
- Builders diverge early, or not at all.
- Every verdict, refusal and rendered byte is unchanged.

## Detriments if this is not built

- Every unit of a long run keeps paying 15 or more minutes of fixed overhead.
- A 100-unit run spends more than a day of builder time producing nothing.

## Build-level rules

- **Classification (M2)**: five units, MISSING at open, Tier-2, one per fix, as the owner cut it.
- Parity is the acceptance: each touched check gives the same exit code, refusal text and rendered bytes before and after on the real tree, plus a measured timing.
- `memory/builds/dDeclaredLoop/` and its run's branch are a live run's, and are not touched.
- Kit versions move only through the lander's mint.
- No landing or push without the owner's explicit ask.
- No spec audit: not declared (owner, 2026-11-14).

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aLightenedLoop-1` | the commit tail: the index generator writes only changed bytes and caches its render by input hash, check 9's staged skip admits a records edit that moves nothing it renders, and check 29 exits early when no staged spec is an INPROGRESS chain spec |
| 2 | `TOOL-aLightenedLoop-2` | the idle-wake tick: one cheap tick verb that ends a healthy turn, and a longer cadence while a tracked task is registered |
| 3 | `TOOL-aLightenedLoop-3` | `--dispatch`: run before the builder spawns, and its spec-token cache keyed on input hashes; scoping to the unit's build was declined at its fork, since it moves cross-build joins |
| 4 | `TOOL-aLightenedLoop-4` | divergence: a feasibility-first builder brief, spec writers citing their code claims, and the template's re-stamp rule |
| 5 | `TOOL-aLightenedLoop-5` | the stop-guard caches the liveness verdict, keyed on every input the verdict reads, expired by the liveness clock, with an environment kill switch |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 5 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLightenedLoop-1 — the commit tail: `--write` writes only changed bytes, a render stamp answers the hook, check 9's staged skip admits a records edit, and check 29 exits early](spec/2026-11-14-spec-TOOL-aLightenedLoop-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-2 — the idle-wake tick: one cheap `--wake` verb that ends a healthy turn, and a longer cadence while a registered task is open](spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md) | 2 | 2 | INPROGRESS | rev-1 | 2026-11-14 |
| [TOOL-aLightenedLoop-3 — `--dispatch` runs before the builder spawns, and its spec-token cache keys on what the checker read](spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md) | 3 | 2 | SPECCED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-4 — a builder checks its spec can be built before its first edit, a spec cites where it read the code, and a watched path brings its manifest re-stamp](spec/2026-11-14-spec-TOOL-aLightenedLoop-4.md) | 4 | 2 | SPECCED | rev-1 | 2026-11-14 |
| [TOOL-aLightenedLoop-5 — the stop-guard caches the `--liveness` verdict, keyed on every input the verdict reads and expired by the liveness clock](spec/2026-11-14-spec-TOOL-aLightenedLoop-5.md) | 5 | 2 | SPECCED | rev-2 | 2026-11-14 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5.

Ids whose spec moved past its audited revision: none — 0 of 5 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLightenedLoop-1` | no |
| 2 | `TOOL-aLightenedLoop-2` | no |
| 3 | `TOOL-aLightenedLoop-3` | no |
| 4 | `TOOL-aLightenedLoop-4` | no |
| 5 | `TOOL-aLightenedLoop-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
