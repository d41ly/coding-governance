**Serves:** research TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46

# Probe brief — specs 43, 44, 45, 46 against the built branch, before their builders start

## The prompt

> Read-only probes of steps 12 and 13 let their units build on the first dispatch, where builders of earlier units each spent a dispatch discovering stale specs. This probe does the same for step 14.

## The brief

### Goal
For each of `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, `-44.md`, `-45.md`, `-46.md`, report every item that is stale against HEAD, read-only, writing nothing: every `path:N` citation, named constant, function, case, leg, quoted output line and premise in §1, §2 and §4 that no longer holds (with what HEAD has and where); every §2 item or criterion an earlier unit already built (naming the commit or symbol); every criterion whose observation depends on another unit's arm that reds at HEAD; every criterion command that cannot run as spelled from the repository root (bare file names, missing sources); every staged break that cannot red on what it names; and every guard line a spec adds to `tools/gate-legs.json` that another build's live spec touches without the leg (`python tools/check-spec-tokens.py --legs-for <path>` names a path's legs). For -44: TOOL-dGroundRules-40 rev-4 already respells the disjoint row as a string-prefix trap (`tools/policy` against `tools/policy-x.py`), so report any part of -44 that duplicates it. Units 32 to 41 restate or depend on one another by design; report only where a restatement itself is stale. TOOL-dGroundRules-37 is being built meanwhile; name any finding that depends on it. Return one section per spec, each finding with its spec location, what the spec says, what HEAD has and the HEAD location, or `no stale item`.

### Non-goals
Any write; any spec other than the four; product code.

### Acceptance
One section per spec as the goal says.

### Gates
No gate runs in this pass.

### Limitations
TOOL-dGroundRules-37 is uncommitted while this probe runs.

### Reuse
The probe of specs 39 to 41, `2026-10-24-prompt-TOOL-dGroundRules-39-1-spec-reviewer.md`.
