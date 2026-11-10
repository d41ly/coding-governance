# Brief — aGuardedEffort: unit 1's observation prints one line of a refusal its criteria read three of

**Serves:** research TOOL-aGuardedEffort-1

## The brief

### Goal
DIVERGENCE: spec §4 "The observation" contradicts §4 "The texts" and §6 AC1 and AC3, so no code can satisfy all three. "The texts" puts the Agent remedy (`handoff.py role-efforts --model "<id>"`) on the refusal's second line, and for a Workflow refusal puts the per-workflow line and the `handoff.py stage-efforts <workflow> --model "<id>"` remedy on later lines. "The observation" prints only the first line of a refusal: its `say` helper splits on the newline and keeps element 0. AC1 requires the `a-none` and `a-high` observation lines to name `role-efforts --model`, and AC3 requires the `w-none` and `w-high` lines to name `builder`, `medium` and `stage-efforts build --model`; none of those tokens is on line 1.

### Items
1. §4 "The observation" prints the whole refusal on one line: the `say` helper trims the refusal and joins its lines with ` | `. "The texts" and the criteria stay as they are.
2. §4 "The parity probe" and "The observation" take their temporary directory from the caller: a directory argument or an environment variable the probe names, never `$TMPDIR` and never `os.tmpdir()`.
3. The transcript read stays the whole file, as spec §3 says. The build brief's Limitations sentence that the hook reads its tail is superseded by the spec, and §9 says so.
4. The spec takes a rev bump to rev-2 and a §9 line naming this record.

### Acceptance
1. Read against "The texts", every token AC1 and AC3 name appears in the line "The observation" prints for its case.
2. `python tools/check-spec-tokens.py` prints 0 unwaived hits.
3. No criterion's observed behaviour moved, and the status header changes only its rev.

### Gates
harness arms · roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · hook destinations · codebase-map coverage + freshness · docs · kit/dogfood doc parity · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the bar once at the close.

### Non-goals
The agents a running harness spawns through its own `agent()`, which no hook sees. The `committer` and `probe` stages, which take no level (ask `TOOL-aProfiledEffort-5`). Any change to a level, a profile, or the resolver's rules. A second matching rule: the hook's match is the resolver's, proved by parity. A refusal when the model cannot be read. Reading the model from anywhere but the call and the transcript.

### Limitations
The guard stops forgetting, not evasion, as rule 6's ceiling says: a hook-less run, a forged transcript and a hand-edited index pass it. A session reads hooks from its launch tree, so the guard arms in sessions started after it lands. The transcript is large; the hook reads its tail, never the whole file. An adopter with no profile tables in its policy gets an index whose effort section holds the defaults alone. Kit versions move through the lander's `mint`. The builder runs the two suites it adds arms to, once each, and no bar.

### Reuse
`tools/hooks/agent-cap.js` rule 6 (`checkHandoffSpawn`, `checkHarnessCall`, `extractWorkflowArgs`, `renderHandoffDeny`) is the seam, and the new check runs after it on the calls it admits. `tools/hooks/format-guard.js` already reads the payload's `transcript_path`. `tools/roles/render_agents.py` renders `.claude/roles.json` and `--check` grades it; `roles_lib.resolve_profile`, `resolve_effort` and `resolve_stage_efforts` are the one resolver the index is rendered through. The reuse probe returned `resolve_effort`, `resolve_stage_efforts` and `extractWorkflowArgs`. Records: `TOOL-aProfiledEffort-1` to `-4`, `TOOL-aOrientedCast-7`, `-14` and `-27` (rule 6).

