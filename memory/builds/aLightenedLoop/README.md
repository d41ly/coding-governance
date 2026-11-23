---
slug: aLightenedLoop
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
ids: TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 TOOL-aLightenedLoop-6 TOOL-aLightenedLoop-7 TOOL-aLightenedLoop-8
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
| 6 | `TOOL-aLightenedLoop-6` | the closing review round 1 repaired: check 39 admits the wake reader, the spec-token key derived inside its stability bracket, check 29 reads chain specs once, and the arms that could not fail made able to |
| 7 | `TOOL-aLightenedLoop-7` | the tracked idle-wake cadence retired at the owner's call, its conf key removed everywhere, `--wake` naming the base cadence, and the idle-wake help page's block marked not to run |
| 8 | `TOOL-aLightenedLoop-8` | the reconcile with origin/main: the merge, and unit 3's input-keyed spec-token cache ported onto the split start and read halves of the check |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 8 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 TOOL-aLightenedLoop-6 TOOL-aLightenedLoop-7 TOOL-aLightenedLoop-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLightenedLoop-1 — the commit tail: `--write` writes only changed bytes, a render stamp answers the hook, check 9's staged skip admits a records edit, and check 29 exits early](spec/2026-11-14-spec-TOOL-aLightenedLoop-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-2 — the idle-wake tick: one cheap `--wake` verb that ends a healthy turn, and a longer cadence while a registered task is open](spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-11-14 |
| [TOOL-aLightenedLoop-3 — `--dispatch` runs before the builder spawns, and its spec-token cache keys on what the checker read](spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-4 — a builder checks its spec can be built before its first edit, a spec cites where it read the code, and a watched path brings its manifest re-stamp](spec/2026-11-14-spec-TOOL-aLightenedLoop-4.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-14 |
| [TOOL-aLightenedLoop-5 — the stop-guard caches the `--liveness` verdict, keyed on every input the verdict reads and expired by the liveness clock](spec/2026-11-14-spec-TOOL-aLightenedLoop-5.md) | 5 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-6 — the closing review round 1 repaired: check 39 admits the wake reader, the spec-token key derived inside its stability bracket, check 29 reads chain specs once, and the arms that could not fail made able to](spec/2026-11-14-spec-TOOL-aLightenedLoop-6.md) | 6 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aLightenedLoop-7 — the tracked idle-wake cadence retired: its conf key removed everywhere, `--wake` naming the base cadence, and the idle-wake help page's block marked not to run](spec/2026-11-15-spec-TOOL-aLightenedLoop-7.md) | 7 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aLightenedLoop-8 — the reconcile with origin/main: the merge, and unit 3's input-keyed spec-token cache carried onto the check's start and read halves](spec/2026-11-15-spec-TOOL-aLightenedLoop-8.md) | 8 | 2 | CLOSED | rev-1 | 2026-11-15 |
<!-- /gen:build-units -->

Records: 33 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 TOOL-aLightenedLoop-6 TOOL-aLightenedLoop-7 TOOL-aLightenedLoop-8.

Ids whose spec moved past its audited revision: none — 0 of 8 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLightenedLoop-1` | no |
| 2 | `TOOL-aLightenedLoop-2` | no |
| 3 | `TOOL-aLightenedLoop-3` | no |
| 4 | `TOOL-aLightenedLoop-4` | no |
| 5 | `TOOL-aLightenedLoop-5` | no |
| 6 | `TOOL-aLightenedLoop-6` | no |
| 7 | `TOOL-aLightenedLoop-7` | no |
| 8 | `TOOL-aLightenedLoop-8` | no |

A step's `Parallel` yes means its units share an order; BUILD-METHOD M6 still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-15-prompt-TOOL-aLightenedLoop-8-reconcile.md`, `2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md` and 15 more under prompts/ |
| reviews | `2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md` (CLEAN WITH FIXES) |
| override | `2026-11-14-build-TOOL-aLightenedLoop-1-override-1.md` |
| red-fix | `2026-11-14-build-TOOL-aLightenedLoop-5-red-fix-4.md`, `2026-11-14-build-TOOL-aLightenedLoop-2-red-fix-3.md` and 2 more under build/ |
| research | `2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md` |
| logs | `2026-11-15-build-TOOL-aLightenedLoop-8-1-acceptance-ledger.md`, `2026-11-15-build-TOOL-aLightenedLoop-7-1-acceptance-ledger.md` and 7 more under build/ |
| card ref | `refs/gov/builds/aLightenedLoop/card` |
<!-- /gen:build-routes -->
