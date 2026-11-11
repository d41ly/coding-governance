# Fix brief — TOOL-dFairHearing-23, re-grounded on what units 1 to 22 built

**Serves:** research TOOL-dFairHearing-23

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md` so a correct build of it passes on today's tree. Twenty units of this build have landed since it was written, several of them taking or changing work this spec schedules. Each builder return under `memory/builds/dFairHearing/build/*-builder-return.md` names what it left to unit 23; read the ones for units 6, 8, 13, 15, 16, 17 and 18 first. Commit nothing; the main loop commits.

### Items
1. **Work an earlier unit already landed.** Unit 18 (`b21501741`) landed the `WHOLE_DESIGN_LENSES` literal, its receiver branch and the suite's `no-such-preset` arm, which S15 schedules. Unit 16 (rev-7 S9) took the kickoff-manifest re-stamp of S28. Unit 1 pass (b) (`2d992a209`) added `twinFlags: []` to `unattended-build.test.sh`'s synthesis double. Unit 8 (`4a0e73da6`) already put `TOOL_ROOT` in kit.toml's row (S38). For each: drop it from Scope, or keep a criterion that observes it already done, and say which, citing the commit.
2. **What units 6, 8 and 17 handed here, confirmed covered.** The synthesis double `build_merged_returns` in `tools/workflows/unattended-build.test.sh` returns no `grades` (unit 6's tally reads them unguarded) and no `dispositions` (unit 8's schema requires them), so the unattended-build self-test reads the synthesis as dead; make sure a scope item and a criterion fix that. Unit 6's §4 Migration says a missing `grades` falls back to the item's severity while S30/AC21 make it a refusal: say which holds, and correct the other spec's sentence as a repair (rev bump and §9 line on unit 6's spec). Unit 17's AC6 CEILING token (S19/AC11): check the criterion can pass.
3. **What units 13, 16 and 18 handed here.** Unit 13: `check-verifier-fanout.test.sh`'s `mkfix` arms AC2 and AC3 red on the whole-tree lens-slot rule (S23/AC14). Unit 16: three fan-out fixtures that copy the gate without its new `.js` (S27), and the new `spec-audit opt-in pack self-test` leg's registry, budget and foreign-prefix rows (S26). Unit 18: its AC7 tag-shape half (S1/AC1) and AC10 render-diff half (S9/AC4). Re-ground each against the tree as it now stands.
4. **Criteria that are already green.** AC18's grep half already prints 5. Every criterion whose red case today's tree no longer produces is rewritten so it can go red against the unit's own parent commit, or dropped with a §9 line saying why.
5. **Cites and guards.** Re-ground every `path:line` cite against HEAD, and every §7 leg line against the guards its §4 files trip in `tools/gate-legs.json`.
6. Rev bump and one §9 line per change, naming this brief; unit 6's spec gets its own if item 2 corrects it. Leave each status header's state as it is.

### Acceptance
Unit 23's spec at its next rev: no scope item for work already landed without a criterion saying so; every criterion able to go red at the unit's parent; units 6, 8, 13, 16, 17 and 18's hand-offs each named in a scope item. The main loop runs the spec-token checker before committing.

### Gates
None you run.

### Non-goals
No design change beyond what the items name, no code, no write outside units 23's and 6's specs.
