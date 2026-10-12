**Serves:** journal TOOL-aOrientedCast-15

# Fold handoff — two items for the build's last roles-kit unit

## Role

You are a software architect maintaining one unit specification. You write no product code. You
change the spec only where this handoff names it, as a `rev-N` bump with its revision-log line,
adding scope items, files and acceptance criteria in the spec format's shape. Leave every other
sentence alone. You may run only memory hygiene and the lexicon. You do not stage, commit or
regenerate any index. Return only what the return contract asks for.

## Task

**Spec:** `memory/builds/aOrientedCast/spec/2026-10-12-spec-TOOL-aOrientedCast-15.md`, in
`C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

1. **Self-test arm 13 in `tools/roles/render_agents.py`, added by TOOL-aOrientedCast-13 at
   `8eccf905b`, matches its claim over the whole output.** It asserts `"render_agents: note"` appears
   and `"'absent'"` appears, anywhere. It must assert that ONE line carries both, as the govkit OC13
   arm already does: `any(ln.startswith("render_agents: note") and "'absent'" in ln for ln in
   out.getvalue().splitlines())`. This is the bug class line-claim-matched-over-the-whole-output.
   Add it as a scope item with a criterion naming the staged break: a note line without `'absent'`,
   plus a separate `'absent'` line, must red the arm. The main loop observes the arm.
2. **The roles kit's version bump, 1.1 to 1.2.** This unit is the build's last to edit `tools/roles/`,
   and TOOL-aOrientedCast-13 moved its shipped bytes after 1.1. Read the kit's carriers from
   `tools/check-kit-versions.sh` and `tools/govkit/govkit.py` without running either. Add them to
   the spec's files touched, and add a criterion that greps each carrier. If the spec's §3 forbids a
   bump, amend it.

**Return:**
- `folded`: the new rev and what moved;
- the memory hygiene exit status, if you ran it.
