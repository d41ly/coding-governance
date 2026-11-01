# Brief — dShippedRelease: spec-token repairs on round 5's promotions

**Serves:** research DEPL-dShippedRelease-144

## The prompt

> Repair the spec-token hits round 5's promotions left, in units 140 and 144.

## The brief

### Goal

`python tools/check-spec-tokens.py` reports no hit naming a spec of this build. That check is the main loop's: do not run it.

### Items

1. In `memory/builds/dShippedRelease/spec/2026-11-01-spec-DEPL-dShippedRelease-140.md`, an acceptance criterion backticks the path-shaped `tools/integrations/ci/ci_emit.py`, which is not tracked at this base. Spell it by basename, or reword, as unit 120's criteria and unit 128's AC1 do, keeping the criterion runnable as written: state where the command runs if the basename alone would not say.
2. In `memory/builds/dShippedRelease/spec/2026-11-01-spec-DEPL-dShippedRelease-144.md`, acceptance criteria backtick `C:/x/memory/a.md`, `C:/x2/memory/a.md`, `/c/x/memory/a.md`, `tools/integrations/release.py` and `help/deploy.md`, none tracked. Reword so no backticked token in a criterion is path-shaped, keeping every observable: literal inputs in plain unbackticked text, as unit 133's AC3 does, and an untracked file by basename with its folder in prose, as unit 138's AC34 does.

### Acceptance

Your return names, per spec, what you changed. No new requirement enters either spec. Nothing but these two specs changes.

### Gates

`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` over the staged specs, and no other gate. Run it after your last edit, and report its exit code.

### Non-goals

No commit, no index regeneration, no rev bump: both units are at rev-1 and unaudited. Stage your edits. Temp files go under the session scratchpad spelled absolute.
