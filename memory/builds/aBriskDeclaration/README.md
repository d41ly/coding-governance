---
slug: aBriskDeclaration
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
ids: TOOL-aBriskDeclaration-1
authorized-by: prompt
---

# aBriskDeclaration — a dispatch declaration without a process per unit, and its checker run beside the pass reader

## The problem this build exists to solve

Every unit of an unattended run first declares its write set with `unattended.sh --dispatch`, and on
node `a` one declaration in a 99-unit run takes six to ten minutes. The order gate starts a pipeline
of processes for every unit of the build to read one header line. The spec-token checker then runs
only after the open-pass reader, though neither reads the other. The measurements and the analysis
are in `build/`, and the prompt is in `prompts/`.

## Expected improvements

- The order gate reads every unit's order verb with no process.
- The checker and the open-pass reader overlap, so a declaration costs the longer of the two.
- Every refusal, note and parked row reads as it did.

## Detriments if this is not built

- A dispatch keeps costing minutes per unit, and a builder's bound can expire before it records.
- The order gate's cost grows with each unit a build adds.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: a changed behaviour of the driver's
  `--dispatch` verb.
- `memory/builds/dDeclaredLoop/`, its run's worktree and its branch are a live run's, and are not
  touched. `pass_commit`, `read_attribution_tokens` and `check_pass_open` are left alone, because
  that run's branch rewrote them.
- No unattended self-test suite while that run is live, beyond the driver suite's dispatch arms.
- No landing without the owner's explicit ask.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBriskDeclaration-1` | the order verb read in the shell with no process, and the spec-token checker started before the open-pass reader and read where it ran |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aBriskDeclaration-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBriskDeclaration-1 — `--dispatch` reads the order verb with no process, and starts the spec-token checker before the open-pass reader](spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-11-14 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aBriskDeclaration-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBriskDeclaration-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
