# Brief — dShippedRelease: unit 9's header verb

**Serves:** research DEPL-dShippedRelease-9

## The prompt

> Change unit 9's header verb from closes to advances, as the owner's stop ruling leaves it.

## The brief

### Goal

No spec of this build carries `closes DEPL-dShippedRelease-32`, because the audit rounds put units after unit 9 in build order and the build run's last unit carries `closes`.

### Items

1. In `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-9.md`, the **Status:** line's last verb reads `closes DEPL-dShippedRelease-32`. Change it to `advances DEPL-dShippedRelease-32`. Do the same for any place in that spec that states unit 9 is the unit closing the ask, keeping the sentence true: the ask stays open until the last unit in build order.
2. Read the owner's ruling at `memory/builds/dShippedRelease/prompts/2026-11-01-prompt-DEPL-dShippedRelease-1-owner-stop-chain.md` for why.

### Acceptance

`grep -l "closes DEPL-dShippedRelease-32" memory/builds/dShippedRelease/spec/*` prints nothing. Your return names every line changed.

### Gates

`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` over the staged spec, after your last edit, and no other gate. Report its exit code.

### Non-goals

No commit, no index regeneration. A rev bump only if the spec format requires one for this edit, with its §9 line. Nothing but this spec changes. Stage your edit. Temp files go under the session scratchpad spelled absolute.
