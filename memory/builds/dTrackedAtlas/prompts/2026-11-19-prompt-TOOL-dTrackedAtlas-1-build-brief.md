**Serves:** research TOOL-dTrackedAtlas-1

# Build brief — TOOL-dTrackedAtlas-1: the chain build-state derivation and the schedule's read of it

Build `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-1.md` (rev-2, READY) as written: the
derivation file in this build's `build/` folder, the schedule script's edit, and the acceptance ledger its Files
touched names. The spec is the design; diverge only by returning `diverged: true` with the section and the reason.

- The bug-class checklist over the spec commit `20ca97bea` selected, among others,
  `fixture-passes-by-finding-nothing`, `staged-break-substitutes-a-synthetic-value`,
  `criterion-asserts-what-its-own-command-cannot-show` and `two-answers-to-one-question`: each AC's red case is
  observed on the real shape it names (the pre-change schedule, the scratch clone's planted landing), never a
  synthetic stand-in, and recorded in the ledger beside its green.
- Run no gate, suite or bar: verify with the spec's AC commands only. Fixture clones go under `%TEMP%/<short>`
  and are removed after; the real repository's refs are never written, and the claim cache is never written
  outside a scratch clone.
- No path under `tools/`; no new file under `memory/builds/dClosedLoop/build/` (the schedule is edited in place).
- Commit once, with a `Pass: TOOL-dTrackedAtlas-1` trailer and `Co-Authored-By: Claude Opus 5.5
  <noreply@anthropic.com>`; flip the spec's status to CLOSED in that commit. The pre-commit hook takes minutes:
  bound the commit at `600 s`. Never `--no-verify`, never `git add -A`.
