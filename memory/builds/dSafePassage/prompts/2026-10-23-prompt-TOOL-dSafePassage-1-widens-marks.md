**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-7

# Brief — dSafePassage: two §8 marks the departures report cannot join

## The prompt

> deviations: report dSafePassage · spec run · entries 306 · findings 2
>   entry 1's widens: [the minimal guard's admitted agent-write] joins no record
>   entry 2's widens: [none ·] joins no record

— `deviations.py --report dSafePassage` on the prepared merge, README rule 4's close sequence

## The brief

### Goal

Make both §8 marks read as the run decided, so the departures report joins every choice and exits 0.

### Items

1. `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md` §8 F8 (around line 496) carries
   `widens: the minimal guard's admitted agent-write shapes, …`. That widening was deviation-12's, which commit
   33f58e248 withdrew and filed as the ask `TOOL-dGroundRules-13` in dGroundRules' BACKLOG.md, because the guard
   is dGroundRules' (`cl-dClosedLoop-0012`) and README rule 7 lets this run reach it only through an ask. This
   build widens nothing itself. Rewrite the mark's fields as `widens: none · relaxes: none` on one line, and add a
   sentence after it saying the guard's second write shape is `TOOL-dGroundRules-13`'s to grant, and that the build
   run re-grounds against the guard dGroundRules lands. Bump the spec's rev by one with a §9 line naming this.
2. `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-7.md` §8 F3 (around line 326): the mark's
   hard wrap falls inside `widens: none · relaxes: none`, so the report reads the widens value as `none ·`.
   Re-wrap that paragraph so `widens: none · relaxes: none` sits whole on one line. The text does not change.
   This is a wrap only, so no rev bump.

### Acceptance

`python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dSafePassage`
prints no `widens` finding for either spec. It is read-only, so you may run it.

### Gates

None beyond that read. A role agent runs no gate.

### Non-goals

No other change, and nothing staged or committed. Write nothing outside the two specs.

### Limitations

This is an unattended run, so nobody will answer a question. The worktree's HEAD is a prepared landing merge: do not
commit, reset, merge or check out anything.

### Reuse

The §8 mark shape in `memory/TEMPLATE-SPEC.md`.
