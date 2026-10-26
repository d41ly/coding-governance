**Serves:** research TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41

# Probe brief — specs 39, 40 and 41 against the built branch, before their builders start

## The prompt

> Builders since TOOL-dGroundRules-20 open by probing their spec against HEAD, and most handed back a divergence: the specs predate units 1 to 36, so cited lines moved, premises changed and earlier units built parts of later findings. The read-only probe of specs 36 to 38 let unit 36 build on its first dispatch. This probe does the same for step 13's units 39, 40 and 41. TOOL-dGroundRules-40 also inherits, from TOOL-dGroundRules-34 rev-9, AC17's observation and the arm comment in `tools/check-spec-tokens.test.sh`, because the pair `tools/policy/a.py` against `tools/policy/ab.py` cannot red a raw `startswith` compare.

## The brief

### Goal
For each of `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-39.md`, `-40.md` and `-41.md`, report every item that is stale against HEAD, read-only, writing nothing: every `path:N` citation, named constant, function, case, leg, quoted output line and premise in §1, §2 and §4 that no longer holds (with what HEAD has and where); every §2 item or criterion an earlier unit already built (naming the commit or symbol); every criterion whose observation depends on another unit's arm that reds at HEAD; every guard line a spec adds to `tools/gate-legs.json` that another build's live spec touches without the leg (`python tools/check-spec-tokens.py --legs-for <path>` names a path's legs); and, for -40, whether its AC3 `RAW_BOTH` staging can red on the pairs it names, proposing a string-prefix pair a raw `startswith` confuses that containment does not (for example `tools/policy` against `tools/policy-x.py`) and every place in -40 that pair must change. These units restate TOOL-dGroundRules-34's stripped AC11, AC12, AC15, AC16, AC32 and AC36 by design; report only where the restatement itself is stale. TOOL-dGroundRules-34 is being built meanwhile (its patch reads `build_install_target` with `intake` and a `[gate_runner]` strip); name any finding that depends on it. Return one section per spec, each finding with its spec location, what the spec says, what HEAD has and the HEAD location, or `no stale item`.

### Non-goals
Any write; any spec other than the three; product code.

### Acceptance
One section per spec as the goal says.

### Gates
No gate runs in this pass.

### Limitations
TOOL-dGroundRules-34 is uncommitted while this probe runs.

### Reuse
The probe of specs 36 to 38, `2026-10-24-prompt-TOOL-dGroundRules-36-1-spec-reviewer.md`.
