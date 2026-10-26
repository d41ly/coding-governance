**Serves:** research TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38

# Probe brief — specs 36, 37 and 38 against the built branch, before their builders start

## The prompt

> Every builder since TOOL-dGroundRules-20 has opened by probing its spec against HEAD, and most handed back a divergence: the specs were written before units 1 to 35 landed, so cited lines moved, constants and premises changed, and earlier units already built parts of later findings. Each such round trip costs a builder dispatch. This probe finds those items for the next three units before their builders start, so a writer can fix them first.

## The brief

### Goal
For each of `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md`, `-37.md` and `-38.md`, report every item that is stale against HEAD, read-only, writing nothing: every `path:N` citation, named constant, function, case, leg, quoted output line and premise in §1, §2 and §4 that no longer holds (with what HEAD has and where); every §2 item or criterion an earlier unit already built (naming the commit or symbol); every criterion whose observation depends on another unit's arm that reds at HEAD; and every guard line a spec adds to `tools/gate-legs.json` that another build's live spec touches without the leg (`python tools/check-spec-tokens.py --legs-for <path>` names a path's legs). Skip TOOL-dGroundRules-34's six stripped criteria (AC11, AC12, AC15, AC16, AC32, AC36), which later units restate by design. Name any finding that depends on TOOL-dGroundRules-34, which is being built meanwhile. Return one section per spec, each finding with its spec location, what the spec says, what HEAD has and the HEAD location, or `no stale item`.

### Items
1. For each spec, check every `path:N` citation, every named constant, function, case and leg, every quoted output line, and every premise in §1, §2 and §4 against HEAD; report each that no longer holds, with what HEAD has instead and its location.
2. Report each §2 item or criterion an earlier unit already built, naming the commit or symbol that shows it.
3. Report each criterion whose observation depends on another unit's arm that reds at HEAD.
4. Report each `[guards]` exposure: a guard line a spec adds to `tools/gate-legs.json` that another build's live spec touches without the leg (`python tools/check-spec-tokens.py --legs-for <path>` names a path's legs).
5. Do not report the six stripped criteria of TOOL-dGroundRules-34 (AC11, AC12, AC15, AC16, AC32, AC36), which later units restate by design.

### Acceptance
One section per spec, each finding with its spec location, what the spec says, what HEAD has, and the HEAD location; or `no stale item` for a spec with none.

### Gates
No gate runs in this pass.

### Non-goals
Any write; any spec other than the three; product code.

### Limitations
TOOL-dGroundRules-34 is being built while this probe runs; a finding that depends on 34's change is named as such.

### Reuse
The builders' probe returns recorded in this build's close-owed notes show the common classes: moved line citations, constants renamed, findings already built, criteria depending on another unit's red arm.
