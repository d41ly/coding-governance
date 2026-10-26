**Serves:** research TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60

# Probe brief — specs 53, 54, 56, 57, 58, 59, 60 against the built branch, before their builders start

## The prompt

> Read-only probes of steps 12 to 14 let their units build on the first dispatch, where builders of earlier units each spent a dispatch discovering stale specs. This probe does the same for the remaining steps.

## The brief

### Goal
For each of `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-53.md`, `-54.md`, `-56.md`, `-57.md`, `-58.md`, `-59.md`, `-60.md`, report every item that is stale against HEAD, read-only, writing nothing: every `path:N` citation, named constant, function, case, leg, quoted output line and premise in §1, §2 and §4 that no longer holds (with what HEAD has and where); every §2 item or criterion an earlier unit already built (naming the commit or symbol); every criterion whose observation depends on another unit's arm that reds at HEAD; every criterion command that cannot run as spelled from the repository root (bare file names, missing sources); every staged break that cannot red on what it names; and every guard line a spec adds to `tools/gate-legs.json` that another build's live spec touches without the leg (`python tools/check-spec-tokens.py --legs-for <path>` names a path's legs). These seven observe the overlap table and its trap row through probes; TOOL-dGroundRules-40 (942581c64) built the table as `OVERLAP_PAIRS` with `PFX`-relative rows, and specs -44 and -45 restate the row check. Report each criterion that is already observed by a built unit or by spec -44 or -45 as revised, naming which, so the run can retire a redundant unit; and report stale references to spec -44's constants. Units 1 to 41 are built or building and the specs restate one another by design; report only where a restatement itself is stale. Return one section per spec, each finding with its spec location, what the spec says, what HEAD has and the HEAD location, or `no stale item`.

### Non-goals
Any write; any spec other than those named; product code.

### Acceptance
One section per spec as the goal says.

### Gates
No gate runs in this pass.

### Limitations
TOOL-dGroundRules-41 is being built while this probe runs; name any finding that depends on it.

### Reuse
The step-14 probe, `2026-10-24-prompt-TOOL-dGroundRules-43-1-spec-reviewer.md`.
