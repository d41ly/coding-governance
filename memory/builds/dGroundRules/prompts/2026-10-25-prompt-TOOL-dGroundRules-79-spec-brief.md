**Serves:** research TOOL-dGroundRules-79

# Spec brief — TOOL-dGroundRules-79, govkit selfcheck green over this build's policy kit

## The prompt

At the close the main loop ran `python tools/govkit/govkit.py selfcheck` at `fce5603f8`: it exits 1, and the govkit selftest (`tools/govkit/selftest.py`) fails 70 arms because each starts from a selfcheck that should be green over this repository. The selfcheck's red lines:

> govkit: guard pathspec 'AGENTS.md' (leg 'policy fixtures') falls into 0 declared classes [], not exactly one — a taxonomy that does not partition its own input gives the emitter no rule for the remainder
> govkit: guard pathspec 'help/policy.md' (leg 'policy fixtures') falls into 0 declared classes [], not exactly one — a taxonomy that does not partition its own input gives the emitter no rule for the remainder
> govkit: 'tools/policy/README.md' (kit 'policy', which declares [[regenerate]]) says `update` re-renders without naming GOVKIT_RERENDER in the same sentence, and with GOVKIT_RERENDER=0 exported `update` declines the regenerate: `kit.toml`'s `[[regenerate]]` runs the same verb on every update (TOOL-dGroundRules-21 S37).
> govkit: 'tools/policy/adopt-policy.sh' (kit 'policy', which declares [[regenerate]]) says `update` re-renders without naming GOVKIT_RERENDER in the same sentence, and with GOVKIT_RERENDER=0 exported `update` declines the regenerate: `[[regenerate]]` in kit.toml runs this same verb on every update (TOOL-dGroundRules-21 S37).
> govkit: 'tools/policy/check_policy.py' (kit 'policy', which declares [[regenerate]]) says `update` re-renders without naming GOVKIT_RERENDER in the same sentence, and with GOVKIT_RERENDER=0 exported `update` declines the regenerate: A failed git step is a WRONG naming the step.""" rows = policy.load_catalogue(KIT) repo, kit, bare = build_landed_repo(rows) try: helper = ["node", str(kit / "policy-mirror.js"), "get", AGENTS_KEY, "-
> govkit: 'tools/policy/kit.toml' (kit 'policy', which declares [[regenerate]]) says `update` re-renders without naming GOVKIT_RERENDER in the same sentence, and with GOVKIT_RERENDER=0 exported `update` declines the regenerate: `--scaffold` IS the re-render: on every update it re-runs the settings render over a kept policy file, so a changed renderer reaches every adopter (TOOL-dGroundRules-21 S37). [[regenerate]] argv = ["b

`AGENTS.md` joined the `policy fixtures` guard in TOOL-dGroundRules-67 (`4f76c4b39`); the policy kit and its prose are this build's. Memory note: govkit's selfcheck grades kit prose, so a sentence saying `update` re-renders must name `GOVKIT_RERENDER` in that same sentence.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-79.md`, a Tier-1 micro-spec at order 27, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that makes `govkit selfcheck` exit 0 over this repository. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-verify each red line at HEAD (run `python tools/govkit/govkit.py selfcheck` yourself; it reads, it writes nothing) and read the code that emits it: where the guard-pathspec class taxonomy is declared and how a class is matched, and the GOVKIT_RERENDER prose rule.
2. S1: give `AGENTS.md` and `help/policy.md` exactly one declared class each, by the taxonomy's own rule (extend the declaration, or show the guard line belongs elsewhere), naming every reader of that declaration.
3. S2: respell each sentence in the four policy-kit files the selfcheck names so it names `GOVKIT_RERENDER`, keeping each sentence's meaning; touch no other prose. TOOL-dGroundRules-78 (builds just before this unit) edits `tools/policy/README.md` and `help/policy.md` too: cite by heading or symbol, not line.
4. Each acceptance criterion is a probe the pass may run, never a whole suite or the bar: the selfcheck itself is a read-only command the pass may run, so AC1 is its exit code and the absence of each red line, with `Red when:` naming a staged break (a respelled sentence reverted, the class removed). The govkit selftest is a self-test the close runs.
5. §6 names the legs the touched files owe through `derive_guarded_legs`, plus any unguarded leg that reads them (govkit selfcheck among them if it is a leg).
6. §7 "Open questions" reads exactly `none`, with no bullet under it: a bullet outside an F-item there refuses the CLOSED flip at hygiene check 12. Any follow-up goes in the §8 revision log as prose. Keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; the `reported, not repaired` version-constant lines the selfcheck prints (they do not fail it); the govkit kit's own code unless the taxonomy declaration lives there.

### Limitations
Measured by the main loop at `fce5603f8`; the selfcheck output is in the run's scratchpad as `selfcheck-fce.txt`, the selftest log as `sr-g_govkit.log`.

### Reuse
The taxonomy declaration the selfcheck reads, and the sentences already naming GOVKIT_RERENDER in other kits.
