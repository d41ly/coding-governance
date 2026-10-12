**Serves:** journal TOOL-aOrientedCast-6 TOOL-aOrientedCast-8

# Fold handoff — two defects the build passes found, routed into the units that own their files

## Role

You are a software architect maintaining a set of unit specifications. You write no product code.
You change each spec only where a finding below names it, as a `rev-N` bump with its `§9` line
saying what changed and why. You leave every other sentence alone. A new scope item gets its own
`S<n>`, at least one acceptance criterion naming a DIRECT observation and its command, its files in
`§4 ### Files touched (estimate)`, and its legs on the `§7` line. You return only what the return
contract asks for.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.
Both specs are under `memory/builds/aOrientedCast/spec/`, and neither unit is built yet.

**1. TOOL-aOrientedCast-8 gains the roles kit's install-prefix clean-up.**
`bash tools/check-install-prefix.sh --offenders` names nine keys, all in files earlier units of this
build created:

| File | Keys |
|---|---|
| `tools/roles/check_roles.py` | `"tools", "model"` |
| `tools/roles/render_agents.py` | `"tools", "model"` · `"roles"` · `"workflows"` · `"workflows"#2` · `workflows/a.js` · `workflows/missing.js` · `workflows/missing.js#2` |
| `tools/roles/roles_lib.py` | `"tools", "model"` |

The leg is a BAN with no ratchet (`tools/hooks/README.md`, "The authoring rule for kit files"), so
it is red at the close until they are gone. Read the checker's patterns before deciding how each
spelling changes. Most are front-matter key names or self-test fixture names, not paths into a
sibling kit, so the fix is a spelling the ban does not read as a path. It is never a waiver
added for a new key. Say which spelling replaces each, and make the observation
`check-install-prefix.sh --offenders` printing none of these keys, with each file's own behaviour
re-observed: `check_roles.py`'s and `render_agents.py --selftest`'s existing direct checks.
TOOL-aOrientedCast-8 already edits the roles kit to register and wire it, which is why it owns this.

**2. TOOL-aOrientedCast-6 gains one fixture in the scratch guard's suite.**
`tools/hooks/scratch-guard.test.sh` near line 701 (arm AC10) sends a READY body whose `## task` is a
single line through the real kickoff checker's `--card --append`. Since KICK-aOrientedCast-1, that
checker refuses a READY body missing any of the eight task fields, so the arm reds at the close. The
fix gives that body all eight task fields filled, and moves the `README.md:1` row under `## read`.
The helper `render_task_section` in `skills/session-kickoff/manifest-check.test.sh` prints a filled
task section; reuse its shape rather than writing a second one. The observation is that arm alone,
run through a slice (the memory note "Slice a suite to debug one arm"), RED at this spec's base and
GREEN after. TOOL-aOrientedCast-6 already edits the scratch guard and that suite, which is why it
owns this.

**Rules.**
- No product code.
- No commit: the main loop commits after you return.
- Do not run the build-index generator.
- No merge bar, and no `*.test.sh` suite.
- Temporary files go under
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-deterministic-attended-workflows-943570/e131d82c-aaf3-45ad-abb9-258d7ab9ad1b/scratchpad`.
- Run `python tools/check-spec-tokens.py` once at the end, and fix any hit in a spec you touched.

**Return:**
- `folded`: one line per spec, with its new rev and the finding it answers;
- `refused`: any finding you could not apply, with why;
- the `check-spec-tokens.py` exit status.
