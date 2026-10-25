**Serves:** research TOOL-dGroundRules-68

# Spec brief — TOOL-dGroundRules-68, the writer-split arms read in a checkout

## The prompt

> The close ran `bash tools/hooks/agent-cap.test.sh` at HEAD and it failed 4 of 363: TOOL-dGroundRules-18's writer-split arms (`writer split: K 6 above a stub limit of 4`, `...and the K it read against that limit`, `writer split: K 6 at a stub limit of 6 -> allow (control)`, `verifier split: K 6 under a stub limit of 6`), each stderr `BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this Workflow call — the payload cwd … is in no git checkout, so the settings in force and the landed agent limit cannot be read, and a rule that cannot read does not admit.` The arms' payload carries no `cwd` and `run_limit_call` runs the hook from `$TMP`; the suite's own comment says "$TMP lies in no checkout, so rules 6 and 7 add nothing", which stopped holding when TOOL-dGroundRules-21 (f6674a6a2) made rule 7 refuse a cwd it cannot read. The same failures appear with the hook rolled back to before TOOL-dGroundRules-61 and to before -18, so the arms were never green in a whole-suite run.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-68.md`, a Tier-1 micro-spec at order 22, status `DEFERRED`, in the shape `2026-10-24-spec-TOOL-dGroundRules-67.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. S1: the TOOL-dGroundRules-18 writer-split block of `tools/hooks/agent-cap.test.sh` runs its hook copy inside a scratch git checkout (the way the rule-7 block builds `$R7`: `git init`, `main`, a committed tree) whose `.claude/settings.json` holds both agent-limit variables at a value rule 7 admits for each stub limit the block writes (read `checkSettingsInForce` to choose it), and its payloads carry that checkout as `cwd`; the stub `policy-mirror.js` beside the hook copy stays the only limit source. The stale comment about `$TMP` is respelled to what holds.
2. S2: the `no policy kit beside the hooks kit` arm keeps its expected answer; state what rule 7 does there with no policy kit, verified by reading the hook.
3. The fix is test-side only; `tools/hooks/agent-cap.js` does not change. Name the suite's assertion floor effect (none expected: no arm added).
4. AC1: `bash tools/hooks/agent-cap.test.sh` prints no `FAIL` line naming `writer split` or `verifier split` — but the suite is a bar leg, so the criterion observes it through the close's `agent-cap self-test` leg and the main loop's run; give the pass a probe it may run instead (the block's own commands copied into a scratch script, or the hook run directly on the block's payload in the scratch checkout). Red when: the arms run outside a checkout again. §7 names `agent-cap self-test` and the legs the touched file trips (`python tools/check-spec-tokens.py --legs-for tools/hooks/agent-cap.test.sh`), and declares no `New arm:` (the arms exist; this unit makes them run as written).
5. Keep every acceptance code span on one line; no acceptance line starts at column 0 with `AC<n>`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; product code; the hook itself.

### Limitations
Measured by the main loop at 4f76c4b39 in a scratch clone; the suite log is in the run's scratchpad as `sr-g_agentcap.log`.

### Reuse
The rule-7 block of the same suite, which builds `$R7` as a checkout and writes its settings.
