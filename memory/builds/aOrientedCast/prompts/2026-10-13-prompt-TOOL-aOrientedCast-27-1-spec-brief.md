**Serves:** journal TOOL-aOrientedCast-25 TOOL-aOrientedCast-27

# Brief record — the owner's fifth addendum, and TOOL-aOrientedCast-25's size trim

## The prompt

The owner, in this build's session on 2026-10-13, verbatim:

```text
another addition to the build - from this session's background tasks, I'm noticing that spawned agents do not carry correct names: 'Fold two specs, spec three units' are what gov-spec-builder has been called the entire session. Agent/workflow names should always reflect the units they're working on (slug, unit id, action).
```

## The brief

### Goal

Every agent a session spawns is named for what it is doing now: the build's slug, the unit id and
the action. A direct spawn's name is derived from its handoff and checked by the spawn guard; a
harness agent's label carries the same three parts. Separately, TOOL-aOrientedCast-25's spec comes
back under the spec-size ceiling so `--dispatch` admits passes again.

### Items

1. **Trim TOOL-aOrientedCast-25**, for the writer handed unit `TOOL-aOrientedCast-25`. Its spec
   measures 49183 bytes against the 49152 spec ceiling, and the spec-token checker's size join reds
   on it, so `--dispatch` refuses every pass in the build. Its generated records region grows by a
   row whenever a new record names the unit. Cut at least 600 bytes of authored text: history,
   restated evidence, or prose that points rather than restates. Do not touch the
   `<!-- gen:spec-records -->` region, the scope, or any acceptance criterion's meaning. Bump the
   rev with its §9 line.
2. **Spec TOOL-aOrientedCast-27**, for the writer handed unit `TOOL-aOrientedCast-27`: order 28,
   streams tooling, Tier-2, full ten sections, at
   `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-27.md`.
   - **Direct spawns.** `handoff.py render` prints the name an `Agent` call's `description` must
     carry, built from the marker's build, unit and role: for example
     `aOrientedCast · TOOL-aOrientedCast-27 · spec-write`, with the action taken from the role's
     workflow. The spawn guard's rule 6 in `tools/hooks/agent-cap.js` refuses an `Agent` call whose
     `description` is not that name.
   - **Harness agents.** `tools/workflows/unattended-build.js`, `unattended-unit.js` and
     `tier2-review.js` give every `agent()` call a `label` carrying the slug, the unit id where the
     stage serves one unit (else the stage's scope, such as a review round), and the stage.
     A `Workflow` run's own title is its script's static `meta.name`, which the tool does not let a
     call set: say so in §3 rather than promise it.
   - **The agent lines.** TOOL-aOrientedCast-20's `<unit-id|label>` field then reads a unit id for
     every harness agent that serves one.
   - Read the specs of TOOL-aOrientedCast-7 (the spawn guard), -20 (the agents verb) and -24, which is
     open and edits `tools/hooks/` and `tools/unattended/`. Keep this unit's write set disjoint from
     -24's and -25's, or say which must build first.

### Acceptance

The trim leaves `python tools/check-spec-tokens.py` with no size hit on TOOL-aOrientedCast-25.
TOOL-aOrientedCast-27's spec carries the full ten sections, a §6 whose every criterion is a direct
check a builder may run, and a `New arm:` line per new refusal, naming its staged break.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.
Each spec's §7 names the legs its change touches.

### Non-goals

- Renaming agents that already ran, or rewriting the agent ledger's past lines.
- Changing a `Workflow` run's title, which the tool takes from the script.
- Re-opening the owner's earlier rulings in this build.
