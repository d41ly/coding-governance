# Brief — aGuardedEffort: the closing review's two highs, five mediums and two lows, batched

**Serves:** research TOOL-aGuardedEffort-2

## The brief

### Goal
Each of the nine items the closing diff review confirmed at round 1 is closed by the fix its report carries. The review record is `memory/builds/aGuardedEffort/reviews/2026-11-10-review-TOOL-aGuardedEffort-1-diff-review-round1.md`, items 1 to 9; each item's fix is the one under that item, the skeptic's where the report says it corrected the finder's.

### Items
1. Item 1 (ids 1, 5): rule 8 takes an unset `Workflow` stage's level from the role the call's own `args.roles` names for that stage, and a stage key the call omits counts as differing for that workflow; it stops reading the policy's slot for a call whose roles differ from it.
2. Item 2 (ids 9, 17): the rule 8 fixture's unset levels differ from its default stage levels, so an arm fails when the default stage table is read in place of the level a stage runs at.
3. Item 3 (ids 4, 6): a harness workflow with no stages entry in the index is not graded as empty and admitted silently: the renderer and the hook agree on one population, and the gap is refused as a broken index or noted on stderr, whichever the report's fix says.
4. Item 4 (id 8): an arm runs the any-of rule over a harness two workflows share.
5. Item 5 (id 10): a transcript fixture whose first and last main-chain assistant models differ, with a sidechain and a non-assistant entry after the last, pins the model read.
6. Item 6 (id 11): the `Workflow` half of rule 8 is run over a rendered index in the roles adopter suite.
7. Item 7 (ids 12, 18): an arm reds when rule 8 is moved after rule 7 or before rule 6, and AC9's red-when clause names a break its payload can show.
8. Item 8 (ids 7, 19): the six running-text sites that say the hook runs rules 6 and 7 name rule 8.
9. Item 9 (id 15): an arm covers the four-key shape test of the index's effort value.

### Acceptance
1. A unit-harness call on a model no profile matches, with `roles` naming a role whose rendered level is not the default stage level and no `efforts`, is refused; the same call with the level its role runs at is graded on that level.
2. A review-harness call whose `roles` omit a stage key is not admitted through that workflow's unset level.
3. Each new arm is declared on a `New arm:` line with the staged break that reds it, and the main loop sees each red then green at the close.
4. A search of the tree for the phrase the six sites carry finds none outside records.

### Gates
harness arms · roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · hook destinations · codebase-map coverage + freshness · docs · kit/dogfood doc parity · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the bar once at the close.

### Non-goals
The agents a running harness spawns through its own `agent()`, which no hook sees. The `committer` and `probe` stages, which take no level (ask `TOOL-aProfiledEffort-5`). Any change to a level, a profile, or the resolver's rules. A second matching rule: the hook's match is the resolver's, proved by parity. A refusal when the model cannot be read. Reading the model from anywhere but the call and the transcript.

### Limitations
The guard stops forgetting, not evasion, as rule 6's ceiling says: a hook-less run, a forged transcript and a hand-edited index pass it. A session reads hooks from its launch tree, so the guard arms in sessions started after it lands. The transcript is large; the hook reads its tail, never the whole file. An adopter with no profile tables in its policy gets an index whose effort section holds the defaults alone. Kit versions move through the lander's `mint`. The builder runs the two suites it adds arms to, once each, and no bar.

### Reuse
`tools/hooks/agent-cap.js` rule 6 (`checkHandoffSpawn`, `checkHarnessCall`, `extractWorkflowArgs`, `renderHandoffDeny`) is the seam, and the new check runs after it on the calls it admits. `tools/hooks/format-guard.js` already reads the payload's `transcript_path`. `tools/roles/render_agents.py` renders `.claude/roles.json` and `--check` grades it; `roles_lib.resolve_profile`, `resolve_effort` and `resolve_stage_efforts` are the one resolver the index is rendered through. The reuse probe returned `resolve_effort`, `resolve_stage_efforts` and `extractWorkflowArgs`. Records: `TOOL-aProfiledEffort-1` to `-4`, `TOOL-aOrientedCast-7`, `-14` and `-27` (rule 6).

