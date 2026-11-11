# Brief — aGuardedEffort: the close bar's one red this build owns, a forked `sed` in the roles adopter suite

**Serves:** research TOOL-aGuardedEffort-2

## The brief

### Goal
The merge bar at `5f7f52862` reds the leg `shell hygiene (a fork spent on builtin work)` with one finding: `tools/roles/adopt-roles.test.sh` holds one `var-pipe` site no registry row declares. The site is line 303, which this build added: `[ "$rc" = 0 ] || printf '%s
' "$out" | sed 's/^/    /'`. Convert it to the no-fork form, so the leg is green with no new registry row.

### Items
1. Line 303 of `tools/roles/adopt-roles.test.sh` prints `$out` indented four spaces a line with a parameter expansion and one `printf`, piping into nothing.
2. No other line of any file changes, and no registry row is added.

### Acceptance
1. `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt .`, the command the leg `shell hygiene (a fork spent on builtin work)` runs, reports no finding for `tools/roles/adopt-roles.test.sh`.
2. A probe of the converted line with a two-line `$out` and a nonzero `rc` prints both lines indented four spaces, and prints nothing when `rc` is 0.

### Gates
shell hygiene (a fork spent on builtin work) · roles adopter self-test; then the bar once at the close.

### Non-goals
The agents a running harness spawns through its own `agent()`, which no hook sees. The `committer` and `probe` stages, which take no level (ask `TOOL-aProfiledEffort-5`). Any change to a level, a profile, or the resolver's rules. A second matching rule: the hook's match is the resolver's, proved by parity. A refusal when the model cannot be read. Reading the model from anywhere but the call and the transcript.

### Limitations
The guard stops forgetting, not evasion, as rule 6's ceiling says: a hook-less run, a forged transcript and a hand-edited index pass it. A session reads hooks from its launch tree, so the guard arms in sessions started after it lands. The transcript is large; the hook reads its tail, never the whole file. An adopter with no profile tables in its policy gets an index whose effort section holds the defaults alone. Kit versions move through the lander's `mint`. The builder runs the two suites it adds arms to, once each, and no bar.

### Reuse
`tools/hooks/agent-cap.js` rule 6 (`checkHandoffSpawn`, `checkHarnessCall`, `extractWorkflowArgs`, `renderHandoffDeny`) is the seam, and the new check runs after it on the calls it admits. `tools/hooks/format-guard.js` already reads the payload's `transcript_path`. `tools/roles/render_agents.py` renders `.claude/roles.json` and `--check` grades it; `roles_lib.resolve_profile`, `resolve_effort` and `resolve_stage_efforts` are the one resolver the index is rendered through. The reuse probe returned `resolve_effort`, `resolve_stage_efforts` and `extractWorkflowArgs`. Records: `TOOL-aProfiledEffort-1` to `-4`, `TOOL-aOrientedCast-7`, `-14` and `-27` (rule 6).

