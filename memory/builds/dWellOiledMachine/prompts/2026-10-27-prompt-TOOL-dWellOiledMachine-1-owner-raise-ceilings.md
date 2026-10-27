**Serves:** research TOOL-dWellOiledMachine-1

# Owner ruling — raise the two leg ceilings in a unit of this build, then close and land

## The prompt

> Raise the spec tokens and routed commits ceilings with evidence rows in a separate unit, then re-run dWellOiledMachine's close and land it.

— owner, 2026-10-27, answering the decision the run parked at its hand-off (`memory/builds/dWellOiledMachine/RUN.md`,
HELD owner-decision at `0075cd1c4`).

## What the run was doing

- The close's bar at `10ab21489` was red on 2 of 72 legs, both timed out twice, in the pool and on the serial retry,
  and attributed CONTENDED: `spec tokens (a spec's own names resolve)` at its 390 s ceiling and
  `routed commits name a specced unit` at its 300 s ceiling.
- Each leg alone, the two run side by side on node a at `ec8ad0363`, exited 0: spec tokens in 512 s with its packet
  join over 1 live chain run, routed commits in 358 s.

## How the run applies it

- "A separate unit" is read as one new unit of this build, as `TOOL-dGroundRules-87` was for dGroundRules: the run
  adds it with `--rescope --act add`, specs it, builds it and commits it before the close. It is the one unit this
  spec run builds; every other unit stays DEFERRED to the build run (README rule 1).
- The unit raises the two ceilings in `tools/gate-legs.json` from fresh readings of each leg alone, each written to
  `tools/run-gates/ceiling-evidence.txt` through `derive-ceilings.py --write --observed`, the route that unit used.
- The unit is not run through the spec-audit chain: the owner's ruling of 2026-10-27
  (`memory/builds/dWellOiledMachine/prompts/2026-10-27-prompt-TOOL-dWellOiledMachine-1-owner-stop-chain.md`) made
  round 8 the last round, so it closes under the same `specs-audited` override as `-122` to `-126`.
- Then the run re-runs `--close`, lands with `push-main.sh --land` and is marked landed.
