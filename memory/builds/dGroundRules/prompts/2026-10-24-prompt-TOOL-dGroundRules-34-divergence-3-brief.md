**Serves:** research TOOL-dGroundRules-34

# Divergence brief 3 — TOOL-dGroundRules-34, AC17's staged break cannot red on S15's pairs

## The prompt

> Its builder built TOOL-dGroundRules-34 rev-8 at c9f389589 (saved as a patch that applies cleanly), observed AC38 and every other buildable criterion green, and handed it back as a DIVERGENCE on AC17 (with S17 and §7's `New arm: tools/check-spec-tokens.test.sh · covers AC17`): staged to compare raw strings with `startswith` in either direction, `check_writes_intersect` still prints `False` for S15's second pair, since neither `tools/policy/ab.py` nor `tools/policy/a.py` is a string prefix of the other, so the arm unit 32 built on S15's pairs cannot tell a raw prefix compare from containment and its RED-first observation would stay green. TOOL-dGroundRules-40, the promoted repair of review id 17, rests on the same premise in its AC3.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md` to the run's ruling: S17's claim that the arm tells a raw prefix compare from containment, AC17 and the `New arm:` line covering AC17 move to TOOL-dGroundRules-40, which owns the repair of id 17 and will spell a pair a raw `startswith` confuses. Author only: no product code, no commit, no gate.

### Items
1. S17 keeps what it builds and drops the "so it tells" claim; AC17 is restated as observed by TOOL-dGroundRules-40 (name that unit and its criterion), with no command of its own; §7's `New arm:` line covering AC17 goes.
2. §3 gains a hands-off edge to TOOL-dGroundRules-40 naming the AC17 observation and the arm's pair, and §5 or §4 says the arm comment in `tools/check-spec-tokens.test.sh` that claims a raw prefix compare calls the pair overlapping is TOOL-dGroundRules-40's to correct.
3. Leave AC11, AC12, AC15, AC16, AC32 and AC36 untouched.
4. The status header's rev rises by one, with a §9 line naming the disagreement and the ruling. The file must end at or under 48600 bytes measured with `wc -c` including its records region: this revision removes more than it adds, and if it still exceeds 48600, shorten older §9 lines. Every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48600; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec, including TOOL-dGroundRules-40, which the main loop revises before that unit; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's per-criterion results at c9f389589 stand; its patch `TOOL-dGroundRules-34-dispatch3.patch` is the build.

### Reuse
TOOL-dGroundRules-40's spec is the target of the hands-off edge.
