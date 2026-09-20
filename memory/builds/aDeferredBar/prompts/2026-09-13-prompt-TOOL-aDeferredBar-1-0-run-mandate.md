# Run mandate — aDeferredBar

**Serves:** journal TOOL-aDeferredBar-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-09-13. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts.

## The prompt

> The owner has noticed that unattended builds instruct their build workflows/agents to run
> gates/full gates within individual build units often stalling the units by several hours - that
> should not happen. Full gates should NOT run until the build is complete, if it's absolutely
> necessary gates should run SCOPED. Unattended self-tests and gates should NEVER run within build
> workflows/agents. Understand the problem, design and solution and build it per the protocol.

## How the three sentences were read

- **"Full gates should NOT run until the build is complete."** A `GATE_FULL=1` or `GATE_SELFTESTS=1`
  bar, `run-selftests.sh`, or `run-unattended-gates.sh` is not run by anyone — main loop or child —
  while the run's phase precedes `VERIFYING`. The close's own `gates-green` bar and the kit-work
  `GATE_SELFTESTS=1` bar both happen after every unit is terminal.
- **"If it's absolutely necessary gates should run SCOPED."** The plain `bash tools/run-gates/run-gates.sh`
  with no flag, on the run's branch, is the scoped form the manifest already defines: guarded legs
  run only where the branch touched their paths. It is permitted at the MAIN LOOP only, and is not
  the default — the default inside a pass is the direct check the spec's acceptance names.
- **"Unattended self-tests and gates should NEVER run within build workflows/agents."** No `*.test.sh`
  suite and no bar inside a stage or unit agent of `unattended-build.js` / `unattended-unit.js`. A
  new arm's failing case is observed by running the CHECKER on a staged break, never the suite.

## What the run was told about scope

Nothing beyond the prompt. No `--waive` was named. ACCEPTANCE and GATES were derived from the prose,
the workflow scripts, the run records and the gate ledger; no owner question was asked, and the
derivation is the research record under `build/`.
